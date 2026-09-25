#!/usr/bin/env python3
"""mermaidcheck.py — fail on a Mermaid flowchart whose edge labels miss WCAG AA contrast.

DOCS-6630. GitBook renders Mermaid with its stock themes, and in the DARK theme a flowchart edge
label (`A -->|Yes| B`, `A -- No --> B`) is `#ccc` text on a `#585858` pill: 4.43:1, under the
4.5:1 WCAG AA needs for ~12px text. Light mode is fine (10.31:1). There is no site-level custom
CSS on our GitBook plan to fix it once, and `classDef` cannot reach it — the label is not a
descendant of a classed node — so the fix has to live in each diagram:

    %%{init: {"themeVariables": {"edgeLabelBackground": "#eef2ff"}}}%%      <- first line
    ...
    linkStyle default color:#111111                                          <- last line

Both halves are needed, and the one-line variant first proposed on DOCS-6630 (the directive
with `"tertiaryTextColor": "#111111"`) is WRONG: rendered with mermaid 11.14.0, the version
GitBook loads, `tertiaryTextColor` does not reach edge-label text, so it leaves the `#ccc`
glyphs on the new near-white pill — 1.44:1, far worse than doing nothing. The pill colour must be
set by the directive (a theme variable; no diagram syntax reaches it), and the text colour by
`linkStyle default`, which mermaid applies to every edge's label as an inline style and which
still applies alongside numbered `linkStyle N stroke:…` lines. Measured in headless Chrome
against mermaid 11.14.0: 16.89:1 in both themes, with subgraph titles and unclassed node labels
unchanged.

What counts as "has an edge label": a `flowchart`/`graph` block with at least one link carrying
text in either form — pipe (`-->|x|`, `---|x|`, `-.->|x|`, `==>|x|`) or inline (`-- x -->`,
`== x ==>`, `-. x .->`). Node text (`[...]`, `(...)`, `{...}`, quoted strings), `%%` lines,
`accTitle`/`accDescr` and style statements are blanked first, so a `--` or `|` inside a label or a
description is not mistaken for a link. Flowcharts with no edge labels need nothing: they render
no pill.

What counts as "fixed": an init directive setting `themeVariables.edgeLabelBackground`, a
`linkStyle default` line setting `color`, and the two hex colours at >= 4.5:1. The colours are
not pinned to the house values, so a diagram may choose its own — the contrast is the rule.

Usage:   .claude/hooks/mermaidcheck.py <file> [<file> ...]
         .claude/hooks/mermaidcheck.py --stdin0          # NUL-delimited paths on stdin
         .claude/hooks/mermaidcheck.py --fix <file> ...  # add the house fix where it is missing
Exit:    0 = every edge-labelled flowchart carries a passing fix (or --fix changed what it could)
         1 = at least one does not
         2 = usage error
Output:  findings on stderr as `path:line: message`; one summary line on stdout, so a caller can
         tell "nothing to check" apart from "checked and clean". Mirrors includecheck.sh.
"""

import json
import re
import sys

DIRECTIVE = '%%{init: {"themeVariables": {"edgeLabelBackground": "#eef2ff"}}}%%'
LINKSTYLE = "linkStyle default color:#111111"
MIN_RATIO = 4.5

# `.claude/` and `dev-docs/` document the convention itself, with deliberately partial examples.
EXEMPT = (".claude/", "dev-docs/")

FENCE_OPEN = re.compile(r"^([ \t]*)(`{3,}|~{3,})[ \t]*mermaid\b")
TYPE_LINE = re.compile(r"^\s*(flowchart|graph)\b")
STYLE_STMT = re.compile(r"^\s*(classDef|class|style|linkStyle|click|accTitle|direction)\b")

