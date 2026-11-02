---
description: >-
  How GridGain 9 replicates partitions and keeps data consistent — consistency guarantees, RAFT replication, and high availability mode.
---

# Replication and Consistency

{% columns %}
{% column %}
{% content-ref url="../data-consistency-and-replication.md" %}
[Data Consistency and Replication](../data-consistency-and-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 maintains data consistency through RAFT replication and consensus, the guarantees it provides, and how the cluster behaves during node and network failures.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../high-availability-mode.md" %}
[High Availability Mode](../high-availability-mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure high availability mode on GridGain 9 distribution zones to prioritize partition availability over strict consistency, enabling automatic recovery from majority replica loss.
{% endcolumn %}
{% endcolumns %}
