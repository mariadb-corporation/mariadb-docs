---
description: >-
  What the dump and load utilities do not do on MariaDB, what a target server
  must be prepared with, which behaviors are by design, and known issues.
---

# Limitations

This page lists what the dump and load utilities do not do on MariaDB, what you must prepare on a target server, and which behaviors are intended. Several of the limitations match the default behavior of `mariadb-dump`.

## Not Available

| Feature | Impact | What to do |
| --- | --- | --- |
| Binary log dump and replay (`util.dump_binlogs()`, `util.load_binlogs()`) | No point-in-time recovery from MariaDB Shell. | Use `mariadb-backup`, or `mariadb-binlog` to replay binary logs after a restore. |
| The dump options `ocimds` and `compatibility` | Tables cannot be converted while they are dumped, for example to InnoDB with primary keys for a Galera cluster. | Convert the tables on the target after loading. The load option `createInvisiblePKs` adds an invisible primary key to tables that have none. |

## Not Carried

| Not carried | What to do | Same as `mariadb-dump`? |
| --- | --- | --- |
| The history of system-versioned tables (only current rows are dumped, and the dump warns) | Use `mariadb-dump --dump-history` for tables whose history you must keep. | Yes by default; `mariadb-dump` has an option to include it. |
| Engine-independent statistics (`mysql.table_stats`, `mysql.column_stats`, `mysql.index_stats`) | Run `ANALYZE TABLE ... PERSISTENT FOR ALL` on each table after loading. The load option `analyzeTables` runs a plain `ANALYZE TABLE`, which does not collect them. | Yes by default; `mariadb-dump --system=stats` carries them. |
| `CREATE SERVER` definitions, used by Spider and FEDERATED tables | Create them on the target before loading. | Yes by default; `mariadb-dump --system=servers` carries them. |
| The data of tables on MERGE, FEDERATED, Spider, CONNECT, OQGRAPH, and VP engines | Their data belongs to other tables, servers, or files; only the definition is dumped. | Yes; `mariadb-dump --no-data-med` is on by default. |

Without the engine-independent statistics, the optimizer on the target can choose different query plans until you collect them again.

## Target Preparation

| Situation | What happens | What to do |
| --- | --- | --- |
| An account uses a loadable authentication plugin (`ed25519`, `gssapi`, `pam`, `parsec`) that is not installed on the target. | The load stops with a note that names the plugin and the account, and says how many accounts were already created. | Install the plugin with `INSTALL SONAME` on the target, then run the same load again. It resumes, and accounts already created are kept. |
| The dump contains encrypted tables, and the target has no key management plugin. | The load stops with the server's error `errno: 140 "Wrong create options"`, which does not mention encryption. | Configure a key management plugin on the target that provides the same key IDs. |
| The target has `local_infile` turned off. | The data load fails. | `SET GLOBAL local_infile = ON` on the target. |
| The target already has some of the objects or accounts in the dump. | The load lists them and stops before changing anything. | Exclude them, or use `dropExistingObjects` or `ignoreExistingObjects`. When you load accounts from `util.dump_instance()` into a new server, exclude the accounts the server already has, such as `root`. |
| The source and target use different `lower_case_table_names` settings. | The load is refused. | Load into a server with the same setting. |

## By Design

| Behavior | Why |
| --- | --- |
| Dumps load MariaDB to MariaDB and MySQL to MySQL; a dump from the other vendor is refused. | The SQL dialects and object types differ, and a partial translation would lose data without notice. See [Vendor Rules](mariadb-specific-features.md#vendor-rules). |
| The grants of `PUBLIC` are merged into the target's, never replaced, even with `dropExistingObjects`. | `PUBLIC` applies to every account on the target. Removing its grants could lock other applications out. To start from a clean `PUBLIC`, revoke its grants on the target before loading. |
| The global read lock waits as long as the server's `lock_wait_timeout` allows, one day by default on MariaDB. | The server setting governs the wait, as for `mariadb-dump` and `mariadb-backup`. Lower `lock_wait_timeout` for the dump account to bound it. |
| A consistent dump blocks writes to MyISAM tables for its whole length. | `BACKUP STAGE BLOCK_DDL` blocks DML on non-transactional tables. Writes to InnoDB tables continue. |
| An unknown column type stops the dump and names the column. | Guessing how to carry an unknown type could corrupt data. Exclude the table to dump the rest. |
| Selecting partitions of a system-versioned table is refused. | MariaDB does not allow partition selection on such a table, which is always dumped whole. |
| `updateGtidSet` on a Galera node sets the position on that node only. | MariaDB keeps `gtid_slave_pos` per node. Start the replica on the node that was loaded. |
| A sequence restarts at `next_not_cached_value`, ahead of the last value handed out. | Values reserved by the sequence cache are skipped rather than reused, as after a server restart. |
| S3 tables are dumped like other tables. | `mariadb-dump` skips them unless `--copy-s3-tables` is given. |
| The copy utilities cannot resume after an interruption. | The data is a live stream with no files to resume from. Run the copy again with `dropExistingObjects` or `ignoreExistingObjects`. |

## Known Issues

* **Views with MariaDB-only syntax.** For views that use syntax such as `FOR SYSTEM_TIME`, `WITH TIES`, a `VALUES` table constructor, `INTERSECT ALL`, or `CAST(... AS UUID)`, the dump cannot check whether they refer to tables that are not in the dump. Such views are dumped correctly, and the dump says that it could not check them.
* **Untested engines.** Tables on the Spider, CONNECT, OQGRAPH, VP, and FEDERATED engines are handled as described in [What a Dump Carries](what-a-dump-carries.md), but have not been tested, because the server packages used for testing do not include these engines. Subpartitions of system-versioned tables are not tested either.
* **The manifest records the source configuration.** `@.json` contains every global system variable of the source, including file paths, host names, cluster addresses, and `report_password` if the server was started with one. Store and share dumps with the same care as the server's configuration files. See [The Manifest](what-a-dump-carries.md#the-manifest).
* **Object storage is not validated.** Amazon S3, OCI Object Storage, and Azure Blob Storage have not been tested against MariaDB. Local and network file systems are fully tested. See [Object Storage](object-storage.md).
