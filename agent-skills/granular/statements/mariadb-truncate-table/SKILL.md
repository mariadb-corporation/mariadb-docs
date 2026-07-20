---
name: mariadb-truncate-table
description: "MariaDB-specific syntax and behavior for TRUNCATE TABLE — DROP privilege (not DELETE), implicit commit with no rollback, unconditional AUTO_INCREMENT reset, no ON DELETE triggers, FK-parent tables rejected unless self-referencing, system-versioned tables and SEQUENCEs reject TRUNCATE outright, always '0 rows affected', and the WAIT n | NOWAIT extension. Use when writing, generating, or reviewing TRUNCATE TABLE statements that target MariaDB."
---

# TRUNCATE TABLE in MariaDB

*Last updated: 2026-07-20*

`TRUNCATE TABLE` looks like a fast `DELETE FROM tbl_name` with no `WHERE` clause, but MariaDB implements it as a DDL-like operation with its own privilege model, transaction semantics, and object-type restrictions. This skill covers where that behavior diverges from standard SQL and from what an LLM typically assumes.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one. (None of the behaviors below are newer than 10.6 — TRUNCATE's DDL semantics, the FK check, and the `WAIT`/`NOWAIT` clause all predate it.)

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `GRANT DELETE ON db.tbl TO user` is enough to let `user` run `TRUNCATE TABLE tbl` | `TRUNCATE TABLE` checks the `DROP` privilege, not `DELETE` — grant `DROP` instead. |
| "`TRUNCATE` resets `AUTO_INCREMENT` just like `DELETE FROM tbl` with no `WHERE` does" | `DELETE` **never** resets the counter, even when it removes every row. Only `TRUNCATE TABLE` resets `AUTO_INCREMENT` to the table's starting value, unconditionally — including on MyISAM and InnoDB, which normally never reuse values. |
| Wrapping `TRUNCATE TABLE` in a transaction so it can be rolled back on error | `TRUNCATE TABLE` causes an implicit commit (like other DDL) and cannot be rolled back. Any prior uncommitted work in the same transaction is committed too. Use `DELETE` inside the transaction if rollback must remain possible. |
| Assuming an `AFTER DELETE`/`BEFORE DELETE` trigger (e.g., an audit-log trigger) fires when a table is truncated | `TRUNCATE TABLE` does not delete rows one by one and does **not** invoke `ON DELETE` triggers at all. If trigger-based side effects must run, use `DELETE`. |
| `TRUNCATE TABLE parent_tbl` to quickly empty a table that other tables reference via `FOREIGN KEY` | InnoDB refuses this with `ER_TRUNCATE_ILLEGAL_FK` (`Cannot truncate a table referenced in a foreign key constraint`), unless the only FK is self-referencing, or the session has `SET FOREIGN_KEY_CHECKS=0`. Plain `DELETE` enforces FKs row-by-row instead of rejecting the whole statement. |
| `TRUNCATE TABLE t` to wipe current data from a `WITH SYSTEM VERSIONING` table while keeping (or "dropping") its history | MariaDB **rejects** `TRUNCATE TABLE` on a system-versioned table outright with `System-versioned tables do not support TRUNCATE TABLE` (`ER_VERS_NOT_SUPPORTED`). Use `DELETE HISTORY` to purge history, or `DELETE`/`DROP`+`CREATE` to clear current rows. |
| `TRUNCATE TABLE seq` to reset a `SEQUENCE` back to its start value | Sequences reject `TRUNCATE` with `ER_ILLEGAL_HA` ("doesn't have this option"). Use `ALTER SEQUENCE seq RESTART` or `DROP SEQUENCE` + `CREATE SEQUENCE` instead. |
| Reading the "rows affected" count from `TRUNCATE TABLE` to log how many rows were removed | `TRUNCATE TABLE` always reports **0 rows affected**, regardless of how many rows actually existed — treat it as "no information," not "zero rows removed." |
| Adding `IF EXISTS` to `TRUNCATE TABLE`, or assuming it silently no-ops on a missing table | Not supported. `TRUNCATE TABLE` on a nonexistent table errors `ER_NO_SUCH_TABLE` (`Table '...' doesn't exist`, SQLSTATE `42S02`) just like referencing it in most other statements. |

## Syntax

```sql
TRUNCATE [TABLE] tbl_name
  [WAIT n | NOWAIT]
```

* The `TABLE` keyword is optional — `TRUNCATE tbl_name` and `TRUNCATE TABLE tbl_name` are equivalent.
* `tbl_name` may be schema-qualified as `db_name.tbl_name`.
* `WAIT n | NOWAIT` is a MariaDB extension: it overrides `lock_wait_timeout` (and `innodb_lock_wait_timeout`) for this statement only — `WAIT n` sets both to `n` seconds, `NOWAIT` sets both to `0`. This clause is shared with several other DDL statements (`ALTER TABLE`, `RENAME TABLE`, `LOCK TABLES`, `DROP TRIGGER`, …), not unique to `TRUNCATE`.
* In `sql_mode=ORACLE`, the optional keywords `DROP STORAGE` / `REUSE STORAGE` are additionally accepted after the table name — they parse but have no effect (no-ops). Outside Oracle mode, that syntax is a parse error.
* No `IF EXISTS` form exists.

## DELETE vs TRUNCATE

| Aspect | `DELETE FROM tbl` (no `WHERE`) | `TRUNCATE TABLE tbl` |
|---|---|---|
| Privilege required | `DELETE` | `DROP` |
| Transaction | Normal DML; can be rolled back | Implicit commit; cannot be rolled back |
| `AUTO_INCREMENT` | Left untouched | Reset to the table's starting value |
| `ON DELETE` triggers | Fire once per row | Never fire |
| Rows-affected count | Accurate | Always reported as 0 |
| Row removal mechanism | Row-by-row | Drop-and-recreate (InnoDB, when unconstrained) or a mechanical "delete all" via the handler for other engines/cases |
| Binary logging / replication | Logged as DML (row or statement, per `binlog_format`) | Always logged in **statement** format, treated like `DROP TABLE` + `CREATE TABLE` for replication purposes |

## Foreign Keys

* A table that is the **parent** in a non-self-referencing `FOREIGN KEY` (i.e., some other table's FK references it) cannot be truncated: MariaDB raises `ER_TRUNCATE_ILLEGAL_FK` (SQLSTATE `42000`), naming the offending constraint.
* Self-referencing foreign keys (a table referencing its own columns) do **not** block `TRUNCATE`.
* Setting `SET FOREIGN_KEY_CHECKS=0` for the session bypasses this check entirely, allowing the truncate to proceed even though the table is FK-referenced.

## System-Versioned Tables and Sequences

* `TRUNCATE TABLE` on a table created `WITH SYSTEM VERSIONING` is rejected with `ER_VERS_NOT_SUPPORTED` ("System-versioned tables do not support TRUNCATE TABLE"), whether or not the session holds `LOCK TABLES`. To clear such a table, use `DELETE` (optionally followed by `DELETE HISTORY`), or drop and recreate it.
* `TRUNCATE TABLE` on a `SEQUENCE` object is rejected with `ER_ILLEGAL_HA`. Sequences support `RENAME` but not `TRUNCATE`; use `ALTER SEQUENCE ... RESTART` to reset one.
* `TRUNCATE TABLE` on a `VIEW` fails with `ER_NO_SUCH_TABLE` — views were never valid targets.

## Auto-Increment and Transaction Semantics

* `TRUNCATE TABLE` unconditionally resets the table's `AUTO_INCREMENT` counter to its starting value (the value from `AUTO_INCREMENT=N` at `CREATE TABLE` time, or 1 by default) — even for engines like InnoDB and MyISAM that otherwise never reuse a used `AUTO_INCREMENT` value. `DELETE` never resets it, even when every row is removed.
* `TRUNCATE TABLE` causes an implicit commit and cannot itself be rolled back; issuing it mid-transaction also commits everything else done earlier in that transaction.
* `TRUNCATE TABLE` **can** be run on a table the session already holds under `LOCK TABLES ... WRITE` (it upgrades that lock internally) — but it fails with `ER_TABLE_NOT_LOCKED` if the session holds `LOCK TABLES` on a *different* table and tries to truncate one it didn't lock, and with `ER_TABLE_NOT_LOCKED_FOR_WRITE` if it only holds a `READ` lock.

## Examples

```sql
-- Requires DROP privilege, not DELETE
GRANT DROP ON reporting.staging_import TO 'etl_user'@'%';

-- Empty a table and confirm AUTO_INCREMENT restarts at 1
CREATE TABLE t1 (a INT AUTO_INCREMENT PRIMARY KEY);
INSERT INTO t1 (a) VALUES (NULL), (NULL);   -- a = 1, 2
TRUNCATE TABLE t1;
INSERT INTO t1 (a) VALUES (NULL), (NULL);   -- a = 1, 2 again

-- Bypass the FK-parent restriction deliberately
SET FOREIGN_KEY_CHECKS=0;
TRUNCATE TABLE parent_tbl;
SET FOREIGN_KEY_CHECKS=1;

-- Cap how long the statement waits for its metadata lock
TRUNCATE TABLE big_table WAIT 5;
TRUNCATE TABLE big_table NOWAIT;
```

## See Also

- **`mariadb-delete`** — the row-by-row, rollback-able, trigger-firing alternative when `TRUNCATE`'s restrictions (privilege, FK, versioning, sequences) get in the way.
- **`mariadb-system-versioned-tables`** — why `TRUNCATE` is rejected on these tables and what `DELETE HISTORY` does instead.
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/table-statements/truncate-table>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/changing-deleting-data/delete>
  - <https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/system-versioned-tables>
