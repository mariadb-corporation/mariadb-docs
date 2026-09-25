---
description: >-
  How GridGain redistributes partitions across nodes as the cluster topology
  changes — full and historical rebalancing, and partition loss handling.
icon: arrows-rotate
---

# Rebalancing

When nodes join or leave the cluster, GridGain moves partitions between nodes to keep data balanced and available. This section covers how rebalancing works, the faster history-based variant, and what happens when partitions are lost.

{% columns %}
{% column %}
{% content-ref url="data-rebalancing.md" %}
[data-rebalancing](data-rebalancing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% content-ref url="historical-rebalancing.md" %}
[historical-rebalancing](historical-rebalancing.md)
{% endcontent-ref %}
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partition-loss-policy.md" %}
[partition-loss-policy](partition-loss-policy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
