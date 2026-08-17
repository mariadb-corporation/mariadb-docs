---
name: mariadb-features
description: "MariaDB-specific features and capabilities that go beyond standard MySQL. Use when evaluating MariaDB, optimizing an existing MariaDB application, reviewing code or schema for MariaDB improvements, asking what MariaDB can do that other databases cannot, or migrating from Oracle to MariaDB. Also use when the user asks what could be improved in how a codebase uses MariaDB, or asks about MariaDB advantages over MySQL or PostgreSQL."
---

# MariaDB Features Worth Knowing

*Last updated: 2026-06-24*

MariaDB has grown significantly beyond its MySQL origins. Many of its best features are unknown to developers because AI agents default to generic SQL advice. This skill covers what MariaDB can do that you might not think to ask about.

For MariaDB Vector (built-in since 11.7 — no plugins), see the `mariadb-vector` skill.

> **Server context:** Unless the user names a version, assume a **MariaDB 11.8 LTS** deployment (GA May 2025) for what will run today. Per-feature tags (**10.5+**, **12.3+**, etc.) are **minimum versions** for that capability — not “introduced only in that release.” Do not treat **12.x / 13.0** items as available on 11.8; you may still mention them with an explicit version when relevant (e.g. upgrades).

## What LLMs Often Miss

