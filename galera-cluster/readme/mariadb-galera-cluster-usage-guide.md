---
description: >-
  MariaDB Galera Cluster is a multi-primary replication solution for high
  availability and consistency, integrating Galera technology with MariaDB
  Community Server and Enterprise Server.
---

# MariaDB Galera Cluster Overview

_MariaDB Enterprise Cluster is a solution designed to handle high workloads exceeding the capacity of a single server. It is based on Galera Cluster technology integrated with MariaDB Enterprise Server and includes features like data-at-rest encryption for added security. This multi-primary replication alternative is ideal for maintaining data consistency across multiple servers, providing enhanced reliability and scalability._

## Overview

MariaDB Enterprise Cluster, powered by Galera, is available with MariaDB Enterprise Server. MariaDB Galera Cluster is available with MariaDB Community Server.

In order to handle increasing load and especially when that load exceeds what a single server can process, it is best practice to deploy multiple MariaDB Enterprise Servers with a replication solution to maintain data consistency between them. MariaDB Enterprise Cluster is a multi-primary replication solution that serves as an alternative to the single-primary MariaDB Replication.

## An Introduction to Database Replication

Database replication is the process of continuously copying data from one database server (a "node") to another, creating a distributed and resilient system. The goal is for all nodes in this system to contain the same set of data, forming what is known as a database cluster. From the perspective of a client application, this distributed nature is often transparent, allowing it to interact with the cluster as if it were a single database.

### Replication Architectures

#### **Primary/Replica**

<div align="left"><figure><img src="../.gitbook/assets/asynchronousreplication.png" alt=""><figcaption><p>Primary/Primary Replication</p></figcaption></figure></div>

The most common replication architecture is Primary/Replica (also known as Master/Slave). In this model:

* The Primary node is the authoritative source. It is the only node that accepts write operations (e.g., `INSERT`, `UPDATE`, `DELETE`).
* The Primary logs these changes and sends them to one or more Replica nodes.
* The Replicas receive the stream of changes and apply them to their own copy of the data. Replicas are typically used for read-only queries, backups, or as a hot standby for failover.

#### **Multi-Primary Replication**

<div align="left"><figure><img src="../.gitbook/assets/synchronousreplication.png" alt=""><figcaption><p>Multi-primary Replication</p></figcaption></figure></div>

In a multi-primary system, every node in the cluster acts as a primary. This means any node can accept write operations. When a node receives an update, it automatically propagates that change to all other primary nodes in the cluster. Each primary node logs its own changes and communicates them to its peers to maintain synchronization.

### Replication Protocols: Asynchronous vs. Synchronous

Beyond the architecture, the replication _protocol_ determines how transactions are confirmed across the cluster.

#### **Asynchronous Replication (Lazy Replication)**

In asynchronous replication, the primary node commits a transaction locally first and then sends the changes to the replicas in the background. The transaction is confirmed as complete to the client immediately after it's saved on the primary. This means there is a brief period, known as replication lag, where the replicas have not yet received the latest data.

#### **Synchronous Replication (Eager Replication)**

In synchronous replication, a transaction is not considered complete (committed) until it has been successfully applied and confirmed on all participating nodes. When the client receives confirmation, it is a guarantee that the data exists consistently across the cluster.

### The Trade-offs of Synchronous Replication

#### **Advantages**

Synchronous replication offers several powerful advantages over its asynchronous counterpart:

* High Availability: Since all nodes are fully synchronized, if one node fails, there is zero data loss. Traffic can be immediately directed to another node without complex failover procedures, as all data replicas are guaranteed to be consistent.
* Read-After-Write Consistency: Synchronous replication guarantees causality. A `SELECT` query issued immediately after a transaction will always see the effects of that transaction, even if the query is executed on a different node in the cluster.

#### **Disadvantages**

Traditionally, eager replication protocols coordinate nodes one operation at a time. They use a two phase commit, or distributed locking. A system with $$𝑛$$ number of nodes due to process $$𝑜$$ operations with a throughput of $$𝑡$$ transactions per second gives you $$𝑚$$ messages per second with:

<p align="center"><span class="math">𝑚=𝑛×𝑜×𝑡</span></p>

What this means that any increase in the number of nodes leads to an exponential growth in the transaction response times and in the probability of conflicts and deadlock rates.

