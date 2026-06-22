---
name: doc-from-ticket
description: Turn a MariaDB DOCS Jira ticket into a concrete, source-verified documentation edit for mariadb-docs. Fetches the ticket, follows it to the upstream MDEV/source change, VERIFIES the claims against local MariaDB source code, locates the right .md page, and drafts the GitBook edit. Use when asked to "document DOCS-XXXX", "write the docs for this ticket", or "draft the page for <DOCS ticket>".
allowed-tools: Bash, Read, Grep, Glob, Edit, Write, WebFetch, mcp__atlassian-mariadb__getJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# doc-from-ticket

Produce a documentation edit from a MariaDB **DOCS** ticket — and **prove every factual claim
against the actual MariaDB source code** before writing it. The verification step is the point
of this skill: documentation that asserts a default, a syntax, or a "since version X" must be
backed by source, not by the ticket prose (which is often a paraphrase or a feature *request*).

References: `dev-docs/space-map.md`, `dev-docs/gitbook-syntax.md`, `dev-docs/link-aliases.md`,
`dev-docs/style-guide.md`. Jira access is via the `jira` skill's config (server
`atlassian-mariadb`, cloudId `164b0d33-…`).

## When to use

"Document DOCS-XXXX", "write the docs for this ticket", "draft the page for <ticket>". Typically
run after `/jira-start DOCS-XXXX` has put you on the ticket's branch.

If a **`doc-impact` report** (`/impact`) is already in the conversation, **reuse it** — its
affected-page list and "claims to verify" are exactly this skill's inputs; don't redo the
change-analysis from scratch. Skip drafting if that report concluded **no docs are needed**. Also
check `reports_dir` for an on-disk skeleton from a prior `/impact` run — find it by key per the
cookbook (`find "$reports_dir" -type d -name 'DOCS-XXXX' -o -name 'MDEV-XXXXX'`); if present, build
on its `PENDING` rows rather than starting fresh — §7 explains the move/rename.

## 0. Source configuration (first-run, then remembered)

Verification needs local MariaDB source. Read the per-user config:

```
.claude/doc-sources.local.json   (gitignored — paths differ per machine/user)
```

Schema:

```json
{
  "sources": [
    { "product": "server",   "path": "/abs/path/to/MariaDB-server", "ref": "main" },
    { "product": "maxscale",  "path": "/abs/path/to/MaxScale",       "ref": "main" }
  ]
}
```

- **If the file is missing or empty (first run):** ask the user which products they work with
  and, for each, the **local repo path** and the **branch/ref to verify against** (the
  authoritative ref — a single default branch per repo, e.g. `main`). Before writing, **validate
  both**:
  - path is a git repo: `git -C <path> rev-parse --git-dir`
  - ref resolves to a commit: `git -C <path> rev-parse --verify <ref>^{commit}`

  Reject and re-prompt on either failure (a mistyped ref must fail here, at config time — not
  mid-verification with a raw git error). Write the file only once both pass.
- **On later runs:** use it silently. If the user says "reconfigure sources" / "add a source",
  update the file.
- **If a needed product has no configured source:** tell the user, and either ask for the path
  or proceed in **degraded mode** (draft from ticket + existing docs only) — but clearly mark
  every claim you could not verify against source. Never silently skip verification.

> Verification uses the configured **single default ref** per repo (not the ticket's Release
> Series). Still record the ticket's `Release Series` in your notes, and if a claim looks
> version-specific, flag that it was verified against `<ref>`, not that series.

The same config file also holds **`reports_dir`** — the directory **outside this repo** where the
fact-check report (§7) is written; it is **never committed**. If `reports_dir` is missing, prompt
and validate it per `dev-docs/cookbook-fact-trail.md` › *Where reports live* (reject any path
inside the repo), then continue.

## 1. Connection check + fetch the ticket

Run the `jira` skill's **Setup** check (confirm `atlassian-mariadb` reaches
`mariadbcorp.atlassian.net`). Then:

```
mcp__atlassian-mariadb__getJiraIssue(cloudId="164b0d33-ee39-4b4d-b1d5-e71a97376560", issueIdOrKey="DOCS-XXXX")
```

## 2. Parse the ticket

MariaDB DOCS tickets (especially `[Auto] Documentation needed` ones) carry a consistent trail:

- **MDEV key** + **Link to ticket** (`jira.mariadb.org/browse/MDEV-XXXXX`) — the upstream change.
- **Release Series** (e.g. `13.1`) — the version the change targets.
- Often a **`github.com/MariaDB/server` PR** link in the body.
- **Summary** and **Original Description**.

Extract these. The MDEV/PR is your pointer into the source. If useful and reachable, `WebFetch`
the public MDEV ticket or the GitHub PR to get exact symbol names / the commit diff — but treat
that as a *lead*, not proof. **The local source at the configured ref is the source of truth.**

## 3. Verify against source (the core step)

**First, make sure the ref is current and pin the commit.** Verifying against a stale local
branch would produce confident-but-wrong docs — the whole point of this skill. So:

```bash
# refresh the configured ref from upstream (don't switch the working tree)
git -C <repo.path> fetch --quiet
# resolve and RECORD the exact commit you are verifying against
sha="$(git -C <repo.path> rev-parse <repo.ref>)"
```

If the local `<ref>` is behind its upstream (e.g. `git -C <path> rev-list --count <ref>..origin/<ref>` > 0),
verify against the upstream-tracking ref (or tell the user the source is stale). Report claims as
"verified against `<repo> @ <sha>`" — the **commit SHA**, not just the branch name.

List each concrete, checkable claim the doc would make, then confirm each against that ref. Read
it **without disturbing the working tree** using `git -C`:

