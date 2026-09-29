#!/usr/bin/env python3
"""railroadcheck.py — fail on a railroad-diagram SVG that is unreadable in dark mode.

DOCS-6637. The `*-railroad.svg` diagrams come from the bottlecaps RR generator (v2.6, default
theme; see dev-docs/railroad-diagrams.md). Its SVG has a transparent background, opaque yellow
boxes, and near-black connector strokes:

    .line       stroke #332900        .bold-line  stroke #141000
    .thin-line  stroke #1F1800        .filled     fill   #332900   (the arrowheads)

On GitBook's light page ground that is fine. On the dark ground the connectors are about 1.2:1,
under the 3:1 WCAG 2.1 SC 1.4.11 needs for non-text contrast, and the boxes appear to float with
nothing joining them. A reader reported exactly that on the CONSTRAINT page. The diagrams are
plain `<img>` references, so page CSS cannot reach inside them. The fix has to be in each file.

The fix is a white card behind the diagram:

    <svg ... width="W+16" height="H+16">
       <defs>...</defs>
       <rect class="plate" width="100%" height="100%" rx="8" style="fill: #FFFFFF; stroke: none"/>
       <g transform="translate(8 8)">
          ...the generator's drawing, unchanged...
       </g>
    </svg>

The fill goes in an inline `style`, not a `fill=` attribute. The generator's own stylesheet has
`rect, circle, polygon {fill: #332900}`, and a CSS rule beats a presentation attribute, so
`fill="#fff"` renders as a dark-brown rectangle. The 8px padding and rounded corners make it read
as a card on a dark page, not a white hole. On the light ground the card is invisible.

What counts as "fixed": the first drawn element after `</defs>` is a `rect.plate` covering 100%
of the canvas, and every connector colour in the file's stylesheet clears 3:1 against the plate's
fill. The colour is not pinned to white, so contrast is the rule.

The generator has no option for a background, so a regenerated diagram loses the card. Run
`--fix` on it after every regeneration. The CI gate (railroadcheck-pr.yml) catches a diagram
committed without it.

Usage:   .claude/hooks/railroadcheck.py <file.svg> [<file.svg> ...]
         .claude/hooks/railroadcheck.py --stdin0          # NUL-delimited paths on stdin
         .claude/hooks/railroadcheck.py --fix <file.svg> ...  # add the card where it is missing
Exit:    0 = every diagram has a passing card (or --fix added it)
         1 = at least one does not
         2 = usage error
Output:  findings on stderr as `path: message`; one summary line on stdout, so a caller can tell
         "nothing to check" apart from "checked and clean". Mirrors mermaidcheck.py.
"""

import re
import sys

PAD = 8
RADIUS = 8
PLATE_FILL = "#FFFFFF"
MIN_RATIO = 3.0

PLATE = (f'<rect class="plate" width="100%" height="100%" rx="{RADIUS}" '
         f'style="fill: {PLATE_FILL}; stroke: none"/>')

SVG_OPEN = re.compile(r'<svg\b[^>]*>')
WIDTH = re.compile(r'\bwidth="(\d+(?:\.\d+)?)"')
HEIGHT = re.compile(r'\bheight="(\d+(?:\.\d+)?)"')
DEFS_END = "</defs>"
FIRST_ELEMENT = re.compile(r'\s*(<[^!?][^>]*>)')
PLATE_TAG = re.compile(r'<rect\b(?=[^>]*\bclass="plate")[^>]*>')
STYLE_FILL = re.compile(r'\bfill:\s*(#[0-9A-Fa-f]{3,6})\b')
HEX = r'#[0-9A-Fa-f]{3,6}'
# The generator's connector rules: stroke on the three line classes, fill on the arrowheads.
CONNECTORS = (
    (".line", re.compile(r'\.line\s*\{[^}]*\bstroke:\s*(' + HEX + r')')),
    (".bold-line", re.compile(r'\.bold-line\s*\{[^}]*\bstroke:\s*(' + HEX + r')')),
    (".thin-line", re.compile(r'\.thin-line\s*\{[^}]*\bstroke:\s*(' + HEX + r')')),
    (".filled", re.compile(r'\.filled\s*\{[^}]*\bfill:\s*(' + HEX + r')')),
)


