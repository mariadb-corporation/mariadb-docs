---
description: >-
  A strategy for migrating from a MySQL Galera Cluster to a MariaDB Galera
  Cluster by setting up the new cluster as an asynchronous replica, minimizing
  downtime.
---

# Migration from MySQL Galera Cluster to MariaDB Galera Cluster using Replication

This guide details migrating a live database from a MySQL Galera Cluster to a [MariaDB Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide). The migration strategy requires setting up a new MariaDB Cluster and using [asynchronous replication](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/about-galera-replication#synchronous-vs.-asynchronous-replication) to sync it with the existing MySQL Cluster. The method includes a reliable failback route.

{% hint style="info" %}
This document focuses on the migration process itself. For detailed comparisons between the two database systems, please refer to [Incompatibilities and Feature Differences Between MariaDB and MySQL.](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences)
{% endhint %}

## Prerequisites

* **MySQL Server**: A running MySQL Galera Cluster (version 8.0 or 8.4) to migrate.
* **MariaDB Server**: The target [MariaDB version that supports Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-guide#galera-versions). This guide assumes the latest stable version.
* **`mysqldump`**: A command-line utility by MySQL to create initial database backup.

{% hint style="warning" %}
Due to changes in MySQL 8.0+, `mariadb-dump` may not be compatible for this initial step.
{% endhint %}

* **Root or Sudo Access**: Administrative [privileges](../../../../security/user-account-management/roles/system-users-roles-and-privileges.md) are required on all servers involved in the migration.

## Migration Steps

{% stepper %}
{% step %}
### Check for Incompatibilities

{% hint style="warning" %}
While MariaDB maintains a high degree of compatibility with MySQL, it is crucial to review any differences that could impact your applications.
{% endhint %}

* **Version Compatibility**: Select a [MariaDB version compatible](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/differences-between-the-mysql-and-mariadb-query-optimizer) with your MySQL version for replication.
* **Feature Differences**: Review the [Incompatibilities and Feature Differences](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences) to identify any deprecated features or changes in [system tables](../../../../reference/system-tables/), [user accounts](../../../../security/user-account-management/), and authentication that might affect your setup.

**Replication Compatibility**

| MySQL Version | Compatible MariaDB Version                  |
| ------------- | ------------------------------------------- |
| 5.7           | 10.2 and newer                              |
| 8.0           | 10.6.21, 10.11.11, 11.4.5, 11.7.2 and newer |

For more details, see [MySQL to MariaDB Replication Compatibilit](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/replication-compatibility-between-mariadb-and-mysql)y.
{% endstep %}

{% step %}
### Install and Configure a New MariaDB Galera Cluster

Set up a new, empty [MariaDB Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide) that will become the target for the migration.

1. **Install MariaDB Server and Galera Provider**

Install MariaDB Server package and Galera wsrep provider library on each node of the new cluster. Refer [Install](../../installing-mariadb/) and [Upgrade MariaDB](../../upgrading/) for detailed instructions.

2. **Configure Each MariaDB Node**

[Create a configuration file](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide#id-4.-configure-galera-cluster-galera.cnf-on-each-node) at `/etc/mysql/conf.d/galera.cnf` on each node. The configuration will be mostly identical across nodes, except for node-specific details like `wsrep_node_name` and `wsrep_node_address`.

**Example `galera.cnf`:**

```toml
[mysqld]
# MariaDB settings
binlog_format=ROW
default_storage_engine=InnoDB
innodb_autoinc_lock_mode=2
bind-address=0.0.0.0

# Galera Provider Configuration
wsrep_on=ON
wsrep_provider=/usr/lib/galera/libgalera_smm.so # Adjust path if necessary

# Galera Cluster Configuration
wsrep_cluster_name="new_mariadb_cluster"
wsrep_cluster_address="gcomm://node1_ip,node2_ip,node3_ip"

# Node-specific Configuration
wsrep_node_name="mariadb_node1"
wsrep_node_address="node1_ip"

# SST Configuration
wsrep_sst_method=mariadb-backup

```

{% hint style="info" %}
It is recommended to set `wsrep_sst_method` on all nodes to ensure consistency during [State Snapshot Transfers ](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts)(SST).
{% endhint %}
{% endstep %}

{% step %}
### Back Up the MySQL Database

A full logical backup of the MySQL database is required to seed the new MariaDB Cluster.

1.  **Enable Binary Logging on MySQL**

    [Asynchronous replication](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/about-galera-replication#synchronous-vs.-asynchronous-replication) requires the [binary log](https://dev.mysql.com/doc/refman/8.4/en/binary-log.html) to be enabled on the MySQL source. If not enabled, enable it on at least one node in your MySQL cluster.

    1. **Edit `my.cnf`**: In the `[mysqld]` section of your [MySQL configuration file](https://dev.mysql.com/doc/refman/8.4/en/replication-options-binary-log.html#option_mysqld_log-bin), add `log-bin=mysql-bin`.
    2. **Restart MySQL**: A server restart is required for the change to take effect.

{% hint style="danger" %}
Restarting MySQL will cause a brief outage for the node.
{% endhint %}

2. **Create the Backup with `mysqldump`**

Use `mysqldump` from the source MySQL server to create a full backup. Using `--all-databases` and `--master-data` will include all databases and the binary log position needed to start replication.

{% code overflow="wrap" %}
```bash
mysqldump --user=backup_user --password --all-databases --master-data=2 > /path/to/backup.sql
```
{% endcode %}

{% hint style="info" %}
This above command generates a backup file and logs the source's binary log file name and position in the output.
{% endhint %}
{% endstep %}

{% step %}
#### Bootstrap the MariaDB Cluster and Restore Data

Start the first node of the MariaDB cluster and load the MySQL backup.

1. **Bootstrap the First Node**

Start the first MariaDB node with the `--wsrep-new-cluster` option. This initializes the cluster.

```bash
sudo galera_new_cluster
```

2. **Load the Backup File**

Transfer the `backup.sql` file to the first MariaDB node and import it:

```bash
mariadb -u root -p < /path/to/backup.sql
```

3. **Start Subsequent Nodes**

Start the MariaDB service normally on the remaining nodes. They will connect to the first node, and a State Snapshot Transfer (SST) will automatically sync their data.

```bash
sudo systemctl start mariadb
```

4. **Verify the Cluster**

Connect to any node and check the cluster size to ensure all nodes have joined successfully.

```sql
SHOW STATUS LIKE 'wsrep_cluster_size';
```

{% hint style="info" %}
Cluster size should match the number of nodes in your cluster.
{% endhint %}
{% endstep %}

{% step %}
### Set Up Asynchronous Replication

Configure one of the MariaDB nodes to act as a replica of the source MySQL cluster.

1. **Create a Replication User on MySQL**

On the MySQL source node where binlogging is enabled, create a dedicated user for replication.

```sql
CREATE USER 'repl_user'@'mariadb_node_ip' IDENTIFIED BY 'your_password';
GRANT REPLICATION SLAVE ON *.* TO 'repl_user'@'mariadb_node_ip';
```

2. **Configure the MariaDB Replica**

On one of the MariaDB nodes, configure and start the [replication process](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/using-mariadb-replication-with-mariadb-galera-cluster/configuring-mariadb-replication-between-two-mariadb-galera-clusters). Use the binary log file and position noted from the `mysqldump` output (`MASTER_LOG_FILE` and `MASTER_LOG_POS`) or use GTID-based replication.

```sql
CHANGE MASTER TO
  MASTER_HOST='mysql_source_ip',
  MASTER_PORT=3306,
  MASTER_USER='repl_user',
  MASTER_PASSWORD='your_password',
  MASTER_USE_GTID=slave_pos;

START SLAVE;
```
{% endstep %}

{% step %}
### Monitor and Failover

With replication running, the MariaDB cluster will catch up with any changes made to the MySQL cluster since the backup was taken.

1. **Monitor Replication Lag**

Check the replica status on the MariaDB node to ensure it is synchronized.

```sql
SHOW SLAVE STATUS\G
```

Ensure the following conditions are met on the replica:

* `Slave_IO_Running: Yes`
* `Slave_SQL_Running: Yes`
* `Seconds_Behind_Master: 0`

A `Seconds_Behind_Master` value of `0` indicates the replica is completely synchronized.

2. **Perform the Failover**

Once the MariaDB cluster is fully synchronized, follow these steps:

1. **Stop Application Traffic:** Cease traffic to the MySQL cluster.
2. **Verify Synchronization:** Confirm the MariaDB replica has processed all events from the MySQL binary log.
3. **Promote MariaDB:**
   * Stop replication on the MariaDB node using `STOP SLAVE;`.
   * Update your application to connect to the MariaDB Galera Cluster.
4. **Resume Application Traffic:** Redirect traffic to the MariaDB cluster.
5. **Decommission MySQL:** After confirming the application runs smoothly on MariaDB, decommission the MySQL cluster.
{% endstep %}
{% endstepper %}
