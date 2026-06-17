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

## Workflow (CI, stub)

`.github/workflows/extract-function-skills.yml` (not yet written) re-runs the
extractor when the relevant `server/reference/**` function pages change and
opens a PR regenerating the affected `granular/functions/*/SKILL.md` body, with
the hand-written scaffold sections preserved.

## Files

- `extract_function_category.py` — the extractor (Tier 2 pilot, used for
  `mariadb-json-functions`).
- `templates/function-category.scaffold.md` — the hand-written wrapper into
  which extracted entries are spliced.
