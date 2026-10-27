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
headless Chrome (Page.printToPDF over the DevTools protocol). Chrome rather
than LaTeX because the corpus contains raw HTML tables and Mermaid diagrams
that a TeX engine cannot render.
"""

import argparse
import base64
import datetime
import fcntl
import hashlib
import html
import json
import os
import re
import select
import shutil
import subprocess
import sys
import tempfile
import time
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitbook_preprocess import (  # noqa: E402
    INLINE_CODE_RE, iter_lines, preprocess, unescape_md)

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
    "gridgain-8": "GridGain 8",
    "gridgain-9": "GridGain 9",
}

# `help-tables/` is generated SQL, and the remaining top-level directories are
# include containers or contributor docs -- none are browsable spaces.
ALL_SPACES = [
    "server", "release-notes", "maxscale", "platform", "connectors",
    "analytics", "tools", "mariadb-cloud", "general-resources",
    "galera-cluster", "home", "gridgain-8", "gridgain-9",
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
    # Reference labels come from these, so a `{% content-ref %}` names the page
    # the same way the contents list and the PDF outline do.
    titles = {path: clean_title(title) for _, title, path in entries}

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
            titles=titles,
        ))
    return "\n\n".join(chunks), entries


# SUMMARY.md titles carry Markdown escapes from the GitBook migration
# (`wsrep\_provider\_options`). The TOC is emitted as raw HTML, so they have to
# be unescaped here or the backslashes show up in the rendered contents list.
def clean_title(title):
    return unescape_md(title)


# Only count markers naming a real GitBook block. A bare `{%` also occurs in
# legitimate content -- `sformat('arg1: {%W %M %Y}')` in the SQL reference --
# and flagging that would train readers to ignore this warning.
LEAK_RE = re.compile(
    r"\{%\s*(?:end)?(?:hint|tabs?|stepper|step|columns?|code|content-ref"
    r"|embed|file|include|openapi|updates?|if)\b")


def count_leaked_markers(markdown):
    return len(LEAK_RE.findall(markdown))


# Two ways an outbound link can be built wrong, both of which look like a
# working link in the PDF and so cannot be caught by eye in 6,000 pages:
#
# - an app.gitbook.com *editor* URL that escaped the rewriter (see
#   `GITBOOK_SPACE_IDS`), which demands a login;
# - a published URL still carrying its `.md` source suffix, which the site
#   answers with an HTTP 200 soft-404 -- so even a link checker calls it fine
#   while the reader gets an error page.
EDITOR_URL_RE = re.compile(r"app\.gitbook\.com", re.I)
SUFFIXED_URL_RE = re.compile(r"https?://mariadb\.com/docs/[^\s)\"'<>]*\.md\b",
                             re.I)


def _count_in_prose(markdown, pattern):
    """Count `pattern` outside fenced and inline code.

    Code is skipped for the same reason the preprocessor skips it: a URL inside
    a fence is content, not a link. `general-resources` documents both the
    `app.gitbook.com/s/<id>` prefixes and a `.md` alias example literally, and
    MaxScale has an editor URL in a SQL comment -- counting those would make
    these warnings fire on every build and train readers to ignore them.
    """
    count = 0
    for line, in_code in iter_lines(markdown):
        if in_code:
            continue
        count += len(pattern.findall(INLINE_CODE_RE.sub("", line)))
    return count


def count_editor_urls(markdown):
    return _count_in_prose(markdown, EDITOR_URL_RE)


def count_suffixed_urls(markdown):
    return _count_in_prose(markdown, SUFFIXED_URL_RE)


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


def build_html(space, body_html, toc_html, entries, version_label,
               cover="azure"):
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
    cover_class = COVER_CLASS[cover]
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{css}</style>
</head><body>
<section class="cover cover-{cover_class}">
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


class RenderError(RuntimeError):
    """Chrome failed to produce a PDF for one space."""


# Chrome is driven over the DevTools protocol, not with --print-to-pdf. That
# flag hands the finished PDF back in one piece, and Chrome 155's renderer dies
# on one that large: release-notes (~308 MB before qpdf) failed on every run
# with "V8 error: Empty MaybeLocal" while each half of it printed fine
# (DOCS-6945). Page.printToPDF with transferMode=ReturnAsStream returns the PDF
# in chunks instead, and gives the same pages, links and destinations.
#
# The protocol runs over --remote-debugging-pipe -- Chrome reads fd 3, writes
# fd 4, NUL-delimited JSON -- so it needs no WebSocket library. Controlling the
# session also retires two workarounds: the page itself says when it is ready
# (`window.__renderComplete`, set after Mermaid), where --virtual-time-budget
# only advanced a virtual clock; and the build closes Chrome itself, where
# --print-to-pdf sometimes left it idling for tens of minutes after writing the
# file.
CHROME_TIMEOUT_S = 1800
READY_POLL_S = 0.5
PDF_CHUNK = 8 << 20         # bytes per IO.read; the result is base64 on top
PAGE_READY_JS = ("document.readyState === 'complete'"
                 " && window.__renderComplete === true")


class ChromePipe:
    """One headless Chrome, spoken to over the DevTools protocol pipe."""

    def __init__(self, chrome, deadline):
        self.deadline = deadline
        # Private profile: never contend with another instance's singleton lock.
        self.profile = tempfile.mkdtemp(prefix="mariadb-pdf-chrome-")
        self.log = open(os.path.join(self.profile, "stderr.log"), "w+")
        to_r, self.wr = os.pipe()        # Chrome reads on fd 3
        self.rd, from_w = os.pipe()      # Chrome writes on fd 4

        def child_fds():
            # Park both ends above fd 9 first. os.pipe() can itself return 3
            # or 4, and dup2 onto the same number would keep close-on-exec.
            a = fcntl.fcntl(to_r, fcntl.F_DUPFD_CLOEXEC, 10)
            b = fcntl.fcntl(from_w, fcntl.F_DUPFD_CLOEXEC, 10)
            os.dup2(a, 3)
            os.dup2(b, 4)

        self.proc = subprocess.Popen(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox",
             "--remote-debugging-pipe", f"--user-data-dir={self.profile}",
             "--no-first-run", "--disable-extensions",
             "--allow-file-access-from-files", "about:blank"],
            # close_fds runs after preexec_fn and would close fds 3 and 4
            # again. Everything else Python opens is non-inheritable anyway.
            close_fds=False, preexec_fn=child_fds,
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=self.log)
        os.close(to_r)
        os.close(from_w)
        self.buf = b""
        self.next_id = 0

    def diagnosis(self):
        """Chrome's own account of a failure, without the dbus noise."""
        self.log.seek(0)
        lines = self.log.read().splitlines()
        fatal = [ln for ln in lines
                 if "FATAL" in ln or "renderer termination" in ln]
        return "\n".join(fatal or lines[-20:])[:2000]

    def _recv(self):
        while b"\0" not in self.buf:
            left = self.deadline - time.monotonic()
            if left <= 0:
                raise RenderError(
                    f"Chrome exceeded {CHROME_TIMEOUT_S}s with no complete PDF")
            ready, _, _ = select.select([self.rd], [], [], min(left, 5))
            if not ready:
                continue
            chunk = os.read(self.rd, 1 << 20)
            if not chunk:
                raise RenderError(
                    f"Chrome exited mid-render:\n{self.diagnosis()}")
            self.buf += chunk
        msg, self.buf = self.buf.split(b"\0", 1)
        return json.loads(msg)

    def call(self, method, params=None, session=None):
        self.next_id += 1
        msg = {"id": self.next_id, "method": method, "params": params or {}}
        if session:
            msg["sessionId"] = session
        data = json.dumps(msg).encode() + b"\0"
        while data:
            data = data[os.write(self.wr, data):]
        while True:
            reply = self._recv()
            if reply.get("method") == "Inspector.targetCrashed":
                raise RenderError(
                    f"Chrome's renderer crashed:\n{self.diagnosis()}")
            if reply.get("id") == self.next_id:
                if "error" in reply:
                    raise RenderError(
                        f"{method} failed: {reply['error'].get('message')}\n"
                        f"{self.diagnosis()}")
                return reply["result"]
            # Anything else is an event this build has no use for.

    def close(self):
        try:
            if self.proc.poll() is None:
                self.deadline = time.monotonic() + 10
                self.call("Browser.close")
        except (RenderError, OSError):
            pass
        try:
            self.proc.wait(timeout=30)
        except subprocess.TimeoutExpired:
            self.proc.kill()
            self.proc.wait(timeout=30)
        for fd in (self.wr, self.rd):
            os.close(fd)
        self.log.close()
        shutil.rmtree(self.profile, ignore_errors=True)


