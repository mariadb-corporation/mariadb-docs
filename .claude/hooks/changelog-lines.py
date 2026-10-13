#!/usr/bin/env python3
"""changelog-lines.py — the revision list of a changelog page, from git.

WHY THIS EXISTS
    A changelog page is fixed boilerplate around one generated block: a bullet per
    commit in the release. Until DOCS-6612 that block came from two places, both
    by hand:

      * Community Server: mariadb.org-tools/release/prep-changelog, which runs
        `git checkout <branch>` then `git reset --hard <rev>` in the shared
        server clone with no error handling. If the branch has not been fetched,
        the checkout fails silently and the reset rewrites whatever branch was
        checked out.
      * Connectors: a `git log --pretty=...` one-liner per connector, followed by
        hand-escaping in an editor. The seven connectors use four line formats,
        two commit orders, three hash lengths, and differing escapes, and the
        format belongs to the series, not the product: Connector/Python 1.1 is
        nested and 2.0 is flat.

    This script produces both, read-only. It never checks out, resets, pulls or
    fetches; it runs `git log` against refs that must already exist.

THREE MODES
    server     The prep-changelog format: --topo-order, 10-character hashes,
               merge commits on one styled line, everything else as a revision
               line plus a nested subject. The range is `<start>..<rev>` minus
               everything reachable from `--exclude` (the release commit of the
               latest release in the next-older maintained series). The leading
               "Includes all fixes from" bullets are not generated; the page
               writer adds them.

    connector  The format is INFERRED from a template: the previous changelog
               page in the same series. Hash length, nested vs. flat, the
               separator, the date <mark>, `]` escaping, and issue-key linking
               are all read off its existing lines, so a new page matches its
               neighbors without a per-product table to keep in sync. Commit
               order follows the family: nested pages use --topo-order, flat
               pages use git's default order (both proven, below).

    repo-setup The two single-page changelogs, release-notes/tools/mariadb-repo-setup-
               changelog.md and mariadb-es-repo-setup-changelog.md. These are not
               built from git log: the script's own `# Notes:` comment block IS the
               changelog, one `YYYY-MM-DD - item` entry per version, and the version
               is that date (`version="..."` on line 4). The scripts live in the
               mariadb-enterprise-scripts repository, untagged; the release is the
               file there at the commit that was uploaded to the CDN, and the
               published checksum is generated from that file just before upload.
               So this reads the script with `git show <rev>:<name>` and prints the
               entries newer than the page's newest, plus the version and sha256
               for the Versions table on the "Package Repository Setup and Usage"
               page. TODO-NNNN prefixes are dropped (the release-day commit strips
               them from the script too, 4171898); MDEV keys stay, as published.
               `&` is left bare, as published.

PROVE THE FORMAT BEFORE USING IT: --verify
    `--verify` regenerates a PUBLISHED page from that page's own range and diffs
    the revision block. Run it on the template before generating the new page:
    a clean diff proves the inferred format and the range rule together. On
    DOCS-6612 (2026-10-13) it reproduced, with zero differing lines, Connector/C
    3.3.21 and 3.4.9, C++ 1.1.9 and 1.0.8, ODBC 3.2.10 and 3.1.24, Python 1.1.14
    and 1.1.13, J 2.7.15 and 3.4.4, Node.js 3.2.5, and R2DBC 1.2.4 and 1.4.2.
    Every other difference was a hand edit by the page's author (a typo fixed in
    a commit subject, an identifier renamed) or one omitted commit; for Server
    13.0.2, 13.1.1, 11.8.9, 11.4.13, and 10.6.26 the commit list and order
    matched exactly, with differences only in escaping and hand-fixed typos.
    repo-setup reproduced all 78 entries of both pages: the ES page exactly, the
    Community page except two hand edits (a misspelled "unneeded" corrected, "release series"
    added).
    A diff in COMMITS (lines added, removed, or moved) means the range is wrong;
    a diff only inside subject text is an author's hand edit.

ESCAPING
    Commit subjects are text the page renders as Markdown, so outside a balanced
    `code span`: `\\ _ * & < [` are escaped, and `]` too where the template does.
    `<` matters most: an unescaped `<subquery>` is parsed as an HTML tag and
    GitBook drops it (DOCS-6717). Server pages leave `[` bare, as published. A leading `- ` or `* ` (a multi-line message
    flattened into a subject) is removed, since it would render as a nested
    bullet, and runs of spaces collapse to one. Server merge lines are left raw,
    as prep-changelog emits them.

WARNINGS (stderr, never fatal)
    The script flags what published pages show authors fixing by hand: an issue
    key with a mismatched bracket (`[CONJ-1333}`), a version bump naming another
    version (a 3.3 bump merged into a 3.4 range; Connector/C 3.4.11 omits one),
    and an unbalanced backtick.

USAGE
    changelog-lines.py connector --template PAGE --repo DIR --range A..B
                                 [--version X.Y.Z] [--verify]
    changelog-lines.py server --repo DIR --start REF --rev REF
                              [--exclude REF] [--verify PAGE]
    changelog-lines.py repo-setup --repo DIR [--rev REF] --name SCRIPT
                                  --page PAGE [--verify]

Exit: 0 = lines printed (or --verify clean), 1 = --verify found differences,
2 = usage error, unreadable template, or a ref git cannot resolve.
"""

