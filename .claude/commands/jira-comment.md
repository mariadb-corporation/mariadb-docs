---
description: Add a comment to a DOCS ticket.
argument-hint: DOCS-XXXX <comment text>
allowed-tools: Read, mcp__atlassian-mariadb__addCommentToJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /jira-comment

Run the **COMMENT** procedure in `.claude/skills/jira/SKILL.md`.

- Run the skill's **Setup** connection check first.
- Parse `$ARGUMENTS` into the ticket key (`DOCS-XXXX`) and the comment body.
- Post via `addCommentToJiraIssue` with `contentFormat="markdown"`.
- Echo the ticket key and a one-line confirmation.

Input: $ARGUMENTS
