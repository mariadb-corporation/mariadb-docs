---
name: docs-check
description: Validate changed MariaDB documentation pages the way CI does, before committing or opening a PR. Use when the user asks to check docs, validate a page, run pre-PR checks, "check links", "run codespell", or before creating a docs PR. Runs codespell + lychee link-check on changed files and checks frontmatter, GitBook block balance, alias usage, and SUMMARY.md consistency, then reports pass/fail by check.
allowed-tools: Bash, Read, Grep, Glob
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# docs-check

Mirrors the PR CI gates (codespell + lychee) locally and adds quick structural checks, so a
docs PR passes on the first push. Reference: `dev-docs/cookbook-pre-pr.md`.

## When to use

- Before committing doc changes or opening a PR.
- The user says: "check the docs", "validate this page", "run pre-PR checks", "check links",
  "run codespell", "will this pass CI?".

## Scope — which files

Default to the files the user changed. Determine the set in this order:

1. If the user named specific files/paths, use those.
2. Else use staged + unstaged changes vs `main`:
   ```bash
   git diff --name-only origin/main...HEAD -- '*.md' '*.html'; \
   git diff --name-only -- '*.md' '*.html'; \
   git diff --cached --name-only -- '*.md' '*.html'
   ```
   (de-duplicate the union; ignore deleted files).
3. If nothing changed, ask the user which space/path to check — **never** run across the whole
   repo unprompted (server alone is ~4,500 files).

## Checks

Run all that apply, then report each as PASS / FAIL / SKIPPED.

### 1–2. Spelling + links (codespell + lychee) — via `doc-lint.sh`

Run the **canonical** linter (the single source of truth for the CI-mirroring flags/excludes)
on the file set, from the repo root:

```bash
.claude/hooks/doc-lint.sh <files>
```

- It runs codespell and lychee with the exact CI-mirroring flags/excludes (defined only in
  `doc-lint.sh`) and exits non-zero on a real failure.
- If a tool isn't installed it prints a `SKIPPED` notice on stderr and does **not** fail —
  report that check as SKIPPED (`pipx install codespell`;
  lychee → https://github.com/lycheeverse/lychee).
- **Do not** re-spell the codespell flags or lychee excludes here — they live only in
  `doc-lint.sh`. If a codespell hit is a real term (not a typo), tell the user it can be added
  to `.codespellignore`; don't reword silently. Never report `{alias}` links as broken or
  expand them.

The remaining checks below are **best-effort, LLM-performed heuristics** — report them as
warnings, not hard failures, and **ignore anything inside fenced code blocks (```) or
`{% code %}` blocks** (SQL/JSON/protocol samples legitimately contain `{`, `%`, raw URLs, and
brace-like text that would otherwise false-positive).

### 3. Frontmatter

For each changed page, confirm it opens with a YAML frontmatter block containing
`description:`. Flag new pages missing it. `icon:` is recommended, not required.

### 4. GitBook blocks balanced (heuristic)

Outside code blocks, check that block tags pair up:

- `{% hint %}` ↔ `{% endhint %}`, and every hint `style=` is one of
  `info`/`warning`/`danger`/`success` (flag `tip`/`warn`).
- `{% tabs %}`/`{% endtabs %}`, `{% tab %}`/`{% endtab %}`.
- `{% code %}`/`{% endcode %}`, `{% content-ref %}`/`{% endcontent-ref %}`.

Treat an apparent imbalance as a **warning** to confirm with the user, not a definite error —
a `{%`-like fragment inside a code sample is not a real block.

### 5. Link style (heuristic)

- Same-space links should be relative `.md` paths.
- Cross-space links should use `{alias}` (see `dev-docs/link-aliases.md`), not raw
  `app.gitbook.com` URLs. Flag any raw GitBook URL **in prose** (not in code samples).

### 6. SUMMARY.md consistency

If any page was **added/moved/renamed**, confirm the space's `SUMMARY.md` has a matching entry
pointing at the correct path. Flag pages with no nav entry, and `SUMMARY.md` entries pointing
at non-existent files. (Note: the nightly error-sync job legitimately auto-commits
`server/SUMMARY.md` — don't treat its entries as anomalies.)

## Output

Report a compact summary, e.g.:

```
docs-check on 3 files:
  codespell ...... PASS
  lychee ......... FAIL (2 broken links — see below)
  frontmatter .... PASS
  gitbook blocks . FAIL (unclosed {% tabs %} in server/foo.md)
  link style ..... PASS
  SUMMARY.md ..... PASS
```

List each failure with file:line and a concrete fix. Don't auto-fix unless the user asks;
when you do fix, re-run the affected check to confirm.

## Notes

- This is a convenience gate; **CI is authoritative**. If a checker is missing locally, say so
  and remind the user CI will still run it.
- Do not modify `.github/workflows/*`, `help-tables/` (generated), or expand `{alias}` links.
