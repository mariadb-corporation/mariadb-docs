#!/usr/bin/env python3
"""new-findings.py — print the doc-lint findings in AFTER that BEFORE did not already contain.

Used by gitbook-edit-digest.sh (DOCS-6914) to tell what a GitBook commit introduced apart from
what was already failing on its parent. See the comment above the parent run in that script for
why the raw gate output cannot be reported as-is.

    new-findings.py <before.log> <after.log>

doc-lint.sh output is a sequence of BLOCKS: a line starting in column 0, plus any indented lines
that follow it (versioncheck and the register audits wrap their explanations that way). A block
that is a single line ending in ':' is a HEADER ("lychee found broken links:", "[path]:"); it is
never a finding itself, but is printed once in front of the first new finding under it so the
excerpt still says which gate and which file.

Blocks are compared after normalization, because an edit moves line numbers: a dead link at
"(at 84:33)" in the parent is the same dead link at "(at 86:33)" after two lines were added
above it. A changed line number alone is therefore NOT a new finding. Output is the original,
unnormalized text. Standard library only.
"""

import re
import sys
from collections import Counter

# Per-run noise: lychee's summary and preamble change on every run and say nothing about a page.
NOISE = re.compile(r"^(🔍|Issues found in \d+ input|Find details below|Hint: )")

# A block that opens with a gate's own name ("fragcheck: 1 heading anchor(s)...", "doc-lint:
# retired ...", "versioncheck: ...") starts a new gate even when it is not a header, so the
# headers of the gate before it no longer apply. Without this, a new fragcheck finding printed
# lychee's "[file]:" header above it with no lychee finding under it (seen on the DOCS-6914
# acceptance run). Lychee entries open with "[" and codespell entries with a path, so neither
# matches.
GATE_START = re.compile(r"^[A-Za-z][\w-]*: ")

NORMALIZE = [
    (re.compile(r"\(at \d+:\d+\)"), "(at N)"),     # lychee positions
    (re.compile(r":\d+:"), ":N:"),                 # codespell / grep-style path:line:
    (re.compile(r"\bline \d+\b"), "line N"),       # register audits, includecheck
    (re.compile(r"\s+"), " "),
]


def blocks(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    out, cur = [], None
    for line in lines:
        if not line.strip():
            continue
        if line[0].isspace() and cur is not None:
            cur.append(line)
            continue
        cur = [line]
        out.append(cur)
    return [b for b in out if not NOISE.match(b[0])]


def key(block):
    text = "\n".join(block)
    for pattern, repl in NORMALIZE:
        text = pattern.sub(repl, text)
    return text.strip()


def is_header(block):
    return len(block) == 1 and block[0].rstrip().endswith(":")


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip().splitlines()[0], file=sys.stderr)
        return 2
    seen = Counter(key(b) for b in blocks(argv[1]) if not is_header(b))
    pending, printed = [], set()
    for b in blocks(argv[2]):
        if is_header(b):
            # A file header resets under its gate header; a gate header resets everything.
            if b[0].startswith("["):
                pending = [h for h in pending if not h[0].startswith("[")]
            else:
                pending = []
            pending.append(b)
            continue
        if GATE_START.match(b[0]):
            pending = []
        k = key(b)
        if seen[k] > 0:
            seen[k] -= 1        # a multiset: two identical findings before, three after = one new
            continue
        for h in pending:
            if id(h) not in printed:
                print(h[0])
                printed.add(id(h))
        print("\n".join(b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
