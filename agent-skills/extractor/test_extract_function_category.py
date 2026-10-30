#!/usr/bin/env python3
"""
Regression tests for extract_function_category.py (DOCS-6889).

Run from the repo root:

    python3 -m unittest discover -s agent-skills/extractor -p 'test_*.py' -v

Two layers, because each catches what the other cannot:

* FIXTURES pin the page shapes the extractor must survive -- in particular a
  version tab that opens with a `{% hint %}From MariaDB X:{% endhint %}`
  block, the shape DOCS-6672 introduced on every tabbed page. Without the fix,
  a tabbed Syntax section was skipped as "no Syntax SQL code block" and a
  tabbed Description came out as the bare `{% tabs %} {% tab ... %}` markup.

* The REAL-TREE guard runs every category regenerate.py feeds into a skill
  and fails on any GitBook markup leaking into an entry, and on any of the
  functions that regression silently dropped going missing again. A page-
  format change elsewhere in the docs will trip this rather than ship a
  quietly degraded catalog: every content gate on the bot PR passed while
  five entries were broken, because none of them reads generated content.

Standard library only, like the extractor itself.
"""
from __future__ import annotations

import re
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import extract_function_category as efc  # noqa: E402
import regenerate  # noqa: E402

FRONTMATTER = "---\ndescription: >-\n  Frontmatter fallback.\n---\n\n"

TABBED_SYNTAX = FRONTMATTER + textwrap.dedent("""\
    # CRC32

    ## Syntax

    {% tabs %}
    {% tab title="Current" %}
    {% hint style="info" %}
    From MariaDB 10.8:
    {% endhint %}

    ```bnf
    CRC32([par,]expr)
    ```
    {% endtab %}

    {% tab title="< 10.8" %}
    {% hint style="info" %}
    Before MariaDB 10.8:
    {% endhint %}

    ```sql
    CRC32(expr)
    ```
    {% endtab %}
    {% endtabs %}

    ## Description

    Computes a cyclic redundancy check value.
    """)

TABBED_DESCRIPTION = FRONTMATTER + textwrap.dedent("""\
    # SESSION\\_USER

    ## Syntax

    ```bnf
    SESSION_USER()
    ```

    ## Description

    {% tabs %}
    {% tab title="Current" %}
    {% hint style="info" %}
    From MariaDB 11.7:
    {% endhint %}

    Shows the value of CURRENT_USER() when the session was created.
    {% endtab %}

    {% tab title="< 11.7" %}
    {% hint style="info" %}
    Before MariaDB 11.7:
    {% endhint %}

    Returns the user name and host name.
    {% endtab %}
    {% endtabs %}
    """)

PLAIN = FRONTMATTER + textwrap.dedent("""\
    # ABS

    ## Syntax

    ```bnf
    ABS(X)
    ```

    ## Description

    Returns the absolute (non-negative) value of X.

    ## Examples
    """)

MIXED_CASE = FRONTMATTER + textwrap.dedent("""\
    # VEC\\_FromText

    ## Syntax

    ```bnf
    VEC_FromText(s)
    ```

    ## Description

    Converts a text representation of a vector to a vector.
    """)

WRAPPED_SIGNATURE = FRONTMATTER + textwrap.dedent("""\
    # LAG

    ## Syntax

    ```bnf
    LAG (expr[, offset]) OVER (
      [ PARTITION BY partition_expression ]
      ORDER BY order_list
    )
    ```

    ## Description

    Accesses data from a previous row.

    ## Examples
    """)

ALTERNATIVE_FORMS = FRONTMATTER + textwrap.dedent("""\
    # SUBSTRING

    ## Syntax

    ```bnf
    SUBSTRING(str,pos),
    SUBSTRING(str FROM pos)
    ```
    """)

EDITORIAL = FRONTMATTER + textwrap.dedent("""\
    # Window Frames

    ## Syntax

    ```bnf
    frame_clause
    ```
    """)

MARKUP_RE = re.compile(r"\{%")


def extract(text: str) -> dict:
    with tempfile.TemporaryDirectory() as d:
        page = Path(d) / "page.md"
        page.write_text(text, encoding="utf-8")
        return efc.extract_function(page)


