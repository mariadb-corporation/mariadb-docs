---
description: Build a release's changelog page (Community Server, any connector, Enterprise Server, or the mariadb_repo_setup / mariadb_es_repo_setup scripts) from its TODO ticket and tags, with the revision list generated read-only and its format proven first.
argument-hint: DOCS-XXXX | <product> <version> | mariadb_repo_setup | mariadb_es_repo_setup
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, mcp__atlassian-mariadb__getJiraIssue, mcp__claude_ai_Atlassian_Rovo__getJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources, mcp__claude_ai_Atlassian_Rovo__getAccessibleAtlassianResources
---

# /prep-changelog

Run the **`prep-changelog`** skill (`.claude/skills/prep-changelog/SKILL.md`) for `$ARGUMENTS`.

In short (the skill has the full procedure and guardrails):
1. Resolve the product, version, and release TODO ticket, and read the previous changelog page in
   the same series. That page is the template.
2. Derive the commit range. For Server, that includes the start tag and the exclude commit, neither
   of which is on the ticket.
3. **Prove the format first:** `changelog-lines.py --verify` must regenerate the template page from
   its own range before the new list is generated.
4. Generate the revision list read-only, act on every warning, and assemble the page, its
   `SUMMARY.md` entry, and the release notes page's Changelog link. Enterprise Server is
   scaffold-and-paste. The two repo-setup scripts follow their own section: entries come from the
   script's `# Notes:` block at the uploaded commit in `mariadb-enterprise-scripts`, and a release
   also adds a sha256 row to the Versions table on the "Package Repository Setup and Usage" page.
5. Run `docs-check`, then report the range with full SHAs and the round's remaining work. Never
   run `prep-changelog` or a developer's recipe in a working clone, and never commit or push.

Target: $ARGUMENTS
