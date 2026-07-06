# CLAUDE.md

Guidance for Claude Code (and other AI agents) working in the **MariaDB documentation** repository.

@import AGENTS.md

## Golden rules

1. **This repo is GitBook-backed and edited from two sides.** Pages are edited both in the GitBook web app (which syncs back as `GITBOOK-XXX` commits) and via Git pull requests (`DOCS-XXXX`). Treat `SUMMARY.md` files as GitBook-owned navigation — change them deliberately, never reorder casually. See `AGENTS.md` › *GitBook sync*.
2. **Source is Markdown + GitBook blocks.** Use `{% hint %}`, `{% tabs %}`, `{% code %}`, and `content-ref` correctly — not plain-Markdown substitutes. Reference: `dev-docs/gitbook-syntax.md`.
3. **Cross-space links use `{alias}/path`,** never raw `app.gitbook.com` URLs. A CI Action expands them. Do **not** expand or "fix" aliases yourself, and don't try to validate them locally. Reference: `dev-docs/link-aliases.md`.
4. **Every page needs frontmatter** with at least `description:` (and usually `icon:`). New pages must include it.
5. **American English**, Google developer-style tone. Local summary: `dev-docs/style-guide.md` (canonical guide is linked there).
6. **Run `docs-check` (or `/precommit`) before you commit.** It mirrors the CI gates (codespell + lychee link-check) so PRs pass on the first push. A pre-commit hook runs the same checks automatically — but **only on commits Claude makes via the Bash tool, and only on staged files**; human/IDE/GitBook-UI commits bypass it, and CI is the authoritative gate. Trust model and the hook-vs-CI scope caveat: `.claude/README.md`.
7. **Source-verified edits leave a fact-check paper trail.** Every `doc-impact` / `doc-from-ticket` / `bulk-campaign` run writes a Markdown **fact-check report** (claim → doc `file:line` → source `file:line @ SHA` → verdict) to a per-user directory **outside the repo** (`reports_dir` in `.claude/doc-sources.local.json`) — **never committed**. `/jira-resolve` posts it to the DOCS ticket as a comment; `/verify-claims` re-audits it in any later session. One format, defined once: `dev-docs/cookbook-fact-trail.md`.

## Where things are

| Need | Go to |
|------|-------|
| Repo map, the documentation spaces, conventions, commands | `AGENTS.md` |
| What lives in which space + `SUMMARY.md` rules | `dev-docs/space-map.md` |
| GitBook block syntax (hint/tabs/code/content-ref) | `dev-docs/gitbook-syntax.md` |
| Cross-space link aliases | `dev-docs/link-aliases.md` |
| Style summary | `dev-docs/style-guide.md` |
| Pre-PR checklist (mirror CI locally) | `dev-docs/cookbook-pre-pr.md` |
| DOCS Jira workflow (project facts, transitions, branch model) | `dev-docs/cookbook-jira-workflow.md` |
| Fact-check paper trail (report format, where it lives, lifecycle) | `dev-docs/cookbook-fact-trail.md` |
| GitBook redirects (CSV format for retired/moved URLs) | `dev-docs/cookbook-gitbook-redirects.md` |

## Skills

- **`docs-check`** — validate changed pages the way CI does (spelling, links, frontmatter, alias syntax, `SUMMARY.md` consistency) before committing or opening a PR.
- **`new-page`** — scaffold a new page (frontmatter, style, GitBook syntax, `SUMMARY.md` nav entry) in the right space.
- **`gitbook-format`** — emit/repair GitBook blocks (`hint`/`tabs`/`code`/`content-ref`/`include`) and fix link/alias form.
- **`style-apply`** — editorial pass: fix mechanical style violations (product naming, American spelling, banned words, heading case) and surface voice/structure issues for your call.
- **`jira`** — MariaDB DOCS Jira workflow; backs the `/jira-start`, `/jira-create`, `/jira-resolve`, `/jira-close`, `/jira-comment`, `/jira-mine`, `/jira-chase` commands. Needs the `atlassian-mariadb` MCP connection (see the Jira cookbook); `/jira-chase` also needs the Slack MCP.
- **`doc-impact`** (`/impact <MDEV|DOCS|PR>`) — the "explain"/triage step: analyze a source change for doc impact (user-facing? which pages? claims to verify?) and report — no edits. Writes the **fact-check report skeleton**. Feeds `/doc-ticket`.
- **`doc-from-ticket`** (`/doc-ticket DOCS-XXXX`) — turn a DOCS ticket into a **source-verified** doc edit (verifies claims against local MariaDB source; first run configures the source repos). Writes the completed **fact-check report** (`dev-docs/cookbook-fact-trail.md`).
- **`verify-claims`** (`/verify-claims DOCS-XXXX`) — re-audit a fact-check report in a later session: re-prove each claim against source at the recorded SHA and the current ref, flag drift. Read-only.
- **`bulk-campaign`** — drive a batched, verified, resumable multi-file pass across one space (e.g. a railroad-diagram campaign or a terminology rename), tied to a DOCS ticket; keeps one campaign fact-check report.
- **`propose-improvement`** (`/propose-improvement <topic>`) — file an agent-tooling proposal (new skill or broader change) as a DOCS Task + write the interviewed proposal MD.
- **`report-skill-bug`** (`/skill-bug <name>`) — file a DOCS Task (label `claude-skill-bug`) when a skill breaks.

## Agent-tooling layout

| Kind | Location |
|------|----------|
| Shared Claude Code config / skills / subagents | `.claude/` (committed) |
| Personal, machine-specific overrides | `.claude/settings.local.json` (gitignored) |
| Agent / contributor playbooks | `dev-docs/` |

> Note: `tools/` at the repo root is a **documentation space** (MariaDB Tools docs), *not* a scripts directory. Agent scripts live under `.claude/hooks/`.
