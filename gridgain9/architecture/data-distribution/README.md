---
description: >-
  How GridGain 9 distributes data across a cluster — distribution zones, data partitioning, and data colocation.
---

# Data Distribution

{% columns %}
{% column %}
{% content-ref url="../storage/distribution-zones.md" %}
[Distribution Zones](../storage/distribution-zones.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create and configure GridGain 9 distribution zones to control how tables are partitioned, replicated, and distributed across cluster nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../storage/data-partitioning.md" %}
[Data Partitioning](../storage/data-partitioning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 partitions and replicates table data across cluster nodes, including RAFT consensus, the Fair distribution algorithm, and primary replica leases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-colocation.md" %}
[Data Colocation](../data-colocation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to store related data on the same node in GridGain 9 using the COLOCATE BY clause to speed up multi-entry queries.
{% endcolumn %}
{% endcolumns %}
