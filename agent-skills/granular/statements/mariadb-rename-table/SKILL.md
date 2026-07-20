---
name: mariadb-rename-table
description: "MariaDB-specific syntax and behavior for RENAME TABLE — atomic multi-table renames executed left-to-right with full rollback on any failure (enabling the classic swap trick), works directly on TEMPORARY tables (no ALTER TABLE needed), refuses to run inside an active transaction or under LOCK TABLES, requires ALTER+DROP on the source and CREATE+INSERT on the target, supports IF EXISTS and WAIT/NOWAIT, and has specific cross-database move restrictions for views and tables with triggers. Use when writing, generating, or reviewing RENAME TABLE statements that target MariaDB."
---

# RENAME TABLE in MariaDB

*Last updated: 2026-07-20*

`RENAME TABLE` renames — and optionally moves — one or more tables or views in a single atomic statement. It is the primitive behind the well-known "instant" table-swap pattern, but it has sharper edges (transaction/lock restrictions, exact privilege set, temporary-table handling) than most LLMs assume by analogy with other systems.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| "Temporary tables can't be renamed with `RENAME TABLE`; use `ALTER TABLE ... RENAME TO` instead." | In MariaDB, `RENAME TABLE t1 TO t2;` works directly on a `TEMPORARY` table — no `ALTER TABLE` needed. |
| `RENAME TABLE` inside a `BEGIN … COMMIT` block, assuming it just runs like other DDL. | MariaDB refuses outright: issuing `RENAME TABLE` inside an active transaction (or while `LOCK TABLES` is in effect) raises `ER_LOCK_OR_ACTIVE_TRANSACTION` ("Can't execute the given command because you have active locked tables or an active transaction") rather than implicitly committing and proceeding. |
| Granting only `ALTER` (or only `DROP`) and assuming that covers a rename. | The full requirement is **`ALTER` + `DROP`** on the source table/database and **`CREATE` + `INSERT`** on the target table/database — all four privileges, split across both names. |
| A multi-pair `RENAME TABLE t1 TO t2, t3 TO t4` where, if `t3` is missing, assuming `t1 TO t2` already "took" and only the failing pair errors. | The whole statement is atomic: renames are applied left-to-right, but if any pair fails, **every** rename in the statement is rolled back, including ones that already succeeded. |
| Emulating a table swap with `DROP`/temp-name juggling across several separate statements. | Do it in one atomic statement: `RENAME TABLE t1 TO tmp, t2 TO t1, tmp TO t2;` — safe because the whole thing is one all-or-nothing operation. |
| `RENAME TABLE db1.t TO db2.t;` assumed to always work for moving any object between databases. | It fails for **views** (`ER_FORBID_SCHEMA_CHANGE`, "Changing schema … is not allowed") and for tables that have **triggers** (`ER_TRG_IN_WRONG_SCHEMA`, "Trigger in wrong schema") — cross-database moves are blocked in both cases. |
| Treating `IF EXISTS` as unsupported on `RENAME TABLE` (only assumed valid on `DROP TABLE`/`CREATE TABLE`). | `RENAME TABLE IF EXISTS t1 TO t2, ...` is valid — a missing source table becomes a note/warning instead of an error, and the statement continues with the remaining pairs. |
| Assuming `RENAME TABLE` has no way to control metadata-lock waiting. | Each pair can carry `WAIT n` or `NOWAIT` (e.g. `RENAME TABLE t1 NOWAIT TO t2;`), which sets the lock-wait timeout for that statement's metadata-lock acquisition. |
| Assuming `RENAME TABLES` (plural) is a different statement that must be used for multi-table renames, or that it behaves differently from `RENAME TABLE`. | `TABLE`/`TABLES` are interchangeable — the presence or absence of the `S` has zero effect on behavior, single or multi-table. |

## Syntax

```sql
RENAME TABLE[S] [IF EXISTS] tbl_name
  [WAIT n | NOWAIT]
  TO new_tbl_name
    [, tbl_name2 [WAIT n | NOWAIT] TO new_tbl_name2] ...
```

