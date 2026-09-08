# Skill proposal: `prep-changelog`

**Proposer:** @dbart
**Owner(s):** @dbart
**Date:** 2026-09-08
**Related tickets:** [DOCS-6612](https://mariadbcorp.atlassian.net/browse/DOCS-6612)

## Problem

This skill makes it possible for any team member to easily create Community Server changelog
pages. Previously to do so you needed to run the `prep-changelog` script manually and then paste
the output into a pre-prepared page. The steps were all manual and so rife with chances for errors
to creep in.

## Why a skill (not a script/hook)

A skill can read the TODO ticket and derive the variables the `prep-changelog` script needs
itself.

## Proposed invocation

A slash command like this: `/prep-changelog DOCS-6610`, deriving everything from the linked TODO
ticket and asking for anything it can't figure out.

## Overlap with existing skills

| Existing skill | Overlap? |
|----------------|----------|
| `bulk-campaign` | No overlap |
| `doc-from-ticket` | No overlap |
| `doc-impact` | No overlap |
| `docs-check` | Used — to validate the pages |
| `gitbook-canonical` | No overlap |
| `gitbook-format` | No overlap |
| `gitbook-redirects` | No overlap |
| `jira` | Used — for the ticket workflow |
| `new-page` | Overlaps in that both scaffold a page with frontmatter and a `SUMMARY.md` nav entry, but `prep-changelog` should keep its own changelog page templates, which are different from a standard documentation page |
| `propose-improvement` | No overlap |
| `report-skill-bug` | No overlap |
| `style-apply` | No overlap |
| `verify-claims` | No overlap |

## Tools it will call

Bash for the script, the Jira MCP for the ticket. No untrusted input.

## Dogfood plan

[DOCS-6610](https://mariadbcorp.atlassian.net/browse/DOCS-6610) for 13.0.2, and the next two
Community Server release rounds.

## Rollout

Merge it and try it on the next release round.

## Alternatives considered

_TBD — fill before opening PR_
