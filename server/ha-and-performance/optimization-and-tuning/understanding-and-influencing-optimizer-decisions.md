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

## See also

* [Query Optimizer](query-optimizer/README.md) — internals of how the optimizer works
* [The Optimizer Cost Model from MariaDB 11.0](query-optimizer/the-optimizer-cost-model-from-mariadb-11-0.md)
