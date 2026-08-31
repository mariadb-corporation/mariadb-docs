# Cookbook: pre-PR checklist

Run these checks **before committing / opening a PR** so the build passes on the first push.
They mirror the GitHub Actions that gate every PR. The fastest path is the **`docs-check`**
skill, which runs them for you; this page documents what it does and how to run them by hand.

## What CI checks

| Check | Tool | Workflow |
|-------|------|----------|
| Spelling (content + filenames) | `codespell` | `codespell.yml` |
| Broken links | `lychee` | `link-check-pr.yml` |
| Alias expansion | sed (auto-commit) | `expand-gitbook-aliases.yml` |
| Help-tables regen | Python | `generate-help-tables.yml` |

Only the first two can fail your PR; aliases and help-tables are regenerated automatically.

## 1. Spelling + links + includes + gutted pages — `doc-lint.sh`

The codespell and lychee invocations that mirror CI live in **one** place,
`.claude/hooks/doc-lint.sh`. Run it instead of re-typing the flags:

```bash
# Install the tools once:
pipx install codespell                                   # spelling
# lychee: cargo install lychee  (or brew / docker) — https://github.com/lycheeverse/lychee

# For a PR, check your WHOLE branch diff (not just staged) — this matches what CI lints:
git diff --name-only origin/main...HEAD -- '*.md' '*.html' \
  | xargs -r .claude/hooks/doc-lint.sh
```

`doc-lint.sh` runs codespell and lychee with the exact CI-mirroring flags/excludes (defined
only in that script), exits non-zero on a real failure, and prints a `SKIPPED` notice for any
tool that isn't installed (CI still runs it).

It also resolves every relative `{% include %}` in the file set and fails on a **missing target**
or one that **crosses a space boundary**. That check has **no CI counterpart** — `{% include %}`
is GitBook template syntax, not a Markdown link, so lychee is blind to it and a dead include just
renders as nothing, silently dropping a section from the page. It needs no external tool, so it
never SKIPs. (Added in DOCS-6372, which found two live cases this way.)

It also gates **heading anchors** — links of the form `page.md#some-heading`. This one is
history-aware: it reports only anchors that resolved at `DOC_LINT_BASE` (default `HEAD`) and are
dead in the working tree, because the repo carries ~1,272 pre-existing dead anchors and a plain
check would fail every PR on breakage it did not introduce. It also scans the whole tree instead
of the changed files, since renaming a heading breaks inbound links from pages the commit never
touched — so findings naming files you did not edit are the check working, not noise.

Enabling `--include-fragments` in lychee would *not* substitute for this. lychee's slugger is
GitHub-flavoured and GitBook's is not, so on `main` it produced 386 false positives (the anchor
resolves live) while missing 213 anchors that really are dead. Never delete a dot or a dash from
an anchor to satisfy it; check the rendered page instead, or run
`.claude/hooks/fragcheck.py validate <file>`, which compares computed anchors against the ids
the live site emits. `.claude/hooks/fragcheck.py check` prints the whole current inventory with a
suggested target for each mechanically fixable one.

**GitBook publishes a heading anchor for `##`, `###` and `####` only.** A `#####` heading
renders as a bold paragraph with no `id`, so it is not a link target at all. That matters when
you are repairing a dead anchor: adding the missing heading works only at `####` or shallower,
and promoting a bold pseudo-heading to `#####` produces a page that looks fixed and still sends
the reader to the top (DOCS-6503). A link pointing at one is reported `[unanchored-heading]` —
raise the heading or retarget the link at the enclosing section. A heading GitBook
transliterates and the checker cannot reproduce — `中国` publishes as `zhong-guo` — is listed by
`.claude/hooks/fragcheck.py risky` and reported `[uncertain-slug]` rather than guessed at.

The same gate catches one thing no link checker can: a heading that publishes **another
heading's** anchor. Duplicate a heading line for a new section, edit its text but leave its
`<a href="#x" id="x">` behind, and GitBook honours that explicit id over the text slug — the two
sections share one anchor, the second dedupes to `-1`, and neither owns the anchor a reader
expects. Every link still resolves, just to the wrong section (DOCS-6492), which is exactly why
no checker sees it. `.claude/hooks/fragcheck.py ids` lists them. A heading whose explicit id is a
deliberate historical KB anchor for its own text is **not** flagged, and must not be
"normalised" — those ids exist to keep old inbound links working.

Needs python3 and a git work tree — either missing is a SKIP — and costs about 14 seconds:

```bash
# skip it while iterating on wording
DOC_LINT_SKIP_FRAGMENTS=1 .claude/hooks/doc-lint.sh <files>
```

