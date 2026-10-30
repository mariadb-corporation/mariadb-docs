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

The same is true of every other changelog. Connector changelogs come from a `git log` one-liner
per connector followed by hand-escaping. Enterprise Server changelogs come from a generator outside
this repo, pasted into a page by hand.

## Scope (expanded 2026-10-13)

The proposal began as Community Server only. Built under DOCS-6612, the skill covers:

- **Community Server.** The range rules (`-m`, `-x`, first-RC handling) are unchanged, but the
  `prep-changelog` script is no longer run. `.claude/hooks/changelog-lines.py server` reproduces
  its output with read-only `git log`. That removes the `git reset --hard` hazard described under
  *Alternatives considered* instead of guarding against it. On 13.0.2, 13.1.1, 11.8.9, 11.4.13,
  and 10.6.26 it matched the published commit lists and order exactly.
- **All seven connectors** (C, C++, J, Node.js, ODBC, Python, R2DBC), including the three whose
  changelogs are written by the connector developers. The line format differs by connector *and*
  by series, so `changelog-lines.py connector` infers it from the previous page in the series,
  and `--verify` proves the inference by regenerating that page first. It reproduced 13 of 16
  published pages exactly. The other three differ only by hand edits to commit subjects.
- **Enterprise Server, as scaffold-and-paste.** The generator stays with Daniel. The skill builds
  the page shell, takes the pasted list, and checks its escaping.
- **The `mariadb_repo_setup` and `mariadb_es_repo_setup` scripts.** Each has one changelog page for
  every version. The version is a date, and the entries are the script's own `# Notes:` comments.
  `changelog-lines.py repo-setup` reads the script at the uploaded commit in
  `mariadb-enterprise-scripts`, regenerates all 78 entries of each page (the ES page exactly), and
  prints the sha256 row for the Versions table on the "Package Repository Setup and Usage" page.

Out of scope: MaxScale's per-series changelog, which is a curated feature list rather than a commit
list. Also out of scope: the release notes, Post Download, and `all-releases.md` pages of a round,
which the skill lists as remaining work.

## Why a skill (not a script/hook)

A skill can read the TODO ticket and derive the variables the `prep-changelog` script needs
itself.

## Proposed invocation

A slash command like this: `/prep-changelog DOCS-6610`, deriving everything from the linked TODO
ticket and asking for anything it can't figure out. `/prep-changelog odbc 3.2.11` works too, for
the connectors that have no TODO ticket and release from tags.

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

Bash for `changelog-lines.py` and read-only `git`, the Jira MCP for the DOCS ticket, and a GET-only
`curl` for the TODO ticket on `jira.mariadb.org`. Commit subjects are untrusted text that the
page renders, so the generator escapes them. That escaping is what keeps an `<subquery>` from
vanishing (DOCS-6717).

## Dogfood plan

[DOCS-6610](https://mariadbcorp.atlassian.net/browse/DOCS-6610) for 13.0.2, and the next two
Community Server release rounds, plus the next ODBC or C++ round, since those changelogs are the
docs team's to write.

## Rollout

Merge it and try it on the next release round.

## Alternatives considered

**Keep the status quo — run the script by hand and paste the output.** This is how DOCS-6610
(13.0.2) was done, and it is what motivates the proposal. Three things had to be got right by
hand, none of them obvious:

- `-m` and `-x` are not on the TODO ticket. `-m` is the *minor number* of the previous release in
  the series, and `-x` is the release commit of the latest release in the previous non-EOL series
  (for 13.0.2, the `mariadb-12.3.3` tag commit). Getting `-x` wrong silently duplicates or drops a
  whole series' worth of commits, and nothing downstream catches it.
- The script's raw output is not publishable. Published changelogs escape `` ` ``, `_`, `*` and
  `&` in commit subjects; the script emits them raw, so one MDEV-40153 subject arrived with bare
  `*` characters in a C++ signature that would have rendered as emphasis.
- The script does `git checkout <branch>` then `git reset --hard <rev>` on the shared server clone
  with no error handling, so if the branch has not been fetched the checkout fails silently and
  the reset rewrites whatever branch you happened to be on.

**Grow the `prep-changelog` shell script instead of adding a skill.** Rejected for the reason in
*Why a skill* above: the hard part is reading the release TODO ticket and deriving the arguments,
which a shell script cannot do, and it cannot ask the writer for what it cannot infer.

**Extend `doc-from-ticket` rather than add a new skill.** Not chosen because that skill's job is
verifying prose claims against MariaDB source, whereas a release changelog is generated output
plus fixed boilerplate — different input, no source-claim verification, and a different notion of
"done".

**Trigger it from a hook or CI job.** Rejected: the trigger is a person deciding a release round
is ready, not a repository event, and the round still needs a writer's judgment — whether the
version is the series' *initial GA* changes the release notes body entirely (copied from the
Changes & Improvements page) versus a later release (a grouped notable-MDEV listing).
