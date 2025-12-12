---
description: >-
  Group result sets by one or more columns. Learn to aggregate data using
  functions like SUM, COUNT, and AVG in conjunction with grouping.
---

# GROUP BY

Use the `GROUP BY` clause in a [SELECT](select.md) statement to group rows together that have the same value in one or more column, or the same computed value using expressions with any [functions and operators](../../../sql-functions/) except [grouping functions](../../../sql-functions/aggregate-functions/). When you use a `GROUP BY` clause, you will get a single result row for each group of rows that have the same value for the expression given in `GROUP BY`.

When grouping rows, grouping values are compared as if by the [=](../../../sql-structure/operators/comparison-operators/) operator. For string values, the `=` operator ignores trailing whitespace and may normalize characters and ignore case, depending on the [collation](../../../data-types/string-data-types/character-sets/) in use.

You can use any of the grouping functions in your select expression. Their values will be calculated based on all the rows that have been grouped together for each result row. If you select a non-grouped column or a value computed from a non-grouped column, it is undefined which row the returned value is taken from. This is not permitted if the `ONLY_FULL_GROUP_BY` [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) is used.

You can use multiple expressions in the `GROUP BY` clause, separated by commas.\
Rows are grouped together if they match on each of the expressions.

You can also use a single integer as the grouping expression. If you use an integer _n_,\
the results will be grouped by the \_n\_th column in the select expression.

The `WHERE` clause is applied before the `GROUP BY` clause. It filters non-aggregated\
rows before the rows are grouped together. To filter grouped rows based on aggregate values,\
use the `HAVING` clause. The `HAVING` clause takes any expression and evaluates it as\
a boolean, just like the `WHERE` clause. You can use grouping functions in the `HAVING`\
clause. As with the select expression, if you reference non-grouped columns in the `HAVING`\
clause, the behavior is undefined.

By default, if a `GROUP BY` clause is present, the rows in the output will be sorted by the expressions used in the `GROUP BY`. You can also specify `ASC` or `DESC` (ascending, descending) after those expressions, like in [ORDER BY](order-by.md). The default is `ASC`.

If you want the rows to be sorted by another field, you can add an explicit [ORDER BY](order-by.md). If you don't want the result to be ordered, you can add [ORDER BY NULL](order-by.md).

### WITH ROLLUP

The `WITH ROLLUP` modifier adds extra rows to the result set that represent super-aggregate summaries. For a full description with examples, see [SELECT WITH ROLLUP](select-with-rollup.md).

### GROUP BY Examples

Consider the following table that records how many times each user has played and won a game:

```sql
CREATE TABLE plays (name VARCHAR(16), plays INT, wins INT);
INSERT INTO plays VALUES 
  ("John", 20, 5), 
  ("Robert", 22, 8), 
  ("Wanda", 32, 8), 
  ("Susan", 17, 3);
```

Get a list of win counts along with a count:

```sql
SELECT wins, COUNT(*) FROM plays GROUP BY wins;
+------+----------+
| wins | COUNT(*) |
+------+----------+
|    3 |        1 |
|    5 |        1 |
|    8 |        2 |
+------+----------+
3 rows in set (0.00 sec)
```

The `GROUP BY` expression can be a computed value, and can refer back to an identifier\
specified with `AS`. Get a list of win averages along with a count:

```sql
SELECT (wins / plays) AS winavg, COUNT(*) FROM plays GROUP BY winavg;
+--------+----------+
| winavg | COUNT(*) |
+--------+----------+
| 0.1765 |        1 |
| 0.2500 |        2 |
| 0.3636 |        1 |
+--------+----------+
3 rows in set (0.00 sec)
```

You can use any [grouping function](../../../sql-functions/aggregate-functions/) in the select expression. For each win average as above, get a list of the average play count taken to get that average:

```sql
SELECT (wins / plays) AS winavg, AVG(plays) FROM plays 
  GROUP BY winavg;
+--------+------------+
| winavg | AVG(plays) |
+--------+------------+
| 0.1765 |    17.0000 |
| 0.2500 |    26.0000 |
| 0.3636 |    22.0000 |
+--------+------------+
3 rows in set (0.00 sec)
```

You can filter on aggregate information using the `HAVING` clause. The `HAVING` clause is applied after `GROUP BY` and allows you to filter on aggregate data that is not available to the `WHERE` clause. Restrict the above example to results that involve an average number of plays over 20:

```sql
SELECT (wins / plays) AS winavg, AVG(plays) FROM plays 
  GROUP BY winavg HAVING AVG(plays) > 20;
+--------+------------+
| winavg | AVG(plays) |
+--------+------------+
| 0.2500 |    26.0000 |
| 0.3636 |    22.0000 |
+--------+------------+
2 rows in set (0.00 sec)
```

### See Also

* [SELECT](select.md)
* [Joins and Subqueries](set-operations/)
* [LIMIT](limit.md)
* [ORDER BY](order-by.md)
* [Common Table Expressions](common-table-expressions/)
* [SELECT WITH ROLLUP](select-with-rollup.md)
* [SELECT INTO OUTFILE](select-into-outfile.md)
* [SELECT INTO DUMPFILE](select-into-dumpfile.md)
* [FOR UPDATE](for-update.md)
* [LOCK IN SHARE MODE](lock-in-share-mode.md)
* [Optimizer Hints](../../../../ha-and-performance/optimization-and-tuning/optimizer-hints/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
