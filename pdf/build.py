#!/usr/bin/env python3
"""Build a per-space PDF of the MariaDB documentation.

    python3 pdf/build.py server
    python3 pdf/build.py --all --out-dir dist
    python3 pdf/build.py server --limit 50      # quick iteration

Page order and heading hierarchy come from the space's `SUMMARY.md`, which is
GitBook's own navigation tree -- alphabetical concatenation would scramble the
reading order. Pages not listed there (375 in `server/`) are unpublished and
excluded on purpose.

Pipeline: SUMMARY.md -> manifest -> preprocess -> Pandoc (md->html) ->
headless Chrome --print-to-pdf. Chrome rather than LaTeX because the corpus
contains raw HTML tables and Mermaid diagrams that a TeX engine cannot render.
"""

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitbook_preprocess import preprocess  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(REPO_ROOT, "pdf")
WEB_BASE = "https://mariadb.com/docs"

# Human-facing titles; the directory name is not always presentable.
SPACE_TITLES = {
    "server": "MariaDB Server",
    "release-notes": "MariaDB Release Notes",
    "maxscale": "MariaDB MaxScale",
    "platform": "MariaDB Enterprise Platform",
    "connectors": "MariaDB Connectors",
    "analytics": "MariaDB Analytics and ColumnStore",
    "tools": "MariaDB Tools",
    "mariadb-cloud": "MariaDB Cloud",
    "general-resources": "MariaDB General Resources",
    "galera-cluster": "MariaDB Galera Cluster",
    "home": "MariaDB Documentation",
}

# `help-tables/` is generated SQL, and the remaining top-level directories are
# include containers or contributor docs -- none are browsable spaces.
ALL_SPACES = [
    "server", "release-notes", "maxscale", "platform", "connectors",
    "analytics", "tools", "mariadb-cloud", "general-resources",
    "galera-cluster", "home",
]

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome-stable", "google-chrome", "chromium-browser", "chromium",
]


def find_chrome():
    for cand in CHROME_CANDIDATES:
        if os.path.isabs(cand):
            if os.path.isfile(cand) and os.access(cand, os.X_OK):
                return cand
        else:
            found = shutil.which(cand)
            if found:
                return found
    sys.exit("error: no Chrome/Chromium binary found (see CHROME_CANDIDATES)")


# ---------------------------------------------------------------------------
# SUMMARY.md -> manifest
# ---------------------------------------------------------------------------

ENTRY_RE = re.compile(r"^(\s*)\*\s*\[(.+?)\]\((.+?)\)\s*$")


def parse_summary(space):
    """Return [(depth, title, space_relative_path)] in navigation order.

    Indent width is inferred per line rather than assumed to be two spaces,
    and duplicate targets (56 repo-wide) are kept once, at first appearance,
    so anchors stay unique.
    """
    summary = os.path.join(REPO_ROOT, space, "SUMMARY.md")
    entries, seen = [], set()
    indents = []
    raw = []
    for line in open(summary, encoding="utf-8"):
        m = ENTRY_RE.match(line.rstrip("\n"))
        if not m:
            continue
        indent, title, target = len(m.group(1)), m.group(2), m.group(3)
        if target.startswith(("http://", "https://", "#")):
            continue
        raw.append((indent, title, target.split("#")[0]))
        indents.append(indent)

    # Normalize indentation to depth levels.
    unique_indents = sorted(set(indents))
    depth_of = {ind: i for i, ind in enumerate(unique_indents)}

    for indent, title, target in raw:
        if target in seen:
            continue
        abs_path = os.path.join(REPO_ROOT, space, target)
        if not os.path.isfile(abs_path):
            print(f"  warn: SUMMARY target missing, skipped: {target}",
                  file=sys.stderr)
            continue
        seen.add(target)
        entries.append((depth_of[indent], title.strip(), target))
    return entries


