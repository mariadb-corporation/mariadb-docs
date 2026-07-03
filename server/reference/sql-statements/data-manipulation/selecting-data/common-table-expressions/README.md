---
description: >-
  Learn about Common Table Expressions (CTEs) in MariaDB Server. This section
  explains how to use CTEs for complex, readable, and reusable subqueries,
  simplifying data selection and manipulation.
---

# Common Table Expressions (CTE)

{% columns %}
{% column %}
{% content-ref url="recursive-common-table-expressions-overview.md" %}
[recursive-common-table-expressions-overview.md](recursive-common-table-expressions-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Process hierarchical data using recursive CTEs. These expressions reference themselves to repeatedly execute a subquery, perfect for traversing tree structures or generating sequences.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="non-recursive-common-table-expressions-overview.md" %}
[non-recursive-common-table-expressions-overview.md](non-recursive-common-table-expressions-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define simple temporary result sets. Non-recursive CTEs act like query-local views, improving readability by allowing you to define and reuse subqueries within a single statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="with.md" %}
[with.md](with.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete WITH clause reference: WITH [RECURSIVE] AS (SELECT...) syntax, recursive CTE support, CYCLE...RESTRICT cycle detection, and max_recursive_iterations.
{% endcolumn %}
{% endcolumns %}
