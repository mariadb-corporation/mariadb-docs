---
description: >-
  How GridGain 9 uses the RAFT consensus algorithm to maintain data consistency
  and fault tolerance across the cluster.
---

# RAFT Consensus

GridGain uses the RAFT consensus algorithm to maintain data consistency and fault tolerance across the cluster. This topic explains what RAFT is, how it works, and how GridGain uses it.

## What is RAFT?

[RAFT](https://raft.github.io/) is a consensus algorithm that enables multiple servers in a distributed system to agree on a shared state, even when some servers fail or network partitions occur.

The algorithm ensures that all nodes agree on the cluster status and data update history. This guarantees that all nodes converge on the same state in the same order, providing strong consistency across the cluster.

RAFT achieves consensus through leader election, log replication, and safety mechanisms that work together to maintain consistency.

### Node States and Leadership

Every node in a GridGain RAFT group exists in one of four states:

- **Leader:** The node responsible for handling all client requests and managing log replication to followers. There can be no more than one leader per RAFT group.
- **Follower:** Nodes that replicate data from the leader and participate in voting during elections. Followers passively receive updates from the leader.
- **Candidate:** A transitional state when a follower believes the leader has failed and initiates an election to become the new leader, and proposes itself as a leader on the election start.
- **Learner:** Nodes that only replicate data from the leader, but do not participate in voting.

This single-leader approach simplifies the replication protocol and eliminates conflicts during normal operation. The leader is typically the same node that holds the primary replica lease for the partition.

### Quorum Requirements and Fault Tolerance

RAFT requires a majority [quorum](storage/distribution-zones.md#quorum-size) for both elections and commitment. In a group of N nodes, at least half + 1 RAFT nodes must be available.

| Total RAFT Nodes | Quorum Required | Can Tolerate |
| --- | --- | --- |
| 1 | 1 | 0 failures |
| 2 | 2 | 0 failures |
| 3 | 2 | 1 failure |
| 5 | 3 | 2 failures |
| 7 | 4 | 3 failures |

This quorum requirement ensures that no two disjointed subgroups of a group can have the majority, preventing inconsistencies. If the cluster is partitioned, only the part containing the majority can elect a leader.

The minority partition remains read-only or unavailable until network connectivity is restored. For example, in a 2-node cluster or distribution zone with 2 data replicas, a loss of a single node or copy of data leads to data unavailability.

### Example Cluster Topologies

The following examples show how system and data RAFT groups combine in practice.

| Environment | Nodes | CMG | Replicas | Tolerates |
| --- | --- | --- | --- | --- |
| Development | 1 | 1 | 1 | No failures |
| Low Replica Count | 3 | 3 | 1 | 1 CMG/system node failure; no data failures. Any node loss causes data unavailability for affected partitions, but the cluster remains operational. |
| High Availability | 3 | 3 | 3 | 1 node failure for either CMG/system groups or data. |
| Large cluster | 20 | 5 | 3 | 2 CMG failures, 1 data replica failure per partition; partitions are spread across all 20 nodes |

In a typical 3-node cluster where all nodes are both CMG members and data replica holders with `replicas=3`, the loss of 1 node is tolerable for both system operations and data availability.

## How GridGain Uses RAFT

GridGain relies on RAFT as the foundational mechanism for maintaining consistency and managing cluster operations.

### Cluster Metadata

The [metastorage group](cluster-lifecycle.md#cluster-management-group) handles cluster metadata, such as table and index definitions, distribution zone configurations, and cluster logical topology.

In a similar way, the [Cluster Management Group](cluster-lifecycle.md#cluster-management-group) manages current cluster state, and coordinates node join and leave operations.

### Data Replication

When a table is created, it is immediately [partitioned](storage/data-partitioning.md) according to [distribution zone](storage/distribution-zones.md) configuration, and each partition is assigned to a RAFT group. These RAFT groups are shared by all tables in the same distribution zone and are used to perform data updates and replicate data across the cluster.

### Storage-Based Write Admission

Once per second each node monitors the drives that host its partition Raft log and persistent partition data. When the usage of either drive exceeds the hard limit configured for it, the node refuses incoming client write requests. Read requests, including reads inside read-write transactions, continue to work. Keep in mind that only client writes are blocked, as specific internal operations are required for the cluster to operate.

Nodes broadcast their at-limit state to peers. If the majority of replicas for a partition are at-limit, the primary replica also refuses writes for that partition until enough peers recover.

Writes resume automatically once drive usage drops below the limit, or you raise the limit. For guidance on configuring these limits, see the [Hard Disk Usage Limits](../reference/configuration/node-configuration-parameters.md#hard-disk-usage-limits) section.

Each node also enforces *soft* limits on its partition log storage. Exceeding a soft limit triggers reactive log storage compaction to reclaim space. Client writes are never refused. Keep soft limits below the hard limits so compaction has room to act before admission control engages. For configuration details, see the [Soft Disk Usage Limits](../reference/configuration/node-configuration-parameters.md#soft-disk-usage-limits) section.
