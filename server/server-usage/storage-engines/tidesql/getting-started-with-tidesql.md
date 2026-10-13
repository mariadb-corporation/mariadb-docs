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
| `--mariadb-prefix <path>` | MariaDB install directory (default `/usr/local/mariadb`) |
| `--tidesdb-prefix <path>` | TidesDB library install directory (default `/usr/local`) |
| `--mariadb-version <tag>` | MariaDB branch or tag to build (default the latest MariaDB release on GitHub) |
| `--tidesdb-version <tag>` | TidesDB library release tag (default the latest TidesDB release on GitHub) |
| `--build-dir <path>` | Build directory (default `/tmp/tidesql-build`) |
| `--jobs <n>` | Parallel build jobs (default the detected CPU count) |
| `--skip-deps` | Skip system dependency installation |
| `--skip-tidesdb` | Skip building the library (use an already-installed one) |
| `--rebuild-plugin` | Rebuild only `ha_tidesdb.so`, in the build tree a previous full run left behind, and copy it into the MariaDB install |
| `--skip-engines <list>` | Comma-separated storage engines to exclude from the build |
| `--list-engines` | List available storage engines and exit |
| `--pgo` | Profile-guided optimization, a longer build for faster binaries |
| `--allocator <name>` | Link the library against `system` (default), `jemalloc`, `mimalloc`, or `tcmalloc` |
| `--help`, `-h` | Print the option summary and exit |

The path defaults are for Linux and macOS. Under MSYS2 or Git Bash on Windows they are `C:/mariadb`, `C:/tidesdb`, and `C:/tidesql-build`.

After it finishes, start the server and connect over the socket:

```bash
~/mariadb-tidesdb/bin/mariadbd-safe --defaults-file=~/mariadb-tidesdb/my.cnf &
~/mariadb-tidesdb/bin/mariadb -S /tmp/mariadb.sock
```

## Compression Backends

The zstd, lz4, and snappy compression backends are optional. `install.sh` installs their development packages as part of the dependency step, and the plugin build links each backend only when it finds that library, so a missing one does not cause the plugin build to fail.

When the plugin build finds no installed TidesDB library or headers, it fetches and builds TidesDB v10.2.1 from source and links it statically. That fallback build enables a backend only when both its library and its header are present on the machine. A machine without any of them gets a library that stores data uncompressed. An installed TidesDB older than 10.2.0 stops the build with a message naming the version it found, since the plugin calls APIs that first appeared in 10.2.0.

## The Allocator and Why the Plugin May Fail to Load

`--allocator` changes only the allocator inside `libtidesdb.so`. It does not touch mariadbd's own allocator. The library links an allocator only when it is built with the matching `TIDESDB_WITH_JEMALLOC`, `TIDESDB_WITH_MIMALLOC`, or `TIDESDB_WITH_TCMALLOC` option, which is what `--allocator` sets. It affects one operational detail that matters a great deal.

The plugin is loaded late, with `dlopen`, well after startup. When `libtidesdb.so` was linked against jemalloc, the loader cannot find room in the static TLS block for the allocator's thread-local state at that point, and the plugin fails to load with an error like:

```
Can't open shared library 'ha_tidesdb.so' (errno: 2, libjemalloc.so.2: cannot allocate memory in static TLS block)
```

The fix is to put the allocator in the process image at startup so its TLS is reserved up front. For any allocator other than `system`, `install.sh` looks up the allocator's shared library with `ldconfig` and, when it finds it, writes it into the generated `my.cnf` as `malloc-lib` under `[mysqld_safe]`, so `mariadbd-safe` preloads it before it starts `mariadbd`:

{% code title="my.cnf" %}
```ini
[mysqld_safe]
malloc-lib = /usr/lib/x86_64-linux-gnu/libjemalloc.so.2
```
{% endcode %}

A server started directly as `mariadbd` does not read that section, so preload the allocator yourself:

```bash
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2 \
  ~/mariadb-tidesdb/bin/mariadbd --defaults-file=~/mariadb-tidesdb/my.cnf &
```

A library built with the default `system` allocator has no such requirement and loads with no preload. Check what a build linked against with:

```bash
ldd /usr/local/lib/libtidesdb.so | grep -E 'jemalloc|mimalloc|tcmalloc'
```

Because `--rebuild-plugin` does not rebuild the library, changing `--allocator` needs a full install run to take effect. `install.sh` writes `my.cnf` only when the file does not exist yet, so after such a run, check that the `[mysqld_safe]` line matches the new allocator.

## Installing With MariaDB Foundry

[MariaDB Foundry](https://github.com/MariaDB/foundry) is a build-and-packaging tool that produces distributable plugin packages in `tar.gz`, `rpm`, and `deb` formats for an existing MariaDB Server, and its repository includes a `tidesql` target. It is the path to use when you already have a MariaDB Server installed and want a packaged TideSQL plugin for it, rather than building the whole server from source with `install.sh`. Foundry builds the plugin out of tree against the server's development files and packages it, so it does not build MariaDB itself.

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

A TideSQL table is one column family for its rows, plus one more column family for each secondary index. Each column family is an independent LSM-tree with its own SSTables and its own compaction schedule, while all of them share one memtable and one write-ahead log. That mapping is what the [Data Model](tidesql-data-model.md) page builds on, and it is worth keeping in mind because it explains where storage, statistics, and maintenance operations act.

## Where to Go Next

* [Data Model](tidesql-data-model.md) for how rows, keys, and indexes are laid out.
* [Transactions and Isolation](tidesql-transactions-and-isolation.md) before running anything with write contention, because the concurrency model differs from InnoDB.
* [Durability and Sync Modes](tidesql-durability-and-sync-modes.md) to decide what a committed write guarantees.
* [Table Options](tidesql-table-options.md) for the per-table knobs available at `CREATE TABLE`.

<sub>_This page is licensed: GPLv2_</sub>