# Pipe form: a link operator, optional arrowhead, then |text|.
PIPE_LABEL = re.compile(r"(?:<?[-=.]{2,}[>ox]?)\s*\|[^|\n]*\S[^|\n]*\|")
# Inline form: an opening `--`/`==`/`-.` that is not part of a longer operator, whitespace, text,
# then a closing operator. The look-behind keeps the middle of `---` from opening a label, and
# the required whitespace keeps `-->` and `-.->` out. A leading `<` (`<== x ==>`) is allowed.
INLINE_LABEL = re.compile(
    r"(?<![-=.])(?:--|==|-\.)\s+\S[^\n]*?\s*(?:-->|---|==>|===|\.->|\.-|--[ox]|==[ox])"
)


def blank_node_text(line):
    """Replace quoted strings and bracketed node text with placeholders, innermost first."""
    line = re.sub(r'"[^"\n]*"', '"x"', line)
    for pat in (r"\[[^\[\]\n]*\]", r"\([^()\n]*\)", r"\{[^{}\n]*\}"):
        prev = None
        while prev != line:
            prev, line = line, re.sub(pat, "[x]", line)
    # Asymmetric node `A>text]`: the `>` directly follows the node id. Anchoring on that keeps
    # the rule off an arrowhead, where `-->|label| B[x]` would otherwise lose its label.
    return re.sub(r"(?<=\w)>[^\]\n]*\]", "[x]", line)


