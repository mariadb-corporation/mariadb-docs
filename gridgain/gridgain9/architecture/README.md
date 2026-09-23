---
description: >-
  How GridGain 9 is built: cluster architecture, consensus, data distribution,
  consistency, availability, and storage.
---

# Architecture

This section explains how GridGain 9 works internally — the concepts you need to reason about performance, availability, and data placement. It is background reading rather than task instructions; for operational procedures, see [Cluster Management](../gridgain9-management/README.md).

Start with [Cluster Architecture](cluster-architecture.md) for an end-to-end overview of the node components and how a request flows through the system, then explore the individual topics below.

## In This Section

- [Cluster Architecture](cluster-architecture.md) — the components of a node and how they fit together.
- [RAFT Consensus](raft-consensus.md) — the consensus algorithm that keeps replicas consistent.
- [Cluster Lifecycle](cluster-lifecycle.md) — initialization, node join, and logical vs. physical topology.
- [Cluster Fault Tolerance](cluster-fault-tolerance.md) — how the cluster survives node failures.
- [Data Consistency and Replication](data-consistency-and-replication.md) — the consistency model and how data is replicated.
- [High Availability Mode](high-availability-mode.md) — availability guarantees and their trade-offs.
- [Data Colocation](data-colocation.md) — placing related data together to avoid network hops.
- [Transactions](transactions.md) — the distributed transaction model and MVCC.
- [Storage](storage/README.md) — distribution zones, partitioning, storage profiles, and storage engines.
