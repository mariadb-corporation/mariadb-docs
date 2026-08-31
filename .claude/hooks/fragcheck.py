#!/usr/bin/env python3
"""fragcheck.py — GitBook-accurate heading-anchor (#fragment) checker.

WHY THIS EXISTS
    lychee's --include-fragments uses a GitHub-flavoured slugger that diverges
    from GitBook's, so on this repo it is wrong in BOTH directions: measured on
    main (DOCS-6491, 2026-08-21) it reported 1,129 fragment errors of which 386
    were false positives (the anchor resolves on the live site), while missing
    213 anchors that really are dead. That is why link-check-pr.yml passes no
    --include-fragments, and why turning it on there would not help.

    This implements GitBook's rules instead. `validate` re-derives them from the
    rendered pages, so they stay checkable rather than folkloric.

WHICH HEADINGS PUBLISH AN ANCHOR:  h2, h3 and h4 ONLY  (DOCS-6503)
    h1 is the page title. h5 and h6 render as <p><strong class="font-bold">...</strong>
    </p> with no id at all -- grep '<h5' on any rendered page returns 0. Crediting
    them made this checker wrong in the OPTIMISTIC direction: it computed an anchor
    that does not exist, so a link to it was reported as resolving while the reader
    lands at the top of the page. Such a link is now reported as
    [unanchored-heading]; the honest repair is to raise the heading to h4, or to
    retarget the link at the enclosing section -- never to promote a bold paragraph
    to "#####", which reads as a fix and repairs nothing.

THE SLUG RULES  (each derived from a rendered id="..." on mariadb.com/docs)
    * lowercase; dots and underscores survive
    * an explicit <a ... id="x"> inside the heading line WINS over the text slug
      (KB-migration debris, and GitBook honours it) -- an id="..." in prose does not
    * HTML entities are decoded FIRST, so a trailing "&#x20;" is a space and not an
      "&" to be spelled out (columnstore_cache_use_import&#x20; -> ..._import)
    * a footnote reference in the heading contributes nothing:
      "EITS[^1] vs. InnoDB Statistics" -> eits-vs.-innodb-statistics
    * a trailing kramdown "{#id}" is removed from the text
    * CHARMAP characters are spelled out rather than collapsed to a dash:
      & -> and, | -> or, > -> greater-than, < -> less-than, $ -> usd
      ("$type" -> usdtype, "Accumulators ($group)" -> accumulators-usdgroup),
      U+00AE -> -r- ("MongoDB(R) Shell" -> mongodb-r-shell)
    * apostrophes vanish leaving no dash (Node's -> nodes)
    * every other run of non-word characters collapses to one dash
      (TLS/SSL -> tls-ssl, "(options) -> PoolCluster" -> options-greater-than-poolcluster)
    * "+" vanishes AFTER that collapse, so it leaves its two dashes behind:
      "5.3.2 + MyISAM" -> "5.3.2--myisam" (then id- prefixed, being digit-led),
      while "x--an Imperfect Solution"
      (a literal double dash, one separator run) -> "x-an-imperfect-solution"
    * leading/trailing "-" and trailing "." / "_" are trimmed
    * a digit-leading slug is prefixed "id-" (2_DIGIT_YEAR -> id-2_digit_year)
    * the slug is truncated to 100 characters
    * duplicate slugs get -1, -2, ... in document order

    Validated at 4,599/4,599 computed anchors over 99 pages (47 sampled at
    random, 45 chosen for punctuation density, 7 used to derive the rules) -- and
    that sample, picked for punctuation DENSITY, happened to contain no h5, no "$"
    and no "(R)", which is how five rule gaps survived it (DOCS-6503). The second
    sweep picked pages for STRUCTURAL variety instead: every character that occurs
    in a heading anywhere in the repo and is not a plain ASCII word character, two
    pages each -- 33 pages, 1,317 anchors. Whatever GitBook transliterates that
    CHARMAP does not cover is REPORTED rather than guessed at; see unmappable().

MODES
    fragcheck.py check [path ...]        dead anchors under each path (default: repo)
    fragcheck.py new <rev> [path ...]    only what <rev> had fine -- the gate
    fragcheck.py ids [path ...]          headings publishing another heading's anchor
    fragcheck.py risky [path ...]        headings whose computed anchor is a guess
    fragcheck.py anchors <file.md>       the anchors one file publishes
    fragcheck.py validate <file.md> ...  compare computed anchors to the live page

`new` is what doc-lint.sh calls. It scans the whole tree twice (once here, once in
a throwaway worktree at <rev>) and reports only the difference, so the repo's
pre-existing dead anchors stay out of the way while a heading rename that breaks
inbound links from untouched pages still fails. It gates two classes:

    * anchors that <rev> resolved and the working tree does not (a rename)
    * headings that took over another heading's explicit id (`ids`, DOCS-6492) --
      invisible to every link checker, this one included, because the anchors all
      exist and resolve; they just land on the wrong section
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import pathlib
import unicodedata
import urllib.parse
from collections import Counter

BASE_URL = 'https://mariadb.com/docs'
CACHE = pathlib.Path(tempfile.gettempdir()) / 'fragcheck-cache'
MAX_SLUG = 100

# The levels GitBook renders as <h2>/<h3>/<h4 id="..."> — see the header comment.
ANCHORED = (2, 3, 4)

# Not GitBook spaces, so their links are never published: skip them.
UNPUBLISHED = ('agent-skills/', 'help-tables/', 'dev-docs/', 'dist/', 'pdf/',
               '.claude/', '.github/', '.git/')

FENCE = re.compile(r'^\s*(```|~~~)')
HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
HEADING_ID = re.compile(r'''<a\b[^>]*\bid\s*=\s*["']([^"']+)["']''')
KRAMDOWN_ID = re.compile(r'\s*\{#[A-Za-z0-9._:-]+\}\s*$')
FOOTNOTE_REF = re.compile(r'\[\^[^\]]+\]')
FOOTNOTE_DEF = re.compile(r'^\[\^([^\]]+)\]:')
FOOTNOTE_ANCHOR = re.compile(r'^user-content-fn(?:ref)?-(.+)$')
CODESPAN = re.compile(r'`+([^`]*)`+')
LINK = re.compile(r'\]\(\s*<?([^)>\s]+)>?\s*\)')
ATTR = re.compile(r'''\b(?:href|url)\s*=\s*["']([^"']+)["']''')
SKIP_PREFIX = ('http://', 'https://', 'mailto:', 'ftp://', '//', '/')

# Spelled out instead of collapsing to a dash. Every entry was read off a rendered
# id rather than assumed: "&" from "Source format & GitBook blocks", "$" from
# "#### $type" -> usdtype and "Status Values ($1)" -> status-values-usd1, U+00AE
# from "MongoDB(R) Shell" -> mongodb-r-shell. The values are GitBook's replacement
# text, so the separator run around them is left to the collapse step: "(r)" and
# " and " both end up as one dash on each side. Currency and trademark signs point
# at a speakingurl-style charmap, so more entries almost certainly exist -- but
# only the ones a rendered page has confirmed belong here; unmappable() reports
# the rest instead of extrapolating.
CHARMAP = {'&': ' and ', '|': ' or ', '>': ' greater than ',
           '<': ' less than ', '$': 'usd', '®': '(r)'}


# ---------------------------------------------------------------- slug rules

def strip_inline(text):
    """Reduce heading markup to the words GitBook renders."""
    text = html.unescape(text)                              # &#x20; is a space
    text = KRAMDOWN_ID.sub('', text)                        # trailing {#id}
    text = FOOTNOTE_REF.sub('', text)                       # [^1] renders as a marker
    text = re.sub(r'!\[([^\]]*)\]\([^)]*\)', r'\1', text)   # images
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)    # links -> label
    text = re.sub(r'<[^>]+>', '', text)                     # html tags
    # Park code spans so emphasis sees a non-alphanumeric neighbour: that is what
    # makes `-p`_password_ italic (-> ppassword) while no_dup_key stays literal.
    parked = []

    def park(m):
        parked.append(m.group(1))
        return f'\x00{len(parked) - 1}\x00'

    text = CODESPAN.sub(park, text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'(?<![A-Za-z0-9\\])_([^_\\]+)_', r'\1', text)
    text = re.sub(r'\\(.)', r'\1', text)                    # escapes
    return re.sub(r'\x00(\d+)\x00', lambda m: parked[int(m.group(1))], text)


def gitbook_slug(heading):
    s = strip_inline(heading).lower()
    for char, spelled in CHARMAP.items():
        s = s.replace(char, spelled)
    s = re.sub(r"['‘’]", '', s)     # apostrophes leave no dash
    s = re.sub(r'[^a-z0-9._+]+', '-', s)      # separator runs -> one dash
    s = s.replace('+', '')                    # ... then "+" drops out
    s = s.strip('-')
    s = s.rstrip('._').strip('-')
    if s[:1].isdigit():
        s = 'id-' + s
    return s[:MAX_SLUG]


def unmappable(heading):
    """Characters in a heading that these rules cannot slug faithfully.

    GitBook transliterates rather than collapses: "China - 中国" publishes as
    china-zhong-guo, so it is running a full Unicode charmap that CHARMAP only
    covers the part of. Everything non-ASCII in this repo's headings that is NOT
    a letter -- arrows, em/en dashes, smart quotes, the acute accent, six emoji --
    was confirmed live to collapse to a dash like any other separator, so only
    non-ASCII LETTERS are unknowable. Guessing at those would put a confidently
    wrong anchor in the inventory, which is the whole failure this checker exists
    to avoid, so `risky` lists them and a link that could be one of them is
    reported [uncertain-slug] -- see could_be_guessed(), which keeps unrelated
    dead anchors on the same page plainly [absent].
    """
    return sorted({c for c in strip_inline(heading)
                   if ord(c) > 127 and unicodedata.category(c).startswith('L')})


def uncomment(line, in_comment):
    """Blank out HTML comments, returning (visible_text, still_open)."""
    out = []
    while line:
        if in_comment:
            close = line.find('-->')
            if close < 0:
                return ''.join(out), True
            line, in_comment = line[close + 3:], False
        else:
            open_ = line.find('<!--')
            if open_ < 0:
                out.append(line)
                break
            out.append(line[:open_])
            line, in_comment = line[open_ + 4:], True
    return ''.join(out), in_comment


def content_lines(path):
    """(line_no, visible_text, in_fence) for each line.

    HTML comments are blanked, because GitBook publishes nothing from them: two
    Python comments inside a commented-out example in
    connectors/mariadb-connector-python/usage.md were otherwise read as level-1
    headings, which corrupts any "nearest enclosing heading level" reasoning
    (DOCS-6503 -- reported there as indented code blocks, but HEADING anchors "#"
    at column 0, so an indented block can never match; the cause was the comment).
    Comment markers are not tracked inside a fence, where "<!--" is just text.
    """
    in_fence = in_comment = False
    for n, line in enumerate(read(path).splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            line, in_comment = uncomment(line, in_comment)
        yield n, line, in_fence


def headings_of(path):
    """(line_no, level, raw_text, explicit_id_or_None) for every h1..h6."""
    out = []
    for n, line, in_fence in content_lines(path):
        if in_fence:
            continue
        m = HEADING.match(line)
        if not m:
            continue
        explicit = HEADING_ID.search(m.group(2))
        out.append((n, len(m.group(1)), m.group(2),
                    explicit.group(1) if explicit else None))
    return out


def anchored_headings(path):
    """Only the headings GitBook gives an id to."""
    return [h for h in headings_of(path) if h[1] in ANCHORED]


def anchors_of(path):
    """Anchors a markdown file publishes, in document order."""
    seen = Counter()
    out = []
    for _, _, text, explicit in anchored_headings(path):
        base = explicit if explicit else gitbook_slug(text)
        if not base:
            continue
        n = seen[base]
        seen[base] += 1
        out.append(base if n == 0 else f'{base}-{n}')
    return out


def deep_slugs(path):
    """What an h5/h6 heading WOULD publish if GitBook anchored it. It does not."""
    return {gitbook_slug(text) for _, level, text, _ in headings_of(path)
            if level > max(ANCHORED)} - {''}


def guessed_slugs(path):
    """Anchors this file publishes that these rules can only guess at."""
    return {gitbook_slug(text) for _, _, text, explicit in anchored_headings(path)
            if not explicit and unmappable(text)} - {''}


def footnote_defs(path):
    """Labels defined by a "[^label]:" line, i.e. the live footnote anchors.

    GitBook serialises an annotation as <a data-footnote-ref href="#user-content-
    fn-N">, and renders it as a hover tooltip carrying the definition text -- no
    #user-content-fn-N id is emitted anywhere on the page (checked: 0 hits for
    both "user-content-fn" and "data-footnote" in the rendered HTML). So the
    fragment is unreachable BY DESIGN and a defined footnote is not a defect.
    Treating all of them as dead made [footnote] 21 findings / 0 true positives
    (DOCS-6503); resolving them against these labels leaves only the real class,
    a reference whose definition is missing, where the tooltip comes up empty.
    """
    return {m.group(1) for _, line, in_fence in content_lines(path)
            if not in_fence for m in [FOOTNOTE_DEF.match(line)] if m}


def stolen_ids(path):
    """Headings whose explicit id is the slug of a DIFFERENT heading here.

    The wide class -- an explicit id that merely differs from the heading's own
    text slug -- is 48 cases on this repo and mostly BENIGN: 40 are historical
    KB anchors deliberately kept so old inbound links keep resolving
    (#choosing-mariabackup-for-ssts, the #overview_h2 set on the wsrep variable
    pages). Only the narrow case is a defect: the id belongs to another heading
    on the same page, because a heading line was duplicated for a new section
    and its text edited while the anchor markup was not. GitBook honours the
    explicit id, so the two sections share one anchor, the loser dedupes to -1,
    and the anchor a reader expects for either section does not exist at all
    (DOCS-6492).

    Flagging all 48 would be a 6x overstatement -- DOCS-6413's failure mode.
    """
    heads = anchored_headings(path)
    own = {}
    for n, _, text, _ in heads:
        own.setdefault(gitbook_slug(text), n)
    out = []
    for n, _, text, explicit in heads:
        if not explicit:
            continue
        mine = gitbook_slug(text)
        if explicit == mine:
            continue
        other = own.get(explicit)
        if other is not None and other != n:
            out.append((n, mine, explicit, other))
    return out


# ------------------------------------------------------------- link scanning

def read(path):
    return path.read_text(errors='replace')


def links_of(path):
    """(raw_target, line_no) for every local link carrying a fragment."""
    out = []
    for n, line, in_fence in content_lines(path):
        if in_fence:
            continue
        for target in LINK.findall(line) + ATTR.findall(line):
            if '#' not in target or '{' in target:
                continue
            if target.startswith(SKIP_PREFIX) or 'broken-reference' in target:
                continue
            out.append((target, n))
    return out


def resolve(src, target):
    """Return (target_markdown_path_or_None, fragment)."""
    rel_target, _, frag = target.partition('#')
    frag = urllib.parse.unquote(frag)
    if not rel_target:
        return src, frag
    p = (src.parent / rel_target).resolve()
    if p.is_dir():
        p = p / 'README.md'
    elif not p.exists():
        for alt in (p.with_suffix('.md'), p / 'README.md'):
            if alt.exists():
                p = alt
                break
    return (p if p.is_file() else None), frag


def repo_root(start):
    """Nearest ancestor that looks like this repo (works inside a worktree)."""
    start = pathlib.Path(start).resolve()
    for d in [start] + list(start.parents):
        if (d / '.codespellignore').is_file() or (d / '.git').exists():
            return d
    return start


def relpath(path, root):
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def md_files(root, base):
    """Published .md files under root, each real file once.

    The dedupe is load-bearing: a symlinked page makes rglob yield both names
    while relpath() resolves them to the same string, so every fragment link on
    it is counted and reported twice, indistinguishably from two real links on
    one line. That overstated the DOCS-6499 inventory by 3 -- the "262 remaining"
    figure was really 259 -- and only surfaced because an apply script asserted
    an occurrence count (DOCS-6503).
    """
    root = pathlib.Path(root)
    if root.is_file():
        return [root]
    out, seen = [], set()
    for p in sorted(root.rglob('*.md')):
        if relpath(p, base).startswith(UNPUBLISHED):
            continue
        real = p.resolve()
        if real in seen:
            continue
        seen.add(real)
        out.append(p)
    return out


def loose(frag):
    """Fragment with dash runs collapsed."""
    return re.sub(r'-{2,}', '-', frag)


def squash(frag):
    return re.sub(r'[^a-z0-9]', '', frag.lower())


def could_be_guessed(frag, guessed):
    """Might this fragment be one of the anchors we could only guess at?

    Transliteration only ever EXPANDS an unmappable character into more letters,
    so the guess (where it collapsed to a dash) and the truth share the mappable
    segments in order: guess "china" against truth "china-zhong-guo". Matching on
    that keeps the doubt where it belongs — an unrelated dead anchor on the same
    page is still plainly [absent], not excused by the page's one odd heading.
    """
    for guess in guessed:
        if frag == guess:
            return True
        rest = frag
        for part in filter(None, guess.split('-')):
            at = rest.find(part)
            if at < 0:
                break
            rest = rest[at + len(part):]
        else:
            return True
    return False


def classify(frag, live, deep=(), guessed=()):
    """Bucket a dead anchor and, where possible, name the anchor it meant."""
    if frag in deep:
        return 'unanchored-heading', ''
    if could_be_guessed(frag, guessed):
        return 'uncertain-slug', ''
    by_case = {a.lower(): a for a in live}
    if frag.lower() in by_case:
        return 'case-only', by_case[frag.lower()]
    if loose(frag) in {loose(a) for a in live}:      # before the looser test below
        return 'dash-count', next(a for a in live if loose(a) == loose(frag))
    by_squash = {squash(a): a for a in live}
    if squash(frag) in by_squash:
        return 'punctuation', by_squash[squash(frag)]
    if frag.lstrip('-') in live:
        return 'leading-dash', frag.lstrip('-')
    return 'absent', ''


def page_facts(path):
    """(anchors, h5/h6 slugs, footnote labels, unslugabble?) for one target page.

    A guessed anchor is deliberately WITHHELD from the live set rather than
    offered as known-good. Leaving it in silently resolved every link to it —
    which for "China - 中国" means blessing #china, when the page publishes
    #china-zhong-guo. Withholding it puts both spellings in [uncertain-slug],
    where a human confirms against the rendered page, instead of putting one of
    them in the "resolves" pile on the strength of a guess.
    """
    guessed = guessed_slugs(path)
    anchors = {a for a in anchors_of(path)
               if re.sub(r'-\d+$', '', a) not in guessed}
    return anchors, deep_slugs(path), footnote_defs(path), guessed


def check(paths, base):
    """Return (links_checked, findings, unresolved)."""
    cache, findings, unresolved, checked = {}, [], [], 0
    for root in paths:
        for f in md_files(root, base):
            for target, line in links_of(f):
                tgt, frag = resolve(f, target)
                if not frag:
                    continue
                if tgt is None:
                    unresolved.append((relpath(f, base), line, target))
                    continue
                if tgt not in cache:
                    cache[tgt] = page_facts(tgt)
                checked += 1
                live, deep, notes, guessed = cache[tgt]
                if frag in live:
                    continue
                fn = FOOTNOTE_ANCHOR.match(frag)
                if fn:
                    # No id is published either way, so the reachable question is
                    # whether the tooltip has any text: defined means fine.
                    if fn.group(1) in notes:
                        continue
                    findings.append((relpath(f, base), line, frag,
                                     relpath(tgt, base), 'footnote', ''))
                    continue
                bucket, fix = classify(frag, live, deep, guessed)
                findings.append((relpath(f, base), line, frag,
                                 relpath(tgt, base), bucket, fix))
    return checked, findings, unresolved


def scan_risky(paths, base):
    """Headings whose computed anchor is a guess, as (file, line, chars, slug)."""
    out = []
    for root in paths:
        for f in md_files(root, base):
            for line, _, text, explicit in anchored_headings(f):
                bad = [] if explicit else unmappable(text)
                if bad:
                    out.append((relpath(f, base), line, ''.join(bad),
                                gitbook_slug(text)))
    return out


def scan_ids(paths, base):
    """Every stolen-id finding under each path, as (file, line, own, id, other)."""
    out = []
    for root in paths:
        for f in md_files(root, base):
            for line, mine, stolen, other in stolen_ids(f):
                out.append((relpath(f, base), line, mine, stolen, other))
    return out


# ------------------------------------------------------- reporting / gate

def describe_id(finding):
    src, line, mine, stolen, other = finding
    return (f'{src}:{line}: publishes #{stolen}, which is line {other}\'s '
            f'anchor, instead of its own #{mine}')


STOLEN_HELP = (
    '\n          A heading line duplicated for a new section keeps the original\'s\n'
    '          <a href="#x" id="x">, so both sections publish one anchor, the second\n'
    '          dedupes to -1, and neither owns the anchor a reader expects\n'
    '          (DOCS-6492). Delete the copied markup from the new heading — it then\n'
    '          falls back to its own text slug. A deliberate historical alias is not\n'
    '          flagged: only an id that belongs to another heading on the same page.')


def describe(finding):
    src, line, frag, tgt, bucket, fix = finding
    suffix = f'  [{bucket}]' + (f' -> #{fix}' if fix else '')
    return f'{src}:{line}: #{frag} -> {tgt}{suffix}'


MECHANICAL = ('case-only', 'punctuation', 'dash-count', 'leading-dash')

BUCKET_NOTES = {
    'unanchored-heading':
        'the target IS an h5/h6 heading, which GitBook renders as a bold\n'
        '                        paragraph with no id — raise it to h4 or retarget the link',
    'footnote':
        'a footnote reference with no "[^label]:" definition, so the\n'
        '                        tooltip comes up empty',
    'uncertain-slug':
        'the target page has a heading GitBook transliterates and these\n'
        '                        rules do not — see `risky`; may not be dead at all',
}


def summarize(checked, findings, unresolved, label='dead'):
    print(f'\n{checked} fragment links checked | {len(findings)} {label} | '
          f'{len(unresolved)} unresolvable targets')
    for bucket, n in Counter(f[4] for f in findings).most_common():
        note = ('  (mechanical: the fix is named above)' if bucket in MECHANICAL
                else '  ' + BUCKET_NOTES[bucket] if bucket in BUCKET_NOTES else '')
        print(f'  {n:6d}  {bucket}{note}')


def cmd_check(args):
    root = repo_root(args[0] if args else '.')
    checked, findings, unresolved = check([pathlib.Path(a) for a in args] or [root], root)
    for f in findings:
        print('DEAD ' + describe(f))
    summarize(checked, findings, unresolved)
    return 0


def cmd_risky(args):
    """List headings whose anchor these rules cannot compute faithfully."""
    root = repo_root(args[0] if args else '.')
    found = scan_risky([pathlib.Path(a) for a in args] or [root], root)
    for src, line, chars, slug in found:
        print(f'RISKY {src}:{line}: {chars!r} — guessed #{slug}, '
              f'GitBook transliterates')
    print(f'\nrisky: {len(found)} heading(s) whose computed anchor is a guess')
    if found:
        print('\n          GitBook runs a Unicode charmap ("China - 中国" publishes as\n'
              '          china-zhong-guo) that CHARMAP only covers part of. A link to one\n'
              '          of these anchors is reported [uncertain-slug], not [absent]:\n'
              '          confirm it against the rendered page before treating it as dead.')
    return 0


def cmd_ids(args):
    """List every heading carrying another heading's anchor (absolute, not diffed)."""
    root = repo_root(args[0] if args else '.')
    found = scan_ids([pathlib.Path(a) for a in args] or [root], root)
    for f in found:
        print('STOLEN ' + describe_id(f))
    print(f'\nids: {len(found)} heading(s) publishing another heading\'s anchor')
    if found:
        print(STOLEN_HELP)
    return 1 if found else 0


