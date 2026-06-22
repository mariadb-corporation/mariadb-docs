# jira-chase — skill proposal

**Proposer:** @shinz
**Owner(s):** @shinz
**Date:** 2026-06-22
**Related tickets:** [DOCS-6274](https://mariadbcorp.atlassian.net/browse/DOCS-6274)

## Problem

Remind Jira DOCS ticket reviewers to perform their review.

## Why a skill (not a script/hook)

Needs Claude's judgment, like reading Jira comment threads to figure out who the reviewer(s) is/are, and whether they've since replied, then compose a reminder.

## Proposed invocation

`/jira-chase` with no args chases all Review tickets; draft-and-confirm before sending.

## Overlap with existing skills

| Existing skill | Overlap / boundary |
|----------------|--------------------|
| bulk-campaign | Unrelated. |
| doc-from-ticket | Unrelated. |
| doc-impact | Unrelated. |
| docs-check | Unrelated. |
| gitbook-canonical | Unrelated. |
| gitbook-format | Unrelated. |
| jira | Lives inside `jira` as a NUDGE procedure. |
| new-page | Unrelated. |
| propose-improvement | Unrelated. |
| report-skill-bug | Unrelated. |
| style-apply | Unrelated. |

## Tools it will call

Calls the Jira MCP for comments/status, and the Slack MCP to find reviewers and send them messages.

Reads untrusted input? _TBD — fill before opening PR_ (reads Jira ticket comments authored by others.)

## Dogfood plan

1. Chase reviewers across all current Review-status tickets (the session that prompted this proposal: DOCS-6271, DOCS-6232, DOCS-6163, DOCS-6182, DOCS-6239).
2. A single-ticket chase.
3. A run where some reviewers already replied (verify they're correctly skipped).

## Rollout

Land the NUDGE procedure in the `jira` skill + add a `/jira-chase` command, dogfood solo for a week, then announce to the docs team as part of the Claude rollout.

## Alternatives considered

- **Standalone sibling skill** (`jira-chase` as its own dir) — rejected in favor of a NUDGE procedure inside `jira`, reusing its setup/connection plumbing.
- **GitHub's native reviewer-request feature** — doesn't fit, since reviewers are tracked in Jira ticket comments / @-mentions, not the PR's reviewer field.
- **A scheduled cloud routine** — complements rather than replaces the on-demand command (used in the originating session to chase non-responders after 3 days).
