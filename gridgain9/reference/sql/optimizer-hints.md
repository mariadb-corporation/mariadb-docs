---
description: >-
  SQL optimizer hints in GridGain 9: hint block syntax, precedence rules, and
  the supported hints such as FORCE_INDEX, NO_INDEX, and ENFORCE_JOIN_ORDER.
---

# Optimizer Hints

The query optimizer tries to execute the fastest execution plan. However, you can know about the data design, application design or data distribution in your cluster better. SQL hints can help the optimizer to make optimizations more rationally or build execution plan faster.

{% hint style="info" %}
SQL hints are optional to apply and might be skipped in some cases.
{% endhint %}

## Hints Format

SQL hints are defined by a special comment `/*+ HINT */`, referred to as a _hint block_. Spaces before and after the
hint name are required. The hint block must be placed right after the `SELECT` keyword, or after a table name in the `FROM` clause for table-specific hints (`USE_SECONDARY_STORAGE`, `FORCE_INDEX`, `NO_INDEX`), where it is scoped to that table. Multiple hints can be specified in a single hint block, separated by commas.

Example:

```sql
SELECT /*+ NO_INDEX, DISABLE_DECORRELATION */ T1.* FROM TBL1 T1 WHERE T1.V1 = ? AND T1.V2 = ?
```

### Hint Parameters

Hint parameters, if required, are placed in brackets after the hint name and separated by commas.

The hint parameter can be quoted. Quoted parameters are case-sensitive. You cannot specify both the case-sensitive and case-insensitive parameters in the same hint.

Example:

```sql
SELECT /*+ FORCE_INDEX(TBL1_IDX2,TBL2_IDX1) */ T1.V1, T2.V1 FROM TBL1 T1, TBL2 T2 WHERE T1.V1 = T2.V1 AND T1.V2 > ? AND T2.V2 > ?;

SELECT /*+ FORCE_INDEX('TBL2_idx1') */ T1.V1, T2.V1 FROM TBL1 T1, TBL2 T2 WHERE T1.V1 = T2.V1 AND T1.V2 > ? AND T2.V2 > ?;
```

## Hints Errors

The optimizer tries to apply every hint and its parameters, if possible. But it skips the hint or hint parameters if:

* The hint is not supported.
* Required hint parameters are not passed.
* Hint parameters have been passed, but the hint does not support parameters.
* The hint parameter is incorrect or refers to a nonexistent object, such as a nonexistent index or table.
* The current hints or current parameters are incompatible with the previous ones, such as forcing the use and disabling of the same index.

For example, if a `FORCE_INDEX` hint references an index that does not exist, the following error will be thrown:

```
Hints mentioned indexes "IDX_1", "IDX_2" were not found.
```

## Hint Precedence

When the same table-specific hint type applies to a table from more than one level of a query, the hint closest to the table wins. Same-type hints are overridden, not merged: two `NO_INDEX(...)` lists at different levels are not combined — the inner list replaces the outer one for the affected table.

`NO_INDEX` and `FORCE_INDEX` set on different levels can also override each other. This lets you, for example, disable indexes broadly with a `SELECT`-level `NO_INDEX` and then re-enable a specific index for one table by attaching `FORCE_INDEX` to that table in the `FROM` clause.

Example:

```sql
SELECT /*+ NO_INDEX */ tbl1.val1, tbl2.val1
FROM tbl1 /*+ FORCE_INDEX(idx_val1) */
LEFT JOIN tbl2 ON tbl1.val1 = tbl2.val1;
```

In the example above, `tbl1` is scanned using `idx_val1` because its FROM-clause `FORCE_INDEX` overrides the outer `NO_INDEX`. `tbl2` has no FROM-clause hint, so it inherits the `SELECT`-level `NO_INDEX` and is scanned without an index.

## Supported Hints

### DISABLE_DECORRELATION

Disables optimizations related to subquery decorrelation. By default, the optimizer attempts to decorrelate correlated subqueries into joins for better performance. This hint prevents that optimization.

**Parameters:**

This hint has no parameters.

**Examples:**

```sql
SELECT /*+ DISABLE_DECORRELATION */ (SELECT COUNT(*) FROM t2) FROM t1;

SELECT /*+ DISABLE_DECORRELATION */ * FROM t1 WHERE EXISTS (SELECT 1 FROM t2 WHERE t2.id = t1.id);

SELECT /*+ DISABLE_DECORRELATION */ t1.col1 FROM t1 WHERE t1.col1 < 5 AND EXISTS (SELECT x FROM TABLE(SYSTEM_RANGE(t1.col1, t1.col2)) WHERE MOD(x, 2) = 0);
```

### ENFORCE_JOIN_ORDER

