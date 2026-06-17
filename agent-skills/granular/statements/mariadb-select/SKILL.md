---
name: mariadb-select
description: "MariaDB-specific syntax and behavior for SELECT — optimizer hints (/*+ ... */, JOIN_PREFIX/JOIN_ORDER/JOIN_FIXED_ORDER/JOIN_SUFFIX, MAX_EXECUTION_TIME) and legacy query-level hints, LIMIT extensions (comma-form, ROWS EXAMINED), OFFSET … FETCH … ONLY/WITH TIES, FOR UPDATE / LOCK IN SHARE MODE with WAIT/NOWAIT/SKIP LOCKED, PARTITION pruning, FOR SYSTEM_TIME temporal queries, SELECT INTO OUTFILE/DUMPFILE/variable, WITH ROLLUP, max_statement_time, FROM DUAL. Covers SELECT, SELECT INTO OUTFILE, SELECT INTO DUMPFILE, SELECT … OFFSET … FETCH, and SELECT WITH ROLLUP. Use when writing, generating, or reviewing SELECT statements that target MariaDB."
---

# SELECT in MariaDB

*Last updated: 2026-06-02*

This skill covers the **delta between standard SQL `SELECT` and MariaDB's**. It assumes the agent already knows the standard form (`SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT …`). Everything below documents MariaDB-specific syntax, locking semantics, file output, optimizer-hint variants, and the most common LLM traps. Consolidates **SELECT**, **SELECT INTO OUTFILE**, **SELECT INTO DUMPFILE**, **SELECT … OFFSET … FETCH**, and **SELECT WITH ROLLUP** into a single lookup.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `SELECT SQL_CALC_FOUND_ROWS …` + `SELECT FOUND_ROWS()` for paginated total | Run a separate `SELECT COUNT(*) …` instead. `SQL_CALC_FOUND_ROWS` is legacy and typically *slower* than a dedicated count on modern InnoDB, because it materializes the full result set ignoring `LIMIT` |
| `LIMIT 100, 10` (comma form: offset first, count second) | Prefer `LIMIT 10 OFFSET 100` — both work, but the comma form puts offset and count in the opposite order from most other databases and is a common source of off-by-N bugs |
| `SELECT … FOR UPDATE` in a worker queue | Add `SKIP LOCKED` so workers don't block each other: `SELECT … FOR UPDATE SKIP LOCKED`. *InnoDB only* — silently ignored on other engines (no error, just sequential locking behavior) |
| `SELECT … INTO OUTFILE '/tmp/x'` and the file already exists | Will error — `INTO OUTFILE` and `INTO DUMPFILE` **never overwrite**. Either delete first or write to a fresh path. Also requires the `FILE` privilege and the path must satisfy `secure_file_priv` |
| `SELECT … WITH ROLLUP ORDER BY x` | `WITH ROLLUP` is incompatible with `ORDER BY` — use `ASC`/`DESC` on the `GROUP BY` columns instead. The super-aggregate rows always come last regardless |
| Worrying about a long query running forever | Either `SELECT /*+ MAX_EXECUTION_TIME(5000) */ …` (since 12.0) or `SET STATEMENT max_statement_time = 5 FOR SELECT …` (older) — both bound the statement at the server level |
| Unbounded `SELECT` that might scan too much during exploration | `LIMIT 1000 ROWS EXAMINED 100000` — caps both rows returned *and* rows examined (a MariaDB-specific safety net not in standard SQL) |
| `JOIN_PREFIX(t1, t2)` written as an old-style optimizer hint | The join-order hints (`JOIN_PREFIX`, `JOIN_ORDER`, `JOIN_FIXED_ORDER`, `JOIN_SUFFIX`) are *only* valid inside the `/*+ … */` hint comment syntax (since 12.0). The legacy hint keywords (`STRAIGHT_JOIN`, `HIGH_PRIORITY`, etc.) sit between `SELECT` and the column list and don't use the `/*+ */` form |
| `SQL_CACHE` / `SQL_NO_CACHE` hints | The query cache is **off by default** (`query_cache_type=0`) and is generally counter-productive on modern InnoDB workloads (high write concurrency invalidates cached entries constantly). Drop these hints from generated SQL unless the user has explicitly enabled the cache and is on a read-mostly workload |

## Optimizer Hints

Two distinct surfaces. Both exist; they're not interchangeable.

### 1. Hint-comment form (newer, recommended)

```sql
SELECT /*+ MAX_EXECUTION_TIME(5000) JOIN_ORDER(t2, t1) */
  t1.a, t2.b FROM t1 JOIN t2 ON t1.id = t2.id;
```

