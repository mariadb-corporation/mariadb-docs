---
name: mariadb-alter-table
description: "MariaDB-specific syntax and behavior for ALTER TABLE — online DDL with ALGORITHM (DEFAULT/COPY/INPLACE/NOCOPY/INSTANT) and LOCK clauses, ALTER ONLINE TABLE shorthand, WAIT/NOWAIT lock timeouts, IF EXISTS/IF NOT EXISTS on subclauses, ADD/DROP SYSTEM VERSIONING, ADD PERIOD FOR, DROP CONSTRAINT, FORCE rebuild, CONVERT PARTITION/TABLE, DISCARD/IMPORT TABLESPACE, atomic ALTER, two-phase replication. Use when writing, generating, or reviewing ALTER TABLE statements that target MariaDB, or planning schema migrations against MariaDB."
---

# ALTER TABLE in MariaDB

*Last updated: 2026-06-02*

This skill covers the **delta between standard SQL `ALTER TABLE` and MariaDB's**. It assumes the agent already knows the standard form (`ALTER TABLE name ADD/DROP/MODIFY …`). Everything below documents MariaDB-specific syntax, lock/algorithm behavior, and online-DDL nuances. For column attributes and index options themselves, defer to the **`mariadb-create-table`** skill — both statements share them.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| Several `ALTER TABLE t …;` statements in a row | **Combine into one** `ALTER TABLE t ADD …, DROP …, MODIFY …;` — MariaDB rebuilds the table only once for the whole list, vs. once per statement |
| Reaching for `gh-ost` / `pt-online-schema-change` | Not needed for InnoDB on MariaDB — `ALTER TABLE` defaults to `ALGORITHM=DEFAULT, LOCK=DEFAULT`, which already does online DDL where the operation supports it. For copy-algorithm operations, `LOCK=NONE` is supported since 11.2 |
| `LOCK TABLES … WRITE; ALTER TABLE …; UNLOCK TABLES;` to "make it safe" | The opposite — that *blocks* concurrent reads/writes. Use `ALTER ONLINE TABLE …` or `ALTER TABLE … LOCK=NONE` instead |
| `ALTER TABLE` on a system-versioned table failing with a duplicate-row error | Set `system_versioning_alter_history = KEEP` (session) before altering — see the `mariadb-system-versioned-tables` skill |
| Migration script that fails if a column already exists / a column doesn't exist | Use the subclause-level `IF NOT EXISTS` / `IF EXISTS` (see "IF EXISTS" below) for idempotent migrations — emits a warning instead of erroring |
| `ALTER TABLE t DROP CHECK constraint_name` | `ALTER TABLE t DROP CONSTRAINT constraint_name` — MariaDB uses the standard `DROP CONSTRAINT` form for check constraints (and others) |
| Big `DELETE` to shrink a table, no follow-up | `ALTER TABLE t FORCE;` rebuilds the table and reclaims unused space (requires `innodb_file_per_table=ON`, default) |
| Setting `ALGORITHM=INPLACE` blindly to avoid copy | If the operation rebuilds the clustered index, `INPLACE` may still be slow. Use `ALGORITHM=NOCOPY` to *require* no clustered-index rebuild — it errors out if the operation can't do that |
| Schema migration on a replication primary causing replica lag | Set `binlog_alter_two_phase=ON` (since 10.8) so replicas begin applying when the primary *starts* the ALTER, not when it finishes |

## Online DDL — `ALGORITHM` and `LOCK`

`ALTER TABLE t … , ALGORITHM=…, LOCK=…;`

### ALGORITHM values

| Algorithm | Meaning | Use case |
|---|---|---|
| `DEFAULT` | Pick the most efficient algorithm the operation supports | Almost always the right choice; named for explicit override |
| `COPY` | Build a new table + copy all rows + rename. Generic, works for any engine | Old / fallback path. As of 11.2 supports `LOCK=NONE` for most operations |
| `INPLACE` | Engine-specific in-place operation; *may* still rebuild | Most InnoDB add/drop column / index operations land here |
| `NOCOPY` | **MariaDB-specific.** Like `INPLACE` but errors out if the operation would rebuild the clustered index | Use to guarantee fast schema change on large tables — fail fast if it would be slow |
| `INSTANT` | Metadata-only operation, no data files touched | Add column at end (InnoDB), some column renames, some default-value changes |

> `alter_algorithm` (and the older `old_alter_table`) system variable was **removed in 11.5** — set `ALGORITHM=…` explicitly per statement if you need to override.

### LOCK values

| Lock | Effect |
|---|---|
| `DEFAULT` | Least restrictive lock the operation supports |
| `NONE` | All concurrent DML allowed. As of 11.2, supported for most operations under any algorithm; before 11.2, restricted to certain `ALGORITHM=INPLACE` operations |
| `SHARED` | Concurrent reads only |
| `EXCLUSIVE` | No concurrent DML |

### `ALTER ONLINE TABLE` shorthand

```sql
ALTER ONLINE TABLE t ADD COLUMN c INT;
-- equivalent to:
ALTER TABLE t ADD COLUMN c INT, LOCK=NONE;
```

Fails with an error if the operation can't actually run with `LOCK=NONE`. Use this when you want the migration to refuse rather than silently block writers.

