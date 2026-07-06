---
name: mariadb-create-table
description: "MariaDB-specific syntax and behavior for CREATE TABLE — atomic CREATE OR REPLACE, INVISIBLE / COMPRESSED columns, system-versioned and application-time PERIOD clauses, IGNORED indexes, table-level encryption, page compression, sequence and Aria table options, and the utf8/utf8mb4 trap. Use when writing, generating, or reviewing CREATE TABLE statements that target MariaDB."
---

# CREATE TABLE in MariaDB

*Last updated: 2026-06-01*

This skill covers the **delta between standard SQL `CREATE TABLE` and MariaDB's**. It assumes the agent already knows standard `CREATE TABLE name (col type, …)`. Everything below documents MariaDB-specific syntax, table options, column attributes, and behaviors.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user specifies another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `DROP TABLE x; CREATE TABLE x …` | `CREATE OR REPLACE TABLE x …` (atomic equivalent, no window where the table is missing) |
| `CHARSET = utf8` | `CHARSET = utf8mb4` — `utf8` is an alias for the legacy 3-byte form (`utf8mb3`) and cannot store 4-byte characters (most emoji, some CJK) |
| Manual `created_at` / `updated_at` audit columns | `CREATE TABLE … WITH SYSTEM VERSIONING` — see the `mariadb-system-versioned-tables` skill |
| `ROW_FORMAT = COMPRESSED` for "modern" disk savings | That's the older InnoDB compressed row format. For new tables on modern InnoDB/Aria, prefer `PAGE_COMPRESSED = 1` plus optional `PAGE_COMPRESSION_LEVEL = N` |
| Generated column with `STORED` | Works, but MariaDB's historical keyword is `PERSISTENT`. Both are accepted; `PERSISTENT` shows up in older code and in `SHOW CREATE TABLE` output |
| Foreign keys on a MyISAM / Aria table | Silently parsed and discarded — only InnoDB enforces foreign keys |
| `IF NOT EXISTS` on a table with a different schema | Skips creation and emits a **warning** (not error); the existing table is left untouched even if its definition differs |
| Wrapping `CREATE TABLE` in a transaction | DDL triggers an implicit commit. There is no way to roll back a `CREATE TABLE`; rely on atomic DDL (below) for crash safety instead |

## CREATE OR REPLACE

```sql
CREATE OR REPLACE TABLE t (id INT PRIMARY KEY);
```

- Atomic equivalent of `DROP TABLE IF EXISTS t; CREATE TABLE t …`.
- Cannot be combined with `IF NOT EXISTS`.
- Crash-safe but **not fully atomic** in the strict sense — recovery picks one side cleanly, but observers mid-statement may see the table missing. Plain `CREATE TABLE` *is* fully atomic (since 10.6.1).

## Temporal Tables — `PERIOD FOR …`

MariaDB supports three temporal forms via the `PERIOD FOR` clause:

```sql
-- System-versioned (transaction time, automatic history):
CREATE TABLE t (id INT, val INT) WITH SYSTEM VERSIONING;

-- Application-time period (business-valid time, application-managed):
CREATE TABLE t (
  id INT, val INT,
  valid_from DATE, valid_to DATE,
  PERIOD FOR effective (valid_from, valid_to)
);

-- Bitemporal (both at once):
CREATE TABLE t (
  id INT, val INT,
  valid_from DATE, valid_to DATE,
  PERIOD FOR effective (valid_from, valid_to)
) WITH SYSTEM VERSIONING;
```

For querying history, partitioning by `SYSTEM_TIME`, or removing old history, defer to the **`mariadb-system-versioned-tables`** skill.

Specific columns can be excluded from versioning:

```sql
CREATE TABLE t (
  id INT,
  login_counter INT WITHOUT SYSTEM VERSIONING
) WITH SYSTEM VERSIONING;
```

> **UPDATE behavior note:** for timestamp-based system versioning, a new history row is created for every `UPDATE` that touches a versioned column, even if no column value actually changes. See `mariadb-system-versioned-tables` for details.

## Column-Level MariaDB Extensions

