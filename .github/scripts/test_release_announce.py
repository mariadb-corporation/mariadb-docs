"""Tests for release_announce.py (DOCS-6936, DOCS-7076).

Each test builds commits in a throwaway git repo and asks the script which notes the last
commit published. Run: python3 -m unittest discover -s .github/scripts -p 'test_*.py'
"""
import datetime
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import release_announce as ra  # noqa: E402

FOLDER = 'release-notes/mariadb-cloud-release-notes'
TODAY = datetime.date.today()


def days_ago(n):
    return (TODAY - datetime.timedelta(days=n)).isoformat()


def page(version, feature, hidden=False, released=None, h1=None):
    released = released or TODAY.isoformat()
    return (
        '---\n'
        'description: >-\n'
        f'  MariaDB Cloud {version} is a GA release, released on\n'
        f'  {released}. It adds {feature}.\n'
        'icon: rocket-launch\n'
        + ('hidden: true\n' if hidden else '')
        + '---\n\n'
        f'# {h1 or f"MariaDB Cloud {version} Release Notes: {feature}"}\n\nBody.\n'
    )


def cs_page(version, released=None, kind='Release Notes'):
    released = released or TODAY.isoformat()
    return (
        '---\n'
        'description: >-\n'
        f'  MariaDB {version} is a Stable (GA) release of MariaDB Community Server,\n'
        f'  released on {released}\n'
        '---\n\n'
        f'# MariaDB {version} {kind}\n\n**Release date:** {released}\n'
    )


def operator_page(version, hidden=False):
    return (
        '---\n'
        'description: >-\n'
        f'  MariaDB Enterprise Operator {version} is a Stable (GA) release of MariaDB\n'
        f'  Enterprise Operator, released on {TODAY.isoformat()}\n'
        + ('hidden: true\n' if hidden else '')
        + '---\n\n'
        f'# MariaDB Enterprise Kubernetes Operator {version}\n\nFixes.\n'
    )


