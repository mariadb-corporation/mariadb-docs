---
description: Review GitBook-UI edits from the nightly digest — sort reformatting from content, check the content, propose fixes; asks before any PR, merge or Slack post.
argument-hint: "(optional) today | <sha> | <digest permalink> — omit for the unreviewed digest posts"
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, mcp__claude_ai_Slack__slack_read_channel, mcp__claude_ai_Slack__slack_read_thread, mcp__claude_ai_Slack__slack_get_reactions, mcp__claude_ai_Slack__slack_send_message, mcp__claude_ai_Slack__slack_add_reaction
---

# /gitbook-review

Run the **`gitbook-review`** skill (`.claude/skills/gitbook-review/SKILL.md`) for `$ARGUMENTS`.

1. Setup: inside the mariadb-docs clone, `origin` → `mariadb-corporation/mariadb-docs`,
   `git fetch origin`. Slack is optional; without it, ask for the SHA(s).
2. Collect the commits **by SHA** (never by `GITBOOK-<n>`): from the unreviewed digest posts in
   #docs-notifications, the given SHA, or the given post.
3. Per commit: sort every change into GitBook reformatting or content, review the content, and
   print the per-commit result with a proposed action.
4. **Stop for approval.** Then carry out only the approved actions: fix forward or revert single
   pages in a PR. Never `git revert` a whole commit; never touch a synced Community Tools page.
5. Draft the digest-thread reply; post it only after confirmation.

Input: $ARGUMENTS
