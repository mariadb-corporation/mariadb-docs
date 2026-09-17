#!/usr/bin/env python3
"""shrinkcheck.py — the net line-loss ("gutted page") guard.

WHY THIS EXISTS
    A surviving page loses most of its body while the markup stays valid and
    every remaining link resolves, so codespell and lychee both PASS and the
    only symptom is a reader finding a page that no longer covers its subject.

    DOCS-6442 is the case. A retirement campaign (DOCS-5976 Tier B, c6ea5549a)
    meant to delete ONE {% columns %} content-ref block from the Storage Engines
    landing page and promote FEDERATED into its place. It deleted 23 of the 24
    blocks instead: 298 lines -> 22, 24 content-refs -> 1. SUMMARY.md was
    untouched, so the nav still listed all 27 engines while the page listed one.
    Every gate passed; a reader found it two days later.

    That commit ARRIVED THROUGH A PR, which is the whole argument for gating it
    in CI rather than in a pre-commit hook: the hook "only gates commits that
    Claude Code makes via the Bash tool" (pre-commit.sh header), so it would not
    have fired at all. Gated by shrinkcheck-pr.yml since DOCS-6586.

WHY NET LOSS AND NOT RAW DELETIONS
    Raw deletions flag every reformatting campaign -- alias expansion,
    trailing-backslash removal, changelog normalization -- because those rewrite
    lines rather than remove them. Measured over 300 commits of this repo: raw
    deletions >40% flags 17 files, mostly those campaigns; net loss >40% flags
    4. On c6ea5549a itself the guard yields a ONE-item list at 94%, next-worst
    16%.

WHY IT WAS EXTRACTED FROM doc-lint.sh, AND WHY IN PYTHON
    Same move includecheck.sh made under DOCS-6586: the CI gate must not route
    through doc-lint.sh, which would re-run codespell and lychee (they have
    their own workflows) and the orphan guard (its own workflow now too). One
    implementation, two callers, rather than a copy in a `run:` block.

    It is Python rather than the bash it was extracted from because the
    acknowledgment allowlist has exactly ONE parser (allowlist.py) and a second
    one in awk is the drift this ticket exists to remove. The cost is that the
    LOCAL guard now needs python3 where it used to need only bash -- acceptable
    only because it now HAS a CI counterpart, which is the same trade
    fragcheck.py and navcheck.py already make.

WHAT IT COMPARES
    The WORKING-TREE file against <base>, which is the content codespell and
    lychee are checking too. When the index and the working tree differ, this
    reflects the working tree, not what is staged.

    A file absent from <base> is a new file and has nothing to have lost. That
    also means a RENAME is out of scope, in both directions: with the rename
    detected the pre-image is under the old path, and without it the new path
    simply looks new. A page that is moved and gutted in one commit is the one
    shape this cannot see -- the orphan and include gates cover the other
    consequences of a move.

THRESHOLDS  (environment, same names doc-lint.sh always used)
    DOC_LINT_SHRINK_PCT   (40) percent of the pre-image lost, net, before flagging
    DOC_LINT_SHRINK_MIN   (20) minimum net lines lost, so tiny files can't trip it
    DOC_LINT_SHRINK_FLOOR (30) minimum pre-image size considered at all
    DOC_LINT_BASE       (HEAD) revision the pre-image is read from, unless --base

ACKNOWLEDGMENT
    The `shrink:` section of .claude/hooks/doc-lint-allow.yml -- a checked-in
    entry with a reason, visible in the diff where review already happens
    (DOCS-6586). DOC_LINT_ALLOW_SHRINK still works for a local one-off run and
    is unioned with the file; only the environment variable takes `all`.

    A shrink entry whose page no longer exists is STALE and fails: the register
    prunes itself rather than piling up. There is no "un-shrink" signal, so that
    is as far as self-pruning can go on this half -- an entry whose page has
    since regrown needs the occasional manual pass.

USAGE
    shrinkcheck.py [--base <rev>] <file> [<file> ...]
    shrinkcheck.py [--base <rev>] --stdin0      NUL-delimited paths on stdin

    --stdin0 rather than xargs, for the reason includecheck.sh records: this
    repo is ~9,700 tracked paths, which is over ARG_MAX, and xargs would split
    the run into batches that each return their own status -- so findings in an
    earlier batch could still exit 0.

Exit: 0 = nothing gutted (or SKIPPED), 1 = a finding, 2 = a usage error.
"""