def summary(*names, extra=''):
    lines = ['# Table of contents\n',
             '* [MariaDB Cloud Release Notes](mariadb-cloud-release-notes/README.md)\n']
    lines += [f'  * [{n}](mariadb-cloud-release-notes/{n})\n' for n in names]
    lines.append('  * [All Releases](mariadb-cloud-release-notes/all-releases.md)\n')
    return ''.join(lines) + extra


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

    def result(self, before, after, **kw):
        return ra.newly_published(before, after, **kw)

    def files(self, before, after, **kw):
        return [n['file'] for n in self.result(before, after, **kw)['announce']]

    def skipped(self, before, after, **kw):
        return [(n['file'], n['reason']) for n in self.result(before, after, **kw)['skipped']]

    # --- carried over from the Cloud-only script (DOCS-6936) ---

    def test_new_visible_note_listed_in_summary_is_announced(self):
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.01.md', page('2026.10.01', 'a cache'))
        self.repo.write('release-notes/SUMMARY.md', summary('mariadb-cloud-2026.10.01.md'))
        after = self.repo.commit()
        notes = self.result(before, after)['announce']
        self.assertEqual(len(notes), 1)
        n = notes[0]
        self.assertEqual(n['title'], 'MariaDB Cloud 2026.10.01 Release Notes: a cache')
        self.assertEqual(n['description'], 'MariaDB Cloud 2026.10.01 is a GA release, '
                                           f'released on {TODAY.isoformat()}. It adds a cache.')
        self.assertEqual(n['url'], 'https://mariadb.com/docs/release-notes/'
                                   'mariadb-cloud-release-notes/mariadb-cloud-2026.10.01')
        self.assertEqual(n['released'], TODAY.isoformat())

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
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.10.12.md', page('2026.10.12', 'f'))
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.09.30.md',
                        page('2026.09.30', 'f', released=days_ago(3)))
        self.repo.write('release-notes/SUMMARY.md',
                        summary('mariadb-cloud-2026.10.12.md', 'mariadb-cloud-2026.09.30.md'))
        after = self.repo.commit()
        self.assertEqual(self.files(before, after),
                         [f'{FOLDER}/mariadb-cloud-2026.09.30.md',
                          f'{FOLDER}/mariadb-cloud-2026.10.12.md'])

    def test_folder_absent_before_is_fine(self):
        before = self.repo.commit()
        self.assertEqual(self.files(before, before), [])

    # --- every product (DOCS-7076) ---

    def cs_summary(self, *entries):
        return ('# Table of contents\n'
                '* [Community Server Release Notes](community-server/README.md)\n'
                + ''.join(f'  * [{t}]({p})\n' for t, p in entries))

    def test_other_products_are_announced_and_changelogs_are_not(self):
        before = self.repo.commit()
        self.repo.write('release-notes/community-server/13.0/13.0.3.md', cs_page('13.0.3'))
        self.repo.write('release-notes/community-server/changelogs/13.0/13.0.3.md',
                        cs_page('13.0.3', kind='Changelog'))
        self.repo.write('release-notes/community-server/13.0/whats-new.md',
                        cs_page('13.0', kind="What's New"))
        self.repo.write('release-notes/SUMMARY.md', self.cs_summary(
            ('13.0.3', 'community-server/13.0/13.0.3.md'),
            ('Changelog', 'community-server/changelogs/13.0/13.0.3.md'),
            ("What's New", 'community-server/13.0/whats-new.md')))
        after = self.repo.commit()
        self.assertEqual(self.files(before, after),
                         ['release-notes/community-server/13.0/13.0.3.md'])

    def test_note_without_release_notes_in_h1_counts_by_its_description(self):
        before = self.repo.commit()
        self.repo.write('release-notes/enterprise-operator/26.06/26.06.8.md',
                        operator_page('26.06.8'))
        self.repo.write('release-notes/SUMMARY.md',
                        '* [Operator](enterprise-operator/README.md)\n'
                        '  * [26.06.8](enterprise-operator/26.06/26.06.8.md)\n')
        after = self.repo.commit()
        self.assertEqual(self.files(before, after),
                         ['release-notes/enterprise-operator/26.06/26.06.8.md'])

    def test_note_under_hidden_parent_waits_for_the_parent(self):
        self.repo.write('release-notes/enterprise-manager/26.10/README.md',
                        '---\ndescription: x\nhidden: true\n---\n\n# Enterprise Manager 26.10\n')
        self.repo.write('release-notes/enterprise-manager/26.10/26.10.0.md', cs_page('26.10.0'))
        self.repo.write('release-notes/SUMMARY.md',
                        '* [EM](enterprise-manager/README.md)\n'
                        '  * [26.10](enterprise-manager/26.10/README.md)\n'
                        '    * [26.10.0](enterprise-manager/26.10/26.10.0.md)\n')
        merged = self.repo.commit()
        self.assertEqual(self.files(merged + '^', merged), [])
        self.repo.write('release-notes/enterprise-manager/26.10/README.md',
                        '---\ndescription: x\n---\n\n# Enterprise Manager 26.10\n')
        revealed = self.repo.commit()
        self.assertEqual(self.files(merged, revealed),
                         ['release-notes/enterprise-manager/26.10/26.10.0.md'])

    def test_url_follows_the_nav_not_the_file_path(self):
        before = self.repo.commit()
        self.repo.write('release-notes/gridgain-9/9.1.20/release-notes_9.1.20.md',
                        '---\ndescription: GridGain 9.1.20 is a maintenance release.\n---\n\n'
                        '# GridGain 9.1.20 Release Notes\n')
        self.repo.write('release-notes/SUMMARY.md',
                        '* [GridGain 9](gridgain-9/README.md)\n'
                        '  * [9.1.20](gridgain-9/9.1.20/release-notes_9.1.20.md)\n')
        after = self.repo.commit()
        [n] = self.result(before, after)['announce']
        self.assertEqual(n['url'], 'https://mariadb.com/docs/release-notes/gridgain-9/'
                                   'release-notes_9.1.20')
        self.assertIsNone(n['released'])

    def test_backfilled_old_release_is_held_back(self):
        before = self.repo.commit()
        self.repo.write('release-notes/community-server/10.6/10.6.1.md',
                        cs_page('10.6.1', released='2021-07-06'))
        self.repo.write('release-notes/SUMMARY.md', self.cs_summary(
            ('10.6.1', 'community-server/10.6/10.6.1.md')))
        after = self.repo.commit()
        self.assertEqual(self.files(before, after), [])
        [(f, reason)] = self.skipped(before, after)
        self.assertIn('released 2021-07-06', reason)
        self.assertEqual(self.files(before, after, max_age_days=99999),
                         ['release-notes/community-server/10.6/10.6.1.md'])

    def test_too_many_in_one_push_announces_none(self):
        before = self.repo.commit()
        entries = []
        for i in range(4):
            self.repo.write(f'release-notes/community-server/13.0/13.0.{i}.md',
                            cs_page(f'13.0.{i}'))
            entries.append((f'13.0.{i}', f'community-server/13.0/13.0.{i}.md'))
        self.repo.write('release-notes/SUMMARY.md', self.cs_summary(*entries))
        after = self.repo.commit()
        self.assertEqual(self.files(before, after, max_notes=3), [])
        self.assertEqual(len(self.skipped(before, after, max_notes=3)), 4)
        self.assertEqual(len(self.files(before, after, max_notes=4)), 4)

    def test_placeholder_title_is_held_back(self):
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/mariadb-cloud-byoa.md',
                        page('x', 'y', h1='MariaDB Cloud <YYYY.MM.DD> Release Notes'))
        self.repo.write('release-notes/SUMMARY.md', summary('mariadb-cloud-byoa.md'))
        after = self.repo.commit()
        self.assertEqual(self.files(before, after), [])
        self.assertIn('placeholder', self.skipped(before, after)[0][1])

    def test_reworded_published_page_is_not_announced_again(self):
        # DOCS-6765 retitled two visible Cloud notes; the old H1 lacked "Release Notes" and the
        # old description lacked "is a ... release", so the page only now looks like a note.
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.09.30.md',
                        '---\ndescription: Serverless.\n---\n\n# MariaDB Cloud 2026.09.30\n')
        self.repo.write('release-notes/SUMMARY.md', summary('mariadb-cloud-2026.09.30.md'))
        before = self.repo.commit()
        self.repo.write(f'{FOLDER}/mariadb-cloud-2026.09.30.md', page('2026.09.30', 'Serverless'))
        after = self.repo.commit()
        self.assertEqual(self.files(before, after), [])


class ReleaseDate(unittest.TestCase):
    def test_formats_in_use(self):
        cases = {
            '**Release date:** 15 Sep 2026\n': '2026-09-15',
            '**Release Date:** 3 November 2026\n': '2026-11-03',
            '**Release date**: 19 May 2026\n': '2026-05-19',
            'MaxScale 1 was released on 2022-09-12. This release': '2022-09-12',
            '**Release date:** September 15, 2026\n': '2026-09-15',
        }
        for text, want in cases.items():
            with self.subTest(text=text):
                self.assertEqual(ra.release_date('# T\n\n' + text).isoformat(), want)

    def test_description_date(self):
        text = ('---\ndescription: >-\n  Release notes for MariaDB Connector/C 3.3.20, a Stable\n'
                '  (GA) release published 13 August 2026.\n---\n\n# T\n')
        self.assertEqual(ra.release_date(text).isoformat(), '2026-08-13')

    def test_no_date(self):
        self.assertIsNone(ra.release_date('# GridGain 9.1.8 Release Notes\n\nBody.\n'))


if __name__ == '__main__':
    unittest.main()
