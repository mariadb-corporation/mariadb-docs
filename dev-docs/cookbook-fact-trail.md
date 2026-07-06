# Cookbook: the fact-check paper trail

Every source-verified documentation edit in this repo leaves a **fact-check report** — a
consistent, re-verifiable record of which doc claims are backed by which lines of MariaDB source.
The goal: a writer or developer in a **different session** (or on a different machine) can pick up
the report and confirm that every sentence in the docs is source-proven, without redoing the
analysis.

This page is the **single source of truth** for the report format and where it lives. The skills
that produce, post, and re-check it (`doc-impact`, `doc-from-ticket`, `bulk-campaign`, `jira`,
`verify-claims`) all defer here — don't re-spell the format in a SKILL.md.

## Two-part trail

1. **Local report (always).** A Markdown file written to a per-user reports directory **outside
   the git repo** — never committed. Produced/updated by `doc-impact` (skeleton) and
   `doc-from-ticket` (completed), aggregated by `bulk-campaign`.
2. **Jira copy (on handoff).** When the work is handed off for review (`/jira-resolve`), the
   report's contents are posted to the DOCS ticket as a Markdown **comment**, so reviewers and
   other writers see the same fact-check. A comment — not a file attachment — is deliberate: the
   `atlassian-mariadb` Rovo MCP **exposes no attachment endpoint** (its only issue-write tools are
   comment/worklog/field-edit/transition/link; attachments would need the REST
   `/issue/{key}/attachments` multipart endpoint + a separate API token, which the skills don't
   use). The comment is also better here — small Markdown that renders **inline**, is full-text
   searchable, and needs no download.

## Where reports live (config)

The reports directory is stored per-user in the gitignored
`.claude/doc-sources.local.json` (the same file `doc-from-ticket` uses for source repos):

```json
{
  "reports_dir": "/abs/path/outside/this/repo/mariadb-fact-checks",
  "sources": [
    { "product": "server", "path": "/abs/path/to/MariaDB-server", "ref": "main" }
  ]
}
```

**First-run prompt.** If `reports_dir` is missing, ask the user for an absolute path and validate
it before writing the config:

```bash
# must be absolute, and MUST NOT live inside this repo (reports are never committed)
repo_root="$(git rev-parse --show-toplevel)"
case "$(realpath -m "$candidate")/" in
  "$repo_root"/*) echo "REJECT: inside the repo — pick a directory outside it"; ;;
  *)              mkdir -p "$candidate" && echo "OK"; ;;
esac
```

Reject and re-prompt if the path resolves inside the repo. Create the directory if it doesn't
exist. Remember it silently on later runs; re-prompt only if the user says "reconfigure".

## Layout: grouped by space, one directory per ticket

Reports are **not** a flat pile of files. The tree is grouped by documentation **space** (mirroring
the 11 spaces a writer already navigates), with **one directory per ticket** so a ticket can hold
its report plus dated re-verification snapshots:

```
reports_dir/
  INDEX.md                          # regenerable browse table (see below)
  server/
    DOCS-1234/
      report.md                     # the canonical fact-check report
      runs/
        verify-2026-06-22.md        # optional: a verify-claims snapshot, append-only
  maxscale/
    DOCS-5678/
      report.md
  _unfiled/                         # triage before a space/DOCS key is known
    MDEV-9999/
      report.md
```

Rules:

- **Space** is the report's primary documentation space (`server`, `maxscale`, `connectors`, …).
  A ticket spanning several spaces files under its **primary** space and lists every page in the
  header; the INDEX row notes it's multi-space.
- **`report.md`** is the canonical report; `runs/verify-<YYYY-MM-DD>.md` holds optional
  `verify-claims` snapshots (an audit history).
- **Before a DOCS key or space is known** (pure triage from an MDEV/PR), write
  `_unfiled/MDEV-XXXXX/report.md`. When `doc-from-ticket` runs with the DOCS key and a known
  space, **move the directory** to `<space>/DOCS-XXXX/` (record the MDEV in the header). If triage
  already knows the space, write straight to `<space>/MDEV-XXXXX/` and rename to `DOCS-XXXX/`
  later.
- **Status is a header field, not a directory** — a report doesn't move when its status changes;
  it stays in its space. (Lifecycle below.)

### Deterministic lookup

A skill given only a key (`verify-claims`, `/jira-resolve`, `docs-check`) finds the report without
knowing its space:

```bash
report_dir="$(find "$reports_dir" -type d -name 'DOCS-1234' -not -path '*/runs/*' | head -1)"
report="$report_dir/report.md"        # empty result → no report yet
```

### INDEX.md (regenerable, never hand-maintained)

