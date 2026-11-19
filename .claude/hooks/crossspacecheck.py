#!/usr/bin/env python3
"""crossspacecheck.py — fails a relative link that leaves its own GitBook space.

WHY THIS EXISTS
    Each top-level directory with a SUMMARY.md is a separate GitBook space, and a
    link from one space to another is written as a space link, `{alias}/path`,
    which addresses the target by its published path (dev-docs/link-aliases.md).
    A relative path that climbs out of its own space, like
    `../../../../server/reference/...`, resolves fine on disk, so lychee passes
    it, and GitBook resolves it when the linking page syncs, so it even renders.
    But it addresses the target by its repo file path, so it strands silently
    when that file moves -- which DOCS-7069 does to hundreds of files -- and
    breaks on the linking page's next sync (DOCS-7156). Found 63 of them on
    2026-11-19, 55 in MaxScale pages imported from the MaxScale source.

    includecheck.sh already fails a relative `{% include %}` that crosses a space
    boundary. This is the same rule for links.

WHAT IS CHECKED
    In every page of every space: inline Markdown links `[text](target)`,
    reference definitions `[label]: target`, and `href="..."`, `src="..."`, and
    `url="..."` attributes, which covers HTML links and images and content-ref
    blocks. A target is relative when it has no scheme and does not start with
    `/`, `#`, or `{` (an alias). It crosses when, resolved against the page's
    folder, its first path component is not the page's own space.

    Fenced code blocks and inline code spans are skipped: about-links.md shows a
    cross-space relative link as an example of what not to write.

WHY IT IS HISTORY-AWARE
    main still carries the MaxScale links, which have to be fixed in the MaxScale
    source too, or the next docs import brings them back. `new <rev>` reports
    only a cross-space link that the same file did not already have at <rev>, so
    re-importing the existing ones passes while a new one fails. A moved or new
    file has nothing at <rev>, so all of its cross-space links count as new.

    There is no acknowledgment register: a cross-space relative link is never
    the right way to write a link (decided on DOCS-7156), so, like a dead
    include, it has no legitimate exceptions.

MODES
    crossspacecheck.py check [path ...]      every cross-space link -- for triage
    crossspacecheck.py new <rev> [path ...]  only links new since <rev> -- the gate

    Paths are files or directories, repo-relative. With no paths, every page in
    every space is scanned.

Exit: 0 = none found (or SKIPPED), 1 = found, 2 = usage error.
"""

import collections
import os
import pathlib
import re
import subprocess
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import fragcheck  # for the alias table, read from expand-gitbook-aliases.yml
except ImportError:  # pragma: no cover - only the alias hint needs it
    fragcheck = None

SUMMARY = 'SUMMARY.md'

INLINE = re.compile(r'\]\(\s*<?([^)\s>]+)')
REFDEF = re.compile(r'^\s{0,3}\[[^\]]+\]:\s*<?([^\s>]+)')
ATTR = re.compile(r'\b(?:href|src|url)\s*=\s*"([^"]*)"')
FENCE = re.compile(r'^\s*(```|~~~)')
CODE_SPAN = re.compile(r'(`+)(?:(?!\1).)+?\1')
SCHEME = re.compile(r'^[A-Za-z][A-Za-z0-9+.-]*:')


def repo_root(start='.'):
    d = pathlib.Path(start).resolve()
    for cand in [d] + list(d.parents):
        if (cand / '.codespellignore').is_file() or (cand / '.git').exists():
            return cand
    return d


def git(root, *args):
    p = subprocess.run(['git', '-C', str(root)] + list(args),
                       capture_output=True, text=True)
    return p.returncode == 0, p.stdout


def all_spaces(root):
    return sorted(d.name for d in pathlib.Path(root).iterdir()
                  if d.is_dir() and not d.name.startswith('.')
                  and (d / SUMMARY).is_file())


def targets(text):
    """(line number, raw target) for every link target outside code."""
    infence = False
    for n, line in enumerate((text or '').split('\n'), 1):
        if FENCE.match(line):
            infence = not infence
            continue
        if infence:
            continue
        line = CODE_SPAN.sub('', line)
        for rx in (INLINE, REFDEF, ATTR):
            for m in rx.finditer(line):
                yield n, m.group(1)


def crossings(rel, text):
    """[(line, raw target, target space)] for the cross-space links in a page.

    `rel` is the page's repo-relative posix path; its first component is its space.
    """
    space = rel.split('/')[0]
    out = []
    for n, raw in targets(text):
        path = raw.split('#')[0].split('?')[0]
        if not path or SCHEME.match(path) or path.startswith(('/', '{', '%7B')):
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(rel),
                                                 urllib.parse.unquote(path)))
        top = resolved.replace(os.sep, '/').split('/')[0]
        if top != space:
            out.append((n, raw, top))
    return out


