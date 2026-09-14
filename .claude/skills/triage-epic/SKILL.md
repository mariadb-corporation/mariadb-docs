---
name: triage-epic
description: Sweep a MariaDB DOCS release Epic for On Hold child tickets whose upstream MDEV development work has finished, and release them for writing. For each On Hold child it resolves the primary MDEV, checks the public jira.mariadb.org status/resolution and the local MariaDB source for merged commits, posts a short evidence-backed triage brief, and moves the ticket On Hold → TODO. Use when asked to "triage DOCS-XXXX", "triage the epic", "what's unblocked in the 13.1 epic", "which doc tickets are ready to write", or "sweep the On Hold tickets". Dry-run by default — never transitions anything without approval.
allowed-tools: Bash, Read, Grep, Glob, mcp__atlassian-mariadb__getJiraIssue, mcp__claude_ai_Atlassian_Rovo__getJiraIssue, mcp__atlassian-mariadb__searchJiraIssuesUsingJql, mcp__claude_ai_Atlassian_Rovo__searchJiraIssuesUsingJql, mcp__atlassian-mariadb__getJiraIssueRemoteIssueLinks, mcp__claude_ai_Atlassian_Rovo__getJiraIssueRemoteIssueLinks, mcp__atlassian-mariadb__addCommentToJiraIssue, mcp__claude_ai_Atlassian_Rovo__addCommentToJiraIssue, mcp__atlassian-mariadb__getTransitionsForJiraIssue, mcp__claude_ai_Atlassian_Rovo__getTransitionsForJiraIssue, mcp__atlassian-mariadb__transitionJiraIssue, mcp__claude_ai_Atlassian_Rovo__transitionJiraIssue, mcp__atlassian-mariadb__getAccessibleAtlassianResources, mcp__claude_ai_Atlassian_Rovo__getAccessibleAtlassianResources
owners: [igusev]
last_verified: 2026-09-08
status: active
---

# triage-epic

Release Epics in DOCS (e.g. **DOCS-6084**, "Documentation for MariaDB Server 13.1") are created by
the Documentation Automation System, and so are their children — one `[Auto] Documentation needed:`
Task per upstream **MDEV**. Children are parked in **On Hold** until the development work actually
lands. Nothing moves them back out automatically, so the epic silently accumulates tickets that are
ready to write.

This skill sweeps the On Hold children, decides per ticket whether the upstream work is **done**,
and — with your approval — posts a short evidence-backed brief and moves the ticket to **TODO**.

It is **triage, not drafting.** The brief it posts is explicitly *not* source-verified prose; the
rigorous pass is `/impact` then `/doc-ticket`. Jira conventions: `dev-docs/cookbook-jira-workflow.md`.

## When to use

"Triage DOCS-XXXX", "triage the 13.1 epic", "which doc tickets are ready to write?", "sweep the On
Hold tickets", "has the dev work for this epic landed yet?". Typically run periodically against the
current release epic, before planning a sprint of doc work.

Do **not** use it to close tickets, to write docs, or to touch the upstream MDEV.

## 0. Preflight and configuration

### Required tools

Check before the sweep and stop with a plain message naming what is missing:

```bash
for c in curl jq git; do command -v "$c" >/dev/null || echo "MISSING: $c"; done
```

`curl` and `jq` are **hard requirements** — the readiness decision is read from
`jira.mariadb.org` and parsed as JSON. `git` is needed only with a local clone (below); `gh` only
in degraded mode. Confirm the public Jira actually answers before sweeping a whole epic, so a
blocked network fails once and clearly instead of turning every ticket AMBIGUOUS:

```bash
curl -s -o /dev/null -w '%{http_code}\n' -m 20 \
  "https://jira.mariadb.org/rest/api/2/issue/MDEV-1?fields=status"     # expect 200
```

That endpoint is **anonymous** — no credentials, and unrelated to the Atlassian MCP connection,
which reaches `mariadbcorp` only and cannot see MDEV tickets at all.

### A local MariaDB source clone is optional

