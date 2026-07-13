---
description: >-
  Worked MariaDB Connector/C prepared-statement examples, including bulk inserts
  with column-wise and row-wise parameter binding.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Prepared Statement Examples

{% columns %}
{% column %}
{% content-ref url="bulk-insert-column-wise-binding.md" %}
[bulk-insert-column-wise-binding.md](bulk-insert-column-wise-binding.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Insert multiple rows in a single prepared-statement call using column-wise binding, demonstrating indicator variables and `STMT_ATTR_ARRAY_SIZE`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bulk-insert-row-wise-binding.md" %}
[bulk-insert-row-wise-binding.md](bulk-insert-row-wise-binding.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Insert multiple rows in a single prepared-statement call using row-wise binding, packing parameters into a C struct and setting `STMT_ATTR_ROW_SIZE`.
{% endcolumn %}
{% endcolumns %}
