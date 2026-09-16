---
description: >-
  How GridGain 9 maintains data consistency through RAFT replication and consensus,
  the guarantees it provides, and how the cluster behaves during node and network
  failures.
---

# Data Consistency and Replication

GridGain ensures data consistency across the cluster through replication and consensus mechanisms. This page explains how GridGain maintains consistency, what guarantees you can expect, and how the system behaves during failures.

## Consistency Guarantees

GridGain provides strong consistency guarantees for transactions. When a write operation is confirmed, it is durable and immediately visible to subsequent reads. Take into account that the same data may be seen on concurrent clients after some delay due to replication lag and other reasons. However, those clients will always see consistent data without partial updates, and causally dependent transactions will always be consistent with their causal predecessors. Transactions provide isolation, ensuring you never see partial updates from other transactions. The RAFT consensus protocol ensures all replicas of a partition agree on the order of operations, maintaining consistency within partition groups while replication propagates changes across the cluster.

## System Behavior During Failures

GridGain prioritizes consistency and partition tolerance, which means the system makes specific trade-offs during network issues or node failures. Understanding these trade-offs helps you design resilient applications and plan for failure scenarios.

### Normal Operations

When all nodes are healthy and the network is stable, reads and writes operate normally with all partitions available. This is the state where GridGain delivers optimal performance while maintaining its consistency guarantees.

### Single Node Failure

When a minority of replica nodes fail, the system continues normal operations. The failed node automatically catches up when it returns, and no administrator intervention is required. GridGain's consensus algorithm handles this scenario transparently by using the remaining replicas to maintain the majority quorum.

### Network Partition

