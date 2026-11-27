#!/usr/bin/env python3
"""urlcheck.py — published-URL vs file-path checker for the GitBook spaces.

WHY THIS EXISTS
    A page's file path in the repo should match its published URL, and no URL
    should have a `readme` segment (DOCS-7069). GitBook does not enforce either.
    It builds a page's URL from SUMMARY.md alone -- the nesting of the page's
    entry, any `## Group` heading above it, and its file name -- so a SUMMARY.md
    edit, a new group heading, or a file filed in a different folder from its
    nav position all publish fine, at a URL nobody can find from the repo.

    DOCS-7069 found 618 pages like that on 2026-11-04, across 17 spaces, and the
    first 12 of them published under /readme/ paths. Each fix after the fact
    costs a move, a round of link repointing, and sometimes redirects. This gate
    catches the next one in the PR that introduces it.

HOW THE URL IS DERIVED
    Proved against the GitBook API on 2026-11-19: for 10,724 of the 10,727
    synced pages in all 17 spaces, the path derived here is the path GitBook
    publishes. The other 3 are space home pages (see the last rule).

    * A page's slug is its file name without `.md`, lowercased. A README.md
      takes its folder's name instead.
    * A nested entry's URL is its parent entry's URL plus its own slug.
    * A `## Group` heading adds the slugified group title in front of the pages
      under it, until the next group heading, or a `***` divider, which ends
      the group. The pages after a divider sit at the space root.
    * An entry with a `#fragment` is a link to the page, not a place for it.
    * A page listed more than once has one place: the entry with children if
      there is one, otherwise the first.
    * A space's first entry is its home page. It serves at the space root
      whatever its slug, so it is never checked. Pages nested under it publish
      under its slug, which is `readme` for a README.md, so they are flagged.

WHAT IS A MISMATCH
    A page whose derived URL differs from its file path -- space-relative,
    without `.md`, and with README.md standing for its folder -- or whose URL
    has a `readme` segment. Case counts: GitBook lowercases the slug, so
    Instrumentation_interface.md publishes as instrumentation_interface and is
    flagged. The usual fix is to move the file to match the URL, which changes
    nothing for readers. Changing SUMMARY.md instead changes the URL, and the
    old one then needs a redirect.

WHAT IS NOT CHECKED
    The GridGain docs: the GridGain, GridGain 8, and GridGain 9 spaces, the
    GridGain release notes and clients in Release Notes and Connectors, and
    Control Center in Tools. Those pages belong to the GridGain docs team, and
    452 of them mismatched on 2026-11-19, mostly by design: each release-notes
    file sits in a per-version folder while the nav files it under its series,
    so every new GridGain release would fail the gate. They are left out until
    that team decides how to file them (DOCS-7069), so drop a prefix from
    NOT_CHECKED once its pages match.

WHY IT IS HISTORY-AWARE
    main carried 618 mismatches when DOCS-7069 was filed, most of them in spaces
    other teams own, so an absolute check would fail every unrelated PR. `new`
    reports a page only when it mismatches now AND did not at the base revision:
    a page added or moved to a mismatched place, or re-nested in SUMMARY.md so
    that its URL no longer matches. Same shape as navcheck.py, whose helpers this
    reuses.

MODES
    urlcheck.py check [path ...]      every mismatch under each path -- for triage
    urlcheck.py new <rev> [path ...]  only pages newly mismatched vs <rev> -- the gate
    urlcheck.py stale                 only the stale-acknowledgment audit, which
                                      `check` and `new` also run

    Paths are the changed files; the spaces containing them are what gets
    scanned. With no paths, every space is scanned.

ACKNOWLEDGMENT
    A page synced from another repo can only be fixed there, so this gate is
    acknowledged rather than disabled: an entry with a reason in the `url-path:`
    section of .claude/hooks/doc-lint-allow.yml. DOC_LINT_ALLOW_URL_PATH (paths,
    or "all") works for a local one-off run and is unioned with the file.

    An acknowledgment that is no longer true FAILS: an entry whose page no
    longer exists, is no longer in its space's SUMMARY.md, or now matches its
    URL. So the register prunes itself, as navcheck's `orphan:` section does.

Exit: 0 = no new mismatches (or SKIPPED), 1 = new mismatches found, 2 = usage error.
"""

import os
import pathlib
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import allowlist
    import navcheck
except ImportError:  # pragma: no cover - a broken checkout, not a missing tool
    print('urlcheck: .claude/hooks/allowlist.py or navcheck.py not found. Both '
          'are checked in\n          beside this script, so this is a broken '
          'checkout, not a missing tool.', file=sys.stderr)
    sys.exit(2)

SUMMARY = 'SUMMARY.md'
SECTION = 'url-path'

