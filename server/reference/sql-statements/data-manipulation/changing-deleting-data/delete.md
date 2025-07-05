# DELETE

## Syntax

Single-table syntax:

```sql
DELETE [LOW_PRIORITY] [QUICK] [IGNORE] 
  FROM tbl_name [PARTITION (partition_list)]
  [FOR PORTION OF PERIOD FROM expr1 TO expr2]
  [AS alias]                    -- from MariaDB 11.6
  [WHERE where_condition]
  [ORDER BY ...]
  [LIMIT row_count]
  [RETURNING select_expr 
    [, select_expr ...]]
```

Multiple-table syntax:

```sql
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    tbl_name[.*] [, tbl_name[.*]] ...
    FROM table_references
    [WHERE where_condition]
```

Or:

```sql
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    FROM tbl_name[.*] [, tbl_name[.*]] ...
    USING table_references
    [WHERE where_condition]
```

Trimming history:

```sql
DELETE HISTORY
  FROM tbl_name [PARTITION (partition_list)]
  [BEFORE SYSTEM_TIME [TIMESTAMP|TRANSACTION] expression]
```

## Description

| Option        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Option        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| LOW\_PRIORITY | Wait until all SELECT's are done before starting the statement. Used with storage engines that uses table locking (MyISAM, Aria etc). See [HIGH\_PRIORITY and LOW\_PRIORITY clauses](high_priority-and-low_priority.md) for details.                                                                                                                                                                                                                                                                         |
| QUICK         | Signal the storage engine that it should expect that a lot of rows are deleted. The storage engine can do things to speed up the DELETE like ignoring merging of data blocks until all rows are deleted from the block (instead of when a block is half full). This speeds up things at the expanse of lost space in data blocks. At least [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) and [Aria](../../../../server-usage/storage-engines/aria/) support this feature. |
| IGNORE        | Don't stop the query even if a not-critical error occurs (like data overflow). See [How IGNORE works](../inserting-loading-data/ignore.md) for a full description.                                                                                                                                                                                                                                                                                                                                           |

For the single-table syntax, the `DELETE` statement deletes rows from tbl\_name and returns a count of the number of deleted rows. This count can be obtained by calling the [ROW\_COUNT()](../../../sql-functions/secondary-functions/information-functions/row_count.md) function. The`WHERE` clause, if given, specifies the conditions that identify which rows to delete. With no `WHERE` clause, all rows are deleted. If the [ORDER BY](../selecting-data/order-by.md) clause is specified, the rows are deleted in the order that is specified. The [LIMIT](../selecting-data/limit.md) clause places a limit on the number of rows that can be deleted.

For the multiple-table syntax, `DELETE` deletes from each`tbl_name` the rows that satisfy the conditions. In this case,[ORDER BY](../selecting-data/order-by.md) and [LIMIT](../selecting-data/limit.md)> cannot be used. A `DELETE` can also reference tables which are located in different databases; see [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md) for the syntax.

`where_condition` is an expression that evaluates to true for each row to be deleted. It is specified as described in [SELECT](../selecting-data/select.md).

Currently, you cannot delete from a table and select from the same table in a subquery.

You need the `DELETE` privilege on a table to delete rows from it. You need only the `SELECT` privilege for any columns that are only read, such as those named in the `WHERE` clause. See[GRANT](../../account-management-sql-statements/grant.md).

As stated, a `DELETE` statement with no `WHERE` clause deletes all rows. A faster way to do this, when you do not need to know the number of deleted rows, is to use `TRUNCATE TABLE`. However,\
within a transaction or if you have a lock on the table,`TRUNCATE TABLE` cannot be used whereas `DELETE` can. See [TRUNCATE TABLE](../../table-statements/truncate-table.md), and[LOCK](../../transactions/lock-tables.md).

### AS

{% tabs %}
{% tab title="Current" %}
Single-table `DELETE` statements support aliases. For example:

```sql
CREATE TABLE t1 (c1 INT);
INSERT INTO t1 VALUES (1), (2);

DELETE FROM t1 AS a1 WHERE a1.c1 = 2;
```
{% endtab %}

{% tab title="< 11.6" %}
Single-table `DELETE` statements do **not** support aliases.
{% endtab %}
{% endtabs %}

### PARTITION

See [Partition Pruning and Selection](../../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) for details.

### FOR PORTION OF

See [Application Time Periods - Deletion by Portion](../../../sql-structure/temporal-tables/application-time-periods.md#deletion-by-portion).

### RETURNING

It is possible to return a resultset of the deleted rows for a single table to the client by using the syntax `DELETE ... RETURNING select_expr [, select_expr2 ...]]`

Any of SQL expression that can be calculated from a single row fields is allowed. Subqueries are allowed. The AS keyword is allowed, so it is possible to use aliases.

The use of aggregate functions is not allowed. RETURNING cannot be used in multi-table DELETEs.

### Same Source and Target Table

It is possible to delete from a table with the same source and target. For example:

```sql
DELETE FROM t1 WHERE c1 IN (SELECT b.c1 FROM t1 b WHERE b.c2=0);
```

### DELETE HISTORY

You can use `DELETE HISTORY` to delete historical information from [System-versioned tables](../../../sql-structure/temporal-tables/system-versioned-tables.md).

## Examples

How to use the [ORDER BY](../selecting-data/order-by.md) and [LIMIT](../selecting-data/limit.md) clauses:

```sql
DELETE FROM page_hit ORDER BY TIMESTAMP LIMIT 1000000;
```

How to use the RETURNING clause:

```sql
DELETE FROM t RETURNING f1;
+------+
| f1   |
+------+
|    5 |
|   50 |
|  500 |
+------+
```

The following statement joins two tables: one is only used to satisfy a WHERE condition, but no row is deleted from it; rows from the other table are deleted, instead.

```sql
DELETE post FROM blog INNER JOIN post WHERE blog.id = post.blog_id;
```

### Deleting from the Same Source and Target

```sql
CREATE TABLE t1 (c1 INT, c2 INT);
DELETE FROM t1 WHERE c1 IN (SELECT b.c1 FROM t1 b WHERE b.c2=0);
```

{% tabs %}
{% tab title="Current" %}
The statement returns:

```
Query OK, 0 rows affected (0.00 sec)
```
{% endtab %}

{% tab title="< 10.3.1" %}
The statement returns:

```sql
ERROR 1093 (HY000): Table 't1' is specified twice, both as a target for 'DELETE' 
  AND AS a separate source FOR
```
{% endtab %}
{% endtabs %}

## See Also

* [How IGNORE works](../inserting-loading-data/ignore.md)
* [SELECT](../selecting-data/select.md)
* [ORDER BY](../selecting-data/order-by.md)
* [LIMIT](../selecting-data/limit.md)
* [REPLACE ... RETURNING](replacereturning.md)
* [INSERT ... RETURNING](../inserting-loading-data/insertreturning.md)
* [Returning clause](https://www.youtube.com/watch?v=n-LTdEBeAT4) (video)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
