#!/usr/bin/env python3
"""release_announce.py — list the release notes a push published, for every product (DOCS-7076).

Compares two commits and prints, as JSON, every release note in the Release Notes space that is
published at AFTER but was not at BEFORE. The workflow announce-release-notes.yml posts each one
to #mariadb-product-releases. It began as cloud_release_announce.py (DOCS-6936, MariaDB Cloud
only); DOCS-7076 widened it to every product, so the docs are where the whole portfolio's
releases get announced.

WHAT COUNTS AS A RELEASE NOTE
  The space mixes release notes with changelogs, "What's New", lifecycle, compatibility and
  index pages, and every product names its files differently (13.0.2.md, 11.8.9-6.md,
  release-notes_9.1.8.md, mariadb-cloud-2026.10.12.md, ...). So a file is judged by what it says
  about itself, not by its name. A page is a release note when all of these hold:

    - it is a Markdown file inside a product folder (release-notes/<product>/...), not under
      .gitbook/;
    - it is not README.md or all-releases.md, and "changelog" is not in its path;
    - its H1 says "Release Notes", or its file name carries a version and its `description:`
      says it "is a ... release" (Enterprise Operator notes are titled just
      "MariaDB Enterprise Kubernetes Operator 25.10.5").

PUBLISHED, NOT ADDED
  Notes are routinely merged hidden and unhidden when the release ships (Cloud, Enterprise
  Server, Enterprise Manager, GridGain all do it). Announcing on file creation would post a
  release that has not happened. A note is published at a commit when it is a release note
  there, release-notes/SUMMARY.md lists it, and neither it nor any of its nav ancestors says
  `hidden: true` (GitBook drops a hidden page's children from the navigation too).

  A note announces on the push where it goes from not-published to published, whichever of
  those changed. BEFORE is checked for visibility only, so an edit that merely changes whether
  an already-visible page looks like a release note never announces it. Nothing remembers what was already announced, so a note that is hidden again
  and later unhidden is announced a second time.

NOT EVERY NEWLY PUBLISHED NOTE IS NEWS
  The space also receives migrations (47 GridGain 9 notes in one PR), backfills (17 Connector/C++
  changelogs, a missing 2021 note) and renames. Posting those would flood a company-wide
  channel with years-old releases. Two guards, both reported rather than silent:

    - STALE: the note states a release date (a "Release date:" line, or "released on
      YYYY-MM-DD" / "published 13 August 2026" in its description or opening text) older than MAX_AGE_DAYS
      before the AFTER commit. A note with no date at all (GridGain, MaxScale's older notes)
      passes this guard.
    - TOO MANY: more than MAX_NOTES notes survive in one push. Then none is announced. A real
      release day publishes a handful; dozens means a restructure. Re-run with a higher limit
      from workflow_dispatch if they really are new.

  A third guard holds back a note whose title or URL is still a placeholder
  ("MariaDB Cloud <YYYY.MM.DD> Release Notes", which DOCS-6320 listed in the nav unhidden).

  Skipped notes go in "skipped" with the reason, and the workflow reports them to
  #docs-notifications so a wrongly dated release never vanishes unnoticed.

THE MESSAGE
  The H1 in bold (it names the product and version, and for Cloud the feature), the note's own
  `description:`, and the live URL. The description is read with desccheck.py's parser, so the
  text desccheck gates is the text that gets posted (DOCS-6586: one parser or none).

  The URL comes from the note's position in SUMMARY.md, computed by the help-tables
  nav_entries(), because GitBook publishes a page at its nav position, not its file path (the
  GridGain 9 notes differ). The workflow still fetches each URL and refuses to post one that
  does not answer 200.

Usage: release_announce.py BEFORE AFTER     (commit SHAs or refs, both must be local)
Env:   MAX_AGE_DAYS (default 30), MAX_NOTES (default 10)
Exit:  0 success (nothing to announce is success), 1 git failure, 2 usage error.
"""
import datetime
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '.claude', 'hooks'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'help-tables'))
from desccheck import FRONTMATTER, H1, parse  # noqa: E402
from markdown_extractor import nav_entries  # noqa: E402

SPACE = 'release-notes'
SUMMARY = SPACE + '/SUMMARY.md'
SITE = 'https://mariadb.com/docs/'
HIDDEN = re.compile(r'^hidden:\s*true\s*$', re.M)
VERSION_IN_NAME = re.compile(r'\d+\.\d+')
IS_A_RELEASE = re.compile(r'\bis an? [^.]{0,80}\brelease\b', re.I)
RELEASE_NOTES = re.compile(r'release notes', re.I)
# A draft listed in the nav before its reveal ("MariaDB Cloud <YYYY.MM.DD> Release Notes",
# DOCS-6320) must not reach a company-wide channel.
PLACEHOLDER = re.compile(r'<[^>]*>|\bYYYY\b|\bTBD\b', re.I)

# "**Release date:** 15 Sep 2026", "**Release Date:** 3 November 2026", "**Release date**: ..."
DATE_LINE = re.compile(r'release date\W{0,6}\s*([A-Za-z0-9, -]{8,30})', re.I)
DATE_IN_DESC = re.compile(r'(?:released|published) (?:on )?'
                          r'(\d{4}-\d{2}-\d{2}|\d{1,2} [A-Za-z]+ \d{4}|[A-Za-z]+ \d{1,2},? \d{4})')
