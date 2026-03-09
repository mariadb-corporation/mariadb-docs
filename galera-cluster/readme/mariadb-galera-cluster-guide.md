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

* No replica lag
* No lost transactions
* Read scalability
* Smaller client latencies

The [Getting Started with MariaDB\
Galera Cluster](../galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster.md) page has instructions on how to get up and running with MariaDB Galera Cluster.

A great resource for Galera users is [Codership on Google Groups](https://groups.google.com/forum/?fromgroups#!forum/codership-team) (_`codership-team`_ _`'at'`_ _`googlegroups`_ _`(dot)`_ _`com`_) - If you use Galera, it is recommended you subscribe.

## Galera Versions

MariaDB Galera Cluster is powered by:

* MariaDB Server.
* The [Galera wsrep provider library](https://github.com/codership/galera/).

The functionality of MariaDB Galera Cluster can be obtained by installing the standard MariaDB Server packages and the [Galera wsrep provider library](https://github.com/codership/galera/) package. The following [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) version corresponds to each MariaDB Server version:

* In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) and later, MariaDB Galera Cluster uses [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4. This means that the wsrep API version is 26 and the [Galera wsrep provider library](https://github.com/codership/galera/) is version 4.X.
* In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) and before, MariaDB Galera Cluster uses [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 3. This means that the wsrep API is version 25 and the [Galera wsrep provider library](https://github.com/codership/galera/) is version 3.X.

See [Deciphering Galera Version Numbers](https://galeracluster.com/library/documentation/versioning-information.html/) for more information about how to interpret these version numbers.

### Galera 4 Versions

The following table lists each version of the [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4 wsrep provider, and it lists which version of MariaDB each one was first released in. If you would like to install [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4 using [yum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum), [apt](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/apt-upgrade-fails-but-the-database-is-running), or [zypper](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper), then the package is called `galera-4`.

| Galera Version | Released in MariaDB Version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 26.4.22        | [11.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.2), [11.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.6), [10.11.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.12), [10.6.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.22), [10.5.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.29)                                                                                                                                                                                                                                                                                                                                          |
| 26.4.21        | [11.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.1), [11.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.7/11.7.2), [11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.5), [10.11.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.11), [10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.21), [10.5.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.28)                                                                                                                                                                                                                                      |
| 26.4.20        | [11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.7/11.7.1), [11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/11.6.2), [11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.4), [11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.6), [10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.10), [10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.20), [10.5.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.27)                                                                                                                     |
| 26.4.19        | [11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.3), [11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.5), [11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.6), [10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9), [10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.19), [10.5.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.26)                                                                                                                                                                                                                           |
| 26.4.18        | [11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.4), [11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.5), [11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.6), [10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.8), [10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.18), [10.5.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.25), [10.4.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.34)                                                                                                        |
| 26.4.16        | [11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.2), [11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.3), [11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.4), [10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.6), [10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.7), [10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.16), [10.5.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.23), [10.4.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.32) |
| 26.4.14        | [10.10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.3), [10.9.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/10.9.5), [10.8.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.7), [10.7.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.8), [10.6.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.12), [10.5.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.19), [10.4.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.28)                                                                                           |
| 26.4.13        | [10.10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.2), [10.9.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/10.9.4), [10.8.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.6), [10.7.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.7), [10.6.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.11), [10.5.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.18), [10.4.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.27)                                                                                           |
| 26.4.12        | [10.10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.1), [10.9.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/10.9.2), [10.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.4), [10.7.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.5), [10.6.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.9), [10.5.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.17), [10.4.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.26)                                                                                             |
| 26.4.11        | [10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1), [10.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.2), [10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6), [10.5.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.14), [10.4.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.22)                                                                                                                                                                                                                                                                                                        |
| 26.4.9         | [10.6.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.4), [10.5.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.12), [10.4.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.21)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 26.4.8         | [10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.1), [10.5.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.10), [10.4.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.19)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 26.4.7         | [10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9), [10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.18)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 26.4.6         | [10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.7), [10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.16)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 26.4.5         | [10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.4), [10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.14)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 26.4.4         | [10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.1), [10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.13)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 26.4.3         | [10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0), [10.4.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 26.4.2         | [10.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.4)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 26.4.1         | [10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 26.4.0         | [10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

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

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formId="4316" %}
