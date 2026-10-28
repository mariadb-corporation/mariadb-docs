---
description: >-
  Complete Galera Cluster reference: active-active multi-primary replication,
  IST vs SST (gcache.size), galera_new_cluster bootstrap, pc.bootstrap recovery.
---

# What is MariaDB Galera Cluster?

_MariaDB Galera Cluster is a Linux-exclusive, multi-primary cluster designed for MariaDB, offering features such as active-active topology, read/write capabilities on any node, automatic membership and node joining, true parallel replication at the row level, and direct client connections, with an emphasis on the native MariaDB experience._

## About

![galera\_small](../.gitbook/assets/1.PNG)

MariaDB Galera Cluster is a [virtually synchronous](about-galera-replication.md) multi-primary cluster for MariaDB. It is available on Linux only and only supports the [InnoDB storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-storage-engine-introduction) (although there is experimental support for [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine) and, from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6), [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria). See the [wsrep\_replicate\_myisam](../reference/galera-cluster-system-variables.md#wsrep_replicate_myisam) system variable, or, from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6), the [wsrep\_mode](../reference/galera-cluster-system-variables.md#wsrep_mode) system variable.

## Features

* [Virtually synchronous replication](about-galera-replication.md)
* Active-active multi-primary topology
* Read and write to any cluster node
* Automatic membership control: failed nodes drop from the cluster
* Automatic node joining
* True parallel replication, on row level
* Direct client connections, native MariaDB look & feel

## Benefits

The above features yield several benefits for a DBMS clustering solution, including:

* Minimal replica lag
* Protection against single-node data loss
* Read scalability
* Smaller client latencies

The [Getting Started with MariaDB\
Galera Cluster](../galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster.md) page has instructions on how to get up and running with MariaDB Galera Cluster.

A great resource for Galera users is [Codership on Google Groups](https://groups.google.com/forum/?fromgroups#!forum/codership-team) (_`codership-team`_ _`'at'`_ _`googlegroups`_ _`(dot)`_ _`com`_) - If you use Galera, it is recommended you subscribe.

## Galera Versions

MariaDB Galera Cluster is powered by:

* MariaDB Server.
* The [Galera wsrep provider library](https://github.com/codership/galera/).

The functionality of MariaDB Galera Cluster can be obtained by installing the standard MariaDB Server packages and the [Galera wsrep provider library](https://github.com/codership/galera/) package. MariaDB Galera Cluster uses [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4. This means that the wsrep API version is 26 and the [Galera wsrep provider library](https://github.com/codership/galera/) is version 4.X.

See [Versioning Information](https://web.archive.org/web/20190722120303/https://galeracluster.com/library/documentation/versioning-information.html) for more information about how to interpret these version numbers.

### Galera 4 Versions

The Galera 4 wsrep provider package is called `galera-4` when you install it with [yum]({server}/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum), [apt]({server}/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files), or [zypper]({server}/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper).

For the provider version that each MariaDB Server release ships with, see [Galera wsrep Provider Versions](../reference/galera-wsrep-provider-versions.md).

## Cluster Failure and Recovery Scenarios

While a Galera Cluster is designed for high availability, various scenarios can lead to node or cluster outages. This guide describes common failure situations and the procedures to safely recover from them.

### Graceful Shutdown Scenarios

This covers situations where nodes are intentionally stopped for maintenance or configuration changes, based on a three-node cluster.

#### **One Node is Gracefully Stopped**

When one node is stopped, it sends a message to the other nodes, and the cluster size is reduced. Properties like Quorum calculation are automatically adjusted. As soon as the node is started again, it rejoins the cluster based on its `wsrep_cluster_address` variable.

If the write-set cache (`gcache.size`) on a donor node still has all the transactions that were missed, the node will rejoin using a fast Incremental State Transfer (IST). If not, it will automatically fall back to a full State Snapshot Transfer (SST).

#### **Two Nodes Are Gracefully Stopped**

The single remaining node forms a Primary Component and can serve client requests. To bring the other nodes back, you simply start them.

However, the single running node must act as a Donor for the state transfer. During the SST, its performance may be degraded, and some load balancers may temporarily remove it from rotation. For this reason, it's best to avoid running with only one node.

#### **All Three Nodes Are Gracefully Stopped**

When the entire cluster is shut down, you must bootstrap it from the most advanced node to prevent data loss.

1. Identify the most advanced node: On each server, check the `seqno` value in the `/var/lib/mysql/grastate.dat` file. The node with the highest `seqno` was the last to commit a transaction.
2.  Bootstrap from that node: Use the appropriate MariaDB script to start a new cluster from this node only.

    Bash

    ```
    galera_new_cluster
    ```
3. Start the other nodes normally: Once the first node is running, start the MariaDB service on the other nodes. They will join the new cluster via SST.

### Unexpected Node Failure (Crash) Scenarios

This covers situations where nodes become unavailable due to a power outage, hardware failure, or software crash.

#### **One Node Disappears from the Cluster**

If one node crashes, the two remaining nodes will detect the failure after a timeout period and remove the node from the cluster. Because they still have Quorum (2 out of 3), the cluster continues to operate without service disruption. When the failed node is restarted, it will rejoin automatically as described above.

#### **Two Nodes Disappear from the Cluster**

The single remaining node cannot form a Quorum by itself. It will switch to a non-Primary state and refuse to serve queries to protect data integrity. Any query attempt will result in an error:

```
ERROR 1047 (08S01): WSREP has not yet prepared node for application use
```

Recovery:

* If the other nodes come back online, the cluster will re-form automatically.
*   If the other nodes have permanently failed, you must manually force the remaining node to become a new Primary Component. Warning: Only do this if you are certain the other nodes are permanently down.

    ```sql
    SET GLOBAL wsrep_provider_options='pc.bootstrap=true';
    ```

{% hint style="info" %}
If the [wsrep\_provider plugin](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-replication-cluster-plugins/wsrep_provider) is enabled, `SET GLOBAL wsrep_provider_options` fails. Run `SET GLOBAL wsrep_provider_pc_bootstrap=ON;` instead. See [pc.bootstrap](../reference/wsrep-variable-details/wsrep_provider_options.md#pc.bootstrap).
{% endhint %}

#### **All Nodes Go Down Without a Proper Shutdown**

In a datacenter power failure or a severe bug, all nodes may crash. The `grastate.dat` file will not be updated correctly and will show `seqno: -1`.

**Recovery:**

1.  On each node, run `mysqld` with the `--wsrep-recover` option. This will read the database logs and report the node's last known transaction position (GTID).

    Bash

    ```
    mysqld --wsrep-recover
    ```
2. Compare the sequence numbers from the recovered position on all nodes.
3. On the node with the highest sequence number, edit its `/var/lib/mysql/grastate.dat` file and set `safe_to_bootstrap: 1`.
4. Bootstrap the cluster from that node using the `galera_new_cluster` command.
5. Start the other nodes normally.

### Recovering from a Split-Brain Scenario

A split-brain occurs when a network partition splits the cluster, and no resulting group has a Quorum. This is most common with an even number of nodes. All nodes will become non-Primary.

**Recovery:**

1. Choose one of the partitioned groups to become the new Primary Component.
2.  On one node within that chosen group, manually force it to bootstrap:

    ```sql
    SET GLOBAL wsrep_provider_options='pc.bootstrap=true';
    ```
3. This group will now become operational. When network connectivity is restored, the nodes from the other partition will automatically detect this Primary Component and rejoin it.

{% hint style="info" %}
If the [wsrep\_provider plugin](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-replication-cluster-plugins/wsrep_provider) is enabled, `SET GLOBAL wsrep_provider_options` fails. Run `SET GLOBAL wsrep_provider_pc_bootstrap=ON;` instead. See [pc.bootstrap](../reference/wsrep-variable-details/wsrep_provider_options.md#pc.bootstrap).
{% endhint %}

{% hint style="danger" %}
Never execute the bootstrap command on both sides of a partition. This will create two independent, active clusters with diverging data, leading to severe data inconsistency.
{% endhint %}

## See Also

* [Codership on Google Groups](https://groups.google.com/forum/?fromgroups#!forum/codership-team) (`codership-team 'at' googlegroups (dot) com`) - A great mailing list for Galera users.
* [About Galera Replication](about-galera-replication.md)
* [Codership: Using Galera Cluster](https://codership.com/content/using-galera-cluster)
* [Galera Use Cases](../galera-use-cases.md)
* [Getting Started with MariaDB Galera Cluster](../galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster.md)
* [MariaDB Galera Cluster - Known Limitations](../reference/mariadb-galera-cluster-known-limitations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
