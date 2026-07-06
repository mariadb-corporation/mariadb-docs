---
description: >-
  Using LIMIT ROWS EXAMINED to cap how many rows a query examines.
---

# LIMIT ROWS EXAMINED

## Syntax

```bnf
SELECT ... FROM ... WHERE ...
[group_clause] [order_clause]
LIMIT [[OFFSET,] row_count] ROWS EXAMINED rows_limit;
```

Similar to the parameters of `LIMIT`, _`rows_limit`_ can be both a prepared statement parameter, or a stored program parameter.

## Description

The purpose of this optimization is to provide the means to terminate the execution of [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements which examine too many rows, and thus use too many resources. This is achieved through an extension of the [LIMIT](../../../reference/sql-statements/data-manipulation/selecting-data/limit.md) clause —`LIMIT ROWS EXAMINED number_of_rows`. Whenever possible the semantics of `LIMIT ROWS EXAMINED` is the same as that of normal `LIMIT` (for instance for aggregate functions).

The `LIMIT ROWS EXAMINED` clause is taken into account by the query engine only during query execution. Thus the clause is ignored in the following cases:

* If a query is [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md)-ed.
* During query optimization.
* During auxiliary operations such as writing to system tables (e.g. logs).

The clause is not applicable to [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) or [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) statements, and if used in those statements produces a syntax error.

The effects of this clause are as follows:

* The server counts the number of read, inserted, modified, and deleted rows during query execution. This takes into account the use of temporary tables, and sorting for intermediate query operations.
* Once the counter exceeds the value specified in the LIMIT ROWS EXAMINED clause, query execution is terminated as soon as possible.
* The effects of terminating the query because of LIMIT ROWS EXAMINED are as follows:
  * The result of the query is a subset of the complete query, depending on when the query engine detected that the limit was reached. The result may be empty if no result rows could be computed before reaching the limit.
  * A warning is generated of the form: "Query execution was interrupted. The query examined at least 100 rows, which exceeds LIMIT ROWS EXAMINED (20). The query result may be incomplete."
  * If query processing was interrupted during filesort, an error is returned in addition to the warning.
  * If a UNION was interrupted during execution of one of its queries, the last step of the UNION is still executed in order to produce a partial result.
  * Depending on the join and other execution strategies used for a query, the same query may produce no result at all, or a different subset of the complete result when terminated due to LIMIT ROWS EXAMINED.
  * If the query contains a GROUP BY clause, the last group where the limit was reached will be discarded.

The `LIMIT ROWS EXAMINED` clause cannot be specified on a per-subquery basis. There can be only one `LIMIT ROWS EXAMINED` clause for the whole `SELECT` statement. If a `SELECT` statement contains several subqueries with `LIMIT ROWS EXAMINED`, the one that is parsed last is taken into\
account.

## Examples

A simple example of the clause is:

```sql
SELECT * FROM t1, t2 LIMIT 10 ROWS EXAMINED 10000;
```

The `LIMIT ROWS EXAMINED` clause is global for the whole statement.

If a composite query (such as `UNION`, or query with derived tables or with subqueries) contains more than one `LIMIT ROWS EXAMINED`, the last one parsed is taken into account. In this manner either the last or the outermost one is taken into account. For instance, in the query:

```sql
SELECT * FROM t1
WHERE c1 IN (SELECT * FROM t2 WHERE c2 > ' ' LIMIT ROWS EXAMINED 0)
LIMIT ROWS EXAMINED 11;
```

The limit that is taken into account is 11, not 0.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
