---
description: >-
  Delve into the MariaDB Server query optimizer. This section provides internal
  documentation on how queries are parsed, optimized, and executed for maximum
  efficiency and performance.
---

# Query Optimizer

{% columns %}
{% column %}
{% content-ref url="block-based-join-algorithms.md" %}
[block-based-join-algorithms.md](block-based-join-algorithms.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Block-based join algorithms in MariaDB: Block Nested Loop, Block Hash Join, and Batch Key Access.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="condition-selectivity-computation-internals.md" %}
[condition-selectivity-computation-internals.md](condition-selectivity-computation-internals.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the optimizer computes condition selectivities (internals).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="extended-keys.md" %}
[extended-keys.md](extended-keys.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Extended Keys optimization, which uses primary-key parts appended to secondary indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="minmax-optimization.md" %}
[minmax-optimization.md](minmax-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MIN/MAX optimization, which resolves MIN() and MAX() from an index without scanning rows.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="notes-when-an-index-cannot-be-used.md" %}
[notes-when-an-index-cannot-be-used.md](notes-when-an-index-cannot-be-used.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Situations in which the optimizer cannot use an index.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-debugging-with-gdb.md" %}
[optimizer-debugging-with-gdb.md](optimizer-debugging-with-gdb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tips for debugging MariaDB optimizer code with GDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-development.md" %}
[optimizer-development.md](optimizer-development.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Notes on MariaDB optimizer development.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer_max_sel_arg_weight.md" %}
[optimizer_max_sel_arg_weight.md](optimizer_max_sel_arg_weight.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The optimizer_max_sel_arg_weight setting, which caps the complexity of range analysis.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="range-optimizer.md" %}
[range-optimizer.md](range-optimizer.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The range optimizer, which builds range scans from WHERE conditions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="the-optimizer-cost-model-from-mariadb-11-0.md" %}
[the-optimizer-cost-model-from-mariadb-11-0.md](the-optimizer-cost-model-from-mariadb-11-0.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The optimizer cost model introduced in MariaDB 11.0.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-trace/" %}
[optimizer-trace](optimizer-trace/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimizer trace, which records how the optimizer builds a query's execution plan.
{% endcolumn %}
{% endcolumns %}
