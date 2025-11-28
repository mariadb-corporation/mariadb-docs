# Using MariaDB GTIDs with MariaDB Galera Cluster

MariaDB's [global transaction IDs (GTIDs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) are very useful when used with [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), which is primarily what that feature was developed for. [Galera Cluster](../../), on the other hand, was developed by Codership for all MySQL and MariaDB variants, and the initial development of the technology pre-dated MariaDB's [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) implementation. As a side effect, [MariaDB Galera Cluster](../../) (at least until [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)) only partially supports MariaDB's [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) implementation.

## GTID Support for Write Sets Replicated by Galera Cluster

Galera Cluster has its own [certification-based replication method](../../readme/about-galera-replication.md) that is substantially different from [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication). However, it would still be beneficial if [MariaDB Galera Cluster](../../) was able to associate a Galera Cluster write set with a [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) that is globally unique but that is also consistent for that write set on each cluster node.

### Wsrep GTID Mode

MariaDB supports [wsrep\_gtid\_mode](../../reference/galera-cluster-system-variables.md#wsrep_gtid_mode).

MariaDB has a feature called wsrep GTID mode. When this mode is enabled, MariaDB uses some tricks to try to associate each Galera Cluster write set with a [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) that is globally unique, but that is also consistent for that write set on each cluster node. These tricks work in some cases, but [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) can still become inconsistent among cluster nodes.

#### Enabling Wsrep GTID Mode

Several things need to be configured for wsrep GTID mode to work, such as

* [wsrep\_gtid\_mode=ON](../../reference/galera-cluster-system-variables.md#wsrep_gtid_mode) needs to be set on all nodes in the cluster.
* [wsrep\_gtid\_domain\_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id) needs to be set to the same value on all nodes in a given cluster, so that each cluster node uses the same domain when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for Galera Cluster's write sets. When replicating between two clusters, each cluster should have this set to a different value, so that each cluster uses different domains when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for their write sets.
* [log\_slave\_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_slave_updates) needs to be enabled on all nodes in the cluster. See [MDEV-9855](https://jira.mariadb.org/browse/MDEV-9855).
* [log\_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_bin) needs to be set to the same path on all nodes in the cluster. See [MDEV-9856](https://jira.mariadb.org/browse/MDEV-9856).

And as an extra safety measure:

* [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_domain_id) should be set to a different value on all nodes in a given cluster, and each of these values should be different than the configured [wsrep\_gtid\_domain\_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id) value. This is to prevent a node from using the same domain used for Galera Cluster's write sets when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for non-Galera transactions, such as DDL executed with [wsrep\_sst\_method=RSU](../../reference/galera-cluster-system-variables.md#wsrep_sst_method) set or DML executed with [wsrep\_on=OFF](../../reference/galera-cluster-system-variables.md#wsrep_on) set.

If you want to avoid writes accidentally local GTIDS, you can avoid it with by setting this:

```ini
wsrep_mode = DISALLOW_LOCAL_GTID 
```

In this case you get an error:

```
ERROR 4165 (HY000): Galera replication not supported
```

You can overwrite it temporarily with:

```sql
SET sql_log_bin = 0;
```

For information on setting [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#server_id), see [Using MariaDB Replication with MariaDB Galera Cluster: Setting server\_id on Cluster Nodes](using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#setting-server_id-on-cluster-nodes).

### GTIDs for Transactions Applied by Slave Thread

If a Galera Cluster node is also a [replication slave](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview), then that node's [slave SQL thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-threads#slave-sql-thread) will be applying transactions that it replicates from its replication master. If the node has [log\_slave\_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_slave_updates) set, then each transaction that the [slave SQL thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-threads#slave-sql-thread) applies will also generate a Galera Cluster write set that is replicated to the rest of the nodes in the cluster.

The node acting as slave includes the transaction's original `Gtid_Log_Event` in the replicated write set, so all nodes should associate the write set with its original GTID. See [MDEV-13431](https://jira.mariadb.org/browse/MDEV-13431).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
