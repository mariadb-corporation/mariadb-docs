# `.claude/` — shared Claude Code configuration

This directory is **committed and shared** across everyone who works on the docs with Claude
Code. It contains:

| Path | What it is |
|------|------------|
| `settings.json` | Project settings, incl. the `PreToolUse(Bash)` hook wiring |
| `settings.local.json` | **Personal** overrides — gitignored, never committed |
| `hooks/doc-lint.sh` | Canonical codespell + lychee linter (single source of truth, mirrors CI), plus four checks it delegates to their own scripts: includes (`includecheck.sh`), heading anchors (`fragcheck.py`), orphaned pages and gutted pages (`navcheck.py` and an inline guard) |
| `hooks/includecheck.sh` | Resolves every relative GitBook `{% include %}`; fails on a dead or cross-space target. Also the entry point for `includecheck-pr.yml` (DOCS-6586), which runs it tree-wide |
| `hooks/fragcheck.py` | GitBook-accurate heading-anchor checker, called by `doc-lint.sh` |
| `hooks/navcheck.py` | Orphaned-page (nav coverage) checker, called by `doc-lint.sh` |
| `hooks/pre-commit.sh` | PreToolUse hook: gates Claude-made `git commit`s by calling `doc-lint.sh` |
| `hooks/doc-lint-test.sh` | Regression suite for `doc-lint.sh` — fixtures in a throwaway repo; run it after editing the linter |
| `skills/` | Shared skills (e.g. `docs-check`) |
| `commands/` | Shared slash commands (e.g. `/precommit`) |

## First-time setup (new teammates)

The skills and commands need **no installation** — they're committed here, so cloning the repo
and opening it in Claude Code makes all of them available automatically (Claude Code auto-loads
`.claude/skills/`, `.claude/commands/`, and `CLAUDE.md` → `AGENTS.md`). Type `/` to see the
commands. What you *do* set up is the per-user, gitignored pieces below.

> Launching Claude from a **parent workspace folder** that contains this repo as a subdirectory
> (instead of opening `mariadb-docs/` directly)? Auto-loading won't reach the project skills.
> See [`dev-docs/cookbook-multi-repo-workspace.md`](../dev-docs/cookbook-multi-repo-workspace.md)
> for the user-global symlink setup that fixes it.

1. **Install Claude Code** and get access to the `mariadb-docs` repo. Clone it and open the repo
   folder in Claude Code.
2. **Approve the project hooks.** On first open, Claude Code asks you to trust this project's
   settings — the committed `PreToolUse` hook (see *Trust model* below). Approve it to enable the
   pre-commit doc check.
3. **Connect the MariaDB Jira** (needed for `/jira-*`, `/doc-ticket`, `/impact`, `/skill-bug`,
   `/propose-improvement`). You need **one** Atlassian MCP connection that reaches
   `mariadbcorp.atlassian.net`; the tooling doesn't care what it's called. Check what you already
   have:
   ```bash
   claude mcp list          # look for an Atlassian entry
   ```
   If the account-level **`claude.ai Atlassian Rovo`** connection is present and authenticated to
   your MariaDB account, you're done. Only if you need MariaDB *alongside* another Atlassian
   account (e.g. GridGain) in the same session, add a second, separately-authenticated server:
   ```bash
   claude mcp add --transport http atlassian-mariadb https://mcp.atlassian.com/v1/mcp
   ```
   then `/mcp` → `atlassian-mariadb` → authenticate **in a browser signed in to your MariaDB
   account**. Either way, verify with `getAccessibleAtlassianResources()` — it must list
   `mariadbcorp`. Full steps + the wrong-account pitfall:
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

## Who tests the linter

`hooks/doc-lint.sh` had no test of its own until DOCS-6471, and it cost a real outage: DOCS-6409
was a `mktemp` template with no `X` characters that made the script **exit 2 on every
GNU-coreutils run** — for 135 commits. Because the failing line sat *before* the checks, it
silently took the GitBook include resolver down with it, so a feature shipped the same day never
ran on Linux at all. On BSD/macOS `mktemp` the identical line worked fine, so the only machine
that could have noticed was a Linux one, and nothing on Linux ever ran the script.

`hooks/doc-lint-test.sh` is the gate for that class. It builds fixtures in a throwaway git repo
under `TMPDIR` — it never reads this checkout's content — and asserts exit codes and messages for
the include resolver, the gutted-page guard, the env-var knobs, the repo-root guard, and every
"tool not installed" SKIP branch. Since DOCS-6586 it also covers `includecheck.sh` as its own
entry point — its `--stdin0` mode, its usage errors, and the fact that a missing
`includecheck.sh` FAILS `doc-lint.sh` rather than SKIPping (every other dependency is an external
tool a contributor may not have; that one is checked in beside it, so its absence is a broken
checkout). Run it after any change to `doc-lint.sh` or `includecheck.sh`:

```bash
.claude/hooks/doc-lint-test.sh              # --keep to inspect the sandbox, --verbose for output
```

`.github/workflows/doc-lint-test.yml` runs it on **every** PR, on both `ubuntu-latest` and
`macos-latest`, and shellchecks every tracked shell script alongside it. Both platforms on
purpose: the suite's first run found the mirror image of DOCS-6409 — an empty-array expansion
that is an error under `set -u` before bash 4.4, so on the bash 3.2 that stock macOS still ships,
every `{% include %}` climbing out of its own directory was misreported as unresolvable. Same
class of bug, opposite platform. A single-runner gate sees one and not the other.

## Single source of truth

The codespell flags and the lychee exclude set are defined **only** in `hooks/doc-lint.sh`.
The skill, the `/precommit` command, and `dev-docs/cookbook-pre-pr.md` all delegate to it. If CI
changes those flags/excludes, update `doc-lint.sh` and nothing else.
