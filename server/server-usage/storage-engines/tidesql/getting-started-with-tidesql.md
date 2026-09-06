---
description: >-
  Loading the TideSQL plugin, the install.sh builder, the one linkage detail
  that decides whether the plugin loads, and creating your first table.
---

# Getting Started with TideSQL

TideSQL is a pluggable storage engine for MariaDB Server, built on the TidesDB library. It lets a MariaDB table keep its data in a TidesDB log-structured merge tree, reachable through ordinary SQL. TideSQL is a shared-object plugin. Once a MariaDB server is built with the plugin, load it at startup from `my.cnf`:

{% code title="my.cnf" %}
```ini
[mysqld]
plugin-load-add=ha_tidesdb.so
plugin-maturity=beta
```
{% endcode %}

or dynamically in a running server:

```sql
INSTALL SONAME 'ha_tidesdb';
```

The plugin ships at Beta maturity, so the server's `plugin_maturity` threshold has to be `beta` or lower or the load is refused. A stable server defaults that threshold to `gamma`, which is stricter than `beta`, so the `plugin-maturity=beta` line above is needed, and `install.sh` writes it into the `my.cnf` it generates.

Once loaded it appears in `SHOW ENGINES`:

```
Engine: TidesDB
Support: YES
Comment: LSM B-tree engine with ACID transactions, MVCC concurrency, replication, and secondary, spatial, full-text and vector indexes
Transactions: YES
     XA: YES
Savepoints: YES
```

## Building With install.sh

The repository ships `install.sh`, which clones MariaDB, builds it with the plugin against a matching TidesDB library, and writes a ready-to-run `my.cnf`. It resolves system dependencies, submodules, and configuration.

```bash
git clone https://github.com/tidesdb/tidesql.git
cd tidesql
./install.sh --mariadb-prefix ~/mariadb-tidesdb
```

The options it accepts:

| Option | Description |
|--------|-------------|
| `--mariadb-prefix <path>` | MariaDB install directory |
| `--tidesdb-prefix <path>` | TidesDB library install directory (default `/usr/local`) |
| `--mariadb-version <tag>` | MariaDB branch or tag to build |
| `--tidesdb-version <tag>` | TidesDB library release tag |
| `--build-dir <path>` | Build directory |
| `--jobs <n>` | Parallel build jobs |
| `--skip-deps` | Skip system dependency installation |
| `--skip-tidesdb` | Skip building the library (use an already-installed one) |
| `--rebuild-plugin` | Rebuild and reinstall only `ha_tidesdb.so` against an existing MariaDB install |
| `--skip-engines <list>` | Comma-separated storage engines to exclude from the build |
| `--list-engines` | List available storage engines and exit |
| `--pgo` | Profile-guided optimization, a longer build for faster binaries |
| `--s3` | Build the library with its S3 connector compiled in, which requires libcurl |
| `--allocator <name>` | Link the library against `system` (default), `jemalloc`, `mimalloc`, or `tcmalloc` |

After it finishes, start the server and connect over the socket:

```bash
~/mariadb-tidesdb/bin/mariadbd --defaults-file=~/mariadb-tidesdb/my.cnf &
~/mariadb-tidesdb/bin/mariadb -S /tmp/mariadb.sock
```

## The Allocator and Why the Plugin May Fail to Load

`--allocator` changes only the allocator inside `libtidesdb.so`. It does not touch mariadbd's own allocator. It affects one operational detail that matters a great deal.

`jemalloc`, `mimalloc`, and `tcmalloc` place their thread-local state in the initial-exec TLS model. That model needs its space reserved when the program starts. The plugin is loaded late, with `dlopen`, well after startup, so when `libtidesdb.so` was linked against one of those allocators the loader cannot find room for its TLS and the plugin fails to load with an error like:

```
Can't open shared library 'ha_tidesdb.so' (errno: 2, libjemalloc.so.2: cannot allocate memory in static TLS block)
```

