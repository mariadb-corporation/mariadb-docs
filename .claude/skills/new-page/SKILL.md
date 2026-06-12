---
name: new-page
description: Scaffold a new MariaDB documentation page in the right space with correct frontmatter, house style, GitBook syntax, and a SUMMARY.md nav entry in the correct place. Use when the user asks to "create a new page", "add a docs page", "start a new doc", "write a page about X", or "add a page under <space>". Scopes to one space; asks for the target location if unclear.
allowed-tools: Bash, Read, Grep, Glob, Edit, Write
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# new-page

Create a new documentation page that is publishable as-is: correct frontmatter, the house
style, valid GitBook syntax, and — crucially — a `SUMMARY.md` navigation entry so the page
actually appears in the docs. References: `dev-docs/space-map.md`, `dev-docs/style-guide.md`,
`dev-docs/gitbook-syntax.md`, `dev-docs/link-aliases.md`.

## When to use

The user says: "create a new page", "add a docs page about X", "start a new doc under
`<space>`", "write a page on Y".

## 0. Gather the essentials (ask only what's missing)

- **Topic / title** of the page.
- **Space** it belongs to (server, maxscale, connectors, …). If unclear, propose one from
  `dev-docs/space-map.md` and confirm — **never guess across spaces.**
- **Where in that space** (which subdirectory / which parent in the nav). If unclear, look at
  the space's structure and propose a location.

Do not proceed to write until the space and location are settled. Operate within **one** space.

## 1. Decide the file path

- **Leaf pages:** prefer **kebab-case** `.md` (e.g. `configuring-the-binary-log.md`), but
  **preserve underscores when the name is an identifier** — a system variable, function, or tool
  (e.g. `auto_increment-handling.md`, `my_print_defaults.md`). Many existing files use
  underscores deliberately; match the convention of siblings.
- **Section landing pages must be named `README.md`** (uppercase). If you're creating a new
  subsection (a directory), its index page is `<dir>/README.md`, not `index.md` or a
  kebab-named page — GitBook treats `README.md` as the directory's page.
- GitBook derives the published URL from the **file path**, so the path is the URL — choose it
  deliberately (this is independent of where the page sits in `SUMMARY.md`).
- Place the file in the appropriate subdirectory of the space (see the space's sub-structure in
  `dev-docs/space-map.md`). SQL/reference content lives under `server/reference/`.
- **Refuse to create pages** in non-space directories: `mariadb-platform/` and
  `.gitbook/includes/` are for **include snippets** (use those only when the task is explicitly
  a reusable include), and `help-tables/` is generated. See `dev-docs/space-map.md` ›
  *Non-space directories*. **Don't confuse `mariadb-platform/` (includes-only, no nav) with the
  `platform/` space** (MariaDB Enterprise Platform docs) — Platform pages go in `platform/`.
- Confirm the path doesn't already exist (`ls`/`git ls-files`).

## 2. Write the page

Start from this skeleton, then fill it in:

```markdown
---
description: >-
  One- to two-sentence summary of the page, in American English. Used for SEO and listings.
---

# <Page Title>

<Lead paragraph: what this page covers and who it's for.>

## <Section>

<Body. Use GitBook blocks where appropriate — see dev-docs/gitbook-syntax.md.>
```

Rules:

- **Always include `description:`** on a new page (folded `>-` style) — even though ~half of
  existing pages have no frontmatter at all, new pages should have it. `icon:` is **optional and
  rarely used** (≈0.2% of pages) — omit it unless a sibling page sets one. When matching
  neighbors, match frontmatter *style/keys*, not their *absence* of frontmatter.
- **House style:** American English, Google developer-doc tone, sentence-style headings, one
  `#` H1. See `dev-docs/style-guide.md`.
- **GitBook blocks:** use `{% hint %}` (styles `info`/`warning`/`danger`/`success`),
  `{% tabs %}`, `{% code %}`, `{% content-ref %}` correctly — see `dev-docs/gitbook-syntax.md`.
  If you need callouts/tabs/titled code, prefer invoking the **`gitbook-format`** skill rather
  than hand-rolling block syntax.
- **Links:** same-space links are relative `.md` paths; cross-space links use `{alias}/path`
  (never raw `app.gitbook.com` URLs). See `dev-docs/link-aliases.md`.
- **Reuse shared content — don't duplicate:** if the page needs boilerplate that already
  appears on sibling pages (a standard note, install snippet, version banner, etc.), pull it in
  with an `{% include %}` instead of copying it. Reference an existing reusable block by copying
  its directive from a sibling page **in the same space** (search only the current space — a
  reusable URL embeds a space ID and isn't portable), or create a file include under
  `<space>/.gitbook/includes/` — but **never fabricate a `~/reusable/<id>` URL** (those exist
  only in the GitBook UI). Delegate the include syntax to the **`gitbook-format`** skill; full
  detail in `dev-docs/gitbook-syntax.md`.

## 3. Add the `SUMMARY.md` nav entry (do not skip)

A page with no `SUMMARY.md` entry won't appear in the published nav. Edit the **space's**
`SUMMARY.md`:

1. Open `<space>/SUMMARY.md` and find the section/parent the page belongs under.
2. Add `* [<Page Title>](<path within space>/<file>.md)` at the right place. **Match the
   surrounding style exactly**: `* [Title](path)` with **two-space indents per nesting level**.
   Set the indent to match the **sibling entries under your chosen parent** — nav nesting is a
   **topical grouping and need not match the file's directory depth** (entries under one nav
   section routinely link into unrelated directories). Set the link to the real `path/to/file.md`
   regardless of where it sits in the nav.
3. Pick a sensible position (alphabetical or topical, matching neighbors). If the right slot is
   ambiguous, ask rather than guess — reordering nav is disruptive.
4. Don't reorder or touch unrelated entries. (Note: the nightly error-sync job legitimately
   auto-commits `server/SUMMARY.md`.)

## 4. Validate before finishing

Run the canonical linter on the new file from the repo root, then the structural checks:

```bash
.claude/hooks/doc-lint.sh <new-file>
```

Or invoke the **`docs-check`** skill on the new file (frontmatter present, blocks balanced,
link style, `SUMMARY.md` consistency). Fix anything it flags.

## 5. Report

Tell the user: the file path (and resulting URL hint), the `SUMMARY.md` entry added, and the
validation result. Note any judgment calls you made (space, location, nav placement) so they
can adjust.

## Guardrails

- One space at a time; never fan out across spaces.
- Never author standalone pages in `mariadb-platform/`, `.gitbook/includes/`, or `help-tables/`.
- Never expand `{alias}` links or paste raw `app.gitbook.com` URLs.
- Don't invent facts — if the page needs technical content you can't verify, leave a clearly
  marked `<!-- TODO: confirm ... -->` and tell the user.
