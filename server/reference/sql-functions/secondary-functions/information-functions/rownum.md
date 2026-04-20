# ROWNUM

{% hint style="info" %}
`ROWNUM()` is available from [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.1).
{% endhint %}

## Syntax

```sql
ROWNUM()
```

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) one can just use `ROWNUM`, without the parentheses.

## Description

`ROWNUM()` returns the current number of accepted rows in the current context. It main purpose is to emulate the [ROWNUM pseudo column in Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ROWNUM-Pseudocolumn.html#GUID-2E40EC12-3FCF-4A4F-B5F2-6BC669021726). For MariaDB native applications, we recommend the usage of [LIMIT](../../../sql-statements/data-manipulation/selecting-data/limit.md), as it is easier to use and gives more predictable results than the usage of `ROWNUM()`.

The main difference between using `LIMIT` and`ROWNUM()` to limit the rows in the result is that`LIMIT` works on the result set while `ROWNUM` works on the number of accepted rows (before any `ORDER` or`GROUP BY` clauses).

The following queries will return the same results:

```sql
SELECT * FROM t1 LIMIT 10;
SELECT * FROM t1 WHERE ROWNUM() <= 10;
```

While the following may return different results based on in which orders the rows are found:

```sql
SELECT * FROM t1 ORDER BY a LIMIT 10;
SELECT * FROM t1 ORDER BY a WHERE ROWNUM() <= 10;
```

The recommended way to use `ROWNUM` to limit the number of returned rows and get predictable results is to have the query in a subquery and test for `ROWNUM()` in the outer query:

```sql
SELECT * FROM (SELECT * FROM t1 ORDER BY a) WHERE ROWNUM() <= 10;
```

`ROWNUM()` can be used in the following contexts:

* [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md)
* [INSERT](../../../sql-statements/data-manipulation/inserting-loading-data/insert.md)
* [UPDATE](../../../sql-statements/data-manipulation/changing-deleting-data/update.md)
* [DELETE](../../../sql-statements/data-manipulation/changing-deleting-data/delete.md)
* [LOAD DATA INFILE](../../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)

Used in other contexts, `ROWNUM()` will return 0.

## Examples

```sql
INSERT INTO t1 VALUES (1,ROWNUM()),(2,ROWNUM()),(3,ROWNUM());

INSERT INTO t1 VALUES (1),(2) RETURNING a, ROWNUM();

UPDATE t1 SET row_num_column=ROWNUM();

DELETE FROM t1 WHERE a < 10 AND ROWNUM() < 2;

LOAD DATA INFILE 'filename' INTO TABLE t1 fields terminated BY ',' 
  lines terminated BY "\r\n" (a,b) SET c=ROWNUM();
```

## Optimizations

In many cases where `ROWNUM()` is used, MariaDB will use the same optimizations it uses with [LIMIT](../../../sql-statements/data-manipulation/selecting-data/limit.md).

`LIMIT` optimization is possible when using `ROWNUM` in the following manner:

* When one is in a top level `WHERE` clause comparing `ROWNUM()` with a numerical constant using any of the following expressions:
  * `ROWNUM()` < number.
  * `ROWNUM()` <= number.
  * `ROWNUM()` = 1`ROWNUM()` can be also be the right argument to the comparison function.

In the above cases, `LIMIT` optimization can be done in the\
following cases:

* For the current subquery when the `ROWNUM` comparison is done on the top level:

```sql
SELECT * FROM t1 WHERE ROWNUM() <= 2 AND t1.a > 0
```

* For an inner subquery, when the upper level has only a `ROWNUM()` comparison in the `WHERE` clause:

```sql
SELECT * FROM (SELECT * FROM t1) AS t WHERE ROWNUM() <= 2
```

## Other Changes Related to ROWNUM

When `ROWNUM()` is used anywhere in a query, the optimization to ignore `ORDER BY` in subqueries are disabled.

This was done to get the following common Oracle query to work as expected:

```sql
SELECT * FROM (SELECT * FROM t1 ORDER BY a DESC) AS t WHERE rownum() <= 2;
```

By default, MariaDB ignores any `ORDER BY` in subqueries both because the SQL standard defines results sets in subqueries to be un-ordered and because of performance reasons (especially when using views in subqueries). See [MDEV-3926](https://jira.mariadb.org/browse/MDEV-3926) "Wrong result with `GROUP BY ... WITH ROLLUP`" for a discussion of this topic.

## Other Considerations

While MariaDB tries to emulate Oracle's usage of `ROWNUM()` as closely as possible, there are cases where the result is different:

* When the optimizer finds rows in a different order (because of different storage methods or optimization). This may also happen in Oracle if one adds or deletes an index, in which case the rows may be found in a different order.

Note that usage of `ROWNUM()` in functions or [stored procedures](../../../../server-usage/stored-routines/stored-procedures/) will use their own context, not the caller's context.

## See Also

* [MDEV-24089](https://jira.mariadb.org/browse/MDEV-24089) support Oracle syntax: rownum
* [LIMIT clause](../../../sql-statements/data-manipulation/selecting-data/limit.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
