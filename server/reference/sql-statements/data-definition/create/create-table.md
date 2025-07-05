# CREATE TABLE

## Syntax

```sql
CREATE [OR REPLACE] [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (<a data-footnote-ref href="#user-content-fn-1">create_definition</a>,...) [<a data-footnote-ref href="#user-content-fn-2">table_options</a>    ]... [<a data-footnote-ref href="#user-content-fn-3">partition_options</a>]
CREATE [OR REPLACE] [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(<a data-footnote-ref href="#user-content-fn-1">create_definition</a>,...)] [<a data-footnote-ref href="#user-content-fn-2">table_options</a>   ]... [<a data-footnote-ref href="#user-content-fn-3">partition_options</a>]
    select_statement
CREATE [OR REPLACE] [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
   { LIKE old_table_name | (LIKE old_table_name) }

select_statement:
    [IGNORE | REPLACE] [AS] SELECT ...   (Some legal select statement)
```

## Description

Use the `CREATE TABLE` statement to create a table with the given name.

In its most basic form, the `CREATE TABLE` statement provides a table name followed by a list of columns, indexes, and constraints. By default, the table is created in the default database. Specify a database with `db_name.tbl_name`. If you quote the table name, you must quote the database name and table name separately as ``db_name`.`tbl_name``. This is particularly useful for [CREATE TABLE ... SELECT](create-table.md#create-table-select), because it allows to create a table into a database, which contains data from other databases. See [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md).

If a table with the same name exists, error 1050 results. Use [IF NOT EXISTS](create-table.md#create-table-if-not-exists) to suppress this error and issue a note instead. Use [SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md) to see notes.

The `CREATE TABLE` statement automatically commits the current transaction, except when using the [TEMPORARY](create-table.md#create-temporary-table) keyword.

For valid identifiers to use as table names, see [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md).

{% hint style="info" %}
If the `default_storage_engine` is set to `ColumnStore` , it needs setting on all UMs. Otherwise when the tables using the default engine are replicated across UMs, they will use the wrong engine. You should therefore not use this option as a session variable with ColumnStore.
{% endhint %}

[Microsecond precision](../../../sql-functions/date-time-functions/microseconds-in-mariadb.md) can be between 0-6. If no precision is specified it is assumed to be 0, for backward compatibility reasons.

## Privileges

Executing the `CREATE TABLE` statement requires the [CREATE](../../account-management-sql-statements/grant.md#table-privileges) privilege for the table or the database.

## CREATE OR REPLACE

If the `OR REPLACE` clause is used and the table already exists, then instead of returning an error, the server will drop the existing table and replace it with the newly defined table.

This syntax was originally added to make [replication](../../../../ha-and-performance/standard-replication/) more robust if it has to rollback and repeat statements such as `CREATE ... SELECT` on replicas.

```sql
CREATE OR REPLACE TABLE table_name (a int);
```

is basically the same as:

```sql
DROP TABLE IF EXISTS table_name;
CREATE TABLE table_name (a int);
```

with the following exceptions:

* If `table_name` was locked with [LOCK TABLES](../../transactions/lock-tables.md) it will continue to be locked after the statement.
* Temporary tables are only dropped if the `TEMPORARY` keyword was used. (With [DROP TABLE](../drop/drop-table.md), temporary tables are preferred to be dropped before normal tables).

### Things to be Aware of With CREATE OR REPLACE

* The table is dropped first (if it existed), after that the `CREATE` is done. Because of this, if the `CREATE` fails, then the table will not exist anymore after the statement. If the table was used with `LOCK TABLES` it will be unlocked.
* One can't use `OR REPLACE` together with `IF EXISTS`.
* [Replicas](../../../../ha-and-performance/standard-replication/) will by default use `CREATE OR REPLACE` when replicating `CREATE` statements that don''t use `IF EXISTS`. This can be changed by setting the variable [slave-ddl-exec-mode](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) to `STRICT`.

## CREATE TABLE IF NOT EXISTS

If the `IF NOT EXISTS` clause is used, then the table will only be created if a table with the same name does not already exist. If the table already exists, then a warning will be triggered by default.

## CREATE TEMPORARY TABLE

Use the `TEMPORARY` keyword to create a temporary table that is only available to the current session. Temporary tables are dropped when the session ends. Temporary table names are specific to the session. They will not conflict with other temporary tables from other sessions even if they share the same name. They will shadow names of non-temporary tables or views, if they are identical. A temporary table can have the same name as a non-temporary table which is located in the same database. In that case, their name will reference the temporary table when used in SQL statements. You must have the [CREATE TEMPORARY TABLES](../../account-management-sql-statements/grant.md#database-privileges) privilege on the database to create temporary tables. If no storage engine is specified, the [default\_tmp\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_tmp_storage_engine) setting will determine the engine.

{% tabs %}
{% tab title="Current" %}
[ROCKSDB](../../../../server-usage/storage-engines/myrocks/) temporary tables cannot be created by setting the [default\_tmp\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_tmp_storage_engine) system variable, or using `CREATE TEMPORARY TABLE LIKE`.  If you try, an error is returned. Explicitly creating a temporary table with `ENGINE=ROCKSDB` has never been permitted.
{% endtab %}

{% tab title="< 10.7" %}
[ROCKSDB](../../../../server-usage/storage-engines/myrocks/) temporary tables cannot be created by setting the [default\_tmp\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_tmp_storage_engine) system variable, or using `CREATE TEMPORARY TABLE LIKE`. They can be specified, but fail silently, and a `MyISAM` table is created instead. Explicitly creating a temporary table with `ENGINE=ROCKSDB` has never been permitted.
{% endtab %}
{% endtabs %}

## CREATE TABLE ... LIKE

Use the `LIKE` clause instead of a full table definition to create an empty table with the same definition as another table, including columns, indexes, and table options. Foreign key definitions, as well as any DATA DIRECTORY or INDEX DIRECTORY table options specified on the original table, will not be created.

`LIKE` does not preserve the `TEMPORARY` status of the original table. To make the new table `TEMPORARY` as well, use `CREATE TEMPORARY TABLE ... LIKE`.

`LIKE` does not work with [views](../../../../server-usage/views/), only base tables. Attempting to use it on a view will result in an error:

```sql
CREATE VIEW v (mycol) AS SELECT 'abc';

CREATE TABLE v2 LIKE v;
ERROR 1347 (HY000): 'test.v' is not of type 'BASE TABLE'
```

The same version of the table storage format as found in the original table is used for the new table.

`CREATE TABLE ... LIKE` performs the same checks as `CREATE TABLE`. So a statement may fail if a change in the [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) renders it invalid. For example:

```sql
CREATE OR REPLACE TABLE x (d DATE DEFAULT '0000-00-00');

SET SQL_MODE='NO_ZERO_DATE';

CREATE OR REPLACE TABLE y LIKE x;
ERROR 1067 (42000): Invalid default value for 'd'
```

## CREATE TABLE ... SELECT

You can create a table containing data from other tables using the `CREATE ... SELECT` statement. Columns will be created in the table for each field returned by the `SELECT` query.

You can also define some columns normally and add other columns from a `SELECT`. You can also create columns in the normal way and assign them some values using the query, this is done to force a certain type or other field characteristics. The columns that are not named in the query will be placed before the others. For example:

```sql
CREATE TABLE test (a INT NOT NULL, b CHAR(10)) ENGINE=MyISAM
    SELECT 5 AS b, c, d FROM another_table;
```

Remember that the query just returns data. If you want to use the same indexes, or the same columns attributes (`[NOT] NULL`, `DEFAULT`, `AUTO_INCREMENT`) in the new table, you need to specify them manually. Types and sizes are not automatically preserved if no data returned by the `SELECT` requires the full size, and `VARCHAR` could be converted into `CHAR`. The [CAST()](../../../sql-functions/string-functions/cast.md) function can be used to forcee the new table to use certain types.

Aliases (`AS`) are taken into account, and they should always be used when you `SELECT` an expression (function, arithmetical operation, etc).

If an error occurs during the query, the table will not be created at all.

If the new table has a primary key or `UNIQUE` indexes, you can use the [IGNORE](../../data-manipulation/inserting-loading-data/ignore.md) or `REPLACE` keywords to handle duplicate key errors during the query. `IGNORE` means that the newer values must not be inserted an identical value exists in the index. `REPLACE` means that older values must be overwritten.

If the columns in the new table are more than the rows returned by the query, the columns populated by the query will be placed after other columns. Note that if the strict `SQL_MODE` is on, and the columns that are not names in the query do not have a `DEFAULT` value, an error will raise and no rows will be copied.

[Concurrent inserts](../../data-manipulation/inserting-loading-data/concurrent-inserts.md) are not used during the execution of a `CREATE ... SELECT`.

If the table already exists, an error similar to the following will be returned:

```sql
ERROR 1050 (42S01): Table 't' already exists
```

If the `IF NOT EXISTS` clause is used and the table exists, a note will be produced instead of an error.

To insert rows from a query into an existing table, [INSERT ... SELECT](../../data-manipulation/inserting-loading-data/insert-select.md) can be used.

## Column Definitions

<pre class="language-sql"><code class="lang-sql">create_definition:
  { col_name column_definition | <a data-footnote-ref href="#user-content-fn-1">index_definition</a> | <a data-footnote-ref href="#user-content-fn-2">period_definition</a> | CHECK (expr) }

column_definition:
  <a data-footnote-ref href="#user-content-fn-3">data_type</a>
    [NOT NULL | NULL] [DEFAULT default_value | (expression)]
    [ON UPDATE [NOW | CURRENT_TIMESTAMP] [(precision)]]
    [AUTO_INCREMENT] [ZEROFILL] [UNIQUE [KEY] | [PRIMARY] KEY]
    [INVISIBLE] [{WITH|WITHOUT} SYSTEM VERSIONING]
    [COMMENT 'string'] [REF_SYSTEM_ID = value]
    [<a data-footnote-ref href="#user-content-fn-1">reference_definition</a>]
  | <a data-footnote-ref href="#user-content-fn-3">data_type</a> [GENERATED ALWAYS] 
  AS [ ROW {START|END} [NOT NULL ENABLE] [[PRIMARY] KEY]
        | (expression) [VIRTUAL | PERSISTENT | STORED] ]
      [INVISIBLE] [UNIQUE [KEY]] [COMMENT 'string']

constraint_definition:
   CONSTRAINT [constraint_name] CHECK (expression)
</code></pre>

{% hint style="info" %}
**Note:**


{% endhint %}

{% tabs %}
{% tab title="Current" %}
MariaDB accepts the shortcut format with a `REFERENCES` clause only in `ALTER TABLE` and `CREATE TABLE` statements, but that syntax does nothing. For example:

```sql
CREATE TABLE b(for_key INT REFERENCES a(not_key));
```

MariaDB will attempt to apply the constraint. See [Foreign Keys examples](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md#references).
{% endtab %}

{% tab title="< 10.5" %}
MariaDB accepts the shortcut format with a `REFERENCES` clause only in `ALTER TABLE` and `CREATE TABLE` statements, but that syntax does nothing. For example:

```sql
CREATE TABLE b(for_key INT REFERENCES a(not_key));
```
{% endtab %}
{% endtabs %}

Each definition either creates a column in the table or specifies and index or constraint on one or more columns. See [Indexes](create-table.md#indexes) below for details on creating indexes.

Create a column by specifying a column name and a data type, optionally followed by column options. See [Data Types](../../../data-types/) for a full list of data types allowed in MariaDB.

### NULL and NOT NULL

Use the `NULL` or `NOT NULL` options to specify that values in the column may or may not be `NULL`, respectively. By default, values may be `NULL`. See also [NULL Values in MariaDB](../../../data-types/null-values.md).

### DEFAULT Column Option

Specify a default value using the `DEFAULT` clause. If you don't specify `DEFAULT` then the following rules apply:

* If the column is not defined with `NOT NULL`, `AUTO_INCREMENT` or `TIMESTAMP`, an explicit `DEFAULT NULL` will be added.\
  Note that in MySQL, you may get an explicit `DEFAULT` for primary key parts, if not specified with NOT NULL.

The default value will be used if you [INSERT](../../data-manipulation/inserting-loading-data/insert.md) a row without specifying a value for that column, or if you specify [DEFAULT](../../../sql-functions/secondary-functions/information-functions/default.md) for that column.

[CURRENT\_TIMESTAMP](../../../sql-functions/date-time-functions/now.md) may also be used as the default value for a [DATETIME](../../../data-types/date-and-time-data-types/datetime.md)

You can use most functions in `DEFAULT`. Expressions should have parentheses around them. If you use a non deterministic function in `DEFAULT` then all inserts to the table will be [replicated](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements/data-definition/create/broken-reference/README.md) in [row mode](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#row-based). You can even refer to earlier columns in the `DEFAULT` expression (excluding `AUTO_INCREMENT` columns):

```sql
CREATE TABLE t1 (a int DEFAULT (1+1), b int DEFAULT (a+1));
CREATE TABLE t2 (a bigint primary key DEFAULT UUID_SHORT());
```

The `DEFAULT` clause cannot contain any [stored functions](../../../../server-usage/stored-routines/stored-functions/) or [subqueries](../../data-manipulation/selecting-data/joins-subqueries/subqueries/), and a column used in the clause must already have been defined earlier in the statement.

It is possible to assign [BLOB](../../../data-types/string-data-types/blob.md) or [TEXT](../../../data-types/string-data-types/text.md) columns a `DEFAULT` value.

You can also use DEFAULT ([NEXT VALUE FOR sequence](../../../sql-structure/sequences/sequence-functions/next-value-for-sequence_name.md)).

### AUTO\_INCREMENT Column Option

Use [AUTO\_INCREMENT](../../../data-types/auto_increment.md) to create a column whose value can be set automatically from a simple counter. You can only use `AUTO_INCREMENT` on a column with an integer type. The column must be a key, and there can only be one `AUTO_INCREMENT` column in a table. If you insert a row without specifying a value for that column (or if you specify `0`, `NULL`, or [DEFAULT](../../../sql-functions/secondary-functions/information-functions/default.md) as the value), the actual value will be taken from the counter, with each insertion incrementing the counter by one. You can still insert a value explicitly. If you insert a value that is greater than the current counter value, the counter is\
set based on the new value. An `AUTO_INCREMENT` column is implicitly `NOT NULL`. Use [LAST\_INSERT\_ID](../../../sql-functions/secondary-functions/information-functions/last_insert_id.md) to get the [AUTO\_INCREMENT](../../../data-types/auto_increment.md) value most recently used by an [INSERT](../../data-manipulation/inserting-loading-data/insert.md) statement.

### ZEROFILL Column Option

If the `ZEROFILL` column option is specified for a column using a [numeric](../../../data-types/numeric-data-types/numeric-data-type-overview.md) data type, then the column will be set to `UNSIGNED` and the spaces used by default to pad the field are replaced with zeros. `ZEROFILL` is ignored in expressions or as part of a [UNION](../../data-manipulation/selecting-data/joins-subqueries/union.md). `ZEROFILL` is a non-standard MySQL and MariaDB enhancement.

### PRIMARY KEY Column Option

Use `PRIMARY KEY` to make a column a primary key. A primary key is a special type of a unique key. There can be at most one primary key per table, and it is implicitly `NOT NULL`.

Specifying a column as a unique key creates a unique index on that column. See the [Index Definitions](create-table.md#index-definitions) section below for more information.

### UNIQUE KEY Column Option

Use `UNIQUE KEY` (or just `UNIQUE`) to specify that all values in the column must be distinct from each other. Unless the column is `NOT NULL`, there may be multiple rows with `NULL` in the column.

Specifying a column as a unique key creates a unique index on that column.

See the [Index Definitions](create-table.md#index-definitions) section below for more information.

### COMMENT Column Option

You can provide a comment for each column using the `COMMENT` clause. The maximum length is 1024 characters. Use the [SHOW FULL COLUMNS](../../administrative-sql-statements/show/show-columns.md) statement to see column comments.

### REF\_SYSTEM\_ID

`REF_SYSTEM_ID` can be used to specify Spatial Reference System IDs for spatial data type columns. For example:

```sql
CREATE TABLE t1(g GEOMETRY(9,4) REF_SYSTEM_ID=101);
```

### Generated Columns

A generated column is a column in a table that cannot explicitly be set to a specific value in a [DML query](../../data-manipulation/). Instead, its value is automatically generated based on an expression. This expression might generate the value based on the values of other columns in the table, or it might generate the value by calling [built-in functions](../../../sql-functions/) or [user-defined functions (UDFs)](../../../../server-usage/user-defined-functions/).

There are two types of generated columns:

* `PERSISTENT` or `STORED`: This type's value is actually stored in the table.
* `VIRTUAL`: This type's value is not stored at all. Instead, the value is generated dynamically when the table is queried. This type is the default.

Generated columns are also sometimes called computed columns or virtual columns.

For a complete description about generated columns and their limitations, see [Generated (Virtual and Persistent/Stored) Columns](generated-columns.md).

### COMPRESSED

Certain columns may be compressed. See [Storage-Engine Independent Column Compression](../../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md).

### INVISIBLE

Columns may be made invisible, and hidden in certain contexts. See [Invisible Columns](invisible-columns.md).

### WITH SYSTEM VERSIONING Column Option

Columns may be explicitly marked as included from system versioning. See [System-versioned tables](../../../sql-structure/temporal-tables/system-versioned-tables.md) for details.

### WITHOUT SYSTEM VERSIONING Column Option

Columns may be explicitly marked as excluded from system versioning. See [System-versioned tables](../../../sql-structure/temporal-tables/system-versioned-tables.md) for details.

## Index Definitions

```sql
index_definition:
    {INDEX|KEY} [index_name] [index_type] (index_col_name,...) [index_option] ...
  {{{|}}} {FULLTEXT|SPATIAL} [INDEX|KEY] [index_name] (index_col_name,...) [index_option] ...
  {{{|}}} [CONSTRAINT [symbol]] PRIMARY KEY [index_type] (index_col_name,...) [index_option] ...
  {{{|}}} [CONSTRAINT [symbol]] UNIQUE [INDEX|KEY] [index_name] [index_type] (index_col_name,...) [index_option] ...
  {{{|}}} [CONSTRAINT [symbol]] FOREIGN KEY [index_name] (index_col_name,...) reference_definition

index_col_name:
    col_name [(length)] [ASC | DESC]

index_type:
    USING {BTREE | HASH | RTREE}

index_option:
    [ KEY_BLOCK_SIZE [=] value
  {{{|}}} index_type
  {{{|}}} WITH PARSER parser_name
  {{{|}}} VISIBLE
  {{{|}}} COMMENT 'string'
  {{{|}}} CLUSTERING={YES| NO} ]
  [ IGNORED | NOT IGNORED ]

reference_definition:
    REFERENCES tbl_name (index_col_name,...)
      [MATCH FULL | MATCH PARTIAL | MATCH SIMPLE]
      [ON DELETE reference_option]
      [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION
```

`INDEX` and `KEY` are synonyms.

Index names are optional, if not specified an automatic name will be assigned. Index name are needed to drop indexes and appear in error messages when a constraint is violated.

For limits on InnoDB indexes, see [InnoDB Limitations](../../../../server-usage/storage-engines/innodb/innodb-limitations.md).

### Index Categories

#### Plain Indexes

Plain indexes are regular indexes that are not unique, and are not acting as a primary key or a foreign key. They are also not the "specialized" `FULLTEXT` or `SPATIAL` indexes.

See [Getting Started with Indexes: Plain Indexes](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#plain-indexes) for more information.

#### PRIMARY KEY

For `PRIMARY KEY` indexes, you can specify a name for the index, but it is ignored, and the name of the index is always `PRIMARY`. A warning is explicitly issued if a name is specified. Before then, the name was silently ignored.

See [Getting Started with Indexes: Primary Key](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#primary-key) for more information.

#### UNIQUE

The `UNIQUE` keyword means that the index will not accept duplicated values, except for NULLs. An error will raise if you try to insert duplicate values in a UNIQUE index.

For `UNIQUE` indexes, you can specify a name for the constraint, using the `CONSTRAINT` keyword. That name will be used in error messages.

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
Unique, if index type is not specified, is normally a BTREE index that can also be used by the optimizer to find rows. If the key is longer than the max key length for the used storage engine, a HASH key will be created. This enables MariaDB to enforce uniqueness for any type or number of columns.
{% endhint %}
{% endtab %}

{% tab title="< 10.5" %}
\-
{% endtab %}
{% endtabs %}

See [Getting Started with Indexes: Unique Index](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#unique-index) for more information.

#### FOREIGN KEY

For `FOREIGN KEY` indexes, a reference definition must be provided.

For `FOREIGN KEY` indexes, you can specify a name for the constraint, using the `CONSTRAINT` keyword. That name will be used in error messages.

First, you have to specify the name of the target (parent) table and a column or a column list which must be indexed and whose values must match to the foreign key's values. The `MATCH` clause is accepted to improve the compatibility with other DBMS's, but has no meaning in MariaDB. The `ON DELETE` and `ON UPDATE` clauses specify what must be done when a `DELETE` (or a `REPLACE`) statements attempts to delete a referenced row from the parent table, and when an `UPDATE` statement attempts to modify the referenced foreign key columns in a parent table row, respectively. The following options are allowed:

* `RESTRICT`: The delete/update operation is not performed. The statement terminates with a 1451 error (SQLSTATE '2300').
* `NO ACTION`: Synonym for `RESTRICT`.
* `CASCADE`: The delete/update operation is performed in both tables.
* `SET NULL`: The update or delete goes ahead in the parent table, and the corresponding foreign key fields in the child table are set to `NULL`. (They must not be defined as `NOT NULL` for this to succeed).
* `SET DEFAULT`: This option is currently implemented only for the PBXT storage engine, which is disabled by default and no longer maintained. It sets the child table's foreign key fields to their `DEFAULT` values when the referenced parent table key entries are updated or deleted.

If either clause is omitted, the default behavior for the omitted clause is `RESTRICT`.

See [Foreign Keys](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) for more information.

#### FULLTEXT

Use the `FULLTEXT` keyword to create full-text indexes.

See [Full-Text Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) for more information.

#### SPATIAL

Use the `SPATIAL` keyword to create geometric indexes.

See [SPATIAL INDEX](../../../sql-structure/geometry/spatial-index.md) for more information.

### Index Options

#### KEY\_BLOCK\_SIZE Index Option

The `KEY_BLOCK_SIZE` index option is similar to the [KEY\_BLOCK\_SIZE](create-table.md#key_block_size) table option.

With the [InnoDB](../../../../server-usage/storage-engines/innodb/) storage engine, if you specify a non-zero value for the `KEY_BLOCK_SIZE` table option for the whole table, then the table will implicitly be created with the [ROW\_FORMAT](create-table.md#row_format) table option set to `COMPRESSED`. However, this does not happen if you just set the `KEY_BLOCK_SIZE` index option for one or more indexes in the table. The [InnoDB](../../../../server-usage/storage-engines/innodb/) storage engine ignores the `KEY_BLOCK_SIZE` index option. However, the [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md) statement may still report it for the index.

For information about the `KEY_BLOCK_SIZE` index option, see the [KEY\_BLOCK\_SIZE](create-table.md#key_block_size) table option below.

#### Index Types

Each storage engine supports some or all index types. See [Storage Engine Index Types](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md) for details on permitted index types for each storage engine.

Different index types are optimized for different kind of operations:

* `BTREE` is the default type, and normally is the best choice. It is supported by all storage engines. It can be used to compare a column's value with a value using the =, >, >=, <, <=, `BETWEEN`, and `LIKE` operators. `BTREE` can also be used to find `NULL` values. Searches against an index prefix are possible.
* `HASH` is only supported by the MEMORY storage engine. `HASH` indexes can only be used for =, <=, and >= comparisons. It can not be used for the `ORDER BY` clause. Searches against an index prefix are not possible.
* `RTREE` is the default for [SPATIAL](../../../sql-structure/geometry/spatial-index.md) indexes, but if the storage engine does not support it `BTREE` can be used.

{% tabs %}
{% tab title="Current" %}
Index columns names are listed between parenthesis. After each column, a prefix length can be specified. If no length is specified, the whole column will be indexed. `ASC` and `DESC` can be specified. Individual columns in the index can be explicitly sorted in ascending or descending order. This can be useful for optimizing certain ORDER BY cases ([MDEV-13756](https://jira.mariadb.org/browse/MDEV-13756), [MDEV-26938](https://jira.mariadb.org/browse/MDEV-26938), [MDEV-26939](https://jira.mariadb.org/browse/MDEV-26939), [MDEV-26996](https://jira.mariadb.org/browse/MDEV-26996)). Not only ascending, but also descending, indexes can be used to optimize [MIN()](../../../sql-functions/aggregate-functions/min.md) and [MAX()](../../../sql-functions/aggregate-functions/max.md) ([MDEV-27576](https://jira.mariadb.org/browse/MDEV-27576)).
{% endtab %}

{% tab title="< 11.4 / 10.8" %}
Index columns names are listed between parenthesis. After each column, a prefix length can be specified. If no length is specified, the whole column will be indexed. `ASC` and `DESC` can be specified. Prior to [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108), this was only for compatibility with other DBMSs, but had no meaning in MariaDB. From [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108), individual columns in the index can now be explicitly sorted in ascending or descending order. This can be useful for optimizing certain ORDER BY cases ([MDEV-13756](https://jira.mariadb.org/browse/MDEV-13756), [MDEV-26938](https://jira.mariadb.org/browse/MDEV-26938), [MDEV-26939](https://jira.mariadb.org/browse/MDEV-26939), [MDEV-26996](https://jira.mariadb.org/browse/MDEV-26996)). From [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-0-release-notes), not only ascending, but also descending, indexes can now be used to optimize [MIN()](../../../sql-functions/aggregate-functions/min.md) and [MAX()](../../../sql-functions/aggregate-functions/max.md) ([MDEV-27576](https://jira.mariadb.org/browse/MDEV-27576)).
{% endtab %}
{% endtabs %}

The maximum number of parts in an index is 32.

#### WITH PARSER Index Option

The `WITH PARSER` index option only applies to [FULLTEXT](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) indexes and contains the fulltext parser name. The fulltext parser must be an installed plugin.

#### VISIBLE Index Option

{% tabs %}
{% tab title="Current" %}
Indexes can be declared visible. This is the default and it shows up in [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md).
{% endtab %}

{% tab title="< 10.5.3" %}
Indexes cannot be declared visible.
{% endtab %}
{% endtabs %}

#### COMMENT Index Option

A comment of up to 1024 characters is permitted with the `COMMENT` index option.

The `COMMENT` index option allows you to specify a comment with user-readable text describing what the index is for. This information is not used by the server itself.

#### CLUSTERING Index Option

The `CLUSTERING` index option is only valid for tables using the [TokuDB](../../../../server-usage/storage-engines/tokudb/) storage engine.

#### IGNORED / NOT IGNORED

{% tabs %}
{% tab title="Current" %}
Indexes can be specified to be ignored by the optimizer. See [Ignored Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md).
{% endtab %}

{% tab title="< 10.6.0" %}
Indexes can be specified to be ignored by the optimizer. See [Ignored Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md).
{% endtab %}
{% endtabs %}

## Periods

```sql
period_definition:
    PERIOD FOR [time_period_name | SYSTEM_TIME] (start_column_name, end_column_name)
```

MariaDB supports [System-versioned tables](../../../sql-structure/temporal-tables/system-versioned-tables.md), [Application-time-period tables](../../../sql-structure/temporal-tables/application-time-periods.md) or [Bitemporal Tables](../../../sql-structure/temporal-tables/bitemporal-tables.md).

## Constraint Expressions

MariaDB introduced two ways to define a constraint:

* `CHECK(expression)` given as part of a column definition.
* `CONSTRAINT [constraint_name] CHECK (expression)`

Before a row is inserted or updated, all constraints are evaluated in the order they are defined. If any constraints fails, then the row will not be updated.\
One can use most deterministic functions in a constraint, including [UDFs](../../../../server-usage/user-defined-functions/).

```sql
CREATE TABLE t1 (a INT CHECK(a>0) ,b INT CHECK (b> 0), CONSTRAINT abc CHECK (a>b));
```

If you use the second format and you don't give a name to the constraint, then the constraint will get a auto generated name. This is done so that you can later delete the constraint with [ALTER TABLE DROP constraint\_name](../alter/alter-table.md).

One can disable all constraint expression checks by setting the variable `check_constraint_checks` to `OFF`. This is useful for example when loading a table that violates some constraints that you want to later find and fix in SQL.

See [CONSTRAINT](../constraint.md) for more information.

## Table Options

For each individual table you create (or alter), you can set some table options. The general syntax for setting options is:

```sql
<OPTION_NAME> = <option_value>, [<OPTION_NAME> = <option_value> ...]
```

The equal sign is optional.

Some options are supported by the server and can be used for all tables, no matter what storage engine they use; other options can be specified for all storage engines, but have a meaning only for some engines. Also, engines can [extend CREATE TABLE with new options](../../../../server-usage/storage-engines/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md).

If the `IGNORE_BAD_TABLE_OPTIONS` [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) is enabled, wrong table options generate a warning; otherwise, they generate an error.

```sql
table_option:    
    [STORAGE] ENGINE [=] engine_name
  | AUTO_INCREMENT [=] number
  | AVG_ROW_LENGTH [=] number
  | [DEFAULT] CHARACTER SET [=] <a data-footnote-ref href="#user-content-fn-7">charset_name</a>
  | CHECKSUM [=] {0 | 1}
  | [DEFAULT] COLLATE [=] <a data-footnote-ref href="#user-content-fn-7">collation_name</a>
  | COMMENT [=] 'string'
  | CONNECTION [=] 'connect_string'
  | DATA DIRECTORY [=] 'absolute path to directory'
  | DELAY_KEY_WRITE [=] {0 | 1}
  | ENCRYPTED [=] {YES | NO}
  | ENCRYPTION_KEY_ID [=] number
  | IETF_QUOTES [=] {YES | NO}
  | INDEX DIRECTORY [=] 'absolute path to directory'
  | INSERT_METHOD [=] { NO | FIRST | LAST }
  | KEY_BLOCK_SIZE [=] number
  | MAX_ROWS [=] number
  | MIN_ROWS [=] number
  | PACK_KEYS [=] {0 | 1 | DEFAULT}
  | PAGE_CHECKSUM [=] {0 | 1}
  | PAGE_COMPRESSED [=] {0 | 1}
  | PAGE_COMPRESSION_LEVEL [=] {0 .. 9}
  | PASSWORD [=] 'string'
  | ROW_FORMAT [=] {DEFAULT|DYNAMIC|FIXED|COMPRESSED|REDUNDANT|COMPACT|PAGE}
  | SEQUENCE [=] {0|1}
  | STATS_AUTO_RECALC [=] {DEFAULT|0|1}
  | STATS_PERSISTENT [=] {DEFAULT|0|1}
  | STATS_SAMPLE_PAGES [=] {DEFAULT|number}
  | TABLESPACE tablespace_name
  | TRANSACTIONAL [=]  {0 | 1}
  | UNION [=] (tbl_name[,tbl_name]...)
  | WITH SYSTEM VERSIONING
```

### \[STORAGE] ENGINE

`[STORAGE] ENGINE` specifies a [storage engine](../../../../server-usage/storage-engines/) for the table. If this option is not used, the default storage engine is used instead. That is, the [default\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) session option value if it is set, or the value specified for the `--default-storage-engine` [mariadbd startup option](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md), or the default storage engine, [InnoDB](../../../../server-usage/storage-engines/innodb/). If the specified storage engine is not installed and active, the default value will be used, unless the `NO_ENGINE_SUBSTITUTION` [SQL MODE](../../../../server-management/variables-and-modes/sql-mode.md) is set (default). This is only true for `CREATE TABLE`, not for `ALTER TABLE`. For a list of storage engines that are present in your server, issue a [SHOW ENGINES](../../administrative-sql-statements/show/show-engines.md).

### AUTO\_INCREMENT

`AUTO_INCREMENT` specifies the initial value for the [AUTO\_INCREMENT](../../../data-types/auto_increment.md) primary key. This works for MyISAM, Aria, InnoDB, MEMORY, and ARCHIVE tables. You can change this option with `ALTER TABLE`, but in that case the new value must be higher than the highest value which is present in the `AUTO_INCREMENT` column. If the storage engine does not support this option, you can insert (and then delete) a row having the wanted value - 1 in the `AUTO_INCREMENT` column.

### AVG\_ROW\_LENGTH

`AVG_ROW_LENGTH` is the average rows size. It only applies to tables using [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) and [Aria](../../../../server-usage/storage-engines/aria/aria-storage-engine.md) storage engines that have the [ROW\_FORMAT](create-table.md#row_format) table option set to `FIXED` format.

MyISAM uses `MAX_ROWS` and `AVG_ROW_LENGTH` to decide the maximum size of a table (default: 256TB, or the maximum file size allowed by the system).

### \[DEFAULT] CHARACTER SET/CHARSET

`[DEFAULT] CHARACTER SET` (or `[DEFAULT] CHARSET`) is used to set a default character set for the table. This is the character set used for all columns where an explicit character set is not specified. If this option is omitted or `DEFAULT` is specified, the database's default character set will be used (except for the [JSON data type](../../../data-types/string-data-types/json.md), which is utf8mb4 by default). See [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on setting the [character sets](../../../data-types/string-data-types/character-sets/).

### CHECKSUM/TABLE\_CHECKSUM

`CHECKSUM` (or `TABLE_CHECKSUM`) can be set to 1 to maintain a live checksum for all table's rows. This makes write operations slower, but [CHECKSUM TABLE](../../table-statements/checksum-table.md) will be very fast. This option is only supported for [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) and [Aria tables](../../../../server-usage/storage-engines/aria/aria-storage-engine.md).

### \[DEFAULT] COLLATE

`[DEFAULT] COLLATE` is used to set a default collation for the table. This is the collation used for all columns where an explicit character set is not specified. If this option is omitted or `DEFAULT` is specified, the database's default option will be used (except for the [JSON data type](../../../data-types/string-data-types/json.md), which uses utf8mb4\_bin by default). See [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) for details on setting the [collations](../../../data-types/string-data-types/character-sets/)

### COMMENT

`COMMENT` is a comment for the table. The maximum length is 2048 characters. Also used to define table parameters when creating a [Spider](../../../../server-usage/storage-engines/spider/) table.

### CONNECTION

`CONNECTION` is used to specify a server name or a connection string for a [Spider](../../../../server-usage/storage-engines/spider/), [CONNECT](../../../../server-usage/storage-engines/connect/), [Federated or FederatedX table](../../../../server-usage/storage-engines/federatedx-storage-engine/about-federatedx.md).

### DATA DIRECTORY/INDEX DIRECTORY

`DATA DIRECTORY` and `INDEX DIRECTORY` are supported for MyISAM and Aria, and DATA DIRECTORY is also supported by InnoDB if the [innodb\_file\_per\_table](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) server system variable is enabled, but only in CREATE TABLE, not in [ALTER TABLE](../alter/alter-table.md). So, carefully choose a path for InnoDB tables at creation time, because it cannot be changed without dropping and re-creating the table. These options specify the paths for data files and index files, respectively. If these options are omitted, the database's directory will be used to store data files and index files. Note that these table options do not work for [partitioned](../../../../server-usage/partitioning-tables/) tables (use the partition options instead), or if the server has been invoked with the [--skip-symbolic-links startup option](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md). To avoid the overwriting of old files with the same name that could be present in the directories, you can use [the --keep\_files\_on\_create option](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) (an error will be issued if files already exist). These options are ignored if the `NO_DIR_IN_CREATE` [SQL\_MODE](../../../../server-management/variables-and-modes/sql-mode.md) is enabled (useful for replicas). Also note that symbolic links cannot be used for InnoDB tables.

`DATA DIRECTORY` works by creating symlinks from where the table would normally have been (inside the [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir)) to where the option specifies. For security reasons, to avoid bypassing the privilege system, the server does not permit symlinks inside the datadir. Therefore, `DATA DIRECTORY` cannot be used to specify a location inside the datadir. An attempt to do so will result in an error `1210 (HY000) Incorrect arguments to DATA DIRECTORY`.

### DELAY\_KEY\_WRITE

`DELAY_KEY_WRITE` is supported by MyISAM and Aria, and can be set to 1 to speed up write operations. In that case, when data are modified, the indexes are not updated until the table is closed. Writing the changes to the index file altogether can be much faster. However, note that this option is applied only if the `delay_key_write` server variable is set to 'ON'. If it is 'OFF' the delayed index writes are always disabled, and if it is 'ALL' the delayed index writes are always used, disregarding the value of `DELAY_KEY_WRITE`.

### ENCRYPTED

The `ENCRYPTED` table option can be used to manually set the encryption status of an [InnoDB](../../../../server-usage/storage-engines/innodb/) table. See [InnoDB Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/) for more information.

Aria does not support the `ENCRYPTED` table option. See [MDEV-18049](https://jira.mariadb.org/browse/MDEV-18049).

See [Data-at-Rest Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/) for more information.

### ENCRYPTION\_KEY\_ID

The `ENCRYPTION_KEY_ID` table option can be used to manually set the encryption key of an [InnoDB](../../../../server-usage/storage-engines/innodb/) table. See [InnoDB Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/) for more information.

Aria does not support the `ENCRYPTION_KEY_ID` table option. See [MDEV-18049](https://jira.mariadb.org/browse/MDEV-18049).

See [Data-at-Rest Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/) for more information.

### IETF\_QUOTES

For the [CSV](../../../../server-usage/storage-engines/csv/) storage engine, the `IETF_QUOTES` option, when set to `YES`, enables IETF-compatible parsing of embedded quote and comma characters. Enabling this option for a table improves compatibility with other tools that use CSV, but is not compatible with MySQL CSV tables, or MariaDB CSV tables created without this option. Disabled by default.

### INSERT\_METHOD

`INSERT_METHOD` is only used with [MERGE](../../../../server-usage/storage-engines/merge.md) tables. This option determines in which underlying table the new rows should be inserted. If you set it to 'NO' (which is the default) no new rows can be added to the table (but you will still be able to perform `INSERT`s directly against the underlying tables). `FIRST` means that the rows are inserted into the first table, and `LAST` means that thet are inserted into the last table.

### KEY\_BLOCK\_SIZE

`KEY_BLOCK_SIZE` is used to determine the size of key blocks, in bytes or kilobytes. However, this value is just a hint, and the storage engine could modify or ignore it. If `KEY_BLOCK_SIZE` is set to 0, the storage engine's default value will be used.

With the [InnoDB](../../../../server-usage/storage-engines/innodb/) storage engine, if you specify a non-zero value for the `KEY_BLOCK_SIZE` table option for the whole table, then the table will implicitly be created with the [ROW\_FORMAT](create-table.md#row_format) table option set to `COMPRESSED`.

### MIN\_ROWS/MAX\_ROWS

`MIN_ROWS` and `MAX_ROWS` let the storage engine know how many rows you are planning to store as a minimum and as a maximum. These values will not be used as real limits, but they help the storage engine to optimize the table. `MIN_ROWS` is only used by MEMORY storage engine to decide the minimum memory that is always allocated. `MAX_ROWS` is used to decide the minimum size for indexes.

### PACK\_KEYS

`PACK_KEYS` can be used to determine whether the indexes will be compressed. Set it to 1 to compress all keys. With a value of 0, compression will not be used. With the `DEFAULT` value, only long strings will be compressed. Uncompressed keys are faster.

### PAGE\_CHECKSUM

`PAGE_CHECKSUM` is only applicable to [Aria](../../../../server-usage/storage-engines/aria/) tables, and determines whether indexes and data should use page checksums for extra safety.

### PAGE\_COMPRESSED

`PAGE_COMPRESSED` is used to enable [InnoDB page compression](../../../../server-usage/storage-engines/innodb/innodb-page-compression.md) for [InnoDB](../../../../server-usage/storage-engines/innodb/) tables.

### PAGE\_COMPRESSION\_LEVEL

`PAGE_COMPRESSION_LEVEL` is used to set the compression level for [InnoDB page compression](../../../../server-usage/storage-engines/innodb/innodb-page-compression.md) for [InnoDB](../../../../server-usage/storage-engines/innodb/) tables. The table must also have the [PAGE\_COMPRESSED](create-table.md#page_compressed) table option set to `1`.

Valid values for `PAGE_COMPRESSION_LEVEL` are 1 (the best speed) through 9 (the best compression), .

### PASSWORD

`PASSWORD` is unused.

### RAID\_TYPE

`RAID_TYPE` is an obsolete option, as the raid support has been disabled since MySQL 5.0.

### ROW\_FORMAT

The `ROW_FORMAT` table option specifies the row format for the data file. Possible values are engine-dependent.

#### Supported MyISAM Row Formats

For [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/), the supported row formats are:

* `FIXED`
* `DYNAMIC`
* `COMPRESSED`

The `COMPRESSED` row format can only be set by the [myisampack](../../../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) command line tool.

See [MyISAM Storage Formats](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-storage-formats.md) for more information.

#### Supported Aria Row Formats

For [Aria](../../../../server-usage/storage-engines/aria/aria-storage-engine.md), the supported row formats are:

* `PAGE`
* `FIXED`
* `DYNAMIC`.

See [Aria Storage Formats](../../../../server-usage/storage-engines/aria/aria-storage-formats.md) for more information.

#### Supported InnoDB Row Formats

For [InnoDB](../../../../server-usage/storage-engines/innodb/), the supported row formats are:

* `COMPACT`
* `REDUNDANT`
* `COMPRESSED`
* `DYNAMIC`.

If the `ROW_FORMAT` table option is set to `FIXED` for an InnoDB table, then the server will either return an error or a warning depending on the value of the [innodb\_strict\_mode](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode) system variable. If the [innodb\_strict\_mode](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode) system variable is set to `OFF`, then a warning is issued, and MariaDB will create the table using the default row format for the specific MariaDB server version. If the [innodb\_strict\_mode](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode) system variable is set to `ON`, then an error will be raised.

See [InnoDB Storage Formats](../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md) for more information.

#### Other Storage Engines and ROW\_FORMAT

Other storage engines do not support the `ROW_FORMAT` table option.

### SEQUENCE

If the table is a [sequence](../../../sql-structure/sequences/), then it will have the `SEQUENCE` set to `1`.

### STATS\_AUTO\_RECALC

`STATS_AUTO_RECALC` indicates whether to automatically recalculate persistent statistics (see `STATS_PERSISTENT`, below) for an InnoDB table.\
If set to `1`, statistics will be recalculated when more than 10% of the data has changed. When set to `0`, stats will be recalculated only when an [ANALYZE TABLE](../../table-statements/analyze-table.md) is run. If set to `DEFAULT`, or left out, the value set by the [innodb\_stats\_auto\_recalc](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_recalc) system variable applies. See [InnoDB Persistent Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).

### STATS\_PERSISTENT

`STATS_PERSISTENT` indicates whether the InnoDB statistics created by [ANALYZE TABLE](../../table-statements/analyze-table.md) will remain on disk or not. It can be set to `1` (on disk), `0` (not on disk, the pre-MariaDB 10 behavior), or `DEFAULT` (the same as leaving out the option), in which case the value set by the [innodb\_stats\_persistent](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent) system variable will apply. Persistent statistics stored on disk allow the statistics to survive server restarts, and provide better query plan stability. See [InnoDB Persistent Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).

### STATS\_SAMPLE\_PAGES

`STATS_SAMPLE_PAGES` indicates how many pages are used to sample index statistics. If 0 or DEFAULT, the default value, the [innodb\_stats\_sample\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_sample_pages) value is used. See [InnoDB Persistent Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).

### TRANSACTIONAL

`TRANSACTIONAL` is only applicable for Aria tables. In future Aria tables created with this option will be fully transactional, but currently this provides a form of crash protection. See [Aria Storage Engine](../../../../server-usage/storage-engines/aria/aria-storage-engine.md) for more details.

### UNION

`UNION` must be specified when you create a MERGE table. This option contains a comma-separated list of MyISAM tables which are accessed by the new table. The list is enclosed between parenthesis. Example: `UNION = (t1,t2)`

### WITH SYSTEM VERSIONING

`WITH SYSTEM VERSIONING` is used for creating [System-versioned tables](../../../sql-structure/temporal-tables/system-versioned-tables.md).

## Partitions

```sql
partition_options:
    PARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY(column_list)
        | RANGE(expr)
        | LIST(expr)
        | SYSTEM_TIME [INTERVAL time_quantity <a data-footnote-ref href="#user-content-fn-8">time_unit</a>] [LIMIT num] }
    [PARTITIONS num]
    [SUBPARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY(column_list) }
      [SUBPARTITIONS num]
    ]
    [(partition_definition [, partition_definition] ...)]


partition_definition:
    [PARTITION] partition_name
        [VALUES {LESS THAN {(expr) | MAXVALUE} | IN (value_list)}]
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'comment_text' ]
        [DATA DIRECTORY [=] 'data_dir']
        [INDEX DIRECTORY [=] 'index_dir']
        [MAX_ROWS [=] max_number_of_rows]
        [MIN_ROWS [=] min_number_of_rows]
        [TABLESPACE [=] tablespace_name]
        [NODEGROUP [=] node_group_id]
        [(subpartition_definition [, subpartition_definition] ...)]


subpartition_definition:
    SUBPARTITION logical_name
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'comment_text' ]
        [DATA DIRECTORY [=] 'data_dir']
        [INDEX DIRECTORY [=] 'index_dir']
        [MAX_ROWS [=] max_number_of_rows]
        [MIN_ROWS [=] min_number_of_rows]
        [TABLESPACE [=] tablespace_name]
        [NODEGROUP [=] node_group_id]
```

If the `PARTITION BY` clause is used, the table will be [partitioned](../../../../server-usage/partitioning-tables/). A partition method must be explicitly indicated for partitions and subpartitions. Partition methods are:

* \[LINEAR] [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md) creates a hash key which will be used to read and write rows. The partition function can be any valid SQL expression which returns an `INTEGER` number. Thus, it is possible to use the [HASH](../../../../server-usage/partitioning-tables/partitioning-types/hash-partitioning-type.md) method on an integer column, or on functions which accept integer columns as an argument. However, `VALUES LESS THAN` and `VALUES IN` clauses can not be used with [HASH](../../../../server-usage/partitioning-tables/partitioning-types/hash-partitioning-type.md). An example:

```sql
CREATE TABLE t1 (a INT, b CHAR(5), c DATETIME)
    PARTITION BY HASH ( YEAR(c) );
```

\[LINEAR] [HASH](../../../../../server-management/partitioning-tables/partitioning-types/hash-partitioning-type.md) can be used for subpartitions, too.

* \[LINEAR] [KEY](../../../../../server-management/partitioning-tables/partitioning-types/key-partitioning-type.md) is similar to [HASH](../../../../server-usage/partitioning-tables/partitioning-types/hash-partitioning-type.md), but the index has an even distribution of data. Also, the expression can only be a column or a list of columns. `VALUES LESS THAN` and `VALUES IN` clauses can not be used with [KEY](../../../../server-usage/partitioning-tables/partitioning-types/key-partitioning-type.md).
* [RANGE](../../../../server-usage/partitioning-tables/partitioning-types/range-partitioning-type.md) partitions the rows using on a range of values, using the `VALUES LESS THAN` operator. `VALUES IN` is not allowed with `RANGE`. The partition function can be any valid SQL expression which returns a single value.
* [LIST](../../../../server-usage/partitioning-tables/partitioning-types/list-partitioning-type.md) assigns partitions based on a table's column with a restricted set of possible values. It is similar to `RANGE`, but `VALUES IN` must be used for at least 1 columns, and `VALUES LESS THAN` is disallowed.
* `SYSTEM_TIME` partitioning is used for [System-versioned tables](../../../sql-structure/temporal-tables/system-versioned-tables.md) to store historical data separately from current data.

Only [HASH](../../../../server-usage/partitioning-tables/partitioning-types/hash-partitioning-type.md) and [KEY](../../../../server-usage/partitioning-tables/partitioning-types/key-partitioning-type.md) can be used for subpartitions, and they can be `[LINEAR]`.

It is possible to define up to 8092 partitions and subpartitions.

The number of defined partitions can be optionally specified as `PARTITION count`. This can be done to avoid specifying all partitions individually. But you can also declare each individual partition and, additionally, specify a `PARTITIONS count` clause; in the case, the number of `PARTITION`s must equal count.

Also see [Partitioning Types Overview](../../../../server-usage/partitioning-tables/partitioning-types/partitioning-types-overview.md).

{% tabs %}
{% tab title="Current" %}
The `PARTITION` keyword is optional as part of the partition definition. Instead of this:

```sql
CREATE OR REPLACE TABLE t1 (x INT)
  PARTITION BY RANGE(x) (
    partition p1 values less than (10),
    partition p2 values less than (20),
    partition p3 values less than (30),
    partition p4 values less than (40),
    partition p5 values less than (50),
    partition pn values less than maxvalue);
```

The following can be used:

```sql
CREATE OR REPLACE TABLE t1 (x INT)
  PARTITION BY RANGE(x) (
    p1 values less than (10),
    p2 values less than (20),
    p3 values less than (30),
    p4 values less than (40),
    p5 values less than (50),
    pn values less than maxvalue);
```
{% endtab %}

{% tab title="< 10.7.1" %}
The `PARTITION` keyword is not optional as part of the partition definition. You must use this syntax:

```sql
CREATE OR REPLACE TABLE t1 (x INT)
  PARTITION BY RANGE(x) (
    partition p1 values less than (10),
    partition p2 values less than (20),
    partition p3 values less than (30),
    partition p4 values less than (40),
    partition p5 values less than (50),
    partition pn values less than maxvalue);
```
{% endtab %}
{% endtabs %}

## Sequences

`CREATE TABLE` can also be used to create a [SEQUENCE](../../../sql-structure/sequences/). See [CREATE SEQUENCE](../../../sql-structure/sequences/create-sequence.md) and [Sequence Overview](../../../sql-structure/sequences/sequence-overview.md).

## Atomic DDL

{% tabs %}
{% tab title="Current" %}
MariaDB supports [Atomic DDL](../atomic-ddl.md). `CREATE TABLE` is atomic, except for `CREATE OR REPLACE`, which are only crash-safe.
{% endtab %}

{% tab title="< 10.6.1" %}
\-
{% endtab %}
{% endtabs %}

## Examples

```sql
CREATE TABLE IF NOT EXISTS test (
a BIGINT auto_increment PRIMARY KEY,
name VARCHAR(128) charset utf8,
KEY name (name(32))
) engine=InnoDB default charset latin1;
```

This example shows a couple of things:

* Usage of `IF NOT EXISTS`; If the table already existed, it will not be created. There will not be any error for the client, just a warning.
* How to create a `PRIMARY KEY` that is [automatically generated](../../../data-types/auto_increment.md).
* How to specify a table-specific [character set](../../../data-types/string-data-types/character-sets/) and another for a column.
* How to create an index (`name`) that is only partly indexed (to save space).

The following clauses will work:

```sql
CREATE TABLE t1(
  a int DEFAULT (1+1),
  b int DEFAULT (a+1),
  expires DATETIME DEFAULT(NOW() + INTERVAL 1 YEAR),
  x BLOB DEFAULT USER()
);
```

## See Also

* [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md)
* [ALTER TABLE](../alter/alter-table.md)
* [DROP TABLE](../drop/drop-table.md)
* [Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md)
* [CREATE TABLE with Vectors](../../../sql-structure/vectors/create-table-with-vectors.md)
* Storage engines can add their own [attributes for columns, indexes and tables](../../../../server-usage/storage-engines/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes.md)
* Variable [slave-ddl-exec-mode](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)
* [InnoDB Limitations](https://mariadb.com/kb/en/InnoDB_Limitations)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}

[^1]: [#index-definitions](create-table.md#index-definitions "mention")

[^2]: [#periods](create-table.md#periods "mention")

[^3]: [data-types](../../../data-types/ "mention")
