# PDF generation

Builds one PDF per GitBook space from the Markdown in this repository
(DOCS-5710). GitBook's own PDF export is capped at 100 pages per download, so
whole-space output has to be generated from source.

## Quick start

```bash
./pdf/fetch-deps.sh                 # once: fetch the Mermaid bundle
python3 pdf/build.py galera-cluster # one space -> dist/mariadb-galera-cluster.pdf
python3 pdf/build.py --all          # all eleven spaces
python3 pdf/build.py server --limit 50 --keep-html   # fast iteration
```

Requirements: `python3`, `pandoc` 3.x, Chrome or Chromium. Optional but
recommended: `qpdf` (lossless size pass), `poppler-utils` (page-count
reporting), `npm` (only for `fetch-deps.sh`).

In CI, `.github/workflows/generate-pdfs.yml` builds every space in parallel and
attaches the results to a GitHub Release. A full run produces several hundred MB,
so it is cut per documentation snapshot rather than per push:

- **Automatically**, at 04:00 UTC on the 15th of each month, so a current
  snapshot exists even in a month when nobody remembers to cut one. Scheduled
  runs publish immediately, because a draft release does not move
  `releases/latest`, which the documentation home page links to.
- **Manually** (`workflow_dispatch`), to re-cut after a Server release lands.
  Manual runs default to a draft so the output can be checked before it is
  published.

Both default to the tag `docs-pdf-YYYY-MM` — one release per calendar month, so
a mid-month re-cut replaces that month's assets rather than adding a
near-identical release. Pass an explicit `tag` to keep a snapshot separate.

## Output

| Space | Doc pages | PDF pages |
|-------|----------:|----------:|
| `server` | 4,101 | ~6,540 |
| `release-notes` | 2,772 | ~5,720 |
| `maxscale` | 771 | ~5,810 |
| `platform` | 813 | ~500 |
| `connectors` | 289 | ~660 |
| `analytics` | 174 | ~590 |
| `tools` | 128 | ~610 |
| `general-resources` | 124 | ~220 |
| `mariadb-cloud` | 110 | ~300 |
| `galera-cluster` | 101 | ~270 |
| `home` | 2 | ~7 |

There is deliberately **no combined all-spaces PDF**: concatenating every space
produces roughly 16,000 pages, which no reader handles usefully, and three
spaces account for 90% of it.

## How it works

```
SUMMARY.md ─▶ manifest ─▶ preprocess ─▶ pandoc (md→html) ─▶ Chrome --print-to-pdf ─▶ qpdf
```

1. **`SUMMARY.md` is the manifest.** It is GitBook's navigation tree, so it
   supplies both reading order and nesting depth — depth becomes the heading
   level, which becomes the PDF outline. Concatenating files alphabetically
   would scramble the reading order instead.

   Pages absent from `SUMMARY.md` (375 in `server/`) are unpublished and are
   excluded on purpose. Duplicate entries (56 repo-wide) are emitted once, at
   first appearance, so anchors stay unique.

2. **`gitbook_preprocess.py` rewrites the GitBook blocks.** Pandoc does not
   know them and passes them through as literal body text, so without this step
   readers see `{% hint style="info" %}` in the prose.

3. **Pandoc converts to an HTML fragment.** TeX math extensions are disabled —
   GitBook has no TeX support, so a `$` in shell prose is a dollar sign, and
   leaving math on renders phrases like `write_rate = ...` as mangled equations.

4. **Chrome prints it.** Not LaTeX: the corpus contains 118 pages with raw
   `<table>` markup and 111 with Mermaid diagrams, which a TeX engine cannot
   render. Chrome also lets `pdf/style.css` own the layout.

5. **`qpdf` repacks it losslessly** — see *Size* below.

## What the preprocessor handles

