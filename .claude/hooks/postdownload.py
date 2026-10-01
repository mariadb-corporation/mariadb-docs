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

    It does NOT yet assert the other direction -- that a newly added release
    notes page HAS its Post Download page. That is DOCS-6408's gate, it needs
    the changed-files plumbing, and it is why this module exports
    `post_download_for()` rather than keeping it private. It cannot be run
    tree-wide: 67 existing connector releases have no Post Download page, only
    two of which are acknowledged, and the rest are a mix of pages predating the
    system (Connector/J 1.1.x is from 2013) and gaps nobody has triaged.

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
    postdownload.py path <file>    print the Post Download page a release-notes
                                   page maps to, or why it maps to none

Exit: 0 = register clean (or SKIPPED), 1 = a finding, 2 = a usage error.
"""

import os
import pathlib
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


def main(argv):
    args = argv[1:]
    mode = 'audit'
    target = None
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
        elif mode != 'audit':
            print(f'postdownload: unknown mode {mode!r} (expected audit or path)',
                  file=sys.stderr)
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
