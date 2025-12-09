---
description: >-
  Maps SQL Server backup concepts like differential and transaction log backups
  to MariaDB equivalents such as `mariadb-backup` (hot backups) and binary logs
  for incremental recovery.
---

# MariaDB Backups Overview for SQL Server Users

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

MariaDB has the following types of backups:

* Logical backups (dumps).
* Hot backups with mariadb-backup.
* Snapshots.
* Incremental backups.

## Logical Backups (Dumps)

A _dump_, also called a _logical backup_, consists of the SQL statements needed to recreate MariaDB databases and their data into another server. A dump is the slowest form of backup to restore, because it implies executing all the SQL statements needed to recreate data. However it is also the most flexible, because restoring will work on any MariaDB version, because the SQL syntax is usually compatible. It is even possible to restore a dump into an older version, though the incompatible syntax (new features) will be ignored. Under certain conditions, MariaDB dumps may also be restored on other DBMSs, including SQL Server.

The compatibility between different versions and technologies is achieved by using [executable comments](../../../../reference/sql-statements/comment-syntax.md), but we should be aware of how they work. If we use a feature introduced in version 11.1, for example, it will be included in the dump inside an executable comment. If we restore that backup on a server with [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), the 11.1 feature will be ignored. This is the only way to restore backups in older MariaDB versions.

### `mariadb-dump`

Logical backups are usually taken with [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) (previously called mysqldump).

mariadb-dump allows one to dump all databases, a single database, or a set of tables from a database. It is even possible to specify a `WHERE` clause, which under certain circumstances allows to obtain incremental dumps.