def anchor_for(path):
    """Stable, unique, short HTML id derived from the page path.

    Deep paths in `server/` produce slugs well past the 127-byte limit PDF
    places on name tokens, which makes readers reject the destination. A
    truncated slug plus a hash of the full path stays inside the limit while
    remaining unique and human-recognizable.
    """
    slug = re.sub(r"[^a-z0-9]+", "-",
                  path.lower().removesuffix(".md")).strip("-")
    digest = hashlib.sha1(path.encode("utf-8")).hexdigest()[:8]
    return f"pg-{slug[-60:].lstrip('-')}-{digest}"


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def build_markdown(space, entries, limit=None):
    space_dir = os.path.join(REPO_ROOT, space)
    if limit:
        entries = entries[:limit]

    anchors = {path: anchor_for(path) for _, _, path in entries}

    chunks = []
    for depth, title, path in entries:
        abs_path = os.path.join(space_dir, path)
        try:
            with open(abs_path, encoding="utf-8") as fh:
                src = fh.read()
        except OSError as exc:
            print(f"  warn: unreadable {path}: {exc}", file=sys.stderr)
            continue
        chunks.append(preprocess(
            src,
            page_path=abs_path,
            space_dir=space_dir,
            anchors=anchors,
            heading_offset=depth,
            web_base=WEB_BASE,
            anchor_id=anchors[path],
            title=title,
        ))
    return "\n\n".join(chunks), entries


# SUMMARY.md titles carry Markdown escapes from the GitBook migration
# (`wsrep\_provider\_options`). The TOC is emitted as raw HTML, so they have to
# be unescaped here or the backslashes show up in the rendered contents list.
MD_ESCAPE_RE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!<>|~])")


def clean_title(title):
    return MD_ESCAPE_RE.sub(r"\1", title).strip()


# Only count markers naming a real GitBook block. A bare `{%` also occurs in
# legitimate content -- `sformat('arg1: {%W %M %Y}')` in the SQL reference --
# and flagging that would train readers to ignore this warning.
LEAK_RE = re.compile(
    r"\{%\s*(?:end)?(?:hint|tabs?|stepper|step|columns?|code|content-ref"
    r"|embed|file|include|openapi|updates?|if)\b")


def count_leaked_markers(markdown):
    return len(LEAK_RE.findall(markdown))


def build_toc_html(entries):
    """A clickable table of contents mirroring SUMMARY.md."""
    rows = []
    for depth, title, path in entries:
        rows.append(
            f'<li class="toc-d{min(depth, 5)}">'
            f'<a href="#{anchor_for(path)}">{html.escape(clean_title(title))}</a></li>')
    return ('<nav class="toc"><h1>Contents</h1><ul>'
            + "".join(rows) + "</ul></nav>")


# Math and raw-TeX extensions must be OFF: GitBook has no TeX support, so a
# `$` in shell prose is a dollar sign, not the start of an equation. Leaving
# them on renders phrases like `write_rate = ...` as mangled math.
PANDOC_FROM = (
    "markdown"
    "+fenced_divs+pipe_tables+raw_html+autolink_bare_uris"
    "+backtick_code_blocks+footnotes+strikeout+task_lists+header_attributes"
    "-tex_math_dollars-tex_math_single_backslash-tex_math_double_backslash"
    "-raw_tex-latex_macros-citations"
)


def run_pandoc(markdown, title):
    """Convert the assembled Markdown to an HTML fragment.

    Syntax highlighting is disabled so print CSS owns code styling and the
    intermediate HTML stays small on a 4,000-page space.
    """
    cmd = [
        "pandoc",
        "--from", PANDOC_FROM,
        "--to", "html5",
        "--syntax-highlighting=none",
        "--wrap", "none",
        "--metadata", f"title={title}",
    ]
    proc = subprocess.run(cmd, input=markdown, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"error: pandoc failed:\n{proc.stderr[:4000]}")
    if proc.stderr.strip():
        print(f"  pandoc notes: {proc.stderr.strip()[:500]}", file=sys.stderr)
    return proc.stdout


MERMAID_JS = os.path.join(PDF_DIR, "vendor", "mermaid.min.js")


