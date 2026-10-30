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
    navcheck.py stale                 only the stale-acknowledgment audit, which
                                      `check` and `new` also run

    Paths are the changed files; the spaces containing them are what gets
    scanned, since adding a page to one space cannot orphan a page in another.
    With no paths, every space is scanned.

ACKNOWLEDGMENT
    A deliberately unlisted page is legitimate -- a `hidden: true` page, or an
    unreleased draft -- so this gate is meant to be acknowledged rather than
    disabled. The acknowledgment is an entry with a reason in the `orphan:`
    section of .claude/hooks/doc-lint-allow.yml, which puts it in the diff where
    review already happens (DOCS-6586, decided on the ticket). Parsed by
    allowlist.py, the single parser for that file.

    DOC_LINT_ALLOW_ORPHAN (space/comma-separated paths, or "all") still works for
    a local one-off run and is unioned with the file; only the environment
    variable takes "all", because in a checked-in file that would be a permanent
    repo-wide disable.

    An acknowledgment that is no longer true FAILS, so the register prunes itself
    at the point someone forgets instead of piling up entries nobody dares
    remove: an entry whose page has since been listed in SUMMARY.md, whose page
    no longer exists, or which names a path that is not a page in any space at
    all. This was the condition on the ticket's go-ahead.


Exit: 0 = no new orphans (or SKIPPED), 1 = new orphans found, 2 = usage error.
Unlike fragcheck.py this needs no worktree -- the base side is read with
git ls-tree and git show, which is why it costs milliseconds rather than seconds.
"""

import os
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import allowlist
except ImportError:  # pragma: no cover - a broken checkout, not a missing tool
    print('navcheck: .claude/hooks/allowlist.py not found. It is checked in '
          'beside this\n          script, so this is a broken checkout, not a '
          'missing tool, and a check\n          that cannot read its '
          'acknowledgments must not report success.', file=sys.stderr)
    sys.exit(2)

SUMMARY = 'SUMMARY.md'
SECTION = 'orphan'

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


def tree_pages(root, space):
    """Pages of `space` in the working tree, as git sees them.

    Enumerated with `git ls-files --cached --others --exclude-standard` rather
    than os.walk, and the distinction is the whole point: the base side of the
    `new` gate is read with git ls-tree, so walking the filesystem here compares
    a set that includes IGNORED and untracked litter against one that cannot.
    Any stray Markdown in a space -- a /graphify GRAPH_REPORT.md, a scratch page,
    an editor backup -- then reports as newly orphaned by whatever PR runs the
    gate next, and it does not reproduce in CI, which runs on a clean checkout.
    `--others --exclude-standard` keeps the case the gate exists for (a page you
    just wrote and have not listed) while dropping what .gitignore covers.
    """
    ok, listing = git(root, 'ls-files', '--cached', '--others',
                      '--exclude-standard', '-z', '--', space + '/')
    if not ok:
        # No git (a tarball, say). Fall back to the filesystem: over-reporting
        # beats silently checking nothing.
        pages = set()
        for dirpath, dirnames, filenames in os.walk(pathlib.Path(root) / space):
            dirnames[:] = [d for d in dirnames if d != '.gitbook']
            for fn in filenames:
                rel = os.path.relpath(os.path.join(dirpath, fn),
                                      root).replace(os.sep, '/')
                if is_page(rel, space):
                    pages.add(rel)
        return pages
    # NUL-delimited, so a path containing a space or a newline cannot split.
    return {ln for ln in listing.split('\0') if is_page(ln, space)}


def orphans_now(root, space):
    """(orphans, pages examined) for `space` in the working tree.

    The page count is returned rather than derived again by the caller because
    navcheck-pr.yml asserts on it: "scanned 9,468 pages, none newly orphaned"
    and "scanned nothing at all" are otherwise the same exit code, so a wrong
    working directory or an empty space list would leave the gate permanently
    and silently green. Same assertion shape as includecheck.sh's include count.
    """
    sm = pathlib.Path(root) / space / SUMMARY
    if not sm.is_file():
        return set(), 0
    refs = parse_refs(sm.read_text(encoding='utf-8', errors='replace'), space)
    pages = tree_pages(root, space)
    return pages - refs, len(pages)


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


def entries(root):
    """The `orphan:` acknowledgments, or a hard error if the register is broken.

    A malformed register is exit 2, never an empty one: reading it as empty
    would fail a PR that HAD acknowledged its finding correctly, and the author
    would have a valid-looking entry in the diff and a red gate with no
    explanation.
    """
    try:
        return allowlist.load(root)[SECTION]
    except allowlist.AllowlistError as exc:
        print(f'navcheck: {allowlist.allowlist_path(root)} is malformed — {exc}',
              file=sys.stderr)
        print("          Fix the entry; the accepted shape is in allowlist.py's "
              'header. A\n          malformed register is a hard error rather '
              'than an empty one, so an\n          acknowledgment can never be '
              'silently lost.', file=sys.stderr)
        raise SystemExit(2)


def allowed(root):
    """Paths exempt from the orphan gate, and whether the whole gate is off.

    The union of the checked-in register and DOC_LINT_ALLOW_ORPHAN. Only the
    environment variable can say "all" -- see allowlist.py's header.
    """
    env = {t for t in re.split(r'[\s,]+', os.environ.get('DOC_LINT_ALLOW_ORPHAN', '')) if t}
    return ({e['path'] for e in entries(root)} | (env - {'all'})), ('all' in env)


def stale(root, acks):
    """Acknowledgments that are no longer true, as [(entry, why)].

    Three ways an entry stops applying, all of them the register's own defect
    rather than a finding about a page -- so they are reported whatever the
    file scope of the run is, and whether or not DOC_LINT_ALLOW_ORPHAN=all is
    set.
    """
    out = []
    spaces = set(all_spaces(root))
    for e in acks:
        rel = e['path']
        if not (pathlib.Path(root) / rel).is_file():
            out.append((e, 'no such file'))
            continue
        space = rel.split('/')[0]
        if space not in spaces or not is_page(rel, space):
            out.append((e, 'not a nav-listable page in any space'))
            continue
        sm = pathlib.Path(root) / space / SUMMARY
        if rel in parse_refs(sm.read_text(encoding='utf-8', errors='replace'), space):
            out.append((e, f'now listed in {space}/{SUMMARY}'))
    return out


def report_stale(bad):
    print(f'navcheck: {len(bad)} stale acknowledgment'
          f'{"" if len(bad) == 1 else "s"} in {allowlist.REL_PATH}:',
          file=sys.stderr)
    for e, why in bad:
        print(f'  line {e["line"]}: {e["path"]} — {why}', file=sys.stderr)
    print("\n          An acknowledgment that is no longer true is worse than "
          'none: it\n          exempts a page that nobody has looked at since. '
          'Delete these entries\n          in this PR — the register is meant '
          'to prune itself at the point\n          someone forgets (DOCS-6586).',
          file=sys.stderr)


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
    print(f'\n          Deliberately unlisted? Add an entry with its reason to the\n'
          f'          `{SECTION}:` section of {allowlist.REL_PATH}, so the\n'
          '          acknowledgment is in the diff a reviewer reads (DOCS-6586).',
          file=sys.stderr)
    if len(found) <= HINT_MAX:
        print('          For a local one-off run, DOC_LINT_ALLOW_ORPHAN does the same:\n'
              f'          DOC_LINT_ALLOW_ORPHAN=\'{" ".join(found)}\'', file=sys.stderr)


def audit(root):
    """The stale-acknowledgment pass. Returns 1 if the register needs pruning.

    Run by every mode, because a stale entry belongs to the register rather
    than to any one PR's file set -- and because the alternative, a separate
    audit somebody has to remember, is exactly what Daniel's go-ahead on
    DOCS-6586 asked this not to be.
    """
    bad = stale(root, entries(root))
    if not bad:
        return 0
    report_stale(bad)
    return 1


def cmd_stale(args):
    """The audit on its own, for triage and for a scheduled run."""
    root = repo_root(args[0] if args else '.')
    rc = audit(root)
    if not rc:
        n = len(entries(root))
        print(f'navcheck: {n} orphan acknowledgment(s), none stale')
    return rc


def cmd_check(args):
    root = repo_root(args[0] if args else '.')
    rc = audit(root)
    skip, off = allowed(root)
    if off:
        return rc
    found = []
    pages = 0
    for space in spaces_for(root, args):
        orphans, n = orphans_now(root, space)
        pages += n
        found += sorted(orphans - skip)
    if found:
        report(sorted(found), 'present')
        return 1
    print(f'navcheck: no orphaned pages ({pages} page(s) scanned)')
    return rc


def cmd_new(args):
    if not args:
        print('navcheck: `new` needs a revision', file=sys.stderr)
        return 2
    rev, paths = args[0], args[1:]
    root = repo_root(paths[0] if paths else '.')

    rc = audit(root)

    skip, off = allowed(root)
    if off:
        return rc

    # The base side is read out of the object store, so `root` must be the top of the repo
    # that store belongs to. If this tree is NESTED inside an unrelated git repo -- an unpacked
    # tarball dropped into another checkout, say -- then git answers for the OUTER repo, which
    # has never heard of these files: `orphans_at` comes back empty, "existed at the base" is
    # false for every page, and every long-unlisted page is reported as NEWLY orphaned. The
    # history-awareness that keeps the 219-page backlog out of the way collapses, silently and
    # in the false-positive direction. A SKIP is the honest answer -- with no usable base
    # revision the gate cannot run, and a check that cannot run must not report findings
    # either. `check` is unaffected: it is absolute, and reads only the working tree.
    ok, top = git(root, 'rev-parse', '--show-toplevel')
    if ok and pathlib.Path(top.strip()).resolve() != pathlib.Path(root).resolve():
        print(f'navcheck: {root} is not the top of its git repository '
              f'({top.strip()} is) — SKIPPED', file=sys.stderr)
        return rc

    ok, _ = git(root, 'rev-parse', '--verify', '-q', rev + '^{commit}')
    if not ok:
        print(f'navcheck: base revision {rev!r} not found — SKIPPED', file=sys.stderr)
        return rc

    fresh, pre, pages, spaces = [], 0, 0, 0
    for space in spaces_for(root, paths):
        now, n = orphans_now(root, space)
        now -= skip
        pages += n
        spaces += 1
        before = orphans_at(root, rev, space)
        pre += len(now & before)
        fresh += sorted(now - before)

    if fresh:
        report(sorted(fresh), 'added or de-listed')
        return 1

    print(f'navcheck: no newly orphaned pages vs {rev} '
          f'({pre} pre-existing, unchanged; '
          f'{pages} page(s) scanned in {spaces} space(s))')
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
    print(f'navcheck: unknown mode {mode!r} (expected `check`, `new` or `stale`)',
          file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