For consistency reasons, when using the default storage engine [InnoDB](understanding-mariadb-architecture.md#innodb), it is important to use the `--single-transaction` option. This will read all data in a single transaction. It's important however to understand that long transactions may have a big impact on performance.

The `--master-data` option adds the statements to setup a slave to the dump.

MariaDB also supports statements which make easy to write applications to obtain custom types of dumps. For most `CREATE <object_type>` statement, a corresponding `SHOW CREATE <object_type>` exists. For example, [SHOW CREATE TABLE](../../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) returns the `CREATE TABLE` statement that can be used to recreate a certain table, without data.

### `mydumper`

[mydumper](https://github.com/maxbube/mydumper) is a 3rd party tools to take dumps from MariaDB and MySQL databases. It is much faster than `mariadb-dump` because it takes backups with several parallel threads, usually one thread for each available CPU core. It produces several files, that can be used to restore a database using the related tool myloader.

Since is it a 3rd party tool, it could be incompatible with some present or future MariaDB features.

## Hot Backups (`mariadb-backup`)

`mariadb-backup` is a tool for taking a backup of MariaDB files while MariaDB is working. A lock is only held for a small amount of time, so it is suitable to backup a server without causing disruptions. It works by taking corrupted backups and then bringing them to a consistent state by using the [InnoDB undo log](../../../../server-usage/storage-engines/innodb/innodb-undo-log.md). `mariadb-backup` also properly backups [MyRocks](../../../../server-usage/storage-engines/myrocks/) tables and non-transactional storage engines.

## Cold Backups and Snapshots

A copy of all MariaDB files is a working backup. Therefore, the easiest way to backup a dataset is to shutdown the server and copy all its files. It will be entirely possible to start another server with a copy of those files. This is often referred to as a _cold backup_. However, in most cases we don't want to do this, because it implies downtime for the server: it will not be working at least for the time necessary to copy the files.

Snapshots are usually a better idea, as they are a consistent copy of the files at a given moment in time, taken without stopping the normal operations.

A snapshot of the files can be taken at several levels: filesystem level, if the filesystem supports snapshots, for example `zfs`; Linux Logical Volume Manager (LVM) also supports snapshots; and virtual machines also allow one to take snapshots. Windows shadow copies are also snapshots, with a benefit: it is possible to restore a single file from a shadow copy. A snapshot is not an expensive operation, because it does not imply a copy of the files. The current files will not be modified anymore, and changes to them will be written in separate places.

The problem with snapshots is that they behave like a logical copy of the files as they are in a given point in time. But database files are not guaranteed to be consistent in every moment, because contents can be buffered before being flushed to the disk. You can think a database snapshot like a database after an operating system crash.

With non-transactional tables, some data is typically lost. Data changes that are present in a buffer before the snapshot, but not written on a disk, cannot be recovered in any way. Data changes in transactional tables, like InnoDB tables, can always be recovered after restoring a snapshot (or after a crash), as long as a commit was done. Tables will still need to be repaired, just like it happens after an SQL Server crash.

Snapshots can be taken while MariaDB is running. To restore them, stop MariaDB first - or kill the process, because you don't really care of the consequences in this case. Then restore a snapshot and start MariaDB again.

For more information about snapshots, check your filesystem, LVM or virtual machine documentation.

## Incremental Backups

The term incremental backup in MariaDB indicates what SQL Server calls a [_differential backup_](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/differential-backups-sql-server). An important difference is that in SQL Server such backups are based on the [transaction log](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/transaction-log-backups-sql-server), which wouldn't be possible in MariaDB because transaction logs are handled at storage engine level.

As mentioned [here](understanding-mariadb-architecture.md#the-binary-log), MariaDB can use the [binary log](../../../server-monitoring-logs/binary-log/) instead for backup purposes. Such incremental backups can be done manually. This means that:

* The binary log files are copied just like any other regular file.
* To copy those files it is necessary to have the proper permissions at filesystem level, not in MariaDB.
* Backups do not expire until we delete the last needed complete backup.

### Replaying the Binary Log

The page [Using mariadb-binlog](../../../../clients-and-utilities/logging-tools/mariadb-binlog/using-mariadb-binlog.md) shows how to use the mariadb-binlog utility to replay a binary log file.

The page also shows how to edit the binary log before replaying it. This allows one to undo an SQL statement that was executed by mistake, for example a `DROP TABLE` against a wrong table. The high level procedure is the following:

* Restore a backup that is older than the SQL statement to undo.
* Use `mariadb-binlog` to generate a file with the SQL statements that were executed after the backup.
* Edit the SQL file, erasing the unwanted statement.
* Run the SQL file.

### Incremental Backups with mariadb-backup

The simplest way to take an incremental backup is to use mariadb-backup. This tool is able to take and restore incremental backups. For the complete procedure to use, see [Incremental Backup and Restore with mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup.md).

mariadb-backup can run on both Linux and Windows systems.

### Flashback

[Flashback](../../../server-monitoring-logs/binary-log/flashback.md) is a feature that allows one to bring all databases, some databases or some tables back to a certain point in time. This can only be done if the binary log is enabled. Flashback is not a proper backup, but it can be used to restore a certain set of data.

### Copying Individual Tables

It is entirely possible to restore a single table from a physical backup, or to copy the table to another server.

With the [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) storage engine it was very easy to move tables between different servers, as long as the MySQL or MariaDB version was the same.

[InnoDB](../../../../server-usage/storage-engines/innodb/) is nowadays the default storage engine, and it is more complex, as it supports transactions for example. It still supports restoring a table from a physical file, this feature is called _transportable tablespaces_. There is a particular procedure to follow, and some limitations. This is basically the MariaDB equivalent of detaching and re-attaching tables in SQL Server.

For more information, see [InnoDB File-Per-Table Tablespaces](../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md).

By default. all table files are located in the _data directory_, which is defined by the system variable [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir). There may be exceptions, because a table's files can be located elsewhere using the [DATA DIRECTORY and INDEX DIRECTORY](../../../../reference/sql-statements/data-definition/create/create-table.md#data-directoryindex-directory) options in `CREATE TABLE`.

Regardless of the storage engine used, each table's structure is generally stored in a file with the `.frm` extension.

The files used for [partitioned tables](../../../../server-usage/partitioning-tables/) are different from the files used for non-partitioned tables. See [Partitions Files](../../../../server-usage/partitioning-tables/partitions-files.md) for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
