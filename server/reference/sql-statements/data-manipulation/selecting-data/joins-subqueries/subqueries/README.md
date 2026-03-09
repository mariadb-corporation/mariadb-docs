---
description: >-
  Nest queries within other SQL statements. Learn to use scalar, column, row,
  and table subqueries to filter or calculate data dynamically.
---

# Subqueries

{% columns %}
{% column %}
{% content-ref url="subqueries-and-all.md" %}
[subqueries-and-all.md](subqueries-and-all.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compare a value against all results from a subquery. The `ALL` operator returns `TRUE` if the comparison holds for every row returned by the subquery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subqueries-and-any.md" %}
[subqueries-and-any.md](subqueries-and-any.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compare a value against any result from a subquery. The `ANY` (or `SOME`) operator returns `TRUE` if the comparison holds for at least one row. `IN` can be used for `=ANY`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subqueries-and-exists.md" %}
[subqueries-and-exists.md](subqueries-and-exists.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Test for the existence of rows. The `EXISTS` operator returns `TRUE` if the subquery returns at least one row, often used for correlated subqueries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subqueries-and-joins.md" %}
[subqueries-and-joins.md](subqueries-and-joins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand when to use subqueries versus joins. This guide explains performance implications and how to rewrite subqueries as joins for efficiency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subqueries-in-a-from-clause-derived-tables.md" %}
[subqueries-in-a-from-clause-derived-tables.md](subqueries-in-a-from-clause-derived-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use a subquery as a temporary table. Derived tables allow you to select from the result set of another query within the `FROM` clause.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subqueries-row-subqueries.md" %}
[subqueries-row-subqueries.md](subqueries-row-subqueries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Retrieve a single row of multiple values. A row subquery returns a tuple that can be compared against a row constructor in the outer query.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subqueries-scalar-subqueries.md" %}
[subqueries-scalar-subqueries.md](subqueries-scalar-subqueries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return a single value. A scalar subquery produces a one-row, one-column result that can be used anywhere a constant or expression is valid.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subquery-limitations.md" %}
[subquery-limitations.md](subquery-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Review restrictions on subquery usage. This page details unsupported operations, such as modifying a table while selecting from it in a subquery.
{% endcolumn %}
{% endcolumns %}
