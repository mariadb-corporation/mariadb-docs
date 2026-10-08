---
description: >-
  Details the pre-configured rules for monitoring MariaDB Server, Galera
  Cluster, MaxScale, GridGain 8 clusters, and system health, including
  sustained-duration triggers to prevent alert fatigue.
---

# Built-in Alert Rules

MariaDB Enterprise Manager includes a comprehensive set of pre-configured alert rules to provide production-ready monitoring for your entire database stack out-of-the-box. These alerts are built on the integrated Grafana Alerting engine and are designed to detect common issues across your MariaDB Servers, Galera Clusters, MaxScale instances, GridGain 8 clusters, and the underlying operating systems.

A key feature of these rules is the use of a **"sustained for"** duration. This means a condition must remain true for a specified period (e.g., 3 minutes) before an alert will fire. This prevents alert fatigue from brief, transient spikes and ensures you are only notified of persistent, actionable problems.

## MariaDB Server

| Alert name                        | Description                                                                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MariadbInstanceDown**           | MariaDB instance down for 3 minutes (sustained for 3m). Triggers when the exporter reports the instance as down (`mariadb_up = 0`) **or** when no sample from `mariadb_up` has been received for more than 120 seconds. |
| **ReplicaProcessDown**            | MariaDB instance has a Replica process Down (sustained for 3m). Triggers when replication is unhealthy: the I/O or SQL thread is stopped, **or** `Seconds_Behind_Master` is missing (replica not reporting progress).   |
| **ReplicaSecondsBehindPrimary**   | MariaDB replica is more than 600s behind primary (sustained for 3m). Triggers when replication lag exceeds 600 seconds.                                                                                                 |
| **HighUtilizationMaxConnections** | MariaDB instance has high connection utilization (sustained for 5m). Triggers when `Threads_connected` exceeds \~80% of `max_connections`.                                                                              |
| **MariaDBInstanceRestart**        | MariaDB instance restarted recently (sustained for 5m). Triggers when server uptime is below 1 hour, indicating a recent restart.                                                                                       |
| **MariaDBDeadlockFound**          | MariaDB Deadlock found in the last 15m (sustained for 5m). Triggers when the count of InnoDB deadlocks increases compared to 15 minutes ago.                                                                            |

## Galera Cluster

| Alert name                          | Description                                                                                                                                                                                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GaleraClusterDown**               | Galera instance down for 5 minutes (sustained for 5m). Triggers when the cluster is not in Primary state (`wsrep_cluster_status ≠ 1`) **or** the node is not ready (`wsrep_ready ≠ 1`).                   |
| **GaleraNodeNotReady**              | Galera node not ready (state ≠ 4) for 5m (sustained for 5m). Triggers when the node is not in **Synced** state and it’s **not** a temporary DESYNC (desync counter did not change in the last 5 minutes). |
| **GaleraInWrongState**              | Galera instance is in an unexpected state (sustained for 5m). Triggers when the node’s state comment isn’t one of the normal values (Synced / Donor / Joining / Joined / Waiting for SST).                |
| **GaleraClusterDonorFallingBehind** | Galera donor lagging (recv queue > 100) for 5m (sustained for 5m). Triggers when a **Donor** node (state=2) accumulates a large receive queue, indicating it’s falling behind replication.                |
| **GaleraClusterSizeChanged**        | Galera cluster size changed in last 15m (sustained for 5m). Triggers when the cluster size **increases** within 15 minutes.                                                                               |

## MaxScale

| Alert name               | Description                                                                                                                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MaxScaleInstanceDown** | MaxScale down for 3 minutes (sustained for 3m). Triggers when **no recent MaxScale metrics** have been received for more than 120 seconds (e.g., MaxScale down or exporter/scrape pipeline issue). |
| **MaxScaleNoPrimary**    | MaxScale has no primary for 3 minutes (sustained for 3m). Triggers when MaxScale reports **zero servers with role = Primary/Master**.                                                              |

## Node/OS

