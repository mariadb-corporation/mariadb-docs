## Table-level hints

Supported variants of syntax:
```sql
hint_name([@query_block_name])
hint_name([@query_block_name] [tbl_name [, tbl_name] ...])
hint_name([tbl_name@query_block_name [, tbl_name@query_block_name] ...])
```
See [Syntax of query-block](expanded-optimizer-hints.md#syntax-of-query-block-level-hints) and [table level hints](expanded-optimizer-hints.md#syntax-of-table-level-hints) for more information.

### * **`BKA()`, `NO_BKA()`**
{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}

Enable or disable [batched key access join](../query-optimizer/block-based-join-algorithms.md#batch-key-access-join) algorithm.

### * **`BNL()`, `NO_BNL()`**
{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}
Enable or disable [block nested-loop join](../query-optimizer/block-based-join-algorithms.md#block-nested-loop-join) algorithm.

These hints override the settings of system variables used [to manage usage of block-based join algorithms](../query-optimizer/block-based-join-algorithms.md#managing-usage-of-block-based-join-algorithms).

#### Examples
```sql
SET join_cache_level = 2;
SELECT /*+ BKA(t13) */ * FROM t12, t13
  WHERE t12.a=t13.a AND (t13.b+1 <= t13.b+1);
```
`join_cache_level = 2` limits the use of block-based join algorithms to flat or incremental BNL (BKA joins are not allowed). However, with the `BKA(t13)` hint tables `t12` and `t13` will be joined using the BKA hashed algorithm.

The same works in the opposite direction too. Say we have a very permissive setting `join_cache_level = 8` that allows all block-based join algorithms. However, with the `NO_BKA(t13)` hint tables `t12` and `t13` will be joined using the BNL hashed algorithm.
```sql
SET join_cache_level = 8;
SET optimizer_switch='join_cache_bka=on';
SELECT /*+ NO_BKA(t13) */ * FROM t12, t13
  WHERE t12.a=t13.a AND (t13.b+1 <= t13.b+1);
```

These hints can be applied either to particular tables or to the whole query-block. When applied to particular tables, the hint body should mention tables that _receive_ data from previous tables, i.e. which appear later in the join order. That means the hints in examples above will work if the optimizer joins tables `t12` and `t13` in that order. If the optimizer joins tables in the reverse order, the hints should mention `t12` in their body instead.

### * **`DERIVED_CONDITION_PUSHDOWN()`, `NO_DERIVED_CONDITION_PUSHDOWN()`**
{% hint style="info" %}
Available from MariaDB 12.1.
{% endhint %}

These hints enable or disable the [Condition Pushdown into Derived Table Optimization](../query-optimizations/optimizations-for-derived-tables/condition-pushdown-into-derived-table-optimization.md), effectively overriding the optimizer switch setting `condition_pushdown_for_derived=[on|off]`. They apply to derived tables, views and CTEs of the query.

#### Examples
```sql
SELECT /*+ NO_DERIVED_CONDITION_PUSHDOWN(v1) */ * 
  FROM v1, t2 WHERE
  ((v1.max_c>300) AND (v1.avg_c>t2.d) AND (v1.b=t2.b)) OR
    ((v1.max_c<135) AND (v1.max_c<t2.c) AND (v1.a=t2.a));
```
Here the hint disables pushing conditions `(max_c > 300 or max_c < 135)` into the view `v1`.

In the next example the optimization is disabled by the optimizer switch setting, however the hint allows pushing conditions into the view `v1` inside `cte`:
```sql
set optimizer_switch='condition_pushdown_for_derived=off';

explain format=JSON
WITH cte AS (
  SELECT /*+ QB_NAME(qb1) */ max_c, avg_c
  FROM v1,t2
  WHERE ((v1.max_c>300) and (v1.avg_c>t2.d) and (v1.b=t2.b)) or
    ((v1.max_c<135) and (v1.max_c<t2.c) and (v1.a=t2.a))
)
SELECT /*+ DERIVED_CONDITION_PUSHDOWN(@qb1) */ * FROM cte;
```

Example with pushing down conditions into a derived table:
```sql
SELECT /*+ NO_DERIVED_CONDITION_PUSHDOWN(dt) */ * FROM (
  SELECT qb.b AS a
  FROM (
    SELECT 1 * t4.b AS b, 1 * t4.a AS a FROM t4
  ) qb
  GROUP BY qb.a
) dt WHERE (dt.a = 2);
```

 ### * **`MERGE()`, `NO_MERGE()`**
 {% hint style="info" %}
Available from MariaDB 12.1.
{% endhint %}

These hints enable or disable the [Derived Table Merge Optimization](../query-optimizations/optimizations-for-derived-tables/derived-table-merge-optimization.md), effectively overriding the optimizer switch setting `derived_merge=[on|off]`.

#### Examples
Let's say there is a statement:
```sql
EXPLAIN EXTENDED
SELECT a, b
FROM (SELECT a, b FROM t1) AS dt
WHERE a < 3 AND b > 8;

+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | SIMPLE      | t1    | ALL   | NULL          | NULL     | NULL    | NULL |   10 |     100.00  | Using where
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```
By default the derived table `dt` gets merged into the main `SELECT`, so the output of `EXPLAIN` displays only one line.

However, if the user does not want `dt` to be merged, they can add `NO_MERGE()` hint:
```sql
EXPLAIN EXTENDED
SELECT /*+ NO_MERGE(dt)*/ a, b
FROM (SELECT a, b FROM t1) AS dt
WHERE a < 3 AND b > 8;

+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | PRIMARY     | <derived2> | ALL | NULL          | NULL     | NULL    | NULL |   10 |     100.00  | Using where
|  2 | DERIVED     | t1    | ALL   | NULL          | NULL     | NULL    | NULL |   10 |     100.00  | Using where
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```
Now the output displays two lines indicating that `dt` has not been merged but materialized instead. The same effect could be achieved by applying query-block level variant of the hint: `/*+ NO_MERGE()*/` (however, the hint would affect not only `dt` but all other derived tables of the query block, if there were any).

The hints can be applied to CTE's too:
```sql
set session optimizer_switch='derived_merge=off';

EXPLAIN
WITH cte AS (SELECT a, b FROM t1)
SELECT /*+ MERGE(cte)*/ a, b
FROM cte WHERE a < 3 AND b > 8;
```
However, they do **not** have effect on merging of views.

### * **`SPLIT_MATERIALIZED()`, `NO_SPLIT_MATERIALIZED()`**
{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}

These hints control the Split-materialized optimization also known as [Lateral Derived optimization](../query-optimizations/optimizations-for-derived-tables/lateral-derived-optimization.md).

Let's look at the statement which will employ the lateral derived optimization by default:
```sql
EXPLAIN
SELECT t1.n1 FROM t1,
   (SELECT n1, n2 FROM t1 WHERE c1 = 'a' GROUP BY n1) AS t
WHERE t.n1 = t1.n1 AND t.n2 = t1.n2 AND c1 = 'a' GROUP BY n1;

+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | PRIMARY     | t1    | ref   | c1,n1_c1_n2   | c1       |       1 | const|    2 |     100.00  | Using index condition; Using where; Using temporary; Using filesort
|  1 | PRIMARY     | <derived2> | ref | key0          | key0     |       8 | test.t1.n1,test.t1.n2|    1 |     100.00  | 
|  2 | LATERAL DERIVED | t1 | ref | c1,n1_c1_n2   | n1_c1_n2 |       4 | test.t1.n1|    1 |     100.00  | Using where; Using index
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```
`select_type` = `LATERAL DERIVED` at the bottom line of `EXPLAIN` output indicates the optimization has been applied.

If the user applies the hint, the optimization will be disabled and there will be no more `LATERAL DERIVED` in the output:
```sql
EXPLAIN
SELECT /*+ NO_SPLIT_MATERIALIZED(t) */ t1.n1 FROM t1,
   (SELECT n1, n2 FROM t1 WHERE c1 = 'a' GROUP BY n1) AS t
WHERE t.n1 = t1.n1 AND t.n2 = t1.n2 AND c1 = 'a' GROUP BY n1;

+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | PRIMARY     | t1    | ref   | c1,n1_c1_n2   | c1       |       1 | const|    2 |     100.00  | Using index condition; Using where; Using temporary; Using filesort
|  1 | PRIMARY     | <derived2> | ref | key0          | key0     |       8 | test.t1.n1,test.t1.n2|    1 |     100.00  | 
|  2 | DERIVED     | t1    | ref   | c1            | c1       |       1 | const|    2 |     100.00  | Using index condition; Using where; Using temporary; Using filesort
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```
As with other hints, users can use `SPLIT_MATERIALIZED()` to force the optimization when it is not chosen by the cost-based optimizer or disabled by default ( `optimizer_switch='split_materialized=off'` ).

