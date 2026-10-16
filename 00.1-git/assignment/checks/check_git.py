"""Automated checks for the Module 0.1 assignment (Git and GitHub).

Run from the webdev folder:  python3 00.1-git/assignment/checks/check_git.py
Read-only: it inspects your repo and GitHub, and never changes anything.
"""

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "about-me"
REQUIRED_IGNORES = ["node_modules/", ".venv/", "__pycache__/", ".env", "*.db", ".answers.md"]
FORBIDDEN_DIRS = {"node_modules", ".venv", "__pycache__"}
FORBIDDEN_FILES = {".env", ".answers.md", ".DS_Store"}

results = []


def run(*args):
    """Run a command in the repo and return (exit code, stdout)."""
    proc = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip()


def check(name, ok, hint=""):
    results.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok and hint:
        print(f"       -> {hint}")


def check_local_state():
    _, branch = run("git", "branch", "--show-current")
    check("You are on main", branch == "main",
          f"you are on '{branch}'. Finish on main.")

    _, status = run("git", "status", "--porcelain")
    check("Working tree is clean", status == "",
          "git status shows uncommitted or untracked changes.")

    code, remote = run("git", "ls-remote", "origin", "refs/heads/main")
    _, local = run("git", "rev-parse", "main")
    remote_sha = remote.split()[0] if remote else ""
    check("Local main matches main on GitHub", code == 0 and remote_sha == local,
          "your main and GitHub's main have different commits. Are you ahead or behind?")


def check_ignores():
    gitignore = ROOT / ".gitignore"
    lines = [line.strip() for line in gitignore.read_text().splitlines()] if gitignore.exists() else []
    missing = [p for p in REQUIRED_IGNORES if p not in lines]
    check(".gitignore has all required patterns", not missing,
          f"missing: {', '.join(missing)}")

    _, tracked = run("git", "ls-files")
    bad = []
    for path in tracked.splitlines():
        parts = path.split("/")
        name = parts[-1]
        if FORBIDDEN_DIRS & set(parts[:-1]) or name in FORBIDDEN_FILES or name.endswith(".db"):
            bad.append(path)
    check("No forbidden files are committed", not bad,
          f"these should never be in the repo: {', '.join(bad)}")


def check_readme():
    readme = ROOT / "README.md"
    text = readme.read_text() if readme.exists() else ""

    match = re.search(r"^#+\s*about me\s*$(.*?)(?=^#|\Z)", text, re.I | re.M | re.S)
    check("README has an 'About me' heading with text under it",
          match and match.group(1).strip(),
          "look for a Markdown heading named 'About me' followed by some text.")

    markers = re.search(r"^(<{7}|>{7})( |$)", text, re.M)
    check("README has no leftover conflict markers", not markers,
          "a <<<<<<< or >>>>>>> line is still in README.md.")


def check_pull_request():
    code, out = run("gh", "pr", "list", "--state", "merged", "--head", BRANCH,
                    "--json", "number,body,baseRefName")
    if code != 0:
        check(f"A merged PR from '{BRANCH}' into main exists", False,
              "could not ask GitHub. Does `gh auth status` say you're logged in?")
        return False

    prs = [pr for pr in json.loads(out or "[]") if pr["baseRefName"] == "main"]
    check(f"A merged PR from '{BRANCH}' into main exists", prs,
          f"no merged PR from a branch named '{BRANCH}' yet.")
    if not prs:
        check("The PR has a description", False, "needs the merged PR first.")
        check("The PR has at least 2 commits", False, "needs the merged PR first.")
        return False

    pr = prs[0]
    check("The PR has a description", pr["body"].strip(),
          "the PR description is empty. You can still edit it on GitHub.")

    code, out = run("gh", "pr", "view", str(pr["number"]), "--json", "commits")
    commits = json.loads(out)["commits"] if code == 0 else []
    check("The PR has at least 2 commits", len(commits) >= 2,
          f"the PR has {len(commits)} commit(s).")
    return True


def check_branch_cleanup(pr_merged):
    code, _ = run("git", "rev-parse", "--verify", "--quiet", f"refs/heads/{BRANCH}")
    check(f"Local '{BRANCH}' branch deleted", pr_merged and code != 0,
          "needs the merged PR first." if not pr_merged else f"git branch still lists '{BRANCH}'.")

    code, out = run("git", "ls-remote", "--heads", "origin", BRANCH)
    check(f"'{BRANCH}' branch deleted on GitHub", pr_merged and code == 0 and out == "",
          "needs the merged PR first." if not pr_merged else "the branch still exists on GitHub.")


def check_conflict_merge():
    """Look for a merge commit on main whose two parents conflict in README.md."""
    _, merges = run("git", "rev-list", "--merges", "main")
    found = False
    for sha in merges.splitlines():
        _, line = run("git", "rev-list", "--parents", "-n", "1", sha)
        parents = line.split()[1:]
        if len(parents) != 2:
            continue
        code, out = run("git", "merge-tree", "--write-tree", "--name-only", "--no-messages", *parents)
        if code == 1 and "README.md" in out.splitlines()[1:]:
            found = True
            break
    check("main contains a resolved merge conflict in README.md", found,
          "no merge on main where both sides changed the same README line.")


def main():
    print("Module 0.1 assignment checks\n")
    check_local_state()
    check_ignores()
    check_readme()
    pr_merged = check_pull_request()
    check_branch_cleanup(pr_merged)
    check_conflict_merge()
    print(f"\n{sum(results)}/{len(results)} checks passed.")


if __name__ == "__main__":
    main()
