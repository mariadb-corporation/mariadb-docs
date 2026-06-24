---
name: mariadb-update
description: "MariaDB-specific syntax and behavior for UPDATE — single-table vs multi-table forms and their different rules, UPDATE … ORDER BY … LIMIT, PARTITION pruning, RETURNING with OLD_VALUE() (since 13.0), left-to-right assignment evaluation and SIMULTANEOUS_ASSIGNMENT sql_mode, IGNORE / LOW_PRIORITY modifiers, rows-matched-vs-changed reporting, updating system-versioned and application-time-period (FOR PORTION OF) tables, and CTEs before UPDATE (since 12.3). Use when writing, generating, or reviewing UPDATE statements that target MariaDB."
---

# UPDATE in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL `UPDATE` and MariaDB's**. It assumes the agent already knows the standard form (`UPDATE t SET col = expr WHERE …`). Everything below documents MariaDB-specific syntax, assignment semantics, the single-table/multi-table split, and the most common LLM traps.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Assumes `UPDATE … RETURNING` is unsupported (only `INSERT`/`DELETE` return rows) | `UPDATE t SET a = a + 1 WHERE id = 5 RETURNING OLD_VALUE(a) AS before, a AS after;` — supported **since 13.0**, single-table only. `OLD_VALUE(col)` gives the pre-update value, a bare column gives the new one |
| Adds `ORDER BY` or `LIMIT` to a **multi-table** UPDATE | Not allowed. `ORDER BY` and `LIMIT` work only on the **single-table** form. Same restriction applies to `PARTITION` and `RETURNING` — all four are single-table-only |
| `UPDATE t SET col1 = col2, col2 = col1` expecting a simultaneous swap | Single-table UPDATE evaluates assignments **left-to-right**, so by the time `col2` is set, `col1` already holds the new value (no swap). For simultaneous semantics: `SET sql_mode = 'SIMULTANEOUS_ASSIGNMENT'`. Multi-table UPDATE gives **no** ordering guarantee at all |
| Sets the same column twice in one statement expecting last-write-wins | In plain mode the last assignment wins. Under `SIMULTANEOUS_ASSIGNMENT` it is an **error** (`ER_UPDATED_COLUMN_ONLY_ONCE`) — a column can't be changed more than once per statement |
| Treats the "rows affected" count as rows matched by `WHERE` | UPDATE reports rows **changed**, not matched. Rows whose new value equals the old are matched but not counted as changed (server message: `Rows matched: N Changed: M`). The client-side count depends on the `CLIENT_FOUND_ROWS` connection flag |
| Assumes one UPDATE of a system-versioned table writes one row | Each changed row also **inserts a history row**; the result reports an extra `Inserted: N`. Budget for the storage and for triggers seeing the history write. See `mariadb-system-versioned-tables` |
| Reaches for `LOW_PRIORITY` to de-prioritize an UPDATE on InnoDB | `LOW_PRIORITY` only affects table-lock engines (MyISAM, MEMORY, Aria). On InnoDB (row-level locking) it has **no effect** — drop it from generated SQL |
| Expects `IGNORE` to skip every problem row | `UPDATE IGNORE` **skips** rows that would cause duplicate-key conflicts, but rows with data-conversion problems are **clamped to the closest valid value**, not skipped. It's not a blanket "ignore errors" |
| Avoids referencing the target table in the `UPDATE`'s own `WHERE` subquery | Allowed: `UPDATE t SET c = c + 1 WHERE id = (SELECT MAX(id) FROM t);`. (Note: `DELETE` has the *opposite* restriction — it cannot delete from a table read in a subquery. See `mariadb-delete`) |
| Tries to assign to a column of a CTE or derived table | CTEs and derived tables in an UPDATE are **read-only** — read from them, but update only a real base table. `WITH … UPDATE …` is supported **since 12.3** |
| Assumes partition selection isn't available | `UPDATE t PARTITION (p0, p1) SET … WHERE …` limits the update to named partitions (single-table form) |