def luminance(hexcolor):
    h = hexcolor.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    chans = []
    for i in (0, 2, 4):
        v = int(h[i:i + 2], 16) / 255
        chans.append(v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4)
    return 0.2126 * chans[0] + 0.7152 * chans[1] + 0.0722 * chans[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


HEX = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def blocks(lines):
    """Yield (start, end) line indexes of each mermaid block body (exclusive of the fences)."""
    i = 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        if not m:
            i += 1
            continue
        fence = m.group(2)
        j = i + 1
        while j < len(lines) and not re.match(r"^[ \t]*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", lines[j]):
            j += 1
        yield i + 1, j
        i = j + 1


def analyse(body):
    """Return a dict describing one block body, or None if it is not a flowchart."""
    idx = 0
    # Optional YAML frontmatter, then blank lines and %% lines, then the diagram type.
    k = 0
    while k < len(body) and not body[k].strip():
        k += 1
    front_end = None
    if k < len(body) and body[k].strip() == "---":
        for q in range(k + 1, len(body)):
            if body[q].strip() == "---":
                front_end = q
                break
        k = (front_end + 1) if front_end is not None else len(body)
    type_idx = None
    for q in range(k, len(body)):
        s = body[q].strip()
        if not s or s.startswith("%%"):
            continue
        type_idx = q
        break
    if type_idx is None or not TYPE_LINE.match(body[type_idx]):
        return None

    info = {"front_end": front_end, "type_idx": type_idx, "labelled": False,
            "bg": None, "fg": None, "init_idx": None, "problems": []}
    in_descr = False
    for q, raw in enumerate(body):
        s = raw.strip()
        if s.startswith("%%{"):
            m = re.match(r"%%\{\s*init(?:ialize)?\s*:\s*(.*)\}\s*%%\s*$", s)
            if m:
                info["init_idx"] = q
                try:
                    cfg = json.loads(m.group(1).replace("'", '"'))
                    bg = (cfg.get("themeVariables") or {}).get("edgeLabelBackground")
                    if bg:
                        info["bg"] = bg
                except (ValueError, AttributeError):
                    info["problems"].append((q, "init directive is not parseable JSON"))
            continue
        if q <= type_idx or s.startswith("%%"):
            continue
        if in_descr:
            if "}" in s:
                in_descr = False
            continue
        if re.match(r"accDescr\s*\{", s):
            in_descr = "}" not in s.split("{", 1)[1]
            continue
        lm = re.match(r"linkStyle\s+default\s+(.*)$", s)
        if lm:
            cm = re.search(r"(?:^|[,;\s])color\s*:\s*([^,;\s]+)", lm.group(1))
            if cm:
                info["fg"] = cm.group(1)
            continue
        if STYLE_STMT.match(s) or re.match(r"accDescr\s*:", s):
            continue
        flat = blank_node_text(s)
        if PIPE_LABEL.search(flat) or INLINE_LABEL.search(flat):
            info["labelled"] = True
    return info


def verdict(info):
    """Return a list of problem strings for a labelled flowchart ([] = passes)."""
    out = [p for _, p in info["problems"]]
    bg, fg = info["bg"], info["fg"]
    if not bg:
        out.append("no init directive setting themeVariables.edgeLabelBackground")
    if not fg:
        out.append("no `linkStyle default color:...` line")
    if bg and fg:
        if not (HEX.match(bg) and HEX.match(fg)):
            out.append(f"edge-label colours must be hex to be checked (got {bg} / {fg})")
        elif contrast(bg, fg) < MIN_RATIO:
            out.append(f"edge-label contrast {contrast(bg, fg):.2f}:1 is under {MIN_RATIO}:1")
    return out


def indent_of(body, type_idx):
    counts = {}
    for s in body[type_idx + 1:]:
        if s.strip():
            ind = s[: len(s) - len(s.lstrip())]
            counts[ind] = counts.get(ind, 0) + 1
    return min(counts, key=lambda k: (len(k), -counts[k])) if counts else "    "


def process(path, fix):
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"{path}: cannot read: {e}", file=sys.stderr)
        return 0, 0, 1, False
    lines = text.split("\n")
    checked = failed = 0
    edits = []  # (insert_at, line) in file coordinates, applied bottom-up
    for start, end in blocks(lines):
        body = lines[start:end]
        info = analyse(body)
        if not info or not info["labelled"]:
            continue
        checked += 1
        problems = verdict(info)
        if not problems:
            continue
        if fix and not info["bg"] and not info["fg"] and not info["problems"] and info["init_idx"] is None:
            at = start + (info["front_end"] + 1 if info["front_end"] is not None else 0)
            edits.append((end, indent_of(body, info["type_idx"]) + LINKSTYLE))
            edits.append((at, DIRECTIVE))
            continue
        failed += 1
        for p in problems:
            print(f"{path}:{start + info['type_idx'] + 1}: edge-labelled flowchart: {p}", file=sys.stderr)
        if fix:
            print(f"{path}:{start + info['type_idx'] + 1}: not auto-fixed (it already has a partial "
                  f"fix or its own init directive) — merge the house values by hand", file=sys.stderr)
    if edits:
        for at, line in sorted(edits, key=lambda e: e[0], reverse=True):
            lines.insert(at, line)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    return checked, failed, 0, bool(edits)


def main(argv):
    fix = False
    args = argv[1:]
    if args and args[0] == "--fix":
        fix, args = True, args[1:]
    if not args:
        print(f"usage: {argv[0]} [--fix] <file> [<file> ...] | --stdin0", file=sys.stderr)
        return 2
    if args[0] == "--stdin0":
        if len(args) != 1:
            print(f"usage: {argv[0]} --stdin0   (reads NUL-delimited paths on stdin; takes no other arguments)",
                  file=sys.stderr)
            return 2
        paths = [p for p in sys.stdin.buffer.read().decode("utf-8").split("\0") if p]
    else:
        paths = args
    paths = [p for p in paths if p.endswith(".md") and not p.startswith(EXEMPT)]
    if not paths:
        print("mermaidcheck: no Markdown files to check")
        return 0
    checked = failed = errors = changed = 0
    for p in paths:
        c, f, e, ch = process(p, fix)
        checked, failed, errors, changed = checked + c, failed + f, errors + e, changed + ch
    print(f"mermaidcheck: {checked} edge-labelled flowchart(s) in {len(paths)} file(s); "
          f"{failed} failing" + (f"; fixed {changed} file(s)" if fix else ""))
    return 1 if (failed or errors) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