# Repo-relative path prefixes the gate skips; see WHAT IS NOT CHECKED above.
NOT_CHECKED = (
    'gridgain/',
    'gridgain-8/',
    'gridgain-9/',
    'connectors/gridgain-8/',
    'connectors/gridgain-9/',
    'release-notes/gridgain-8/',
    'release-notes/gridgain-9/',
    'tools/enterprise/control-center/',
)

ENTRY_RE = re.compile(r'^(\s*)[*+-] \[.*\]\(\s*<?([^)>\s]+?)>?\s*\)\s*$')
GROUP_RE = re.compile(r'^##+ +(.*?)\s*$')
DIVIDER_RE = re.compile(r'^\s*([*_-])(\s*\1){2,}\s*$')


def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')


def page_slug(target):
    base = os.path.basename(target)
    if base.lower() == 'readme.md':
        folder = os.path.basename(os.path.dirname(target))
        return folder.lower() if folder else 'readme'
    return base[:-len('.md')].lower()


def derive(text):
    """(home, {target: (url, has_children)}) for a SUMMARY.md text.

    Targets are space-relative, normalized. `home` is the first entry's target.
    """
    places = []         # [target or None for a link, url, has_children]
    stack = []          # [(indent, url, index into places)]
    group = ''
    for line in (text or '').split('\n'):
        g = GROUP_RE.match(line)
        if g:
            group, stack = slugify(g.group(1)), []
            continue
        if DIVIDER_RE.match(line):
            group, stack = '', []
            continue
        m = ENTRY_RE.match(line)
        if not m:
            continue
        indent, raw = len(m.group(1).expandtabs(4)), m.group(2)
        target = raw.split('#')[0]
        if target.startswith(('http://', 'https://')) or not target.endswith('.md'):
            continue
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if stack:
            places[stack[-1][2]][2] = True
        parent = stack[-1][1] if stack else group
        url = (parent + '/' if parent else '') + page_slug(target)
        stack.append((indent, url, len(places)))
        places.append([None if '#' in raw else os.path.normpath(target), url, False])

    pages, home = {}, None
    for target, url, kids in places:
        if target is None:
            continue
        if home is None:
            home = target
        if target not in pages or (kids and not pages[target][1]):
            pages[target] = (url, kids)
    return home, pages


def file_url(target):
    """The URL a file's path implies: no `.md`, README.md standing for its folder."""
    stem = target[:-len('.md')]
    if os.path.basename(target).lower() == 'readme.md':
        stem = os.path.dirname(target)
    return stem


def mismatches(text, space, exists=None):
    """{repo-relative file: (url, has_children)} for the pages that mismatch."""
    home, pages = derive(text)
    out = {}
    for target, (url, kids) in pages.items():
        if target == home:
            continue
        rel = f'{space}/{target}'
        if rel.startswith(NOT_CHECKED):
            continue
        if exists is not None and not exists(rel):
            continue
        if url != file_url(target) or 'readme' in url.split('/'):
            out[rel] = (url, kids)
    return out


def summary_now(root, space):
    sm = pathlib.Path(root) / space / SUMMARY
    return sm.read_text(encoding='utf-8', errors='replace') if sm.is_file() else None


def mismatches_now(root, space):
    """(mismatches, pages examined) for `space` in the working tree."""
    text = summary_now(root, space)
    if text is None:
        return {}, 0
    return (mismatches(text, space, lambda rel: (pathlib.Path(root) / rel).is_file()),
            len(derive(text)[1]))


def mismatches_at(root, rev, space):
    """The files that mismatched at `rev`. Read from the object store."""
    ok, text = navcheck.git(root, 'show', f'{rev}:{space}/{SUMMARY}')
    return set(mismatches(text, space)) if ok else set()


def entries(root):
    try:
        return allowlist.load(root)[SECTION]
    except allowlist.AllowlistError as exc:
        print(f'urlcheck: {allowlist.allowlist_path(root)} is malformed — {exc}',
              file=sys.stderr)
        raise SystemExit(2)


def allowed(root):
    """Paths exempt from the gate, and whether the whole gate is off."""
    env = {t for t in re.split(r'[\s,]+', os.environ.get('DOC_LINT_ALLOW_URL_PATH', ''))
           if t}
    return ({e['path'] for e in entries(root)} | (env - {'all'})), ('all' in env)


def stale(root, acks):
    """Acknowledgments that are no longer true, as [(entry, why)]."""
    out = []
    spaces = set(navcheck.all_spaces(root))
    for e in acks:
        rel = e['path']
        space = rel.split('/')[0]
        if not (pathlib.Path(root) / rel).is_file():
            out.append((e, 'no such file'))
        elif space not in spaces:
            out.append((e, 'not a page in any space'))
        elif rel.startswith(NOT_CHECKED):
            out.append((e, 'a GridGain page, which this check skips'))
        elif os.path.normpath(rel[len(space) + 1:]) not in derive(summary_now(root, space))[1]:
            out.append((e, f'not listed in {space}/{SUMMARY}'))
        elif rel not in mismatches_now(root, space)[0]:
            out.append((e, 'now matches its URL'))
    return out


