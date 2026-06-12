---
description: Turn a MariaDB DOCS ticket into a source-verified documentation edit (verifies claims against local MariaDB source, then drafts the page edit).
argument-hint: DOCS-XXXX
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, WebFetch, mcp__atlassian-mariadb__getJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /doc-ticket

Run the **`doc-from-ticket`** skill (`.claude/skills/doc-from-ticket/SKILL.md`) for the ticket in
`$ARGUMENTS`.

In short (the skill has the full procedure and guardrails):
1. First run configures the local MariaDB source repos (`.claude/doc-sources.local.json`,
   gitignored); later runs reuse it.
2. Run the `jira` skill's connection check, fetch the DOCS ticket, parse the MDEV / Release
   Series / PR trail.
3. **Verify every factual claim against local source** (read-only `git -C <repo> grep/show`,
   pinning the commit SHA) — flag anything unverifiable rather than asserting it.
4. Locate the target `.md`, draft the GitBook edit (delegating block/link syntax to
   `gitbook-format`), and **present — don't apply — by default**. Never push/commit/PR.

Ticket: $ARGUMENTS
