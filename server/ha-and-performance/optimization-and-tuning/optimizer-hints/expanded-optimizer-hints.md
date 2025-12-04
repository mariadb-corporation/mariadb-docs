# Expanded New-Style Optimizer Hints

{% hint style="info" %}
New-style optimizer hints were introduced in MariaDB 12.0 and 12.1.
{% endhint %}

## **Description**

Each individual hint is hint name and arguments. In case there are no arguments, the `()` parentheses are still present:

```
hint:  hint_name([arguments])
```

Incorrect hints produce warnings (a setting to make them errors is not implemented yet).

Hints that are not ignored are kept in the query text (you can see them in `SHOW PROCESSLIST`, Slow Query Log, `EXPLAIN EXTENDED`). Hints that were incorrect and were ignored are removed from there.

### **Hint Hierarchy**

Hints can be:

* global - they apply to whole query;
* table-level - they apply to a table;
* index-level - they apply to an index in a table.

#### **Table-Level Hints**

```sql
hint_name([table_name [table_name [,...]] )
```

#### **Index-Level Hints**

Index-level hints apply to indexes. Possible syntax variants are:

```sql
hint_name(table_name [index_name [, index_name] ...])

hint_name(table_name@query_block [index_name [, index_name] ...])

hint_name(@query_block  table_name [index_name [, index_name] ...])
```

### **Effect of Optimizer Hints**

The optimizer can be controlled by

1. server variables - optimizer\_switch, join\_cache\_level, and so forth;
2. old-style hints;
3. new-style hints.

Old-style hints do not overlap with server variable settings.

New-style hints are more specific than server variable settings, so they override the server variable settings.

Hints are "narrowly interpreted" and "best effort" - if a hint dictates to do something, for example:

```sql
SELECT  /*+ MRR(t1 t1_index1) */  ... FROM t1 ...
```

It means: When considering a query plan that involves using `t1_index1` in a way that one can use `MRR`, use `MRR`. If the query planning is such that use of `t1_index1` doesn't allow to use `MRR`, it won't be used.

The optimizer may also consider using `t1_index2` and pick that over `using t1_index1`. In such cases, the hint is effectively ignored and no warning is given.

### **Query Block Naming**

The `QB_NAME` hint is used to assign a name to the query block the hint is in. The Query block is either a `SELECT` statement or a top-level construct of an `UPDATE` or `DELETE` statement.

```sql
SELECT /*+ QB_NAME(foo) */ select_list FROM ...
```

The name can then can be used

* to refer to the query block;
* to refer to a table in the query block as `table_name@query_block_name`.

Query block scope is the whole statement. It is invalid to use the same name for multiple query blocks. You can refer to the query block "down into subquery", "down into derived table", "up to the parent" and "to a right sibling in the `UNION`". You cannot refer "to a left sibling in a `UNION`".

Hints inside views are not supported, yet. You can neither use hints in `VIEW` definitions, nor control query plans inside non-merged views. (This is because `QB_NAME` binding are done "early", before we know that some tables are views.)

### **SELECT#N NAMES**

Besides the given name, any query block is given a name `select`_`#n`_  (where _`#n`_ stands for a number). You can see it when running `EXPLAIN EXTENDED`:

```sql
Note 1003 SELECT /*+ NO_RANGE_OPTIMIZATION(t3@select#1 PRIMARY) */ ...
```

It is **not** possible to use it in the hint text:

```sql
SELECT /*+ BKA(tbl1@`select#1`) */ 1 FROM tbl1 ...;
```

### **QB\_NAME in CTEs**

Hints that control `@name` will control the first use of the CTE (common table expression).

## Available Expanded Optimizer Hints

### NO\_ROWID\_FILTER

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

```
/* +NO_ROWID_FILTER([table_name [index_name [ ... ] ]] ) */
```

Does not consider `ROWID` filter for the scope of the hint (all tables in the query block, specific table, and specific indexes). See [ROWID\_FILTER](expanded-optimizer-hints.md#rowid_filter) for details.

### NO\_SPLIT\_MATERIALIZED

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

When a derived table is materialized, MariaDB processes and stores the results of that derived table temporarily before joining it with other tables. The "lateral derived" optimization specifically looks for ways to optimize these types of derived tables. It does that by pushing a splitting condition down into the derived table, to limit the number of rows materialized into the derived table. The `SPLIT_MATERIALIZED` hint forces this behavior, while `NO_SPLIT_MATERIALIZED` prevents it.

`NO_SPLIT_MATERIALIZED(`_`X`_`)` disables the use of split-materialized optimization in the context of _`X` :_

```sql
SELECT
  /*+ NO_SPLIT_MATERIALIZED(CUST_TOTALS) */
  ...
