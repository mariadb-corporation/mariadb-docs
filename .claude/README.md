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

## First-time setup (new teammates)

The skills and commands need **no installation** — they're committed here, so cloning the repo
and opening it in Claude Code makes all of them available automatically (Claude Code auto-loads
`.claude/skills/`, `.claude/commands/`, and `CLAUDE.md` → `AGENTS.md`). Type `/` to see the
commands. What you *do* set up is the per-user, gitignored pieces below.

1. **Install Claude Code** and get access to the `mariadb-docs` repo. Clone it and open the repo
   folder in Claude Code.
2. **Approve the project hooks.** On first open, Claude Code asks you to trust this project's
   settings — the committed `PreToolUse` hook (see *Trust model* below). Approve it to enable the
   pre-commit doc check.
3. **Connect the MariaDB Jira** (needed for `/jira-*`, `/doc-ticket`, `/impact`, `/skill-bug`,
   `/propose-improvement`). This is a **second** MCP connection, separate from any GridGain one:
   ```bash
   claude mcp add --transport http atlassian-mariadb https://mcp.atlassian.com/v1/mcp
   ```
   then `/mcp` → `atlassian-mariadb` → authenticate **in a browser signed in to your MariaDB
   account** (`mariadbcorp.atlassian.net`). Full steps + the wrong-account pitfall:
   `dev-docs/cookbook-jira-workflow.md › Connecting the MariaDB Jira`.
4. **Configure local source repos** (for `/doc-ticket` and `/impact` verification). Clone the
   MariaDB source you work on (e.g. `MariaDB/server`); the **first run** of those commands prompts
   for the path + authoritative ref and saves `.claude/doc-sources.local.json` (gitignored).
5. **Install the local check tools** (for `/precommit`, `docs-check`, and the pre-commit hook):
   `pipx install codespell`, install [`lychee`](https://github.com/lycheeverse/lychee), and ensure
   `jq` is present. If they're missing, the checks just warn — **CI still gates** every PR.
   Optional: `gh` (GitHub CLI) for PR linking in `/jira-resolve`.
6. **Read, then try.** Skim `CLAUDE.md` (golden rules + skill/command list) and `AGENTS.md` (repo
   map). Smoke-test with `/jira-mine` and `/precommit`.

> Only steps 3–5 are per-user. Everything else comes with the clone.

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