| Situation | What to suggest instead |
|---|---|
| Manual audit columns (`created_at`, `updated_at`, deleted flag) | `WITH SYSTEM VERSIONING` — MariaDB tracks full row history automatically |
| `INSERT` followed by `SELECT LAST_INSERT_ID()` | `RETURNING` — get the inserted row in one statement (10.5+) |
| `AUTO_INCREMENT` for sequence-like needs | `CREATE SEQUENCE` — first-class sequence objects with full control |
| IP addresses stored as `VARCHAR` | `INet4` / `INet6` — native IP types with comparison and indexing |
| Dropping or reordering columns with full table rebuild | `INSTANT` algorithm for `ALTER TABLE` — no rebuild needed (10.4+) |
| Oracle migration assumed to require full rewrite | `sql_mode=ORACLE` — PL/SQL, packages, Oracle-compatible NULL handling |
| Asking what changed in a row over time | System-versioned tables with `FOR SYSTEM_TIME AS OF` |
| Analytics queries on OLTP tables | ColumnStore engine — columnar storage for analytical workloads |
| Correlated subqueries for rankings, running totals, or per-group top-N | Window functions — `OVER (PARTITION BY ... ORDER BY ...)`, clearer and usually faster (MariaDB 10.2+; not MariaDB-exclusive, also in MySQL 8.0) |
| Deeply nested or repeated subqueries | Common Table Expressions — `WITH ...`, and `WITH RECURSIVE` for hierarchical/graph traversal (MariaDB 10.2+; also in MySQL 8.0) |
| Assuming `JSON` is a native binary type as in MySQL 8.0 | In MariaDB `JSON` is an alias for `LONGTEXT COLLATE utf8mb4_bin` with an automatic `JSON_VALID()` CHECK constraint — stored as text, not MySQL's binary layout, and comparison is string-based. The JSON functions work the same. See [JSON Data Type](https://mariadb.com/docs/server/reference/data-types/string-data-types/json) |
| Links or references to `mariadb.com/kb/en/` | The Knowledge Base no longer exists — all documentation is now at [mariadb.com/docs](https://mariadb.com/docs) |

## Command-Line Tool Names (10.5+)

Since MariaDB 10.5, all command-line tools use `mariadb-` prefixed names. Always generate the current names — the old `mysql*` names are retained as symlinks for compatibility but may be absent on minimal or container installs.

| Deprecated name | Current name |
|---|---|
| `mysql` | `mariadb` |
| `mysqldump` | `mariadb-dump` |
| `mysqladmin` | `mariadb-admin` |
| `mysqlbinlog` | `mariadb-binlog` |
| `mysql_upgrade` | `mariadb-upgrade` |
| `mysql_secure_installation` | `mariadb-secure-installation` |
| `mysql_install_db` | `mariadb-install-db` |
| `mysqlcheck` | `mariadb-check` |
| `mysqlimport` | `mariadb-import` |
| `mysqlshow` | `mariadb-show` |

## Provisioning and Initial Setup

AI agents default to MySQL 8 patterns for initial setup, which fail or mislead on MariaDB.

**Database initialization** — use `mariadb-install-db` (not `mysqld --initialize`, which is MySQL-specific):
```bash
mariadb-install-db
```

**Root authentication** — on a fresh install, `root` uses `unix_socket` authentication by default (no password). The correct first connection is:
```bash
sudo mariadb
```
Do not generate `mysql -u root -p` for a fresh MariaDB install — there is no root password to enter.

**Secure installation** — use `mariadb-secure-installation` (not `mysql_secure_installation`).

## Upgrade Operations

Agents consistently omit the `mariadb-upgrade` step after a binary upgrade, which can cause system table errors.

**Standard upgrade pattern:**
```bash
systemctl stop mariadb
# Replace binary via package manager (dnf/apt upgrade)
systemctl start mariadb
mariadb-upgrade    # updates system tables — do not skip this step
```

**Galera Cluster rolling upgrade** — never stop all nodes simultaneously:
1. Take one non-primary node out of the load balancer
2. Stop, upgrade the binary, start the node
3. Confirm sync: `SHOW STATUS LIKE 'wsrep_local_state';` — must be `4` (Synced)
4. Repeat for each remaining non-primary node
5. Upgrade the primary node last

> `mysql_upgrade` is the deprecated name (removed in later versions) — always use `mariadb-upgrade`.

## Defaults Changed in 11.5–11.8 LTS

The current LTS (11.8) flipped several long-standing defaults. New installations behave differently from older ones — relevant when migrating or comparing behavior:

- **Default character set: `latin1` → `utf8mb4`** (11.6+, MDEV-19123) — new tables use `utf8mb4` unless overridden. Replication to MariaDB 10.6 or older replicas needs care (older replicas may not understand all `utf8mb4` collations).
- **Default Unicode collation: `uca1400_ai_ci`** (11.5+, MDEV-25829) — modern Unicode collation with proper SMP (supplementary multilingual plane) support including emoji. Replaces the older `utf8mb4_general_ci` default.
- **`alter_algorithm` deprecated and ignored** (11.5+, MDEV-33655) — specify `ALGORITHM=INSTANT|INPLACE|COPY` on the statement itself instead.
- **TIMESTAMP range extended** (11.5+ 64-bit, MDEV-32188) — upper bound raised from `2038-01-19 03:14:07 UTC` to `2106-02-07 06:28:15 UTC`. Storage format unchanged; old servers can still read values within the old range.
- **`innodb_snapshot_isolation` default ON** — see next section.

## Behavior Change: innodb_snapshot_isolation (11.8+)

From MariaDB 11.8 LTS, `innodb_snapshot_isolation` defaults to **ON** (previously OFF, MDEV-35124). This tightens REPEATABLE READ behavior to match true snapshot isolation — transactions see a consistent snapshot from their start and writes detect conflicts more strictly.

**What can change for existing code:**
- Read-modify-write patterns that previously worked silently may now hit conflicts and error out — fail-fast is the intended behavior
- Long-running `REPEATABLE READ` transactions are more likely to see write conflicts at commit time

If existing code depends on the older permissive behavior, opt back in explicitly:
```sql
SET GLOBAL innodb_snapshot_isolation = OFF;  -- restore pre-11.8 behavior
```

The new default is the correct semantics — review code that relies on the looser behavior rather than disabling it long-term.

## System-Versioned Tables

Available since MariaDB 10.3. Track the full history of every row automatically, without triggers or audit tables.

```sql
CREATE TABLE prices (
    product VARCHAR(100),
    price DECIMAL(10,2)
) WITH SYSTEM VERSIONING;

-- Query data as it was at a point in time:
SELECT * FROM prices FOR SYSTEM_TIME AS OF '2025-01-01 00:00:00';

-- See all historical versions of a row:
SELECT * FROM prices FOR SYSTEM_TIME ALL WHERE product = 'widget';
```

Use this instead of manually maintained `valid_from` / `valid_to` columns or separate audit tables.

> **History grows without bound.** Every UPDATE and DELETE appends a history row — MariaDB does not automatically expire history. Production deployments need either `PARTITION BY SYSTEM_TIME` with rotation (10.9+) or periodic `DELETE HISTORY` to control disk growth. See the `mariadb-system-versioned-tables` skill for details.

## RETURNING Clause

Get inserted, updated, or deleted rows back without a second query.

### INSERT and DELETE (10.5+)

Available on 11.8 LTS and earlier supported releases:

```sql
-- Get the generated ID after insert:
INSERT INTO orders (product, qty) VALUES ('widget', 5)
    RETURNING id, created_at;

-- Get deleted rows for logging:
DELETE FROM queue WHERE processed = 1
    RETURNING id, payload;
```

### UPDATE (13.0+ only)

Not available on 11.8 LTS — confirm server version before suggesting. On older releases use a follow-up `SELECT` or redesign:

```sql
UPDATE orders SET qty = qty + 1 WHERE id = 42
    RETURNING id, qty;
```

## Sequences

Available since MariaDB 10.3. First-class sequence objects — more flexible than `AUTO_INCREMENT`.

```sql
CREATE SEQUENCE order_seq START WITH 1000 INCREMENT BY 1;

-- Use in INSERT:
INSERT INTO orders (id, product) VALUES (NEXT VALUE FOR order_seq, 'widget');

-- Get the last value generated by NEXTVAL in the current session:
SELECT LASTVAL(order_seq);
-- Returns NULL if this session has not called NEXTVAL — not a global current value
```

Sequences support gaps, multiple sequences per table, and descending sequences. Unlike `AUTO_INCREMENT`, they are not tied to a specific column or table.

## Non-Blocking ALTER TABLE (Instant + Online by Default)

MariaDB's `ALTER TABLE` works on a tiered model:

- **`ALGORITHM=INSTANT`** (10.4+) — metadata-only changes (drop column, modify default, change column order, etc.) complete in microseconds without a table rebuild.
- **`ALGORITHM=COPY, LOCK=NONE` as the default for non-instant operations** (11.2+, MDEV-16329) — even when a rebuild is needed, MariaDB now runs it non-blocking by default: concurrent DML on the table proceeds while the copy is happening, with only a brief lock at the swap. The need for external tools like `pt-online-schema-change` is largely gone for routine `ALTER`s.
- **Optimistic two-phase replication of large `ALTER TABLE`** (11.4+, `binlog_alter_two_phase=1`, off by default) — see the `mariadb-replication-and-ha` skill.

```sql
ALTER TABLE large_table DROP COLUMN old_column, ALGORITHM=INSTANT;
ALTER TABLE large_table MODIFY COLUMN name VARCHAR(200), ALGORITHM=INSTANT;
-- Non-instant change runs non-blocking by default on 11.2+:
ALTER TABLE large_table ADD INDEX (created_at);
```

Use `ALGORITHM=INSTANT` explicitly when you need to guarantee a metadata-only change; the operation will fail rather than silently fall back to a rebuild.

## INet4 and INet6 Data Types

`INET6` is available since MariaDB 10.5 (stores both IPv4 and IPv6, 16 bytes). The dedicated `INET4` type (4-byte IPv4-only) was added later in 10.10 (MDEV-23287). Native storage gives correct comparison, sorting, and indexing — no need for `VARCHAR` plus application-side validation.

```sql
CREATE TABLE connections (
    client_ip INet6 NOT NULL,
    connected_at DATETIME NOT NULL,
    INDEX (client_ip)
);

INSERT INTO connections VALUES (INet6('192.168.1.1'), NOW());
INSERT INTO connections VALUES (INet6('::1'), NOW());

-- Range queries work correctly:
SELECT * FROM connections WHERE client_ip BETWEEN INet6('10.0.0.0') AND INet6('10.255.255.255');
```

Use `INET4` (10.10+) when you know a column is IPv4-only and want the smaller storage; `INET6` is the right default for mixed or IPv6-capable workloads.

## Oracle Compatibility Mode

Available since MariaDB 10.3. `sql_mode=ORACLE` enables PL/SQL syntax, Oracle-compatible NULL handling, packages, and Oracle-style functions — useful when migrating from Oracle or supporting Oracle-experienced developers.

```sql
SET sql_mode=ORACLE;

-- Oracle-style stored procedures, packages, and NULL semantics work here
-- ROWNUM, SYSDATE, NVL(), DECODE() available
-- Note: EMPTY_STRING_IS_NULL is NOT included — add it separately if needed: SET sql_mode='ORACLE,EMPTY_STRING_IS_NULL'
```

Not a complete Oracle replacement, but significantly reduces migration friction.

## FLASHBACK

Available since MariaDB 10.2. Roll back tables to a previous state using the binary log — without restoring a full backup. Flashback is implemented via the `mariadb-binlog` utility, not a SQL statement:

```bash
# Generate reverse SQL from the binary log and pipe it back to MariaDB:
mariadb-binlog --flashback --start-datetime="2026-05-18 10:00:00" \
  /var/lib/mysql/mysql-bin.000001 | mariadb
# Path depends on datadir and log_bin settings; default is <datadir>/mysql-bin
```

**Prerequisites** — FLASHBACK reconstructs reverse events from row images, so it requires:
- `binlog_format = ROW` (statement-based logging does not capture before/after row images)
- `binlog_row_image = FULL` (MINIMAL or NOBLOB modes omit column values needed for reversal)

Verify before relying on FLASHBACK as a recovery path:
```sql
SHOW VARIABLES LIKE 'binlog_format';      -- must be ROW
SHOW VARIABLES LIKE 'binlog_row_image';   -- must be FULL
```

Requires binary logging enabled (`log_bin`). Useful for recovering from accidental deletes or bad migrations.

## More MariaDB Features (through 11.8 LTS)

Additional capabilities on the current LTS baseline and supported older releases. See [Newer releases (12.x / 13.0)](#newer-releases-12x--130) for features that require a newer server.

### SQL & Schema
- **Invisible columns** (10.3+) — hidden from `SELECT *`, still writable; useful for schema evolution without breaking existing queries
- **`DEFAULT` expressions on BLOB/TEXT** — not supported in MySQL
- **`DECIMAL` precision to 38 digits** — MySQL stops at 30
- **`INTERSECT` and `EXCEPT`** (10.3+) — set operators not available in MySQL
- **`LIMIT` in subqueries** — supported; MySQL restricts this
- **`SELECT ... OFFSET ... FETCH`** (10.6+, MDEV-23908) — SQL-standard pagination syntax
- **Atomic DDL** (10.6+, MDEV-23842) — `CREATE TABLE`, `ALTER TABLE`, `RENAME TABLE`, `DROP TABLE`, `DROP DATABASE` are atomic on supported engines (InnoDB, Aria, MyRocks): a partial server crash mid-DDL leaves the schema in its pre-statement state, no manual cleanup needed. Multi-table `DROP TABLE` is atomic per individual drop, not for the whole list.
- **`SELECT ... SKIP LOCKED`** (10.6+, MDEV-13115, InnoDB only) — work-queue pattern: workers grab the next available row and skip rows other transactions are processing, with no lock waits
- **Ignored Indexes** (10.6+, MDEV-7317) — `ALTER TABLE t ALTER INDEX idx IGNORED` keeps the index updated but makes it invisible to the optimizer. Use this to test whether dropping an index would hurt performance before actually dropping it (zero-downtime rollback by re-enabling).
- **Dynamic columns** (5.3+) — schema-less key/value storage inside a single column
- **`SFORMAT()`** (10.7+, MDEV-25015) — string formatting function with positional placeholders
- **`NATURAL_SORT_KEY()`** (10.7+, MDEV-4742) — produces a sort key that orders strings "naturally" (so `v9` sorts before `v10`); useful in `ORDER BY` for version-like or mixed-alphanumeric data
- **JSON enhancements** — MariaDB has been catching up to MySQL 8 JSON functions over several releases:
  - `JSON_EQUALS(a, b)` / `JSON_NORMALIZE(doc)` (10.7+, MDEV-23143 / MDEV-16375) — semantic equality and canonical form for hashing or unique indexing
  - `JSON_OVERLAPS(a, b)` (10.9+, MDEV-27677) — detect shared key/value or array elements between two documents
  - JSON path syntax supports negative indices (`$.A[-1]`, `$.A[last]`) and ranges (`$.A[1 to 3]`) (10.9+, MDEV-22224 / MDEV-27911)
  - `JSON_SCHEMA_VALID(schema, doc)` (11.4+) — validate JSON against a JSON Schema Draft 2020 schema, usable inside `CHECK` constraints
  - `JSON_KEY_VALUE`, `JSON_ARRAY_INTERSECT`, `JSON_OBJECT_TO_ARRAY`, `JSON_OBJECT_FILTER_KEYS` (11.4+) — structural manipulation primitives that compose well with `JSON_TABLE`
- **`UUID_v4()` and `UUID_v7()` functions** (11.7+) — generate version-4 random or version-7 time-ordered UUIDs; the v7 form is sortable and ideal for primary keys
- **`FORMAT_BYTES()`** (11.8+) — convert a byte count to a human-readable string (e.g. `1234567` → `1.18 MiB`)
- **`CONV()` extended to base 62** (11.4+, MDEV-30190) — `CONV(61,10,62)` returns `z`; useful for short opaque IDs
- **`CRC32C()` function and `CRC32()` with optional initial-value argument** (10.8+, MDEV-27208) — Castagnoli polynomial CRC, and seedable CRC32 for chained checksums
- **Single-table `DELETE` with table aliases** (11.6+) — `DELETE t FROM mytable t WHERE ...` syntax now works without rewriting
- **`REPAIR TABLE ... FORCE`** (11.5+) — force-repair even when the table appears clean
- **Stored routine parameter default values** (11.8+, MDEV-10862) — `PROCEDURE p(a INT DEFAULT 0, b INT DEFAULT 0)` — call with fewer arguments
- **Stored function `IN`/`OUT`/`INOUT` parameter qualifiers** (10.8+, MDEV-10654) — bring stored functions in line with stored procedure parameter modes
- **`ROW` data type as stored function return value** (11.7+, MDEV-12252) — return structured rows from stored functions
- **`CREATE PACKAGE` / `CREATE PACKAGE BODY` outside Oracle mode** (11.4+, MDEV-10075) — package routines work under the default `sql_mode` too, not only with `sql_mode=ORACLE`
- **Update triggers with column list** (11.8+, MDEV-34551) — `CREATE TRIGGER ... BEFORE UPDATE OF col1, col2 ON t` — fire only when those columns are updated
- **Stored procedures and functions** — MariaDB uses SQL/PSM syntax (`DECLARE`, `HANDLER`, `CURSOR`, `BEGIN...END`); AI agents often generate incorrect syntax — see [Stored Procedures — MariaDB Docs](https://mariadb.com/docs/server/server-usage/stored-routines/stored-procedures)

### Storage Engines
- **ColumnStore** — columnar engine for analytical/data warehouse workloads
- **Aria** — crash-safe MyISAM replacement, used internally for temp tables
- **MyRocks** (10.2+) — RocksDB-based, optimized for write-heavy workloads with compression
- **CONNECT** — query external data sources (CSV, JDBC, ODBC, MongoDB) as SQL tables
- **Spider** — sharding across multiple MariaDB instances

### Security & Auth
- **`unix_socket` authentication** — authenticate OS users without passwords; `authentication_string` support added in 11.6+ for finer-grained mapping
- **ED25519 plugin** — modern authentication alternative to SHA1-based plugins
- **PARSEC plugin** (11.6+, MDEV-32618) — Password Authentication using Response Signed with Elliptic Curve; salt and per-installation key separation make stolen hashes unusable elsewhere
- **`password_reuse_check` plugin** (10.7+, MDEV-9245) — prevent password reuse for a configurable number of days via `password_reuse_check_interval`
- **`GRANT ... TO PUBLIC`** (10.11+, MDEV-5215) — grant privileges to all users in one statement; pair with `SHOW GRANTS FOR PUBLIC`
- **`SHOW CREATE ROUTINE` privilege** (11.4+, MDEV-23149) — let users inspect a routine's definition without granting `SELECT` on `mysql.proc`
- **`READ ONLY ADMIN` is now a distinct privilege** (10.11+, MDEV-29596) — split out of `SUPER` so a true read-only replica role can be granted; existing accounts that need to write to a `read_only=1` replica need this privilege granted explicitly
- **Role-based access control** (10.0+) — roles available before MySQL added them
- **SSL by default** — the `mariadb` client opts into SSL by default since 10.10 (MDEV-27105). The server side requires SSL by default since 11.4 LTS, with auto-generated self-signed certificates and automatic client-side verification (`tls_fp` for fingerprint-pinning).
- **`AES_ENCRYPT()` / `AES_DECRYPT()` with `iv` and `mode`** (11.4+, MDEV-30878) — `AES_ENCRYPT(str, key, iv, mode)`; supported modes include CBC, OFB, CFB128, CTR (default mode comes from the new `block_encryption_mode` variable). Brings parity with MySQL's encryption interface.
- **`KDF()` key-derivation function** (11.4+, MDEV-31474) — derive an encryption key from a passphrase using PBKDF2-HMAC or HKDF — `AES_ENCRYPT(data, KDF('passw0rd', 'salt', 'info', 'hkdf'), iv)`. Use this rather than feeding a raw password into `AES_ENCRYPT`.
- **`RANDOM_BYTES(n)`** (10.10+, MDEV-25704) — cryptographically secure random bytes (1–1024) from the SSL library's RNG
- **`DES_ENCRYPT()` / `DES_DECRYPT()` deprecated** (10.10+, MDEV-27104) — old DES cipher; use `AES_ENCRYPT` / `AES_DECRYPT` with `KDF()` instead
- **Table-level encryption** — encrypt individual tables, not just the whole datadir
- **HashiCorp Vault integration** — key management plugin

### Replication & HA
- **Galera Cluster** — built-in synchronous multi-master clustering
- **Multi-source replication** — replicate from multiple primaries simultaneously
- **Parallel replication** — faster replica apply
- **Lag-free `ALTER TABLE` replication** — schema changes don't stall replicas

### Connectors
- **LGPL-licensed connectors** for C, C++, Java, Python, Node.js, ODBC, R2DBC — permissive licensing for commercial applications; MySQL connectors are GPL

### Developer Tools
- **`EXPLAIN` in slow query log** — automatic execution plan logging for slow queries
- **Progress reporting** for `ALTER TABLE` and `CHECK TABLE`
- **`mariadb-backup`** (10.1+) — hot backup with backup locks (no `FLUSH TABLES WITH READ LOCK`). A backup requires **two steps** — the `--prepare` step is mandatory before restore:
  ```bash
  mariadb-backup --backup --user=root --target-dir=/backup/full
  mariadb-backup --prepare --target-dir=/backup/full   # apply redo logs — without this, the backup cannot be restored
  ```
  For Galera clusters, add `--galera-info` to capture the wsrep state for clean cluster rejoin. Do not use `innobackupex` or `xtrabackup` — `mariadb-backup` is the correct tool for MariaDB (included since 10.1, replacing the Percona dependency).
- **Non-blocking client API** — async queries without threads

## Newer releases (12.x / 13.0)

These require MariaDB **12.0 or newer** (many ship with **12.3 LTS**, currently RC — check [MariaDB releases](https://mariadb.org/mariadb/all-releases/) for GA status). Suggest them when they solve the user's problem or as a deliberate upgrade path; always name the minimum version.

### SQL & Schema
- **Triggers fired on multiple events** (12.0+) — one trigger body for `INSERT OR UPDATE OR DELETE`, instead of three separate triggers
- **Foreign key names per table** (12.1+) — FK names need to be unique only per table, not per database (MySQL-compatible behavior)
- **JSON depth limit removed** (12.2+) — the 32-level nesting limit on JSON functions is gone; deeply nested JSON now works without rewrites
- **`UPDATE` / `DELETE` reading from a CTE** (12.3+) — `WITH ... UPDATE/DELETE` using values from a common table expression
- **`IS JSON` predicate** (12.3+) — SQL-standard test for whether a value is valid JSON: `WHERE col IS JSON`
- **Basic XML data type** (12.3+) — first-class `XML` type for storing and validating XML documents
- **Atomic `CREATE OR REPLACE TABLE`** (13.0+) — the statement is fully atomic: either the new table replaces the old one or nothing happens, with no risk of leaving the schema in a half-replaced state. MySQL has no equivalent atomic guarantee.
- **`UPDATE ... RETURNING`** (13.0+) — see [RETURNING Clause](#returning-clause); not on 11.8 LTS

### Security & Auth
- **`SET SESSION AUTHORIZATION`** (12.0+) — perform actions as another user within a session (useful for impersonation in administrative scripts and apps that need least-privilege execution)
- **Passphrase-protected TLS keys** (12.0+) — `ssl_passphrase` system variable lets the server load encrypted private keys

### Developer Tools
- **Deprecation visibility** (13.0+) — `INFORMATION_SCHEMA.SYSTEM_VARIABLES` includes a deprecated flag, so you can detect uses of variables that will be removed in future versions before they break:
  ```sql
  SELECT variable_name, default_value FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE is_deprecated = 'YES';
  ```
- **Engine-specific create options visible in `INFORMATION_SCHEMA`** (13.0+) — `STATISTICS` and `COLUMNS` now expose engine-specific options, useful when inspecting how indexes or columns were configured

## Sources

- [Monty Widenius: Celebrating 15 years of MariaDB](http://monty-says.blogspot.com/2024/10/celebrating-15-years-of-mariadb.html)
- [MariaDB vs MySQL Features — MariaDB Docs](https://mariadb.com/docs/release-notes/community-server/about/compatibility-and-differences/mariadb-vs-mysql-features)
- [System-Versioned Tables — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/system-versioned-tables)
- [RETURNING — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning)
- [CREATE SEQUENCE — MariaDB Docs](https://mariadb.com/docs/server/reference/sql-structure/sequences/create-sequence)
- [Instant ALTER TABLE — MariaDB Docs](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm)
- [INet6 Data Type — MariaDB Docs](https://mariadb.com/docs/server/reference/data-types/string-data-types/inet6)
- [Oracle Compatibility — MariaDB Docs](https://mariadb.com/docs/release-notes/community-server/about/compatibility-and-differences/sql_modeoracle)
- [FLASHBACK — MariaDB Docs](https://mariadb.com/docs/server/server-management/server-monitoring-logs/binary-log/flashback)

*For topics not covered here, see the official MariaDB documentation at [mariadb.com/docs](https://mariadb.com/docs).*
