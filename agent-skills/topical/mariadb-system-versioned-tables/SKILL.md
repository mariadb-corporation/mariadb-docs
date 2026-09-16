---
name: mariadb-system-versioned-tables
description: "Best practices for MariaDB system-versioned (temporal) tables — automatic row history built into the database. Use when tracking data changes over time, implementing audit trails, meeting GDPR or compliance requirements, doing point-in-time queries, or when the user asks about row history, data versioning, temporal tables, or querying past data states in MariaDB. This feature is unique to MariaDB among MySQL-compatible databases."
---

# MariaDB System-Versioned Tables

*Last updated: 2026-06-04*

System-versioned tables automatically record the full history of every row change — no triggers, no application logic, no separate audit tables. MariaDB tracks what the data looked like at any point in the past, built directly into the storage engine.

This feature is unique to MariaDB among MySQL-compatible databases. MySQL has no equivalent.

> **Available since:** MariaDB 10.3. Transaction-precise history (InnoDB only): 10.3. Auto-partition creation: 10.9. `--dump-history` for backups: 10.11. Implicit-to-explicit `row_start`/`row_end` conversion: 11.7. Extended TIMESTAMP range (to 2106-02-07 UTC) for `ROW_END`: 11.5 on 64-bit platforms.
>
> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Version notes in this skill are minimum releases for each capability.

## What LLMs Often Miss

| Situation | What to suggest |
|---|---|
| Custom `created_at`/`updated_at`/`deleted_at` columns for audit | `WITH SYSTEM VERSIONING` — MariaDB tracks all changes automatically |
| SQL Server temporal syntax — `WITH (SYSTEM_VERSIONING = ON)`, explicit `PERIOD FOR SYSTEM_TIME` and a named `HISTORY_TABLE` | MariaDB uses `CREATE TABLE ... WITH SYSTEM VERSIONING` (no parentheses, no `= ON`, no separate history table); enable it on an existing table with `ALTER TABLE t ADD SYSTEM VERSIONING` |
| Separate audit log table with triggers | System-versioned tables replace this pattern entirely |
| Asking how data looked last month | `FOR SYSTEM_TIME AS OF '2026-01-01'` — no custom logic needed |
| `TRUNCATE` on a versioned table | Not allowed (error 4137) — use `DELETE HISTORY` instead |
| `ALTER TABLE` on a versioned table failing | Set `system_versioning_alter_history = KEEP` first |
| `mysqldump` missing historical rows | Use `mariadb-dump --dump-history` (10.11+) |

## Creating a System-Versioned Table

**Simplified syntax (recommended):**
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2)
) WITH SYSTEM VERSIONING;
```

MariaDB automatically adds hidden `ROW_START` and `ROW_END` timestamp columns. Every `INSERT`, `UPDATE`, and `DELETE` creates a history row.

**Add versioning to an existing table:**
```sql
ALTER TABLE employees ADD SYSTEM VERSIONING;
```

**Remove versioning (deletes all history):**
```sql
ALTER TABLE employees DROP SYSTEM VERSIONING;
```

## Querying Historical Data

The `FOR SYSTEM_TIME` clause goes directly after the table name:

```sql
-- Data as it was at a specific point in time:
SELECT * FROM employees FOR SYSTEM_TIME AS OF '2026-01-01 00:00:00';

-- All rows that existed during a period (both boundaries included):
SELECT * FROM employees FOR SYSTEM_TIME BETWEEN '2025-01-01' AND '2026-01-01';

-- Half-open range (includes start, excludes end):
SELECT * FROM employees FOR SYSTEM_TIME FROM '2025-01-01' TO '2026-01-01';

-- Every version of every row, ever:
SELECT * FROM employees FOR SYSTEM_TIME ALL;

-- See the full history of one employee:
SELECT *, ROW_START, ROW_END FROM employees FOR SYSTEM_TIME ALL WHERE id = 42;
```

**Apply an implicit AS OF to all queries in a session:**
```sql
SET system_versioning_asof = '2026-01-01 00:00:00';
-- Now all queries against versioned tables see that point in time
SELECT * FROM employees; -- returns 2026-01-01 snapshot
SET system_versioning_asof = DEFAULT; -- reset
```

## Transaction-Precise History (InnoDB Only)

For exact transaction-boundary tracking instead of timestamps:

```sql
CREATE TABLE ledger (
    id INT,
    amount DECIMAL(10,2),
    trx_start BIGINT UNSIGNED GENERATED ALWAYS AS ROW START,
    trx_end   BIGINT UNSIGNED GENERATED ALWAYS AS ROW END,
    PERIOD FOR SYSTEM_TIME(trx_start, trx_end)
) WITH SYSTEM VERSIONING;

