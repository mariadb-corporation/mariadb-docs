---
name: mariadb-explain
description: "MariaDB-specific behavior of EXPLAIN and its relatives (ANALYZE, EXPLAIN FORMAT=JSON, SHOW EXPLAIN/ANALYZE FOR) — MariaDB has no `EXPLAIN ANALYZE`; it uses a standalone `ANALYZE <statement>` that actually executes the query (and, for UPDATE/DELETE/INSERT, actually writes); plain EXPLAIN never runs anything; only FORMAT=JSON/TRADITIONAL exist (no TREE); and EXPLAIN covers INSERT/REPLACE directly. Use when writing, generating, or reviewing query-plan/EXPLAIN statements that target MariaDB."
---

# EXPLAIN in MariaDB

*Last updated: 2026-07-20*

This skill covers the delta between the `EXPLAIN`/`ANALYZE`/query-plan family most LLMs default to and MariaDB's actual grammar and runtime behavior, verified against `sql/sql_yacc.yy`, `sql/sql_parse.cc`, `sql/sql_explain.cc`, `sql/sql_update.cc`, and `sql/sql_delete.cc` in the MariaDB server source.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `EXPLAIN ANALYZE SELECT …` | Drop the `EXPLAIN` keyword: **`ANALYZE SELECT …`**. `EXPLAIN ANALYZE` is not a valid production in MariaDB's grammar — `EXPLAIN` (lexed as the same token as `DESCRIBE`) only combines with `EXTENDED`, `PARTITIONS`, `FORMAT=JSON`, or `FOR CONNECTION`, never with `ANALYZE`. The syntax was replaced by the standalone `ANALYZE` statement back in MariaDB 10.1.0 |
| `EXPLAIN SELECT …` to see "real" row counts | Plain `EXPLAIN` **never executes the query** — it only optimizes and reports estimates. To get real, executed-based numbers (`r_rows`, `r_filtered`), run **`ANALYZE SELECT …`** instead, which actually runs the statement (and discards the result set) |
| Assuming `EXPLAIN` always shows a filtering percentage column | Plain tabular `EXPLAIN` omits the `filtered` column entirely. You need **`EXPLAIN EXTENDED`** (or `ANALYZE`, which always includes it) to get `filtered` — MariaDB never made `EXTENDED` the silent default |
| `EXPLAIN` only for `SELECT` | MariaDB's `EXPLAIN`/`ANALYZE` grammar directly accepts `SELECT`, `INSERT`, `REPLACE`, `UPDATE`, and `DELETE` |
| `ANALYZE UPDATE …` / `ANALYZE DELETE …` treated as a dry-run / read-only inspection | These statements **actually perform the update/delete** — `ANALYZE` only skips the write path when the plan proves the `WHERE` clause impossible; otherwise the modification commits normally, annotated with `r_rows`/`r_filtered`. Only `EXPLAIN` (not `ANALYZE`) is a true no-op for DML |
| `EXPLAIN FORMAT=TREE` | MariaDB supports exactly two `FORMAT` values: **`JSON`** and **`TRADITIONAL`** (the default tabular form, explicitly nameable). There is no `TREE` format — using it raises `ER_UNKNOWN_EXPLAIN_FORMAT` |
| `EXPLAIN tbl_name` treated as a query-plan request | `EXPLAIN tbl_name` is a synonym for **`DESCRIBE tbl_name`** / `SHOW COLUMNS FROM tbl_name` — it returns the column list, not an execution plan. Only `EXPLAIN` in front of `SELECT`/`INSERT`/`REPLACE`/`UPDATE`/`DELETE` produces a plan |
| Confusing `ANALYZE TABLE tbl_name` with query-profiling `ANALYZE` | `ANALYZE TABLE tbl_name` is a completely different statement (recomputes engine index/table statistics for the optimizer). Query profiling is the MariaDB-specific extension `ANALYZE <explainable_statement>` (no `TABLE` keyword, no table name — a `SELECT`/`INSERT`/`REPLACE`/`UPDATE`/`DELETE` follows instead) — same leading keyword, disambiguated by what follows it |
| Polling / re-running a slow query to "see" its plan while it's still running | Use **`SHOW EXPLAIN FOR <connection_id>`** or **`SHOW ANALYZE FOR <connection_id>`** to inspect a query that's still executing in another connection, found via `SHOW PROCESSLIST` — no need to wait for it to finish or kill it |

