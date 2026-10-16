# Module 0.1 Assignment: Git and GitHub

## Goal
Use the real daily workflow on your own `webdev` repo: branch, commit, push, pull request, merge, sync, clean up. Then create a merge conflict on purpose and resolve it.

Work on your own. If you get stuck, ask for a hint (one at a time, each one is logged).

## Check your progress
Run this any time from the `webdev` folder. It only reads your repo and GitHub, it never changes anything:

```
python3 00.1-git/assignment/checks/check_git.py
```

Most checks fail at the start. They turn green as you go.

## Part 1: About me (branch + pull request)
- [ ] Start from an up-to-date `main`.
- [ ] Create a branch named exactly `about-me`.
- [ ] Add an `## About me` section to `README.md`: who you are and what you want to build.
- [ ] Make **at least 2 commits** on the branch, each with a descriptive message.
- [ ] Push the branch to GitHub.
- [ ] Open a pull request into `main` **with a description** (what you changed and why).
- [ ] Read the PR's "Files changed" tab, then merge the PR on GitHub.
- [ ] Delete the branch on GitHub.
- [ ] Update your local `main` and delete your local `about-me` branch.

## Part 2: Merge conflict on purpose
- [ ] Create two branches from the same `main` (you choose the names).
- [ ] On each branch, change **the same line** of `README.md` in a different way, and commit.
- [ ] Merge the first branch into `main`.
- [ ] Merge the second branch into `main`, get a conflict, and resolve it (no conflict markers left).
- [ ] Finish the merge with a commit, push `main`, and delete both branches.

## Done when
- [ ] `git status` is clean, and your local `main` matches GitHub.
- [ ] Every automated check passes.
- [ ] You type **submit**.

## Stretch goal (optional)
Do the conflict the way teams do it: push both conflict branches and open a PR for each. Merge the first PR on GitHub. GitHub will then say the second PR has conflicts. Resolve them locally on the second branch (bring `main` into it), push, and merge the second PR on GitHub.
