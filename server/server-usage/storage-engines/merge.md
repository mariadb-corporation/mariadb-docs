---
description: >-
  The MERGE storage engine allows a collection of identical MyISAM tables to be
  treated as a single logical table, useful for managing large datasets.
---

# MERGE

## Description

The MERGE storage engine, also known as the MRG\_MyISAM engine, is a collection of identical [MyISAM](myisam-storage-engine/) tables that can be used as one. "Identical" means that all tables have identical column and index information. You cannot merge MyISAM tables in which the columns are listed in a different order, do not have exactly the same columns, or have the indexes in different order. However, any or all of the MyISAM tables can be compressed with [myisampack](../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md). Column names and index names can be different, as long as data types and `NULL`/`NOT NULL` clauses are the same. Differences in table options such as `AVG_ROW_LENGTH`, `MAX_ROWS`, or `PACK_KEYS` do not matter. The row format does matter: you cannot merge a table that has `ROW_FORMAT=FIXED` with one that has `ROW_FORMAT=DYNAMIC`.

The rules for indexes are described in [Index Usage](#index-usage).

The following options are meaningful for `MERGE` tables:

* `UNION`. This option specifies the list of the underlying `MyISAM` tables. The list is enclosed between parentheses and separated with commas. The underlying tables can be in different databases; qualify their names with the database name, for example `UNION=(t1,db2.t2)`.
* `INSERT_METHOD`. This option specifies whether, and how, `INSERT`s are allowed for the table. Allowed values are: `NO` (`INSERT`s are not allowed), `FIRST` (new rows are written into the first table specified in the `UNION` list), `LAST` (new rows are written into the last table specified in the `UNION` list). The default value is `NO`.

To change the list of underlying tables, use [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) with a new `UNION` list. This does not copy any data.

If you define a `MERGE` table with a definition which is different from the underlying `MyISAM` tables, or one of the underlying tables is not `MyISAM`, the `CREATE TABLE` statement does not return any error. But any statement which involves the table produces an error like the following:

```sql
ERROR 1168 (HY000): Unable to open underlying table which is differently defined 
  or of non-MyISAM type or doesn't exist
```

A [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md) shows more information about the problem.

The error is also produced if the table is properly defined, but an underlying table's definition changes at some point in time.

If you try to insert a new row into a `MERGE` table with `INSERT_METHOD=NO`, you get an error like the following:

```sql
ERROR 1036 (HY000): Table 'tbl_name' is read only
```

## Index Usage

A `MERGE` table has no index files of its own. It uses the indexes of the underlying `MyISAM` tables, so its index definitions must match them:

* The indexes of the `MERGE` table must match the first indexes of each underlying table, in the same order. Indexes are compared by position, not by name.
* The underlying tables can have more indexes than the `MERGE` table. The extra indexes are not used through the `MERGE` table.
* An index that does not match the index in the same position of every underlying table causes error 1168. This includes an index that the underlying tables do not have at all, and an index defined in a different order.

For example, if the underlying tables have `PRIMARY KEY (a), INDEX (b), INDEX (c)`, a `MERGE` table can declare no indexes, `INDEX (a)`, or `INDEX (a), INDEX (b)`. It cannot declare `INDEX (b)` alone, or `INDEX (b), INDEX (a)`.

For a lookup through an index, the server searches the index of every underlying table and returns the matching rows in index order. The cost of an index lookup therefore grows with the number of underlying tables. Index lookups on a `MERGE` table over many tables are slower than on one table that holds the same rows.

### Unique Indexes

A `MERGE` table cannot enforce uniqueness across its underlying tables. Each underlying table enforces its own unique indexes, so the same value can exist in several of them.

Inserting through the `MERGE` table checks only the table that receives the row (the first or last table, depending on `INSERT_METHOD`). A value that already exists in another underlying table is accepted.

You can declare a `PRIMARY KEY` or `UNIQUE` index on a `MERGE` table, but avoid it. The optimizer trusts the declaration and stops after the first matching row, so a lookup misses the matching rows in the other underlying tables. Declare a plain `INDEX` on the `MERGE` table instead, even when the column is a `PRIMARY KEY` in the underlying tables. The [examples](#examples) show the difference.

## Generated Columns

A `MERGE` table cannot declare [generated columns](../../reference/sql-statements/data-definition/create/generated-columns.md). Doing so fails with:

```sql
ERROR 1910 (HY000): MRG_MyISAM storage engine does not support generated columns
```

You can build a `MERGE` table on `MyISAM` tables that have stored (`PERSISTENT`) generated columns. The `MERGE` table sees them as regular columns: declare them as ordinary columns with the same data type and the same `NULL`/`NOT NULL` clause.

`VIRTUAL` generated columns are not stored in the `MyISAM` tables. Avoid them in tables you want to merge: unless they are the last columns of each underlying table and are left out of the `MERGE` table definition, any statement on the `MERGE` table fails with error 1168.

## Examples

### Creating a MERGE Table

```sql
CREATE TABLE t1 (
    a INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    message CHAR(20)) ENGINE=MyISAM;

CREATE TABLE t2 (
    a INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    message CHAR(20)) ENGINE=MyISAM;

INSERT INTO t1 (message) VALUES ('Testing'),('table'),('t1');

INSERT INTO t2 (message) VALUES ('Testing'),('table'),('t2');

CREATE TABLE total (
    a INT NOT NULL AUTO_INCREMENT,
    message CHAR(20), INDEX(a))
    ENGINE=MERGE UNION=(t1,t2) INSERT_METHOD=LAST;

SELECT * FROM total;
+---+---------+
| a | message |
+---+---------+
| 1 | Testing |
| 2 | table   |
| 3 | t1      |
| 1 | Testing |
| 2 | table   |
| 3 | t2      |
+---+---------+
```

The column `a` is a `PRIMARY KEY` in `t1` and `t2`, but a plain `INDEX` in `total`.

### Using the Index

A lookup on `a` uses the index and finds the matching row in each underlying table:

```sql
EXPLAIN SELECT * FROM total WHERE a = 2;
+------+-------------+-------+------+---------------+------+---------+-------+------+-------+
| id   | select_type | table | type | possible_keys | key  | key_len | ref   | rows | Extra |
+------+-------------+-------+------+---------------+------+---------+-------+------+-------+
|    1 | SIMPLE      | total | ref  | a             | a    | 4       | const | 2    |       |
+------+-------------+-------+------+---------------+------+---------+-------+------+-------+

SELECT * FROM total WHERE a = 2;
+---+---------+
| a | message |
+---+---------+
| 2 | table   |
| 2 | table   |
+---+---------+
```

The same lookup on a `MERGE` table that declares `a` as its `PRIMARY KEY` returns only one of the two rows:

```sql
CREATE TABLE total_pk (
    a INT NOT NULL AUTO_INCREMENT,
    message CHAR(20), PRIMARY KEY(a))
    ENGINE=MERGE UNION=(t1,t2) INSERT_METHOD=LAST;

SELECT * FROM total_pk WHERE a = 2;
+---+---------+
| a | message |
+---+---------+
| 2 | table   |
+---+---------+
```

### Inserting Rows

With `INSERT_METHOD=LAST`, new rows go into `t2`. The unique check covers only `t2`, so a value that exists only in `t1` is accepted:

```sql
INSERT INTO total VALUES (2, 'duplicate');
ERROR 1062 (23000): Duplicate entry '2' for key 'a'

INSERT INTO t1 VALUES (5, 'only in t1');

INSERT INTO total VALUES (5, 'also in t2');

SELECT * FROM total WHERE a = 5;
+---+------------+
| a | message    |
+---+------------+
| 5 | only in t1 |
| 5 | also in t2 |
+---+------------+
```

### Adding an Underlying Table

To add a table, for example a new table for each month of log data, create it with the same definition and change the `UNION` list:

```sql
CREATE TABLE t3 LIKE t1;

ALTER TABLE total UNION=(t1,t2,t3);
```

New rows now go into `t3`, the last table in the list.

### Finding a Mismatched Table

In the following example, we create three `MyISAM` tables, and then a `MERGE` table on them. However, one of them uses a different data type for the column b, so a `SELECT` produces an error:

```sql
CREATE TABLE s1 (
  a INT,
  b INT
) ENGINE = MyISAM;

CREATE TABLE s2 (
  a INT,
  b INT
) ENGINE = MyISAM;

CREATE TABLE s3 (
  a INT,
  b TINYINT
) ENGINE = MyISAM;

CREATE TABLE t_mrg (
  a INT,
  b INT
) ENGINE = MERGE,UNION=(s1,s2,s3);

SELECT * FROM t_mrg;
ERROR 1168 (HY000): Unable to open underlying table which is differently defined
 or of non-MyISAM type or doesn't exist
```

To find out what's wrong, use `CHECK TABLE`:

```sql
CHECK TABLE t_mrg\G
*************************** 1. row ***************************
   Table: test.t_mrg
      Op: check
Msg_type: Error
Msg_text: Table 'test.s3' is differently defined or of non-MyISAM type or doesn't exist
*************************** 2. row ***************************
   Table: test.t_mrg
      Op: check
Msg_type: Error
Msg_text: Unable to open underlying table which is differently defined or of non-MyISAM type or doesn't exist
*************************** 3. row ***************************
   Table: test.t_mrg
      Op: check
Msg_type: error
Msg_text: Corrupt
```

The problem is in `s3`'s definition.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
