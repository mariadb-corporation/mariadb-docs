---
description: >-
  How the dump and load utilities carry sequences, Oracle-mode packages, CHECK
  constraints, roles and DENY, system-versioned tables, MariaDB data types,
  and GTIDs, and which vendors they accept.
---

# MariaDB-Specific Features

MariaDB features that have no MySQL counterpart are dumped and restored with their definitions and data intact. The utilities also use MariaDB's own server mechanisms: the `BACKUP STAGE` lock for consistent dumps, MariaDB GTIDs for replica provisioning, and session-level `CHECK` enforcement for loads.

Each feature on this page is covered by an end-to-end test that creates it on a MariaDB server, dumps it, loads it into a second server, and compares definitions and data, including checksums.

## Vendor Rules

A dump made from a MariaDB server can only be loaded into a MariaDB server, and a dump made from a MySQL server only into a MySQL server. The load refuses a dump from the other vendor before it runs any DDL, and the copy utilities refuse a source and a target of different vendors. The SQL dialects and object types differ too much for a partial translation, which would lose data without notice.

| Source | Target | Result |
| --- | --- | --- |
| MariaDB | MariaDB | Loads |
| MySQL | MySQL | Loads |
| MariaDB | MySQL | Refused |
| MySQL | MariaDB | Refused |

The dump options `ocimds` and `compatibility` exist only for MySQL HeatWave Service and are refused for a MariaDB source. The same applies to other MySQL-only features listed in the built-in help, such as data masking policies, library objects, Lakehouse targets, and `BULK LOAD`: they have no effect on MariaDB.

## Objects

| Feature | What is preserved |
| --- | --- |
| Sequences | The definition and the current position, including how many times a cycling sequence has wrapped. |
| Oracle-mode packages | The package specification and body, also next to a standalone function of the same name, and `GRANT EXECUTE` on packages. |
| `CHECK` constraints | The constraints, and existing rows that violate them. |

### Sequences

A sequence is written to the DDL script of its schema as a `CREATE SEQUENCE` statement followed by `DO SETVAL(...)`, which sets its position. The load creates sequences before any table, so a column `DEFAULT NEXT VALUE FOR seq` resolves when the table is created.

The restored position is `next_not_cached_value` of the source, which includes the values the sequence cache had reserved. The restored sequence may therefore skip some values, but never repeats one. This is also where the server itself resumes after a restart.

Sequences are selected with the table filters, `includeTables` and `excludeTables`; there is no separate sequence option. When you load a schema under a new name with `schema`, a column `DEFAULT` that draws from a sequence of the same schema refers to the renamed schema. If `util.dump_tables()` dumps a table whose default refers to a sequence that is not in the dump, the dump warns that the table can only be created where that sequence exists.

### Oracle-Mode Packages

Packages are dumped with the routines of their schema, in this order: package specifications, functions, procedures, package bodies. The specification can then declare types that routines use, and a body can call those routines. Packages are selected with `includeRoutines` and `excludeRoutines`; excluding `shop.billing` excludes the package, its body, and a function named `billing`.

### CHECK Constraints

MariaDB can hold rows that violate a table's own `CHECK` constraints, for example rows inserted before the constraint was added. To restore such rows as they are, the load sessions set `check_constraint_checks = 0` on the target, as `mariadb-import` does. `util.import_table()` does the same.

## Access Control

Accounts are carried by `util.dump_instance()` and `util.copy_instance()`, and loaded only when you set `loadUsers` on the load.

| Feature | What is preserved |
| --- | --- |
| Roles | MariaDB's hostless roles, roles granted to roles, default roles, and `WITH ADMIN OPTION`. |
| Roles of dumped accounts | When `includeUsers` selects an account, the roles granted to it are dumped too, transitively, and the dump lists them in a note. A role named in `excludeUsers` stays excluded. |
| The `PUBLIC` role | Its grants, merged into the grants `PUBLIC` already has on the target. They are never removed from the target, even with `dropExistingObjects`. |
| `DENY` | At every level: global, schema, table, column, routine, and package. Requires MariaDB 13.1.1 or later. |
| Authentication | Password hashes and the authentication plugins of each account, including `IDENTIFIED VIA plugin1 OR plugin2`. Tested with `ed25519`, `unix_socket`, and `mysql_native_password`. |

