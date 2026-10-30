#!/usr/bin/env python3
"""timeless.py — high-precision finder for undated product claims (DOCS-6640).

WHY THIS EXISTS
    DOCS-6639: "The Docker images are currently beta maturity, so they are not
    currently recommended for production." Nobody knew when "currently" was
    written, so a customer read it as true today. The rule against this is in
    dev-docs/style-guide.md ("Timeless wording"); this is the check for it.

WHY IT IS NOT A BLANKET GREP
    "currently" is usually RIGHT: "the currently connected clients", "the
    statement currently executing" describe runtime state. The DOCS-6640 passes
    read ~1,000 hits by hand and kept most of them. A gate that fires on every
    "currently connected" gets switched off within a week, so PATTERNS below
    only match the shapes that were wrong in that campaign: maturity and support
    status, promises of future support, and sentence-level "as of now" framing.
    Precision over recall -- a miss is caught at review; a false alarm teaches
    people to ignore the digest.

WHAT IT DOES NOT DECIDE
    A hit is a question, not a verdict. "Version 2.0 is currently a Release
    Candidate" is TRUE today; the fix is to anchor it ("As of 2.0.0rc2, ..."),
    not to delete the word. Verify every hit against source before rewording.

USAGE
    timeless.py check [PATH ...]   every hit under PATH (default: the repo)
    timeless.py new REV            hits present now but not at REV (the digest)

    Exit status: 0 no hits, 1 hits reported, 2 usage error.

    `new` compares (file, normalized line text) sets between REV and the working
    tree, so a hit that merely moved is not reported again. A hit on a line that
    was edited for another reason IS reported: the text changed, and whoever
    touched the line is best placed to fix it (its first run found exactly that
    -- a second "currently" left on a line DOCS-6640 had already edited). Only
    changed .md files are read at REV.
"""
import re
import subprocess
import sys
import pathlib

# Published trees where these words are correct by construction.
SKIP = (
    'release-notes/',            # a release note IS the date stamp
    'maxscale/maxscale-old-versions/',   # archived, frozen
    'general-resources/community/contributing-participating/google-summers-of-code/',  # year-stamped
    'server/reference/error-codes/',     # literal server message text
    # Not GitBook spaces (same list as fragcheck.py UNPUBLISHED).
    'agent-skills/', 'help-tables/', 'dev-docs/', 'dist/', 'pdf/',
    '.claude/', '.github/', '.git/',
)

ADV = r'(?:currently|at the moment|for now|at this time|at present|presently)'
MATURITY = (r'(?:beta|alpha|gamma|release candidate|rc|experimental|incubation|'
            r'(?:tech(?:nical)?\s+)?preview)')

# (label, compiled regex). Each shape was wrong at least once in DOCS-6640.
PATTERNS = [
    ('maturity', re.compile(
        rf'\b(?:is|are)\s+{ADV}\s+(?:an?\s+|in\s+)?{MATURITY}\b', re.I)),
    ('maturity', re.compile(
        rf'\b{ADV}\s+(?:available\s+as\s+(?:an?\s+)?)?{MATURITY}\b', re.I)),
    ('support', re.compile(
        rf'\b(?:not\s+{ADV}|{ADV}\s+not)\s+(?:supported|available|implemented|possible)\b', re.I)),
    ('support', re.compile(
        # "supports", not "available": "currently available backups" is runtime
        # state, and the maturity patterns above already catch "available as a
        # Tech Preview".
        rf'\b{ADV}\s+(?:only\s+)?(?:supports?|supported)\b', re.I)),
    ('promise', re.compile(r'\bcoming soon\b', re.I)),
    ('promise', re.compile(
        r'\bwill\s+be\s+(?:supported|added|available|implemented)\s+'
        r'(?:soon|in\s+(?:the\s+)?future|in\s+(?:an?\s+)?(?:upcoming|future|later)\s+'
        r'(?:release|version)s?)\b', re.I)),
    ('dated', re.compile(
        r'\b(?:as of (?:this writing|now|today)|for the time being|at the time of writing)\b', re.I)),
    ('dated', re.compile(
        r'(?:^|[.!?]\s+)(?:Currently|At the moment|At present|At this time|Presently|Nowadays),\s')),
]