FROM
  customer
  (SELECT SUM(amount), o_custkey FROM orders GROUP BY o_custkey) as CUST_TOTALS
WHERE
   customer.c_custkey= o_custkey AND
   customer.country='FI';
```

### ROWID\_FILTER

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

```
/* +ROWID_FILTER( [table_name [index_name [ ...] ]]) */
```

Like [NO\_RANGE\_OPTIMIZATION](expanded-optimizer-hints.md#no_range_optimization) or [MRR](expanded-optimizer-hints.md#mrr-and-no_mrr), this hint can be applied to:

* Query blocks — `NO_ROWID_FILTER()`
* Table — `NO_ROWID_FILTER(`_`table_name`_`)`
* Specific indexes — `NO_ROWID_FILTER(`_`table_name index1 index2 ...`_`)`&#x20;

Forces the use of `ROWID_FILTER` for the table index it targets:

* For query blocks and tables, it enables the use of the `ROWID` filter, assuming it is disabled globally.
* For indexes, it forces its use, regardless of the costs. The following query forces the use of the `ROWID` filter made from _`t1.idx1`_ if the chosen plan allows so (that is, if the access method to _`t1`_ allows it):

```sql
SELECT /*+ ROWID_FILTER(t1 idx1) */
...
```

{% hint style="warning" %}
Assuming the optimizer would pick _`idx2`_ for table _`t1`_ if the hint was _not_ used, this could result in the usage of both _`idx2`_ and _`idx1`_ if the hint _is_ used. That might become more expensive than a full table scan, or result in a change of the join order.

Therefore, do not "blindly" use this filter, but rather make sure its use doesn't have a negative impact as described.
{% endhint %}

### SPLIT\_MATERIALIZED

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

When a derived table is materialized, MariaDB processes and stores the results of that derived table temporarily before joining it with other tables. The "lateral derived" optimization specifically looks for ways to optimize these types of derived tables. It does that by pushing a splitting condition down into the derived table, to limit the number of rows materialized into the derived table. The `SPLIT_MATERIALIZED` hint forces this behavior, while `NO_SPLIT_MATERIALIZED` prevents it.

`SPLIT_MATERIALIZED(`_`X`_`)` enables and forces the use of split-materialized optimization in the context of _`X`_, unless it is impossible to do (for instance, because a table is not a materialized derived table).

```sql
SELECT
  /*+ SPLIT_MATERIALIZED(CUST_TOTALS) */
  ...
FROM
  customer
  (SELECT SUM(amount), o_custkey FROM orders GROUP BY o_custkey) as CUST_TOTALS
WHERE
   customer.c_custkey= o_custkey AND
   customer.country='FI';
```

{% hint style="info" %}
The following hints are available from MariaDB 12.0, unless indicated otherwise.
{% endhint %}

Hints are placed after the main statement verb.

```sql
UPDATE /*+ hints */ table ...;
DELETE /*+ hints */ FROM table... ;
SELECT /*+ hints */  ...
```

They can also appear after the `SELECT` keyword in any subquery:

```sql
SELECT * FROM t1 WHERE a IN (SELECT /*+ hints */ ...)
```

There can be one or more hints separated with space:

```sql
hints:  hint hint ...
```

### **JOIN\_INDEX and NO\_JOIN\_INDEX**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

An index-level hint that enables or disables the specified indexes for an access method (range, ref, etc.). Equivalent to `FORCE INDEX FOR JOIN` and `IGNORE INDEX FOR JOIN`.

### **GROUP\_INDEX and NO\_GROUP\_INDEX**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

An index-level hint that enables or disables the specified indexes for index scans for `GROUP BY` operations. Equivalent to `FORCE INDEX FOR GROUP BY` and `IGNORE INDEX FOR GROUP BY`.

### **ORDER\_INDEX and NO\_ORDER\_INDEX**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

An index-level hint that enables or disables the specified indexes for sorting rows. Equivalent to `FORCE INDEX FOR ORDER BY` and `IGNORE INDEX FOR ORDER BY`.

### **INDEX and NO\_INDEX**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

An index-level hint that enables or disables the specified indexes, for all scopes (join access method, GROUP BY, or sorting). Equivalent to `FORCE INDEX` and `IGNORE INDEX`.

### INDEX\_MERGE and NO\_INDEX\_MERGE

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
* Invalid Hints: If a hint directs the optimizer to use specific indexes, but those indexes do not provide sufficient ROR scans to form a valid plan, the server is unable to honor the hint. in this scenario, the server emits a warning.

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

### **NO\_RANGE\_OPTIMIZATION**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

An index-level hint that disables range optimization for certain index(es):

```sql
SELECT /*+ NO_RANGE_OPTIMIZATION(tbl index1 index2) */  * FROM tbl ...
```

### **NO\_ICP**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

An index-level hint that disables [Index Condition Pushdown](../query-optimizations/index-condition-pushdown.md) for the indexes. ICP+BKA is disabled as well.

```sql
SELECT /*+ NO_ICP(tbl index1 index2) */  * FROM tbl ...
```

### **MRR and NO\_MRR**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

Index-level hints to force or disable use of MRR.

```sql
SELECT /*+ MRR(tbl index1 index2) */  * FROM tbl ... 

