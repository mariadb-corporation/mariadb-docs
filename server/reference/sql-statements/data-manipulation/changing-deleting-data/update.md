---
description: >-
  Modify existing data in a table. This statement changes the values of
  specified columns in rows that match a given condition.
---

# UPDATE

## Syntax

Single-table syntax:

```sql
UPDATE [LOW_PRIORITY] [IGNORE] table_reference 
  [PARTITION (partition_list)]
  [FOR PORTION OF period FROM expr1 TO expr2]
  SET col1={expr1|DEFAULT} [,col2={expr2|DEFAULT}] ...
  [WHERE where_condition]
  [ORDER BY ...]
  [LIMIT row_count]
```

Multiple-table syntax:

```sql
UPDATE [LOW_PRIORITY] [IGNORE] table_references
    SET col1={expr1|DEFAULT} [, col2={expr2|DEFAULT}] ...
    [WHERE where_condition]
```

## Description

For the single-table syntax, the `UPDATE` statement updates columns of existing rows in the named table with new values. The`SET` clause indicates which columns to modify and the values they should be given. Each value can be given as an expression, or the keyword`DEFAULT` to set a column explicitly to its default value. The`WHERE` clause, if given, specifies the conditions that identify which rows to update. With no `WHERE` clause, all rows are updated. If the [ORDER BY](../selecting-data/order-by.md) clause is specified, the rows are\
updated in the order that is specified. The [LIMIT](../selecting-data/limit.md) clause places a limit on the number of rows that can be updated.

{% tabs %}
{% tab title="Current" %}
Both clauses can be used with multiple-table updates.
{% endtab %}

{% tab title="< 10.3" %}
Both clauses can be used with multiple-table updates. For the multiple-table syntax, `UPDATE` updates rows in each table named in `table_references` that satisfy the conditions. In this case, [ORDER BY](../selecting-data/order-by.md) and [LIMIT](../selecting-data/limit.md) could not be used.
{% endtab %}
{% endtabs %}

An `UPDATE` can also reference tables which are located in different databases; see [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md) for the syntax.

`where_condition` is an expression that evaluates to true for each row to be updated.

`table_references` and `where_condition` are as specified as described in [SELECT](../selecting-data/select.md).

For single-table updates, assignments are evaluated in left-to-right order, while for multi-table updates, there is no guarantee of a particular order. If the `SIMULTANEOUS_ASSIGNMENT` [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md) is set, UPDATE statements evaluate all assignments simultaneously.

You need the `UPDATE` privilege only for columns referenced in an `UPDATE` that are actually updated. You need only the [SELECT](../selecting-data/select.md) privilege for any columns that are read but not modified. See [GRANT](../../account-management-sql-statements/grant.md).

The `UPDATE` statement supports the following modifiers:

* If you use the `LOW_PRIORITY` keyword, execution of the `UPDATE` is delayed until no other clients are reading from the table. This affects only storage engines that use only table-level locking (MyISAM, MEMORY, MERGE). See [HIGH\_PRIORITY and LOW\_PRIORITY clauses](high_priority-and-low_priority.md) for details.
* If you use the `IGNORE` keyword, the update statement does not abort even if errors occur during the update. Rows for which duplicate-key conflicts occur are not updated. Rows for which columns are\
  updated to values that would cause data conversion errors are updated to the closest valid values instead.

### PARTITION

See [Partition Pruning and Selection](../../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) for details.

### FOR PORTION OF

See [Application Time Periods - Updating by Portion](../../../sql-structure/temporal-tables/application-time-periods.md#updating-by-portion).

### UPDATE Statements With the Same Source and Target

`UPDATE` statements may have the same source and target. For example, given the following table:

```sql
DROP TABLE t1;
CREATE TABLE t1 (c1 INT, c2 INT);
INSERT INTO t1 VALUES (10,10), (20,20);

UPDATE t1 SET c1=c1+1 WHERE c2=(SELECT MAX(c2) FROM t1);

SELECT * FROM t1;
+------+------+
| c1   | c2   |
+------+------+
|   10 |   10 |
|   21 |   20 |
+------+------+
```

## Example

Single-table syntax:

```sql
UPDATE table_name SET column1 = value1, column2 = value2 WHERE id=100;
```

Multiple-table syntax:

```sql
UPDATE tab1, tab2 SET tab1.column1 = value1, tab1.column2 = value2 WHERE tab1.id = tab2.id;
```

## See Also

* [How IGNORE works](../inserting-loading-data/ignore.md)
* [SELECT](../selecting-data/select.md)
* [ORDER BY](../selecting-data/order-by.md)
* [LIMIT](../selecting-data/limit.md)
* [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
