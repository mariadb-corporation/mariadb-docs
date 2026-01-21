---
description: >-
  Insert or replace rows based on unique keys. This statement acts like INSERT,
  but if a duplicate key exists, it deletes the old row and inserts the new one.
---

# REPLACE

{% hint style="info" %}
The RETURNING clause was introduced in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes).
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

`REPLACE` works exactly like [INSERT](../inserting-loading-data/insert.md), except that if an old row in the table has the same value as a new row for a `PRIMARY KEY` or a`UNIQUE` index, the old row is deleted before the new row is inserted. If the table has more than one `UNIQUE` keys, it is possible that the new row conflicts with more than one row. In this case, all conflicting rows will be deleted.

The table name can be specified in the form `db_name`.`tbl_name` or, if a default database is selected, in the form `tbl_name` (see [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md)). This allows to use [REPLACE ... SELECT](../inserting-loading-data/insert-select.md) to copy rows between different databases.

Basically it works like this:

```sql
BEGIN;
SELECT 1 FROM t1 WHERE KEY=# FOR UPDATE;
IF FOUND-ROW
  DELETE FROM t1 WHERE KEY=# ;
ENDIF
INSERT INTO t1 VALUES (...);
END;
```

The above can be replaced with:

```sql
REPLACE INTO t1 VALUES (...)
```

`REPLACE` is a MariaDB/MySQL extension to the SQL standard. It either inserts, or deletes and inserts. For other MariaDB/MySQL extensions to standard SQL --- that also handle duplicate values --- see [IGNORE](../inserting-loading-data/ignore.md) and [INSERT ON DUPLICATE KEY UPDATE](../inserting-loading-data/insert-on-duplicate-key-update.md).

Note that unless the table has a `PRIMARY KEY` or`UNIQUE` index, using a `REPLACE` statement makes no sense. It becomes equivalent to `INSERT`, because there is no index to be used to determine whether a new row duplicates another.

Values for all columns are taken from the values. See [Partition Pruning and Selection](../../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) for details. Specified in the`REPLACE` statement. Any missing columns are set to their default values, just as happens for `INSERT`. You cannot refer to values from the current row and use them in the new row. If you use an assignment such as `'SET col = col + 1'`, the reference to the column name on the right hand side is treated as`DEFAULT(col)`, so the assignment is equivalent to`'SET col = DEFAULT(col) + 1'`.

To use `REPLACE`, you must have both the`INSERT` and `DELETE` [privileges](../../account-management-sql-statements/grant.md) for the table.

There are some issues you should be aware of, before using `REPLACE`:

* If there is an [AUTO\_INCREMENT](../../../../data-types/auto_increment.md) field, a new value will be generated.
* If there are foreign keys, `ON DELETE` action will be activated by `REPLACE`.
* [Triggers](../../../../server-usage/triggers-events/triggers/) on `DELETE` and `INSERT` will be activated by `REPLACE`.

To avoid some of these behaviors, you can use `INSERT ... ON DUPLICATE KEY UPDATE`.

This statement activates `INSERT` and `DELETE` triggers. See [Trigger Overview](../../../../server-usage/triggers-events/triggers/trigger-overview.md) for details.

### PARTITION

See [Partition Pruning and Selection](../../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) for details.

### REPLACE RETURNING

`REPLACE ... RETURNING` returns a resultset of the replaced rows. This returns the listed columns for all the rows that are replaced, or alternatively, the specified `SELECT` expression. Any SQL expressions which can be calculated can be used in the select expression for the `RETURNING` clause, including virtual columns and aliases, expressions which use various operators such as bitwise, logical and arithmetic operators, string functions, date-time functions, numeric functions, control flow functions, secondary functions and stored functions. Along with this, statements which have subqueries and prepared statements can also be used.

#### Examples

Simple `REPLACE` statement:

```sql
REPLACE INTO t2 VALUES (1,'Leopard'),(2,'Dog') RETURNING id2, id2+id2 
as Total ,id2|id2, id2&&id2;
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

Aggregate functions cannot be used in the RETURNING clause. Since aggregate functions work on a set of values and if the purpose is to get the row count, `ROW_COUNT()` with `SELECT` can be used, or it can be used in `REPLACE...SELECT`.

`REPLACE ... RETURNING` returns a result set of the replaced rows. This returns the listed columns for all the rows that are replaced, or alternatively, the specified `SELECT` expression. Any SQL expressions which can be calculated can be used in the select expression for the `RETURNING` clause, including virtual columns and aliases, expressions which use various operators such as bitwise, logical and arithmetic operators, string functions, date-time functions, numeric functions, control flow functions, secondary functions and stored functions. Along with this, statements which have subqueries and prepared statements can also be used.

## Examples

Simple `REPLACE` statement:

```sql
REPLACE INTO t2 VALUES (1,'Leopard'),(2,'Dog') RETURNING id2, id2+id2 
as Total ,id2|id2, id2&&id2;
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

Aggregate functions cannot be used in the `RETURNING` clause. Since aggregate functions work on a set of values and if the purpose is to get the row count, `ROW_COUNT()` with `SELECT` can be used, or it can be used in `REPLACE...SELECT...RETURNING` if the table in the `RETURNING` clause is not the same as the `REPLACE` table. `SELECT...RETURNING` if the table in the `RETURNING` clause is not the same as the `REPLACE` table.

## See Also

* [INSERT](../inserting-loading-data/insert.md)
* [HIGH\_PRIORITY and LOW\_PRIORITY clauses](high_priority-and-low_priority.md)
* [INSERT DELAYED](../inserting-loading-data/insert-delayed.md) for details on the `DELAYED` clause

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