## WAIT / NOWAIT — Lock Timeout per Statement

```sql
ALTER TABLE t WAIT 5 ADD COLUMN c INT;     -- wait up to 5s for MDL, then ER_LOCK_WAIT_TIMEOUT
ALTER TABLE t NOWAIT ADD COLUMN c INT;     -- fail immediately if MDL can't be acquired
```

Bounds how long the statement will wait for the metadata lock. Indispensable for safe migration tooling — without these the statement may queue indefinitely behind a long-running transaction. Applies to many other statements too (`SELECT … FOR UPDATE WAIT N`, `LOCK TABLES … NOWAIT`, etc.).

## IF EXISTS / IF NOT EXISTS on Subclauses

MariaDB allows `IF EXISTS` / `IF NOT EXISTS` on individual subclauses, not just on the table:

```sql
ALTER TABLE t
  ADD COLUMN IF NOT EXISTS c INT,
  ADD INDEX IF NOT EXISTS idx_c (c),
  DROP COLUMN IF EXISTS legacy_col,
  DROP FOREIGN KEY IF EXISTS fk_old;
```

When the condition isn't met (column already exists, column doesn't exist, …), the statement emits a **warning** and skips that subclause, continuing to the next. This is how idempotent migrations are written in MariaDB. Supported subclauses: `ADD COLUMN`, `ADD INDEX`, `ADD FOREIGN KEY`, `ADD PARTITION`, `CREATE INDEX`, `DROP COLUMN`, `DROP INDEX`, `DROP FOREIGN KEY`, `DROP PARTITION`, `CHANGE COLUMN`, `MODIFY COLUMN`.

`ALTER TABLE IF EXISTS t …` (on the table itself) emits a warning if the table is missing rather than erroring.

## System Versioning Operations

```sql
ALTER TABLE t ADD SYSTEM VERSIONING;     -- start versioning an existing table
ALTER TABLE t DROP SYSTEM VERSIONING;    -- stop versioning; DELETES ALL HISTORY
ALTER TABLE t ADD PERIOD FOR effective (valid_from, valid_to);   -- application-time period
```

**Trap:** any other `ALTER` on an already-system-versioned table requires `system_versioning_alter_history = KEEP` (session-level), otherwise the statement errors out. Setting this preserves existing history rows under the new schema — querying historical data may return rows that don't match the new column definitions, which is documented behavior.

See the `mariadb-system-versioned-tables` skill for the full versioning model.

## DROP CONSTRAINT

```sql
ALTER TABLE t DROP CONSTRAINT c_name;
```

Single statement drops any kind of constraint by name — check constraints, named foreign keys, named unique constraints. Use this rather than older form-specific clauses like `DROP CHECK`.

## FORCE — Rebuild the Table

```sql
ALTER TABLE t FORCE;
```

Rebuilds the table without changing its definition. Two main use cases:

- **Reclaim space** after large `DELETE` operations (requires `innodb_file_per_table=ON`, the default).
- **Re-validate data** under a stricter `sql_mode` — e.g. setting `NO_ZERO_DATE` and then `FORCE` will surface existing rows that violate the new mode.

## Partition Operations

Standard SQL partition-management clauses are supported. MariaDB-specific or version-specific points:

| Clause | Notes |
|---|---|
| `CONVERT PARTITION p TO TABLE t2` | Detach a partition into a standalone table |
| `CONVERT TABLE t2 TO PARTITION p VALUES …` | Attach a standalone table as a new partition |
| `EXCHANGE PARTITION p WITH TABLE t2` | Swap data between a partition and a table |
| `REMOVE PARTITIONING` | Convert a partitioned table back to a regular table |

For partitioning by `SYSTEM_TIME` (auto-rotating history partitions for system-versioned tables), see the `mariadb-system-versioned-tables` skill.

## DISCARD / IMPORT TABLESPACE — InnoDB Transportable Tablespaces

```sql
-- On the source server:
FLUSH TABLES t FOR EXPORT;     -- creates t.cfg alongside t.ibd
-- copy t.ibd and t.cfg to the destination datadir
-- On the destination:
ALTER TABLE t DISCARD TABLESPACE;
-- ...place the .ibd file in the destination's datadir...
ALTER TABLE t IMPORT TABLESPACE;
```

InnoDB-only. Aria, MyISAM, etc. don't need this — they pick up data files placed in the datadir directly.

## Atomic ALTER and Replication

- `ALTER TABLE` is **atomic** for InnoDB, MyRocks, MyISAM, and Aria — crash recovery leaves either the old or the new table intact, never partial `#sql-*` files. (Since 10.6.)
- DDL still triggers an implicit commit; no transactional rollback of an `ALTER`.
- Set `binlog_alter_two_phase=ON` (since 10.8) to start replicating ALTER when it *begins* on the primary rather than when it finishes. Eliminates the replication lag of a long-running schema change.

## See Also

- **`mariadb-create-table`** — column definitions, index definitions, and table options (shared syntax surface)
- **`mariadb-system-versioned-tables`** — versioning model, `system_versioning_alter_history`, history-row semantics
- Canonical reference: `server/reference/sql-statements/data-definition/alter/alter-table/README.md` (~870 lines) plus `…/alter-table/online-schema-change.md` — consult only for edge cases not covered here
