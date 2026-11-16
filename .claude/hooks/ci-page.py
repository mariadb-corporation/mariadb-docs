#!/usr/bin/env python3
"""ci-page.py — create and check a Community Server Changes & Improvements page.

WHY THIS EXISTS
    Each Community Server series gets a Changes & Improvements (C&I) page
    when its Preview (X.Y.0) is published on mariadb.org. mariadb.com only
    publishes the RC (X.Y.1) and the GA (X.Y.2 and later), and the RC and
    initial-GA release notes copy their body from the C&I page. So the page
    has to be right by the RC, and again by the initial GA.

    Nothing checked that. In November 2026 the 13.1 page, and the 13.1.1 RC
    notes copied from it, still listed 11 Preview_13.1 features that had
    moved to 13.2 or 13.3 or were never finished (DOCS-7111). Ralf
    Gebhardt's searches (2026-11-12) find both kinds of drift; `check` runs
    them (DOCS-7110).

CREATE (at Preview time)
    The page lists the MDEVs labeled Preview_X.Y. For the 12.3, 13.1, and
    13.2 previews that label named exactly the MDEVs of the first page.

    --todo cross-checks the label against the preview TODO, whose issue
    links name the MDEVs in the preview: directly (TODO-6130 for 13.1), or
    through one umbrella MDEV that links them in turn (TODO-6311 links
    MDEV-41087 "prepare 13.2 preview"). A linked MDEV without the label
    (MDEV-33463 on TODO-6130) and a labeled MDEV the TODO doesn't link are
    reported, not listed or dropped. So is a listed MDEV that is not
    Closed/Fixed, or whose fix versions don't name the series.

    The text is the Release Note Summary (customfield_13206), else the Jira
    summary, with rn-generate.py's rules (flattened to one line, no trailing
    period, Markdown-escaped), followed by the key link. Items sort by key
    number. The page around the list is the one Sergei Golubchik and dbart
    wrote for 12.3, 13.1, and 13.2: the description, the title, the latest-X.Y include
    (or, with --banner, `hidden: true` and the unreleased include), the
    release-model sentence, "## New Features", the license line, and the
    feedback form.

    The result is a draft. The 12.3 page dropped 2 of its 15 linked MDEVs
    and reworded 9 of the 13 it kept.

CHECK (at RC and initial-GA time)
    Ralf's searches, with X.Y.1 the RC and X.Y.2 the GA:
      A  labels = Preview_X.Y AND fixVersion not in (X.Y.1, X.Y.2)
         flagged for the preview, not in the series
      B  project = MDEV AND fixVersion in (X.Y.1) AND type in (Epic, "New Feature")
         at the RC
      C  the same with fixVersion in (X.Y.1, X.Y.2), at the GA
    plus one of ours:
      D  labels = Preview_X.Y AND fixVersion in (<stage versions>)
         preview items that are in the series, whatever their type (B and
         C miss a Task or a Bug, such as MDEV-24813 in 13.1)

    Reported, for the C&I page and for each --also page (the RC or GA
    release notes, whose body is a copy):
      * remove: an A item on the page whose fix versions are all outside
        the series (it moved to a later one)
      * check:  an A item on the page still targeted at X.Y but unresolved,
        or with no fix version (it may still land in X.Y.2)
      * missing: a B/C or D item not on the page. Not every one belongs:
        an internal task filed as a New Feature (MDEV-39548 in 13.1) is
        left out on purpose.
    A key counts as on the page if it appears anywhere in it.

PROVEN
    On DOCS-7110 (2026-11-12):
      * create reproduced the MDEV sets of the 13.1 page as first committed
        (5e5b52cc7, 32 of 32) and of the 13.2 page (7ef349204, 17 of 17),
        and listed all 15 of 12.3's, the 13 its page kept plus the 2
        dropped by hand. --todo agreed with the label for TODO-6130,
        TODO-6311 (through MDEV-41087), and TODO-5769, apart from
        MDEV-33463, which TODO-6130 links without the label.
      * check --stage rc on 13.1 found the 11 items of DOCS-7111 (8 remove,
        3 check) on both the C&I page and 13.1.1.md, and the RC features
        missing from the page.

USAGE
    ci-page.py create --series 13.2 (--prev 13.1 | --long-term "June 2029")
                      --out <page> [--todo TODO-6311]
                      [--banner unreleased-13.2.md] [--force]
    ci-page.py check  --series 13.1 --stage rc|ga --page <C&I page>
                      [--also <release notes page> ...]

    The token is found as for rn-generate.py ($JIRA_MARIADB_TOKEN, or the
    file named by $JIRA_MARIADB_TOKEN_FILE, default
    ~/.config/mariadb-jira/token). It is never printed. Read-only: the
    script only reads jira.mariadb.org, and writes only --out.

Exit: create: 0 = page written. check: 0 = nothing to report, 1 =
differences listed. 2 = usage error, missing token, or no MDEV with the
label.
"""