def audit(root):
    bad = stale(root, entries(root))
    if not bad:
        return 0
    print(f'urlcheck: {len(bad)} stale acknowledgment{"" if len(bad) == 1 else "s"} '
          f'in {allowlist.REL_PATH}:', file=sys.stderr)
    for e, why in bad:
        print(f'  line {e["line"]}: {e["path"]} — {why}', file=sys.stderr)
    print('\n          Delete these entries in this PR -- an acknowledgment that is no\n'
          '          longer true exempts a page nobody has looked at since.',
          file=sys.stderr)
    return 1


def report(found, label):
    print(f'urlcheck: {len(found)} page(s) {label} whose published URL does not '
          'match the file path:', file=sys.stderr)
    for rel, (url, kids) in sorted(found.items()):
        space = rel.split('/')[0]
        move = f'{space}/{url}/README.md' if kids else f'{space}/{url}.md'
        print(f'  {rel}\n      publishes at /{space}/{url}\n      would match as {move}',
              file=sys.stderr)
    print('\n          GitBook builds the URL from SUMMARY.md: the entry\'s nesting, any\n'
          '          `## Group` heading above it, and the lowercased file name (a\n'
          '          README.md takes its folder\'s name). Either move the file to the\n'
          '          path shown, which changes nothing for readers, or change the\n'
          '          SUMMARY.md entry so the URL follows the file. A URL with a\n'
          '          `readme` segment means the page is nested under its space\'s\n'
          '          home page (DOCS-7069).', file=sys.stderr)
    print(f'\n          Can only be fixed upstream (synced content)? Add an entry with\n'
          f'          its reason to the `{SECTION}:` section of {allowlist.REL_PATH}.',
          file=sys.stderr)


def cmd_stale(args):
    root = navcheck.repo_root(args[0] if args else '.')
    rc = audit(root)
    if not rc:
        print(f'urlcheck: {len(entries(root))} url-path acknowledgment(s), none stale')
    return rc


def cmd_check(args):
    root = navcheck.repo_root(args[0] if args else '.')
    rc = audit(root)
    skip, off = allowed(root)
    if off:
        return rc
    found, pages = {}, 0
    for space in navcheck.spaces_for(root, args):
        now, n = mismatches_now(root, space)
        pages += n
        found.update({k: v for k, v in now.items() if k not in skip})
    if found:
        report(found, 'present')
        return 1
    print(f'urlcheck: every published URL matches its file path ({pages} page(s) scanned; '
          'GridGain paths not checked)')
    return rc


def cmd_new(args):
    if not args:
        print('urlcheck: `new` needs a revision', file=sys.stderr)
        return 2
    rev, paths = args[0], args[1:]
    root = navcheck.repo_root(paths[0] if paths else '.')
    rc = audit(root)
    skip, off = allowed(root)
    if off:
        return rc

    # Same guards as navcheck.py's `new`, for the same reasons: with no usable base revision the
    # history-awareness collapses and every pre-existing mismatch reads as new.
    ok, top = navcheck.git(root, 'rev-parse', '--show-toplevel')
    if ok and pathlib.Path(top.strip()).resolve() != pathlib.Path(root).resolve():
        print(f'urlcheck: {root} is not the top of its git repository '
              f'({top.strip()} is) — SKIPPED', file=sys.stderr)
        return rc
    ok, _ = navcheck.git(root, 'rev-parse', '--verify', '-q', rev + '^{commit}')
    if not ok:
        print(f'urlcheck: base revision {rev!r} not found — SKIPPED', file=sys.stderr)
        return rc

    fresh, pre, pages, spaces = {}, 0, 0, 0
    for space in navcheck.spaces_for(root, paths):
        now, n = mismatches_now(root, space)
        now = {k: v for k, v in now.items() if k not in skip}
        pages += n
        spaces += 1
        before = mismatches_at(root, rev, space)
        pre += len(set(now) & before)
        fresh.update({k: v for k, v in now.items() if k not in before})

    if fresh:
        report(fresh, 'added, moved, or re-nested')
        return 1
    print(f'urlcheck: no newly mismatched URLs vs {rev} '
          f'({pre} pre-existing, unchanged; '
          f'{pages} page(s) scanned in {spaces} space(s); GridGain paths not checked)')
    return rc


def main(argv):
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(__doc__.rstrip(), file=sys.stderr)
        return 2
    mode, args = argv[1], argv[2:]
    if mode == 'check':
        return cmd_check(args)
    if mode == 'new':
        return cmd_new(args)
    if mode == 'stale':
        return cmd_stale(args)
    print(f'urlcheck: unknown mode {mode!r} (expected `check`, `new` or `stale`)',
          file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
