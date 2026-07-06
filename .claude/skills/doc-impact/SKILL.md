---
name: doc-impact
description: Analyze a MariaDB source change for its documentation impact — the "explain" step before drafting. Given an MDEV ticket, a DOCS ticket, or a MariaDB/server PR/commit, it reads the actual code change, determines what is user-facing, whether docs are needed and which pages, and lists the claims to verify. Produces an analysis report; it does NOT edit docs (hand off to doc-from-ticket / /doc-ticket for that). Use when asked to "explain the doc impact of X", "what docs does MDEV-XXXXX need", "analyze this PR for documentation", or to triage whether a change needs docs.
allowed-tools: Bash, Read, Grep, Glob, Write, WebFetch, mcp__atlassian-mariadb__getJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# doc-impact

The **discovery / triage** half of the doc pipeline: read a source change and report its
**documentation impact** — what a user would observe, whether docs are needed, which page(s) are
affected, and the specific claims a writer must verify. This is the MariaDB analog of GridGain's
`/explain`: it produces an **analysis, not an edit**. Drafting is `doc-from-ticket`'s job
(`/doc-ticket`), which can consume this report.

Source access reuses `doc-from-ticket`'s config — the local MariaDB repos in
`.claude/doc-sources.local.json` (gitignored). If it's absent, configure it the same way
`doc-from-ticket` §0 describes (prompt for product → path → authoritative ref), then continue.

**Paper trail.** This skill also writes the **fact-check report skeleton** (§4 below) — the
triage half of the two-part paper trail described in `dev-docs/cookbook-fact-trail.md`. That
report needs a `reports_dir` (a directory **outside this repo** where reports are stored, never
committed), also kept in `.claude/doc-sources.local.json`. If `reports_dir` is missing, prompt and
validate it per the cookbook's *Where reports live* section before writing.

## When to use

"Explain the doc impact of MDEV-XXXXX / this PR", "what docs does this change need?", "does
MDEV-XXXXX need documentation?", "triage this for docs". Run it **before** drafting — or before
even deciding to draft.

## 0. Resolve the input

Accept any of:

- **`DOCS-XXXX`** → `getJiraIssue` (server `atlassian-mariadb`, cloudId `164b0d33-…`). Parse
  **whatever is present** — the **PR link** is the reliable field; an **MDEV key** and a
  **Release Series** are *often* there but **not guaranteed** (and the MDEV id frequently appears
  only **inside the diff**, not in the ticket fields). Don't invent a Release Series you can't
  find.
- **`MDEV-XXXXX`** → the upstream change on the **public** `jira.mariadb.org` (a *different* Jira,
  not our MCP). `WebFetch https://jira.mariadb.org/browse/MDEV-XXXXX` for summary, description,
  **Fix Version**, and linked commits/PR.
- **A `github.com/MariaDB/server` PR or a commit ref** → analyze its diff directly.

Run the `jira` skill's connection check only if you need `getJiraIssue` (DOCS input).

## 1. Get the actual change (source is the source of truth)

The ticket text states *intent*; the **code change** states what shipped. Get the diff:

```bash
# from the configured local source repo, read-only
git -C <repo.path> fetch --quiet
# find the commit(s) that INTRODUCED the change — by MDEV id or the PR merge — and pin THAT
git -C <repo.path> log --oneline <repo.ref> --grep="MDEV-XXXXX"
change_sha="<the commit you'll analyze>"
git -C <repo.path> show "$change_sha"                   # the change itself
```

**Pin the change's commit SHA** (`change_sha`), not the branch-ref head — every "claim to
verify" you cite must point at the commit that introduced the change, so a writer (or
`doc-from-ticket`) can re-check the exact same source.

**If the change isn't in the local repo yet** (or no source is configured), fall back to the PR
diff and say you're reading the PR, not local source. Note: `github.com/MariaDB/server/pull/N.diff`
**302-redirects** to `https://patch-diff.githubusercontent.com/raw/MariaDB/server/pull/N.diff`,
and WebFetch does **not** auto-follow cross-host redirects — so issue the WebFetch against that
`patch-diff.githubusercontent.com/raw/...` URL directly (the redirect target serves the unified
diff).

## 2. Classify the user-facing surface

Scan the diff for what a user can observe (skip pure internals — refactors, tests, comments):

| Surface | Where it shows in the diff |
|---------|----------------------------|
| System/status variable (name, **default**, scope, dynamic/read-only) | `sql/sys_vars.cc`, `sql/mysqld.cc` |
| SQL syntax / grammar | `sql/sql_yacc.yy`, `sql/lex.h` |
| Startup option / flag | `sql/sys_vars.cc`, `*/handler.cc` |
| Error code / message | `sql/share/errmsg-utf8.txt` |
| New/changed function, default change, behavior change, deprecation/removal | the touched component |

