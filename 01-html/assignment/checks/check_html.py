"""Automated checks for the Module 1 assignment (expense tracker static page).

Run from the webdev folder:  python3 01-html/assignment/checks/check_html.py
Read-only: it parses your index.html and never changes it.
"""

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ASSIGNMENT = Path(__file__).resolve().parents[1]
PAGE = Path(sys.argv[1]) if len(sys.argv) > 1 else ASSIGNMENT / "index.html"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
UNLABELLED_TYPES = {"submit", "button", "hidden", "reset", "image"}
NOT_TOTAL_TAGS = {"html", "body", "main", "section", "div", "form", "ul", "ol", "li", "label", "option", "select", "button"}

results = []


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag = tag
        self.attrs = {key: value or "" for key, value in attrs}
        self.parent = parent
        self.children = []

    def text(self):
        parts = [c if isinstance(c, str) else c.text() for c in self.children]
        return " ".join(" ".join(parts).split())

    def walk(self):
        for child in self.children:
            if isinstance(child, Node):
                yield child
                yield from child.walk()

    def find(self, *tags):
        return (node for node in self.walk() if node.tag in tags)

    def inside(self, tag):
        node = self.parent
        while node is not None:
            if node.tag == tag:
                return True
            node = node.parent
        return False


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None)
        self.current = self.root
        self.doctype = ""

    def handle_decl(self, decl):
        self.doctype = decl

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in VOID:
            self.current = node

    def handle_startendtag(self, tag, attrs):
        self.current.children.append(Node(tag, attrs, self.current))

    def handle_endtag(self, tag):
        # Close the nearest open element with this tag, forgiving like a browser.
        node = self.current
        while node is not self.root and node.tag != tag:
            node = node.parent
        if node is not self.root:
            self.current = node.parent

    def handle_data(self, data):
        self.current.children.append(data)


def check(name, ok, hint=""):
    results.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok and hint:
        print(f"       -> {hint}")


def describe(node):
    label = node.attrs.get("id") or node.attrs.get("name") or "no id/name"
    kind = f" type={node.attrs['type']}" if "type" in node.attrs else ""
    return f"<{node.tag}{kind}> ({label})"


def input_type(node):
    return (node.attrs.get("type") or "text").lower()


def check_skeleton(builder, root):
    check("Starts with <!DOCTYPE html>", builder.doctype.strip().lower() == "doctype html",
          "the very first line of the file declares modern HTML.")

    html = next(root.find("html"), None)
    check("<html> has a lang attribute", html and html.attrs.get("lang"),
          "tell browsers and screen readers the page language.")

    metas = list(root.find("meta"))
    check("<meta charset> is set", any(m.attrs.get("charset") for m in metas))
    check("<meta name=\"viewport\"> is set", any(m.attrs.get("name") == "viewport" for m in metas),
          "needed for phone screens (Module 2 depends on it).")

    title = next(root.find("title"), None)
    title_text = title.text() if title else ""
    check("<title> is filled in (not \"Document\")", title_text and title_text != "Document",
          "the text shown in the browser tab.")


def check_layout(root):
    headers = list(root.find("header"))
    h1s = list(root.find("h1"))
    check("A <header> exists", headers)
    check("Exactly one <h1>, inside the <header>", len(h1s) == 1 and h1s[0].inside("header"),
          f"found {len(h1s)} <h1>. One per page, in the header.")
    mains = list(root.find("main"))
    check("A <main> exists", mains)


def check_form(root):
    forms = [f for f in root.find("form") if f.inside("main")]
    check("A <form> inside <main>", forms)
    if not forms:
        return
    form = forms[0]
    inputs = list(form.find("input"))

    check("Expense name: a text input in the form",
          any(input_type(i) == "text" for i in inputs))
    check("Amount: a number input in the form",
          any(input_type(i) == "number" for i in inputs))

    def real_options(select):
        values = [o.attrs.get("value", o.text()) for o in select.find("option")]
        return [v for v in values if v.strip()]

    selects = list(form.find("select"))
    check("Category: a <select> with at least 3 categories",
          any(len(real_options(s)) >= 3 for s in selects),
          "options with an empty value (like a \"Choose…\" placeholder) don't count.")

    buttons = [b.text() for b in form.find("button")]
    buttons += [i.attrs.get("value", "") for i in inputs if input_type(i) == "submit"]
    check("An Add button in the form", any("add" in b.lower() for b in buttons),
          "the button's visible text should say Add.")


def check_labels(root):
    label_targets = {l.attrs.get("for") for l in root.find("label") if l.attrs.get("for")}
    controls = [n for n in root.find("input", "select", "textarea")
                if not (n.tag == "input" and input_type(n) in UNLABELLED_TYPES)]
    missing = [describe(c) for c in controls
               if not c.inside("label") and c.attrs.get("id") not in label_targets]
    check("Every input/select/textarea has a linked <label>", not missing,
          f"no matching label for: {', '.join(missing)}")


def check_ids(root):
    ids = [n.attrs["id"] for n in root.walk() if "id" in n.attrs]
    duplicates = [i for i, count in Counter(ids).items() if count > 1]
    spaced = [i for i in ids if re.search(r"\s", i) or not i]
    check("IDs are unique", not duplicates, f"used more than once: {', '.join(duplicates)}")
    check("IDs contain no spaces", not spaced, f"invalid ids: {', '.join(repr(i) for i in spaced)}")


def check_expenses(root):
    lists = [l for l in root.find("ul", "ol") if l.inside("main") and not l.inside("form")]
    best = max(lists, key=lambda l: len(list(l.find("li"))), default=None)
    items = list(best.find("li")) if best else []
    check("A list in <main> with at least 3 expenses", len(items) >= 3,
          f"found {len(items)} list item(s) outside the form.")
    check("Every expense shows an amount (a number)",
          items and all(re.search(r"\d", li.text()) for li in items))

    totals = [n for n in root.walk()
              if n.tag not in NOT_TOTAL_TAGS and not n.inside("form")
              and re.search(r"total", n.text(), re.I) and re.search(r"\d", n.text())
              and len(n.text()) <= 80]
    check("A total line with a number (e.g. \"Total: ...\")", totals,
          "a short element whose text says Total and shows the amount.")


def main():
    print("Module 1 assignment checks\n")
    if not PAGE.exists():
        check(f"{PAGE.name} exists in 01-html/assignment/", False,
              "create your page at 01-html/assignment/index.html")
        print(f"\n{sum(results)}/{len(results)} checks passed.")
        return

    builder = TreeBuilder()
    builder.feed(PAGE.read_text(encoding="utf-8"))
    root = builder.root

    check_skeleton(builder, root)
    check_layout(root)
    check_form(root)
    check_labels(root)
    check_ids(root)
    check_expenses(root)
    print(f"\n{sum(results)}/{len(results)} checks passed.")


if __name__ == "__main__":
    main()
