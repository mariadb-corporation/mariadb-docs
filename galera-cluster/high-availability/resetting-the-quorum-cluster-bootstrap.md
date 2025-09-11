# Resetting the Quorum (Cluster Bootstrap)

{% hint style="info" %}
_This page provides a step-by-step guide for an emergency recovery procedure. For a general overview of what Quorum is and how to monitor it, see_ [_Understanding Quorum, Monitoring, and Recovery._](understanding-quorum-monitoring-and-recovery.md)
{% endhint %}

When a network failure or a crash affects over half of your cluster nodes, the cluster might lose its [Primary Component](understanding-quorum-monitoring-and-recovery.md#primary-component). In such cases, the remaining nodes may return an `Unknown command` error for many queries. This behavior is a safeguard to prevent data inconsistency.

You can confirm this by checking the `wsrep_cluster_status` [variable](../reference/galera-cluster-status-variables.md#wsrep_cluster_status) on all nodes:

```sql
SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';
```

If none of your nodes return a value of `Primary`, you must manually intervene to reset the Quorum and bootstrap a new Primary Component.

## Find the Most Advanced Node

Before you can reset the Quorum, you must identify the most advanced node in the cluster. This is the node whose local database committed the last [transaction](../galera-architecture/certification-based-replication.md). Starting the cluster from any other [node](recovering-a-primary-component.md) can result in data loss.

### The "Safe-to-Bootstrap" Feature

To facilitate a safe restart and prevent an administrator from choosing the wrong node, modern versions of Galera Cluster include a ["Safe-to-Bootstrap" feature](understanding-quorum-monitoring-and-recovery.md#recovering-from-a-full-cluster-shutdown).

When a cluster is shut down gracefully, the last node to be stopped will be the most up-to-date. Galera tracks this and marks only that last node as safe to bootstrap from by setting a flag in its state file. If you attempt to bootstrap from a node marked as unsafe, Galera will refuse and show a message in the logs. In the case of a sudden, simultaneous crash, all nodes will be considered unsafe, requiring manual intervention.

### Procedure for Selecting the Right Node

The procedure to select the right node depends on how the cluster was stopped.

#### Orderly Cluster Shutdown

In the case of a planned, orderly shutdown, you only need to follow the recommendation of the "Safe-to-Bootstrap" feature. On each node, inspect the `/var/lib/mysql/grastate.dat` [file](recovering-a-primary-component.md#manual-bootstrap-using-grastate.dat) and look for the one where `safe_to_bootstrap: 1` is set.

```toml
# GALERA saved state
version: 2.1
uuid:    9acf4d34-acdb-11e6-bcc3-d3e36276629f
seqno:   15
safe_to_bootstrap: 1
```

Use this node for the bootstrap.

#### Full Cluster Crash

In the case of a hard crash, all nodes will likely have `safe_to_bootstrap: 0`. You must therefore manually determine which node is the most advanced.

1.  On each node, run the `mysqld` daemon with the `--wsrep-recover` option. This will read the InnoDB storage engine logs and report the last known transaction position in the MariaDB error log.

    ```log
    mysqld --wsrep-recover
    ```
2.  Inspect the error log for a line similar to this:

    ```ini
    ...
    [Note] WSREP: Recovered position: 37bb872a-ad73-11e6-819f-f3b71d9c5ada:345628
    ...
    ```
3. Compare the sequence number (the number after the colon) from all nodes. The node with the highest sequence number is the most advanced.
4. On that most advanced node, you can optionally edit the `/var/lib/mysql/grastate.dat` file and set `safe_to_bootstrap: 1` to signify that you have willfully chosen this node.

## Bootstrap the New Primary Component

Once you have identified the most advanced node, there are two methods to bootstrap the new Primary Component from it.

### Automatic Bootstrap (Recommended)

This method is recommended if the `mysqld` process is still running on the most advanced node. It is non-destructive and can preserve the [GCache](rapid-node-recovery-with-ist-and-the-gcache.md#the-write-set-cache-gcache), increasing the chance of a fast [Incremental State Transfer (IST)](rapid-node-recovery-with-ist-and-the-gcache.md#incremental-state-transfer-ist) for the other nodes.

To perform an automatic bootstrap, connect to the most advanced node with a [`mariadb` client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) and execute:

```sql
SET GLOBAL wsrep_provider_options='pc.bootstrap=YES';
```

This node will now form a new Primary Component by itself.

### Manual Bootstrap

This method involves a [full shutdown](recovering-a-primary-component.md#manual-bootstrap-using-grastate.dat) and a special startup of the most advanced node.

1. Ensure the `mysqld` service is stopped on all nodes in the cluster.
2.  On the most advanced node only, start the cluster using the [bootstrap script](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#bootstrap):

    Bash

    ```
    galera_new_cluster
    ```

### Start the Remaining Nodes

After the first node is successfully running and has formed the new Primary Component, start the MariaDB service normally on all of the other nodes.

```bash
systemctl start mariadb
```

They will detect the existing Primary Component, connect to it, and automatically initiate a [State Transfer](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) to synchronize their data and rejoin the cluster.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
