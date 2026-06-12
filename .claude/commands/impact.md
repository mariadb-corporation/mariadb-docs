---
description: Analyze a MariaDB source change (MDEV ticket, DOCS ticket, or MariaDB/server PR/commit) for its documentation impact — what's user-facing, whether docs are needed, which pages, and claims to verify. Produces a report; does not edit.
argument-hint: MDEV-XXXXX | DOCS-XXXX | a MariaDB/server PR URL or commit SHA
allowed-tools: Bash, Read, Grep, Glob, WebFetch, mcp__atlassian-mariadb__getJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources
---

# /impact

Run the **`doc-impact`** skill (`.claude/skills/doc-impact/SKILL.md`) for `$ARGUMENTS`.

It's the "explain" / triage step **before** drafting:
1. Resolve the input (DOCS ticket → its MDEV/PR; MDEV → public `jira.mariadb.org`; or a
   `MariaDB/server` PR/commit) and get the **actual diff** from local source (read-only,
   pinned to a SHA), reusing `doc-from-ticket`'s `.claude/doc-sources.local.json` config.
2. Classify the **user-facing surface** (variables, syntax, options, errors, behavior changes).
3. Decide **docs needed? YES/NO/MAYBE**, which page(s), and list the **claims to verify**.
4. Output the impact report and recommend the next step — usually `/doc-ticket DOCS-XXXX` to
   draft (or `/jira-create` to file the DOCS ticket first).

**Analysis only — never edits, commits, or pushes.** A clean "NO docs needed" for an
internal-only change is a valid result.

Input: $ARGUMENTS
