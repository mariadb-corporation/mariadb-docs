---
name: prep-changelog
description: Build a release's changelog page in mariadb-docs: MariaDB Community Server, any of the seven connectors (C, C++, J, Node.js, ODBC, Python, R2DBC), Enterprise Server, or a new version of the mariadb_repo_setup / mariadb_es_repo_setup scripts (single-page changelogs fed from the scripts' own Notes comments, plus the sha256 Versions table). Derives the commit range from the release TODO ticket and the tags, generates the revision list read-only with .claude/hooks/changelog-lines.py after proving its format against the previous page, and assembles the page, its SUMMARY.md entry, and the release notes page's Changelog link. Enterprise Server is scaffold-and-paste, because its generator is not in this repo. Use when asked to "prep the changelog", "make the changelog for 13.0.3", "do the ODBC 3.2.11 changelog", "update the repo_setup changelog", "/prep-changelog DOCS-XXXX", or as the changelog half of a release-notes round.
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, mcp__atlassian-mariadb__getJiraIssue, mcp__claude_ai_Atlassian_Rovo__getJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources, mcp__claude_ai_Atlassian_Rovo__getAccessibleAtlassianResources
owners: [dbart]
last_verified: 2026-10-13
status: active
---

# prep-changelog

A changelog page is fixed boilerplate around one generated block: a bullet per commit in the
release. The block is the easy part to get wrong silently. A bad range drops or duplicates a whole
series' worth of commits, and nothing downstream notices. So this skill spends its care on the
**range** and the **format**, and proves both before writing anything.

Proposal and rationale: `dev-docs/skill-proposals/0002-prep-changelog.md` (DOCS-6612).

## What it does and doesn't do