For this reason, asynchronous replication remains the dominant replication protocol for database performance, scalability and availability. Widely adopted open source databases, such as MySQL and PostgreSQL only provide asynchronous replication solutions.

### Galera's Solution: Modern Synchronous Replication

Galera Cluster solves the traditional problems of synchronous replication by using a modern, certification-based approach built on several key innovations:

* Group Communication: A robust messaging layer ensures that information is delivered to all nodes reliably and in the correct order, forming a solid foundation for data consistency.
* Write-Set Replication: Instead of coordinating on every individual operation, database changes (writes) are grouped into a single package called a "write-set." This write-set is replicated as a single message, avoiding the high overhead of traditional two-phase commit.
* Optimistic Execution: Transactions are first executed optimistically on a local node. The resulting write-set is then broadcast to the cluster for a fast, parallel certification process. If it passes certification (meaning no conflicts), it is committed on all nodes.
* Transaction Reordering: This clever technique allows for the reordering of non-conflicting transactions before they are committed, which significantly increases parallelism and reduces the rate of transaction rollbacks.

The certification-based replication system that Galera Cluster uses is built on these powerful approaches, delivering the benefits of synchronous replication without the traditional performance bottlenecks.

## How it Works

MariaDB Enterprise Cluster is built on MariaDB Enterprise Server with Galera Cluster and MariaDB MaxScale. In MariaDB Enterprise Server 10.5 and later, it features enterprise-specific options, such as data-at-rest encryption for the write-set cache, that are not available in other Galera Cluster implementations.

As a multi-primary replication solution, any MariaDB Enterprise Server can operate as a Primary Server. This means that changes made to any node in the cluster replicate to every other node in the cluster, using certification-based replication and global ordering of transactions for the InnoDB storage engine.

{% hint style="info" %}
MariaDB Enterprise Cluster is only available for Linux operating systems.
{% endhint %}

## Architecture

There are a few things to consider when planning the hardware, virtual machines, or containers for MariaDB Enterprise Cluster.

MariaDB Enterprise Cluster architecture involves deploying [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) with multiple instances of MariaDB Enterprise Server. The Servers are configured to use multi-primary replication to maintain consistency between themselves while [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) routes reads and writes between them.

The application establishes a client connection to [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/). MaxScale then routes statements to one of the MariaDB Enterprise Servers in the cluster. Writes made to any node in this cluster replicate to all the other nodes of the cluster.

When MariaDB Enterprise Servers start in a cluster:

* Each Server attempts to establish network connectivity with the other Servers in the cluster
* Groups of connected Servers form a component
* When a Server establishes network connectivity with the Primary Component, it synchronizes its local database with that of the cluster
* As a member of the Primary Component, the Server becomes operational — able to accept read and write queries from clients
* During startup, the Primary Component is the Server bootstrapped to run as the Primary Component. Once the cluster is online, the Primary Component is any combination of Servers which includes a minimum of more than half the total number of Servers.
* A Server or group of Servers that loses network connectivity with the majority of the cluster becomes non-operational.

In planning the number of systems to provision for MariaDB Enterprise Cluster, it is important to keep cluster operation in mind. Ensuring that it has enough disk space and that it is able to maintain a Primary Component in the event of outages.

* Each Server requires the minimum amount of disk space needed to store the entire database. The upper storage limit for MariaDB Enterprise Cluster is that of the smallest disk in use.
* Each switch in use should have an odd number of Servers above three.
* In a cluster that spans multiple switches, each data center in use should have an odd number of switches above three.
* In a cluster that spans multiple data centers, use an odd number of data centers above three.
* Each data center in use should have at least one Server dedicated to backup operations. This can be another cluster node or a separate Replica Server kept in sync using MariaDB Replication.

In case of planning Servers to the switch, switches to the data center, and data centers in the cluster, this model helps preserve the Primary Component. A minimum of three in use means that a single Server or switch can fail without taking down the cluster.

Using an odd number above three reduces the risk of a split-brain situation (that is, a case where two separate groups of Servers believe that they are part of the Primary Component and remain operational).

## Cluster Configuration

Nodes in MariaDB Enterprise Cluster are individual MariaDB Enterprise Servers configured to perform multi-primary cluster replication. This configuration is set using a series of system variables in the configuration file.