def pages(root, paths):
    """Repo-relative .md pages in spaces, under `paths` (every space when empty)."""
    spaces = set(all_spaces(root))
    found = set()
    roots = paths or sorted(spaces)
    for p in roots:
        full = pathlib.Path(root) / p
        try:
            rel = full.resolve().relative_to(pathlib.Path(root).resolve()).as_posix()
        except ValueError:
            continue
        if rel.split('/')[0] not in spaces:
            continue
        if full.is_file() and rel.endswith('.md'):
            found.add(rel)
        elif full.is_dir():
            for f in full.rglob('*.md'):
                found.add(f.resolve().relative_to(pathlib.Path(root).resolve()).as_posix())
    return sorted(found)


def alias_for(root, space):
    """The alias to use for links into `space`, or None if it has none yet."""
    if fragcheck is None:
        return None
    ids = {sid for sid, d in fragcheck.SPACE_DIRS.items() if d == space}
    names = [a for a, target in fragcheck.aliases(pathlib.Path(root)).items()
             if target in ids]
    if not names:
        return None
    return space if space in names else names[0]


def report(root, found, label):
    print(f'crossspacecheck: {len(found)} relative link(s) {label} that leave their '
          'own space:', file=sys.stderr)
    for rel, n, raw, top in found:
        alias = alias_for(root, top)
        if alias:
            use = f'use {{{alias}}}/<published path>'
        elif fragcheck is None:
            use = 'use its space link, {alias}/<published path>'
        else:
            use = f'{top}/ has no alias yet'
        print(f'  {rel}:{n}: {raw}\n      points into {top}/ -- {use}', file=sys.stderr)
    print('\n          Each top-level folder is a separate GitBook space. A relative path\n'
          '          into another one addresses the target by its file path, so it breaks\n'
          '          when that file moves (DOCS-7156). Write a space link instead, with the\n'
          '          target\'s published path, which can differ from its file path\n'
          '          (DOCS-7069): see dev-docs/link-aliases.md.', file=sys.stderr)


def cmd_check(args):
    root = repo_root()
    scanned = pages(root, args)
    found = []
    for rel in scanned:
        text = (pathlib.Path(root) / rel).read_text(encoding='utf-8', errors='replace')
        found += [(rel, n, raw, top) for n, raw, top in crossings(rel, text)]
    if found:
        report(root, found, 'present')
        return 1
    print(f'crossspacecheck: no relative link leaves its own space '
          f'({len(scanned)} page(s) scanned)')
    return 0


def cmd_new(args):
    if not args:
        print('crossspacecheck: `new` needs a revision', file=sys.stderr)
        return 2
    rev, paths = args[0], args[1:]
    root = repo_root()

    # Same guards as navcheck.py's `new`: with no usable base revision every
    # existing link would read as new, so the honest answer is a SKIP.
    ok, top = git(root, 'rev-parse', '--show-toplevel')
    if ok and pathlib.Path(top.strip()).resolve() != pathlib.Path(root).resolve():
        print(f'crossspacecheck: {root} is not the top of its git repository '
              f'({top.strip()} is) — SKIPPED', file=sys.stderr)
        return 0
    ok, _ = git(root, 'rev-parse', '--verify', '-q', rev + '^{commit}')
    if not ok:
        print(f'crossspacecheck: base revision {rev!r} not found — SKIPPED', file=sys.stderr)
        return 0

    scanned = pages(root, paths)
    fresh, pre = [], 0
    for rel in scanned:
        text = (pathlib.Path(root) / rel).read_text(encoding='utf-8', errors='replace')
        now = crossings(rel, text)
        if not now:
            continue
        # Only a page with a crossing now is read at the base, so a whole-tree run
        # costs one `git show` per offending page rather than one per page.
        ok, old = git(root, 'show', f'{rev}:{rel}')
        before = collections.Counter(raw for _, raw, _ in crossings(rel, old if ok else ''))
        for n, raw, tgt in now:
            if before[raw] > 0:
                before[raw] -= 1
                pre += 1
            else:
                fresh.append((rel, n, raw, tgt))
    if fresh:
        report(root, fresh, 'added')
        return 1
    print(f'crossspacecheck: no new relative links leave their space vs {rev} '
          f'({pre} pre-existing, unchanged; {len(scanned)} page(s) scanned)')
    return 0


def main(argv):
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(__doc__.rstrip(), file=sys.stderr)
        return 2
    mode, args = argv[1], argv[2:]
    if mode == 'check':
        return cmd_check(args)
    if mode == 'new':
        return cmd_new(args)
    print(f'crossspacecheck: unknown mode {mode!r} (expected `check` or `new`)',
          file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