def load_mermaid():
    """Return the Mermaid bundle, or None to fall back to plain code blocks.

    The 3.5 MB bundle is fetched by `pdf/fetch-deps.sh` rather than committed;
    without it the 111 pages with diagrams still build, showing diagram source.
    """
    if os.path.isfile(MERMAID_JS):
        with open(MERMAID_JS, encoding="utf-8") as fh:
            return fh.read()
    print("  note: pdf/vendor/mermaid.min.js absent -- diagrams will render as "
          "source text (run pdf/fetch-deps.sh to enable)", file=sys.stderr)
    return None


def build_html(space, body_html, toc_html, entries, version_label):
    with open(os.path.join(PDF_DIR, "style.css"), encoding="utf-8") as fh:
        css = fh.read()
    mermaid_js = load_mermaid()
    mermaid_block = (
        f"<script>{mermaid_js}</script>\n<script>"
        "(async () => {"
        "  try {"
        "    mermaid.initialize({ startOnLoad: false, theme: 'neutral' });"
        "    await mermaid.run({ querySelector: 'pre.mermaid' });"
        "  } catch (e) { console.error('mermaid', e); }"
        "  window.__renderComplete = true;"
        "})();</script>"
        if mermaid_js else
        "<script>window.__renderComplete = true;</script>"
    )

    title = SPACE_TITLES.get(space, space)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{css}</style>
</head><body>
<section class="cover">
  <h1>{html.escape(title)}</h1>
  <p class="subtitle">Documentation</p>
  <p class="meta">{html.escape(version_label)}<br>{len(entries)} pages</p>
  <p class="legal">&copy; MariaDB. Content licensed CC BY-SA / GNU FDL.
  The authoritative, continuously updated version of this documentation is at
  <a href="{WEB_BASE}">mariadb.com/docs</a>.</p>