The fix is to put the allocator in the process image at startup so its TLS is reserved up front. Use MariaDB's `--malloc-lib`, or preload it directly:

```bash
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2 \
  ~/mariadb-tidesdb/bin/mariadbd --defaults-file=~/mariadb-tidesdb/my.cnf &
```

A library built with the default `system` allocator has no such requirement and loads with no preload. Check what a build was linked against with:

```bash
ldd /usr/local/lib/libtidesdb.so | grep -E 'jemalloc|mimalloc|tcmalloc'
```

Because `--rebuild-plugin` does not rebuild the library, changing `--allocator` needs a full install run to take effect.

## Installing With MariaDB Foundry

[MariaDB Foundry](https://github.com/MariaDB/foundry) is a build-and-packaging tool that produces distributable plugin packages in `tar.gz`, `rpm`, and `deb` formats for an existing MariaDB Server, and its repository includes a `tidesql` target. It is the path to use when you already have a MariaDB Server installed and want a packaged TideSQL plugin for it, rather than building the whole server from source with `install.sh`. Foundry packages an already-built plugin against the server's development files, so it does not build MariaDB itself.

{% hint style="info" %}
Use `install.sh` when you want the builder to clone and build MariaDB and the TidesDB library together. Use MariaDB Foundry when you already run a MariaDB Server and only need a packaged plugin to install onto it.
{% endhint %}

Foundry needs the MariaDB development files, either the `MariaDB-devel` package on RPM systems or `libmariadb-dev` on DEB systems, or the `CMAKE_PREFIX_PATH` and `LIBRARY_PATH` environment variables pointing at them. From an empty build directory, build the packages by pointing CMake at Foundry's `run.cmake`:

```bash
cmake -P /path/to/foundry/run.cmake /path/to/foundry/tidesql
```

To build an RPM package specifically:

```bash
cmake -DRPM=1 -P run.cmake tidesql
```

Install the resulting package with your system package manager, then load the plugin as shown above with `plugin-load-add=ha_tidesdb.so` and `plugin-maturity=beta`, or with `INSTALL SONAME 'ha_tidesdb'`. See the [MariaDB Foundry repository](https://github.com/MariaDB/foundry) for its full usage and requirements.

## Your First Table

Creating a TidesDB table is a matter of the `ENGINE` clause:

```sql
CREATE TABLE events (
  id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  ts    DATETIME NOT NULL,
  kind  VARCHAR(50),
  data  TEXT
) ENGINE=TIDESDB;
```

This creates one TidesDB column family to hold the table's rows. If you later drop the table, that column family and all of its SSTables are removed with it.

```sql
INSERT INTO events (ts, kind, data) VALUES (NOW(), 'signup', 'alice');
INSERT INTO events (ts, kind, data) VALUES (NOW(), 'login',  'alice');

SELECT * FROM events ORDER BY id;
```

Everything you would expect from a SQL table works from here. The rest of this documentation covers the parts that are specific to TidesDB.

### The One Idea to Carry Forward

A TideSQL table is one column family for its rows, plus one more column family for each secondary index. Each column family is an independent LSM-tree with its own memtable presence, its own SSTables, and its own compaction schedule. That mapping is what the [Data Model](tidesql-data-model.md) page builds on, and it is worth keeping in mind because it explains where storage, statistics, and maintenance operations act.

## Where to Go Next

* [Data Model](tidesql-data-model.md) for how rows, keys, and indexes are laid out.
* [Transactions and Isolation](tidesql-transactions-and-isolation.md) before running anything with write contention, because the concurrency model differs from InnoDB.
* [Durability and Sync Modes](tidesql-durability-and-sync-modes.md) to decide what a committed write guarantees.
* [Table Options](tidesql-table-options.md) for the per-table knobs available at `CREATE TABLE`.

<sub>_This page is licensed: GPLv2_</sub>
