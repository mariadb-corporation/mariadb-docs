---
name: bulk-campaign
description: Drive a repo-wide, multi-file documentation pass across mariadb-docs — batched, progress-tracked, and verified per file. Use for campaigns like "add railroad diagrams to all SQL pages", a terminology rename across a space, a frontmatter backfill, or any change that repeats over many .md files. Scopes to one space/path, ties to a DOCS ticket, and never fans out across the whole repo unprompted.
allowed-tools: Bash, Read, Grep, Glob, Edit, Write
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# bulk-campaign

Run a sustained, multi-file documentation change safely: discover the work-list, process it in
small batches, verify each file, track progress so it's resumable, and never silently truncate.
Modeled on real campaigns like **DOCS-5614** ("add Railroad diagrams to N more SQL pages") whose
history is a series of small, reviewable batch commits.

## When to use

"Add X to all pages under <space>", "rename Y → Z across <space>", "backfill frontmatter
`description:` for pages missing it", "apply <transformation> to every SQL-statement page" — any
change that repeats across many `.md` files.

## 0. Define the campaign (settle before touching files)

Gather, asking only what's missing:

- **The transformation** — exactly what changes in each file (what to add/edit/replace).
- **The scope** — a **space and path** plus a selector (e.g. *all `.md` under
  `server/reference/sql-statements/` whose body contains a syntax block*). **Never operate
  across all spaces unprompted** — require an explicit space/path. Server alone is ~4,500 files.
- **The tracking ticket** — a `DOCS-XXXX` campaign ticket. If none exists, offer `/jira-create`
  (and `/jira-start` to branch + go IN PROGRESS). Commits and the branch carry that key.

## 1. Build the work-list (and confirm before editing)

Enumerate the matching files within scope, then **stop and confirm**:

```bash
# example: SQL-statement pages, excluding nav/landing/generated
grep -rl "<selector>" server/reference/sql-statements/ --include=*.md \
  | grep -vE '/(SUMMARY|README)\.md$'
```

Report: total count, a short sample, and **what's excluded** (e.g. `SUMMARY.md`, `README.md`
landing pages, generated `help-tables/`). Do not proceed until the user confirms the list and
size. If the list is surprisingly large, say so and propose narrowing.

## 2. Plan batches

- Default batch size **~5 files** (matches the DOCS-5614 cadence — small, reviewable commits).
- Show the batch plan (N batches of ~5).
- **GitBook-sync hazard:** large structural passes (mass moves/renames, `SUMMARY.md`
  reordering) can collide with concurrent GitBook-UI edits. For those, warn the user and
  coordinate; prefer content-only edits in place. See `AGENTS.md` › *GitBook sync*.

## 3. Process each file (per batch)

For every file in the batch:

1. **Apply the transformation.** Delegate GitBook block/link syntax to the **`gitbook-format`**
   skill; new-page conventions to **`new-page`** if adding pages. **Never modify content inside
   fenced or `{% code %}` blocks** (the code-sample rule).
2. **Verify it actually applied** — re-read the changed region; don't assume the edit matched.
3. **Validate** — `.claude/hooks/doc-lint.sh <file>` (or the `docs-check` skill). Record the
   result.
4. **Record** the file as `done` / `failed` (with the reason) in the progress log (§5).

Never skip a file silently. A file you couldn't transform is `failed` with a reason, surfaced in
the summary — not omitted.

## 4. Per-batch review and commit

- Present the batch's diff (`git diff --stat` + key hunks) for the user to review.
- **Commit only with explicit go-ahead**, one commit per batch:
  ```
  DOCS-XXXX <campaign description> (N more)
  ```
- **Never `git push`** and never open the PR — the user pushes and opens the PR when ready.
- If the user hasn't authorized commits, leave the batch staged/working and let them commit.

## 5. Track progress (resumable)

Maintain a progress log so a long campaign can stop and resume:

- Keep a running checklist in the conversation, and optionally persist to a **gitignored** state
  file `.claude/bulk-campaign.local.json`:
  ```json
  { "ticket": "DOCS-XXXX", "scope": "server/reference/sql-statements/",
    "done": ["a.md","b.md"], "failed": [{"file":"c.md","reason":"..."}], "total": 120 }
  ```
- On resume, read the state file (if present), skip files already `done`, and continue.

## 6. Final report

```
Campaign DOCS-XXXX — <description>
  scope:   server/reference/sql-statements/  (selector: …)
  files:   120 in scope
  done:    118   failed: 2   skipped: 0
  batches: 24 (committed: 24)
  failures:
    - server/.../foo.md — <reason>
```

State any bound you applied (top-N, sampling) explicitly — **no silent caps**.

## Guardrails

- **One space/path at a time.** Never sweep the whole repo without an explicit, confirmed scope.
- **Confirm the work-list before editing**; surface exclusions and size.
- **Per-file verification is mandatory**; failures are reported, never hidden.
- **Never push or open PRs**; commit per-batch only with explicit approval, with `DOCS-XXXX` in
  the message.
- Respect generated content (`help-tables/`) and `SUMMARY.md` ownership; coordinate structural
  passes against the GitBook sync.
- Don't fabricate content a page doesn't support; if the transformation needs a judgment call
  per file, pause and ask rather than guessing across the batch.
