---
description: >-
  Overview of the six Grafana dashboards Enterprise Manager provides for
  GridGain 8 clusters, how to open them, and what they need to show data.
hidden: true
---

# GridGain 8 Cluster

MariaDB Enterprise Manager includes six Grafana dashboards for GridGain 8 clusters. They are provisioned automatically in the **GridGain Cluster** folder in Grafana, separate from the **MariaDB Server and MaxScale** folder.

| Dashboard                                               | What it covers                                                                                           | Default time range |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------ |
| [Cluster](cluster.md)                                   | Overall cluster health: state, topology, partition redundancy, JVM, transactions, SQL, and thread pools  | 1 hour             |
| [Compute](compute.md)                                   | Compute job states, timings, and the thread pool that runs compute jobs                                  | 1 hour             |
| [Node](node.md)                                         | Everything about one node: memory, CPU, data region, storage, communication, and workload               | 1 hour             |
| [Persistence](persistence.md)                           | Data volume against disk footprint, checkpoints, the write-ahead log (WAL), and write throttling         | 3 hours            |
| [Caches](caches.md)                                     | Per-cache throughput, size, transactions, and hit and rollback ratios                                    | 1 hour             |
| [Data Center Replication](data-center-replication.md)   | Replication to and from remote data centers: throughput, backlog, and latency                            | 1 hour             |

## Requirements

The dashboards show data only after the cluster sends its metrics to Enterprise Manager. To configure this, see [Add a GridGain 8 Cluster](../../../../administration/deployment/adding-databases/add-gridgain-8-cluster.md#send-cluster-metrics-to-enterprise-manager).

The [Caches](caches.md) dashboard also needs cache statistics enabled for each cache (`statisticsEnabled=true` in the cache configuration).

## Opening the Dashboards

In the **Databases** list, click the three-dot menu (⋮) next to a GridGain 8 cluster and select **View monitoring dashboard** to open the [Cluster](cluster.md) dashboard for that cluster. Use the quick-action icon next to a node name to open the [Node](node.md) dashboard for that node. These actions appear once the cluster or node is reporting metrics.

Every GridGain 8 dashboard has a **GridGain Dashboards** menu that opens the other five dashboards with the same cluster, node, and time range selected.

## Filters

| Filter          | Dashboards          | Description                                                                                 |
| --------------- | ------------------- | ------------------------------------------------------------------------------------------- |
| **Database**    | All                 | The cluster, shown as `gridgain/<cluster name>`.                                            |
| **Instance**    | Node                | The node, identified by its consistent ID.                                                  |
| **Data region** | Node, Persistence   | The data region. The list contains every data region the cluster reports.                   |

## How Node Status Is Determined

GridGain 8 nodes push their metrics to Enterprise Manager. A node that stops reporting would otherwise keep showing its last values as current, so the dashboards treat a node as offline when it has not reported for 30 seconds:

* Status tiles show **N/A** when no node in scope is reporting. N/A means the cluster or the metrics pipeline has stopped.
* Node tables and state timelines show the node as **OFFLINE**.

GridGain 8 metrics carry no node name or host name, so tables and legends identify nodes by their consistent ID.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
