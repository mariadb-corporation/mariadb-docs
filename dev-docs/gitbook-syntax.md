# GitBook syntax reference

Pages are Markdown plus GitBook block extensions. These blocks are the most common
machine-authoring mistakes — use them as shown, not plain-Markdown lookalikes.

Canonical source: the docs team's internal **GitBook Editing** page in Confluence (DOCS space) —
it wins when it disagrees with this digest; update this file to match. Prose/grammar style lives
in `dev-docs/style-guide.md`.

## Frontmatter

About half of existing pages open with YAML frontmatter; the rest have none. **New pages should
always include `description:`** (used for SEO + listings) even though many older pages lack it.
`icon:` is **rarely used** (≈0.2% of pages) — optional, omit if unsure.

```yaml
---
description: >-
  A concise, one- to two-sentence summary of the page, in American English.
---
```

Multi-line descriptions use YAML folded style (`>-`) as above. `icon:` (e.g. `icon: paperclip`)
may be added as a second key but is not expected.

## Headings

- The page **title is the `#` H1**; body sections start at `##`. Don't skip levels. (GitBook's
  app renumbers in its block dialog — Markdown `##` shows there as "H1" — but the **Markdown
  source** uses `#` title, `##` sections; author to the Markdown.)
- **Link targets:** headings down to `####` (Markdown) can be linked to; **`#####`+ cannot** be
  GitBook link targets (they work in GitHub preview but GitBook ignores them).
- **Casing is Title Case** — see `dev-docs/style-guide.md` › *Headings* (capitalize words ≥4
  letters; literals stay unformatted). This is a prose-style rule, enforced by `style-apply`.

## Hints (callouts)

```
{% hint style="info" %}
Body text. Supports Markdown.
{% endhint %}
```

Valid styles — use exactly these:

| Style | Use for (per the GitBook Editing guide) |
|-------|------------------------------------------|
| `info` | General information, tips and tricks (default, grey). Also the prime candidate for **reusable content**. |
| `warning` | Raise awareness for a particular piece of functionality (orange). |
| `danger` | Alert readers to destructive actions or critical information (red). |
| `success` | Highlight benefits of a feature or method (green). |

> Do **not** use `tip` or `warn` — a handful exist in the repo by mistake. Use `info` and
> `warning` respectively.

## Tabs

```
{% tabs %}
{% tab title="Ubuntu" %}
Instructions for Ubuntu.
{% endtab %}

{% tab title="RHEL" %}
Instructions for RHEL.
{% endtab %}
{% endtabs %}
```

## Code blocks with a title or line numbers

For a titled or line-numbered block, wrap a fenced code block in `{% code %}`:

````
{% code title="my.cnf" overflow="wrap" lineNumbers="true" %}
```ini
[mysqld]
max_connections = 200
```
{% endcode %}
````

A plain fenced code block (no title needed) is just standard Markdown:

````
```sql
SELECT * FROM t;
```
````

## Page references (content-ref)

A rich link card to another page:

```
{% content-ref url="reference/sql-statements/data-definition/create/create-table.md" %}
[create-table.md](reference/sql-statements/data-definition/create/create-table.md)
{% endcontent-ref %}
```

The link body and `url=` may point at a **file** (`.md`) or at a **directory** for a section
reference (e.g. `[Connecting](1-connecting/)`) — match the form of the target.

For a reference to a page in **another space**, use a link alias (see `link-aliases.md`).

## Images

Standard Markdown, with assets stored alongside content:

```
![Alt text describing the image](path/to/image.png)
```

## Reusable content (includes)

Shared content is pulled into a page with the `{% include %}` directive rather than
copy-pasted. Includes are heavily used here (~half of all pages). There are **two forms**:

### 1. Reusable-content include (most common)

References a GitBook **reusable content** block by its app URL:

```
{% include "https://app.gitbook.com/s/<spaceId>/~/reusable/<reusableId>/" %}
```

- The reusable block is authored/managed in the **GitBook web app** — it has no source file in
  this repo.
- **You can reference an existing one, but you cannot create a new one from Git** (there's no
  `~/reusable/<id>` to invent). To reuse a known shared block (e.g. a standard note that already
  appears on sibling pages), copy its exact `{% include %}` directive from one of those pages.
- **Never fabricate a `~/reusable/<id>` URL.** If no existing reusable fits, use a file include
  (below) or plain content instead.
- **Editing a reusable propagates to every page that includes it** — it's owned/edited only in
  its **parent space**. The block is backed by a file under that space's `.gitbook/includes/`, so
  to change its *formatting* (e.g. wrap it in a `{% hint %}`) edit that file in Git — e.g.
  `release-notes/.gitbook/includes/latest-10-6.md`. Don't edit a reusable's text casually; the
  change lands everywhere it's referenced.

### 2. File include

References a snippet file via a **relative path** to the snippet:

```
{% include "../../../.gitbook/includes/<snippet>.md" %}
```

- **Snippets are per-space:** they live in `<space>/.gitbook/includes/<snippet>.md`. (A repo-root
  `.gitbook/includes/` also exists but is rarely the target — default to the space's own.)
- **The relative depth = the number of directories between the page and its space root.** A page
  at `server/a/b/c/page.md` is 3 directories below `server/`, so the prefix is `../../../`
  (→ `server/.gitbook/includes/<snippet>.md`). The most common real depth is `../../../`; they
  range from `../` to `../../../../../../`.
- **You can create these from Git:** add the snippet file under `<space>/.gitbook/includes/`,
  then reference it. **Always verify the resolved path exists** (e.g. `ls`) before writing the
  directive — a wrong `../` count silently renders an empty include and isn't caught by
  link-check.

Don't duplicate include content into pages by hand — reference the include. To add or repair an
`{% include %}` directive, use the **`gitbook-format`** skill.

## Lists with nested blocks

To put a code block, hint, or other block **inside a list item**, indent the whole block by 2
spaces (the GitBook app can't do this — it's a Git/editor-only edit):

````markdown
* Validate the configuration. Example:
  {% code %}
  ```bash
  mariadbd --defaults-file=/etc/my.cnf --validate-config
  ```
  {% endcode %}
````

## Tables

Markdown tables. Notes from the GitBook Editing guide:

- **No whitespace padding** — Markdown tables don't need aligned columns; don't pad cells (it can
  bloat a page's size dramatically).
- **Bulk table edits** (splitting a table, deleting many rows) are easier in GitHub/an editor
  than the GitBook app.
- Setting a column **width** or **sticky header** in the app converts the table to raw HTML,
  which is then hard to edit — avoid unless necessary.

## Links

- **Within the same space:** relative Markdown link to the `.md` file
  — `[CREATE TABLE](reference/.../create-table.md)`.
- **To another space:** a link alias — `[MaxScale]({maxscale}/readme)`. See `link-aliases.md`.
- Never paste raw `https://app.gitbook.com/...` URLs.
