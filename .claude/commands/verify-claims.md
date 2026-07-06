---
description: Re-verify a fact-check report against MariaDB source — confirm each documented claim is still source-proven, and surface any drift. Read-only audit; does not edit.
argument-hint: DOCS-XXXX | MDEV-XXXXX | path to a report (optional — inferred from the current branch if omitted)
allowed-tools: Bash, Read, Grep, Glob, WebFetch
---

# /verify-claims

Run the **`verify-claims`** skill in `.claude/skills/verify-claims/SKILL.md` for `$ARGUMENTS`.

- Resolve the report key from the argument, or infer `DOCS-XXXX` from the current branch.
- Read `reports_dir` + `sources` from `.claude/doc-sources.local.json`; locate the report by key
  in the space-grouped tree (`<space>/<KEY>/report.md`; stop if there's no report — suggest
  `/doc-ticket` to create one).
- Re-check each claim row against source at the recorded SHA **and** the current ref (drift), and
  confirm the doc location still matches: `STILL-VERIFIED` / `DRIFTED` / `SOURCE-MOVED` /
  `DOC-CHANGED` / `UNVERIFIABLE`.
- Print the per-claim table and a plain verdict (**ALL CLEAR** / **NEEDS ATTENTION**). Read-only —
  never edits docs, source, or the report.

Report: $ARGUMENTS
