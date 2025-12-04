---
description: >-
  The MERGE storage engine allows a collection of identical MyISAM tables to be
  treated as a single logical table, useful for managing large datasets.
---

# MERGE

## Description

The MERGE storage engine, also known as the MRG\_MyISAM engine, is a collection of identical [MyISAM](myisam-storage-engine/) tables that can be used as one. "Identical" means that all tables have identical column and index information. You cannot merge MyISAM tables in which the columns are listed in a different order, do not have exactly the same columns, or have the indexes in different order. However, any or all of the MyISAM tables can be compressed with [myisampack](../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md). Columns names and indexes names can be different, as long as data types and `NULL`/`NOT NULL` clauses are the same. Differences in table options such as `AVG_ROW_LENGTH`, `MAX_ROWS`, or `PACK_KEYS` do not matter.

Each index in a `MERGE` table must match an index in underlying `MyISAM` tables, but the opposite is not true. Also, a `MERGE` table cannot have a `PRIMARY KEY` or `UNIQUE` indexes, because it cannot enforce uniqueness over all underlying tables.

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
