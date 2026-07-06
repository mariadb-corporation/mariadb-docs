# Cookbook: GitBook redirects

`mariadb-docs` has **no in-repo redirect mechanism** — there is no `.gitbook.yaml` or
redirects file that Git controls. When you rename, move, split, or consolidate pages, the old
URLs die and external bookmarks / search-engine results dead-end.

GitBook itself **does** support redirects, but they are configured **manually** in the GitBook
site UI (there is no API or MCP for it). So the repo-side job is to **produce a redirect CSV**
and hand it to whoever administers the GitBook site; they import it.

## When to produce a redirect CSV

Any change that removes or relocates a published URL:

- page renames or slug changes,
- moving a page to a different section,
- splitting one page into several,
- retiring duplicate pages / consolidating trees (e.g. DOCS-6312).

Do this **in addition to** rewriting in-repo inbound links — lychee only catches in-repo
breakage, never external bookmarks.

## The CSV format (this is the part that trips people up)

| Column | What GitBook wants | Example |
|--------|--------------------|---------|
| header row | **exactly** `source,destination` | `source,destination` |
| `source` | the **old** URL as a **site-relative path**, leading slash, including the space prefix; no `.md` | `/server/server-usage/basics/mariadb-usage-guide-1` |
| `destination` | the **new** location as a **full absolute URL** | `https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-usage-guide` |

Two mistakes cause almost every import failure:

1. **Wrong header.** GitBook rejects `from,to`. It must be `source,destination`.
2. **Bare path in `destination`.** A site-relative path in the destination column fails with
   **`Invalid destination URL`** for every row. The destination must be a **full `https://…`
   URL**, even though the source is a path. (The source is a dead path by definition, so
   GitBook doesn't validate it; the destination it *does* validate as a real URL.)

### Deriving the paths

A published URL maps from the file path like this:

- drop the `.md` extension,
- `README.md` → its directory,
- the site path is `/<space>/<path-from-space-root>` — for the server space that is
  `/server/...` (the docs site mounts each space under its slug: `/server`, `/galera`,
  `/maxscale`, …),
- the public base is `https://mariadb.com/docs`, so a full URL is
  `https://mariadb.com/docs/server/<path>`.

**Sanity-check the base once:** open the real, current canonical page in a browser and confirm
its URL matches what you generated. If the host/base differs, it's a find-and-replace on the
prefix and the rest holds.

Watch for slug quirks — the on-disk basename is the slug, so suffix oddities carry through
(e.g. in DOCS-6312 the surviving `adding-and-changing-data` and `alter-table` pages kept a `-1`
suffix while their retired twins did not).

## Worked example (DOCS-6312)

Consolidating the two quickstart-guide trees retired 16 `server-usage/` URLs in favor of
`mariadb-quickstart-guides/`. The delivered CSV:

```csv
source,destination
/server/server-usage/basics/mariadb-usage-guide-1,https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-usage-guide
/server/server-usage/tables/mariadb-indexes-guide-1,https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-indexes-guide
/server/server-usage/data-handling/mariadb-adding-and-changing-data-guide,https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-adding-and-changing-data-guide-1
```

Include a row for each retired **section/landing** too (point it at the nearest surviving
landing), not just the leaf pages.

## Importing (the manual step)

The person with GitBook site admin access does this — it is not a Git operation:

1. GitBook → the site → **Settings → Redirects**.
2. Add a single redirect, or **Import** the CSV.
3. If rows error, read the message: `Invalid destination URL` → destination isn't a full URL;
   a header error → it isn't `source,destination`.

## Checklist

- [ ] In-repo inbound links to the old paths already repointed (separate from redirects).
- [ ] CSV header is `source,destination`.
- [ ] `source` = site-relative path (`/server/…`, no `.md`, README→dir).
- [ ] `destination` = full `https://mariadb.com/docs/server/…` URL.
- [ ] Base URL verified against one real live page.
- [ ] A row for every retired page **and** every retired section landing.
- [ ] Handed to a GitBook site admin to import (you can't do it via Git/API/MCP).
