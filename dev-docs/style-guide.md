# Style guide (local digest)

This is the **agent-facing digest** of the MariaDB documentation style rules. The **canonical
sources** win when they disagree with this file (update this file to match):

- The **published style guide** —
  `https://mariadb.com/docs/general-resources/about/about-mariadb-documentation/documentation-style-guide/`
- The docs team's internal **Documentation Guidelines** (generic) and **GitBook Editing**
  (tool-specific) pages in Confluence (DOCS space) — the fuller sources; ask the docs team for
  access. `dev-docs/gitbook-syntax.md` digests the GitBook-source-format parts.

The `style-apply` skill enforces the checkable parts of this digest.

## Core conventions

- **American English** (not British). Present tense (unless genuinely about the future); active
  voice; second person ("you", not "one"/"they"/"he"). Concise — cut wordiness. Use consistent
  terminology across pages; avoid jargon and colloquialism. Break up text-heavy paragraphs.

## Headings

- **Title Case: capitalize the words in a heading.** Exceptions: words with **fewer than 4
  letters** (e.g. *to*, *the*, *and*, *for*, *in*, *of*) stay lowercase, and **literals** are not
  capitalized (and not formatted as code) in headings — avoid literals in headings where
  possible. *(This is the opposite of sentence case — get it right.)*
- Heading levels & link targets (GitBook): the page title is the `#` H1; body sections start at
  `##`. In Markdown, headings `##`–`####` can be link targets; `#####`+ **cannot**. Don't skip
  levels. Detail: `dev-docs/gitbook-syntax.md`.

## Literals, placeholders, keywords

- **Literals → inline `code`** (backticks): program/command names, variable & option names,
  keyboard shortcuts, SQL keywords, file names. Keywords like `NULL` and value ranges (`0` to
  `360`) are formatted as code.
- **Placeholders → *italics*** (and also `code` when adjacent to a literal). Use **meaningful
  names** — `table`, `database`, `string` — not `tbl`, `db`, `x`, `<x>`. Exception: inside code
  blocks GitBook can't format, so use "fancy" placeholders there (e.g. `CREATE TABLE tbl`).
- **Don't mix natural language and keywords:** "INSERTs cannot be used" → "`INSERT` statements
  cannot be used." **SQL things are statements, not commands** ("the `INSERT` statement", not
  "the INSERT command").
- **Don't treat a code block as part of a sentence** — introduce it, then show it.

## Grammar & word choice

- **Oxford comma is mandatory** in enumerations: "`DELETE`, `TRUNCATE`, or `MODIFY`".
- **Avoid hyphens** (modern English agglutinates): `sub-partition`→`subpartition`,
  `non-equal`→`nonequal` (or "not equal"); keep a hyphen only where ambiguous (`re-creation`).
  Distinguish compound adjectives from noun chains: "a `case-sensitive` syntax" (adjective) vs
  "this syntax is case sensitive" (predicate); "to **back up** your data, make a **backup**".
- `commandline` → **command line**; `resultset` / `result-set` → **result set**.
- **Avoid "for example"** unless it's genuinely needed to mark an example.
- **Avoid assumptive/filler words:** *simply*, *easily*, *obviously*, *basically*, *of course*,
  *please*. Say "Click OK", not "Simply click OK".
- **Neutral action verbs:** avoid violent metaphors — `kill`/`abort`/`hang` → `terminate` /
  `stop` / `cancel` / `unresponsive`.

## Inclusive terminology (DOCS-5606)

In core docs (Server, MaxScale, ColumnStore, Connectors): **master → primary**, **slave →
replica**. Exceptions where the term **cannot** change:

- **Release notes** (they reflect the past) — leave as-is.
- **Software-fixed terms**: system variables, status variables,
  `information_schema.slave_status`, and SQL keywords (there is no `PRIMARY` alias for `MASTER`).
- **ColumnStore** uses **leader / follower**.

Discovery (informational for the unchangeable cases):
`git grep -Ei "blacklist|whitelist|master|slave|sanity|abort|basically|obviously|dummy"`.

## Forward-looking statements

**Avoid** statements about future/unreleased behavior. Exception: a concrete, planned change —
indicated by an MDEV ticket with a **Fix Version** filled in. (This is exactly what
`doc-from-ticket` verifies before asserting behavior.)

## Links

- Same space → relative `.md` link; other space → `{alias}` link; never raw `app.gitbook.com`
  URLs. See `dev-docs/link-aliases.md`.
- **Avoid over-linking:** at most **one link per page section** to a given target; render the
  rest as `literals`.

## Naming

Product names as MariaDB writes them: **MariaDB Server**, **MariaDB MaxScale**, **Galera
Cluster**, **ColumnStore**, **MariaDB Enterprise Platform**. Note: "MariaDB server" (lowercase,
common noun — "the MariaDB server process") and "Galera cluster" (a cluster instance) are often
correct; only the branded product is title-cased.

In **running prose**, use the full product name on first mention; a short form on subsequent
mentions in the same page is fine and normal ("If you are upgrading from an older major version
of MaxScale…").

### Release-note page titles

Release-note H1s follow a **per-product** convention that is not derivable from the rule above.
Match the sibling pages in the same directory rather than applying the full product name
everywhere. Check before you edit, and don't "correct" a page into disagreeing with its
neighbours.

**MariaDB MaxScale** is the one product where the parent and child titles deliberately differ:

| Page role | H1 form |
|-----------|---------|
| Series page — `release-notes/maxscale/<series>/README.md` | `MariaDB MaxScale 25.10 Release Notes` |
| Point release nested under it | `MaxScale 25.10.3 Release Notes` |

The short form on children avoids repeating the brand at every level of a nav tree whose parent
already carries it. `SUMMARY.md` nav labels mirror the page's own H1, so the two must agree.
Changelog pages (`<series>-changelog.md`) use the short form — they are not parents of release
notes. The `old-releases/2.4` and `old-releases/2.5` archives predate this convention and use
the full name throughout; they are self-consistent, so leave them alone.

Other products do **not** split parent from child, so don't generalize the MaxScale pattern:

- **ColumnStore** — same form at both levels: `MariaDB ColumnStore 6 Release Notes` over
  `MariaDB ColumnStore 6.4.8 Release Notes`.
- **Connectors** — same form at both levels, and **without** the MariaDB prefix in titles:
  `Connector/J 3.5 Release Notes` over `Connector/J 3.5.9 Release Notes`.
- **Community Server** — varies the word order between levels, not the brand form:
  `Release Notes - MariaDB 12.3 Series` over `MariaDB 12.3.3 Release Notes`.

The MaxScale release notes are generated — `release-notes/maxscale/script/generate_release_notes.sh`
emits the point-release form. If this convention changes, change the template too, or the next
generated page reintroduces the old form.

## Spelling check

CI runs **codespell** (`.codespellignore`). If a flagged word is a real term, add it to
`.codespellignore` sparingly — only for genuine false positives.