When the network splits the cluster into separate groups, only the group that contains the majority of both the [cluster management](../lifecycle.md#cluster-management-group) and [metastorage](../lifecycle.md#cluster-metastorage-group) nodes continues full operations. Groups without the required majorities become unavailable or read-only depending on what majorities they retain.

For each data partition, only the group with the majority of that partition's replicas can accept writes. This prevents split-brain scenarios where both sides of a network partition might try to accept conflicting updates. When the network partition heals, the groups that could not write will automatically catch up from the group that maintained the majority.

### Multiple Node Failure

When the majority of replica nodes for a partition fail, that partition becomes unavailable for writes. If the primary replica survived, existing data remains readable through read-only transactions, but no new writes can be accepted. The system waits for nodes to return rather than risking data loss by proceeding without the majority.

If nodes cannot be recovered, manual intervention through the [disaster recovery](../disaster-recovery.md) procedures may be necessary to restore partition availability. This might involve accepting some data loss in exchange for returning the partition to service.

## Consistency vs. Availability Trade-off

GridGain's design ensures you never lose committed data or see inconsistent results. The trade-off is that partitions become unavailable when they cannot maintain consistency guarantees. This design is appropriate when data correctness is critical, losing data is unacceptable, and brief unavailability during failures is acceptable.

If your workload prioritizes availability over consistency - meaning you prefer the system to remain operational even if it might mean losing recent writes - consider using [high availability mode](high-availability-mode.md). This mode changes the behavior so that when a majority of replicas are lost, the system automatically reconfigures partitions to continue operations with the surviving replicas. See [Cluster Fault Tolerance](../cluster-fault-tolerance.md) for detailed information about how different failure scenarios affect cluster availability.

## Replication and Consensus

GridGain replicates each partition to multiple nodes based on the [REPLICAS](distribution-zones.md#configuring-data-replication) setting you configure in the distribution zone. When a client sends updated data to a partition's primary replica, that primary replica coordinates replication to the other replicas. Once a majority of replicas confirm they have received and stored updated data, it is considered committed. The primary replica then responds to the client, while remaining replicas receive updates asynchronously. This process ensures durability - committed data survives node failures as long as a majority of replicas survive.

### RAFT Consensus Protocol

GridGain uses the RAFT consensus protocol to coordinate replicas and ensure all replicas process operations in the same order. Each partition's replicas form a RAFT group where one replica acts as the leader that coordinates all write operations. Other replicas act as followers that replicate operations from the leader and participate in elections, or as learners that receive updates passively without voting rights. The [quorum size](distribution-zones.md#quorum-size) configuration determines how many replicas must acknowledge operations before they are considered committed.

For detailed information about how RAFT groups work, including leader election, write replication, and log management, see the [Understanding RAFT Consensus](data-partitions.md#understanding-raft-consensus) section in the Data Partitions documentation.

### Voting Members and Learners

Not all replicas necessarily participate in voting. GridGain automatically designates some replicas as learners to optimize the performance and fault tolerance balance. Voting members form the consensus group and participate in elections, while learners only receive updates without voting. The consensus group size is calculated as `quorumSize * 2 - 1`.

For example, if you have 5 replicas with quorum size 3, all 5 replicas become voting members since 3 * 2 - 1 equals 5. However, with 5 replicas and quorum size 2, only 3 replicas are voting members while 2 become learners. This second configuration can lose only 1 voting member before becoming unavailable, which is why using quorum size 3 with 5 replicas provides better fault tolerance.

### Write Acknowledgment

GridGain uses majority quorum for write acknowledgment. With 3 replicas, 2 must acknowledge (tolerating 1 failure). With 5 replicas, 3 must acknowledge (tolerating 2 failures). With 7 replicas, 4 must acknowledge (tolerating 3 failures). A write is committed only when the required quorum acknowledges it, ensuring durability even if some replicas are temporarily unavailable.

Note that with only 1 replica, there is no redundancy, and with 2 replicas, both must acknowledge, so losing either replica makes writes impossible. This is why 3 replicas is the recommended minimum for production workloads.

## Primary Replicas and Leases

To ensure only one node coordinates writes to a partition, GridGain uses a lease system managed by the placement driver component. A lease is a time-limited exclusive right to act as the partition's primary replica. The placement driver runs as part of cluster management and grants time-limited leases to replication group leaders. Only the leaseholder can coordinate write operations for its partition, which prevents conflicting writes during failures.

The placement driver continuously monitors and renews leases for healthy primary replicas. Every 500 milliseconds, it checks which leases are approaching expiration and renews them for primaries that remain healthy. Leases are renewed when they have half their configured duration remaining - with the default 5-second expiration, renewal happens when 2.5 seconds remain. This continuous renewal means a healthy primary's lease never actually expires during normal operation.

When a primary replica fails, its lease continues to be valid until it expires naturally. The placement driver cannot grant a new lease during this time because the old lease might still allow the failed primary to coordinate writes. Once the lease expires, the placement driver can grant a new lease to a different replica, typically the newly elected RAFT leader.

The time from primary failure to write availability depends on lease expiration plus leader election time. With default settings, lease expiration takes up to 5 seconds, and leader election typically takes between 1 and 11 seconds depending on cluster condition. As a result, write recovery typically completes within 6-16 seconds. Read-only transactions continue unaffected during this window since they can read from any available replica.

Leases have a configured duration (5 seconds by default) and cannot be revoked early - they must expire naturally. You can adjust lease timing through the replication configuration. Shorter lease durations provide faster failover when the primary fails but impose higher coordination overhead from more frequent renewals. Longer lease durations reduce coordination overhead but mean slower failover. The default values provide a good balance for most deployments:

```shell
cluster config update ignite.replication.leaseExpirationIntervalMillis=5000
```

For detailed information about how leases interact with RAFT groups and affect recovery times during different failure scenarios, see [Cluster Fault Tolerance](../cluster-fault-tolerance.md).

## Reading Data

GridGain handles reads differently depending on the transaction type. Read-write transactions always read from the primary replica (the leaseholder) to ensure they see the latest committed data and that reads reflect writes made within the same transaction. This coordination with the primary replica is necessary because read-write transactions may make modifications that need to interact with other concurrent transactions.

Read-only transactions do not block or interfere with writes. Instead of taking locks, they read data as of their transaction's read timestamp, so they never wait for concurrent writes to complete. For details on transaction behavior, see [Transactions](../transactions.md).

Reads through the table and key-value APIs are always served by the primary replica, even inside a read-only transaction. SQL is the exception: the SQL engine can map a read-only query onto non-primary replicas, which spreads read load across all replicas and lets a query read from a local replica, avoiding a network hop. This is disabled by default - see the cluster-wide [`sql.allowFollowerReads`](../config/cluster-config.md#sql-configuration) setting and the `allowFollowerReads` statement property.

### Safe Time Synchronization

To ensure backup replicas serve consistent data, GridGain tracks safe time for each replica. The safe time is the latest timestamp for which the replica has all committed data. It is updated after each write or periodically during idle periods. When an SQL query reads from a backup replica, the replica checks whether its safe time has advanced far enough to serve that read. If not, the transaction waits until the safe time advances.

The idle update period is controlled by [`idleSafeTimePropagationDurationMillis`](../config/cluster-config.md#replication-configuration), which defaults to 1000 milliseconds. This means that during idle periods, replicas receive safe time updates at least once per second to ensure they can serve recent reads even when no writes are happening.

## Monitoring Consistency

You can monitor partition health using the `recovery partition states` [CLI command](../../ignite-cli-tool.md#disaster-recovery-commands):

```shell
recovery partition states --zone ZONE_NAME
```

This shows the current state of each partition, helping you identify problems before they impact availability. See [Partition States](../disaster-recovery.md#partition-states) for descriptions of what each state means.

You can also query system views to inspect replication status. The `system.zone_partitions` view shows partition assignments across the cluster, while `system.primary_replicas` shows which nodes currently hold primary replica leases:

```sql
-- View partition assignments
SELECT * FROM system.zone_partitions;

-- View current primary replicas
SELECT * FROM system.primary_replicas;
```

See [System Views](../metrics/system-views.md) for the complete reference on available system views.

## Planning for Consistency

When designing your distribution zones and replica strategy, several considerations help ensure you get the consistency and availability characteristics you need.

### Production Replica Counts

The number of replicas you configure directly determines fault tolerance. GridGain requires a majority of replicas to remain available for write operations, which means the number of tolerable failures is always less than half the replica count. The following table shows recommended configurations for different requirements:

| Replicas | Tolerable Failures | Recovery Without Majority | Recommended Use Case |
|---|---|---|---|
| 1 | 0 | Not possible | Development and testing only - provides no fault tolerance |
| 2 | 0 | Not possible | Not recommended - both nodes required for writes, no fault tolerance advantage over single replica |
| 3 | 1 | Strong Consistency: Manual intervention required<br>High Availability: Automatic recovery, typically within several seconds, up to 15 seconds in unfavorable network conditions | Minimum production configuration for non-critical data |
| 5 | 2 | Strong Consistency: Manual intervention required<br>High Availability: Automatic recovery, typically within several seconds, up to 15 seconds in unfavorable network conditions | Recommended for critical data requiring higher fault tolerance |
| 7 | 3 | Strong Consistency: Manual intervention required<br>High Availability: Automatic recovery, typically within several seconds, up to 15 seconds in unfavorable network conditions | Very high availability requirements, can tolerate three simultaneous failures |

{% hint style="info" %}
Always use odd numbers for replica counts. Even numbers like 4 or 6 provide no additional fault tolerance compared to the next lower odd number but require more storage and impose higher replication overhead. For example, 4 replicas tolerates only 1 failure (the same as 3 replicas), while 6 replicas tolerates only 2 failures (the same as 5 replicas).
{% endhint %}

The default configuration uses only 1 replica, which provides no fault tolerance - any node failure makes that partition's data unavailable. This default is suitable only for development or testing environments. Always configure at least 3 replicas for production deployments.

### Quorum and Distribution Zone Configuration

Keep default quorum settings unless you have specific requirements, as GridGain calculates sensible defaults based on replica count. Understand that higher quorum reduces risk of data loss during failures but increases the risk of unavailability since more replicas must be online to accept writes.

When planning distribution zones, group related tables in the same zone for colocation benefits, which improves query performance by reducing cross-partition operations. Consider creating separate zones for data with different consistency requirements - for example, you might use strong consistency for critical transactional data and [high availability mode](high-availability-mode.md) for caching or non-critical data.
