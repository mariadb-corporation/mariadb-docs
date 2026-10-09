#!/usr/bin/env python3
"""versioncheck.py — the paired "most recent version" include guard.

WHY THIS EXISTS
    Every connector, and every live Community Server series, states its most
    recent version in TWO includes that live in two different spaces:

        release-notes/.gitbook/includes/latest-<key>.md
            the banner, the version link and the Download button, pulled into
            the series/connector landing pages and Download Latest Releases

        platform/.gitbook/includes/most-recent-<key>.md
            one bullet, pulled into every Post Download page for that connector
            or series -- 116 pages for Connector/J, 57 for Node.js

    Nothing compares them. Bumping one and not the other leaves the two spaces
    stating DIFFERENT "most recent" versions, on live pages, with every existing
    gate green: both files are valid Markdown, every link in them resolves, and
    neither page shrank. codespell, lychee, includecheck, navcheck, fragcheck
    and shrinkcheck all pass a mismatched pair.

    DOCS-6734 is the case. `most-recent-odbc.md` read "3.2., released   2025" --
    a truncated version and a half-deleted date -- while `latest-odbc.md` read
    3.2.9. It was live on three Post Download pages, and no check could see it.

WHY PAIR EQUALITY, AND NOT "IS IT THE NEWEST RELEASE"
    DOCS-6408 proposed asserting the platform include against the newest
    release-notes page, and left open "whether the most-recent-<x> include-
    freshness assertion is worth the false failures it will produce on a
    held-back release". It is not, for two separate reasons:

    1. The newest release is not always the one to advertise. A connector
       version that ships only INSIDE a Community Server release has no
       standalone package and no download to link to. Both Connector/C includes
       correctly sat at 3.4.9 through the August 2026 releases while 3.3.20 and
       3.4.10 shipped; a "newest version wins" rule would have advanced them to
       a download that does not exist. That exemption is the other half of
       DOCS-6734 and needs a signal this check does not have yet.

    2. A round can legitimately merge with `hidden: true` pending its release
       TODOs. The release notes are in the tree and the includes correctly still
       name the PREVIOUS version, so a freshness assertion fails a correct PR.

    Pair equality has neither problem. It compares the two files against EACH
    OTHER rather than against an external notion of truth, so it is silent on a
    held-back release (neither include moved) and on a no-standalone release
    (neither include moved), and it still catches the bump-one-forget-the-other
    mistake -- which is the failure that actually happened. It needs no
    changed-file plumbing and no allowlist, which is why this half of DOCS-6734
    lands on its own rather than waiting on the other.

WHAT IT ASSERTS
    1. PAIR EQUALITY, for every key that has includes on BOTH sides. The
       versions must be the same string. Zero maintenance: the set of pairs is
       discovered from the tree on every run.

    2. CONNECTOR COVERAGE, in both directions. A connector with a release-notes
       include must have a platform one and vice versa, unless it is named in
       NO_PLATFORM_INCLUDE below with the reason. A new connector therefore
       cannot arrive half-wired without someone deciding which it is.

    An exemption whose release-notes include has gone is STALE and fails, so the
    list prunes itself at the point someone forgets -- the rule
    doc-lint-allow.yml already applies to its own entries.

WHAT IT DELIBERATELY DOES NOT ASSERT
    Series coverage, for two independent reasons. A Community Server series
    legitimately loses its platform include when it goes EOL and its Post
    Download pages are retired, while the release-notes include stays as a
    historical marker -- 10.5, 11.3, 11.5, 11.6, 11.7 and 12.0 are all in that
    state today. And Enterprise Server has no Post Download pages AT ALL, so
    `latest-es`, `latest-es-10.6` and their siblings have no platform
    counterpart to be missing: they are unpaired by construction rather than by
    oversight, and no `most-recent-es*` include will ever exist for them to be
    compared against. Asserting coverage over series would therefore mean a list
    that grows every time a series ages out, for a failure nobody has had.
    Series that DO pair are still held to pair equality below, which is where a
    live bug would be.

    Dates. The platform bullet carries a release date and the release-notes
    include does not, so there is nothing to compare it against. `most-recent-
    odbc.md`'s mangled date was found because its VERSION was truncated in the
    same edit, not because anything checked the date.

    A preview series, on the version itself. Before a series goes GA it has no
    per-version release-notes page, so its banner names the series and links
    straight to downloads.mariadb.org ("MariaDB 13.2 Preview") while the
    platform bullet names the concrete release that does have a Post Download
    page (13.2.0). Both are right. Such a pair is held to the weaker assertion
    that the platform version is IN the series the banner names.

WHY THE EXEMPTIONS ARE IN THIS FILE AND NOT doc-lint-allow.yml
    That register is for per-page acknowledgments -- "this page is an orphan on
    purpose", "this page shrank on purpose" -- keyed by path, added by the
    author of the PR that trips the guard. These are neither: they are
    structural facts about which products the foundation website offers for
    download, they are keyed by connector rather than by path, and they change
    roughly never. Keeping them next to the rule they qualify means the reason
    is where the reader already is.

WHY TREE-WIDE, AND WHY IT TAKES NO FILE ARGUMENTS
    The finding is never local to one file -- it is a disagreement BETWEEN two
    files in two different spaces, and a PR that edits only one of them is
    exactly the PR that causes it. Scoping to changed files would blind the
    check to its own failure mode. The whole scan is 44 files and runs in
    milliseconds, so there is nothing to gain by narrowing it. Same reasoning
    includecheck.sh records for being tree-wide.

USAGE
    versioncheck.py                 scan the tree it is run inside
    versioncheck.py --root <dir>    scan that checkout instead

Exit: 0 = every pair agrees, 1 = a finding, 2 = a usage error.
"""

