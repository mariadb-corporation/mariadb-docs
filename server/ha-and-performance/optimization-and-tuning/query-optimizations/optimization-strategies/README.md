---
description: >-
  Discover effective optimization strategies for MariaDB Server queries. This
  section provides a variety of techniques and approaches to enhance query
  performance and overall database efficiency.
---

# Optimization Strategies

{% columns %}
{% column %}
{% content-ref url="duplicateweedout-strategy.md" %}
[duplicateweedout-strategy.md](duplicateweedout-strategy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
DuplicateWeedout is a semi-join execution strategy that runs the subquery as a regular inner join and removes duplicate record combinations using a temporary table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="firstmatch-strategy.md" %}
[firstmatch-strategy.md](firstmatch-strategy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
FirstMatch is a semi-join execution strategy that avoids duplicate results by short-cutting subquery execution as soon as the first matching record is found, improving performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="improvements-to-order-by.md" %}
[improvements-to-order-by.md](improvements-to-order-by.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes MariaDB improvements to the ORDER BY optimizer, including cost- based index switching for ORDER BY with small LIMIT and multiple-equality handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="loosescan-strategy.md" %}
[loosescan-strategy.md](loosescan-strategy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LooseScan is a semi-join execution strategy that avoids duplicate record combinations by using an index on the subquery table to pick one row per group.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="semi-join-materialization-strategy.md" %}
[semi-join-materialization-strategy.md](semi-join-materialization-strategy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Semi-join Materialization runs an uncorrelated IN-subquery into a temporary table, then joins it via the Materialization-scan or Materialization-lookup strategy.
{% endcolumn %}
{% endcolumns %}