| Clause | Effect |
|---|---|
| `col VARCHAR(N) COMPRESSED` | Per-value zlib compression on the column (transparent to clients) |
| `col INT INVISIBLE` | Excluded from `SELECT *`; explicit `SELECT col` still works; `INSERT` without column list skips it |
| `DEFAULT (expr)` | Defaults can be any deterministic expression — `DEFAULT (1+1)`, `DEFAULT(NOW() + INTERVAL 1 YEAR)`, `DEFAULT USER()` |
| `col INT GENERATED ALWAYS AS (expr) PERSISTENT` | Stored generated column. `PERSISTENT` is MariaDB's keyword; `STORED` is also accepted as an alias. Use `VIRTUAL` (default) for computed-on-read |
| `col INT GENERATED ALWAYS AS (expr) VIRTUAL` | Computed-on-read generated column (no storage cost, evaluated per query) |
| `col VECTOR(N)` *(since 11.7)* | Fixed-length float vector column — see the `mariadb-vector` skill |

## Index Definitions — MariaDB-Specific Options

```sql
INDEX idx_name (col1, col2) [index_type] [index_option …]
```

| Option | Meaning |
|---|---|
| `IGNORED` / `NOT IGNORED` *(since 10.6)* | Optimizer pretends the index doesn't exist (still maintained on writes). Use to "soft-disable" an index before dropping it |
| `INVISIBLE` / `VISIBLE` | Optimizer ignores the index; DML still updates it |
| `COMMENT '…'` | Free-text annotation, visible in `INFORMATION_SCHEMA.STATISTICS` |
| `WITH PARSER name` | Fulltext indexes only — pluggable parser |
| `CLUSTERING=YES` | Spider engine only |

Keywords `INDEX` and `KEY` are interchangeable in MariaDB.

## Table Options — MariaDB-Specific or Often-Confused

| Option | Meaning |
|---|---|
| `ENGINE = InnoDB` | Default engine. Set globally via `default_storage_engine`. If an engine isn't installed, substitution happens silently unless `sql_mode` includes `NO_ENGINE_SUBSTITUTION` |
| `ENCRYPTED = YES` | Per-table at-rest encryption. Requires an encryption key-management plugin (e.g. `file_key_management`) and `innodb_encrypt_tables`. Combine with `ENCRYPTION_KEY_ID = N` |
| `PAGE_COMPRESSED = 1` | InnoDB / Aria page-level compression (LZ4 / zstd / lzma / lz4hc / bzip2 / snappy, depending on which compression provider plugins are loaded). **Distinct from `ROW_FORMAT = COMPRESSED`** (older InnoDB zlib mechanism). Add `PAGE_COMPRESSION_LEVEL = 0..9` |
| `ROW_FORMAT = …` | Per-engine row layout. InnoDB: `COMPACT \| DYNAMIC \| COMPRESSED \| REDUNDANT`. Aria: `PAGE \| FIXED \| DYNAMIC`. MyISAM: `FIXED \| DYNAMIC \| COMPRESSED` |
| `SEQUENCE = 1` | Makes this `CREATE TABLE` produce a sequence instead of a regular table. Prefer the dedicated `CREATE SEQUENCE` statement |
| `TRANSACTIONAL = 1` | Crash-safe Aria. Aria-only; ignored on other engines |
| `IETF_QUOTES = YES` | Aria's IETF-style identifier quoting. Aria-only |
| `WITH SYSTEM VERSIONING` | Table-level versioning (see temporal section) |
| `UNION = (t1, t2, …)` | MERGE engine table list |
| `CONNECTION = '…'` | Connection string for FederatedX / CONNECT engines |
| `DATA DIRECTORY = '…'` / `INDEX DIRECTORY = '…'` | Place table data or indexes on a different filesystem. Absolute paths only |

## Atomic DDL

- Plain `CREATE TABLE` is **atomic** since 10.6.1 — crash recovery either has the table fully created or not at all.
- `CREATE OR REPLACE TABLE` is **crash-safe but not fully atomic** — see above.
- All DDL still triggers an implicit commit; there is no way to roll back a `CREATE TABLE` from inside a transaction.

## See Also

- **`mariadb-system-versioned-tables`** — full system-versioning, application-time, bitemporal, querying history, partitioning, removing history
- **`mariadb-vector`** — `VECTOR(N)` columns and vector indexes
- Canonical reference on `mariadb.com/docs`, consult only for edge cases not covered here: <https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table>
