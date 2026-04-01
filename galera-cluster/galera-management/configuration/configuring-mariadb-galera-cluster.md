# Configuring MariaDB Galera Cluster

A number of options need to be set in order for Galera Cluster to work when using MariaDB. These should be set in the [MariaDB option file](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files).

## Mandatory Options

Several options are mandatory, which means that they _must_ be set in order for Galera Cluster to be enabled or to work properly with MariaDB. The mandatory options are:

* [wsrep\_provider](../../reference/galera-cluster-system-variables.md#wsrep_provider) — Path to the Galera library
* [wsrep\_cluster\_address](../../reference/galera-cluster-system-variables.md#wsrep_cluster_address) — See [Galera Cluster address format and usage](galera-cluster-address.md)
* [binlog\_format=ROW](https://mariadb.com/docs/general-resources/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4000-to-4099/e4056) — See [Binary Log Formats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats)
* [wsrep\_on=ON](../../reference/galera-cluster-system-variables.md#wsrep_on) — Enable wsrep replication
* [default\_storage\_engine=InnoDB](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#default_storage_engine) — This is the default value, or alternately [wsrep\_replicate\_myisam=1](../../reference/galera-cluster-system-variables.md#wsrep_replicate_myisam) (before MariaDB 10.6) or [wsrep\_mode=REPLICATE\_ARIA,REPLICATE\_MYISAM](../../reference/galera-cluster-system-variables.md#wsrep_mode=REPLICATE_ARIA,REPLICATE_MYISAM) (MariaDB 10.6 and later).
  * [innodb\_doublewrite=1](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-system-variables#innodb_doublewrite) — This is the default value, and should not be changed.

## Performance-related Options

These are optional optimizations that can be made to improve performance.

* [innodb\_flush\_log\_at\_trx\_commit=](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_log_at_trx_commit)1 — This is not usually recommended in the case of standard MariaDB. However, it is a safer, recommended option with Galera Cluster, since inconsistencies can always be fixed by recovering from another node.
  * [innodb\_flush\_log\_at\_trx\_commit=](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_log_at_trx_commit) `0` can result in the loss of acknowledged transactions during simultaneous power failures or coordinated process crashes
* [innodb\_autoinc\_lock\_mode=2](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-system-variables#innodb_autoinc_lock_mode) — This tells InnoDB to use interleaved method. Interleaved is the fastest and most scalable lock mode, and should be used when BINLOG\_FORMAT is set to ROW.\
  Setting the auto-increment lock mode for InnoDB to interleaved, you’re allowing slaves threads to operate in parallel.
* [wsrep\_slave\_threads=4](../../reference/galera-cluster-system-variables.md#wsrep_slave_threads)\
  — This makes state transfers quicker for new nodes. You should start with four slave threads per CPU core.\
  The logic here is that, in a balanced system, four slave threads can typically saturate a CPU core. However, I/O performance can increase this figure several times over. For example, a single-core ThinkPad R51 with a 4200 RPM drive can use thirty-two slave threads. The value should not be set higher than [wsrep\_cert\_deps\_distance](../../reference/galera-cluster-status-variables.md#wsrep_cert_deps_distance).

## Writing Replicated Write Sets to the Binary Log

Like with [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), write sets that are received by a node with [Galera Cluster's certification-based replication](../../readme/about-galera-replication.md) are not written to the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) by default. If you would like a node to write its replicated write sets to the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log), then you will have to set [log\_slave\_updates=ON](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-and-binary-log-system-variables). This is especially helpful if the node is a replication master. See [Using MariaDB Replication with MariaDB Galera Cluster: Configuring a Cluster Node as a Replication Master](../../high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md).

## Replication Filters

Like with [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), [replication filters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-filters) can be used to filter write sets from being replicated by [Galera Cluster's certification-based replication](../../readme/about-galera-replication.md). However, they should be used with caution because they may not work as you'd expect.

The following replication filters are honored for [InnoDB](https://mariadb.com/docs/server/server-usage/storage-engines/innodb) DML, but not DDL:

* [binlog\_do\_db](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-filters#binlog_do_db)
* [binlog\_ignore\_db](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-filters#binlog_ignore_db)
* [replicate\_wild\_do\_table](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-filters#replicate_wild_do_table)
* [replicate\_wild\_ignore\_table](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-filters#replicate_wild_ignore_table)

The following replication filters are honored for DML and DDL for tables that use both the [InnoDB](https://mariadb.com/docs/server/server-usage/storage-engines/innodb) and [MyISAM](https://mariadb.com/docs/server/server-usage/storage-engines/myisam-storage-engine) storage engines:

* [replicate\_do\_table](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-filters#replicate_do_table)
* [replicate\_ignore\_table](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-filters#replicate_ignore_table)

However, it should be kept in mind that if replication filters cause inconsistencies that lead to replication errors, then nodes may abort.

See also [MDEV-421](https://jira.mariadb.org/browse/MDEV-421) and [MDEV-6229](https://jira.mariadb.org/browse/MDEV-6229).

## Network Ports

Galera Cluster needs access to the following ports:

* Standard MariaDB Port (default: 3306) - For MySQL client connections and [State Snapshot Transfers](../../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) that use the `mysqldump` method. This can be changed by setting [port](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#port).
* Galera Replication Port (default: 4567) - For Galera Cluster replication traffic, multicast replication uses both UDP transport and TCP on this port. Can be changed by setting [wsrep\_node\_address](../../reference/galera-cluster-system-variables.md#wsrep_node_address).
* Galera Replication Listening Interface (default: `0.0.0.0:4567`) needs to be set using [gmcast.listen\_addr](../../reference/wsrep-variable-details/wsrep_provider_options.md#gmcastlisten_addr), either
  * in [wsrep\_provider\_options](../../reference/galera-cluster-system-variables.md#wsrep_provider_options): `wsrep_provider_options='gmcast.listen_addr=tcp://<IP_ADDR>:<PORT>;'`
  * or in [wsrep\_cluster\_address](../../reference/galera-cluster-system-variables.md#wsrep_cluster_address)
* IST Port (default: 4568) - For Incremental State Transfers. Can be changed by setting [ist.recv\_addr](https://galeracluster.com/library/documentation/galera-parameters.html#ist-recv-addr) in [wsrep\_provider\_options](../../reference/galera-cluster-system-variables.md#wsrep_provider_options).
* SST Port (default: 4444) - For all [State Snapshot Transfer](../../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) methods other than `mysqldump`. Can be changed by setting [wsrep\_sst\_receive\_address](../../reference/galera-cluster-system-variables.md#wsrep_sst_receive_address).

## Mutiple Galera Cluster Instances on One Server

If you want to run multiple Galera Cluster instances on one server, then you can do so by starting each instance with [mysqld\_multi](https://mariadb.com/docs/server/clients-and-utilities/legacy-clients-and-utilities/mysqld_multi), or if you are using [systemd](https://mariadb.com/docs/server/server-management/starting-and-stopping-mariadb/systemd), then you can use the relevant [systemd method for interacting with multiple MariaDB instances](https://mariadb.com/docs/server/server-management/starting-and-stopping-mariadb/systemd#interacting-with-the-mariadb-server-process).

You need to ensure that each instance is configured with a different [datadir](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#datadir).

You also need to ensure that each instance is configured with different [network ports](https://mariadb.com/docs/galera-cluster/galera-management/configuring-mariadb-galera-cluster#network-ports).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
