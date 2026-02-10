# reorder\_outer\_joins

* **Introduced in**: MariaDB 12.3
* **Type**: `optimizer_switch` flag
* **Default Value**: `OFF`&#x20;
* **Dynamic**: Yes
* **Scope**: Global

## Description

The `reorder_outer_joins` flag in the `optimizer_switch` system variable manages whether the query optimizer reorders independent LEFT JOIN (and equivalent RIGHT JOIN, which are internally transformed to LEFT JOINs) operations to find the cost-effective execution plans.

With independent LEFT JOINs, there are no unnecessary dependencies on other outer joined tables; instead, each joined table depends only on the base table or on the previous tables in the join order. For example, in the query:

```
SELECT * FROM t1
LEFT JOIN t3 ON t3.key1 = t1.a
LEFT JOIN t2 ON t2.key1 = t1.a;
```

Before MariaDB 12.3, the optimizer was forced to follow the written order:

```
t1 → t3 → t2
```

Even if an alternative, such as is faster, depending on table sizes and indexing.

```
 t1 → t2 → t3
```

## Recommended Configuration

It is recommended to always set `optimizer_prune_level=0` when enabling this optimization feature, unless the join involves many tables (e.g., more than 10). This prevents heuristic pruning from inadvertently discarding optimal join orders that become available in the expanded search space.

### Configuration Example

```
SET optimizer_switch='reorder_outer_joins=ON';
SET optimizer_prune_level=0;
```

## Enabling the Optimization

When you enable this optimization, the optimizer evaluates potential join orders based on estimated costs and heuristics.

```
SET optimizer_switch='reorder_outer_joins=on';
```

When it is disabled, it restores the default behavior:

```
SET optimizer_switch='reorder_outer_joins=off';
```

With this feature is enabled, the optimizer can choose better execution order.

## Example

By default, outer joins impose ordering constraints during query optimization. For example:

```
SELECT * FROM t1
LEFT JOIN t3 ON t3.key1 = t1.a
LEFT JOIN t2 ON t2.key1 = t1.a;
```

* Without `reorder_outer_joins`_,_ the optimizer may be restricted in how it orders `t2` and `t3` relative to `t1`, even when alternative join order are logically valid.

```
SET optimizer_switch='reorder_outer_joins=OFF'; 

EXPLAIN SELECT * FROM t1 
     LEFT JOIN t3 ON t3.key1 = t1.a
     LEFT JOIN t2 ON t2.key1 = t1.a; 

-- Possible Join order: t1 → t3 → t2
```

* When `reorder_outer_joins=ON`, the optimizer can evaluate additional join orders (similar to `INNER JOINs`), which may result in better execution plans.

```
SET optimizer_prune_level=0; 
SET optimizer_switch='reorder_outer_joins=ON'; 

EXPLAIN SELECT * FROM t1 
     LEFT JOIN t3 ON t3.key1 = t1.a
     LEFT JOIN t2 ON t2.key1 = t1.a; 

-- With reordering enabled, the optimizer may choose:
-- t1 → t2 → t3 (if cost-based evaluation prefers it) 
```

## When to Use this Feature

Enabling `reorder_outer_joins=ON` in the following scenarios would be beneficial:

* Queries with Multiple Independent LEFT JOINs: When a query performs multiple `LEFT JOIN` operations against the same base table(s) without cross-dependencies between the outer tables.
* Small to Medium Join Sizes: Most effective when the total table count is typically ≤ 10. For larger joins (> 10 tables), the expanded search space might increase optimization time.
* Complex Outer Join Logic: Beneficial when using complex join structures (including those written in Oracle-style `(+)` syntax), where greater flexibility in reordering can unlock more efficient access paths.

## Performance Considerations

This optimization `reorder_outer_joins` feature expands the search space by allowing the optimizer to evaluate join orders that were previously forbidden.

* Enabling this feature, together with the following setting, can help with queries that involve a smaller number of tables by allowing more join order possibilities (up to 10 tables, for instance):

```
SET optimizer_prune_level=0; 
```

It may allow you to explore a more thorough search space, which could enhance the quality of the execution plan.

* Using `optimizer_prune_level=0` may result in a considerable increase in optimization (planning) time for queries that combine more tables.
* Heuristic pruning may remove potentially optimal join orders when `optimizer_prune_level` is larger than 0, which could lead to a less effective execution plan.

## Use Cases

This optimization feature can be useful when:

* A query containing multiple `LEFT JOIN` operations may provide a suboptimal execution plan.
* Using Oracle compatibility outer join syntax, where table sequence in the `FROM` clause may affect join order. For example,

```
SELECT * 
FROM t1,t2,t3 
WHERE t1.col1 = t2.col1(+) 
  AND t1.col2 = t3.col2(+);
```

Without `reorder_outer_joins`_,_ the optimizer may follow the table order specified in the `FROM` clause.&#x20;

With `reorder_outer_joins=ON`, the optimizer considers both:

```
t1 → t2 → t3
t1 → t3 → t2
```

and select the one with the lowest estimated cost.

## Limitations

* Large joins may increase execution planning time because the number of possible join orders grows factorially.
* Pruning may eliminate optimal orders early, since an execution plan that looks inefficient first, could be the best one.

## See Also

* [optimizer\_prune\_level](../system-variables/server-system-variables.md#optimizer_prune_level)
* [optimizer\_trace](../system-variables/server-system-variables.md#optimizer_trace)
* [optmizer\_switch](optimizer-switch.md)
* [Optimizer Switch](index-hints-how-to-force-query-plans.md#optimizer-switch)
* [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md)
