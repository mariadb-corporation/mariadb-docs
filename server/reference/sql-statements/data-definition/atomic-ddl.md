---
description: >-
  Learn about crash-safe DDL operations in MariaDB. This feature ensures data
  definition statements are either fully committed or completely rolled back,
  preventing metadata inconsistency.
---

# Atomic DDL

{% tabs %}
{% tab title="Current" %}
We improved readability for DDL (Data Definition Language) operations to make most of them atomic, and the rest crash-safe, even if the server crashes in the middle of an operation.
{% endtab %}

{% tab title="Background" %}
These improvements were made in [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes).
{% endtab %}
{% endtabs %}

The design of Atomic/Crash-safe DDL ([MDEV-17567](https://jira.mariadb.org/browse/MDEV-17567)) allows it to work with all storage engines.

## Definitions

* Atomic means that either the operation succeeds (and is logged to the [binary log](../../../server-management/server-monitoring-logs/binary-log/) or is completely reversed.
* Crash-safe means that in case of a crash, after the server has restarted, all tables are consistent, there are no temporary files or tables on disk and the binary log matches the status of the server.
* DDL Data definition language.
* DML Data manipulation language.
* 'DDL recovery log' or 'DDL log' for short, is the new log file, `ddl_recovery.log` by default, that stores all DDL operations in progress. This is used to recover the state of the server in case of sudden crash.

## Background

Before 10.6, in case of a crash, there was a small possibility that one of the following things could happen:

* There could be temporary tables starting with `#sql-alter` or `#sql-shadow` or temporary files ending with '' left.
* The table in the storage engine and the table's .frm file could be out of sync.
* During a multi-table rename, only some of the tables were renamed.

## Which DDL Operations are Now Atomic

* [CREATE TABLE](create/create-table.md), except when used with [CREATE OR REPLACE](create/create-table.md), which is only crash safe.
* [RENAME TABLE](rename-table.md) and [RENAME TABLES](rename-table.md).
* [CREATE VIEW](../../../server-usage/views/create-view.md)
* [CREATE SEQUENCE](../../sql-structure/sequences/create-sequence.md)
* [CREATE TRIGGER](../../../server-usage/triggers-events/triggers/create-trigger.md)
* [DROP TRIGGER](drop/drop-trigger.md)
* [DROP TABLE](drop/drop-table.md) and [DROP VIEW](../../../server-usage/views/drop-view.md). Dropping multiple tables is only crash safe.
* [ALTER TABLE](alter/alter-table/)
* [ALTER SEQUENCE](../../sql-structure/sequences/alter-sequence.md) is not listed above as it is internally implemented as a DML.

## Which DDL Operations are Now Crash Safe

### DROP TABLE of Multiple Tables.

[DROP TABLE](drop/drop-table.md) over multiple tables is treated as if every DROP is a separate, atomic operation. This means that after a crash, all fully, or partly, dropped tables will be dropped and logged to the binary log. The undropped tables will be left untouched.

### CREATE OR REPLACE TABLE

[CREATE OR REPLACE TABLE foo](create/create-table.md) is implemented as:

```sql
DROP TABLE IF EXISTS foo;
CREATE TABLE foo ...
```

This means that if there is a crash during `CREATE TABLE` then the original table 'foo' will be dropped even if the new table was not created.\
If the table was not re-created, the binary log will contain the`DROP TABLE`.

#### DROP DATABASE

[DROP DATABASE](drop/drop-database.md) is implemented as:

```sql
  DROP TABLE table
LOOP OVER ALL tables
```

Each [DROP TABLE](drop/drop-table.md) is atomic, but in case of a crash, things will work the same way as [DROP TABLE](drop/drop-table.md) with multiple tables.

### Atomic with Different Storage Engines

Atomic/Crash-safe DDL works with all storage engines that either have atomic DDLs internally or are able to re-execute `DROP` or `RENAME` in case of failure.

This should be true for most storage engines. The ones that still need some work are:

* The [S3 storage engine](../../../server-usage/storage-engines/s3-storage-engine/).
* The [partitioning engine](../../../server-usage/partitioning-tables/). Partitioning should be atomic for most cases, but there are still some known issues that need to be tested and fixed.

### The DDL Log Recovery File

The new startup option [--log-ddl-recovery=path](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) (`ddl_recovery.log` by default) can be used to specify the place for the DDL log file. This is mainly useful in the case when one has a filesystem on persistent memory, as there is a lot of sync on this file during DDL operations.

This file contains all DDL operations that are in progress.

At MariaDB server startup, the DDL log file is copied to a file with the same base name but with a `backup.log` suffix. This is mainly done to be able to find out what went wrong if recovery fails.

If the server crashes during recovery (unlikely but possible), the recovery will continue where it was before. The recovery will retry each entry up to 3 times before giving up and proceeding with the next entry.

### Conclusions

* We believe that a clean separation of layers leads to an easier-to-maintain solution. The Atomic DDL implementation in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106) introduced minimal changes to the storage engine API, mainly for native ALTER TABLE.
* In our InnoDB implementation, no file format changes were needed on top of the RENAME undo log that was introduced in [MariaDB 10.2.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10219-release-notes) for a backup-safe TRUNCATE re-implementation. Correct use of sound design principles (write-ahead logging and transactions; also file creation now follows the ARIES protocol) is sufficient. We removed the hacks (at most one CREATE or DROP per transaction) and correctly implemented `rollback` and `purge` triggers for the InnoDB SYS\_INDEXES table.
* Numerous DDL recovery bugs in InnoDB were found and fixed quickly thanks to [rr-project.org](https://rr-project.org). We are still working on one: data files must not be deleted before the DDL transaction is committed.

Thanks to Atomic/Crash-safe DDL, the MariaDB server is now much more stable and reliable in unstable environments. There is still ongoing work to fix the few remaining issues mentioned above to make all DDL operations Atomic.

### See Also

* [MDEV-17567](https://jira.mariadb.org/browse/MDEV-17567) Atomic DDL. This MDEV entry links to all other entries related to Atomic operations that contains a lot of information how things are implemented.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