import argparse
import difflib
import pathlib
import re
import subprocess
import sys

REV_RE = re.compile(
    r'^\* \[Revision #([0-9a-f]+)\]\((https://github\.com/[^)]+?)/commit/[0-9a-f]+\)(.*)$')
SERVER_MERGE_PREFIX = '* <sup>_<mark style="color:$primary;">Merge'
BRACKET_KEY_RE = re.compile(r'\[([A-Z][A-Z0-9]+-\d+)\]')
BARE_KEY_LINK_RE = re.compile(
    r'(?<!\\\[)\[([A-Z][A-Z0-9]+)-\d+\]\((https://jira\.mariadb\.org/[^)]*?)\1-\d+\)')
SERVER_URL = 'https://github.com/MariaDB/server'


class Fail(Exception):
    pass


def git(repo, *args):
    p = subprocess.run(['git', '-C', str(repo)] + list(args),
                       capture_output=True, text=True)
    if p.returncode != 0:
        raise Fail(f'git {" ".join(args[:3])} failed in {repo}: '
                   f'{p.stderr.strip().splitlines()[-1] if p.stderr.strip() else "no output"}')
    return p.stdout


def commit_of(repo, ref):
    """The commit a ref names. ^{commit}, because a release tag is annotated and
    its own SHA is not the commit's -- passing it as an exclude would still work,
    but printing it as "the release commit" would be wrong."""
    p = subprocess.run(['git', '-C', str(repo), 'rev-parse', '--verify', '-q',
                        f'{ref}^{{commit}}'], capture_output=True, text=True)
    if p.returncode != 0:
        raise Fail(f'{ref!r} is not a commit in {repo}. Fetch the tags first '
                   f'(`git -C {repo} fetch origin --tags`, which changes no branch '
                   f'or working tree), or check the spelling.')
    return p.stdout.strip()


def page_block(path):
    """The revision block of a page: every revision line, plus the nested subject
    line under it when there is one."""
    try:
        lines = pathlib.Path(path).read_text(encoding='utf-8').splitlines()
    except OSError as exc:
        raise Fail(f'cannot read {path}: {exc}')
    out = []
    for i, line in enumerate(lines):
        if REV_RE.match(line) or line.startswith(SERVER_MERGE_PREFIX):
            out.append(line)
            if i + 1 < len(lines) and lines[i + 1].startswith('  * '):
                out.append(lines[i + 1])
    return out