```ini
[mariadb]

# General Configuration
bind_address             = 0.0.0.0
innodb_autoinc_lock_mode = 2

# Cluster Configuration
wsrep_cluster_name    = "accounting_cluster"
wsrep_cluster_address = "gcomm://192.0.2.1,192.0.2.2,192.0.2.3"

# wsrep Provider
wsrep_provider = /usr/lib/galera/libgalera_enterprise_smm.so
wsrep_provider_options = "evs.suspect_timeout=PT10S"
```

Additional information on system variables is available in the Reference chapter.

### General Configuration

The `innodb_autoinc_lock_mode` system variable must be set to a value of 2 to enable interleaved lock mode. MariaDB Enterprise Cluster does not support other lock modes.

Ensure also that the `bind_address` system variable is properly set to allow MariaDB Enterprise Server to listen for TCP/IP connections:

```ini
bind_address             = 0.0.0.0
innodb_autoinc_lock_mode = 2
```

### Cluster Name and Address

MariaDB Enterprise Cluster requires that you set a name for your cluster, using the `wsrep_cluster_name` system variable. When nodes connect to each other, they check the cluster name to ensure that they've connected to the correct cluster before replicating data. All Servers in the cluster must have the same value for this system variable.

Using the `wsrep_cluster_address` system variable, you can define the back-end protocol (always gcomm) and comma-separated list of the IP addresses or domain names of the other nodes in the cluster.

```ini
wsrep_cluster_name    = "accounting_cluster"
wsrep_cluster_address = "gcomm://192.0.2.1,192.0.2.2,192.0.2.3"
```

It is best practice to list all nodes on this system variable, as this is the list the node searches when attempting to reestablish network connectivity with the primary component.

**Note:** In certain environments, such as deployments in the cloud, you may also need to set the `wsrep_node_address` system variable, so that MariaDB Enterprise Server properly informs other Servers how to reach it.

### Galera Replicator Plugin

MariaDB Enterprise Server connects to other Servers and replicates data from the cluster through a wsrep Provider called the Galera Replicator plugin. In order to enable clustering, specify the path to the relevant `.so` file using the `wsrep_provider` system variable.

MariaDB Enterprise Server 10.4 and later installations use an enterprise-build of the Galera Enterprise 4 plugin. This includes all the features of Galera Cluster 4 as well as enterprise features like GCache encryption.

To enable MariaDB Enterprise Cluster, use the `libgalera_enterprise_smm.so` library:

```
wsrep_provider = /usr/lib/galera/libgalera_enterprise_smm.so
```

MariaDB Enterprise Server use the older community-release of the Galera 3 plugin. This is set using the `libgalera_smm.so` library:

```
wsrep_provider = /usr/lib/galera/libgalera_smm.so
```

In addition to system variables, there is a set of options that you can pass to the wsrep Provider to configure or to otherwise adjust its operations. This is done through the `wsrep_provider_options` system variable:

```
wsrep_provider_options = "evs.suspect_timeout=PT10S"
```

Additional information is available in the Reference chapter.

## Cluster Replication

MariaDB Enterprise Cluster implements a multi-primary replication solution.

When you write to a table on a node, the node collects the write into a write-set transaction, which it then replicates to the other nodes in the cluster.

Your application can write to any node in the cluster. Each node certifies the replicated write-set. If the transaction has no conflicts, the nodes apply it. If the transaction does have conflicts, it is rejected and all of the nodes revert the changes.

### Quorum

The first node you start in MariaDB Enterprise Cluster bootstraps the Primary Component. Each subsequent node that establishes a connection joins and synchronizes with the Primary Component. A cluster achieves a quorum when more than half the nodes are joined to the Primary Component.

When a component forms that has less than half the nodes in the cluster, it becomes non-operational, since it believes there is a running Primary Component to which it has lost network connectivity.

These quorum requirements, combined with the requisite number of odd nodes, avoid a split brain situation, or one in which two separate components believe they are each the Primary Component.

### Dynamically Bootstrapping the Cluster

In cases where the cluster goes down and your nodes become non-operational, you can dynamically bootstrap the cluster.

First, find the most up-to-date node (that is, the node with the highest value for the `wsrep_last_committed` status variable):

