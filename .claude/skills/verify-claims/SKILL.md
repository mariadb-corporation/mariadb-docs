---
name: verify-claims
description: Re-verify a fact-check report against MariaDB source in a later session — confirm each documented claim is still source-proven. Use when asked to "verify the claims", "re-check the fact-check report", "audit DOCS-XXXX's claims", or before approving/merging a doc PR a different writer drafted. Reads the local report, re-checks each claim against source at the recorded SHA (and the current ref, to surface drift), and reports per-claim status. Read-only — never edits docs, source, or the report.
allowed-tools: Bash, Read, Grep, Glob, Write, WebFetch
owners: [igusev]
last_verified: 2026-06-22
status: active
---

# verify-claims

The **consuming** end of the fact-check paper trail (`dev-docs/cookbook-fact-trail.md`). Given a
report produced by `doc-impact` / `doc-from-ticket` / `bulk-campaign`, re-prove every claim from
scratch — so a developer or another writer, in a **different session** and without the original
context, can trust that the documentation is source-backed (or see exactly what drifted).

This is an **audit, not an edit.** It never changes docs, source, or the report; it produces a
verdict per claim and a summary.

## When to use

"Verify the claims for DOCS-XXXX", "re-check the fact-check report", "audit this page's claims
against source", "is DOCS-XXXX still source-proven?", or as a reviewer's pre-merge gate on a doc
PR someone else drafted.

## 0. Config (same as doc-from-ticket)

Read `.claude/doc-sources.local.json` (gitignored) for **`reports_dir`** and the **`sources`**
(local MariaDB repos + refs). If either is missing, prompt and validate per
`dev-docs/cookbook-fact-trail.md` › *Where reports live* and `doc-from-ticket` §0. Source repos
are read **read-only** (`git -C <path> show/log/grep`, never checkout).

## 1. Locate the report

Accept a `DOCS-XXXX` / `MDEV-XXXXX` key or an explicit report path.

- Key → find it in the space-grouped tree (`dev-docs/cookbook-fact-trail.md`):
  ```bash
  report="$(find "$reports_dir" -type d -name '<KEY>' -not -path '*/runs/*' | head -1)/report.md"
  ```
  If absent, say so and stop (nothing to verify — suggest `/doc-ticket` to generate one). Don't
  reconstruct a report from the docs.
- Parse the header (DOCS/MDEV, source `product @ sha`, doc page(s)) and the **Claims** table.

## 2. Re-check each claim

For every row, independently confirm both halves — don't trust the recorded verdict:

1. **Source evidence holds at the recorded SHA.** Read the cited `<product> <file>:<line> @ <sha>`
   from the configured source repo and confirm it still says what the claim asserts:
   ```bash
   git -C <source.path> show <sha>:<file> | sed -n '<line-context>p'
   # or, if the line moved within that commit, re-grep the symbol at that SHA:
   git -C <source.path> grep -n "<symbol>" <sha> -- '<path-glob>'
   ```
2. **Drift check against the current ref.** Re-resolve the same fact at the configured ref's head
   (`git -C <source.path> rev-parse <ref>`) and compare — has the default/scope/syntax changed
   since the report's SHA?
3. **Doc still matches.** Confirm the repo's `Doc location` (`file:line`) still contains the
   claim as written (the page may have been edited since the report).

Assign one status per row:

| Status | Meaning |
|--------|---------|
| `STILL-VERIFIED` | Source at the SHA confirms it, current ref agrees, doc still matches. |
| `DRIFTED` | True at the recorded SHA but the **current ref differs** — the doc may now be stale. |
| `SOURCE-MOVED` | The cited file/line/symbol no longer resolves at the SHA — evidence pointer is wrong. |
| `DOC-CHANGED` | The doc location no longer contains the claim (page edited since the report). |
| `UNVERIFIABLE` | Source for this product isn't configured, or the row had no SHA to check. |

A row already recorded `UNVERIFIED`/`PENDING` is reported as-is (still open), not as a pass.

## 3. Report

```
verify-claims — DOCS-XXXX  (report: <reports_dir>/<space>/DOCS-XXXX/report.md)
Source: server @ <sha>  (current ref head: <sha2>)

  # | claim                          | status
  1 | default of foo_buffer is 16M   | STILL-VERIFIED
  2 | FOO syntax since 13.1          | DRIFTED  (current ref: now 13.2)
  3 | foo is dynamic, GLOBAL         | DOC-CHANGED (doc now says SESSION)

Summary: 1 still-verified · 1 drifted · 1 doc-changed · 0 unverifiable
Verdict: NEEDS ATTENTION — rows 2,3 no longer match. Re-run /doc-ticket DOCS-XXXX to refresh.
```

End with a plain verdict: **ALL CLEAR** (every row `STILL-VERIFIED`) or **NEEDS ATTENTION** (any
other status), and point drift/changes back to `/doc-ticket` to refresh the page and report.

Also persist the run as an audit snapshot next to the report:
`<report_dir>/runs/verify-<YYYY-MM-DD>.md` (the date from `date +%F`) — the same per-claim table
plus the verdict. This is the **only** thing the skill writes; it never touches `report.md`, the
docs, or source.

## Guardrails

- **Audit-only.** Never edit docs, source, or `report.md`; never stage/commit/push. The single
  file it writes is the `runs/verify-<date>.md` snapshot (outside the repo). To fix drift, hand
  back to `/doc-ticket`.
- **Re-prove independently** — confirm against source; don't just trust the recorded verdict (the
  whole point is catching a report that was wrong or has gone stale).
- **No source configured for a product** → report those rows `UNVERIFIABLE`, don't guess.
- **Source is pinned by SHA**; a claim row without a SHA is `UNVERIFIABLE`, not assumed true.
- One report at a time.
</content>