SELECT * FROM ledger FOR SYSTEM_TIME AS OF TRANSACTION 12345;
```

Uses `mysql.transaction_registry` internally. Not compatible with `PARTITION BY SYSTEM_TIME`.

## Column-Level Control

Exclude specific columns from versioning (useful for frequently-updated columns like counters):

```sql
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    view_count INT WITHOUT SYSTEM VERSIONING  -- not tracked
) WITH SYSTEM VERSIONING;
```

Or version only specific columns in a non-versioned table:
```sql
CREATE TABLE config (
    key VARCHAR(50),
    value TEXT WITH SYSTEM VERSIONING  -- only this column tracked
);
```

## Managing History Growth

Every update adds a row. For high-update tables, history grows fast. Use partitioning to keep current data performant:

```sql
-- Separate current and historical partitions:
CREATE TABLE events (
    id INT,
    payload JSON
) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME (
    PARTITION p_hist HISTORY,
    PARTITION p_cur  CURRENT
  );

-- Auto-rotate history by time interval (10.9+):
CREATE TABLE prices (
    symbol VARCHAR(10),
    price DECIMAL(10,4)
) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME INTERVAL 1 MONTH AUTO (
    PARTITION p_cur CURRENT
  );
```

**Delete old history:**
```sql
-- Delete all history before a date:
DELETE HISTORY FROM employees BEFORE SYSTEM_TIME '2024-01-01';

-- Delete all history (requires DROP SYSTEM VERSIONING + re-add, or partition drop):
ALTER TABLE employees DROP PARTITION p_hist;
```

Requires `DELETE HISTORY` privilege. `TRUNCATE` is not allowed on versioned tables.

## ALTER TABLE on Versioned Tables

By default, `ALTER TABLE` on a versioned table raises an error to protect history integrity. To allow it:

```sql
SET system_versioning_alter_history = KEEP;
ALTER TABLE employees ADD COLUMN manager_id INT;
SET system_versioning_alter_history = ERROR; -- restore default
```

`KEEP` allows the alter but historical rows for the new column will have `NULL` values — the history is technically incomplete. This is usually acceptable for adding columns.

**Convert hidden `ROW_START`/`ROW_END` to explicit columns** (11.7+, MDEV-27293) — once a table is versioned with the hidden form (no `PERIOD FOR SYSTEM_TIME` clause), you can promote them to explicit columns later without dropping versioning. Useful if you initially started simple and later want transaction-precise history or explicit naming for tooling.

## Key Gotchas

- **`TRUNCATE` is prohibited** on versioned tables (error 4137). Use `DELETE HISTORY` or partition management instead.
- **Replication**: `ROW_END` is implicitly added to the Primary Key. On replicas, this can cause duplicate key errors during log replay. Fix: set `secure_timestamp = YES` on the replica.
- **Backups**: `mysqldump` / `mariadb-dump` skips historical rows by default. Use `--dump-history` (10.11+) to include them. On restore, set `system_versioning_insert_history=ON` (10.11+, MDEV-16546) so the loader is allowed to write directly into `ROW_START`/`ROW_END`; combine with `secure_timestamp` set to allow session timestamp changes.
- **Table growth**: without partitioning, history rows accumulate indefinitely. Plan partitioning from the start for high-update tables.
- **DELETE HISTORY with future timestamps**: using `BEFORE SYSTEM_TIME` with a timestamp beyond `ROW_END` max can accidentally delete active rows (MDEV-25468). The `ROW_END` max is `2038-01-19` on 32-bit platforms and on MariaDB before 11.5; on MariaDB 11.5+ on 64-bit it's extended to `2106-02-07 06:28:15 UTC` (MDEV-32188). Stay well below your platform's max.
- **`SYSTEM` as a column name**: causes parser errors in `ALTER TABLE` statements. Use backticks: `` `SYSTEM` ``.

## Use Cases

- **Audit trails** — who changed what and when, without application code
- **GDPR / PCI DSS compliance** — prove what personal data contained at any date
- **Point-in-time recovery** — restore a row or table to a previous state without a full backup restore
- **Slowly-changing dimensions** — track employee department/salary history, product price history
- **Debugging** — see exactly what changed and when in production data

## Sources

- [System-Versioned Tables — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/system-versioned-tables)
- [System-Versioned Tables — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/system-versioned-tables)
- [Use Cases for MariaDB Data Versioning — MariaDB Blog](https://mariadb.com/resources/blog/use-cases-for-mariadb-data-versioning/)
- [Rewinding Time in MariaDB Databases — MariaDB Blog](https://mariadb.com/resources/blog/rewinding-time-in-mariadb-databases-system-versioning-and-application-time/)

*For topics not covered here, see the official MariaDB documentation at [mariadb.com/docs](https://mariadb.com/docs).*