Disables commute joins and enforces the join order defined by the user in a query.

**Parameters:**

This hint has no parameters.

**Examples:**

```sql
SELECT /*+ ENFORCE_JOIN_ORDER */ COUNT(bt.id) FROM big_tbl bt JOIN small_tbl st ON bt.id = st.id;

SELECT /*+ ENFORCE_JOIN_ORDER */ * FROM t1 JOIN t2 USING (id);
```

### EXPAND_DISTINCT_AGG

If specified, the optimizer will rewrite `DISTINCT` aggregates into `GROUP BY` subqueries.

**Parameters:**

This hint has no parameters.

**Examples:**

```sql
SELECT /*+ EXPAND_DISTINCT_AGG */ SUM(DISTINCT val0), SUM(DISTINCT val1) FROM test GROUP BY grp0;

SELECT /*+ EXPAND_DISTINCT_AGG */ COUNT(DISTINCT col1), AVG(DISTINCT col2) FROM tbl;
```

### FORCE_INDEX

Forces index scan.

{% hint style="info" %}
The `FORCE_INDEX` and `NO_INDEX` hints cannot target the same index, but may be used together in a query if they reference different indexes.
{% endhint %}

**Parameters:**

* Single index name to force the use of that specific index.
* Multiple index names. They can relate to different tables. The optimizer will use the specified indexes for scanning.

**Examples:**

```sql
SELECT /*+ FORCE_INDEX(TBL1_IDX2) */ T1.* FROM TBL1 T1 WHERE T1.V1 = ? AND T1.V2 > ?;

SELECT /*+ FORCE_INDEX(TBL1_IDX2, TBL2_IDX1) */ T1.V1, T2.V1 FROM TBL1 T1, TBL2 T2 WHERE T1.V1 = T2.V1 AND T1.V2 > ? AND T2.V2 > ?;

SELECT /*+ NO_INDEX(IDX_VAL1), FORCE_INDEX(IDX_VAL3), NO_INDEX(IDX_VAL2_VAL3) */ * FROM TBL1 WHERE  val1='v'  AND val2='v' AND val3='v';

-- Hint placed in the FROM clause, scoped to TBL1 only:
SELECT * FROM TBL1 /*+ FORCE_INDEX(IDX_VAL2_VAL3) */ WHERE val2 = 'v';
```

### NO_INDEX

Disables index scan.

{% hint style="info" %}
The `FORCE_INDEX` and `NO_INDEX` hints cannot target the same index, but may be used together in a query if they reference different indexes.
{% endhint %}

**Parameters:**

* Empty. Disables all indexes, forcing a table scan.
* Single index name to disable that specific index.
* Multiple index names. They can relate to different tables. The optimizer will avoid using the specified indexes.

**Examples:**

```sql
SELECT /*+ NO_INDEX */ T1.* FROM TBL1 T1 WHERE T1.V1 = ? AND T1.V2 > ?;

SELECT /*+ NO_INDEX(TBL1_IDX2) */ T1.* FROM TBL1 T1 WHERE T1.V1 = ? AND T1.V2 > ?;

SELECT /*+ NO_INDEX(TBL1_IDX2, TBL2_IDX1) */ T1.V1, T2.V1 FROM TBL1 T1, TBL2 T2 WHERE T1.V1 = T2.V1 AND T1.V2 > ? AND T2.V2 > ?;

SELECT /*+ NO_INDEX(IDX_VAL1), FORCE_INDEX(IDX_VAL3), NO_INDEX(IDX_VAL2_VAL3) */ * FROM TBL1 WHERE  val1='v'  AND val2='v' AND val3='v';

-- Hints placed in the FROM clause, scoped to TBL1 only:
SELECT * FROM TBL1 /*+ NO_INDEX */ WHERE id = 0;

SELECT * FROM TBL1 /*+ NO_INDEX(IDX_VAL1, IDX_VAL2_VAL3) */ WHERE val1 = 1;
```

### USE_SECONDARY_STORAGE

Forces the query to use secondary storage instead of primary storage. Secondary storage is used to store a separate copy of data.

{% hint style="info" %}
When data is written to the primary storage, it will automatically be propagated to secondary storage, without the need for using the optimizer hint. Only use the hint to read data from secondary storage.
{% endhint %}

**Parameters:**

This hint has no parameters.

**Examples:**

```sql
SELECT * FROM tbl /*+ USE_SECONDARY_STORAGE */;

SELECT COUNT(*) FROM tbl /*+ USE_SECONDARY_STORAGE */ WHERE col1 > ?;

SELECT SUM(field1) FROM tbl /*+ USE_SECONDARY_STORAGE */;
```
