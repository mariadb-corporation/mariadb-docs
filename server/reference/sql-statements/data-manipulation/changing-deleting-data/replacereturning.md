---
description: >-
  Replace rows and retrieve the results immediately. This extension returns the
  values of the replaced or inserted rows in the same operation.
---

# REPLACE...RETURNING

{% hint style="info" %}
`REPLACE ... RETURNING` was added in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes), and returns a result set of the replaced rows.
{% endhint %}

## Syntax

```sql
REPLACE [LOW_PRIORITY | DELAYED]
 [INTO] tbl_name [PARTITION (partition_list)] [(col,...)]
 {VALUES | VALUE} ({expr | DEFAULT},...),(...),...
[RETURNING select_expr 
      [, select_expr ...]]
```

Or:

```sql
REPLACE [LOW_PRIORITY | DELAYED]
    [INTO] tbl_name [PARTITION (partition_list)]
    SET col={expr | DEFAULT}, ...
[RETURNING select_expr 
      [, select_expr ...]]
```

Or:

```sql
REPLACE [LOW_PRIORITY | DELAYED]
    [INTO] tbl_name [PARTITION (partition_list)] [(col,...)]
    SELECT ...
[RETURNING select_expr 
      [, select_expr ...]]
```

## Description

`REPLACE ... RETURNING` returns a result set of the replaced rows. The statement returns the listed columns for all the rows that are replaced, or alternatively, the specified `SELECT` expression. Any SQL expressions which can be calculated can be used in the select expression for the RETURNING clause, including virtual columns and aliases, expressions which use various operators such as bitwise, logical and arithmetic operators, string functions, date-time functions, numeric functions, control flow functions, secondary functions and stored functions. Along with this, statements which have subqueries and prepared statements can also be used.

## Examples

Simple `REPLACE` statement:

```sql
REPLACE INTO t2 VALUES (1,'Leopard'),(2,'Dog') RETURNING id2, id2+id2 
AS Total ,id2|id2, id2&&id2;
+-----+-------+---------+----------+
| id2 | Total | id2|id2 | id2&&id2 |
+-----+-------+---------+----------+
|   1 |     2 |       1 |        1 |
|   2 |     4 |       2 |        1 |
+-----+-------+---------+----------+
```

Using stored functions in `RETURNING`:

```sql
DELIMITER |
CREATE FUNCTION f(arg INT) RETURNS INT
    BEGIN
      RETURN (SELECT arg+arg);
    END|

DELIMITER ;
PREPARE stmt FROM "REPLACE INTO t2 SET id2=3, animal2='Fox' RETURNING f2(id2),
UPPER(animal2)";

EXECUTE stmt;
+---------+----------------+
| f2(id2) | UPPER(animal2) |
+---------+----------------+
|       6 | FOX            |
+---------+----------------+
```

Subqueries in the statement:

```sql
REPLACE INTO t1 SELECT * FROM t2 RETURNING (SELECT id2 FROM t2 WHERE 
id2 IN (SELECT id2 FROM t2 WHERE id2=1)) AS new_id;
+--------+
| new_id |
+--------+
|      1 |
|      1 |
|      1 |
|      1 |
+--------+
```

Subqueries in the `RETURNING` clause that return more than one row or column cannot be used..

Aggregate functions cannot be used in the `RETURNING` clause. Since aggregate functions work on a set of values and if the purpose is to get the row count, `ROW_COUNT()` with `SELECT` can be used, or it can be used in `REPLACE...SELECT...RETURNING` if the table in the `RETURNING` clause is not the same as the `REPLACE` table.

## See Also

* [INSERT ... RETURNING](../inserting-loading-data/insertreturning.md)
* [DELETE ... RETURNING](delete.md#returning)
* [Returning clause](https://www.youtube.com/watch?v=n-LTdEBeAT4) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