FENCE = re.compile(r'^\s*(```|~~~)')
CODE_OPEN = re.compile(r'\{%\s*code\b')
CODE_CLOSE = re.compile(r'\{%\s*endcode\s*%\}')
LINK_TARGET = re.compile(r'\]\([^)]*\)')
HTML_TAG = re.compile(r'<[^>]+>')


def strip_spans(line):
    """Drop inline code spans (CommonMark: backslash escapes, equal-length runs)."""
    out, i, n = [], 0, len(line)
    while i < n:
        c = line[i]
        if c == '\\' and i + 1 < n:
            out.append(line[i:i + 2])
            i += 2
            continue
        if c == '`':
            j = i
            while j < n and line[j] == '`':
                j += 1
            run, k = j - i, j
            while k < n:
                if line[k] == '`':
                    m = k
                    while m < n and line[m] == '`':
                        m += 1
                    if m - k == run:
                        out.append(' ')
                        i = m
                        break
                    k = m
                else:
                    k += 1
            else:
                out.append(line[i:j])
                i = j
            continue
        out.append(c)
        i += 1
    return ''.join(out)


def hits_in_text(text):
    """Yield (lineno, label, prose) for each matching prose line."""
    fence = code = False
    for ln, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            fence = not fence
            continue
        if CODE_OPEN.search(line):
            code = True
        if CODE_CLOSE.search(line):
            code = False
            continue
        if fence or code:
            continue
        prose = HTML_TAG.sub(' ', LINK_TARGET.sub(']', strip_spans(line)))
        for label, rx in PATTERNS:
            if rx.search(prose):
                yield ln, label, ' '.join(prose.split())
                break


def repo_root():
    out = subprocess.run(['git', 'rev-parse', '--show-toplevel'],
                         capture_output=True, text=True)
    if out.returncode:
        sys.exit('timeless.py: not inside a git work tree')
    return pathlib.Path(out.stdout.strip())


def skipped(rel):
    return rel.startswith(SKIP)


def md_files(root, paths):
    seen = set()
    for p in paths or [root]:
        p = pathlib.Path(p).resolve()
        files = [p] if p.is_file() else sorted(p.rglob('*.md'))
        for f in files:
            rel = f.relative_to(root).as_posix()
            # SUMMARY.md mirrors page titles, which error-code pages take verbatim
            # from the server's message text.
            if f.suffix != '.md' or f.name == 'SUMMARY.md' or skipped(rel) or f.resolve() in seen:
                continue
            seen.add(f.resolve())
            yield rel, f


def report(rows):
    for rel, ln, label, prose in rows:
        print(f'{rel}:{ln}: [{label}] {prose[:220]}')
    print(f'{len(rows)} undated product claim(s)', file=sys.stderr)
    return 1 if rows else 0


def cmd_check(paths):
    root = repo_root()
    rows = [(rel, ln, label, prose)
            for rel, f in md_files(root, paths)
            for ln, label, prose in hits_in_text(f.read_text(encoding='utf-8', errors='replace'))]
    return report(rows)


def cmd_new(rev):
    root = repo_root()
    if subprocess.run(['git', 'cat-file', '-e', f'{rev}^{{commit}}'],
                      cwd=root, capture_output=True).returncode:
        print(f'timeless.py: {rev} is not a commit in this clone', file=sys.stderr)
        return 2
    changed = subprocess.run(
        ['git', 'diff', '--name-only', '--diff-filter=AMR', rev, '--', '*.md'],
        cwd=root, capture_output=True, text=True, check=True).stdout.split()
    rows = []
    for rel in changed:
        if skipped(rel) or rel.endswith('SUMMARY.md') or not (root / rel).is_file():
            continue
        now = list(hits_in_text((root / rel).read_text(encoding='utf-8', errors='replace')))
        if not now:
            continue
        old = subprocess.run(['git', 'show', f'{rev}:{rel}'], cwd=root,
                             capture_output=True, text=True)
        before = {prose for _, _, prose in hits_in_text(old.stdout)} if old.returncode == 0 else set()
        rows += [(rel, ln, label, prose) for ln, label, prose in now if prose not in before]
    return report(rows)


def main(argv):
    if len(argv) >= 1 and argv[0] == 'check':
        return cmd_check(argv[1:])
    if len(argv) == 2 and argv[0] == 'new':
        return cmd_new(argv[1])
    print(__doc__.split('USAGE', 1)[1].split('Exit status', 1)[0].strip(), file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