(Added in DOCS-6491.)

Finally, it flags a **gutted page**: any file in the set that lost more than **40%** of its lines
*net* (deletions minus additions, minimum 20 lines lost, pre-image at least 30 lines) against
`DOC_LINT_BASE` (default `HEAD`). This has no CI counterpart either, and it exists because the
other checks are blind to it — when a page loses most of its body but the surviving markup is
valid and the remaining links resolve, codespell and lychee both PASS. That is exactly what
happened in DOCS-6442: a retirement campaign meant to delete one `{% columns %}` content-ref
block from the Storage Engines landing page and deleted 23 of 24 instead (298 lines → 22,
24 content-refs → 1). `SUMMARY.md` was untouched, so the nav still listed all 27 engines while
the page listed one; a reader found it two days later.

Net loss is the metric, not raw deletions — raw deletions flag every reformatting campaign (alias
expansion, hard-break removal, changelog normalization), because those *rewrite* lines. Measured
over 300 commits of this repo: raw deletions >40% flags 17 files, net loss >40% flags 4.

A big shrink is often correct, so this gate is meant to be **acknowledged, not silenced**:

```bash
# after confirming the page still covers what it should
DOC_LINT_ALLOW_SHRINK='path/to/README.md' .claude/hooks/doc-lint.sh <files>
```

and say why in the commit message. Tunable: `DOC_LINT_SHRINK_PCT`, `DOC_LINT_SHRINK_MIN`,
`DOC_LINT_SHRINK_FLOOR`, `DOC_LINT_BASE`; `DOC_LINT_ALLOW_SHRINK=all` disables the check.
For a landing page, the fastest confirmation is to compare its content-ref count against the
space's `SUMMARY.md` children — `SUMMARY.md` is authoritative for nav, and it is what DOCS-6442
used to rebuild the page.

- A real term flagged as a typo? Add it to `.codespellignore` (one word per line) — sparingly.
- The lychee exclude set skips **any URL containing `{` or `%7B`** — which covers `{alias}`
  links (so they never trip link-check), but also means a genuinely broken link that happens to
  contain a brace would be skipped too. Don't rely on lychee to catch braced URLs; just don't
  hand-expand aliases.

> **CI failure notices.** When a workflow run fails on GitHub, the run summary may link to
> internal Atlassian SOP pages (`mariadbcorp.atlassian.net/...`) for fix steps. Those URLs
> require MariaDB SSO — they're not public and won't open from an external browser session.

> **Hook vs. PR scope.** The pre-commit hook and `/precommit` check only **staged** files; CI
> checks the **full PR diff**. Passing the hook is not a guarantee CI passes — run the
> whole-branch command above before opening the PR. (See `.claude/README.md`.)

## 2. Structural sanity checks (heuristic)

These aren't enforced by CI but catch common GitBook mistakes. They're heuristics — **ignore
anything inside fenced code blocks (```) or `{% code %}` blocks**, since SQL/JSON/protocol
samples legitimately contain `{`, `%`, and raw URLs.

- **Frontmatter:** new pages have `description:` (and usually `icon:`).
- **`SUMMARY.md`:** if you added/moved/renamed a page, its `SUMMARY.md` entry exists, points at
  the right path, and matches the surrounding indentation/link style. (The nightly error-sync
  job legitimately auto-commits `server/SUMMARY.md` — that's an authorized exception.)
- **Retired/moved URLs → redirects:** if the PR renames, moves, or deletes published pages,
  produce a GitBook redirect CSV so old bookmarks don't dead-end (there's no in-repo redirect
  mechanism). See `dev-docs/cookbook-gitbook-redirects.md` or run `/redirects-csv`.
- **GitBook blocks:** hints use a valid style (`info`/`warning`/`danger`/`success`); `tabs`,
  `code`, `content-ref` blocks are balanced (every open has its `end…`).
- **Links:** same-space links are relative `.md` paths; cross-space links use `{alias}`.
- **Generated content:** you did **not** hand-edit `help-tables/` or server error-code pages —
  edit the source reference page instead.

## Automating it

- **`/precommit`** — runs the checks on **staged** files on demand.
- **`docs-check`** skill — runs them against your changed files and reports by check.
- **Pre-commit hook** (`.claude/hooks/pre-commit.sh`, wired in `.claude/settings.json`) — runs
  `doc-lint.sh` on staged files when **Claude Code** runs `git commit`, blocking on real
  failures and warning (without blocking) if a tool isn't installed. It does **not** gate human
  or GitBook-UI commits — see `.claude/README.md`.
