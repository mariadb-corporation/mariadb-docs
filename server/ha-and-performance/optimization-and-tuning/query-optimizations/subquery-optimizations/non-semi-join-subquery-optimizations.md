# Non-semi-join Subquery Optimizations

Certain kinds of IN-subqueries cannot be flattened into [semi-joins](semi-join-subquery-optimizations.md). These subqueries can be both correlated or non-correlated. In order to provide consistent performance in all cases, MariaDB provides several alternative strategies for these types of subqueries. Whenever several strategies are possible, the optimizer chooses the optimal one based on cost estimates.

The two primary non-semi-join strategies are materialization (also called outside-in materialization), and in-to-exists transformation. Materialization is applicable only for non-correlated subqueries, while in-to-exist can be used both for correlated and non-correlated subqueries.

## Applicability

An IN subquery cannot be flattened into a semi-join in the following cases. The examples below use the _World_ database from the MariaDB regression test suite.

### Subquery in a disjunction (OR)

The subquery is located directly or indirectly under an OR operation\
in the WHERE clause of the outer query.

Query pattern:

```sql
SELECT ... FROM ... WHERE (expr1, ..., exprN) [NOT] IN (SELECT ... ) OR expr;
```

Example:

```sql
SELECT Name FROM Country
WHERE (Code IN (SELECT Country FROM City WHERE City.Population > 100000) OR
       Name LIKE 'L%') AND
      surfacearea > 1000000;
```

### Negated subquery predicate (NOT IN)

The subquery predicate itself is negated.

Query pattern:

```sql
SELECT ... FROM ... WHERE ... (expr1, ..., exprN) NOT IN (SELECT ... ) ...;
```

Example:

```sql
SELECT Country.Name
FROM Country, CountryLanguage 
WHERE Code NOT IN (SELECT Country FROM CountryLanguage WHERE LANGUAGE = 'English')
  AND CountryLanguage.Language = 'French'
  AND Code = Country;
```

### Subquery in the SELECT or HAVING clause

The subquery is located in the SELECT or HAVING clauses of the outer query.

Query pattern:

```sql
SELECT field1, ..., (SELECT ...)  WHERE ...;
SELECT ...  WHERE ... HAVING (SELECT ...);
```

Example:

```sql
SELECT Name, City.id IN (SELECT capital FROM Country WHERE capital IS NOT NULL) AS is_capital
FROM City
WHERE City.population > 10000000;
```

### Subquery with a UNION

The subquery itself is a UNION, while the IN predicate may be anywhere in the query where IN is allowed.

Query pattern:

```sql
... [NOT] IN (SELECT ... UNION SELECT ...)
```

Example:

```sql
SELECT * FROM City WHERE (Name, 91) IN
(SELECT Name, round(Population/1000) FROM City WHERE Country = "IND" AND Population > 2500000
UNION
 SELECT Name, round(Population/1000) FROM City WHERE Country = "IND" AND Population < 100000);
```

## Materialization for non-correlated IN-subqueries

### Materialization basics

The basic idea of subquery materialization is to execute the subquery and store its result in an internal temporary table indexed on all its columns. Naturally, this is possible only when the subquery is non-correlated. The IN predicate tests whether its left operand is present in the subquery result. Therefore it is not necessary to store duplicate subquery result rows in the temporary table. Storing only unique subquery rows provides two benefits - the size of the temporary table is smaller, and the index on all\
its columns can be unique.

If the size of the temporary table is less than the tmp\_table\_size system variable, the table is a hash-indexed in-memory HEAP table. In the rare cases when the subquery result exceeds this limit, the temporary table is stored on disk in an ARIA or MyISAM B-tree indexed table (ARIA is the default).

Subquery materialization happens on demand during the first execution of the IN predicate. Once the subquery is materialized, the IN predicate is evaluated very efficiently by index lookups of the outer expression into the unique index of the materialized temporary table. If there is a match, IN is TRUE, otherwise IN is FALSE.

### NULL-aware efficient execution

An IN predicate may produce a NULL result if there is a NULL value in either of its arguments. Depending on its location in a query, a NULL predicate value is equivalent to FALSE. These are the cases when substituting NULL with FALSE would reject exactly the same result rows. A NULL result of IN is indistinguishable from a FALSE if the IN predicate is:

