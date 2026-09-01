#!/usr/bin/env python3
"""navcheck.py — orphaned-page (nav coverage) checker for the GitBook spaces.

WHY THIS EXISTS
    GitBook publishes only the pages listed in a space's SUMMARY.md. A page file
    with no nav entry never renders -- and no other gate in this repo can see
    that. The file is valid Markdown, so codespell passes; its links resolve, so
    lychee passes; it is simply never built. There is no failing signal anywhere,
    and the only symptom is a reader reporting a missing page.

    DOCS-6566 is the case this exists for. dde0fb263 added four post-download
    pages (Server 12.3.3, 11.8.9, 11.4.13, 10.11.19) and bumped their
    most-recent-*.md includes, but never touched platform/SUMMARY.md. All four
    sat unpublished for eight days until a reader noticed. Every gate was green
    the whole time. Notably, every OTHER commit that ever added a post-download
    page updated SUMMARY.md in the same commit -- so this is not a broken
    generator to fix, it is a hand-edit step with no backstop, which is exactly
    what a linter is for.

WHY IT IS HISTORY-AWARE  (the same trap fragcheck.py documents)
    main carries 219 pre-existing orphans -- 191 in server alone, measured over
    the 11 spaces that have a SUMMARY.md (9,468 .md files vs 9,238 nav refs).
    An absolute check would therefore fail every unrelated PR on breakage it did
    not introduce, which is precisely why the heading-anchor gate diffs against a
    base revision rather than reporting its ~1,272 pre-existing dead anchors.
    `new` reports only what changed, so the backlog stays out of the way while a
    newly orphaned page still fails.

    A page is NEWLY orphaned when it is unreferenced now AND either did not exist
    at the base revision, or was referenced there. That covers both directions:
        * a page added with no nav entry          -- the DOCS-6566 case
        * a nav entry deleted, page file surviving -- the quieter one, since the
          page keeps working locally and only vanishes from the built site

WHAT IS NOT A PAGE
    * the space's own SUMMARY.md (it is the nav, not a page in it)
    * anything under .gitbook/ -- includes and reusable snippets are pulled into
      pages by {% include %} and are never nav-listed (117 such files today)
    A directory only counts as a space if it holds a SUMMARY.md, which is what
    keeps dev-docs/, .claude/ and help-tables/ out without naming them.

    Cross-space SUMMARY entries are absolute app.gitbook.com URLs (6 today) and
    are skipped: they point into another space, so they can never mark a local
    file as referenced.

MODES
    navcheck.py check [path ...]      every orphan under each path -- for triage
    navcheck.py new <rev> [path ...]  only pages newly orphaned vs <rev> -- the gate

    Paths are the changed files; the spaces containing them are what gets
    scanned, since adding a page to one space cannot orphan a page in another.
    With no paths, every space is scanned.

ESCAPE HATCH
    DOC_LINT_ALLOW_ORPHAN  space/comma-separated repo-relative paths to exempt,
                           or "all". A deliberately unlisted page is legitimate;
                           name it here and say why in the commit message.

Exit: 0 = no new orphans (or SKIPPED), 1 = new orphans found, 2 = usage error.
Unlike fragcheck.py this needs no worktree -- the base side is read with
git ls-tree and git show, which is why it costs milliseconds rather than seconds.
"""

import os
import pathlib
import re
import subprocess
import sys

SUMMARY = 'SUMMARY.md'

# Markdown link targets in SUMMARY.md. GitBook writes plain relative paths here;
# the only exceptions on main are 6 absolute cross-space URLs, filtered below.
LINK_RE = re.compile(r'\]\(\s*<?([^)>\s]+?)>?\s*\)')


def repo_root(start='.'):
    """Nearest ancestor that looks like this repo."""
    d = pathlib.Path(start).resolve()
    for cand in [d] + list(d.parents):
        if (cand / '.codespellignore').is_file() or (cand / '.git').exists():
            return cand
    return d


def git(root, *args):
    """Run git, returning (ok, stdout)."""
    p = subprocess.run(['git', '-C', str(root)] + list(args),
                       capture_output=True, text=True)
    return p.returncode == 0, p.stdout


def is_page(rel, space):
    """True if `rel` (repo-relative, posix) is a nav-listable page of `space`."""
    if not rel.endswith('.md'):
        return False
    parts = rel.split('/')
    if parts[0] != space:
        return False
    if os.path.basename(rel) == SUMMARY:
        return False
    return '.gitbook' not in parts


def parse_refs(text, space):
    """Repo-relative page paths that a space's SUMMARY.md links to."""
    refs = set()
    for target in LINK_RE.findall(text or ''):
        target = target.split('#')[0].strip()
        if not target or target.startswith(('http://', 'https://', 'mailto:')):
            continue
        if not target.endswith('.md'):
            continue
        # SUMMARY.md sits at the space root, so targets resolve against it.
        refs.add(os.path.normpath(os.path.join(space, target)).replace(os.sep, '/'))
    return refs


