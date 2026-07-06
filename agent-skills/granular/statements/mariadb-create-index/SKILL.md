---
name: mariadb-create-index
description: "MariaDB-specific syntax and behavior for CREATE INDEX / DROP INDEX — that it maps to ALTER TABLE (batch multiple adds), can't create a PRIMARY KEY, needs a prefix length on TEXT/BLOB columns, has no expression/functional indexes (index a generated column instead), real descending indexes (since 10.8), IGNORED indexes for safe optimizer testing, UNIQUE/FULLTEXT/SPATIAL/VECTOR kinds, USING BTREE/HASH/RTREE, CREATE OR REPLACE / IF NOT EXISTS, KEY_BLOCK_SIZE being ignored here, and dropping a PRIMARY KEY via DROP INDEX `PRIMARY`. Use when writing, generating, or reviewing CREATE INDEX / DROP INDEX statements that target MariaDB."
---

# CREATE INDEX in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL `CREATE INDEX` and MariaDB's**. It assumes the agent knows the basic `CREATE INDEX i ON t (col);` form. For defining indexes inline with the table, see `mariadb-create-table`; for *choosing* indexes and query-shape pitfalls, see the `mariadb-query-optimization` topical skill.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `CREATE INDEX` … to add a `PRIMARY KEY` | Not possible — `CREATE INDEX` cannot create a primary key. Use `ALTER TABLE t ADD PRIMARY KEY (…)` or define it in `CREATE TABLE` (preferable for InnoDB, which clusters on the PK and would otherwise rebuild) |
| `CREATE INDEX i ON t ((col1 + col2))` or any expression index | MariaDB has **no expression/functional index** in `CREATE INDEX` — index columns are plain column names only. Add a generated column and index that: `ALTER TABLE t ADD c INT AS (col1 + col2) PERSISTENT, ADD INDEX (c);` |
| Indexes a `TEXT`/`BLOB` column without a prefix length | A prefix length is **mandatory** for `TEXT`/`BLOB` (otherwise `ER_BLOB_KEY_WITHOUT_LENGTH`): `CREATE INDEX i ON t (body(255));` |
| Issues several `CREATE INDEX` statements on one table | Each `CREATE INDEX` maps to an `ALTER TABLE … ADD INDEX`, so N statements can mean N table operations. Add them in **one** `ALTER TABLE t ADD INDEX …, ADD INDEX …` to do the work once |
| Filters with a function on the indexed column (`WHERE DATE(ts) = …`, `WHERE LOWER(email) = …`) and expects the index to be used | Wrapping an indexed column in a function defeats the index. Rewrite as a range (`ts >= … AND ts < …`), or index a generated column holding the expression. See `mariadb-query-optimization` |
| Assumes a `DESC` index key is decorative / ignored | Descending index parts are **physically real** *(since 10.8)* — `CREATE INDEX i ON t (a ASC, b DESC)` stores `b` in reverse order, which can serve mixed-direction `ORDER BY` without a filesort |
| Drops an index just to measure whether a query still needs it | Mark it `IGNORED` instead — the optimizer ignores it while it stays fully maintained, so you can test impact and flip it back instantly: `ALTER TABLE t ALTER INDEX i IGNORED;` (or `IGNORED` in the `CREATE INDEX` options) |
| `DROP INDEX i; CREATE INDEX i …` to change an index | `CREATE OR REPLACE INDEX i ON t (…)` drops and recreates it in one statement. `CREATE INDEX IF NOT EXISTS i …` warns (note) instead of erroring if it already exists |
| Tries `DROP INDEX` to remove a primary key by table name | Drop it by the reserved name, quoted: ``DROP INDEX `PRIMARY` ON t;`` |
| Sets `KEY_BLOCK_SIZE` on a `CREATE INDEX` expecting it to take effect | `KEY_BLOCK_SIZE` is **ignored** by `CREATE INDEX` (it still shows in `SHOW CREATE TABLE`). Set it at the table level if you need it |

## Syntax

```sql
CREATE [OR REPLACE] [UNIQUE | FULLTEXT | SPATIAL | VECTOR] INDEX
    [IF NOT EXISTS] index_name
    [USING {BTREE | HASH | RTREE}]
    ON tbl_name (col_name [(length)] [ASC | DESC], …)
    [WAIT n | NOWAIT]
    [index_option …]
    [algorithm_option | lock_option] …;
```

Key points:

- **Maps to `ALTER TABLE`.** `CREATE INDEX` and `DROP INDEX` are shortcuts for `ALTER TABLE … ADD/DROP INDEX`; the online-DDL `ALGORITHM` and `LOCK` clauses apply (see `mariadb-alter-table`).
- **Index kinds:** `UNIQUE`, `FULLTEXT`, `SPATIAL`, and `VECTOR` *(since 11.7)*. `VECTOR` indexes take `DISTANCE = {EUCLIDEAN | COSINE}` and `M = n` options — see the `mariadb-vector` topical skill.
- **`USING BTREE | HASH | RTREE`** selects the index algorithm where the engine supports a choice.
- **`IGNORED` / `NOT IGNORED`** toggles whether the optimizer considers the index, without dropping it.
- **`WITHOUT OVERLAPS`** (in a `UNIQUE` index) constrains application-time periods so they can't overlap — see temporal-tables material.
- **`WAIT n` / `NOWAIT`** bounds the metadata-lock wait.

```sql
CREATE UNIQUE INDEX uq_email ON users (email);
CREATE INDEX i_body ON articles (body(255));          -- prefix required for TEXT/BLOB
CREATE OR REPLACE INDEX i_created ON orders (created_at DESC);
```

## `DROP INDEX`

```sql
DROP INDEX [IF EXISTS] index_name ON tbl_name [WAIT n | NOWAIT];
```

Maps to `ALTER TABLE … DROP INDEX`. Use ``DROP INDEX `PRIMARY` ON t`` to drop a primary key (the quotes are required — `PRIMARY` is a keyword). `IF EXISTS` downgrades a missing index to a warning.

## See Also

- **`mariadb-create-table`** — defining indexes inline at table creation (preferable for InnoDB primary keys) and the full index-definition surface
- **`mariadb-alter-table`** — what `CREATE INDEX`/`DROP INDEX` actually map to; batching several index changes into one statement; `ALGORITHM`/`LOCK` online-DDL options
- **`mariadb-query-optimization`** (topical) — choosing indexes, and why functions on indexed columns prevent index use
- **`mariadb-vector`** (topical) — `VECTOR` indexes, `DISTANCE`, and `M`
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-index>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/drop/drop-index>