| Hint | Effect | Since |
|---|---|---|
| `MAX_EXECUTION_TIME(N)` | Cap statement at N milliseconds | 12.0 |
| `JOIN_PREFIX(t, …)` | Force these tables to be joined first | 12.0 |
| `JOIN_ORDER(t, …)` | Hint join order without making it absolute | 12.0 |
| `JOIN_FIXED_ORDER(t, …)` | Hard-fix the join order to exactly this | 12.0 |
| `JOIN_SUFFIX(t, …)` | Force these tables to be joined last | 12.0 |

The hint-comment block must come **immediately after `SELECT`**, before any other modifiers. Multiple hints can share one comment. Available since **11.8** as syntax; specific hints listed above shipped in 12.0.

### 2. Legacy keyword form (still supported)

These sit as bare keywords between `SELECT` and the column list:

| Keyword | Effect |
|---|---|
| `STRAIGHT_JOIN` | Join tables in the order they appear in `FROM` |
| `HIGH_PRIORITY` | Give this `SELECT` higher priority than competing writes (MyISAM-era; minimal effect on modern InnoDB) |
| `SQL_SMALL_RESULT` / `SQL_BIG_RESULT` | Optimizer hint about expected result-set size (drives temp-table choice) |
| `SQL_BUFFER_RESULT` | Force result buffering to release table locks earlier |
| `SQL_CALC_FOUND_ROWS` | Counts rows ignoring `LIMIT` for `FOUND_ROWS()` — see "What LLMs Often Miss" |
| `SQL_CACHE` / `SQL_NO_CACHE` | Per-statement override of the query cache. The cache is off by default and typically harmful on modern workloads; the hints are still parsed but rarely useful |

## LIMIT, OFFSET, FETCH

Three syntaxes for pagination — all valid:

```sql
-- Comma form (offset first, count second):
SELECT … FROM t LIMIT 100, 10;

-- With explicit OFFSET keyword:
SELECT … FROM t LIMIT 10 OFFSET 100;

-- Standard SQL OFFSET … FETCH (since 10.6):
SELECT … FROM t ORDER BY id OFFSET 100 ROWS FETCH NEXT 10 ROWS ONLY;
```

Notes:

- `LIMIT row_count OFFSET offset` is the safer, less ambiguous form. The comma form puts offset first; the `OFFSET` keyword form puts count first.
- `FETCH … WITH TIES` (also since 10.6) returns extra rows that tie for the last spot — **requires an `ORDER BY` clause** or errors out (ER 4180).
- `FIRST` and `NEXT` are interchangeable; `ROW` and `ROWS` are interchangeable.
- **`LIMIT … ROWS EXAMINED N`** is MariaDB-specific:

  ```sql
  SELECT … FROM t WHERE … LIMIT 10 ROWS EXAMINED 100000;
  ```

  Stops the scan once N rows have been examined (not just returned). Useful as a safety bound during exploration, or to enforce a soft SLA on a query.

## Row Locking — `FOR UPDATE`, `LOCK IN SHARE MODE`

```sql
SELECT … FROM t WHERE … FOR UPDATE       [WAIT n | NOWAIT | SKIP LOCKED];
SELECT … FROM t WHERE … LOCK IN SHARE MODE [WAIT n | NOWAIT | SKIP LOCKED];
```

| Modifier | Effect |
|---|---|
| `WAIT n` | Wait up to *n* seconds for the lock, then error with lock-wait-timeout |
| `NOWAIT` | Fail immediately if the lock can't be acquired |
| `SKIP LOCKED` | Skip rows currently locked by other transactions — return only what can be locked. Implicit `NOWAIT`. **InnoDB only**; silently ignored on other engines |

`FOR UPDATE` acquires write locks; `LOCK IN SHARE MODE` acquires read locks. The standard SQL synonym `FOR SHARE` is also accepted.

Worker-queue idiom (the canonical `SKIP LOCKED` use case):

```sql
START TRANSACTION;
SELECT id, payload FROM jobs
  WHERE status = 'pending'
  ORDER BY priority, id
  LIMIT 1
  FOR UPDATE SKIP LOCKED;
-- ... process the job, then UPDATE its status ...
COMMIT;
```

## Temporal Queries — `FOR SYSTEM_TIME`

Available on tables created `WITH SYSTEM VERSIONING`:

```sql
SELECT * FROM t FOR SYSTEM_TIME AS OF TIMESTAMP '2026-01-01 00:00:00';
SELECT * FROM t FOR SYSTEM_TIME BETWEEN ts1 AND ts2;
SELECT * FROM t FOR SYSTEM_TIME FROM ts1 TO ts2;
SELECT * FROM t FOR SYSTEM_TIME ALL;
```

