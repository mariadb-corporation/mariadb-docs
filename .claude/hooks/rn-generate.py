#!/usr/bin/env python3
"""rn-generate.py — draft a Community Server release notes page from Jira and git.

WHY THIS EXISTS
    Community Server release notes have come from the "Release Notes script"
    Apps Script project: create_CS_RN_doc_v2() in CreateCSReleaseNoteDoc.gs,
    which writes a Google Doc that is then edited and pasted into GitBook.
    DOCS-7099 (2026 Q4) reimplemented it from its source and compared the
    outputs. The script's scope comes from RN_VERSION_CONFIG in
    ConfigurationService.gs, and that drops fixes:

      * Its base query is one version, the last entry of supportedCS (11.8 in
        Q4), limited to the next versions of the ES-tracked branches
        (supportedES: 10.6, 11.4, 11.8). Each other series gets only the base
        issues that also carry its tag. So 10.11-only fixes vanish (6 in Q4),
        and the 12.3 list is the 11.8 list again (32 12.3-only fixes missing).
      * It trusts the Jira fix version. In Q4, 13 to 22 tagged fixes per
        release had commits outside the release revision, and fixes that did
        ship carried a stale Q3 tag or no tag for the series.

    This script applies the script's field rules per release, from that
    release's own fix version, then corrects the list against the release
    commits. It only reads: jira.mariadb.org over REST, and `git log` in the
    server clone. It never fetches, checks out, or resets.

SELECTION (the script's field rules, from RN_buildMaintenanceJQL)
    An issue qualifies when all of these hold:
      * project MDEV
      * status Closed or Done, resolution Fixed or Done
      * Bug Category (customfield_13205) is set and is not "Not for Release
        Notes". The script's JQL says `"Bug Category" not in (...)`, which
        never matches an empty field, so an uncategorized issue is out, even a
        New Feature with a Release Note Summary.
      * not a non-Task whose Affects Version is "N/A" (MDEV-40229 in Q4)
    Not reproduced: the script's backport-label clause (cf[11404] =
    RM_BACKPORT_<year>_Q<n>) selected nothing extra in Q4.

CORRECTION AGAINST THE RELEASE COMMITS (--no-correct turns it off)
    * Remove a selected issue when some commit names it, but none reachable
      from --rev does: the fix landed after the release revision.
    * Add an issue named in the SUBJECT of a commit in <prev-tag>..<rev>,
      never mentioned in the previous tag's history, that passes the field
      rules, whatever its fix version says. Subjects only, because bodies and
      test names mention unrelated keys ("galera.MDEV-38260 fails").
    * Keep, and flag, a selected issue that no commit names at all: it may be
      fixed in another repository (the Galera library, DuckDB) or under
      another MDEV. Ask before dropping it.
    The report on stderr also lists issues named in new commits that fail the
    field rules while still unresolved: ask engineering about those.

LAYOUT (as create_CS_RN_doc_v2() writes it)
    One section per issue's FIRST component (no component: "General"); a
    component of "N/A" becomes "OTHER", as on published pages. Sections sort
    alphabetically, ignoring case; items sort by key. The text is the Release
    Note Summary (customfield_13206), else the Jira summary, flattened to one
    line, without a trailing period (house style), Markdown-escaped outside
    code spans. One deliberate difference from the script: the storage
    engines nest under "### Storage Engines", InnoDB first, as on published
    pages.

    The page around the list is the previous release's page (--template): its
    header up to "## Notable Items" and its "## Changelog" footer, with the
    version replaced. Sections the editor writes by hand (General, Security)
    are not generated. With --banner, the page is held back: `hidden: true`,
    the unreleased banner after the title, and TBD for the date.

REVIEW FLAGS (--flags TSV: key, section, reasons, text)
    The patterns Daniel's Q3 editorial pass removed or changed (DOCS-6477,
    commits cad8b64f8 and 9df256153): Tests/CI components, bare debug
    assertions and sanitizer reports without a Release Note Summary, the
    `Security` label (check against the CVE list), items already on the
    previous page, items without a Release Note Summary, and items added from
    the commits. The script never removes a flagged item; the editor decides.

PROVEN
    On DOCS-7099 (2026-11-10), with --no-correct, 11.8.10 reproduced the
    script's Google Doc exactly (236 of 236 issues, all in the same section);
    10.11.20, 11.4.14, and 12.3.4 contained every issue the script listed,
    plus exactly the fixes its version scope cannot reach.

USAGE
    rn-generate.py --version 11.8.10 --prev-tag mariadb-11.8.9 --rev <sha>
                   --repo <server clone> --template <previous RN page>
                   --out <new RN page> [--banner unreleased-11-8.md]
                   [--flags FILE.tsv] [--report FILE.json] [--no-correct]

    The token comes from $JIRA_MARIADB_TOKEN, or the file named by
    $JIRA_MARIADB_TOKEN_FILE (default ~/.config/mariadb-jira/token), as for
    the prep-changelog skill. It is never printed.

Exit: 0 = page written, 2 = usage error, missing token, or a ref git cannot
resolve.
"""