## The Statement Family — Estimate vs. Actual

MariaDB's plan-inspection surface has three tiers, all sharing the same tabular/JSON output shape:

| Statement | Executes the query? | Extra columns | Notes |
|---|---|---|---|
| `EXPLAIN [EXTENDED\|PARTITIONS\|FORMAT=JSON] {SELECT\|INSERT\|REPLACE\|UPDATE\|DELETE}` | **No** — optimizes only, never runs | `filtered` (only with `EXTENDED`) | Pure estimate; safe against DML |
| `ANALYZE [FORMAT=JSON] explainable_statement` | **Yes** — runs it for real | `r_rows`, `filtered`, `r_filtered` (tabular); much more in JSON | For `SELECT`, the result set is executed then discarded. For `INSERT`/`UPDATE`/`REPLACE`/`DELETE`, the write actually happens |
| `SHOW EXPLAIN\|ANALYZE [FORMAT=JSON] FOR <connection_id>` | Inspects a query **already running** in another connection | Same columns as above, snapshotted mid-execution | MariaDB-specific; no standalone `EXPLAIN ANALYZE` needed since you inspect the live connection instead |

`EXPLAIN ANALYZE` as its own two-keyword statement is retired: `EXPLAIN` and `ANALYZE` head two independent, non-combinable grammar productions. An agent asked to "profile this query" that reflexively emits `EXPLAIN ANALYZE …` will get a syntax error, not a plan. The correct rewrite is dropping the `EXPLAIN` and keeping only `ANALYZE`.

## `FORMAT=JSON`

```sql
EXPLAIN FORMAT=JSON SELECT * FROM t1 WHERE col1 = 1;
ANALYZE FORMAT=JSON SELECT * FROM t1 WHERE col1 = 1;
```

Both return a single row with a single column holding a JSON document describing the query block, tables, access types, and (for `ANALYZE FORMAT=JSON`) execution statistics. MariaDB's JSON shape is its own design — not a port of any other engine's `FORMAT=JSON`, and not interchangeable with it field-for-field.

`ANALYZE FORMAT=JSON` adds, beyond the tabular `r_rows`/`filtered`/`r_filtered`:

- **`r_loops`** — how many times a plan node executed.
- **`r_total_time_ms`** — cumulative time spent in a node, including its subnodes. For `UPDATE`/`DELETE`, this includes making the row changes but excludes commit time.
- **`r_buffer_size`** — size of any buffer the node used (e.g., join buffer).
- **`r_engine_stats`** (InnoDB tables) — page-access counters; only non-zero members are printed.
- *(since 11.5)* **`r_index_rows`** and **`r_icp_filtered`** — separate the count of index tuples enumerated (before any check) from post-Index-Condition-Pushdown selectivity; and **`r_total_filtered`** — combined selectivity across ICP, Rowid Filtering, and the attached condition.

## `EXPLAIN EXTENDED` + `SHOW WARNINGS`

```sql
EXPLAIN EXTENDED SELECT * FROM employees WHERE last_name = 'Marx';
SHOW WARNINGS;
```

`EXTENDED` is a live, non-deprecated modifier — it is not folded into the default tabular output. It does two things:

1. Adds the `filtered` column (percentage estimate of rows surviving the attached condition) to the tabular result.
2. Emits exactly one `Note`-level warning containing the query as the optimizer rewrote it (constant propagation, redundant-condition removal, etc.) — retrievable with a subsequent `SHOW WARNINGS`.

Both behaviors fire only for the tabular path; `EXTENDED` and `FORMAT=JSON` are alternatives, not composable — the JSON output already carries the `filtered` and `attached_condition` fields unconditionally. `ANALYZE` always includes the `filtered` column (and `r_filtered`) with or without `EXTENDED`.

## `SHOW EXPLAIN` / `SHOW ANALYZE` FOR `<connection_id>`

```sql
SHOW PROCESSLIST;                      -- find the connection id
SHOW EXPLAIN FOR 7;                    -- what is connection 7 doing?
SHOW ANALYZE FOR 7;                    -- ...with runtime stats so far
SHOW EXPLAIN FORMAT=JSON FOR 7;        -- same, as JSON     (since 10.9)
SHOW ANALYZE FORMAT=JSON FOR 7;        -- same, as JSON     (since 10.9)
EXPLAIN FOR CONNECTION 7;              -- alias for SHOW EXPLAIN FOR 7 (since 10.9)
```