## Single-table vs multi-table — the core split

The two forms have **different grammars**. Mixing them up is the most common structural error.

```sql
-- Single-table: supports PARTITION, ORDER BY, LIMIT, RETURNING, FOR PORTION OF
UPDATE [LOW_PRIORITY] [IGNORE] table_ref
    [PARTITION (p_list)]
    [FOR PORTION OF period FROM expr1 TO expr2]
    SET col1 = {expr | DEFAULT} [, col2 = {expr | DEFAULT}] …
    [WHERE condition]
    [ORDER BY …]
    [LIMIT row_count]
    [RETURNING select_expr [, …]];        -- since 13.0

-- Multi-table: NONE of PARTITION / ORDER BY / LIMIT / RETURNING
UPDATE [LOW_PRIORITY] [IGNORE] table_refs
    SET col1 = {expr | DEFAULT} [, …]
    [WHERE condition];
```

A multi-table UPDATE joins tables and can write to several of them in one statement:

```sql
UPDATE orders o JOIN customers c ON o.cust_id = c.id
  SET o.region = c.region, c.order_count = c.order_count + 1
  WHERE o.status = 'new';
```

## Assignment evaluation order

Single-table UPDATE assigns **left-to-right** by default, so later assignments see the results of earlier ones:

```sql
-- counter ends at +2, because col2 sees the already-incremented col1:
UPDATE t SET col1 = col1 + 1, col2 = col1 WHERE id = 1;

-- True simultaneous assignment (e.g. a swap) needs the sql_mode:
SET sql_mode = 'SIMULTANEOUS_ASSIGNMENT';
UPDATE t SET col1 = col2, col2 = col1 WHERE id = 1;   -- swaps
```

Multi-table UPDATE makes **no ordering guarantee** — don't rely on assignment order across joined tables.

## `RETURNING` (since 13.0)

Single-table UPDATE can return data from the affected rows. Use `OLD_VALUE(col)` for the value before the update and a bare column reference for the value after:

```sql
UPDATE accounts SET balance = balance - 100
  WHERE id = 42
  RETURNING id, OLD_VALUE(balance) AS old_balance, balance AS new_balance;
```

`RETURNING` is **not** available on multi-table UPDATE (errors with "RETURNING for multi-table UPDATE").

## `ORDER BY … LIMIT` (single-table)

Bound how many rows a single-table UPDATE touches, in a defined order — useful for batched updates over a large table:

```sql
UPDATE page_hit SET processed = 1
  WHERE processed = 0
  ORDER BY ts
  LIMIT 1000;
```

## Temporal tables

- **System-versioned tables:** a normal UPDATE automatically closes the old row version and inserts a history row (reflected in the `Inserted: N` count). Query history with `SELECT … FOR SYSTEM_TIME …`. Full model: see `mariadb-system-versioned-tables`.
- **Application-time-period tables:** `UPDATE t FOR PORTION OF period FROM expr1 TO expr2 SET …` updates only the slice of each row's period that overlaps the range, splitting rows at the boundaries as needed.

## See Also

- **`mariadb-system-versioned-tables`** — history-row semantics, `FOR SYSTEM_TIME`, versioning-aware behavior referenced above
- **`mariadb-select`** — shared `ORDER BY`, `LIMIT`, `PARTITION`, and subquery surface; row-locking semantics that interact with UPDATE
- **`mariadb-delete`** — the sibling write statement, with the *opposite* same-table-subquery restriction
- **`mariadb-insert`** — `INSERT … ON DUPLICATE KEY UPDATE` when you mean "update if present, else insert"
- Canonical references (consult only for edge cases not covered here):
  - `server/reference/sql-statements/data-manipulation/changing-deleting-data/update.md` (~195 lines)
  - `…/high_priority-and-low_priority.md` (LOW_PRIORITY engine scope)
