---
description: >-
  Configure high availability mode on GridGain 9 distribution zones to
  prioritize partition availability over strict consistency, enabling automatic
  recovery from majority replica loss.
---

# High Availability Mode

High availability mode is a consistency option for distribution zones that prioritizes partition availability over strict consistency guarantees. When a partition configured for high availability loses its majority of replicas, the system automatically reconfigures to continue operating with the remaining replicas rather than becoming unavailable. This behavior differs from strong consistency mode, which requires manual intervention to recover from majority loss.

## How Automatic Recovery Works

When a distribution zone uses high availability mode, GridGain continuously monitors the health of partition replicas. For each partition, it tracks which replicas are currently available and compares this against the configured replica assignments. When GridGain detects that a partition has lost its majority of replicas, it initiates automatic recovery.

The recovery process reconfigures the partition's RAFT group to include only the currently available replicas. This allows the partition to establish a new majority with fewer members and resume processing read and write operations. The reconfiguration happens without user intervention and typically completes within several seconds, up to 15 seconds in unfavorable network conditions. This includes the time needed for detecting the failure, performing the reconfiguration, and electing a new leader.

During the recovery window, operations attempting to access the affected partition experience failures or timeouts. Applications should implement retry logic to handle these temporary failures. Once recovery completes, the partition becomes available again and operations succeed normally, though with a reduced number of replicas until the failed nodes return or rebalancing adds new replicas.

The system tracks the historical state of partition assignments to minimize data loss risks during recovery. When a minority of replicas continues after majority loss, it verifies that continuing with those replicas is the appropriate action. This tracking prevents scenarios where an outdated replica with stale data could incorrectly become the source of truth for the partition.

After automatic recovery completes, the partition operates with fewer replicas than originally configured. The system attempts to restore full replica count when failed nodes return to service or when rebalancing operations assign new replicas. Returning nodes are validated before being added back to ensure they do not introduce conflicting data.

## Consistency Tradeoff

High availability mode accepts potential data loss in exchange for continuous operation. This tradeoff stems from how the system handles majority failures - by allowing a minority to continue, there is risk that the failed majority had recent writes that the surviving minority did not receive.

For example, consider a partition with three replicas where two nodes fail simultaneously. In strong consistency mode, the partition becomes unavailable because the single surviving replica cannot form a majority. The system waits for operator intervention to either restore the failed nodes or explicitly accept potential data loss through manual disaster recovery. In high availability mode, the single surviving replica automatically reconfigures to form a new single-member group and continues processing operations.

The data loss risk in high availability mode occurs when the failed majority had successfully committed writes that had not yet replicated to the surviving minority. Standard RAFT consensus requires writing to a majority before acknowledging success to clients, which typically means data committed to clients has reached multiple replicas. However, in the specific timing window where writes reached the majority but the minority had replication lag, those writes may be lost if the majority fails and the minority continues.

## Comparing High Availability and Strong Consistency

The choice between high availability mode and strong consistency mode affects how your cluster responds to failures. Understanding these differences helps you select the appropriate mode for each distribution zone based on your application requirements.

Strong consistency mode follows standard RAFT behavior where a partition requires a majority of its replicas to remain available. With three replicas, losing two makes the partition unavailable. With five replicas, losing three makes it unavailable. The partition remains unavailable until you either restore enough failed nodes to recreate the majority or perform manual disaster recovery operations that explicitly accept potential data loss. Recovery times range from hours to days depending on how quickly you can restore nodes or complete recovery procedures.

High availability mode automatically recovers from majority loss by reconfiguring partitions to continue with available replicas. The same failures that make strong consistency partitions unavailable trigger automatic recovery in high availability mode. Recovery typically completes within several seconds, up to 15 seconds in unfavorable network conditions, and the partition resumes normal operations with reduced replica count. The faster recovery trades off the possibility of data loss if the failed majority had recent writes that the surviving minority did not receive.

