# Inserting and Updating with Views

A [view](./) can be used for inserting or updating. However, there are certain limitations.

## Updating with views

A view cannot be used for updating if it uses any of the following:

* ALGORITHM=TEMPTABLE (see [View Algorithms](view-algorithms.md))
* [HAVING](../../reference/sql-statements/data-manipulation/selecting-data/select.md)
* [GROUP BY](../../reference/sql-statements/data-manipulation/selecting-data/select.md#group-by)
* [DISTINCT](../../reference/sql-statements/data-manipulation/selecting-data/select.md#distinct)
* [UNION](../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md)
* [UNION ALL](../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/union.md)
* An aggregate function, such as [MAX()](../../reference/sql-functions/aggregate-functions/max.md), [MIN()](../../reference/sql-functions/aggregate-functions/min.md), [SUM()](../../reference/sql-functions/aggregate-functions/sum.md) or [COUNT()](../../reference/sql-functions/aggregate-functions/count.md)
* subquery in the SELECT list
* subquery in the WHERE clause referring to a table in the FROM clause
* if it has no underlying table because it refers only to literal values
* the FROM clause contains a non-updatdable view.
* multiple references to any base table column
* an outer join
* an inner join where more than one table in the view definition is being updated
* if there's a LIMIT clause, the view does not contain all primary or not null unique key columns from the underlying table and the [updatable\_views\_with\_limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#updatable_views_with_limit) system variable is set to `0`.

## Inserting with views

A view cannot be used for inserting if it fails any of the criteria for [updating](inserting-and-updating-with-views.md#updating-with-views), and must also meet the following conditions:

* the view contains all base table columns that don't have default values
* no base table columns are present in view select list more than once
* the view columns are all simple columns, and not derived in any way. The following are examples of derived columns
  * column\_name + 25
  * LOWER(column\_name)
  * (subquery)
  * 9.5
  * column1 / column2

## Checking whether a view is updatable

MariaDB stores an IS\_UPDATABLE flag with each view, so it is always possible to see if MariaDB considers a view updatable (although not necessarily insertable) by querying the IS\_UPDATABLE column in the INFORMATION\_SCHEMA.VIEWS table.

## WITH CHECK OPTION

The WITH CHECK OPTION clause is used to prevent updates or inserts to views unless the WHERE clause in the SELECT statement is true.

There are two keywords that can be applied. WITH LOCAL CHECK OPTION restricts the CHECK OPTION to only the view being defined, while WITH CASCADED CHECK OPTION checks all underlying views as well. CASCADED is treated as default if neither keyword is given.

If a row is rejected because of the CHECK OPTION, an error similar to the following is produced:

```sql
ERROR 1369 (HY000): CHECK OPTION failed 'db_name.view_name'
```

A view with a WHERE which is always false (like `WHERE 0`) and WITH CHECK OPTION is similar to a [BLACKHOLE](../storage-engines/blackhole.md) table: no row is ever inserted and no row is ever returned. An insertable view with a WHERE which is always false but no CHECK OPTION is a view that accepts data but does not show them.

## Examples

```sql
CREATE TABLE table1 (x INT);

CREATE VIEW view1 AS SELECT x, 99 AS y FROM table1;
```

Checking whether the view is updateable:

```sql
SELECT TABLE_NAME,IS_UPDATABLE FROM INFORMATION_SCHEMA.VIEWS;
+------------+--------------+
| TABLE_NAME | IS_UPDATABLE |
+------------+--------------+
| view1      | YES          |
+------------+--------------+
```

This query works, as the view is updateable:

```sql
UPDATE view1 SET x = 5;
```

This query fails, since column `y` is a literal.

```sql
UPDATE view1 SET y = 5;
ERROR 1348 (HY000): Column 'y' is not updatable
```

Here are three views to demonstrate the WITH CHECK OPTION clause.

```sql
CREATE VIEW view_check1 AS SELECT * FROM table1 WHERE x < 100 WITH CHECK OPTION;

CREATE VIEW view_check2 AS SELECT * FROM view_check1 WHERE x > 10 WITH LOCAL CHECK OPTION;

CREATE VIEW view_check3 AS SELECT * FROM view_check1 WHERE x > 10 WITH CASCADED CHECK OPTION;
```

This insert succeeds, as `view_check2` only checks the insert against `view_check2`, and the WHERE clause evaluates to true (`150` is `>10`).

```sql
INSERT INTO view_check2 VALUES (150);
```

This insert fails, as `view_check3` checks the insert against both `view_check3` and the underlying views. The WHERE clause for `view_check1` evaluates as false (`150` is `>10`, but `150` is not `<100`), so the insert fails.

```sql
INSERT INTO view_check3 VALUES (150);
ERROR 1369 (HY000): CHECK OPTION failed 'test.view_check3'
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
