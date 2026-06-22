---
description: Hand a DOCS ticket off for editorial review — comment with the PR link and transition to Review. (Use /jira-close after merge.)
argument-hint: DOCS-XXXX (optional — inferred from the current branch if omitted)
allowed-tools: Bash, Read, Grep, Glob, mcp__atlassian-mariadb__getJiraIssue, mcp__atlassian-mariadb__getTransitionsForJiraIssue, mcp__atlassian-mariadb__transitionJiraIssue, mcp__atlassian-mariadb__addCommentToJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /jira-resolve

Run the **RESOLVE** procedure in `.claude/skills/jira/SKILL.md` for `$ARGUMENTS`.

- Run the skill's **Setup** connection check first.
- Resolve the key from the argument, or infer it from the current branch's `DOCS-XXXX` prefix.
- Stop if the ticket is already in Review/Closed (idempotent).
- Find the PR link (`gh pr view` or the `DOCS-XXXX` commit on `origin/main`); ask if none found.
- Comment with the PR link (`contentFormat="markdown"`).
- Post the **fact-check report** (found by key under `reports_dir`, grouped by space:
  `<space>/DOCS-XXXX/report.md`) as a second Markdown comment if it exists, set its `Status:` to
  `handed-off`, and regen `INDEX.md`; warn (and ask) if the doc ticket has no report.
- Transition to **`Review`** (match by name). This does **not** close the ticket — the reviewer
  runs `/jira-close` after merge.
- Confirm with `Ticket / Status: Review / PR link / report posted`.

Ticket: $ARGUMENTS
