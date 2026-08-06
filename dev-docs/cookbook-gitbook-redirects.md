# Cookbook: GitBook redirects

`mariadb-docs` has **no in-repo redirect mechanism** — there is no `.gitbook.yaml` or
redirects file that Git controls. When you rename, move, split, or consolidate pages, the old
URLs die and external bookmarks / search-engine results dead-end.

GitBook itself **does** support redirects, configured two ways:

- **The GitBook site UI** — one rule at a time, or a CSV import. This is the normal path, and the
  repo-side job for it is to **produce a redirect CSV** and hand it to whoever administers the
  GitBook site.
- **The GitBook API**, reachable through the `gitbook-api` MCP server: `listSiteRedirects`,
  `getSiteRedirectBySource`, `createSiteRedirect`, `updateSiteRedirectById`,
  `bulkUpsertSiteRedirects`. Useful for bulk loads and, above all, for **verifying** what is
  actually configured — see [Troubleshooting](#troubleshooting-a-redirect-that-looks-broken).

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

## Troubleshooting a redirect that looks broken

A redirect that misbehaves in a browser is usually **not** a broken GitBook rule.
`mariadb.com/docs` sits behind Cloudflare, and Cloudflare answers some requests itself — GitBook
never sees them. So before concluding anything, establish **which layer answered**.

### Step 1: Find out who answered

Request both slash forms and look for `x-gitbook-*` response headers:

```bash
curl -s -o /dev/null -D - "https://mariadb.com/docs/<path>"   # no trailing slash
curl -s -o /dev/null -D - "https://mariadb.com/docs/<path>/"  # trailing slash
```

| `x-gitbook-*` headers | Who answered |
|-----------------------|--------------|
| present | **GitBook** — the redirect config is in play; continue to step 2 |
| absent | **Cloudflare** — the request never reached GitBook; nothing you configure in GitBook can affect it |

The two forms routinely disagree, so check both. Add `?cb=$RANDOM` to bypass edge caching, and use
`curl -D - -L` to see the **whole hop chain** — the first hop is the one that matters.

### Step 2: Find out whether the rule is stored

Don't infer this from the live URL. Ask the API:

- `getSiteRedirectBySource` (`GET /orgs/{org}/sites/{site}/redirect?source=<site-relative-path>`)
  returns the rule and its resolved `target`.
- `listSiteRedirects` with `search=<slug>` finds rules by path.

If the rule is present, `draft: false`, with the right destination, but the live URL goes somewhere
else — the rule is fine and something in front of GitBook is intercepting it.

### Two failure modes that look like GitBook bugs but are Cloudflare's

Both were misdiagnosed on DOCS-6370 before the header check was applied:

- **Self-redirect loop.** The no-slash form 301s to *the identical URL* — `ERR_TOO_MANY_REDIRECTS`,
  no error page, just a hang. Worse than a 404 for readers, and invisible to link checkers.
- **Silent wrong page.** The no-slash form 301s to a *different* page's old slug; GitBook then
  faithfully resolves that wrong slug, so the reader gets **HTTP 200 on the wrong page**. No link
  checker will ever flag this.

In both cases the trailing-slash form 307s to the correct target, because the GitBook rule was
always right. **The fix is to remove the Cloudflare rule** (an IT request) — adding or editing a
GitBook rule cannot win a race it never enters.

Two corollaries worth remembering:

- **Don't measure whether an import "took" using the no-slash form.** DOCS-6370 concluded that 10 of
  18 imported rows had silently failed. All 18 had applied; the 10 were simply unobservable behind
  Cloudflare.
- **A `site-page` destination is not a workaround.** Switching a rule's destination from
  `external` (absolute URL) to `site-page` (internal page reference) changes nothing here. Tested
  and reverted on DOCS-6370 — don't spend time on it again.

## Checklist

- [ ] In-repo inbound links to the old paths already repointed (separate from redirects).
- [ ] CSV header is `source,destination`.
- [ ] `source` = site-relative path (`/server/…`, no `.md`, README→dir).
- [ ] `destination` = full `https://mariadb.com/docs/server/…` URL.
- [ ] Base URL verified against one real live page.
- [ ] A row for every retired page **and** every retired section landing.
- [ ] Handed to a GitBook site admin to import (or loaded via the API — but not via Git).
- [ ] **Re-probed every row after import**, on **both** slash forms, checking `x-gitbook-*` to see
      which layer answered. A CSV import reports no error for a row that ends up unobservable.