The clause goes immediately after the table name (before any alias). The system variable `system_versioning_asof` applies a default `FOR SYSTEM_TIME AS OF` to every query in the session.

Full versioning model, transaction-precise vs. timestamp-precise variants, query-time-vs-transaction-time, etc.: see the **`mariadb-system-versioned-tables`** skill.

## `INTO OUTFILE`, `INTO DUMPFILE`, `INTO @var`

```sql
SELECT … INTO OUTFILE 'file_name'
    [CHARACTER SET charset_name]
    [{FIELDS | COLUMNS} [TERMINATED BY 's'] [[OPTIONALLY] ENCLOSED BY 'c'] [ESCAPED BY 'c']]
    [LINES [STARTING BY 's'] [TERMINATED BY 's']];

SELECT … INTO DUMPFILE 'file_name';

SELECT col1, col2 INTO @var1, @var2 FROM t WHERE …;
```

| Form | What it does |
|---|---|
| `INTO OUTFILE` | Writes the resultset as text, one row per line, with configurable field/line separators. Inverse of `LOAD DATA INFILE`. Defaults: tab-separated fields, newline-terminated lines |
| `INTO DUMPFILE` | Writes a **single row** (must be one) as raw bytes — no separators, no escaping. Use for `BLOB` extraction (images, etc.) |
| `INTO @var, …` | Assigns the row's column values to user variables. The query must return exactly one row |

Common constraints (apply to both `OUTFILE` and `DUMPFILE`):

- **The file must not exist.** No overwrite, ever — delete or rotate beforehand.
- The connecting user needs the **`FILE`** global privilege.
- The path is constrained by `secure_file_priv` — if it's set (it usually is), files can only be written under that directory. `secure_file_priv = NULL` disables file I/O entirely.
- The file path is a **string literal**, not a variable. Workaround: build the statement dynamically and `PREPARE`/`EXECUTE` it.

ANSI placement of `INTO OUTFILE` (between the column list and `FROM`) is supported for simple `SELECT`s only. For a `UNION` or set operation, place `INTO OUTFILE` on a wrapping `SELECT * FROM ( … )`:

```sql
SELECT * INTO OUTFILE '/path/out.tsv'
FROM (SELECT * FROM t1 UNION SELECT * FROM t2);
```

## `WITH ROLLUP`

```sql
SELECT country, year, SUM(sales) FROM sales
  GROUP BY country, year WITH ROLLUP;
```

Adds super-aggregate rows: one per group prefix, then a grand total. The super-aggregated columns appear as `NULL` in the extra rows.

Constraints and traps:

- **Cannot be combined with `ORDER BY`.** Use `ASC` / `DESC` on the `GROUP BY` columns to control ordering; super-aggregate rows always come last regardless.
- **`LIMIT` applies *after* rollup rows are added** — so `LIMIT 4` on a rollup result may cut off the grand-total row.
- **`NULL` ambiguity**: super-aggregate rows have `NULL` in grouped columns. If your data also contains genuine `NULL`s in those columns, the result is ambiguous; use `GROUPING()` (where available) or an explicit sentinel during display.

## Other MariaDB-specific Bits

| Clause | Notes |
|---|---|
| `PARTITION (p1, p2, …)` after a table name | Limit scan to specified partitions; combines with `WHERE` |
| `FROM DUAL` | Optional placeholder when no `FROM` clause is needed: `SELECT 1 + 1 FROM DUAL;` |
| `NEXT VALUE FOR seq_name` | Get the next sequence value in a `SELECT` (see CREATE SEQUENCE) |
| `JSON_TABLE(json, '$[*]' COLUMNS (…))` in `FROM` | Treat a JSON document as a derived table |
| `INTERSECT`, `EXCEPT` | Full standard set operators; not just `UNION` |
| `VALUES (…), (…), …` standalone | Can be used in place of `SELECT` in many contexts: `VALUES (1, 'a'), (2, 'b')` |
| Recursive CTEs (`WITH RECURSIVE x AS (…)`) | Full standard support |

## See Also

- **`mariadb-system-versioned-tables`** — full `FOR SYSTEM_TIME` semantics, transaction-precise history, versioning-aware partitioning
- **`mariadb-create-table`** / **`mariadb-alter-table`** — shared column, index, and table-option surface
- Canonical references:
  - `server/reference/sql-statements/data-manipulation/selecting-data/select.md` (~220 lines)
  - `…/select-into-outfile.md` (~80 lines)
  - `…/select-into-dumpfile.md` (~60 lines)
  - `…/select-offset-fetch.md` (~120 lines)
  - `…/select-with-rollup.md` (~155 lines)

  Consult only for edge cases not covered here.
