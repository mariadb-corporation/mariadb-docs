# `.claude/` — shared Claude Code configuration

This directory is **committed and shared** across everyone who works on the docs with Claude
Code. It contains:

| Path | What it is |
|------|------------|
| `settings.json` | Project settings, incl. the `PreToolUse(Bash)` hook wiring |
| `settings.local.json` | **Personal** overrides — gitignored, never committed |
| `hooks/doc-lint.sh` | Canonical codespell + lychee linter (single source of truth, mirrors CI) |
| `hooks/pre-commit.sh` | PreToolUse hook: gates Claude-made `git commit`s by calling `doc-lint.sh` |
| `skills/` | Shared skills (e.g. `docs-check`) |
| `commands/` | Shared slash commands (e.g. `/precommit`) |

## ⚠️ Trust model — read before cloning

`settings.json` registers a **`PreToolUse(Bash)` hook**. Once you open this repo in Claude Code,
that hook runs `.claude/hooks/pre-commit.sh` (which runs `doc-lint.sh`) **on every Bash command
Claude executes** — automatically, with no per-run prompt.

Consequences:

- **Cloning + opening this repo = agreeing to run these committed shell scripts locally.**
- A pull request that edits `.claude/hooks/*.sh` is proposing **code that will execute on the
  machine of anyone who reviews that PR in Claude Code.** Review changes to these scripts with
  the same scrutiny as any executable — this repo accepts outside contributions.
- If you don't want the hook, override it in `.claude/settings.local.json` (gitignored) or
  disable hooks in your Claude Code settings.

## Scope — what the hook does and does NOT cover

The pre-commit hook **only gates commits that Claude Code makes via the Bash tool.** It does
**not** run for:

- a human running `git commit` in a terminal,
- IDE / GUI commits,
- edits made in the **GitBook web app** (which sync back as `GITBOOK-XXX` commits).

So it's a convenience that catches issues in agent-driven commits early — **not** a
team-wide guarantee. For coverage of *all* commits, install a real Git hook
(`core.hooksPath`) or adopt the [`pre-commit`](https://pre-commit.com) framework that calls
`doc-lint.sh`. **CI is the authoritative gate** for every PR regardless.

## Hook vs. CI: passing the hook ≠ passing CI

| | Files checked |
|--|--------------|
| Pre-commit hook / `/precommit` | **staged** files only (`git diff --cached`) |
| `docs-check` skill | changed vs `main` (staged + unstaged + `origin/main...HEAD`) |
| CI (`codespell.yml`, `link-check-pr.yml`) | the **full PR diff** against the base branch |

A file changed earlier in your branch but not currently staged can pass the hook yet still be
linted by CI. Before opening a PR, run the full check over your whole branch diff — see
`dev-docs/cookbook-pre-pr.md`.

## Single source of truth

The codespell flags and the lychee exclude set are defined **only** in `hooks/doc-lint.sh`.
The skill, the `/precommit` command, and `dev-docs/cookbook-pre-pr.md` all delegate to it. If CI
changes those flags/excludes, update `doc-lint.sh` and nothing else.