- **Does:** the changelog page, its `release-notes/SUMMARY.md` entry (and a series group if this is
  the series' first changelog), and the Changelog link on the release notes page.
- **Also does:** a new version of `mariadb_repo_setup` or `mariadb_es_repo_setup`, which works
  differently. See *Repo-setup scripts*.
- **Doesn't:** write the release notes page, the Post Download page, `all-releases.md`, or the
  `latest-*` / `most-recent-*` includes. Those belong to the same round, so list them as remaining
  work at the end, but leave them alone.
- **Never runs** `mariadb.org-tools/release/prep-changelog`, or a connector developer's
  `git pull && git checkout` recipe, in anyone's working clone. The script does `git checkout
  <branch>` then `git reset --hard <rev>` with no error handling: an unfetched branch makes the
  checkout fail silently and the reset rewrites whatever branch was checked out.
  `changelog-lines.py` reproduces its output with read-only `git log`, so it is never needed.
- **Never commits or pushes.** Present the result. The writer reviews and commits.

## Inputs

`/prep-changelog DOCS-XXXX`, or a product and version (`/prep-changelog odbc 3.2.11`,
`/prep-changelog server 13.0.3`). From a DOCS ticket, fetch it with the `jira` skill (run its
**Setup** check first) and read the product and versions from the summary and description.

Then get the **release TODO ticket** on `jira.mariadb.org`. It is Jira *Server*, so the Atlassian
MCP cannot reach it. Use a GET with a personal access token, never a write:

```bash
curl -s -H "Authorization: Bearer $(cat ~/.config/jira-claude-access-token)" \
  "https://jira.mariadb.org/rest/api/2/issue/TODO-NNNN?fields=summary,description,comment"
```

Search by summary if the DOCS ticket doesn't name the TODO (`project=TODO AND summary~"13.0.3"`).

| Product | TODO ticket? | What it carries |
|---------|--------------|-----------------|
| Community Server | Yes, `Release Community Server X.Y.Z …` | A table of Version · Branch (`bb-X.Y-release`) · Revision · tarbuildnum, one row per release in the round |
| Connector/ODBC | Yes, `Connector/ODBC X.Y.Z … GA Release` | `ver=`, `branch=`, `commit=` blocks, one per series |
| C, C++, J, Node.js, Python, R2DBC | Usually none | Developers release straight from tags; use the tags |

**The release date** comes from Daniel's "Releases Published" comment on the TODO ticket, not the
planned date in its description, which slips. If the round has not shipped, the date is unknown:
see *Unreleased rounds* below.

## Where pages live

| Product | Changelog page | Template = previous page in the same series |
|---------|----------------|---------------------------------------------|
| Community Server | `release-notes/community-server/changelogs/<X.Y>/<X.Y.Z>.md` | yes |
| Connector/C, C++, J, ODBC, Python | `release-notes/connectors/<c\|c++\|java\|odbc\|python>/changelogs/<X.Y>/<X.Y.Z>.md` | yes |
| Connector/Node.js | `release-notes/connectors/node.js/changelogs/<N>.x/<X.Y.Z>.md` (by major version) | yes |
| Connector/R2DBC | `release-notes/connectors/r2dbc/changelogs/<X.Y.Z>.md` (flat) | yes |
| Enterprise Server | `release-notes/enterprise-server/<X.Y>/changelog-<X.Y.Z-N>.md` (prefix form) | yes |
| `mariadb_repo_setup`, `mariadb_es_repo_setup` | `release-notes/tools/mariadb-repo-setup-changelog.md`, `…/mariadb-es-repo-setup-changelog.md`: **one page each, new entries on top** | not applicable; see *Repo-setup scripts* below |

Read the template before anything else. The page structure, the revision-line format, and the
footer all come from it, and they differ by product **and** by series (Connector/Python 1.1 is
nested and 2.0 is flat). Never normalize one product's pages to another's style.

## Step 1: the range

### Community Server

The range is `mariadb-<X.Y>.<prev>..<rev>`, minus everything reachable from the **exclude**
commit. `<rev>` is the Revision in the TODO table. Neither the start nor the exclude is on the
ticket:

- **Start:** the tag of the previous release in the same series, `mariadb-<X.Y>.<prev>`.
  **First RC (`.1`) exception:** Preview (`.0`) releases are not tagged and get no changelog page,
  so the first RC's changelog covers `.0` and `.1` together. Its start *is* the exclude commit.
- **Exclude:** the **release commit** of the latest release in the next-older maintained series, in
  the same round where there is one: 12.3.3 for 13.0.2, 13.0.2 for 13.1.1, 11.4.13 for 11.8.9,
  10.6.28 for 10.11.19. The page's `* Includes all fixes from [MariaDB …]` bullet names the same
  release, so the two must agree. The oldest maintained series has no exclude.
  - Use the commit, not the tag name. `git rev-parse mariadb-12.3.3` returns the annotated *tag's*
    SHA, so use `mariadb-12.3.3^{commit}`; the script does.
  - **The exclude release may be untagged, or not even announced yet**, when its round ships
    together with this one. Then take its Revision from **that round's TODO** and check it with
    `git merge-base --is-ancestor <ex> <rev>`: it must pass, or the exclude is not in this
    history and silently drops nothing. A tag created later can point at a newer commit, so
    re-running an old page against the tag may differ by a commit or two. 10.11.19 is an example.

Run against the server source clone, the `server` entry in `.claude/doc-sources.local.json`.
`changelog-lines.py` only runs `git log` and `git rev-parse`. If a ref is missing it says so. Fetch
with `git -C <server> fetch origin --tags`, which changes no branch or working tree. Never check
out or reset anything in that clone. It is pinned to a ref for other skills.

### Connectors

The range is `<prev-tag>..<this release>`:

- **Tags:** Connector/C and Python tag `v3.4.11`, `v1.1.14`. C++, J, Node.js, ODBC, and R2DBC tag
  bare `1.1.9`, `3.5.10`.
- **End of range:** the tag. For ODBC, the TODO's `commit=`. If both exist they must name the same
  commit. If they differ, the TODO commit is the release, so use it and say so.
- **First release of a series:** there is no previous tag in the series. Pick the base on purpose:
  the fork point (`git merge-base` with the older series' branch) or the last release the new
  series counts from. Then add a sentence to the page, as C++ 1.0.0 does: `This changelog lists the
  changes since Connector/C++ 0.9.4.`
- **Dates and maturity** come from the release notes page, not from the tag date. Tags are often
  created days after the release.

Work in a **scratch blobless clone** in the session scratchpad, never in a working clone under
`~/src`. Those are people's working trees, and the developers' recipes pull and switch branches
in them:

```bash
git clone -q --filter=blob:none --no-checkout \
  https://github.com/mariadb-corporation/mariadb-connector-<c|cpp|j|nodejs|odbc|python|r2dbc>.git "$SP/<name>"
```

## Step 2: prove the format, then generate

`.claude/hooks/changelog-lines.py` produces the revision block. For connectors it **infers the
format from the template page**: hash length, nested vs. flat, separator, the date `<mark>`, `]`
escaping, issue-key linking, and commit order. Its header explains each.

**Always verify first.** Regenerate the *template* page from the template's own range and diff.
For example, for ODBC 3.2.11 the template is 3.2.10:

```bash
python3 .claude/hooks/changelog-lines.py connector --verify \
  --template release-notes/connectors/odbc/changelogs/3.2/3.2.10.md \
  --repo "$SP/mariadb-connector-odbc" --range 3.2.9..3.2.10
