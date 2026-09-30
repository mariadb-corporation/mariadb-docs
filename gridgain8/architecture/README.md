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
[Memory Architecture](memory-architecture.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain's multi-tiered, page-based memory architecture that stores data and indexes both in memory and on disk for in-memory speed with disk durability.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="clustering.md" %}
[Clustering](clustering.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain nodes discover each other to form a cluster, the difference between server, client, and thin clients, and how a cluster is activated.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="baseline-topology.md" %}
[Baseline Topology](baseline-topology.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The baseline topology is the set of server nodes that hold data and controls when data rebalancing happens, either manually or through autoadjustment.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-modeling/" %}
[Data Modeling](data-modeling/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How data is distributed and represented in a GridGain cluster, covering data partitioning, affinity colocation, and the key-value and SQL access models.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rebalancing/" %}
[Rebalancing](rebalancing/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain redistributes partitions across nodes as the cluster topology changes — full and historical rebalancing, and partition loss handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="storage/" %}
[Storage](storage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain's storage options for keeping data beyond RAM, including native persistence for durable on-disk storage and swapping as an extension of memory.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mvcc.md" %}
[Multiversion Concurrency Control](mvcc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Multiversion concurrency control (MVCC) in GridGain 8, enabled through the TRANSACTIONAL_SNAPSHOT atomicity mode, its limitations, and how to use it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="split-brain-protection.md" %}
[Split-Brain Protection](split-brain-protection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain helps you detect and mitigate network segmentation (the split-brain problem) using the Topology Validator and SegmentationResolver APIs.
{% endcolumn %}
{% endcolumns %}
