# Rapid Node Recovery with IST and the GCache

{% hint style="info" %}
This page provides a deep-dive into Incremental State Transfer (IST), a method for a node to synchronize with the cluster. For information on a fallback mechanism, see [State Snapshot Transfers (SSTs)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md).
{% endhint %}

## Incremental State Transfer (IST)?

An Incremental State Transfer (IST) is the fast and efficient process where a joining node receives only the missing [transactions](../galera-architecture/certification-based-replication.md#how-the-process-works) it needs to catch up with the cluster, rather than receiving a full copy of the entire database.

This is the preferred provisioning method because it is:

* Fast: Transferring only the missing changes is significantly faster than copying the entire dataset.
* Non-Blocking: The donor node can continue to serve read and write traffic while an IST is in progress.

### Conditions for IST

IST is an automatic process, but it is only possible if the following conditions are met:

* The joining node has previously been a member of the cluster (its [state UUID](../reference/galera-cluster-status-variables.md#wsrep_local_state_uuid) matches the cluster's).
* All of the [write-sets](../galera-architecture/introduction-to-galera-architecture.md#the-wsrep-api) that the joiner is missing are still available in the donor node's Write-set Cache (GCache).

If these conditions are not met, the cluster automatically falls back to performing a full State Snapshot Transfer (SST).

## The Write-Set Cache (GCache)

The GCache is a special cache on each node whose primary purpose is to store recent write-sets specifically to facilitate Incremental State Transfers. The size and configuration of the GCache are therefore critical for the cluster's recovery speed and [high availability](understanding-quorum-monitoring-and-recovery.md#quorum-calculation).

### How the GCache Enables IST

When a node attempts to rejoin the cluster, it reports the [sequence number (`seqno`)](../galera-architecture/introduction-to-galera-architecture.md#global-transaction-id-gtid) of the last transaction it successfully applied. The potential donor node then checks its GCache for the very next `seqno` in that sequence.

#### If the `seqno` is found in the GCache

The donor has the necessary history. It streams all subsequent write-sets from its GCache to the joiner. The joiner applies them in order and quickly becomes [Synced](monitoring-mariadb-galera-cluster.md#understanding-galera-node-states).

#### If the `seqno` is NOT found in the GCache

The node was disconnected for too long, and the required history has been purged from the cache. IST is not possible, and an SST is initiated.

### Configuring the GCache

You can control the GCache behavior with several [parameters](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.dir) in the `[galera]` section of your configuration file (`my.cnf`).

| Parameter                                                                                      | Description                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [gcache.size](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.size)       | Controls the size of the on-disk ring-buffer file. A larger GCache can hold more history, increasing the chance of a fast IST over SST.                                                                                                                                                          |
| [gcache.dir](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.dir)         | Specifies where GCache files are stored. Best practice is to place it on the fastest available storage like SSD or NVMe.                                                                                                                                                                         |
| [gcache.recover](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.recover) | Enabled by default in [modern Galera versions](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104#galera-4), it allows a node to recover its GCache post-restart, enabling immediate service as a donor for IST. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
