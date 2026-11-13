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

### RAFT Log Storage

Each node keeps the RAFT logs of its persistent partitions, the metastorage group, and the CMG in the segment log storage. Volatile partitions keep their RAFT log in memory, as described in [Log Storage Budget](storage/engines/in-memory-storage.md#log-storage-budget).

A node runs three separate log storages, one each for partitions, the metastorage group, and the CMG. Each storage keeps its files in the `segstore` subdirectory of its component's log path:

| Log | Default location |
| --- | --- |
| Partitions | `{system.partitionsLogPath}/segstore` |
| Metastorage group | `{system.metastoragePath}/log/segstore` |
| CMG | `{system.cmgPath}/log/segstore` |

All RAFT groups of a storage append their entries to the same segment file. When the file is full, the storage starts a new one and writes index files for the full one. A segment file is 2 GiB by default. You can change the file size and the other storage settings in the [Log Storage Configuration](../reference/configuration/node-configuration-parameters.md#log-storage-configuration).

#### Durability

The partitions log follows the [`raft.fsync`](../reference/configuration/node-configuration-parameters.md#raft-configuration) setting, which is off by default. With `fsync` off, the node syncs the log to disk when a segment file is full, and before a storage engine persists its data. The log on disk then holds every entry that the persisted data depends on. The metastorage and CMG logs always use `fsync`.

#### Reclaiming Disk Space

Truncating a RAFT log does not free disk space right away. Each storage compacts its segment files once its size exceeds a compaction threshold. Compaction deletes the files that hold no live entries, and copies the live entries of other files into new, smaller files.

The threshold is the smaller of `logStorage.softLogSizeLimitBytes` and half of `raft.logStorage.softPartitionsLogSizeLimitBytes`, but at least one segment file. With default settings, compaction starts at about 10 GiB. The node computes the threshold at startup, so a change to either property applies to compaction after a restart.

If the partitions log keeps growing past `raft.logStorage.softPartitionsLogSizeLimitBytes`, the node flushes the data of its persistent partitions to disk, truncates their logs, and then compacts the segment files. For details, see [Soft Disk Usage Limits](../reference/configuration/node-configuration-parameters.md#soft-disk-usage-limits).

#### Migrating From the RocksDB Log

Versions before 9.2 keep RAFT logs in RocksDB. After an upgrade to 9.2, a node keeps writing the existing logs to RocksDB until the cluster version is 9.2.0 or later. The cluster version changes when you commit a [rolling upgrade](../gridgain9-management/upgrade/rolling-upgrade.md).

After the commit, each RAFT group writes new entries to the segment log storage and reads older ones from RocksDB. A group stops using RocksDB once its log is truncated past the last RocksDB entry. The migration cannot be reverted.

### Storage-Based Write Admission

Once per second each node monitors the drives that host its partition Raft log and persistent partition data. When the usage of either drive exceeds the hard limit configured for it, the node refuses incoming client write requests. Read requests, including reads inside read-write transactions, continue to work. Keep in mind that only client writes are blocked, as specific internal operations are required for the cluster to operate.

Nodes broadcast their at-limit state to peers. If the majority of replicas for a partition are at-limit, the primary replica also refuses writes for that partition until enough peers recover.

Writes resume automatically once drive usage drops below the limit, or you raise the limit. For guidance on configuring these limits, see the [Hard Disk Usage Limits](../reference/configuration/node-configuration-parameters.md#hard-disk-usage-limits) section.

Each node also enforces *soft* limits on its partition log storage. Exceeding a soft limit triggers reactive log storage compaction to reclaim space. Client writes are never refused. Keep soft limits below the hard limits so compaction has room to act before admission control engages. For configuration details, see the [Soft Disk Usage Limits](../reference/configuration/node-configuration-parameters.md#soft-disk-usage-limits) section.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
