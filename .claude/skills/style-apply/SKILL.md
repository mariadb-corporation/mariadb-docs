---
name: style-apply
description: Apply the MariaDB documentation house style to a GitBook Markdown page — fix mechanical violations (product naming, American spelling, banned/weasel words, heading case) and surface voice/structure issues that need judgment. Use when asked to "apply the style guide", "style-check this page", "fix the wording/tone", "make this match house style", or as an editorial pass before a PR. Scopes to the page(s) given; never rewrites code samples.
allowed-tools: Bash, Read, Grep, Glob, Edit
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# style-apply

Enforce the MariaDB house style on an existing page: run a **deterministic lint** for the
mechanical violations (safe to auto-fix), and **surface the judgment calls** (voice, structure)
for the user to decide. The canonical rules live in `dev-docs/style-guide.md` (which links the
authoritative MariaDB + Google guides) — that guide wins if anything here disagrees.

This skill changes **prose**, not structure or syntax. Block/link syntax (`{% hint %}`, code
fences, aliases) is the **`gitbook-format`** skill's job; if a fix needs a GitBook block,
delegate there.

## When to use

"Apply the style guide", "style-check this page", "fix the tone/wording", "make this match house
style", or an editorial pass before opening a PR. If the user only wants a report (no edits),
treat it as **lint-only** and skip the apply step.

## 0. Scope

Operate on the **page(s) named** (or the changed pages from `git diff --name-only HEAD`, which
covers staged + unstaged). **Never
sweep a whole space/repo** unprompted — server alone is ~4,500 files. For a multi-page style
campaign, that's the `bulk-campaign` skill (which can call this one per file).

## 1. Read the page and the guide

