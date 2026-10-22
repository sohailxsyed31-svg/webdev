# Module 1 Assignment: Expense Tracker (static page)

## Goal
Build the first version of your expense tracker as a plain HTML page. It doesn't work yet (that's Module 3, JavaScript), but it has every piece the app will need: a form to add an expense, a list of expenses, and a total.

Create your page at `01-html/assignment/index.html`. Work on your own. If you get stuck, ask for a hint (one at a time, each one is logged).

## Check your progress
Run this any time from the `webdev` folder. It only reads your page, it never changes it:

```
python3 01-html/assignment/checks/check_html.py
```

## Requirements

### Page
- [ ] Complete skeleton: `<!DOCTYPE html>`, `lang`, `charset`, `viewport`, and a real `<title>` (not "Document").
- [ ] A `<header>` containing the page's only `<h1>`.
- [ ] A `<main>` holding the form, the expense list, and the total.
- [ ] Formatted (Shift+Option+F) and free of typos.

### Form
- [ ] Expense name: a text input.
- [ ] Amount: a number input.
- [ ] Category: a `<select>` dropdown with at least 3 categories.
- [ ] An **Add** button.
- [ ] Every field has a `<label>` linked with `for`/`id` (test it by clicking each label).
- [ ] IDs are unique and contain no spaces.

### Expenses
- [ ] A list of **3 hardcoded expenses**. Each one shows its name, amount, and category.
- [ ] A total line, like "Total: …". The number must equal the sum of your 3 amounts (I check this one by hand).

## Done when
- [ ] Every automated check passes.
- [ ] Every checklist item above is met.
- [ ] Your work is committed and pushed on `module-1-html`.
- [ ] You type **submit**.

## Stretch goal (optional)
Add a **date** field to the form (`<input type="date">`, labeled), and show a date on each hardcoded expense using the `<time>` element. Look up `<time>` on MDN (developer.mozilla.org) yourself: reading docs is part of the job.
