# Optimizer Hints

Optimizer hints are options available that affect the execution plan.

## SELECT Modifiers

### HIGH PRIORITY

`HIGH_PRIORITY` gives the statement a higher priority. If the table is locked, high priority `SELECT`s will be executed as soon as the lock is released, even if other statements are queued. `HIGH_PRIORITY` applies only if the storage engine only supports table-level locking (`MyISAM`, `MEMORY`, `MERGE`). See [HIGH\_PRIORITY and LOW\_PRIORITY clauses](../changing-deleting-data/high_priority-and-low_priority.md) for details.

### SQL\_CACHE / SQL\_NO\_CACHE

If the [query\_cache\_type](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) system variable is set to 2 or `DEMAND`, and the current statement is cacheable, `SQL_CACHE` causes the query to be cached and `SQL_NO_CACHE` causes the query not to be cached. For `UNION`s, `SQL_CACHE` or `SQL_NO_CACHE` should be specified for the first query. See also [The Query Cache](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) for more detail and a list of the types of statements that aren't cacheable.

### SQL\_BUFFER\_RESULT

`SQL_BUFFER_RESULT` forces the optimizer to use a temporary table to process the result. This is useful to free locks as soon as possible.

### SQL\_SMALL\_RESULT / SQL\_BIG\_RESULT

`SQL_SMALL_RESULT` and `SQL_BIG_RESULT` tell the optimizer whether the result is very big or not. Usually, `GROUP BY` and `DISTINCT` operations are performed using a temporary table. Only if the result is very big, using a temporary table is not convenient. The optimizer automatically knows if the result is too big, but you can force the optimizer to use a temporary table with `SQL_SMALL_RESULT`, or avoid the temporary table using `SQL_BIG_RESULT`.

### STRAIGHT\_JOIN

`STRAIGHT_JOIN` applies to the [JOIN](joins-subqueries/joins/join-syntax.md) queries, and tells the optimizer that the tables must be read in the order they appear in the `SELECT`. For `const` and `system` table this options is sometimes ignored.

### SQL\_CALC\_FOUND\_ROWS

`SQL_CALC_FOUND_ROWS` is only applied when using the `LIMIT` clause. If this option is used, MariaDB will count how many rows would match the query, without the `LIMIT` clause. That number can be retrieved in the next query, using [FOUND\_ROWS()](../../../sql-functions/secondary-functions/information-functions/found_rows.md).

### USE/FORCE/IGNORE INDEX

`USE INDEX`, `FORCE INDEX` and `IGNORE INDEX` constrain the query planning to a specific index. For further information about some of these options, see [How to force query plans](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/index-hints-how-to-force-query-plans.md).

## Expanded Optimizer Hints

### Syntax

{% tabs %}
{% tab title="Current" %}
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

#### Description

Each individual hint is hint name and arguments. In case there are no arguments,\
the () brackets are still present:

```
hint:  hint_name([arguments])
```

Incorrect hints produce warnings (a setting to make them errors is not implemented yet).\
Hints that are not ignored are kept in the query text (you can see them in SHOW PROCESSLIST, Slow Query Log, EXPLAIN EXTENDED)\
Hints that were incorrect and were ignored are removed from there.

**Hint Hierarchy**

Hints can be

* global - they apply to whole query;
* table-level - they apply to a table;
* index-level - they apply to an index in a table.

**Table-Level Hints**

```sql
hint_name([table_name [table_name [,...]] )
```

**Index-Level Hints**

Index-level hints apply to indexes. Possible syntax variants are:

```sql
hint_name(table_name [index_name [, index_name] ...])

hint_name(table_name@query_block [index_name [, index_name] ...])

hint_name(@query_block  table_name [index_name [, index_name] ...])
```

**Query Block Naming**

The `QB_NAME` hint is used to assign a name to the query block the hint is in. The Query Block is either a `SELECT` or a top-level construct of `UPDATE` or `DELETE` statement.

```sql
SELECT /*+ QB_NAME(foo) */ select_list FROM ...
```

The name can then can be used

* to refer to the query block;
* to refer to a table in the query block as `table_name@query_block_name`.

Query block scope is the whole statement. It is invalid to use the same name for multiple query blocks. You can refer to the query block "down into subquery", "down into derived table", "up to the parent" and "to a right sibling in the UNION". You cannot refer "to a left sibling in a UNION".

Hints inside views are not supported, yet. You can neither use hints in `VIEW` definitions, nor control query plans inside non-merged views. (This is because `QB_NAME` binding are done "early", before we know that some tables are views.)

**SELECT#N NAMES**

Besides the given name, any query block is given a name select#n. You can see it when running `EXPLAIN EXTENDED`:

```sql
Note 1003 SELECT /*+ NO_RANGE_OPTIMIZATION(t3@select#1 PRIMARY) */ ...
```