import os
import pathlib
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import allowlist
except ImportError:  # pragma: no cover - a broken checkout, not a missing tool
    print('shrinkcheck: .claude/hooks/allowlist.py not found. It is checked in '
          'beside this\n             script, so this is a broken checkout, not '
          'a missing tool, and a check\n             that cannot read its '
          'acknowledgments must not report success.', file=sys.stderr)
    sys.exit(2)

SECTION = 'shrink'


def git(root, *args, binary=False):
    p = subprocess.run(['git', '-C', str(root)] + list(args),
                       capture_output=True, text=not binary)
    return p.returncode == 0, p.stdout


def count_lines(data):
    """Newlines, exactly as `wc -l` counts them.

    Spelled out because the guard's thresholds were calibrated against `wc -l`
    in the bash original: a file with no trailing newline counts one line short,
    and matching that keeps every measured figure in the header comparable.
    """
    return data.count(b'\n')


def stale_entries(root, entries):
    """Allowlist entries whose page is gone from the working tree."""
    return [e for e in entries if not (pathlib.Path(root) / e['path']).is_file()]


def report_stale(stale):
    print(f'shrinkcheck: {len(stale)} stale allowlist entr'
          f'{"y" if len(stale) == 1 else "ies"} in '
          f'{allowlist.REL_PATH}:', file=sys.stderr)
    for e in stale:
        print(f'  line {e["line"]}: {e["path"]} — no such file', file=sys.stderr)
    print('\n             The page an acknowledgment names no longer exists, so '
          'the entry\n             cannot apply to anything. Delete it in this '
          'PR. The register is\n             meant to prune itself at the point '
          'someone forgets rather than\n             pile up entries nobody '
          'dares remove (DOCS-6586).', file=sys.stderr)


def check(root, files, base, pct, minimum, floor, skip):
    """Report every file in `files` that lost too much against `base`."""
    findings = 0
    compared = 0
    for rel in files:
        rel = rel[2:] if rel.startswith('./') else rel
        if rel in skip:
            continue
        # Absent from the base revision = a new file, so nothing to have lost.
        ok, _ = git(root, 'cat-file', '-e', f'{base}:{rel}')
        if not ok:
            continue
        ok, pre_data = git(root, 'show', f'{base}:{rel}', binary=True)
        if not ok:
            continue
        try:
            post_data = (pathlib.Path(root) / rel).read_bytes()
        except OSError:
            continue
        compared += 1
        pre = count_lines(pre_data)
        post = count_lines(post_data)
        if pre < floor:
            continue
        net = pre - post
        if net < minimum:
            continue
        if net / pre * 100 <= pct:
            continue
        findings += 1
        print(f'shrinkcheck: possible gutted page — {rel}', file=sys.stderr)
        print(f'             lost {net} of {pre} lines net '
              f'({net / pre * 100:.0f}%) vs {base}.', file=sys.stderr)
        print('             Confirm the page still covers everything it should. '
              'For a landing page,\n             compare its content-ref count '
              "against the space's SUMMARY.md children —\n             "
              'SUMMARY.md is authoritative for nav, so a page listing far fewer '
              'of its\n             children than SUMMARY.md does is the '
              'signature of this bug (DOCS-6442).', file=sys.stderr)
        print(f'             Intentional? Add it to the `{SECTION}:` section of '
              f'{allowlist.REL_PATH}\n             with the reason, so the '
              f'acknowledgment is in the diff a reviewer reads.\n'
              f'             Locally, DOC_LINT_ALLOW_SHRINK=\'{rel}\' does the '
              f'same for one run.', file=sys.stderr)
    return findings, compared


