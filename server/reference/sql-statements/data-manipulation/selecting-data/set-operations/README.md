---
description: >-
  SQL set operations combine the results of multiple query blocks in a single
  result, using the standard SQL operators EXCEPT, INTERSECT, and UNION, and the
  Oracle operator MINUS.
---

# Set Operations

{% columns %}
{% column %}
{% content-ref url="precedence-control-in-table-operations.md" %}
[precedence-control-in-table-operations.md](precedence-control-in-table-operations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control the execution order of UNION, EXCEPT, and INTERSECT operations. Learn how to use parentheses to define explicit operation priority.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="except.md" %}
[except.md](except.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return rows from the first result set that do not appear in the second. This set operator performs a subtraction of two datasets.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="intersect.md" %}
[intersect.md](intersect.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return only the rows that appear in both result sets. INTERSECT implicitly applies DISTINCT and follows the same column-naming, ORDER BY, and LIMIT rules as UNION.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="minus.md" %}
[minus.md](minus.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Oracle-compatible synonym for the EXCEPT operator. It returns rows from the first query that are not present in the second query.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="union.md" %}
[union.md](union.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Combine results from multiple SELECT statements into a single result set. This operator can optionally remove duplicates or include all rows.
{% endcolumn %}
{% endcolumns %}