It is **not** possible to use it in the hint text:

```sql
SELECT /*+ BKA(tbl1@`select#1`) */ 1 FROM tbl1 ...;
```

**QB\_NAME in CTEs**

Hints that control `@name` will control the first use of the CTE (common table expression).

**Effect of Optimizer Hints**

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

#### List of Hints

#### JOIN\_INDEX and NO\_JOIN\_INDEX

An index-level hint that enables or disables the specified indexes for an access method (range, ref, etc.). Equivalent to `FORCE INDEX FOR JOIN` and `IGNORE INDEX FOR JOIN`.

#### GROUP\_INDEX and NO\_GROUP\_INDEX

An index-level hint that enables or disables the specified indexes for index scans for `GROUP BY` operations. Equivalent to `FORCE INDEX FOR GROUP BY` and `IGNORE INDEX FOR GROUP BY`.

#### ORDER\_INDEX and NO\_ORDER\_INDEX

An index-level hint that enables or disables the specified indexes for sorting rows. Equivalent to `FORCE INDEX FOR ORDER BY` and `IGNORE INDEX FOR ORDER BY`.

#### INDEX and NO\_INDEX

An index-level hint that enables or disables the specified indexes, for all scopes (join access method, GROUP BY, or sorting). Equivalent to `FORCE INDEX` and `IGNORE INDEX`.

**NO\_RANGE\_OPTIMIZATION**

An index-level hint that disables range optimization for certain index(es):

```sql
SELECT /*+ NO_RANGE_OPTIMIZATION(tbl index1 index2) */  * FROM tbl ...
```

**NO\_ICP**

An index-level hint that disables [Index Condition Pushdown](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown.md) for the indexes. ICP+BKA is disabled as well.

```sql
SELECT /*+ NO_ICP(tbl index1 index2) */  * FROM tbl ...
```

**MRR and NO\_MRR**

Index-level hints to force or disable use of MRR.

```sql
SELECT /*+ MRR(tbl index1 index2) */  * FROM tbl ... 

SELECT /*+ NO_MRR(tbl index1 index2) */  * FROM tbl ...
```

This controls:

* MRR optimization for range access (mdev35483-mrr-is-narrow.sql);
* BKA mdev35483-mrr-controls-bka-partially.sql.

**BKA() and NO\_BKA()**

Query block or table-level hints.

BKA() also enables MRR to make BKA possible. (This is different from session variables, where you need to enable MRR separately). This also enables BKAH.

**BNL() and NO\_BNL()**

Controls BNL-H.

The implementation is "BNL() hint effectively increases join\_cache\_level up to 4 " .. for the table(s) it applies to.

**MAX\_EXECUTION\_TIME()**

Global-level hint to limit query execution time

```sql
SELECT /*+ MAX_EXECUTION_TIME(milliseconds) */ ...  ;
```

A query that doesn't finish in the time specified will be aborted with an error.\
If `@@max_statement_time` is set, the hint will be ignored and a warning produced. Note that this contradicts the stated principle that "new-style hints are more specific than server variable settings, so they override the server variable settings".

#### SPLIT\_MATERIALIZED(X) and NO\_SPLIT\_MATERIALIZED(X)

Enables or disables the use of the Split Materialized Optimization (also called the[ Lateral Derived Optimization](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/lateral-derived-optimization.md)).

#### DERIVED\_CONDITION\_PUSHDOWN and NO\_DERIVED\_CONDITION\_PUSHDOWN&#x20;

Enables or disables the use of [condition pushdown for derived tables](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/condition-pushdown-into-derived-table-optimization.md).

**Subquery Hints**

**SUBQUERY Hint**

Query block-level hint.

```sql
SUBQUERY([@query_block_name] MATERIALIZATION)