```sql
SHOW STATUS LIKE 'wsrep_last_committed';
```

Once you determine the node with the most recent transaction, you can designate it as the Primary Component by running the following on it:

```sql
SET GLOBAL wsrep_provider_options="pc.bootstrap=YES";
```

The node bootstraps the Primary Component onto itself. Other nodes in the cluster with network connectivity then submit state transfer requests to this node to bring their local databases into sync with what's available on this node.

### State Transfers

From time to time a node can fall behind the cluster. This can occur due to expensive operations being issued to it or due to network connectivity issues that lead to write-sets backing up in the queue. Whatever the cause, when a node finds that it has fallen too far behind the cluster, it attempts to initiate a state transfer.

In a state transfer, the node connects to another node in the cluster and attempts to bring its local database back in sync with the cluster. There are two types of state transfers:

* Incremental State Transfer (IST)
* State Snapshot Transfer (SST)

When the donor node receives a state transfer request, it checks its write-set cache (that is, the GCache) to see if it has enough saved write-sets to bring the joiner into sync. If the donor node has the intervening write-sets, it performs an IST operation, where the donor node only sends the missing write-sets to the joiner. The joiner applies these write-sets following the global ordering to bring its local databases into sync with the cluster.

When the donor does not have enough write-sets cached for an IST, it runs an SST operation. In an SST, the donor uses a backup solution, like MariaDB Enterprise Backup, to copy its data directory to the joiner. When the joiner completes the SST, it begins to process the write-sets that came in during the transfer. Once it's in sync with the cluster, it becomes operational.

IST's provide the best performance for state transfers and the size of the GCache may need adjustment to facilitate their use.

### Flow Control

MariaDB Enterprise Server uses Flow Control to sometimes throttle transactions and ensure that all nodes work equitably.

Write-sets that replicate to a node are collected by the node in its received queue. The node then processes the write-sets according to global ordering. Large transactions, expensive operations, or simple hardware limitations can lead to the received queue backing up over time.

When a node's received queue grows beyond certain limits, the node initiates Flow Control. In Flow Control, the node pauses replication to work through the write-sets it already has. Once it has worked the received queue down to a certain size, it re-initiates replication.

### Eviction

A node or nodes will be removed or evicted from a cluster if it becomes non-responsive.

In MariaDB Enterprise Cluster, each node monitors network connectivity and response times from every other node. MariaDB Enterprise Cluster evaluates network performance using the EVS Protocol.

When a node finds another to have poor network connectivity, it adds an entry to the delayed list. If the node becomes active again and the network performance improves for a certain amount of time, an entry for it is removed from the delayed list. That is, the longer a node has network problems the longer it has to be active again to be removed from the delayed list.

If the number of entries for a node in the delayed list exceeds a threshold established for the cluster, the EVS Protocol evicts the node from the cluster.

Evicted nodes become non-operational components. They cannot rejoin the cluster until you restart MariaDB Enterprise Server.

### Streaming Replication

Under normal operation, huge transactions and long-running transactions are difficult to replicate. MariaDB Enterprise Cluster rejects conflicting transactions and rolls back the changes. A transaction that takes several minutes or longer to run can encounter issues if a small transaction is run on another node and attempts to write to the same table. The large transaction fails because it encounters a conflict when it attempts to replicate.

MariaDB Enterprise Server 10.4 and later support streaming replication for MariaDB Enterprise Cluster. In streaming replication, huge transactions are broken into transactional fragments, which are replicated and applied as the operation runs. This makes it more difficult for intervening sessions to introduce conflicts.

### Initiate Streaming Replication

To initiate streaming replication, set the `wsrep_trx_fragment_unit and wsrep_trx_fragment_size` system variables. You can set the unit to `BYTES, ROWS, or STATEMENTS`:

```sql
SET SESSION wsrep_trx_fragment_unit='STATEMENTS';

SET SESSION wsrep_trx_fragment_size=5;
```

Then, run your transaction.

Streaming replication works best with very large transactions where you don't expect to encounter conflicts. If the statement does encounter a conflict, the rollback operation is much more expensive than usual. As such, it's best practice to enable streaming replication at a session-level and to disable it by setting the `wsrep_trx_fragment_size` system variable to 0 when it's not needed.