The promotion decision comes entirely from Jira fields (§5). A clone adds **revert detection** and
the **SHAs quoted in the brief** — valuable, not required. Three usable setups:

| Setup | What you get | Cost |
|-------|--------------|------|
| **No clone** (degraded) | Full READY/CANDIDATE/NOT READY tiering; no revert check; no SHAs | nothing |
| **`git clone --filter=blob:none`** *(recommended)* | Everything this skill needs — `git log --grep` and `branch --contains` never touch blobs | a fraction of a full clone |
| **Full clone** | Same as above; also serves `/doc-ticket` source verification | ~5 GB |

Do **not** use `--single-branch`: it drops the `bb-*` and `preview-*` branches this skill reads.

### Config files

Both **gitignored** (paths and preferences differ per machine):

- **`.claude/doc-sources.local.json`** — **read-only here.** This skill consumes the entry whose
  `product` is `server` (its `path` and authoritative `ref`) but never creates or edits the file:
  `doc-from-ticket` and `/impact` own it, and their first run prompts for it. If it is absent,
  either point the user at `/impact` to set it up, or simply continue in **degraded mode** (§4b) —
  a supported way to run, not a failure. Before using a configured path, validate it
  (`git -C <path> rev-parse --git-dir`, `git -C <path> rev-parse --verify <ref>^{commit}`) and drop
  to degraded mode with a clear message if either fails.
- **`.claude/triage-epic.local.json`** — the tiering knobs. Optional; these are the built-in
  defaults, used as-is when the file is absent:

  ```json
  {
    "require_resolution":        true,
    "ready_resolutions":         ["Fixed", "Done"],
    "require_numbered_fixversion": true,
    "numbered_fixversion_regex": "^[0-9]+\\.[0-9]+\\.[0-9]+$",
    "candidate_mdev_statuses":   ["In Testing", "In Review"],
    "never_ready_statuses":      ["Stalled", "Open", "Confirmed"],
    "release_branch_globs":      ["main", "1*.*", "preview-*"],
    "build_branch_globs":        ["bb-*"],
    "hold_status":               "On Hold",
    "target_status":             "TODO"
  }
  ```

  **The readiness bar is the MDEV's resolution plus a numbered fix version — not its status, and
  not commit evidence.** This is the DOCS team's demonstrated bar, not a guess. Of DOCS-6084's 28
  children, all 16 that ever left On Hold have an MDEV that is `Closed` / `Fixed` with a fix version
  of `13.1.1` or `13.1.2`; all 11 still parked have an unresolved MDEV whose fix version is the bare
  `13.1`. Sixteen for sixteen, and the MDEV always closes weeks *before* the doc work (MDEV-14443
  closed 2026-07-20, DOCS-6218 finished 2026-09-03).

  `13.1` is the **rolling placeholder** on an unreleased series; `13.1.1` is the point release the
  fix actually shipped in. That digit is the whole signal — it separates "the code exists somewhere"
  from "this shipped, go document it" — which is why `numbered_fixversion_regex` demands three
  components.

  `release_branch_globs` are the refs that count as **merged**; `build_branch_globs` are
  work-in-progress refs. Never treat a `bb-*` push as merged — MariaDB developers push there long
  before the change reaches `main`. Neither kind of ref can reach READY on its own (§5).

## 1. Setup and input

1. Run the `jira` skill's **Setup** check (`getAccessibleAtlassianResources()` must return
   `mariadbcorp.atlassian.net`, cloudId `164b0d33-ee39-4b4d-b1d5-e71a97376560`, with
   `write:jira-work`). Never pick a connection by name. All calls below take that `cloudId`; prefix
   tool names per the `jira` skill's table.
2. Resolve the input key from `DOCS-XXXX` or a `browse/DOCS-XXXX` URL. `getJiraIssue` it.
   - `issuetype == Epic` → that is the epic.
   - Anything else → use its `parent` as the epic and say so ("DOCS-6085 is a child of DOCS-6084;
     triaging the epic"). No parent → stop and ask.
3. Record the epic's **target series** from its summary (`Documentation for MariaDB Server 13.1`
   → `13.1`). It is used in §6 to flag children aimed at a different series.

