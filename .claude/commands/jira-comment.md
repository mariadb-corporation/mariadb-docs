---
description: Add a comment to a DOCS ticket.
argument-hint: DOCS-XXXX <comment text>
allowed-tools: Read, mcp__claude_ai_Atlassian_MCP__addOrEditJiraIssueComment, mcp__claude_ai_Atlassian_MCP__getAccessibleAtlassianResources, mcp__atlassian-mariadb__addCommentToJiraIssue, mcp__claude_ai_Atlassian_Rovo__addCommentToJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources, mcp__claude_ai_Atlassian_Rovo__getAccessibleAtlassianResources
---

# /jira-comment

Run the **COMMENT** procedure in `.claude/skills/jira/SKILL.md`.

- Run the skill's **Setup** connection check first.
- Parse `$ARGUMENTS` into the ticket key (`DOCS-XXXX`) and the comment body.
- Post via `addOrEditJiraIssueComment` on v2 (markdown is the default), or
  `addCommentToJiraIssue` with `contentFormat="markdown"` on a v1 connection.
- Echo the ticket key and a one-line confirmation.

Input: $ARGUMENTS
