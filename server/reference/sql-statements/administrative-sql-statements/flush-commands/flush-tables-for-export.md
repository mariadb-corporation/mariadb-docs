---
description: >-
  Prepare individual tables for binary backup. This command flushes changes to
  disk and locks tables, allowing safe copying of .ibd files while the server
  runs.
---

# FLUSH TABLES FOR EXPORT

## Syntax

```sql
FLUSH TABLE[S] table_name [, table_name] FOR EXPORT
```

## Description

`FLUSH TABLES ... FOR EXPORT` flushes changes to the specified tables to disk so that binary copies can be made while the server is still running. This works for [Archive](../../../../server-usage/storage-engines/archive.md), [Aria](../../../../server-usage/storage-engines/aria/), [CSV](../../../../server-usage/storage-engines/csv/), [InnoDB](../../../../server-usage/storage-engines/innodb/), [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) and [MERGE](../../../../server-usage/storage-engines/merge.md) tables.

The table is read locked until you issue [UNLOCK TABLES](../../transactions/transactions-unlock-tables.md).

If a storage engine does not support `FLUSH TABLES FOR EXPORT`, a 1031 error ([SQLSTATE](../../programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) 'HY000') is produced.

If `FLUSH TABLES ... FOR EXPORT` is in effect in the session, the following statements will produce an error if attempted:

* `FLUSH TABLES WITH READ LOCK`
* `FLUSH TABLES ... WITH READ LOCK`
* `FLUSH TABLES ... FOR EXPORT`
* Any statement trying to update any table

If any of the following statements is in effect in the session, attempting `FLUSH TABLES ... FOR EXPORT` will produce an error.

* `FLUSH TABLES ... WITH READ LOCK`
* `FLUSH TABLES ... FOR EXPORT`
* `LOCK TABLES ... READ`
* `LOCK TABLES ... WRITE`

`FLUSH FOR EXPORT` is not written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/).

This statement requires the [RELOAD](../../account-management-sql-statements/grant.md#global-privileges) and the [LOCK TABLES](../../account-management-sql-statements/grant.md#database-privileges) privileges.

If one of the specified tables cannot be locked, none of the tables will be locked.

If a table does not exist, an error like the following will be produced:

```
ERROR 1146 (42S02): Table 'test.xxx' doesn't exist
```

If a table is a view, an error like the following will be produced:

```
ERROR 1347 (HY000): 'test.v' is not BASE TABLE
```

## Example

```sql
FLUSH TABLES test.t1 FOR EXPORT;
#  Copy files related to the table (see below)
UNLOCK TABLES;
```

For a full description, please see [copying MariaDB tables](../../../../server-usage/tables/copying-tables-between-different-mariadb-databases-and-mariadb-servers.md).

## See Also

* [FLUSH TABLES](flush.md)
* [Copying Tables Between Different MariaDB Databases and MariaDB Servers](../../../../server-usage/tables/copying-tables-between-different-mariadb-databases-and-mariadb-servers.md)
* [Copying Transportable InnoDB Tablespaces](../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces)
* [myisampack](../../../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) - Compressing the MyISAM data file for easier distribution.
* [aria\_pack](../../../../clients-and-utilities/aria-clients-and-utilities/aria_pack.md) - Compressing the Aria data file for easier distribution

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
