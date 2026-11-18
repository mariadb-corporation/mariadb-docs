---
description: >-
  Techniques for analyzing and improving GridGain 9 SQL query performance:
  the EXPLAIN command, performance tips, and SQL statistics.
---

# SQL Tuning

Analyze and improve the performance of your GridGain 9 SQL queries.

* [How to Improve Queries With EXPLAIN Command](using-explain.md) — read query execution plans, diagnose common performance issues, and tune your queries.
* [SQL Performance Tips](sql-performance-tips.md) — batch statements, avoid slow correlated subqueries, time requests, and drop cached plans.
* [SQL Statistics](sql-statistics.md) — define, collect, and monitor the statistics that the optimizer uses to select query plans.
* [Improving Query Plans With Statistics](statistics-tutorial.md) — collect statistics on a TPC-H data set, measure the effect on query time, and choose column groups.

{% columns %}
{% column %}
{% content-ref url="using-explain.md" %}
[Improving Queries with EXPLAIN](using-explain.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to use the GridGain 9 SQL EXPLAIN command to read query execution plans, diagnose common performance issues, and improve query performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-performance-tips.md" %}
[SQL Performance Tips](sql-performance-tips.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Ways to improve GridGain 9 SQL performance: batching statements, avoiding slow correlated subqueries, timing requests in the CLI, and dropping cached plans.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-statistics.md" %}
[SQL Statistics](sql-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 collects and uses SQL statistics: statistics objects, column groups, manual refresh, system views, configuration, and permissions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="statistics-tutorial.md" %}
[Improving Query Plans With Statistics](statistics-tutorial.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tutorial that shows how to collect SQL statistics in GridGain 9 on a TPC-H data set, measure the effect on query time, and choose column groups.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