```bash
# search the ref for a symbol (system variable, option, keyword, error code)
git -C <repo.path> grep -n "innodb_log_file_buffering" "$sha" -- 'sql/*' 'storage/*'
# read an exact file at the ref
git -C <repo.path> show "$sha":storage/innobase/handler/ha_innodb.cc | sed -n '...'
```

Verify the claim types that matter for docs:

| Claim | Where to confirm |
|-------|------------------|
| System/status variable name, **default**, scope, read-only/dynamic | `sql/sys_vars.cc`, `sql/mysqld.cc`, the engine's var table |
| SQL syntax / grammar | `sql/sql_yacc.yy`, `sql/lex.h` |
| Option / startup flag | `sql/sys_vars.cc`, `*/handler.cc` option structs |
| Error code / message | `sql/share/errmsg-utf8.txt`, `include/my*.h` |
| Behavior / condition | the function named in the MDEV/PR |

For each claim, record: **verified** (with `file:line` at the ref) / **contradicts the ticket**
(document what the source actually says) / **unverifiable** (say so; do not assert it).

**Hard rule:** if you cannot confirm a claim against source, either omit it or mark it clearly
for human confirmation (`<!-- TODO: confirm against source -->`). Do not let ticket prose become
an authoritative doc statement unchecked — feature *requests* describe desired behavior that may
not match what shipped.

## 4. Locate the target page

Use the verified symbol names to find where the docs already cover it:

```bash
docs_root="$(git rev-parse --show-toplevel)"
grep -rn "<variable-or-keyword>" "$docs_root/server/" --include=*.md
```

Pick the page readers would actually land on (the existing topic), not a stray grep hit. SQL /
variable reference lives under `server/reference/`. See `dev-docs/space-map.md`. If a new page is
warranted, **stop and confirm with the user** (a new page needs a `SUMMARY.md` entry — that's the
`new-page` skill's job).

## 5. Draft the edit

- Match the voice and structure of the surrounding page (American English; see
  `dev-docs/style-guide.md`).
- Use correct GitBook syntax — delegate blocks/links to the **`gitbook-format`** skill
  (`{% hint %}` for caveats, version notes, etc.). Cross-space links use `{alias}`.
- Tie each sentence to a **verified** fact; cite the source `file:line` (at the ref) in your
  presentation to the user, not in the page text.
- Offer **one** alternative phrasing if there's a real trade-off; skip otherwise.
- For version-specific behavior, add a note stating the version (from Release Series / the PR),
  and flag that it was verified against `<ref>`.

## 6. Present — do not apply by default

Show the proposed edit (target `file:line`, the snippet, the source citations, the
verification table). **Wait for the user's go-ahead before writing.** If they said "apply" /
"just do it", apply with `Edit`, then validate with `.claude/hooks/doc-lint.sh <file>` (or the
`docs-check` skill).

**Never `git add`, `git commit`, `git push`, or open a PR.** Editing the file on the current
branch is the limit — staging/committing and the Jira transition (`/jira-resolve`) are separate,
user-driven steps.

## 7. Write the fact-check report (paper trail)

The verification table you built in §3 **is** the paper trail — persist it. Format, location, and
naming are defined once in `dev-docs/cookbook-fact-trail.md`; follow it.

- Write/update `<reports_dir>/<space>/DOCS-XXXX/report.md` (space = the edited page's space). If a
  skeleton from `/impact` exists under the **MDEV** key (e.g. `_unfiled/MDEV-XXXXX/`), **move that
  directory** to `<space>/DOCS-XXXX/` (record the MDEV in the header) so there's one canonical
  directory per ticket. Regenerate `INDEX.md` after writing (cookbook).
- Header: DOCS/MDEV/Release Series, the page(s) edited, `Source: <product> @ <sha>` (the **pinned
  commit** from §3, not the branch name), `Status: drafted`.
- One claim row per checkable fact in your edit: the claim **as it reads in the doc**, its **doc
  `file:line`**, the **source evidence** (`<product> <file>:<line> @ <sha>`), and the **verdict**
  (`VERIFIED` / `CORRECTED` / `UNVERIFIED`). Every `VERIFIED`/`CORRECTED` row must carry the SHA;
  anything you marked `<!-- TODO: confirm -->` in the doc is an `UNVERIFIED` row.
- Write the report whether or not the user applied the edit (it records what you verified). If the
  edit isn't applied yet, use the proposed `file:line`; correct them if/when you apply.

This is the **only** file written outside the repo, and it is **never committed** — `/jira-resolve`
posts its contents to the ticket as a comment.

## Output summary

After drafting, report:
- The DOCS ticket → MDEV/PR → the source repo **@ commit SHA** you verified against (not just
  the branch name).
- A **verification table**: each claim → verified (`file:line` @ SHA) / corrected / unverifiable.
- The target page + line, and whether a counterpart edit (another version/page) is advisable.
- The **fact-check report path** (`<reports_dir>/<space>/DOCS-XXXX/report.md`) and that
  `/jira-resolve` will post it to the ticket. Suggest `/verify-claims DOCS-XXXX` to re-audit it in
  a later session.

## Guardrails

- **Verification is mandatory.** Unverifiable claims are flagged, never asserted.
- **The fact-check report is mandatory** (§7) — every source-verified edit leaves one in
  `reports_dir`. It is written outside the repo and **never committed**.
- Source is read **read-only** via `git -C <path> grep/show <ref>` — never modify or check out
  branches in the source repo.
- One ticket at a time; if the ticket implies several distinct pages, draft one at a time and
  confirm between them.
- Don't fabricate examples the source/ticket doesn't support.