</section>
{toc_html}
<main>
{body_html}
</main>
{mermaid_block}
</body></html>
"""


def html_to_pdf(html_path, pdf_path, chrome):
    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--allow-file-access-from-files",
        "--virtual-time-budget=600000",
        f"--print-to-pdf={pdf_path}",
        # Percent-encode: an --out-dir containing spaces would otherwise
        # truncate the URL and Chrome would print an error page.
        "file://" + quote(os.path.abspath(html_path)),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
    if not os.path.isfile(pdf_path):
        sys.exit(f"error: Chrome produced no PDF:\n{proc.stderr[:4000]}")


def build_space(space, out_dir, version_label, limit=None, keep_html=False,
                no_optimize=False):
    print(f"[{space}] parsing SUMMARY.md")
    entries = parse_summary(space)
    print(f"[{space}] {len(entries)} pages in navigation order")

    print(f"[{space}] preprocessing")
    markdown, entries = build_markdown(space, entries, limit)

    leaked = count_leaked_markers(markdown)
    if leaked:
        print(f"[{space}] warn: {leaked} unconverted GitBook markers remain",
              file=sys.stderr)

    print(f"[{space}] pandoc")
    body_html = run_pandoc(markdown, SPACE_TITLES.get(space, space))
    page = build_html(space, body_html, build_toc_html(entries), entries,
                      version_label)

    os.makedirs(out_dir, exist_ok=True)
    html_path = os.path.join(out_dir, f"mariadb-{space}.html")
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(page)

    pdf_path = os.path.join(out_dir, f"mariadb-{space}.pdf")
    print(f"[{space}] rendering PDF via Chrome")
    html_to_pdf(html_path, pdf_path, find_chrome())

    if not no_optimize:
        print(f"[{space}] optimizing")
        optimize_pdf(pdf_path)

    if not keep_html:
        os.remove(html_path)

    size_mb = os.path.getsize(pdf_path) / 1e6
    pages = pdf_page_count(pdf_path)
    print(f"[{space}] done: {pdf_path} ({size_mb:.1f} MB, {pages} PDF pages)")
    return {"space": space, "pdf": pdf_path, "size_mb": size_mb,
            "pdf_pages": pages, "doc_pages": len(entries),
            "leaked_markers": leaked}


def optimize_pdf(path):
    """Losslessly shrink the PDF with qpdf, preserving every link.

    Chrome emits no object streams and leaves roughly half its streams
    uncompressed, so repacking saves ~35% (8.3 MB -> 5.4 MB on
    `galera-cluster`) with links, named destinations and page count untouched.

    Ghostscript shrinks more but strips every /Link and /Dest, which would kill
    cross-reference navigation -- do not substitute it here.
    """
    if not shutil.which("qpdf"):
        print("  note: qpdf absent -- skipping lossless size optimization",
              file=sys.stderr)
        return

    tmp = path + ".opt"
    proc = subprocess.run(
        ["qpdf", "--object-streams=generate", "--compress-streams=y",
         "--recompress-flate", "--compression-level=9", "--linearize",
         path, tmp],
        capture_output=True, text=True)
    # qpdf exits 3 on recoverable warnings and still writes valid output.
    if proc.returncode not in (0, 3) or not os.path.isfile(tmp):
        print(f"  warn: qpdf failed, keeping unoptimized PDF: "
              f"{proc.stderr.strip()[:300]}", file=sys.stderr)
        if os.path.isfile(tmp):
            os.remove(tmp)
        return

    before = os.path.getsize(path)
    after = os.path.getsize(tmp)
    if after >= before:
        os.remove(tmp)
        return
    os.replace(tmp, path)
    print(f"  optimized: {before / 1e6:.1f} MB -> {after / 1e6:.1f} MB "
          f"({100 * (1 - after / before):.0f}% smaller)")


def pdf_page_count(path):
    if not shutil.which("pdfinfo"):
        return "?"
    proc = subprocess.run(["pdfinfo", path], capture_output=True, text=True)
    m = re.search(r"^Pages:\s+(\d+)", proc.stdout, re.MULTILINE)
    return int(m.group(1)) if m else "?"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spaces", nargs="*", help="space directories to build")
    ap.add_argument("--all", action="store_true", help="build every space")
    ap.add_argument("--out-dir", default=os.path.join(REPO_ROOT, "dist"))
    ap.add_argument("--limit", type=int, help="only the first N pages (testing)")
    ap.add_argument("--version-label", default="",
                    help="text for the cover page, e.g. 'Snapshot 2026-07-28'")
    ap.add_argument("--keep-html", action="store_true",
                    help="retain the intermediate HTML for debugging")
    ap.add_argument("--no-optimize", action="store_true",
                    help="skip the qpdf lossless size pass")
    ap.add_argument("--list-spaces", action="store_true",
                    help="print the buildable spaces as JSON and exit; with "
                         "space arguments, validate them first (CI matrix)")
    args = ap.parse_args()

    # A full run takes tens of minutes; unbuffered output lets CI logs and
    # `tail -f` show which space is in flight instead of nothing until the end.
    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)

    if args.list_spaces:
        wanted = args.spaces or ALL_SPACES
        unknown = [s for s in wanted if s not in ALL_SPACES]
        if unknown:
            ap.error(f"not a documentation space: {', '.join(unknown)}")
        print(json.dumps(wanted))
        return

    spaces = ALL_SPACES if args.all else args.spaces
    if not spaces:
        ap.error("name at least one space, or pass --all")
    unknown = [s for s in spaces if s not in ALL_SPACES]
    if unknown:
        ap.error(f"not a documentation space: {', '.join(unknown)}")

    if not shutil.which("pandoc"):
        sys.exit("error: pandoc is not installed")

    results = [build_space(s, args.out_dir, args.version_label, args.limit,
                           args.keep_html, args.no_optimize) for s in spaces]

    print("\n=== summary ===")
    for r in results:
        print(f"{r['space']:20} {r['doc_pages']:5} docs  "
              f"{str(r['pdf_pages']):>6} pages  {r['size_mb']:6.1f} MB"
              + (f"  ({r['leaked_markers']} leaked)" if r["leaked_markers"] else ""))


if __name__ == "__main__":
    main()