`INDEX.md` is a generated browse table — regenerate it by scanning report headers whenever a
report is written or its status changes (it's cheap and always-accurate, so never goes stale):

```bash
# one row per report; reads the header table of each report.md
{ echo '| Key | Space | Page(s) | Status | Updated | Verdicts |'
  echo '|-----|-------|---------|--------|---------|----------|'
  find "$reports_dir" -name report.md -not -path '*/runs/*' | sort | while read -r r; do
    # extract Key/Space/Page(s)/Status/Generated from the header and a VERIFIED/UNVERIFIED tally
    : # (skill fills these from the parsed header + claim verdict counts)
  done
} > "$reports_dir/INDEX.md"
```

The skill fills each row from the report's parsed header and a count of claim verdicts. INDEX is a
convenience for humans browsing; the reports themselves remain the source of truth.

## The format

```markdown
# Fact-check report — DOCS-1234

| Field | Value |
|-------|-------|
| DOCS ticket | DOCS-1234 |
| MDEV | MDEV-9999 |
| Release Series | 13.1 |
| Doc page(s) | server/reference/system-variables/foo.md |
| Source | server @ a1b2c3d4 (ref main) |
| Generated | 2026-06-22 by doc-from-ticket |
| Status | drafted |

## Claims

| # | Claim (as documented) | Doc location | Source evidence | Verdict |
|---|-----------------------|--------------|-----------------|---------|
| 1 | Default of `foo_buffer` is 16M | foo.md:42 | server sql/sys_vars.cc:1234 @ a1b2c3d4 | VERIFIED |
| 2 | `FOO` syntax exists since 13.1 | foo.md:55 | server sql/sql_yacc.yy:9876 @ a1b2c3d4 | VERIFIED |
| 3 | foo is dynamic, GLOBAL scope | foo.md:60 | — | UNVERIFIED |
```

Rules for the table:

- **Claim** — the factual assertion *as it reads in the docs* (a default, a scope, a "since
  version X", a behavior). One row per checkable claim; skip pure prose.
- **Doc location** — `file:line` in this repo where the claim appears (relative to repo root or
  the page filename — be consistent within a report). `—` until a page is drafted.
- **Source evidence** — `<product> <path>:<line> @ <pinned-SHA>`. The **pinned commit SHA** is
  mandatory; a branch name alone is not re-verifiable. `—` when there is no source backing.
- **Verdict** — one of:
  | Verdict | Meaning |
  |---------|---------|
  | `VERIFIED` | Source at the pinned SHA confirms the claim as documented. |
  | `CORRECTED` | Source contradicted the ticket/draft; the doc was changed to match source (note the correction). |
  | `UNVERIFIED` | Could not confirm against source — flagged in the doc with `<!-- TODO: confirm against source -->`, never asserted as fact. |
  | `PENDING` | Triage-only (set by `doc-impact`): a claim to verify, not yet checked or drafted. |

- **Status** (header): `triaged` (doc-impact skeleton) → `drafted` (doc-from-ticket completed) →
  `handed-off` (posted to Jira on `/jira-resolve`).

## Lifecycle

```
/impact MDEV-9999      → _unfiled/MDEV-9999/report.md      (PENDING rows, status: triaged)
                          (or server/MDEV-9999/report.md if the space is already clear)
/jira-create           → DOCS-1234 exists
/doc-ticket DOCS-1234  → moves dir → server/DOCS-1234/report.md; fills doc:line, source@SHA,
                          verdicts (status: drafted); regenerates INDEX.md
/jira-resolve DOCS-1234→ posts report.md as a Jira comment (status: handed-off); regen INDEX
/verify-claims DOCS-1234 (any later session) → re-checks each row against source at the SHA,
                          writes server/DOCS-1234/runs/verify-<date>.md
```

## Re-verification (`verify-claims`)

A later session re-checks a report without the original context: for each row it confirms (a) the
**source evidence** still says what the report claims, at the recorded SHA *and* at the current
ref (to surface drift), and (b) the **doc location** still contains the claim. It reports per row:
`STILL-VERIFIED` / `DRIFTED` (source changed since the SHA) / `SOURCE-MOVED` (file/line gone) /
`DOC-CHANGED` (the doc no longer matches). It writes its run to
`<space>/<KEY>/runs/verify-<YYYY-MM-DD>.md` as an audit snapshot but never edits the report or the
docs — it's an audit.

## Guardrails

- The report is **local-only and never committed.** It lives outside the repo; the Jira comment is
  the shared/durable copy.
- Every `VERIFIED`/`CORRECTED` row **must** carry a pinned source SHA. No SHA → it's `UNVERIFIED`.
- Don't fabricate rows to look thorough — an honest `UNVERIFIED`/`PENDING` is the point.
</content>
</invoke>
