#!/usr/bin/env python3
"""cloud_release_announce.py — list the MariaDB Cloud release notes a push published (DOCS-6936).

Compares two commits and prints, as JSON, every Cloud release note that is published at AFTER
but was not at BEFORE, oldest first. The workflow announce-cloud-release-notes.yml posts each
one to #mariadb-product-releases.

PUBLISHED, NOT ADDED
  Cloud release notes are routinely merged with `hidden: true` and unhidden days later, once the
  release ships (the 2026.10.12 BYOC note, DOCS-6673; the Query Result Cache note, DOCS-6392).
  Announcing on file creation would post a release that has not happened. So a note counts as
  published when all three hold at a commit:

    - the file exists under release-notes/mariadb-cloud-release-notes/ and is named
      mariadb-cloud-YYYY.MM.DD*.md (README.md and all-releases.md are not release notes);
    - its frontmatter does not say `hidden: true`;
    - release-notes/SUMMARY.md links to it, so it is in the navigation.

  A note announces on the push where it goes from not-published to published, whichever of the
  three changed. Nothing needs to remember what was already announced -- with one consequence:
  a note that is hidden again and later unhidden is announced a second time.

THE MESSAGE
  Matches the post Adam Luciano made by hand on 2026-10-01: the release note's own `description:`
  (which every Cloud release note opens with "MariaDB Cloud <version> is a <maturity> release,
  released on <date>. It ..."), and the live URL. The H1 goes first in bold because it carries
  the feature name ("... Release Notes: Query Result Cache"), which the ticket asks for.

  The description is read with desccheck.py's parser, not a second one: the same text desccheck
  gates is the text that gets posted (DOCS-6586: one parser or none).

  The URL is the file's path in the Release Notes space. GitBook builds a URL from the page's
  SUMMARY.md position, not its file path, and the two agree for this folder today; the workflow
  does not trust that, it fetches the URL and refuses to post anything that does not answer 200.

Usage: cloud_release_announce.py BEFORE AFTER     (commit SHAs or refs, both must be local)
Exit:  0 success (an empty list is success), 1 git failure, 2 usage error.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '.claude', 'hooks'))
from desccheck import FRONTMATTER, H1, parse  # noqa: E402

SPACE = 'release-notes'
FOLDER = SPACE + '/mariadb-cloud-release-notes'
SUMMARY = SPACE + '/SUMMARY.md'
BASE_URL = 'https://mariadb.com/docs/release-notes/'
NOTE = re.compile(r'mariadb-cloud-\d{4}\.\d{2}\.\d{2}[^/]*\.md')
HIDDEN = re.compile(r'^hidden:\s*true\s*$', re.M)


def git(*args):
    return subprocess.run(('git',) + args, check=True, capture_output=True,
                          text=True).stdout


def show(ref, path):
    """File content at ref, or None if the file does not exist there."""
    r = subprocess.run(['git', 'show', f'{ref}:{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def notes_at(ref):
    out = git('ls-tree', '--name-only', f'{ref}:{FOLDER}') if show(ref, FOLDER) else ''
    return sorted(n for n in out.split() if NOTE.fullmatch(n))


def in_summary(summary, name):
    rel = FOLDER[len(SPACE) + 1:] + '/' + name
    return summary is not None and f']({rel})' in summary


def is_hidden(text):
    m = FRONTMATTER.match(text)
    return bool(m and HIDDEN.search(m.group(1)))


def published(ref, summary):
    """{name: page text} for every note published at ref."""
    found = {}
    for name in notes_at(ref):
        text = show(ref, f'{FOLDER}/{name}')
        if text is not None and not is_hidden(text) and in_summary(summary, name):
            found[name] = text
    return found


def describe(name, text):
    d = parse(text)
    h1 = H1.search(FRONTMATTER.sub('', text, count=1))
    return {
        'file': f'{FOLDER}/{name}',
        'title': h1.group(1) if h1 else name[:-3],
        'description': d[2] if d else '',
        'url': BASE_URL + FOLDER[len(SPACE) + 1:] + '/' + name[:-3],
    }


def newly_published(before, after):
    was = published(before, show(before, SUMMARY))
    now = published(after, show(after, SUMMARY))
    return [describe(n, now[n]) for n in sorted(now) if n not in was]


def main(argv):
    if len(argv) != 3:
        print(__doc__.split('Usage: ')[1].split('\n')[0], file=sys.stderr)
        return 2
    try:
        notes = newly_published(argv[1], argv[2])
    except subprocess.CalledProcessError as e:
        print(f'git failed: {e.stderr.strip()}', file=sys.stderr)
        return 1
    json.dump(notes, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