def html_to_pdf(html_path, pdf_path, chrome):
    if os.path.exists(pdf_path):
        os.remove(pdf_path)     # a stale file would look like instant success

    chrome_pipe = ChromePipe(chrome, time.monotonic() + CHROME_TIMEOUT_S)
    try:
        target = chrome_pipe.call(
            "Target.createTarget", {"url": "about:blank"})["targetId"]
        session = chrome_pipe.call(
            "Target.attachToTarget",
            {"targetId": target, "flatten": True})["sessionId"]
        chrome_pipe.call("Inspector.enable", session=session)
        # Percent-encode: an --out-dir containing spaces would otherwise
        # truncate the URL and Chrome would print an error page.
        chrome_pipe.call(
            "Page.navigate",
            {"url": "file://" + quote(os.path.abspath(html_path))},
            session=session)

        # Wait until images have loaded and Mermaid has run.
        while not chrome_pipe.call(
                "Runtime.evaluate",
                {"expression": PAGE_READY_JS, "returnByValue": True},
                session=session)["result"].get("value"):
            time.sleep(READY_POLL_S)

        stream = chrome_pipe.call(
            "Page.printToPDF",
            {"printBackground": True, "preferCSSPageSize": True,
             "transferMode": "ReturnAsStream"},
            session=session)["stream"]
        with open(pdf_path, "wb") as fh:
            while True:
                chunk = chrome_pipe.call(
                    "IO.read", {"handle": stream, "size": PDF_CHUNK},
                    session=session)
                data = chunk.get("data", "")
                fh.write(base64.b64decode(data) if chunk.get("base64Encoded")
                         else data.encode("latin-1"))
                if chunk.get("eof"):
                    break
        chrome_pipe.call("IO.close", {"handle": stream}, session=session)
    finally:
        chrome_pipe.close()

    with open(pdf_path, "rb") as fh:
        if fh.read(5) != b"%PDF-":
            raise RenderError(f"Chrome's output is not a PDF: {pdf_path}")


