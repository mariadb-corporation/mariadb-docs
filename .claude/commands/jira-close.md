---
description: Close a DOCS ticket after its doc PR is merged — transition to Closed.
argument-hint: DOCS-XXXX (optional — inferred from the current branch if omitted)
allowed-tools: Bash, Read, Grep, Glob, mcp__claude_ai_Atlassian_MCP__getJiraIssue, mcp__claude_ai_Atlassian_MCP__executeRead, mcp__claude_ai_Atlassian_MCP__transitionJiraIssue, mcp__claude_ai_Atlassian_MCP__addOrEditJiraIssueComment, mcp__claude_ai_Atlassian_MCP__getAccessibleAtlassianResources, mcp__atlassian-mariadb__getJiraIssue, mcp__claude_ai_Atlassian_Rovo__getJiraIssue, mcp__atlassian-mariadb__getTransitionsForJiraIssue, mcp__claude_ai_Atlassian_Rovo__getTransitionsForJiraIssue, mcp__atlassian-mariadb__transitionJiraIssue, mcp__claude_ai_Atlassian_Rovo__transitionJiraIssue, mcp__atlassian-mariadb__addCommentToJiraIssue, mcp__claude_ai_Atlassian_Rovo__addCommentToJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources, mcp__claude_ai_Atlassian_Rovo__getAccessibleAtlassianResources
---

# /jira-close

Run the **CLOSE** procedure in `.claude/skills/jira/SKILL.md` for `$ARGUMENTS`.

- Run the skill's **Setup** connection check first.
- Resolve the key (arg or current-branch prefix); stop if already Closed.
- **Confirm the PR is merged** before closing — don't close unmerged work; ask if unsure.
- Transition to **`Closed`** (match by name); optionally comment with the merge commit.
- If the ticket was filed from a GitHub issue (`Issue created automatically from Github Issue:`
  in the description) and that issue is still open, draft a closing comment, show it, and close
  the issue on confirmation (skill CLOSE step 5). This also applies when the ticket is already
  Closed.
- Confirm with `Ticket / Status: Closed / GitHub issue: #<n> closed | already closed | none`.

Ticket: $ARGUMENTS