| Alert name                         | Description                                                                                                                                                                                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NodeFilesystemSpaceUsage**       | Filesystem disk space is above 90% (sustained for 1h). Triggers when disk space used exceeds 90% on a writable filesystem.                                                                                                              |
| **NodeFilesystemSpaceFillingUp**   | Filesystem predicted to run out of space within \~24h (sustained for 1h). Triggers when usage is above 80% **and** the trend (predictive model) indicates free space will reach zero within \~24 hours; excludes read-only filesystems. |
| **NodeMemoryHighUtilization**      | Instance is running out of memory > 95% (sustained for 15m). Triggers when memory utilization exceeds 95%.                                                                                                                              |
| **NodeCPUHighUtilization**         | Instance is running out of CPU > 90% (sustained for 15m). Triggers when CPU utilization exceeds 90% over a 5-minute window.                                                                                                             |
| **NodeFilesystemAlmostOutOfFiles** | Filesystem has less than 3% inodes left (sustained for 1h). Triggers when available inodes drop below 3% on a writable filesystem.                                                                                                      |
| **NodeNetworkReceiveErrs**         | Network interface has a high receive-error rate (sustained for 1h). Triggers when receive errors exceed **1%** of total received packets over a 2-minute rate window.                                                                   |
| **NodeFileDescriptorLimit**        | Kernel is predicted to exhaust file descriptors soon (sustained for 15m). Triggers when allocated file descriptors exceed **70%** of the kernel limit.                                                                                  |
| **NodeFileDescriptorLimit**        | Kernel is close to exhausting file descriptors (sustained for 15m). Triggers when allocated file descriptors exceed **90%** of the kernel limit.                                                                                        |

## GridGain 8 Cluster

GridGain 8 alert rules are provisioned in the **GridGain Cluster** folder in Grafana and are evaluated every minute. In a notification, the cluster is identified as `gridgain/<cluster tag>` and the node by its consistent ID.

GridGain 8 nodes push their metrics to Enterprise Manager rather than being scraped, so availability rules detect a node that stops reporting rather than an exporter that reports the node as down.

### Cluster and Nodes

| Alert name                       | Description                                                                                                                                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **GridGainNodeDown**             | GridGain node stopped reporting for 3 minutes (sustained for 3m). Triggers when no metrics have been received from a node for more than 120 seconds. A node that stays silent for more than about 5 minutes drops out of the query, and the alert resolves. |
| **GridGainClusterInactive**      | GridGain cluster is not active (sustained for 3m). Triggers when a node reports the cluster as inactive (deactivated).                                                                                                                            |
| **GridGainFailedNodes**          | GridGain cluster has failed nodes (sustained for 5m). Triggers when cluster discovery reports one or more failed nodes, meaning nodes dropped out of the topology.                                                                                 |
| **GridGainServerNodesDecreased** | GridGain server node count decreased (sustained for 5m). Triggers when the cluster has fewer server nodes than 15 minutes ago.                                                                                                                      |
| **GridGainServerNodesIncreased** | GridGain server node count increased (sustained for 5m). Triggers when the cluster has more server nodes than 15 minutes ago.                                                                                                                      |
| **GridGainNodeRestart**          | GridGain node restarted recently (sustained for 5m). Triggers when node uptime is below 1 hour, indicating a recent restart.                                                                                                                       |
| **GridGainNodeNotInBaseline**    | GridGain server node is not in the baseline topology (sustained for 15m). Triggers when a running node is not part of the cluster's baseline topology.                                                                                            |
| **GridGainCoordinatorChanged**   | GridGain cluster coordinator changed (sustained for 1m). Triggers when the coordinator role moved to another node within the last 10 minutes.                                                                                                     |

### Partitions and Partition Map Exchange

| Alert name                          | Description                                                                                                                                                                                                                         |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GridGainPartitionsWithoutCopies** | GridGain cache group has partitions with no copies (sustained for 10m). Triggers when a cache group has partitions with no copy on any node, which means the data in those partitions is lost. Only cache groups that reported a copy count within the last hour are evaluated. |
| **GridGainNoPartitionBackups**      | GridGain cache group is running without partition backups (sustained for 15m). Triggers when a cache group keeps only one copy of each partition.                                                                                     |
| **GridGainRebalanceInProgress**     | GridGain cache group is rebalancing (sustained for 5m). Triggers when partitions of a cache group have been moving between nodes during the last 35 minutes.                                                                         |
| **GridGainPmeInProgress**           | GridGain cluster ran a partition map exchange (sustained for 1m). Triggers when the cluster ran a partition map exchange (PME) within the last 10 minutes.                                                                            |
| **GridGainPmeTooLong**              | GridGain partition map exchange took over 10 seconds (sustained for 5m). Triggers when a PME within the last 10 minutes lasted longer than 10 seconds.                                                                               |
| **GridGainPmeHung**                 | GridGain partition map exchange looks hung (sustained for 5m). Triggers when a PME within the last 10 minutes lasted longer than 60 seconds, which can block the cluster.                                                            |

### Memory and Data Regions

