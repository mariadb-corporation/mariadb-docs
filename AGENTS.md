# AGENTS.md

Cross-tool reference for AI agents working in the **MariaDB documentation** repository
(`github.com/mariadb-corporation/mariadb-docs`, published at https://mariadb.com/docs).

This file is the dense reference; `CLAUDE.md` holds the short rules and imports this file.

## What this repo is

The complete source of the MariaDB product documentation: **Markdown pages** authored with
**GitBook** extensions, organized into independent **spaces**. It is large — roughly 9,900
`.md` files — so always orient with the space map before searching.

## GitBook sync (read this first)

Pages are edited from **two sides**, and both land in Git history:

- **`GITBOOK-XXX` commits** — authored in the GitBook web app, synced back to Git.
- **`DOCS-XXXX` commits** — authored via Git pull requests (the contributor / agent path).

Consequences for agents:

- **`SUMMARY.md` is GitBook navigation**, not a normal page. Each space has one. Editing it
  reorders/renames the published nav tree. Change it only when you intentionally add, move, or
  rename a page — and match the existing indentation/link style exactly.
- **Avoid large structural refactors** (mass renames/moves) without coordinating — they can
  collide with concurrent GitBook-UI edits and are painful to reconcile in the sync.
- **Frontmatter and GitBook blocks are meaningful**, not decoration. Preserve them.

## The documentation spaces

There are **11 browsable GitBook spaces** (each with a `README.md` landing page and a
`SUMMARY.md` nav tree) plus the generated `help-tables/`. **Not every top-level directory is a
space** — see *Non-space directories* below. Full breakdown and sub-structure:
`dev-docs/space-map.md`.

| Space | Path | Scope | Rough size |
|-------|------|-------|-----------:|
| Server | `server/` | MariaDB Server — SQL reference, admin, security, HA | ~4,540 |
| Release Notes | `release-notes/` | Release notes for all products | ~2,810 |
| Platform | `platform/` | MariaDB Enterprise Platform | ~820 |
| MaxScale | `maxscale/` | MaxScale proxy | ~780 |
| Connectors | `connectors/` | C, C++, Java, ODBC, Python, Node.js, .NET, R2DBC | ~290 |
| Analytics | `analytics/` | ColumnStore / analytics | ~190 |
| MariaDB Cloud | `mariadb-cloud/` | Cloud / DBaaS | ~135 |
| Tools | `tools/` | Enterprise Manager, MCP server, Operator, AI-RAG | ~130 |
| General Resources | `general-resources/` | About, community, style, legal | ~130 |
| Galera Cluster | `galera-cluster/` | Galera replication | ~95 |
| Help Tables | `help-tables/` | **Generated** SQL help tables | 2 |
| Home | `home/` | Landing / portal | 4 |

> `tools/` is documentation content (a space), **not** a scripts directory.

### Non-space directories

These top-level directories are **not** browsable spaces — don't treat them as content:

- `mariadb-platform/` — a GitBook **includes** container (`mariadb-platform/.gitbook/includes/`,
  ~16 reusable "most-recent release" snippets). It holds include files, not browsable pages, so
  it has no `README.md` or `SUMMARY.md`. Add a **new include file** here when the work needs one
  (e.g. a reusable snippet referenced from a page) — but don't author standalone pages here.
- `dev-docs/` — agent/contributor playbooks (this file's companions). Not published.
- `.claude/` — shared Claude Code config, skills, hooks. Not published.
- `.gitbook/includes/` — repo-level reusable snippets inserted into pages by GitBook.

## Source format & GitBook blocks

Plain Markdown plus GitBook extensions. Get these right — they are the most common
machine-authoring mistakes. Full reference with examples: `dev-docs/gitbook-syntax.md`.

- **Hints** (callouts): `{% hint style="info" %}` … `{% endhint %}`. Valid styles:
  `info`, `warning`, `danger`, `success`. (`tip`/`warn` appear rarely and are mistakes —
  use `info`/`warning`.)
- **Tabs**: `{% tabs %}` / `{% tab title="…" %}` / `{% endtab %}` / `{% endtabs %}`.
- **Code with title/line numbers**: `{% code title="…" %}` … `{% endcode %}`.
- **Page references**: `{% content-ref url="…" %}` … `{% endcontent-ref %}`.

## Frontmatter

Most pages open with YAML frontmatter. New pages **must** include `description:`
(used for SEO and listings) and usually `icon:`:

```yaml
---
description: One- or two-sentence summary of the page (American English).
icon: paperclip
---
```

## Cross-space links: aliases

Link between spaces with `{alias}/path/to/page`, never raw `app.gitbook.com` URLs.
A PR GitHub Action (`expand-gitbook-aliases.yml`) rewrites aliases to real URLs on merge.

- Do **not** expand aliases yourself or rewrite expanded URLs back.
- Aliased links **don't resolve in a local editor / GitHub UI** — that's expected; they work
  on the published site. The link-checker is configured to skip them.

Alias table and rules: `dev-docs/link-aliases.md`.

## CI gates (and how to preempt them locally)

Pull requests run these GitHub Actions. Mirror them locally with the **`docs-check`** skill
(or the pre-commit hook) so PRs pass on the first push. Full checklist: `dev-docs/cookbook-pre-pr.md`.

| Workflow | Tool | What it checks |
|----------|------|----------------|
| `codespell.yml` | codespell | Common misspellings in changed `*.md`/`*.html` (+ filenames), using `.codespellignore` |
| `link-check-pr.yml` | lychee | Broken links in changed `*.md`/`*.html` (skips `{alias}` links, localhost, a few known hosts) |
| `expand-gitbook-aliases.yml` | sed | Expands `{alias}` → real URL on PR (auto-commits) |
| `generate-help-tables.yml` | Python | Regenerates `help-tables` SQL from `server/reference/**` |
| `nightly-error-sync.yml` | Python | Nightly regen of server error-code pages |

## Generated content — do not hand-edit

- **`help-tables/`** is generated from `server/reference/**` by `help-tables/markdown_extractor.py`.
  To change help-table output, edit the **source reference page**, not the generated SQL.
- Server **error-code pages** are refreshed by the nightly error-sync job, which also
  auto-commits `server/SUMMARY.md` — an authorized exception to the "SUMMARY.md is hand-curated"
  rule. Don't treat its entries as anomalies.

## Style

American English; Google developer-documentation tone. Local summary and links to the
canonical MariaDB style guide: `dev-docs/style-guide.md`.

## Common gotchas

1. `SUMMARY.md` is published navigation — edit deliberately, preserve indentation/link style.
2. `tools/` is a docs space, not a scripts dir — agent scripts go in `.claude/hooks/`.
3. `{alias}` links won't resolve locally and must not be expanded by hand.
4. `help-tables/` and server error pages are generated — edit the source, not the output.
5. CI runs codespell + lychee on **every changed `*.md`** — including files under `dev-docs/`.
   Keep agent docs clean too.
6. Server alone is ~4,540 files — scope searches and bulk edits to a space/path, never the whole repo.
7. Both GitBook-UI and Git edits are live; don't assume Git is the only writer.
8. **`server/reference/**/*.md` heading invariant.** Pages under `server/reference/` must keep the `# Title` / `## Syntax` / `## Description` (or `## Overview`) / `## Examples` / `## See Also` heading shape — `help-tables/markdown_extractor.py` parses these to build the MariaDB CLI's `HELP` content. Full detail: `help-tables/HELP_TABLES_PIPELINE.md`.