* not negated,
* not a function argument,
* inside a WHERE or ON clause.

In all these cases the evaluation of IN is performed as described in the previous paragraph via index lookups into the materialized subquery. In all remaining cases when NULL cannot be substituted with FALSE, it is not possible to use index lookups. This is not a limitation in the server, but a consequence\
of the NULL semantics in the ANSI SQL standard.

Suppose an IN predicate is evaluated as

```sql
NULL IN (SELECT
not_null_col FROM t1)
```

, that is, the left operand of IN is a NULL value, and there are no NULLs in the subquery. In this case the value of IN is neither FALSE, nor TRUE. Instead it is NULL. If we were to perform an index lookup with\
the NULL as a key, such a value would not be found in not\_null\_col, and the IN predicate would incorrectly produce a FALSE.

In general, an NULL value on either side of an IN acts as a "wildcard" that matches any value, and if a match exists, the result of IN is NULL. Consider the following example:

If the left argument of IN is the row: `(7, NULL, 9)`, and the result of the right subquery operand of IN is the table:

```sql
(7, 8, 10)
(6, NULL, NULL)
(7, 11, 9)
```

The the IN predicate matches the row `(7, 11, 9)`, and the result of IN is NULL. Matches where the differing values on either side of the IN arguments are matched by a NULL in the other IN argument, are\
called _partial matches_.

