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
| Tools | `tools/` | Enterprise Manager, MCP server, Kubernetes Operator, AI-RAG |
| General Resources | `general-resources/` | About, community, style guide, legal, theory |
| Galera Cluster | `galera-cluster/` | Galera synchronous replication |
| Help Tables | `help-tables/` | **Generated** SQL `HELP` tables (do not hand-edit) |
| Home | `home/` | Portal / landing |

(11 browsable spaces + the generated `help-tables/`.)

## Non-space directories

Top-level directories that look like content but are **not** browsable spaces:

| Path | What it is |
|------|------------|
| `mariadb-platform/` | GitBook **includes** container (`.gitbook/includes/`, ~16 reusable "most-recent release" snippets). Holds include files, not pages, so it has no `README.md` or `SUMMARY.md`. Add a new **include file** here when the work requires one; don't author standalone pages. |
| `.gitbook/includes/` | Repo-level reusable snippets inserted into pages by GitBook. |
| `dev-docs/` | Agent/contributor playbooks (not published). |
| `.claude/` | Shared Claude Code config, skills, hooks (not published). |

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
`enterprise-manager-release-notes/`, `mcp-server-release-notes/`, `ai-rag-release-notes/`,
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
