---
name: mariadb-create-sequence
description: "MariaDB-specific syntax and behavior for CREATE SEQUENCE — sequences are ordinary tables (any transactional engine, default BIGINT SIGNED) wrapped with sequence semantics, support atomic CREATE OR REPLACE / IF NOT EXISTS, default to CACHE 1000, expose ANSI (NEXT VALUE FOR), PostgreSQL (NEXTVAL()), and Oracle-mode (seq.nextval) access forms, special-case INCREMENT BY 0 for multi-master/Galera replication, require row-based binlogging, and (since 11.5) truncate rather than reject out-of-range MINVALUE/MAXVALUE/START literals. Use when writing, generating, or reviewing CREATE SEQUENCE statements that target MariaDB."
---

# CREATE SEQUENCE in MariaDB

*Last updated: 2026-07-20*

This covers the delta between standard-SQL/Oracle-style sequence objects and MariaDB's `CREATE SEQUENCE`, which is implemented as a specially wrapped table rather than a standalone catalog object.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `DROP SEQUENCE IF EXISTS s; CREATE SEQUENCE s ...` to redefine a sequence | `CREATE OR REPLACE SEQUENCE s ...` — atomic, and `CREATE SEQUENCE ... IF NOT EXISTS` also exists for idempotent creation |
| Assuming a sequence is stored by a storage engine literally named `SEQUENCE` | A sequence created by `CREATE SEQUENCE` is an ordinary table on whatever engine you name (InnoDB/Aria/MyISAM — anything supporting tables without rollback), wrapped by an internal handler. The storage engine literally called `SEQUENCE` is an unrelated feature: a virtual, on-the-fly row generator behind `seq_1_to_N`-style table names |
| `NEXTVAL()` / `CURRVAL()` as the only forms | Three families are supported: ANSI `NEXT VALUE FOR seq` / `PREVIOUS VALUE FOR seq`, PostgreSQL-style `NEXTVAL(seq)` / `LASTVAL(seq)`, and Oracle-mode (`SQL_MODE=ORACLE`) `seq.nextval` / `seq.currval` |
| Assuming no caching, or that caching is opt-in | `CACHE` defaults to **1000**, not 0. Values are reserved in blocks; `FLUSH TABLES`, a server restart, or dropping the connection discards the unused part of the cache (expect gaps). Dropping cache to `1` can roughly halve insert throughput and inflate binlog size several-fold |
| Rejecting `INCREMENT BY 0` as meaningless | `INCREMENT BY 0` is special-cased: the sequence instead uses the session's `auto_increment_increment` / `auto_increment_offset`, which is MariaDB's documented way to run one sequence definition safely across multi-master or Galera nodes |
| Assuming `SELECT NEXT VALUE FOR seq` is a safe read under any binlog format | It mutates the sequence's backing row and is always row-logged; under `BINLOG_FORMAT=STATEMENT` it raises an error (`impossible to write to binary log...limited to row-based logging`). Use `ROW` or `MIXED` |
| `ALTER SEQUENCE s AS BIGINT INCREMENT BY 5` in one statement | The parser rejects combining `AS <type>` with any other clause in the same `ALTER SEQUENCE` — issue the type change alone. Internally it also runs as a full `ALTER TABLE` column-change, unlike every other `ALTER SEQUENCE` clause, which is a fast, single-row metadata update |
| Expecting `CREATE SEQUENCE s MAXVALUE=99999999999999999999999999` to error immediately | *(since 11.5)* Oracle-style literals wider than the sequence's `AS` type are accepted by the parser and silently truncated to the type's bound, with a `Note`-level warning (`Truncated incorrect INTEGER value`) — not a hard error |
| `UPDATE`/`DELETE` against a sequence's backing table to change its state | Not allowed on sequence tables. Use `ALTER SEQUENCE`, `SETVAL()`, or a full-row `INSERT` (the one legacy exception, kept for `mariadb-dump` compatibility) |

## Syntax

```sql
CREATE [OR REPLACE] [TEMPORARY] SEQUENCE [IF NOT EXISTS] sequence_name
    [AS {TINYINT | SMALLINT | MEDIUMINT | INT | INTEGER | BIGINT} [SIGNED | UNSIGNED]]
    [INCREMENT [BY | =] number]
    [MINVALUE [=] number | NO MINVALUE | NOMINVALUE]
    [MAXVALUE [=] number | NO MAXVALUE | NOMAXVALUE]
    [START [WITH | =] number]
    [CACHE [=] number | NOCACHE]
    [CYCLE | NOCYCLE]
    [table_options]
```

