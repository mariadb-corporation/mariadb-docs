---
description: Report a broken Claude Code skill — file a DOCS Jira Task labeled claude-skill-bug and return the URL.
argument-hint: <skill name> (e.g. jira, doc-from-ticket)
allowed-tools: Bash, Read, Grep, Glob, mcp__atlassian-mariadb__createJiraIssue, mcp__atlassian-mariadb__atlassianUserInfo, mcp__atlassian-mariadb__lookupJiraAccountId, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /skill-bug

Run the **`report-skill-bug`** skill (`.claude/skills/report-skill-bug/SKILL.md`) for the skill
in `$ARGUMENTS`.

In short (full procedure + redaction rules + failure modes in the skill):
1. Confirm the skill exists; gather env (Claude Code / OS / shell) and the invocation /
   expected / actual.
2. Run the `jira` connection check, then create a DOCS **Task** labeled **`claude-skill-bug`**,
   **assigned** (skill owner or current user) so it isn't lost, with secrets redacted.
3. Return the ticket URL.

Skill: $ARGUMENTS
