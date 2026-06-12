---
name: gitbook-format
description: Emit or repair GitBook block syntax in MariaDB docs and convert links to the right form. Use when the user asks to "add a hint/note/callout", "make this a warning box", "add tabs", "format this code block with a title", "add a content-ref", "fix the GitBook formatting", or "convert these links to aliases". Knows the valid hint styles and the cross-space alias table; never touches content inside code blocks.
allowed-tools: Read, Grep, Glob, Edit, Write, Bash
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# gitbook-format

Produce correct GitBook-flavored Markdown: callouts, tabs, titled code, page-reference cards,
and proper links. Use it when authoring new content or cleaning up a page that uses
plain-Markdown substitutes for GitBook blocks. Canonical references:
`dev-docs/gitbook-syntax.md` and `dev-docs/link-aliases.md` — defer to those for exact syntax.

For block types **outside this skill's daily-use set** (stepper, columns, updates, cards,
embeds, files, buttons, icons, expandable, variables, expressions, `.gitbook.yaml`,
`SUMMARY.md` format, OpenAPI), defer to the vendored
[`gitbook-canonical`](../gitbook-canonical/SKILL.md) skill — the upstream GitBook reference.

## When to use

The user says: "add a note/hint/callout", "make this a warning", "turn this into tabs",
"give this code block a title", "add a content-ref to X", "fix the GitBook formatting on this
page", "convert these to alias links".

## Capabilities

### 1. Hints (callouts)

Convert prose notes / blockquote-style admonitions into:

```
{% hint style="info" %}
…
{% endhint %}
```

Style mapping — use **only** these four:

| Intent | Style |
|--------|-------|
| Note / tip / FYI | `info` |
| Caution / heads-up | `warning` |
| Data loss / security / destructive | `danger` |
| Confirmation / "done" | `success` |

Fix any `style="tip"` → `info` and `style="warn"` → `warning` (both are mistakes that exist in
a handful of pages).

### 2. Tabs

Turn "on Ubuntu / on RHEL"-style parallel content into:

```
{% tabs %}
{% tab title="Ubuntu" %}
…
{% endtab %}
{% tab title="RHEL" %}
…
{% endtab %}
{% endtabs %}
```

### 3. Code blocks with a title / line numbers

Wrap a fenced code block in `{% code %}` only when a title or line numbers add value:

````
{% code title="my.cnf" overflow="wrap" lineNumbers="true" %}
```ini
…
```
{% endcode %}
````

A plain fenced block needs no `{% code %}`.

### 4. Page references (content-ref)

```
{% content-ref url="<relative-or-alias path>" %}
[<file>.md](<same path>)
{% endcontent-ref %}
```

The link body can point at a file (`[create-table.md](.../create-table.md)`) **or a directory**
for a section reference (`[Text](1-connecting/)`). Match the form of the URL you're referencing.

### 5. Includes (`{% include %}`)

Reuse shared content instead of copy-pasting it. Two forms (full detail in
`dev-docs/gitbook-syntax.md`):

- **Reusable-content include** — `{% include "https://app.gitbook.com/s/<space>/~/reusable/<id>/" %}`.
  Reference an existing one only: if the same shared block already appears on sibling pages,
  copy its exact directive. **Never fabricate a `~/reusable/<id>` URL** — those blocks are
  created in the GitBook UI and have no source here. The URL embeds a **space ID**, so only copy
  it from a page **in the same space** (it's not portable across spaces).
- **File include** — `{% include "../../../.gitbook/includes/<snippet>.md" %}`. Snippets are
  **per-space** (`<space>/.gitbook/includes/`). The `../` prefix has **one `..` per directory
  between the page and its space root** — a page at `server/a/b/c/page.md` is 3 dirs below
  `server/`, so `../../../`. You may create the snippet file there and reference it; **always
  `ls` the resolved path to confirm it exists** before writing the directive (a wrong count
  renders an empty include and link-check won't catch it). Full detail: `dev-docs/gitbook-syntax.md`.

When duplicated boilerplate appears across pages, prefer converting it to an include over
repeating it. If no suitable reusable block exists and a file include isn't warranted, leave the
content inline rather than inventing an include.

### 6. Links

- **Same space** → relative `.md` path: `[CREATE TABLE](reference/.../create-table.md)`.
- **Other space** → alias: `[MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/readme)`. Alias table:
  `dev-docs/link-aliases.md`.
- **Convert** raw `https://app.gitbook.com/...` URLs and hard-coded cross-space URLs into the
  appropriate alias. **Never** expand an existing `{alias}` into a URL — the CI Action does that.

### 7. Repair unbalanced blocks

For each block type, every opener has its closer: `{% hint %}`↔`{% endhint %}`,
`{% tabs %}`↔`{% endtabs %}`, `{% tab %}`↔`{% endtab %}`, `{% code %}`↔`{% endcode %}`,
`{% content-ref %}`↔`{% endcontent-ref %}`. Flag and fix mismatches. (`{% include %}` is a
self-contained directive — no closer.)

## Hard guardrails

- **Never modify content inside fenced code blocks (```) or `{% code %}` blocks.** SQL, JSON,
  config, and protocol samples legitimately contain `{`, `%`, `{%`-like fragments, and raw
  URLs — they are examples, not GitBook syntax or links to "fix". This is the #1 false-positive
  trap; treat code-fence contents as opaque.
- **Never expand `{alias}` links.** Leave them as `{alias}/path`.
- **Never fabricate a reusable include URL/ID** (`~/reusable/<id>`). Only reference one copied
  verbatim from an existing page; otherwise use a file include or inline content.
- **Don't rewrite prose** beyond the formatting change requested — preserve wording, change
  structure/syntax only.
- **Scope to the file(s) given.** Don't sweep a whole space unless explicitly asked (and if
  asked, treat it as a bulk pass and confirm scope first).

## Workflow

1. Read the target file(s). Identify the content to convert or repair, skipping code-fence
   regions.
2. Apply the change with `Edit`, matching the conventions in `dev-docs/gitbook-syntax.md`.
3. Verify block balance and, if links changed, run `.claude/hooks/doc-lint.sh <file>` (or the
   `docs-check` skill) to confirm nothing broke.
4. Report what changed (which blocks/links), and confirm code samples were left untouched.
