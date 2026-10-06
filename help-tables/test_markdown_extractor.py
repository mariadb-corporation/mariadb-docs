#!/usr/bin/env python3
"""
Regression tests for markdown_extractor.py (DOCS-6894).

Run from the repo root:

    python3 -m unittest discover -s help-tables -p 'test_*.py' -v

The extractor turns server/reference pages into fill_help_tables.sql, which
ships with the server and backs the HELP command. Until DOCS-6894 it ran its
Markdown-stripping rules over the whole topic text, code included, so:

* the italic rule ate asterisks: `SELECT * FROM t` became `SELECT  FROM t`;
* a fenced block in a Description came out as ``sql ... ``, because fences
  went through the inline-code rule;
* the `\\_` rule rewrote LIKE patterns inside examples;
* topic names kept their Markdown escapes (AUTO\\_INCREMENT), which HELP's
  LIKE lookup does not match.

Two layers, as for the function-skill extractor (DOCS-6889): FIXTURES pin
each defect, and the REAL-TREE guard builds every topic from the actual pages
and fails on any of the four classes reappearing -- a page-format change is
as likely to break this as a code change.

Standard library only, like the extractor itself.
"""
from __future__ import annotations

import re
import sys
import textwrap
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import markdown_extractor as mx  # noqa: E402


def build(page: str):
    """Run one page through the same steps process_single_file() takes."""
    content, name = mx.find_line_range(textwrap.dedent(page).splitlines())
    syntax, desc, example = mx.extract_sections(content)
    return mx.build_output(name, syntax, desc, example,
                           str(mx.REPO_ROOT / "server/reference/x.md"))


PAGE = """\
    # AUTO\\_INCREMENT

    ## Syntax

    ```sql
    SELECT * FROM t1 WHERE a*b = c*d;
    ```

    ## Description

    Counts rows with `COUNT(*)`, and *emphasis* is plain text.
    See [SHOW](show.md) and the \\* character.

    ```sql
    SHOW VARIABLES LIKE 'character_set\\_%';
    ```

    Text after the block.

    ```mermaid
    graph TD; A-->B;
    ```

    ## Examples

    ```sql
    SELECT * FROM t1;
    INSERT INTO t1 VALUES ('13*04*21');
    ```
"""


class FixtureTests(unittest.TestCase):

    def setUp(self):
        self.topic = build(PAGE)
        self.text = self.topic["description"]

    def test_syntax_code_is_verbatim(self):
        self.assertIn("SELECT * FROM t1 WHERE a*b = c*d;", self.text)

    def test_example_code_is_verbatim(self):
        self.assertIn("SELECT * FROM t1;", self.text)
        self.assertIn("('13*04*21')", self.text)

    def test_description_fence_lines_are_dropped_and_code_kept(self):
        self.assertIn("SHOW VARIABLES LIKE 'character_set\\_%';", self.text)
        self.assertNotIn("``", self.text)
        self.assertNotRegex(self.text, r"(?m)^sql$")

    def test_prose_around_a_fence_is_still_stripped(self):
        self.assertIn("Counts rows with COUNT(*), and emphasis is plain text.",
                      self.text)
        self.assertIn("See SHOW and the * character.", self.text)
        self.assertIn("Text after the block.", self.text)

    def test_mermaid_source_is_dropped(self):
        self.assertNotIn("graph TD", self.text)

    def test_topic_name_is_unescaped(self):
        self.assertEqual(self.topic["name"], "AUTO_INCREMENT")

    def test_non_markdown_backslashes_survive(self):
        # \n and \d are not Markdown escapes; prose about strings keeps them.
        self.assertEqual(mx.strip_markdown(r"Use \n or \d here."),
                         r"Use \n or \d here.")

    def test_escaped_backticks_do_not_open_a_code_span(self):
        # identifier-names.md: the quote character, written as \`\`\`.
        self.assertEqual(
            mx.strip_markdown("character - \\`\\`\\`, but the `ANSI_QUOTES` "
                              "[SQL\\_MODE](sql_mode.md) option"),
            "character - ```, but the ANSI_QUOTES SQL_MODE option")

    def test_nested_emphasis(self):
        self.assertEqual(mx.strip_markdown("- **Marked *Open request*** - add"),
                         "- Marked Open request - add")

    def test_list_bullets_are_not_emphasis(self):
        text = "* [Index Condition Pushdown](icp.md)\n* Rowid *filtering*\n* x"
        self.assertEqual(mx.strip_markdown(text),
                         "* Index Condition Pushdown\n* Rowid filtering\n* x")

    def test_characters_outside_utf8mb3_are_spelled_out(self):
        self.assertEqual(mx.fit_utf8mb3("or just a \U0001F44D, to"),
                         "or just a [thumbs up sign], to")
        self.assertEqual(mx.fit_utf8mb3("caf\u00e9 \u2014 ok"), "caf\u00e9 \u2014 ok")

    def test_indented_fence_in_a_list_item(self):
        text = mx.strip_description(
            "1. Run:\n\n   ```bash\n   mariadb -e 'SELECT 1'\n   ```\n")
        self.assertEqual(text, "1. Run:\n\nmariadb -e 'SELECT 1'")

    def test_longer_fence_is_not_closed_by_a_shorter_one(self):
        text = mx.strip_description("````md\n```sql\nSELECT 1;\n```\n````\n")
        self.assertEqual(text, "```sql\nSELECT 1;\n```")


class RealTreeTests(unittest.TestCase):
    """Build every topic from the real pages, as main() does."""

    @classmethod
    def setUpClass(cls):
        mx.NAV_URL_MAP = mx.build_nav_url_map(mx.REPO_ROOT / "server", "server")
        files = mx.get_files(str(mx.REPO_ROOT / "server" / "reference"))
        cls.topics = []
        for path in files:
            content, name = mx.find_line_range(mx.open_file(path))
            if content is None:
                continue
            syntax, desc, example = mx.extract_sections(content)
            if not desc.strip() and not example:
                continue
            cls.topics.append(
                (path, mx.build_output(name, syntax, desc, example, path)))

    def offenders(self, predicate):
        return [Path(p).relative_to(mx.REPO_ROOT).as_posix()
                for p, t in self.topics if predicate(t)][:10]

    def test_tree_is_not_empty(self):
        self.assertGreater(len(self.topics), 1000)

    def test_no_select_star_lost(self):
        self.assertEqual(
            self.offenders(lambda t: "SELECT  FROM" in t["description"]), [])

    def test_no_fence_markup_leaks(self):
        # A leftover fence is a line of its own: `sql, ``, ``cpp. Backticks
        # inside a line can be real content (identifier-names.md escapes
        # three of them to show the quote character).
        self.assertEqual(
            self.offenders(lambda t: re.search(r"(?m)^\s*(`{1,3}|~{3,})[\w+-]*\s*$",
                                               t["description"])), [])

    def test_everything_fits_utf8mb3(self):
        # mysql.help_topic is utf8mb3: a 4-byte character stops a strict load.
        self.assertEqual(
            self.offenders(lambda t: re.search(r"[\U00010000-\U0010FFFF]",
                                               t["name"] + t["description"])), [])

    def test_no_escaped_topic_names(self):
        self.assertEqual(
            self.offenders(lambda t: mx.MD_ESCAPE.search(t["name"])), [])


if __name__ == "__main__":
    unittest.main()