def main(argv):
    args = argv[1:]
    base = os.environ.get('DOC_LINT_BASE', 'HEAD')
    stdin0 = False
    files = []
    while args:
        a = args.pop(0)
        if a in ('-h', '--help'):
            print(__doc__.rstrip(), file=sys.stderr)
            return 2
        if a == '--stdin0':
            stdin0 = True
        elif a == '--base':
            if not args:
                print('shrinkcheck: --base needs a revision', file=sys.stderr)
                return 2
            base = args.pop(0)
        elif a.startswith('--'):
            print(f'shrinkcheck: unknown option {a!r}', file=sys.stderr)
            return 2
        else:
            files.append(a)

    if stdin0:
        if files:
            print('shrinkcheck: --stdin0 takes the paths on stdin, so name no '
                  'files as arguments', file=sys.stderr)
            return 2
        files = [p for p in sys.stdin.buffer.read().decode(
            'utf-8', 'replace').split('\0') if p]

    # Kept before the filter below, because shrinkcheck-pr.yml asserts that the
    # number of paths it fed is the number this script says it received. A
    # broken pipe, a mangled NUL list or a silently emptied pathspec would
    # otherwise look exactly like "nothing in this PR could have shrunk".
    received = len(files)

    # Keep only existing Markdown/HTML paths -- the same filter doc-lint.sh
    # applies, so both callers check the same set.
    files = [f for f in files
             if f.endswith(('.md', '.html')) and pathlib.Path(f).is_file()]

    root = allowlist.repo_root(files[0] if files else '.')

    try:
        entries = allowlist.load(root)[SECTION]
    except allowlist.AllowlistError as exc:
        print(f'shrinkcheck: {allowlist.allowlist_path(root)} is malformed — '
              f'{exc}', file=sys.stderr)
        print('             Fix the entry; the accepted shape is in '
              'allowlist.py\'s header. A\n             malformed register is a '
              'hard error rather than an empty one, so an\n             '
              'acknowledgment can never be silently lost.', file=sys.stderr)
        return 2

    env = allowlist.env_paths(SECTION)
    allow_all = 'all' in env
    skip = {e['path'] for e in entries} | (env - {'all'})

    # A SKIP, not a failure: never block a local commit over a missing baseline.
    # Both callers that must not tolerate it assert the base themselves --
    # shrinkcheck-pr.yml before invoking, exactly as fragcheck-pr.yml does.
    ok, _ = git(root, 'rev-parse', '--is-inside-work-tree')
    if not ok:
        print('shrinkcheck: not a git work tree — SKIPPED (needs a base revision)',
              file=sys.stderr)
        return 0
    ok, _ = git(root, 'rev-parse', '--verify', '-q', base + '^{commit}')
    if not ok:
        print(f'shrinkcheck: base revision {base!r} not found — SKIPPED',
              file=sys.stderr)
        return 0

    rc = 0

    # Checked whatever the file scope is, and before the `all` hatch: a stale
    # entry is a defect in the register itself, not a finding about a page, so
    # neither "this PR touched nothing relevant" nor a local
    # DOC_LINT_ALLOW_SHRINK=all should hide it.
    stale = stale_entries(root, entries)
    if stale:
        report_stale(stale)
        rc = 1

    if allow_all:
        print('shrinkcheck: DOC_LINT_ALLOW_SHRINK=all — line-loss check skipped')
        return rc

    findings, compared = check(root, files, base,
                               float(os.environ.get('DOC_LINT_SHRINK_PCT', 40)),
                               int(os.environ.get('DOC_LINT_SHRINK_MIN', 20)),
                               int(os.environ.get('DOC_LINT_SHRINK_FLOOR', 30)),
                               skip)
    if findings:
        rc = 1

    # The counts, always, and on stdout. "Compared 812 files, none gutted" and
    # "compared nothing at all" are otherwise the same exit code -- a pathspec
    # typo, an empty file list or a wrong working directory would make the gate
    # permanently and silently green. shrinkcheck-pr.yml asserts against this
    # line; includecheck.sh prints its counts for the same reason.
    print(f'shrinkcheck: {compared} file(s) compared against {base}, '
          f'{findings} possibly gutted '
          f'({received} given, {len(files)} eligible, {len(skip)} acknowledged)')
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv))
