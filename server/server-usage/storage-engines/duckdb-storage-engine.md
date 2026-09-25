---
description: >-
  DuckDB embedded in MariaDB Server as a storage engine, giving columnar,
  vectorized analytical query execution next to your transactional tables.
---

# DuckDB Storage Engine

{% hint style="info" %}
The DuckDB storage engine is at **gamma** maturity and ships as a separate plugin package. It is available from MariaDB 11.4.13, 11.8.9, 12.3.3, 13.0.2, and 13.1.1.
{% endhint %}

The DuckDB storage engine embeds [DuckDB](https://duckdb.org/) — a columnar, vectorized, in-process analytical engine — inside MariaDB Server as a loadable plugin (`ha_duckdb.so`). Tables created with `ENGINE=DuckDB` store their data in DuckDB's own columnar format, and queries against them are executed by DuckDB. A single `SELECT` can join a `DuckDB` table with an `InnoDB` table, so analytical and transactional data live in one server, behind one SQL interface and one client protocol.

MariaDB Server keeps ownership of metadata, parsing, privileges, and the client protocol. DuckDB owns data storage, analytical execution, and its own MVCC transactions.

The engine draws on Alibaba's [AliSQL](https://github.com/alibaba/AliSQL) DuckDB integration, rewritten against MariaDB's handler API and plugin system, and links against upstream DuckDB v1.5.5.

## Use Cases

* **Hybrid transactional and analytical processing** — InnoDB serves the transactional workload, DuckDB serves analytics, in the same server.
* **Ad hoc analytical queries** — joins, aggregations, and window functions over large data sets without exporting to a separate system.
* **Removing ETL steps** — the analytical engine runs in process, so there is no separate cluster and no data movement pipeline.

## Availability and Requirements

The plugin is built only for 64-bit Linux on `x86_64` and `aarch64`, and requires a C++17 compiler (GCC 12 or later) to build.

Packages are published in the MariaDB repositories for:

* **RPM** — RHEL, Rocky Linux, AlmaLinux, and CentOS 8, 9, and 10.
* **DEB** — Debian 11, 12, and 13; Ubuntu 22.04, 24.04, and 26.04.

Both architectures are packaged for every supported version. There is no Windows, macOS, or 32-bit build.

## Installing

The engine is not part of the `mariadb-server` package. Configure the [MariaDB repository](../../server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage.md) for your release, then install the plugin package.

{% tabs %}
{% tab title="Debian, Ubuntu" %}
```sh
sudo apt update
sudo apt install mariadb-plugin-duckdb
sudo systemctl restart mariadb
```

The package installs `/etc/mysql/mariadb.conf.d/duckdb.cnf`, which loads the plugin at startup.
{% endtab %}

{% tab title="RHEL, Rocky, AlmaLinux" %}
```sh
sudo dnf install MariaDB-duckdb-engine
sudo systemctl restart mariadb
```

The package installs `/etc/my.cnf.d/duckdb.cnf`, which loads the plugin at startup.
{% endtab %}
{% endtabs %}

The plugin package requires the `mariadb-server` package of exactly the same version.

### Verifying the Installation

```sql
SHOW ENGINES;
```

The output includes a `DUCKDB` row with `Support` set to `YES`. The embedded DuckDB version is reported as a status variable:

```sql
SHOW STATUS LIKE 'Duckdb_version';
```

Because the engine is at gamma maturity and release servers are at stable maturity, the error log records one warning at load time:

```
Plugin 'DUCKDB' is of maturity level gamma while the server is stable
```

The plugin still loads: the default value of [`plugin_maturity`](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity) is one level below the server's own maturity, so no `plugin-maturity` setting is needed. Setting `plugin_maturity` to `stable` prevents the engine from loading.

### First Table

```sql
CREATE DATABASE analytics;
USE analytics;

CREATE TABLE orders (
  id BIGINT NOT NULL AUTO_INCREMENT,
  amount DECIMAL(15,2),
  created_at DATETIME,
  PRIMARY KEY (id)
) ENGINE=DuckDB DEFAULT CHARSET=utf8mb4;

INSERT INTO orders (amount, created_at) VALUES (199.99, NOW()), (299.50, NOW());

SELECT SUM(amount) FROM orders;
```

Two defaults shape that statement:

* `duckdb_require_primary_key` is `ON`, so a DuckDB table needs a primary key.
* DuckDB stores all strings as UTF-8, so columns must use `utf8mb4`, `utf8mb3`, `utf8`, or `ascii`. Other character sets are rejected at DDL time.

## How Queries Are Executed

The engine adds a `select_handler`, so a `SELECT` that touches a DuckDB table is handed to DuckDB whole rather than being executed row by row. Before sending the statement, the engine rewrites MariaDB-specific syntax — `GROUP BY ... WITH ROLLUP`, `CONVERT()`, `STRAIGHT_JOIN`, `REGEXP`, `RLIKE`, `LIMIT offset, count` — into DuckDB equivalents, and strips optimizer hints such as `FORCE INDEX` and `SQL_NO_CACHE`. DuckDB's optimizer then chooses join order and drives hashing, aggregation, and sorting.

Pushdown is declined for statements MariaDB marks as having side effects — user variable reads and assignments, system variable reads, `LAST_INSERT_ID()`, `BENCHMARK()`, `SLEEP()`, `LOAD_FILE()`, locking functions, `SELECT ... INTO`, and the `PROCEDURE` clause. Those statements fall back to a row-by-row table scan.

`UPDATE` and `DELETE` on a single table with a simple `WHERE` clause are also pushed down as whole statements.

### Cross-Engine Queries

When one `SELECT` mixes engines, the entire query still goes to DuckDB. DuckDB cannot find the non-DuckDB tables in its catalog, so a replacement scan callback redirects them back into MariaDB Server: a cooperative fiber on a background connection runs a synthetic `SELECT` of only the needed columns, with the relevant part of the `WHERE` clause applied, and streams the rows into DuckDB in vector-sized batches.

```sql
SELECT d.id, d.amount, i.name
  FROM analytics.orders d      -- ENGINE=DuckDB
  JOIN inventory.products i    -- ENGINE=InnoDB
    ON d.product_id = i.id
 WHERE d.amount > 1000;
```

Because the external scan runs through the full server pipeline, the MariaDB optimizer picks the access path for the InnoDB side, including index access and index condition pushdown. Only the DuckDB side of the query is parallelized; each external table is produced by a single fiber.

The fiber runs in its own transaction, so uncommitted changes made by the current session in other engines are not visible to it. Set the session variable `duckdb_cross_engine_ryow` to `ON` to read your own writes instead: external tables are then read directly through the parent transaction, at the cost of losing index access and index condition pushdown for those tables.

## Supported Operations

* **DDL** — `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`, `RENAME TABLE`, `TRUNCATE`, and `DROP DATABASE`. `ALTER TABLE ... ENGINE=DuckDB` converts an existing table.
* **`INSERT`, `UPDATE`, `DELETE`** — translated to DuckDB SQL, either per row or in batches.
* **`SELECT`** — pushed down whole, including aggregations, joins, window functions, common table expressions, `UNION`, `EXCEPT`, and `INTERSECT`.
* **`AUTO_INCREMENT`** — supported in `CREATE TABLE`, backed by a DuckDB sequence named `mdb_autoinc_`*`table`*. Each statement reserves a block of `duckdb_autoinc_cache_size` values, so gaps in the sequence are normal. Adding an `AUTO_INCREMENT` column with `ALTER TABLE`, or converting a table that has one, fails with `ER_TABLE_CANT_HANDLE_AUTO_INCREMENT`.
* **Column defaults** — literal and expression defaults are forwarded to DuckDB. A default that reads a MariaDB sequence (`NEXT VALUE FOR`) is not forwarded; MariaDB Server evaluates it and supplies the value, and the statement raises a note.
* **`run_in_duckdb()`** — executes a statement in DuckDB directly. See [Running DuckDB SQL Directly](#running-duckdb-sql-directly).

Indexes are accepted in DDL but are not created in DuckDB, and the engine reports no index capabilities to the optimizer, so they give no access paths. Only the `NOT NULL` constraints that a `PRIMARY KEY` implies reach the DuckDB table.

{% hint style="warning" %}
A `PRIMARY KEY` or `UNIQUE` index on a DuckDB table is therefore **not enforced**. Two rows with the same primary key value are accepted, and a row level `UPDATE` or `DELETE`, which locates rows by the first key's columns, then affects both.
{% endhint %}

The primary key is still needed for that row lookup, which is why `duckdb_require_primary_key` defaults to `ON`.

## Data Type Mapping

| MariaDB type | DuckDB type |
| --- | --- |
| `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `BIGINT` | `TINYINT`, `SMALLINT`, `INTEGER`, `INTEGER`, `BIGINT` (`U`-prefixed when `UNSIGNED`) |
| `FLOAT`, `DOUBLE` | `FLOAT`, `DOUBLE` |
| `DECIMAL(p,s)` with *p* ≤ 38 | `DECIMAL(p,s)` |
| `DECIMAL(p,s)` with *p* > 38 | `DOUBLE`, or `DECIMAL(38,s)` when `duckdb_use_double_for_decimal` is `OFF` |
| `DATE` | `DATE` |
| `TIME` | `TIME` |
| `DATETIME` | `DATETIME` |
| `TIMESTAMP` | `TIMESTAMPTZ` |
| `YEAR` | `INTEGER` |
| `CHAR`, `VARCHAR`, `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, `LONGTEXT`, `JSON` | `VARCHAR` with a mapped collation |
| `BINARY`, `VARBINARY`, `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB` | `BLOB` |
| `ENUM`, `SET` | `VARCHAR` |
| `BIT`, `GEOMETRY` types | `BLOB` |
| `UUID` | `UUID` |

Because `TIMESTAMP` becomes `TIMESTAMPTZ`, keep the server time zone and the DuckDB session time zone consistent to avoid shifted values.

### Character Sets and Collations

Each `VARCHAR` column carries a DuckDB collation derived from its MariaDB collation:

| MariaDB collation | DuckDB collation |
| --- | --- |
| `_bin` | `POSIX` (byte comparison) |
| `_ai_ci` (accent and case insensitive) | `NOCASE.NOACCENT` |
| `_as_ci` (accent sensitive, case insensitive) | `NOCASE` |
| `_as_cs` (accent and case sensitive) | `POSIX` |

DuckDB's `NOCASE` and `NOACCENT` are simple transformations — lowercasing and stripping diacritics — not the Unicode Collation Algorithm weight tables MariaDB uses. Comparison and sort results can therefore differ from the same query on an InnoDB table, particularly for non-ASCII text: German `ß`, Turkish dotted and dotless `i`, and ligatures such as `æ` are the usual examples. `_as_cs` collations sort by UTF-8 byte value rather than by collation weight, which changes `ORDER BY` results.

Set the session variable `duckdb_force_no_collation` to `ON` to disable collation pushdown and compare as bytes.

## Transactions and Concurrency

The whole server shares one DuckDB instance and one database file, `duckdb.db`, in the data directory. Each connection gets its own DuckDB connection and transaction, with MVCC-isolated reads.

The engine takes no MariaDB table level locks, so concurrency is DuckDB's: several sessions can write at once, inserts never conflict with each other, and DuckDB's optimistic concurrency control raises a conflict error when two transactions update or delete the same row, failing the second one. The shared buffer pool means one large scan can evict pages another session is using.

Transactions are coordinated through MariaDB's transaction layer: `COMMIT` and `ROLLBACK` are passed on to DuckDB. `XA PREPARE` is rejected.

{% hint style="warning" %}
With the default `duckdb_dml_in_batch=ON`, `INSERT`, `UPDATE`, and `DELETE` statements are buffered and applied to DuckDB at commit. A write is therefore not visible to a later read in the same transaction. Set `duckdb_dml_in_batch=OFF` for read-after-write behavior inside a transaction, at a cost in write throughput.
{% endhint %}

## Running DuckDB SQL Directly

The plugin package also registers the `run_in_duckdb()` function, which sends one statement straight to the embedded DuckDB instance and returns DuckDB's rendering of the result as a string. It is the bulk load path for DuckDB's own readers:

```sql
SELECT run_in_duckdb('INSERT INTO taxi.trips
  SELECT * FROM read_parquet(''/data/yellow_tripdata_2024-01.parquet'')');
```

The file is read inside the server process, so the path must be readable by the operating system account running `mariadbd`.

{% hint style="danger" %}
`run_in_duckdb()` runs arbitrary DuckDB SQL in process, as the server's operating system user, against the single shared DuckDB instance. DuckDB applies no access control of its own, so a caller can read and write any DuckDB table regardless of MariaDB grants, read and write local files, reach the network through auto-installable extensions, attach other databases, and change global DuckDB settings. Neither the `FILE` privilege nor `secure_file_priv` applies to this I/O.

The function is gated by two coarse checks: `duckdb_allow_run_in_duckdb` must be `ON` (it is `OFF` by default), and the caller must hold the `SUPER` privilege. Treat it as a host-level capability, leave it off unless it is needed, and do not enable it on shared or multitenant servers.
{% endhint %}

Enable it explicitly when needed:

```ini
[mysqld]
duckdb-allow-run-in-duckdb=ON
```

With the variable `OFF`, a call fails with `ER_OPTION_PREVENTS_STATEMENT`. With it `ON`, a caller without `SUPER` gets an access denied error.

## Managing the Database File

All DuckDB tables share one file, and dropping a table or deleting rows frees blocks for reuse without shrinking the file. `VACUUM` in DuckDB only refreshes statistics; it does not compact storage. `CHECKPOINT` flushes the write-ahead log and merges row groups that hold many deleted rows, which reuses space inside the file; it fails while other transactions are running, and `FORCE CHECKPOINT` waits for them. It shrinks the file only when the free blocks form a contiguous run at its end, which is rarely true on a busy server.

To check space use:

```sql
SELECT run_in_duckdb('SELECT * FROM pragma_database_size()');
```

The reliable way to reclaim space is to export the database, remove the file, and import it again:

```sql
SELECT run_in_duckdb('EXPORT DATABASE ''/var/tmp/duckdb_export'' (FORMAT PARQUET)');
```

Then stop the server, delete `duckdb.db` from the data directory, start the server, and import:

```sql
SELECT run_in_duckdb('IMPORT DATABASE ''/var/tmp/duckdb_export''');
```

`duckdb_checkpoint_threshold` controls how large the write-ahead log grows before an automatic checkpoint runs.

## System Variables

The plugin adds the following variables. Scope `Global` variables are set for the whole server; `Session` variables can be changed per connection. Two variables are read only and can be set only at startup.

| Variable | Scope | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `duckdb_memory_limit` | Global | Bytes | `0` | Memory DuckDB may use. `0` sizes it automatically as 80% of physical memory minus `innodb_buffer_pool_size_max`, with a 1 GB floor. |
| `duckdb_max_threads` | Global | Integer | `0` | DuckDB execution threads. `0` uses DuckDB's own default. |
| `duckdb_temp_directory` | Global, read only | String | `duckdb_tmp` in the data directory | Directory DuckDB spills to. DuckDB can only enforce its memory limit if it has spill space. |
| `duckdb_max_temp_directory_size` | Global | Bytes | `0` | Cap on spill space. `0` means 90% of the space available. |
| `duckdb_checkpoint_threshold` | Global | Bytes | `268435456` (256 MB) | Write-ahead log size that triggers an automatic checkpoint. |
| `duckdb_require_primary_key` | Global | Boolean | `ON` | Reject `CREATE TABLE` and `ALTER TABLE` without a primary key. |
| `duckdb_use_double_for_decimal` | Global | Boolean | `ON` | Store `DECIMAL` with precision above 38 as `DOUBLE` instead of clamping to `DECIMAL(38,s)`. |
| `duckdb_dml_in_batch` | Global | Boolean | `ON` | Buffer `INSERT`, `UPDATE`, and `DELETE` and apply them at commit. |
| `duckdb_copy_ddl_in_batch` | Global | Boolean | `ON` | Use batch inserts when a DDL statement copies a table. |
| `duckdb_update_modified_column_only` | Global | Boolean | `ON` | Send only changed columns in an `UPDATE`. |
| `duckdb_autoinc_cache_size` | Global | Integer | `1000` | `AUTO_INCREMENT` values reserved from the backing sequence per statement. |
| `duckdb_appender_allocator_flush_threshold` | Global | Bytes | `67108864` (64 MB) | Batch memory at which the appender allocator is flushed. |
| `duckdb_scheduler_process_partial` | Global | Boolean | `ON` | Process tasks partially before rescheduling them. |
| `duckdb_use_direct_io` | Global, read only | Boolean | `OFF` | Use direct I/O for DuckDB data files. |
| `duckdb_allow_run_in_duckdb` | Global | Boolean | `OFF` | Allow `run_in_duckdb()`, which also requires `SUPER`. |
| `duckdb_log_options` | Global | Set | empty | What to write to the error log: `DUCKDB_QUERY`, `DUCKDB_QUERY_RESULT`. |
| `duckdb_cross_engine_ryow` | Session | Boolean | `OFF` | Read your own uncommitted writes from non-DuckDB tables in cross-engine queries, giving up index access for them. |
| `duckdb_force_no_collation` | Session | Boolean | `OFF` | Disable collation pushdown and compare strings as bytes. |
| `duckdb_explain_output` | Session | Enum | `PHYSICAL_ONLY` | DuckDB `EXPLAIN` detail: `ALL`, `OPTIMIZED_ONLY`, or `PHYSICAL_ONLY`. |
| `duckdb_disabled_optimizers` | Session | Set | empty | DuckDB optimizer rules to disable, such as `JOIN_ORDER` or `FILTER_PUSHDOWN`. Intended for diagnosis. |
| `duckdb_merge_join_threshold` | Session | Integer | `4611686018427387904` | Row count above which a merge join is preferred. |

List the current values with:

```sql
SHOW VARIABLES LIKE 'duckdb%';
```

## Status Variables

| Variable | Description |
| --- | --- |
| `Duckdb_version` | Version of the embedded DuckDB library. |
| `Duckdb_rows_insert`, `Duckdb_rows_update`, `Duckdb_rows_delete` | Rows written through the per row path. |
| `Duckdb_rows_insert_in_batch`, `Duckdb_rows_update_in_batch`, `Duckdb_rows_delete_in_batch` | Rows written through the batch path. |
| `Duckdb_commit`, `Duckdb_rollback` | DuckDB transactions committed and rolled back. |

## Performance

TPC-H at scale factor 10 (about 11 GB of raw data, 86.6 million rows, 60 million of them in `lineitem`) on an Intel Core i7-13700H with 64 GB of RAM and an NVMe SSD, running MariaDB 11.4.13 with `duckdb_memory_limit=8G` and 20 threads:

| Metric | Result |
| --- | --- |
| Loading the data set with DuckDB `COPY` | 33 seconds |
| All 22 TPC-H queries, warm | 4.30 seconds |

Each query also pays a fixed cost of roughly 40 ms for connection and pushdown setup, which dominates the cheapest queries and is negligible on the heavy ones.

## Limitations

Statement and syntax limitations:

* **`PRIMARY KEY` and `UNIQUE` indexes are not enforced.** They are recorded by MariaDB but not created in DuckDB, so duplicate values are accepted.
* **Temporary tables** are not supported. `CREATE TEMPORARY TABLE ... ENGINE=DuckDB` fails with `Table storage engine 'DUCKDB' does not support the create option 'TEMPORARY'`.
* **Partitioning** is not supported, in `CREATE TABLE` or in `ALTER TABLE`.
* **`XA PREPARE`** is not supported.
* **Invisible columns** are not supported, which also rules out features built on them, such as system versioned tables.
* **Generated columns** are not supported.
* **Strict `GROUP BY`** — DuckDB rejects a selected column that is neither grouped nor aggregated, whatever `sql_mode` allows.
* **`ALTER TABLE ... ALTER COLUMN DROP DEFAULT`** is not propagated to the DuckDB catalog.

Query pushdown limitations. These matter because the pushed statement is the original SQL text, so some MariaDB-specific token meanings survive into DuckDB:

* A **double quoted string literal** is an identifier to DuckDB. `JSON_OBJECT("month", …)` fails with a binder error; use single quotes.
* An **unquoted column alias that is a DuckDB reserved word** — `SELECT expr year` — is a parser error. Write `AS year` or quote it.
* **Executable comments** (`/*! … */`, `/*M! … */`) are ordinary comments to DuckDB, so their contents are ignored rather than executed.
* **`TIMESTAMPDIFF()`** is not translated and fails. Use `UNIX_TIMESTAMP()` arithmetic instead.
* Some functions have no DuckDB equivalent or differ in syntax — `GROUP_CONCAT()`, `DATE_FORMAT()`, `FORMAT()`, `JSON_CONTAINS()` with three arguments, `FOUND_ROWS()`, and `LAST_INSERT_ID()` among them.

Function semantics are otherwise aligned by compatibility overrides registered in DuckDB at startup, covering byte oriented `LENGTH()` and `OCTET_LENGTH()`, `ASCII()`, `ORD()`, `HEX()`, `OCT()`, `BIN()`, `LOCATE()`, `MID()`, `ADDTIME()`, `SUBTIME()`, `LTRIM()`, `RTRIM()`, the `REGEXP_*` functions, `WEEK()` and `YEARWEEK()` modes, `TO_DAYS()`, `DAYOFWEEK()`, and `WEEKDAY()`.

A maintained compatibility matrix is published in the server repository, at [`storage/duckdb/docs/mariadb-duckdb-incompatibilities.md`](https://github.com/MariaDB/server/blob/11.4/storage/duckdb/docs/mariadb-duckdb-incompatibilities.md).

## Building From Source

The engine is part of the server source tree, under `storage/duckdb/`, and builds DuckDB from a submodule. A helper script installs the build dependencies and drives the build:

```sh
# Use the branch matching your target version: 11.4, 11.8, 12.3, 13.0, or 13.1
git clone --recurse-submodules -b 11.4 \
  https://github.com/MariaDB/server.git mariadb-server
cd mariadb-server

# Install build dependencies (requires root)
./storage/duckdb/build.sh -D

# Build and install
./storage/duckdb/build.sh

# Or build a DEB or RPM package instead
./storage/duckdb/build.sh -p
```

## See Also

* [DuckDB documentation](https://duckdb.org/docs/) — the embedded engine's own reference, including its collation limitations, concurrency model, and storage layout.
* [MDEV-39234](https://jira.mariadb.org/browse/MDEV-39234) — feature ticket for the engine.
* [`storage/duckdb/`](https://github.com/MariaDB/server/tree/11.4/storage/duckdb) — engine source, `README.md`, and design notes, including the security model of `run_in_duckdb()` and dataset tutorials.
* [DuckDB Storage Engine for MariaDB: When the Sea Lion Learns to Quack](https://mariadb.org/duckdb-storage-engine-for-mariadb-when-the-sea-lion-learns-to-quack/) — Roman Nozdrin.
* [MariaDB DuckDB: A New Playground for Analytics](https://mariadb.org/mariadb-duckdb-a-new-playground-for-analytics-a-first-look-at-the-new-storage-engine/) — Frédéric Descamps.
* [SHOW ENGINES](../../reference/sql-statements/administrative-sql-statements/show/show-engines.md)
* [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