DATE_FORMATS = ('%Y-%m-%d', '%d %b %Y', '%d %B %Y', '%b %d %Y', '%B %d %Y', '%b %d, %Y',
                '%B %d, %Y')


def git(*args):
    return subprocess.run(('git',) + args, check=True, capture_output=True,
                          text=True).stdout


def read_tree(ref):
    """{path: text} for every Markdown file in the space at ref, read in one git process."""
    paths = [p for p in git('ls-tree', '-r', '--name-only', ref, SPACE + '/').split('\n')
             if p.endswith('.md')]
    if not paths:
        return {}
    stdin = ''.join(f'{ref}:{p}\n' for p in paths).encode()
    out = subprocess.run(['git', 'cat-file', '--batch'], input=stdin, check=True,
                         capture_output=True).stdout
    files, pos = {}, 0
    for p in paths:
        nl = out.index(b'\n', pos)
        size = int(out[pos:nl].split()[2])
        files[p] = out[nl + 1:nl + 1 + size].decode('utf-8', 'replace')
        pos = nl + 1 + size + 1
    return files


def is_hidden(text):
    m = FRONTMATTER.match(text or '')
    return bool(m and HIDDEN.search(m.group(1)))


def body(text):
    return FRONTMATTER.sub('', text, count=1)


def title(text):
    m = H1.search(body(text))
    return m.group(1) if m else ''


def description(text):
    d = parse(text)
    return d[2] if d else ''


def is_release_note(path, text):
    parts = path.split('/')
    name = parts[-1]
    if len(parts) < 3 or parts[1].startswith('.'):
        return False
    if name in ('README.md', 'all-releases.md') or 'changelog' in path.lower():
        return False
    if RELEASE_NOTES.search(title(text)):
        return True
    return bool(VERSION_IN_NAME.search(name) and IS_A_RELEASE.search(description(text)))


def release_date(text):
    """The release date the note states, or None."""
    head = body(text)[:3000]
    candidates = [m.group(1) for m in DATE_IN_DESC.finditer(description(text))]
    candidates += [m.group(1) for m in DATE_LINE.finditer(head)]
    candidates += [m.group(1) for m in DATE_IN_DESC.finditer(head)]
    for raw in candidates:
        raw = raw.strip().rstrip('.,')
        for fmt in DATE_FORMATS:
            for cut in range(len(raw), 7, -1):   # tolerate trailing words after the date
                try:
                    return datetime.datetime.strptime(raw[:cut].strip(), fmt).date()
                except ValueError:
                    continue
    return None


def visible(ref):
    """{path: (page text, nav entry)} for every page of the space published at ref."""
    files = read_tree(ref)
    summary = files.get(SUMMARY)
    if summary is None:
        return {}
    found = {}
    for path, entry in nav_entries(summary, SPACE, SPACE).items():
        text = files.get(path)
        if text is None or is_hidden(text):
            continue
        if any(is_hidden(files.get(p)) for p in entry['parents']):
            continue
        found[path] = (text, entry)
    return found


def published(ref):
    """{path: (page text, nav entry)} for every release note published at ref."""
    return {p: v for p, v in visible(ref).items() if is_release_note(p, v[0])}


def describe(path, text, entry):
    d = release_date(text)
    return {
        'file': path,
        'title': title(text) or path.rsplit('/', 1)[-1][:-3],
        'description': description(text),
        'url': SITE + entry['url'],
        'released': d.isoformat() if d else None,
    }


def commit_date(ref):
    return datetime.date.fromisoformat(git('log', '-1', '--format=%cs', ref).strip())


def newly_published(before, after, max_age_days=30, max_notes=10):
    """{'announce': [...], 'skipped': [...]}, each sorted by release date, then file."""
    # BEFORE is checked for visibility only, not re-classified: an edit that makes an
    # already-published page look like a release note (a reworded H1 or description, as
    # DOCS-6765 did to two Cloud notes) must not announce it again.
    was = visible(before)
    now = published(after)
    new = [describe(p, *now[p]) for p in now if p not in was]
    new.sort(key=lambda n: (n['released'] or '9999', n['file']))

    cutoff = commit_date(after) - datetime.timedelta(days=max_age_days)
    announce, skipped = [], []
    for n in new:
        if PLACEHOLDER.search(n['title'] + ' ' + n['url']):
            skipped.append(dict(n, reason='title or URL is still a placeholder'))
        elif n['released'] and datetime.date.fromisoformat(n['released']) < cutoff:
            skipped.append(dict(n, reason=f'released {n["released"]}, more than '
                                          f'{max_age_days} days before this push'))
        else:
            announce.append(n)
    if len(announce) > max_notes:
        skipped += [dict(n, reason=f'{len(announce)} notes published in one push '
                                   f'(limit {max_notes}): looks like a migration or backfill')
                    for n in announce]
        announce = []
    return {'announce': announce, 'skipped': skipped}


def main(argv):
    if len(argv) != 3:
        print(__doc__.split('Usage: ')[1].split('\n')[0], file=sys.stderr)
        return 2
    try:
        result = newly_published(argv[1], argv[2],
                                 int(os.environ.get('MAX_AGE_DAYS') or 30),
                                 int(os.environ.get('MAX_NOTES') or 10))
    except subprocess.CalledProcessError as e:
        print(f'git failed: {e.stderr.strip() if isinstance(e.stderr, str) else e.stderr}',
              file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