import argparse
import collections
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.parse
import urllib.request

JIRA = 'https://jira.mariadb.org'
FIELDS = ('versions,resolutiondate,summary,status,resolution,components,customfield_13205,'
          'customfield_13206,issuetype,labels,fixVersions,project')
KEY_RE = re.compile(r'MDEV-\d+')
SE = 'Storage Engine - '
TESTS = {'Tests, MTR', 'CI'}
DEBUG_RE = re.compile(r'assert|asan|msan|ubsan|valgrind|sanitizer|heap-use-after|use-of-uninit', re.I)


def die(msg):
    print(f'rn-generate: {msg}', file=sys.stderr)
    sys.exit(2)


def token():
    tok = os.environ.get('JIRA_MARIADB_TOKEN')
    if not tok:
        path = os.environ.get('JIRA_MARIADB_TOKEN_FILE') or os.path.expanduser('~/.config/mariadb-jira/token')
        try:
            tok = pathlib.Path(path).read_text().strip()
        except OSError:
            die('no jira.mariadb.org token: see .claude/README.md › Setup, step 3')
    return tok


def search(tok, jql):
    out, start = [], 0
    while True:
        q = urllib.parse.urlencode({'jql': jql, 'fields': FIELDS, 'startAt': start,
                                    'maxResults': 200, 'validateQuery': 'false'})
        req = urllib.request.Request(f'{JIRA}/rest/api/2/search?{q}',
                                     headers={'Authorization': 'Bearer ' + tok})
        d = json.load(urllib.request.urlopen(req))
        out += d['issues']
        start += len(d['issues'])
        if start >= d['total'] or not d['issues']:
            return out


def git_keys(repo, *args):
    r = subprocess.run(['git', '-C', repo, 'log', *args], capture_output=True, text=True)
    if r.returncode:
        die(f'git log {" ".join(args)}: {r.stderr.strip()}')
    return set(KEY_RE.findall(r.stdout))


def qualifies(i):
    """The script's field rules, without the fix version."""
    f = i['fields']
    cat = (f.get('customfield_13205') or {}).get('value')
    affects = {v['name'] for v in f.get('versions') or []}
    return (i['key'].startswith('MDEV-')
            and (f['resolution'] or {}).get('name') in ('Fixed', 'Done')
            and f['status']['name'] in ('Closed', 'Done')
            and cat not in (None, 'Not for Release Notes')
            and not (f['issuetype']['name'] != 'Task' and 'N/A' in affects))


def section(f):
    comps = [c['name'] for c in f['components']]
    if not comps:
        return 'General'
    return 'OTHER' if comps[0] == 'N/A' else comps[0]


def escape(text):
    """Escape Markdown outside code spans; turn `x' into `x`."""
    text = re.sub(r"`([^`']+)'", r'`\1`', text)
    out = []
    for part in re.split(r'(`[^`]*`)', text):
        if len(part) > 1 and part.startswith('`') and part.endswith('`'):
            out.append(part)
        else:
            part = re.sub(r'(?<!\\)([_*])', r'\\\1', part)
            out.append(part.replace('<', '\\<').replace('`', '\\`'))
    return ''.join(out)


def bullet_text(f):
    rns = (f.get('customfield_13206') or '').strip()
    text = ' '.join((rns or f['summary'].strip()).split()).rstrip('.').rstrip()
    return re.sub(r'^#', r'\\#', escape(text)), bool(rns)