```

For Server, verify against the previous release's page and its own range and exclude:

```bash
python3 .claude/hooks/changelog-lines.py server --repo <server> \
  --start mariadb-13.0.1 --rev mariadb-13.0.2 --exclude mariadb-12.3.3 \
  --verify release-notes/community-server/changelogs/13.0/13.0.2.md
```

Read the diff:

- **Revisions added, removed, or moved:** the range rule is wrong for this series, or the template
  was built from a different range. Stop and find out why before generating. Never "fix" it by
  editing lines.
- **Text differences inside subjects only:** hand edits by the page's author (a typo corrected, an
  identifier renamed) or a broken published line the generator escapes correctly (an unescaped
  `<CONFIG>` that GitBook dropped, a bare `*` that renders as emphasis). Fine, so carry on.

Then generate the new block. Pass `--version` for connectors so version-bump warnings work:

```bash
python3 .claude/hooks/changelog-lines.py connector \
  --template <previous page> --repo "$SP/mariadb-connector-odbc" \
  --range 3.2.10..3.2.11 --version 3.2.11 > "$SP/lines.md"
```

**Read every warning** on stderr, and decide each one rather than ignoring it:

- **A mismatched issue-key bracket** (`[CONJ-1333}`): fix the line by hand, the way the published
  pages do.
- **A version bump naming another version:** a merge from another series brought in its bump
  commit. Connector/C 3.4.11's page omits 3.3.21's. Drop it, and tell the writer that you did.
- **An unbalanced backtick:** check the line renders.

## Step 3: assemble the page

Copy the template page and change only what belongs to the release:

1. **Frontmatter `description:`**, in the Server form with an ISO date and no final period:
   `MariaDB 13.0.3 is a Stable (GA) release of MariaDB Community Server 13.0, released on
   2026-11-12`. For a connector: `MariaDB Connector/ODBC 3.2.11 is a Stable (GA) release of MariaDB
   Connector/ODBC 3.2, released on 2026-11-12`. This applies even where older pages in the tree say
   `Full changelog for …` or `published 29 September 2026`. Don't rewrite those older pages.
   Enterprise changelogs keep `hidden: true`. **Every** Enterprise changelog has it: the page is
   reached only by its Changelog button. It does not mean the release is unreleased.
2. **H1**, the button row (Release Notes link, self link), the Server-only `Alternate download`
   line, and any `{% include "…/latest-<x>.md" %}` the template carries.
3. **`**Release date:**`** in body form with a three-letter month: `12 Nov 2026`.
4. **The "For the highlights" link**, and on Server the GitHub compare link,
   `compare/mariadb-<X.Y.prev>...mariadb-<X.Y.Z>`.
5. **Server leading bullets**, written by hand above the revision list:
   - always, when there is an exclude: `* Includes all fixes from [MariaDB <ex>](../<ex series>/<ex>.md)`
   - first RC only, before that line: `* Changes from the [MariaDB <X.Y> Preview](../../<X.Y>/mariadb-<X.Y>-changes-and-improvements.md) are also included in this changelog`
6. **The revision block**: replace the template's block with the generated one.
7. **The footer**: keep the template's footer as it is. License lines differ by product and are not
   the skill's to change.

**Enterprise Server is scaffold-and-paste.** Daniel runs the generator, which is not in this repo,
and its output is the changelog's bullet list. Build steps 1–4 from the previous Enterprise
changelog (prefix filename `changelog-<ver>.md`, `hidden: true`), leave a clearly marked gap, and
**ask for the paste**. Then check it: no unescaped `<` outside code spans (DOCS-6717), no `*`
that would render as emphasis, and links that are absolute `jira.mariadb.org` URLs.

## Step 4: nav and links

- **`release-notes/SUMMARY.md`:** add the entry directly above the previous release in the same
  group, newest first, matching that group's link text exactly (`[MariaDB 13.0.3 Changelog]`,
  `[Connector/ODBC 3.2.11 Changelog]`, `[Changelog for MariaDB Enterprise Server 11.8.10-7]`). A
  series' first changelog needs its group README too, copied from the previous series (`Changelogs
  - MariaDB 13.2 Series`). `navcheck` fails a page with no `SUMMARY.md` entry, because that page
  would publish nowhere.
- **The release notes page:** its Changelog button and its "see the changelog" sentence must point
  at the new page. If the release notes page does not exist yet, say so. Don't create it.

## Repo-setup scripts

`mariadb_repo_setup` (Community Server) and `mariadb_es_repo_setup` (Enterprise Server) work
differently from everything above. Skip Steps 1–4 for them and follow this section.

- **One page per script, for every version ever.** A release adds an entry at the top of the
  existing page. It never creates a page or a `SUMMARY.md` entry.
- **The version is a date.** It's the `version="YYYY-MM-DD"` on line 4 of the script, which
  `--version` prints. There are no tags, no series, and no commit range.
- **The changelog is the script's own `# Notes:` comment block**, one dated entry per version,
  newest first, with items wrapped across comment lines. The page reproduces it, which is why its
  intro says the entries are "reproduced from the changelog comments at the top of the script".
