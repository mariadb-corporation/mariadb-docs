# ORDER BY

## Description

Use the `ORDER BY` clause to order a resultset, such as that are returned from a [SELECT](select.md)\
statement. You can specify just a column or use any expression with functions. If you are\
using the `GROUP BY` clause, you can use grouping functions in `ORDER BY`. Ordering is done after grouping.

You can use multiple ordering expressions, separated by commas. Rows will be sorted by\
the first expression, then by the second expression if they have the same value for the first, and so on.

You can use the keywords `ASC` and `DESC` after each ordering expression to force that ordering to be ascending or descending, respectively. Ordering is ascending by default.

You can also use a single integer as the ordering expression. If you use an integer _n_, the results will be ordered by the _&#x6E;_&#x74;h column in the select expression.

When string values are compared, they are compared as if by the [STRCMP](../../../sql-functions/string-functions/strcmp.md) function. `STRCMP` ignores trailing whitespace and may normalize characters and ignore case, depending on the [collation](../../../data-types/string-data-types/character-sets/) in use.

Duplicated entries in the `ORDER BY` clause are removed.

`ORDER BY` can also be used to order the activities of a [DELETE](../changing-deleting-data/delete.md) or [UPDATE](../changing-deleting-data/update.md) statement (usually with the [LIMIT](limit.md) clause).

{% tabs %}
{% tab title="Current" %}
It is possible to use `ORDER BY` (or [LIMIT](limit.md)) in a multi-table [UPDATE](../changing-deleting-data/update.md) statement.
{% endtab %}

{% tab title="< 10.3.2" %}
It is **not** possible to use `ORDER BY` (or [LIMIT](limit.md)) in a multi-table [UPDATE](../changing-deleting-data/update.md) statement.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
MariaDB allows packed sort keys and values of non-sorted fields in the sort buffer. This can make filesort temporary files much smaller when `VARCHAR`, `CHAR` or `BLOB` columns are used, notably speeding up some `ORDER BY` sorts.
{% endtab %}

{% tab title="< 10.5" %}
MariaDB does not allow packed sort keys and values of non-sorted fields in the sort buffer.
{% endtab %}
{% endtabs %}

## Examples

```sql
CREATE TABLE seq (i INT, x VARCHAR(1));
INSERT INTO seq VALUES (1,'a'), (2,'b'), (3,'b'), (4,'f'), (5,'e');

SELECT * FROM seq ORDER BY i;
+------+------+
| i    | x    |
+------+------+
|    1 | a    |
|    2 | b    |
|    3 | b    |
|    4 | f    |
|    5 | e    |
+------+------+

SELECT * FROM seq ORDER BY i DESC;
+------+------+
| i    | x    |
+------+------+
|    5 | e    |
|    4 | f    |
|    3 | b    |
|    2 | b    |
|    1 | a    |
+------+------+

SELECT * FROM seq ORDER BY x,i;
+------+------+
| i    | x    |
+------+------+
|    1 | a    |
|    2 | b    |
|    3 | b    |
|    5 | e    |
|    4 | f    |
+------+------+
```

ORDER BY in an [UPDATE](../changing-deleting-data/update.md) statement, in conjunction with [LIMIT](limit.md):

```sql
UPDATE seq SET x='z' WHERE x='b' ORDER BY i DESC LIMIT 1;

SELECT * FROM seq;
+------+------+
| i    | x    |
+------+------+
|    1 | a    |
|    2 | b    |
|    3 | z    |
|    4 | f    |
|    5 | e    |
+------+------+
```

`ORDER BY` can be used in a multi-table update:

```sql
CREATE TABLE warehouse (product_id INT, qty INT);
INSERT INTO warehouse VALUES (1,100),(2,100),(3,100),(4,100);

CREATE TABLE store (product_id INT, qty INT);
INSERT INTO store VALUES (1,5),(2,5),(3,5),(4,5);

UPDATE warehouse,store SET warehouse.qty = warehouse.qty-2, store.qty = store.qty+2 
  WHERE (warehouse.product_id = store.product_id AND store.product_id  >= 1) 
    ORDER BY store.product_id DESC LIMIT 2;

SELECT * FROM warehouse;
+------------+------+
| product_id | qty  |
+------------+------+
|          1 |  100 |
|          2 |  100 |
|          3 |   98 |
|          4 |   98 |
+------------+------+

SELECT * FROM store;
+------------+------+
| product_id | qty  |
+------------+------+
|          1 |    5 |
|          2 |    5 |
|          3 |    7 |
|          4 |    7 |
+------------+------+
```

## See Also

* [Why is ORDER BY in a FROM subquery ignored?](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/faq/developer-questions/why-is-order-by-in-a-from-subquery-ignored)
* [SELECT](select.md)
* [UPDATE](../changing-deleting-data/update.md)
* [DELETE](../changing-deleting-data/delete.md)
* [Improvements to ORDER BY Optimization](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimization-strategies/improvements-to-order-by.md)
* [Joins and Subqueries](joins-subqueries/)
* [LIMIT](limit.md)
* [GROUP BY](group-by.md)
* [Common Table Expressions](common-table-expressions/)
* [SELECT WITH ROLLUP](select-with-rollup.md)
* [SELECT INTO OUTFILE](select-into-outfile.md)
* [SELECT INTO DUMPFILE](select-into-dumpfile.md)
* [FOR UPDATE](for-update.md)
* [LOCK IN SHARE MODE](lock-in-share-mode.md)
* [Optimizer Hints](optimizer-hints.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