def key_num(k):
    return int(k.split('-')[1])


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--version', required=True, help='the release, e.g. 11.8.10')
    ap.add_argument('--prev-tag', required=True, help='the previous release tag, e.g. mariadb-11.8.9')
    ap.add_argument('--rev', required=True, help='the release revision from the TODO ticket')
    ap.add_argument('--repo', required=True, help='the server clone')
    ap.add_argument('--template', required=True, help="the previous release's release notes page")
    ap.add_argument('--out', required=True, help='the page to write')
    ap.add_argument('--banner', help='unreleased include, e.g. unreleased-11-8.md; holds the page back')
    ap.add_argument('--flags', help='write review flags to this TSV')
    ap.add_argument('--report', help='write the corrections to this JSON')
    ap.add_argument('--no-correct', action='store_true', help='fix-version selection only, as the script does')
    a = ap.parse_args(argv)

    try:
        template = pathlib.Path(a.template).read_text()
        head = template[:template.index('## Notable Items')]
        foot = template[template.index('## Changelog'):]
    except (OSError, ValueError):
        die(f'{a.template}: unreadable, or no "## Notable Items" / "## Changelog" heading')
    prev_version = a.prev_tag.removeprefix('mariadb-')

    tok = token()
    tagged = {i['key']: i for i in search(tok, f'fixVersion = "{a.version}" ORDER BY key')}
    selected = {k for k, i in tagged.items() if qualifies(i)}
    chosen = {k: tagged[k] for k in selected}
    report = {'removed': [], 'added': [], 'kept_no_commit': [], 'unresolved_committed': []}

    if not a.no_correct:
        in_rev = git_keys(a.repo, a.rev, '--format=%B')
        in_prev = git_keys(a.repo, a.prev_tag + '^{commit}', '--format=%B')
        new = git_keys(a.repo, f'{a.prev_tag}^{{commit}}..{a.rev}', '--format=%s') - in_prev
        anywhere = git_keys(a.repo, '--all', '--since=2024-01-01', '--format=%B')
        for k in sorted(selected, key=key_num):
            if k not in in_rev:
                if k in anywhere:
                    report['removed'].append(k)
                    del chosen[k]
                else:
                    report['kept_no_commit'].append(k)
        cand = sorted(new - selected, key=key_num)
        for n in range(0, len(cand), 100):
            for i in search(tok, f'issuekey in ({",".join(cand[n:n + 100])})'):
                f = i['fields']
                if qualifies(i):
                    chosen[i['key']] = i
                    report['added'].append([i['key'], [v['name'] for v in f['fixVersions']], f['summary']])
                elif not f['resolution'] and i['key'].startswith('MDEV-'):
                    report['unresolved_committed'].append([i['key'], f['status']['name'], f['summary']])
        for lst in report.values():
            lst.sort(key=lambda x: key_num(x[0] if isinstance(x, list) else x))

    groups = collections.defaultdict(list)
    for i in chosen.values():
        groups[section(i['fields'])].append(i)
    for s in groups:
        groups[s].sort(key=lambda i: key_num(i['key']))
    engines = sorted((s for s in groups if s.startswith(SE)), key=lambda s: (s != SE + 'InnoDB', s.lower()))
    others = sorted((s for s in groups if not s.startswith(SE)), key=str.lower)

    def items(s):
        return '\n'.join(f"* {bullet_text(i['fields'])[0]} ([{i['key']}]({JIRA}/browse/{i['key']}))"
                         for i in groups[s]) + '\n'

    body = ['## Notable Items\n']
    if engines:
        body.append('### Storage Engines\n')
        for s in engines:
            body += [f'#### {s[len(SE):]} Storage Engine\n', items(s)]
    for s in others:
        body += [f'### {s}\n', items(s)]

    pv = re.escape(prev_version)
    head = re.sub(pv, a.version, head)
    foot = re.sub(pv, a.version, foot)
    if a.banner:
        head = re.sub(r'released on \d{4}-\d{2}-\d{2}', 'released on TBD', head)
        head = head.replace('\n---\n\n# ', '\nhidden: true\n---\n\n# ', 1)
        head = re.sub(r'(# MariaDB [\d.]+ Release Notes\n)',
                      r'\1\n{% include "../../.gitbook/includes/' + a.banner + '" %}\n', head, count=1)
        head = re.sub(r'\*\*Release date:\*\* .*', '**Release date:** TBD', head)
    pathlib.Path(a.out).write_text(head + '\n'.join(body) + '\n' + foot)

    added = {r[0]: r[1] for r in report['added']}
    prev_keys = set(KEY_RE.findall(template))
    rows = []
    for s in engines + others:
        for i in groups[s]:
            f = i['fields']
            text, has_rns = bullet_text(f)
            why = []
            if {c['name'] for c in f['components']} & TESTS:
                why.append('test/CI component')
            if not has_rns and DEBUG_RE.search(f['summary']):
                why.append('debug/sanitizer report, no RNS')
            if 'security' in {l.lower() for l in f['labels']}:
                why.append('Security label: check against the CVE list')
            if i['key'] in prev_keys:
                why.append('already listed on the previous page')
            if not has_rns:
                why.append('no RNS: Jira summary used')
            if i['key'] in added:
                why.append('added from the release commits; Jira fix version is '
                           + (','.join(added[i['key']]) or 'empty'))
            rows.append((i['key'], s, '; '.join(why), text[:90]))
    if a.flags:
        pathlib.Path(a.flags).write_text(''.join('\t'.join(r) + '\n' for r in rows))
    if a.report:
        pathlib.Path(a.report).write_text(json.dumps(report, indent=1) + '\n')

    count = lambda s: sum(1 for r in rows if s in r[2])
    print(f'{a.version}: {len(chosen)} items in {len(groups)} sections '
          f'(fix version selected {len(selected)}, removed {len(report["removed"])}, '
          f'added {len(report["added"])}); flags: {count("test/CI")} test/CI, '
          f'{count("debug/sanitizer")} debug/sanitizer, {count("Security label")} Security, '
          f'{count("no RNS")} without RNS', file=sys.stderr)
    for name, lst in report.items():
        if lst:
            keys = [x[0] if isinstance(x, list) else x for x in lst]
            print(f'  {name}: {" ".join(keys)}', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
