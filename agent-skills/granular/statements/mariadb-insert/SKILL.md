---
name: mariadb-insert
description: "MariaDB-specific syntax and behavior for INSERT — RETURNING to get inserted rows in one round trip, INSERT … ON DUPLICATE KEY UPDATE with VALUE()/VALUES(), INSERT IGNORE warning and error-coercion behavior, INSERT … SELECT, the SET form, PARTITION targeting, multi-row VALUES, priority/DELAYED modifiers and their engine limits, and LAST_INSERT_ID() semantics after multi-row inserts. Use when writing, generating, or reviewing INSERT statements that target MariaDB, or when an upsert is needed."
---

# INSERT in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL `INSERT` and MariaDB's**. It assumes the agent already knows the standard forms (`INSERT INTO t (cols) VALUES (…)` and `INSERT INTO t SELECT …`). Everything below documents MariaDB-specific syntax, duplicate-key handling, the `RETURNING` extension, and the most common LLM traps.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `INSERT …` then a separate `SELECT` (or `LAST_INSERT_ID()` gymnastics) to see what was inserted | `INSERT INTO t (…) VALUES (…) RETURNING id, created_at, …` returns the inserted rows in one statement. Supports expressions, stored functions, and single-row subqueries (no aggregates) |
| To do an "upsert," reach for `REPLACE` | Use `INSERT … ON DUPLICATE KEY UPDATE` — it updates the existing row in place, preserving unmentioned columns and not churning `AUTO_INCREMENT` or firing `DELETE` triggers. `REPLACE` deletes and re-inserts (see `mariadb-replace`) |
| Inside `ON DUPLICATE KEY UPDATE`, only knows `VALUES(col)` to reference the would-be-inserted value | Both work; `VALUE(col)` is the current canonical name, `VALUES(col)` the older alias. Note `VALUES(col)`/`VALUE(col)` is **only** valid inside `ON DUPLICATE KEY UPDATE` — a syntax error elsewhere |
| Expects `INSERT IGNORE` to skip duplicates **silently** | Each skipped row raises a **warning** (e.g. code 1062) — check `SHOW WARNINGS`. The fully-silent legacy behavior is gated behind `OLD_MODE=NO_DUP_KEY_WARNINGS_WITH_IGNORE`, which is deprecated since 11.3 |
| Thinks `INSERT IGNORE` only swallows duplicate-key errors | It downgrades **all** errors to warnings — a missing `NOT NULL` default (1364), out-of-range/invalid values (coerced to the closest valid value), etc. Easy to mask real data problems with it |
| Combines `INSERT IGNORE … ON DUPLICATE KEY UPDATE` (or `DELAYED … ON DUPLICATE KEY UPDATE`) expecting both to apply | `IGNORE` and `DELAYED` are **silently ignored** when `ON DUPLICATE KEY UPDATE` is present |
| Reads "2 rows affected" from `ON DUPLICATE KEY UPDATE` as 2 rows inserted | The count is **1 per row inserted, 2 per existing row updated** (0 if an update changed nothing). So a batch reporting "2" inserted one of nothing — it updated one |
| Expects `LAST_INSERT_ID()` after a multi-row INSERT to give the **last** generated id | It returns the `AUTO_INCREMENT` value of the **first** successfully inserted row. Derive the others by offset, or use `RETURNING id` |
| Uses `INSERT DELAYED` as fire-and-forget on any table | `DELAYED` is honored only on table-lock engines (MyISAM, Aria, MEMORY, ARCHIVE, BLACKHOLE) and errors (1616) elsewhere; it's also a no-op on replicas, in stored programs, and on partitioned tables. Treat it as legacy — prefer a normal INSERT (and `LAST_INSERT_ID()` isn't available after a `DELAYED` insert) |
| `INSERT … SELECT` reading from the same table it inserts into | Not allowed — the `SELECT` source can't be the `INTO` target. Stage through a temporary table |
| Adds `LOW_PRIORITY` / `HIGH_PRIORITY` to speed up an InnoDB insert | These only affect table-lock engines; no effect on InnoDB. `HIGH_PRIORITY` isn't even valid in the `INSERT … SELECT` form |
| Assumes partition targeting isn't available | `INSERT INTO t PARTITION (p0, p1) VALUES (…)` restricts the insert to named partitions (errors if a row doesn't belong) |

## `RETURNING`

Return data from the rows just inserted, in a single statement:

```sql
INSERT INTO orders (cust_id, total) VALUES (42, 99.50), (43, 12.00)
  RETURNING id, cust_id, total * 1.2 AS gross;
```

Allowed: column references, expressions, stored functions, single-row/single-column subqueries, and prepared statements. **Not** allowed: aggregate functions. For a plain count, use `ROW_COUNT()`. `RETURNING` is a MariaDB extension — not in standard SQL.

## `ON DUPLICATE KEY UPDATE` (the real upsert)

```sql
INSERT INTO inventory (sku, qty) VALUES ('A1', 5), ('B2', 3)
  ON DUPLICATE KEY UPDATE qty = qty + VALUE(qty);
```

- Fires when an inserted row would collide with a `PRIMARY KEY` or `UNIQUE` index. The `UPDATE` clause runs against the existing row; unmentioned columns are left untouched.
- `VALUE(col)` (alias `VALUES(col)`) inside the `UPDATE` clause = the value that *would have been* inserted for that column. Bare column names refer to the existing row.
- If a row matches more than one unique index, only the **first** matched index's row is updated — ambiguous on multi-unique tables; design around it.

This is almost always what's wanted over `REPLACE`. See `mariadb-replace` for the contrast.

## `INSERT IGNORE`

```sql
INSERT IGNORE INTO t (id, name) VALUES (1, 'a'), (1, 'dup'), (2, 'b');
SHOW WARNINGS;   -- the skipped duplicate surfaces here
```

Downgrades errors to warnings rather than aborting the statement. Useful for best-effort bulk loads, but it masks duplicate-key collisions, missing defaults, and value coercion alike — don't use it to paper over a schema mismatch.

## Forms and modifiers

```sql
-- SET form (one row, named assignments):
INSERT INTO person SET first_name = 'John', last_name = 'Doe';

-- Multi-row VALUES (VALUES and VALUE are interchangeable):
INSERT INTO t VALUES (1, 'a'), (2, 'b'), (3, 'c');

-- INSERT ... SELECT (source table ≠ target table):
INSERT INTO archive (id, payload) SELECT id, payload FROM live WHERE ts < '2025-01-01';

-- Partition targeting:
INSERT INTO t PARTITION (p0, p1) VALUES (…);
```

Priority/queue modifiers: `[LOW_PRIORITY | DELAYED | HIGH_PRIORITY]` on the `VALUES`/`SET` forms; the `SELECT` form takes only `[LOW_PRIORITY | HIGH_PRIORITY]` (no `DELAYED`). All are table-lock-engine concerns — typically irrelevant on InnoDB.

## See Also

- **`mariadb-replace`** — `REPLACE` (delete-then-insert) and exactly when `ON DUPLICATE KEY UPDATE` is the better upsert
- **`mariadb-select`** — the `SELECT` source for `INSERT … SELECT`, plus `PARTITION` pruning and priority semantics
- **`mariadb-create-table`** / **`mariadb-alter-table`** — `AUTO_INCREMENT`, `DEFAULT` expressions, and `UNIQUE`/`PRIMARY KEY` definitions that drive `ON DUPLICATE KEY UPDATE` and `IGNORE` behavior
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert-ignore>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert-select>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert-default-duplicate-values>
