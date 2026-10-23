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

## Module 0.1: Git and GitHub

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

### Assignment: about-me PR + merge conflict ✅ PASS
- Checks: 13/13 (`python3 00.1-git/assignment/checks/check_git.py`).
- Part 1: PR #1 "Add build goal to README.md" merged on GitHub (2 commits), branch deleted on GitHub and locally, local main pulled.
- Part 2: branches `machine-learning` and `deep-learning` added different lines at the end of the README. First merged as fast-forward, second conflicted, resolved by keeping both lines (merge commit `59565ff`), pushed, both branches deleted.
- Verification: PR title named a nonexistent file (`ABOUT_ME.md`) and the description described the goal, not the change. Both fixed on GitHub, then PASS. Answered 3 questions: who made each merge commit and where (GitHub vs my computer), why `git branch -f` lost nothing (branches are labels), fast-forward vs conflict.
- Hints used: 2. (1) Move a commit made on main by mistake: `git switch -c about-me` + `git branch -f main origin/main`. (2) `git commit --amend` to fix the last commit's message and content.
- Nudges (not counted): what to write in About me, use `git pull` instead of a local merge, fix the PR description.
- Struggled with: committed on main despite warnings, `git add.` (3 times), spaces in branch names, `git branch <name>` instead of `git switch -c <name>`, `git push main`, `git merge about_me` instead of `git pull`, vague commit messages and PR description, needed guidance to read merge commit authors.

## Module 0.1: Git and GitHub ✅ COMPLETE

## Module 1: HTML (branch `module-1-html`, merged in PR #2)

### Lesson 1: Page structure ✅
- Learned: tags, elements, attributes; page skeleton (`<!DOCTYPE html>`, `html lang`, `head`, `meta charset`, `meta viewport`, `title`, `body`); `<title>` (tab) vs `<h1>` (page); browser default styles; indentation is only for humans; browsers silently fix mistakes (a `<p>` in `<head>` still shows), so HTML bugs don't raise errors; Emmet `!` + Tab generates the skeleton.
- Hands-on: `01-html/lessons/lesson1.html` typed by hand, opened with `open`.
- Struggled with: copied `❯` into a command, missing `!`. Style nit: space before `=` in an attribute.
- Hints used: 0.

### Lesson 2: Headings, text, links, images ✅
- Learned: `h1`–`h6` as hierarchy (one `h1`, don't skip levels, size comes from CSS), `p`, `strong`, `em`, `br`, `<a href>` absolute vs relative paths (relative to the HTML file's own folder), `<img src alt>`, empty elements (`img`, `meta`, `br`), `alt` as fallback + for screen readers.
- Hands-on: `01-html/lessons/lesson2.html` with GitHub link, relative link to lesson1, image `webdev.jpeg`. Broke `src` on purpose and saw alt text + broken icon.
- Struggled with: used a `.textClipping` instead of a real image, wrong relative paths (extra `lessons/`, leading `/`), words running together around `<strong>`/`<em>`, left Emmet's default `<title>Document</title>`, space before `=`, space before `!`.
- Hints used: 0 (bugs found in code review).

### Lesson 3: Lists, divs, semantic tags ✅
- Learned: `ul`/`ol`/`li` (`ol` when order matters), block vs inline (`p` stacks, `a` flows), `div` = box with no meaning, semantic `header`/`main`/`section`/`footer` add meaning not style (header → div swap changed nothing), HTML comments `<!-- -->`, Format Document (Shift+Option+F), indentation reveals missing closing tags.
- Hands-on: `01-html/lessons/lesson3.html` (skills page with two sections, ul + ol, div, footer).
- Struggled with: first experiment swapped `<h1>` instead of `<header>` (heading shrank), forgot `<header>` and then to swap it back, lost a `</section>` (caught by formatting), footer text not in `<p>`, typo, skipped Q3 until prompted.
- Hints used: 1 (count opening vs closing `<section>` tags).

