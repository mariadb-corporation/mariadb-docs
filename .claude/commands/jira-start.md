---
description: Start work on a DOCS ticket — create a DOCS-XXXX feature branch from main and move the ticket to IN PROGRESS.
argument-hint: DOCS-XXXX (or a mariadbcorp.atlassian.net/browse/ URL)
allowed-tools: Bash, Read, Grep, Glob, mcp__atlassian-mariadb__getJiraIssue, mcp__atlassian-mariadb__getTransitionsForJiraIssue, mcp__atlassian-mariadb__transitionJiraIssue, mcp__atlassian-mariadb__editJiraIssue, mcp__atlassian-mariadb__atlassianUserInfo, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /jira-start

Run the **START** procedure in `.claude/skills/jira/SKILL.md` for the ticket in `$ARGUMENTS`.

Steps (see the skill for full detail and the exact tool payloads):
1. Run the skill's **Setup** connection check first (confirm `atlassian-mariadb` reaches
   `mariadbcorp.atlassian.net`).
2. Fetch the ticket, display it, assign to the current user if unassigned.
3. Reuse the current branch if it's already `DOCS-XXXX-…`, else confirm and cut
   `DOCS-XXXX-short-slug` from `origin/main` with `--no-track`.
4. Transition to `IN PROGRESS` (match the live transition by name).
5. Confirm, and suggest `doc-from-ticket DOCS-XXXX` next.

Ticket: $ARGUMENTS
