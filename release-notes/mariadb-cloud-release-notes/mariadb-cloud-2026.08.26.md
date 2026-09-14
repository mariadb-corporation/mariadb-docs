---
description: >-
  Release notes for MariaDB Cloud Enterprise Cluster general availability,
  covering the synchronous replication topology on the PowerPlus tier,
  cluster-aware monitoring and alerts, and snapshot backups with
  point-in-time recovery.
icon: rocket-launch
---

# MariaDB Cloud 2026.08.26 Release Notes

**Release Date:** 26 August 2026

MariaDB Enterprise Cluster is now generally available on MariaDB Cloud. It was previously offered as a Tech Preview.

## New Features

### Enterprise Cluster on the PowerPlus tier

Enterprise Cluster is a deployment topology that uses synchronous replication with write-set certification, so a transaction is committed on every node or none. It is intended for workloads that require strict data consistency and zero-data-loss failover, rather than the asynchronous primary/replica model used by Replicated services.

* Available to services on the PowerPlus tier, in Amazon Web Services, Google Cloud, and Microsoft Azure.
* A cluster consists of 3 to 5 nodes to maintain quorum. A single-node option is available for development and test use.
* MariaDB MaxScale routes all write traffic to a single active writer node and load-balances reads across the remaining nodes.
* Multi-node clusters can be distributed across multiple Availability Zones within a cloud region.
* Enterprise Cluster is presented as a distinct topology alongside Single Node and Replicated, and can be provisioned and scaled from the Portal and the REST API.

For details, see [Enterprise Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd/quickstart/enterprise-cluster).

### Cluster-aware monitoring and alerts

The Portal now includes Galera-specific monitoring for Enterprise Cluster services:

* Panels for flow control pause time, flow control messages sent, replication queue depth, write conflicts, maximum replication latency, transaction rate, and write-set traffic.
* A **Galera** service dashboard with a **Galera Nodes** panel, reporting each node's status, whether it accepts queries, its local state, flow control state, cluster status, and connection state.
* Cluster state is reflected in the service topology status.

Four alerts are available for Enterprise Cluster services. They are not enabled by default: add them to an alert policy from the Portal, after which they can be delivered through your configured notification channels:

| Alert | Severity | Condition |
| ----- | -------- | --------- |
| Galera cluster down | Critical | The cluster is not in the Primary state, or the node is not ready, for 5 minutes. |
| Galera node not ready | Warning | The node is not in the Synced state for 5 minutes, and the change is not a temporary desync. |
| Galera node in an unexpected state | Critical | The node's state is not one of Synced, Donor/Desynced, Joining, Joined, or Waiting for SST, for 5 minutes. |
| Galera donor lagging | Warning | A donor node's receive queue exceeds 100 for 5 minutes, indicating it is falling behind. |

### Backup and restore

* Enterprise Cluster uses cloud-native snapshot backups. Because the cluster maintains write-set consistency, a snapshot taken from any single healthy node represents the state of the whole cluster.
* Point-in-time recovery is supported between snapshots, in the same way as for a Replicated service.
* Restores are initialized on a single node to bootstrap the cluster, after which MariaDB Cloud brings the remaining nodes online using State Snapshot Transfers.

## Limitations

* Full (physical) backups and logical backups are not available for the Enterprise Cluster topology.
* Terraform Provider support is not currently available for Enterprise Cluster.
* Unsafe or highly sensitive `wsrep_` configuration variables are system-managed. A curated subset is exposed through the Configuration Manager.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
