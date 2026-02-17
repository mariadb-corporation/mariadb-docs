---
description: >-
  Complete MariaDB backup and recovery guide. Complete resource for backup
  methods, mariabackup usage, scheduling, and restoration for production use.
---

# Backup and Restore Overview

This article briefly discusses the main ways to backup MariaDB. For detailed descriptions and syntax, see the individual pages. More detail is in the process of being added.

## Logical vs Physical Backups

Logical backups consist of the SQL statements necessary to restore the data, such as [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md), [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) and [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md).

Physical backups are performed by copying the individual data files or directories.

The main differences are as follows:

* logical backups are more flexible, as the data can be restored on other hardware configurations, MariaDB versions or even on another DBMS, while physical backups cannot be imported on significantly different hardware, a different DBMS, or potentially even a different MariaDB version.
* logical backups can be performed at the level of database and table, while physical databases are the level of directories and files. In the [MyISAM](../storage-engines/myisam-storage-engine/) and [InnoDB](../storage-engines/innodb/) storage engines, each table has an equivalent set of files.
* logical backups are larger in size than the equivalent physical backup.
* logical backups takes more time to both backup and restore than the equivalent physical backup.
* log files and configuration files are not part of a logical backup

## Backup Tools

### `mariadb-backup`

The mariadb-backup program is a physical online backup tool and a fork of Percona XtraBackup with added support for compression and data-at-rest encryption.

#### **Storage Engines and Backup Types**

MariaDB Backup creates a file-level backup of data from the MariaDB Server data directory. This backup includes temporal data, and the encrypted and unencrypted tablespaces of supported storage engines (e.g., InnoDB, MyRocks, Aria).

MariaDB Server implements:

* Full backups, which contain all data in the database.
* Incremental backups, which contain modifications since the last backup.
* Partial backups, which contain a subset of the tables in the database.

Backup support is specific to storage engines. All supported storage engines enable full backup. The InnoDB storage engine additionally supports incremental backup.

#### **Non-Blocking Backups**

A feature of MariaDB Backup and MariaDB Server, non-blocking backups minimize workload impact during backups. When MariaDB Backup connects to MariaDB Server, staging operations are initiated to protect data during read.

Non-blocking backup functionality differs from historical backup functionality in the following ways:

* MariaDB Backup includes optimizations to backup staging, including DDL statement tracking, which reduces lock-time during backups.
* MariaDB Backup in MariaDB Community Server 10.4 and later will block writes, log tables, and statistics.
* Older releases used `FLUSH TABLES WITH READ LOCK`, which closed open tables and only allowed tables to be reopened with a read lock during the duration of backups.

#### **Understanding Recovery**

Full backups produced using MariaDB Server are not initially point-in-time consistent, and an attempt to restore from a raw full backup will cause InnoDB to crash to protect the data. Incremental backups contain only the changes since the last backup and cannot be used standalone to perform a restore.

To restore from a backup, you first need to prepare the backup for point-in-time consistency using the `--prepare` command:

* Running `--prepare` on a _full backup_ synchronizes the tablespaces, ensuring they are point-in-time consistent.
* Running `--prepare` on an _incremental backup_ synchronizes the tablespaces and applies the updated data into the previous full backup.
* Running `--prepare` on data used for a _partial restore_ requires the `--export` option to create the necessary `.cfg` files.

#### **Restore Requires Empty Data Directory**

For MariaDB Backup to safely restore data from full and incremental backups, the data directory must be empty. When MariaDB Backup restores from a backup using `--copy-back` or `--move-back`, it copies or moves the backup files into the MariaDB Server data directory.

#### **Creating the Backup User**

When MariaDB Backup performs a backup operation, it connects to the running MariaDB Server to manage locks and backup staging that prevent the Server from writing to a file while being read. It is recommended that a dedicated user be created and authorized to perform backups:

```sql
CREATE USER 'mariabackup'@'localhost' IDENTIFIED BY 'mbu_passwd';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR
      ON * TO 'mariabackup'@'localhost';
```

{% hint style="info" %}
While MariaDB Backup requires a user for backup operations, no user is required for restore operations since restores occur while MariaDB Server is not running.
{% endhint %}

### `mariadb-dump`

[mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) (previously mysqldump) performs a logical backup. It is the most flexible way to perform a backup and restore, and a good choice when the data size is relatively small.

For large datasets, the backup file can be large, and the restore time lengthy.

`mariadb-dump` dumps the data into SQL format (it can also dump into other formats, such as CSV or XML) which can then easily be imported into another database. The data can be imported into other versions of MariaDB, MySQL, or even another DBMS entirely, assuming there are no version or DBMS-specific statements in the dump.

mariadb-dump dumps triggers along with tables, as these are part of the table definition. However, [stored procedures](../stored-routines/stored-procedures/), [views](../views/), and [events](../triggers-events/event-scheduler/events.md) are not, and need extra parameters to be recreated explicitly (for example, `--routines` and `--events`). [Procedures](../stored-routines/stored-procedures/) and [functions](../../reference/sql-functions/) are however also part of the system tables (for example [mysql.proc](../../reference/system-tables/the-mysql-database-tables/mysql-proc-table.md)).

