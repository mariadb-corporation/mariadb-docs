---
description: MariaDB has pseudo columns that can be used for different purposes.
---

# Pseudo Columns

{% columns %}
{% column %}
{% content-ref url="_rowid.md" %}
[_rowid.md](_rowid.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Access the unique row identifier. This pseudo column often aliases the primary key, allowing direct row access even if the primary key column name is unknown.
{% endcolumn %}
{% endcolumns %}
