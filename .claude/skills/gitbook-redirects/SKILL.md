---
name: gitbook-redirects
description: Build a GitBook redirect CSV when mariadb-docs pages are renamed, moved, split, or retired. Use when the user asks to "create a redirects CSV", "make GitBook redirects", "set up redirects for moved/retired pages", or when a page-restructuring task removes or relocates published URLs. Produces the CSV; a GitBook site admin imports it manually (no API/MCP).
allowed-tools: Bash, Read, Grep, Glob, Write
owners: [shinz]
last_verified: 2026-07-06
status: active
---

# gitbook-redirects

Produce a **GitBook redirect CSV** so old URLs don't dead-end after pages are renamed, moved,
split, or retired. `mariadb-docs` has no in-repo redirect mechanism; GitBook redirects are
configured **manually** in the site UI (no API/MCP), so this skill's deliverable is the CSV — a
GitBook site admin imports it.

Full reference (read it): **`dev-docs/cookbook-gitbook-redirects.md`**. This skill is the
procedure; the cookbook is the canonical explanation.

## When to use

The user says: "create a redirects CSV", "make GitBook redirects", "redirect the old URLs",
"set up redirects for the pages we moved/retired". Also run it as a follow-up whenever a task
(often a `DOCS-XXXX` consolidation, split, or rename) removes or relocates published URLs — in
**addition** to repointing in-repo inbound links (lychee only catches in-repo breakage).

## Procedure

1. **Gather the old → new pairs.** From the task, the PR diff, or the user: every retired/moved
   page (its old path) and where it now lives (the surviving canonical page). Include retired
   **section/landing** pages too, pointed at the nearest surviving landing — not just leaf pages.
   For deletions, `git log --diff-filter=D --name-only` on the branch lists what was removed.

2. **Derive each path:**
   - old URL → **`source`**: a **site-relative path** with leading slash, including the space
     prefix, `.md` dropped, `README.md` → its directory. Server space = `/server/...`.
   - new page → **`destination`**: a **full absolute URL** — `https://mariadb.com/docs/server/<path>`.
   - Watch slug quirks: the on-disk basename is the slug (suffixes like `-1` carry through).

3. **Verify the base once.** Open one real canonical page in a browser (or confirm with the
   user) that its live URL matches the `https://mariadb.com/docs/server/...` you generated. If
   the host/base differs, it's a find-and-replace on the prefix.

4. **Write the CSV** to a working file outside the repo (e.g. the scratchpad — it is **not**
   committed):
   - Header **exactly** `source,destination`.
   - One row per retired page + section landing.

5. **Hand it off.** Tell the user to import it in GitBook → the site → **Settings → Redirects**
   (single redirect or CSV import). Note the two failure modes so they can self-diagnose:
   `Invalid destination URL` → a destination isn't a full URL; a header error → it isn't
   `source,destination`.

## Output shape

```csv
source,destination
/server/server-usage/basics/mariadb-usage-guide-1,https://mariadb.com/docs/server/mariadb-quickstart-guides/mariadb-usage-guide
```

## Guardrails

- **Do not** commit the CSV to the repo, and **do not** attempt the import yourself — there is
  no Git/API/MCP path; it's a manual GitBook UI action by a site admin.
- Still repoint in-repo inbound links to the retired pages separately (that's not what
  redirects cover).