# Cover treatments, both verified against WCAG (see pdf/style.css).
COVER_CLASS = {"azure": "azure", "sea-fresh": "sea"}


def build_space(space, out_dir, version_label, limit=None, keep_html=False,
                no_optimize=False, cover="azure"):
    print(f"[{space}] parsing SUMMARY.md")
    entries = parse_summary(space)
    print(f"[{space}] {len(entries)} pages in navigation order")

    print(f"[{space}] preprocessing")
    markdown, entries = build_markdown(space, entries, limit)

    leaked = count_leaked_markers(markdown)
    if leaked:
        print(f"[{space}] warn: {leaked} unconverted GitBook markers remain",
              file=sys.stderr)

    editor_urls = count_editor_urls(markdown)
    if editor_urls:
        print(f"[{space}] warn: {editor_urls} app.gitbook.com editor URLs "
              f"remain (unmapped space ID?)", file=sys.stderr)

    suffixed_urls = count_suffixed_urls(markdown)
    if suffixed_urls:
        print(f"[{space}] warn: {suffixed_urls} site URLs still end in .md "
              f"(soft-404 on the site)", file=sys.stderr)

    print(f"[{space}] pandoc")
    body_html = run_pandoc(markdown, SPACE_TITLES.get(space, space))
    page = build_html(space, body_html, build_toc_html(entries), entries,
                      version_label, cover)

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
            "leaked_markers": leaked, "editor_urls": editor_urls,
            "suffixed_urls": suffixed_urls}


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
    ap.add_argument("--version-label", default=None,
                    help="cover-page text, e.g. 'Snapshot 2026-07-28'; "
                         "defaults to today's date. Pass '' to omit it.")
    ap.add_argument("--keep-html", action="store_true",
                    help="retain the intermediate HTML for debugging")
    ap.add_argument("--no-optimize", action="store_true",
                    help="skip the qpdf lossless size pass")
    ap.add_argument("--cover", choices=sorted(COVER_CLASS), default="azure",
                    help="cover treatment: Blue Azure with white text "
                         "(default) or Sea Fresh with Deep Ocean text")
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

    # An undated snapshot of continuously-updated documentation is close to
    # useless -- and with an empty default, forgetting the flag dropped the date
    # silently. The workflow resolves it the same way, so a local build and a CI
    # build now label the cover identically. `--version-label ''` still omits it.
    label = args.version_label
    if label is None:
        label = "Snapshot " + datetime.date.today().isoformat()
    print(f"cover label: {label or '(none)'}")

    # One space failing must not discard the others: a full run is tens of
    # minutes, and the CI matrix has fail-fast disabled for the same reason.
    results, failed = [], []
    for space in spaces:
        try:
            results.append(build_space(
                space, args.out_dir, label, args.limit,
                args.keep_html, args.no_optimize, args.cover))
        except RenderError as exc:
            print(f"[{space}] FAILED: {exc}", file=sys.stderr)
            failed.append(space)

    print("\n=== summary ===")
    for r in results:
        print(f"{r['space']:20} {r['doc_pages']:5} docs  "
              f"{str(r['pdf_pages']):>6} pages  {r['size_mb']:6.1f} MB"
              + (f"  ({r['leaked_markers']} leaked)" if r["leaked_markers"] else "")
              + (f"  ({r['editor_urls']} editor URLs)" if r["editor_urls"] else "")
              + (f"  ({r['suffixed_urls']} .md URLs)" if r["suffixed_urls"] else ""))

    if failed:
        print(f"\nFAILED: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
