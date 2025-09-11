# Galera Cluster Deployment Variants

MariaDB Galera Cluster is flexible and can be deployed in several different topologies to meet various business needs, from [high availability](../high-availability/understanding-quorum-monitoring-and-recovery.md) within a single data center to geographically distributed disaster recovery. The primary deployment patterns are designed for Local Area Networks (LAN) and Wide Area Networks (WAN).

## Standard LAN Cluster (Single Data Center)

This is the most common deployment pattern for achieving high availability and read scaling within a single data center.

### Topology

The cluster consists of an [odd number of nodes](../high-availability/understanding-quorum-monitoring-and-recovery.md#quorum-calculation) (typically 3 or 5) located in the same data center, connected by a high-speed, low-latency network.

### Purpose

| Purpose                                                                                                                              | Description                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High Availability                                                                                                                    | The cluster can survive the [failure of one or more nodes](../high-availability/recovering-a-primary-component.md#recovering-a-single-failed-node) (depending on its size) without interruption of service.             |
| [Read Scalability](../high-availability/load-balancing/load-balancing-in-mariadb-galera-cluster.md#read-write-splitting-recommended) | Application read traffic can be distributed across all nodes in the cluster.                                                                                                                                            |
| Maintenance                                                                                                                          | [Nodes can be taken offline for maintenance ](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md)(e.g., software upgrades) without causing downtime. |

### Key Consideration

While this provides excellent protection against server failure, the entire cluster is vulnerable to a full data center outage.

## Wide Area Network (WAN) Cluster (Multi-Data Center)

This pattern is designed for [disaster recovery](../high-availability/using-mariadb-replication-with-mariadb-galera-cluster/overview-of-hybrid-replication.md#common-use-cases) and providing lower latency for a geographically distributed user base.

### Topology

The cluster nodes are distributed across two or more physical locations (data centers), connected by a WAN link. To maintain [quorum](../high-availability/understanding-quorum-monitoring-and-recovery.md), it is essential to have an odd number of nodes and an odd number of locations. A typical setup involves three data centers with one or more nodes in each.

### Purpose:

| Aspect            | Description                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Disaster Recovery | If one data center experiences a complete outage, the cluster can maintain quorum and continue to operate from the remaining locations. |
| Reduced Latency   | Client applications can be directed to the topologically closest node, reducing network latency for read operations.                    |

### Key Considerations:

| Consideration     | Description                                                                                                                                                                                                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Network Latency   | WAN replication is sensitive to network latency. The round-trip time between the most distant nodes will set the baseline for [transaction commit latency](../galera-management/performance-tuning/flow-control-in-galera-cluster.md#flow-control-sequence). High latency affects writes. |
| Network Stability | The WAN link must be stable and reliable. Frequent [network partitions](../high-availability/understanding-quorum-monitoring-and-recovery.md#understanding-and-recovering-from-a-split-brain) can lead to nodes being evicted from the cluster, impacting stability.                      |
| Segments          | Nodes within the same location can be configured into a segment using the `gmcast.segment` [parameter](../galera-management/configuration/configuring-mariadb-galera-cluster.md#network-ports), optimizing communication by using the fast local network for replication.                 |

## Two-Node Cluster with a Galera Arbitrator

This is a special deployment variant used to achieve high availability with only two full data nodes.

### Topology

The cluster consists of two MariaDB Galera nodes and one lightweight [Galera Arbitrator (`garbd`)](../high-availability/understanding-quorum-monitoring-and-recovery.md#the-galera-arbitrator-garbd) process, which runs on a third, separate machine.

### Purpose:

Cost-Effective High Availability: It provides automatic failover for a two-node cluster without the resource cost of a third full database server.

### How it Works

The Galera Arbitrator acts as a voting member for quorum calculations but does not store any data or handle any client traffic. This creates a 3-member cluster from a voting perspective. If one of the data nodes fails, the remaining data node and the arbitrator still form a majority (2 out of 3), allowing the cluster to maintain quorum and stay online.

### Key Consideration

If the node running the arbitrator fails, the cluster reverts to a standard 2-node setup with no automatic failover capability. Therefore, the arbitrator itself should be [monitored](../high-availability/monitoring-mariadb-galera-cluster.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