import pathlib
import re
import sys

REL_DIR = 'release-notes/.gitbook/includes'
REL_PREFIX = 'latest-'
PLAT_DIR = 'platform/.gitbook/includes'
PLAT_PREFIX = 'most-recent-'

# Connectors that have a release-notes include and correctly no platform one.
# Both are absent from the foundation website's download listing, so they have
# no Post Download pages for a platform include to be pulled into (DOCS-6408's
# naming map records the same two as "none"/"none").
NO_PLATFORM_INCLUDE = {
    'cpp': 'Connector/C++ is not offered for download on the foundation '
           'website, so it has no Post Download pages — DOCS-6408',
    'r2dbc': 'Connector/R2DBC is not offered for download on the foundation '
             'website, so it has no Post Download pages — DOCS-6408',
}

# A version as either side spells it: 3.4.11, 10.11.19, 12.3. No Enterprise
# build suffix (10.6.27-23) is matched, because no pair can contain one --
# Enterprise Server has no Post Download pages at all, so it has no platform
# include for a release-notes one to be compared against. Anchored nowhere on
# purpose -- both extractors below narrow the text to one element FIRST, because
# a bare search over a whole include would hit the `3.4/` directory component of
# an href long before the version it links to.
VERSION_RE = re.compile(r'\d+\.\d+(?:\.\d+)*')

# release-notes side: the version is the first <strong> in the hint, whether the
# file writes it bare (<strong>3.4.11</strong>) or prefixed
# (<strong>MariaDB 12.1.2</strong>).
STRONG_RE = re.compile(r'<strong>(.*?)</strong>', re.S)
TAG_RE = re.compile(r'<[^>]+>')

# A pre-GA series has no per-version release notes page yet, so its banner names
# the SERIES and links straight to downloads.mariadb.org -- "MariaDB 13.2
# Preview" against a platform bullet reading 13.2.0, which is correct on both
# sides. Matched on the rendered word rather than listed by series, because the
# banner is rewritten the moment the series goes GA (13.1's now reads 13.1.1).
PREVIEW_RE = re.compile(r'\bpreview\b', re.I)

# platform side: one bullet. The version is either the text of a Markdown link
# or a bare token, and in the link case the URL repeats the series ahead of the
# version (".../10.11/10.11.19"), so prefer the link TEXT where there is one.
LINK_TEXT_RE = re.compile(r'\[([^\]]*)\]')

# `latest-10-11` and `most-recent-10.11` name the same series with different
# separators; `latest-13.1` and `most-recent-13.1` already agree. Only a bare
# two-number key is rewritten, so `es-10.6` keeps its shape.
SERIES_SEP_RE = re.compile(r'\d+[-.]\d+')

# A series key, which is exempt from the coverage assertion above: `10-11`,
# `13.1`, `es-11.8`, and the bare `es` pointer to the current LTS series. The
# `es-` forms are here only so coverage skips them -- Enterprise Server has no
# Post Download pages, so an `es-*` key can never have a platform include and
# can never form a pair.
SERIES_RE = re.compile(r'(?:es-)?\d+[-.]\d+')


