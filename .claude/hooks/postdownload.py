#!/usr/bin/env python3
"""postdownload.py — the Post Download page map, and the no-standalone register.

WHY THIS EXISTS
    A connector or Server release round touches three places, and until
    DOCS-6408 only the first was enforced by anything:

      1. release-notes/<product>/<series>/<version>.md  + changelog, the
         all-releases row, and the SUMMARY.md entry
      2. platform/post-download/<stem>-<version>.md     + its SUMMARY.md entry
      3. platform/.gitbook/includes/most-recent-<x>.md  naming the newest
         version  (gated since DOCS-6734 by versioncheck.py)

    Two consecutive rounds shipped release notes with no platform pages at all
    and nothing caught either: Connector/J 2.7.15/3.3.6/3.4.4/3.5.10 (DOCS-6376,
    fixed weeks later in DOCS-6406) and Connector/Node.js 3.2.5/3.3.4/3.4.7/
    3.5.4 (DOCS-6405, caught by a human in review).

    This module owns the NAMING MAP those checks need, because no two spaces
    agree on a product's name -- `java` becomes `j`, `node.js` stays `node.js`
    in the page stem but becomes `nodejs` in the include, `c++` becomes `cpp` --
    and a second copy of that table is the drift it exists to prevent.

WHAT IT GATES TODAY
    The `no-standalone:` section of the acknowledgment register, in both
    directions, so an exemption cannot outlive the fact it records:

      * an entry naming a page that no longer exists is stale
      * an entry whose release HAS a Post Download page is stale -- the whole
        claim of the entry is that there is no download to land on, and once
        the page exists that claim is simply false
      * an entry naming something that is not a release-notes page under a
        product this map knows is rejected, rather than silently exempting
        nothing

    The other direction -- that a newly added release notes page HAS its Post
    Download page -- is `new <rev>` (DOCS-6408). It cannot be run tree-wide: 67
    existing connector releases have no Post Download page, only two of which
    are acknowledged, and the rest are a mix of pages predating the system
    (Connector/J 1.1.x is from 2013) and gaps nobody has triaged. So it reads
    only pages that are absent at <rev>, the way `navcheck.py new` does, and
    requires of each:

      * the Post Download page exists
      * platform/SUMMARY.md links to it
      * or the release is acknowledged in the `no-standalone:` register

    A page counts as new by PATH, so a pure move of released notes looks new
    and needs a register entry if it never had a download page. `hidden: true`
    notes are held to the same rule: a held-back round still ships its
    platform page (DOCS-6405). The `most-recent-<x>` include is not checked
    here; versioncheck.py owns it.

WHY THE EXEMPTION IS A REGISTER ENTRY AND NOT PAGE FRONTMATTER
    Decided on DOCS-6734 after checking both. GitBook's frontmatter set is
    closed -- description, icon, hidden, vars, if, layout -- so a bare
    `standalone: false` key is not something GitBook promises to keep, and the
    sanctioned escape hatch (`vars:`) is used by no page in this repo, so its
    survival across a web-app round-trip is unproven. The web app is already
    known to silently drop content it does not model (GITBOOK-1636 deleted HTML
    comments), and an exemption that can be silently switched off by someone
    editing prose in a browser is worse than no exemption at all.

    .claude/ is not a GitBook space and never syncs, so a register entry cannot
    be touched that way. It also lands in the diff a reviewer already reads,
    which is the argument DOCS-6586 made for the other two sections.

    The prose sentence on the page stays -- it is what tells a READER why there
    is no download link. It is not the signal, because it cannot be one: of the
    67 releases with no Post Download page, two carry such a sentence and they
    are worded differently from each other.

USAGE
    postdownload.py audit          check the no-standalone register (default)
    postdownload.py new <rev> [--advisory] [file ...]
                                   release-notes pages added since <rev> that
                                   lack a Post Download page (the DOCS-6408
                                   gate); files, if given, scope the check.
                                   --advisory only rewords the findings for the
                                   docs team instead of the PR author, for a
                                   fork PR whose contributor cannot be asked to
                                   write platform pages; the exit code is the
                                   same, and the caller decides what it means
    postdownload.py path <file>    print the Post Download page a release-notes
                                   page maps to, or why it maps to none

Exit: 0 = clean (or SKIPPED), 1 = a finding, 2 = a usage error.
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
    print('postdownload: .claude/hooks/allowlist.py not found. It is checked in '
          'beside this\n              script, so this is a broken checkout, not '
          'a missing tool, and a\n              check that cannot read its '
          'acknowledgments must not report success.', file=sys.stderr)
    sys.exit(2)

SECTION = 'no-standalone'
POST_DOWNLOAD = 'platform/post-download'

# release-notes directory -> Post Download page stem, or None for a product that
# has no Post Download pages at all. Proven against the tree on DOCS-6408 (the
# Node.js stem was split across two spellings until #1008 made it uniform at
# 57/57) and extended here with the release-notes include column that
# versioncheck.py pairs on.
#
#   dir under release-notes/     stem under platform/post-download/
PRODUCTS = {
    'connectors/c': 'mariadb-connector-c',
    'connectors/java': 'mariadb-connector-j',
    'connectors/node.js': 'mariadb-connector-node.js',
    'connectors/odbc': 'mariadb-connector-odbc',
    'connectors/python': 'mariadb-connector-python',
    # Not offered for download on the foundation website, so no Post Download
    # pages exist and none should -- the same two versioncheck.py exempts from
    # its platform-include coverage rule.
    'connectors/c++': None,
    'connectors/r2dbc': None,
    # Community Server rounds have Post Download pages too (490 of them), and
    # DOCS-6408 asks for the same gate over them.
    'community-server': 'mariadb-server',
}


def repo_root(start='.'):
    """Nearest ancestor that looks like this repo.

    Spelled the same way as allowlist.py, navcheck.py and fragcheck.py; see the
    note there on why the test suite needs it.
    """
    d = pathlib.Path(start).resolve()
    for cand in [d] + list(d.parents):
        if (cand / '.codespellignore').is_file() or (cand / '.git').exists():
            return cand
    return d


def product_for(rel_path):
    """(dir, stem) for a release-notes page, or None if it is not one.

    Longest prefix wins, so `connectors/c++` is never read as `connectors/c`.
    """
    p = rel_path.replace('\\', '/')
    if not p.startswith('release-notes/'):
        return None
    tail = p[len('release-notes/'):]
    for d in sorted(PRODUCTS, key=len, reverse=True):
        if tail.startswith(d + '/'):
            return d, PRODUCTS[d]
    return None


def post_download_for(rel_path):
    """The Post Download page a release-notes page requires.

    Returns a repo-relative path, or None when the page needs none -- which is
    the case for a product with no Post Download pages, for a changelog, and for
    anything that is not a versioned release page (README.md, all-releases.md).
    DOCS-6408's gate is meant to read this rather than re-deriving it.
    """
    found = product_for(rel_path)
    if found is None:
        return None
    d, stem = found
    if stem is None:
        return None
    page = pathlib.Path(rel_path)
    if page.name == 'README.md' or 'changelogs' in page.parts:
        return None
    version = page.stem
    # A version, not a landing page: digits and dots, with an optional build
    # suffix. `all-releases`, `whats-new` and the like fall out here.
    core = version.split('-', 1)[0]
    if not core or not all(part.isdigit() for part in core.split('.')):
        return None
    return f'{POST_DOWNLOAD}/{stem}-{version}.md'


def audit(root):
    """Check every no-standalone entry still records something true."""
    try:
        entries = allowlist.load(root)[SECTION]
    except allowlist.AllowlistError as exc:
        print(f'postdownload: {allowlist.allowlist_path(root)} is malformed — '
              f'{exc}', file=sys.stderr)
        print('              Fix the entry; the accepted shape is in '
              'allowlist.py\'s header. A\n              malformed register is a '
              'hard error rather than an empty one, so an\n              '
              'acknowledgment can never be silently lost.', file=sys.stderr)
        return None

    # Nothing to audit and no tree to audit it against. A SKIP rather than a
    # failure, the same contract versioncheck.py and shrinkcheck.py carry, so a
    # sandbox or a partial checkout never blocks a local commit. The workflow
    # asserts the entry count rather than trusting this exit code.
    if not (pathlib.Path(root) / POST_DOWNLOAD).is_dir():
        print(f'postdownload: no {POST_DOWNLOAD}/ — SKIPPED (not a docs checkout)',
              file=sys.stderr)
        return None

    findings = 0
    for e in entries:
        page = pathlib.Path(root) / e['path']
        if not page.is_file():
            findings += 1
            print(f'postdownload: stale entry — {e["path"]}', file=sys.stderr)
            print(f'              line {e["line"]} of {allowlist.REL_PATH} '
                  f'acknowledges a page that no\n              longer exists, so '
                  f'the entry cannot apply to anything. Delete it in\n'
                  f'              this PR.', file=sys.stderr)
            continue
        expected = post_download_for(e['path'])
        if expected is None:
            findings += 1
            print(f'postdownload: not a release page — {e["path"]}',
                  file=sys.stderr)
            print(f'              line {e["line"]} of {allowlist.REL_PATH} '
                  f'names something that would never\n              need a Post '
                  f'Download page — a changelog, a landing page, or a product\n'
                  f'              with none — so exempting it exempts nothing. '
                  f'Name the version page.', file=sys.stderr)
            continue
        if (pathlib.Path(root) / expected).is_file():
            findings += 1
            print(f'postdownload: stale entry — {e["path"]}', file=sys.stderr)
            print(f'              line {e["line"]} of {allowlist.REL_PATH} says '
                  f'this release has no standalone\n              package, but '
                  f'{expected}\n              exists. Whatever was true when the '
                  f'entry was written, there is a\n              download page '
                  f'now — delete the entry in this PR.', file=sys.stderr)
    return findings, len(entries)


LINK_RE = re.compile(r'\]\(\s*<?([^)>\s]+)')


def git(root, *args):
    """Run git, returning (ok, stdout)."""
    p = subprocess.run(['git', '-C', str(root)] + list(args),
                       capture_output=True, text=True)
    return p.returncode == 0, p.stdout


def summary_refs(root):
    """Repo-relative paths platform/SUMMARY.md links to."""
    f = pathlib.Path(root) / 'platform' / 'SUMMARY.md'
    if not f.is_file():
        return set()
    text = f.read_text(encoding='utf-8', errors='replace')
    return {'platform/' + t.split('#', 1)[0].lstrip('./')
            for t in LINK_RE.findall(text)}


def new_pages(root, rev, scope):
    """Release-notes pages present now and absent at `rev`, sorted.

    Present = tracked or untracked-but-not-ignored AND on disk, so a page you
    have only just written is seen before it is staged, and one deleted in the
    working tree is not. Absent at `rev` is read from the object store.
    """
    ok, now = git(root, 'ls-files', '--cached', '--others', '--exclude-standard',
                  '-z', '--', 'release-notes/')
    if not ok:
        return None
    ok, then = git(root, 'ls-tree', '-r', '--name-only', '-z', rev, '--',
                   'release-notes/')
    if not ok:
        return None
    before = {p for p in then.split('\0') if p}
    out = set()
    for p in (x for x in now.split('\0') if x):
        if p in before or not p.endswith('.md'):
            continue
        if not (pathlib.Path(root) / p).is_file():
            continue
        if scope is not None and p not in scope:
            continue
        out.add(p)
    return sorted(out)


def check_new(root, rev, files, advisory=False):
    """Gate: every new release page has its Post Download page.

    Returns (findings, checked) or None for a SKIP.
    """
    try:
        exempt = {e['path'] for e in allowlist.load(root)[SECTION]}
    except allowlist.AllowlistError as exc:
        print(f'postdownload: {allowlist.allowlist_path(root)} is malformed — '
              f'{exc}', file=sys.stderr)
        return None
    if not (pathlib.Path(root) / POST_DOWNLOAD).is_dir():
        print(f'postdownload: no {POST_DOWNLOAD}/ — SKIPPED (not a docs checkout)',
              file=sys.stderr)
        return None
    # The base side is read from the object store of the repo `root` belongs
    # to; if this tree is nested in another repo, git answers for the outer one
    # and every page would read as new. navcheck.py carries the same guard.
    ok, top = git(root, 'rev-parse', '--show-toplevel')
    if ok and pathlib.Path(top.strip()).resolve() != pathlib.Path(root).resolve():
        print(f'postdownload: {root} is not the top of its git repository '
              f'({top.strip()} is) — SKIPPED', file=sys.stderr)
        return None
    ok, _ = git(root, 'rev-parse', '--verify', '-q', rev + '^{commit}')
    if not ok:
        print(f'postdownload: base revision {rev!r} not found — SKIPPED',
              file=sys.stderr)
        return None

    scope = {f.replace('\\', '/') for f in files} if files else None
    pages = new_pages(root, rev, scope)
    if pages is None:
        print('postdownload: git could not list the release notes — SKIPPED',
              file=sys.stderr)
        return None

    refs = summary_refs(root)
    findings = checked = 0
    for page in pages:
        expected = post_download_for(page)
        if expected is None:
            continue
        checked += 1
        if page in exempt:
            continue
        if not (pathlib.Path(root) / expected).is_file():
            findings += 1
            if advisory:
                print(f'postdownload: Post Download page owed — {page}',
                      file=sys.stderr)
                print(f'              expected {expected}\n              A '
                      f'docs-team member adds this page and its '
                      f'platform/SUMMARY.md entry; the\n              '
                      f'contributor does not need to. If this version shipped '
                      f'only inside a\n              Server release, add a '
                      f'`no-standalone:` entry with a reason to\n              '
                      f'{allowlist.REL_PATH}.', file=sys.stderr)
            else:
                print(f'postdownload: missing Post Download page — {page}',
                      file=sys.stderr)
                print(f'              expected {expected}\n              Add it '
                      f'(and its platform/SUMMARY.md entry) in this PR. If '
                      f'this\n              version shipped only inside a '
                      f'Server release and has no standalone\n              '
                      f'package, add a `no-standalone:` entry with a reason to '
                      f'{allowlist.REL_PATH}.', file=sys.stderr)
        elif expected not in refs:
            findings += 1
            who = ('A docs-team member adds the entry.' if advisory
                   else 'Add the entry.')
            print(f'postdownload: Post Download page not in the nav — '
                  f'{expected}', file=sys.stderr)
            print(f'              {page} has its page, but platform/SUMMARY.md '
                  f'does not link it, so it\n              would publish '
                  f'nowhere. {who}', file=sys.stderr)
    return findings, checked


def main(argv):
    args = argv[1:]
    mode = 'audit'
    target = None
    files = []
    advisory = False
    if args and args[0] in ('-h', '--help'):
        print(__doc__.rstrip(), file=sys.stderr)
        return 2
    if args and not args[0].startswith('-'):
        mode = args.pop(0)
        if mode == 'path':
            if not args:
                print('postdownload: `path` needs a release-notes page',
                      file=sys.stderr)
                return 2
            target = args.pop(0)
        elif mode == 'new':
            if not args:
                print('postdownload: `new` needs a base revision',
                      file=sys.stderr)
                return 2
            target = args.pop(0)
            advisory = '--advisory' in args
            files, args = [a for a in args if a != '--advisory'], []
        elif mode != 'audit':
            print(f'postdownload: unknown mode {mode!r} (expected audit, new or '
                  f'path)', file=sys.stderr)
            return 2
    if args:
        print(f'postdownload: unexpected argument {args[0]!r}', file=sys.stderr)
        return 2

    root = repo_root()

    if mode == 'path':
        rel = target
        try:
            rel = pathlib.Path(target).resolve().relative_to(root).as_posix()
        except (ValueError, OSError):
            pass
        expected = post_download_for(rel)
        print(expected if expected else
              f'none — {rel} maps to no Post Download page')
        return 0

    if mode == 'new':
        result = check_new(root, target, files, advisory)
        if result is None:
            return 0
        findings, n = result
        # Always printed, on stdout, for the same reason the audit line is: zero
        # new pages is legitimate, but "checked none" and "never ran" must not
        # share an exit code. postdownload-pr.yml asserts this line.
        print(f'postdownload: {n} new release page{"" if n == 1 else "s"} '
              f'checked vs {target}, {findings} without a Post Download page')
        return 1 if findings else 0

    result = audit(root)
    if result is None:
        return 0
    findings, n = result

    # The counts, always, and on stdout. "Audited 2 entries, both still true"
    # and "read an empty register" are otherwise the same exit code, so a moved
    # register or a wrong working directory would leave this permanently and
    # silently green. postdownload-pr.yml asserts this line.
    print(f'postdownload: {n} no-standalone entr'
          f'{"y" if n == 1 else "ies"} audited, {findings} stale')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
