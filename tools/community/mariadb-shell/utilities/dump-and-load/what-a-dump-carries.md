---
description: >-
  The objects a MariaDB Shell dump carries, the ones it carries only in part,
  what it leaves out by design, and what its manifest records about the source
  server.
---

# What a Dump Carries

A dump carries everything that makes up the schemas, data, and access control of a database, MariaDB-specific objects included. System schemas and server-level state are left out by design.

## Carried Objects

| Object | Carried | Notes |
| --- | --- | --- |
| Schemas | Yes | With their character set and collation. |
| Tables and their data | Yes | All table options, partitions and subpartitions, compressed and encrypted tables. |
| Indexes and constraints | Yes | Primary, unique, secondary, full-text, spatial, and vector indexes; foreign keys; `CHECK` constraints. |
| Views | Yes | Created after the tables and views they use. |
| Stored procedures and functions | Yes | With their definer and SQL mode. |
| Oracle-mode packages | Yes | Package specification and package body. |
| Triggers and events | Yes | |
| Sequences | Yes | Definition and current position. |
| Accounts, roles, and grants | Yes | With `util.dump_instance()` and `util.copy_instance()`: password hashes, authentication plugins, resource limits, roles and default roles, `GRANT` and `DENY`. |
| Replication position | Yes | The binary log file and position, and the GTID position, at the time of the snapshot. Recorded when the binary log is enabled and the account has `BINLOG MONITOR`. |
| System-versioned tables | Partly | Definition and current rows. The history is not carried, and the dump warns about each such table. |
| Tables on engines that keep their data elsewhere (MERGE, FEDERATED, Spider, CONNECT, OQGRAPH, VP) | Definition only | Their data belongs to other tables, servers, or files, so only the `CREATE TABLE` statement is dumped, as `mariadb-dump` does by default. A note names each such table. |

See [MariaDB-Specific Features](mariadb-specific-features.md) for details on sequences, packages, roles, system versioning, and MariaDB data types.

### Selecting What to Dump

By default every carried object of the selected schemas is dumped. You narrow a dump with the following options, described on the [Dump Utilities](dump-utilities.md) page:

* `includeSchemas`, `excludeSchemas`, `includeTables`, `excludeTables`, and the same pairs for routines, events, triggers, and users.
* `routines`, `events`, `triggers`, and `users` to leave out a whole kind of object.
* `ddlOnly` for definitions without data, and `dataOnly` for data without definitions.
* `where` for a row condition per table, and `partitions` for selected partitions.

Sequences are selected with the table filters, because they share the table namespace. Packages are selected with the routine filters.

The load has the same filters, so you can also restore part of a complete dump. See [Load Dump Utility](load-dump-utility.md).

## Excluded by Design

| Not carried | Why | Instead |
| --- | --- | --- |
| The system schemas `mysql`, `information_schema`, `performance_schema`, and `sys` | They hold server state. Accounts are carried separately, as statements. | Use `util.dump_instance()` to carry accounts. |
| The system accounts `mariadb.sys`, `mysql.sys`, and `mysql.session` | They belong to the server installation. | |
| Engine-independent statistics (`mysql.table_stats`, `mysql.column_stats`, `mysql.index_stats`) | They are system state in the `mysql` schema. | Run `ANALYZE TABLE ... PERSISTENT FOR ALL` on the target after loading. |
| Server configuration, plugins, and `CREATE SERVER` definitions | They are server-level setup. | Prepare the target before the load. |
| Binary logs | Not available for MariaDB in MariaDB Shell. | Use `mariadb-backup` or `mariadb-binlog` for point-in-time recovery. |

The rows of the log tables `mysql.general_log`, `mysql.slow_log`, and `mysql.transaction_registry` are never dumped.

See [Limitations](limitations.md) for how these compare with `mariadb-dump`.

## The Manifest

The manifest, `@.json` in the dump directory, describes the dump: the function and options that created it, the dumped schemas, the MariaDB Shell version, and the start time. It also records the source server:

| Field | Contents |
| --- | --- |
| `source.vendor` | `mariadb` or `mysql`. The load uses it to refuse a dump from the other vendor. |
| `serverVersion`, `server`, `hostname`, `user` | The source version, its host name, and the account that ran the dump. |
| `source.binlog`, `binlogFile`, `binlogPosition`, `gtidExecuted` | The binary log file and position, and the MariaDB GTID position (`gtid_current_pos`), at the time of the snapshot. |
| `source.sysvars` | Every global system variable of the source, as `SHOW GLOBAL VARIABLES` reported it at dump time. |

To display the recorded position without loading anything, run a load with `showMetadata` and `dryRun`:

```python
util.load_dump("/backups/for-replica", {"showMetadata": True, "dryRun": True})
```

The load uses only a few of the recorded system variables. `lower_case_table_names` must match the target, or the load is refused. A mismatch in `partial_revokes` is reported. The version, host name, and port identify the source. The other variables are a record of how the source was configured, and none of them is applied to the target.

{% hint style="warning" %}
`source.sysvars` is the complete, unfiltered list of the source's global system variables. It includes file paths, host names, cluster addresses, the `init_connect` statement, and, if the server was started with one, the value of `report_password`. Store and share dumps with the same care as the server's configuration files.
{% endhint %}
