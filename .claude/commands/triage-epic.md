---
description: Sweep a DOCS release Epic for On Hold children whose upstream MDEV work has landed — check the public MDEV status and local merged commits, then (on approval) post a triage brief and move each ticket On Hold → TODO.
argument-hint: DOCS-XXXX (the release Epic, or any child of it)
allowed-tools: Bash, Read, Grep, Glob, mcp__atlassian-mariadb__getJiraIssue, mcp__claude_ai_Atlassian_Rovo__getJiraIssue, mcp__atlassian-mariadb__searchJiraIssuesUsingJql, mcp__claude_ai_Atlassian_Rovo__searchJiraIssuesUsingJql, mcp__atlassian-mariadb__getJiraIssueRemoteIssueLinks, mcp__claude_ai_Atlassian_Rovo__getJiraIssueRemoteIssueLinks, mcp__atlassian-mariadb__addCommentToJiraIssue, mcp__claude_ai_Atlassian_Rovo__addCommentToJiraIssue, mcp__atlassian-mariadb__getTransitionsForJiraIssue, mcp__claude_ai_Atlassian_Rovo__getTransitionsForJiraIssue, mcp__atlassian-mariadb__transitionJiraIssue, mcp__claude_ai_Atlassian_Rovo__transitionJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources, mcp__claude_ai_Atlassian_Rovo__getAccessibleAtlassianResources
---

# /triage-epic

Run the **`triage-epic`** skill (`.claude/skills/triage-epic/SKILL.md`) for `$ARGUMENTS`.

1. Run the `jira` skill's **Setup** connection check first.
2. Resolve `$ARGUMENTS` to the release Epic (a child key resolves to its parent), then list its
   **On Hold** children via `parent = <EPIC>` JQL — not `issuelinks`, which is empty on these epics.
3. Per child: resolve the **primary MDEV** by the §3 precedence (never a bare grep), then gather
   evidence — public `jira.mariadb.org` status/resolution/fixVersions plus merged, non-reverted
   commits in the local MariaDB source at its authoritative ref.
4. Tier each as READY / CANDIDATE / NOT READY / AMBIGUOUS and print the **dry-run table**.
5. **Stop for approval.** On approval only: post the triage brief and transition On Hold → TODO.

**Dry run by default — writes nothing until you approve.** Read-only against `jira.mariadb.org`
and the source clone. Writes no docs: hand off with `/impact DOCS-XXXX` then `/doc-ticket DOCS-XXXX`.

Input: $ARGUMENTS