def cmd_new(args):
    """Report anchors dead in the working tree that were fine at <rev>."""
    if not args:
        print('fragcheck: `new` needs a revision', file=sys.stderr)
        return 2
    rev, paths = args[0], args[1:]
    root = repo_root(paths[0] if paths else '.')
    roots = [pathlib.Path(p) for p in paths] or [root]
    _, now, _ = check(roots, root)
    now_ids = scan_ids(roots, root)

    tmp = tempfile.mkdtemp(prefix='fragcheck-base-')
    worktree = os.path.join(tmp, 'base')
    try:
        add = subprocess.run(['git', '-C', str(root), 'worktree', 'add',
                              '--detach', '-q', worktree, rev],
                             capture_output=True, text=True)
        if add.returncode != 0:
            print(f'fragcheck: cannot check out {rev} — no baseline, SKIPPED\n'
                  f'           {add.stderr.strip()}', file=sys.stderr)
            return 0
        # .resolve() matters: on macOS the temp dir is reached through a symlink,
        # and relpath() resolves each file, so an unresolved root yields absolute
        # keys that can never match the working tree's relative ones.
        base_root = pathlib.Path(worktree).resolve()
        _, before, _ = check([base_root], base_root)
        before_ids = scan_ids([base_root], base_root)
    finally:
        subprocess.run(['git', '-C', str(root), 'worktree', 'remove', '--force',
                        worktree], capture_output=True)
        shutil.rmtree(tmp, ignore_errors=True)

    def key(f):
        return (f[0], f[3], f[2])      # source, target, fragment -- not the line

    def idkey(f):
        return (f[0], f[2], f[3])      # file, own slug, stolen id -- not the line

    rc = 0
    was_dead = {key(f) for f in before}
    fresh = [f for f in now if key(f) not in was_dead]
    if fresh:
        rc = 1
        print(f'fragcheck: {len(fresh)} heading anchor(s) that {rev} resolved are now dead:',
              file=sys.stderr)
        for f in fresh:
            print('  ' + describe(f), file=sys.stderr)
        print('\n          A renamed heading breaks every inbound link to its old anchor,\n'
              '          including links from pages this commit never touched. Either restore\n'
              '          the heading text or retarget the links listed above.', file=sys.stderr)
        if any(f[4] == 'unanchored-heading' for f in fresh):
            print('\n          [unanchored-heading] means the target is an h5/h6, which GitBook\n'
                  '          renders as a bold paragraph with no id. Promoting a bold block to\n'
                  '          "#####" therefore fixes nothing, however much it looks like it does\n'
                  '          (DOCS-6503): use "####" or shallower, or link the enclosing section.',
                  file=sys.stderr)

    # Diffed against <rev> for the same reason as the dead anchors: this repo is
    # also edited from the GitBook UI, so an absolute check would fail unrelated
    # PRs the moment a GITBOOK-* commit introduced one case.
    was_stolen = {idkey(f) for f in before_ids}
    fresh_ids = [f for f in now_ids if idkey(f) not in was_stolen]
    if fresh_ids:
        rc = 1
        print(f'fragcheck: {len(fresh_ids)} heading(s) now carry another heading\'s '
              f'anchor:', file=sys.stderr)
        for f in fresh_ids:
            print('  ' + describe_id(f), file=sys.stderr)
        print(STOLEN_HELP, file=sys.stderr)

    if not rc:
        print(f'fragcheck: no new dead heading anchors vs {rev} '
              f'({len(now)} pre-existing, unchanged); no new stolen heading ids '
              f'({len(now_ids)} pre-existing)')
    return rc


