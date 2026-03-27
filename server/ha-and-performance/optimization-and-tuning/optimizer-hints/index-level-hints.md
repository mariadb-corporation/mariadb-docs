# Index-Level Hints

## Overview

These hints follow the syntax of index-level hints which includes two variants:

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

## **`GROUP_INDEX()`, `NO_GROUP_INDEX()`**&#x20;

{% hint style="info" %}
These hints are available from MariaDB 12.1.
{% endhint %}

These hints enable or disable the specified indexes for index scans for `GROUP BY` operations but do not affect other operations: access to table data and sorting. Equivalent to old-style hints `FORCE INDEX FOR GROUP BY` and `IGNORE INDEX FOR GROUP BY`.

### Examples

```sql
-- Do not use indexes of `t1` for the `GROUP BY` operation
SELECT /*+ NO_GROUP_INDEX(t1)*/ a, MAX(b) FROM t1 GROUP BY a;
```

```sql
-- Force `idx_ab` index to be used for `GROUP BY`, although other 
-- indexes may be also applicable
SELECT /*+ GROUP_INDEX(t1 idx_ab) */ a, MAX(b) FROM t1 GROUP BY a;
```

## **`JOIN_INDEX()`, `NO_JOIN_INDEX()`**

{% hint style="info" %}
These hints are available from MariaDB 12.1.
{% endhint %}

Enable or disable the specified indexes for an access method (`range`, `ref`, etc.). Equivalent to old-style hints `FORCE INDEX FOR JOIN` and `IGNORE INDEX FOR JOIN`.

### Example

```sql
-- Force the optimizer to consider only `idx1` and `idx2` indexes to access
-- table `t1` data, although there may be other indexes applicable
SELECT /*+ JOIN_INDEX(t1 idx1, idx2)*/a FROM t1 WHERE a > 1 AND a < 3;
```

## **`INDEX()`, `NO_INDEX()`**

{% hint style="info" %}
These hints are available from MariaDB 12.1.
{% endhint %}

Enable or disable the specified indexes for all scopes (access to table data, grouping and sorting). Equivalent to old-style hints `FORCE INDEX` and `IGNORE INDEX`.

### Examples

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

## **`ORDER_INDEX()`, `NO_ORDER_INDEX()`**

{% hint style="info" %}
These hints are available from MariaDB 12.1.
{% endhint %}

These hints enable or disable the specified indexes for sorting rows but do not affect other operations: access to table data and grouping. Equivalent to old-style hints `FORCE INDEX FOR ORDER BY` and `IGNORE INDEX FOR ORDER BY`.

### Example

```sql
-- Forbid using of index `i_ab` for sorting. However, the optimizer is free
-- to use any other available index
SELECT /*+ NO_ORDER_INDEX(t1 i_ab) */ a FROM t1 ORDER BY a;
```

## Combining Multiple Index Hints

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

## `INDEX_MERGE()`, `NO_INDEX_MERGE()`

{% hint style="info" %}
This hint is available from MariaDB 12.2.
{% endhint %}

The `INDEX_MERGE` and `NO_INDEX_MERGE` optimizer hints provide granular control over the optimizer's use of index merge strategies. They allow users to override the optimizer's cost-based calculations and global switch settings, to force or prevent the merging of indexes for specific tables.

### Syntax

```sql
/*+ INDEX_MERGE(table_name [index_name, ...]) */
/*+ NO_INDEX_MERGE(table_name [index_name, ...]) */
```

### Behavior

The hints operate by modifying the set of keys the optimizer considers for merge operations. The specific behavior depends on whether specific index keys are provided within the hint.

### **INDEX\_MERGE Hint**

This hint instructs the optimizer to employ an index merge strategy.

* Without arguments: When specified as `INDEX_MERGE(tbl)`, the optimizer considers all available keys for that table and selects the cheapest index merge combination.
*   With specific keys: When specified with keys, for instance, `INDEX_MERGE(tbl key1, key2)`, the optimizer considers only the listed keys for the merge operation. All other keys are excluded from consideration for index merging.

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>The <code>INDEX_MERGE</code> hint overrides the global <a href="../query-optimizations/optimizer-switch.md">optimizer_switch</a>. Even if a specific strategy (such as <a href="../query-optimizations/index_merge-sort_intersection.md">index_merge_intersection</a>) is disabled globally, the hint forces the optimizer to attempt the strategy using the specified keys.</p></div>



### **NO\_INDEX\_MERGE Hint**

This hint instructs the optimizer to avoid index merge strategies.