- `tbl_name` may be qualified as `db_name.tbl_name` on either side of `TO`, which moves the table to another database as part of the rename (subject to the view/trigger restrictions below).
- Multiple `tbl_name TO new_tbl_name` pairs may be given, comma-separated, in one statement; they execute strictly left-to-right.
- `IF EXISTS` suppresses the error (turning it into a warning) when a named source table does not exist.
- `WAIT n | NOWAIT` sets the lock-wait timeout for acquiring the metadata lock needed for that pair's rename.
- Do not confuse this with `RENAME USER old TO new [, ...]`, which shares the `RENAME` keyword but is a completely different statement (account management, not table DDL).

## Atomicity, Ordering, and the Swap Trick

`RENAME TABLE` with multiple pairs is one atomic operation: no other session can see any of the tables mid-rename, pairs are applied in the order written, and if any pair fails, all renames performed earlier in the same statement are reverted. This is what makes the classic swap safe:

```sql
CREATE TABLE new_table (...);
-- populate new_table --
RENAME TABLE old_table TO backup_table, new_table TO old_table;
```

or, to swap two existing tables' names outright:

```sql
RENAME TABLE t1 TO tmp_table,
             t2 TO t1,
             tmp_table TO t2;
```

For most storage engines (including InnoDB, MyRocks, MyISAM, and Aria) this atomicity extends to crash safety: if the server crashes mid-statement, all tables — and any trigger files touched — revert to their pre-statement names on recovery.

## Restrictions on When RENAME TABLE Can Run

`RENAME TABLE` cannot be issued:
- inside an active (explicit or already-started) transaction, or
- while the session holds tables via `LOCK TABLES`.

Both cases raise `ER_LOCK_OR_ACTIVE_TRANSACTION` immediately, before any table is touched — there is no implicit commit-and-continue behavior here, unlike some other DDL statements.

## Moving Tables Between Databases

Qualifying either side with a database name moves the table:

```sql
RENAME TABLE db1.t TO db2.t;
```

This requires the databases to be reachable by the storage engine (effectively, the same filesystem/tablespace for file-based engines). Two cases are explicitly blocked:

- **Tables with triggers** cannot be moved to another database — MariaDB raises `ER_TRG_IN_WRONG_SCHEMA` ("Trigger in wrong schema", error 1435). Triggers on a table that stays within the same database are automatically updated to reference the new table name.
- **Views** cannot be moved to another database at all — MariaDB raises `ER_FORBID_SCHEMA_CHANGE` ("Changing schema from 'old_db' to 'new_db' is not allowed", error 1450). Renaming a view within the same database works normally.

## Temporary Tables

`RENAME TABLE` works directly on `TEMPORARY` tables — there is no need to fall back to `ALTER TABLE ... RENAME TO`. Temporary-table renames are handled separately from permanent-table renames internally (they are not written to the DDL recovery log, since temporary tables disappear on crash anyway) but use identical syntax.

## Privileges

Executing `RENAME TABLE` requires:
- **`ALTER`** and **`DROP`** on the source table (or its database), and
- **`CREATE`** and **`INSERT`** on the target table (or its database).

All four privileges are checked, split across the two names — granting only a subset of them is a common under-provisioning mistake.

## Contrast With ALTER TABLE ... RENAME TO

`ALTER TABLE tbl_name RENAME TO new_name` renames a single table as one clause of a (possibly larger) `ALTER TABLE` statement, and can also move a table between databases. It does not offer the multi-pair, all-or-nothing semantics of `RENAME TABLE` — there is no equivalent to the comma-separated swap trick. Use `RENAME TABLE` when the goal is purely renaming/swapping one or more tables atomically; use `ALTER TABLE ... RENAME TO` when the rename is one of several changes being made to a table in the same statement.

## See Also

- **`mariadb-alter-table`** — the single-table `RENAME TO` alternative, and the only way to rename columns/indexes in the same statement.
- **`mariadb-create-trigger`** — why a table with triggers can't be moved across databases with `RENAME TABLE`.
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/rename-table>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/alter/alter-table>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/atomic-ddl>