| Block | Occurrences | Treatment |
|-------|------------:|-----------|
| `{% @marketo/form %}` and other integrations | ~9,000 | dropped |
| `{% include %}` | ~9,000 | local files inlined; remote and boilerplate dropped |
| `{% column %}` / `{% columns %}` | ~6,200 | linearized (a PDF page is one column) |
| `{% content-ref %}` | ~2,400 | collapsed to a link labelled with the target's title |
| `{% hint %}` | ~1,690 | callout styled per severity |
| `{% tab %}` / `{% tabs %}` | ~1,400 | sequential labeled subsections |
| `{% step %}` / `{% stepper %}` | ~730 | explicitly numbered steps |
| `{% code title=… %}` | ~290 | title emitted as a caption |
| `{% embed %}`, `{% file %}`, `{% openapi %}`, `{% if %}`, `{% updates %}` | ~20 | reduced to link text, or unwrapped |
| ` ```mermaid ` fences | 111 files | rendered by Mermaid in the browser |
| `{server}`-style aliases | ~10 files | expanded to `mariadb.com/docs` URLs |

Two properties of the corpus shape the implementation:

- **Blocks span code fences.** A `{% stepper %}` opens, several fenced shell
  samples follow, then `{% endstepper %}` closes. Matching an open/close pair
  with a single `re.DOTALL` regex therefore fails on real pages, so block
  conversion is one line-oriented pass carrying fence state.
- **Markers are not always alone on a line.** `{% hint style="info" %} For the
  CTE…` occurs verbatim in the corpus, so replacements inject their own line
  breaks rather than assuming they own the line.

Anything inside a fenced code block is left untouched — a `{% hint %}` in a
GitBook-syntax example is content, not markup.

Two things are normalized per page because concatenation makes local quirks
global:

- **Unbalanced blocks are closed.** A page that opens `{% hint %}` without
  closing it would otherwise leave the generated container open to the end of
  the *whole space*, dragging every later page inside it.
- **Footnote labels are namespaced.** Nearly every page numbers its footnotes
  from `[^1]`, so concatenation collides them and readers get another page's
  footnote text.

### Links

In-space links are rewritten to internal PDF anchors, so cross-references still
work offline; without this every `.md` link in a concatenated document is dead.
Directory-style links resolve to that directory's `README.md`. Links that leave
the space point at `mariadb.com/docs`, since the target is not in this PDF.
Image paths are made absolute `file://` URLs and percent-decoded first, because
the source encodes them (`15%20(1).PNG`) while the filesystem does not.

### Cross-space links must be un-expanded first

`expand-gitbook-aliases.yml` rewrites every `{server}`-style alias that sits in a
link target into an app.gitbook.com **editor** URL and commits that back to the
branch. So in any checkout, a cross-space link already looks like:

```
https://app.gitbook.com/o/<org>/s/SsmexDFPv2xG2OTyO5yV/server-management/…
```

GitBook resolves those to `mariadb.com/docs` when it renders the site. Nothing
else does — so a PDF built from source has to reverse the mapping, or **every**
cross-space link sends the reader to the editor, which demands a login. That was
38,462 links across the corpus. `GITBOOK_SPACE_IDS` maps space ID → space, and a
page's published URL path is its repo-relative path minus `.md`.

Two cases need more than the obvious substitution:

- **Some links are invisible to a link regex.** Link text containing an escaped
  bracket (`[SHOW \[FULL\] PROCESSLIST](…)`) and links split over two lines by a
  migration hard break both occur in the corpus. A fallback pass rewrites the
  bare URL, which still lands the reader on the right page. It skips fenced *and*
  inline code, because `general-resources` documents the
  `app.gitbook.com/s/<id>` prefixes literally and rewriting them there would
  turn an explanation into a false statement.
- **Unmappable spaces are unlinked, not guessed.** A few links name a legacy
  pre-split space with no public equivalent; the link text is kept and the dead
  destination dropped, since sending a reader to a login screen is worse than
  not linking.

This is checked twice, because the failure is invisible in a 6,000-page PDF —
the link looks fine until someone clicks it. `build.py` warns if any editor URL
survives in prose, and the workflow fails the build if one reaches the PDF's own
link annotations. Both should always be zero; a hit means an unmapped space ID.

### Outbound URLs must drop the `.md`

