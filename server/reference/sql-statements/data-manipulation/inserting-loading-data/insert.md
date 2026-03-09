---
description: >-
  Complete guide to inserting data in MariaDB. Complete INSERT syntax for single
  rows, bulk operations, and ON DUPLICATE KEY handling for production use.
---

# INSERT

## Syntax

```sql
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
 [INTO] tbl_name [PARTITION (partition_list)] [(col,...)]
 {VALUES | VALUE} ({expr | DEFAULT},...),(...),...
 [ ON DUPLICATE KEY UPDATE
   col=expr
     [, col=expr] ... ] [RETURNING select_expr 
      [, select_expr ...]]
```

Or:

```sql
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name [PARTITION (partition_list)]
    SET col={expr | DEFAULT}, ...
    [ ON DUPLICATE KEY UPDATE
      col=expr
        [, col=expr] ... ] [RETURNING select_expr 
      [, select_expr ...]]
```

Or:

```sql
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name [PARTITION (partition_list)] [(col,...)]
    SELECT ...
    [ ON DUPLICATE KEY UPDATE
      col=expr
        [, col=expr] ... ] [RETURNING select_expr 
      [, select_expr ...]]
```

The `INSERT` statement is used to insert new rows into an existing table. The `INSERT ... VALUES`\
and `INSERT ... SET` forms of the statement insert rows based on explicitly specified values. The `INSERT ... SELECT` form inserts rows selected from another table or tables. `INSERT ... SELECT` is discussed further in the [INSERT ... SELECT](insert-select.md) article.

The table name can be specified in the form `db_name`.`tbl_name` or, if a default database is selected, in the form `tbl_name` (see [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md)). This allows to use [INSERT ... SELECT](insert-select.md) to copy rows between different databases.

The PARTITION clause can be used in both the INSERT and the SELECT part. See [Partition Pruning and Selection](../../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) for details.

{% tabs %}
{% tab title="Current" %}
The `RETURNING` clause can be used.
{% endtab %}

{% tab title="< 10.5" %}
The `RETURNING` clause is not available.
{% endtab %}
{% endtabs %}

The columns list is optional. It specifies which values are explicitly inserted, and in which order. If this clause is not specified, all values must be explicitly specified, in the same order they are listed in the table definition.

The list of value follow the `VALUES` or `VALUE` keyword (which are interchangeable, regardless how much values you want to insert), and is wrapped by parenthesis. The values must be listed in the same order as the columns list. It is possible to specify more than one list to insert more than one rows with a single statement. If many rows are inserted, this is a speed optimization.

For one-row statements, the `SET` clause may be more simple, because you don't need to remember the columns order. All values are specified in the form `col` = `expr`.

Values can also be specified in the form of a SQL expression or subquery. However, the subquery cannot access the same table that is named in the `INTO` clause.

If you use the `LOW_PRIORITY` keyword, execution of the `INSERT` is delayed until no other clients are reading from the table. If you use the `HIGH_PRIORITY` keyword, the statement has the same priority as `SELECT`s. This affects only storage engines that use only table-level locking (MyISAM, MEMORY, MERGE). However, if one of these keywords is specified, [concurrent inserts](concurrent-inserts.md) cannot be used. See [HIGH\_PRIORITY and LOW\_PRIORITY clauses](../changing-deleting-data/high_priority-and-low_priority.md) for details.

## INSERT DELAYED

For more details on the `DELAYED` option, see [INSERT DELAYED](insert-delayed.md).

## HIGH PRIORITY and LOW PRIORITY

See [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md).

## Defaults and Duplicate Values

See [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md) for details..

## INSERT IGNORE

See [INSERT IGNORE](insert-ignore.md).

## INSERT ON DUPLICATE KEY UPDATE

See [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md).

## Examples

Specifying the column names:

```sql
INSERT INTO person (first_name, last_name) VALUES ('John', 'Doe');
```

Inserting more than 1 row at a time:

```sql
INSERT INTO tbl_name VALUES (1, "row 1"), (2, "row 2");
```

Using the `SET` clause:

```sql
INSERT INTO person SET first_name = 'John', last_name = 'Doe';
```

SELECTing from another table:

```sql
INSERT INTO contractor SELECT * FROM person WHERE status = 'c';
```

See [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md) and [INSERT IGNORE](insert-ignore.md) for further examples.

## INSERT ... RETURNING

`INSERT ... RETURNING` returns a result set of the inserted rows.

It returns the listed columns for all the rows that are inserted, or alternatively, the specified `SELECT` expression. Any SQL expressions which can be calculated can be used in the select expression for the `RETURNING` clause, including virtual columns and aliases, expressions which use various operators such as bitwise, logical and arithmetic operators, string functions, date-time functions, numeric functions, control flow functions, secondary functions and stored functions. Along with this, statements which have subqueries and prepared statements can also be used.

### Examples

Simple INSERT statement:

```sql
INSERT INTO t2 VALUES (1,'Dog'),(2,'Lion'),(3,'Tiger'),(4,'Leopard') 
RETURNING id2,id2+id2,id2&id2,id2||id2;
+-----+---------+---------+----------+
| id2 | id2+id2 | id2&id2 | id2||id2 |
+-----+---------+---------+----------+
|   1 |       2 |       1 |        1 |
|   2 |       4 |       2 |        1 |
|   3 |       6 |       3 |        1 |
|   4 |       8 |       4 |        1 |
+-----+---------+---------+----------+
```

Using stored functions in RETURNING

```sql
DELIMITER |
CREATE FUNCTION f(arg INT) RETURNS INT
    BEGIN
       RETURN (SELECT arg+arg);
    END|

DELIMITER ;

PREPARE stmt FROM "INSERT INTO t1 SET id1=1, animal1='Bear' RETURNING f(id1), UPPER(animal1)";

EXECUTE stmt;
+---------+----------------+
| f(id1)  | UPPER(animal1) |
+---------+----------------+
|       2 | BEAR           |
+---------+----------------+
```

Subqueries in the `RETURNING` clause that return more than one row or column cannot be used.

Aggregate functions cannot be used in the `RETURNING` clause. Since aggregate functions work on a set of values, and if the purpose is to get the row count, `ROW_COUNT()` with `SELECT` can be used or it can be used in `INSERT...SELECT...RETURNING` if the table in the RETURNING clause is not the same as the `INSERT` table.

## See Also

* [INSERT DELAYED](insert-delayed.md)
* [INSERT SELECT](insert-select.md)
* [REPLACE](../changing-deleting-data/replace.md) Equivalent to `DELETE` + `INSERT` of conflicting row.
* [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)
* [How to quickly insert data into MariaDB](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/how-to-quickly-insert-data-into-mariadb.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
