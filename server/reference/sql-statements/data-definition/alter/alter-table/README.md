# ALTER TABLE

## Syntax

{% hint style="info" %}
In the syntax, these options are the same as for the [CREATE TABLE statement](../../create/create-table.md):

* table\_option
* column\_definition
* partition\_options
* partition\_definition
{% endhint %}

```sql
ALTER [ONLINE] [IGNORE] TABLE [IF EXISTS] tbl_name
    [WAIT n | NOWAIT]
    alter_specification [, alter_specification] ...

alter_specification:
    table_option ...
  | ADD [COLUMN] [IF NOT EXISTS] col_name column_definition
        [FIRST | AFTER col_name ]
  | ADD [COLUMN] [IF NOT EXISTS] (col_name column_definition, ...)
  | ADD {INDEX|KEY} [IF NOT EXISTS] [index_name]
        [index_type] (index_col_name,...) [index_option] ...
  | ADD [CONSTRAINT [symbol]] PRIMARY KEY [IF NOT EXISTS]
        [index_type] (index_col_name,...) [index_option] ...
  | ADD [CONSTRAINT [symbol]]
        UNIQUE [INDEX|KEY] [IF NOT EXISTS] [index_name]
        [index_type] (index_col_name,...) [index_option] ...
  | ADD FULLTEXT [INDEX|KEY] [IF NOT EXISTS [index_name]
        (index_col_name,...) [index_option] ...
  | ADD SPATIAL [INDEX|KEY] [IF NOT EXISTS [index_name]
        (index_col_name,...) [index_option] ...
  | ADD VECTOR [INDEX|KEY] [IF NOT EXISTS [index_name]
        (index_col_name,...) [index_option] ...
  | ADD [CONSTRAINT [symbol]]
        FOREIGN KEY [IF NOT EXISTS] [index_name] (index_col_name,...)
        reference_definition
  | ADD PERIOD FOR [time_period_name|SYSTEM_TIME] (start_column_name, end_column_name)
  | ALTER [COLUMN] col_name SET DEFAULT literal | (expression)
  | ALTER [COLUMN] col_name DROP DEFAULT
  | ALTER {INDEX|KEY} [IF EXISTS] index_name [NOT] IGNORED
  | CHANGE [COLUMN] [IF EXISTS] old_col_name new_col_name column_definition
        [FIRST|AFTER col_name]
  | MODIFY [COLUMN] [IF EXISTS] col_name column_definition
        [FIRST | AFTER col_name]
  | DROP [COLUMN] [IF EXISTS] col_name [RESTRICT|CASCADE]
  | DROP [CONSTRAINT] PRIMARY KEY
  | DROP {INDEX|KEY} [IF EXISTS] index_name
  | DROP FOREIGN KEY [IF EXISTS] fk_symbol
  | DROP CONSTRAINT [IF EXISTS] constraint_name
  | DISABLE KEYS
  | ENABLE KEYS
  | RENAME [TO] new_tbl_name
  | ORDER BY col_name [, col_name] ...
  | RENAME COLUMN [IF EXISTS] old_col_name TO new_col_name
  | RENAME {INDEX|KEY} old_index_name TO new_index_name
  | CONVERT TO CHARACTER SET charset_name [COLLATE collation_name]
  | [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | DISCARD TABLESPACE
  | IMPORT TABLESPACE
  | ALGORITHM [=] {DEFAULT|INPLACE|COPY|NOCOPY|INSTANT}
  | LOCK [=] {DEFAULT|NONE|SHARED|EXCLUSIVE}
  | FORCE
  | partition_options
  | CONVERT TABLE normal_table TO partition_definition [{WITH | WITHOUT} VALIDATION]
  | CONVERT PARTITION partition_name TO TABLE tbl_name
  | ADD PARTITION [IF NOT EXISTS] (partition_definition)
  | DROP PARTITION [IF EXISTS] partition_names
  | TRUNCATE PARTITION partition_names
  | COALESCE PARTITION number
  | REORGANIZE PARTITION [partition_names INTO (partition_definitions)]
  | ANALYZE PARTITION partition_names
  | CHECK PARTITION partition_names
  | OPTIMIZE PARTITION partition_names
  | REBUILD PARTITION partition_names
  | REPAIR PARTITION partition_names
  | EXCHANGE PARTITION partition_name WITH TABLE tbl_name [{WITH | WITHOUT} VALIDATION]
  | REMOVE PARTITIONING
  | ADD SYSTEM VERSIONING
  | DROP SYSTEM VERSIONING

index_col_name:
    col_name [(length)] [ASC | DESC]

index_type:
    USING {BTREE | HASH | RTREE}

index_option:
  [ KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | VISIBLE
  | COMMENT 'string'
  | CLUSTERING={YES| NO} ]
  [ IGNORED | NOT IGNORED ]

  table_option [[,] table_option] ...

```

## Description

`ALTER TABLE` enables you to change the structure of an existing table. For example, you can add or delete columns, create or destroy indexes, change the type of existing columns, or rename columns or the table itself. You can also change the comment for the table and the storage engine of the table.

If another connection is using the table, a [metadata lock](../../../transactions/metadata-locking.md) is active, and this statement will wait until the lock is released. This is also true for non-transactional tables.

