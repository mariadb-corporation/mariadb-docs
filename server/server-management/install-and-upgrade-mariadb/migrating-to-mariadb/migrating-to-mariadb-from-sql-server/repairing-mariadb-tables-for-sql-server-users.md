---
description: >-
  Explains how to check and repair tables in MariaDB using `CHECK TABLE` and
  `REPAIR TABLE`, noting that InnoDB typically handles corruption by crashing to
  prevent data loss.
---

# Repairing MariaDB Tables for SQL Server Users

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

Repairing tables in MariaDB is not similar to repairing tables in SQL Server.

The first thing to understand is that every MariaDB table is handled by a [storage engine](understanding-mariadb-architecture.md#storage-engines). Storage engines are plugins that know how to physically read and write a table, so each storage engine allows one to repair tables in different ways. The default storage engine is [InnoDB](../../../../server-usage/storage-engines/innodb/).

MariaDB provides specific SQL statements to deal with corrupted tables:

* [CHECK TABLE](../../../../reference/sql-statements/table-statements/check-table.md) checks if a table is corrupted;
* [REPAIR TABLE](../../../../reference/sql-statements/table-statements/repair-table.md) repairs a table if it is corrupted.

As a general rule, there is no reason why a table that is corrupted on a master should also be corrupted on the slaves. Therefore, `REPAIR` is generally used with the `NO_WRITE_TO_BINLOG` option, to avoid replicating it to the slaves.

## Partitioned Tables

[Partitioned tables](../../../../server-usage/partitioning-tables/) are normally split into multiple physical files (one per partition). Even if one of the partitions is corrupted, in most cases other partitions are healthy.

For this reason, `CHECK TABLE` and `REPAIR TABLE` don't work on partitioned tables. Instead, use [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) to check or repair a single partition.

For example:

```
ALTER TABLE orders CHECK PARTITION p_2019, p_2020;
ALTER TABLE orders REPAIR PARTITION p_2019, p_2020;
```

## Indexes

Indexes can get corrupted. However, as long as data is not corrupted, indexes can always be dropped and rebuilt with [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/):

```
ALTER TABLE customer DROP INDEX idx_email;
ALTER TABLE customer ADD INDEX idx_email (email);
```

## Checking and Repairing Tables

Here we discuss how to repair tables, depending on the storage engine.

### InnoDB

InnoDB follows the "fail fast" philosophy. If table corruption is detected, by default InnoDB deliberately causes MariaDB to crash to avoid corruption propagation, logging an error into the [error log](../../../server-monitoring-logs/error-log.md). This happens even if the corruption is found with a `CHECK TABLE` statement. This behavior can be changed with the [innodb\_corrupt\_table\_action](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_corrupt_table_action) server variable.

To repair an InnoDB table after a crash:

1. Restart MariaDB with the [--innodb-force-recovery](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery) option set to a low but non-zero value.
2. If MariaDB fails to start, retry with a higher value. Repeat until you succeed.

At this point, you can follow two different procedures, depending if you can use a backup or not. Provided that you have a usable backup, it is often the best option to bring the database up quickly. But if you want to reduce the data loss as much as possible, you prefer to follow the second method.

Restoring a backup:

1. Drop the whole database with [DROP DATABASE](../../../../reference/sql-statements/data-definition/drop/drop-database.md).
2. Restore a backup of the database. The exact procedure depends on the [type of backup](mariadb-backups-overview-for-sql-server-users.md).

Recovering existing data:

1. Dump data from the corrupter table, ordered by primary key. MariaDB could crash when it finds damaged data. Repeat the process skipping damaged data.
2. Save somewhere the table structure with [SHOW CREATE TABLE](../../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md).
3. Restart MariaDB.
4. Drop the table with [DROP TABLE](../../../../reference/sql-statements/data-definition/drop/drop-table.md).
5. Recreate the table and restore the dump.

For more details, see [InnoDB Recovery Modes](../../../../server-usage/storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes.md).

### Aria and MyISAM

[MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) is not crash-safe. In case of a MariaDB crash, the changes applied to MyISAM tables but not yet flushed to the disk are lost.

[Aria](../../../../server-usage/storage-engines/aria/) is crash-safe by default, which means that in case of a crash, after repairing any table that is damaged, no changes are lost. However, Aria tables are not crash-safe if created with `TRANSACTIONAL=0` or `ROW_FORMAT` set to `FIXED` or `DYNAMIC`.

System tables use the Aria storage engine and they are crash-safe.

To check if a MyISAM/Aria table is corrupted, we can use [CHECK TABLE](../../../../reference/sql-statements/table-statements/check-table.md). To repair a MyISAM/Aria table, one can use [REPAIR TABLE](../../../../reference/sql-statements/table-statements/repair-table.md). Before running `REPAIR TABLE` against big tables, consider increasing [myisam\_repair\_threads](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_repair_threads) or [aria\_repair\_threads](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_repair_threads).

MyISAM and Aria tables can also be automatically repaired when corruption is detected. This is particularly useful for Aria, in case corrupted system tables prevent MariaDB from starting. See [myisam\_recover\_options](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options) and [aria\_recover\_options](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_recover_options). By default Aria runs the quickest repair type. Occasionally, to repair a system table, we may have to start MariaDB in this way:

```
mysqld --aria-recover-options=BACKUP,FORCE
```

It is also possible to stop MariaDB and repair MyISAM tables with [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md), and Aria tables with [aria\_chk](../../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md). With default values, a repair can be unnecessarily very slow. Before running these tools, be sure to check the [Memory and Disk Use With myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/memory-and-disk-use-with-myisamchk.md) page.

### Other Storage Engines

Notes on the different storage engines:

* For [MyRocks](../../../../server-usage/storage-engines/myrocks/), see [MyRocks and CHECK TABLE](../../../../server-usage/storage-engines/myrocks/myrocks-and-check-table.md).
* With [ARCHIVE](../../../../server-usage/storage-engines/archive.md), `REPAIR TABLE` also improves the compression rate.
* For [CSV](../../../../server-usage/storage-engines/csv/), see [Checking and Rpairing CSV Tables](../../../../server-usage/storage-engines/csv/checking-and-repairing-csv-tables.md).
* Some special storage engines, like [MEMORY](../../../../server-usage/storage-engines/memory-storage-engine.md) or [BLACKHOLE](../../../../server-usage/storage-engines/blackhole.md), do not support any form of check and repair.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
