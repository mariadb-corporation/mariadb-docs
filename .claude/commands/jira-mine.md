---
description: List your open MariaDB DOCS tickets (assigned to you, not Done).
argument-hint: "(optional filter, e.g. a status like 'inprogress')"
allowed-tools: Read, mcp__atlassian-mariadb__searchJiraIssuesUsingJql, mcp__atlassian-mariadb__atlassianUserInfo, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /jira-mine

Run the **MINE** procedure in `.claude/skills/jira/SKILL.md`.

- Run the skill's **Setup** connection check first.
- Query DOCS tickets assigned to the current user that aren't Done, newest first.
- If `$ARGUMENTS` names a status (e.g. `inprogress`, `review`, `todo`), add it to the JQL.
- Print a compact table: `key · status · summary`.

Filter: $ARGUMENTS