def repo_root(start='.'):
    """Nearest ancestor that looks like this repo.

    Spelled the same way as allowlist.py, navcheck.py and fragcheck.py, and for
    the same reason: the checkers are invoked from the repo root in every real
    call, but the test suite runs them from a sandbox. Duplicated rather than
    imported because this check has no acknowledgment register, so allowlist.py
    is otherwise nothing to do with it.
    """
    d = pathlib.Path(start).resolve()
    for cand in [d] + list(d.parents):
        if (cand / '.codespellignore').is_file() or (cand / '.git').exists():
            return cand
    return d


def normalize(key):
    """The shared key for an include name, across the two spellings."""
    return key.replace('-', '.') if SERIES_SEP_RE.fullmatch(key) else key


def is_series(key):
    """True for a Server series, which the coverage assertion skips."""
    return key == 'es' or bool(SERIES_RE.fullmatch(key))


def collect(root, rel_dir, prefix):
    """Map normalized key -> path, for every include in one of the two dirs."""
    found = {}
    d = pathlib.Path(root) / rel_dir
    if not d.is_dir():
        return found
    for path in sorted(d.glob(f'{prefix}*.md')):
        found[normalize(path.name[len(prefix):-len('.md')])] = path
    return found


def rel_version(text):
    """The version a release-notes `latest-*` include advertises.

    Returns (version, is_preview). A preview banner names a series rather than a
    release, so the caller compares it differently.
    """
    m = STRONG_RE.search(text)
    if not m:
        return None, False
    inner = TAG_RE.sub('', m.group(1))
    v = VERSION_RE.search(inner)
    return (v.group(0) if v else None), bool(PREVIEW_RE.search(inner))


def plat_version(text):
    """The version a platform `most-recent-*` include states."""
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith('*'):
            continue
        # Cut the date clause before searching. Nothing in a rendered date
        # matches VERSION_RE, but a truncated one is exactly the shape this
        # check exists to catch, and it must not be able to supply a version.
        head = line.split(', released', 1)[0]
        link = LINK_TEXT_RE.search(head)
        v = VERSION_RE.search(link.group(1) if link else head)
        return v.group(0) if v else None
    return None


def read(path):
    try:
        return path.read_text(encoding='utf-8', errors='replace')
    except OSError:
        return None


def rel(root, path):
    return path.relative_to(root).as_posix()