A link that leaves the space is turned into a site URL, and the published URL is
the repo path **without** its suffix — `README.md` publishes as its own
directory. Leaving the `.md` on produces a **soft 404**: the site answers
`HTTP 200` with a 46 KB error page instead of the real 3 MB one, so a status-code
link check calls it healthy while the reader gets nothing. That affected 183
links (mostly `maxscale` and `release-notes`), which is why `build.py` counts
`.md`-suffixed site URLs and CI fails on them.

Unlike an in-space link, an outbound link **keeps its `#fragment`**: the target
page is not in this PDF, so the section anchor still does useful work on the
site. 405 links were losing one — `server-system-variables.md#wait_timeout`
dropped the reader at the top of a very long page rather than at the variable.

### Reference labels come from page titles

GitBook stores a `{% content-ref %}` with the target's *filename* as its link
text and renders the real page title from its own database, so 2,298 of the
corpus's 2,377 refs carry a label like
`backup-and-restore-via-dbforge-studio.md`. Printed verbatim, that is the one
place a PDF reference reads worse than the website.

The title is taken from `SUMMARY.md` first, so a reference names a page exactly
as the contents list and the PDF outline do; a page outside the navigation falls
back to its own H1. Only the label changes — the block's own URL is still what
gets linked.

Plain inline links are deliberately left alone. Five in the corpus have a label
ending in `.md`, and every one is a genuine reference to a repository file
(`CONTRIBUTING.md`, `install.md`), so blanket-rewriting labels would corrupt
them.

Two findings from this that are **source** bugs, not PDF bugs:

- ~~`expand-gitbook-aliases.yml` maps both `{skysql}` and `{release-notes}` to
  `aEnK0ZXmUbJzqQrTjFyb`. Every path under that ID resolves under
  `release-notes/`, so `{skysql}` links land in the wrong space.~~ Fixed in
  DOCS-6371: `{skysql}` now resolves to the MariaDB Cloud space, since SkySQL
  was renamed MariaDB Cloud and has no space of its own.
- 669 distinct cross-space targets (6,063 of 37,601 references) do not exist at
  the linked path in the checkout — for example error-code pages that moved out
  of `reference/mariadb-internals/using-mariadb-with-your-programs-api/`. Most
  still reach a page on the live site through a redirect: of a 40-target sample,
  33 resolved after following redirects and 7 ended in a 404, which puts the
  genuinely dead subset near 120. The PDF reproduces each link faithfully rather
  than guessing a replacement, so those few are dead in the PDF exactly as they
  are on the site.

## Brand colors and contrast

`style.css` uses the MariaDB brand palette (slide 26 of the corporate deck), and
every text/background pair is checked against WCAG 2.1 AA:

```bash
python3 pdf/check_contrast.py     # exits non-zero on any failure; runs in CI
```

| Color | Hex | On white | Used for |
|-------|-----|---------:|----------|
| Blue Azure | `#0E6488` | 6.57:1 AA | headings, links, default cover |
| Deep Ocean | `#003545` | 13.16:1 AAA | top-level headings, step labels |
| Granite | `#424F62` | 8.31:1 AAA | secondary and deep-TOC text |
| Open Seas | `#00838F` | 4.52:1 AA | rules; small text uses `#00707a` (5.84:1) |
| Sea Fresh | `#96DDCF` | 1.55:1 | fills only — table headers, step rules, alt cover |
| Electric Eel | `#ABC74A` | 1.91:1 | decorative rules only, never text |

Three deliberate decisions:

- **Never `opacity` for secondary text.** Dimming white to 75% over Blue Azure
  looks fine on screen and measures 4.45:1 — under the AA floor, and it landed
  on the 8.5pt legal line where contrast matters most. Secondary cover text uses
  explicit verified colors instead.
- **Warning and Important are intentionally off-palette.** The brand has no
  amber or red; forcing them into blues and greens would make a warning
  indistinguishable from a note. Being slightly off-brand is the better
  accessibility outcome. Color is never the only signal regardless — every
  callout carries a bold `Note:` / `Tip:` / `Warning:` / `Important:` label, so
  the distinction survives greyscale printing and color-vision deficiency.
