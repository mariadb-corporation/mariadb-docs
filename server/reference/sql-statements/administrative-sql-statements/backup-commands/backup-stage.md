---
description: >-
  Control backup phases for external tools. Learn how to cycle through stages
  like START, BLOCK_DDL, and BLOCK_COMMIT to perform consistent backups with
  minimal locking.
---

# BACKUP STAGE

The `BACKUP STAGE` commands are a set of commands to make it possible to make an efficient external backup tool.

## Syntax

```sql
BACKUP STAGE [START | FLUSH | BLOCK_DDL | BLOCK_COMMIT | END ]
```

In the following text, a transactional table means InnoDB, or specifically an InnoDB-like engine with redo log that can lock redo purges and can be copied without locks by an outside process.

## Goals with BACKUP STAGE Commands

* To be able to do a majority of the backup with the minimum possible server locks. Especially for transactional tables (InnoDB, MyRocks etc) there is only need for a very short block of new commits while copying statistics and log tables.
* DDL are only needed to be blocked for a very short duration of the backup while [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/) is copying the tables affected by DDL during the initial part of the backup.
* Most non transactional tables (those that are not in use) will be copied during `BACKUP STAGE START`. The exceptions are system statistic and log tables that are not blocked during the backup until `BLOCK_COMMIT`.
* Should work efficiently with backup tools that use disk snapshots.
* Should work as efficiently as possible for all table types that store data on the local disks.
* As little copying as possible under higher level stages/locks. For example, .frm (dictionary) and .trn (trigger) files should be copying while copying the table data.

## `BACKUP STAGE` Commands

### `BACKUP STAGE START`

The `START` stage is designed for the following tasks:

* Blocks purge of redo files for storage engines that needs this (Aria)
* Start logging of DDL commands into 'datadir'/ddl.log. This may take a short time as the command has to wait until there are no active DDL commands.

### `BACKUP STAGE FLUSH`

The `FLUSH` stage is designed for the following tasks:

* FLUSH all changes for inactive non-transactional tables, except for statistics and log tables.
* Close all tables that are not in use, to ensure they are marked as closed for the backup.
* BLOCK all new write locks for all non transactional tables (except statistics and log tables). The command will not wait for tables that are in use by read-only transactions.

DDLs don't have to be blocked at this stage as they can't cause the table to be in an inconsistent state. This is true also for non-transactional tables.

### `BACKUP STAGE BLOCK_DDL`

The `BLOCK_DDL` stage is designed for the following tasks:

* Wait for all statements using write locked non-transactional tables to end.
* Blocks [CREATE TABLE](../../data-definition/create/create-table.md), [DROP TABLE](../../data-definition/drop/drop-table.md), [TRUNCATE TABLE](../../table-statements/truncate-table.md), and [RENAME TABLE](../../data-definition/rename-table.md).
* Blocks also start off a new [ALTER TABLE](../../data-definition/alter/alter-table/) and the final rename phase of [ALTER TABLE](../../data-definition/alter/alter-table/). Running ALTER TABLES are not blocked.

### `BACKUP STAGE BLOCK_COMMIT`

The `BLOCK_COMMIT` stage is designed for the following tasks:

* Lock the binary log and commit/rollback to ensure that no changes are committed to any tables. If there are active commits or data to be copied to the binary log this will be allowed to finish. Active transactions will not affect `BLOCK_COMMIT`.
* This doesn't lock temporary tables that are not used by replication. However these will be blocked when it's time to write to the binary log.
* Lock system log tables and statistics tables, flush them and mark them closed.

When the `BLOCK_COMMIT`'s stages return, this is the 'backup time'. Everything committed will be in the backup and everything not committed will roll back.

Transactional engines will continue to do changes to the redo log during the `BLOCK COMMIT` stage, but this is not important as all of these will roll back later as the changes will not be committed.

### `BACKUP STAGE END`

The `END` stage is designed for the following tasks:

* End DDL logging
* Free resources

## Using `BACKUP STAGE` Commands with Backup Tools

### Using `BACKUP STAGE` Commands with mariadb-backup

{% tabs %}
{% tab title="Current" %}
The `BACKUP STAGE` commands are a set of commands to make it possible to make an efficient external backup tool.
{% endtab %}

{% tab title="< 11.2.4 / 11.1.5 / 11.0.6" %}
The `BACKUP STAGE` commands are a set of commands to make it possible to make an efficient external backup tool. How [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/) uses these commands depends on which version you are using. It depends on whether you are using the version that is bundled with MariaDB Community Server or the version that is bundled with [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-enterprise-server/README.md).
{% endtab %}

{% tab title="< 10.11.8" %}
The `BACKUP STAGE` commands are a set of commands to make it possible to make an efficient external backup tool. How [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/) uses these commands depends on which version you are using. It depends on whether you are using the version that is bundled with MariaDB Community Server or the version that is bundled with [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-enterprise-server/README.md).
{% endtab %}
{% endtabs %}

See [mariadb-backup and BACKUP STAGE Commands](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/mariadb-backup-and-backup-stage-commands.md) for some examples on how [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/) uses these commands.

### Using `BACKUP STAGE` Commands with Storage Snapshots

The `BACKUP STAGE` commands are a set of commands to make it possible to make an efficient external backup tool. These commands could even be used by tools that perform backups by taking a snapshot of a file system, SAN, or some other kind of storage device. See [Storage Snapshots and BACKUP STAGE Commands](storage-snapshots-and-backup-stage-commands.md) for some examples on how to use each `BACKUP STAGE` command in an efficient way.

## Privileges

`BACKUP STAGE` requires the [RELOAD](../../account-management-sql-statements/grant.md) privilege.

## Notes

* Only one connection can run `BACKUP STAGE START`. If a second connection tries, it will wait until the first one has executed `BACKUP STAGE END`.
* If the user skips a `BACKUP STAGE`, then all intermediate backup stages will automatically be run. This will allow us to add new stages within the `BACKUP STAGE` hierarchy in the future with even more precise locks without causing problems for tools using an earlier version of the `BACKUP STAGE` implementation.
* One can use the [max\_statement\_time](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_statement_time) or [lock\_wait\_timeout](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout) system variables to ensure that a `BACKUP STAGE` command doesn't block the server too long.
* DDL logging is only be available from [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes) and [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes), or in [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-enterprise-server/README.md).
* A disconnect will automatically release backup stages.
* There is no easy way to see which is the current stage.

## See Also

* [BACKUP LOCK](backup-lock.md) Locking a table from DDL.
* [MDEV-5336](https://jira.mariadb.org/browse/MDEV-5336). Implement BACKUP STAGE for safe external backups.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
