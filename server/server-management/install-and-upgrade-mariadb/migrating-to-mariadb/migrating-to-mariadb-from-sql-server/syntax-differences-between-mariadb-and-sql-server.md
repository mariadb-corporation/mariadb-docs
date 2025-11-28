# Syntax Differences between MariaDB and SQL Server

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

This article contains a non-exhaustive list of syntax differences between MariaDB and SQL Server and is written for SQL Server users who are unfamiliar with MariaDB.

## Compatibility Features

Some features are meant to improve syntax and semantics compatibility between MariaDB versions, between MariaDB and MySQL, and between MariaDB and other DBMSs. This section focuses on compatibility between MariaDB and SQL Server.

### sql\_mode and old\_mode

SQL semantics and syntax, in MariaDB, are affected by the [sql\_mode](../../../variables-and-modes/sql_mode.md) variable. Its value is a comma-separated list of flags, and each of them, if specified, affects a different aspect of SQL syntax and semantics.

A particularly important flag for users familiar with SQL Server is [MSSQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql).

sql\_mode can be changed locally, in which case it only affects the current session; or globally, in which case it will affect all new connections (but not the connections already established). sql\_mode must be assigned a comma-separated list of flags.

A usage example:

```
# check the current global and local sql_mode values
SELECT @@global.sql_mode;
SELECT @@session.sql_mode;
# empty sql_mode for all users
SET GLOBAL sql_mode = '';
# add MSSQL flag to the sql_mode for the current session
SET SESSION sql_mode = CONCAT(sql_mode, ',MSSQL');
```

[old\_mode](../../../variables-and-modes/old_mode.md) is very similar to sql\_mode, but its purpose is to provide compatibility with older MariaDB versions. Its flags shouldn't affect compatibility with SQL Server (though it is theoretically possible that some of them do, as a side effect).

### Executable Comments

