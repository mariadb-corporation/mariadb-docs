---
description: >-
  The MERGE storage engine allows a collection of identical MyISAM tables to be
  treated as a single logical table, useful for managing large datasets.
---

# MERGE

## Description

The MERGE storage engine, also known as the MRG\_MyISAM engine, is a collection of identical [MyISAM](myisam-storage-engine/) tables that can be used as one. "Identical" means that all tables have identical column and index information. You cannot merge MyISAM tables in which the columns are listed in a different order, do not have exactly the same columns, or have the indexes in different order. However, any or all of the MyISAM tables can be compressed with [myisampack](../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md). Columns names and indexes names can be different, as long as data types and `NULL`/`NOT NULL` clauses are the same. Differences in table options such as `AVG_ROW_LENGTH`, `MAX_ROWS`, or `PACK_KEYS` do not matter.

Each index in a `MERGE` table must match the index in the same position in every underlying `MyISAM` table, but the underlying tables can have additional indexes. A `MERGE` table can declare a `PRIMARY KEY` or `UNIQUE` index, but it cannot enforce uniqueness across the underlying tables. See [Indexes](#indexes).

The following options are meaningful for `MERGE` tables:

* `UNION`. This option specifies the list of the underlying `MyISAM` tables. The list is enclosed between parentheses and separated with commas.
* `INSERT_METHOD`. This options specifies whether, and how, `INSERT`s are allowed for the table. Allowed values are: `NO` (`INSERT`s are not allowed), `FIRST` (new rows are written into the first table specified in the `UNION` list), `LAST` (new rows are written into the last table specified in the `UNION` list). The default value is `NO`.

If you define a `MERGE` table with a definition which is different from the underlying `MyISAM` tables, or one of the underlying tables is not `MyISAM`, the `CREATE TABLE` statement will not return any error. But any statement which involves the table will produce an error like the following:

```sql
ERROR 1168 (HY000): Unable to open underlying table which is differently defined 
  or of non-MyISAM type or doesn't exist
```

A [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md) will show more information about the problem.

The error is also produced if the table is properly define, but an underlying table's definition changes at some point in time.

If you try to insert a new row into a `MERGE` table with `INSERT_METHOD=NO`, you will get an error like the following:

```sql
ERROR 1036 (HY000): Table 'tbl_name' is read only
```

It is possible to build a `MERGE` table on `MyISAM` tables which have one or more [virtual columns](../../reference/sql-statements/data-definition/create/generated-columns.md). `MERGE` itself does not support virtual columns, thus such columns are seen as regular columns. The data types and sizes will still need to be identical, and they cannot be `NOT NULL`.

## Indexes

### How MERGE Indexes Map to the Underlying Tables

MariaDB compares the indexes of a `MERGE` table with the indexes of each underlying table by position: the first index with the first index, the second with the second, and so on. Each pair must index the same columns in the same order, with the same data types, lengths, collations, and sort direction (`ASC` or `DESC`). Index names do not have to match, and neither does the kind of index: a plain `INDEX` on the `MERGE` table can match a `PRIMARY KEY` or `UNIQUE` index on an underlying table.

An underlying table can have more indexes than the `MERGE` table, as long as the extra indexes come after the ones the `MERGE` table defines. If the indexes don't line up, statements on the `MERGE` table fail with error 1168, as with any other definition mismatch.

### Uniqueness

A `PRIMARY KEY` or `UNIQUE` index on a `MERGE` table does not make values unique across the underlying tables. The same value can exist in several underlying tables, and a `SELECT` on the `MERGE` table returns every copy. When you insert through the `MERGE` table, the row is written to the first or last underlying table (see `INSERT_METHOD`), and only that table's own unique indexes are checked, including unique indexes that the `MERGE` table does not declare.

{% hint style="warning" %}
If a `MERGE` table declares a `PRIMARY KEY` or `UNIQUE` index, the optimizer treats that index as unique. An equality lookup on it, such as `WHERE a = 2`, can return only the first matching row, even when several underlying tables contain that value. To get every matching row, declare a non-unique `INDEX` on the `MERGE` table instead, as in the examples below.
{% endhint %}

### Index Lookups

The optimizer can use `MERGE` table indexes for lookups, range scans, `ORDER BY`, and index-only (covering) reads. Each index lookup searches the index of every underlying table and merges the results in index order, so a lookup costs more as you add underlying tables.

## Examples

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

Uniqueness is enforced only within each underlying table, so the value `2` appears once in `t1` and once in `t2`. An index lookup on the `MERGE` table returns both rows:

```sql
SELECT * FROM total WHERE a = 2;
+---+---------+
| a | message |
+---+---------+
| 2 | table   |
| 2 | table   |
+---+---------+
```

In the following example, the `MERGE` table declares only the first of the underlying table's two `UNIQUE` indexes. An insert through the `MERGE` table is still rejected when it would duplicate a value in the second index, because the underlying table checks its own indexes:

```sql
CREATE TABLE t4 (c1 INT, c2 INT, UNIQUE (c1), UNIQUE (c2)) ENGINE=MyISAM;
CREATE TABLE m4 (c1 INT, c2 INT, UNIQUE (c1)) ENGINE=MERGE UNION=(t4) INSERT_METHOD=LAST;

INSERT INTO m4 VALUES (1,2);
INSERT INTO m4 VALUES (3,2);
ERROR 1022 (23000): Can't write; duplicate key in table 'm4'
```

In the following example, we'll create three `MyISAM` tables, and then a `MERGE` table on them. However, one of them uses a different data type for the column b, so a `SELECT` will produce an error:

```sql
CREATE TABLE t1 (
  a INT,
  b INT
) ENGINE = MyISAM;

CREATE TABLE t2 (
  a INT,
  b INT
) ENGINE = MyISAM;

CREATE TABLE t3 (
  a INT,
  b TINYINT
) ENGINE = MyISAM;

CREATE TABLE t_mrg (
  a INT,
  b INT
) ENGINE = MERGE,UNION=(t1,t2,t3);

SELECT * FROM t_mrg;
ERROR 1168 (HY000): Unable to open underlying table which is differently defined
 or of non-MyISAM type or doesn't exist
```

To find out what's wrong, we'll use a `CHECK TABLE`:

```sql
CHECK TABLE t_mrg\G
*************************** 1. row ***************************
   Table: test.t_mrg
      Op: check
Msg_type: Error
Msg_text: Table 'test.t3' is differently defined or of non-MyISAM type or doesn't exist
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

Now, we know that the problem is in `t3`'s definition.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
