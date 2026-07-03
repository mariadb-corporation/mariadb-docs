# Indexes

For a basic overview, see [The Essentials of an Index](essentials-of-an-index-guide.md).

There are four main kinds of indexes; primary keys (unique and not null), unique indexes (unique and can be null), plain indexes (not necessarily unique) and full-text indexes (for full-text searching).

The terms 'KEY' and 'INDEX' are generally used interchangeably, and statements should work with either keyword.

## Primary Key

A primary key is unique and can never be null. It will always identify only one record, and each record must be represented. Each table can only have one primary key.

In [InnoDB](../server-usage/storage-engines/innodb/) tables, all indexes contain the primary key as a suffix. Thus, when using this storage engine, keeping the primary key as small as possible is particularly important. If a primary key does not exist and there are no UNIQUE indexes, InnoDB creates a 6-bytes clustered index which is invisible to the user.

Many tables use a numeric ID field as a primary key. The [AUTO\_INCREMENT](../reference/data-types/auto_increment.md) attribute can be used to generate a unique identity for new rows, and is commonly-used with primary keys.

Primary keys are usually added when the table is created with the [CREATE TABLE](../reference/sql-statements/data-definition/create/create-table.md#indexes) statement. For example, the following creates a primary key on the ID field. Note that the ID field had to be defined as NOT NULL, otherwise the index could not have been created.

```sql
CREATE TABLE `Employees` (
  `ID` TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `First_Name` VARCHAR(25) NOT NULL,
  `Last_Name` VARCHAR(25) NOT NULL,
  `Position` VARCHAR(25) NOT NULL,
  `Home_Address` VARCHAR(50) NOT NULL,
  `Home_Phone` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`ID`)
);
```

You cannot create a primary key with the [CREATE INDEX](../reference/sql-statements/data-definition/create/create-index.md) command. If you do want to add one after the table has already been created, use [ALTER TABLE](../reference/sql-statements/data-definition/alter/alter-table.md), for example:

```sql
ALTER TABLE Employees ADD PRIMARY KEY(ID);
```

### Finding Tables Without Primary Keys

Tables in the `INFORMATION_SCHEMA`database can be queried to find tables that do not have primary keys. For example, here is a query using the [TABLES](../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) and [KEY\_COLUMN\_USAGE](../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-key_column_usage-table.md) tables that can be used:

```sql
SELECT t.TABLE_SCHEMA, t.TABLE_NAME
FROM information_schema.TABLES AS t
LEFT JOIN information_schema.KEY_COLUMN_USAGE AS c 
ON t.TABLE_SCHEMA = c.CONSTRAINT_SCHEMA
   AND t.TABLE_NAME = c.TABLE_NAME
   AND c.CONSTRAINT_NAME = 'PRIMARY'
WHERE t.TABLE_SCHEMA != 'information_schema'
   AND t.TABLE_SCHEMA != 'performance_schema'
   AND t.TABLE_SCHEMA != 'mysql'
   AND c.CONSTRAINT_NAME IS NULL;
```

## Unique Index

A Unique Index must be unique, but it can have columns that may be NULL. So each key value identifies only one record, but not each record needs to be represented.

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)

Unique, if index type is not specified, is normally a BTREE index that can also be used by the optimizer to find rows. If the key is longer than the max key length for the used storage engine and the storage engine supports long unique index, a HASH key will be created. This enables MariaDB to enforce uniqueness for any type or number of columns.

For example, to create a unique key on the Employee\_Code field, as well as a primary key, use:

```sql
CREATE TABLE `Employees` (
  `ID` TINYINT(3) UNSIGNED NOT NULL,
  `First_Name` VARCHAR(25) NOT NULL,
  `Last_Name` VARCHAR(25) NOT NULL,
  `Position` VARCHAR(25) NOT NULL,
  `Home_Address` VARCHAR(50) NOT NULL,
  `Home_Phone` VARCHAR(12) NOT NULL,
  `Employee_Code` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY (`Employee_Code`)
);
```

Unique keys can also be added after the table is created with the [CREATE INDEX](../reference/sql-statements/data-definition/create/create-index.md) command, or with the [ALTER TABLE](../reference/sql-statements/data-definition/alter/alter-table.md) command, for example:

```sql
ALTER TABLE Employees ADD UNIQUE `EmpCode`(`Employee_Code`);
```

and

```sql
CREATE UNIQUE INDEX HomePhone ON Employees(Home_Phone);
```

Indexes can contain more than one column. MariaDB is able to use one or more columns on the leftmost part of the index, if it cannot use the whole index. (except for the HASH index type).

Take another example:

```sql
CREATE TABLE t1 (a INT NOT NULL, b INT, UNIQUE (a,b));

INSERT INTO t1 VALUES (1,1), (2,2);

SELECT * FROM t1;
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    2 |
+---+------+
```

Since the index is defined as unique over both columns _a_ and _b_, the following row is valid, as while neither _a_ nor _b_ are unique on their own, the combination is unique:

```sql
INSERT INTO t1 VALUES (2,1);

SELECT * FROM t1;
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    1 |
| 2 |    2 |
+---+------+
```

The fact that a `UNIQUE` constraint can be `NULL` is often overlooked. In SQL any `NULL` is never equal to anything, not even to another `NULL`. Consequently, a `UNIQUE` constraint will not prevent one from storing duplicate rows if they contain null values:

