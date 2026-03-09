---
description: >-
  Details the pre-configured rules for monitoring MariaDB Server, Galera
  Cluster, and system health, including sustained-duration triggers to prevent
  alert fatigue.
---

# Built-in Alert Rules

MariaDB Enterprise Manager includes a comprehensive set of pre-configured alert rules to provide production-ready monitoring for your entire database stack out-of-the-box. These alerts are built on the integrated Grafana Alerting engine and are designed to detect common issues across your MariaDB Servers, Galera Clusters, MaxScale instances, and the underlying operating systems.

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

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
