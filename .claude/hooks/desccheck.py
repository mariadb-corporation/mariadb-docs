#!/usr/bin/env python3
"""desccheck.py — fail on a frontmatter `description:` that GitBook will render broken.

DOCS-6763. GitBook publishes a page's `description:` three ways — the subtitle under the H1, the
`<meta name="description">` tag, and the og:/twitter: preview cards — and treats it as PLAIN
TEXT in all three. Measured against the live site on 2026-10-01:

  * It is cut at exactly 200 characters, with no ellipsis, in the on-page subtitle as well as in
    the meta tags. MaxScale SmartRouter (207 chars) rendered as "...for hybrid (HTAP) proc";
    a 251-char MaxScale tutorial ended mid-sentence on "...a co-located tiebreaker or Galera".
  * Markdown is not rendered. `mysql_tzinfo_to_sql` in backticks shows the backticks, literally,
    in the subtitle a reader sees. `**`, `[text](url)` and backslash escapes would too.

So the 200-character limit is measured on the SOURCE text, markup included — there is no
"rendered length" that is shorter than the raw one.

What fails:

  long         more than 200 characters after YAML folding (lines joined by single spaces)
  blank-line   a blank line inside a block scalar: `>-` turns it into a newline, splitting the
               description into two paragraphs (MaxScale Exasolrouter, before #1184)
  literal      a `|` block scalar, which keeps every line break
  markdown     backticks, `**`, `[text](url)`, or a backslash escape such as `\\_` — all shown
               literally
  liquid       `{%` or `{{`, a GitBook tag or variable, also shown literally
  empty        a `description:` key with no text
  title        the description is the H1 again (case and punctuation ignored), which tells a
               search-results reader nothing the title did not

What does NOT fail: `<` and `&`. GitBook HTML-escapes them (`/restores/<ID>` renders as
written), so they are not a defect.

The parser handles the scalar forms YAML frontmatter uses — plain, single- and double-quoted,
and `>`/`|` block scalars with continuation lines — rather than importing PyYAML, so the gate
needs nothing installed. It was checked against PyYAML on every published page (5,509
descriptions, 0 differences after whitespace normalization) when it was written.

Pages outside a GitBook space are exempt (EXEMPT, the same list fragcheck.py's UNPUBLISHED
uses): `agent-skills/` SKILL.md descriptions in particular are agent-trigger text, not page
descriptions, and are long on purpose.

Usage: desccheck.py <file> [<file> ...] | --stdin0
Exit:  0 clean, 1 findings or unreadable file, 2 usage error.
"""
import re
import sys

LIMIT = 200

# Not GitBook spaces, so nothing in them is published. Keep in step with fragcheck.py.
EXEMPT = ('agent-skills/', 'help-tables/', 'dev-docs/', 'dist/', 'pdf/',
          '.claude/', '.github/', '.git/')

FRONTMATTER = re.compile(r'---\r?\n(.*?)\r?\n---\r?\n', re.S)
BLOCK = re.compile(r'[>|][-+0-9]*')
H1 = re.compile(r'^# (.+?)\s*$', re.M)
MARKDOWN = (
    (re.compile(r'`'), 'a backtick'),
    (re.compile(r'\*\*'), '`**`'),
    (re.compile(r'\]\('), 'a Markdown link'),
    (re.compile(r'\\[\\`*_{}\[\]()#+\-.!|<>]'), 'a backslash escape'),
)


def parse(text):
    """Return (line_no, style, value, has_blank_line) for `description:`, or None if absent."""
    m = FRONTMATTER.match(text)
    if not m:
        return None
    lines = m.group(1).split('\n')
    for i, line in enumerate(lines):
        line = line.rstrip('\r')
        if not line.startswith('description:'):
            continue
        head = line[len('description:'):].strip()
        cont = []
        for nxt in lines[i + 1:]:
            nxt = nxt.rstrip('\r')
            if nxt.startswith((' ', '\t')) or not nxt.strip():
                cont.append(nxt)
            else:
                break
        while cont and not cont[-1].strip():
            cont.pop()
        blank = any(not c.strip() for c in cont)
        words = [c.strip() for c in cont if c.strip()]
        if BLOCK.fullmatch(head):
            style = 'literal' if head.startswith('|') else 'folded'
            value = ' '.join(words)
        elif head[:1] in ('"', "'"):
            style = 'quoted'
            q = head[0]
            raw = ' '.join([head] + words)
            raw = raw[1:-1] if len(raw) > 1 and raw.endswith(q) else raw[1:]
            value = raw.replace("''", "'") if q == "'" else raw.replace('\\"', '"')
        else:
            style = 'plain'
            value = ' '.join([head] + words) if head else ' '.join(words)
        return i + 2, style, value, blank  # +2: the opening `---` is line 1
    return None


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())


def problems(text, found):
    _, style, value, blank = found
    out = []
    if not value.strip():
        return ['empty description']
    if len(value) > LIMIT:
        out.append(f'{len(value)} characters; GitBook cuts the subtitle and meta description '
                   f'at {LIMIT}, mid-word and with no ellipsis')
    if blank:
        out.append('blank line inside the block scalar splits it into two paragraphs')
    if style == 'literal':
        out.append('`|` block scalar keeps its line breaks; use `>-`')
    for rx, what in MARKDOWN:
        if rx.search(value):
            out.append(f'contains {what}, which GitBook shows literally (descriptions are plain text)')
    if '{%' in value or '{{' in value:
        out.append('contains a GitBook tag or variable, which is shown literally')
    h1 = H1.search(text[FRONTMATTER.match(text).end():])
    if h1 and norm(h1.group(1)) and norm(h1.group(1)) == norm(value):
        out.append('repeats the page title; say what the page covers instead')
    return out


def main(argv):
    args = argv[1:]
    if not args:
        print(f'usage: {argv[0]} <file> [<file> ...] | --stdin0', file=sys.stderr)
        return 2
    if args[0] == '--stdin0':
        if len(args) != 1:
            print(f'usage: {argv[0]} --stdin0   (reads NUL-delimited paths on stdin; takes no '
                  f'other arguments)', file=sys.stderr)
            return 2
        given = [p for p in sys.stdin.buffer.read().decode('utf-8').split('\0') if p]
    else:
        given = args
    paths = [p for p in given if p.endswith('.md') and not p.startswith(EXEMPT)]
    checked = failed = errors = 0
    for p in paths:
        try:
            with open(p, encoding='utf-8') as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError) as e:
            print(f'{p}: cannot read: {e}', file=sys.stderr)
            errors += 1
            continue
        found = parse(text)
        if not found:
            continue
        checked += 1
        probs = problems(text, found)
        if probs:
            failed += 1
            for pr in probs:
                print(f'{p}:{found[0]}: description: {pr}', file=sys.stderr)
    print(f'desccheck: {checked} description(s) in {len(paths)} published file(s) '
          f'({len(given)} given, {len(given) - len(paths)} exempt or not Markdown); '
          f'{failed} failing')
    return 1 if (failed or errors) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