In order to efficiently compute the result of an IN predicate in the presence of NULLs, MariaDB implements two special algorithms for [partial matching, described here in detail](https://askmonty.org/worklog/Server-Sprint/?tid=68).

* Rowid-merge partial matching\
  This technique is used when the number of rows in the subquery result is above a certain limit. The technique creates special indexes on some of the columns of the temporary table, and merges them by alternative scanning of each index thus performing an operation similar to set-intersection.
* Table scan partial matching\
  This algorithm is used for very small tables when the overhead of the rowid-merge algorithm is not justifiable. Then the server simply scans the materialized subquery, and checks for partial matches. Since this strategy doesn't need any in-memory buffers, it is also used when there is not enough memory to hold the indexes of the rowid-merge strategy.

### Limitations

In principle the subquery materialization strategy is universal, however, due to some technical limitations in the MariaDB server, there are few cases when the server cannot apply this optimization.

* BLOB fields\
  Either the left operand of an IN predicate refers to a BLOB field, or the subquery selects one or more BLOBs.
* Incomparable fields\
  TODO

In the above cases, the server reverts to the [IN-TO-EXISTS](non-semi-join-subquery-optimizations.md#the-in-to-exists-transformation) transformation.

## The IN-TO-EXISTS transformation

This optimization is the only subquery execution strategy that existed in older versions of MariaDB and MySQL prior to [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3). We have made various changes and fixed a number of bugs in this code as well, but in essence it remains the same.

## Performance discussion

### Example speedup over MySQL 5.x and [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.1/changes-improvements-in-mariadb-5-1)/5.2

Depending on the query and data, either of the two strategies described here may result in orders of magnitude better/worse plan than the other strategy. Older versions of MariaDB and any current MySQL version (including MySQL 5.5, and MySQL 5.6 DMR as of July 2011) implement only the IN-TO-EXISTS transformation. As illustrated below, this strategy is inferior in many common cases to subquery materialization.

Consider the following query over the data of the DBT3 benchmark scale 10. Find customers with top balance in their nations:

```sql
SELECT * FROM part
WHERE p_partkey IN
      (SELECT l_partkey FROM lineitem
       WHERE l_shipdate BETWEEN '1997-01-01' AND '1997-02-01')
ORDER BY p_retailprice DESC LIMIT 10;
```

The times to run this query is as follows:

* Execution time in [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.2/changes-improvements-in-mariadb-5-2)/MySQL 5.x (any MySQL): > 1 h\
  The query takes more than one hour (we didn't wait longer), which makes it impractical to use subqueries in such cases. The EXPLAIN below shows that the subquery was transformed into a correlated one, which indicates an IN-TO-EXISTS transformation.

```sql
+--+------------------+--------+--------------+-------------------+----+------+---------------------------+
|id|select_type       |table   |type          |key                |ref |rows  |Extra                      |
+--+------------------+--------+--------------+-------------------+----+------+---------------------------+
| 1|PRIMARY           |part    |ALL           |NULL               |NULL|199755|Using where; Using filesort|
| 2|DEPENDENT SUBQUERY|lineitem|index_subquery|i_l_suppkey_partkey|func|    14|Using where                |
+--+------------------+--------+--------------+-------------------+----+------+---------------------------+
```

* Execution time in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3): 43 sec\
  In [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3) it takes less than a minute to run the same query. The EXPLAIN shows that the subquery remains uncorrelated, which is an indication that it is being executed via subquery materialization.

```sql
+--+------------+-----------+------+------------------+----+------+-------------------------------+
|id|select_type |table      |type  |key               |ref |rows  |Extra                          |
+--+------------+-----------+------+------------------+----+------+-------------------------------+
| 1|PRIMARY     |part       |ALL   |NULL              |NULL|199755|Using temporary; Using filesort|
| 1|PRIMARY     |<subquery2>|eq_ref|distinct_key      |func|     1|                               |
| 2|MATERIALIZED|lineitem   |range |l_shipdate_partkey|NULL|160060|Using where; Using index       |
+--+------------+-----------+------+------------------+----+------+-------------------------------+
```

The speedup here is practically infinite, because both MySQL and older MariaDB versions cannot complete the query in any reasonable time.

In order to show the benefits of partial matching we extended the _customer_ table from the DBT3 benchmark with two extra columns:

* c\_pref\_nationkey - preferred nation to buy from,
* c\_pref\_brand - preferred brand.

Both columns are prefixed with the percent NULL values in the column, that is, c\_pref\_nationkey\_05 contains 5% NULL values.

Consider the query "Find all customers that didn't buy from a preferred country, and from a preferred brand withing some date ranges":

```sql
SELECT COUNT(*)
FROM customer
WHERE (c_custkey, c_pref_nationkey_05, c_pref_brand_05) NOT IN
  (SELECT o_custkey, s_nationkey, p_brand
   FROM orders, supplier, part, lineitem
   WHERE l_orderkey = o_orderkey AND
         l_suppkey = s_suppkey AND
         l_partkey = p_partkey AND
         p_retailprice < 1200 AND
         l_shipdate >= '1996-04-01' AND l_shipdate < '1996-04-05' AND
         o_orderdate >= '1996-04-01' AND o_orderdate < '1996-04-05');
```

* Execution time in [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.2/changes-improvements-in-mariadb-5-2)/MySQL 5.x (any MySQL): 40 sec
* Execution time in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3): 2 sec

The speedup for this query is 20 times.

### Performance guidelines

TODO

## Optimizer control

In certain cases it may be necessary to override the choice of the optimizer. Typically this is needed for benchmarking or testing purposes, or to mimic the behavior of an older version of the server, or if the optimizer made a poor choice.

All the above strategies can be controlled via the following switches in [optimizer\_switch](../../system-variables/server-system-variables.md#optimizer_switch) system variable.

* materialization=on/off\
  In some very special cases, even if materialization was forced, the optimizer may still revert to the IN-TO-EXISTS strategy if materialization is not applicable. In the cases when materialization requres partial matching (because of the presense of NULL values), there are two subordinate switches that\
  control the two partial matching strategies:
  * partial\_match\_rowid\_merge=on/off\
    This switch controls the Rowid-merge strategy. In addition to this switch, the system variable [rowid\_merge\_buff\_size](../../system-variables/server-system-variables.md#rowid_merge_buff_size) controls the maximum memory available to the Rowid-merge strategy.
  * partial\_match\_table\_scan=on/off\
    Controls the alternative partial match strategy that performs matching via a table scan.
* in\_to\_exists=on/off\
  This switch controls the IN-TO-EXISTS transformation.
* tmp\_table\_size and max\_heap\_table\_size system variables\
  The tmp\_table\_size system variable sets the upper limit for internal MEMORY temporary tables. If an internal temporary table exceeds this size, it is converted automatically into a Aria or MyISAM table on disk with a B-tree index. Notice however, that a MEMORY table cannot be larger than\
  max\_heap\_table\_size.

The two main optimizer switches - _materialization_ and _in\_to\_exists_ cannot be simultaneously off. If both are set to off, the server will issue an error.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
