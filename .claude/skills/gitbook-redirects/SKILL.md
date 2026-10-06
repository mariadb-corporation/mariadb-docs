---
name: gitbook-redirects
description: Add GitBook redirects when mariadb-docs pages are renamed, moved, split, or retired. Use when the user asks to "create a redirects CSV", "make GitBook redirects", "set up redirects for moved/retired pages", or when a page-restructuring task removes or relocates published URLs. With site admin, loads the rules through the gitbook-api MCP server (draft, check, publish); without it, produces a CSV for a site admin to import.
allowed-tools: Bash, Read, Grep, Glob, Write
owners: [shinz]
last_verified: 2026-09-30
status: active
---

# gitbook-redirects

Add **GitBook redirects** so old URLs don't dead-end after pages are renamed, moved, split, or
retired. `mariadb-docs` has no in-repo redirect mechanism: redirects are GitBook site settings,
not files in Git. There are two ways to set them, and which one you use depends on one
permission:

- **Site admin → the GitBook API**, through the `gitbook-api` MCP server. You load, check, and
  publish the rules yourself.
- **No site admin → a CSV** that a GitBook site admin imports in the site UI. The
  organization's default `create` role does not grant admin, so this is the route for most
  writers, by design.

Full reference (read it): **`dev-docs/cookbook-gitbook-redirects.md`**. This skill is the
procedure; the cookbook is the canonical explanation, including why a redirect that looks broken
is usually Cloudflare, not GitBook.

## When to use

The user says: "create a redirects CSV", "make GitBook redirects", "redirect the old URLs",
"set up redirects for the pages we moved/retired". Also run it as a follow-up whenever a task
(often a `DOCS-XXXX` consolidation, split, or rename) removes or relocates published URLs — in
**addition** to repointing in-repo inbound links (lychee only catches in-repo breakage).

**Timing:** redirects go in **after** the PR that removes the pages has merged and Git Sync has
published it. Until then the old page still resolves, and a real page always outranks a rule
with the same source, so a rule loaded early is untestable.

## Procedure

1. **Gather the old → new pairs.** From the task, the PR diff, or the user: every retired/moved
   page (its old path) and where it now lives (the surviving canonical page). Include retired
   **section/landing** pages too, pointed at the nearest surviving landing — not just leaf pages.
   For deletions, `git log --diff-filter=D --name-only` on the branch lists what was removed.

2. **Derive each path.** A page's URL is its position in the space's `SUMMARY.md`, not its file
   path. The two usually agree, but check the `SUMMARY.md` entry.
   - old URL → **`source`**: a **site-relative path** with leading slash, including the space
     prefix, `.md` dropped, `README.md` → its directory. Server space = `/server/...`.
   - new page → **destination**. For the API, a space-relative path (step 4). For the CSV, a
     **full absolute URL**: `https://mariadb.com/docs/server/<path>`.
   - Watch slug quirks: the on-disk basename is the slug (suffixes like `-1` carry through).

3. **Probe before and check permissions.**
   - `curl` the destinations, which must return 200. For a rename, also `curl` the old URLs:
     GitBook's slug-history alias may already redirect them (see the cookbook).
   - Check admin with **`listOrganizationsForAuthenticatedUser`** (`GET /orgs`) →
     `items[0].permissions.admin`. Reads such as `listSiteRedirects` keep working without admin;
     only writes fail, with "You must have admin permission", so check first. If it's `false`,
     go to step 5.

4. **API route (admin).** Organization `MariaDB` and site `MariaDB Documentation`; get the
   ids and each space's id from `list_sites` / `get_site_structure`.
   - **Check for existing rules** on every source *and* every destination path:
     `listSiteRedirects` with `search=<slug>`, or `getSiteRedirectBySource`. A rule sourced from
     a destination path is a latent self-redirect (see the cookbook).
   - **Stage as drafts** with `bulkUpsertSiteRedirects` (PUT, up to 500 per call). Use
     `intent: "draft"` and a path destination, which GitBook resolves to the page for you:
     ```json
     {"redirects": [{"source": "/server/<old-path>", "intent": "draft",
       "destination": {"kind": "path", "spaceId": "<space id>", "path": "<new-path>"}}]}
     ```
     Read the per-item status in the response. A draft rule does not affect the live site.
   - **Publish** with a second call: `{"source": "/server/<old-path>", "intent": "publish"}`
     for each rule.
   - **Delete** a rule with `destination: null`. There is no single-rule delete operation.

5. **CSV route (no admin).** Write the CSV to a working file outside the repo (e.g. the
   scratchpad; it is **not** committed):
   - Header **exactly** `source,destination`.
   - One row per retired page and section landing, with absolute destination URLs.
   - Verify the base once: one real canonical page's live URL must match the
     `https://mariadb.com/docs/server/...` you generated.
   - Hand it off: GitBook → the site → **Settings → Redirects** → **Import**. A CSV import goes
     live immediately; there is no draft stage. The two errors: `Invalid destination URL` → a
     destination isn't a full URL; a header error → it isn't `source,destination`.

6. **Re-probe every rule after it is live**, on **both** slash forms, with `curl -s -o /dev/null
   -D - -L` plus `?cb=$RANDOM`, and look for `x-gitbook-*` headers to see which layer answered.
   Neither route reports a rule that ends up unobservable behind Cloudflare.

## Output shape (CSV route)

```csv
source,destination
/server/server-usage/basics/mariadb-usage-guide-1,https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-usage-guide
```

## Guardrails

- **Never** commit the CSV, and never put redirects in Git. There is no Git path.
- **Load redirects only after the removing PR has merged and synced.** Publishing is a live-site
  change: say what you're about to publish before the publish call.
- Still repoint in-repo inbound links to the retired pages separately (that's not what
  redirects cover).