SELECT /*+ NO_MRR(tbl index1 index2) */  * FROM tbl ...
```

This controls:

* MRR optimization for range access;
* BKA.

### **BKA() and NO\_BKA()**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

Query block or table-level hints.

`BKA()` also enables MRR to make BKA possible. (This is different from session variables, where you need to enable MRR separately). This also enables BKAH.

### **BNL() and NO\_BNL()**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

Controls BNL-H.

The implementation is "BNL() hint effectively increases join\_cache\_level up to 4 " .. for the table(s) it applies to.

### **MAX\_EXECUTION\_TIME()**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

Global-level hint to limit query execution time

```sql
SELECT /*+ MAX_EXECUTION_TIME(milliseconds) */ ...  ;
```

A query that doesn't finish in the time specified will be aborted with an error.

If `@@max_statement_time` is set, the hint will be ignored and a warning produced. Note that this contradicts the stated principle that "new-style hints are more specific than server variable settings, so they override the server variable settings".

### **SPLIT\_MATERIALIZED(X) and NO\_SPLIT\_MATERIALIZED(X)**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

Enables or disables the use of the Split Materialized Optimization (also called the[ Lateral Derived Optimization](../query-optimizations/optimizations-for-derived-tables/lateral-derived-optimization.md)).

### **DERIVED\_CONDITION\_PUSHDOWN and NO\_DERIVED\_CONDITION\_PUSHDOWN**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

Enables or disables the use of [condition pushdown for derived tables](../query-optimizations/optimizations-for-derived-tables/condition-pushdown-into-derived-table-optimization.md).

### **MERGE and NO\_MERGE**

{% hint style="info" %}
This hint is available from MariaDB 12.1.
{% endhint %}

Table-level hint that enables the use of merging, or disables and uses materialization, for the specified tables, views or common table expressions.

### **SUBQUERY**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

Query block-level hint.

```sql
SUBQUERY([@query_block_name] MATERIALIZATION)

