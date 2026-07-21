---
description: >-
  See which execution plan the MariaDB query optimizer chose, understand why,
  and influence it — using EXPLAIN, ANALYZE, optimizer trace, and hints.
icon: route
---

# Understanding and Influencing Optimizer Decisions

For every query, the MariaDB query optimizer chooses an execution plan: the
order in which to join tables, which index (if any) to use for each table, and
which optimization strategies to apply. When a query is slower than expected,
the questions are usually: *which plan did the optimizer choose?*, *why did it
choose that plan?*, and *how do I steer it toward a better one?*

MariaDB provides tools that answer these questions in increasing order of
detail. A typical investigation moves through them in sequence.

## 1. See the plan: EXPLAIN

`EXPLAIN` shows the plan the optimizer *intends* to use, without running the
query. It reports the join order, the access method chosen for each table (the
`type` column), the index used (`key`), and the estimated number of rows
examined (`rows`).

{% content-ref url="../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md" %}
[explain.md](../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md)
{% endcontent-ref %}

For a machine-readable plan that also includes cost estimates and the
conditions attached to each table, use `EXPLAIN FORMAT=JSON`.

{% content-ref url="../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain-format-json.md" %}
[explain-format-json.md](../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain-format-json.md)
{% endcontent-ref %}

## 2. Validate the estimates: ANALYZE

The row counts in `EXPLAIN` output are *estimates*. `ANALYZE` runs the query and
reports the actual figures next to the estimates — most importantly `r_rows`
(rows actually read) and `r_filtered` (the percentage of rows that actually
passed the filter). A large gap between the estimated `rows`/`filtered` and the
actual `r_rows`/`r_filtered` is the clearest sign that the optimizer worked from
inaccurate statistics, which is a common cause of a poor plan.

{% content-ref url="../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement.md" %}
[analyze-statement.md](../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement.md)
{% endcontent-ref %}

{% hint style="info" %}
To inspect the plan of a query that is already running in another session, use
[SHOW EXPLAIN](../../reference/sql-statements/administrative-sql-statements/show/show-explain.md).
{% endhint %}

## 3. See why: optimizer trace

Where `EXPLAIN` and `ANALYZE` show *what* the optimizer did, the optimizer trace
records *why*: the alternative plans it considered, the cost it assigned to each,
and the ones it rejected. Enable it for the session, run the query, then read the
JSON trace from `INFORMATION_SCHEMA.OPTIMIZER_TRACE`:

```sql
SET optimizer_trace = 'enabled=on';
SELECT ...;                                    -- the query to investigate
SELECT * FROM INFORMATION_SCHEMA.OPTIMIZER_TRACE\G
SET optimizer_trace = 'enabled=off';
```

{% content-ref url="query-optimizer/optimizer-trace/optimizer-trace-overview.md" %}
[optimizer-trace-overview.md](query-optimizer/optimizer-trace/optimizer-trace-overview.md)
{% endcontent-ref %}

## 4. Influence the plan

Once you understand the plan, two mechanisms let you change it:

* **Optimizer hints** — `/*+ ... */` comments placed in the query that steer the
  optimizer for that single statement (for example, forcing or forbidding a join
  strategy or an index) without changing server-wide behavior. A hint overrides
  the corresponding `optimizer_switch` setting for that query.
* **`optimizer_switch`** — a system variable that enables or disables individual
  optimizations globally or for the session.

Prefer hints when targeting one problem query; use `optimizer_switch` when you
need to change behavior across the workload.

{% content-ref url="optimizer-hints/README.md" %}
[README.md](optimizer-hints/README.md)
{% endcontent-ref %}

{% content-ref url="query-optimizations/optimizer-switch.md" %}
[optimizer-switch.md](query-optimizations/optimizer-switch.md)
{% endcontent-ref %}

## Queries pushed down to a smart storage engine

Some engines — MariaDB ColumnStore is the main example — can execute an entire
`SELECT` themselves rather than returning rows for the server to join, filter,
and sort. An engine advertises this by providing a *select handler*. When the
whole statement is handed off this way, the roles change:

* **The server still parses and prepares the statement.** Name and column
  resolution happen as usual, before the server looks for an engine that can
  take the query. Only a top-level `SELECT` is eligible for full pushdown — a
  subquery is not pushed down on its own.
* **The engine decides whether it can run the query.** The server walks the
  query's tables looking for one whose engine offers a select handler, then asks
  that engine to accept the statement. Checking that the query is something the
  engine can actually execute — for example, that it does not mix tables from
  different engines — is the engine's responsibility, not the server's.
* **The server's cost-based optimizer is bypassed.** Once an engine accepts the
  query, the server does not perform its usual join-order search, index
  selection, or optimization-strategy selection. Deciding how to execute the
  query — and producing the rows — is entirely the engine's own planner. The
  server simply streams back the result.

Because there is no server-side plan for a pushed-down query, the tracing tools
above behave differently:

{% hint style="info" %}
For a fully pushed-down statement, `EXPLAIN` reports `PUSHED SELECT` (or
`PUSHED DERIVED` for a pushed-down derived table) instead of a normal plan, and
optimizer trace, optimizer hints, and `optimizer_switch` do not apply to the
pushed-down part — there is no server-side plan for them to describe or change.
To understand or tune how such a query runs, use the engine's own tooling and
documentation.
{% endhint %}

In a `UNION`, pushdown can be *partial*: branches that an engine can run are
pushed down, while the remaining branches are executed by the server.

## See also

* [Query Optimizer](query-optimizer/README.md) — internals of how the optimizer works
* [The Optimizer Cost Model from MariaDB 11.0](query-optimizer/the-optimizer-cost-model-from-mariadb-11-0.md)