import argparse
import importlib.util
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CS = ROOT / 'release-notes' / 'community-server'
INCLUDES = ROOT / 'release-notes' / '.gitbook' / 'includes'

# The Jira access and the bullet text rules are rn-generate.py's, so the two
# pages a release gets read the same.
_spec = importlib.util.spec_from_file_location('rn_generate', HERE / 'rn-generate.py')
rn = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rn)

KEY_RE = re.compile(r'MDEV-\d+')
LICENSE = '<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>'
FORM = '{% @marketo/form formid="4316" formId="4316" %}'


def die(msg):
    print(f'ci-page: {msg}', file=sys.stderr)
    sys.exit(2)


def note(msg=''):
    print(msg, file=sys.stderr)


def issue(tok, key):
    req = urllib.request.Request(f'{rn.JIRA}/rest/api/2/issue/{key}?fields=summary,issuelinks',
                                 headers={'Authorization': 'Bearer ' + tok})
    return json.load(urllib.request.urlopen(req))


def by_keys(tok, keys):
    out = []
    for n in range(0, len(keys), 100):
        out += rn.search(tok, f'issuekey in ({",".join(keys[n:n + 100])})')
    return out


def done(f):
    return f['status']['name'] in ('Closed', 'Done') and (f['resolution'] or {}).get('name') in ('Fixed', 'Done')


def fix_versions(f):
    return [v['name'] for v in f['fixVersions']]


def in_series(name, series):
    return name == series or name.startswith(series + '.')


def ci_link(series):
    """The relative link from one series' C&I page to another's."""
    for d in (CS / series, CS / 'old-releases' / series):
        pages = sorted(d.glob('*changes-and-improvements*.md'))
        if pages:
            return pages[0].relative_to(CS).as_posix()
    die(f'no Changes & Improvements page for {series} under {CS.relative_to(ROOT)}')


def latest_include(series):
    for name in (f'latest-{series}.md', f'latest-{series.replace(".", "-")}.md'):
        if (INCLUDES / name).exists():
            return name
    name = f'latest-{series}.md'
    note(f'note: release-notes/.gitbook/includes/{name} does not exist yet; create it with the page')
    return name


def mdev_links(tok, key):
    return {k for l in issue(tok, key)['fields']['issuelinks']
            for k in [(l.get('outwardIssue') or l.get('inwardIssue'))['key']] if k.startswith('MDEV-')}


def create(a):
    tok = rn.token()
    label = f'Preview_{a.series}'
    listed = sorted(rn.search(tok, f'project = MDEV AND labels = {label}'), key=lambda i: rn.key_num(i['key']))
    if not listed:
        die(f'no MDEV is labeled {label}')
    note(f'{len(listed)} MDEVs labeled {label}, listed')

    if a.todo:
        labeled = {i['key'] for i in listed}
        linked = mdev_links(tok, a.todo)
        for k in sorted(linked - labeled, key=rn.key_num):
            # An umbrella ("prepare 13.2 preview") links the preview's MDEVs itself.
            below = mdev_links(tok, k) - {a.todo}
            if below & labeled:
                note(f'  {a.todo} links {k}, which links {len(below)} MDEVs: following it')
                linked |= below
        missing = sorted(linked - labeled, key=rn.key_num)
        for i in by_keys(tok, missing) if missing else []:
            if not (mdev_links(tok, i['key']) & labeled):
                note(f'  linked from {a.todo}, no {label} label, left out: {i["key"]} {i["fields"]["summary"]}')
        for k in sorted(labeled - linked, key=rn.key_num):
            note(f'  labeled, not linked from {a.todo}, listed: {k}')
    for i in listed:
        f = i['fields']
        why = []
        if not done(f):
            why.append(f'{f["status"]["name"]}/{(f["resolution"] or {}).get("name") or "unresolved"}')
        if not any(in_series(v, a.series) for v in fix_versions(f)):
            why.append('fix version ' + (', '.join(fix_versions(f)) or 'none'))
        if why:
            note(f'  listed, check: {i["key"]} ({"; ".join(why)}) {f["summary"]}')
    without_rns = sum(1 for i in listed if not (i['fields'].get('customfield_13206') or '').strip())
    note(f'  {without_rns} of {len(listed)} have no Release Note Summary and use the Jira summary')

    if a.long_term:
        model = (f'MariaDB {a.series} is a [long term release](../about/release-model.md), '
                 f'maintained until {a.long_term}.')
    else:
        model = (f'MariaDB {a.series} is a [rolling release](../about/release-model.md). It is an evolution of '
                 f'[MariaDB {a.prev}](../{ci_link(a.prev)}) with many entirely new features.')
    include = a.banner or latest_include(a.series)
    bullets = []
    for i in listed:
        text, _ = rn.bullet_text(i['fields'])
        bullets.append(f' * {text} ([{i["key"]}]({rn.JIRA}/browse/{i["key"]}))')
    page = '\n'.join([
        '---',
        'description: >-',
        "  An overview of changes, improvements, and what's new in MariaDB Community",
        f'  Server {a.series}',
        *(['hidden: true'] if a.banner else []),
        '---',
        '',
        f'# MariaDB {a.series} Changes & Improvements',
        '',
        f'{{% include "../../.gitbook/includes/{include}" %}}',
        '',
        model,
        '',
        '## New Features',
        '',
        *bullets,
        '',
        LICENSE,
        '',
        FORM,
        ''])
    out = pathlib.Path(a.out)
    if out.exists() and not a.force:
        die(f'{out} exists; it may hold hand edits (--force to overwrite)')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    note(f'wrote {out}')
    return 0


