# Tier 2 function-skill extractor

Generates the per-function entries for `granular/functions/*/SKILL.md` from the
canonical MariaDB function reference pages. The hand-written parts of each skill
(frontmatter, intro, the category-level "What LLMs Often Miss" table) are
**not** generated — they wrap the extractor's output via a template.

This mirrors the minimalism of [`help-tables/markdown_extractor.py`](../../help-tables/markdown_extractor.py):
regex-based, no markdown-library dependency, reads the canonical doc template.

## Usage

```bash
./extract_function_category.py \
  ../../server/reference/sql-functions/special-functions/json-functions \
  [--exclude FUNCTION ...]
```

Output is Markdown on stdout — the dense per-function listing. Assemble it into
a `SKILL.md` by wrapping it with `templates/function-category.scaffold.md`.

## Tests

```bash
python3 -m unittest discover -s agent-skills/extractor -p 'test_*.py' -v
```

Run from the repo root. `test_extract_function_category.py` pins the page
shapes the extractor must survive (version tabs that open with a hint, wrapped
signatures, mixed-case function names) and runs every category against the
real pages, failing on GitBook markup in an entry or a function going missing.
CI runs it on every PR (`doc-lint-test.yml`, job `extractor-test`) and before
each scheduled regeneration. A failure is usually caused by a page-format change
elsewhere in the docs, not by an extractor edit (DOCS-6889).

## Workflow (CI)

`.github/workflows/extract-function-skills.yml` runs the tests, then
`regenerate.py`, on a schedule. If any catalog changed, it opens or refreshes a
PR that rewrites only the generated block of each affected
`granular/functions/*/SKILL.md`. The hand-written scaffold sections are kept.
**Read that PR's diff before merging.** The content gates check that it is
well-formed, not that every function is still there.

## Files

- `extract_function_category.py`: the extractor.
- `regenerate.py`: runs the extractor for every Tier 2 category and splices
  the output into each skill's `BEGIN/END GENERATED` block (`--check` reports
  drift without writing).
- `test_extract_function_category.py`: the tests above.
- `templates/function-category.scaffold.md`: the hand-written wrapper into
  which extracted entries are spliced.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
