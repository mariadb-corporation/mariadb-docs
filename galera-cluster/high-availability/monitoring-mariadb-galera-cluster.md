# Monitoring MariaDB Galera Cluster

From a [database client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client), you can check the status of [write-set replication](../galera-architecture/introduction-to-galera-architecture.md#the-wsrep-api) throughout the cluster using standard queries. Status variables that relate to write-set replication have the prefix `wsrep_`, meaning that you can display them all using the following query:

```plsql
SHOW GLOBAL STATUS LIKE 'wsrep_%'
```

## Understanding Quorum and Cluster Integrity

The most fundamental aspect of a healthy cluster is [Quorum](understanding-quorum-monitoring-and-recovery.md#advanced-quorum-control). Quorum is a mechanism that ensures data consistency by requiring a majority of nodes to be online and in communication to form a Primary Component. Only the Primary Component will process transactions. This prevents ["split-brain" scenarios](understanding-quorum-monitoring-and-recovery.md#understanding-and-recovering-from-a-split-brain) where a network partition could otherwise lead to data conflicts.

You can check the cluster's integrity and Quorum status using these key variables. For a healthy cluster, the values for these variables must be identical on every node.

| Parameter                  | Description                                                                                                    | Expected Value               |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `wsrep_cluster_status`     | Status of the component the node belongs to. The healthy value is `Primary`. Any other value indicates issues. | `Primary`                    |
| `wsrep_cluster_size`       | Number of nodes in the current component. This should match the expected total nodes in the cluster.           | Matches total expected nodes |
| `wsrep_cluster_state_uuid` | Unique identifier for the cluster's state. It must be consistent across all nodes.                             | Same on all nodes            |
| `wsrep_cluster_conf_id`    | Identifier for the cluster membership group. It must be the same on all nodes.                                 | Same on all nodes            |

## Checking Individual Node Status

You can monitor the status of individual nodes to ensure they are in working order and able to receive write-sets.

| Status Variable             | Description                                                      | Expected Value | Notes                                              |
| --------------------------- | ---------------------------------------------------------------- | -------------- | -------------------------------------------------- |
| `wsrep_ready`               | Indicates if the node can accept queries.                        | `ON`           | If `OFF`, the node will reject almost all queries. |
| `wsrep_connected`           | Indicates if the node has network connectivity with other nodes. | `ON`           | If `OFF`, the node is isolated.                    |
| `wsrep_local_state_comment` | Shows the current node state in a readable format.               | N/A            | Output is human-readable and varies.               |

## Understanding Galera Node States

<div align="left"><figure><img src="../.gitbook/assets/galerafsm.png" alt=""><figcaption></figcaption></figure></div>

The value of `wsrep_local_state_comment` tells you exactly what a node is doing. The most common states include:

| Node Status | Description                                                                                                                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Synced      | The node is a healthy, fully operational, and active member of the cluster.                                                                                                                                 |
| Donor       | The node is providing a [State Snapshot Transfer (SST)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md#sst-methods) to another node; typically read-only. |
| Joining     | The node is establishing a connection and synchronizing with the cluster.                                                                                                                                   |
| Joined      | The node has received a state transfer but is applying transactions to catch up before syncing.                                                                                                             |
| Initialized | The node is not connected to any cluster component.                                                                                                                                                         |

## Checking Replication Health

These [status variables](../reference/galera-cluster-status-variables.md) can help identify performance issues and bottlenecks.&#x20;

{% hint style="warning" %}
Many status variables are differential and reset after each `FLUSH STATUS` command.
{% endhint %}

| Metric Name                  | Description                                                                                                                                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wsrep_local_recv_queue_avg` | Average size of the queue of write-sets waiting to be applied. A value consistently higher than `0.0` indicates falling behind and may trigger [Flow Control](../galera-management/performance-tuning/flow-control-in-galera-cluster.md#monitoring-flow-control). |
| `wsrep_flow_control_paused`  | Fraction of time the node has been paused by Flow Control. A value close to `0.0` is ideal; a high value indicates a performance bottleneck.                                                                                                                      |
| `wsrep_local_send_queue_avg` | Average size of the queue of write-sets waiting to be sent to other nodes. Values much greater than `0.0` can indicate network throughput issues.                                                                                                                 |
| `wsrep_cert_deps_distance`   | Represents the node’s potential for parallel transaction application, helping to optimally tune the `wsrep_slave_threads` [parameter](../reference/galera-cluster-system-variables.md#wsrep_slave_threads).                                                       |

## Recovering a Cluster After a Full Outage

If the entire cluster shuts down or [loses Quorum](resetting-the-quorum-cluster-bootstrap.md#procedure-for-selecting-the-right-node), you must manually re-establish a Primary Component by bootstrapping from the most advanced node.

#### Step 1: Identify the Most Advanced Node

The "most advanced" node is the one that contains the most recent data. You must bootstrap the cluster from this node to avoid any data loss.

1. Log in to each of your database servers.
2. Examine the [`grastate.dat` file](resetting-the-quorum-cluster-bootstrap.md#find-the-most-advanced-node) located in the MariaDB data directory (e.g., `/var/lib/mysql/`).
3. Look for the `seqno:` value in this file. The node with the highest `seqno` is the most advanced node. If a node was shut down gracefully, its `seqno` may be `-1`; these nodes should not be used to bootstrap if a node with a positive `seqno` is available.

#### Step 2: Bootstrap the New Primary Component

Once you have identified the most advanced node, start the MariaDB service only on that node using a special bootstrap procedure using the command:

```bash
galera_new_cluster
```

{% hint style="info" %}
You can start `mariadbd` with the [--wsrep-new-cluster](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#wsrep-new-cluster) option.
{% endhint %}

This node will come online and form a new Primary Component by itself, with a cluster size of 1.

#### Step 3: Start the Other Nodes

After the first node is successfully running as a new Primary Component, start the MariaDB service normally on all of the other nodes.

```bash
systemctl start mariadb
```

They will detect the existing Primary Component, connect to it, and automatically initiate a [State Transfer (IST or SST)](rapid-node-recovery-with-ist-and-the-gcache.md) to synchronize their data and rejoin the cluster.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
