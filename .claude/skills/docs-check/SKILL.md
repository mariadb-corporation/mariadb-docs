---
name: docs-check
description: Validate changed MariaDB documentation pages the way CI does, before committing or opening a PR. Use when the user asks to check docs, validate a page, run pre-PR checks, "check links", "run codespell", or before creating a docs PR. Runs codespell + lychee link-check on changed files and checks frontmatter, GitBook block balance, alias usage, and SUMMARY.md consistency, then reports pass/fail by check.
allowed-tools: Bash, Read, Grep, Glob
owners: [igusev]
last_verified: 2026-06-12
status: active
---

# docs-check

Mirrors the PR CI gates (codespell + lychee) locally and adds quick structural checks, so a
docs PR passes on the first push. Reference: `dev-docs/cookbook-pre-pr.md`.

## When to use

- Before committing doc changes or opening a PR.
- The user says: "check the docs", "validate this page", "run pre-PR checks", "check links",
  "run codespell", "will this pass CI?".

## Scope — which files

Default to the files the user changed. Determine the set in this order:

1. If the user named specific files/paths, use those.
2. Else use staged + unstaged changes vs `main`:
   ```bash
   git diff --name-only origin/main...HEAD -- '*.md' '*.html'; \
   git diff --name-only -- '*.md' '*.html'; \
   git diff --cached --name-only -- '*.md' '*.html'
   ```
   (de-duplicate the union; ignore deleted files).
3. If nothing changed, ask the user which space/path to check — **never** run across the whole
   repo unprompted (server alone is ~4,500 files).

## Checks

Run all that apply, then report each as PASS / FAIL / SKIPPED.

### 1–5. Spelling + links + includes + orphans + gutted pages — via `doc-lint.sh`

Run the **canonical** linter (the single source of truth for the CI-mirroring flags/excludes)
on the file set, from the repo root:

```bash
.claude/hooks/doc-lint.sh <files>
```

- It runs codespell and lychee with the exact CI-mirroring flags/excludes (defined only in
  `doc-lint.sh`) and exits non-zero on a real failure.
