---
description: >-
  Explore MariaDB Server's internal optimizations. This section delves into how
  the database engine enhances query execution, data storage, and overall
  performance through its core architecture.
---

# MariaDB Internal Optimizations

{% columns %}
{% column %}
{% content-ref url="fair-choice-between-range-and-index_merge-optimizations.md" %}
[fair-choice-between-range-and-index_merge-optimizations.md](fair-choice-between-range-and-index_merge-optimizations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the optimizer chooses fairly between the range and index_merge access methods.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="multi-range-read-optimization.md" %}
[multi-range-read-optimization.md](multi-range-read-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Multi-Range Read (MRR) optimization, which improves performance for I/O-bound queries scanning many rows.
{% endcolumn %}
{% endcolumns %}