SUBQUERY([@query_block_name] INTOEXISTS)
```

This controls non-semi-join subqueries. The parameter specifies which subquery to use. Use of this hint disables conversion of subquery into semi-join.

For details, see the [Subquery Hints section](expanded-optimizer-hints.md#subquery-hints-1).

### **SEMIJOIN and NO\_SEMIJOIN**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

Query block-level hints.

This controls the conversion of subqueries to semi-joins and which semi-join strategies are allowed.

```sql
[NO_]SEMIJOIN([@query_block_name] [strategy [, strategy] ...])
```

where the strategy is one of `DUPSWEEDOUT`, `FIRSTMATCH`, `LOOSESCAN`, `MATERIALIZATION`.

Hints are placed after the main statement verb.

```sql
UPDATE /*+ hints */ table ...;
DELETE /*+ hints */ FROM table... ;
SELECT /*+ hints */  ...
```

They can also appear after the `SELECT` keyword in any subquery:

```sql
SELECT * FROM t1 WHERE a IN (SELECT /*+ hints */ ...)
```

There can be one or more hints separated with space:

```sql
hints:  hint hint ...
```

### Join Order Hints

{% hint style="info" %}
Join order hints are available from MariaDB 12.0.
{% endhint %}

Syntax of the `JOIN_FIXED_ORDER` hint:

```sql
hint_name([@query_block_name])
```

Syntax of other join-order hints:

```sql
hint_name([@query_block_name] tbl_name [, tbl_name] ...)
hint_name(tbl_name[@query_block_name] [, tbl_name[@query_block_name]] ...)
```

#### Available Join Order Hints

For the following join order hint syntax,

* _`tbl`_ is the name of a table used in the statement. A hint that names tables applies to all tables that it names. The `JOIN_FIXED_ORDER` hint names no tables and applies to all tables in the `FROM` clause of the query block in which it occurs;
* _`query_block_name`_ is the query block to which the hint applies. If the hint includes no leading _`@query_block_name`_, it applies to the query block in which it occurs. When using the _`tbl@query_block_name`_ syntax, the hint applies to the named table in the named query block. To assign a name to a query block, see [Optimizer Hints for Naming Query Blocks](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints#query-block-naming).

General notes:

* If a table has an alias, hints must refer to the alias, not the table name.
* Table names in hints cannot be qualified with schema names.

#### `JOIN_FIXED_ORDER([@query_block_name])`

Forces the optimizer to join tables using the order in which they appear in the `FROM` clause. This is the same as specifying `SELECT STRAIGHT_JOIN`.

#### `JOIN_ORDER([@query_block_name] tbl [, tbl] ...)`

Instructs the optimizer to join tables using the specified table order. The hint applies to the named tables. The optimizer may place tables that are not named anywhere in the join order, including between specified tables.

* Alternative syntax: \
  `JOIN_ORDER(tbl[@query_block_name] [, tbl[@query_block_name]] ...`)

#### `JOIN_PREFIX([@query_block_name] tbl [, tbl] ...)`

Instructs the optimizer to join tables using the specified table order for the first tables of the join execution plan. The hint applies to the named tables. The optimizer places all other tables after the named tables.

* Alternative syntax:\
  `JOIN_PREFIX(tbl[@query_block_name] [, tbl[@query_block_name]] ...`)

#### `JOIN_SUFFIX([@query_block_name] tbl [, tbl] ...)`

Instructs the optimizer to join tables using the specified table order for the last tables of the join execution plan. The hint applies to the named tables. The optimizer places all other tables before the named tables.

### Subquery Hints

{% hint style="info" %}
Subquery hints are available from MariaDB 12.0.
{% endhint %}

#### **Overview**

Subquery hints determine:

* If semijoin transformations are to be used;
* Which semijoin strategies are permitted;
* When semijoins are not used, whether to use subquery materialization or `IN-to-EXISTS` transformations.

#### **Syntax**

```
hint_name([@query_block_name] [strategy [, strategy] ...])
```

* `hint_name`: The following hint names are permitted to enable or disable the named semijoin strategies: `SEMIJOIN`, `NO_SEMIJOIN`.
* `strategy`: Enable or disable a semi-join strategy. The following strategy names are permitted: `DUPSWEEDOUT`, `FIRSTMATCH`, `LOOSESCAN`, `MATERIALIZATION`.

#### **Strategies**

For `SEMIJOIN` hints, if no strategies are named, semi-join is used based on the strategies enabled according to the `optimizer_switch` system variable, if possible. If strategies are named, but inapplicable for the statement, `DUPSWEEDOUT` is used.

For `NO_SEMIJOIN` hints, semi-join is not used if no strategies are named. If named strategies rule out all applicable strategies for the statement, `DUPSWEEDOUT` is used.

If a subquery is nested within another, and both are merged into a semi-join of an outer query, any specification of semi-join strategies for the innermost query are ignored. `SEMIJOIN` and `NO_SEMIJOIN` hints can still be used to enable or disable semi-join transformations for such nested subqueries.

If `DUPSWEEDOUT` is disabled, the optimizer may generate a query plan that is far from optimal.&#x20;

#### **Examples**

```sql
SELECT /*+ NO_SEMIJOIN(@subquery1 FIRSTMATCH, LOOSESCAN) */ * FROM t2
  WHERE t2.a IN (SELECT /*+ QB_NAME(subq1) */ a FROM t3);
SELECT /*+ SEMIJOIN(@subquery1 MATERIALIZATION, DUPSWEEDOUT) */ * FROM t2
  WHERE t2.a IN (SELECT /*+ QB_NAME(subquery1) */ a FROM t3);
```

Syntax of hints that affect whether to use subquery materialization or `IN`-to-`EXISTS` transformations:

```sql
SUBQUERY([@query_block_name] strategy)
```

The hint name is always `SUBQUERY`.

For `SUBQUERY` hints, these _`strategy`_ values are permitted: `INTOEXISTS`, `MATERIALIZATION`.

```sql
SELECT id, a IN (SELECT /*+ SUBQUERY(MATERIALIZATION) */ a FROM t1) FROM t2;
SELECT * FROM t2 WHERE t2.a IN (SELECT /*+ SUBQUERY(INTOEXISTS) */ a FROM t1);
```

For semi-join and `SUBQUERY` hints, a leading `@`_`query_block_name`_ specifies the query block to which the hint applies. If the hint includes no leading `@`_`query_block_name`_, the hint applies to the query block in which it occurs. To assign a name to a query block, see [Naming Query Blocks](expanded-optimizer-hints.md#query-block-naming).

If a hint comment contains multiple subquery hints, the first is used. If there are other following hints of that type, they produce a warning. Following hints of other types are silently ignored.
