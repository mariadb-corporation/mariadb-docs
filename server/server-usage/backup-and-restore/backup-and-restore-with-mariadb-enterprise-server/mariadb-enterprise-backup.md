---
description: >-
  This page details MariaDB Enterprise Backup, an enhanced version of
  mariadb-backup with enterprise-specific optimizations and support.
---

# MariaDB Enterprise Backup

## Overview

Regular and reliable backups are essential to successful recovery of mission critical applications. [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) backup and restore operations are performed using MariaDB Enterprise Backup, an enterprise-build of [MariaDB Backup](../mariadb-backup/).

MariaDB Enterprise Backup is compatible with MariaDB Enterprise Server.

## Storage Engines and Backup Types

MariaDB Backup creates a file-level backup of data from the MariaDB Community Server data directory. This backup includes [temporal data](../../../reference/sql-structure/temporal-tables/), and the encrypted and unencrypted tablespaces of supported storage engines (e.g., [InnoDB](../../storage-engines/innodb/), [MyRocks](../../storage-engines/myrocks/), [Aria](../../storage-engines/aria/)).

MariaDB Enterprise Server implements:

* Full backups, which contain all data in the database.
* Incremental backups, which contain modifications since the last backup.
* Partial backups, which contain a subset of the tables in the database.

Backup support is specific to storage engines. All supported storage engines enable full backup. The InnoDB storage engine additionally supports incremental backup.

**Note:** MariaDB Enterprise Backup does not support backups of MariaDB ColumnStore. Backup of MariaDB ColumnStore can be performed using [MariaDB ColumnStore Tools](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/management/columnstore-system/mariadb-columnstore-backup-and-restore/backup-and-restore-for-mariadb-columnstore-110). Backup of data ingested to MariaDB ColumnStore can also occur pre-ingestion, such as in the case of HTAP where backup could occur of transactional data in MariaDB Enterprise Server, and restore of data to MariaDB ColumnStore would then occur through reprocessing..

## Nonblocking Backups

A feature of MariaDB Enterprise Backup and MariaDB Enterprise Server, non-blocking backups minimize workload impact during backups. When MariaDB Enterprise Backup connects to MariaDB Enterprise Server, staging operations are initiated to protect data during read.

Non-blocking backup functionality differs from historical backup functionality in the following ways:

* MariaDB Enterprise Backup in MariaDB Enterprise Server includes enterprise-only optimizations to backup staging, including DDL statement tracking, which reduces lock-time during backups.
* MariaDB Backup in MariaDB Community Server 10.4 and later will block writes, log tables, and statistics.
* Older MariaDB Community Server releases used FLUSH TABLES WITH READ LOCK, which closed open tables and only allowed tables to be reopened with a read lock during the duration of backups.

## Understanding Recovery

MariaDB Enterprise Backup creates complete or incremental backups of MariaDB Enterprise Server data, and is also used to restore data from backups produced using MariaDB Enterprise Backup.

### Preparing Backups for Recovery

Full backups produced using MariaDB Enterprise Server are not initially point-in-time consistent, and an attempt to restore from a raw full backup will cause InnoDB to crash to protect the data.

Incremental backups produced using MariaDB Enterprise Backup contain only the changes since the last backup and cannot be used standalone to perform a restore.

To restore from a backup, you first need to prepare the backup for point-in-time consistency using the `--prepare` command:

* Running the `--prepare` command on a full backup synchronizes the tablespaces, ensuring that they are point-in-time consistent and ready for use in recovery.
* Running the `--prepare` command on an incremental backup synchronizes the tablespaces and also applies the updated data into the previous full backup, making it a complete backup ready for use in recovery.
* Running the `--prepare` command on data that is to be used for a partial restore (when restoring only one or more selected tables) requires that you also use the `--export` option to create the necessary `.cfg` files to use in recovery.

### Restore Requires Empty Data Directory

When MariaDB Enterprise Backup restores from a backup, it copies or moves the backup files into the MariaDB Enterprise Server data directory, as defined by the datadir system variable.

For MariaDB Backup to safely restore data from full and incremental backups, the data directory must be empty. One way to achieve this is to move the data directory aside to a unique directory name:

1. Make sure that the Server is stopped.
2. Move the data directory to a unique name (e.g., `/var/lib/mysql-2020-01-01`) OR remove the old data directory (depending on how much space you have available).
3. Create a new (empty) data directory (e.g., `mkdir /var/lib/mysql)`.
4. Run MariaDB Backup to restore the databases into that directory.
5. Change the ownership of all the restored files to the correct system user (e.g., `chown -R mysql:mysql /var/lib/mysql`).
6. Start MariaDB Enterprise Server, which now uses the restored data directory.
7. When ready, and if you have not already done so, delete the old data directory to free disk space.

## Creating the Backup User

When MariaDB Backup performs a backup operation, it not only copies files from the data directory but also connects to the running MariaDB Enterprise Server.

This connection to MariaDB Enterprise Server is used to manage locks that prevent the Server from writing to a file while being read for a backup.

MariaDB Backup establishes this connection based on the user credentials specified with the `--user` and `--password` options when performing a backup.

It is recommended that a dedicated user be created and authorized to perform backups.

{% tabs %}
{% tab title="Current" %}
MariaDB Backup requires this user to have the `RELOAD, PROCESS, LOCK TABLES,` and `REPLICATION CLIENT` privileges.

```sql
CREATE USER 'mariadb-backup'@'localhost'
IDENTIFIED BY 'mbu_passwd';

GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR
ON *.*
TO 'mariadb-backup'@'localhost';
```

In the above example, MariaDB Backup would run on the local system that runs MariaDB Enterprise Server. Where backups may be run against a remote server, the user authentication and authorization should be adjusted.

While MariaDB Backup requires a user for backup operations, no user is required for restore operations since restores occur while MariaDB Enterprise Server is not running.
{% endtab %}

{% tab title="< 10.5" %}
MariaDB Backup requires this user to have the `RELOAD, PROCESS, LOCK TABLES,` and `REPLICATION CLIENT` privileges.

```sql
CREATE USER 'mariadb-backup'@'localhost'
IDENTIFIED BY 'mbu_passwd';

GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT
ON *.*
TO 'mariadb-backup'@'localhost';
```

In the above example, MariaDB Backup would run on the local system that runs MariaDB Enterprise Server. Where backups may be run against a remote server, the user authentication and authorization should be adjusted.

While MariaDB Backup requires a user for backup operations, no user is required for restore operations since restores occur while MariaDB Enterprise Server is not running.
{% endtab %}
{% endtabs %}

## Full Backup and Restore

Full backups performed with MariaDB Backup contain all table data present in the database.

When performing a full backup, MariaDB Backup makes a file-level copy of the MariaDB Enterprise Server data directory. This backup omits log data such as the binary logs (binlog), error logs, general query logs, and slow query logs.

### Performing Full Backups

When you perform a full backup, MariaDB Backup writes the backup to the `--target-dir` path. The directory must be empty or non-existent and the operating system user account must have permission to write to that directory. A database user account is required to perform the backup.

The version of `mariadb-backup` or `mariadb-backup` should be the same version as the MariaDB Enterprise Server version. When the version does not match the server version, errors can sometimes occur, or the backup can sometimes be unusable.

To create a backup, execute mariadb-backup or mariadb-backup with the `--backup` option, and provide the database user account credentials using the `--user` and `--password` options:

```bash
sudo mariadb-backup --backup \
      --target-dir=/data/backups/full \
      --user=mariadb-backup \
      --password=mbu_passwd
```

Subsequent to the above example, the backup is now available in the designated `--target-dir` path.

### Preparing a Full Backup for Recovery

A raw full backup is not [point-in-time consistent](mariadb-enterprise-backup.md#point-in-time-recoveries) and must be prepared before it can be used for a restore. The backup can be prepared any time after the backup is created and before the backup is restored. However, MariaDB recommends preparing a backup immediately after taking the backup to ensure that the backup is consistent.

The backup should be prepared with the same version of MariaDB Backup that was used to create the backup.

To prepare the backup, execute mariadb-backup or mariadb-backup with the `--prepare` option:

```bash
sudo mariadb-backup --prepare \
   --use-memory=34359738368 \
   --target-dir=/data/backups/full
```

For best performance, the `--use-memory` option should be set to the server's `innodb_buffer_pool_size` value.

### Restoring from Full Backups

Once a full backup has been prepared to be point-in-time consistent, MariaDB Backup is used to copy backup data to the MariaDB Enterprise Server data directory.

To restore from a full backup:

1. Stop the MariaDB Enterprise Server
2. Empty the data directory
3. Restore from the "full" directory using the `--copy-back` option:

```bash
mariadb-backup --copy-back --target-dir=/data/backups/full
```

MariaDB Backup writes to the data directory as the current user, which can be changed using `sudo`. To confirm that restored files are properly owned by the user that runs MariaDB Enterprise Server, run a command like this (adapted for the correct user/group):

```bash
chown -R mysql:mysql /var/lib/mysql
```

Once this is done, start MariaDB Enterprise Server:

```bash
sudo systemctl start mariadb
```

When the Server starts, it works from the restored data directory.

## Incremental Backup and Restore

Full backups of large data-sets can be time-consuming and resource-intensive. MariaDB Backup supports the use of incremental backups to minimize this impact.

While full backups are resource-intensive at time of backup, the resource burden around incremental backups occurs when preparing for restore. First, the full backup is prepared for restore, then each incremental backup is applied.

### Performing Incremental Backups

When you perform an incremental backup, MariaDB Backup compares a previous full or incremental backup to what it finds on MariaDB Community Server. It then creates a new backup containing the incremental changes.

Incremental backup is supported for InnoDB tables. Tables using other storage engines receive full backups even during incremental backup operations.

To increment a full backup, use the `--incremental-basedir` option to indicate the path to the full backup and the `--target-dir` option to indicate where you want to write the incremental backup:

```bash
mariadb-backup --backup \
      --incremental-basedir=/data/backups/full \
      --target-dir=/data/backups/inc1 \
      --user=mariadb-backup \
      --password=mbu_passwd
```

In this example, MariaDB Backup reads the `/data/backups/full directory`, and MariaDB Enterprise Server then creates an incremental backup in the `/data/backups/inc1` directory.

### Preparing an Incremental Backup

An incremental backup must be applied to a prepared full backup before it can be used in a restore operation. If you have multiple full backups to choose from, pick the nearest full backup prior to the incremental backup that you want to restore. You may also want to back up your full-backup directory, as it are modified by the updates in the incremental data.

If your full backup directory is not yet prepared, run this to make it consistent:

```bash
mariadb-backup --prepare --target-dir=/data/backups/full
```

Then, using the prepared full backup, apply the first incremental backup's data to the full backup in an incremental preparation step:

```bash
mariadb-backup --prepare \
      --target-dir=/data/backups/full \
      --incremental-dir=/data/backups/inc1
```

Once the incremental backup has been applied to the full backup, the full backup directory contains the changes from the incremental backup (that is, the inc1/ directory). Feel free to remove inc1/ to save disk space.

### Restoring from Incremental Backups

Once you have prepared the full backup directory with all the incremental changes you need (as described above), stop the MariaDB Community Server, [Empty](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/backing-up-and-restoring-databases/backup-and-restore-with-mariadb-enterprise-server/mariadb-backup-enterprise-docs/README.md#restore-requires-empty-data-directory) its data directory, and restore from the original full backup directory using the --copy-back option:

```bash
mariadb-backup --copy-back --target-dir=/data/backups/full
```

MariaDB Backup writes files into the data directory using either the current user or root (in the case of a sudo operation), which may be different from the system user that runs the database. Run the following to recursively update the ownership of the restored files and directories:

```bash
chown -R mysql:mysql /var/lib/mysql
```

Then, start MariaDB Enterprise Server. When the Server starts, it works from the restored data directory.

## Partial Backup and Restore

In a partial backup, MariaDB Backup copies a specified subset of tablespaces from the MariaDB Enterprise Server data directory. Partial backups are useful in establishing a higher frequency of backups on specific data, at the expense of increased recovery complexity. In selecting tablespaces for a partial backup, please consider referential integrity.

### Performing a Partial Backup

Command-line options can be used to narrow the set of databases or tables to be included within a backup:

| Option                | Description                                   |
| --------------------- | --------------------------------------------- |
| `--databases`         | List of databases to include                  |
| `--databases-exclude` | List of databases to omit from the backup     |
| `--databases-file`    | Path to file listing the databases to include |
| `--tables`            | List of tables to include                     |
| `--tables-exclude`    | List of tables to exclude                     |
| `--tables-file`       | Path to file listing the tables to include    |

For example, you may wish to produce a partial backup, which excludes a specific database:

```bash
mariadb-backup --backup \
      --target-dir=/data/backups/part \
      --user=mariadb-backup \
      --password=mbu_passwd \
      --database-exclude=test
```

Partial backups can also be incremental:

```bash
mariadb-backup --backup \
      --incremental-basedir=/data/backups/part \
      --target-dir=/data/backups/part_inc1 \
      --user=mariadb-backup \
      --password=mbu_passwd  \
      --database-exclude=test
```

### Preparing a Backup Before a Partial Restore

As with full and incremental backups, partial backups are not point-in-time consistent. A partial backup must be prepared before it can be used for recovery.

A partial restore can be performed from a full backup or partial backup.

The preparation step for either partial or full backup restoration requires the use of transportable tablespaces for InnoDB. As such, each prepare operation requires the --export option:

```bash
mariadb-backup --prepare --export --target-dir=/data/backups/part
```

When using a partial incremental backup for restore, the incremental data must be applied to its prior partial backup data before its data is complete. If performing partial incremental backups, run the prepare statement again to apply the incremental changes onto the partial backup that served as the base.

```bash
mariadb-backup --prepare --export \
      --target-dir=/data/backups/part \
      --incremental-dir=/data/backups/part_inc1
```

### Performing a Partial Restore

Unlike full and incremental backups, you cannot restore partial backups directly using MariaDB Backup. Further, as a partial backup does not contain a complete data directory, you cannot restore MariaDB Community Server to a startable state solely with a partial backup.

To restore from a partial backup, you need to prepare a table on the MariaDB Community Server, then manually copy the files into the data directory.

The details of the restore procedure depend on the characteristics of the table:

* [Partial Restore Non-partitioned Tables](mariadb-enterprise-backup.md#partial-restore-non-partitioned-tables)
* [Partial Restore Partitioned Tables](mariadb-enterprise-backup.md#partial-restore-partitioned-tables)
* [Partial Restore of Tables with Full-Text Indexes](mariadb-enterprise-backup.md#partial-restore-of-tables-with-full-text-indexes)

As partial restores are performed while the server is running, not stopped, care should be taken to prevent production workloads during restore activity.

**Note:** You can also use data from a full backup in a partial restore operation if you have prepared the data using the `--export` option as described above.

### Partial Restore Nonpartitioned Tables

To restore a non-partitioned table from a backup, first create a new table on MariaDB Community Server to receive the restored data. It should match the specifications of the table you're restoring.

Be extra careful if the backup data is from a server with a different version than the restore server, as some differences (such as a differing `ROW_FORMAT`) can cause an unexpected result.

1. Create an empty table for the data being restored:

```sql
CREATE TABLE test.address_book (
   id INT PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(255),
   email VARCHAR(255));
```

2. Modify the table to discard the tablespace:

```sql
ALTER TABLE test.address_book DISCARD TABLESPACE;
```

3. You can copy (or move) the files for the table from the backup to the data directory:

```bash
# cp /data/backups/part_inc1/test/address_book.* /var/lib/mysql/test
```

4. Use a wildcard to include both the .ibd and .cfg files. Then, change the owner to the system user running MariaDB Community Server:

```bash
# chown mysql:mysql /var/lib/mysql/test/address_book.*
```

5. Lastly, import the new tablespace:

```sql
ALTER TABLE test.address_book IMPORT TABLESPACE;
```

MariaDB Community Server looks in the data directory for the tablespace you copied in, then imports it for use. If the table is encrypted, it also looks for the encryption key with the relevant key ID that the table data specifies.

6. Repeat this step for every table you wish to restore.

### Partial Restore Partitioned Tables

Restoring a partitioned table from a backup requires a few extra steps compared to restoring a non-partitioned table.

To restore a partitioned table from a backup, first create a new table on MariaDB Community Server to receive the restored data. It should match the specifications of the table you're restoring, including the partition specification.

Be extra careful if the backup data is from a server with a different version than the restore server, as some differences (such as a differing ROW\_FORMAT) can cause an unexpected result.

1. Create an empty table for the data being restored:

```sql
CREATE TABLE test.students (
   id INT PRIMARY KEY AUTO_INCREMENT
   name VARCHAR(255),
   email VARCHAR(255),
   graduating_year YEAR)
PARTITION BY RANGE (graduating_year) (
   PARTITION p9 VALUES LESS THAN 2019
   PARTITION p1 VALUES LESS THAN MAXVALUE
);
```

2. Then create a second empty table matching the column specification, but without partitions. This is your working table:

```sql
CREATE TABLE test.students_work AS
SELECT * FROM test.students WHERE NULL;
```

3. For each partition you want to restore, discard the working table's tablespace:

```sql
ALTER TABLE test.students_work DISCARD TABLESPACE;
```

4. Then, copy the table files from the backup, using the new name:

```bash
# cp /data/backups/part_inc1/test/students.ibd /var/lib/mysql/test/students_work.ibd
# cp /data/backups/part_inc1/test/students.cfg /var/lib/mysql/test/students_work.cfg
```

5. Change the owner to that of the user running MariaDB Community Server:

```bash
# chown mysql:mysql /var/lib/mysql/test/students_work.*
```

6. Import the copied tablespace:

```sql
ALTER TABLE test.students_work IMPORT TABLESPACE;
```

7. Lastly, exchange the partition, copying the tablespace from the working table into the partition file for the target table:

```sql
ALTER TABLE test.students EXCHANGE PARTITION p0 WITH TABLE test.students_work;
```

8. Repeat the above process for each partition until you have them all exchanged into the target table. Then delete the working table, as it's no longer necessary:

```sql
DROP TABLE test.students_work;
```

This restores a partitioned table.

### Partial Restore of Tables with Full-Text Indexes

When restoring a table with a full-text search (FTS) index, InnoDB may throw a schema mismatch error.

In this case, to restore the table, it is recommended to:

* Remove the corresponding .cfg file.
* Restore data to a table without any secondary indexes including FTS.
* Add the necessary secondary indexes to the restored table.

For example, to restore table t1 with FTS index from database db1:

1. In the MariaDB shell, drop the table you are going to restore:

```sql
DROP TABLE IF EXISTS db1.t1;
```

2. Create an empty table for the data being restored:

```sql
CREATE TABLE db1.t1(f1 CHAR(10)) ENGINE=INNODB;
```

3. Modify the table to discard the tablespace:

```sql
ALTER TABLE db1.t1 DISCARD TABLESPACE;
```

4. In the operating system shell, copy the table files from the backup to the data directory of the corresponding database:

```bash
$ sudo cp /data/backups/part/db1/t1.* /var/lib/mysql/db1
```

5. Remove the .cfg file from the data directory:

```bash
$ sudo rm /var/lib/mysql/db1/t1.cfg
```

6. Change the owner of the newly copied files to the system user running MariaDB Community Server:

```bash
$ sudo chown mysql:mysql /var/lib/mysql/db1/t1.*
```

7. In the MariaDB shell, import the copied tablespace:

```sql
ALTER TABLE db1.t1 IMPORT TABLESPACE;
```

8. Verify that the data has been successfully restored:

```sql
SELECT * FROM db1.t1;
```

```
+--------+
| f1     |
+--------+
| ABC123 |
+--------+
```

9. Add the necessary secondary indexes:

```sql
ALTER TABLE db1.t1 FORCE, ADD FULLTEXT INDEX f_idx(f1);
```

10. The table is now fully restored:

```sql
SHOW CREATE TABLE db1.t1\G
```

```
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `f1` char(10) DEFAULT NULL,
  FULLTEXT KEY `f_idx` (`f1`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

## Point-in-Time Recoveries

Point-in-time recovery (PITR) is [documented here](../mariadb-backup/point-in-time-recovery-pitr-mariadb-backup.md).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