When adding a `UNIQUE` index on a column (or a set of columns) which have duplicated values, an error will be produced and the statement will be stopped. To suppress the error and force the creation of `UNIQUE` indexes, discarding duplicates, the [IGNORE](../../../data-manipulation/inserting-loading-data/ignore.md) option can be specified. This can be useful if a column (or a set of columns) should be UNIQUE but it contains duplicate values; however, this technique provides no control on which rows are preserved and which are deleted. Also, note that `IGNORE` is accepted but ignored in `ALTER TABLE ... EXCHANGE PARTITION` statements.

This statement can also be used to rename a table. For details see [RENAME TABLE](../../rename-table.md).

When an index is created, the storage engine may use a configurable buffer in the process. Incrementing the buffer speeds up the index creation. [Aria](../../../../../server-usage/storage-engines/aria/) and [MyISAM](../../../../../server-usage/storage-engines/myisam-storage-engine/) allocate a buffer whose size is defined by [aria\_sort\_buffer\_size](../../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_sort_buffer_size) or [myisam\_sort\_buffer\_size](../../../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_sort_buffer_size), also used for [REPAIR TABLE](../../../table-statements/repair-table.md). [InnoDB](../../../../../server-usage/storage-engines/innodb/) allocates three buffers whose size is defined by [innodb\_sort\_buffer\_size](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_sort_buffer_size).

## Privileges