## 2. Enumerate the On Hold children

Children attach through the team-managed **`parent`** field. `issuelinks` on these epics is
**empty** — do not look for children there.

```
searchJiraIssuesUsingJql(
  cloudId="164b0d33-…",
  jql='parent = DOCS-XXXX AND status = "<hold_status>" ORDER BY key',   # default: "On Hold"
  fields=["summary","description","status","assignee","updated"],
  maxResults=100)
```

Ask for **only those fields**. A full-field search over a 28-child epic exceeds the tool's token
budget; the result is then spilled to a file and you must parse it with `jq` instead of reading it:

```bash
jq -r '.issues.nodes[] | [.key, .fields.status.name, .fields.summary] | @tsv' "<spilled-file>"
```

Report the totals before doing any work ("28 children: 14 Closed, 11 On Hold, 1 Review, 1 TODO,
1 DUPLICATED — triaging the 11 On Hold"). If there are none, say so and stop.

**Say how long it will take.** Cost scales with the On Hold count: one public-Jira request per
ticket, plus — with a clone — a `git log --grep` per release ref per ticket. Eleven tickets took
**over two minutes** on a WSL checkout of `MariaDB/server` on a `/mnt` drive, and a single
`git for-each-ref --contains` on that repo's ~3,900 branches takes about **9 seconds**. Tell the
user the expected order of magnitude up front, and run the evidence pass in the background rather
than letting a long sweep look hung. Keep the release-ref list short (the epic's own series, its
`preview-*`, and `main`) instead of walking all 33.

## 3. Resolve the primary MDEV (precedence — do not guess)

`[Auto]` descriptions have a fixed header:

```
**Assignee:** Elena Stepanova              ← the MDEV's dev assignee, NOT the doc writer
Documentation needed for ticket: MDEV-38983
**Summary:** …
**Release Series:** 13.1
**Link to ticket:** [https://jira.mariadb.org/browse/MDEV-38983](…)
—
**Original Description:** …
```

Take the primary MDEV in this order:

1. the `Documentation needed for ticket: MDEV-NNNNN` line;
2. the remote issue link whose `relationship` is `action item from` and whose `object.url` is on
   `jira.mariadb.org` — `getJiraIssueRemoteIssueLinks(cloudId, issueIdOrKey)`;
3. the `**Link to ticket:**` URL.

> **Never bare-grep `MDEV-[0-9]+` over the description.** The *Original Description* routinely
> cites related tickets: DOCS-5943 mentions MDEV-23844 alongside its real MDEV-25292, DOCS-6177
> mentions MDEV-16699, DOCS-6219 mentions two extras. A grep picks whichever comes first.

If (1) and (2) disagree, or neither resolves: mark the ticket **AMBIGUOUS**, leave it On Hold, and
report it. Do not guess a key you are about to comment on.

Also extract the ticket's own `**Release Series:**` for §6.

## 4. Gather evidence per MDEV

Two independent sources. Both are read-only.

### 4a. Public MariaDB Jira (anonymous, no MCP connection needed)

`jira.mariadb.org` serves its REST API without authentication — the MariaDB MCP connection reaches
`mariadbcorp` only and cannot see MDEV tickets at all.

```bash
curl -s -m 20 "https://jira.mariadb.org/rest/api/2/issue/MDEV-40030?fields=summary,status,resolution,resolutiondate,fixVersions,comment" \
  | jq -r '[.key, .fields.status.name, (.fields.resolution.name // "-"),
            ([.fields.fixVersions[].name] | join("|")), (.fields.resolutiondate // "-")[0:10]] | @tsv'
```

Fetch **sequentially** with a timeout, one ticket at a time; this is a public community server, not
an internal API. A non-200 or an empty body is evidence of nothing — mark the ticket AMBIGUOUS.

Read the comments too: developers announce landings there in prose (`"Pushed to bb-blob-main-monty"`,
`"The PR is here: https://github.com/MariaDB/server/pull/4732"`). Useful as a lead and for the
brief's "notable decisions" line — **never** as proof on its own.

### 4b. Merged commits in local MariaDB source

Read `.claude/doc-sources.local.json` and take the entry **whose `product` is `server`** — `sources`
is an *array* of `{product, path, ref}` objects, not a map, so select it rather than indexing:

```bash
cfg=.claude/doc-sources.local.json
p="$(jq -r '.sources[] | select(.product=="server") | .path' "$cfg")"
ref="$(jq -r '.sources[] | select(.product=="server") | .ref'  "$cfg")"
git -C "$p" fetch --quiet
```

> **Never write `\b` in a `git log --grep` pattern.** `\b` is a GNU-regex extension: under `-E`
> (POSIX ERE) on macOS/BSD it matches **nothing at all** — no error, no warning, just zero commits.
> A revert query written that way silently never fires, so the "any revert disqualifies" guardrail
> quietly stops working and every CANDIDATE collapses to NOT READY, **on Mac machines only**.
>
> Use a **plain substring `--grep`** (portable BRE, no `-E`, no `-P`) and enforce the word boundary
> in `awk`, which this section already does for subjects. That needs neither GNU regex nor a
> PCRE-enabled git.

```bash
# every commit anywhere in the repo that names the key
git -C "$p" log --all --oneline --grep="MDEV-40030"

# the subset reachable from the authoritative ref — this is what "merged" means
git -C "$p" log "$ref" --oneline --grep="MDEV-40030"

# for a specific commit, which branches carry it
git -C "$p" branch -a --contains <sha>
```

Rules:

- **Subject, not body.** `--grep` matches the whole commit message, so a commit fixing something
  else that merely *cites* the key will match. A commit counts as **implementing** the change only
  when its **subject** starts with the key; anything else is a reference. Filter explicitly, and
  anchor the tail so `MDEV-3064` cannot match `MDEV-30645`:

  ```bash
  git -C "$p" log "$ref" --date=short --format='%h|%ad|%s' --grep="MDEV-38975" \
    | awk -F'|' '$3 ~ /^(Revert )?MDEV-38975([^0-9]|$)/'
  ```

  On `preview-13.1-preview` that turns **2** message matches into **1** real implementation commit:
  it drops `99de1d0a1b0 Fix CI regressions from MDEV-38975 forward-port to main`, which names the
  key but implements nothing, and keeps `4216091efc1 MDEV-38975: HEAP engine BLOB/TEXT/JSON/GEOMETRY
  support…`. Tiering on the unfiltered list reads a CI cleanup as the feature landing.

  On `preview-13.1-preview`, MDEV-30645 matches 4 commits by message but 3 by subject, and
  MDEV-38975's newest *matching* commit is titled `MDEV-40591 …`. Tiering on the unfiltered list
  reads another ticket's work as this one's.
- **Merged** = at least one commit naming the key is reachable from `ref` (or from a ref matching
  `release_branch_globs`). Always report **which** ref carried it — `main` and
  `preview-13.1-preview` mean different things to a writer.
- Commits only on `bb-*` branches are weaker still: work in progress, nothing more.
- **Merged is never sufficient for READY** (§5). Commit evidence answers *"what changed, and is it
  still there?"* — it is what catches reverts and never-landed work, and what gives the brief its
  SHAs. It does not answer *"has this shipped?"*; only the MDEV's resolution and numbered fix
  version do. MDEV-38975 is the case that settles it: merged to `preview-13.1-preview` on
  2026-06-13, and on 2026-09-04 the QA lead wrote *"I'm afraid this feature won't make it to 13.1
  release."* Promoting on the merge would have told a writer to document a feature being pulled.
- **Any revert disqualifies — do not reason from commit order.** If *any* commit reachable from
  `ref` has a `Revert` subject naming the key, the ticket drops to **NOT READY** and is flagged for
  a human, however many non-revert commits sit beside it.

  Ask for reverts in their **own query** over the full history — never by scanning a capped or
  paged commit list for `Revert` subjects. MDEV-25292's revert sits 40+ commits deep; a `head -40`
  scan misses it and the ticket comes back clean:

  Then **confirm each hit actually reverts your key**: take the *first* `MDEV-<digits>` token after
  `Revert` and require it to equal the target. A revert of some other ticket often names yours in
  passing — MDEV-35915 matches two commits titled
  `Revert "MDEV-37686 rpl.create_or_replace_mix2 fails in MDEV-35915 branch"`, which revert
  MDEV-37686 on a branch named after MDEV-35915. Counting those as reverts of MDEV-35915 buries a
  live feature under someone else's rollback.

  Both steps in one portable pass — two plain `--grep`s with `--all-match`, then `awk` for the
  boundary and the first-key test:

  ```bash
  git -C "$p" log --all --format='%h|%s' --grep="Revert" --grep="MDEV-25292" --all-match \
    | awk -F'|' -v k=MDEV-25292 '$2 ~ /^Revert/ {
        s=$2; sub(/^Revert[^M]*/,"",s)
        if (match(s,/MDEV-[0-9]+/) && substr(s,RSTART,RLENGTH)==k) print $1"  "$2 }'
  ```

  Verified against both cases: it returns `2bd41fc5bf7 Revert MDEV-25292 Atomic CREATE OR REPLACE
  TABLE` for MDEV-25292, and nothing for MDEV-35915.

  Ordering cannot decide this. On MDEV-25292, `git log main --grep` lists
  `1f85eeeb53a` (author date 2022-08-31) *above* `2bd41fc5bf7 Revert MDEV-25292 Atomic CREATE OR
  REPLACE TABLE` (2022-10-27), because the log walks commit date while `%ad` shows author date, and
  these were rebased. "Is the newest commit a revert?" answers **no** here and would promote a
  feature that was backed out. Presence of the revert is the signal; sequence is not.
- Record the **SHAs and dates** you relied on; they go in the brief.

### 4b-i. Degraded mode (no clone configured) — still promotes

**READY is decided by Jira alone (§5), so degraded mode reaches READY like any other run.** The
clone only supplies revert detection and the SHAs quoted in the brief. Losing it costs evidence
detail, not the verdict — never report "0 promoted" merely because no clone is configured.

What changes without a clone:

- **Say so in the brief**, on every ticket: *"Revert check skipped — no local source configured."*
  A resolved MDEV with a numbered fix version and a live revert is unlikely (a revert normally
  reopens the ticket), but it is the one case this mode cannot see.
- The brief carries no SHAs; cite the MDEV's fix version and status instead.
- `gh` becomes a requirement in this mode only. If it is missing or unauthenticated, skip the
  GitHub lookups and say so — they are supplementary, and their absence must not change a tier.

Optional GitHub colour, labelled *weak evidence* wherever it appears:

```bash
gh api -X GET search/commits -f q="repo:MariaDB/server MDEV-40030" --jq '.total_count'
gh pr list -R MariaDB/server --search "MDEV-40030" --state all --json number,state,mergedAt
```

`search/commits` indexes the **default branch only** — it returned `0` for MDEV-40030, MDEV-40033
and MDEV-38983 even though all three had code on build branches. A zero here is **not** evidence of
absence, and must never downgrade a ticket on its own.

## 5. Tier each ticket

| Tier | Condition | Action |
|------|-----------|--------|
| **READY** | MDEV `resolution` ∈ `ready_resolutions` **and** a fix version matching `numbered_fixversion_regex` (`13.1.1`, not `13.1`) — **and** no revert found (or, in degraded mode, none checkable — flag it) | propose comment + On Hold → TODO |
| **CANDIDATE** | MDEV unresolved, **and** real code evidence exists: a non-reverted subject commit on a release or `preview-*` ref; **or** commits only on `bb-*`; **or** a merged `MariaDB/server` PR | report with its evidence; ask per ticket |
| **NOT READY** | **no code evidence anywhere** (whatever the MDEV status); **or** the work was reverted | leave On Hold, list with the reason |
| **AMBIGUOUS** | MDEV unresolvable, conflicting keys, MDEV fetch failed | leave On Hold, list for a human |

**Only the MDEV's resolution and numbered fix version promote a ticket.** Merged code, a green PR,
`In Testing`, and a developer saying "pushed" are all CANDIDATE at best — every one of them is a
statement about *code*, and the question a doc writer needs answered is whether it **shipped**.
A feature can sit merged on a preview branch for months and still be pulled from the release.

**A status alone is never evidence.** `candidate_mdev_statuses` describes *which unresolved states
are worth surfacing* — it does not by itself make a ticket a CANDIDATE. With no code anywhere, an
`In Review` ticket is NOT READY: MDEV-38983 sits in review with an open PR and not one commit in
any branch, so there is nothing for a writer to look at yet.

**How each config knob is applied** — every one is honored, none is decorative:

| Knob | Where it acts |
|------|---------------|
| `require_resolution`, `ready_resolutions` | READY row: the MDEV's `resolution` must be present and in the list. Set `require_resolution: false` to promote on the fix version alone. |
| `require_numbered_fixversion`, `numbered_fixversion_regex` | READY row: at least one `fixVersions[].name` must match. Set to `false` for a project that never uses point versions. |
| `candidate_mdev_statuses` | Which unresolved statuses are worth reporting, alongside code evidence. |
| `never_ready_statuses` | Caps the tier at CANDIDATE with a conflict flag (below). |
| `release_branch_globs`, `build_branch_globs` | §4b: which refs count as merged, and which are work in progress. |
| `hold_status` | §2's JQL — `status = "<hold_status>"`, not a hardcoded `On Hold`. |
| `target_status` | §7's transition target, matched by name against the live transition list. |

**When rules collide, the cautious one wins:**

1. **A revert on a release ref beats everything** — NOT READY, flagged, even if the MDEV is
   resolved. Resolution plus a live revert is a contradiction a human must look at.
2. **`never_ready_statuses` caps the tier at CANDIDATE**, with a conflict flag reading *"merged to
   `<ref>` but MDEV is `<status>`"*. Merged-then-contested is real: MDEV-39176 landed on
   `preview-13.1-preview` in April and was called "conceptually wrong" in an August review;
   MDEV-30645 is on the same ref but Stalled and retargeted to 13.2.
3. A bare fix version (`13.1`) never satisfies the numbered-version test, however many commits back
   it up.

**Negative human signals demote, they never promote.** Before proposing a READY ticket, read the
MDEV's last few comments for someone saying the work will *not* ship in this series — MDEV-38975
has merged code on `preview-13.1-preview` and a 2026-09-04 comment from the QA lead saying
"I'm afraid this feature won't make it to 13.1 release". Keep the tier, attach the flag and quote
the comment in the dry-run table; the asymmetry is deliberate — prose is not proof that something
landed, but it is a fair warning that it may be pulled.

**A run that promotes nothing is a good run.** On a live release epic the normal result is zero
READY and a handful of CANDIDATEs — the upstream work simply has not closed yet. Report that
plainly. Never widen the bar to produce a promotion.

## 6. Dry run (default — write nothing)

Print one table, then the proposed brief for each promotable ticket:

```
Epic DOCS-6084 — Documentation for MariaDB Server 13.1  (target series 13.1)
  children: 28   On Hold: 11   source: MariaDB/server @ main (a1b2c3d)

  TICKET     MDEV         STATUS/RESOLUTION   FIXVER   EVIDENCE                       TIER        SERIES
  DOCS-6275  MDEV-39518   Closed / Fixed      13.1.1   shipped                        READY       13.1
  DOCS-6237  MDEV-40030   In Testing / —      13.1     d68872cca73 → preview-13.1     CANDIDATE   13.1
  DOCS-6085  MDEV-38983   In Review / —       13.1     none in any branch (PR open)   NOT READY   13.1
  DOCS-6220  MDEV-30645   Stalled / —         13.2     ea8801efa80 → preview-13.1     CANDIDATE   13.1  ⚠ conflict
  DOCS-5943  MDEV-25292   In Testing / —      13.1     2bd41fc5bf7 Revert on main     NOT READY   ⚠ 13.0
```

The FIXVER column is the deciding one: `13.1.1` promotes, bare `13.1` does not.

Flag in the table, never silently:

- **series mismatch** — the child's `Release Series` differs from the epic's target (DOCS-5943 is
  13.0 and DOCS-6246 is 13.2, both under the 13.1 epic), or the MDEV's `fixVersions` disagrees with
  the child's series;
- reverted work, missing fixVersion, MDEV fetch failures, and anything AMBIGUOUS.

Then **stop and ask for approval**: the whole READY set at once, CANDIDATEs individually. Accept
"all", "all ready", a list of keys, or an exclusion list. Write nothing until you have it.

## 7. Apply (only what was approved)

Per approved ticket, in order:

1. `addCommentToJiraIssue(cloudId, issueIdOrKey, contentFormat="markdown", …)` with the brief:

   ```markdown
   **Triage: upstream development looks complete.**

   **MDEV-40030** — Add support for CHECK TABLE to memory tables
   Status: Closed · Resolution: Fixed · Fix version: 13.1.1 · https://jira.mariadb.org/browse/MDEV-40030

   **What shipped:** `ha_heap::check()` implemented, so `CHECK TABLE` now works on MEMORY tables
   instead of silently returning OK.

   **Evidence:** `a1b2c3d` (2026-06-13) on `main` — MariaDB/server.
   **Notable from the MDEV discussion:** coverage gap on two error paths raised in review; no
   behavior change agreed.

   *Not source-verified — this is automated triage from ticket, Jira and commit metadata.
   Run `/impact DOCS-6237`, then `/doc-ticket DOCS-6237`, before writing.*

   Moved On Hold → TODO by `triage-epic`.
   ```

   Keep it to roughly ten lines. The closing disclaimer is **mandatory** — a later reader must not
   mistake a triage brief for verified fact.
2. `getTransitionsForJiraIssue(cloudId, issueIdOrKey)`, match the transition by **name**
   (`TODO`, id 11 — trust the live list), then `transitionJiraIssue`.
3. If the comment succeeds and the transition fails, say so per ticket; do not retry blindly and do
   not leave the run reporting success.

Comment first, transition second — a ticket that moves with no explanation on it is worse than one
that has the explanation and did not move.

## 8. Report

```
Epic DOCS-6084 — triage complete
  On Hold examined: 11
  promoted → TODO:  3   (DOCS-6237, DOCS-6387, DOCS-6229)
  left On Hold:     7   (5 no evidence, 1 reverted, 1 stalled)
  ambiguous:        1   (DOCS-6177 — description and remote link name different MDEVs)
  flags:            2 series mismatches (DOCS-5943 → 13.0, DOCS-6246 → 13.2)
  next:             /impact DOCS-6237
```

State any bound you applied (a `maxResults` page you did not follow, tickets you skipped) — **no
silent caps**.

## Guardrails

- **Dry run by default.** No comment and no transition without explicit approval in this session.
- **Read-only upstream.** Never comment on, transition, or otherwise write to `jira.mariadb.org`,
  and never modify the MariaDB source clone (`git -C … log/show/branch` only, plus `fetch`).
- **Only a resolved MDEV with a numbered fix version promotes.** A comment saying "pushed", a
  merged commit, a green PR and `In Testing` are all CANDIDATE evidence. Zero promotions is a
  normal, correct outcome — never relax the bar to manufacture one.
- **Never bare-grep for the MDEV key** (§3). An ambiguous ticket stays On Hold.
- **Only `hold_status` → `target_status`.** This skill does not close, cancel, reassign, or edit
  descriptions, and does not touch children in any other status.
- **Degraded mode is labeled, not crippled** — with no clone, tiering still runs and still
  promotes; every brief states that the revert check was skipped.
- **No docs are written here.** Hand off to `/impact` and `/doc-ticket`; this skill writes no `.md`
  file, no fact-check report, no branch, no commit.
