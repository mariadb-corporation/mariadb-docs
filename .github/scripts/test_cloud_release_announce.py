"""Tests for cloud_release_announce.py (DOCS-6936).

Each test builds commits in a throwaway git repo and asks the script which notes the last
commit published. Run: python3 -m unittest discover -s .github/scripts -p 'test_*.py'
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cloud_release_announce as cra  # noqa: E402

FOLDER = 'release-notes/mariadb-cloud-release-notes'


def page(version, feature, hidden=False):
    return (
        '---\n'
        'description: >-\n'
        f'  MariaDB Cloud {version} is a GA release, released on\n'
        f'  {version.replace(".", "-")}. It adds {feature}.\n'
        'icon: rocket-launch\n'
        + ('hidden: true\n' if hidden else '')
        + '---\n\n'
        f'# MariaDB Cloud {version} Release Notes: {feature}\n\nBody.\n'
    )


def summary(*names):
    lines = ['# Table of contents\n',
             '* [MariaDB Cloud Release Notes](mariadb-cloud-release-notes/README.md)\n']
    lines += [f'  * [{n}](mariadb-cloud-release-notes/{n})\n' for n in names]
    lines.append('  * [All Releases](mariadb-cloud-release-notes/all-releases.md)\n')
    return ''.join(lines)


class Repo:
    def __init__(self, path):
        self.path = path
        self.git('init', '-q')
        self.git('config', 'user.email', 't@example.com')
        self.git('config', 'user.name', 't')
        self.write('README.md', 'root\n')
        self.commit()

    def git(self, *args):
        return subprocess.run(('git', '-C', self.path) + args, check=True,
                              capture_output=True, text=True).stdout.strip()

    def write(self, rel, text):
        full = os.path.join(self.path, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w') as f:
            f.write(text)

    def remove(self, rel):
        os.remove(os.path.join(self.path, rel))

    def commit(self):
        self.git('add', '-A')
        self.git('commit', '-q', '--allow-empty', '-m', 'c')
        return self.git('rev-parse', 'HEAD')


class NewlyPublished(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Repo(self.tmp.name)
        self.cwd = os.getcwd()
        os.chdir(self.tmp.name)

    def tearDown(self):
        os.chdir(self.cwd)
        self.tmp.cleanup()

    def files(self, before, after):
        return [n['file'] for n in cra.newly_published(before, after)]

    def test_new_visible_note_listed_in_summary_is_announced(self):
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md', page('2026.10.01', 'a cache'))
        self.repo.write('release-notes/SUMMARY.md', summary('mariadb-cloud-2026.10.01.md'))
        after = self.repo.commit()
        notes = cra.newly_published(before, after)
        self.assertEqual(len(notes), 1)
        n = notes[0]
        self.assertEqual(n['title'], 'MariaDB Cloud 2026.10.01 Release Notes: a cache')
        self.assertEqual(n['description'], 'MariaDB Cloud 2026.10.01 is a GA release, '
                                           'released on 2026-10-01. It adds a cache.')
        self.assertEqual(n['url'], 'https://mariadb.com/docs/release-notes/'
                                   'mariadb-cloud-release-notes/mariadb-cloud-2026.10.01')

    def test_hidden_note_is_not_announced_until_unhidden(self):
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md',
                        page('2026.10.01', 'a cache', hidden=True))
        self.repo.write('release-notes/SUMMARY.md', summary('mariadb-cloud-2026.10.01.md'))
        merged = self.repo.commit()
        self.assertEqual(self.files(before, merged), [])
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md', page('2026.10.01', 'a cache'))
        unhidden = self.repo.commit()
        self.assertEqual(self.files(merged, unhidden),
                         [f'{FOLDER}/mariadb-cloud-2026.10.01.md'])

    def test_note_missing_from_summary_is_not_announced_until_added(self):
        self.repo.write('release-notes/SUMMARY.md', summary())
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md', page('2026.10.01', 'a cache'))
        added = self.repo.commit()
        self.assertEqual(self.files(before, added), [])
        self.repo.write('release-notes/SUMMARY.md', summary('mariadb-cloud-2026.10.01.md'))
        listed = self.repo.commit()
        self.assertEqual(self.files(added, listed), [f'{FOLDER}/mariadb-cloud-2026.10.01.md'])

    def test_already_published_note_edited_or_hidden_is_not_announced(self):
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md', page('2026.10.01', 'a cache'))
        self.repo.write('release-notes/SUMMARY.md', summary('mariadb-cloud-2026.10.01.md'))
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md', page('2026.10.01', 'a cachet'))
        edited = self.repo.commit()
        self.assertEqual(self.files(before, edited), [])
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md',
                        page('2026.10.01', 'a cachet', hidden=True))
        hidden = self.repo.commit()
        self.assertEqual(self.files(edited, hidden), [])

    def test_readme_and_all_releases_are_never_announced(self):
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/README.md', page('2026.10.01', 'x'))
        self.repo.write(f'{FOLDER}/all-releases.md', page('2026.10.01', 'y'))
        self.repo.write('release-notes/SUMMARY.md', summary())
        after = self.repo.commit()
        self.assertEqual(self.files(before, after), [])

    def test_several_notes_in_one_push_come_out_oldest_first(self):
        before = self.repo.commit()
        for v in ('2026.10.12', '2026.09.30'):
            self.repo.write(f'{FOLDER}/mariadb-cloud-{v}.md', page(v, 'f'))
        self.repo.write('release-notes/SUMMARY.md',
                        summary('mariadb-cloud-2026.10.12.md', 'mariadb-cloud-2026.09.30.md'))
        after = self.repo.commit()
        self.assertEqual(self.files(before, after),
                         [f'{FOLDER}/mariadb-cloud-2026.09.30.md',
                          f'{FOLDER}/mariadb-cloud-2026.10.12.md'])

    def test_folder_absent_before_is_fine(self):
        before = self.repo.commit()
        self.assertEqual(self.files(before, before), [])


if __name__ == '__main__':
    unittest.main()