#### InnoDB Logical Backups

InnoDB uses the [buffer pool](../storage-engines/innodb/innodb-buffer-pool.md), which stores data and indexes from its tables in memory. This buffer is very important for performance. If InnoDB data doesn't fit the memory, it is important that the buffer contains the most frequently accessed data. However, last accessed data is candidate for insertion into the buffer pool. If not properly configured, when a table scan happens, InnoDB may copy the whole contents of a table into the buffer pool. The problem with logical backups is that they always imply full table scans.

An easy way to avoid this is by increasing the value of the [innodb\_old\_blocks\_time](../storage-engines/innodb/innodb-system-variables.md#innodb_old_blocks_time) system variable. It represents the number of milliseconds that must pass before a recently accessed page can be put into the "new" sublist in the buffer pool. Data which is accessed only once should remain in the "old" sublist. This means that they will soon be evicted from the buffer pool. Since during the backup process the "old" sublist is likely to store data that is not useful, one could also consider resizing it by changing the value of the [innodb\_old\_blocks\_pct](../storage-engines/innodb/innodb-system-variables.md#innodb_old_blocks_pct) system variable.

It is also possible to explicitly dump the buffer pool on disk before starting a logical backup, and restore it after the process. This will undo any negative change to the buffer pool which happens during the backup. To dump the buffer pool, the [innodb\_buffer\_pool\_dump\_now](../storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_dump_now) system variable can be set to `ON`. To restore it, the [innodb\_buffer\_pool\_load\_now](../storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_now) system variable can be set to `ON`.

#### `mariadb-dump` Examples

Backing up a single database

```bash
mariadb-dump db_name > backup-file.sql
```

Restoring or loading the database

```bash
mariadb db_name < backup-file.sql
```

See the [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) page for detailed syntax and examples.

### `mariadb-hotcopy`

[mariadb-hotcopy](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-hotcopy.md) performs a physical backup, and works only for backing up [MyISAM](../storage-engines/myisam-storage-engine/) and [ARCHIVE](../storage-engines/archive.md) tables. It can only be run on the same machine as the location of the database directories.

#### `mariadb-hotcopy` Examples

```bash
mariadb-hotcopy db_name [/path/to/new_directory]
mariadb-hotcopy db_name_1 ... db_name_n /path/to/new_directory
```

### Percona XtraBackup

Percona XtraBackup is **not supported** in MariaDB. [mariadb-backup](mariadb-backup/) is the recommended backup method to use instead of Percona XtraBackup. See [Percona XtraBackup Overview: Compatibility with MariaDB](../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md#compatibility-with-mariadb) for more information.

[Percona XtraBackup](../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) is a tool for performing fast, hot backups. It was designed specifically for [XtraDB/InnoDB](../storage-engines/innodb/) databases, but can be used with any storage engine (although not with [encryption](../../security/encryption/data-at-rest-encryption/) and [compression](../storage-engines/innodb/innodb-page-compression.md)). It is not included with MariaDB.

### Filesystem Snapshots

Some filesystems, like Veritas, support snapshots. During the snapshot, the table must be locked. The proper steps to obtain a snapshot are:

* From the [mariadb](../../clients-and-utilities/mariadb-client/) client, execute [FLUSH TABLES WITH READ LOCK](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md). The client must remain open.
* From a shell, execute `mount vxfs snapshot`
* The client can execute [UNLOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md).
* Copy the snapshot files.
* From a shell, unmount the snapshot with `umount snapshot`.

### LVM

Widely-used physical backup method, using a Perl script as a wrapper. See [http://www.lenzg.net/mylvmbackup/](http://www.lenzg.net/mylvmbackup/) for more information.

### Percona TokuBackup

For details, see:

* [TokuDB Hot Backup – Part 1](https://www.percona.com/blog/2013/09/12/tokudb-hot-backup-part-1/)
* [TokuDB Hot Backup – Part 2](https://www.percona.com/blog/2013/09/19/tokudb-hot-backup-part-2/)
* [TokuDB Hot Backup Now a MySQL Plugin](https://www.percona.com/blog/2015/02/05/tokudb-hot-backup-now-mysql-plugin/)

### dbForge Studio for MySQL

Besides the system utilities, it is possible to use third-party GUI tools to perform backup and restore operations. In this context, it is worth mentioning dbForge Studio for MySQL, a feature-rich database IDE that is fully compatible with MariaDB and delivers extensive backup functionality.

The backup and restore module of the Studio allows precise [configuration and management of full and partial backups](backup-and-restore-via-dbforge-studio.md) up to particular database objects. The feature of scheduling regular backups offers specific settings to handle errors and keep a log of them. Additionally, settings and configurations can be saved for later reuse.

These operations are wizard-aided allowing users to set up all tasks in a visual mode.

## See Also

* [Streaming MariaDB backups in the cloud](https://mariadb.com/blog/streaming-mariadb-backups-cloud) (mariadb.com blog)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
