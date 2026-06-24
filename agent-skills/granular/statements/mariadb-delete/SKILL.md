---
name: mariadb-delete
description: "MariaDB-specific syntax and behavior for DELETE — RETURNING deleted rows in one statement, both multi-table forms (DELETE … FROM and DELETE FROM … USING) with ORDER BY/LIMIT (since 11.8), single-table ORDER BY/LIMIT/PARTITION/alias/index hints, DELETE HISTORY for system-versioned tables, FOR PORTION OF for application-time periods, QUICK/LOW_PRIORITY/IGNORE modifiers and their engine limits, deleting from a table referenced in its own subquery, and DELETE-vs-TRUNCATE differences. Use when writing, generating, or reviewing DELETE statements that target MariaDB."
---

# DELETE in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL `DELETE` and MariaDB's**. It assumes the agent already knows the standard form (`DELETE FROM t WHERE …`). Everything below documents MariaDB-specific syntax, the multi-table forms, temporal-table deletion, and the most common LLM traps.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `SELECT` the rows, then `DELETE` them, in two round trips | `DELETE FROM t WHERE … RETURNING id, name` returns the deleted rows in one statement. Single-table only; expressions and aliases allowed, no aggregates |
| "Multi-table DELETE can't take `ORDER BY` / `LIMIT`" | It can, **since 11.8**: `DELETE t1.*, t2.* FROM t1 JOIN t2 ON … ORDER BY t1.id DESC LIMIT 3;`. (The reference page is stale on this point — the capability is real.) |
| Knows only `DELETE t1 FROM …` for multi-table deletes | Both forms are valid: `DELETE t1.*[, t2.*] FROM table_refs WHERE …` **and** `DELETE FROM t1[, t2] USING table_refs WHERE …`. List each table to delete from with `tbl.*` |
| Puts `RETURNING` on a multi-table DELETE | Not allowed — `RETURNING` is single-table only. Use the single-table form, or `ROW_COUNT()` for a count |
| Uses `TRUNCATE` to empty a table inside a transaction or while holding a table lock | `TRUNCATE` does an implicit commit and won't run while the session holds a lock — use `DELETE FROM t` there. `TRUNCATE` also skips `ON DELETE` triggers, ignores FK cascades (and errors if the table is FK-referenced), and resets `AUTO_INCREMENT`; `DELETE` does none of these |
| Expects `DELETE FROM t` (no `WHERE`) to reset `AUTO_INCREMENT` | It does not — the counter keeps climbing. Only `TRUNCATE TABLE` resets it |
| Avoids referencing the target table in the `DELETE`'s subquery | Allowed: `DELETE FROM t1 WHERE c1 IN (SELECT c1 FROM t1 b WHERE b.c2 = 0);` — same source and target works. (Note: the failure on this only existed on long-unmaintained versions) |
| Drops history of a system-versioned table with a plain `DELETE` | A plain `DELETE` only moves rows to history — it doesn't remove them. To prune history use `DELETE HISTORY FROM t [BEFORE SYSTEM_TIME …]` (needs the dedicated `DELETE HISTORY` privilege). See `mariadb-system-versioned-tables` |
| Hand-rolls range deletion on an application-time-period table (read, delete, re-insert the split) | `DELETE FROM t FOR PORTION OF period FROM '2024-01-01' TO '2024-07-01'` shrinks/splits overlapping rows automatically. Not available in multi-table DELETE |
| Adds `QUICK` or `LOW_PRIORITY` expecting them to help on InnoDB | Both are table-lock-engine (MyISAM/Aria) concerns — `QUICK` skips index-block merging, `LOW_PRIORITY` waits for readers. No effect on InnoDB |
| Assumes single-table DELETE can't take an alias or index hints | `DELETE FROM t AS a WHERE a.c = …` (alias, since 11.6) and `USE/FORCE/IGNORE INDEX (…)` (single-table, since 11.8) are both supported |

## Multi-table DELETE

Two equivalent syntaxes; pick whichever reads better. The table(s) actually deleted from are named before `FROM` (first form) or right after `DELETE FROM` (second form); the rest are join references.

```sql
-- Form 1 — deleted tables listed before FROM:
DELETE t1.*, t2.* FROM t1 JOIN t2 ON t1.id = t2.t1_id
  WHERE t2.stale = 1
  ORDER BY t1.id DESC LIMIT 100;        -- ORDER BY / LIMIT since 11.8

-- Form 2 — USING clause:
DELETE FROM t1, t2 USING t1 JOIN t2 ON t1.id = t2.t1_id WHERE t2.stale = 1;
```

`RETURNING` is not available on either multi-table form.

## `RETURNING` (single-table)

```sql
DELETE FROM sessions WHERE expires_at < NOW()
  RETURNING id, user_id, UPPER(token) AS t;
```

Per-row expressions, stored functions, single-row subqueries, and `AS` aliases are allowed; aggregates are not.

## Single-table form

```sql
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
  FROM tbl [PARTITION (p1, p2)] [AS alias]
  [USE INDEX (…) | FORCE INDEX (…) | IGNORE INDEX (…)]   -- since 11.8
  [WHERE condition]
  [ORDER BY …] [LIMIT row_count]
  [RETURNING select_expr [, …]];
```

`ORDER BY … LIMIT` lets you delete a bounded batch in a defined order — useful for chunked deletes over a large table.

## Temporal tables

- **System-versioned tables:** plain `DELETE` moves rows to history rather than removing them. `DELETE HISTORY FROM t BEFORE SYSTEM_TIME '2024-01-01'` prunes the history itself and requires the `DELETE HISTORY` privilege. Full semantics (the `BEFORE SYSTEM_TIME TIMESTAMP`/`TRANSACTION` distinction, edge cases): see `mariadb-system-versioned-tables`.
- **Application-time-period tables:** `DELETE FROM t FOR PORTION OF period FROM expr1 TO expr2` deletes only the overlapping slice of each row's period, splitting rows at the boundaries. Not supported in multi-table DELETE.

## `DELETE` vs `TRUNCATE`

| | `DELETE FROM t` | `TRUNCATE TABLE t` |
|---|---|---|
| Transactional / rollbackable | Yes | No — implicit commit |
| Fires `ON DELETE` triggers | Yes | No |
| FK cascades / can run if FK-referenced | Cascades fire | Errors if the table is FK-referenced |
| Resets `AUTO_INCREMENT` | No | Yes |
| Can run while holding a table lock | Yes | No |

Use `TRUNCATE` only to fast-empty a standalone table outside a transaction.

## See Also

- **`mariadb-system-versioned-tables`** — `DELETE HISTORY` semantics, the `DELETE HISTORY` privilege, `BEFORE SYSTEM_TIME` TIMESTAMP vs TRANSACTION
- **`mariadb-select`** — shared `PARTITION`, `ORDER BY`/`LIMIT`, and subquery surface
- **`mariadb-update`** — the sibling write statement; multi-table rules and `FOR PORTION OF` mirror DELETE's
- Canonical references (consult only for edge cases not covered here):
  - `server/reference/sql-statements/data-manipulation/changing-deleting-data/delete.md` (~240 lines; note: stale on multi-table `ORDER BY`/`LIMIT`)
  - `…/table-statements/truncate-table.md` (~90 lines)