```sql
SET SESSION wsrep_trx_fragment_size=0;
```

### Galera Arbitrator

Deployments on mixed hardware can introduce issues where some MariaDB Enterprise Servers perform better than others. A Server in one part of the world might perform more reliably or be physically closer to most users than others. In cases where a particular MariaDB Enterprise Server holds logical significance for your cluster, you can weight its value in quorum calculations.

Galera Arbitrator is a separate process that runs alongside MariaDB Enterprise Server. While the Arbitrator does not take part in replication, whenever the cluster performs quorum calculations it gives the Arbitrator a vote as though it were another MariaDB Enterprise Server. In effect this means that the system has the vote of MariaDB Enterprise Server plus any running Arbitrators in determining whether it's part of the Primary Component.

Bear in mind that the Galera Arbitrator is a separate package, `galera-arbitrator-4`, which is not installed by default with MariaDB Enterprise Server.

### Scale-out

MariaDB Enterprise Servers that join a cluster attempt to connect to the IP addresses provided to the `wsrep_cluster_address` system variable. This variable adjusts itself at runtime to include the addresses of all connected nodes.

To scale-out MariaDB Enterprise Cluster, start new MariaDB Enterprise Servers with the appropriate `wsrep_cluster_address` list and the same `wsrep_cluster_name` value. The new nodes establish network connectivity with the running cluster and request a state transfer to bring their local database into sync with the cluster.

Once the MariaDB Enterprise Server reports itself as being in sync with the cluster, MariaDB MaxScale can begin including it in the load distribution for the cluster.

Being a multi-primary replication solution means that any MariaDB Enterprise Server in the cluster can handle write operations, but write scale-out is minimal as every Server in the cluster needs to apply the changes.

### Failover

MariaDB Enterprise Cluster does not provide failover capabilities on its own. [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) is used to route client connections to MariaDB Enterprise Server.

Unlike a traditional load balancer, [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) is aware of changes in the node and cluster states.

MaxScale takes nodes out of the distribution that initiate a blocking SST operation or Flow Control or otherwise go down, which allows them to recover or catch up without stopping service to the rest of the cluster.

### Backups

With MariaDB Enterprise Cluster, each node contains a replica of all the data in the cluster. As such, you run [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup) on any node to back up the available data. The process for backing up a node is the same as for a single MariaDB Enterprise Server.

### Encryption

MariaDB Enterprise Server supports data-at-rest encryption to secure data on disk, and data-in-transit encryption to secure data on the network.

MariaDB Enterprise Server support data-at-rest encryption of the GCache, the file used by Galera systems to cache write sets. Encrypting GCache ensures the Server encrypts both data it temporarily caches from the cluster as well as the data it permanently stores in tablespaces.

For data-in-transit, MariaDB Enterprise Cluster supports encryption the same as MariaDB Server and additionally provides data-in-transit encryption for Galera replication traffic and for State Snapshot Transfer (SST) traffic.

### Data-in-Transit Encryption

MariaDB Enterprise Server 10.6 encrypts Galera replication and SST traffic using the server's TLS configuration by default. With the `wsrep_ssl_mode` system variable, you can configure the node to use the TLS configuration of [wsrep Provider options](../reference/wsrep-variable-details/wsrep_provider_options.md).

MariaDB Enterprise Server 10.5 and earlier support encrypting Galera replication and SST traffic through [wsrep Provider options](../reference/wsrep-variable-details/wsrep_provider_options.md).

TLS encryption is only available when used by all nodes in the cluster.

### Enabling GCache Encryption

To encrypt data-at-rest such as GCache, stop the server, set `encrypt_binlog=ON` within the MariaDB Enterprise Server configuration file, and restart the server. This variable also controls encryption of the binary log and the relay log when used.

```ini
[mariadb]
...
# Controls Binary Log, Relay Log, and GCache Encryption
encrypt_binlog=ON
```

### Disabling GCache Encryption

To stop using encryption on the GCache file, stop the server, set `encrypt_binlog=OFF` within the MariaDB Enterprise Server configuration file, and restart the server. This variable also controls encryption of the binary log and the relay log when used.

```ini
[mariadb]
...
# Controls Binary Log, Relay Log, and GCache Encryption
encrypt_binlog=OFF
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
