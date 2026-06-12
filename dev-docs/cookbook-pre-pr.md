# Cookbook: pre-PR checklist

Run these checks **before committing / opening a PR** so the build passes on the first push.
They mirror the GitHub Actions that gate every PR. The fastest path is the **`docs-check`**
skill, which runs them for you; this page documents what it does and how to run them by hand.

## What CI checks

| Check | Tool | Workflow |
|-------|------|----------|
| Spelling (content + filenames) | `codespell` | `codespell.yml` |
| Broken links | `lychee` | `link-check-pr.yml` |
| Alias expansion | sed (auto-commit) | `expand-gitbook-aliases.yml` |
| Help-tables regen | Python | `generate-help-tables.yml` |

Only the first two can fail your PR; aliases and help-tables are regenerated automatically.

## 1. Spelling + links — `doc-lint.sh`

The codespell and lychee invocations that mirror CI live in **one** place,
`.claude/hooks/doc-lint.sh`. Run it instead of re-typing the flags:

```bash
# Install the tools once:
pipx install codespell                                   # spelling
# lychee: cargo install lychee  (or brew / docker) — https://github.com/lycheeverse/lychee

# For a PR, check your WHOLE branch diff (not just staged) — this matches what CI lints:
git diff --name-only origin/main...HEAD -- '*.md' '*.html' \
  | xargs -r .claude/hooks/doc-lint.sh
```

`doc-lint.sh` runs codespell and lychee with the exact CI-mirroring flags/excludes (defined
only in that script), exits non-zero on a real failure, and prints a `SKIPPED` notice for any
tool that isn't installed (CI still runs it).

- A real term flagged as a typo? Add it to `.codespellignore` (one word per line) — sparingly.
- The lychee exclude set skips **any URL containing `{` or `%7B`** — which covers `{alias}`
  links (so they never trip link-check), but also means a genuinely broken link that happens to
  contain a brace would be skipped too. Don't rely on lychee to catch braced URLs; just don't
  hand-expand aliases.

> **Hook vs. PR scope.** The pre-commit hook and `/precommit` check only **staged** files; CI
> checks the **full PR diff**. Passing the hook is not a guarantee CI passes — run the
> whole-branch command above before opening the PR. (See `.claude/README.md`.)

## 2. Structural sanity checks (heuristic)

These aren't enforced by CI but catch common GitBook mistakes. They're heuristics — **ignore
anything inside fenced code blocks (```) or `{% code %}` blocks**, since SQL/JSON/protocol
samples legitimately contain `{`, `%`, and raw URLs.

- **Frontmatter:** new pages have `description:` (and usually `icon:`).
- **`SUMMARY.md`:** if you added/moved/renamed a page, its `SUMMARY.md` entry exists, points at
  the right path, and matches the surrounding indentation/link style. (The nightly error-sync
  job legitimately auto-commits `server/SUMMARY.md` — that's an authorized exception.)
- **GitBook blocks:** hints use a valid style (`info`/`warning`/`danger`/`success`); `tabs`,
  `code`, `content-ref` blocks are balanced (every open has its `end…`).
- **Links:** same-space links are relative `.md` paths; cross-space links use `{alias}`.
- **Generated content:** you did **not** hand-edit `help-tables/` or server error-code pages —
  edit the source reference page instead.

## Automating it

- **`/precommit`** — runs the checks on **staged** files on demand.
- **`docs-check`** skill — runs them against your changed files and reports by check.
- **Pre-commit hook** (`.claude/hooks/pre-commit.sh`, wired in `.claude/settings.json`) — runs
  `doc-lint.sh` on staged files when **Claude Code** runs `git commit`, blocking on real
  failures and warning (without blocking) if a tool isn't installed. It does **not** gate human
  or GitBook-UI commits — see `.claude/README.md`.
