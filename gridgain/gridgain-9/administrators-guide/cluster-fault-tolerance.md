---
description: >-
  Fault tolerance characteristics of GridGain 9 cluster components, what happens
  during failure scenarios, and how to plan for high availability.
---

# Cluster Fault Tolerance

Understanding how GridGain handles failures is essential for running production clusters. This page explains the fault tolerance characteristics of different cluster components, what happens during various failure scenarios, and how to plan for high availability.

## RAFT Groups in GridGain

GridGain uses multiple RAFT consensus groups to manage different aspects of cluster operation. Each group has distinct characteristics and failure behaviors that affect cluster availability.

### Cluster Management Group

The [cluster management group](lifecycle.md#cluster-management-group) (CMG) manages cluster topology and node membership. You configure CMG membership during cluster initialization, and this membership remains fixed throughout the cluster's lifetime. The CMG nodes run a RAFT group that coordinates topology changes and validates new nodes joining the cluster.

When the CMG loses its majority, the cluster continues handling data operations but cannot modify topology. You cannot add new nodes, remove existing nodes, or create new indexes until the majority is restored. For most deployments, a CMG of 3, 5, or 7 nodes provides the right balance between fault tolerance and coordination overhead. Recovery from CMG majority loss requires bringing offline CMG nodes back online - there is no automatic recovery mechanism.

### Metastorage Group

The [metastorage group](lifecycle.md#cluster-metastorage-group) stores the cluster catalog, including table schemas, distribution zones, and configuration. Like the CMG, you configure metastorage membership during initialization, and this membership is fixed. The metastorage nodes run a RAFT group that coordinates all metadata updates.

Losing the metastorage majority makes the cluster unable to process metadata operations. Tables cannot be created or modified, distribution zones cannot be updated, and configuration changes cannot be applied. Existing data operations may continue using cached metadata, but any operation requiring fresh metadata will fail. Recovery requires bringing offline metastorage nodes back online or performing a [cluster reset procedure](system-groups-recovery.md).

### Data Partitions

Each table partition forms its own RAFT group consisting of the partition's replicas. GridGain automatically assigns replicas based on the [distribution zone](storage/distribution-zones.md) configuration - the number of replicas, the partition count, and the data node filter. Unlike CMG and metastorage groups, partition membership changes automatically during rebalancing operations when nodes join or leave the cluster.

Partition groups behave differently depending on whether the distribution zone uses strong consistency or [high availability mode](storage/high-availability-mode.md). With strong consistency, losing the partition majority makes that partition unavailable until you restore the majority or perform disaster recovery. With high availability mode, the system automatically reconfigures the RAFT group to continue with available replicas, prioritizing availability over strict consistency guarantees.

### Lease Management

To coordinate writes across all data partitions, GridGain uses a lease system managed by the placement driver. The placement driver runs as part of cluster management and grants time-limited leases to primary replicas. Only the leaseholder can coordinate write operations for its partition, which prevents conflicting writes during failures.

Leases have a configured duration (5 seconds by default) and cannot be revoked early - they must expire naturally. The placement driver continuously renews leases for healthy primaries, checking every 500 milliseconds and renewing when a lease reaches its midpoint. If a primary replica fails, its lease expires after the full duration, at which point the placement driver can grant a new lease to a different replica. This design trades faster failover for simpler coordination and stronger safety guarantees.

## Replica Counts and Fault Tolerance

The number of replicas you configure for a distribution zone directly determines how many node failures that zone can tolerate. GridGain requires a majority of replicas to be available for write operations, which means the number of tolerable failures is always less than half the replica count.

For example, with 3 replicas, the system requires 2 nodes for writes and tolerates 1 failure. With 5 replicas, 3 nodes are required and 2 failures are tolerated. With 7 replicas, 4 nodes are required and 3 failures are tolerated. This pattern continues for any replica count - the number of tolerable failures is always `(replicas - 1) / 2` when using integer division.

You should always use odd numbers for replica counts. Even numbers like 4 or 6 provide no additional fault tolerance compared to the next lower odd number, but they require more storage space and impose higher replication overhead. For example, 4 replicas tolerates only 1 failure (the same as 3 replicas), while 6 replicas tolerates only 2 failures (the same as 5 replicas).

For production workloads, use at least 3 replicas to provide single-node fault tolerance while maintaining write availability. For critical data requiring higher fault tolerance, use 5 replicas to survive two simultaneous failures. Using 7 or more replicas is rarely necessary unless you need to tolerate three or more simultaneous failures, and the additional coordination overhead may impact performance.

The default configuration uses only 1 replica, which provides no fault tolerance - any node failure makes that partition's data unavailable. This default is suitable only for development or testing environments. Always configure at least 3 replicas for production deployments.

## Recovery Time

### Leader Election

Election timeouts start at approximately 1.2 seconds (with a randomized component of up to 1 additional second) for the first election round. If the first three rounds fail to produce a leader (due to network delays or vote splitting), subsequent rounds use progressively longer timeouts, doubling each time up to a maximum of 11 seconds. Most leader elections complete within 2-3 seconds, but in challenging network conditions or with many concurrent elections, the process may take up to 11 seconds.

For data partitions, leader election affects write availability but not read availability for most SQL queries, since distributed SQL read-only operations can read from any replica. Point lookups by primary key and KV API operations still route to the primary replica.

### Lease Expiration and Renewal

Primary replica leases expire after 5 seconds by default (configured through `ignite.replication.leaseExpirationIntervalMillis`). The placement driver checks leases every 500 milliseconds and renews them when they have 2.5 seconds or less remaining. This means a healthy primary's lease never actually expires - it's renewed continuously while the primary remains available.

When a primary fails, its lease continues to be valid for up to 5 seconds. During this time, the failed primary cannot process writes, but the placement driver cannot grant a new lease yet because the old lease must expire first. Once the lease expires, the placement driver grants a new lease, typically to the newly elected leader. The total time from primary failure to write availability is therefore the sum of lease expiration time (up to 5 seconds) and leader election time (1-11 seconds), resulting in typical recovery times of 6-16 seconds.

### Strong Consistency Recovery

Partitions using strong consistency mode become unavailable when they lose their majority. Recovery requires either restoring the majority by bringing failed nodes back online or performing manual [disaster recovery](disaster-recovery.md) operations. The time required depends entirely on how quickly you can restore nodes or complete recovery procedures - there is no automatic recovery mechanism.

Bringing nodes back online typically allows the partition to recover automatically once the majority is restored. The returning nodes catch up by either replicating missing operations from the log or receiving a full snapshot, which may take minutes to hours depending on how much data needs to be transferred. Manual disaster recovery procedures also vary in duration based on cluster size and data volume, but typically require administrator intervention and coordination, adding operational overhead to the recovery time.

### High Availability Recovery

Partitions using [high availability mode](storage/high-availability-mode.md) recover automatically when they lose their majority. The system detects the loss, reconfigures the RAFT group to include only available replicas, and resumes operations, typically within several seconds, up to 15 seconds in unfavorable network conditions. This includes time for detecting the failure, performing RAFT reconfiguration, and electing a new leader.

The automatic recovery trades consistency guarantees for availability - if the majority that failed had recent writes that the minority did not, those writes are lost when the minority continues. See [High Availability Mode](storage/high-availability-mode.md) for details about this tradeoff and when it is appropriate.

## CMG and Metastorage Impact

The cluster management and metastorage groups provide essential services, but losing their majority has different impacts than losing data partition majorities. Understanding what continues to work and what stops helps you respond appropriately to failures.

### Operations During CMG Majority Loss

When the CMG loses its majority, user transactions and data queries continue normally. Applications can read and write data in existing tables, execute compute jobs, and perform all operations that do not require topology changes. The placement driver continues granting leases to primary replicas, and data partitions continue replicating normally.

The cluster cannot add new nodes to the logical topology or re-add nodes that have left. Index creation requires writing to the metastorage and knowledge of the cluster topology, so it may fail if either the metastorage or the CMG has lost its majority. Any `CREATE INDEX` DDL operation will hang waiting for these dependencies to become available.

To restore full functionality, bring offline CMG nodes back online to restore the majority. There is no mechanism to reconfigure the CMG membership without a majority - if the majority cannot be restored, a [cluster reset](system-groups-recovery.md#cluster-management-group) is required.

### Operations During Metastorage Majority Loss

Losing the metastorage majority prevents metadata operations throughout the cluster. Tables cannot be created, modified, or dropped. Distribution zones cannot be created or altered. Configuration changes cannot be applied. The cluster catalog cannot be updated, which stops all DDL operations.

Existing data operations may continue if they can use cached metadata. Transactions that access already-open tables and execute familiar queries may succeed. However, any operation that requires fresh schema information will fail, and new client connections may not be able to bootstrap their metadata cache.

Recovery requires bringing offline metastorage nodes back online or, if that is not possible, performing a [metastorage repair](system-groups-recovery.md#metastorage-group) operation. Metastorage repair is only permitted when the majority is actually offline - attempting to repair while a working majority exists is rejected to prevent accidental data loss.

## Failure Scenario Matrix

Different failure scenarios affect cluster components differently. This section describes common failure patterns and their impacts.

### Single Node Failure

When a single node fails, the impact depends on what roles that node served. For data partitions with 3 or more replicas, the system continues normally because the majority (2 out of 3, or 3 out of 5, etc.) remains available. For system groups like CMG or metastorage, the same majority logic applies - losing one node from a 3-node or larger group leaves the majority intact.

The primary replica lease may need to expire and transfer to a new node if the failed node held leases, adding up to 5 seconds of write unavailability for affected partitions. If the failed node was a RAFT leader, leader election adds 1-11 seconds. The total impact is typically 6-16 seconds of write unavailability for partitions where the failed node was primary.

Read operations continue unaffected since read-only transactions can use any available replica. Applications experience transparent recovery with possible brief delays for operations that were in flight when the failure occurred.

### Minority Failure

When multiple nodes fail but still less than half of each RAFT group's replicas, the system continues operating normally. All partitions that maintained their majority remain available for reads and writes. System groups like CMG and metastorage continue coordinating topology changes and metadata operations.

The cluster moves into a degraded state with reduced fault tolerance. For example, with 5 replicas, losing 2 nodes leaves only 3 available, meaning one more failure would cause majority loss. The [partition states command](../ignite-cli-tool.md#disaster-recovery-commands) shows these partitions in `Degraded` state:

```bash
recovery partitions states --zones ZONE_NAME --global
```

You should prioritize restoring failed nodes to return to full fault tolerance. The longer the cluster operates with reduced fault tolerance, the higher the risk that an additional failure will cause majority loss and partition unavailability.

### Majority Failure with Strong Consistency

When the majority of replicas fail for a partition using strong consistency, that partition becomes unavailable. If the primary replica survived, the partition enters read-only mode where read-only transactions can access historical data until the lease expires. Once the lease expires, the partition becomes completely unavailable.

The partition remains unavailable until you either restore the majority by bringing failed nodes back online or perform [disaster recovery](disaster-recovery.md#majority-offline). Disaster recovery operations may involve accepting data loss in exchange for restoring availability, so they require careful consideration and administrator involvement.

For system groups like CMG and metastorage, majority loss has the effects described in the previous section. These groups do not have a read-only mode - they either have a majority and function normally, or they lack a majority and cannot coordinate operations.

### Majority Failure with High Availability

Partitions configured for [high availability mode](storage/high-availability-mode.md) recover automatically from majority loss. The system detects that a partition has lost its majority but has at least one replica still available. It then reconfigures the RAFT group to include only the available replicas and resumes operations.

This automatic recovery typically completes within several seconds, up to 15 seconds in unfavorable network conditions, providing much faster recovery than manual disaster recovery procedures. However, it comes with a consistency tradeoff - if the failed majority had recent writes that the surviving minority did not receive, those writes are lost when the minority continues.

You can verify automatic recovery using the partition states command:

```bash
# Before recovery - shows unavailable or read-only
recovery partitions states --zones HA_ZONE --global

# After recovery - should show available or degraded
recovery partitions states --zones HA_ZONE --global
```

The partition remains in a degraded state until you restore the failed nodes. When nodes return, the system attempts to re-add them to the RAFT group, but it carefully checks that they do not have conflicting data that could cause inconsistencies.

### Network Partition

When network failures split the cluster into separate groups, only the group containing majorities of both the CMG and metastorage can continue full operations. Other groups experience the limitations described above for CMG or metastorage majority loss.

For data partitions, each partition independently determines whether its replicas have a majority in their network segment. Some partitions may have majorities in one segment while other partitions have majorities in a different segment, leading to partial availability where some data is accessible and other data is not.

When network connectivity restores, the segments rejoin automatically. Nodes that lost majority and stopped processing operations catch up from nodes that maintained majority and continued. See [Network Segmentation](lifecycle.md#network-segmentation-scenario) for detailed behavior during cluster splits.

## Transaction Behavior During Failures

Transactions interact with failures depending on their type, the operations they perform, and what resources they access.

Read-only transactions may survive primary replica failures, depending on how they are executed. SQL read-only queries (scans, joins, aggregations) typically survive primary replica failures. They read data as of their transaction's start timestamp and do not coordinate with the primary replica, so primary failures do not affect their execution. The only impact is if they attempt to read from a partition that has lost its majority entirely. However, point lookups by primary key (optimized as direct key-value operations) and read-only operations executed from key-value API route to the primary replica and may experience brief unavailability during primary failover.

Read-write transactions must coordinate with the primary replica for each partition they access. If a primary replica fails during the transaction, the transaction fails with a retriable error. Applications should catch these errors and retry the transaction, which will coordinate with the newly elected primary replica.

Transactions that access multiple partitions see the effects of primary failures on any of those partitions. Even if only one partition loses its primary during a transaction, the entire transaction fails and must be retried. This is because transactions provide atomicity - either all operations succeed or none do.
