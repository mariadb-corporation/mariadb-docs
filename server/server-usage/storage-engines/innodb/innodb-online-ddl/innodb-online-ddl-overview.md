# InnoDB Online DDL Overview

InnoDB tables support online DDL, which permits concurrent DML and uses optimizations to avoid unnecessary table copying.

The [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) statement supports two clauses that are used to implement online DDL:

* [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) - This clause controls how the DDL operation is performed.
* [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) - This clause controls how much concurrency is allowed while the DDL operation is being performed.

## Alter Algorithms

InnoDB supports multiple algorithms for performing DDL operations. This offers a significant performance improvement over previous versions. The supported algorithms are:

* `DEFAULT` - This implies the default behavior for the specific operation.
* `COPY`
* `INPLACE`
* `NOCOPY` - This was added in [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes).
* `INSTANT` - This was added in [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes).

## Specifying an Alter Algorithm

The set of alter algorithms can be considered as a hierarchy. The hierarchy is ranked in the following order, with _least efficient_ algorithm at the top, and _most efficient_ algorithm at the bottom:

* `COPY`
* `INPLACE`
* `NOCOPY`
* `INSTANT`

When a user specifies an alter algorithm for a DDL operation, MariaDB does not necessarily use that specific algorithm for the operation. It interprets the choice in the following way:

* If the user specifies `COPY`, then InnoDB uses the `COPY` algorithm.
* If the user specifies any other algorithm, then InnoDB interprets that choice as the least efficient algorithm that the user is willing to accept. This means that if the user specifies `INPLACE`, then InnoDB will use the most efficient algorithm supported by the specific operation from the set (`INPLACE`, `NOCOPY`, `INSTANT`). Likewise, if the user specifies `NOCOPY`, then InnoDB will use the most efficient algorithm supported by the specific operation from the set (`NOCOPY`, `INSTANT`).

There is also a special value that can be specified:

* If the user specifies `DEFAULT`, then InnoDB uses its default choice for the operation. The default choice is to use the most efficient algorithm supported by the operation. The default choice will also be used if no algorithm is specified. Therefore, if you want InnoDB to use the most efficient algorithm supported by an operation, then you usually do not have to explicitly specify any algorithm at all.

### Specifying an Alter Algorithm Using the ALGORITHM Clause

InnoDB supports the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause.

The [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause can be used to specify the _least efficient_ algorithm that the user is willing to accept. It is supported by the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) and [CREATE INDEX](../../../../reference/sql-statements/data-definition/create/create-index.md) statements.

For example, if a user wanted to add a column to a table, but only if the operation used an algorithm that is at least as efficient as the `INPLACE`, then they could execute the following:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50)
);

ALTER TABLE tab ADD COLUMN c VARCHAR(50), ALGORITHM=INPLACE;
```

The above operation should use the `INSTANT` algorithm, because the `ADD COLUMN` operation supports the `INSTANT` algorithm, and the `INSTANT` algorithm is more efficient than the `INPLACE` algorithm.

### Specifying an Alter Algorithm Using System Variables

The [alter\_algorithm](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm) system variable can be used to pick the _least efficient_ algorithm that the user is willing to accept.

For example, if a user wanted to add a column to a table, but only if the operation used an algorithm that is at least as efficient as the `INPLACE`, then they could execute the following:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50)
);

SET SESSION alter_algorithm='INPLACE';
ALTER TABLE tab ADD COLUMN c VARCHAR(50);
```

The above operation would actually use the `INSTANT` algorithm, because the `ADD COLUMN` operation supports the `INSTANT` algorithm, and the `INSTANT` algorithm is more efficient than the `INPLACE` algorithm.\
<>

## Supported Alter Algorithms

The supported algorithms are described in more details below.

### DEFAULT Algorithm

The default behavior, which occurs if `ALGORITHM=DEFAULT` is specified, or if `ALGORITHM` is not specified at all, usually only makes a copy if the operation doesn't support being done in-place at all. In this case, the _most efficient_ available algorithm will usually be used.