class FixtureTests(unittest.TestCase):

    def test_tabbed_syntax_opening_with_a_hint_is_extracted(self):
        fn = extract(TABBED_SYNTAX)
        self.assertEqual(fn["name"], "CRC32")
        # The FIRST tab is the "Current" form; the older tab must not win.
        self.assertEqual(fn["signature"], "CRC32([par,]expr)")

    def test_tabbed_description_opening_with_a_hint_is_prose(self):
        fn = extract(TABBED_DESCRIPTION)
        self.assertEqual(
            fn["description"],
            "Shows the value of CURRENT_USER() when the session was created.")
        self.assertNotRegex(fn["description"], MARKUP_RE)

    def test_hint_text_never_becomes_the_description(self):
        for text in (TABBED_SYNTAX, TABBED_DESCRIPTION):
            self.assertNotIn("MariaDB", extract(text)["description"])

    def test_plain_page_is_unchanged(self):
        fn = extract(PLAIN)
        self.assertEqual(fn["signature"], "ABS(X)")
        self.assertEqual(fn["description"],
                         "Returns the absolute (non-negative) value of X.")

    def test_mixed_case_function_title_is_accepted(self):
        fn = extract(MIXED_CASE)
        self.assertEqual(fn["name"], "VEC_FromText")
        self.assertEqual(fn["signature"], "VEC_FromText(s)")

    def test_wrapped_signature_is_joined_until_its_parens_balance(self):
        self.assertEqual(
            extract(WRAPPED_SIGNATURE)["signature"],
            "LAG (expr[, offset]) OVER ( [ PARTITION BY partition_expression ] "
            "ORDER BY order_list )")

    def test_balanced_first_line_is_not_joined_to_alternative_forms(self):
        self.assertEqual(extract(ALTERNATIVE_FORMS)["signature"],
                         "SUBSTRING(str,pos),")

    def test_multi_word_title_is_still_rejected_as_editorial(self):
        with self.assertRaises(efc.ExtractionError):
            extract(EDITORIAL)


class RealTreeTests(unittest.TestCase):
    """Run every category regenerate.py feeds, against the checked-in pages."""

    # Each was dropped or garbled in a generated catalog once (DOCS-6889).
    MUST_EXTRACT = {
        "secondary-functions/encryption-hashing-and-compression-functions":
            {"AES_DECRYPT", "AES_ENCRYPT"},
        "numeric-functions": {"CRC32"},
        "secondary-functions/information-functions": {"SESSION_USER"},
        "string-functions": {"TO_CHAR", "SFORMAT"},
        "date-time-functions": {"MONTHS_BETWEEN"},
        "special-functions/window-functions":
            {"PERCENTILE_CONT", "PERCENTILE_DISC"},
        "vector-functions": {"VEC_FromText", "VEC_ToText"},
    }

    @classmethod
    def setUpClass(cls):
        if not regenerate.SQLF.is_dir():
            raise unittest.SkipTest(f"{regenerate.SQLF} not found")
        cls.results = {}
        for category in regenerate.CATEGORIES.values():
            extracted = []
            for page in sorted((regenerate.SQLF / category).glob("*.md")):
                if page.stem in ("README", "SUMMARY"):
                    continue
                try:
                    extracted.append(efc.extract_function(page))
                except efc.ExtractionError:
                    pass
            cls.results[category] = extracted

    def test_every_category_extracts_something(self):
        for category, extracted in self.results.items():
            with self.subTest(category=category):
                self.assertTrue(extracted, f"{category}: nothing extracted")

    def test_no_gitbook_markup_leaks_into_any_entry(self):
        for category, extracted in self.results.items():
            for fn in extracted:
                for field in ("signature", "description"):
                    with self.subTest(category=category, fn=fn["name"],
                                      field=field):
                        self.assertNotRegex(fn[field], MARKUP_RE)

    def test_previously_dropped_functions_are_extracted(self):
        for category, names in self.MUST_EXTRACT.items():
            got = {fn["name"] for fn in self.results[category]}
            with self.subTest(category=category):
                self.assertLessEqual(names, got,
                                     f"missing: {sorted(names - got)}")

    def test_no_signature_ends_with_an_open_paren(self):
        # A wrapped signature cut at its first line ends in "(" -- the shape
        # every multi-line window-function signature had before DOCS-6889.
        for category, extracted in self.results.items():
            for fn in extracted:
                with self.subTest(category=category, fn=fn["name"]):
                    self.assertFalse(fn["signature"].endswith("("),
                                     fn["signature"])

    def test_aes_decrypt_signature_names_aes_decrypt(self):
        # The page once showed AES_ENCRYPT in AES_DECRYPT's Current tab.
        fns = self.results[
            "secondary-functions/encryption-hashing-and-compression-functions"]
        sig = next(fn["signature"] for fn in fns if fn["name"] == "AES_DECRYPT")
        self.assertTrue(sig.startswith("AES_DECRYPT("), sig)


if __name__ == "__main__":
    unittest.main()