- Clauses may be given in any order.
- `table_options` accepts any normal `CREATE TABLE` option — most commonly `ENGINE = ...` and `COMMENT = '...'`. If `ENGINE` is omitted, the server's default storage engine is used, same as for a normal `CREATE TABLE`.
- `NOMINVALUE` / `NOMAXVALUE` exist alongside the ANSI `NO MINVALUE` / `NO MAXVALUE` forms specifically for Oracle-syntax compatibility.
- `AS <int type>` *(since 11.5)* sets the underlying integer storage type (any of `TINYINT`/`SMALLINT`/`MEDIUMINT`/`INT`/`INTEGER`/`BIGINT`, optionally `SIGNED`/`UNSIGNED`; `ZEROFILL` is rejected). Default is `BIGINT SIGNED`. Using `BIGINT UNSIGNED` extends the usable range up to `18446744073709551614`.
- `CREATE SEQUENCE` requires the `CREATE` privilege on the target table/schema (it shares the exact privilege path used by `CREATE TABLE`); `CREATE OR REPLACE SEQUENCE` on a non-temporary sequence additionally requires `DROP`.
- `CREATE SEQUENCE` is atomic DDL (as is all DDL since 10.6.1) — no partial-create state survives a crash.

### Defaults (verified against source)

| Clause | Default | Notes |
|---|---|---|
| `AS` type | `BIGINT SIGNED` | |
| `INCREMENT` | `1` | May be negative. `0` defers to `auto_increment_increment` at first use (see gotcha table) |
| `MINVALUE` | `1` if increment ≥ 0 and signed; the type's minimum + 1 if increment < 0 or unsigned. For default `BIGINT SIGNED` with a negative increment: `-9223372036854775807` | |
| `MAXVALUE` | The type's maximum − 1 if increment ≥ 0 or unsigned; `-1` if increment < 0 (signed). For default `BIGINT SIGNED`: `9223372036854775806` | Sequences can never generate the true 64-bit min/max because of this ±1 reservation |
| `START` | `MINVALUE` if increment ≥ 0, `MAXVALUE` if increment < 0 | |
| `CACHE` | `1000` | `0` means "no cache" (every value written immediately) |
| `CYCLE` | `NOCYCLE` (off) | |

### Constraints on Create/Alter Arguments

The following must hold, or the statement fails with `ER_SEQUENCE_INVALID_DATA` (error **4085**, `Sequence 'db.name' has out of range value for options`):

- `MAXVALUE >= START >= MINVALUE`
- `MAXVALUE > MINVALUE`
- `MAXVALUE` / `MINVALUE` are truncated (with a warning), not rejected, if they exceed the `AS` type's bounds *(since 11.5)*.

## Accessing and Modifying Values

| Form | Standard | Notes |
|---|---|---|
| `NEXT VALUE FOR seq` | ANSI SQL | Also usable in a column `DEFAULT` |
| `NEXTVAL(seq)` | PostgreSQL | |
| `seq.nextval` | Oracle | Requires `SQL_MODE=ORACLE` |
| `PREVIOUS VALUE FOR seq` | ANSI SQL | Last value generated *by the current connection* — not a global "last value" |
| `LASTVAL(seq)` | PostgreSQL | |
| `seq.currval` | Oracle | Requires `SQL_MODE=ORACLE` |
| `SETVAL(seq, next_value [, is_used [, round]])` | PostgreSQL-compatible, extended with `round` | Only moves the sequence forward — attempting to set a lower `(round, next_value)` returns `NULL` and has no effect. Requires `INSERT` privilege. Used internally to propagate sequence state to replicas |

`ALTER SEQUENCE ... RESTART [WITH n]` sets the next value directly (equivalent to `SETVAL(seq, n, 0)`); with no value it resets to the recorded `START` value. It takes a brief full-table lock, unlike `SETVAL()`, which is non-blocking.

## Storage Engine and Table Structure

