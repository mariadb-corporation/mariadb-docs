---
description: Run the doc CI checks (codespell + lychee + structural) on all STAGED files before committing.
argument-hint: "(no arguments — always checks staged files)"
allowed-tools: Bash, Read, Grep, Glob
---

# /precommit

Run the same checks the pre-commit hook and CI run, but **on demand** and scoped strictly to
**staged** files (`git diff --cached`). Use this right before a `git commit` to confirm it will
pass CI. This is the manual twin of `.claude/hooks/pre-commit.sh`; the tool checks live in
`.claude/hooks/doc-lint.sh` and the structural heuristics in the **`docs-check`** skill
(`.claude/skills/docs-check/SKILL.md`).

**Takes no arguments** — it always operates on the staged set.

## 1. Collect staged files

```bash
git diff --cached --name-only --diff-filter=ACM -- '*.md' '*.html'
```

- If **nothing** is staged, stop and tell the user there's nothing to check (suggest
  `git add` first). Do **not** fall back to unstaged or whole-repo files — this command is
  staged-only by definition.
- Ignore deleted files (the `--diff-filter=ACM` above already excludes deletions).

## 2. Run the checks

**Tool checks (authoritative)** — run the canonical linter on the staged set from the repo root:

```bash
.claude/hooks/doc-lint.sh <staged files>
```

It runs codespell + lychee with the CI-exact flags/excludes and exits non-zero on a real
failure; a missing tool is reported as `SKIPPED` (not a failure). Don't re-spell the flags here
— they live only in `doc-lint.sh`.

**Structural heuristics (best-effort warnings)** — then apply the `docs-check` skill's
structural checks (frontmatter, GitBook-block balance, link style, `SUMMARY.md` consistency).
Report these as warnings, and **ignore anything inside fenced code blocks or `{% code %}`
blocks** — code samples legitimately contain `{`, `%`, and raw URLs that would false-positive.

See `.claude/skills/docs-check/SKILL.md` for the heuristics and guardrails (never expand
`{alias}` links, never edit `help-tables/` or `.github/workflows/`).

## 3. Report

Print a compact per-check summary and, for each failure, the `file:line` and a concrete fix:

```
/precommit on <N> staged file(s):
  codespell ...... PASS
  lychee ......... FAIL (2 broken links)
  frontmatter .... PASS
  gitbook blocks . PASS
  link style ..... PASS
  SUMMARY.md ..... PASS
```

Do not auto-fix unless the user asks. If the user asks you to fix, apply the fix, `git add` the
corrected files, and re-run the affected check to confirm before reporting done.