Read the target file and `dev-docs/style-guide.md`. **Identify the code regions first** —
everything inside a fenced block (```` ``` ```` / `~~~`, any fence length) or a `{% code %}`
block is **opaque**: never apply prose fixes there (SQL/config/output samples legitimately use
lowercase keywords, British-looking identifiers, "simply", etc.).

## 2. Deterministic fixes (high-confidence — apply, then show the diff)

Run these over **prose only** (outside code regions). These are safe, mechanical, and reviewable.

### Product names with NO common-noun reading (safe to auto-fix in prose)

Only these — every occurrence in prose is a mis-cased product/brand, so fixing casing can't
change meaning:

| Wrong (in prose) | Correct |
|------------------|---------|
| `Maxscale` | **MaxScale** |
| `Columnstore` | **ColumnStore** |
| `Mysql` | **MySQL** |
| `Github` | **GitHub** |

**Run the find over prose only**, excluding nav and code: strip code regions first (§1), then

```bash
grep -rnE '\b(Maxscale|Columnstore|Mysql|Github)\b' <file> --exclude=SUMMARY.md
```

Before proposing each hit, **drop it if** the line is inside a fence / `{% code %}` / `mermaid`
block, **or** it's a literal token — a command/binary (`mysql` client, `mariadb-dump`), a path or
config key (`/etc/columnstore/`, `Columnstore.xml`, `ENGINE=ColumnStore`), or **quoted external
text** (an MDEV ticket title or link display text — common in `release-notes/`; don't rewrite a
quote). Never touch the lowercase binary names `mysql`/`maxscale`/`columnstore`.

> **Not auto-fixed:** `MariaDB server` and `Galera cluster` are usually **correct common-noun
> usage** ("restart the MariaDB server", "build a Galera cluster") — only the branded forms
> *MariaDB Server* / *Galera Cluster* are the product names, and the difference needs judgment.
> These go to §3, not here.

### American English

Run `.claude/hooks/doc-lint.sh <file>` (codespell) — it catches American-spelling violations,
including the British variants (the `-our`/`-ise`/`-logue`/`-yse` families and doubled-`l`
forms). Apply what it reports; don't maintain a separate hand-list here (it would only drift from
codespell and trip the spell-check on this very file).

### Word choices

**Auto-fix — filler that never carries meaning** (delete): `simply`, `easily`, `obviously`,
`basically`, `of course`, `please`. **Rewrite:** `in order to`→`to`, `utilize`→`use`,
`leverage`→`use`.

**Auto-fix — documented spellings/agglutinations** (prose only): `commandline`→`command line`,
`resultset`/`result-set`→`result set`, `sub-partition(s)`→`subpartition(s)`,
`non-equal`→`nonequal`.

**Surface, don't auto-change** (meaning-bearing / judgment): `just` ("just one row" is a
quantifier) and `note that`; **neutral action verbs** — flag `kill`/`abort`/`hang` and suggest
`terminate`/`stop`/`cancel`/`unresponsive`; **"one" → "you"** ("one can…" → "you can…").

### Mechanics

- **One `#` H1** per page (the title) — flag a second H1. Body sections start at `##`; headings
  deeper than `####` can't be GitBook link targets (see `gitbook-syntax.md`).
- **Headings are Title Case** — capitalize words **≥4 letters**; keep words **<4 letters**
  lowercase (*to*, *the*, *and*, *of*, *in*…); don't capitalize or format literals in headings.
  **Flag** violations — don't blindly auto-recase, because proper nouns and the short-word /
  literal exceptions need judgment. *(This reverses an earlier draft that said sentence case —
  the canonical guide mandates Title Case.)*
- First person (`we`, `our`, `let's`) → second person / imperative — **flag**; rewrite only the
  unambiguous cases.

## 3. Judgment items (surface — do NOT auto-rewrite)

List these for the user with file:line; propose a rewrite but don't apply without go-ahead:

- **Product vs common noun** — `MariaDB server` / `Galera cluster` written where the **branded
  product** (*MariaDB Server* / *Galera Cluster*) is meant. Most occurrences are correct common
  nouns; only flag the branded-context ones (titles, "the MariaDB Server product"), and let the
  author confirm.
- **SQL keyword casing in prose** — a statement name written lowercase (`select`, `create table`)
  where the SQL keyword is meant. Don't auto-uppercase — many keywords are also ordinary English
  words (`select`, `order`, `update`, `show`, `use`, `key`). Flag the clear statement references
  (prefer multi-word names like `CREATE TABLE`, `GROUP BY`, or terms already in an inline-`code`
  span); leave running prose alone.
- **Statements, not commands; keywords as code** — "the INSERT command" → "the `INSERT`
  statement"; "INSERTs" → "`INSERT` statements". Flag (it adds code formatting + reword).
- **Literals & placeholders** — literals should be inline `code`; placeholders *italic* with
  meaningful names (`table`, not `tbl`/`x`). Flag unformatted ones; don't mass-reformat blind.
- **Inclusive terms (master/slave)** — flag `master`/`slave` → **primary**/**replica** in core
  docs, but **do not auto-replace**: skip release notes, system/status variable names,
  `information_schema.slave_status`, and the SQL keyword `MASTER` (e.g. `CHANGE MASTER TO`); use
  **leader/follower** for ColumnStore. Discover with
  `git grep -Ei "master|slave|blacklist|whitelist|sanity|abort|basically|obviously|dummy"`.
- **Forward-looking statements** — flag claims about future/unreleased behavior; acceptable only
  when backed by an MDEV ticket with a Fix Version (see `doc-from-ticket`).
- **Over-linking** — more than one link to the same target within a section; suggest making the
  extras `literals`.
- **Oxford comma** — flag enumerations missing it ("A, B or C" → "A, B, or C").
- **"for example"** — flag where it can be cut or replaced by just showing the example.
- **Passive → active voice** and **long/run-on sentences** — propose, don't impose.
- **Tone/structure** — wall-of-text that should be a list/table/steps.
- **MySQL comparisons** — MariaDB docs *do* legitimately document MySQL compatibility (e.g.
  "MySQL Compatibility for …"). Do **not** strip MySQL mentions. Only flag a comparison that
  reads as casual/unnecessary aside (vs. an intentional compatibility note) for the author to
  judge. *(The "don't name MySQL" rule from the DX skill-files project applies to those shipped
  `SKILL.md` artifacts, not to the doc site.)*
- **Admonition fit** — prose that should be a `{% hint %}` (or a hint with the wrong style):
  recommend it and hand the actual block change to `gitbook-format`.
- **Terminology drift** — the page using a different term than neighboring pages for the same
  thing; flag for consistency.

## 4. Apply & validate

- Apply the §2 fixes with `Edit`; show the diff.
- **Re-read** changed regions to confirm the edits landed and didn't touch a code block.
- Run `.claude/hooks/doc-lint.sh <file>` (or the `docs-check` skill) to confirm spelling/links
  still pass and nothing broke.
- If the user said **lint-only**, skip the edits and just produce the §2 + §3 report.

## 5. Report

```
style-apply on <file>:
  Applied (mechanical):
    - L42 "Maxscale" → "MaxScale"
    - L88 dropped filler "simply"
  Surfaced (your call):
    - L17 passive voice → suggested: "<rewrite>"
    - L60 long sentence (48 words) → consider splitting
    - L73 MySQL aside — intentional compatibility note, or trim?
```

## Guardrails

- **Never edit inside fenced or `{% code %}` blocks.** Code samples are opaque.
- **Never expand `{alias}` links, reorder `SUMMARY.md`, or alter GitBook blocks** — those are
  out of scope (aliases: untouched; blocks: `gitbook-format`).
- **Scope to the page(s) given;** no whole-repo sweeps (use `bulk-campaign`).
- **The canonical style guide wins.** When unsure whether something is a violation, surface it
  as a judgment item rather than auto-changing it.
- **Don't change meaning.** Style edits preserve the technical content; if a "fix" would alter
  what the sentence asserts, flag it instead.
- **Don't fabricate** examples, caveats, or version claims to "improve" a page — that's content
  work (`doc-from-ticket`), not style.
