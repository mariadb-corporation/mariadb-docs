---
description: >-
  Optimize derived tables in MariaDB Server queries. This section provides
  techniques and strategies to improve the performance of subqueries and complex
  joins, enhancing overall query efficiency.
---

# Optimizations for Derived Tables

{% columns %}
{% column %}
{% content-ref url="condition-pushdown-into-derived-table-optimization.md" %}
[condition-pushdown-into-derived-table-optimization.md](condition-pushdown-into-derived-table-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Condition Pushdown pushes a parent query's conditions into a derived table or view that cannot be merged, letting the optimizer build efficient access paths.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="derived-table-merge-optimization.md" %}
[derived-table-merge-optimization.md](derived-table-merge-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Derived Table Merge folds a FROM-clause subquery or view into its parent SELECT when it has no grouping, aggregates, or ORDER BY ... LIMIT, avoiding a temporary table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="derived-table-with-key-optimization.md" %}
[derived-table-with-key-optimization.md](derived-table-with-key-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Derived Table with Key lets a materialized derived table have one index that the optimizer uses for joins with other tables instead of a full table scan.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="lateral-derived-optimization.md" %}
[lateral-derived-optimization.md](lateral-derived-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents Lateral Derived Optimization, also referred to as Split Grouping Optimization or Split Materialized Optimization.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="split-materialized-optimization.md" %}
[split-materialized-optimization.md](split-materialized-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Split Materialized Optimization is another name for the Lateral Derived optimization.
{% endcolumn %}
{% endcolumns %}