def infer_style(block, path):
    first = next((line for line in block if REV_RE.match(line)), None)
    if first is None:
        raise Fail(f'{path} has no "* [Revision #..." lines to learn a format from. '
                   f'Use an earlier page in the series as the template.')
    sha, url, rest = REV_RE.match(first).groups()
    body = '\n'.join(block)
    nested = any(line.startswith('  * ') for line in block)
    style = {
        'abbrev': len(sha),
        'url': url,
        'nested': nested,
        'mark': nested and '<mark style="color:$info;">' in rest,
        'sep': '' if nested else (' - ' if rest.startswith(' - ') else ' '),
        'esc_open': True,
        'collapse': True,
        'esc_close': '\\]' in body,
        # `\[[CONJ-1342](https://jira.mariadb.org/browse/CONJ-1342)]`: the flat pages.
        'bracket_links': '\\[[' in body and 'jira.mariadb.org/browse/' in body,
        'bare_key_url': None,
        # Balanced backticks are kept as code spans unless the template escapes them.
        'code_spans': '\\`' not in body,
        # Nested pages are generated --topo-order, flat ones in git's default order.
        'topo': nested,
    }
    m = BARE_KEY_LINK_RE.search(body)
    if m:
        # `[CONPY-321](https://jira.mariadb.org/projects/CONPY/issues/CONPY-321):`
        style['bare_key_url'] = m.group(2)
    return style


def esc_text(s, style):
    s = s.replace('\\', '\\\\')
    for ch in '_*`<' + ('&' if style.get('esc_amp', True) else ''):
        s = s.replace(ch, '\\' + ch)
    keys = []
    if style['bracket_links']:
        def hold(m):
            keys.append(m.group(1))
            return f'\x00{len(keys) - 1}\x00'
        s = BRACKET_KEY_RE.sub(hold, s)
    if style['esc_open']:
        s = s.replace('[', '\\[')
    if style['esc_close']:
        s = s.replace(']', '\\]')
    if keys:
        s = re.sub('\x00(\\d+)\x00',
                   lambda m: (f'\\[[{keys[int(m.group(1))]}](https://jira.mariadb.org/'
                              f'browse/{keys[int(m.group(1))]})]'), s)
    if style['bare_key_url']:
        u = style['bare_key_url']
        s = re.sub(r'(?<![\[\w-])[A-Z][A-Z0-9]+-\d+(?![\]\w])',
                   lambda m: f'[{m.group(0)}]({u}{m.group(0)})', s)
    return s


def esc(subject, style):
    s = re.sub(r'^[-*] +', '', subject.strip())
    if style['collapse']:
        s = re.sub(r' {2,}', ' ', s)
    if style['code_spans'] and s.count('`') >= 2 and s.count('`') % 2 == 0:
        parts = s.split('`')
        return '`'.join(p if i % 2 else esc_text(p, style) for i, p in enumerate(parts))
    return esc_text(s, style)


def warn_subject(sha, subject, version):
    notes = []
    if re.search(r'\[[A-Z][A-Z0-9]+-\d+[^\]\d]', subject) and not re.search(
            r'\[[A-Z][A-Z0-9]+-\d+\]', subject):
        notes.append('issue key with a mismatched bracket; authors fix these by hand')
    if subject.count('`') % 2:
        notes.append('unbalanced backtick, escaped as text')
    if version:
        for v in re.findall(r'(?i)(?:bump|version)\D{0,40}?(\d+\.\d+\.\d+)', subject):
            if v != version:
                notes.append(f'version bump for {v}, not {version}; published pages '
                             f'have dropped these when merged in from another series')
    for n in notes:
        print(f'changelog-lines: {sha} — {n}\n                 {subject}', file=sys.stderr)


def connector_lines(repo, rng, style, version=None):
    order = ['--topo-order'] if style['topo'] else []
    out = git(repo, 'log', *order, f'--abbrev={style["abbrev"]}',
              '--pretty=format:%h%x00%ai%x00%s', rng)
    lines = []
    for row in out.splitlines():
        sha, date, subject = row.split('\x00', 2)
        warn_subject(sha, subject, version)
        link = f'* [Revision #{sha}]({style["url"]}/commit/{sha})'
        if style['nested']:
            d = f'<mark style="color:$info;">{date}</mark>' if style['mark'] else date
            lines.append(f'{link} <sub>_{d}_</sub>')
            lines.append(f'  * {esc(subject, style)}')
        else:
            lines.append(f'{link}{style["sep"]}{esc(subject, style)}')
    return lines


