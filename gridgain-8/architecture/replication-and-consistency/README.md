---
description: >-
  How GridGain keeps partition copies balanced and available as the cluster
  topology changes — full and historical rebalancing, and partition loss handling.
---

# Replication and Consistency

When nodes join or leave the cluster, GridGain moves partitions between nodes to keep data balanced and available. This section covers how rebalancing works, the faster history-based variant, and what happens when partitions are lost.

{% columns %}
{% column %}
{% content-ref url="../rebalancing/data-rebalancing.md" %}
[Data Rebalancing](../rebalancing/data-rebalancing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain redistributes partitions across nodes to keep data balanced, including rebalancing modes, thread pool, message throttling, and monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../rebalancing/historical-rebalancing.md" %}
[Historical Rebalancing](../rebalancing/historical-rebalancing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How historical rebalancing transfers only the WAL delta accumulated while a persistent node was offline, its requirements, sizing, and configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../rebalancing/partition-loss-policy.md" %}
[Partition Loss Policy](../rebalancing/partition-loss-policy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain handles lost partitions through partition loss policies, how to listen for loss events, reset lost partitions, and recover in each cluster type.
{% endcolumn %}
{% endcolumns %}