| Alert name                               | Description                                                                                                                                                                                       |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GridGainHeapHighUtilization**          | GridGain node heap usage above 90% (sustained for 15m). Triggers when used Java heap exceeds 90% of the maximum heap. Nodes without a maximum heap size are not evaluated.                        |
| **GridGainSqlOutOfMemory**               | GridGain SQL queries failed out of memory (sustained for 5m). Triggers when SQL queries on a node failed with an out-of-memory error within the last 15 minutes.                                  |
| **GridGainSqlFreeMemoryLow**             | GridGain SQL free memory below 10% (sustained for 5m). Triggers when free SQL query memory drops below 10% of the node's SQL memory quota. Nodes with the quota disabled are not evaluated.         |
| **GridGainDataRegionUtilizationWarning** | GridGain data region above 80% utilization (sustained for 5m). Triggers when off-heap memory used by a data region exceeds 80% of the region's maximum size.                                        |
| **GridGainDataRegionUtilizationAverage** | GridGain data region above 90% utilization (sustained for 5m). Triggers when off-heap memory used by a data region exceeds 90% of the region's maximum size.                                        |
| **GridGainDataRegionUtilizationHigh**    | GridGain data region above 95% utilization (sustained for 5m). Triggers when off-heap memory used by a data region exceeds 95% of the region's maximum size; page eviction or out-of-memory errors are likely next. |
| **GridGainPageEviction**                 | GridGain node is evicting pages from a data region (sustained for 5m). Triggers when a node evicts pages from a data region.                                                                      |

### Persistence

| Alert name                                     | Description                                                                                                                                                                                                  |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **GridGainCheckpointTooSlow**                  | GridGain checkpoint duration above 3 minutes (sustained for 5m). Triggers when a checkpoint within the last 5 minutes took longer than 3 minutes.                                                             |
| **GridGainCheckpointDutyCycleHigh**            | GridGain node spends over 60% of its time checkpointing (sustained for 15m). Triggers when checkpointing takes up more than 60% of a node's time over a 5-minute window.                                     |
| **GridGainCheckpointBufferUtilizationWarning** | GridGain checkpoint buffer above 66% utilization (sustained for 5m). Triggers when a data region's checkpoint buffer is more than 66% full, meaning writes are outpacing checkpointing.                    |
| **GridGainCheckpointBufferUtilizationHigh**    | GridGain checkpoint buffer above 80% utilization (sustained for 5m). Triggers when a data region's checkpoint buffer is more than 80% full; write throttling is imminent.                                    |
| **GridGainWalArchiveNotDraining**              | GridGain WAL archive is not draining (sustained for 15m). Triggers when the number of WAL archive segments is higher than 30 minutes earlier, meaning the archive has grown for 45 minutes without being reclaimed. |

### CPU, JVM, and Thread Pools

| Alert name                           | Description                                                                                                                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GridGainCpuHigh**                  | GridGain node CPU above 90% (sustained for 15m). Triggers when a node's CPU load exceeds 90%.                                                                                |
| **GridGainGcCpuHigh**                | GridGain node GC CPU above 50% (sustained for 15m). Triggers when garbage collection uses more than 50% of a node's CPU.                                                     |
| **GridGainLongJvmPauses**            | GridGain node had long JVM pauses (sustained for 5m). Triggers when a node records new long JVM pauses, such as stop-the-world garbage collection, within the last 10 minutes. |
| **GridGainThreadCountHigh**          | GridGain node is running over 1000 threads (sustained for 5m). Triggers when a node's thread count exceeds 1000.                                                              |
| **GridGainStripedExecutorQueueHigh** | GridGain striped executor queue above 1000 (sustained for 5m). Triggers when more than 1000 tasks are queued in a node's striped executor, meaning cache operations are queuing. |
| **GridGainThreadPoolQueueHigh**      | GridGain thread pool queue above 1000 (sustained for 5m). Triggers when more than 1000 tasks are queued in any thread pool on a node.                                         |
| **GridGainComputeQueueGrowing**      | GridGain compute execution queue above 100 (sustained for 10m). Triggers when more than 100 jobs are queued in a node's compute execution pool.                              |
| **GridGainRejectedComputeJobs**      | GridGain compute jobs rejected (sustained for 5m). Triggers when a node rejected compute jobs within the last 10 minutes.                                                     |

### Caches and Transactions

| Alert name                                | Description                                                                                                                                                         |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GridGainCacheRollbackRatioHigh**        | GridGain cache rolled back more transactions than it committed (sustained for 15m). Triggers when, over 15 minutes, a cache rolled back more transactions than it committed. |
| **GridGainCacheNoSuccessfulTransactions** | GridGain cache committed no transactions while rolling back (sustained for 15m). Triggers when, over 15 minutes, a cache rolled back transactions and committed none.  |
| **GridGainCacheAllEntriesInHeap**         | GridGain cache holds every entry on heap (sustained for 15m). Triggers when every entry of a cache is held in the Java heap.                                        |

{% hint style="info" %}
The cache rules rely on cache statistics. They stay silent for caches created without `statisticsEnabled=true`.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
