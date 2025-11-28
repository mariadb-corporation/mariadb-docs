---
description: >-
  Concatenate strings from a group. This function joins non-NULL values from
  multiple rows into a single string, with an optional separator.
---

# GROUP\_CONCAT

## Syntax

```sql
GROUP_CONCAT(expr)
```

## Description

This function returns a string result with the concatenated non-NULL values from a group. If any expr in GROUP\_CONCAT evaluates to NULL, that tuple is not present in the list returned by GROUP\_CONCAT.

It returns NULL if all arguments are NULL, or there are no matching rows.

The maximum returned length in bytes is determined by the [group\_concat\_max\_len](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#group_concat_max_len) server system variable, which defaults to 1M.

If group\_concat\_max\_len <= 512, the return type is [VARBINARY](../../data-types/string-data-types/varbinary.md) or [VARCHAR](../../data-types/string-data-types/varchar.md); otherwise, the return type is [BLOB](../../data-types/string-data-types/blob.md) or [TEXT](../../data-types/string-data-types/text.md). The choice between binary or non-binary types depends from the input.

The full syntax is as follows:

```sql
GROUP_CONCAT([DISTINCT] expr [,expr ...]
             [ORDER BY {unsigned_integer | col_name | expr}
                 [ASC | DESC] [,col_name ...]]
             [SEPARATOR str_val]
             [LIMIT {[offset,] row_count | row_count OFFSET offset}])
```

`DISTINCT` eliminates duplicate values from the output string.

[ORDER BY](../../sql-statements/data-manipulation/selecting-data/order-by.md) determines the order of returned values.

`SEPARATOR` specifies a separator between the values. The default separator is a comma (`,`). It is possible to avoid using a separator by specifying an empty string.

### LIMIT

The [LIMIT](../../sql-statements/data-manipulation/selecting-data/limit.md) clause can be used with `GROUP_CONCAT`.

## Examples

```sql
SELECT student_name,
       GROUP_CONCAT(test_score)
       FROM student
       GROUP BY student_name;
```

Get a readable list of MariaDB users from the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table:

```sql
SELECT GROUP_CONCAT(DISTINCT User ORDER BY User SEPARATOR '\n')
   FROM mysql.user;
```

In the former example, `DISTINCT` is used because the same user may occur more than once. The new line () used as a `SEPARATOR` makes the results easier to read.

Get a readable list of hosts from which each user can connect:

```sql
SELECT User, GROUP_CONCAT(Host ORDER BY Host SEPARATOR ', ') 
   FROM mysql.user GROUP BY User ORDER BY User;
```

The former example shows the difference between the `GROUP_CONCAT`'s [ORDER BY](../../sql-statements/data-manipulation/selecting-data/order-by.md) (which sorts the concatenated hosts), and the `SELECT`'s [ORDER BY](../../sql-statements/data-manipulation/selecting-data/order-by.md) (which sorts the rows).

[LIMIT](../../sql-statements/data-manipulation/selecting-data/limit.md) can be used with `GROUP_CONCAT`, so, for example, given the following table:

```sql
CREATE TABLE d (dd DATE, cc INT);

INSERT INTO d VALUES ('2017-01-01',1);
INSERT INTO d VALUES ('2017-01-02',2);
INSERT INTO d VALUES ('2017-01-04',3);
```

the following query:

```sql
SELECT SUBSTRING_INDEX(GROUP_CONCAT(CONCAT_WS(":",dd,cc) 
ORDER BY cc DESC),",",1) FROM d;
+----------------------------------------------------------------------------+
| SUBSTRING_INDEX(GROUP_CONCAT(CONCAT_WS(":",dd,cc) ORDER BY cc DESC),",",1) |
+----------------------------------------------------------------------------+
| 2017-01-04:3                                                               |
+----------------------------------------------------------------------------+
```

can be more simply rewritten as:

```sql
SELECT GROUP_CONCAT(CONCAT_WS(":",dd,cc) ORDER BY cc DESC LIMIT 1) FROM d;
+-------------------------------------------------------------+
| GROUP_CONCAT(CONCAT_WS(":",dd,cc) ORDER BY cc DESC LIMIT 1) |
+-------------------------------------------------------------+
| 2017-01-04:3                                                |
+-------------------------------------------------------------+
```

NULLS:

```sql
CREATE OR REPLACE TABLE t1 (a int, b char);

INSERT INTO t1 VALUES (1, 'a'), (2, NULL);

SELECT GROUP_CONCAT(a, b) FROM t1;
+--------------------+
| GROUP_CONCAT(a, b) |
+--------------------+
| 1a                 |
+--------------------+
```

## See Also

* [CONCAT()](../string-functions/concat.md)
* [CONCAT\_WS()](../string-functions/concat_ws.md)
* [SELECT](../../sql-statements/data-manipulation/selecting-data/select.md)
* [ORDER BY](../../sql-statements/data-manipulation/selecting-data/order-by.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
