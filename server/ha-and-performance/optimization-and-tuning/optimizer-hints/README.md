---
description: >-
  This section details special comments you can add to SQL statements to
  influence the query optimizer, helping you manually select better execution
  plans for improved performance and query tuning.
---

# Optimizer Hints

Optimizer hints are options available that affect the execution plan.

[SELECT Modifiers](select-modifier-hints.md) have been in MariaDB for a long time, while [Expanded (New-Style) Optimizer Hints](expanded-optimizer-hints.md) were introduced in MariaDB 12.0 and 12.1.

{% columns %}
{% column %}
{% content-ref url="select-modifier-hints.md" %}
[select-modifier-hints.md](select-modifier-hints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SELECT modifier hints such as HIGH_PRIORITY, SQL_CACHE, SQL_NO_CACHE, and SQL_BUFFER_RESULT that adjust how individual SELECT statements are executed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="expanded-optimizer-hints.md" %}
[expanded-optimizer-hints.md](expanded-optimizer-hints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
New-style optimizer hints (MariaDB 12.0+) that give granular, per-query control over optimizer choices without changing server-wide variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="index-level-hints.md" %}
[index-level-hints.md](index-level-hints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Index-level optimizer hints that tell the optimizer which indexes to use, ignore, or prefer for a given table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query-block-naming.md" %}
[query-block-naming.md](query-block-naming.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Assign names to query blocks with QB_NAME() so optimizer hints can target specific subqueries or statement blocks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-level-hints.md" %}
[table-level-hints.md](table-level-hints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Table-level optimizer hints that influence join order and per-table optimizer behavior, optionally scoped to a named query block.
{% endcolumn %}
{% endcolumns %}

## See Also

* [Use optimizer\_switch to enable/disable specific optimizations](../query-optimizations/optimizer-switch.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
