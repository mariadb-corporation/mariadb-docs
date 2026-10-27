"""Tests for the Plugin API sync's link fixers and nav builder (DOCS-6988).

The fixtures are cut-down copies of real moxygen output for MariaDB/server#5617
(MDBF-1224). Run with:
  python3 -m unittest discover -v -s .github/scripts -p 'test_*.py'
"""
import importlib.util
import pathlib
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


fragcheck = load(REPO / '.claude' / 'hooks' / 'fragcheck.py', 'fragcheck')
doxygen_refs = load(HERE / 'fix_plugin_api_doxygen_refs.py', 'doxygen_refs')
member_anchors = load(HERE / 'fix_plugin_api_member_anchors.py',
                      'member_anchors')
summary = load(HERE / 'add_server_plugin_api_to_summary.py', 'summary')

FRONTMATTER = '---\ndescription: >-\n  Generated page.\n---\n\n'


class TempDir(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def page(self, name, text):
        path = self.dir / name
        path.write_text(text)
        return path


class DoxygenRefs(TempDir):
    def setUp(self):
        super().setUp()
        self.page('page-concepts.md',
                  '# Plugin API Concepts \n\n## Plugin\n\ntext\n\n'
                  '## Plugin Library\n\ntext\n')
        self.page('plugin_status_vars.md',
                  '# Plugin Status Variables \n\n### enum_mysql_show_type\n\n'
                  '| Enumerator | Description |\n|---|---|\n'
                  '| `SHOW_UNDEF` | Internal only! |\n'
                  '| `SHOW_FUNC` | A function |\n')

    def fix(self):
        return doxygen_refs.fix_dir(self.dir, fragcheck)

    def test_section_ref_resolves_by_link_text(self):
        src = self.page('page-make.md',
                        'A [Plugin Library](page-concepts.md#concepts_1concept'
                        '_plugin_library) holds a [Plugin](page-concepts.md#'
                        'concepts_1concept_plugin).\n')
        rewrites, unresolved = self.fix()
        self.assertEqual(unresolved, [])
        self.assertEqual(len(rewrites), 2)
        self.assertEqual(src.read_text(),
                         'A [Plugin Library](page-concepts.md#plugin-library) '
                         'holds a [Plugin](page-concepts.md#plugin).\n')

    def test_enum_value_goes_to_the_enum_heading(self):
        src = self.page('page-impl.md',
                        'Use [`SHOW_FUNC`](plugin_status_vars.md#group__plugin'
                        '__status__vars_1gga31d3).\n')
        self.fix()
        self.assertIn('(plugin_status_vars.md#enum_mysql_show_type)',
                      src.read_text())

    def test_punctuation_variant_resolves_by_letters(self):
        src = self.page('page-x.md',
                        '## Operator struct st_mysql_const_lex_string\n\n'
                        'See [here](#operatorstructst_mysql_const_lex_string).\n')
        self.fix()
        self.assertIn('(#operator-struct-st_mysql_const_lex_string)',
                      src.read_text())

    def test_live_and_empty_fragments_are_untouched(self):
        text = ('[ok](page-concepts.md#plugin) [index](api.md#) '
                '[ext](https://example.com/a.md#x)\n')
        src = self.page('page-y.md', text)
        rewrites, unresolved = self.fix()
        self.assertEqual((rewrites, unresolved), ([], []))
        self.assertEqual(src.read_text(), text)

    def test_ambiguous_target_is_left_and_reported(self):
        self.page('dup.md', '# Dup\n\n## Plugin\n\n## Plugin\n')
        src = self.page('page-z.md', '[Plugin](dup.md#concepts_1x)\n')
        rewrites, unresolved = self.fix()
        self.assertEqual(rewrites, [])
        self.assertEqual(len(unresolved), 1)
        self.assertEqual(src.read_text(), '[Plugin](dup.md#concepts_1x)\n')


class MemberAnchorPairing(TempDir):
    def test_repeated_field_names_pair_by_order(self):
        # Moxygen numbered the two `length` fields -1 and -2; GitBook
        # publishes them as #length and #length-1. The first link resolves,
        # but to the wrong field, so both must be paired.
        page = self.page('plugin_api_service_sql.md',
                         '# SQL Service\n\n### sql_service_st\n\n'
                         '#### Public Attributes\n\n'
                         '| `a` | [`length`](#length-1) |\n'
                         '| `b` | [`length`](#length-2) |\n\n'
                         '#### length\n\nfirst\n\n#### length\n\nsecond\n')
        rewrites, unresolved = member_anchors.fix_page(page, fragcheck)
        self.assertEqual(unresolved, [])
        text = page.read_text()
        self.assertIn('| `a` | [`length`](#length) |', text)
        self.assertIn('| `b` | [`length`](#length-1) |', text)

    def test_counts_that_differ_are_left_alone(self):
        page = self.page('p.md',
                         '# P\n\n### s\n\n[`x`](#x-5)\n\n'
                         '#### x\n\n#### x\n')
        rewrites, unresolved = member_anchors.fix_page(page, fragcheck)
        self.assertEqual(rewrites, [])
        self.assertEqual(len(unresolved), 1)


class SummaryNav(TempDir):
    SUMMARY = ('# Table of contents\n\n'
               '* [Plugins](reference/plugins/README.md)\n'
               '    * [Plugin Overview](reference/plugins/plugin-overview.md)\n'
               '    * [Plugin API Documentation]'
               '(reference/plugins/api-plugin/README.md)\n'
               '      * [Old](reference/plugins/api-plugin/old.md)\n'
               '        * [Older](reference/plugins/api-plugin/older.md)\n'
               '    * [Plugin Maturity](reference/plugins/maturity.md)\n')

    def setUp(self):
        super().setUp()
        self.page('README.md', '# Plugin API Documentation\n\n'
                  '* [Implementation](page-implementation.md#x)\n'
                  '* [Concepts](page-concepts.md#y)\n'
                  '* [API reference](api.md#)\n')
        self.page('page-concepts.md', FRONTMATTER + '# Plugin API Concepts \n')
        self.page('page-implementation.md',
                  FRONTMATTER + '# Plugin API Implementation\n')
        self.page('page-verification.md', FRONTMATTER + '# Plugin Verification\n')
        self.page('api.md', FRONTMATTER + '# API Reference\n')
        self.page('plugin_api.md', FRONTMATTER + '# Plugin API\n')
        self.page('plugin_client_api.md', FRONTMATTER + '# Client Plugin API\n')
        self.page('plugin_types.md', FRONTMATTER + '# Plugin Types\n\n'
                  '> [`Plugin API`](plugin_api.md)\n')
        self.page('audit.md', FRONTMATTER + '# Audit Plugin\n\n'
                  '> [`Plugin API`](plugin_api.md) / '
                  '[`Plugin Types`](plugin_types.md)\n')
        self.page('daemon.md', FRONTMATTER + '# Daemon Plugin\n\n'
                  '> [`Plugin API`](plugin_api.md) / '
                  '[`Plugin Types`](plugin_types.md)\n')

    def block(self):
        return summary.nav_lines(*summary.build_tree(self.dir))

    def test_nests_by_breadcrumb_and_orders_roots(self):
        d = 'reference/plugins/api-plugin'
        self.assertEqual(self.block(), [
            f'      * [Plugin API Implementation]({d}/page-implementation.md)',
            f'      * [Plugin API Concepts]({d}/page-concepts.md)',
            f'      * [Plugin Verification]({d}/page-verification.md)',
            f'      * [Client Plugin API]({d}/plugin_client_api.md)',
            f'      * [Plugin API]({d}/plugin_api.md)',
            f'        * [Plugin Types]({d}/plugin_types.md)',
            f'          * [Audit Plugin]({d}/audit.md)',
            f'          * [Daemon Plugin]({d}/daemon.md)',
            f'      * [API Reference]({d}/api.md)',
        ])

    def test_replaces_the_whole_old_section_and_is_idempotent(self):
        block = self.block()
        once = summary.rewrite_summary(self.SUMMARY, block)
        self.assertNotIn('old.md', once)
        self.assertNotIn('older.md', once)
        self.assertIn('    * [Plugin Maturity]', once)
        self.assertEqual(summary.rewrite_summary(once, block), once)

    def test_missing_anchor_entry_fails(self):
        with self.assertRaises(SystemExit):
            summary.rewrite_summary('# Table of contents\n', self.block())


if __name__ == '__main__':
    unittest.main()
