---
description: >-
  How GridGain 8 works under the hood — its multi-tiered memory and storage,
  clustering and discovery, data distribution, and consistency model.
icon: sitemap
---

# Architecture

GridGain 8 is a distributed, memory-centric platform built on Apache Ignite. This section explains the concepts and internals behind it: how data is stored across memory and disk, how nodes form a cluster and discover each other, how data is partitioned and rebalanced, and how GridGain keeps data consistent. Understand these before configuring and operating a cluster.

## The Big Picture

GridGain 8 and GridGain 9 share the same architecture at the level of ideas. What differs between the two versions is how each idea is implemented.

- **Distributed cluster.** GridGain runs as a cluster of server nodes that together store and process data. Applications work with the cluster through clients and drivers.
- **In memory and on disk.** Data can be kept entirely in memory or persisted to disk, combining in-memory speed with disk durability.
- **B+ tree storage.** GridGain stores data in memory pages and organizes its indexes as B+ trees.
- **Hash partitioning.** Each table or cache is split into partitions. A hash of a record's key determines its partition, and the partitions are spread across the nodes of the cluster.
- **Distributed copies.** Each partition can be stored on several nodes, so data stays available when a node fails.
- **Data colocation.** Related records that share a colocation key are stored on the same node, so queries and computations over them run locally.
- **SQL, key-value, and compute.** You can work with the same data through SQL or a key-value API, and send computations to the nodes that hold the data.

## How GridGain 8 Implements It

| Concept | GridGain 8 | Read more |
| --- | --- | --- |
| Cluster membership and lifecycle | Nodes find each other through node discovery. A cluster must be activated before it runs workloads, and the baseline topology defines the nodes that store persistent data. | [Clustering](clustering.md), [Baseline Topology](baseline-topology.md) |
| Memory and persistence | A multi-tiered, page-based memory architecture organized into data regions, with Native Persistence (checkpointing and write-ahead log) for durability. | [Memory Architecture](memory-architecture.md), [Native Persistence](storage/native-persistence.md) |
| Partitioning | The affinity function maps keys to partitions using rendezvous hashing. Caches run in partitioned or replicated mode. | [Data Partitioning](data-modeling/data-partitioning.md) |
| Copies and consistency | Backup partitions hold copies of each partition. Partition map exchange (PME) and rebalancing redistribute partitions when the topology changes. | [Backup Partitions](data-modeling/data-partitioning.md#backup-partitions), [Data Rebalancing](rebalancing/data-rebalancing.md) |
| Colocation | The affinity key. | [Affinity Colocation](data-modeling/affinity-colocation.md) |
| SQL engine | H2 parses and optimizes queries and generates execution plans. | [Introduction to SQL](../gridgain8-development/sql/sql-introduction.md) |

## Architecture Topics

{% columns %}
{% column %}
{% content-ref url="cluster/" %}
[Cluster](cluster/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 8 nodes discover each other and form a cluster, how activation and baseline topology control the cluster lifecycle, and how the cluster protects itself from split-brain.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-distribution/" %}
[Data Distribution](data-distribution/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How data is distributed and represented in a GridGain cluster, covering data partitioning, affinity colocation, and the key-value and SQL access models.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-and-consistency/" %}
[Replication and Consistency](replication-and-consistency/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain keeps partition copies balanced and available as the cluster topology changes — full and historical rebalancing, and partition loss handling.
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
{% content-ref url="storage/" %}
[Storage](storage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain's storage architecture — the multi-tiered memory architecture, native persistence for durable on-disk storage, and swapping as an extension of memory.
{% endcolumn %}
{% endcolumns %}
