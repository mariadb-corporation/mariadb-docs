---
description: >-
  Set up asynchronous MariaDB replication between a MariaDB Galera Cluster and
  a standalone MariaDB Server, including server_id, log_slave_updates, and
  wsrep GTID mode configuration.
---

# Configuring MariaDB Replication between MariaDB Galera Cluster and MariaDB Server

[MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) can be used to replicate between [MariaDB Galera Cluster](../../../kb/en/galera-cluster/) and MariaDB Server. This article will discuss how to do that.

## Configuring the Cluster

Before we set up replication, we need to ensure that the cluster is configured properly. This involves the following steps:

* Set [log_slave_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates) on all nodes in the cluster. See [Configuring MariaDB Galera Cluster: Writing Replicated Write Sets to the Binary Log](../../galera-management/configuring-mariadb-galera-cluster.md#writing-replicated-write-sets-to-the-binary-log) and [Using MariaDB Replication with MariaDB Galera Cluster: Configuring a Cluster Node as a Replication Master](using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#configuring-a-cluster-node-as-a-replication-master) for more information on why this is important. This is also needed to [enable wsrep GTID mode](using-mariadb-gtids-with-mariadb-galera-cluster.md#enabling-wsrep-gtid-mode).
* Set [server_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#server_id) to the same value on all nodes in the cluster. See [Using MariaDB Replication with MariaDB Galera Cluster: Setting server\_id on Cluster Nodes](using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#setting-server_id-on-cluster-nodes) for more information on what this means.

### Configuring Wsrep GTID Mode

If you want to use [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) replication, then you also need to configure some things to [enable wsrep GTID mode](using-mariadb-gtids-with-mariadb-galera-cluster.md#enabling-wsrep-gtid-mode). For example:

* [wsrep_gtid_mode=ON](../../reference/galera-cluster-system-variables.md#wsrep_gtid_mode) needs to be set on all nodes in the cluster.
* [wsrep_gtid_domain_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id) needs to be set to the same value on all nodes in the cluster, so that each cluster node uses the same domain when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for Galera Cluster's write sets.
* [log_slave_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables#log_slave_updates) needs to be enabled on all nodes in the cluster. See [MDEV-9855](https://jira.mariadb.org/browse/MDEV-9855) about that.
* [log_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables) needs to be set to the same path on all nodes in the cluster. See [MDEV-9856](https://jira.mariadb.org/browse/MDEV-9856) about that.

And as an extra safety measure:

* [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_domain_id) should be set to a different value on all nodes in a given cluster, and each of these values should be different than the configured [wsrep\_gtid\_domain\_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id) value. This is to prevent a node from using the same domain used for Galera Cluster's write sets when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for non-Galera transactions, such as DDL executed with [wsrep\_sst\_method=RSU](../../reference/galera-cluster-system-variables.md#wsrep_sst_method) set or DML executed with [wsrep\_on=OFF](../../reference/galera-cluster-system-variables.md#wsrep_on) set.

## Configuring the Replica

Before we set up replication, we also need to ensure that the MariaDB Server replica is configured properly. This involves the following steps:

* Set [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#server_id) to a different value than the one that the cluster nodes are using.
* Set [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_domain_id) to a value that is different than the [wsrep\_gtid\_domain\_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id) and [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_domain_id) values that the cluster nodes are using.
* Set [log\_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) and [log\_slave\_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_slave_updates) if you want the replica to log the transactions that it replicates.

## Setting up Replication

Our process to set up replication is going to be similar to the process described at [Setting up a Replication Slave with mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/setting-up-a-replica-with-mariadb-backup), but it will be modified a bit to work in this context.

### Start the Cluster

The very first step is to start the nodes in the first cluster. The first node will have to be [bootstrapped](../../galera-management/getting-started-with-mariadb-galera-cluster.md#bootstrapping-a-new-cluster). The other nodes can be started normally.

Once the nodes are started, you need to pick a specific node that will act as the replication primary for the MariaDB Server.

### Backup the Database on the Cluster's Primary Node and Prepare It

The first step is to simply take and prepare a fresh [full backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/full-backup-and-restore-with-mariadb-backup) of the node that you have chosen to be the replication primary. For example:

```
$ mariadb-backup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

And then you would prepare the backup as you normally would. For example:

```
$ mariadb-backup --prepare \
   --target-dir=/var/mariadb/backup/
```

### Copy the Backup to the Replica

Once the backup is done and prepared, you can copy it to the MariaDB Server that will be acting as replica. For example:

```
$ rsync -avrP /var/mariadb/backup dc2-dbserver1:/var/mariadb/backup
```

### Restore the Backup on the Second Cluster's Replica

At this point, you can restore the backup to the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#datadir), as you normally would. For example:

```
$ mariadb-backup --copy-back \
   --target-dir=/var/mariadb/backup/
```

And adjusting file permissions, if necessary:

```
$ chown -R mysql:mysql /var/lib/mysql/
```

### Start the New Replica

Now that the backup has been restored to the MariaDB Server replica, you can start the MariaDB Server process.

### Create a Replication User on the Cluster's Primary

Before the MariaDB Server replica can begin replicating from the cluster's primary, you need to [create a user account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user) on the primary that the replica can use to connect, and you need to [grant](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant) the user account the [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant#global-privileges) privilege. For example:

```
CREATE USER 'repl'@'dc2-dbserver1' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.*  TO 'repl'@'dc2-dbserver1';
```

### Start Replication on the New Replica

At this point, you need to get the replication coordinates of the primary from the original backup.

The coordinates will be in the [xtrabackup\_binlog\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_binlog_info) file.

mariadb-backup dumps replication coordinates in two forms: [GTID strings](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) and [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates, like the ones you would normally see from [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-binlog-status) output. In this case, it is probably better to use the [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) coordinates.

For example:

```
mariadb-bin.000096 568 0-1-2
```

Regardless of the coordinates you use, you will have to set up the primary connection using [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) and then start the replication threads with [START SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/start-replica).

#### GTIDs

If you want to use GTIDs, then you will have to first set [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_slave_pos) to the [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) coordinates that we pulled from the [xtrabackup\_binlog\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_binlog_info) file, and we would set `MASTER_USE_GTID=slave_pos` in the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) command. For example:

```
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
   MASTER_HOST="c1dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```

#### File and Position

If you want to use the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates, then you would set `MASTER_LOG_FILE` and `MASTER_LOG_POS` in the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) command to the file and position coordinates that we pulled the [xtrabackup\_binlog\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_binlog_info) file. For example:

```
CHANGE MASTER TO 
   MASTER_HOST="c1dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_LOG_FILE='mariadb-bin.000096',
   MASTER_LOG_POS=568,
START SLAVE;
```

### Check the Status of the New Replica

You should be done setting up the replica now, so you should check its status with [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status). For example:

```
SHOW SLAVE STATUS\G
```

Now that the MariaDB Server is up, ensure that it does not start accepting writes yet if you want to set up [circular replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview#ring-replication) between the cluster and the MariaDB Server.

## Setting up Circular Replication

You can also set up [circular replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview#ring-replication) between the cluster and MariaDB Server, which means that the MariaDB Server replicates from the cluster, and the cluster also replicates from the MariaDB Server.

### Create a Replication User on the MariaDB Server Primary

Before circular replication can begin, you also need to [create a user account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user) on the MariaDB Server, since it will be acting as replication primary to the cluster's replica, and you need to [grant](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant) the user account the [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/account-management-sql-commands/grant#global-privileges) privilege. For example:

```
CREATE USER 'repl'@'c1dbserver1' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.*  TO 'repl'@'c1dbserver1';
```

### Start Circular Replication on the Cluster

How this is done would depend on whether you want to use the [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) coordinates or the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates.

Regardless, you need to ensure that the second cluster is not accepting any writes other than those that it replicates from the cluster at this stage.

#### GTIDs

To get the GTID coordinates on the MariaDB Server you can check [gtid_current_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/standard-replication/gtid#gtid_current_pos) by executing:

```
SHOW GLOBAL VARIABLES LIKE 'gtid_current_pos';
```

Then on the node acting as replica in the cluster, you can set up replication by setting [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_slave_pos) to the GTID that was returned and then executing [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to):

```
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
   MASTER_HOST="c2dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```

#### File and Position

To get the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates on the MariaDB Server, you can execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-binlog-status):

```
SHOW MASTER STATUS
```

Then on the node acting as replica in the cluster, you would set `master_log_file` and `master_log_pos` in the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/replication-statements/change-master-to) command. For example:

```
CHANGE MASTER TO 
   MASTER_HOST="c2dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_LOG_FILE='mariadb-bin.000096',
   MASTER_LOG_POS=568;
START SLAVE;
```

### Check the Status of the Circular Replication

You should be done setting up the circular replication on the node in the first cluster now, so you should check its status with [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-replica-status). For example:

```
SHOW SLAVE STATUS\G
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
