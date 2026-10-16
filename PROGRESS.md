# Progress

## Module 0: Setup (restarted with interactive lessons, now complete)

Setup done: Python 3.14.7, curl, git OK. Node v26.11.1 + npm 11.20.0 installed. gh missing (needed in Module 0.1).

### Lesson 1: What is Node.js? ✅
- Learned: Node runs JS files in the terminal like `python3`. npm is like pip, `node_modules/` is like `.venv`. Visitors don't need Node because browsers have their own JS engine. `console.log(2 + 3)` calculates first and prints 5.
- Struggled with: first answer described where JS runs instead of what Node is. Needed to be reminded to report prediction and folder name.
- Hints used: 1 (Node runs on your computer, not in the browser).
- Hands-on: added `console.log(2 + 3)` to hello.js, predicted 5, got 5.

### Lesson 2: How the web works ✅
- Learned: client vs server (restaurant analogy), request/response, response = status code + headers + body, 404 = not found, frontend (React) vs backend (FastAPI), JSON is the data format of API bodies, browser renders HTML while React turns JSON into list items.
- Struggled with: data format of API responses (said "api"; JSON explained to me).
- Hints used: 2 (data format hint, then nudge to finish the question).

### Lesson 3: Reading an HTTP response with curl ✅
- Learned: curl as a mini-browser, `-i` shows headers (status line + Content-Type), blank line separates headers from body, text/html vs application/json, read a 404 JSON response correctly.
- Struggled with: nothing.
- Hints used: 0.

### Assignment: hello.py + hello.js + curl answers ✅ PASS
- Submit attempt 1: NOT YET (Content-Type had typos; body pasted as raw HTML instead of described).
- Submit attempt 2: NOT YET (Content-Type fixed; body was copied page text, not a description of its kind).
- Submit attempt 3: PASS. Both files print the same message, status 200, `text/html; charset=utf-8`, body described in own words as an HTML page. Answered 3 questions about own work correctly (console.log(2+3) calculates first, 200 = OK / 404 = not found, Content-Type tells what kind of body).
- Hints used: 0.
- Struggled with: copying raw output instead of answering in own words, small typing slips.

## Module 0: Setup ✅ COMPLETE (no git checkpoint; work becomes first commit in Module 0.1)

## Module 0.1: Git and GitHub (in progress)

### Lesson 1: What is Git? ✅
- Learned: git records project history as commits (save points with messages), repo = tracked folder with history in `.git/`, branch = safe separate line of work, Git (tool) vs GitHub (website to store/share/back up repos).
- Struggled with: answers were brief, needed a follow-up on GitHub's role. Wording slip: you go back to the earlier saved version, not the "present" one.
- Hints used: 0.

### Lesson 2: Setting up Git and GitHub ✅
- Learned: `git config --global` sets name/email (commits record the author), installed `gh` 2.102.0, `gh auth login` via browser + one-time code, token stored in keyring, `gh auth status` to verify. GitHub account: sohailxsyed31-svg.
- Struggled with: typed commands without the `!` prefix twice, so they went to chat instead of running.
- Hints used: 0.

### Lesson 3: Daily git commands ✅
- Learned: `init`, `status`, `add`, `commit -m`, `log --oneline`; staging area (suitcase); file states untracked → staged → committed, and modified → staged → committed; good commit messages. Practice repo `~/git-practice` has 2 commits.
- Struggled with: `!` shell resets `cd` each command (need `cd ~/git-practice &&` every time). Accidentally ran `git init` in `webdev` (harmless, empty repo, will be used in the guided project). First commit message was a placeholder.
- Hints used: 0.

### Lesson 4: diff, restore, .gitignore ✅
- Learned: `git diff` output (`+` added, `-` removed), `git restore` permanently discards uncommitted edits (git has no copy), `.gitignore` patterns like `*.env`, `.gitignore` itself should be committed, a pushed secret stays in history and must be rotated.
- Struggled with: why a committed secret stays exposed, and that `.gitignore` should be committed (each needed one retry). Gave no prediction before `restore`.
- Hints used: 1 (nudge about teammates cloning the repo).

### Lesson 5: Branches ✅
- Learned: `branch`, `switch -c`, `switch`, `merge`. Branches isolate work, `main` is unaffected until merged, merge goes into the branch you're on, fast-forward vs a real merge commit, merged branches aren't deleted automatically.
- Struggled with: forgetting the `!` prefix many times, `git -status`, `git cat`, `~git-practice` (missing slash), a copied `❯` in a command. Often skipped predictions and "why" answers until prompted.
- Hints used: 2 (merge direction; whether main had new commits).

### Lesson 6: GitHub (remote, push, pull, PRs) ✅
- Learned: remotes and `origin`, `gh repo create --source=. --push`, `push -u`, `pull` = download + merge, `origin/main` is a saved snapshot of GitHub's main (only updated when talking to GitHub), opening a PR and reading its diff, merging on GitHub creates a merge commit, deleting branches on GitHub and locally (`git branch -d`), pull main before branching.
- Practice repo: github.com/sohailxsyed31-svg/git-practice (private). PR #1 merged.
- Setup fix: `gh auth setup-git` so plain `git push` uses the gh login.
- Struggled with: typos (`--source=,`, branch name with spaces, space before `!`), "Closed" vs "Merged" label, why local main falls behind after a GitHub merge (explained), why to pull before branching (one retry).
- Hints used: 2 (where the merge happened; what a new branch would be missing).

### Lesson 7: Merge conflicts ✅
- Learned: conflicts happen when branches change the same place differently (different places merge automatically), conflict markers, HEAD = current branch, resolve by edit → `git add` → `git commit`, `git merge --abort` as escape hatch, fast-forward vs merge commit, resolving to "A only" still needs a commit (or use --abort), ahead → push / behind → pull.
- Struggled with: skipped the HEAD question until prompted, first fix wasn't saved (markers still in file), why a commit is needed after resolving (good question, discussed), auto-merge condition needed a retry (first retry copied my sentence).
- Hints used: 2 (which branch HEAD is on; why lines 1–4 merged automatically).

### Guided project: the `webdev` repo ✅
- Wrote `.gitignore` (node_modules/, .venv/, __pycache__/, .env, *.db, .answers.md, .DS_Store) and `README.md` (Markdown heading + list).
- First commit `d90442b` "Add course setup and Module 0 files" (7 files). Created private repo github.com/sohailxsyed31-svg/webdev with `gh repo create --private --source=. --push`.
- Struggled with: copied bullet dashes into `.gitignore`, Markdown needs a space after `#` and `-`, `git add.` (no space), `cat` without a filename, unsure where files were saved (verified with a listing).
- Hints used: 1 (build the commit message from the staged file groups).

## Next
- Module 0.1 assignment (on my own):
  1. Branch `about-me`: add an "About me" section to the README, at least 2 commits, push, open a PR with a description, merge on GitHub, update local main, delete the branch.
  2. Create a merge conflict on purpose: two branches change the same README line, merge one, merge the other, resolve the conflict.
- Then verification ("submit").
- Note: `claude.md` has been renamed to `CLAUDE.md` (done). `webdev/` already has an empty git repo (accidental `git init`).
