---
name: propose-improvement
description: File an agent-tooling proposal for mariadb-docs. Use when the user says "propose an improvement", "propose a new skill", "draft a skill proposal", or "file a proposal". Asks whether it's a new Claude Code skill or a broader change, files a DOCS Jira Task (labeled claude-skill), and interviews the proposer to write the proposal MD (dev-docs/skill-proposals/ for skills, dev-docs/agent-improvements/ for everything else). The skill is the scribe; the proposer is the source. Does not open the PR.
allowed-tools: Bash, Read, Write, Glob, mcp__atlassian-mariadb__createJiraIssue, mcp__atlassian-mariadb__atlassianUserInfo, mcp__atlassian-mariadb__getAccessibleAtlassianResources
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# propose-improvement

Gathers a proposal's content, files the DOCS Jira ticket, and writes the proposal MD. **The
skill is the scribe; the proposer is the source** — every body word in the MD comes from a
proposer answer (or `_TBD — fill before opening PR_` when skipped). Pairs with
`report-skill-bug`. **Does not open the PR.**

Jira plumbing uses the `jira` skill's config (server `atlassian-mariadb`, cloudId `164b0d33-…`,
project `DOCS`). Run that skill's **Setup** connection check before any Jira write.

## When to use

Trigger phrases: "propose an improvement", "propose a new skill", "propose a skill called
`<name>`", "draft a proposal for `<topic>`", "file a proposal". If the user is still *discussing*
whether to propose, don't trigger — wait until they want it filed.

## Workflow

### 0. Classify (one question, its own turn)

> Which kind of proposal is this?
> 1. **New Claude Code skill** — adds a new `.claude/skills/<name>/`.
> 2. **General agent-tooling improvement** — a cookbook/hook/command/workflow change, anything
>    that isn't a new skill.

- **Skill branch** → §1a–§4a. Output `dev-docs/skill-proposals/NNNN-<name>.md`, Jira title
  `[skill proposal] <name>`.
- **Improvement branch** → §1b–§4b. Output `dev-docs/agent-improvements/NNNN-<slug>.md`, Jira
  title `[agent-improvement] <slug>`.

If `$ARGUMENTS` clearly names a skill (kebab-case noun, no verbs), default to (1) and confirm in
one sentence; if it reads as a sentence/topic, default to (2) and confirm.

---

### Skill branch

**1a. Resolve the name.** From `$ARGUMENTS`, else ask once, open-ended (no suggestions):
> Short name for the proposed skill (kebab-case, no `skill-` prefix)?

