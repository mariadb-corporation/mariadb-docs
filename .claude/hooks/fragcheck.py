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

THE SLUG RULES  (each derived from a rendered id="..." on mariadb.com/docs)
    * a level-1 heading is the page title and publishes no anchor
    * lowercase; dots and underscores survive
    * an explicit <a ... id="x"> inside the heading line WINS over the text slug
      (KB-migration debris, and GitBook honours it) -- an id="..." in prose does not
    * & -> and, | -> or, > -> greater-than, < -> less-than
    * apostrophes vanish leaving no dash (Node's -> nodes)
    * every other run of non-word characters collapses to one dash
      (TLS/SSL -> tls-ssl, "(options) -> PoolCluster" -> options-greater-than-poolcluster)
    * "+" vanishes AFTER that collapse, so it leaves its two dashes behind:
      "5.3.2 + MyISAM" -> "5.3.2--myisam", while "x--an Imperfect Solution"
      (a literal double dash, one separator run) -> "x-an-imperfect-solution"
    * leading/trailing "-" and trailing "." / "_" are trimmed
    * a digit-leading slug is prefixed "id-" (2_DIGIT_YEAR -> id-2_digit_year)
    * the slug is truncated to 100 characters
    * duplicate slugs get -1, -2, ... in document order

    Validated at 4,599/4,599 computed anchors over 99 pages (47 sampled at
    random, 45 chosen for punctuation density, 7 used to derive the rules).

MODES
    fragcheck.py check [path ...]        dead anchors under each path (default: repo)
    fragcheck.py new <rev> [path ...]    only anchors that <rev> had fine -- the gate
    fragcheck.py anchors <file.md>       the anchors one file publishes
    fragcheck.py validate <file.md> ...  compare computed anchors to the live page

`new` is what doc-lint.sh calls: it scans the whole tree twice (once here, once in
a throwaway worktree at <rev>) and reports only the difference, so the repo's
pre-existing dead anchors stay out of the way while a heading rename that breaks
inbound links from untouched pages still fails.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import pathlib
import urllib.parse
from collections import Counter

BASE_URL = 'https://mariadb.com/docs'
CACHE = pathlib.Path(tempfile.gettempdir()) / 'fragcheck-cache'
MAX_SLUG = 100

# Not GitBook spaces, so their links are never published: skip them.
UNPUBLISHED = ('agent-skills/', 'help-tables/', 'dev-docs/', 'dist/', 'pdf/',
               '.claude/', '.github/')

FENCE = re.compile(r'^\s*(```|~~~)')
HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
HEADING_ID = re.compile(r'''<a\b[^>]*\bid\s*=\s*["']([^"']+)["']''')
CODESPAN = re.compile(r'`+([^`]*)`+')
LINK = re.compile(r'\]\(\s*<?([^)>\s]+)>?\s*\)')
ATTR = re.compile(r'''\b(?:href|url)\s*=\s*["']([^"']+)["']''')
SKIP_PREFIX = ('http://', 'https://', 'mailto:', 'ftp://', '//', '/')


# ---------------------------------------------------------------- slug rules

def strip_inline(text):
    """Reduce heading markup to the words GitBook renders."""
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
    s = (s.replace('&', '-and-').replace('|', '-or-')
          .replace('>', '-greater-than-').replace('<', '-less-than-'))
    s = re.sub(r"['‘’]", '', s)     # apostrophes leave no dash
    s = re.sub(r'[^a-z0-9._+]+', '-', s)      # separator runs -> one dash
    s = s.replace('+', '')                    # ... then "+" drops out
    s = s.strip('-')
    s = s.rstrip('._').strip('-')
    if s[:1].isdigit():
        s = 'id-' + s
    return s[:MAX_SLUG]


def anchors_of(path):
    """Anchors a markdown file publishes, in document order."""
    seen = Counter()
    out = []
    in_fence = False
    for line in read(path).splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if not m or len(m.group(1)) == 1:
            continue
        explicit = HEADING_ID.search(m.group(2))
        base = explicit.group(1) if explicit else gitbook_slug(m.group(2))
        if not base:
            continue
        n = seen[base]
        seen[base] += 1
        out.append(base if n == 0 else f'{base}-{n}')
    return out


# ------------------------------------------------------------- link scanning

def read(path):
    return path.read_text(errors='replace')


def links_of(path):
    """(raw_target, line_no) for every local link carrying a fragment."""
    out = []
    in_fence = False
    for n, line in enumerate(read(path).splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
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
    root = pathlib.Path(root)
    if root.is_file():
        return [root]
    return [p for p in sorted(root.rglob('*.md'))
            if not relpath(p, base).startswith(UNPUBLISHED)]


def loose(frag):
    """Fragment with dash runs collapsed."""
    return re.sub(r'-{2,}', '-', frag)


def squash(frag):
    return re.sub(r'[^a-z0-9]', '', frag.lower())


def classify(frag, live):
    """Bucket a dead anchor and, where possible, name the anchor it meant."""
    if frag.startswith('user-content-fn'):
        return 'footnote', ''      # GitBook publishes no footnote anchors at all
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
                    cache[tgt] = set(anchors_of(tgt))
                checked += 1
                live = cache[tgt]
                if frag in live:
                    continue
                bucket, fix = classify(frag, live)
                findings.append((relpath(f, base), line, frag,
                                 relpath(tgt, base), bucket, fix))
    return checked, findings, unresolved


# ------------------------------------------------------- reporting / gate

def describe(finding):
    src, line, frag, tgt, bucket, fix = finding
    suffix = f'  [{bucket}]' + (f' -> #{fix}' if fix else '')
    return f'{src}:{line}: #{frag} -> {tgt}{suffix}'


def summarize(checked, findings, unresolved, label='dead'):
    print(f'\n{checked} fragment links checked | {len(findings)} {label} | '
          f'{len(unresolved)} unresolvable targets')
    for bucket, n in Counter(f[4] for f in findings).most_common():
        mechanical = bucket in ('case-only', 'punctuation', 'dash-count',
                                'leading-dash')
        print(f'  {n:6d}  {bucket}'
              + ('  (mechanical: the fix is named above)' if mechanical else ''))


def cmd_check(args):
    root = repo_root(args[0] if args else '.')
    checked, findings, unresolved = check([pathlib.Path(a) for a in args] or [root], root)
    for f in findings:
        print('DEAD ' + describe(f))
    summarize(checked, findings, unresolved)
    return 0


def cmd_new(args):
    """Report anchors dead in the working tree that were fine at <rev>."""
    if not args:
        print('fragcheck: `new` needs a revision', file=sys.stderr)
        return 2
    rev, paths = args[0], args[1:]
    root = repo_root(paths[0] if paths else '.')
    _, now, _ = check([pathlib.Path(p) for p in paths] or [root], root)

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
    finally:
        subprocess.run(['git', '-C', str(root), 'worktree', 'remove', '--force',
                        worktree], capture_output=True)
        shutil.rmtree(tmp, ignore_errors=True)

    def key(f):
        return (f[0], f[3], f[2])      # source, target, fragment -- not the line

    was_dead = {key(f) for f in before}
    fresh = [f for f in now if key(f) not in was_dead]
    if not fresh:
        print(f'fragcheck: no new dead heading anchors vs {rev} '
              f'({len(now)} pre-existing, unchanged)')
        return 0
    print(f'fragcheck: {len(fresh)} heading anchor(s) that {rev} resolved are now dead:',
          file=sys.stderr)
    for f in fresh:
        print('  ' + describe(f), file=sys.stderr)
    print('\n          A renamed heading breaks every inbound link to its old anchor,\n'
          '          including links from pages this commit never touched. Either restore\n'
          '          the heading text or retarget the links listed above.', file=sys.stderr)
    return 1


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
    total = miss = 0
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
        bad = [a for a in mine if a not in live]
        total += len(mine)
        miss += len(bad)
        print(f'{"OK  " if not bad else "MISS"} {len(mine):3d} anchors, '
              f'{len(bad)} unmatched  {arg}')
        for a in bad:
            print(f'       computed {a!r} is not among the live ids')
    print(f'\nvalidate: {total - miss}/{total} computed anchors confirmed live')
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
    if mode == 'check':
        return cmd_check(args)
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
