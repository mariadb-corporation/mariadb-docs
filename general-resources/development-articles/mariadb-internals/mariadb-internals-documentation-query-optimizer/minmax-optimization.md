# MIN/MAX optimization

## Min/Max optimization without GROUP BY

MariaDB and MySQL can optimize the [MIN()](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-functions/aggregate-functions/min.md) and [MAX()](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-functions/aggregate-functions/max.md) functions to be a single row lookup in the following cases:

* There is only one table used in the `SELECT`.
* You only have constants, `MIN()` and `MAX()` in the `SELECT` part.
* The argument to `MIN()` and `MAX()` is a simple column reference that is part of a key.
* There is no `WHERE` clause or the `WHERE` is used with a constant for all prefix parts of the key before the argument to `MIN()`/`MAX()`.
* If the argument is used in the `WHERE` clause, it can be compared to a constant with `<` or `<=` in case of `MAX()` and with `>` or `>=` in case of `MIN()`.

Here are some examples to clarify this.\
In this case we assume there is an index on columns `(a,b,c)`

```sql
SELECT MIN(a),MAX(a) FROM t1
SELECT MIN(b) FROM t1 WHERE a=const
SELECT MIN(b),MAX(b) FROM t1 WHERE a=const
SELECT MAX(c) FROM t1 WHERE a=const AND b=const
SELECT MAX(b) FROM t1 WHERE a=const AND b<const
SELECT MIN(b) FROM t1 WHERE a=const AND b>const
SELECT MIN(b) FROM t1 WHERE a=const AND b BETWEEN const AND const
SELECT MAX(b) FROM t1 WHERE a=const AND b BETWEEN const AND const
```

* Instead of `a=const` the condition `a IS NULL` can be used.

The above optimization also works for [subqueries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries):

```sql
SELECT x FROM t2 WHERE y= (SELECT MIN(b) FROM t1 WHERE a=const)
```

Cross joins, where there is no join condition for a table, can also be optimized to a few key lookups:

```sql
SELECT min(t1.key_part_1), max(t2.key_part_1) FROM t1, t2
```

## Min/Max optimization with GROUP BY

MariaDB and MySQL support loose index scan, which can speed up certain `GROUP BY` queries. The basic idea is that when scanning a `BTREE` index (the most common index type for the MariaDB storage engines) we can jump over identical values for any prefix of a key and thus speed up the scan significantly.

Loose scan is possible in the following cases:

* The query uses only one table.
* The `GROUP BY` part only uses indexed columns in the same order as in the index.
* The only aggregated functions in the `SELECT` part are `MIN()` and `MAX()` functions and all of them using the same column which is the next index part after the used `GROUP BY` columns.
* Partial indexed columns cannot be used (like only indexing 10 characters of a `VARCHAR(20)` column).

Loose scan will apply for your query if [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) shows `Using index for group-by` in the `Extra` column.\
In this case the optimizer will do only one extra row fetch to calculate the value for `MIN()` or `MAX()` for every unique key prefix.

The following examples assume that the table `t1` has an index on `(a,b,c)`.

```sql
SELECT a, b, MIN(c),MAX(c) FROM t1 GROUP BY a,b
```

## See also

* [MIN()](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-functions/aggregate-functions/min.md)
* [MAX()](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-functions/aggregate-functions/max.md)
* [MySQL manual on loose index scans](https://dev.mysql.com/doc/refman/5.7/en/group-by-optimization.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