SUBQUERY([@query_block_name] INTOEXISTS)
```

This controls non-semi-join subqueries. The parameter specifies which subquery to use. Use of this hint disables conversion of subquery into semi-join.

**SEMIJOIN and NO\_SEMIJOIN**

Query block-level hints.

This controls the conversion of subqueries to semi-joins and which semi-join strategies are allowed.

```sql
[NO_]SEMIJOIN([@query_block_name] [strategy [, strategy] ...])
```

where the strategy is one of DUPSWEEDOUT, FIRSTMATCH, LOOSESCAN, MATERIALIZATION.
{% endtab %}

{% tab title="<12.1" %}
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

**Description**

Each individual hint is hint name and arguments. In case there are no arguments,\
the () brackets are still present:

```
hint:  hint_name([arguments])
```

Incorrect hints produce warnings (a setting to make them errors is not implemented yet).\
Hints that are not ignored are kept in the query text (you can see them in SHOW PROCESSLIST, Slow Query Log, EXPLAIN EXTENDED)\
Hints that were incorrect and were ignored are removed from there.

**Hint Hierarchy**

Hints can be

* global - they apply to whole query;
* table-level - they apply to a table;
* index-level - they apply to an index in a table.

**Table-Level Hints**

```sql
hint_name([table_name [table_name [,...]] )
```

**Index-Level Hints**

Index-level hints apply to indexes. Possible syntax variants are:

```sql
hint_name(table_name [index_name [, index_name] ...])

hint_name(table_name@query_block [index_name [, index_name] ...])

hint_name(@query_block  table_name [index_name [, index_name] ...])
```

**Query Block Naming**

The `QB_NAME` hint is used to assign a name to the query block the hint is in. The Query Block is either a `SELECT` or a top-level construct of `UPDATE` or `DELETE` statement.

```sql
SELECT /*+ QB_NAME(foo) */ select_list FROM ...
```

The name can then can be used

* to refer to the query block;
* to refer to a table in the query block as `table_name@query_block_name`.

Query block scope is the whole statement. It is invalid to use the same name for multiple query blocks. You can refer to the query block "down into subquery", "down into derived table", "up to the parent" and "to a right sibling in the UNION". You cannot refer "to a left sibling in a UNION".

Hints inside views are not supported, yet. You can neither use hints in `VIEW` definitions, nor control query plans inside non-merged views. (This is because `QB_NAME` binding are done "early", before we know that some tables are views.)

**SELECT#N NAMES**

Besides the given name, any query block is given a name select#n. You can see it when running `EXPLAIN EXTENDED`:

```sql
Note 1003 SELECT /*+ NO_RANGE_OPTIMIZATION(t3@select#1 PRIMARY) */ ...
```

It is **not** possible to use it in the hint text:

```sql
SELECT /*+ BKA(tbl1@`select#1`) */ 1 FROM tbl1 ...;
```

**QB\_NAME in CTEs**

Hints that control `@name` will control the first use of the CTE (common table expression).

**Effect of Optimizer Hints**

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

**List of Hints**

**NO\_RANGE\_OPTIMIZATION**

An index-level hint that disables range optimization for certain index(es):

```sql
SELECT /*+ NO_RANGE_OPTIMIZATION(tbl index1 index2) */  * FROM tbl ...
```

**NO\_ICP**

An index-level hint that disables [Index Condition Pushdown](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown.md) for the indexes. ICP+BKA is disabled as well.

```sql
SELECT /*+ NO_ICP(tbl index1 index2) */  * FROM tbl ...
```

**MRR and NO\_MRR**

Index-level hints to force or disable use of MRR.

```sql
SELECT /*+ MRR(tbl index1 index2) */  * FROM tbl ... 

SELECT /*+ NO_MRR(tbl index1 index2) */  * FROM tbl ...
```

This controls:

* MRR optimization for range access (mdev35483-mrr-is-narrow.sql);
* BKA mdev35483-mrr-controls-bka-partially.sql.

**BKA() and NO\_BKA()**

Query block or table-level hints.

BKA() also enables MRR to make BKA possible. (This is different from session variables, where you need to enable MRR separately). This also enables BKAH.

**BNL() and NO\_BNL()**

Controls BNL-H.

The implementation is "BNL() hint effectively increases join\_cache\_level up to 4 " .. for the table(s) it applies to.

**MAX\_EXECUTION\_TIME()**

Global-level hint to limit query execution time

```sql
SELECT /*+ MAX_EXECUTION_TIME(milliseconds) */ ...  ;
```

A query that doesn't finish in the time specified will be aborted with an error.\
If `@@max_statement_time` is set, the hint will be ignored and a warning produced. Note that this contradicts the stated principle that "new-style hints are more specific than server variable settings, so they override the server variable settings".

**Subquery Hints**

**SUBQUERY Hint**

Query block-level hint.

```sql
SUBQUERY([@query_block_name] MATERIALIZATION)

SUBQUERY([@query_block_name] INTOEXISTS)
```

This controls non-semi-join subqueries. The parameter specifies which subquery to use. Use of this hint disables conversion of subquery into semi-join.

**SEMIJOIN and NO\_SEMIJOIN**

Query block-level hints.

This controls the conversion of subqueries to semi-joins and which semi-join strategies are allowed.

```sql
[NO_]SEMIJOIN([@query_block_name] [strategy [, strategy] ...])
```

where the strategy is one of DUPSWEEDOUT, FIRSTMATCH, LOOSESCAN, MATERIALIZATION.
{% endtab %}

{% tab title="< 12.0" %}
Expanded optimizer hints are not available.
{% endtab %}
{% endtabs %}

## See Also

* [Use optimizer\_switch to enable/disable specific optimizations](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
