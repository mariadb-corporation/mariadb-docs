---
name: report-skill-bug
description: Report a Claude Code skill in mariadb-docs that broke. Use when the user says "report a skill bug", "file a bug for <skill>", or "<skill> is broken" — or when a skill fails clearly mid-session and the user wants it logged. Files a DOCS Jira Task labeled claude-skill-bug via the MariaDB Jira connection and returns the ticket URL.
allowed-tools: Bash, Read, Grep, Glob, mcp__atlassian-mariadb__createJiraIssue, mcp__atlassian-mariadb__atlassianUserInfo, mcp__atlassian-mariadb__lookupJiraAccountId, mcp__atlassian-mariadb__getAccessibleAtlassianResources
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# report-skill-bug

Files a Jira ticket for a broken Claude Code skill. **No browser, no UI, no clipboard** — you
create the ticket via the **`atlassian-mariadb` MCP connection** and return the URL. Uses the
`jira` skill's config (server `atlassian-mariadb`, cloudId `164b0d33-…`, project `DOCS`).

## When to use

Trigger phrases: "report a skill bug", "file a bug for `<skill>`", "the `<skill>` skill is
broken", or after a skill fails clearly mid-session and the user asks to log it.

**Proactive trigger.** If you observe an obvious skill failure mid-session — wrong output, a step
that contradicts its own SKILL.md, an MCP call that consistently errors, instructions that loop —
pause and ask once: *"I noticed `<skill>` did `<X>`, which looks like a bug. Want me to file it
via report-skill-bug?"* Don't file unilaterally; the user confirms. Ask once; drop it if declined.

## Workflow

### 1. Identify the skill

Confirm which skill broke and verify it exists:

```bash
ls .claude/skills/<name>/SKILL.md   # or .claude/commands/<name>.md for a slash command
```

If the user didn't name it but a skill failed in this session, propose that one and confirm. If
unclear, list `.claude/skills/*/` and `.claude/commands/*.md` for the user to pick. Don't file
against a name that has no matching file.

### 2. Gather environment (inline — no external script)

```bash
echo "Claude Code: $(claude --version 2>/dev/null || echo unknown)"
echo "OS: $(uname -sr)"
echo "Shell: $SHELL"
```

Keep the output for the `## Environment` section; don't dump raw to the user.

### 3. Collect the bug details

Ask only for what the session doesn't already show:

- **Invocation** — the exact command/prompt (e.g. `/jira-start DOCS-1234`).
- **Expected** vs **Actual**.
- **Optional transcript snippet** — if the user points to a file or pastes a block, include up
  to ~8 KB.

If the user already explained these, don't re-ask — confirm and proceed.

### 4. Connection check, then create the ticket

Run the `jira` skill's **Setup** check first (`getAccessibleAtlassianResources()` must show
`mariadbcorp.atlassian.net`). Then:

```
mcp__atlassian-mariadb__createJiraIssue(
  cloudId="164b0d33-ee39-4b4d-b1d5-e71a97376560",
  projectKey="DOCS",
  issueTypeName="Task",
  summary="[skill: <name>] <one-line of what broke>",
  description="<structured markdown — template below>",
  contentFormat="markdown",
  assignee_account_id="<skill owner, else current user>",
  additional_fields={"labels": ["claude-skill-bug"]}
)
```

> DOCS has **no Bug issue type** — file a **Task** and tag it with the **`claude-skill-bug`**
> label so it's filterable. (No components on this project.)
>
> **Visibility — set an assignee.** An unassigned, label-only ticket may reach no one: the
> `claude-skill-bug` label currently has no watcher or board filter. So **always set
> `assignee_account_id`** (top-level param) — prefer the broken skill's owner (from its
> `owners:` frontmatter, resolved via `lookupJiraAccountId` if it's a handle), else the current
> user (`atlassianUserInfo()`). Tell the user the ticket relies on the label for discovery and
> recommend a one-time saved filter / board column on `claude-skill-bug`.

**Description template:**

````markdown
## Skill
<name>

## Environment
- Claude Code: <version>
- OS: <uname>
- Shell: <shell>

## What happened
**Invocation:** `<exact command or prompt>`

**Expected:** <one paragraph>

**Actual:** <one paragraph>

## Transcript
```
<up to ~8 KB; redact tokens, absolute home paths, secrets>
```
````

**Redact before sending:** API tokens, JWTs, `Bearer .*`, `ATATT.*`, `glpat-.*`, and absolute
home paths (`/Users/<name>/`, `/home/<name>/`). Replace with `<REDACTED>`.

### 5. Report the result

Extract the issue key and print only:

```
Filed:    https://mariadbcorp.atlassian.net/browse/<KEY>
Label:    claude-skill-bug
Assignee: <name>
```

Note once that the ticket is discoverable mainly via the `claude-skill-bug` label (no watcher
yet). No further commentary unless asked.

## Failure modes

- **`atlassian-mariadb` offline / wrong account.** `getAccessibleAtlassianResources()` doesn't
  show `mariadbcorp` → tell the user to reconnect `atlassian-mariadb` under their MariaDB account
  (see `dev-docs/cookbook-jira-workflow.md`), or file manually in DOCS with the
  `claude-skill-bug` label. Don't open a browser — out of scope.
- **Skill name has no matching file.** Stop and confirm the name; don't file against a
  nonexistent skill.

## Don't

- Don't open a browser, call `gh`, or use the clipboard — ticket creation is API-only.
- Don't include secrets in the description.
- Don't use the GridGain Rovo connection (`mcp__claude_ai_Atlassian_Rovo__*`) — this is MariaDB.
- Don't wrap the result in extra prose; the user wants the URL.