For single node failures or minority failures, both modes behave identically. The partition remains available using the surviving majority, and the system operates normally aside from reduced fault tolerance until the failed node returns. Leader election may cause 1 to 11 seconds of unavailability if the failed node was the leader, but this affects both modes equally.

Network partitions affect the modes differently. In strong consistency mode, only the network segment containing the majority can continue operating. The minority segment's partitions become unavailable until network connectivity restores. In high availability mode, the majority segment continues normally, but the minority segment may also reconfigure its partitions to remain available, leading to split-brain scenarios where both segments continue with potentially conflicting data. Reconciliation after network healing requires careful attention in high availability mode.

Recovery operations differ significantly between the modes. Strong consistency mode requires manual intervention through the disaster recovery CLI commands when majority loss occurs. Operators must explicitly acknowledge the recovery action and potential data loss. High availability mode requires no operator intervention - the system automatically recovers and continues. However, operators should still monitor partition states after failures to verify successful recovery and check for data loss.

Choose strong consistency mode when data integrity is paramount, and you can tolerate extended unavailability during recovery. Use 5 or more replicas to improve fault tolerance while maintaining strict consistency guarantees.

Choose high availability mode when continuous availability is more important than preventing all possible data loss. Caching layers, analytics data, session storage, and other regenerable data workloads benefit from automatic recovery. Plan for 3 replicas typically, which provides single-node fault tolerance and enables automatic recovery from dual-node failures within seconds.

## Configuring High Availability Mode

Distribution zones control the consistency mode for all tables created within that zone. When creating a distribution zone, specify the consistency mode in the zone configuration. The default mode is strong consistency, so you must explicitly configure high availability mode if you want its behavior.

Create a distribution zone with high availability mode using SQL DDL:

```sql
CREATE ZONE IF NOT EXISTS exampleZone (REPLICAS 3, CONSISTENCY MODE 'HIGH_AVAILABILITY') STORAGE PROFILES['default'];
```

This creates a zone with three replicas configured for automatic recovery. Tables created in this zone inherit the high availability behavior. You cannot change a zone's consistency mode after creation - to switch modes, create a new zone and migrate your tables.

When configuring high availability zones, consider the replica count carefully. With 3 replicas, the zone tolerates one node failure while maintaining normal operations, and automatically recovers from two node failures within seconds. The single remaining replica after recovery has no fault tolerance, so restoring failed nodes or adding new replicas becomes urgent. With 5 replicas, the zone tolerates two failures normally and can automatically recover from three failures, leaving 2 replicas after recovery for continued single-failure tolerance.

You can verify the consistency mode of existing zones using system views:

```sql
SELECT ZONE_NAME, ZONE_CONSISTENCY_MODE, ZONE_REPLICAS
FROM SYSTEM.ZONES;
```

This shows the consistency mode and replica count for all distribution zones in the cluster. Look for `HIGH_AVAILABILITY` in the `ZONE_CONSISTENCY_MODE` column to identify zones configured for automatic recovery.

## Verifying Automatic Recovery

After a failure that triggers automatic recovery, verify that the partition successfully reconfigured and resumed operations. The partition states command shows the current state of partitions across the cluster:

```bash
recovery partitions states --zones EXAMPLEZONE --global
```

Before automatic recovery completes, affected partitions appear with read-only or unavailable states, indicating they lost their majority. After recovery completes, the partitions transition to available or degraded states. Degraded state indicates the partition is operational but has fewer replicas than configured, meaning it has reduced fault tolerance.

You can check specific partitions rather than all partitions in a zone:

```bash
recovery partitions states --zones EXAMPLEZONE --partitions 0,1,2 --global
```

This helps focus on partitions you know were affected by the failure. Compare the partition states before and after the failure event to confirm recovery completed as expected.

Monitor for partitions remaining in degraded state for extended periods. While degraded partitions function normally, they have reduced fault tolerance and another failure could make them unavailable. Plan to restore failed nodes or trigger rebalancing to return degraded partitions to their full replica count.
