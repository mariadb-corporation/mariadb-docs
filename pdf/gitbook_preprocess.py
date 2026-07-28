"""Convert GitBook-flavored Markdown into plain Markdown suitable for PDF.

GitBook custom blocks (`{% hint %}`, `{% tabs %}`, `{% columns %}`, ...) are
invisible to Pandoc and leak into the output as literal body text, so every one
of them has to be rewritten or dropped before conversion. This module owns that
rewriting; `build.py` owns page ordering and the PDF pipeline.

Two properties drive the design:

* Blocks routinely **span code fences** -- a `{% stepper %}` opens, several
  fenced shell samples follow, then `{% endstepper %}` closes. Matching an
  open/close pair with one regex therefore fails on real pages, so block
  conversion is a single line-oriented pass that carries fence state.
* Markers are **not always alone on a line** (`{% hint style="info" %} For the
  CTE...` occurs verbatim in the corpus), so replacements inject their own line
  breaks rather than assuming they own the line.

The full tag inventory is in `pdf/README.md`.
"""

import html as _html
import os
import re
import sys
from urllib.parse import quote, unquote

# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.DOTALL)


def split_frontmatter(text):
    """Return (frontmatter_dict, body). Only scalar keys are parsed."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            meta[km.group(1)] = km.group(2).strip().strip("'\"")
    return meta, text[m.end():]


# ---------------------------------------------------------------------------
# Fence tracking
#
# Every transform must leave fenced code untouched: a `{% hint %}` inside a
# GitBook-syntax example is content, not markup.
# ---------------------------------------------------------------------------

FENCE_RE = re.compile(r"^(\s{0,3})(`{3,}|~{3,})(.*)$")


def iter_lines(text):
    """Yield (line_without_newline, in_code) for every line of `text`.

    `in_code` is True for the fence delimiters themselves as well as their
    contents, so callers can pass those lines through verbatim.
    """
    fence = None  # (marker_char, marker_len)
    for line in text.split("\n"):
        m = FENCE_RE.match(line)
        if fence is None:
            if m:
                fence = (m.group(2)[0], len(m.group(2)))
                yield line, True
            else:
                yield line, False
        else:
            yield line, True
            if m and m.group(2)[0] == fence[0] and len(m.group(2)) >= fence[1] \
                    and not m.group(3).strip():
                fence = None


def map_prose_lines(text, fn):
    """Rewrite non-code lines with `fn`; `fn` may return multi-line text."""
    out = []
    for line, in_code in iter_lines(text):
        out.append(line if in_code else fn(line))
    return "\n".join(out)


def prose_only(fn):
    """Apply `fn` to each run of prose, leaving fenced code verbatim.

    Suitable only for transforms that are line-local; anything that pairs an
    opening and closing marker must use the block pass instead.
    """
    def wrapped(text, *a, **kw):
        return map_prose_lines(text, lambda line: fn(line, *a, **kw))
    return wrapped


# ---------------------------------------------------------------------------
# Marker patterns
# ---------------------------------------------------------------------------

HINT_OPEN = re.compile(r"\{%\s*hint\s+style=[\"'](\w+)[\"']\s*%\}")
HINT_CLOSE = re.compile(r"\{%\s*endhint\s*%\}")
TABS_OPEN = re.compile(r"\{%\s*tabs\s*%\}")
TABS_CLOSE = re.compile(r"\{%\s*endtabs\s*%\}")
TAB_OPEN = re.compile(r"\{%\s*tab\s+title=[\"'](.*?)[\"']\s*%\}")
TAB_CLOSE = re.compile(r"\{%\s*endtab\s*%\}")
STEPPER_OPEN = re.compile(r"\{%\s*stepper\s*%\}")
STEPPER_CLOSE = re.compile(r"\{%\s*endstepper\s*%\}")
STEP_OPEN = re.compile(r"\{%\s*step\s*%\}")
STEP_CLOSE = re.compile(r"\{%\s*endstep\s*%\}")
COLUMN_ANY = re.compile(r"\{%\s*(?:end)?columns?\s*%\}")
CODE_OPEN = re.compile(r"\{%\s*code\b([^%]*)%\}")
CODE_CLOSE = re.compile(r"\{%\s*endcode\s*%\}")
TITLE_ATTR = re.compile(r"title=[\"'](.*?)[\"']")
CREF_OPEN = re.compile(r"\{%\s*content-ref\s+url=[\"'](.*?)[\"'][^%]*%\}")
CREF_CLOSE = re.compile(r"\{%\s*endcontent-ref\s*%\}")
EMBED_OPEN = re.compile(r"\{%\s*embed\s+url=[\"'](.*?)[\"'][^%]*%\}")
FILE_OPEN = re.compile(r"\{%\s*file\s+src=[\"'](.*?)[\"'][^%]*%\}")
MD_LINK_INLINE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")

# ~9,000 marketing form embeds and other integration blocks: no PDF meaning.
INTEGRATION = re.compile(r"\{%\s*@[\w/.@-]+[^%]*%\}")
# Conditionals, OpenAPI and "updates" wrappers: keep any body, drop the wrapper.
WRAPPER_ONLY = re.compile(
    r"\{%\s*(?:end)?(?:if|openapi|updates|update|embed|file)\b[^%]*%\}")
# Backstop for anything the specific rules above did not catch.
ANY_MARKER = re.compile(r"\{%[^%]*%\}")

HINT_LABEL = {
    "info": "Note",
    "success": "Tip",
    "warning": "Warning",
    "danger": "Important",
}


def _esc_inline(s):
    """Make an attribute value safe to drop into Markdown prose."""
    return _html.escape(s.strip(), quote=False)


# ---------------------------------------------------------------------------
# Block conversion (single fence-aware pass)
# ---------------------------------------------------------------------------

# A few pages escape the braces (`\{% tabs %\}`), which stops GitBook rendering
# the block at all -- those pages are broken on the live site too. Normalizing
# here keeps the PDF clean; the source still wants fixing.
ESCAPED_MARKER = re.compile(r"\\(\{%)|(%)\\(\})")


def unescape_markers(text):
    return map_prose_lines(
        text, lambda ln: ESCAPED_MARKER.sub(
            lambda m: m.group(1) or (m.group(2) + m.group(3)), ln))


def convert_blocks(text):
    """Rewrite every GitBook block marker into Pandoc fenced divs.

    Runs as one pass because blocks nest and span code fences; a stack tracks
    step numbering and a small state flag handles the multi-line
    `{% content-ref %}` body.
    """
    text = unescape_markers(text)
    out = []
    step_counters = []       # one counter per open {% stepper %}
    cref = None              # (url, [buffered lines]) while inside content-ref
    depth = [0]              # open fenced divs, so the page can be balanced

    def open_div(classes):
        depth[0] += 1
        return f"\n::: {{{classes}}}\n"

    def close_div():
        # A stray close (unbalanced source) would otherwise emit a bare ':::'
        # that Pandoc prints literally.
        if depth[0] == 0:
            return ""
        depth[0] -= 1
        return "\n:::\n"

    for line, in_code in iter_lines(text):
        if in_code:
            if cref is not None:
                cref[1].append(line)
            else:
                out.append(line)
            continue

        # --- content-ref: consume until the closing marker ----------------
        if cref is not None:
            if CREF_CLOSE.search(line):
                url, body = cref[0], "\n".join(cref[1])
                inner = MD_LINK_INLINE.search(body)
                label = inner.group(1) if inner else \
                    (url.rstrip("/").split("/")[-1] or url)
                out.append(f"\nSee [{_esc_inline(label)}]({url}).\n")
                cref = None
            else:
                cref[1].append(line)
            continue

        m = CREF_OPEN.search(line)
        if m:
            before = line[:m.start()].rstrip()
            if before:
                out.append(before)
            cref = (m.group(1), [line[m.end():]])
            continue

        # --- integration blocks and bare wrappers -------------------------
        line = INTEGRATION.sub("", line)

        # --- code fences with GitBook attributes --------------------------
        def code_open_sub(mm):
            tm = TITLE_ATTR.search(mm.group(1))
            return f"\n**`{_esc_inline(tm.group(1))}`**\n" if tm else ""

        line = CODE_OPEN.sub(code_open_sub, line)
        line = CODE_CLOSE.sub("", line)

        # --- hints --------------------------------------------------------
        def hint_open_sub(mm):
            style = mm.group(1).lower()
            label = HINT_LABEL.get(style, "Note")
            return open_div(f".hint .hint-{style}") + f"**{label}:**\n"

        line = HINT_OPEN.sub(hint_open_sub, line)
        line = HINT_CLOSE.sub(lambda mm: close_div(), line)

        # --- tabs ---------------------------------------------------------
        line = TABS_OPEN.sub(lambda mm: open_div(".tabs"), line)
        line = TABS_CLOSE.sub(lambda mm: close_div(), line)
        line = TAB_OPEN.sub(
            lambda mm: open_div(".tab") + f"**{_esc_inline(mm.group(1))}**\n",
            line)
        line = TAB_CLOSE.sub(lambda mm: close_div(), line)

        # --- stepper ------------------------------------------------------
        def stepper_open_sub(mm):
            step_counters.append(0)
            return open_div(".stepper")

        def stepper_close_sub(mm):
            if step_counters:
                step_counters.pop()
            return close_div()

        def step_open_sub(mm):
            # Steps outside a stepper occur in the corpus; number them anyway.
            if not step_counters:
                step_counters.append(0)
            step_counters[-1] += 1
            return open_div(".step") + f"**Step {step_counters[-1]}**\n"

        line = STEPPER_OPEN.sub(stepper_open_sub, line)
        line = STEPPER_CLOSE.sub(stepper_close_sub, line)
        line = STEP_OPEN.sub(step_open_sub, line)
        line = STEP_CLOSE.sub(lambda mm: close_div(), line)

        # --- columns: a PDF page is one column ----------------------------
        line = COLUMN_ANY.sub("", line)

        # --- media --------------------------------------------------------
        line = EMBED_OPEN.sub(lambda mm: f"\n<{mm.group(1)}>\n", line)
        line = FILE_OPEN.sub(lambda mm: f"\nFile: `{mm.group(1)}`\n", line)
        line = WRAPPER_ONLY.sub("", line)

        # --- anything left ------------------------------------------------
        line = ANY_MARKER.sub("", line)

        out.append(line)

    # An unbalanced open would swallow the rest of the page; close it instead.
    if cref is not None:
        out.append(f"\nSee <{cref[0]}>.\n")

    # Pages with an unbalanced block marker exist in the corpus. Left open, the
    # div runs to the end of the *concatenated* document and drags every later
    # page inside it, so close whatever this page left open.
    if depth[0]:
        out.append("\n" + "\n:::\n" * depth[0])

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Includes
# ---------------------------------------------------------------------------

INCLUDE_RE = re.compile(r"\{%\s*include\s+[\"'](.*?)[\"']\s*%\}")

# Boilerplate repeated on thousands of pages; inlining it per page would add
# hundreds of pages of noise.
BOILERPLATE = ("contributing-content", "license-cc-by-sa-gnu-fdl", "announce")


def resolve_includes(text, page_path, depth=0):
    """Inline local include files; drop remote and boilerplate ones.

    3,269 includes point at `app.gitbook.com/.../~/reusable/`, whose content
    lives only in GitBook and is unreachable from a source checkout.
    """
    if depth > 3:
        return map_prose_lines(text, lambda ln: INCLUDE_RE.sub("", ln))

    def sub_line(line):
        def sub(m):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                return ""
            if any(b in target for b in BOILERPLATE):
                return ""
            resolved = os.path.normpath(
                os.path.join(os.path.dirname(page_path), target))
            if not os.path.isfile(resolved):
                return ""
            try:
                with open(resolved, encoding="utf-8") as fh:
                    inner = fh.read()
            except OSError:
                return ""
            _, inner = split_frontmatter(inner)
            inner = resolve_includes(inner, resolved, depth + 1).strip()
            return "\n" + inner + "\n" if inner else ""
        return INCLUDE_RE.sub(sub, line)

    return map_prose_lines(text, sub_line)


# ---------------------------------------------------------------------------
# Alias placeholders -> public URLs
# ---------------------------------------------------------------------------

ALIAS_URLS = {
    "server": "https://mariadb.com/docs/server",
    "galera": "https://mariadb.com/docs/galera-cluster",
    "maxscale": "https://mariadb.com/docs/maxscale",
    "columnstore": "https://mariadb.com/docs/columnstore",
    "connectors": "https://mariadb.com/docs/connectors",
    "tools": "https://mariadb.com/docs/tools",
    "platform": "https://mariadb.com/docs/platform",
    "release-notes": "https://mariadb.com/docs/release-notes",
    "general-resources": "https://mariadb.com/docs/general-resources",
    "mariadb-cloud": "https://mariadb.com/docs/mariadb-cloud",
    "skysql": "https://mariadb.com/docs/mariadb-cloud",
}

# Only match inside a link target, so prose braces are left alone.
ALIAS_RE = re.compile(r"\{(" + "|".join(map(re.escape, ALIAS_URLS)) + r")\}")


@prose_only
def expand_aliases(line):
    return ALIAS_RE.sub(lambda m: ALIAS_URLS[m.group(1)], line)


# ---------------------------------------------------------------------------
# Mermaid -> tagged block for client-side rendering
# ---------------------------------------------------------------------------

MERMAID_RE = re.compile(r"^[ \t]*```mermaid[ \t]*\n(.*?)^[ \t]*```[ \t]*$",
                        re.DOTALL | re.MULTILINE)


def convert_mermaid(text):
    """Hand diagram source to the browser, which renders it before printing."""
    return MERMAID_RE.sub(
        lambda m: '\n<pre class="mermaid">'
                  + _html.escape(m.group(1).rstrip()) + "</pre>\n",
        text)


# ---------------------------------------------------------------------------
# Footnotes
# ---------------------------------------------------------------------------

FOOTNOTE_LABEL = re.compile(r"\[\^([^\]\s]+)\]")


def namespace_footnotes(text, page_key):
    """Prefix footnote labels with a per-page key.

    Nearly every page numbers its footnotes from 1, so concatenating a space
    collides them: Pandoc then reports duplicate references and unused
    definitions, and readers get another page's footnote text.
    """
    return map_prose_lines(
        text, lambda ln: FOOTNOTE_LABEL.sub(rf"[^{page_key}-\1]", ln))


# ---------------------------------------------------------------------------
# Heading demotion
# ---------------------------------------------------------------------------

ATX_RE = re.compile(r"^(#{1,6})(\s+)(.*)$")


@prose_only
def demote_headings(line, offset):
    """Shift a page's headings to nest under its position in the TOC.

    Levels clamp at 6; `server/` nests 8 deep, so the deepest pages flatten
    rather than emit invalid HTML.
    """
    if offset <= 0:
        return line
    m = ATX_RE.match(line)
    if not m:
        return line
    return "#" * min(len(m.group(1)) + offset, 6) + m.group(2) + m.group(3)


# ---------------------------------------------------------------------------
# Link and asset rewriting
# ---------------------------------------------------------------------------

MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(<?([^)>\s]+?)>?(?:\s+\"[^\"]*\")?\)")
IMG_LINK_RE = re.compile(r"!\[([^\]]*)\]\(<?([^)>\s]+?)>?(?:\s+\"[^\"]*\")?\)")
HTML_HREF_RE = re.compile(r'href="([^"]+)"')
HTML_SRC_RE = re.compile(r'src="([^"]+)"')
ABSOLUTE = ("http://", "https://", "mailto:", "data:", "#", "tel:")


def rewrite_links(text, page_path, space_dir, anchors, web_base):
    """Point in-space links at PDF anchors, out-of-space links at the website.

    Without this, concatenating pages leaves every `.md` link dead -- the
    failure mode flagged on the ticket. Images are made absolute `file://` URLs
    so Chrome can load them from the checkout.
    """
    page_dir = os.path.dirname(page_path)

    def anchor_target(url):
        if url.startswith(ABSOLUTE):
            return None
        raw, _, _frag = url.partition("#")
        if not raw:
            return None
        rel = os.path.relpath(
            os.path.normpath(os.path.join(page_dir, raw)), space_dir)
        rel = rel.replace(os.sep, "/")
        # A directory-style link resolves to that directory's README.
        for cand in (rel, f"{rel}/README.md", f"{rel}.md"):
            if cand in anchors:
                return "#" + anchors[cand]
        if rel.startswith(".."):
            # Another space: send the reader to the published site.
            return web_base.rstrip("/") + "/" + rel.lstrip("./")
        return None

    def asset_target(url):
        if url.startswith(("http://", "https://", "data:", "file://")):
            return None
        # Asset links are percent-encoded in the source (`15%20(1).PNG`), but
        # the filesystem holds the decoded name, so decode before the check.
        raw = unquote(url.split("#")[0])
        resolved = os.path.normpath(os.path.join(page_dir, raw))
        if not os.path.isfile(resolved):
            return None
        return "file://" + quote(os.path.abspath(resolved))

    def fix_line(line):
        def img_sub(m):
            new = asset_target(m.group(2))
            return f"![{m.group(1)}]({new})" if new else m.group(0)

        def src_sub(m):
            new = asset_target(m.group(1))
            return f'src="{new}"' if new else m.group(0)

        def md_sub(m):
            new = anchor_target(m.group(2))
            return f"[{m.group(1)}]({new})" if new else m.group(0)

        def href_sub(m):
            new = anchor_target(m.group(1))
            return f'href="{new}"' if new else m.group(0)

        line = IMG_LINK_RE.sub(img_sub, line)
        line = HTML_SRC_RE.sub(src_sub, line)
        line = MD_LINK_RE.sub(md_sub, line)
        line = HTML_HREF_RE.sub(href_sub, line)
        return line

    return map_prose_lines(text, fix_line)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def _first_heading_matches(body, title):
    m = re.search(r"^#{1,6}\s+(.*)$", body.lstrip()[:400], re.MULTILINE)
    if not m:
        return False
    norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())
    return norm(m.group(1)) == norm(title)


def preprocess(text, *, page_path, space_dir, anchors, heading_offset,
               web_base, anchor_id, title):
    """Turn one GitBook page into PDF-ready Markdown."""
    _, body = split_frontmatter(text)

    body = resolve_includes(body, page_path)
    body = convert_blocks(body)
    body = namespace_footnotes(body, anchor_id)
    body = expand_aliases(body)
    body = convert_mermaid(body)
    body = rewrite_links(body, page_path, space_dir, anchors, web_base)

    # Drop the page's own leading H1 when it merely repeats the TOC title,
    # before demotion so the comparison sees the original level.
    if _first_heading_matches(body, title):
        body = re.sub(r"\A\s*#{1,6}[ \t]+.*?(?:\r?\n|\Z)", "", body, count=1)

    body = demote_headings(body, heading_offset)

    # Give every page a heading at its TOC depth so the PDF outline mirrors
    # SUMMARY.md even when the page's own H1 is missing or differs.
    level = min(heading_offset + 1, 6)
    heading = f'{"#" * level} {title} {{#{anchor_id}}}\n\n'

    # Collapse the blank-line runs the div injection leaves behind.
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return heading + body + "\n"


if __name__ == "__main__":
    # Smoke-test one page: python3 gitbook_preprocess.py <file.md>
    path = sys.argv[1]
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    print(preprocess(
        src, page_path=path, space_dir=os.path.dirname(path) or ".",
        anchors={}, heading_offset=0, web_base="https://mariadb.com/docs",
        anchor_id="smoke", title="Smoke Test"))