```sql
INSERT INTO t1 VALUES (3,NULL), (3, NULL);

SELECT * FROM t1;
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    1 |
| 2 |    2 |
| 3 | NULL |
| 3 | NULL |
+---+------+
```

Indeed, in SQL two last rows, even if identical, are not equal to each other:

```sql
SELECT (3, NULL) = (3, NULL);

+---------------------- +
| (3, NULL) = (3, NULL) |
+---------------------- +
| 0                     |
+---------------------- +
```

In MariaDB you can combine this with [virtual columns](../reference/sql-statements/data-definition/create/generated-columns.md) to\
enforce uniqueness over a subset of rows in a table:

```sql
CREATE TABLE Table_1 (
  user_name VARCHAR(10),
  status ENUM('Active', 'ON-Hold', 'Deleted'),
  del CHAR(0) AS (IF(status IN ('Active', 'ON-Hold'),'', NULL)) persistent,
  UNIQUE(user_name,del)
)
```

This table structure ensures that all _active_ or _on-hold_ users have distinct\
names, but as soon as a user is _deleted_, his name is no longer part of the\
uniqueness constraint, and another user may get the same name.

If a unique index consists of a column where trailing pad characters are stripped or ignored, inserts into that column where values differ only by the number of trailing pad characters will result in a duplicate-key error.

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)

For some engines, like InnoDB, `UNIQUE` can be used with any type of columns or any number of columns.

```sql
CREATE TABLE t1 (a INT PRIMARY KEY,
b BLOB,
c1 VARCHAR(1000),
c2 VARCHAR(1000),
c3 VARCHAR(1000),
c4 VARCHAR(1000),
c5 VARCHAR(1000),
c6 VARCHAR(1000),
c7 VARCHAR(1000),
c8 VARCHAR(1000),
c9 VARCHAR(1000),
UNIQUE KEY `b` (b),
UNIQUE KEY `all_c` (c1,c2,c3,c4,c6,c7,c8,c9)) ENGINE=myisam;
```

If the key length is longer than the max key length supported by the engine, a HASH key will be created.\
This can be seen with `SHOW CREATE TABLE table_name` or `SHOW INDEX FROM table_name`:

```sql
SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       TABLE: t1
CREATE TABLE: CREATE TABLE `t1` (
  `a` int(11) NOT NULL,
  `b` blob DEFAULT NULL,
  `c1` varchar(1000) DEFAULT NULL,
  `c2` varchar(1000) DEFAULT NULL,
  `c3` varchar(1000) DEFAULT NULL,
  `c4` varchar(1000) DEFAULT NULL,
  `c5` varchar(1000) DEFAULT NULL,
  `c6` varchar(1000) DEFAULT NULL,
  `c7` varchar(1000) DEFAULT NULL,
  `c8` varchar(1000) DEFAULT NULL,
  `c9` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`a`),
  UNIQUE KEY `b` (`b`) USING HASH,
  UNIQUE KEY `all_c` (`c1`,`c2`,`c3`,`c4`,`c6`,`c7`,`c8`,`c9`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci
```

## Plain Indexes

Indexes do not necessarily need to be unique. For example:

```sql
CREATE TABLE t2 (a INT NOT NULL, b INT, INDEX (a,b));

INSERT INTO t2 VALUES (1,1), (2,2), (2,2);

SELECT * FROM t2;
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    2 |
| 2 |    2 |
+---+------+
```

## Full-Text Indexes

Full-text indexes support full-text indexing and searching. See the [Full-Text Indexes](../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) section.

## Choosing Indexes

In general you should only add indexes to match the queries your application\
uses. Any extra will waste resources. In an application with very small tables,\
indexes will not make much difference but as soon as your tables are larger\
than your buffer sizes the indexes will start to speed things up dramatically.

Using the [EXPLAIN](../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) statement on your queries can help you decide which columns need indexing.

If you query contains something like `LIKE '%word%'`, without a fulltext index you are using a full table scan every time, which is very slow.

If your table has a large number of reads and writes, consider using delayed\
writes. This uses the db engine in a "batch" write mode, which cuts down on\
disk io, therefore increasing performance.

Use the [CREATE INDEX](../reference/sql-statements/data-definition/create/create-index.md) command to create an index.

If you are building a large table then for best performance add the index after\
the table is populated with data. This is to increase the insert performance\
and remove the index overhead during inserts.

## Viewing Indexes

You can view which indexes are present on a table, as well as details about them, with the [SHOW INDEX](../reference/sql-statements/administrative-sql-statements/show/show-index.md) statement.

If you want to know how to re-create an index, run `SHOW CREATE TABLE` .

## When to Remove an Index

If an index is rarely used (or not used at all) then remove it to increase INSERT,\
and UPDATE performance.

If [user statistics](../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) are enabled, the [Information Schema](../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/) [INDEX\_STATISTICS](../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md) table stores the index usage.

If the [slow query log](../server-management/server-monitoring-logs/slow-query-log/) is enabled and the `log_queries_not_using_indexes` server system variable is `ON`, the queries which do not use indexes are logged.

_The initial version of this article was copied, with permission, from_ [_Proper\_Indexing\_Strategy_](https://hashmysql.org/wiki/Proper_Indexing_Strategy) _on 2012-10-30._

## See Also

* [AUTO\_INCREMENT](../reference/data-types/auto_increment.md)
* [The Essentials of an Index](broken-reference/)

CC BY-SA / Gnu FDL