Validate `^(?!skill-)[a-z][a-z0-9-]+$`; refuse if `.claude/skills/<name>/` exists or
`dev-docs/skill-proposals/[0-9]{4}-<name>.md` exists (tell the user which; don't auto-rename).

**2a. One-line problem statement** (≤120 chars; goes in the Jira description only).

**3a. Next NNNN:**
```bash
ls dev-docs/skill-proposals/ 2>/dev/null | grep -E '^[0-9]{4}-' | sort | tail -1
```
Increment the leading 4-digit number (zero-padded; start `0001`; don't fill gaps). Create
`dev-docs/skill-proposals/` if it doesn't exist yet.

**4a. File Jira + scaffold + interview** — see §Jira and §Scaffold below (skill variant).

---

### Improvement branch

**1b. Gather the description (one turn, open-ended).** If `$ARGUMENTS` reads as a description,
treat it as the problem statement and ask only for the proposed direction; else ask both:
> 1. One-line problem statement (≤120 chars; goes in the Jira description).
> 2. One-paragraph proposed direction (≤4 sentences; also goes in Jira).

Both pre-fill the MD's **Problem** and **Proposed change** (no re-asking later).

**2b. Derive the slug silently** from the problem statement: lowercase, drop stopwords
(`a/an/the/and/or/with/for/to/in/on/of/by/from/that/this/it/its/as`), non-alphanumeric → `-`,
truncate ≤60 chars at a word boundary, strip edge `-`. Must match `^[a-z][a-z0-9-]+$`. On
collision with an existing `dev-docs/agent-improvements/NNNN-<slug>.md`, append `-2`, `-3`, …

**3b. Next NNNN:**
```bash
ls dev-docs/agent-improvements/ 2>/dev/null | grep -E '^[0-9]{4}-' | sort | tail -1
```
Same rule as §3a. Create the directory if absent.

**4b. File Jira + scaffold + interview** — see §Jira and §Scaffold below (improvement variant).

---

## §Jira — file the DOCS ticket

Run the `jira` skill **Setup** check. Then create a **Task** (DOCS has no Improvement type),
labeled **`claude-skill`**:

```
mcp__atlassian-mariadb__createJiraIssue(
  cloudId="164b0d33-ee39-4b4d-b1d5-e71a97376560",
  projectKey="DOCS",
  issueTypeName="Task",
  summary="[skill proposal] <name>"   |   "[agent-improvement] <slug>",
  description="<short markdown — see below>",
  contentFormat="markdown",
  assignee_account_id="<the proposer — current user from atlassianUserInfo()>",
  additional_fields={"labels": ["claude-skill"]}
)
```

> **Visibility — assign it.** Like `claude-skill-bug`, the `claude-skill` label has no watcher or
> board filter yet, so an unassigned ticket may reach no one. Assign the proposer (current user)
> and tell them the ticket is discoverable via the label; recommend a one-time saved filter on
> `claude-skill` for the team.

Description (short — the MD is the proposal; the ticket is the discussion thread):

```markdown
## Problem
<one-line problem statement>

## Proposed direction        (improvement branch only)
<one-paragraph direction>

## Proposal MD
`dev-docs/<skill-proposals|agent-improvements>/NNNN-<name|slug>.md` (PR pending; linked here when opened).
```

Capture the new `DOCS-XXXX` key. **If the Setup check fails or create errors → manual-Jira
mode:** don't write a broken link; scaffold the MD with a `DOCS-XXXX (file manually)` placeholder
on the `Related tickets:` line, and tell the user to file it (project DOCS, Task, label
`claude-skill`) and update the line. Don't `@mention` anyone; don't put the long-form proposal in
the ticket.

## §Scaffold — write the proposal MD and interview

Create the output dir if needed. Identify the proposer's GitHub handle: reuse one already in
`.claude/skills/*/SKILL.md` `owners:` or a prior proposal's `**Proposer:**`; if none/ambiguous,
ask once (don't infer from `git config`).

Write the MD with this structure, then **interview the proposer to fill the body** — one section
per turn for the skill branch; for the improvement branch, pre-fill Problem/Proposed change from
§1b and ask the rest in one bundled turn.

**Skill-proposal sections:** Problem · Why a skill (not a script/hook) · Proposed invocation ·
Overlap with existing skills (one row per current `.claude/skills/*`, pre-listed) · Tools it will
call (`allowed-tools`; reads untrusted input?) · Dogfood plan (3 real tasks) · Rollout ·
Alternatives considered.

**Improvement-proposal sections:** Problem (pre-filled) · Proposed change (pre-filled) · Affected
surfaces (files/skills/commands/hooks, tagged edit/new/delete/move) · Rollout · Alternatives
considered · Open questions.

Frontmatter: title, `**Proposer:** @handle`, `**Owner(s):** @handle`, `**Date:** <ISO>`,
`**Related tickets:** [DOCS-XXXX](https://mariadbcorp.atlassian.net/browse/DOCS-XXXX)`.

### Interview guardrails

- **Open-ended only** — ask the section's question and wait; no multiple-choice, no
  pre-proposed answers, no pulling candidates from earlier conversation. The proposer is the
  source.
- **No fabrication** — every body word comes from a proposer answer. If you'd be inferring, ask.
- **Skip cleanly** — "skip"/"TBD"/"I don't know"/a bare ≤3-word fragment → `_TBD — fill before
  opening PR_`. Don't push back; don't fabricate filler.
- **One section per turn** (skill branch). Quote answers verbatim; light formatting only.

## Print the result

```
Filed:  https://mariadbcorp.atlassian.net/browse/<KEY>      (omit in manual-Jira mode)
Wrote:  dev-docs/<dir>/NNNN-<name|slug>.md  (<count> sections marked TBD)

Next:
1. Open the proposal PR; reference the DOCS ticket from the PR description.
2. Discussion-first — no skill/implementation code in this PR.
```

## Don't

- Don't call the GridGain Rovo connection — use `mcp__atlassian-mariadb__*` only.
- Don't open the PR; don't fabricate body content; don't suggest the proposal subject.
- Don't put the long-form proposal in the Jira description — the MD is the proposal.
- Don't conflate the branches — a new skill always uses the skill branch (it has the overlap
  analysis + dogfood expectation); a hook/cookbook/command change never does.

---

Propose the following: $ARGUMENTS