If an account uses a loadable authentication plugin, such as `ed25519`, `gssapi`, `pam`, or `parsec`, the plugin must be installed on the target. See [Limitations](limitations.md#target-preparation).

## Tables and Data Types

| Feature | What is preserved |
| --- | --- |
| System-versioned tables | The definition, including `PARTITION BY SYSTEM_TIME`, and the current rows. The history is not carried; the dump warns about each such table, and the loaded rows start a new history. |
| Application-time periods and `UNIQUE ... WITHOUT OVERLAPS` keys | Definition and data. Chunks of such tables load one at a time. See [How Chunks Are Scheduled](how-dump-and-load-work.md#how-chunks-are-scheduled). |
| `UUID`, `INET4`, `INET6`, `XMLTYPE` | Data, exactly, in the printable form the server sends and accepts. |
| `JSON` | Definition and data. MariaDB stores `JSON` as `LONGTEXT` with a `json_valid()` check, and the dump recognizes such columns as JSON. |
| `VECTOR` columns and vector indexes | Definition and data. |
| Dynamic columns | Data, byte for byte. |
| Invisible, compressed, virtual, and persistent columns; ignored indexes | Definition and data. |
| Aria tables, `PAGE_COMPRESSED` tables, encrypted tables | Table options. Encrypted tables need key management on the target, and a `PAGE_COMPRESSED` table uses the target's `innodb_compression_algorithm`. |

A system-versioned table is always dumped whole. Selecting some of its partitions with the `partitions` option is refused, because MariaDB does not allow partition selection on such a table.

A column type that MariaDB Shell does not know, for example `mysql_json` in a table upgraded from MySQL 5.7, stops the dump with an error that names the column and table. Guessing how to carry an unknown type could corrupt data without notice. Exclude the table with `excludeTables` to dump the rest.

## Server Integration

| Feature | Used for |
| --- | --- |
| `BACKUP STAGE` | MariaDB's backup lock. `BACKUP STAGE BLOCK_DDL` blocks schema changes for the length of a consistent dump. Requires the `RELOAD` privilege. See [Consistency on MariaDB](how-dump-and-load-work.md#consistency-on-mariadb). |
| MariaDB GTIDs | The dump records `gtid_current_pos`; a load with `updateGtidSet` writes it to `gtid_slave_pos` to provision a replica. |
| `check_constraint_checks` | Turned off in load sessions so that rows violating a `CHECK` constraint can be restored. |
| `BINLOG MONITOR` | The privilege the dump uses to read the binary log position, in place of MySQL's `REPLICATION CLIENT`. |

### MariaDB GTIDs and updateGtidSet

A MariaDB GTID has the form `domain-server-sequence`, and a GTID position lists the last applied sequence for each replication domain. The dump records the source's `gtid_current_pos`, which combines what the server wrote to its binary log and what it applied as a replica. This is the same position `mariadb-backup` records. GTIDs on MariaDB come with the binary log, so a position is recorded whenever `log_bin` is on.

The load option `updateGtidSet` writes the dumped position to the target's `gtid_slave_pos`, which is where `CHANGE MASTER TO ... MASTER_USE_GTID = slave_pos` resumes replication. The target's binary log state is never changed.

| Value | Effect on MariaDB | Condition |
| --- | --- | --- |
| `off` (default) | Nothing | |
| `replace` | Sets `gtid_slave_pos` to the dumped position | The dumped position must cover the target's current `gtid_slave_pos`, so that nothing already replicated is forgotten. |
| `append` | Adds the dumped position to the target's `gtid_slave_pos` | The two positions must not share a replication domain. |

Both values are refused while any replica connection is running on the target. Stop replication first. See [Provision a Replica](quick-start.md#provision-a-replica) for a complete example.

On a Galera cluster, `gtid_slave_pos` is local to each node. A load with `updateGtidSet` sets the position only on the node it is connected to, while Galera replicates the data to every node. Start asynchronous replication on that same node.
