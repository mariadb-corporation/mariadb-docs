# Backing Up a MariaDB Galera Cluster

The recommended strategy for creating a full, consistent backup of a MariaDB Galera Cluster is to perform the backup on a single [node](../../high-availability/monitoring-mariadb-galera-cluster.md#checking-individual-node-status). Because all nodes in a [healthy cluster](../../high-availability/understanding-quorum-monitoring-and-recovery.md) contain the same data, a complete backup from one node represents a snapshot of the entire cluster at a specific point in time.

The preferred tool for this is [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview). `mariadb-backup` creates a "hot" backup without blocking the node from serving traffic for an extended period.

## The Challenge of Consistency in a Live Cluster

While taking a backup, the donor node is still receiving and applying transactions from the rest of the cluster. If the backup process is long, it's possible for the data at the _end_ of the backup to be newer than the data at the _beginning_, leading to an inconsistent state within the backup files.

To prevent this, it's important to temporarily pause the node's replication stream during the backup process.

## Recommended Backup Procedure

This procedure ensures a fully consistent backup with minimal impact on the cluster's availability.

#### 1. Select a Backup Node

Choose a node from your cluster to serve as the backup source. It's a good practice to use a non-primary node if you are directing writes to a single server.

#### 2. Desynchronize the Node (Pause Replication)

To guarantee consistency, you should temporarily pause the node's ability to apply new replicated transactions. This is done by setting the `wsrep_desync` [variable](../../reference/galera-cluster-system-variables.md#wsrep_desync) to `ON`.

1. Take the selected node out of your [load balancer's](../../high-availability/load-balancing/load-balancing-in-mariadb-galera-cluster.md#id-2.-recommended-load-balancer-mariadb-maxscale) rotation so it no longer receives application traffic.
2.  Connect to the node with a `mariadb` client and execute:

    ```sql
    SET GLOBAL wsrep_desync = ON;
    ```

    The node will finish applying any transactions already in its queue and then pause, entering a ["desynced" state](../../high-availability/monitoring-mariadb-galera-cluster.md#understanding-galera-node-states). The rest of the cluster will continue to operate normally.

#### 3. Perform the Backup

With the node's replication paused, run the `mariadb-backup` [command](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#list-of-mariadb-backup-options) to create a full backup.

```bash
mariadb-backup --backup --target-dir=/path/to/backup/ --user=backup_user --password=...
```

#### 4. Resynchronize the Node

Once the backup is complete, you can allow the node to rejoin the cluster's replication stream.

1.  Connect to the node again and execute:

    ```sql
    SET GLOBAL wsrep_desync = OFF;
    ```

    The node will now request an [Incremental State Transfer (IST)](../../high-availability/rapid-node-recovery-with-ist-and-the-gcache.md#incremental-state-transfer-ist) from its peers to receive all the transactions it missed while it was desynchronized and quickly catch up.
2. Once the node is fully synced (you can verify this by checking that [wsrep\_local\_state\_comment](../../reference/galera-cluster-status-variables.md#wsrep_local_state_comment) is [Synced](../../high-availability/monitoring-mariadb-galera-cluster.md#understanding-galera-node-states)), add it back to your load balancer's rotation.

This procedure ensures you get a fully consistent snapshot of your cluster's data with zero downtime for your application.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
