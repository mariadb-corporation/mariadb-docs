---
description: Build a GitBook redirect CSV for renamed/moved/retired mariadb-docs pages (header source,destination; destination = full URL).
argument-hint: "(optional) the retired→canonical pairs, a DOCS ticket / PR, or the paths that moved"
allowed-tools: Bash, Read, Grep, Glob, Write
---

# /redirects-csv

Run the **`gitbook-redirects`** skill (`.claude/skills/gitbook-redirects/SKILL.md`) for
`$ARGUMENTS`. Full reference: `dev-docs/cookbook-gitbook-redirects.md`.

In short (full procedure + gotchas in the skill and cookbook):
1. Gather the old→new pairs from `$ARGUMENTS` (or the current branch's deletions/renames),
   including retired section/landing pages.
2. Build the CSV: header **`source,destination`**; `source` = site-relative path
   (`/server/...`, no `.md`, `README`→dir); `destination` = **full URL**
   (`https://mariadb.com/docs/server/...`). Verify the base against one live page.
3. Write it to the scratchpad (never commit it) and hand it to a GitBook site admin to import
   (Settings → Redirects). It cannot be applied via Git/API/MCP.

Arguments: $ARGUMENTS
