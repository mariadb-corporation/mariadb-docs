# Expanded New-Style Optimizer Hints

{% hint style="info" %}
New-style optimizer hints were introduced in MariaDB 12.0 and 12.1.
{% endhint %}

## Description

In order to control optimizer choices of query plans, one can use
 [optimizer_switch](../system-variables/server-system-variables.md#optimizer_switch), [join cache level](../system-variables/server-system-variables.md#join_cache_level) and other system variables. However, these variables affect execution of all queries but not some specific ones. To get more granular control, one can:
 * specify server variables before execution of every query (or group of queries);
 * use [SET STATEMENT ... FOR](../../../reference/sql-statements/administrative-sql-statements/set-commands/set-statement.md) to temporarily change server variables for a specific query;
 * use optimizer hints.

The benefit of optimizer hints is that they can control specific parts of the query:
how to handle a particular SELECT or subquery, which indexes to use to access
certain tables, etc.

Technically, hints are specifically formatted comments embedded right into the query text. For example:

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

### Hints inside views

Hints may be specified within VIEW's during their creation. For example:
```sql
CREATE VIEW v1 AS
  SELECT /*+ GROUP_INDEX(t1 idx1) */ FROM t1 ... GROUP BY ... HAVING ...
```
The hints are then visible in the output of `SHOW CREATE VIEW`.

#### Limitations
Hints inside views are applied locally within that VIEW's scope and do not affect the outer query. Query blocks declared inside views cannot be referenced from hints in the outer query.

```sql
-- Query block name `qb_v1` is not accessible from outer queries using `v1`!
CREATE VIEW v1 AS
  SELECT /*+ QB_NAME(qb_v1) */ FROM t1 ... GROUP BY ... HAVING ...
```
To reference inner view objects from outside the view, refer to other [query block addressing methods](query-block-naming.md) like [query block names with path](query-block-naming.md#explicit-query-block-names-with-path) or [implicit names based on aliases](query-block-naming.md#implicit-names-based-on-aliases).

## Hint Hierarchy

Hints can apply at different levels:

* global - the hints affect _the whole query_;
* query-block-level - the hints affect _a certain query block_ of the query;
* table-level - the hints affect _certain tables_;
* index-level - the hints affect _particular indexes of tables_.

## Available Optimizer Hints

This table provides an overview of optimizer hints supported in MariaDB, showing which optimizations each hint controls and at what level (global, query block, table, or index) they can be applied.

| Hint Name | Affected Optimization | Applicable Scopes |
|-----------|----------------------|-------------------|
| [`BKA`, `NO_BKA`](table-level-hints.md) | Batched key access join | Query block, Table |
| [`BNL`, `NO_BNL`](table-level-hints.md) | Block nested-loop join | Query block, Table |
| [`DERIVED_CONDITION_PUSHDOWN`, `NO_DERIVED_CONDITION_PUSHDOWN`](table-level-hints.md#derived_condition_pushdown-no_derived_condition_pushdown) | Condition pushdown for derived tables | Query block, Table |
| [`GROUP_INDEX`, `NO_GROUP_INDEX`](index-level-hints.md) | Use of indexes for `GROUP BY` operations | Table, Index |
| [`INDEX`, `NO_INDEX`](index-level-hints.md) | Use of indexes | Table, Index |
| [`INDEX_MERGE`, `NO_INDEX_MERGE`](index-level-hints.md#index_merge-no_index_merge) | Index merge | Table, Index |
| [`JOIN_FIXED_ORDER`](#join-order-hints) | Straight join order | Query block |
| [`JOIN_INDEX`, `NO_JOIN_INDEX`](index-level-hints.md) | Use of indexes for data access | Index |
| [`JOIN_ORDER`](#join-order-hints) | Join order | Table |
| [`JOIN_PREFIX`](#join-order-hints) | Join order for first tables | Table |
| [`JOIN_SUFFIX`](#join-order-hints) | Join order for last tables | Table |
| [`MAX_EXECUTION_TIME`](#max_execution_time) | Query execution time limit | Global |
| [`MERGE`, `NO_MERGE`](table-level-hints.md#merge-no_merge) | Derived table/CTE merging | Query block, Table |
| [`MRR`, `NO_MRR`](index-level-hints.md#mrr-no_mrr) | Multi-Range Read | Table, Index |
| [`NO_ICP`](#no_icp) | Index Condition Pushdown | Table, Index |
| [`NO_RANGE_OPTIMIZATION`](index-level-hints.md#no_range_optimization) | Range optimization | Table, Index |
| [`ORDER_INDEX`, `NO_ORDER_INDEX`](index-level-hints.md) | Use of indexes for sorting | Table, Index |
| [`QB_NAME`](query-block-naming.md) | Assigns name to query block | Query block |
| [`ROWID_FILTER`, `NO_ROWID_FILTER`](index-level-hints.md#rowid_filter-no_rowid_filter) | Rowid filtering | Table, Index |
| [`SEMIJOIN`, `NO_SEMIJOIN`](#subquery-hints) | Semi-join optimization | Query block |
| [`SPLIT_MATERIALIZED`, `NO_SPLIT_MATERIALIZED`](table-level-hints.md#split_materialized-no_split_materialized) | Lateral derived / split materialization | Table |
| [`SUBQUERY`](#subquery-hints) | Subquery transformation | Query block |


### Syntax of global hints
Such hints affect _the whole query_.

#### Syntax
```sql
hint_name(arguments)
```
Currently, there is only one global hint:

* [`MAX_EXECUTION_TIME`](#max_execution_time)

### Syntax of Query-Block Level Hints
These hints affect _a certain query block_ of the query.

#### Syntax
```sql
hint_name([@query_block_name])
```
#### Examples
```sql
SELECT /*+ NO_BNL() */ * FROM t1 JOIN t2 ON t1.a = t2.a;
```
This statement contains one query block (since its name is not specified explicitly, this query block is assigned an implicit name `select#1`). The [`NO_BNL()`](table-level-hints.md#bnl-no_bnl) hint does not specify a query block name, so it is applied to the query block where the hint is specified. The hint disables block nested loop join for any tables of this query block.

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

See [query block naming](query-block-naming.md) for more information.

### Syntax of Table-Level Hints

These hints affect _certain tables_ of the statement.

There are two syntax variants of table-level hints: to affect tables from the same query block, and to affect tables from different query blocks.

#### Tables from the same query block

This variant addresses some or all tables of a particular query block:
```sql
hint_name([@query_block_name] [tbl_name [, tbl_name] ...])
```
Both `@query_block_name` and the list of `tbl_name`'s are optional.
If `@query_block_name` is **not** specified, the hint applies to tables of the query block the hint is added to. If no tables are specified in the list, the hint affects the whole query block and effectively becomes a [query-block-level hint](#syntax-of-query-block-level-hints).

#### Examples
```sql
SELECT /*+ NO_MERGE(dt) */ dt.a, dt.b
  FROM (SELECT a, b FROM t1) AS dt
  JOIN (SELECT a, b FROM t2) AS dt2 ON dt.a = dt2.a;
```
The hint disables merging of derived table `dt` into the upper SELECT. More information about this hint [can be found here](table-level-hints.md#merge-no_merge).

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

For example, a user wants to disable [batched key access join](table-level-hints.md#bka-no_bka) for table `t2` from derived query `dt` and for table `t3` from the topmost query block. They can mention both table names in the hint body as follows:
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
`select#1` here is the implicit system name of the topmost query block (see more about this at [query block naming](query-block-naming.md)).

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
### List of available table-level hints
See description and the list of available table-level hints [here](table-level-hints.md).

### Syntax of Index-Level Hints

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

While [`INDEX`/`NO_INDEX` hints](index-level-hints.md#index-no_index) control the use of indexes for any operations, [`GROUP_INDEX`/`NO_GROUP_INDEX`](index-level-hints.md#group_index-no_group_index), 
[`JOIN_INDEX`/`NO_JOIN_INDEX`](index-level-hints.md#join_index-no_join_index) and [`ORDER_INDEX`/`NO_ORDER_INDEX`](index-level-hints.md#order_index-no_order_index) provide more fine-grained control.

### List of available index-level hints
See description and the list of available index-level hints [here](index-level-hints.md).


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


### * `JOIN_FIXED_ORDER()`

Forces the optimizer to join tables using the order in which they appear in the `FROM` clause. This is the same as specifying `SELECT STRAIGHT_JOIN`.

#### Examples
```sql
-- Tables will be joined in the order `t2` -> `t1` even if order `t1` -> `t2` looks more promising:
SELECT /*+ JOIN_FIXED_ORDER() */ f1, f2
  FROM t2 JOIN t1 ON t1.id = t2.id ORDER BY f1, f2;
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

#### Overview

Subquery hints determine:

* If [Semi-join subquery optimizations](../query-optimizations/subquery-optimizations/semi-join-subquery-optimizations.md) are to be used;
* Which semijoin strategies are permitted;
* When semijoins are not used, whether to use subquery materialization or [IN-TO-EXISTS transformation](../query-optimizations/subquery-optimizations/non-semi-join-subquery-optimizations.md#the-in-to-exists-transformation).

### * **`SEMIJOIN()`, `NO_SEMIJOIN()`**
#### Syntax

```
hint_name([@query_block_name] [strategy [, strategy] ...])
```

* `hint_name`: `SEMIJOIN` or `NO_SEMIJOIN`.
* `strategy`: name of the strategy to be enabled (in case of `SEMIJOIN` hint) or disabled (in case of `NO_SEMIJOIN` hint). The following strategy names are permitted: `DUPSWEEDOUT`, `FIRSTMATCH`, `LOOSESCAN`, `MATERIALIZATION`.

For `SEMIJOIN` hints, if no strategies are named, semi-join is used based on the strategies enabled according to the `optimizer_switch` system variable, if possible. If strategies are named, but inapplicable for the statement, `DUPSWEEDOUT` is used.

For `NO_SEMIJOIN` hints, semi-join is not used if no strategies are named. If named strategies rule out all applicable strategies for the statement, `DUPSWEEDOUT` is used.

If a subquery is nested within another, and both are merged into a semi-join of an outer query, any specification of semi-join strategies for the innermost query are ignored. `SEMIJOIN` and `NO_SEMIJOIN` hints can still be used to enable or disable semi-join transformations for such nested subqueries.

#### Examples

```sql
SELECT /*+ NO_SEMIJOIN(@subq1 FIRSTMATCH, LOOSESCAN) */ * FROM t2
  WHERE t2.a IN (SELECT /*+ QB_NAME(subq1) */ a FROM t3);

SELECT /*+ SEMIJOIN(@subq1 MATERIALIZATION, DUPSWEEDOUT) */ * FROM t2
  WHERE t2.a IN (SELECT /*+ QB_NAME(subquery1) */ a FROM t3);
```

### * **`SUBQUERY()`**

#### Syntax
```sql
SUBQUERY([@query_block_name] strategy)
```

* `strategy`: allowed values are `INTOEXISTS` and `MATERIALIZATION`.

#### Examples
```sql
SELECT id, a IN (SELECT /*+ SUBQUERY(MATERIALIZATION) */ a FROM t1) FROM t2;

SELECT /*+ SUBQUERY(@qb1 INTOEXISTS) */* FROM t2 WHERE t2.a IN (SELECT /*+ QB_NAME(qb1)*/ a FROM t1);
```

## Global hints

### * **`MAX_EXECUTION_TIME()`**
{% hint style="info" %}
Available from MariaDB 12.0.
{% endhint %}

Global hint to limit query execution time

```sql
SELECT /*+ MAX_EXECUTION_TIME(milliseconds) */ ...  ;
```

A query that doesn't finish in the time specified will be aborted with an error.

However, if `@@max_statement_time` system variable is set, the hint will be ignored and a warning produced. Note that this contradicts the stated principle that "new-style hints are more specific than server variable settings, so they override the server variable settings".