For each, note what changed (old → new) and the **version** (Release Series / Fix Version).

## 3. Determine documentation impact

Decide and state plainly:

- **Docs needed? YES / NO / MAYBE.** An internal-only change (refactor, test, perf with no
  observable change) is **NO** — say so; don't manufacture work.
- **What kind:** new variable → reference table; new behavior → note on the existing topic; new
  syntax → reference page; breaking change → migration note + warning; deprecation/removal →
  note (+ the version policy).
- **Which page(s):** grep the docs for the symbols to find where it's already covered:
  ```bash
  docs_root="$(git rev-parse --show-toplevel)"
  grep -rn "<variable-or-keyword>" "$docs_root/server/" --include=*.md
  ```
  Name the existing page to edit, or flag that a **new page** is warranted (which needs a
  `SUMMARY.md` entry — `new-page`'s job).
- **Forward-looking check:** if the change is planned-but-unreleased (Fix Version set, not yet
  shipped), flag it — per the style guide, forward-looking statements are avoided unless backed
  by exactly such a ticket. Note the version gating.

## 4. Write the fact-check report skeleton (paper trail)

Persist the triage as a report so the drafting step (and a later session) can build on it. Format,
location, and naming are defined once in `dev-docs/cookbook-fact-trail.md` — follow it; don't
re-spell the format here.

- Ensure `reports_dir` is configured (prompt + validate per the cookbook if missing).
- Path follows the cookbook's space-grouped layout: `<reports_dir>/<space>/<KEY>/report.md`. Use
  the affected space + **DOCS** key when both are known; if the space isn't settled yet, write
  `<reports_dir>/_unfiled/MDEV-XXXXX/report.md` (or `<space>/MDEV-XXXXX/report.md`) —
  `doc-from-ticket` moves/renames it to the DOCS key later.
- Write the header (DOCS/MDEV/Release Series/affected page(s)/source `@ change_sha`/`Status:
  triaged`) and one **`PENDING`** claim row per "claim to verify" — claim text + the source
  pointer you found (`<product> <file>:<line> @ <change_sha>`), **Doc location** left as `—`
  (no page drafted yet).
- If a report for this key already exists (find it per the cookbook's lookup), update it in place
  rather than clobbering it.
- If the triage concluded **NO docs needed**, still write a minimal report stating that (status
  `triaged`, no claim rows, a one-line "no user-facing change" note) so the decision is recorded.
- Regenerate `INDEX.md` (cookbook) after writing.

Tell the user the report path in the output below.

## 5. Output: the impact report

```
Doc-impact — MDEV-XXXXX  (DOCS-XXXX if known) — <summary>
Source:     MariaDB/server @ <change-sha>   (Release Series / Fix Version <…>, if known)

User-facing change:
  - <what the user observes; old → new>

Docs needed?  YES | NO | MAYBE
  Why: <one line>

Affected page(s):
  - <server/reference/.../foo.md>   — existing; <add table row / note>
  - (or) new page under <path>      — needs SUMMARY.md entry (use new-page)

Claims to verify (hand to /doc-ticket):
  - <default of `x` is `N`>          — sql/sys_vars.cc:<line> @ <change-sha>
  - <syntax `…` exists since <X.Y>>

Recommendation: edit <page> | new page | NO docs needed | needs human triage
Report:   <reports_dir>/<space>/<DOCS-XXXX>/report.md   (or _unfiled/MDEV-XXXXX/; skeleton, triaged)
Next: /doc-ticket DOCS-XXXX   (or /jira-create to file the DOCS ticket first, then /doc-ticket)
```

## Guardrails

- **Analysis only — never edit, stage, commit, push, or open a PR.** This skill reports; it
  hands drafting to `doc-from-ticket` / `/doc-ticket`. The **one** thing it writes is the
  fact-check report in `reports_dir` (§4) — a file **outside the repo**, never a repo/doc file.
- **Source is read-only** (`git -C <repo> show/log/grep`, never checkout); Jira/MDEV reads are
  read-only.
- **Don't assert beyond the diff.** If the code doesn't show it, say "unverified" — the ticket's
  prose may describe a *request*, not what shipped.
- **"No docs needed" is a valid, useful answer** for internal-only changes — state it rather
  than inventing a doc task.
- One change at a time; scope grep to the relevant space/path.
