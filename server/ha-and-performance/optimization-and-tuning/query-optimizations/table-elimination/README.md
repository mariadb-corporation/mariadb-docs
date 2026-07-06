---
description: >-
  Learn about table elimination for query optimization in MariaDB Server. This
  section explains how the optimizer removes unnecessary tables from query
  plans, improving performance.
---

# Table Elimination

{% columns %}
{% column %}
{% content-ref url="table-elimination-external-resources.md" %}
[table-elimination-external-resources.md](table-elimination-external-resources.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Links to external resources demonstrating table elimination in MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-elimination-in-mariadb.md" %}
[table-elimination-in-mariadb.md](table-elimination-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Shows how the MariaDB table elimination module merges a view and removes outer-joined tables that are guaranteed a single match and unused elsewhere in the query.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-elimination-in-other-databases.md" %}
[table-elimination-in-other-databases.md](table-elimination-in-other-databases.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compares table elimination support in Microsoft SQL Server 2005/2008 and Oracle 11g, noting SQL Server's more advanced handling of subselect join conditions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-elimination-user-interface.md" %}
[table-elimination-user-interface.md](table-elimination-user-interface.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Shows how to confirm table elimination by inspecting EXPLAIN output for absent tables, and notes the debug-build table_elimination switch.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="what-is-table-elimination.md" %}
[what-is-table-elimination.md](what-is-table-elimination.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduces table elimination, which resolves a query without accessing some referenced tables, using an Anchor Modeling actors example to show when it applies.
{% endcolumn %}
{% endcolumns %}
