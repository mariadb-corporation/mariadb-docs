---
description: >-
  How data is distributed and represented in a GridGain cluster, covering data
  partitioning, affinity colocation, and the key-value and SQL access models.
---

# Data Distribution

This section explains how GridGain distributes and represents data across a cluster. It covers the physical organization of data through [data partitioning](../data-modeling/data-partitioning.md) and [affinity colocation](../data-modeling/affinity-colocation.md), as well as the two logical representations of data — the key-value cache and SQL tables — described in the [Data Modeling introduction](../data-modeling/introduction.md).

{% columns %}
{% column %}
{% content-ref url="../data-modeling/introduction.md" %}
[Introduction](../data-modeling/introduction.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How data is stored and accessed in GridGain, contrasting the physical partitioned layout with the equivalent key-value cache and SQL table views.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-modeling/data-partitioning.md" %}
[Data Partitioning](../data-modeling/data-partitioning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain partitions data across server nodes with the affinity function, the partitioned and replicated cache modes, backups, and partition map exchange.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-modeling/affinity-colocation.md" %}
[Affinity Colocation](../data-modeling/affinity-colocation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How affinity colocation stores related cache entries together on the same node so multi-entry queries run locally, and how to configure a custom affinity key.
{% endcolumn %}
{% endcolumns %}