* Without arguments: When specified as `NO_INDEX_MERGE(tbl)`, index merge optimizations are completely disabled for the specified table.
* With specific keys: When specified with keys, for instance, `NO_INDEX_MERGE(tbl key1)`, the listed keys are excluded from consideration. The optimizer may still perform a merge using other available keys. However, if excluding the listed keys leaves insufficient row-ordered retrieval (ROR) scans available, no merge is performed.

### Algorithm Selection and Limitations

While these hints control which keys are candidates for merging, they do not directly dictate the specific merge algorithm (Intersection, Union, or Sort-Union).

* Indirect Control: You can influence the strategy indirectly by combining these hints with [optimizer\_switch](../query-optimizations/optimizer-switch.md) settings, but specific algorithm selection is not guaranteed.
* Invalid Hints: If a hint directs the optimizer to use specific indexes, but those indexes do not provide sufficient ROR scans to form a valid plan, the server is unable to honor the hint. In this scenario, the server emits a warning.

### Examples

In the following examples, the [index\_merge\_intersection](../query-optimizations/index_merge-sort_intersection.md) switch is globally disabled. However, the `INDEX_MERGE` hint forces the optimizer to consider specific keys (`f2` and `f4`), resulting in an intersection strategy.

You can see that we disable intersection with `NO_INDEX_MERGE` for the following query and the behavior reflects in the [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) output. The query after that shows with the hint enabling merge–an intersection of `f3,f4` is used. In the last example, a different intersection is used: `f3,PRIMARY`.

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

## **`NO_ICP()`**

This hint is available from MariaDB 12.0.

Disables [Index Condition Pushdown](../query-optimizations/index-condition-pushdown.md) for a specified table or a subset of its indexes. Effectively overrides the optimizer\_switch setting `index_condition_pushdown=on`.

### Examples

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

## **`NO_RANGE_OPTIMIZATION()`**

{% hint style="info" %}
This hint is available from MariaDB 12.0.
{% endhint %}

An index-level hint that disables range optimization for certain index(es) or a whole table. There is no corresponding optimizer switch setting for this optimization.

### Examples

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

## `MRR()`, `NO_MRR()`

{% hint style="info" %}
These hints are available from MariaDB 12.0.
{% endhint %}

These hints allow to control [the multi-range read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md), effectively overriding the optimizer switch setting `mrr=[on|off]`.

### Examples

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

## `ROWID_FILTER()`, `NO_ROWID_FILTER()`

{% hint style="info" %}
These hints are available from MariaDB 12.1.
{% endhint %}

Allows to control the [ROWID filter optimization](../query-optimizations/rowid-filtering-optimization.md). Effectively they override the optimizer switch setting `rowid_filter=[on|off]`.

* Rules for `ROWID_FILTER()` hint:
  * if the hint body includes only a table name and no index names, the optimizer is free to choose any indexes applicable for rowid-filtering optimization;
  * if the body includes both a table name and one or more index names, the optimizer will only consider the specified indexes for rowid-filtering;
  * the hint forces the use of rowid-filtering (if applicable) despite being less efficient than not using the optimization (from the optimizer's point of view);
* Rules for `NO_ROWID_FILTER()` hint:
  * if the hint body includes only a table name and no index names, the optimizer will not use any indexes for rowid-filtering;
  * if the body includes both a table name and one or more index names, the optimizer will not use the specified indexes for rowid-filtering but can use any other not listed.

### Examples

```sql
SELECT /*+ rowid_filter(t1)*/ a FROM t1 WHERE a < 'e' AND b > 't';
SELECT /*+ no_rowid_filter(t1)*/ a FROM t1 WHERE a < 'e' AND b > 't';
SELECT /*+ rowid_filter(t1 key_a, key_b)*/ a FROM t1 WHERE a < 'e' AND b > 't';
SELECT /*+ no_rowid_filter(t1 key_c)*/ a FROM t1 WHERE a < 'e' AND b > 't';
```

## Interaction with Other Index Hints

If `[NO_]INDEX()`, `[NO_]JOIN_INDEX()` hints are specified for the same table, then only indexes whitelisted by `INDEX()` or `JOIN_INDEX()` can be considered for rowid filters. `ROWID_FILTER(` hint cannot force the use of indexes that are disabled by `NO_INDEX()` / `NO_JOIN_INDEX()` or omitted from `INDEX()` / `JOIN_INDEX()`. For example, if one index should be used for data access and another for a rowid filter, the filter index must be mentioned in _both_ hints:

```sql
SELECT /*+ index(t1 key_a, key_b) rowid_filter(t1 key_b) */ a FROM t1 ....
```
