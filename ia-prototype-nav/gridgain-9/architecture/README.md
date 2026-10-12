---
description: >-
  How GridGain 9 is built: cluster architecture, consensus, data distribution,
  consistency, availability, and storage.
icon: house-blank
---

# Architecture

This section explains how GridGain 9 works internally — the concepts you need to reason about performance, availability, and data placement. It is background reading rather than task instructions; for operational procedures, see [Cluster Management](../gridgain9-management/README.md).

Start with [Cluster Architecture]({gridgain9}/architecture/cluster-architecture) for an end-to-end overview of the node components and how a request flows through the system, then explore the individual topics below.

## The Big Picture

GridGain 8 and GridGain 9 share the same architecture at the level of ideas. What differs between the two versions is how each idea is implemented.

- **Distributed cluster.** GridGain runs as a cluster of server nodes that together store and process data. Applications work with the cluster through clients and drivers.
- **In memory and on disk.** Data can be kept entirely in memory or persisted to disk, combining in-memory speed with disk durability.
- **B+ tree storage.** GridGain stores data in memory pages and organizes its indexes as B+ trees.
- **Hash partitioning.** Each table or cache is split into partitions. A hash of a record's key determines its partition, and the partitions are spread across the nodes of the cluster.
- **Distributed copies.** Each partition can be stored on several nodes, so data stays available when a node fails.
- **Data colocation.** Related records that share a colocation key are stored on the same node, so queries and computations over them run locally.
- **SQL, key-value, and compute.** You can work with the same data through SQL or a key-value API, and send computations to the nodes that hold the data.

## How GridGain 9 Implements It

| Concept | GridGain 9 | Read more |
| --- | --- | --- |
| Cluster membership and lifecycle | A new cluster is initialized once with `cluster init`. The cluster management group (CMG) and the metastorage are RAFT groups that manage topology and cluster metadata. | [Cluster Lifecycle]({gridgain9}/architecture/cluster-lifecycle), [Cluster Fault Tolerance]({gridgain9}/architecture/cluster-fault-tolerance) |
| Memory and persistence | Storage engines, selected through storage profiles: aimem (in-memory page memory), aipersist (persistent page memory), RocksDB, and columnar storage. | [Storage Engines]({gridgain9}/architecture/storage/engines), [Storage Profiles]({gridgain9}/architecture/storage/storage-profiles) |
| Partitioning | Each table belongs to a distribution zone that sets its number of partitions. A hash of the colocation key selects the partition, and the Fair distribution algorithm assigns partitions to nodes. | [Data Partitioning]({gridgain9}/architecture/storage/data-partitioning), [Distribution Zones]({gridgain9}/architecture/storage/distribution-zones) |
| Copies and consistency | Each partition is replicated `REPLICAS` times through RAFT consensus, and a primary replica holds a lease to serve operations. | [Data Consistency and Replication]({gridgain9}/architecture/data-consistency-and-replication), [RAFT Consensus]({gridgain9}/architecture/raft-consensus) |
| Colocation | The colocation key, set with `COLOCATE BY`. | [Data Colocation]({gridgain9}/architecture/data-colocation) |
| SQL engine | Apache Calcite. | [SQL Overview]({gridgain9}/gridgain9-development/sql/overview) |

## Architecture Topics

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/architecture/cluster" %}
[Cluster]({gridgain9}/architecture/cluster)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How a GridGain 9 cluster is built and run — node components and request flow, RAFT consensus, cluster initialization and lifecycle, and fault tolerance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/architecture/data-distribution" %}
[Data Distribution]({gridgain9}/architecture/data-distribution)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 distributes data across a cluster — distribution zones, data partitioning, and data colocation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/architecture/replication-and-consistency" %}
[Replication and Consistency]({gridgain9}/architecture/replication-and-consistency)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 replicates partitions and keeps data consistent — consistency guarantees, RAFT replication, and high availability mode.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/architecture/transactions" %}
[Transactions]({gridgain9}/architecture/transactions)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How ACID transactions work in GridGain 9 — transaction types, guarantees, isolation, MVCC, locking, timeouts, coordination, and monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/architecture/storage" %}
[Storage]({gridgain9}/architecture/storage)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of the GridGain 9 storage system: how tables, distribution zones, storage profiles, and storage engines work together to store your data.
{% endcolumn %}
{% endcolumns %}
