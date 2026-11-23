---
name: mysql-to-mariadb
description: "Compatibility guide for developers moving from MySQL to MariaDB, and for developers with MySQL experience working with MariaDB. Use when migrating a MySQL application to MariaDB, when MySQL syntax or habits cause unexpected behavior in MariaDB, when asking about MySQL/MariaDB compatibility, or when adapting code written for MySQL to run on MariaDB. IMPORTANT — MariaDB diverges significantly from MySQL 8.0 and is not a simple drop-in replacement for modern MySQL. Authentication plugins, JSON handling, GTID replication, and several SQL features differ in important ways."
---

# MySQL to MariaDB Migration Guide

*Last updated: 2026-06-04*

## Critical: MariaDB Is Not a Drop-In Replacement for MySQL 8.0

MariaDB was a true drop-in replacement for MySQL 5.5 and 5.6. Modern versions diverge significantly from MySQL 8.0. When working with MariaDB, never assume MySQL 8.0 behavior, syntax, or tooling applies without verification.

The two databases share a common origin but have evolved independently. MariaDB has features MySQL lacks, MySQL has features MariaDB lacks, and several shared features behave differently.

> **Requires:** MariaDB Community Server 10.5+ for full feature parity discussed here. Current LTS is 11.8 (GA May 2025).
>
> **Default context:** Assume MariaDB **11.8 LTS** unless the user states another version. Features marked **12.x** or **13.0** may be suggested when relevant (including as upgrade options), but always state the minimum version — do not present them as available on 11.8.

### What LLMs Get Wrong