- **The scripts live in `~/src/mariadb-corporation/mariadb-enterprise-scripts`**, the
  `enterprise-scripts` entry in `.claude/doc-sources.local.json`. The release is the file **at
  the commit that was uploaded to the CDN**, and the published checksum is generated from that file
  just before upload. So read it from git at that commit, and never from a working copy, which
  may carry unreleased edits. `changelog-lines.py` uses `git show <rev>:<name>` and changes
  nothing in the clone.
- **The release-day commit** moves `version=` *and* the newest Notes date to the release date,
  and strips `TODO-NNNN` identifiers from the notes. 4171898 did all three for 2026-09-15. So a
  commit whose `version=` disagrees with its newest note, or whose notes still carry `TODO-`, is
  not the release. The script warns on both. Ask which commit was uploaded rather than guess.

```bash
E=~/src/mariadb-corporation/mariadb-enterprise-scripts
# 1. Prove the format: every entry on the page must regenerate from the released script.
python3 .claude/hooks/changelog-lines.py repo-setup --repo "$E" --rev <release commit> \
  --name mariadb_es_repo_setup --page release-notes/tools/mariadb-es-repo-setup-changelog.md --verify
# 2. The new entries, plus the version and sha256 (on stderr).
python3 .claude/hooks/changelog-lines.py repo-setup --repo "$E" --rev <release commit> \
  --name mariadb_es_repo_setup --page release-notes/tools/mariadb-es-repo-setup-changelog.md
```

In `--verify`, an entry that is added, removed, or redated means the wrong commit, so stop.
Wording differences are hand edits on the page. The Community page has two: a misspelling of "unneeded" was
corrected, and "release series" was added to the 2026-09-15 entry. Keep them.

A release touches **two** pages:

1. **The changelog page.** Insert the generated entries directly above the current newest
   `* **YYYY-MM-DD**` entry. Nothing else on the page changes.
2. **"MariaDB Package Repository Setup and Usage"**
   (`server/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage.md`),
   section `## Versions`. Add the printed `| <version> | `<sha256>` |` row at the **top** of that
   script's table, in the matching tab. The download-and-verify examples near the top use a
   `${checksum}` variable and never change.

Cross-check before you finish. If the script has reached the CDN, its download must hash to the
same value: `curl -sL https://r.mariadb.com/downloads/mariadb_repo_setup | sha256sum`, or
`https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup` for Enterprise. A
mismatch means the wrong commit, or an upload that differs from git. Stop and ask. A script not
yet uploaded is an unreleased round (below).

Report anything else the version's notes change that the setup page describes, such as a new
default series, a newly supported OS, or a new option. The page's *Current Supported Major
Versions*, *Supported Distributions*, and *Full List of Options* sections may need it. Flag it,
but don't edit it here.

## Unreleased rounds

If the round has not shipped (no "Releases Published" comment), the page still gets built. In that
case:

- Add `hidden: true` **and** the unreleased banner (`{% include
  "…/.gitbook/includes/unreleased-<x-y>.md" %}`) to the changelog. Create the include from an
  existing one if the series lacks it. The release notes page needs the same treatment; report it,
  don't do it.
- Leave the date as `TBD` in both places, and keep the `SUMMARY.md` entry.
- **The DOCS ticket does not close on merge.** Release-day updates (dates, removing the banner and
  `hidden`) are part of it. Say so in the summary.

## Step 5: check and report

Run `docs-check` (or `.claude/hooks/doc-lint.sh <files>`) on every changed file, and
`python3 .claude/hooks/navcheck.py new origin/main`. Then report:

- the range used, with full SHAs: start, end, and exclude for Server, plus where each came from (tag,
  TODO ticket, `merge-base`)
- the `--verify` result on the template, and every warning with what you did about it
- the files changed
- what the round still needs that this skill does not do: release notes page, Post Download page,
  `all-releases.md`, `latest-*` and `most-recent-*` includes, and release-day updates if
  unreleased

Put the range and the verify result in the PR body too. It is the only record of how the list was
made.
