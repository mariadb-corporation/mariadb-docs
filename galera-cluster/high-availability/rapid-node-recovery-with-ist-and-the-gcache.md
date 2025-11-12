# Rapid Node Recovery with IST and the GCache

{% hint style="info" %}
This page provides a deep-dive into Incremental State Transfer (IST), a method for a node to synchronize with the cluster. For information on a fallback mechanism, see [State Snapshot Transfers (SSTs)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md).
{% endhint %}

## Incremental State Transfer (IST)

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

{% tabs %}
{% tab title="seqno is found" %}
The donor has the necessary history. It streams all subsequent write-sets from its GCache to the joiner. The joiner applies them in order and quickly becomes [Synced](monitoring-mariadb-galera-cluster.md#understanding-galera-node-states).
{% endtab %}

{% tab title="seqno is NOT found" %}
The node was disconnected for too long, and the required history has been purged from the cache. IST is not possible, and an SST is initiated.
{% endtab %}
{% endtabs %}

### Configuring the GCache

You can control the GCache behavior with several [parameters](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.dir) in the `[galera]` section of your configuration file (`my.cnf`).

| Parameter                                                                                      | Description                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [gcache.size](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.size)       | Controls the size of the on-disk ring-buffer file. A larger GCache can hold more history, increasing the chance of a fast IST over SST.                                                                                                                                                          |
| [gcache.dir](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.dir)         | Specifies where GCache files are stored. Best practice is to place it on the fastest available storage like SSD or NVMe.                                                                                                                                                                         |
| [gcache.recover](../reference/wsrep-variable-details/wsrep_provider_options.md#gcache.recover) | Enabled by default in [modern Galera versions](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104#galera-4), it allows a node to recover its GCache post-restart, enabling immediate service as a donor for IST. |

### Tuning `gcache.size`

The `gcache.size` parameter is the most critical setting for ensuring nodes can use IST. A GCache that is too small is the most common reason for a cluster falling back to a full SST.

The ideal size depends on your cluster's write rate and the amount of downtime you want to tolerate for a node before forcing an SST. For instance, do you want a node that is down for 1 hour for maintenance to recover instantly (IST), or can you afford a full SST?

#### **Calculating Size Based on Write Rate**

The most accurate way to size your GCache is to base it on your cluster's write rate.

{% stepper %}
{% step %}
Find your cluster's write rate:

You can calculate this using the `wsrep_received_bytes` status variable. First, check the value and note the time:

```sql
SHOW STATUS LIKE 'wsrep_received_bytes';
```

```
+------------------------+-----------+
| Variable_name          | Value     |
+------------------------+-----------+
| wsrep_received_bytes   | 6637093   |
+------------------------+-----------+
```

Wait for a significant interval during peak load (e.g., 3600 seconds, or 1 hour). Run the query again:

```sql
SHOW STATUS LIKE 'wsrep_received_bytes';
```

```
+------------------------+-----------+
| Variable_name          | Value     |
+------------------------+-----------+
| wsrep_received_bytes   | 79883093  |
+------------------------+-----------+
```

Now, calculate the rate (bytes per second):

$$
write\_rate = \frac{recv_2 - recv_1}{time_2 - time_1}
$$

* $$\text{Example: } \frac{(79883093 - 6637093) \text{ bytes}}{3600 \text{ seconds}} = 20346 \text{ bytes/sec}$$
{% endstep %}

{% step %}
Calculate your desired GCache size:

Decide on the time window you want to support (e.g., 2 hours = 7200 seconds).

$$
required\_cachesize = write\_rate \times desired\_time\_window\_in\_seconds
$$

* $$\text{Example: } 20346 \text{ bytes/sec} \times 7200 \text{ sec} \approx 146,491,200 \text{ bytes (or } \sim\text{140MiB)}$$&#x20;

In this example, a `gcache.size` of 140M would allow a node to be down for 2 hours and still rejoin using IST.
{% endstep %}

{% step %}
Check your current GCache validity period:

Conversely, you can use your write rate to see how long your _current_ GCache size is valid:

$$
period\_of\_validity\_(seconds) = \frac{current\_gcache.size\_in\_bytes}{write\_rate}
$$
{% endstep %}
{% endstepper %}

#### A General Heuristic for Sizing

If you cannot calculate the write rate, you can use a simpler heuristic based on your data directory size as a starting point.

1. Start with the size of your data directory.
2. Subtract the size of the GCache's ring buffer file itself (default: `galera.cache`).
3. Consider your SST method:
   * If you use `mysqldump` for SST, you can also subtract the size of your InnoDB log files (as `mysqldump` does not copy them).
   * If you use `rsync` or `xtrabackup`, the log files _are_ copied, so they should be part of the total size.

{% hint style="warning" %}
These calculations are guidelines. If your cluster nodes frequently request SSTs, it is a clear sign your `gcache.size` is too small. In cases where you must avoid SSTs as much as possible, you should use a much larger GCache than suggested, assuming you have the available storage.
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