# Published Server pages leave `[` bare, and keep prep-changelog's double spaces: `[No MDEV#]`, `strto[u][l]l`. With no `(` after
# the `]` it renders as text either way, and escaping it would make every --verify noisy.
SERVER_STYLE = {'esc_open': False, 'esc_close': False, 'collapse': False, 'bracket_links': False, 'bare_key_url': None,
                'code_spans': True}


def server_lines(repo, start, rev, exclude):
    rng = [f'{commit_of(repo, start)}..{commit_of(repo, rev)}']
    if exclude:
        rng.append('^' + commit_of(repo, exclude))
    merges = set(git(repo, 'log', '--merges', '--topo-order', '--pretty=format:%H',
                     *rng).split())
    lines = []
    for row in git(repo, 'log', '--topo-order', '--pretty=format:%H%x00%ai%x00%s',
                   *rng).splitlines():
        full, date, subject = row.split('\x00', 2)
        sha = full[:10]
        url = f'{SERVER_URL}/commit/{sha}'
        if full in merges:
            lines.append(f'{SERVER_MERGE_PREFIX}</mark>_</sup> [<sup>_<mark style='
                         f'"color:$primary;">Revision #{sha}</mark>_</sup>]({url}) '
                         f'<sup>_<mark style="color:$info;">{date} - {subject}</mark>_</sup>')
        else:
            warn_subject(sha, subject, None)
            lines.append(f'* [Revision #{sha}]({url}) <sup>_<mark style="color:$info;">'
                         f'{date}</mark>_</sup>')
            lines.append(f'  * {esc(subject, SERVER_STYLE)}')
    return lines


REPO_SETUP_STYLE = {'esc_open': False, 'esc_close': False, 'collapse': True,
                    'bracket_links': False, 'bare_key_url': None, 'code_spans': True,
                    'esc_amp': False}
NOTES_DATE_RE = re.compile(r'^#\s+(\d{4}-\d{2}-\d{2})\s+-\s+(.*)$')
NOTES_ITEM_RE = re.compile(r'^#\s+-\s+(.*)$')
NOTES_MORE_RE = re.compile(r'^#\s+(\S.*)$')
PAGE_DATE_RE = re.compile(r'^\* \*\*(\d{4}-\d{2}-\d{2})\*\*$')


def repo_setup_notes(text, where):
    """(version, [(date, [item, ...]), ...]) from a repo-setup script, newest first.

    An entry starts `#   YYYY-MM-DD - item`, a further item `#   <spaces> - item`, and
    any other comment line continues the item above it (the script wraps at ~80
    columns). The block ends at the first line that is not a comment."""
    lines = text.splitlines()
    version = next((m.group(1) for m in (re.match(r'^version="([^"]+)"', x) for x in lines)
                    if m), None)
    try:
        start = lines.index('# Notes:') + 1
    except ValueError:
        raise Fail(f'{where} has no "# Notes:" line -- not a repo-setup script?')
    entries = []
    for line in lines[start:]:
        if not line.startswith('#'):
            break
        m = NOTES_DATE_RE.match(line)
        if m:
            entries.append((m.group(1), [m.group(2)]))
            continue
        m = NOTES_ITEM_RE.match(line)
        if m and entries:
            entries[-1][1].append(m.group(1))
            continue
        m = NOTES_MORE_RE.match(line)
        if m and entries:
            entries[-1][1][-1] += ' ' + m.group(1)
    if not entries:
        raise Fail(f'{where}: no dated entries under "# Notes:"')
    return version, entries


def repo_setup_lines(entries):
    out = []
    for date, items in entries:
        out.append(f'* **{date}**')
        for item in items:
            item = re.sub(r'^TODO-\d+:?\s+', '', item.strip())
            out.append(f'  * {esc(item, REPO_SETUP_STYLE)}')
    return out