# ------------------------------------------------------------- live validate

CHROME = {'gb-trademark', 'mask-image', 'search-input', 'table-of-contents',
          'toc-button', 'toc-scroll-container', 'undefined'}


def fetch(url):
    cached = CACHE / (re.sub(r'[^a-z0-9]+', '_', url) + '.html')
    if cached.exists():
        return cached.read_text(errors='replace')
    html = subprocess.run(['curl', '-sL', '--max-time', '60', url],
                          capture_output=True, text=True).stdout
    CACHE.mkdir(exist_ok=True)
    cached.write_text(html, errors='replace')
    return html


def cmd_validate(args):
    """Compare computed anchors against the ids the live site renders."""
    total = miss = risky = 0
    for arg in args:
        path = pathlib.Path(arg).resolve()
        root = repo_root(path)
        page = relpath(path, root)[:-3]
        if page.endswith('/README'):
            page = page[:-len('/README')]
        html = fetch(f'{BASE_URL}/{page}')
        live = {i for i in re.findall(r'id="([A-Za-z0-9][A-Za-z0-9._-]{2,})"', html)
                if i not in CHROME and not i.startswith('base-ui-')
                and not re.fullmatch(r'p-[0-9a-f]{16,}', i)}
        if len(html) < 5000 or not live:
            print(f'SKIP (no live content) {arg}')
            continue
        mine = anchors_of(path)
        # A heading these rules cannot slug faithfully is a known unknown, not a
        # rule failure — count it apart so the confirmed figure stays an oracle.
        guessed = guessed_slugs(path)
        bad = [a for a in mine if a not in live and a not in guessed]
        unsure = [a for a in mine if a not in live and a in guessed]
        total += len(mine)
        miss += len(bad)
        risky += len(unsure)
        print(f'{"OK  " if not bad else "MISS"} {len(mine):3d} anchors, '
              f'{len(bad)} unmatched'
              + (f', {len(unsure)} unslugabble' if unsure else '') + f'  {arg}')
        for a in bad:
            print(f'       computed {a!r} is not among the live ids')
        for a in unsure:
            print(f'       guessed  {a!r} — transliterated heading, see `risky`')
    print(f'\nvalidate: {total - miss - risky}/{total - risky} computed anchors '
          f'confirmed live' + (f' ({risky} unslugabble, excluded)' if risky else ''))
    return 1 if miss else 0


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'check'
    args = sys.argv[2:]
    if mode == 'anchors':
        print('\n'.join(anchors_of(pathlib.Path(args[0]))))
        return 0
    if mode == 'validate':
        return cmd_validate(args)
    if mode == 'new':
        return cmd_new(args)
    if mode == 'ids':
        return cmd_ids(args)
    if mode == 'risky':
        return cmd_risky(args)
    if mode == 'check':
        return cmd_check(args)
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
