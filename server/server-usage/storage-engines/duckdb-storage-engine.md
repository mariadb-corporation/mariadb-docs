---
description: >-
  DuckDB embedded as a MariaDB storage engine for analytical workloads.
  Experimental — alpha maturity, not in mainline MariaDB releases.
---

# DuckDB Storage Engine

{% hint style="danger" %}
**Experimental — for evaluation only.** The DuckDB storage engine is at **alpha** maturity. It is not yet merged into MariaDB Server `main`, not built into MariaDB releases, and not signed in any official package. Interfaces, configuration variables, behavior, and supported operations are subject to change. **Do not use in production.**
{% endhint %}

The DuckDB storage engine embeds [DuckDB](https://duckdb.org/) — a columnar, vectorized, in-process analytical database engine — inside MariaDB Server as a loadable plugin (`ha_duckdb.so`). Tables created with `ENGINE=DuckDB` store data in DuckDB's native columnar format, and queries against them are executed by the DuckDB engine. Cross-engine joins between DuckDB and other engines (e.g. InnoDB) are supported in a single `SELECT`.

The engine borrows its design from Alibaba's [AliSQL](https://github.com/alibaba/AliSQL) DuckDB integration. The original code was heavily refactored to use MariaDB's handler API and plugin system, and the engine links against vanilla upstream DuckDB.

## Use cases

- **HTAP (Hybrid Transactional/Analytical Processing)** — InnoDB serves the transactional workload, DuckDB serves analytics, both in the same MariaDB server.
- **Ad-hoc analytical queries** — joins, aggregations, and window functions over large datasets without exporting data to a separate system.
- **Eliminating ETL** — the analytical engine runs in-process; no separate cluster or data-movement pipeline.

## Architecture

DuckDB 1.5.2 is statically linked into a single plugin shared library (`ha_duckdb.so`) along with the built-in ICU and JSON extensions. The engine integrates with MariaDB via the standard `handler` API and adds a `select_handler` for full query pushdown.

Cross-engine queries (a single `SELECT` joining a `DuckDB` table with, for example, an `InnoDB` table) are handled as follows: the entire query is pushed down to DuckDB. When DuckDB references a non-DuckDB table, a callback re-enters the MariaDB query pipeline through a cooperative fiber to stream rows back. The MariaDB optimizer still chooses the access path on the non-DuckDB side, and DuckDB's optimizer drives join order, hashing, and aggregation.

## Supported platforms

- **OS:** Linux only.
- **Architectures:** `x86_64` and `aarch64` (ARM64).
- **Distributions** (auto-detected by the build script): Ubuntu 22.04, Ubuntu 24.04, Debian 12, Rocky Linux 8, Rocky Linux 9. Fedora 42 builds are produced by the MariaDB CI.
- **Compiler:** GCC 12 or later (C++17 required).
- **MariaDB Server:** the engine is being prepared for MariaDB 11.4. A merge into the mainline source tree and the shipping version are not yet final.

## Installing

The engine is **not** included in MariaDB releases. There are two ways to obtain it: prebuilt test packages from MariaDB CI, or building from source.

### Option 1: prebuilt test packages

MariaDB CI builds the engine for several Linux distributions and publishes the artifacts on [ci.mariadb.org](https://ci.mariadb.org/). Each CI run has its own job number and a subdirectory per distribution and architecture, for example `amd64-ubuntu-2404-deb-autobake/` or `aarch64-ubuntu-2404-deb-autobake/`.

{% hint style="warning" %}
These packages are **unsigned** and intended for testing only.
{% endhint %}

The CI job number is **not stable** across rebuilds. For the current job URL, see the blog posts under [See also](#see-also).

Example for Ubuntu 24.04 (`amd64`), with a current job number `<JOB>`:

```sh
# Fetch the .deb files for the job
wget -r -np -nH --cut-dirs=2 -A '*.deb' \
  https://ci.mariadb.org/<JOB>/amd64-ubuntu-2404-deb-autobake/

# Install the server and the DuckDB plugin package
sudo dpkg -i mariadb-server*.deb mariadb-plugin-duckdb*.deb || sudo apt -f install
```

### Option 2: build from source

The engine integration lives on the `11.4` branch of [`MariaDB/server`](https://github.com/MariaDB/server). The engine source resides in the server repository under `storage/duckdb/`; a helper script there handles dependency installation and the build.

```sh
git clone --recurse-submodules -b 11.4 \
  https://github.com/MariaDB/server.git mariadb-server
cd mariadb-server

# Install build prerequisites (requires root)
./storage/duckdb/build.sh -D

# Build, install and start MariaDB server
./storage/duckdb/build.sh -S

# Optional: build a DEB or RPM instead
./storage/duckdb/build.sh -p
```

On Rocky Linux 8, pass `-R` to use `gcc-toolset-12`:

```sh
./storage/duckdb/build.sh -R
```

### Enabling the plugin

The DuckDB plugin is not loaded by default. Add a configuration file to the server's drop-in directory:

- **Debian / Ubuntu:** `/etc/mysql/mariadb.conf.d/duckdb.cnf`
- **Rocky / Fedora / openSUSE:** `/etc/my.cnf.d/duckdb.cnf`

```ini
[mysqld]
plugin-maturity=alpha
plugin-load-add=ha_duckdb.so
duckdb-memory-limit=8G
```

Each line is significant:

- `plugin-maturity=alpha` is **required**. The server's default maturity threshold rejects alpha plugins; this line is the explicit opt-in.
- `plugin-load-add=ha_duckdb.so` loads the engine at startup.
- `duckdb-memory-limit` sets the cap on memory DuckDB itself may use. The default (1 GiB) is too low for most analytical workloads — raise it to reflect the host's available RAM.

Restart the server, then verify the engine is registered:

```sql
SHOW ENGINES\G
```

The output should include a `DuckDB` row with `Support: YES`.

### Verifying the install

```sql
CREATE DATABASE analytics;
USE analytics;

CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  amount DECIMAL(15, 2),
  created_at TIMESTAMP
) ENGINE=DuckDB DEFAULT CHARSET=utf8mb4;

INSERT INTO orders VALUES (1, 199.99, NOW()), (2, 299.50, NOW());

SELECT SUM(amount) FROM orders;
```

DuckDB requires UTF-8: specify `DEFAULT CHARSET=utf8mb4` (or another UTF-8 charset) on every DuckDB table. Non-UTF8 charsets fall back to binary comparison.

## Supported operations

- **DDL:** `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`, `RENAME TABLE`. `ALTER TABLE ... ENGINE=DuckDB` migrates an existing table into DuckDB storage.
- **`INSERT`:** all major MariaDB column types.
- **`SELECT`:** full pushdown to DuckDB, including aggregations, joins, window functions, `GROUP BY`, and `ORDER BY`.
- **`UPDATE` and `DELETE`:** translated to DuckDB SQL.
- **Cross-engine `JOIN`:** a single `SELECT` can join DuckDB tables with InnoDB (or other) tables. Example:

  ```sql
  SELECT d.id, d.amount, i.name
    FROM analytics.orders d        -- ENGINE=DuckDB
    JOIN inventory.products i      -- ENGINE=InnoDB
      ON d.product_id = i.id
   WHERE d.amount > 1000;
  ```

- **User-defined functions:** DuckDB-side UDFs are registered with MariaDB.

## Configuration variables

The plugin adds a family of `duckdb_*` server variables. The most commonly tuned ones:

| Variable | Type | Default | Purpose |
|---|---|---|---|
| `duckdb_memory_limit` | integer (bytes) | `1073741824` (1 GiB) | Maximum memory DuckDB may use. Raise for analytical workloads. |
| `duckdb_max_threads` | integer | (auto) | Maximum DuckDB execution threads. |
| `duckdb_temp_directory` | string | (auto) | Directory used by DuckDB for spilling. |
| `duckdb_require_primary_key` | boolean | `ON` | Reject `CREATE TABLE` without a `PRIMARY KEY`. |
| `duckdb_max_temp_directory_size` | integer (bytes) | (unlimited) | Cap on temp-directory usage. |

Additional tuning and debugging variables (batching, log categories, optimizer hints, `EXPLAIN` verbosity, etc.) are exposed by the plugin. List the full current set with:

```sql
SHOW VARIABLES LIKE 'duckdb%';
```

## Limitations

The engine is at alpha maturity. Known limitations at the time of writing:

- **No `AUTO_INCREMENT`** and no `UUID` default-value generation.
- **`DECIMAL` precision capped at 38** — DuckDB's maximum. Wider MariaDB `DECIMAL` columns fail at DDL conversion.
- **Strict `GROUP BY`** — DuckDB rejects `SELECT` columns that are neither in the `GROUP BY` clause nor aggregated, even when MariaDB's `sql_mode` would allow it.
- **No XA `PREPARE`.**
- **UTF-8 only** — non-UTF8 charsets fall back to binary comparison. UCA-based MariaDB collations are approximated using DuckDB's `NOCASE` / `NOACCENT` collations.
- **Some MariaDB functions are not pushdown-compatible** — for example, `GROUP_CONCAT()`, `DATE_FORMAT()`, `JSON_CONTAINS()`, `FOUND_ROWS()`, and `LAST_INSERT_ID()` have no DuckDB equivalent or differ in syntax. Such queries fall back to MariaDB-side evaluation.
- **`ALTER COLUMN DROP DEFAULT`** isn't propagated to the DuckDB catalog.
- **`TIMESTAMP` is stored as `TIMESTAMPTZ`** — keep MariaDB and DuckDB timezone settings consistent to avoid value shifts.
- **Cross-engine scan is single-threaded** — only the DuckDB side of a cross-engine query is parallelized.
- **Cross-engine `INSERT` (DuckDB → InnoDB)** has restrictions; see the engine compatibility matrix.

A maintained compatibility matrix is published in the engine repository at [`docs/mariadb-duckdb-incompatibilities.md`](https://github.com/MariaDB/duckdb-engine/blob/main/docs/mariadb-duckdb-incompatibilities.md).

## See also

- [MDEV-39234](https://jira.mariadb.org/browse/MDEV-39234) — upstream feature ticket.
- [`MariaDB/duckdb-engine`](https://github.com/MariaDB/duckdb-engine) — canonical engine source repository.
- [`11.4`](https://github.com/MariaDB/server/tree/11.4) branch — the MariaDB Server fork containing the integration scaffolding.
- [DuckDB Storage Engine for MariaDB: When the Sea Lion Learns to Quack](https://mariadb.org/duckdb-storage-engine-for-mariadb-when-the-sea-lion-learns-to-quack/) — Roman Nozdrin, 2026-06-09.
- [MariaDB DuckDB: A New Playground for Analytics](https://mariadb.org/mariadb-duckdb-a-new-playground-for-analytics-a-first-look-at-the-new-storage-engine/) — Frédéric Descamps, 2026-06-12.
- [SHOW ENGINES](../../reference/sql-statements/administrative-sql-statements/show/show-engines.md)
- [INSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
