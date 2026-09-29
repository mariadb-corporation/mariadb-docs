---
description: >-
  Deploying GridGain 9 for high availability — keeping the cluster and its data
  available through node and zone failures.
---

# High Availability

High availability is about keeping a GridGain 9 cluster serving requests through node, rack, and data-center failures. It builds on the replication and consensus described in [Architecture](../../architecture/README.md) and is realized through how you size replicas, place data, and configure availability behavior.

The concepts live in the Architecture section; this section focuses on applying them to a deployment.

## Key Topics

- [High Availability Mode](../../architecture/high-availability-mode.md) — the availability guarantees GridGain 9 offers and their trade-offs.
- [Cluster Fault Tolerance](../../architecture/cluster-fault-tolerance.md) — how the cluster tolerates node failures.
- [Data Consistency and Replication](../../architecture/data-consistency-and-replication.md) — how replication underpins availability.
- [Distribution Zones](../../architecture/storage/distribution-zones.md) — controlling replica counts and data placement.
- [Performance Tuning](../performance-tuning/README.md) — keeping a highly available cluster performant under load.
