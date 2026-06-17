#!/usr/bin/env python3
"""
Tier 2 extractor for MariaDB DX skill files.

Walks a single SQL-function category directory under
`mariadb-docs/server/reference/sql-functions/.../<category>/` and emits a
dense per-function listing suitable for embedding in a SKILL.md.

Usage:
    extract_function_category.py <category-dir> [--exclude name [name ...]]

Output: Markdown on stdout. Hand-curated frontmatter, intro, and
"What LLMs Often Miss" sections must be assembled around it by a wrapping
SKILL.md template.

The extractor is regex-based (no markdown library dependency) and follows
the same minimalism as mariadb-docs/help-tables/markdown_extractor.py.

Pages are expected to use the canonical MariaDB doc template:
    ---
    description: >-
      <one or two lines>
    ---
    # FUNCTION_NAME
    [optional {% hint style="info" %}...available from MariaDB X.Y...{% endhint %}]
    ## Syntax
    ```sql
    <signature>
    ```
    ## Description
    ...
Pages that don't match are reported on stderr and skipped.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ----------------------------------------------------------------------
# Regex extractors
# ----------------------------------------------------------------------

# Pull the YAML `description: >- ... ---` block at the top of the file.
FRONTMATTER_RE = re.compile(
    r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL
)
DESC_RE = re.compile(
    r"^description:\s*>-?\s*\n((?:  .*\n)+)", re.MULTILINE
)

# Title line: `# NAME` — names sometimes have GitBook-escaped underscores
# (e.g. `JSON\_EXTRACT`).
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

# First fenced SQL code block under the Syntax heading.
# Tolerates `## Syntax` and `### Syntax` (some pages are inconsistent).
SYNTAX_BLOCK_RE = re.compile(
    r"^#{2,3}\s+Syntax\s*\n+```sql\s*\n(.*?)\n```",
    re.DOTALL | re.MULTILINE,
)

# First non-empty paragraph under the `## Description` heading. Skips
# leading blank lines, captures until the next blank line or heading.
DESCRIPTION_BODY_RE = re.compile(
    r"^##\s+Description\s*\n+(.+?)(?:\n\n|\n#{2,})",
    re.DOTALL | re.MULTILINE,
)

# Alias-only stub: pages like JSON_PRETTY whose body is just
# "FOO is an alias for [BAR](bar.md)." with no Syntax section.
ALIAS_RE = re.compile(
    r"`?\w+`?\s+is\s+an\s+alias\s+for\s+\[?`?(\w+)`?\]?",
    re.IGNORECASE,
)

# Available-from-version hint: GitBook hint blocks that say
# "available from MariaDB X.Y" or "added in MariaDB X.Y".
SINCE_RE = re.compile(
    r"(?:available\s+from|added\s+in|introduced\s+in)\s+MariaDB\s+(\d+\.\d+(?:\.\d+)?)",
    re.IGNORECASE,
)

# GitBook markup that we want to strip from extracted prose so the agent
# isn't reading workflow noise.
GITBOOK_HINT_RE = re.compile(
    r"\{%\s*hint[^%]*%\}.*?\{%\s*endhint\s*%\}", re.DOTALL
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
MULTISPACE_RE = re.compile(r"\s+")


def unescape_title(s: str) -> str:
    """GitBook escapes `_` as `\\_` inside Markdown headings. Undo it."""
    return s.replace("\\_", "_").strip()


def clean_description(raw: str) -> str:
    """Normalize a multi-line YAML folded-scalar description into one line."""
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    return " ".join(lines)


def first_signature(syntax_block: str) -> str:
    """Take the first non-blank line of the syntax code block as the signature."""
    for line in syntax_block.splitlines():
        line = line.strip()
        if line:
            return line
    return ""


def clean_prose(s: str) -> str:
    """Strip GitBook markup and collapse whitespace for one-line display."""
    s = GITBOOK_HINT_RE.sub("", s)
    s = MARKDOWN_LINK_RE.sub(r"\1", s)
    s = s.replace("\\_", "_")
    s = MULTISPACE_RE.sub(" ", s)
    return s.strip()


def first_sentence(paragraph: str) -> str:
    """Return the first sentence (ending in '.', '!', or '?') of a paragraph."""
    paragraph = paragraph.strip()
    m = re.match(r"(.+?[.!?])(?:\s|$)", paragraph, re.DOTALL)
    return m.group(1) if m else paragraph


# ----------------------------------------------------------------------
# Per-page extraction
# ----------------------------------------------------------------------


class ExtractionError(Exception):
    pass


def extract_function(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    title_match = TITLE_RE.search(text)
    if not title_match:
        raise ExtractionError(f"no `# Title` heading in {path.name}")
    name = unescape_title(title_match.group(1))

    # Editorial pages (e.g. "Differences between X and Y") don't look like
    # function names. Function names are uppercase with underscores/digits.
    if not re.match(r"^[A-Z][A-Z0-9_]*$", name):
        raise ExtractionError(
            f"{path.name}: title `{name}` doesn't look like a function — editorial page?"
        )

    since_match = SINCE_RE.search(text)
    since = since_match.group(1) if since_match else ""

    # Strip GitBook hints before scanning for alias / description so the
    # hint text doesn't pollute the prose extraction.
    body = GITBOOK_HINT_RE.sub("", text)

    # Alias-only stub path: no Syntax block, body says "X is an alias for Y".
    syntax_match = SYNTAX_BLOCK_RE.search(text)
    if not syntax_match:
        alias = ALIAS_RE.search(body)
        if alias:
            return {
                "path": path,
                "name": name,
                "signature": "",
                "alias_of": alias.group(1).upper(),
                "description": "",
                "since": since,
            }
        raise ExtractionError(f"no Syntax SQL code block in {path.name}")

    signature = first_signature(syntax_match.group(1))

    # Prefer the first sentence of `## Description` (reference-quality prose)
    # over the YAML frontmatter description (often SEO-y).
    description = ""
    desc_match = DESCRIPTION_BODY_RE.search(body)
    if desc_match:
        description = first_sentence(clean_prose(desc_match.group(1)))

    # Fall back to frontmatter description if no Description body found.
    if not description:
        fm = FRONTMATTER_RE.search(text)
        if fm:
            d = DESC_RE.search(fm.group(1) + "\n")
            if d:
                description = clean_prose(clean_description(d.group(1)))

    return {
        "path": path,
        "name": name,
        "signature": signature,
        "alias_of": None,
        "description": description,
        "since": since,
    }


# ----------------------------------------------------------------------
# Rendering
# ----------------------------------------------------------------------


def render_entry(fn: dict) -> str:
    """Render one function as a tight per-function block.

    Standard form:
        ### NAME
        `signature`
        Description. *(since X.Y)*

    Alias form:
        ### NAME
        Alias for `OTHER`. *(since X.Y)*
    """
    since = f" *(since {fn['since']})*" if fn["since"] else ""

    if fn.get("alias_of"):
        return f"### {fn['name']}\nAlias for `{fn['alias_of']}`.{since}\n"

    desc = fn["description"] or "(no description in source)"
    return (
        f"### {fn['name']}\n"
        f"`{fn['signature']}`  \n"
        f"{desc}{since}\n"
    )


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("category_dir", type=Path,
                        help="Directory of function reference pages")
    parser.add_argument("--exclude", nargs="*", default=[],
                        help="Filenames (without .md) to skip")
    args = parser.parse_args()

    excluded = set(args.exclude) | {"README", "SUMMARY"}

    pages = sorted(p for p in args.category_dir.glob("*.md")
                   if p.stem not in excluded)

    extracted: list[dict] = []
    errors: list[str] = []

    for page in pages:
        try:
            extracted.append(extract_function(page))
        except ExtractionError as e:
            errors.append(str(e))

    extracted.sort(key=lambda fn: fn["name"])

    print(f"<!-- Extracted from {args.category_dir} -->")
    print(f"<!-- {len(extracted)} functions, "
          f"{len(errors)} pages skipped on extraction failure -->")
    print()
    for fn in extracted:
        print(render_entry(fn))

    if errors:
        print("=" * 60, file=sys.stderr)
        print("Extraction errors (these pages were skipped):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