- **Open Seas is darkened for small text.** At 4.52:1 it passes AA by 0.02,
  which is too fragile for 9pt labels; `#00707a` keeps the hue (185°) and
  saturation at 5.84:1.

### Cover treatments

```bash
python3 pdf/build.py server                      # Blue Azure, white text (default)
python3 pdf/build.py server --cover sea-fresh    # Sea Fresh, Deep Ocean text
```

Both exceed AA at every size: Blue Azure/white is 6.57:1, Sea Fresh/Deep Ocean
is 8.49:1.

The cover also carries a snapshot label, which **defaults to today's date** —
documentation here is continuously updated, so an undated PDF cannot be placed
in time. The workflow resolves it identically, so a local build and a CI build
label the cover the same way.

```bash
python3 pdf/build.py server                                  # Snapshot <today>
python3 pdf/build.py server --version-label "Snapshot July 2026"
python3 pdf/build.py server --version-label ""               # omit deliberately
```

The build echoes `cover label: …` before it starts, because an empty default
used to drop the date silently whenever the flag was forgotten.

## Size

Chrome emits no object streams and leaves roughly half its streams
uncompressed. `qpdf --object-streams=generate --recompress-flate` recovers
~35% (`galera-cluster`: 8.3 MB → 5.4 MB) with links, named destinations and
page count all intact. It runs automatically when `qpdf` is on `PATH`; skip it
with `--no-optimize`.

**Do not substitute Ghostscript.** It compresses harder but strips every
`/Link` and `/Dest` — on `galera-cluster`, 3,575 links and 743 destinations all
became zero — which destroys cross-reference navigation.

## Chrome does not reliably exit

Headless Chrome writes a complete, valid PDF and then *sometimes* keeps
running — observed on `tools` and `mariadb-cloud`, where the finished file sat
on disk while the process idled for tens of minutes. So `build.py` treats **the
output file as the completion signal, not process exit**: it polls the PDF's
size and terminates Chrome once that size has been stable for a few checks.
Verified equivalent to letting Chrome exit on its own — same 611 pages, 3,859
links and 1,397 destinations on `tools`, final page intact.

Two related traps:

- **`--virtual-time-budget` bounds nothing in wall-clock terms.** It advances a
  virtual clock; it will not stop a hung render. `CHROME_TIMEOUT_S` is the only
  real ceiling.
- **Always pass `--user-data-dir`.** Without it Chrome shares the default
  profile and can block on the singleton lock when another instance exists.

A space that still fails is reported and skipped rather than aborting the run,
matching `fail-fast: false` in the workflow — a full build is tens of minutes
and one bad space should not discard the rest.

## Known limitations

- **Remote reusable includes are dropped.** 3,269 includes point at
  `app.gitbook.com/…/~/reusable/…`, whose content lives only in GitBook and is
  unreachable from a source checkout. They are boilerplate (contributing
  notice, license, announcements), so the PDFs simply omit them — but this is
  why a PDF is not byte-identical to the rendered page.
- **Tabs lose interactivity.** Every panel is printed in sequence, so mutually
  exclusive alternatives (for example per-distribution install steps) all
  appear.
- **Headings flatten past six levels.** `server/` nests eight deep in
  `SUMMARY.md`; levels 7 and 8 render as level 6.
- **A few pages escape their block markers** (`\{% tabs %\}`), which stops
  GitBook rendering the block on the live site too. The preprocessor normalizes
  them so the PDF is correct; the source still wants fixing. Find them with:

  ```bash
  grep -rn '\\{%' --include='*.md' .
  ```

## Files

| File | Purpose |
|------|---------|
| `build.py` | manifest, assembly, Pandoc/Chrome/qpdf pipeline, CLI |
| `gitbook_preprocess.py` | GitBook-block rewriting, link and asset rewriting |
| `style.css` | print stylesheet: brand palette, cover, TOC, callouts, tables, code |
| `check_contrast.py` | asserts every text pair meets WCAG 2.1 AA (runs in CI) |
| `fetch-deps.sh` | fetches the Mermaid bundle into `pdf/vendor/` (gitignored) |