- If a tool isn't installed it prints a `SKIPPED` notice on stderr and does **not** fail —
  report that check as SKIPPED (`pipx install codespell`;
  lychee → https://github.com/lycheeverse/lychee).
- **Do not** re-spell the codespell flags or lychee excludes here — they live only in
  `doc-lint.sh`. If a codespell hit is a real term (not a typo), tell the user it can be added
  to `.codespellignore`; don't reword silently. Never report `{alias}` links as broken or
  expand them.
- It also resolves every relative `{% include %}` and fails on a **missing target** or one that
  **crosses a space boundary** (each top-level directory is a separate GitBook space, so a
  relative include may not leave it — cross-space reuse must use the by-ID form). This check has
  **no CI counterpart** and needs no external tool, so it never reports SKIPPED. It matters
  because a dead include renders as *nothing* — the page silently loses a section, and lychee
  cannot see `{% include %}` at all since it is template syntax, not a Markdown link. To fix,
  correct the `../` depth, or switch to
  `{% include "https://app.gitbook.com/s/<spaceId>/~/reusable/<reusableId>/" %}` when the snippet
  genuinely lives in another space. Added in DOCS-6372.
- It also gates **GitBook heading anchors** — a link to `page.md#some-heading` whose anchor no
  longer exists. No CI counterpart, and unlike every other check here it is *history-aware*: it
  reports only anchors that resolved at `DOC_LINT_BASE` (default `HEAD`) and are dead now, so the
  ~1,272 pre-existing dead anchors in the repo cannot fail unrelated work. It scans the whole
  tree rather than the changed files, because renaming a heading breaks inbound links from pages
  the commit never touched — expect the findings to name files the user did not edit, and treat
  that as the point, not a bug. **Never "fix" an anchor by deleting a dot or a dash to match
  what lychee wants**: `lychee --include-fragments` uses a GitHub-flavoured slugger that
  disagrees with GitBook and is wrong in both directions (386 false positives and 213 misses on
  `main`), which is why this check exists at all. Check a doubtful anchor against the rendered
  page, or with `.claude/hooks/fragcheck.py validate <file>`. Needs python3 and a git work tree;
  missing either is a SKIP. Costs ~14s, so `DOC_LINT_SKIP_FRAGMENTS=1` skips it while iterating.
  Added in DOCS-6491.
- **GitBook anchors `##`, `###` and `####` only.** A `#####` heading renders as a bold paragraph
  with no `id`, so it cannot be linked to. When repairing a dead anchor, add the missing heading
  at `####` or shallower: promoting a bold pseudo-heading to `#####` looks like a fix, drops the
  dead-anchor count, and still lands the reader at the top of the page (DOCS-6503). A link to one
  is reported `[unanchored-heading]`. A heading GitBook transliterates and the rules cannot
  reproduce — `中国` publishes as `zhong-guo` — is listed by `.claude/hooks/fragcheck.py risky`
  and reported `[uncertain-slug]`, never silently resolved against a guess.
- The same gate catches a heading that publishes **another heading's** anchor. Duplicate a
  heading line for a new section, edit its text but leave its `<a href="#x" id="x">` behind, and
  GitBook honours that explicit id over the text slug: the two sections share one anchor, the
  second dedupes to `-1`, and neither owns the anchor a reader expects. Every link still
  resolves, just to the wrong section, so no link checker — this one included — can see it from
  the links alone. `.claude/hooks/fragcheck.py ids` lists them. **A heading whose explicit id is
  a deliberate historical KB anchor for its own text is not flagged, and must not be
  "normalised"** — those ids exist to keep old inbound links working, and rewriting them breaks
  exactly what they preserve. On `main` 48 headings differed from their text slug and only 8 were
  defects, so treating the wide class as the bug would be a 6× overstatement. Added in DOCS-6492.
- It also gates **orphaned pages** — a page file with no entry in its space's `SUMMARY.md`.
  GitBook publishes only what `SUMMARY.md` lists, so the page never renders, and no other check
  here can see it: the markup is valid (codespell PASSes) and the links resolve (lychee PASSes);
  the page is simply never built. DOCS-6566 is the case — `dde0fb263` added four post-download
  pages without touching `platform/SUMMARY.md` and they sat unpublished for eight days with every
  gate green, until a reader reported them. Like the anchor gate it is **history-aware**, and for
  the same reason: `main` carries 219 pre-existing orphans (190 in `server`), so it reports only
  pages newly orphaned against `DOC_LINT_BASE` — added with no nav entry, or de-listed while the
  file survives. Needs python3 and a git work tree; missing either is a SKIP. Costs ~40 ms, so
  there is no skip flag. A deliberately unlisted page is legitimate: re-run with
  `DOC_LINT_ALLOW_ORPHAN='<path>'` and tell the user to say why in the commit message — report it
  as FAIL when unverified, WARN when acknowledged. For triage,
  `.claude/hooks/navcheck.py check [path ...]` lists every current orphan, not just the new ones.
  Added in DOCS-6567.
- It also flags a **gutted page** — any file that lost more than 40% of its lines *net*
  (deletions minus additions; min 20 lines lost, pre-image ≥ 30 lines) against `DOC_LINT_BASE`
  (default `HEAD`). No CI counterpart, never SKIPs. This catches what the other checks
  structurally cannot: a page that loses most of its body while the surviving markup stays valid
  and the remaining links resolve, so codespell and lychee both PASS. DOCS-6442 is the case —
  a campaign meant to remove one `{% columns %}` content-ref block from the Storage Engines
  landing page removed 23 of 24 (298 lines → 22, 24 content-refs → 1) with `SUMMARY.md`
  untouched, so nav listed 27 engines and the page listed one.
  **Do not silence this by reflex.** Verify the page first: for a landing page, compare its
  content-ref count with the space's `SUMMARY.md` children (`SUMMARY.md` is authoritative for
  nav — it is what DOCS-6442 used to rebuild the page). If the shrink is genuinely intended,
  re-run with `DOC_LINT_ALLOW_SHRINK='<path>'` and tell the user to state the reason in the
  commit message. Report it as FAIL when unverified, WARN when acknowledged.

