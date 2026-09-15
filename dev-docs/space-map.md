# Space map

The repository is split into independent **GitBook spaces**. Most top-level directories are a
space, each with a `README.md` (landing page) and a `SUMMARY.md` (navigation tree) — but a few
top-level directories are *not* spaces (see *Non-space directories* below). Use this map to
orient before searching — the repo is ~9,900 `.md` files.

## Spaces

| Space | Path | Scope |
|-------|------|-------|
| Server | `server/` | MariaDB Server: SQL reference, admin, security, HA & performance |
| Release Notes | `release-notes/` | Release notes for every product |
| Platform | `platform/` | MariaDB Enterprise Platform |
| MaxScale | `maxscale/` | MaxScale database proxy |
| Connectors | `connectors/` | Client connectors (C, C++, Java, ODBC, Python, Node.js, .NET, R2DBC) |
| Analytics | `analytics/` | ColumnStore and analytics |
| MariaDB Cloud | `mariadb-cloud/` | Cloud / DBaaS |
| Tools | `tools/` | Enterprise Manager, MCP server, Kubernetes Operator, AI-RAG, Control Center |
| GridGain | `gridgain/` | GridGain 8 and GridGain 9 — **placeholder**, content being migrated from AsciiDoc |
| General Resources | `general-resources/` | About, community, style guide, legal, theory |
| Galera Cluster | `galera-cluster/` | Galera synchronous replication |
| Help Tables | `help-tables/` | **Generated** SQL `HELP` tables (do not hand-edit) |
| Home | `home/` | Portal / landing |

(12 browsable spaces + the generated `help-tables/`.)

The `gridgain/` space is new and holds placeholder landing pages only. It is **not** registered in
`pdf/build.py` (`ALL_SPACES` / `SPACE_TITLES`) — add it there once real content lands, or the PDF
job will publish a near-empty book.

## Non-space directories

Top-level directories that look like content but are **not** browsable spaces:

| Path | What it is |
|------|------------|
| `<space>/.gitbook/includes/` | A space's reusable snippets, inserted into its pages by GitBook. Belongs to that space only — see *Reusable includes* below. |
| `dev-docs/` | Agent/contributor playbooks (not published). |
| `.claude/` | Shared Claude Code config, skills, hooks (not published). |

## Reusable includes

A relative `{% include "../.gitbook/includes/foo.md" %}` resolves **within one space** and may not
cross a space boundary — each space has its own GitBook Git-sync root, so a path climbing into a
sibling space fails even though it resolves on disk. Add a new snippet to the
`.gitbook/includes/` of the space that uses it. Cross-space reuse goes by ID instead:

```
{% include "https://app.gitbook.com/s/<spaceId>/~/reusable/<reusableId>/" %}
```

Two containers that belonged to **no** space — `mariadb-platform/.gitbook/includes/` (16 files)
and the repo-root `.gitbook/includes/` (2 files) — were deleted in DOCS-6372: the GitBook API
showed no space wired to either, so nothing in them could render, and their contents had gone a
year stale. `.claude/hooks/doc-lint.sh` now fails on a missing or cross-space include; lychee
cannot see `{% include %}` at all, because it is template syntax rather than a Markdown link.

## Sub-structure of the larger spaces

**`server/`** (largest space):

- `architecture/` — internals and design
- `reference/` — SQL statements, functions, data types, system variables, status variables
- `server-management/` — install, configure, operate
- `server-usage/` — using the server day to day
- `security/` — auth, encryption, privileges
- `ha-and-performance/` — replication, clustering, tuning
- `clients-and-utilities/` — bundled clients (`mysql`, `mysqldump`, etc.)
- `mariadb-quickstart-guides/` — task-oriented getting-started guides

**`release-notes/`** is partitioned by product: `community-server/`, `enterprise-server/`,
`maxscale/`, `columnstore/`, `galera-cluster/`, `connectors/`, `enterprise-operator/`,
`enterprise-manager/`, `mcp-server-release-notes/`, `ai-rag-release-notes/`,
`advanced-cluster/`.

**`connectors/`** has one directory per connector (`mariadb-connector-c/`,
`-cpp/`, `-j/`, `-net/`, `-nodejs/`, `-odbc/`, `-python/`, `-r2dbc/`) plus
`connectors-quickstart-guides/`.

## Working with `SUMMARY.md`

`SUMMARY.md` **is the published navigation** for its space (GitBook owns it). Rules:

- Add a new page to the right place in the tree when you create it, or it won't appear in nav.
- Match the existing list style exactly — `* [Title](path/to/page.md)` with two-space indents
  per nesting level. Look at neighboring entries before adding.
- Don't reorder or rename existing entries unless that's the actual task — it changes the live
  site structure and can conflict with GitBook-UI edits.
- Nav nesting is a **topical grouping** and need **not** match the file's directory location —
  entries under one nav section routinely link into unrelated directories. Match the indent of
  the sibling entries under your chosen parent, and link to the real file path. (GitBook derives
  the page URL from the file path, independent of nav position.)

## Moving or renaming a page

Per the GitBook Editing guide, **prefer doing this in the GitBook app** — it creates the
redirects and updates GitHub for you. The app **cannot move a page between spaces**, though.

When you must do it in **Git** (e.g. a cross-space move):

1. Change the page's **file path** (e.g. `server/x.md` → `platform/x.md`).
2. Update the **`SUMMARY.md` of every affected space** (both the source and destination space
   for a cross-space move), placing the entry in the correct section.
3. **Add a redirect** if the URL changes (renames/moves). Redirects are managed in the GitBook
   admin UI and only apply to pages that no longer exist at the old path.
4. **Don't rename pages in GitHub unless absolutely necessary** — renaming in the app is safer
   (it preserves GitBook's invisible page IDs and auto-creates redirects).

This is the territory a future `move-page` skill would automate; until then, do it carefully and
verify the redirect after.

## Finding a page

- Start from the space directory above, not a repo-wide grep.
- The page URL on mariadb.com/docs mirrors the file path within its space.
- For SQL/reference content, it's almost always under `server/reference/`.
