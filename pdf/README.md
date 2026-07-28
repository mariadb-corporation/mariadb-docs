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
attaches the results to a GitHub Release. It is `workflow_dispatch`-only: a full
run produces several hundred MB, so it is cut per documentation snapshot rather
than per push.

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
| `{% content-ref %}` | ~2,400 | collapsed to the link it contains |
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

## Size

Chrome emits no object streams and leaves roughly half its streams
uncompressed. `qpdf --object-streams=generate --recompress-flate` recovers
~35% (`galera-cluster`: 8.3 MB → 5.4 MB) with links, named destinations and
page count all intact. It runs automatically when `qpdf` is on `PATH`; skip it
with `--no-optimize`.

**Do not substitute Ghostscript.** It compresses harder but strips every
`/Link` and `/Dest` — on `galera-cluster`, 3,575 links and 743 destinations all
became zero — which destroys cross-reference navigation.

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
| `style.css` | print stylesheet (cover, TOC, callouts, tables, code) |
| `fetch-deps.sh` | fetches the Mermaid bundle into `pdf/vendor/` (gitignored) |
