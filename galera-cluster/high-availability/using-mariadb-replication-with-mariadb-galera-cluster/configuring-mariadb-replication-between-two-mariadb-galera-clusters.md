# Configuring MariaDB Replication between Two MariaDB Galera Clusters

[MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) can be used for replication between two [MariaDB Galera Clusters](../../). This article will discuss how to do that.

## Configuring the Clusters

Before we set up replication, we need to ensure that the clusters are configured properly. This involves the following steps:

* Set [log\_slave\_updates=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_slave_updates) on all nodes in both clusters. See [Configuring MariaDB Galera Cluster: Writing Replicated Write Sets to the Binary Log](../../galera-management/configuration/configuring-mariadb-galera-cluster.md#writing-replicated-write-sets-to-the-binary-log) and [Using MariaDB Replication with MariaDB Galera Cluster: Configuring a Cluster Node as a Replication Master](using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#configuring-a-cluster-node-as-a-replication-master) for more information on why this is important. This is also needed to [enable wsrep GTID mode](using-mariadb-gtids-with-mariadb-galera-cluster.md#enabling-wsrep-gtid-mode).
* Set [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#server_id) to the same value on all nodes in a given cluster, but be sure to use a different value in each cluster. See [Using MariaDB Replication with MariaDB Galera Cluster: Setting server\_id on Cluster Nodes](using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica.md#setting-server_id-on-cluster-nodes) for more information on what this means.

### Configuring Wsrep GTID Mode

If you want to use [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) replication, then you also need to configure some things to [enable wsrep GTID mode](using-mariadb-gtids-with-mariadb-galera-cluster.md#enabling-wsrep-gtid-mode). For example:

* [wsrep\_gtid\_mode=ON](../../reference/galera-cluster-system-variables.md#wsrep_gtid_mode) needs to be set on all nodes in each cluster.
* [wsrep\_gtid\_domain\_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id) needs to be set to the same value on all nodes in a given cluster so that each cluster node uses the same domain when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for Galera Cluster's write sets. Each cluster should have this set to a different value so that each cluster uses different domains when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for their write sets.
* [log\_slave\_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_slave_updates) needs to be enabled on all nodes in the cluster. See [MDEV-9855](https://jira.mariadb.org/browse/MDEV-9855) about that.
* [log\_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_bin) needs to be set to the same path on all nodes in the cluster. See [MDEV-9856](https://jira.mariadb.org/browse/MDEV-9856) about that.

And as an extra safety measure:

* [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_domain_id) should be set to a different value on all nodes in a given cluster, and each of these values should be different than the configured [wsrep\_gtid\_domain\_id](../../reference/galera-cluster-system-variables.md#wsrep_gtid_domain_id) value. This is to prevent a node from using the same domain used for Galera Cluster's write sets when assigning [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) for non-Galera transactions, such as DDL executed with [wsrep\_OSU\_method=RSU](../../reference/galera-cluster-system-variables.md#wsrep_osu_method) set or DML executed with [wsrep\_on=OFF](../../reference/galera-cluster-system-variables.md#wsrep_on) set.

## Configuring Parallel Replication

To improve the performance of the replication stream between clusters, it is recommended to enable [parallel replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/parallel-replication) on the nodes in the destination cluster (the cluster acting as the replica).

```sql
SET GLOBAL slave_parallel_threads = 4; -- Adjust based on workload
SET GLOBAL slave_parallel_mode = 'optimistic';
```

## Setting up Replication

Our process to set up replication is going to be similar to the process described at [Setting up a Replication Slave with mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup), but it will be modified a bit to work in this context.

{% stepper %}
{% step %}
### Start the First Cluster

The very first step is to start the nodes in the first cluster. The first node will have to be [bootstrapped](../../galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster.md#bootstrapping-a-new-cluster). The other nodes can be started normally.

Once the nodes are started, you need to pick a specific node that will act as the replication primary for the second cluster.
{% endstep %}

{% step %}
### Backup the Database on the First Cluster's Primary Node and Prepare It

The first step is to simply take and prepare a fresh [full backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup) of the node that you have chosen to be the replication primary. For example:

```bash
$ mariadb-backup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

And then you would prepare the backup as you normally would. For example:

```bash
$ mariadb-backup --prepare \
   --target-dir=/var/mariadb/backup/
```
{% endstep %}

{% step %}
### Copy the Backup to the Second Cluster's Replica

Once the backup is done and prepared, you can copy it to the node in the second cluster that will be acting as replica. For example:

```bash
$ rsync -avrP /var/mariadb/backup c2dbserver:/var/mariadb/backup
```
{% endstep %}

{% step %}
### Restore the Backup on the Second Cluster's Replica

At this point, you can restore the backup to the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir), as you normally would. For example:

```bash
$ mariadb-backup --copy-back \
   --target-dir=/var/mariadb/backup/
```

And adjusting file permissions, if necessary:

```bash
$ chown -R mysql:mysql /var/lib/mysql/
```
{% endstep %}

{% step %}
### Bootstrap the Second Cluster's Replica

Now that the backup has been restored to the second cluster's replica, you can start the server by [bootstrapping](../../galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster.md#bootstrapping-a-new-cluster) the node.
{% endstep %}

{% step %}
### Create a Replication User on the First Cluster's Primary

Before the second cluster's replica can begin replicating from the first cluster's primary, you need to [create a user account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi#create-user) on the primary that the replica can use to connect, and you need to [grant](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) the user account the [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave) privilege. For example:

```sql
CREATE USER 'repl'@'c2dbserver1' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.*  TO 'repl'@'c2dbserver1';
```
{% endstep %}

{% step %}
### Start Replication on the Second Cluster's Replica

At this point, you need to get the replication coordinates of the primary from the original backup.

The coordinates will be in the [xtrabackup\_binlog\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_binlog_info) file.

mariadb-backup dumps replication coordinates in two forms: [GTID strings](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) and [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates, like the ones you would normally see from [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) output. In this case, it is probably better to use the [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) coordinates.

For example:

```
mariadb-bin.000096 568 0-1-2
```

Regardless of the coordinates you use, you will have to set up the primary connection using [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) and then start the replication threads with [START SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/legacy-replication-statements/legacy-commands-start-slave).

{% tabs %}
{% tab title="GTIDs" %}
If you want to use GTIDs, then you will have to first set [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_slave_pos) to the [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) coordinates that we pulled from the [xtrabackup\_binlog\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_binlog_info) file, and we would set `MASTER_USE_GTID=slave_pos` in the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) command. For example:

```sql
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
   MASTER_HOST="c1dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```
{% endtab %}

{% tab title="File and Position" %}
If you want to use the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates, then you would set `MASTER_LOG_FILE` and `MASTER_LOG_POS` in the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) command to the file and position coordinates that we pulled the [xtrabackup\_binlog\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/files-created-by-mariadb-backup#xtrabackup_binlog_info) file. For example:

```sql
CHANGE MASTER TO 
   MASTER_HOST="c1dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_LOG_FILE='mariadb-bin.000096',
   MASTER_LOG_POS=568,
START SLAVE;
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
### Check the Status of the Second Cluster's Replica

You should be done setting up the replica now, so you should check its status with [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/legacy-replication-statements/legacy-commands-show-slave-status). For example:

```sql
SHOW SLAVE STATUS\G
```
{% endstep %}

{% step %}
### Start the Second Cluster

If the replica is replicating normally, then the next step would be to start the MariaDB Server process on the other nodes in the second cluster.

Now that the second cluster is up, ensure that it does not start accepting writes yet if you want to set up [circular replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview#ring-replication) between the two clusters.
{% endstep %}
{% endstepper %}

## Setting up Circular Replication

You can also set up [circular replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-overview#ring-replication) between the two clusters, which means that the second cluster replicates from the first cluster, and the first cluster also replicates from the second cluster.

{% stepper %}
{% step %}
### Create a Replication User on the Second Cluster's Primary

Before circular replication can begin, you also need to [create a user account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi#create-user) on the second cluster's primary that the first cluster's replica can use to connect, and you need to [grant](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) the user account the the [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave) privilege. For example:

```sql
CREATE USER 'repl'@'c1dbserver1' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.*  TO 'repl'@'c1dbserver1';
```
{% endstep %}

{% step %}
### Start Circular Replication on the First Cluster

How this is done would depend on whether you want to use the [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) coordinates or the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates.

Regardless, you need to ensure that the second cluster is not accepting any writes other than those that it replicates from the first cluster at this stage.

{% tabs %}
{% tab title="GTIDs" %}
To get the GTID coordinates on the second cluster, you can check [gtid\_current\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_current_pos) by executing:

```sql
SHOW GLOBAL VARIABLES LIKE 'gtid_current_pos';
```

Then on the first cluster, you can set up replication by setting [gtid\_current\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_current_pos) to the GTID that was returned and then executing [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to):

```sql
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
   MASTER_HOST="c2dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_USE_GTID=slave_pos;
START SLAVE;
```
{% endtab %}

{% tab title="File and Position" %}
To get the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) file and position coordinates on the second cluster, you can execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status):

```sql
SHOW MASTER STATUS
```

Then on the first cluster, you would set `master_log_file` and `master_log_pos` in the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) command. For example:

```sql
CHANGE MASTER TO 
   MASTER_HOST="c2dbserver1", 
   MASTER_PORT=3310, 
   MASTER_USER="repl",  
   MASTER_PASSWORD="password", 
   MASTER_LOG_FILE='mariadb-bin.000096',
   MASTER_LOG_POS=568;
START SLAVE;
```


{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
### Check the Status of the Circular Replication

You should be done setting up the circular replication on the node in the first cluster now, so you should check its status with [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/legacy-replication-statements/legacy-commands-show-slave-status). For example:

```sql
SHOW SLAVE STATUS\G
```
{% endstep %}
{% endstepper %}

{% @marketo/form formId="4316" %}
