---
description: >-
  How GridGain 9 is built: cluster architecture, consensus, data distribution,
  consistency, availability, and storage.
icon: house-blank
---

# Architecture

This section explains how GridGain 9 works internally — the concepts you need to reason about performance, availability, and data placement. It is background reading rather than task instructions; for operational procedures, see [Cluster Management](../gridgain9-management/README.md).

Start with [Cluster Architecture](cluster-architecture.md) for an end-to-end overview of the node components and how a request flows through the system, then explore the individual topics below.

{% columns %}
{% column %}
{% content-ref url="cluster-architecture.md" %}
[Cluster Architecture](cluster-architecture.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A deeper look at the GridGain 9 system architecture: node components, cluster coordination, RAFT replication, transaction processing, and query execution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="raft-consensus.md" %}
[RAFT Consensus](raft-consensus.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 uses the RAFT consensus algorithm to maintain data consistency and fault tolerance across the cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cluster-lifecycle.md" %}
[Cluster Lifecycle](cluster-lifecycle.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How a GridGain 9 cluster is initialized and how its lifecycle works, including topology, cluster initialization, system groups, and node join scenarios.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cluster-fault-tolerance.md" %}
[Cluster Fault Tolerance](cluster-fault-tolerance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Fault tolerance characteristics of GridGain 9 cluster components, what happens during failure scenarios, and how to plan for high availability.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-consistency-and-replication.md" %}
[Data Consistency and Replication](data-consistency-and-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 maintains data consistency through RAFT replication and consensus, the guarantees it provides, and how the cluster behaves during node and network failures.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="high-availability-mode.md" %}
[High Availability Mode](high-availability-mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure high availability mode on GridGain 9 distribution zones to prioritize partition availability over strict consistency, enabling automatic recovery from majority replica loss.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-colocation.md" %}
[Data Colocation](data-colocation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to store related data on the same node in GridGain 9 using the COLOCATE BY clause to speed up multi-entry queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions.md" %}
[Transactions](transactions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How ACID transactions work in GridGain 9 — transaction types, guarantees, isolation, MVCC, locking, timeouts, coordination, and monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="storage/" %}
[Storage](storage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of the GridGain 9 storage system: how tables, distribution zones, storage profiles, and storage engines work together to store your data.
{% endcolumn %}
{% endcolumns %}