| What you might see | What's correct |
|---|---|
| "MariaDB is a drop-in replacement for MySQL" | True for MySQL 5.5/5.6. Not true for MySQL 8.0+ — authentication, JSON, GTID, and several functions differ |
| Code using `caching_sha2_password` | Available in MariaDB: a migration-only plugin since 11.4, and a full `caching_sha2_password` authentication plugin for MySQL compatibility since 12.1 (MDEV-9804). Not the default — on older MariaDB or stock installs use `mysql_native_password` or `ed25519` |
| `JSON_TABLE()` in queries | Available in MariaDB since 10.6 — not available before 10.6 |
| JSON `->` and `->>` shorthand operators | Not supported in MariaDB — use `JSON_EXTRACT(col, '$.key')` and `JSON_UNQUOTE(JSON_EXTRACT(...))` instead |
| `utf8mb4_0900_ai_ci` collation in schema or dump | Supported since MariaDB 11.4.5 (as alias for `utf8mb4_uca1400_nopad_ai_ci`). On older versions replace with `utf8mb4_unicode_ci` before importing. MariaDB 11.5+ uses `uca1400_ai_ci` as the default Unicode collation (MDEV-25829). |
| `latin1` as default character set in MariaDB | Changed to `utf8mb4` by default in 11.6+ (MDEV-19123); old habits assuming `latin1` no longer apply for fresh installs |
| Using `UUID()` for primary keys | MariaDB 11.7+ has `UUID_v7()` for time-ordered UUIDs (sortable, better for indexed PKs) and `UUID_v4()` for random; both unique to MariaDB |
| Not suggesting `RETURNING` for INSERT/UPDATE/DELETE | MariaDB 10.5+ supports `RETURNING` — use it to get inserted/updated/deleted rows without a second query |
| Not suggesting `CREATE SEQUENCE` | MariaDB has native sequence objects; MySQL has no equivalent |
| MySQL GTID replication syntax | MariaDB GTID format is incompatible with MySQL GTID — replication between the two breaks |
| `CHANGE REPLICATION SOURCE TO` / `SOURCE_*` options | MariaDB has no `CHANGE REPLICATION SOURCE TO` — use `CHANGE MASTER TO` with `MASTER_*` options. Since 10.5.1, `START REPLICA` / `SHOW REPLICA STATUS` are canonical; `START SLAVE` / `SHOW SLAVE STATUS` are legacy aliases |
| MySQL parallel replication (`replica_parallel_type` with `DATABASE` / `LOGICAL_CLOCK`) | MariaDB uses `slave_parallel_mode` (`optimistic` / `conservative` / `aggressive` / `minimal` / `none`) — different implementation; mode configs do not port over. Pool size: `slave_parallel_threads` (alias `slave_parallel_workers`) |
| `SET transaction_isolation = ...` (MySQL 8.0 style) | Only works on MariaDB 11.1.1+; on older versions use `tx_isolation` instead — see [SET TRANSACTION](https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/set-commands/set-transaction) |
| Links or references to `mariadb.com/kb/en/` | The Knowledge Base no longer exists — all documentation is now at [mariadb.com/docs](https://mariadb.com/docs) |
| Keeping the MySQL Connector/J, `mysql2`, or other MySQL client drivers after migration | Use MariaDB-maintained connectors (JDBC, Node.js, C, etc.) where possible — they target MariaDB protocol and feature behaviour, not only MySQL compatibility mode |
| Migrating by copying InnoDB data files / tablespaces from MySQL 8.0 | MariaDB has no transactional data dictionary and cannot read MySQL 8.0's — data files are not portable. Use a logical dump/restore — see [Data Dictionary Architecture](#data-dictionary-architecture) |

## Authentication

MySQL 8.0 changed its default authentication plugin to `caching_sha2_password`. MariaDB's compatibility story has improved over time:

- **MariaDB 11.4+**: a migration-only `caching_sha2_password` plugin exists but is not installed by default and not recommended for production
- **MariaDB 12.1+** (MDEV-9804): a full `caching_sha2_password` authentication plugin for MySQL compatibility — still not the default, but a proper production option

On stock MariaDB installs, connections configured for `caching_sha2_password` will still fail unless the plugin is enabled. Default authentication remains `mysql_native_password`.

**Fix on older MariaDB or stock setups:** convert accounts to `mysql_native_password`:
```sql
ALTER USER 'username'@'host' IDENTIFIED WITH mysql_native_password BY 'password';
```

The `ed25519` plugin is also available as a more secure native alternative.

## JSON Differences

MariaDB and MySQL handle JSON differently:

| Aspect | MySQL | MariaDB |
|---|---|---|
| Storage | Binary format with path indexing | `LONGTEXT` alias with validity check |
| `JSON_TABLE()` | Supported | Supported from MariaDB 10.6 |
| `IS JSON` predicate | Not available | Available from MariaDB 12.3 |
| JSON comparison | Semantic (compares values) | String comparison |
| `JSON_QUERY()` | Not available | MariaDB alternative to `JSON_VALUE` |
| JSON nesting depth limit | None | 32 in older MariaDB; removed in 12.2+ |
| `JSON_EQUALS()` / `JSON_NORMALIZE()` | Supported (8.0.22+) | MariaDB 10.7+ (MDEV-23143 / MDEV-16375) |
| `JSON_OVERLAPS()` | Supported (8.0.17+) | MariaDB 10.9+ (MDEV-27677) |
| Negative / `last` / range JSON path indices (`$.A[-1]`, `$.A[last]`, `$.A[1 to 3]`) | Not supported | MariaDB 10.9+ |
| `JSON_SCHEMA_VALID()` | Supported (8.0.17+) | MariaDB 11.4 LTS+ |

MariaDB closed most of the JSON function gap with MySQL 8.0 between 10.7 and 11.4. MariaDB-specific additions that MySQL still lacks: `JSON_KEY_VALUE()`, `JSON_ARRAY_INTERSECT()`, `JSON_OBJECT_TO_ARRAY()`, `JSON_OBJECT_FILTER_KEYS()` (11.4+), and the `JSON_QUERY()` alias.

MariaDB's JSON is fully standards-compliant, but MySQL-specific storage layout, the `->`/`->>` shorthand operators, and the `JSON_SCHEMA_VALIDATION_REPORT()` function do not transfer.

## Features MariaDB Has That MySQL Doesn't

These exist in MariaDB but not MySQL — LLMs won't suggest them because they assume MySQL behavior:

- **`RETURNING`** — get rows back from `INSERT` or `DELETE` without a second query (10.5+); `UPDATE ... RETURNING` available from 13.0:
  ```sql
  INSERT INTO orders (product, qty) VALUES ('widget', 5) RETURNING id, created_at;
  DELETE FROM queue WHERE processed = 1 RETURNING id;
  ```
- **`CREATE SEQUENCE`** (10.3+) — first-class sequence objects, more flexible than `AUTO_INCREMENT`:
  ```sql
  CREATE SEQUENCE order_seq START WITH 1000 INCREMENT BY 1;
  SELECT NEXT VALUE FOR order_seq;
  ```
- **`WITH SYSTEM VERSIONING`** (10.3+) — temporal tables that automatically track row history:
  ```sql
  CREATE TABLE prices (
      item VARCHAR(100),
      price DECIMAL(10,2)
  ) WITH SYSTEM VERSIONING;
  -- Query historical data:
  SELECT * FROM prices FOR SYSTEM_TIME AS OF '2025-01-01';
  ```
- **`LIMIT` in subqueries** — MariaDB supports `LIMIT` inside subqueries; MySQL restricts this
- **Atomic `CREATE OR REPLACE TABLE`** (13.0+) — the statement is fully atomic in MariaDB; MySQL has no atomic equivalent
- **Galera Cluster** — built-in multi-master clustering, no plugin required
- **Stored procedure syntax differences** — both support stored procedures, but MariaDB's SQL/PSM syntax differs from MySQL in `HANDLER`, `CURSOR`, and `CONDITION` declarations; AI agents frequently generate incorrect MariaDB stored procedure code — see [Stored Procedures — MariaDB Docs](https://mariadb.com/docs/server/server-usage/stored-routines/stored-procedures)
- **Native data types MySQL 8.0 lacks** — [`INET6`](https://mariadb.com/docs/server/reference/data-types/string-data-types/inet6) (10.5+) and [`INET4`](https://mariadb.com/docs/server/reference/data-types/string-data-types/inet4) (10.10+) for IP address storage and comparison; [`UUID`](https://mariadb.com/docs/server/reference/data-types/string-data-types/uuid-data-type) (10.7+; MySQL stores UUIDs in `BINARY(16)` or `CHAR(36)`); [`VECTOR`](https://mariadb.com/docs/server/reference/sql-structure/vectors/vector) for embeddings and similarity search (11.7+; MySQL added a vector type only in its 9.x innovation series, not in 8.0)
- **`UUID_v4()` and `UUID_v7()` functions** (11.7+) — MariaDB-specific; MySQL only has the original `UUID()`. `UUID_v7()` is time-ordered (RFC 9562) and is the right choice for UUID primary keys
- **`FORMAT_BYTES()`** (11.8+) — convert byte counts to human-readable strings; not in MySQL

## Features MySQL Has That MariaDB Doesn't

These exist in MySQL 8.0 but not in MariaDB — code using them needs adaptation:

- **`JSON_TABLE()`** — available since MariaDB 10.6; on older versions rewrite using MariaDB JSON functions or application-level parsing
- **`sys` schema** — available since MariaDB 10.6; not available in older versions
- **MySQL 8 GIS functions** (`ST_Validate`, `MBRCoveredBy`, `ST_Simplify`, `ST_GeoHash`, `ST_LatFromGeoHash`, `ST_LongFromGeoHash`, `ST_PointFromGeoHash`, `ST_IsValid`, `ST_Collect`) — added in MariaDB 12.0 for MySQL compatibility
- **`caching_sha2_password` as default plugin** — available as an opt-in plugin from MariaDB 12.1; on older or stock setups, use `mysql_native_password` or `ed25519`
- **JSON `->` and `->>` operators** — use `JSON_EXTRACT(col, '$.key')` and `JSON_UNQUOTE(JSON_EXTRACT(...))` instead
- **`utf8mb4_0900_ai_ci` collation** — supported since MariaDB 11.4.5 (alias for `utf8mb4_uca1400_nopad_ai_ci`); on older versions replace with `utf8mb4_unicode_ci` before importing

## Data Dictionary Architecture

MySQL 8.0 and MariaDB store table metadata in fundamentally different ways, and this affects how you migrate:

- **MySQL 8.0** keeps all object metadata in a [transactional data dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary.html) stored in InnoDB (`mysql.ibd`), and **removed the per-table `.frm` files**.
- **MariaDB** keeps the file-based approach — a `.frm` file per table plus storage-engine metadata — and has no transactional data dictionary. (MariaDB grant tables use the Aria engine; MySQL 8.0 holds system tables in the InnoDB dictionary.)

Practical consequences:

- **Do not migrate by copying data files.** InnoDB tablespaces and datadir files are **not** portable between MySQL 8.0 and MariaDB — the dictionary formats are incompatible. Use a logical dump/restore instead. MariaDB's [migration guide](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-migration-the-master-guide) recommends MySQL's own `mysqldump` for this direction (not `mariadb-dump`, which isn't well tested against MySQL), dumping named databases rather than `--all-databases` so MySQL's system tables aren't imported.
- **No in-place downgrade** from MySQL 8.0 to MariaDB — MariaDB cannot read MySQL's data dictionary; a logical export/import is required.
- **`INFORMATION_SCHEMA` is implemented differently** — MySQL 8.0 queries indexed dictionary tables, while MariaDB builds I_S views dynamically; metadata-heavy queries against I_S can have different performance characteristics, so don't assume MySQL 8.0 timings carry over.

## Optimizer Differences

MariaDB and MySQL use different query optimizers with different cost models. Identical SQL can produce different execution plans. After migration:

- Re-run `EXPLAIN` on critical queries — do not assume execution plans transfer
- Index hints that work in MySQL may not be needed (or may differ) in MariaDB
- MariaDB's optimizer is more aggressively tunable via `optimizer_switch`

## Version Compatibility Quick Reference

| MySQL version | MariaDB equivalent | Drop-in? |
|---|---|---|
| 5.5 | 5.5 | Yes |
| 5.6 | 10.0–10.1 | Mostly |
| 5.7 | 10.2–10.4 | Limited |
| 8.0 | 10.5+ | No — significant differences |

## Sources

- [MariaDB vs MySQL Compatibility — MariaDB Docs](https://mariadb.com/docs/release-notes/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility)
- [Moving from MySQL to MariaDB — MariaDB Docs](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/)
- [MDEV-28906 — MySQL 8.0 desired compatibility (Jira epic)](https://jira.mariadb.org/browse/MDEV-28906) — tracks MySQL 8.0 compatibility work; check individual sub-task status before assuming an item is still missing — closed sub-tasks mean the feature has been implemented
- [RETURNING — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning)
- [CREATE SEQUENCE — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-structure/sequences/create-sequence)
- [System-Versioned Tables — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/system-versioned-tables)
- [Authentication Plugins — MariaDB Docs](https://mariadb.com/docs/server/reference/plugins/authentication-plugins)

*For topics not covered here, see the official MariaDB documentation at [mariadb.com/docs](https://mariadb.com/docs).*
