---
name: mariadb-drop-table
description: "MariaDB-specific syntax and behavior for DROP TABLE — RESTRICT/CASCADE being no-ops, the DROP TEMPORARY TABLE guard against dropping a same-named base table, partial drops in a multi-table statement, IF EXISTS warning behavior, failure when a table is referenced by a foreign key, DROP TABLE on a view, automatic trigger removal, implicit-commit (and the DROP TEMPORARY exception), WAIT/NOWAIT, and CREATE OR REPLACE TABLE as the atomic replace. Use when writing, generating, or reviewing DROP TABLE statements that target MariaDB."
---

# DROP TABLE in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL `DROP TABLE` and MariaDB's**. It assumes the agent knows the basic `DROP TABLE t;` form. Everything below documents MariaDB-specific behavior and the traps that bite generated SQL.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Adds `CASCADE` expecting dependent objects (FK children, etc.) to be dropped too | `RESTRICT` and `CASCADE` are **parsed but do nothing** on `DROP TABLE` — accepted only for portability. Nothing cascades. To remove a referencing foreign key, drop or alter that table explicitly |
| Bare `DROP TABLE x` to discard a temporary table | `DROP TEMPORARY TABLE x` — `TEMPORARY` restricts the drop to temporary tables, so a stray base table of the same name can never be dropped by accident. The safer form whenever you mean a temp table |
| Assumes one missing table aborts `DROP TABLE a, b, c` and leaves the rest | **Partial drop**: the tables that exist are still dropped; the missing ones are collected and reported together at the end. Without `IF EXISTS` you get both the drops *and* an error |
| Expects `DROP TABLE IF EXISTS missing` to still error | `IF EXISTS` turns the unknown-table error into a **note-level warning** (visible via `SHOW WARNINGS`) — not an error, not silent |
| `DROP TABLE v` where `v` is a view | Errors (`ER_IT_IS_A_VIEW`) — use `DROP VIEW v`. (See `mariadb-create-view`) |
| Drops a table that another table's foreign key references | Blocked (`ER_ROW_IS_REFERENCED`). Drop the referencing FK first, or `SET foreign_key_checks = 0` for the session to bypass the check |
| Wraps `DROP TABLE` in a transaction expecting to roll it back | DDL does an **implicit commit** — it can't be rolled back. The one exception: `DROP TEMPORARY TABLE` does *not* implicitly commit the surrounding transaction |
| Drops a table, then separately hunts down its triggers | `DROP TABLE` removes the table's triggers automatically — no separate `DROP TRIGGER` needed |
| `DROP TABLE x; CREATE TABLE x …` to replace a table definition | `CREATE OR REPLACE TABLE x …` — atomic, with no window where the table is missing. See `mariadb-create-table` |
| Uses `DROP TABLE` to clear rows or reset `AUTO_INCREMENT` | That destroys the table. To empty it, use `TRUNCATE TABLE` (resets `AUTO_INCREMENT`, implicit commit) or `DELETE FROM` (transactional). See `mariadb-delete` |

## Syntax

```sql
DROP [TEMPORARY] TABLE [IF EXISTS]
    tbl_name [, tbl_name] …
    [WAIT n | NOWAIT]
    [RESTRICT | CASCADE];
```

Clause order is load-bearing: `WAIT`/`NOWAIT` comes **after** the table list and **before** the (no-op) `RESTRICT`/`CASCADE`. `TABLE` and `TABLES` are interchangeable.

```sql
-- Missing tables tolerated as warnings:
DROP TABLE IF EXISTS employees, customers;

-- Guard against dropping a same-named base table:
DROP TEMPORARY TABLE IF EXISTS scratch;

-- Qualified names can span databases in one statement:
DROP TABLE app.sessions, archive.sessions;

-- Bound the metadata-lock wait instead of blocking:
DROP TABLE big_table WAIT 5;     -- or NOWAIT to fail immediately
```

`WAIT n` / `NOWAIT` sets the lock-wait timeout for the statement — useful when a long-held metadata lock would otherwise make the `DROP` block. A single-table `DROP TABLE` is atomic (crash-safe) on InnoDB/Aria/MyISAM; in a multi-table drop each individual table drop is atomic, but the statement as a whole is **not** all-or-nothing.

## See Also

- **`mariadb-create-table`** — `CREATE OR REPLACE TABLE` (the atomic replace) and the shared implicit-commit / atomic-DDL behavior
- **`mariadb-create-view`** — `DROP VIEW` for views (`DROP TABLE` won't drop them)
- **`mariadb-delete`** — when you want to *empty* a table rather than drop it: `TRUNCATE TABLE` vs `DELETE FROM`
- Canonical reference on `mariadb.com/docs`, consult only for edge cases not covered here: <https://mariadb.com/docs/server/reference/sql-statements/data-definition/drop/drop-table>
