---
description: >-
  Understand backup locking stages. This page explains how mariadb-backup uses
  BACKUP STAGE statements to minimize locking during operation.
---

# mariadb-backup and BACKUP STAGE

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

The [BACKUP STAGE](../../../reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) statements make it possible to make an efficient external backup tool. How `mariadb-backup` uses these statements depends on the version of MariaDB Server it is bundled with.

Every release of MariaDB Enterprise Server uses all of the `BACKUP STAGE` statements to do the work described below. MariaDB Community Server gained the same behavior in MariaDB Community Server 10.11.8, 11.0.6, 11.1.5, 11.2.4, and 11.4.2, and in every release since. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).

{% hint style="info" %}
The change landed in a maintenance release of each series, so the version series alone does not tell you which behavior you get. Releases before those listed above use the older behavior, as do all releases in the 10.6 series and earlier and all releases in the 11.3 series.
{% endhint %}

{% include "../../../.gitbook/includes/for-a-complete-list-of-mari....md" %}

## `BACKUP STAGE` Before MariaDB Community Server 10.11.8

In these releases, the [BACKUP STAGE](../../../reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) statements are supported, but `mariadb-backup` does not use them in the most efficient way. It simply executes the following `BACKUP STAGE` statements to lock the database:

```sql
BACKUP STAGE START;
BACKUP STAGE BLOCK_COMMIT;
```

When the backup is complete, it executes the following `BACKUP STAGE` statement to unlock the database:

```sql
BACKUP STAGE END;
```

{% hint style="info" %}
To use a version of `mariadb-backup` that uses the [BACKUP STAGE](../../../reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) statements in the most efficient way, upgrade to MariaDB Community Server 10.11.8, 11.0.6, 11.1.5, 11.2.4, or 11.4.2 or later, or use MariaDB Enterprise Server.
{% endhint %}

### Tasks Performed Prior to `BACKUP STAGE`

* Copy some transactional tables.
  * InnoDB (i.e. `ibdataN` and file extensions `.ibd` and `.isl`)
* Copy the tail of some transaction logs.
  * The tail of the InnoDB redo log (i.e. `ib_logfileN` files) are copied for InnoDB tables.

### `BACKUP STAGE START`

`mariadb-backup` does not perform any tasks in the `START` stage.

### `BACKUP STAGE FLUSH`

`mariadb-backup` does not perform any tasks in the `FLUSH` stage.

### `BACKUP STAGE BLOCK_DDL`

`mariadb-backup` does not perform any tasks in the `BLOCK_DDL` stage.

### `BACKUP STAGE BLOCK_COMMIT`

`mariadb-backup` performs the following tasks in the `BLOCK_COMMIT` stage:

* Copy other files.
  * i.e. file extensions `.frm`, `.isl`, `.TRG`, `.TRN`, `.opt`, `.par`
* Copy some transactional tables.
  * Aria (i.e. `aria_log_control` and file extensions `.MAD` and `.MAI`)
* Copy the non-transactional tables.
  * `MyISAM` (i.e. file extensions `.MYD` and `.MYI`)
  * `MERGE` (i.e. file extensions `.MRG`)
  * `ARCHIVE` (i.e. file extensions `.ARM` and `.ARZ`)
  * `CSV` (i.e. file extensions `.CSM` and `.CSV`)
* Create a MyRocks checkpoint using the `rocksdb_create_checkpoint` system variable.
* Copy the tail of some transaction logs.
  * The tail of the InnoDB redo log (i.e. `ib_logfileN` files) are copied for InnoDB tables.
* Save the binary log position to `xtrabackup_binlog_info`.
* Save the Galera Cluster state information to `xtrabackup_galera_info`.

### `BACKUP STAGE END`

`mariadb-backup` performs the following tasks in the `END` stage:

* Copy the MyRocks checkpoint into the backup.

## `BACKUP STAGE` in MariaDB Enterprise Server and MariaDB Community Server 10.11.8 and Later

The following sections describe how `mariadb-backup` uses each [BACKUP STAGE](../../../reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage.md) statement in an efficient way.

### `BACKUP STAGE START`

`mariadb-backup` performs the following tasks in the `START` stage:

* Copy all transactional tables.
  * InnoDB (i.e. `ibdataN` and file extensions `.ibd` and `.isl`)
  * Aria (i.e. `aria_log_control` and file extensions `.MAD` and `.MAI`)
* Copy the tail of all transaction logs.
  * The tail of the InnoDB redo log (i.e. `ib_logfileN` files) are copied for InnoDB tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) are copied for Aria tables.

### `BACKUP STAGE FLUSH`

`mariadb-backup` performs the following tasks in the `FLUSH` stage:

* Copy all non-transactional tables that are not in use. This list of used tables is found with `SHOW OPEN TABLES`.
  * `MyISAM` (i.e. file extensions `.MYD` and `.MYI`)
  * `MERGE` (i.e. file extensions `.MRG`)
  * `ARCHIVE` (i.e. file extensions `.ARM` and `.ARZ`)
  * `CSV` (i.e. file extensions `.CSM` and `.CSV`)
* Copy the tail of all transaction logs.
  * The tail of the InnoDB redo log (i.e. `ib_logfileN` files) are copied for InnoDB tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) are copied for Aria tables.

### `BACKUP STAGE BLOCK_DDL`

`mariadb-backup` performs the following tasks in the `BLOCK_DDL` stage:

* Copy other files.
  * i.e. file extensions `.frm`, `.isl`, `.TRG`, `.TRN`, `.opt`, `.par`
* Copy the non-transactional tables that were in use during `BACKUP STAGE FLUSH`.
  * `MyISAM` (i.e. file extensions `.MYD` and `.MYI`)
  * `MERGE` (i.e. file extensions `.MRG`)
  * `ARCHIVE` (i.e. file extensions `.ARM` and `.ARZ`)
  * `CSV` (i.e. file extensions `.CSM` and `.CSV`)
* Check `ddl.log` for DDL executed before the `BLOCK DDL` stage.
  * The file names of newly created tables can be read from `ddl.log`.
  * The file names of dropped tables can also be read from `ddl.log`.
  * The file names of renamed tables can also be read from `ddl.log`, so the files can be renamed instead of re-copying them.
* Copy changes to system log tables.
  * mysql.general\_log
  * mysql.slow\_log
  * This is easy as these are append only.
* Copy the tail of all transaction logs.
  * The tail of the InnoDB redo log (i.e. `ib_logfileN` files) are copied for InnoDB tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) are copied for Aria tables.

### `BACKUP STAGE BLOCK_COMMIT`

`mariadb-backup` performs the following tasks in the `BLOCK_COMMIT` stage:

* Create a MyRocks checkpoint using the rocksdb\_create\_checkpoint system variable.
* Copy changes to system log tables.
  * mysql.general\_log
  * mysql.slow\_log
  * This is easy as these are append only.
* Copy changes to statistics tables.
  * mysql.table\_stats
  * mysql.column\_stats
  * mysql.index\_stats
* Copy the tail of all transaction logs.
  * The tail of the InnoDB redo log (i.e. `ib_logfileN` files) are copied for InnoDB tables.
  * The tail of the Aria redo log (i.e. `aria_log.N` files) are copied for Aria tables.
* Save the binary log position to `xtrabackup_binlog_info`.
* Save the Galera Cluster state information to `xtrabackup_galera_info`.

### `BACKUP STAGE END`

`mariadb-backup` performs the following tasks in the `END` stage:

* Copy the MyRocks checkpoint into the backup.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