def check(root):
    """Report every disagreeing pair and every half-wired connector."""
    rel_includes = collect(root, REL_DIR, REL_PREFIX)
    plat_includes = collect(root, PLAT_DIR, PLAT_PREFIX)
    findings = 0
    compared = 0

    # Neither directory present means this is not a checkout of the docs repo --
    # doc-lint-test.sh runs doc-lint.sh against a throwaway sandbox that roots at
    # its own .codespellignore, and this check has nothing to say about it. A
    # SKIP, not a failure: never block a local commit over subject matter that
    # is simply absent, the same contract shrinkcheck.py has for a missing base
    # revision. The risk a SKIP carries -- that a MOVED includes directory would
    # make the gate permanently green -- is answered in versioncheck-pr.yml,
    # which asserts the pair count rather than trusting the exit code. ONE
    # directory missing is a real finding and falls through to the checks below.
    if not rel_includes and not plat_includes:
        print(f'versioncheck: no {REL_DIR}/ and no {PLAT_DIR}/ — SKIPPED '
              f'(not a docs checkout)', file=sys.stderr)
        return None

    for key in sorted(set(rel_includes) & set(plat_includes)):
        rel_path, plat_path = rel_includes[key], plat_includes[key]
        rel_text, plat_text = read(rel_path), read(plat_path)
        if rel_text is None or plat_text is None:
            continue
        compared += 1
        (rel_v, preview), plat_v = rel_version(rel_text), plat_version(plat_text)

        # An unreadable version is reported, never skipped. Truncation is how
        # DOCS-6734's live bug presented, and a silent skip would make the one
        # file most likely to be broken the one file nobody checks.
        for path, version, what in ((rel_path, rel_v, 'a <strong> version'),
                                    (plat_path, plat_v, 'a version bullet')):
            if version is None:
                findings += 1
                print(f'versioncheck: no version found — {rel(root, path)}',
                      file=sys.stderr)
                print(f'              Expected {what}. Either the include was '
                      f'truncated mid-edit or its\n              shape changed; '
                      f'if the shape changed on purpose, teach the extractor in'
                      f'\n              .claude/hooks/versioncheck.py about it.',
                      file=sys.stderr)

        if rel_v is None or plat_v is None:
            continue

        # A preview banner names the series, so require only that the platform
        # release belongs to it. Note this is NOT the same as forgiving a
        # shorter version generally: `3.2` against `3.2.9` on a GA connector is
        # the truncation DOCS-6734 found live, and equality still catches it.
        if preview:
            if plat_v == rel_v or plat_v.startswith(rel_v + '.'):
                continue
            findings += 1
            print(f'versioncheck: preview series mismatch — {key}',
                  file=sys.stderr)
            print(f'              {rel(root, rel_path)} previews series {rel_v}'
                  f'\n              {rel(root, plat_path)} says {plat_v}, which '
                  f'is not in that series.', file=sys.stderr)
            continue

        if rel_v == plat_v:
            continue
        findings += 1
        print(f'versioncheck: paired includes disagree — {key}', file=sys.stderr)
        print(f'              {rel(root, rel_path)} says {rel_v}\n'
              f'              {rel(root, plat_path)} says {plat_v}',
              file=sys.stderr)
        print('              These two render the "most recent version" in '
              'different spaces, so the\n              site states two answers '
              'at once. Bump whichever is behind — they move\n              '
              'together, and neither advances for a release with no standalone '
              'download.', file=sys.stderr)

    # Coverage, both directions, connectors only -- see the header on why series
    # are out of scope here.
    for key in sorted(set(rel_includes) - set(plat_includes)):
        if is_series(key) or key in NO_PLATFORM_INCLUDE:
            continue
        findings += 1
        print(f'versioncheck: no platform include — {key}', file=sys.stderr)
        print(f'              {rel(root, rel_includes[key])} has no '
              f'{PLAT_DIR}/{PLAT_PREFIX}{key}.md,\n              so its Post '
              f'Download pages state no version at all.', file=sys.stderr)
        print(f'              If {key} is not offered for download, add it to '
              f'NO_PLATFORM_INCLUDE in\n              '
              f'.claude/hooks/versioncheck.py with the reason.', file=sys.stderr)

    for key in sorted(set(plat_includes) - set(rel_includes)):
        if is_series(key):
            continue
        findings += 1
        print(f'versioncheck: no release-notes include — {key}', file=sys.stderr)
        print(f'              {rel(root, plat_includes[key])} has no '
              f'{REL_DIR}/{REL_PREFIX}{key}.md,\n              so the release-'
              f'notes space advertises no version for it.', file=sys.stderr)

    # Self-pruning, the rule doc-lint-allow.yml applies to its own entries: an
    # exemption for a connector that no longer has an include cannot qualify
    # anything, and left alone it would outlive the reason it records.
    for key, reason in sorted(NO_PLATFORM_INCLUDE.items()):
        if key in rel_includes:
            continue
        findings += 1
        print(f'versioncheck: stale exemption — {key}', file=sys.stderr)
        print(f'              NO_PLATFORM_INCLUDE in '
              f'.claude/hooks/versioncheck.py exempts {key!r}\n'
              f'              ({reason}), but {REL_DIR}/{REL_PREFIX}{key}.md no '
              f'longer exists.\n              Delete the entry in this PR.',
              file=sys.stderr)

    return findings, compared, len(rel_includes), len(plat_includes)


def main(argv):
    args = argv[1:]
    root = None
    while args:
        a = args.pop(0)
        if a in ('-h', '--help'):
            print(__doc__.rstrip(), file=sys.stderr)
            return 2
        if a == '--root':
            if not args:
                print('versioncheck: --root needs a directory', file=sys.stderr)
                return 2
            root = args.pop(0)
        else:
            print(f'versioncheck: unexpected argument {a!r}. This check is '
                  'tree-wide and takes no\n              file arguments — see '
                  'its header for why.', file=sys.stderr)
            return 2

    root = repo_root(root or '.')
    result = check(root)
    if result is None:
        return 0
    findings, compared, n_rel, n_plat = result

    # The counts, always, and on stdout. "Compared 15 pairs, all agree" and
    # "found no includes at all" are otherwise the same exit code, so a moved
    # includes directory or a wrong working directory would leave this gate
    # permanently and silently green. versioncheck-pr.yml asserts this line;
    # includecheck.sh and shrinkcheck.py print their counts for the same reason.
    print(f'versioncheck: {compared} pair(s) compared, {findings} finding(s) '
          f'({n_rel} release-notes include(s), {n_plat} platform include(s), '
          f'{len(NO_PLATFORM_INCLUDE)} exempt)')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
