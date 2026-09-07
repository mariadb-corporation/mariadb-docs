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
  **Requires `admin` on the site**, which the organization's default `create` role does not
  grant — so for most writers the CSV above is the only route, and that is by design.

## When to produce a redirect CSV

Any change that removes or relocates a published URL:

- page renames or slug changes,
- moving a page to a different section,
- splitting one page into several,
- retiring duplicate pages / consolidating trees (e.g. DOCS-6312).

Do this **in addition to** rewriting in-repo inbound links — lychee only catches in-repo
breakage, never external bookmarks.

## What happens when you rename a published page

Three GitBook behaviors decide whether a rename needs redirects at all, and none of them is
what you would guess. All three were established on DOCS-6408, which renamed three published
`platform/post-download/` pages.

**A real page outranks a rule with the same source.** GitBook resolves an existing page first
and falls through to a redirect rule only when nothing resolves. A rule whose source matches a
live page therefore never fires, and a rename cannot be "shadowed" by one. DOCS-6408 predicted
the opposite in its PR body, and the live site disproved it: all three renamed pages returned
200 as soon as Git Sync landed, though two rules were sourced from exactly those paths.

**Git Sync preserves a page's id across a rename.** A rule's destination is a page id, not a
path (`destination.kind: site-page`), so a rule pointing at a renamed page silently follows it
to the new URL. That is convenient in the common direction — but a rule *sourced from* the new
canonical path becomes a **self-redirect**, its source and resolved target identical. That is
the loop described in [Troubleshooting](#troubleshooting-a-redirect-that-looks-broken), and
renaming a page is one of the ways to create one. It stays latent for as long as the page keeps
winning, which is exactly why nothing looks wrong at the time.

**The old URL keeps working without a rule.** GitBook adds an automatic slug-history alias, so
the pre-rename URL 307s to the new one on its own. On DOCS-6408 two of the three old URLs
redirected correctly with no stored rule at all, and the prepared CSV turned out to have nothing
left to import. An alias is weaker than a stored rule, though — it is GitBook's bookkeeping
rather than your configuration — so it is worth having explicit rules stored for URLs that
matter.

### What to do after a rename

**Step 1 is for everyone; steps 2–4 assume site admin.** Redirect rules are site settings, and
the organization's default `create` role does not grant `admin` on a site — so expect a 403 on
the API calls below unless you hold it. (Writes certainly need it; whether a plain read does was
not tested, so don't count on it.) That is why the `gitbook-redirects` skill's deliverable is a
CSV handed to an admin, and why the two are not in conflict: the CSV is the non-admin route to
the same outcome.

1. **Probe the old URLs before preparing anything.** No permissions needed — `curl` the old paths
   as in [Step 1](#step-1-find-out-who-answered) above. The aliases may already do the job, in
   which case the deliverable is nothing. If they don't, produce the CSV and hand it over; an
   admin can then run the rest.
2. **Audit rules sourced from the new canonical path**, not only from the old one. The old path
   is the obvious half; the new path is where a self-redirect hides. `listSiteRedirects` with
   `search=<slug>` covers both in one call.
3. **Delete any self-redirect the rename created.** There is no single-rule delete operation:
   use `bulkUpsertSiteRedirects` with `destination` set to `null` for that source, which can
   create the replacement rules in the same call.
4. **Mind the order.** Delete rules sourced from the canonical path only *after* Git Sync has
   published the rename — until then, those rules are what keeps the old URL alive.

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
  Cloudflare is not the only way to get one: see
  [What happens when you rename a published page](#what-happens-when-you-rename-a-published-page).
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
- [ ] For a rename: old URLs probed **before** preparing a CSV — GitBook's slug-history alias may
      already cover them, leaving nothing to import.
- [ ] For a rename: rules sourced from the **new** canonical path audited, and any self-redirect
      the rename created deleted (after Git Sync publishes, not before).
- [ ] CSV header is `source,destination`.
- [ ] `source` = site-relative path (`/server/…`, no `.md`, README→dir).
- [ ] `destination` = full `https://mariadb.com/docs/server/…` URL.
- [ ] Base URL verified against one real live page.
- [ ] A row for every retired page **and** every retired section landing.
- [ ] Handed to a GitBook site admin to import (or loaded via the API — but not via Git).
- [ ] **Re-probed every row after import**, on **both** slash forms, checking `x-gitbook-*` to see
      which layer answered. A CSV import reports no error for a row that ends up unobservable.