def check(a):
    tok = rn.token()
    s = a.series
    rc, ga = f'{s}.1', f'{s}.2'
    stage = [rc] if a.stage == 'rc' else [rc, ga]
    label = f'Preview_{s}'
    features = 'B' if a.stage == 'rc' else 'C'
    queries = {
        'A': f'labels = {label} AND fixVersion not in ({rc}, {ga})',
        features: f'project = MDEV AND fixVersion in ({", ".join(stage)}) AND type in (Epic, "New Feature")',
        'D': f'labels = {label} AND fixVersion in ({", ".join(stage)})',
    }
    found = {q: sorted(rn.search(tok, jql), key=lambda i: rn.key_num(i['key'])) for q, jql in queries.items()}
    note(f'{s} {a.stage.upper()} ({", ".join(stage)}):')
    for q, jql in queries.items():
        url = f'{rn.JIRA}/issues/?' + urllib.parse.urlencode({'jql': jql})
        note(f'  {q}: {len(found[q])} — {url}')

    expected = {i['key']: i for i in found[features] + found['D']}
    total = 0
    for path in [a.page] + (a.also or []):
        if path != a.page and not pathlib.Path(path).exists():
            # The release notes are written from the C&I page, so at first they don't exist.
            note(f'  {path} does not exist yet: not checked')
            continue
        text = pathlib.Path(path).read_text()
        on = set(KEY_RE.findall(text))
        differences = 0
        print(f'\n## {path}')
        for i in found['A']:
            if i['key'] not in on:
                continue
            f = i['fields']
            fv = fix_versions(f)
            if fv and not any(in_series(v, s) for v in fv):
                verdict = f'remove: now {", ".join(fv)}'
            else:
                verdict = (f'check: {f["status"]["name"]}/{(f["resolution"] or {}).get("name") or "unresolved"}, '
                           f'fix version {", ".join(fv) or "none"}')
            print(f'  {verdict} | {i["key"]} {f["summary"]}')
            differences += 1
        for k, i in sorted(expected.items(), key=lambda kv: rn.key_num(kv[0])):
            if k in on:
                continue
            f = i['fields']
            rns = 'RNS' if (f.get('customfield_13206') or '').strip() else 'no RNS'
            print(f'  missing: {f["issuetype"]["name"]}, {f["status"]["name"]}, {rns} | {k} {f["summary"]}')
            differences += 1
        if not differences:
            print('  nothing to report')
        total += differences
    return 1 if total else 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('create', help='draft the page from the preview TODO')
    c.add_argument('--todo', help='the preview TODO to cross-check the label against, e.g. TODO-6311')
    c.add_argument('--series', required=True, help='e.g. 13.2')
    model = c.add_mutually_exclusive_group(required=True)
    model.add_argument('--prev', help='rolling release: the previous series, e.g. 13.1')
    model.add_argument('--long-term', metavar='UNTIL', help='long-term release: end of maintenance, e.g. "June 2029"')
    c.add_argument('--banner', help='unreleased include, e.g. unreleased-13.2.md; holds the page back')
    c.add_argument('--out', required=True, help='the page to write')
    c.add_argument('--force', action='store_true', help='overwrite an existing page')
    k = sub.add_parser('check', help="diff the page against Ralf's searches")
    k.add_argument('--series', required=True, help='e.g. 13.1')
    k.add_argument('--stage', required=True, choices=('rc', 'ga'))
    k.add_argument('--page', required=True, help='the C&I page')
    k.add_argument('--also', action='append', help='a release notes page copied from it; repeatable')
    a = ap.parse_args(argv)
    if not re.fullmatch(r'\d+\.\d+', a.series):
        die(f'--series {a.series}: expected X.Y')
    return create(a) if a.cmd == 'create' else check(a)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
