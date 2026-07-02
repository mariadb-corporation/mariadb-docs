---
description: >-
  Optimize subqueries in MariaDB Server for improved performance. This section
  provides techniques and best practices to ensure your nested queries execute
  efficiently and enhance overall query speed.
---

# Subquery Optimizations

{% columns %}
{% column %}
{% content-ref url="condition-pushdown-into-in-subqueries.md" %}
[condition-pushdown-into-in-subqueries.md](condition-pushdown-into-in-subqueries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes Condition Pushdown into IN subqueries, enabled through the condition_pushdown_for_subquery optimizer_switch flag.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="conversion-of-big-in-predicates-into-subqueries.md" %}
[conversion-of-big-in-predicates-into-subqueries.md](conversion-of-big-in-predicates-into-subqueries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Converts large IN predicates into IN subqueries once the list exceeds in_predicate_conversion_threshold elements, avoiding costly range analysis.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="exists-to-in-optimization.md" %}
[exists-to-in-optimization.md](exists-to-in-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
EXISTS-to-IN rewrites trivially correlated and semi-join EXISTS subqueries into IN subqueries so MariaDB's richer IN-subquery strategies can apply.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="non-semi-join-subquery-optimizations.md" %}
[non-semi-join-subquery-optimizations.md](non-semi-join-subquery-optimizations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Covers strategies for IN-subqueries that cannot become semi-joins, chiefly materialization (with NULL-aware partial matching) and the IN-to-EXISTS transformation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizing-group-by.md" %}
[optimizing-group-by.md](optimizing-group-by.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Automatically removes redundant DISTINCT and GROUP BY-without-HAVING clauses in IN/ALL/ANY/SOME/EXISTS subqueries, allowing more efficient query plans.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="semi-join-subquery-optimizations.md" %}
[semi-join-subquery-optimizations.md](semi-join-subquery-optimizations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains semi-join IN-subqueries and MariaDB's five semi-join execution strategies: table pullout, FirstMatch, Materialization, LooseScan, and DuplicateWeedout.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subquery-cache.md" %}
[subquery-cache.md](subquery-cache.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The subquery cache speeds up correlated subqueries by caching results with their correlation parameters, avoiding re-execution when a result is already cached.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subquery-optimizations-map.md" %}
[subquery-optimizations-map.md](subquery-optimizations-map.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Presents a map of the subquery types allowed in SQL and the optimizer strategies MariaDB provides to handle each, with links to individual optimization pages.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-pullout-optimization.md" %}
[table-pullout-optimization.md](table-pullout-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Table pullout rewrites a semi-join subquery as a join by pulling tables out into the parent SELECT based on UNIQUE or PRIMARY key definitions.
{% endcolumn %}
{% endcolumns %}