### Lesson 4: Forms and inputs ✅
- Learned: `<form>`, input types (`text`, `email`, `number`), `placeholder`, `required`, `min`, `<select>`/`<option>` (`value` vs visible text, blank first option + `required`), `<button type="submit">`, `<label for>` ↔ `id` (click focuses input, screen readers announce it), `id` (unique, linking) vs `name` (key for submitted data), ids can't contain spaces, submit sends `name=value` pairs in the URL (query string) but with no server nothing is saved.
- Hands-on: `01-html/lessons/lesson4.html` (study group form). Tested required, email validation, `min`, URL query string.
- Struggled with: id/name with spaces (`year of study`), forgot `min="1"`, options didn't match the label (calendar years), space before `=` (3rd time), stray `no` typed into the page, thought label clicks did nothing (cursor focus was easy to miss).
- Hints used: 0.

### Guided project: personal profile page ✅
- `01-html/guided-project/index.html`: header (h1, tagline, photo via `../lessons/myimg.jpg`), main with About / Skills (ul) / Goals (ol) / Find me (absolute + `../` relative links) / Contact (form: name, email, textarea, all labeled), footer.
- Learned: `../` = parent folder, `index.html` as a site's default page, `<textarea>` (has a closing tag), list of links pattern, `strong`/`em` for words not whole paragraphs.
- Struggled with: wrapped whole paragraphs in strong/em, stray comma (`,id`) silently broke a label (found by clicking the label), forgot the textarea label, "Lesson $" typo, formatting.
- Hints used: 0.

### Assignment: expense tracker static page ✅ PASS
- First submit. Checks 19/19 (`python3 01-html/assignment/checks/check_html.py`).
- Page `01-html/assignment/index.html`: header/h1, form in main (text name, number amount, select with 3 categories + required placeholder, "Add Expense" button, all labeled), list of 3 expenses (name — ₹amount — category), Total ₹270 (correct).
- Discussed: dropdown categories (Groceries/Food/Clothes) didn't match expense categories (Travel/Education), so categories must be one fixed list (matters for the Module 3 filter, Module 4 types, Module 6 validation). `min="0"` allows ₹0; use `min="1"` or `min="0.01"` + `step="0.01"`. Add only reloads without JavaScript.
- Struggled with: vague first answers on the category mismatch and `min`, `git sta` / `git com` (cut-off commands), unclosed `"` in a commit message.
- Hints used: 0.

### Git checkpoint ✅
- PR #2 "Module 1 html" merged on GitHub (merge commit `729e544`), branch deleted on GitHub and locally, local main pulled and equal to GitHub, working tree clean, no forbidden files committed.
- Git question: GitHub created the merge commit; local main fast-forwarded because it had no new commits of its own.
- Struggled with: said "I think I pushed everything" without checking (`PROGRESS.md` was uncommitted).

## Module 1: HTML ✅ COMPLETE

## Module 2: CSS (in progress, branch `module-2-css`)

### Lesson 1: What CSS is, connecting a stylesheet ✅
- Learned: rule syntax (selector { property: value; }), element selectors, inline vs `<style>` vs external `<link rel="stylesheet">` (external is best; inline is banned in the assignment), colors (named, hex, rgb), `font-family` with generic fallback (`sans-serif`), `font-size` in px, the cascade (later rule wins), invalid CSS is silently ignored, DevTools Inspect → Styles shows invalid properties crossed out with ⚠️.
- Hands-on: `02-css/lessons/lesson1.html` + `lesson1.css`.
- Struggled with: first answer to "nothing changes" gave only one check (save); left `coor` unfixed and the CSS unformatted after the experiment.
- Hints used: 1 (the `<link>` href as the second thing to check).

### Lesson 2: Classes and selectors ✅
- Learned: `class` attribute + `.class` selector, multiple classes (space-separated), kebab-case names (`expense-card`), id selector exists but avoid for styling, descendant selector (`.card p`, space = "inside"), grouping (`h1, h2`), `:hover` pseudo-class, specificity element < class < id < inline ("later wins" only between equally specific rules).
- Hands-on: `02-css/lessons/lesson2.html` + `lesson2.css`. Predicted correctly that `.note` beats a later `p` rule.
- Struggled with: unclosed `<link>` tag (missing `>`), `.btn :hover` with a space (hover never fired), unnecessary `<br>` between paragraphs, formatting.
- Hints used: 1 (compare `.btn :hover` with `.card p`).

## Next
- Lesson 3 (Module 2): box model.
- Module 2 assignment starts from a copy of the Module 1 tracker. Consider first aligning dropdown and expense categories and fixing `min`.
- Habits to keep: create the branch before editing, read `On branch …` in `git status` before every commit, descriptive commit messages (verb + what changed).