def luminance(hex_colour):
    h = hex_colour.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    chans = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        chans.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = chans
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def fmt(n):
    return str(int(n)) if float(n).is_integer() else f"{n:g}"


def check(text):
    """Return a list of problems; empty means the diagram passes."""
    if not SVG_OPEN.search(text):
        return ["not an SVG document"]
    end = text.find(DEFS_END)
    if end < 0:
        return ["no </defs>: not the RR generator's layout, check it by hand"]
    m = FIRST_ELEMENT.match(text, end + len(DEFS_END))
    tag = m.group(1) if m else ""
    if not PLATE_TAG.fullmatch(tag):
        return ["no background card: connector lines are ~1.2:1 on GitBook's dark page "
                "(run railroadcheck.py --fix)"]
    problems = []
    if 'width="100%"' not in tag or 'height="100%"' not in tag:
        problems.append('the card does not cover the canvas (needs width="100%" height="100%")')
    fill = STYLE_FILL.search(tag)
    if not fill:
        problems.append("the card has no inline style fill; a fill= attribute loses to the "
                        "generator's `rect {fill: #332900}` rule")
        return problems
    for name, rx in CONNECTORS:
        c = rx.search(text)
        if c and ratio(c.group(1), fill.group(1)) < MIN_RATIO:
            problems.append(f"{name} {c.group(1)} on card {fill.group(1)}: contrast "
                            f"{ratio(c.group(1), fill.group(1)):.2f}:1, needs {MIN_RATIO:g}:1")
    return problems


def fix(text):
    """Add the card. Return the new text, or None when the layout is not one we can fix."""
    svg = SVG_OPEN.search(text)
    end = text.find(DEFS_END)
    close = text.rfind("</svg>")
    if not svg or end < 0 or close < 0:
        return None
    tag = svg.group(0)
    w, h = WIDTH.search(tag), HEIGHT.search(tag)
    if not w or not h:
        return None
    new_tag = WIDTH.sub(f'width="{fmt(float(w.group(1)) + 2 * PAD)}"', tag, count=1)
    new_tag = HEIGHT.sub(f'height="{fmt(float(h.group(1)) + 2 * PAD)}"', new_tag, count=1)
    body_start = end + len(DEFS_END)
    # The drawing is wrapped, not re-indented, so a diagram's diff is four lines, not the file.
    body = text[body_start:close].rstrip("\n")
    return (text[:svg.start()] + new_tag + text[svg.end():body_start]
            + f"\n   {PLATE}\n   <g transform=\"translate({PAD} {PAD})\">"
            + body + "\n   </g>\n" + text[close:])


def main(argv):
    do_fix = False
    args = argv[1:]
    if args and args[0] == "--fix":
        do_fix, args = True, args[1:]
    if args == ["--stdin0"]:
        paths = [p for p in sys.stdin.buffer.read().decode("utf-8").split("\0") if p]
    elif args and not any(a.startswith("--") for a in args):
        paths = args
    else:
        print("usage: railroadcheck.py [--fix] <file.svg> ... | [--fix] --stdin0", file=sys.stderr)
        return 2
    if not paths:
        print("railroadcheck: no SVG files to check")
        return 0

    failing = fixed = 0
    for path in paths:
        try:
            with open(path, encoding="utf-8", newline="") as f:
                text = f.read()
        except OSError as e:
            print(f"{path}: cannot read: {e.strerror}", file=sys.stderr)
            failing += 1
            continue
        problems = check(text)
        if problems and do_fix and problems[0].startswith("no background card"):
            new = fix(text)
            if new is not None and not check(new):
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(new)
                fixed += 1
                continue
        for p in problems:
            print(f"{path}: {p}", file=sys.stderr)
        failing += bool(problems)

    summary = f"railroadcheck: {len(paths)} diagram(s); {failing} failing"
    if do_fix:
        summary += f"; fixed {fixed} file(s)"
    print(summary)
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
