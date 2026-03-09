# MariaDB Help Tables Pipeline

This document describes the automated pipeline that generates `fill_help_tables.sql` from the MariaDB documentation Markdown files. The generated SQL populates the `mysql.help_topic`, `mysql.help_category`, `mysql.help_keyword`, and `mysql.help_relation` tables, powering the `HELP` command in the MariaDB client.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Components](#components)
  - [markdown_extractor.py](#markdown_extractorpy)
  - [validate_sql.py](#validate_sqlpy)
  - [generate-help-tables.yml](#generate-help-tablesyml)
- [Output Format](#output-format)
- [How It Works](#how-it-works)
- [Data Constraints & Edge Cases](#data-constraints--edge-cases)
- [Testing Locally](#testing-locally)
- [CI/CD Pipeline](#cicd-pipeline)
- [Troubleshooting](#troubleshooting)
- [Configuration Reference](#configuration-reference)

---

## Overview

When documentation authors edit Markdown files under `server/reference/`, a CI pipeline automatically:

1. Extracts content (syntax, description, examples) from each `.md` file
2. Generates SQL `INSERT` statements matching the MariaDB help table schema
3. Validates the SQL for correctness
4. Uploads the artifact for review
5. Notifies Slack on failure

When a release is approaching, a team member downloads the artifact from the latest successful CI run and delivers it to the server team manually.

---

## Architecture

```
┌──────────────────────┐
│  Markdown docs       │
│  server/reference/   │
│  **/*.md             │
└──────────┬───────────┘
           │  git push / PR
           ▼
┌──────────────────────┐
│  GitHub Actions      │
│  generate-help-      │
│  tables.yml          │
│                      │
│  1. markdown_        │
│     extractor.py     │
│  2. validate_sql.py  │
│  3. Upload artifact  │
└──────────┬───────────┘
           │  on failure
           ▼
┌──────────────────────┐
│  Slack Notification  │
│  (webhook)           │
└──────────────────────┘

           Pre-release:
┌──────────────────────┐
│  Team member         │
│  downloads artifact  │
│  from Actions tab    │
│  and delivers to     │
│  server team         │
└──────────────────────┘
```

---

## Components

### markdown_extractor.py

**Location:** `help-tables/markdown_extractor.py`

**Purpose:** Reads all Markdown files under `server/reference/`, extracts structured content, and generates `fill_help_tables.sql`.

**Usage:**
```bash
python help-tables/markdown_extractor.py
```

**Output:**
- `fill_help_tables.sql` — Complete SQL file ready to load into MariaDB
- `failed_files.txt` — List of files that could not be processed (for review)

**Key functions:**

| Function | Description |
|---|---|
| `get_files()` | Discovers `.md` files under `server/reference/`, excluding configured directories and near-empty READMEs (≤3 lines) |
| `find_line_range()` | Finds the content range in a file: from the `# Title` heading to the first `## See Also`, `<sub>`, or `{% @marketo` marker |
| `extract_sections()` | Splits content into syntax, description, and examples by matching `## Syntax`, `## Description`/`## Overview`, and `## Example(s)` headings |
| `extract_code_block()` | Extracts content from the first `` ```sql `` fenced code block |
| `strip_markdown()` | Converts Markdown to plain text: strips links, backticks, bold/italic, template tags (`{% %}`), escaped underscores |
| `build_output()` | Assembles the final description with `Syntax`, `Description`, and `Examples` section headers (with underlines), appends the URL, and applies truncation |
| `truncate_to_bytes()` | Ensures description fits within MariaDB's `TEXT` column limit (60,000 bytes, conservative vs 65,535 max) |
| `escape_sql()` | Escapes backslashes, single quotes, and newlines for safe SQL insertion |
| `process_single_file()` | End-to-end processing of one `.md` file into a topic dict |
| `process_batch()` | Processes all files with case-insensitive deduplication of topic names |
| `extract_keywords()` | Splits a topic name into keyword tokens for `help_keyword` |
| `build_keywords_and_relations()` | Generates `help_keyword` and `help_relation` INSERT statements with relation deduplication |
| `generate_category_inserts()` | Generates INSERT statements for the static `help_category` table |
| `write_output()` | Writes the complete SQL file: preamble → categories → topics → keywords → relations |

**Configuration constants:**

| Constant | Description |
|---|---|
| `EXCLUDED_DIRS` | Directories to skip: `system-tables`, `error-codes`, `clientserver-protocol`, `product-development` |
| `CATEGORY_MAP` | Maps directory path segments to `help_category_id` values. Default is `35` (Contents) |
| `HELP_CATEGORIES` | Static list of 39 help categories with IDs, names, parent IDs |
| `SQL_PREAMBLE` | GPL header + setup commands (`set names 'utf8'`, `delete from` statements) |

---

### validate_sql.py

**Location:** `help-tables/validate_sql.py`

**Purpose:** Validates the generated `fill_help_tables.sql` for structural correctness.

**Usage:**
```bash
python validate_sql.py fill_help_tables.sql
```

**Exit codes:**
- `0` — All checks passed
- `1` — Validation failed

**Checks performed:**

| Check | Description |
|---|---|
| File exists and is non-empty | Basic sanity |
| Line classification | Every line must be a recognized type (comment, preamble, or INSERT into one of the 4 tables) |
| Topic ID uniqueness | No duplicate `help_topic_id` values |
| Topic name uniqueness | Warns on duplicate names |
| Keyword ID uniqueness | No duplicate `help_keyword_id` values |
| Relation referential integrity | Every `help_relation` references a valid `topic_id` and `keyword_id` |
| Statement termination | All INSERT statements end with `);` |
| Minimum counts | At least 500 topics, 10 categories, 100 keywords |

---

### generate-help-tables.yml

**Location:** `.github/workflows/generate-help-tables.yml`

**Trigger:** Automatically on push or pull request when files matching these paths change:
- `server/reference/**/*.md`
- `markdown_extractor.py`

**Jobs:**

1. **generate** — Checks out the repo, runs `markdown_extractor.py`, validates with `validate_sql.py`, uploads `fill_help_tables.sql` as a GitHub Actions artifact (retained 30 days)
2. **notify** — Runs only if `generate` fails. Sends a Slack message via incoming webhook with repo, branch, commit, actor, and run link

**Required secrets:**
- `SLACK_WEBHOOK_URL` — Slack incoming webhook URL for failure notifications

---

## Output Format

The generated `fill_help_tables.sql` matches the format of MariaDB's original `fill_help_tables.sql` shipped with the server. Structure:

```sql
-- GPL license header
-- "DO NOT EDIT THIS FILE. It is generated automatically."

set names 'utf8';
set sql_log_bin = 0;
use mysql;
delete from help_topic;
delete from help_category;
delete from help_keyword;
delete from help_relation;

-- help_category INSERTs (39 static categories)
insert into help_category (help_category_id,name,parent_category_id,url) values (...);

-- help_topic INSERTs (one per documentation page, ~1000 entries)
INSERT INTO help_topic (help_topic_id, help_category_id, name, description, example, url) VALUES (...);

-- help_keyword INSERTs (one per unique keyword token, ~975 entries)
insert into help_keyword (help_keyword_id,name) values (...);

-- help_relation INSERTs (maps topics to keywords, ~1685 entries)
insert into help_relation (help_topic_id,help_keyword_id) values (...);
```

Each topic's `description` field contains:

```
Syntax
------

<syntax from code block>

Description
-----------

<plain-text description, markdown stripped>

Examples
--------

<SQL examples from code block>

URL: https://mariadb.com/docs/<path>
```

The `example` field is left empty (all content is in `description`), matching the original MariaDB format.

---

## How It Works

### Markdown File Processing

1. **Discovery:** `get_files()` walks `server/reference/` recursively, finding all `.md` files. Skips excluded directories and READMEs with ≤3 lines.

2. **Content extraction:** For each file, `find_line_range()` identifies the content between the `# Title` heading and the end markers (`## See Also`, `<sub>`, `{% @marketo`).

3. **Section parsing:** `extract_sections()` looks for `## Syntax`, `## Description` (or `## Overview`), and `## Example(s)` headings to split the content. If no headings are found, falls back to treating everything after the title as description.

4. **Code block extraction:** `extract_code_block()` pulls content from the first `` ```sql `` fenced code block in each section.

5. **Output assembly:** `build_output()` combines sections with formatted headers (`Syntax\n------`), strips all Markdown formatting, appends the URL, and truncates if needed.

6. **Deduplication:** `process_batch()` performs case-insensitive deduplication of topic names. When two files share the same name, plugin stub pages (descriptions starting with phrases like "This plugin implements") are discarded in favour of the real reference page. If neither candidate is a stub, the alphabetically earlier path wins.

7. **Keyword generation:** `build_keywords_and_relations()` splits each topic name into tokens, assigns keyword IDs, and creates relation mappings (with deduplication).

---

## Data Constraints & Edge Cases

These constraints match the MariaDB `mysql.help_topic` table schema:

| Constraint | Limit | How It's Handled |
|---|---|---|
| `name` column: `CHAR(64)` | Max 64 characters | Truncated to 64 chars in `build_output()` |
| `description` column: `TEXT` | Max 65,535 bytes | Truncated to 60,000 bytes with a `[Truncated]` note in `truncate_to_bytes()` |
| `name` uniqueness | Case-insensitive unique key | Case-insensitive deduplication in `process_batch()` (e.g., `INET4` vs `inet4`) |
| `help_relation` primary key | Unique `(topic_id, keyword_id)` | Deduplicated via `seen_relations` set in `build_keywords_and_relations()` |
| SQL special characters | Backslashes, quotes, newlines | `escape_sql()` escapes `\` → `\\`, `'` → `''`, `\n` → `\\n` (backslashes first) |
| Markdown artifacts | Links, backticks, bold, template tags | `strip_markdown()` converts to plain text |

---

## Testing Locally

### Run the extractor

```bash
python help-tables/markdown_extractor.py
```

Expected output:
```
Found 1246 files to process
Processed: 1009 files
Failed: 237 files
Written to fill_help_tables.sql
  Categories: 39
  Topics: 1009
  Keywords: 975
  Relations: 1685
```

### Validate the output

```bash
python help-tables/validate_sql.py help-tables/fill_help_tables.sql
```

### End-to-end test with MariaDB (Docker)

```bash
# Start a MariaDB container
docker run -d --name webops-mariadb -e MARIADB_ROOT_PASSWORD=changeme mariadb:10.4

# Load the generated SQL
docker exec -i webops-mariadb mysql -uroot -pchangeme < help-tables/fill_help_tables.sql

# Connect and test HELP commands
docker exec -it webops-mariadb mysql -uroot -pchangeme

# Inside the MariaDB shell:
HELP 'contents';     -- Lists all topics and categories
HELP 'UNCOMPRESS';   -- Shows a specific topic
HELP 'AVG';          -- Shows another topic
HELP 'SELECT';       -- Shows SELECT topic
```

### Compare with original MariaDB help tables

```bash
# Load the original (shipped with MariaDB)
docker exec webops-mariadb bash -c "mysql -uroot -pchangeme < /usr/share/mysql/fill_help_tables.sql"

# Test original
docker exec -it webops-mariadb mysql -uroot -pchangeme
HELP 'UNCOMPRESS';

# Reload ours
docker exec -i webops-mariadb mysql -uroot -pchangeme < help-tables/fill_help_tables.sql
HELP 'UNCOMPRESS';
```

### Clean up

```bash
docker stop webops-mariadb && docker rm webops-mariadb
```

---

## CI/CD Pipeline

### Automatic (on every push)

1. Developer edits a `.md` file under `server/reference/`
2. On push/PR, `generate-help-tables.yml` runs automatically
3. If generation or validation fails, Slack notification is sent
4. On success, `fill_help_tables.sql` is uploaded as a GitHub Actions artifact

### Pre-release artifact download

1. Go to **Actions** → **Generate Help Tables**
2. Open the latest successful run on the `main` branch
3. Scroll to **Artifacts** at the bottom of the run summary
4. Download **fill_help_tables** — this is the ready-to-use SQL file
5. Deliver the file to the server team or upload it directly to the server repo

### Required GitHub Secrets

| Secret | Purpose |
|---|---|
| `SLACK_WEBHOOK_URL` | Slack incoming webhook for failure notifications |

---

## Troubleshooting

### "Failed to parse" files

Check `failed_files.txt` after running the extractor. Common causes:
- No `# Title` heading found
- No meaningful content (empty description and no examples)
- Duplicate topic name (case-insensitive) — first occurrence wins

### SQL load errors

| Error | Cause | Fix |
|---|---|---|
| `Data too long for column 'description'` | Description exceeds 65,535 bytes | `truncate_to_bytes()` should handle this. Check if the limit is set correctly. |
| `Data too long for column 'name'` | Name exceeds 64 characters | `build_output()` truncates names. Verify truncation logic. |
| `Duplicate entry for key 'name'` | Case-insensitive name collision | `process_batch()` deduplicates. Check `seen_names` logic. |
| `Duplicate entry for key 'PRIMARY'` in help_relation | Duplicate (topic_id, keyword_id) pair | `build_keywords_and_relations()` deduplicates. Check `seen_relations` logic. |
| `Unknown command '\'` | Unescaped backslash in SQL | `escape_sql()` must escape `\` before other characters. |

### Slack notification not firing

1. Verify the `SLACK_WEBHOOK_URL` secret is set in the repository settings
2. The notify job only runs when the `generate` job fails (`if: failure()`)
3. Check the Actions run log for the notify job

### Adding a new category

1. Add the category tuple to `HELP_CATEGORIES` in `markdown_extractor.py`
2. Add the directory-to-category mapping in `CATEGORY_MAP`
3. The validator will catch if the minimum category count drops

### Adding new excluded directories

Add the directory name to `EXCLUDED_DIRS` in `markdown_extractor.py`.

---

## Configuration Reference

### File Locations

| File | Purpose |
|---|---|
| `help-tables/markdown_extractor.py` | Main extraction script |
| `help-tables/validate_sql.py` | SQL validation script |
| `help-tables/fill_help_tables.sql` | Generated output (git-ignored or committed as needed) |
| `help-tables/failed_files.txt` | List of unprocessed files (generated on each run) |
| `help-tables/HELP_TABLES_PIPELINE.md` | This documentation |
| `.github/workflows/generate-help-tables.yml` | CI validation and artifact upload workflow |

### Dependencies

- **Python 3.11+** — No external packages required (uses only `re`, `pathlib`, `sys`)
- **MariaDB 10.4+** — For E2E testing
- **Docker** — Optional, for local E2E testing

### Source Documentation Path

All Markdown source files live under:
```
server/reference/
```

### URL Format

Generated URLs follow:
```
https://mariadb.com/docs/{path_without_.md_extension}
```

Example: `server/reference/sql-functions/.../uncompress.md` →
`https://mariadb.com/docs/server/reference/sql-functions/.../uncompress`
