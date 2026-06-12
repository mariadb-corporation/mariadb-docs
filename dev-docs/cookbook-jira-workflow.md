# Cookbook: MariaDB DOCS Jira workflow

Conventions reference for the `jira` skill, the `/jira-*` commands, and `doc-from-ticket`.
The skill (`.claude/skills/jira/SKILL.md`) is the source of truth for the exact tool payloads;
this page is the human-facing overview.

## The DOCS project (ground truth, verified 2026-06-12)

| | |
|--|--|
| Site | `mariadbcorp.atlassian.net` (cloudId `164b0d33-ee39-4b4d-b1d5-e71a97376560`) |
| Project | `DOCS` — "Documentation", id `10037`, **team-managed** |
| Issue types | **Task** (default), Epic, Subtask — no Bug/Improvement |
| Create requires | only **Summary** (priority defaults to Major) |
| Components / fix versions | not used |

### Workflow

```
TODO ──▶ IN PROGRESS ──▶ Review ──▶ Closed
            │                          ▲
            └── On Hold / Needs Feedback / CANCELED / DUPLICATED
```

All transitions are **global** (available from any status) and have **no required screen**.
Transition by **name** (ids are stable hints): IN PROGRESS=21, Review=2, Closed=31, On Hold=6,
Needs Feedback=5, TODO=11, CANCELED=3, DUPLICATED=4.

## Connecting the MariaDB Jira (two-account setup)

DOCS lives in MariaDB's Atlassian, which is a **separate account** from GridGain's. We use a
**second** Rovo MCP connection so both work side by side:

1. `claude mcp add --transport http atlassian-mariadb https://mcp.atlassian.com/v1/mcp`
2. In a browser signed in to `mariadbcorp.atlassian.net` (incognito / separate profile if your
   default session is GridGain), run `/mcp` → `atlassian-mariadb` → authenticate.
3. Verify: `getAccessibleAtlassianResources()` on that server lists `mariadbcorp.atlassian.net`.

If it ever shows only `ggsystems`, the connection bound to the wrong account — log out of that
server in `/mcp` and re-auth under a MariaDB browser session. The `jira` skill checks this before
every operation.

## The end-to-end flow

```
/impact DOCS-XXXX          # (triage) analyze the change: docs needed? which pages? claims to verify
/jira-start DOCS-XXXX      # branch DOCS-XXXX-slug from main, ticket → IN PROGRESS
/doc-ticket DOCS-XXXX      # verify against MariaDB source, draft the .md edit
<review & commit, open PR> # your call — the skills never push/commit/PR for you
/jira-resolve DOCS-XXXX    # comment PR link, ticket → Review (editorial review)
/jira-close DOCS-XXXX      # after merge, ticket → Closed
```

`/impact` is optional triage (the "explain" step) — run it first to decide *whether* and *what*
to document; it can also analyze an `MDEV-XXXXX` or a `MariaDB/server` PR before a DOCS ticket
exists. Supporting commands: `/jira-create <desc>` (file a new ticket),
`/jira-comment DOCS-XXXX <text>`, `/jira-mine` (your open tickets).

## Branch & PR conventions

- Branch name: **`DOCS-XXXX-short-slug`**, cut from latest `origin/main` with `--no-track`.
- First push: `git push -u origin DOCS-XXXX-short-slug`.
- Work lands via **PR** (so codespell / lychee / alias-expansion CI runs). Keep `DOCS-XXXX` in
  the branch name and commit messages.
- The skills **never** commit, push, or open the PR — those stay user-driven.

## `doc-from-ticket` and source verification

DOCS tickets (esp. `[Auto] Documentation needed`) reference an upstream **MDEV** ticket
(`jira.mariadb.org`), a **Release Series**, and often a `github.com/MariaDB/server` PR.
`doc-from-ticket` follows that trail and **verifies every factual claim against local MariaDB
source** before drafting — because ticket prose is often a paraphrase or a feature *request*, not
shipped behavior.

- Source repos are configured per-user in `.claude/doc-sources.local.json` (gitignored; paths
  differ per machine). First run prompts for products + paths + the authoritative ref.
- Verification reads the configured **default ref** read-only via `git -C <path> grep/show <ref>`
  — it never checks out or modifies the source repo.
- Unverifiable claims are flagged for human confirmation, never asserted as fact.