This means that, if an operation supports the `INSTANT` algorithm, then it will use that algorithm by default. If an operation does not support the `INSTANT` algorithm, but it does support the `NOCOPY` algorithm, then it will use that algorithm by default. If an operation does not support the `NOCOPY` algorithm, but it does support the `INPLACE` algorithm, then it will use that algorithm by default.

### COPY Algorithm

The `COPY` algorithm refers to the original [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) algorithm.

When the `COPY` algorithm is used, MariaDB essentially does the following operations:

```sql
-- Create a temporary table with the new definition
CREATE TEMPORARY TABLE tmp_tab (
...
);

-- Copy the data from the original table
INSERT INTO tmp_tab
   SELECT * FROM original_tab;

-- Drop the original table
DROP TABLE original_tab;

-- Rename the temporary table, so that it replaces the original one
RENAME TABLE tmp_tab TO original_tab;
```

This algorithm is very inefficient, but it is generic, so it works for all storage engines.

If the `COPY` algorithm is specified with the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause or with the [alter\_algorithm](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm) system variable, then the `COPY` algorithm will be used even if it is not necessary. This can result in a lengthy table copy. If multiple [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operations are required that each require the table to be rebuilt, then it is best to specify all operations in a single [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) statement, so that the table is only rebuilt once.

#### Using the COPY Algorithm with InnoDB

If the `COPY` algorithm is used with an [InnoDB](../) table, then the following statements apply:

* The table will be rebuilt using the current values of the [innodb\_file\_per\_table](../innodb-system-variables.md#innodb_file_per_table), [innodb\_file\_format](../innodb-system-variables.md#innodb_file_format), and [innodb\_default\_row\_format](../innodb-system-variables.md#innodb_default_row_format) system variables.
* The operation will have to create a temporary table to perform the table copy. This temporary table will be in the same directory as the original table, and it's file name will be in the format `#sql${PID}_${THREAD_ID}_${TMP_TABLE_COUNT}`, where `${PID}` is the process ID of `mysqld`, `${THREAD_ID}` is the connection ID, and `${TMP_TABLE_COUNT}` is the number of temporary tables that the connection has open. Therefore, the [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) may contain files with file names like `#sql1234_12_1.ibd`.
* The operation inserts one record at a time into each index, which is very inefficient.
* InnoDB does not use a sort buffer.
* The table copy operation creates a lot fewer [InnoDB undo log](../innodb-undo-log.md) writes. See [MDEV-11415](https://jira.mariadb.org/browse/MDEV-11415) for more information.
* The table copy operation creates a lot of [InnoDB redo log](../innodb-redo-log.md) writes.

### INPLACE Algorithm

The `COPY` algorithm can be incredibly slow, because the whole table has to be copied and rebuilt. The `INPLACE` algorithm was introduced as a way to avoid this by performing operations in-place and avoiding the table copy and rebuild, when possible.

When the `INPLACE` algorithm is used, the underlying storage engine uses optimizations to perform the operation while avoiding the table copy and rebuild. However, `INPLACE` is a bit of a misnomer, since some operations may still require the table to be rebuilt for some storage engines. Regardless, several operations can be performed without a full copy of the table for some storage engines.

A more accurate name for the algorithm would have been the `ENGINE` algorithm, since the [storage engine](../../) decides how to implement the algorithm.

If an [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operation supports the `INPLACE` algorithm, then it can be performed using optimizations by the underlying storage engine, but it may rebuilt.

If the `INPLACE` algorithm is specified with the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause or with the [alter\_algorithm](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm) system variable and if the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operation does not support the `INPLACE` algorithm, then an error will be raised. For example:

```sql
SET SESSION alter_algorithm='INPLACE';

ALTER TABLE tab MODIFY COLUMN c INT;
ERROR 1846 (0A000): ALGORITHM=INPLACE is not supported. Reason: Cannot change column type INPLACE. Try ALGORITHM=COPY
```

In this case, raising an error is preferable, if the alternative is for the operation to make a copy of the table, and perform unexpectedly slowly.

#### Using the INPLACE Algorithm with InnoDB

If the `INPLACE` algorithm is used with an [InnoDB](../) table, then the following statements apply:

* The operation might have to write sort files in the directory defined by the [innodb\_tmpdir](../innodb-system-variables.md#innodb_tmpdir) system variable.
* The operation might also have to write a temporary log file to track data changes by [DML queries](../../../../reference/sql-statements/data-manipulation/) executed during the operation. The maximum size for this log file is configured by the [innodb\_online\_alter\_log\_max\_size](../innodb-system-variables.md#innodb_online_alter_log_max_size) system variable.
* Some operations require the table to be rebuilt, even though the algorithm is inaccurately called "in-place". This includes operations such as adding or dropping columns, adding a primary key, changing a column to [NULL](../../../../reference/data-types/null-values.md), etc.
* If the operation requires the table to be rebuilt, then the operation might have to create temporary tables.
  * It may have to create a temporary intermediate table for the actual table rebuild operation.
    * This temporary table will be in the same directory as the original table, and it's file name will be in the format `#sql${PID}_${THREAD_ID}_${TMP_TABLE_COUNT}`, where `${PID}` is the process ID of `mysqld`, `${THREAD_ID}` is the connection ID, and `${TMP_TABLE_COUNT}` is the number of temporary tables that the connection has open. Therefore, the [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) may contain files with file names like `#sql1234_12_1.ibd`.
  * When it replaces the original table with the rebuilt table, it may also have to rename the original table using a temporary table name.
    * The [innodb\_safe\_truncate](../innodb-system-variables.md#innodb_safe_truncate) system variable is set to `OFF`, then the format will actually be `#sql-ib${TABLESPACE_ID}-${RAND}`, where `${TABLESPACE_ID}` is the table's tablespace ID within InnoDB and `${RAND}` is a randomly initialized number. Therefore, the [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) may contain files with file names like `#sql-ib230291-1363966925.ibd`.
* The storage needed for the above items can add up to the size of the original table, or more in some cases.
* Some operations are instantaneous, if they only require the table's metadata to be changed. This includes operations such as renaming a column, changing a column's [DEFAULT](../../../../reference/sql-statements/data-definition/create/create-table.md#default-column-option) value, etc.

#### Operations Supported by InnoDB with the `INPLACE` Algorithm

With respect to the allowed operations, the `INPLACE` algorithm supports a subset of the operations supported by the `COPY` algorithm, and it supports a superset of the operations supported by the `NOCOPY` algorithm.

See [InnoDB Online DDL Operations with ALGORITHM=INPLACE](innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md) for more information.

### NOCOPY Algorithm

The `NOCOPY` algorithm is supported. The `INPLACE` algorithm can sometimes be surprisingly slow in instances where it has to rebuild the clustered index, because when the clustered index has to be rebuilt, the whole table has to be rebuilt. The `NOCOPY` algorithm was introduced as a way to avoid this.

If an [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operation supports the `NOCOPY` algorithm, then it can be performed without rebuilding the clustered index.

If the `NOCOPY` algorithm is specified with the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause or with the [alter\_algorithm](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm) system variable and if the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operation does not support the `NOCOPY` algorithm, then an error will be raised. For example:

```sql
SET SESSION alter_algorithm='NOCOPY';

ALTER TABLE tab MODIFY COLUMN c INT;
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Cannot change column type INPLACE. Try ALGORITHM=COPY
```

In this case, raising an error is preferable, if the alternative is for the operation to rebuild the clustered index, and perform unexpectedly slowly.

#### Operations Supported by InnoDB with the `NOCOPY` Algorithm

With respect to the allowed operations, the `NOCOPY` algorithm supports a subset of the operations supported by the `INPLACE` algorithm, and it supports a superset of the operations supported by the `INSTANT` algorithm.

See [InnoDB Online DDL Operations with ALGORITHM=NOCOPY](innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md) for more information.

### INSTANT Algorithm

The `INSTANT` algorithm is supported. The `INPLACE` algorithm can sometimes be surprisingly slow in instances where it has to modify data files. The `INSTANT` algorithm was introduced as a way to avoid this.

If an [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operation supports the `INSTANT` algorithm, then it can be performed without modifying any data files.

If the `INSTANT` algorithm is specified with the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause or with the [alter\_algorithm](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm) system variable and if the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operation does not support the `INSTANT` algorithm, then an error will be raised. For example:

```sql
SET SESSION alter_algorithm='INSTANT';

ALTER TABLE tab MODIFY COLUMN c INT;
ERROR 1846 (0A000): ALGORITHM=INSTANT is not supported. Reason: Cannot change column type INPLACE. Try ALGORITHM=COPY
```

In this case, raising an error is preferable, if the alternative is for the operation to modify data files, and perform unexpectedly slowly.

#### Operations Supported by InnoDB with the INSTANT Algorithm

With respect to the allowed operations, the `INSTANT` algorithm supports a subset of the operations supported by the `NOCOPY` algorithm.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

## Alter Locking Strategies

InnoDB supports multiple locking strategies for performing DDL operations. This offers a significant performance improvement over previous versions. The supported locking strategies are:

* `DEFAULT` - This implies the default behavior for the specific operation.
* `NONE`
* `SHARED`
* `EXCLUSIVE`

Regardless of which locking strategy is used to perform a DDL operation, InnoDB will have to exclusively lock the table for a short time at the start and end of the operation's execution. This means that any active transactions that may have accessed the table must be committed or aborted for the operation to continue. This applies to most DDL statements, such as [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md), [CREATE INDEX](../../../../reference/sql-statements/data-definition/create/create-index.md), [DROP INDEX](../../../../reference/sql-statements/data-definition/drop/drop-index.md), [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md), [RENAME TABLE](../../../../reference/sql-statements/data-definition/rename-table.md), etc.

## Specifying an Alter Locking Strategy

### Specifying an Alter Locking Strategy Using the `LOCK` Clause

The [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) statement supports the [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) clause.

The [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) clause can be used to specify the locking strategy that the user is willing to accept. It is supported by the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) and [CREATE INDEX](../../../../reference/sql-statements/data-definition/create/create-index.md) statements.

For example, if a user wanted to add a column to a table, but only if the operation is non-locking, then they could execute the following:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50)
);

ALTER TABLE tab ADD COLUMN c VARCHAR(50), ALGORITHM=INPLACE, LOCK=NONE;
```

If the [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) clause is not explicitly set, then the operation uses `LOCK=DEFAULT`.

### Specifying an Alter Locking Strategy Using `ALTER ONLINE TABLE`

[ALTER ONLINE TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md#alter-online-table) is equivalent to `LOCK=NONE`. Therefore, the [ALTER ONLINE TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-online-ddl/alter-online-table/README.md) statement can be used to ensure that your [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) operation allows all concurrent DML.

## Supported Alter Locking Strategies

The supported algorithms are described in more details below.

To see which locking strategies InnoDB supports for each operation, see the pages that describe which operations are supported for each algorithm:

* [InnoDB Online DDL Operations with ALGORITHM=INPLACE](innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md)
* [InnoDB Online DDL Operations with ALGORITHM=NOCOPY](innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md)
* [InnoDB Online DDL Operations with ALGORITHM=INSTANT](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md)

### DEFAULT Locking Strategy

The default behavior, which occurs if `LOCK=DEFAULT` is specified, or if `LOCK` is not specified at all, acquire the least restrictive lock on the table that is supported for the specific operation. This permits the maximum amount of concurrency that is supported for the specific operation.

### NONE Locking Strategy

The `NONE` locking strategy performs the operation without acquiring any lock on the table. This permits **all** concurrent DML.

If this locking strategy is not permitted for an operation, then an error is raised.

### SHARED Locking Strategy

The `SHARED` locking strategy performs the operation after acquiring a read lock on the table. This permit **read-only** concurrent DML.

If this locking strategy is not permitted for an operation, then an error is raised.

### EXCLUSIVE Locking Strategy

The `EXCLUSIVE` locking strategy performs the operation after acquiring a write lock on the table. This does **not** permit concurrent DML.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