MariaDB supports [executable comments](../../../../reference/sql-statements/comment-syntax.md#executable-comment-syntax). These are designed to write generic queries that are only executed by MariaDB, and optionally only certain versions.

The following examples show how to insert SQL code that will be ignored by SQL Server but executed by MariaDB, or some of its versions.

* Executed by MariaDB and MySQL (see below):

```
SELECT * FROM tab /*! FORCE INDEX (idx_a) */ WHERE a = 1 OR b = 2;
```

* Executed by MariaDB only:

```
SELECT * /*M! , @in_transaction */ FROM tab;
```

* Executed by MariaDB starting from version 10.0.5:

```
DELETE FROM user WHERE id = 100 /*!M100005 RETURNING email */;
```

As explained in the [Understanding MariaDB Architecture](understanding-mariadb-architecture.md) page, MariaDB was initially forked from MySQL. At that time, executable comments were already supported by MySQL. This is why the `/*! ... */` syntax is supported by both MariaDB and MySQL. But because MariaDB also supports specific syntax not supported by MySQL, it added the `/*M! ... */` syntax.

## Generic Syntax

Here we discuss some differences between MariaDB and SQL Server syntax that may affect any user, as well as some hints to make queries compatible with a reasonable amount of work.

### Delimiters

SQL Server uses two different terminators:

* The batch terminator is the `go` command. It tells Microsoft clients to send the text we typed to SQL Server.
* The query terminator is a semicolon (`;`) and it tells SQL Server where a query ends.

It is rarely necessary to use `;` in SQL Server. It is required for certain common table expressions, for example.

But the same doesn't apply to MariaDB. **Normally, with MariaDB**, **you only use `;`.**

However, MariaDB also has some situations where you want to use a `;` but you don't want the [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command-line client to send the query yet. This can be done in any situation, but it is particularly useful when creating [stored routines](../../../../server-usage/stored-routines/) or using [BEGIN NOT ATOMIC](../../../../reference/sql-statements/programmatic-compound-statements/begin-end.md).

The reason is better explained with an example:

```
CREATE PROCEDURE p()
BEGIN
    SELECT * FROM t1;
    SELECT * FROM t2;
END;
```

If we enter this procedure in this way in the `mariadb` client, as soon as we type the first `;` (after the first `SELECT`) and press enter, the statement will be sent. MariaDB will try to parse it and will return an error.

To avoid this, `mariadb` implements the [DELIMITER](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#delimiters) statement. This client statement is never sent to MariaDB. Instead, the client uses it to find out when the typed query should be sent. Let's correct the above example:

```
DELIMITER ||

CREATE PROCEDURE p()
BEGIN
    SELECT * FROM t1;
    SELECT * FROM t2;
END;

DELIMITER ;
```

### Names

In MariaDB, most [names](../../../../reference/sql-structure/sql-language-structure/identifier-names.md) have a maximum length of 64 characters. When migrating an SQL Server database to MariaDB, check if some names exceed this limit (SQL Server maximum length is 128).

By default, MariaDB names are case-sensitive if the operating system has case-sensitive file names (Linux), and case-insensitive if the operating system is case-insensitive (Windows). SQL Server is case-insensitive by default on all operating systems.

When migrating a SQL Server database to MariaDB on Linux, to avoid problems, you may want to set the [lower\_case\_table\_names](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lower_case_table_names) system variable to 1, making table names, database names, and aliases case-insensitive.

Names can be quoted inside backtick characters (\`\`\`). This character can be used in names, in which case it should be doubled. By default, this is the only way to quote names.

To also enable the use of double quotes (`"`), modify sql\_mode by adding the `ANSI_QUOTES` flag. This is the equivalent of setting [QUOTED\_IDENTIFIER](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-quoted-identifier-transact-sql?view=sql-server-ver15) ON in SQL Server.

To also enable the use of SQL Server style quotes (`[` and `]`), modify sql\_mode by adding the `MSSQL` flag.

The case-sensitivity of stored procedures and functions is never a problem, as they are case-insensitive in SQL Server.

### Quoting Strings

In SQL Server, by default, strings can only be quoted with single-quotes (`'`), and to use a double quote in a string, it should be doubled (`''`). This also works by default in MariaDB.

SQL Server also allows to use of double quotes (`"`) to quote strings. This works by default in MariaDB, but as mentioned before, it won't work if sql\_mode contains the `ANSI_QUOTES` flag.

### NULL

The default semantics of [NULL](../../../../reference/data-types/null-values.md) in SQL Server and MariaDB are the same, by default.

However, SQL Server allows one to change it globally with [SET ANSI\_NULLS OFF](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-ansi-nulls-transact-sql), or at the database level with [ALTER DATABASE](../../../../reference/sql-statements/data-definition/alter/alter-database.md).

There is no way to achieve exactly the same result in MariaDB. To perform NULL-safe comparisons in MariaDB, one should replace the [=](../../../../reference/sql-structure/operators/comparison-operators/equal.md) operator with the [<=>](../../../../reference/sql-structure/operators/comparison-operators/null-safe-equal.md) operator.

Also, note that MariaDB doesn't support the `UNKNOWN` pseudo-value. An expression like `NULL OR 0` returns `NULL` in MariaDB.

### LIKE

In MariaDB, [LIKE](../../../../reference/sql-functions/string-functions/like.md) expressions only have two characters with special meanings: `%` and `_`. These two characters have the same meanings they have in SQL Server.

The additional characters recognized by SQL Server (`[`, `]` and `^`) are part of regular expressions. MariaDB supports the [REGEXP](../../../../reference/sql-functions/string-functions/regular-expressions-functions/regexp.md) operator that supports the full regular expression syntax.

## Data Definition Language

Here we discuss some DDL differences that database administrators will want to be aware of.

While this section is meant to highlight the most noticeable DDL differences between MariaDB and SQL Server, there are many others, both in the syntax and in the semantics. See the [ALTER](../../../../reference/sql-statements/data-definition/alter/) statement documentation.

### Altering Tables Online

Altering tables online can be a problem, especially when the tables are big and we don't want to cause a disruption.

MariaDB offers the following solutions to help:

* The [ALTER TABLE ... ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table/#algorithm) clause allows one to specify which algorithm should be used to run a certain operation. For example, `INPLACE` tells MariaDB not to create a table copy (perhaps because we don't have enough disk space), and `INSTANT` tells MariaDB to execute the operation instantaneously. Not all algorithms are supported for certain operations. If the algorithm we've chosen cannot be used, the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement will fail with an error.
* The [ALTER TABLE ... LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table/#alock) clause allows one to specify which lock type should be used. For example, `NONE` tells MariaDB to avoid any lock on the table and `SHARED` only allows one to acquire a share lock. If the operation requires a lock that is more strict than the one, we are requesting, the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement will fail with an error. Sometimes this happens because the `LOCK` level we want is not available for the specified `ALGORITHM`.

To find out which operations require a table copy and which lock levels are necessary, see [InnoDB Online DDL Overview](../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-overview.md).

An `ALTER TABLE` can be queued because a long-running statement (even a `SELECT`) requires a [metadata lock](../../../../reference/sql-statements/transactions/metadata-locking.md). Since this may cause trouble, sometimes we want the operation to simply fail if the wait is too long. This can be achieved with the [WAIT and NOWAIT](../../../../reference/sql-statements/transactions/wait-and-nowait.md) clauses, whose syntax is a bit different from SQL Server.

SQL Server `WITH ONLINE = ON` is equivalent to MariaDB `LOCK = NONE`. However, note that [most ALTER TABLE statements](../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) support `ALGORITHM = INSTANT`, which is non-blocking and much faster (almost instantaneous, as the syntax suggests).

### IF EXISTS, IF NOT EXISTS, OR REPLACE

Most DDL statements, including [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/), support the following syntax:

* `DROP IF EXISTS`: A warning (not an error) is produced if the object does not exist.
* `OR REPLACE`: If the object exists, it is dropped and recreated; otherwise, it is created. This operation is atomic, so at no point in time does the object not exist.
* `CREATE IF NOT EXISTS`: If the object already exists, a warning (not an error) is produced. The object will not be replaced.

These statements are functionally similar (but less verbose) than SQL Server snippets similar to the following:

```
IF NOT EXISTS (
        SELECT name
            FROM sysobjects
            WHERE name = 'my_table' AND xtype = 'U'
    )
    CREATE TABLE my_table (
        ...
    )
go
```

### Altering Columns

With SQL Server, the only syntax to alter a table column is `ALTER TABLE ... ALTER COLUMN`. MariaDB provides more [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) commands to obtain the same result:

* [CHANGE COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#change-column) allows one to perform any change by specifying a new column definition, including the name.
* [MODIFY COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#modify-column) allows any change, except renaming the column. This is a slightly simpler syntax that we can use when we don't want to change a column name.
* [ALTER COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#alter-column) allows one to change or drop the `DEFAULT` value.
* [RENAME COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#rename-column) allows one to only change the column name.

Using a more specific syntax is less error-prone. For example, by using `ALTER TABLE ... ALTER COLUMN`,we will not accidentally change the data type.

The word `COLUMN` is usually optional, except in the case of `RENAME COLUMN`.

### SHOW Statements

MariaDB supports [SHOW](../../../../reference/sql-statements/administrative-sql-statements/show/) statements to quickly list all objects of a certain type (tables, views, triggers...). Most `SHOW` statements support a `LIKE` clause to filter data. For example, to list the tables in the current database whose name begins with 'wp\_':

```
SHOW TABLES LIKE 'wp\_%';
```

This is the equivalent of this query, which would work on both MariaDB and SQL Server:

```
SELECT TABLE_SCHEMA, TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME LIKE 'wp\_';
```

### SHOW CREATE Statements

In general, for each `CREATE` statement, MariaDB also supports a `SHOW CREATE` statement. For example, there is a [SHOW CREATE TABLE](../../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) that returns the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement that can be used to recreate a table.

Though SQL Server has no way to show the DDL statement to recreate an object, `SHOW CREATE` statements are functionally similar to `sp_helptext()`.

### Database Comments

MariaDB does not support extended properties. Instead, it supports a `COMMENT` clause for most [CREATE](../../../../reference/sql-statements/data-definition/create/) and [ALTER](../../../../reference/sql-statements/data-definition/alter/) statements.

For example, to create and then change a table comment:

```
CREATE TABLE counter (
    c INT UNSIGNED AUTO_INCREMENT PRIMARY KEY
)
    COMMENT 'Monotonic counter'
;
ALTER TABLE counter COMMENT
    'Counter. It can contain many values, we only care about the max';
```

Comments can be seen with `SHOW CREATE` statements or by querying `information_schema` tables. For example:

```
SELECT TABLE_COMMENT
    FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = 'test' AND TABLE_NAME = 'counter';
+-----------------------------------------------------------------+
| TABLE_COMMENT                                                   |
+-----------------------------------------------------------------+
| Counter. It can contain many values, we only care about the max |
+-----------------------------------------------------------------+
```

### Error Handling

MariaDB [SHOW ERRORS](../../../../reference/sql-statements/administrative-sql-statements/show/show-errors.md) and [SHOW WARNINGS](../../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) statements can be used to show errors, or warnings and errors. This is convenient for clients, but stored procedures cannot work with the output of these commands.

Instead, inside stored procedures, you can:

* Use the [GET DIAGNOSTICS](../../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics.md) command to assign error properties to variables. This is the equivalent of using SQL Server functions like `ERROR_NUMBER()` or `ERROR_STATE()`.
* Add a [DECLARE HANDLER](../../../../reference/sql-statements/programmatic-compound-statements/declare-handler.md) block to handle all errors, a class of errors, or a specific error. This is the equivalent of SQL Server `TRY ... CATCH`.
* An error or warning can be generated on purpose using [SIGNAL](../../../../reference/sql-statements/programmatic-compound-statements/signal.md). Inside a `DECLARE HANDLER` block, [RESIGNAL](../../../../reference/sql-statements/programmatic-compound-statements/resignal.md) can be used to issue the error again and interrupt the execution of the block. These are the equivalents of SQL Server `RAISERROR()`.

## Administration

Administration and maintenance commands in MariaDB use a different syntax from SQL Server.

* [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) rebuilds table data and indexes. It can be considered as the MariaDB equivalent of SQL Server's `ALTER INDEX REBUILD`. See [Defragmenting InnoDB Tablespaces](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) for more information. This statement is always locked. It supports [WAIT and NOWAIT](../../../../reference/sql-statements/transactions/wait-and-nowait.md) syntax,
* MariaDB has an [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) command, which is equivalent to `UPDATE STATISTICS`.

## BULK INSERT

MariaDB has no `BULK INSERT` statement. Instead, it supports:

* [LOAD DATA INFILE](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) to load data from files in CSV or similar formats;
* [LOAD XML INFILE](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-xml.md) to load data from XML files.

See also [How to Quickly Insert Data Into MariaDB](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/how-to-quickly-insert-data-into-mariadb.md).

## See Also

* [SQL Server and MariaDB Types Comparison](sql-server-and-mariadb-types-comparison.md)
* [MariaDB Transactions and Isolation Levels for SQL Server Users](mariadb-transactions-and-isolation-levels-for-sql-server-users.md)
* [SQL\_MODE=MSSQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
