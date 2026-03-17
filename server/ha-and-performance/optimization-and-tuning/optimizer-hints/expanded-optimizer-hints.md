# Expanded New-Style Optimizer Hints

{% hint style="info" %}
New-style optimizer hints were introduced in MariaDB 12.0 and 12.1.
{% endhint %}

## **Description**

In order to control optimizer choices of query plans, one can use
 [optimizer_switch](../system-variables/server-system-variables.md#optimizer_switch), [join cache level](../system-variables/server-system-variables.md#join_cache_level) and other system variables. However, these variables affect execution of all queries but not some specific ones. To get more granular control, one can use optimizer hints.

Optimizer hints allow to control execution plans on a per-query basis. Technically, they are specifically formatted comments embedded right into the query text. For example:

```sql
SELECT /*+ JOIN_ORDER(t2, t1) NO_INDEX(t2)*/ t1.* FROM t1, t2 ... ;
SELECT /*+ NO_SEMIJOIN() */ * FROM t1 WHERE t1.a IN (...);
SELECT /*+ MERGE(dt1) */ * FROM (SELECT * FROM t1) AS dt1;
DELETE /*+ NO_BNL(t2@qb1) */ * FROM t1 WHERE a IN (SELECT /*+ QB_NAME(qb1) */ .. );
UPDATE /*+ NO_RANGE_OPTIMIZATION(t1 PRIMARY) */  * FROM t1 ...;
```

## Syntax
Hints sequence starts with `/*+` and ends with `*/`. There can be an arbitrary number of hints in the sequence, separated by spaces. Hints are recognized by the parser if they follow the initial keyword `SELECT`, `UPDATE`, `DELETE`. Each query block can have its own set of hints, for example:

```sql
SELECT /*+ ... */ ... FROM t1 WHERE a IN (SELECT /*+ ... */ ...);
UPDATE /*+ ... */ ... WHERE a IN (SELECT /*+ ... */ ... );
SELECT /*+ ... */ ... UNION ALL SELECT /*+ ... */ ...;
```

`INSERT ... SELECT` statements support hints only at the `SELECT` part, not at the `INSERT` part:

```sql
INSERT INTO ... SELECT /*+ ... */ ...;
```

A single query block may have multiple hints in a single hint sequence, for example:

```sql
SELECT /*+ NO_BKA(qb1) INDEX(t1 idx1) JOIN_PREFIX(t2, t1)*/ ... FROM t1, t2 ...;
```
but multiple sequences are not supported:

```sql
SELECT /*+ NO_BKA(qb1) */ /*+ INDEX(t1 idx1) */ ... FROM t1 ...;
```

Incorrect syntax, duplication of hints or other inconsistencies produce warnings:

```sql
SELECT /*+ QB_NAME(qb1) QB_NAME(qb1 ) */ * FROM t2 ...
...
Warnings:
Warning 4219    Hint QB_NAME(`qb1`) is ignored as conflicting/duplicated

SELECT /*+ BKA(t1) NO_BKA(t1) */ * FROM t1 ...
...
Warnings:
Warning 4219    Hint NO_BKA(`t1`) is ignored as conflicting/duplicated

SELECT /*+ INDEX(t1) JOIN_INDEX(t1) */ a FROM t1 ...
...
Warnings:
Warning 4240    Hint JOIN_INDEX(`t1` ) is ignored as conflicting/duplicated (an index hint of the same type or opposite kind has already been specified for this table)

SELECT /*+ SEMIJOIN(loosescan @qb1) */ a FROM t1 ...
...
Warnings:
Warning 1064    Optimizer hint syntax error near '@qb1) */ a FROM t1' at line 1

SELECT /*+ SUBQUERY(@qb1 materialization) */ a FROM t1 ...
...
Warnings:
Warning 4220    Query block name `qb1` is not found for SUBQUERY hint
```
Hints that were not rejected as invalid/conflicting/duplicated are visible in the output of `EXPLAIN EXTENDED`, in section "Warnings":

```sql
EXPLAIN EXTENDED SELECT /*+ INDEX(t1)*/ a FROM t1;
id      select_type     table   type    possible_keys   key     key_len ref     rows    filtered        Extra
1       SIMPLE  t1      index   NULL    i_a     5       NULL    256     100.00  Using index
Warnings:
Note    1003    select /*+ INDEX(`t1`@`select#1`) */ `test`.`t1`.`a` AS `a` from `test`.`t1`

```

### General notes

* If a table has an alias, hints must refer to the alias, not the table name.
* Table names in hints cannot be qualified with schema names.
* Hints may be specified within VIEW's during their creation, and they are applied locally within that VIEW's scope.  For example:
```sql
CREATE VIEW v1 AS
  SELECT /*+ GROUP_INDEX(t1 idx1) */ FROM t1 ... GROUP BY ... HAVING ...
```
The hints are then visible in the output of `SHOW CREATE VIEW`.

## **Hint Hierarchy**

Hints can apply at different levels:

* global - the hints affect _the whole query_;
* query-block-level - the hints affect _a certain query block_ of the query;
* table-level - the hints affect _certain tables_;
* index-level - the hints affect _particular indexes of tables_.

## Available Optimizer Hints

This table provides an overview of optimizer hints supported in MariaDB, showing which optimizations each hint controls and at what level (global, query block, table, or index) they can be applied.

| Hint Name | Affected Optimization | Applicable Scopes |
|-----------|----------------------|-------------------|
| [`BKA`, `NO_BKA`](#table-level-hints) | Batched key access join | Query block, Table |
| [`BNL`, `NO_BNL`](#table-level-hints) | Block nested-loop join | Query block, Table |
| [`DERIVED_CONDITION_PUSHDOWN`, `NO_DERIVED_CONDITION_PUSHDOWN`](#-derived_condition_pushdown-no_derived_condition_pushdown) | Condition pushdown for derived tables | Query block, Table |
| [`GROUP_INDEX`, `NO_GROUP_INDEX`](#index-level-hints) | Use of indexes for `GROUP BY` operations | Table, Index |
| [`INDEX`, `NO_INDEX`](#index-level-hints) | Use of indexes | Table, Index |
| [`INDEX_MERGE`, `NO_INDEX_MERGE`](#index_merge-no_index_merge) | Index merge | Table, Index |
| [`JOIN_FIXED_ORDER`](#join-order-hints) | Straight join order | Query block |
| [`JOIN_INDEX`, `NO_JOIN_INDEX`](#join-order-hints) | Use of indexes for data access | Index |
| [`JOIN_ORDER`](#join-order-hints) | Join order | Table |
| [`JOIN_PREFIX`](#join-order-hints) | Join order for first tables | Table |
| [`JOIN_SUFFIX`](#join-order-hints) | Join order for last tables | Table |
| [`MAX_EXECUTION_TIME`](#max_execution_time) | Query execution time limit | Global |
| [`MERGE`, `NO_MERGE`](#merge-no_merge) | Derived table/CTE merging | Query block, Table |
| [`MRR`, `NO_MRR`](#mrr-no_mrr) | Multi-Range Read | Table, Index |
| [`NO_ICP`](#no_icp) | Index Condition Pushdown | Table, Index |
| [`NO_RANGE_OPTIMIZATION`](#no_range_optimization) | Range optimization | Table, Index |
| [`ORDER_INDEX`, `NO_ORDER_INDEX`](#index-level-hints) | Use of indexes for sorting | Table, Index |
| [`QB_NAME`](#query-block-naming) | Assigns name to query block | Query block |
| [`ROWID_FILTER`, `NO_ROWID_FILTER`](#rowid_filter-no_rowid_filter) | Rowid filtering | Table, Index |
| [`SEMIJOIN`, `NO_SEMIJOIN`](#subquery-hints) | Semi-join optimization | Query block |
| [`SPLIT_MATERIALIZED`, `NO_SPLIT_MATERIALIZED`](#split_materialized-no_split_materialized) | Lateral derived / split materialization | Table |
| [`SUBQUERY`](#subquery-hints) | Subquery transformation | Query block |


### **Syntax of global Hints**
Such hints affect _the whole query_.

#### Syntax
```sql
hint_name(arguments)
```
Currently, there is only one global hint:

* [`MAX_EXECUTION_TIME`](#max_execution_time)

### **Syntax of Query-Block Level Hints**
These hints affect _a certain query block_ of the query.

#### Syntax
```sql
hint_name([@query_block_name])
```
#### Examples
```sql
SELECT /*+ NO_BNL() */ * FROM t1 JOIN t2 ON t1.a = t2.a;
```
This statement contains one query block (since its name is not specified explicitly, this query block is assigned an implicit name `select#1`). The [`NO_BNL()`](#-bnl-no_bnl) hint does not specify a query block name, so it is applied to the query block where the hint is specified. The hint disables block nested loop join for any tables of this query block.

```sql
SELECT /*+ BKA(@qb1)*/ a FROM
  (SELECT /*+ QB_NAME(qb1)*/ * FROM t1 JOIN t2 ON t1.a = t2.a) AS dt;
```
This statement contains two query blocks:
* the topmost one which does not have an explicit name;
* the one corresponding to derived table `dt` which is assigned an explicit name `qb1` with the use of `QB_NAME` hint.

Here the `BKA(@qb1)` hint addresses query block name `qb1`. The hint enables [batched key access join](../query-optimizer/block-based-join-algorithms.md#batch-key-access-join) for tables of this query block.

This syntax is equivalent to:
```sql
SELECT a FROM
  (SELECT /*+ BKA(@qb1) QB_NAME(qb1)*/ * FROM t1 JOIN t2 ON t1.a = t2.a) AS dt;

SELECT a FROM
  (SELECT /*+ BKA()*/ * FROM t1 JOIN t2 ON t1.a = t2.a) AS dt;
```

See [query block naming](#query-block-naming) for more information.

### **Syntax of Table-Level Hints**

These hints affect _certain tables_ of the statement.

There are two syntax variants of table-level hints: to affect tables from the same query block, and to affect tables from different query blocks.

#### Tables from the same query block

This variant addresses some or all tables of a particular query block:
```sql
hint_name([@query_block_name] [tbl_name [, tbl_name] ...])
```
Both `@query_block_name` and the list of `tbl_name`'s are optional.
If `@query_block_name` is **not** specified, the hint applies to tables of the query block the hint is added to. If no tables are specified in the list, the hint affects the whole query block and effectively becomes a [query-block-level hint](#query-block-level-hints).

#### Examples
```sql
SELECT /*+ NO_MERGE(dt) */ dt.a, dt.b
  FROM (SELECT a, b FROM t1) AS dt
  JOIN (SELECT a, b FROM t2) AS dt2 ON dt.a = dt2.a;
```
The hint disables merging of derived table `dt` into the upper SELECT. More information about this hint [can be found here](#-merge-no_merge).

If a user wants to disable merging of both `dt` and `dt2`, they can mention both derived table names in the hint body:
```sql
SELECT /*+ NO_MERGE(dt, dt2) */ dt.a, dt.b
  FROM (SELECT a, b FROM t1) AS dt
  JOIN (SELECT a, b FROM t2) AS dt2 ON dt.a = dt2.a;
```
Alternatively, since there are no more derived tables in the statement besides `dt` and `dt2`, the same effect can be achieved with the query-block level variant of the hint:
```sql
SELECT /*+ NO_MERGE() */ dt.a, dt.b
  FROM (SELECT a, b FROM t1) AS dt
  JOIN (SELECT a, b FROM t2) AS dt2 ON dt.a = dt2.a;
```
Here the effect of the hint is applied to the scope of the main query block.

Now let's consider a more complicated example when a user has a statement with two derived tables one of which is nested into another:
```sql
SELECT dt.a, dt.b
  FROM (
    SELECT t1.a, t1.b FROM t1
    JOIN (SELECT a, b FROM t2) AS dt_inner ON t1.a = dt_inner.a
  ) dt_outer;
```

If a user wants to disable merging of the inner derived table `dt_inner`, there are three ways of doing that:
* assign an explicit name to the query block that the inner derived table belongs to, and address `dt_inner` with a hint from the topmost query block:
```sql
SELECT /*+ NO_MERGE(@inner_qb_name dt_inner) */ dt.a, dt.b
  FROM (
    SELECT /*+ QB_NAME(inner_qb_name) */ t1.a, t1.b FROM t1
    JOIN (SELECT a, b FROM t2) AS dt_inner ON t1.a = dt_inner.a
  ) dt_outer;
```
If there were more derived tables in `inner_qb_name` query block to address, they all should have been mentioned in the hint body, for example: `NO_MERGE(@inner_qb_name dt_inner, dt_inner2, dt_inner3)`

* place the hint right into the inner query block:
```sql
SELECT dt.a, dt.b
  FROM (
    SELECT /*+ NO_MERGE(dt2)*/ t1.a, t1.b FROM t1
    JOIN (SELECT a, b FROM t2) AS dt2 ON t1.a = dt2.a
  ) dt;
```
* use an alternative variant of the syntax that is described [in the paragraph below](#tables-from-different-query-blocks):
```sql
SELECT /*+ NO_MERGE(dt_inner@inner_qb_name) */ dt.a, dt.b
  FROM (
    SELECT /*+ QB_NAME(inner_qb_name) */ t1.a, t1.b FROM t1
    JOIN (SELECT a, b FROM t2) AS dt_inner ON t1.a = dt_inner.a
  ) dt_outer;
```

#### Tables from different query blocks

This variant of the syntax addresses tables from different query blocks:
```sql
hint_name([tbl_name@query_block_name [, tbl_name@query_block_name] ...])
```

For example, a user wants to disable [batched key access join](#-bka-no_bka) for table `t2` from derived query `dt` and for table `t3` from the topmost query block. They can mention both table names in the hint body as follows:
```sql
SELECT /*+ NO_BKA(t2@inner_qb, t3)*/ SUM(t3.a) FROM
    (SELECT /*+ QB_NAME(inner_qb)*/ t1.b FROM t1 JOIN t2 ON t1.a = t2.a) AS dt
    JOIN t3 ON t3.a = dt.b;
```
If they run `EXPLAIN EXTENDED` for this query, they will see the hint applied to both tables from the hint body:
```sql
Warnings:
Note	1003	select /*+ NO_BKA(`t2`@`inner_qb`) NO_BKA(`t3`@`select#1`) */ sum(`test`.`t3`.`a`) AS `SUM(t3.a)` from `test`.`t1` join `test`.`t2` join `test`.`t3` where `test`.`t3`.`a` = `test`.`t1`.`b` and `test`.`t1`.`a` = `test`.`t2`.`a`
```
`select#1` here is the implicit system name of the topmost query block (see more about this at [query block naming](#query-block-naming)).

In fact, the user can add the hints to the query in the same way as it is displayed above:
```sql
SELECT /*+ NO_BKA(`t2`@`inner_qb`) NO_BKA(`t3`@`select#1`) */ SUM(t3.a) FROM
    (SELECT /*+ QB_NAME(inner_qb)*/ t1.b FROM t1 JOIN t2 ON t1.a = t2.a) AS dt
    JOIN t3 ON t3.a = dt.b;
```
or 
```sql
SELECT /*+ NO_BKA(`t2`@`inner_qb`, `t3`@`select#1`) */ SUM(t3.a) FROM
    (SELECT /*+ QB_NAME(inner_qb)*/ t1.b FROM t1 JOIN t2 ON t1.a = t2.a) AS dt
    JOIN t3 ON t3.a = dt.b;
```
It is also possible to assign a name to the topmost query block and refer each table by the explicit block name:
```sql
SELECT /*+ QB_NAME(topmost) NO_BKA(`t2`@`inner_qb`, `t3`@`topmost`) */ SUM(t3.a) FROM
    (SELECT /*+ QB_NAME(inner_qb)*/ t1.b FROM t1 JOIN t2 ON t1.a = t2.a) AS dt
    JOIN t3 ON t3.a = dt.b;
```
or use implicit system names of query blocks:
```sql
SELECT /*+ NO_BKA(`t2`@`select#2`, `t3`@`select#1`) */ SUM(t3.a) FROM
    (SELECT /*+ QB_NAME(qb1)*/ t1.b FROM t1 JOIN t2 ON t1.a = t2.a) AS dt
    JOIN t3 ON t3.a = dt.b;
```

### **Syntax of Index-Level Hints**

These hints affect the use of all or certain indexes of a table.

Possible syntax variants are:

```sql
hint_name(table_name [index_name [, index_name] ...])
hint_name(table_name@query_block [index_name [, index_name] ...])
```
`table_name`/`table_name@query_block` is necessary while the list of `index_name`'s can be omitted. In the latter case the hint applies at the table level. However, index-level hints cannot be elevated to the scope of a query block, i.e., syntax `hint_name(@query_block)` is not allowed.

Let us say a user has a table:

```sql
CREATE TABLE t1 (a INT, b INT, c INT, d INT,
                 KEY i_a(a), KEY i_b(b),
                 KEY i_ab(a,b), KEY i_c(c), KEY i_d(d));
```
and the optimizer chooses range scan of index `i_a` for the query
```sql
SELECT a FROM t1 WHERE a > 1 AND a < 3;
```
If the user wants to enforce the optimizer employ full scan of `t1`, they can add `NO_INDEX` hint:
```sql
SELECT /*+ NO_INDEX(t1)*/ a FROM t1 WHERE a > 1 AND a < 3;
```
If for some reason the optimizer chooses a suboptimal index when there is a more efficient one (say, `i_ab`), the user can force the optimizer to choose the preferred index:
```sql
SELECT /*+ INDEX(t1 i_ab)*/a FROM t1 WHERE a > 1 AND a < 3
```

While [`INDEX`/`NO_INDEX` hints](#-index-no_index) control the use of indexes for any operations, [`GROUP_INDEX`/`NO_GROUP_INDEX`](#-group_index-no_group_index), 
[`JOIN_INDEX`/`NO_JOIN_INDEX`](#-join_index-no_join_index) and [`ORDER_INDEX`/`NO_ORDER_INDEX`](#-order_index-no_order_index) provide more fine-grained control.

## Table-level hints

Supported variants of syntax:
```sql
hint_name([@query_block_name])
hint_name([@query_block_name] [tbl_name [, tbl_name] ...])
hint_name([tbl_name@query_block_name [, tbl_name@query_block_name] ...])
```
See [Syntax of query-block](#syntax-of-query-block-level-hints) and [table level hints](#syntax-table-level-hints) for more information.

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


## Index-level hints

#### Overview 
These hints follow [the syntax of index-level hints](#syntax-of-index-level-hints) which includes two variants:

```sql
hint_name(table_name [index_name [, index_name] ...])
hint_name(table_name@query_block [index_name [, index_name] ...])
```

They enable or disable the specified indexes for index scans for specific operations. The following rules apply:

* for _enabling (or whitelisting)_ hints (`GROUP_INDEX`, `JOIN_INDEX`, `INDEX`, `ORDER_INDEX`):

   * if the hint body includes only a table name and no index names, the optimizer is free to choose any applicable index of that table;
   * if the body includes both a table name and one or more index names, the optimizer will only consider the specified indexes for that table;

* for _disabling (or blacklisting)_ hints (`NO_GROUP_INDEX`, `NO_JOIN_INDEX`, `NO_INDEX`, `NO_ORDER_INDEX`):

   * if the hint body includes only a table name and no index names, the optimizer will not use any indexes for that table;
   * if the body includes both a table name and one or more index names, the optimizer will not use the specified indexes for that table but can use any other not listed.


### * **`GROUP_INDEX()`, `NO_GROUP_INDEX()`**
{% hint style="info" %}
Available from MariaDB 12.1.
{% endhint %}

These hints enable or disable the specified indexes for index scans for `GROUP BY` operations but do not affect other operations: access to table data and sorting. Equivalent to old-style hints `FORCE INDEX FOR GROUP BY` and `IGNORE INDEX FOR GROUP BY`.

#### Examples
```sql
-- Do not use indexes of `t1` for the `GROUP BY` operation
SELECT /*+ NO_GROUP_INDEX(t1)*/ a, MAX(b) FROM t1 GROUP BY a;
```

```sql
-- Force `idx_ab` index to be used for `GROUP BY`, although other 
-- indexes may be also applicable
SELECT /*+ GROUP_INDEX(t1 idx_ab) */ a, MAX(b) FROM t1 GROUP BY a;
```


### * **`JOIN_INDEX()`, `NO_JOIN_INDEX()`**
{% hint style="info" %}
Available from MariaDB 12.1.
{% endhint %}

Enable or disable the specified indexes for an access method (`range`, `ref`, etc.). Equivalent to old-style hints `FORCE INDEX FOR JOIN` and `IGNORE INDEX FOR JOIN`.

#### Example
```sql
-- Force the optimizer to consider only `idx1` and `idx2` indexes to access
-- table `t1` data, although there may be other indexes applicable
SELECT /*+ JOIN_INDEX(t1 idx1, idx2)*/a FROM t1 WHERE a > 1 AND a < 3;
```

### * **`INDEX()`, `NO_INDEX()`**
{% hint style="info" %}
Available from MariaDB 12.1.
{% endhint %}

Enable or disable the specified indexes for all scopes (access to table data, grouping and sorting). Equivalent to old-style hints `FORCE INDEX` and `IGNORE INDEX`.

#### Examples
```sql
-- Forbid using indexes `i_a` and `i_ab` but do not prevent the optimizer
-- from using any other applicable indexes
SELECT /*+ NO_INDEX(t1 i_a, i_ab)*/ a, MAX(b) FROM t1 WHERE a > 1 AND a < 3 GROUP BY a;
```

```sql
-- Force the optimizer to use index `i_a`
UPDATE /*+ INDEX(t1 i_a) */ t1 SET d = 1 WHERE a = 1 AND b = 2 AND c = 3;
```

```sql
-- Do not allow the optimizer to use index `i_ab`, however any other
-- applicable index can be used
DELETE /*+ NO_INDEX(t1 i_ab) */ FROM t1 WHERE a = 1 AND b = 2 AND c = 3;
```

### * **`ORDER_INDEX()`, `NO_ORDER_INDEX()`**
{% hint style="info" %}
Available from MariaDB 12.1.
{% endhint %}

These hints enable or disable the specified indexes for sorting rows but do not affect other operations: access to table data and grouping. Equivalent to old-style hints `FORCE INDEX FOR ORDER BY` and `IGNORE INDEX FOR ORDER BY`.

#### Example
```sql
-- Forbid using of index `i_ab` for sorting. However, the optimizer is free
-- to use any other available index
SELECT /*+ NO_ORDER_INDEX(t1 i_ab) */ a FROM t1 ORDER BY a;
```

### * **Index hints combination**

Multiple index hints can be combined in a single query unless they conflict with each other. For example:

```sql
-- No indexes are allowed for grouping, index `i_ab` is forbidden for ordering,
-- but all indexes are usable for data access
SELECT /*+ NO_GROUP_INDEX(t1), NO_ORDER_INDEX(t1 i_ab) */ a
FROM t1 WHERE a > 1 AND a < 3 
GROUP BY a
ORDER BY a;
```

Here the hints do not conflict with each other because they target different operations.

A conflict may happen when the same class of hints is applied to a single table, for example:
```sql
SELECT /*+ JOIN_INDEX(t1 i_a) NO_JOIN_INDEX(t1 i_d) */ a FROM t1;
```

or when an umbrella hint `INDEX`/`NO_INDEX` is specified:
```sql
SELECT /*+ INDEX(t1 i_a) JOIN_INDEX(t1 i_d) */ a FROM t1 WHERE a < 3;
```
Here the warning will be generated:
```sql
Warning 4238    Hint JOIN_INDEX(`t1` `i_d`) is ignored as conflicting/duplicated (an index hint of the same type has already been specified for this table)
```
because `INDEX` hint is essentially a combination of `JOIN_INDEX`|`GROUP_INDEX`|`ORDER_INDEX`.

If a single SQL query includes both old-style and new-style index hints, old-style hints are silently ignored, for example:
```sql
SELECT /*+ INDEX(t1 i_a) */ * FROM t1 IGNORE INDEX(i_a) WHERE a = 1 AND b = 2 AND c = 3;
```
New-style `INDEX(t1 i_a)` has effect while old-style `IGNORE INDEX(i_a)` does not.

### * `INDEX_MERGE()`, `NO_INDEX_MERGE()`
{% hint style="info" %}
This hint is available from MariaDB 12.2.
{% endhint %}

The `INDEX_MERGE` and `NO_INDEX_MERGE` optimizer hints provide granular control over the optimizer's use of index merge strategies. They allow users to override the optimizer's cost-based calculations and global switch settings, to force or prevent the merging of indexes for specific tables.

#### Syntax

```sql
/*+ INDEX_MERGE(table_name [index_name, ...]) */
/*+ NO_INDEX_MERGE(table_name [index_name, ...]) */
```

#### Behavior

The hints operate by modifying the set of keys the optimizer considers for merge operations. The specific behavior depends on whether specific index keys are provided within the hint.

#### **INDEX\_MERGE Hint**

This hint instructs the optimizer to employ an index merge strategy.

* Without arguments: When specified as `INDEX_MERGE(tbl)`, the optimizer considers all available keys for that table and selects the cheapest index merge combination.
* With specific keys: When specified with keys, for instance, `INDEX_MERGE(tbl key1, key2)`, the optimizer considers only the listed keys for the merge operation. All other keys are excluded from consideration for index merging.

{% hint style="info" %}
The `INDEX_MERGE` hint overrides the global [optimizer\_switch](../query-optimizations/optimizer-switch.md). Even if a specific strategy (such as [index\_merge\_intersection](../query-optimizations/index_merge-sort_intersection.md)) is disabled globally, the hint forces the optimizer to attempt the strategy using the specified keys.
{% endhint %}

#### **NO\_INDEX\_MERGE Hint**

This hint instructs the optimizer to avoid index merge strategies.

* Without arguments: When specified as `NO_INDEX_MERGE(tbl)`, index merge optimizations are completely disabled for the specified table.
* With specific keys: When specified with keys, for instance, `NO_INDEX_MERGE(tbl key1)`, the listed keys are excluded from consideration. The optimizer may still perform a merge using other available keys. However, if excluding the listed keys leaves insufficient row-ordered retrieval (ROR) scans available, no merge is performed.

#### Algorithm Selection and Limitations

While these hints control which keys are candidates for merging, they do not directly dictate the specific merge algorithm (Intersection, Union, or Sort-Union).

* Indirect Control: You can influence the strategy indirectly by combining these hints with [optimizer\_switch](../query-optimizations/optimizer-switch.md) settings, but specific algorithm selection is not guaranteed.
* Invalid Hints: If a hint directs the optimizer to use specific indexes, but those indexes do not provide sufficient ROR scans to form a valid plan, the server is unable to honor the hint. In this scenario, the server emits a warning.

#### Examples

In the following examples, the [index\_merge\_intersection](../query-optimizations/index_merge-sort_intersection.md) switch is globally disabled. However, the `INDEX_MERGE` hint forces the optimizer to consider specific keys (`f2` and `f4`), resulting in an intersection strategy.

You can see that we disable intersection with `NO_INDEX_MERGE` for the following query and the behavior reflects in the [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) output.  The query after that shows with the hint enabling merge–an intersection of `f3,f4` is used.  In the last example, a different intersection is used: `f3,PRIMARY`.

No intersection (no merged indexes):

```sql
MariaDB [test]> EXPLAIN SELECT /*+ NO_INDEX_MERGE(t1 f2, f4, f3) */ COUNT(*) FROM t1 WHERE f4 = 'h' AND f3 = 'b' AND f5 = 'i'\G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: t1
         type: ref
possible_keys: PRIMARY,f3,f4
          key: f3
      key_len: 9
          ref: const,const
         rows: 1
        Extra: Using index condition; Using where
1 row in set (0.009 sec)
```

Intersection of keys `f3, f4`:

```sql
MariaDB [test]> EXPLAIN SELECT /*+ INDEX_MERGE(t1 f2, f4, f3) */ COUNT(*) FROM t1 WHERE f4 = 'h' AND f3 = 'b' AND f5 = 'i'\G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: t1
         type: index_merge
possible_keys: PRIMARY,f3,f4
          key: f3,f4
      key_len: 9,9
          ref: NULL
         rows: 1
        Extra: Using intersect(f3,f4); Using where; Using index
1 row in set (0.010 sec)
```

Intersection of keys `PRIMARY, f3`:

```sql
MariaDB [test]> EXPLAIN SELECT COUNT(*) FROM t1 WHERE f4 = 'h' AND f3 = 'b' AND f5 = 'i'\G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: t1
         type: index_merge
possible_keys: PRIMARY,f3,f4
          key: f3,PRIMARY
      key_len: 9,4
          ref: NULL
         rows: 1
        Extra: Using intersect(f3,PRIMARY); Using where
1 row in set (0.006 sec)
```

### * **`NO_ICP()`**
{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

Disables [Index Condition Pushdown](../query-optimizations/index-condition-pushdown.md) for a specified table or a subset of its indexes. Effectively overrides the optimizer_switch setting `index_condition_pushdown=on`.

#### Examples
```sql
-- By default, ICP is enabled and we can see "Using index condition" in the "Extra" field of EXPLAIN output
> EXPLAIN SELECT * FROM tbl WHERE key_col1 BETWEEN 10 AND 11 AND key_col2 LIKE '%foo%';
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table | type  | possible_keys | key      | key_len | ref  | rows | Extra                 |
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | SIMPLE      | tbl   | range | key_col1      | key_col1 | 5       | NULL |    2 | Using index condition |
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+

-- Hint disables ICP, so there is no more "Using index condition" in the EXPLAIN output
> EXPLAIN SELECT /*+ NO_ICP(tbl)*/ * FROM tbl WHERE key_col1 BETWEEN 10 AND 11 AND key_col2 LIKE '%foo%';
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table | type  | possible_keys | key      | key_len | ref  | rows | Extra                 |
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | SIMPLE      | tbl   | range | key_col1      | key_col1 | 5       | NULL |    2 |                       |
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+

-- Same effect is achieved by specifying both table name and index name
> EXPLAIN SELECT /*+ NO_ICP(tbl key_col1)*/ * FROM tbl WHERE key_col1 BETWEEN 10 AND 11 AND key_col2 LIKE '%foo%';
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table | type  | possible_keys | key      | key_len | ref  | rows | Extra                 |
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | SIMPLE      | tbl   | range | key_col1      | key_col1 | 5       | NULL |    2 |                       |
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```

### * **`NO_RANGE_OPTIMIZATION()`**
{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

An index-level hint that disables range optimization for certain index(es) or a whole table. There is no corresponding optimizer switch setting for this optimization.

#### Examples
```sql
-- By default, the optimizer chooses `PRIMARY` key for `range` access to `t1`
> EXPLAIN SELECT f1 FROM t3 WHERE f1 > 30 AND f1 < 33;
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
id   | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
1    |  SIMPLE     |  t3   | range | PRIMARY,f2_idx|  PRIMARY |    4    | NULL |   2  |     100.00  |  Using where; Using index
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+

-- Exclude `PRIMARY` key from indexes allowed for `range` access, `f2_idx` is used instead
EXPLAIN EXTENDED SELECT /*+ NO_RANGE_OPTIMIZATION(t3 PRIMARY) */ f1 FROM t3 WHERE f1 > 30 AND f1 < 33;
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
id   | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
1    |  SIMPLE     |  t3   | range | PRIMARY,f2_idx| f2_idx   |   4     |  NULL|  2   |   100.00    | Using where; Using index
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+

-- This hint excludes all indexes applicable for `range` access, so the optimizer switches to the `index` access
EXPLAIN EXTENDED SELECT /*+ NO_RANGE_OPTIMIZATION(t3 PRIMARY, f2_idx) */ f1 FROM t3 WHERE f1 > 30 AND f1 < 33;
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
id   | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
1    | SIMPLE      | t3    | index | PRIMARY,f2_idx|  PRIMARY |  4      | NULL | 56   |   4.11      | Using where; Using index

-- The hint disables range access for any indexes of `t3`, `index` access is used as in the test above
EXPLAIN EXTENDED SELECT /*+ NO_RANGE_OPTIMIZATION(t3) */ f1 FROM t3 WHERE f1 > 30 AND f1 < 33;
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
id   | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
1    | SIMPLE      | t3    | index | PRIMARY,f2_idx|  PRIMARY |  4      | NULL | 56   |   4.11      | Using where; Using index

```


### * `MRR()`, `NO_MRR()`
{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}

These hints allow to control [the multi-range read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md), effectively overriding the optimizer switch setting `mrr=[on|off]`.

#### Examples
```sql
-- MRR optimization is disabled by optimizer_switch setting:
set optimizer_switch='mrr=off';

--Turn on MRR for `t1` table
SELECT /*+ MRR(t1) */ * FROM t1 WHERE f2 <= 3 AND 3 <= f3;

--Turn on MRR for `IDX2` of table `t1`
SELECT /*+ MRR(t1 IDX2) */ * FROM t1 WHERE f2 <= 3 AND 3 <= f3;
```

```sql
-- MRR optimization is enabled by optimizer_switch setting (default setting):
set optimizer_switch='mrr=on';

-- Disable multi-range read when accessing table `t1`
SELECT /*+ NO_MRR(t1) */ * FROM t1 WHERE f2 <= 3 AND 3 <= f3;
```


### * `ROWID_FILTER()`, `NO_ROWID_FILTER()`
{% hint style="info" %}
Available from MariaDB 12.1.
{% endhint %}

Allows to control the [ROWID filter optimization](../query-optimizations/rowid-filtering-optimization.md). Effectively they override the optimizer switch setting `rowid_filter=[on|off]`.

* Rules for `ROWID_FILTER()` hint:
   * if the hint body includes only a table name and no index names, the optimizer is free to choose any indexes applicable for rowid-filtering optimization;
   * if the body includes both a table name and one or more index names, the optimizer will only consider the specified indexes for rowid-filtering;
   * the hint forces the use of rowid-filtering (if applicable) despite being less efficient than not using the optimization (from the optimizer's point of view);

* Rules for `NO_ROWID_FILTER()` hint:
   * if the hint body includes only a table name and no index names, the optimizer will not use any indexes for rowid-filtering;
   * if the body includes both a table name and one or more index names, the optimizer will not use the specified indexes for rowid-filtering but can use any other not listed.

#### Examples
```sql
SELECT /*+ rowid_filter(t1)*/ a FROM t1 WHERE a < 'e' AND b > 't';
SELECT /*+ no_rowid_filter(t1)*/ a FROM t1 WHERE a < 'e' AND b > 't';
SELECT /*+ rowid_filter(t1 key_a, key_b)*/ a FROM t1 WHERE a < 'e' AND b > 't';
SELECT /*+ no_rowid_filter(t1 key_c)*/ a FROM t1 WHERE a < 'e' AND b > 't';
```

#### Interaction with other index hints
If `[NO_]INDEX()`, `[NO_]JOIN_INDEX()` hints are specified for the same table, then only indexes whitelisted by `INDEX()` or `JOIN_INDEX()` can be considered for rowid filters. `ROWID_FILTER(` hint cannot force the use of indexes that are disabled by `NO_INDEX()` / `NO_JOIN_INDEX()` or omitted from `INDEX()` / `JOIN_INDEX()`. For example, if one index should be used for data access and another for a rowid filter, the filter index must be mentioned in _both_ hints:
```sql
SELECT /*+ index(t1 key_a, key_b) rowid_filter(t1 key_b) */ a FROM t1 ....
```

## Join Order hints

{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}

#### Overview 
These hints allow to control the order in which tables of a query are joined.

Generally, these hints follow the syntax rules of [table-level hints](#syntax-of-table-level-hints) with some important differences.

Syntax of the `JOIN_FIXED_ORDER` hint:

```sql
hint_name([@query_block_name])
```
In contrast to other table-level hints, `JOIN_FIXED_ORDER` does not allow specifying table names in the hint body.

Syntax variants of other join-order hints:

```sql
hint_name([@query_block_name] tbl_name [, tbl_name] ...)
hint_name(tbl_name[@query_block_name] [, tbl_name[@query_block_name]] ...)
```
Here the query block name may be omitted, but at least one table name must be specified.


### * `JOIN_FIXED_ORDER([@query_block_name])`

Forces the optimizer to join tables using the order in which they appear in the `FROM` clause. This is the same as specifying `SELECT STRAIGHT_JOIN`.

#### Examples
```sql
-- Tables will be joined in the order `t2` -> `t1` even if order `t1` -> `t2` looks more promising:
SELECT /*+ JOIN_FIXED_ORDER() */ f1, f2
  FROM t2 JOIN t1 ON t1.id=t2.id ORDER BY f1, f2;
```

### * `JOIN_ORDER()`

Instructs the optimizer to join tables using the specified table order. The hint applies to the named tables. The optimizer may place tables that are not named anywhere in the join order, including between specified tables.


### * `JOIN_PREFIX()`

Instructs the optimizer to join tables using the specified table order for the first tables of the join execution plan. The hint applies to the named tables. The optimizer places all other tables after the named tables.

### * `JOIN_SUFFIX()`

Instructs the optimizer to join tables using the specified table order for the last tables of the join execution plan. The hint applies to the named tables. The optimizer places all other tables before the named tables.

Example:
```sql
SELECT /*+ JOIN_PREFIX(t2, t5@subq2)
           JOIN_ORDER(t4@subq2, t1)
           JOIN_SUFFIX(t3)*/ count(*)
             FROM t1 JOIN t2 JOIN t3
               WHERE t1.a IN (SELECT /*+ QB_NAME(subq1) */ a FROM t4)
                 AND t2.a IN (SELECT /*+ QB_NAME(subq2) */ a FROM t5);
```

## Subquery hints

{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}

#### **Overview**

Subquery hints determine:

* If [Semi-join subquery optimizations](../query-optimizations/subquery-optimizations/semi-join-subquery-optimizations.md) are to be used;
* Which semijoin strategies are permitted;
* When semijoins are not used, whether to use subquery materialization or [IN-TO-EXISTS transformation](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#the-in-to-exists-transformation).

### * **`SEMIJOIN()`, `NO_SEMIJOIN()`**
#### **Syntax**

```
hint_name([@query_block_name] [strategy [, strategy] ...])
```

* `hint_name`: `SEMIJOIN` or `NO_SEMIJOIN`.
* `strategy`: name of the strategy to be enabled (in case of `SEMIJOIN` hint) or disabled (in case of `NO_SEMIJOIN` hint). The following strategy names are permitted: `DUPSWEEDOUT`, `FIRSTMATCH`, `LOOSESCAN`, `MATERIALIZATION`.

For `SEMIJOIN` hints, if no strategies are named, semi-join is used based on the strategies enabled according to the `optimizer_switch` system variable, if possible. If strategies are named, but inapplicable for the statement, `DUPSWEEDOUT` is used.

For `NO_SEMIJOIN` hints, semi-join is not used if no strategies are named. If named strategies rule out all applicable strategies for the statement, `DUPSWEEDOUT` is used.

If a subquery is nested within another, and both are merged into a semi-join of an outer query, any specification of semi-join strategies for the innermost query are ignored. `SEMIJOIN` and `NO_SEMIJOIN` hints can still be used to enable or disable semi-join transformations for such nested subqueries.

#### **Examples**

```sql
SELECT /*+ NO_SEMIJOIN(@subq1 FIRSTMATCH, LOOSESCAN) */ * FROM t2
  WHERE t2.a IN (SELECT /*+ QB_NAME(subq1) */ a FROM t3);

SELECT /*+ SEMIJOIN(@subq1 MATERIALIZATION, DUPSWEEDOUT) */ * FROM t2
  WHERE t2.a IN (SELECT /*+ QB_NAME(subquery1) */ a FROM t3);
```

### * **`SUBQUERY()`**

#### **Syntax**
```sql
SUBQUERY([@query_block_name] strategy)
```

* `strategy`: allowed values are `INTOEXISTS` and `MATERIALIZATION`.

#### Examples
```sql
SELECT id, a IN (SELECT /*+ SUBQUERY(MATERIALIZATION) */ a FROM t1) FROM t2;

SELECT /*+ SUBQUERY(@qb1 INTOEXISTS) */* FROM t2 WHERE t2.a IN (SELECT /*+ QB_NAME(qb1)*/ a FROM t1);
```


### * **`MAX_EXECUTION_TIME()`**
{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}

Global-level hint to limit query execution time

```sql
SELECT /*+ MAX_EXECUTION_TIME(milliseconds) */ ...  ;
```

A query that doesn't finish in the time specified will be aborted with an error.

However, if `@@max_statement_time` system variable is set, the hint will be ignored and a warning produced. Note that this contradicts the stated principle that "new-style hints are more specific than server variable settings, so they override the server variable settings".


## Query Block Naming

Optimizer hints can address certain named query blocks within the query. Query block is either a top-level `SELECT`/`UPDATE`/`DELETE` statement or a subquery within the statement.

There are three ways to address query blocks:

* by an explicit name assigned using `QB_NAME()` hint
* by implicit name based on position of the query block in the query
* by implicit name based on alias of derived table, view or CTE

### Explicit query block names

* `QB_NAME(query_block_name)` hint is used to assign a name to a query block in which this hint is placed.

#### Examples
Assigning a name to a top-level `SELECT` statement:
```sql
SELECT /*+ QB_NAME(foo) */ * FROM t1 ...;
```
Assigning a name to a subquery:
```sql
SELECT * FROM (SELECT /*+ QB_NAME(subq) */* FROM t1 ...) dt ...;
```
Assigning names to multiple query blocks:
```sql
SELECT /*+ QB_NAME(qb_outer) */ ...
  FROM (SELECT /*+ QB_NAME(dt1) */ ...
  FROM (SELECT /*+ QB_NAME(dt2) */ ... FROM ...) dt2) dt1 ...
```

The assigned name can then be used to refer to the query block in optimizer hints, for example:
```sql
SELECT /*+ QB_NAME(qb_outer) NO_ICP(@qb1 t1) BNL(@dt1) INDEX(t2@dt2 idx1) */ ...
  FROM t1, (SELECT /*+ QB_NAME(dt1) */ ...
      FROM (SELECT /*+ QB_NAME(dt2) */ ... FROM t2 ...) dt2) dt1 ...
```

The scope of a query block name is the whole statement. It is invalid to use the same name for multiple query blocks. You can refer to the query block "down into subquery", "down into derived table", "up to the parent" and "to a right sibling in the `UNION`". You cannot refer "to a left sibling in a `UNION`".

### Explicit query block names with path
{% hint style="info" %}
Available from MariaDB 13.0.
{% endhint %}

* `QB_NAME(query_block_name, query_block_path)` hint is used to assign names to query blocks nested within views, derived tables, and CTEs

#### Syntax
```sql
QB_NAME(name, query_block_path)
```
where
```sql
query_block_path ::= query_block_path_element
                      [ {. query_block_path_element }... ]
query_block_path_element ::= @ qb_path_element_select_num |
                                qb_path_element_view_sel
qb_path_element_view_sel ::= qb_path_element_view_name
                              [ @ qb_path_element_select_num ]
```

`query_block_path` is similar to a path in filesystem in some sense. Each next element descends further into the query blocks structure. Path elements are separated with dots (`.`).

Each path element can be either a:

* View/derived table/CTE name
* Select number in the current query block, such as `@SEL_1`, `@SEL_2`, etc.
* Combination of view/derived table/CTE name and select number, such as `v1@SEL_1`, `dt1@SEL_2`, etc.

#### Examples

```sql
CREATE VIEW v1 AS SELECT * FROM t1 WHERE a < 1000;

-- The name `qb_v1` is assigned to the inner query block of the view `v1`
SELECT /*+ qb_name(qb_v1, v1) no_index(t1@qb_v1)*/* FROM v1;

-- This means the same but specifies that `v1` is present in @SEL_1
-- of the current query block. So, @SEL_1 can be omitted here
SELECT /*+ qb_name(qb_v1, v1@SEL_1) no_index(t1@qb_v1)*/* FROM v1;

-- However, here we have two occurrences of `v1` in different query blocks
-- (@SEL_1 and @SEL_2), so specifying @SEL_1 is essential
SELECT /*+ qb_name(qb_v1, v1@SEL_1) no_index(t1@qb_v1)*/* FROM v1 WHERE a < 10
UNION
SELECT * FROM v1 WHERE b > 100;
```

Path consisting of two elements:
```sql
-- The view has two query blocks
CREATE VIEW v1 AS SELECT * FROM t1 WHERE a < 10 
                  UNION
                  SELECT * FROM t2 WHERE b > 20;

-- This hint means that SELECT#2 of view `v1`, which is present in 
-- SELECT#1 of the current query block, gets the name `qb_v1`.
SELECT /*+ qb_name(qb_v1, v1@sel_1 .@sel_2) */ * FROM v1;
```

Views and derived tables may be nested on multiple levels, for example:
```sql
-- The path follows `dt1` -> `dt2` -> `v2` -> `@SEL_2` of `v2`
SELECT /*+ qb_name(dt2_dt1_v1_1, dt1 .dt2 .v2 .@SEL_2)
           no_index(t1@dt2_dt1_v1_1)*/ v1.*
FROM v1 
     JOIN (SELECT v1.* FROM v1 
           JOIN (SELECT * FROM v2) dt2
          ) dt1
```

#### Limitations
* Only SELECT statements support QB names with path. DML operations
  (UPDATE, DELETE, INSERT) do not support them
* QB names with path are not supported inside view definitions (`CREATE VIEW ...`)


### Implicit names based on position
{% hint style="info" %}
Available from MariaDB 12.2.
{% endhint %}

Besides the given name, any query block has an implicit name `select_#n` (where `#n` stands for a number). You can see these numbers in the column `id` of the `EXPLAIN` output:

```sql
-- `select#1` addresses the topmost query block joining tables `e` and `s`.
-- The hint disables merging of derived table `(select * from salaries) s`
EXPLAIN
SELECT /*+ NO_MERGE(s@`select#1`) */ e.emp_name, s.salary
FROM employees e JOIN (select * from salaries) s ON e.emp_id = s.emp_id
WHERE s.salary > (SELECT AVG(salary) FROM salaries);
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | PRIMARY     | e     | ALL   | PRIMARY       | NULL     | NULL    | NULL |    5 |   100.00    | NULL
|  1 | PRIMARY     | <derived2> | ref | key0          | key0     | 5       | test.e.emp_id |    1 |   100.00    | Using where
|  3 | SUBQUERY    | salaries | ALL | NULL          | NULL     | NULL    | NULL |    5 |   100.00    | NULL
|  2 | DERIVED     | salaries | ALL | NULL          | NULL     | NULL    | NULL |    5 |   100.00    | NULL
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```

```sql
-- `select#2` addresses the query block corresponding to derived table `T`
EXPLAIN SELECT /*+ JOIN_ORDER(@`select#2` twenty,ten) */  * 
FROM (SELECT ten.a AS a FROM (ten JOIN twenty)
      WHERE (ten.a = twenty.a) LIMIT 1000 ) T;
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | PRIMARY     | <derived2> | ALL | NULL          | NULL     | NULL    | NULL |  200 |   100.00    | NULL
|  2 | DERIVED     | twenty  | ALL | NULL          | NULL     | NULL    | NULL |   20 |   100.00    | NULL
|  2 | DERIVED     | ten     | ALL | NULL          | NULL     | NULL    | NULL |   10 |   100.00    | Using where; Using join buffer (flat, BNL join)
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```

#### Limitations
* The positional numbers of query blocks are not stable and can change if the query is modified or its execution plan changes (for example, due to statistics re-collection). If a more stable query block addressing is needed then [explicit naming](#explicit-query-block-names) is probably a better choice.
* Implicit names based on position are not supported inside view definitions (`CREATE VIEW ...`).

### Implicit names based on aliases
{% hint style="info" %}
Available from MariaDB 13.0
{% endhint %}

It is possible to address a query block corresponding to a derived table, view or CTE using its name or an alias in the query.

#### Examples
```sql
-- Addressing a table inside a derived table using implicit QB name
SELECT /*+ no_index(t1@dt) */ *
  FROM (SELECT * FROM t1 WHERE a > 10) AS DT;
-- this is an equivalent to:
SELECT /*+ no_index(t1@dt) */ * FROM
  (SELECT /*+ qb_name(dt)*/ * FROM t1 WHERE a > 10) AS DT;
-- Addressing a query block corresponding to the derived table
SELECT /*+ no_bnl(@dt) */ *
  FROM (SELECT * FROM t1, t2 WHERE t1.a > t2.a) AS DT;

-- View
CREATE VIEW v1 AS SELECT * FROM t1 WHERE a > 10 AND b > 100;

-- referencing a table inside a view by implicit QB name:
SELECT /*+ index_merge(t1@v1 idx_a, idx_b) */ *
  FROM v1, t2 WHERE v1.a = t2.a;
-- equivalent to:
CREATE VIEW v1 AS SELECT /*+ qb_name(qb_v1) */ *
  FROM t1 WHERE a > 10 AND b > 100;
SELECT /*+ index_merge(t1@qb_v1 idx_a, idx_b) */ *
  FROM v1, t2 WHERE v1.a = t2.a;

-- CTE
WITH aless100 AS (SELECT a FROM t1 WHERE b <100)
  SELECT /*+ index(t1@aless100) */ * FROM aless100;
-- equivalent to:
WITH aless100 AS (SELECT /*+ qb_name(aless100) */ a FROM t1 WHERE b <100)
  SELECT /*+ index(t1@aless100) */ * FROM aless100;
```
#### Limitations
* Only SELECT statements support implicit QB names based on aliases. DML operations
  (UPDATE, DELETE, INSERT) do not support them.
* Implicit names based on aliases are not supported inside view definitions (`CREATE VIEW ...`).