MariaDB-specific: there is no need to `KILL` and rerun a long query, or wait for it to finish, to see what it's doing. `SHOW EXPLAIN` snapshots the query plan of a statement actively running in another session; `SHOW ANALYZE` additionally reports the runtime statistics accumulated *so far*. Both require the same privilege as `SHOW PROCESSLIST`, and both error with `ER_TARGET_NOT_EXPLAINABLE` (*"Target is not running an EXPLAINable command"*, error 1932) if the target connection isn't currently mid-plan (e.g., still opening tables) or isn't running an explainable statement at all.

`SHOW ANALYZE` picks up detailed timing (`r_..._time_ms` fields) only if the target connection is itself running `ANALYZE`; a plain `SELECT` being inspected this way reports row counts but not timings, since timing collection is opt-in via `ANALYZE`.

## `EXPLAIN` for `INSERT` / `UPDATE` / `DELETE` / `REPLACE`

```sql
EXPLAIN UPDATE t1 SET c1 = c1 + 1 WHERE c2 > 100;
EXPLAIN DELETE FROM t1 WHERE c2 > 100;
EXPLAIN INSERT INTO t1 SELECT * FROM t2 WHERE c2 > 100;
ANALYZE DELETE FROM t1 WHERE c2 > 100;   -- actually deletes
```

All four DML forms are directly explainable. As with `SELECT`, `EXPLAIN` on any of these is a pure dry run: the server derives and prints the plan, then stops before touching data. `ANALYZE` on any of these executes for real; the only exception the optimizer takes is bailing out early (before running the write) when it can already prove the `WHERE` clause matches nothing.

## `EXPLAIN tbl_name` — the `DESCRIBE` Synonym

```sql
EXPLAIN employees;      -- same as: DESCRIBE employees;  /  SHOW COLUMNS FROM employees;
```

This form has nothing to do with query plans. `EXPLAIN`/`DESCRIBE`/`DESC` are three spellings of the same keyword at the lexer level; followed directly by a table name (no `SELECT`/`UPDATE`/etc.), it lists that table's columns, types, keys, and defaults — identical to `SHOW COLUMNS FROM`.

## Examples

```sql
-- Estimate only: no usable index, so it's a full table scan
EXPLAIN SELECT * FROM employees_example WHERE home_phone = '326-555-3492';
+------+-------------+-------------------+------+---------------+------+---------+------+------+-------------+
| id   | select_type | table             | type | possible_keys | key  | key_len | ref  | rows | Extra       |
+------+-------------+-------------------+------+---------------+------+---------+------+------+-------------+
|    1 | SIMPLE      | employees_example | ALL  | NULL          | NULL | NULL    | NULL |    6 | Using where |
+------+-------------+-------------------+------+---------------+------+---------+------+------+-------------+

-- Estimate + actual: ANALYZE runs the query and adds r_rows / r_filtered
ANALYZE SELECT * FROM tbl1 WHERE key1 BETWEEN 10 AND 200 AND col1 LIKE 'foo%';
           id: 1
  select_type: SIMPLE
        table: tbl1
         type: range
possible_keys: key1
          key: key1
      key_len: 5
          ref: NULL
         rows: 181
       r_rows: 181
     filtered: 100.00
   r_filtered: 10.50
        Extra: Using index condition; Using where

-- Inspecting a query already running in another session (no need to wait for it)
SHOW PROCESSLIST;
SHOW EXPLAIN FOR 1;
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
| id   | select_type | table | type  | possible_keys | key  | key_len | ref  | rows    | Extra       |
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
|    1 | SIMPLE      | tbl   | index | NULL          | a    | 5       | NULL | 1000107 | Using index |
+------+-------------+-------+-------+---------------+------+---------+------+---------+-------------+
```

## See Also

- **`mariadb-select`** — the queries whose plans EXPLAIN describes.
- **`mariadb-show`** — `SHOW EXPLAIN`/`SHOW ANALYZE FOR`, and other introspection statements.
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain-format-json>