Executing the `ALTER TABLE` statement generally requires at least the [ALTER](../../../account-management-sql-statements/grant.md#table-privileges) privilege for the table or the database. If you are renaming a table, this also requires the [DROP](../../../account-management-sql-statements/grant.md#table-privileges), [CREATE](../../../account-management-sql-statements/grant.md#table-privileges) and [INSERT](../../../account-management-sql-statements/grant.md#table-privileges) privileges for the table or the database.

## Online DDL

Online DDL is supported with the [ALGORITHM](./#algorithm) and [LOCK](./#lock) clauses.

See [InnoDB Online DDL Overview](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-overview.md) for more information on online DDL with [InnoDB](../../../../../server-usage/storage-engines/innodb/).

### ALTER ONLINE TABLE

ALTER ONLINE TABLE also works for partitioned tables.

Online `ALTER TABLE` is available by executing the following:

````sql
ALTER ONLINE TABLE ...;
</code></pre>

This statement is equivalent to the following:

```sql
ALTER TABLE ... LOCK=NONE;
````

See the [LOCK](./#lock) alter specification for more information.

## WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](../../../transactions/wait-and-nowait.md).

## IF EXISTS

The `IF EXISTS` and `IF NOT EXISTS` clauses are available for the following:

```sql
ADD COLUMN       [IF NOT EXISTS]
ADD INDEX        [IF NOT EXISTS]
ADD FOREIGN KEY  [IF NOT EXISTS]
ADD PARTITION    [IF NOT EXISTS]
CREATE INDEX     [IF NOT EXISTS]
DROP COLUMN      [IF EXISTS]
DROP INDEX       [IF EXISTS]
DROP FOREIGN KEY [IF EXISTS]
DROP PARTITION   [IF EXISTS]
CHANGE COLUMN    [IF EXISTS]
MODIFY COLUMN    [IF EXISTS]
DROP INDEX       [IF EXISTS]
```

When `IF EXISTS` and `IF NOT EXISTS` are used in clauses, queries will not report errors when the condition is triggered for that clause. A warning with the same message text will be issued and the ALTER will move on to the next clause in the statement (or end if finished).

If this is directive is used after `ALTER ... TABLE`, one will not get an error if the table doesn't exist.

## Column Definitions

See [CREATE TABLE: Column Definitions](../../create/create-table.md#column-definitions) for information about column definitions.

## Index Definitions

See [CREATE TABLE: Index Definitions](../../create/create-table.md#index-definitions) for information about index definitions.

The [CREATE INDEX](../../create/create-index.md) and [DROP INDEX](../../drop/drop-index.md) statements can also be used to add or remove an index.

## Character Sets and Collations

```sql
CONVERT TO CHARACTER SET charset_name [COLLATE collation_name]
[DEFAULT] CHARACTER SET [=] charset_name
[DEFAULT] COLLATE [=] collation_name
```

See [Setting Character Sets and Collations](../../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on setting the [character sets and collations](../../../../data-types/string-data-types/character-sets/).

## Alter Specifications

### Table Options

See [CREATE TABLE: Table Options](../../create/create-table.md#table-options) for information about table options.

### ADD COLUMN

```sql
... ADD COLUMN [IF NOT EXISTS]  (col_name [column_definition](../create/create-table.md#column-definitions),...)
```

Adds a column to the table. The syntax is the same as in [CREATE TABLE](../../create/create-table.md). If you are using `IF NOT_EXISTS` the column will not be added if it was not there already. This is very useful when doing scripts to modify tables.

The `FIRST` and `AFTER` clauses affect the physical order of columns in the datafile. Use `FIRST` to add a column in the first (leftmost) position, or `AFTER` followed by a column name to add the new column in any other position. Note that, nowadays, the physical position of a column is usually irrelevant.

See also [Instant ADD COLUMN for InnoDB](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb.md).

### DROP COLUMN

```sql
... DROP COLUMN [IF EXISTS] col_name [CASCADE|RESTRICT]
```

Drops the column from the table. If you are using `IF EXISTS` you will not get an error if the column didn't exist. If the column is part of any index, the column will be dropped from them, except if you add a new column with identical name at the same time. The index will be dropped if all columns from the index were dropped. If the column was used in a view or trigger, you will get an error next time the view or trigger is accessed. Dropping a column that is part of a multi-column `UNIQUE` constraint is not permitted. For example:

```sql
CREATE TABLE a (
  a int,
  b int,
  primary key (a,b)
);

ALTER TABLE x DROP COLUMN a;
[42000][1072] Key column 'A' doesn't exist in table
```

The reason is that dropping column `a` would result in the new constraint that all values in column `b` be unique. In order to drop the column, an explicit `DROP PRIMARY KEY` and `ADD PRIMARY KEY` would be required.

MariaDB supports instant DROP COLUMN. DROP COLUMN of an indexed column would imply [DROP INDEX](../../drop/drop-index.md) (and in the case of a non-UNIQUE multi-column index, possibly ADD INDEX). These will not be allowed with [ALGORITHM=INSTANT](./#algorithm), but unlike prior versions, they can be allowed with [ALGORITHM=NOCOPY](./#algorithm)

`RESTRICT` and `CASCADE` are allowed to make porting from other database systems easier. In MariaDB, they do nothing.

### MODIFY COLUMN

Allows you to modify the type of a column. The column will be at the same place as the original column and all indexes on the column will be kept. Note that when modifying column, you should specify all attributes for the new column.

```sql
CREATE TABLE t1 (a INT UNSIGNED AUTO_INCREMENT, PRIMARY KEY((a));
ALTER TABLE t1 MODIFY a BIGINT UNSIGNED AUTO_INCREMENT;
```

### CHANGE COLUMN

Works like `MODIFY COLUMN` except that you can also change the name of the column. The column will be at the same place as the original column and all index on the column will be kept.

```sql
CREATE TABLE t1 (a INT UNSIGNED AUTO_INCREMENT, PRIMARY KEY(a));
ALTER TABLE t1 CHANGE a b BIGINT UNSIGNED AUTO_INCREMENT;
```

### ALTER COLUMN

This lets you change column options.

```sql
CREATE TABLE t1 (a INT UNSIGNED AUTO_INCREMENT, b varchar(50), PRIMARY KEY(a));
ALTER TABLE t1 ALTER b SET DEFAULT 'hello';
```

### RENAME INDEX/KEY

{% tabs %}
{% tab title="Current" %}
You can rename an index using the `RENAME INDEX` (or `RENAME KEY`) syntax, for example:

```sql
ALTER TABLE t1 RENAME INDEX i_old TO i_new;
```
{% endtab %}

{% tab title="< 10.5.3" %}
`RENAME INDEX/KEY` is not available.
{% endtab %}
{% endtabs %}

### RENAME COLUMN

{% tabs %}
{% tab title="Current" %}
You can rename a column using the `RENAME COLUMN` syntax, for example:

```sql
ALTER TABLE t1 RENAME COLUMN c_old TO c_new;
```
{% endtab %}

{% tab title="< 10.5.3" %}
`RENAME COLUMN` is not available.
{% endtab %}
{% endtabs %}

### ADD PRIMARY KEY

Adds a primary key. For `PRIMARY KEY` indexes, you can specify a name for the index, but it is silently ignored, and the name of the index is always `PRIMARY`. See [Getting Started with Indexes: Primary Key](../../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#primary-key) for more information.

### DROP PRIMARY KEY

Drops a primary key. For `PRIMARY KEY` indexes, you can specify a name for the index, but it is silently ignored, and the name of the index is always `PRIMARY`. See [Getting Started with Indexes: Primary Key](../../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#primary-key) for more information.

### ADD FOREIGN KEY

Adds a foreign key. For `FOREIGN KEY` indexes, a reference definition must be provided. For `FOREIGN KEY` indexes, you can specify a name for the constraint, using the `CONSTRAINT` keyword. That name will be used in error messages.

First, you have to specify the name of the target (parent) table and a column or a column list which must be indexed and whose values must match to the foreign key's values. The `MATCH` clause is accepted to improve the compatibility with other DBMS's, but has no meaning in MariaDB. The `ON DELETE` and `ON UPDATE` clauses specify what must be done when a `DELETE` (or a `REPLACE`) statements attempts to delete a referenced row from the parent table, and when an `UPDATE` statement attempts to modify the referenced foreign key columns in a parent table row, respectively. The following options are allowed:

* `RESTRICT`: The delete/update operation is not performed. The statement terminates with a 1451 error (SQLSTATE '2300').
* `NO ACTION`: Synonym for `RESTRICT`.
* `CASCADE`: The delete/update operation is performed in both tables.
* `SET NULL`: The update or delete goes ahead in the parent table, and the corresponding foreign key fields in the child table are set to `NULL`. (They must not be defined as `NOT NULL` for this to succeed).
* `SET DEFAULT`: This option is implemented only for the legacy PBXT storage engine, which is disabled by default and no longer maintained. It sets the child table's foreign key fields to their `DEFAULT` values when the referenced parent table key entries are updated or deleted.

If either clause is omitted, the default behavior for the omitted clause is `RESTRICT`.

See [Foreign Keys](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) for more information.

### DROP FOREIGN KEY

Drops a foreign key. See [Foreign Keys](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) for more information.

### ADD INDEX

Adds a plain index. Plain indexes are regular indexes that are not unique, and are not acting as a primary key or a foreign key. They are also not the "specialized" `FULLTEXT` or `SPATIAL` indexes. For limits on InnoDB indexes, see [InnoDB Limitations](../../../../../server-usage/storage-engines/innodb/innodb-limitations.md). See [Getting Started with Indexes: Plain Indexes](../../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#plain-indexes) for more information.

### DROP INDEX

Drops a plain index. Plain indexes are regular indexes that are not unique, and are not acting as a primary key or a foreign key. They are also not the "specialized" `FULLTEXT` or `SPATIAL` indexes. See [Getting Started with Indexes: Plain Indexes](../../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#plain-indexes) for more information.

### ADD UNIQUE INDEX

Adds a unique index. The `UNIQUE` keyword means that the index will not accept duplicated values, except for NULLs. An error will raise if you try to insert duplicate values in a UNIQUE index. For `UNIQUE` indexes, you can specify a name for the constraint, using the `CONSTRAINT` keyword. That name will be used in error messages. See [Getting Started with Indexes: Unique Index](../../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#unique-index) for more information.

### DROP UNIQUE INDEX

Drops a unique index. The `UNIQUE` keyword means that the index will not accept duplicated values, except for NULLs. An error will raise if you try to insert duplicate values in a UNIQUE index. For `UNIQUE` indexes, you can specify a name for the constraint, using the `CONSTRAINT` keyword. That name will be used in error messages. See [Getting Started with Indexes: Unique Index](../../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#unique-index) for more information.

### ADD FULLTEXT INDEX

Adds a `FULLTEXT` index. See [Full-Text Indexes](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) for more information.

### DROP FULLTEXT INDEX

Drops a `FULLTEXT` index. See [Full-Text Indexes](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) for more information.

### ADD SPATIAL INDEX

Adds a SPATIAL index. See [SPATIAL INDEX](../../../../sql-structure/geometry/spatial-index.md) for more information.

### DROP SPATIAL INDEX

Drops a SPATIAL index. See [SPATIAL INDEX](../../../../sql-structure/geometry/spatial-index.md) for more information.

### ENABLE/ DISABLE KEYS

`DISABLE KEYS` disables all non unique keys for the table for storage engines that support this (at least MyISAM and Aria). This can be used to [speed up inserts](../../../../../ha-and-performance/optimization-and-tuning/query-optimizations/how-to-quickly-insert-data-into-mariadb.md) into empty tables. `ENABLE KEYS` enables all disabled keys.

### RENAME TO

Renames a table. See also [RENAME TABLE](../../rename-table.md).

### ADD CONSTRAINT

Modifies the table adding a [constraint](../../constraint.md) on a particular column or columns.

```sql
ALTER TABLE table_name 
ADD CONSTRAINT [constraint_name] CHECK(expression);
```

Before a row is inserted or updated, all constraints are evaluated in the order they are defined. If any constraint fails, then the row will not be updated. One can use most deterministic functions in a constraint, including [UDF's](../../../../../server-usage/user-defined-functions/).

```sql
CREATE TABLE account_ledger (
	id INT PRIMARY KEY AUTO_INCREMENT,
	transaction_name VARCHAR(100),
	credit_account VARCHAR(100),
	credit_amount INT,
	debit_account VARCHAR(100),
	debit_amount INT);

ALTER TABLE account_ledger 
ADD CONSTRAINT is_balanced 
    CHECK((debit_amount + credit_amount) = 0);
```

The `constraint_name` is optional. If you don't provide one in the `ALTER TABLE` statement, MariaDB auto-generates a name for you. This is done so that you can remove it later using [DROP CONSTRAINT](./#drop-constraint) clause.

You can disable all constraint expression checks by setting the variable [check\_constraint\_checks](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#check_constraint_checks) to `OFF`. You may find this useful when loading a table that violates some constraints that you want to later find and fix in SQL.

To view constraints on a table, query [information\_schema.TABLE\_CONSTRAINTS](../../../../system-tables/information-schema/information-schema-tables/information-schema-table_constraints-table.md):

```sql
SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
FROM information_schema.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'account_ledger';

+-----------------+----------------+-----------------+
| CONSTRAINT_NAME | TABLE_NAME     | CONSTRAINT_TYPE |
+-----------------+----------------+-----------------+
| is_balanced     | account_ledger | CHECK           |
+-----------------+----------------+-----------------+
```

### DROP CONSTRAINT

`DROP CONSTRAINT` for `UNIQUE` and `FOREIGN KEY` [constraints](../../constraint.md)\
and `DROP CONSTRAINT` for `CHECK` constraints were introduced in an earlier version of MariaDB.

Modifies the table, removing the given constraint.

```sql
ALTER TABLE table_name
DROP CONSTRAINT constraint_name;
```

When you add a constraint to a table, whether through a [CREATE TABLE](../../create/create-table.md#constraint-expressions) or [ALTER TABLE...ADD CONSTRAINT](./#add-constraint) statement, you can either set a `constraint_name` yourself, or allow MariaDB to auto-generate one for you. To view constraints on a table, query [information\_schema.TABLE\_CONSTRAINTS](../../../../system-tables/information-schema/information-schema-tables/information-schema-table_constraints-table.md). For instance,

```sql
CREATE TABLE t (
   a INT,
   b INT,
   c INT,
   CONSTRAINT CHECK(a > b),
   CONSTRAINT check_equals CHECK(a = c)); 

SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
FROM information_schema.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 't';

+-----------------+----------------+-----------------+
| CONSTRAINT_NAME | TABLE_NAME     | CONSTRAINT_TYPE |
+-----------------+----------------+-----------------+
| check_equals    | t              | CHECK           |
| CONSTRAINT_1    | t              | CHECK           |
+-----------------+----------------+-----------------+
```

To remove a constraint from the table, issue an `ALTER TABLE...DROP CONSTRAINT` statement. For example:

```sql
ALTER TABLE t DROP CONSTRAINT is_unique;
```

### ADD SYSTEM VERSIONING

Adds system versioning. See [System-versioned tables](../../../../sql-structure/temporal-tables/system-versioned-tables.md).

### DROP SYSTEM VERSIONING

Drops system versioning. See [System-versioned tables](../../../../sql-structure/temporal-tables/system-versioned-tables.md).

### ADD PERIOD FOR

See [System-versioned tables](../../../../sql-structure/temporal-tables/system-versioned-tables.md), [Application-time-period tables](../../../../sql-structure/temporal-tables/application-time-periods.md) or [Bitemporal Tables](../../../../sql-structure/temporal-tables/bitemporal-tables.md).

### FORCE

`ALTER TABLE ... FORCE` forces MariaDB to rebuild the table.

```sql
ALTER TABLE tab_name FORCE;
```

With InnoDB, the table rebuild only reclaims unused space (i.e. the space previously used for deleted rows) if the [innodb\_file\_per\_table](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) system variable is set to `ON` (the default). If the system variable is `OFF`, the space will not be reclaimed, but it will be re-used for new data that's later added.

The rebuild may fail if conditions are violated due to a change in the [sql\_mode](../../../../../server-management/variables-and-modes/sql-mode.md). For example:

```sql
CREATE OR REPLACE TABLE x (d DATE DEFAULT '0000-00-00');

SET SQL_MODE='NO_ZERO_DATE';

ALTER TABLE x FORCE;
ERROR 1067 (42000): Invalid default value for 'd'
```

### Partitions

#### ADD PARTITION

See [Partitioning Overview: Adding Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#adding-partitions) for details.

#### ANALYZE PARTITION

See [Partitioning Overview: Analyzing Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#analyzing-partitions) for details.

#### CHECK PARTITION

See [Partitioning Overview: Checking Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#checking-partitions) for details.

#### COALESCE PARTITION

Reduces the number of HASH or KEY partitions in a table. See [Partitioning Overview: Coalescing Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#coalescing-partitions).

#### CONVERT PARTITION / TABLE

{% tabs %}
{% tab title="Current" %}
`CONVERT PARTITION` can be used to remove a partition from a table and make this an ordinary table. For example:

```sql
ALTER TABLE partitioned_table CONVERT PARTITION part1 TO TABLE normal_table;
```

`CONVERT TABLE` will take an existing table and move this to another table as its own partition with a specified [partition definition](../../create/create-table.md#partitions). For example the following moves `normal_table` to a partition of `partitioned_table` with a definition that its values, based on the `PARTITION BY` of the `partitioned_table`, are less than 12345.

```sql
ALTER TABLE partitioned_table CONVERT TABLE normal_table 
  TO PARTITION part1 VALUES LESS THAN (12345);
```

The optional `[{WITH | WITHOUT} VALIDATION]` is permitted.

See [Partitioning Overview: Converting Partitions to/from Tables](../../../../../server-usage/partitioning-tables/partitioning-overview.md#converting-partitions-tofrom-tables) for more details.
{% endtab %}

{% tab title="< 11.4" %}
`CONVERT PARTITION` can be used to remove a partition from a table and make this an ordinary table. For example:

```sql
ALTER TABLE partitioned_table CONVERT PARTITION part1 TO TABLE normal_table;
```

`CONVERT TABLE` will take an existing table and move this to another table as its own partition with a specified [partition definition](../../create/create-table.md#partitions). For example the following moves `normal_table` to a partition of `partitioned_table` with a definition that its values, based on the `PARTITION BY` of the `partitioned_table`, are less than 12345.

```sql
ALTER TABLE partitioned_table CONVERT TABLE normal_table 
  TO PARTITION part1 VALUES LESS THAN (12345);
```

The optional clause `[{WITH | WITHOUT} VALIDATION]` is not available.

See [Partitioning Overview: Converting Partitions to/from Tables](../../../../../server-usage/partitioning-tables/partitioning-overview.md#converting-partitions-tofrom-tables) for more details.&#x20;
{% endtab %}

{% tab title="< 10.7.1" %}
`CONVERT PARTITION` and `CONVERT TABLE` are not available.
{% endtab %}
{% endtabs %}

#### DROP PARTITION

Used to drop specific partitions (and discard all data within the specified partitions) for [RANGE](../../../../../server-usage/partitioning-tables/partitioning-types/range-partitioning-type.md) and [LIST](../../../../../server-usage/partitioning-tables/partitioning-types/list-partitioning-type.md) partitions. See [Partitioning Overview: Dropping Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#dropping-partitions).

#### EXCHANGE PARTITION

{% tabs %}
{% tab title="Current" %}
This clause is used to exchange the contents of a partition with another table. This is performed by swapping the tablespaces of the partition with the other table.

The optional `[{WITH | WITHOUT} VALIDATION]` is permitted.

See [Partitioning Overview: Exchanging Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#exchanging-partitions) for more details.

See also [copying InnoDB's transportable tablespaces](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces).&#x20;
{% endtab %}

{% tab title="< 11.4" %}
This clause is used to exchange the contents of a partition with another table. This is performed by swapping the tablespaces of the partition with the other table.

The optional `[{WITH | WITHOUT} VALIDATION]` is not permitted.

See [Partitioning Overview: Exchanging Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#exchanging-partitions) for more details.

See also [copying InnoDB's transportable tablespaces](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces).&#x20;
{% endtab %}
{% endtabs %}

#### OPTIMIZE PARTITION

See [Partitioning Overview: Optimizing Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#optimizing-partitions) for details.

#### REMOVE PARTITIONING

See [Partitioning Overview: Removing Partitioning](../../../../../server-usage/partitioning-tables/partitioning-overview.md#removing-partitioning).

#### REORGANIZE PARTITION

See [Partitioning Overview: Reorganizing Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#reorganizing-partitions).

#### TRUNCATE PARTITION

See [Partitioning Overview: Truncating Partitions](../../../../../server-usage/partitioning-tables/partitioning-overview.md#truncating-partitions).

### DISCARD TABLESPACE

This is used to discard an InnoDB table's tablespace.

See [copying InnoDB's transportable tablespaces](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) for more information.

### IMPORT TABLESPACE

This is used to import an InnoDB table's tablespace. The tablespace should have been copied from its original server after executing [FLUSH TABLES FOR EXPORT](../../../administrative-sql-statements/flush-commands/flush-tables-for-export.md).

See [copying InnoDB's transportable tablespaces](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) for more information.

`ALTER TABLE ... IMPORT` only applies to InnoDB tables. Most other popular storage engines, such as Aria and MyISAM, will recognize their data files as soon as they've been placed in the proper directory under the datadir, and no special DDL is required to import them.

### ALGORITHM

The `ALTER TABLE` statement supports the `ALGORITHM` clause. This clause is one of the clauses that is used to implement online DDL. `ALTER TABLE` supports several different algorithms. An algorithm can be explicitly chosen for an `ALTER TABLE` operation by setting the `ALGORITHM` clause. The supported values are:

* `ALGORITHM=DEFAULT` - This implies the default behavior for the specific statement, such as if no `ALGORITHM` clause is specified.
* `ALGORITHM=COPY`
* `ALGORITHM=INPLACE`
* `ALGORITHM=NOCOPY`
* `ALGORITHM=INSTANT`

See [InnoDB Online DDL Overview: ALGORITHM](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-overview.md#alter-algorithms) for information on how the `ALGORITHM` clause affects InnoDB.

#### ALGORITHM=DEFAULT

The default behavior, which occurs if `ALGORITHM=DEFAULT` is specified, or if `ALGORITHM` is not specified at all, usually only makes a copy if the operation doesn't support being done in-place at all. In this case, the most efficient available algorithm will usually be used.

The [old\_alter\_table](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_alter_table) system variable is deprecated. Instead, the [alter\_algorithm](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#alter_algorithm) system variable defines the default algorithm for `ALTER TABLE` operations. This was removed in [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115) for the following reasons:

* alter\_algorithm was introduced as a replacement for the old\_alter\_table that was used to force the usage of the original alter table algorithm (copy) in cases where the new alter algorithm did not work. The new option was added as a way to force the usage of a specific algorithm when it should instead have made it possible to disable algorithms that would not work for some reason.
* alter\_algorithm introduced some cases where ALTER TABLE would not work without specifying the ALGORITHM=XXX option together with ALTER TABLE.
* Having different values of alter\_algorithm on the primary and replica could cause replicas to stop unexpectedly.
* ALTER TABLE FORCE, as used by mariadb-upgrade, would not always work if alter\_algorithm was set for the server.
* As part of [MDEV-33449](https://jira.mariadb.org/browse/MDEV-33449) "improving repair of tables" it became clear that alter-algorithm made it harder to provide a better and more consistent ALTER TABLE FORCE and REPAIR TABLE, and it would be better to remove it.

#### ALGORITHM=COPY

`ALGORITHM=COPY` is the name for the original [ALTER TABLE](./) algorithm from early MariaDB versions.

When `ALGORITHM=COPY` is set, MariaDB essentially does the following operations:

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

If `ALGORITHM=COPY` is specified, then the copy algorithm will be used even if it is not necessary. This can result in a lengthy table copy. If multiple [ALTER TABLE](./) operations are required that each require the table to be rebuilt, then it is best to specify all operations in a single [ALTER TABLE](./) statement, so that the table is only rebuilt once.

{% tabs %}
{% tab title="Current" %}
`ALTER TABLE` can perform most operations with `ALGORITHM=COPY`, `LOCK=NONE`. See [LOCK=NONE](./#none).&#x20;
{% endtab %}

{% tab title="< 11.2" %}
`ALTER TABLE` cannot perform operations with `ALGORITHM=COPY`, `LOCK=NONE`.&#x20;
{% endtab %}
{% endtabs %}

#### ALGORITHM=INPLACE

`ALGORITHM=COPY` can be incredibly slow, because the whole table has to be copied and rebuilt. `ALGORITHM=INPLACE` was introduced as a way to avoid this by performing operations in-place and avoiding the table copy and rebuild, when possible.

When `ALGORITHM=INPLACE` is set, the underlying storage engine uses optimizations to perform the operation while avoiding the table copy and rebuild. However, `INPLACE` is a bit of a misnomer, since some operations may still require the table to be rebuilt for some storage engines. Regardless, several operations can be performed without a full copy of the table for some storage engines.

A more accurate name would have been `ALGORITHM=ENGINE`, where `ENGINE` refers to an "engine-specific" algorithm.

If an [ALTER TABLE](./) operation supports `ALGORITHM=INPLACE`, then it can be performed using optimizations by the underlying storage engine, but it may rebuilt.

See [InnoDB Online DDL Operations with ALGORITHM=INPLACE](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md) for more.

#### ALGORITHM=NOCOPY

`ALGORITHM=INPLACE` can sometimes be surprisingly slow in instances where it has to rebuild the clustered index, because when the clustered index has to be rebuilt, the whole table has to be rebuilt. `ALGORITHM=NOCOPY` was introduced as a way to avoid this.

If an `ALTER TABLE` operation supports `ALGORITHM=NOCOPY`, then it can be performed without rebuilding the clustered index.

If `ALGORITHM=NOCOPY` is specified for an `ALTER TABLE` operation that does not support `ALGORITHM=NOCOPY`, then an error will be raised. In this case, raising an error is preferable, if the alternative is for the operation to rebuild the clustered index, and perform unexpectedly slowly.

See [InnoDB Online DDL Operations with ALGORITHM=NOCOPY](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md) for more.

#### ALGORITHM=INSTANT

`ALGORITHM=INPLACE` can sometimes be surprisingly slow in instances where it has to modify data files. `ALGORITHM=INSTANT` was introduced as a way to avoid this.

If an `ALTER TABLE` operation supports `ALGORITHM=INSTANT`, then it can be performed without modifying any data files.

If `ALGORITHM=INSTANT` is specified for an `ALTER TABLE` operation that does not support `ALGORITHM=INSTANT`, then an error will be raised. In this case, raising an error is preferable, if the alternative is for the operation to modify data files, and perform unexpectedly slowly.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more.

### LOCK

The `ALTER TABLE` statement supports the `LOCK` clause. This clause is one of the clauses that is used to implement online DDL. `ALTER TABLE` supports several different locking strategies. A locking strategy can be explicitly chosen for an `ALTER TABLE` operation by setting the `LOCK` clause. The supported values are:

#### DEFAULT

Acquire the least restrictive lock on the table that is supported for the specific operation. Permit the maximum amount of concurrency that is supported for the specific operation.

#### NONE

Acquire no lock on the table. Permit **all** concurrent DML. If this locking strategy is not permitted for an operation, then an error is raised. From [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112), `ALTER TABLE` can do most operations with `ALGORITHM=COPY, LOCK=NONE`, that is, in most cases, unless the algorithm and lock level are explicitly specified, `ALTER TABLE` will be performed using the `COPY` algorithm while simultaneously allowing concurrent DML statements on the altered table. If this is not desired, one can explicitly specify a different lock level or set old\_mode to [LOCK\_ALTER\_TABLE\_COPY](../../../../../server-management/variables-and-modes/old-mode.md#lock_alter_table_copy) that will make `ALGORITHM=COPY` use `LOCK=SHARED` by default (but still allowing `LOCK=NONE` to be specified explicitly).

#### SHARED

Acquire a read lock on the table. Permit **read-only** concurrent DML. If this locking strategy is not permitted for an operation, then an error is raised.

#### EXCLUSIVE

Acquire a write lock on the table. Do **not** permit concurrent DML.

Different storage engines support different locking strategies for different operations. If a specific locking strategy is chosen for an `ALTER TABLE` operation, and that table's storage engine does not support that locking strategy for that specific operation, then an error will be raised.

If the `LOCK` clause is not explicitly set, then the operation uses `LOCK=DEFAULT`.

[ALTER ONLINE TABLE](./#alter-online-table) is equivalent to `LOCK=NONE`. Therefore, the [ALTER ONLINE TABLE](./#alter-online-table) statement can be used to ensure that your `ALTER TABLE` operation allows all concurrent DML.

See [InnoDB Online DDL Overview: LOCK](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-overview.md#supported-alter-locking-strategies) for information on how the `LOCK` clause affects InnoDB.

### Index Options

See [CREATE TABLE](../../create/create-table.md#index-options) page for meaning of the index options.

## Progress Reporting

MariaDB provides progress reporting for `ALTER TABLE` statement for clients that support the new progress reporting protocol. For example, if you were using the [mariadb](../../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client, then the progress report might look like this::

```sql
ALTER TABLE test ENGINE=Aria;
Stage: 1 of 2 'copy to tmp table'    46% of stage
```

The progress report is also shown in the output of the [SHOW PROCESSLIST](../../../administrative-sql-statements/show/show-processlist.md) statement and in the contents of the [information\_schema.PROCESSLIST](../../../../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table.

See [Progress Reporting](./#progress-reporting) for more information.

## Aborting ALTER TABLE Operations

If an `ALTER TABLE` operation is being performed and the connection is killed, the changes will be rolled back in a controlled manner. The rollback can be a slow operation as the time it takes is relative to how far the operation has progressed.

Aborting `ALTER TABLE ... ALGORITHM=COPY` was made faster by removing excessive undo logging ([MDEV-11415](https://jira.mariadb.org/browse/MDEV-11415)). This significantly shortened the time it takes to abort a running ALTER TABLE operation, compared with earlier releases.

## Atomic ALTER TABLE

{% tabs %}
{% tab title="Current" %}
`ALTER TABLE` is atomic for most engines, including InnoDB, MyRocks, MyISAM and Aria ([MDEV-25180](https://jira.mariadb.org/browse/MDEV-25180)). This means that if there is a crash (server down or power outage) during an `ALTER TABLE` operation, after recovery, either the old table and associated triggers and status will be intact, or the new table will be active. In older MariaDB versions one could get leftover #sql-alter..', '#sql-backup..' or 'table\_name.frm˝' files if the system crashed during the `ALTER TABLE` operation.

See [Atomic DDL](../../atomic-ddl.md) for more information.
{% endtab %}

{% tab title="< 10.6.1" %}
Atomic `ALTER TABLE` is not available.
{% endtab %}
{% endtabs %}

## Replication

{% tabs %}
{% tab title="Current" %}
`ALTER TABLE` got fully executed on the primary first, and only then was it replicated and started executing on replicas. [An option](../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_alter_two_phase) was added to replicate sooner and begin executing on replicas, directly when it _starts_ executing on the primary, not when it _finishes_. This way the replication lag caused by a heavy `ALTER TABLE` can be completely eliminated ([MDEV-11675](https://jira.mariadb.org/browse/MDEV-11675)).
{% endtab %}

{% tab title="< 10.8.1" %}
The [binlog\_alter\_two\_phase](../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_alter_two_phase) option is not available.
{% endtab %}
{% endtabs %}

## Examples

Adding a new column:

```sql
ALTER TABLE t1 ADD x INT;
```

Dropping a column:

```sql
ALTER TABLE t1 DROP x;
```

Modifying the type of a column:

```sql
ALTER TABLE t1 MODIFY x bigint unsigned;
```

Changing the name and type of a column:

```sql
ALTER TABLE t1 CHANGE a b bigint unsigned auto_increment;
```

Combining multiple clauses in a single ALTER TABLE statement, separated by commas:

```sql
ALTER TABLE t1 DROP x, ADD x2 INT,  CHANGE y y2 INT;
```

Changing the storage engine and adding a comment:

```sql
ALTER TABLE t1 
  ENGINE = InnoDB 
  COMMENT = 'First of three tables containing usage info';
```

Rebuilding the table (the previous example will also rebuild the table if it was already InnoDB):

```sql
ALTER TABLE t1 FORCE;
```

Dropping an index:

```sql
ALTER TABLE rooms DROP INDEX u;
```

Adding a unique index:

```sql
ALTER TABLE rooms ADD UNIQUE INDEX u(room_number);
```

Adding a primary key for an [application-time period table](../../../../sql-structure/temporal-tables/application-time-periods.md) with a [WITHOUT OVERLAPS](../../../../sql-structure/temporal-tables/application-time-periods.md#without-overlaps) constraint:

```sql
ALTER TABLE rooms ADD PRIMARY KEY(room_number, p WITHOUT OVERLAPS);
```

{% tabs %}
{% tab title="Current" %}
An `ALTER` query can be replicated faster with this statement, which must be run before the `ALTER` statement:

```sql
SET @@SESSION.binlog_alter_two_phase = TRUE;
```

Binlog would contain two event groups, of which the first one gets delivered to replicas before ALTER is taken to actual execution on the primary:

```sql
| master-bin.000001 | 495 | Gtid              |         1 |         537 | GTID 0-1-2 START ALTER                                        |
| master-bin.000001 | 537 | Query             |         1 |         655 | use `test`; alter table t add column b int, algorithm=inplace |
| master-bin.000001 | 655 | Gtid              |         1 |         700 | GTID 0-1-3 COMMIT ALTER id=2                                  |
| master-bin.000001 | 700 | Query             |         1 |    
```
{% endtab %}

{% tab title="< 10.8.1" %}
This statement is not available:

```

sql
SET @@SESSION.binlog_alter_two_phase = true;
```
{% endtab %}
{% endtabs %}

## See Also

* [CREATE TABLE](../../create/create-table.md)
* [DROP TABLE](../../drop/drop-table.md)
* [Character Sets and Collations](../../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [SHOW CREATE TABLE](../../../administrative-sql-statements/show/show-create-table.md)
* [Instant ADD COLUMN for InnoDB](../../../../../server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
