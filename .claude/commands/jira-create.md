---
description: File a new MariaDB DOCS ticket (Task by default) with sensible defaults; prompts only for genuine choices.
argument-hint: <free-form description of the doc work> (prefix "epic:" for an Epic)
allowed-tools: Bash, Read, Grep, Glob, mcp__atlassian-mariadb__createJiraIssue, mcp__atlassian-mariadb__getJiraIssueTypeMetaWithFields, mcp__atlassian-mariadb__atlassianUserInfo, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /jira-create

Run the **CREATE** procedure in `.claude/skills/jira/SKILL.md` for the description in
`$ARGUMENTS`.

- Run the skill's **Setup** connection check first.
- Issue type: **Task** by default (Epic only if the user types `epic:`); narrate it, don't ask.
- Summary: derive a one-sentence summary and confirm it.
- Priority: default **Major**; override only on an explicit signal.
- Create via `createJiraIssue` (project `DOCS`, `contentFormat="markdown"`); add optional fields
  only when asked. Confirm with `Ticket / Type / Priority / URL`.

Description: $ARGUMENTS