The remaining checks below are **best-effort, LLM-performed heuristics** — report them as
warnings, not hard failures, and **ignore anything inside fenced code blocks (```) or
`{% code %}` blocks** (SQL/JSON/protocol samples legitimately contain `{`, `%`, raw URLs, and
brace-like text that would otherwise false-positive).

### 3. Frontmatter

For each changed page, confirm it opens with a YAML frontmatter block containing
`description:`. Flag new pages missing it. `icon:` is recommended, not required.

### 4. GitBook blocks balanced (heuristic)

Outside code blocks, check that block tags pair up:

- `{% hint %}` ↔ `{% endhint %}`, and every hint `style=` is one of
  `info`/`warning`/`danger`/`success` (flag `tip`/`warn`).
- `{% tabs %}`/`{% endtabs %}`, `{% tab %}`/`{% endtab %}`.
- `{% code %}`/`{% endcode %}`, `{% content-ref %}`/`{% endcontent-ref %}`.

Treat an apparent imbalance as a **warning** to confirm with the user, not a definite error —
a `{%`-like fragment inside a code sample is not a real block.

### 5. Link style (heuristic)

- Same-space links should be relative `.md` paths.
- Cross-space links should use `{alias}` (see `dev-docs/link-aliases.md`), not raw
  `app.gitbook.com` URLs. Flag any raw GitBook URL **in prose** (not in code samples).

### 6. SUMMARY.md consistency

**The orphan half of this is now automated** — `doc-lint.sh` fails on a page with no nav entry
(see the orphan gate above), so don't re-derive it by hand or second-guess its verdict. Until
DOCS-6567 this bullet was the repo's *only* orphan check, and being an LLM heuristic that runs
only when someone invokes the skill is exactly how DOCS-6566 shipped four unpublished pages.

What remains for you, because the automated gate does not cover it:

- `SUMMARY.md` entries pointing at **non-existent files** (the dangling direction — a nav entry
  whose target was deleted or renamed).
- Whether a moved/renamed page's entry sits in the **right place** in the tree and reads sensibly
  in context — ordering and nesting are editorial, not mechanical.

(Note: the nightly error-sync job legitimately auto-commits `server/SUMMARY.md` — don't treat its
entries as anomalies.)

### 7. Fact-check report present (heuristic, paper trail)

If the current branch is a `DOCS-XXXX` branch **and** the changed set includes doc-content pages,
check the paper trail (`dev-docs/cookbook-fact-trail.md`): read `reports_dir` from
`.claude/doc-sources.local.json` and find the ticket's report (it's grouped by space:
`find "$reports_dir" -type d -name 'DOCS-XXXX' -not -path '*/runs/*'`, then `report.md`). As a
light sanity pass, confirm the report's `Doc location` entries still point at files in the changed
set.

Treat a missing report or stale doc locations as a **warning**, not a failure — surface it so the
author runs `/doc-ticket` (to generate it) or `/verify-claims DOCS-XXXX` (to re-audit), and note
it's `SKIPPED` if `reports_dir` isn't configured or the branch isn't a `DOCS-XXXX` branch.

## Output

Report a compact summary, e.g.:

```
docs-check on 3 files:
  codespell ...... PASS
  lychee ......... FAIL (2 broken links — see below)
  includes ....... FAIL (dead include in platform/post-download/x.md:22)
  orphan pages ... FAIL (platform/post-download/x.md has no SUMMARY.md entry)
  gutted pages ... FAIL (storage-engines/README.md lost 93% of its lines net)
  frontmatter .... PASS
  gitbook blocks . FAIL (unclosed {% tabs %} in server/foo.md)
  link style ..... PASS
  SUMMARY.md ..... PASS
  fact-check ..... WARN (no report for DOCS-1234 under reports_dir — run /doc-ticket)
```

List each failure with file:line and a concrete fix. Don't auto-fix unless the user asks;
when you do fix, re-run the affected check to confirm.

## Notes

- This is a convenience gate; **CI is authoritative**. If a checker is missing locally, say so
  and remind the user CI will still run it.
- Do not modify `.github/workflows/*`, `help-tables/` (generated), or expand `{alias}` links.