- A sequence is a real table (visible in `SHOW TABLES`), created without rollback support even on transactional engines (InnoDB, Aria, MyISAM all qualify), then wrapped by an internal handler that intercepts reads/writes to implement sequence semantics.
- The single row has 8 fixed columns: `next_not_cached_value`, `minimum_value`, `maximum_value`, `start_value`, `increment`, `cache_size`, `cycle_option`, `cycle_count`. `SHOW CREATE TABLE seq_name` shows this structure; `SHOW CREATE SEQUENCE seq_name` shows the equivalent `CREATE SEQUENCE` form with all defaults filled in.
- Because sequences share the table namespace, `DROP TABLE`, `RENAME TABLE`, `ALTER TABLE ... RENAME`, and `SHOW CREATE TABLE` all work on a sequence; `LOCK TABLES` also affects it (unlike Oracle, where `LOCK TABLE` does not touch sequences). `CREATE TABLE ... SEQUENCE=1` is the table-option equivalent of `CREATE SEQUENCE`.
- `DROP SEQUENCE` only removes sequences — pointing it at a plain table fails (or, with `IF EXISTS`, emits a note). `DROP TABLE` removes either kind.
- Do not confuse this with the unrelated **SEQUENCE storage engine**, which powers virtual, read-only, disk-free row generators named by pattern (`seq_1_to_100`, `seq_1_to_15_step_3`, etc.) for row generation in queries — a completely different feature that happens to share the keyword.

## Replication

- `CREATE SEQUENCE` and `ALTER SEQUENCE` themselves replicate as their own DDL statement (row-based logging is explicitly disabled for the definition row they write).
- Every cache-block refill triggered by `NEXT VALUE FOR` / `NEXTVAL()`, however, is logged as a row event (`Write_rows_log_event`) regardless of the session's binlog format. Because of this, statement-based logging cannot represent it: running `SELECT NEXT VALUE FOR seq` under `BINLOG_FORMAT=STATEMENT` raises an error. Use `ROW` or `MIXED`.
- For master-master setups or Galera, set `INCREMENT=0` so the sequence defers to `auto_increment_increment` / `auto_increment_offset`, guaranteeing non-colliding values per node.
- `SETVAL()` is the mechanism used to propagate a sequence's advanced state to replicas; out-of-order delivery is safe because only the highest `(round, next_value)` pair ever takes effect.

## Errors

| Code | Name | Message (current source text) |
|---|---|---|
| 4084 | `ER_SEQUENCE_RUN_OUT` | `Sequence 'db.name' has run out` — raised once bounds are exhausted and `CYCLE` was not specified |
| 4085 | `ER_SEQUENCE_INVALID_DATA` | `Sequence 'db.name' has out of range value for options` — raised when `CREATE`/`ALTER SEQUENCE` arguments violate the ordering constraints above |

## Examples

```sql
CREATE SEQUENCE s START WITH 100 INCREMENT BY 10;
SELECT NEXTVAL(s);   -- 100
SELECT NEXTVAL(s);   -- 110

-- Idempotent redefinition, no drop/create race:
CREATE OR REPLACE SEQUENCE s START WITH 1 MAXVALUE 10 CACHE 5;

-- Multi-master / Galera friendly sequence:
CREATE SEQUENCE s_mm INCREMENT BY 0;

-- Explicit narrow type, since 11.5:
CREATE SEQUENCE s3 AS SMALLINT UNSIGNED START WITH 1;

-- Use as a DEFAULT instead of AUTO_INCREMENT:
CREATE SEQUENCE s1;
CREATE TABLE t1 (a INT PRIMARY KEY DEFAULT (NEXT VALUE FOR s1), b INT);
INSERT INTO t1 (b) VALUES (1), (2);
```

## See Also

- **`mariadb-create-table`** — the table-option surface (`ENGINE=`, atomic DDL, `CREATE OR REPLACE`) that `CREATE SEQUENCE` inherits, and the `SEQUENCE=1` table-option form
- **`mariadb-alter-table`** — for changing a sequence's engine, comment, or name (via `ALTER TABLE`, not `ALTER SEQUENCE`)
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-structure/sequences/create-sequence>
  - <https://mariadb.com/docs/server/reference/sql-structure/sequences/sequence-overview>
  - <https://mariadb.com/docs/server/reference/sql-structure/sequences/alter-sequence>
  - <https://mariadb.com/docs/server/reference/sql-structure/sequences/drop-sequence>
