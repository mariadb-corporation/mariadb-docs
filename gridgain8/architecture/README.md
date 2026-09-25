---
description: >-
  How GridGain 8 works under the hood — its multi-tiered memory and storage,
  clustering and discovery, data distribution, and consistency model.
icon: sitemap
---

# Architecture

GridGain 8 is a distributed, memory-centric platform built on Apache Ignite. This section explains the concepts and internals behind it: how data is stored across memory and disk, how nodes form a cluster and discover each other, how data is partitioned and rebalanced, and how GridGain keeps data consistent. Understand these before configuring and operating a cluster.

{% columns %}
{% column %}
{% content-ref url="memory-architecture.md" %}
[memory-architecture](memory-architecture.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% content-ref url="storage/" %}
[storage](storage/)
{% endcontent-ref %}
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="clustering.md" %}
[clustering](clustering.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% content-ref url="baseline-topology.md" %}
[baseline-topology](baseline-topology.md)
{% endcontent-ref %}
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-modeling/" %}
[data-modeling](data-modeling/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% content-ref url="rebalancing/" %}
[rebalancing](rebalancing/)
{% endcontent-ref %}
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mvcc.md" %}
[mvcc](mvcc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
{% content-ref url="split-brain-protection.md" %}
[split-brain-protection](split-brain-protection.md)
{% endcontent-ref %}
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