def repo_setup(repo, rev, name, page, verify):
    import hashlib
    where = f'{rev}:{name}'
    p = subprocess.run(['git', '-C', str(repo), 'show', where], capture_output=True)
    if p.returncode != 0:
        raise Fail(f'cannot read {where} in {repo}: '
                   f'{p.stderr.decode(errors="replace").strip()}')
    raw = p.stdout
    version, entries = repo_setup_notes(raw.decode('utf-8', 'replace'), where)
    try:
        page_lines = pathlib.Path(page).read_text(encoding='utf-8').splitlines()
    except OSError as exc:
        raise Fail(f'cannot read {page}: {exc}')
    published = [x for x in page_lines if PAGE_DATE_RE.match(x) or x.startswith('  * ')]
    if verify:
        return report(page, published, repo_setup_lines(entries), unit='entries')
    newest = next((PAGE_DATE_RE.match(x).group(1) for x in published if PAGE_DATE_RE.match(x)),
                  '0000-00-00')
    new = [e for e in entries if e[0] > newest]
    for date, items in entries:
        if any(re.match(r'^TODO-\d+', item.strip()) for item in items):
            print(f'changelog-lines: {date} — a TODO identifier is still in the script\'s '
                  f'notes. Dropped here, but the release-day commit normally strips it from '
                  f'the script too, so {where} may not be the release.', file=sys.stderr)
    if version != entries[0][0]:
        print(f'changelog-lines: version="{version}" but the newest note is dated '
              f'{entries[0][0]}. On release day both move to the release date together '
              f'(4171898); a mismatch means {where} is mid-edit, not the release.',
              file=sys.stderr)
    sha = hashlib.sha256(raw).hexdigest()
    print(f'changelog-lines: {where} is version {version}, sha256 {sha}', file=sys.stderr)
    print(f'changelog-lines: Versions table row: | {version} | `{sha}` |', file=sys.stderr)
    if not new:
        print(f'changelog-lines: nothing newer than {newest} on {page}', file=sys.stderr)
    return repo_setup_lines(new)


def report(page, published, generated, unit='revisions'):
    diff = [d for d in difflib.unified_diff(published, generated, 'published', 'generated',
                                            lineterm='', n=0)]
    changed = [d for d in diff if d[:1] in '+-' and d[:3] not in ('+++', '---')]
    pub_revs = sum(1 for line in published if not line.startswith('  * '))
    gen_revs = sum(1 for line in generated if not line.startswith('  * '))
    print(f'changelog-lines: {page}: {pub_revs} published {unit}, {gen_revs} generated, '
          f'{len(changed)} differing lines')
    for d in diff[2:]:
        print('    ' + d)
    return 1 if changed else 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='mode', required=True)
    c = sub.add_parser('connector')
    c.add_argument('--template', required=True)
    c.add_argument('--repo', required=True)
    c.add_argument('--range', required=True)
    c.add_argument('--version')
    c.add_argument('--verify', action='store_true',
                   help='regenerate the template page itself from --range and diff')
    s = sub.add_parser('server')
    s.add_argument('--repo', required=True)
    s.add_argument('--start', required=True)
    s.add_argument('--rev', required=True)
    s.add_argument('--exclude')
    s.add_argument('--verify', metavar='PAGE')
    r = sub.add_parser('repo-setup')
    r.add_argument('--repo', required=True, help='the mariadb-enterprise-scripts clone')
    r.add_argument('--rev', default='HEAD', help='the commit uploaded to the CDN')
    r.add_argument('--name', required=True, choices=['mariadb_repo_setup', 'mariadb_es_repo_setup'])
    r.add_argument('--page', required=True)
    r.add_argument('--verify', action='store_true',
                   help='render every entry and diff against the whole page')
    try:
        a = ap.parse_args(argv[1:])
    except SystemExit as e:
        return 2 if e.code else 0

    try:
        if a.mode == 'connector':
            if '..' not in a.range:
                raise Fail(f'--range must be A..B, got {a.range!r}')
            published = page_block(a.template)
            style = infer_style(published, a.template)
            generated = connector_lines(a.repo, a.range, style, a.version)
            if a.verify:
                return report(a.template, published, generated)
        elif a.mode == 'server':
            generated = server_lines(a.repo, a.start, a.rev, a.exclude)
            if a.verify:
                return report(a.verify, page_block(a.verify), generated)
        else:
            generated = repo_setup(a.repo, a.rev, a.name, a.page, a.verify)
            if isinstance(generated, int):
                return generated
    except Fail as exc:
        print(f'changelog-lines: {exc}', file=sys.stderr)
        return 2
    print('\n'.join(generated))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