def all_spaces(root):
    return sorted(d.name for d in pathlib.Path(root).iterdir()
                  if d.is_dir() and not d.name.startswith('.')
                  and (d / SUMMARY).is_file())


def spaces_for(root, paths):
    """Spaces touched by `paths`; every space when `paths` is empty."""
    known = all_spaces(root)
    if not paths:
        return known
    hit = set()
    for p in paths:
        try:
            rel = pathlib.Path(p).resolve().relative_to(root).as_posix()
        except ValueError:
            rel = str(p).lstrip('./')
        head = rel.split('/')[0]
        if head in known:
            hit.add(head)
    return sorted(hit)


def orphans_now(root, space):
    """Pages of `space` in the working tree with no SUMMARY.md entry."""
    sm = pathlib.Path(root) / space / SUMMARY
    if not sm.is_file():
        return set()
    refs = parse_refs(sm.read_text(encoding='utf-8', errors='replace'), space)
    pages = set()
    for dirpath, dirnames, filenames in os.walk(pathlib.Path(root) / space):
        dirnames[:] = [d for d in dirnames if d != '.gitbook']
        for fn in filenames:
            rel = os.path.relpath(os.path.join(dirpath, fn), root).replace(os.sep, '/')
            if is_page(rel, space):
                pages.add(rel)
    return pages - refs


def orphans_at(root, rev, space):
    """Same, as of `rev`. Read from the object store -- no worktree needed."""
    ok, listing = git(root, 'ls-tree', '-r', '--name-only', rev, '--', space + '/')
    if not ok:
        return set()
    pages = {ln for ln in listing.splitlines() if is_page(ln, space)}
    ok, text = git(root, 'show', f'{rev}:{space}/{SUMMARY}')
    if not ok:
        # The space did not exist at rev, so nothing there was orphaned.
        return set()
    return pages - parse_refs(text, space)


def allowed():
    raw = os.environ.get('DOC_LINT_ALLOW_ORPHAN', '')
    return {t for t in re.split(r'[\s,]+', raw) if t}


# Above this many findings the copy-paste exemption line is longer than the
# report it follows, so it stops being an offer and becomes noise. `check` on
# main hits 219; the gate path realistically produces one batch of a few.
HINT_MAX = 10


def report(found, label):
    print(f'navcheck: {len(found)} page(s) {label} but not listed in SUMMARY.md:',
          file=sys.stderr)
    for rel in found:
        print(f'  {rel}', file=sys.stderr)
    print('\n          GitBook publishes only what SUMMARY.md lists, so these files\n'
          '          will not appear on the live site at all -- no other check can\n'
          '          see this, because the markup is valid and the links resolve\n'
          '          (DOCS-6566). Add a nav entry in the space\'s SUMMARY.md, placed\n'
          '          where a reader would look for it.', file=sys.stderr)
    if len(found) <= HINT_MAX:
        print('          Deliberately unlisted? Re-run with\n'
              f'          DOC_LINT_ALLOW_ORPHAN=\'{" ".join(found)}\'\n'
              '          and say why in the commit message.', file=sys.stderr)
    else:
        print('          Deliberately unlisted? Name those paths in\n'
              '          DOC_LINT_ALLOW_ORPHAN and say why in the commit message.',
              file=sys.stderr)


def cmd_check(args):
    root = repo_root(args[0] if args else '.')
    skip = allowed()
    if 'all' in skip:
        return 0
    found = []
    for space in spaces_for(root, args):
        found += sorted(orphans_now(root, space) - skip)
    if found:
        report(sorted(found), 'present')
        return 1
    print('navcheck: no orphaned pages')
    return 0


def cmd_new(args):
    if not args:
        print('navcheck: `new` needs a revision', file=sys.stderr)
        return 2
    rev, paths = args[0], args[1:]
    root = repo_root(paths[0] if paths else '.')

    skip = allowed()
    if 'all' in skip:
        return 0

    ok, _ = git(root, 'rev-parse', '--verify', '-q', rev + '^{commit}')
    if not ok:
        print(f'navcheck: base revision {rev!r} not found — SKIPPED', file=sys.stderr)
        return 0

    fresh, pre = [], 0
    for space in spaces_for(root, paths):
        now = orphans_now(root, space) - skip
        before = orphans_at(root, rev, space)
        pre += len(now & before)
        fresh += sorted(now - before)

    if fresh:
        report(sorted(fresh), 'added or de-listed')
        return 1

    print(f'navcheck: no newly orphaned pages vs {rev} '
          f'({pre} pre-existing, unchanged)')
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
    print(f'navcheck: unknown mode {mode!r} (expected `check` or `new`)', file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
