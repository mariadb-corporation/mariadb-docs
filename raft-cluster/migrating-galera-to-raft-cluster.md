---
description: >-
  Migrate a running three-node Galera Cluster to MariaDB Raft Cluster on Enterprise Server 12.3, one node at a time, with asynchronous GTID replication and a single short write pause.
---

# Migrating from Galera Cluster to Raft Cluster

This page describes how to migrate a three-node Galera Cluster to MariaDB Raft Cluster on MariaDB Enterprise Server 12.3. You convert one node at a time, on the existing hosts and with the existing data, and the application keeps writing during almost the whole procedure. A temporary asynchronous replication link carries the writes from the Galera cluster to the new Raft cluster. Writes pause once, for the cutover.

{% hint style="info" %}
Each node is converted on its own host, but a Galera node and a Raft node never join the same cluster. Running both node types in one cluster is not part of this procedure.
{% endhint %}

## How the Migration Works

The nodes are called Node 1, Node 2, and Node 3. Node 1 serves the writes at the start.

* Node 3 leaves the Galera cluster, gets the new server, and restarts on its own data as a one-node Raft cluster. It then follows Node 1 as an asynchronous replica, so it receives every write that Node 1 still accepts.
* Node 2 leaves Galera, gets the new server, joins the Raft cluster of Node 3, and copies its data from Node 3 with `mariabackup`.
* When Node 2 and Node 3 are Raft nodes, you move the writes to Node 2, and Node 3 stops following Node 1. This is the only write pause.
* Node 1 is converted last. It joins the Raft cluster and copies its data from Node 3.

At the end, all three nodes are Raft nodes, one of them is the leader, and no asynchronous replication is left.

## Before You Begin

Check these points before you change any node:

* All three Galera nodes are `Synced`, and `wsrep_cluster_size` is `3` on each node.
* The application can write to any node. You move the writes by changing the target of the application or of the load balancer. This page calls that target the write endpoint.
* All tables use InnoDB, as Galera replication requires.
* Binary logging is on in `ROW` format on every node, `log_slave_updates` is on, each node has a unique `server_id`, and all nodes use `wsrep_gtid_mode=ON` with the same `wsrep_gtid_domain_id`. In the Engineering test, each node also had its own `gtid_domain_id`.
* You have a Customer Download Token for the MariaDB Enterprise repository.
* The Raft listen port and the Raft state transfer port of every node are open between the nodes. Node 3 can also reach the MariaDB port of Node 1.
* Every Raft node runs MariaDB Enterprise Server 12.3.x. You can install the Enterprise Server 12.3 packages on every node: the server, `mariadb-backup`, `galera-enterprise-4`, and `mariadb-raft`. For the repository setup and the package names for your operating system, see [Installation (on Each Node)](mariadb-raft-cluster-quickstart-guide.md#installation-on-each-node).

Install `galera-enterprise-4` on every node. A node that is not yet converted still runs as a Galera node and needs the library, and a Raft node does not use it. Enterprise Server 12.3 does not start with a Galera library that lacks support for the allowlist service, for example Galera 4.9 from some distribution repositories.

{% hint style="warning" %}
The default `raft_tls_mode` is `VERIFY_CA`. With this default, a Raft node does not start until you configure a CA and certificates, unless you set the mode to `ENCRYPT` or `DISABLED`. Decide on the TLS mode before you start. See [A CA for One Raft Cluster](raft-cluster-ca.md) and [Choose a TLS Setup (on Each Node)](mariadb-raft-cluster-quickstart-guide.md#choose-a-tls-setup-on-each-node).
{% endhint %}

### Create the Users

Create a replication user on Node 1 and a user for the `mariabackup` state transfer. Galera copies both to the other nodes. Node 3 uses the replication user to follow Node 1.

```sql
CREATE USER 'repl'@'%' IDENTIFIED BY 'repl_passwd';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

CREATE USER 'sst'@'localhost' IDENTIFIED BY 'sst_passwd';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR, REPLICATION CLIENT ON *.* TO 'sst'@'localhost';
```

### Take a Backup

Take a full backup of Node 1 before any change. A failed migration can leave data files that you cannot revert.

```bash
sudo mariadb-backup --backup \
      --user=mariadb-backup_user \
      --password=mariadb-backup_passwd \
      --target-dir=/data/backup/premigration_backup

sudo mariadb-backup --prepare \
      --target-dir=/data/backup/premigration_backup
```

Test that you can restore the backup.

## Restrictions

* **Reduced fault tolerance.** The Galera cluster has two nodes after Step 1, and one node after Step 2. The Raft cluster has one or two nodes until Step 4. Plan the migration for a period of low risk, and monitor all nodes.
* **Two-node quorum.** A Raft cluster of two nodes needs both nodes to elect a leader.
* **No writes to Raft nodes before the cutover.** A Raft node that follows the Galera cluster is a replica. If it receives writes, its data diverges.
* **Bootstrap marker.** Node 3 was not the last node to leave the Galera cluster. Set its bootstrap marker before you start it as a Raft node. See [Step 1](#step-1-convert-node-3-and-make-it-the-first-raft-node).
* **Donor load.** The donor node carries the load of the backup during each state transfer.
* **State transfer replaces the data directory.** A node that joins by state transfer receives a full copy of the data from the donor, and the copy replaces its previous data directory. Keep TLS certificates and keys outside the data directory.
* **Schema changes.** Schema changes during the migration were not tested. Avoid them.

## When Writes Are Not Possible

| Steps | Writes |
| ----- | ------ |
| Step 1 and Step 2 | Continue on the Galera cluster (Node 1). |
| Step 3 | Paused. The pause starts when you stop the writes to Node 1 and ends when the write endpoint points to Node 2. |
| Step 3, after the pause, and Step 4 | Continue on Raft Node 2. |

During the pause, Node 3 applies the remaining changes and you remove the replication link. The length of the pause depends on the replica lag and on how long your clients take to reconnect.

## Prepare Each Node

Steps 1, 2, and 4 repeat the following tasks on one node. The procedure below tells you when to run each task.

### Stop the MariaDB Server

1. Set the shutdown mode:

   ```sql
   SET GLOBAL innodb_fast_shutdown = 1;
   ```

2. Check for prepared external XA transactions:

   ```sql
   XA RECOVER;
   ```

   Commit or roll back every prepared XA transaction that the statement lists.
3. Stop the server:

   ```bash
   sudo systemctl stop mariadb
   ```

### Remove the Old Version

The package manager refuses a major-version install over the old version, so remove the old version first. Check that the wildcard does not match packages of your own applications.

{% tabs %}
{% tab title="RHEL, AlmaLinux, CentOS, Rocky Linux" %}
```bash
sudo yum remove "MariaDB-*"
sudo yum remove galera-enterprise-4

# Nothing must remain. The command must print nothing.
rpm --query --all | grep -i -E "mariadb|galera"
```
{% endtab %}

{% tab title="Debian, Ubuntu" %}
```bash
sudo apt-get remove "mariadb-*"
sudo apt remove galera-enterprise-4

# Nothing must remain. The command must print nothing.
apt list --installed | grep -i -E "mariadb|galera"
```
{% endtab %}

{% tab title="SLES" %}
```bash
sudo zypper remove "MariaDB-*"
sudo zypper remove galera-enterprise-4

# Nothing must remain. The command must print nothing.
rpm --query --all | grep -i -E "mariadb|galera"
```
{% endtab %}
{% endtabs %}

### Install the New Version

Install the Enterprise Server 12.3 packages, including `galera-enterprise-4` and `mariadb-raft`, by following [Installation (on Each Node)](mariadb-raft-cluster-quickstart-guide.md#installation-on-each-node).

{% hint style="warning" %}
Pass `--mariadb-server-version="12.3"` when you run the repository setup script. Without it, the script configures the latest GA series, which is not 12.3.
{% endhint %}

### Configure the Raft Node

A Raft node uses these settings instead of the Galera provider settings. Keep your other `wsrep_` settings, for example `wsrep_cluster_name`, `wsrep_node_name`, `wsrep_gtid_mode`, and `wsrep_slave_threads`.

```ini
[mysqld]
plugin_load_add=raft
wsrep_on=ON
wsrep_provider=raft
wsrep_sst_method=mariabackup
wsrep_sst_auth=sst:sst_passwd
raft_node_id=node3
raft_bind_address=10.0.0.3
raft_listen_port=5208
raft_sst_listen_port=5210
raft_tls_mode=DISABLED
```

* `wsrep_sst_method=mariabackup` is the method that Engineering tested for the state transfer.
* `raft_node_id` is unique for each node. It is a string of at most 15 characters, or a UUID.
* `raft_listen_port` and `raft_sst_listen_port` must be open between the nodes. In this page, Node 1 uses `5008` and `5010`, Node 2 uses `5108` and `5110`, and Node 3 uses `5208` and `5210`.
* Do not set `wsrep_provider_options` with Galera options. The Galera library is not loaded, and the Raft plugin ignores the variable. Express any tuning with the `raft_` variables. See [Raft System Variables](raft-system-variables.md).
* `raft_tls_mode=DISABLED` in the example is only for a test network. For TLS, set `raft_tls_mode=VERIFY_CA`, `raft_ssl_ca`, `raft_ssl_cert`, and `raft_ssl_key`, and add the same certificates to the `[sst]` section together with `ssl-mode=VERIFY_CA`. See [`raft_tls_mode`](raft-system-variables.md#raft-tls-mode).
* The Raft server creates the socket `raft-server.sock` in the directory that `raft_data_dir` names. Unix socket paths are limited to about 107 characters, so set `raft_data_dir` to a short path if your default working directory is deep.
* A node that follows another node as an asynchronous replica can apply events in parallel. If you want that, set `slave_parallel_threads` on the replica (Node 3 in this procedure). The value is optional, and replication is correct with the default.

`wsrep_cluster_address` and `wsrep_sst_donor` are different for each node. The procedure gives them. The port in `wsrep_cluster_address` is the Raft listen port of that node: the port in `wsrep_node_address` if it has one, otherwise `raft_listen_port`.

### Start the Node and Upgrade the Data Directory

1. Start the server:

   ```bash
   sudo systemctl start mariadb
   ```

2. When the node is `Synced`, run the compatibility utility on that node:

   ```bash
   sudo mariadb-upgrade --skip-write-binlog
   ```

### Test the Node

Run these checks on the converted node.

1. Check the version and the provider:

   ```sql
   SELECT VERSION();
   SELECT @@wsrep_provider;
   ```

2. Check the node state:

   ```sql
   SHOW GLOBAL STATUS WHERE Variable_name IN
     ('wsrep_local_state_comment', 'wsrep_ready', 'wsrep_connected',
      'wsrep_cluster_status', 'wsrep_cluster_size', 'wsrep_provider_name',
      'Raft_node_id', 'Raft_current_leader_node_id');
   SELECT SERVER_STATUS_JSON FROM information_schema.RAFT_STATUS;
   ```

   `wsrep_local_state_comment` is `Synced`, `wsrep_ready` and `wsrep_connected` are `ON`, `wsrep_cluster_status` is `Primary`, `wsrep_provider_name` is `raft`, and the node sees a Raft leader.

## Procedure

### Step 1: Convert Node 3 and Make It the First Raft Node

1. Check on Node 1 that the writes work and that the cluster is `Synced`.
2. On Node 3, run [Stop the MariaDB Server](#stop-the-mariadb-server), [Remove the Old Version](#remove-the-old-version), and [Install the New Version](#install-the-new-version). Do not start it yet.
3. Check on Node 1 and Node 2 that the Galera cluster has size 2 and that the writes continue.
4. Node 3 left the Galera cluster before the other nodes, so you must allow it to start a new cluster on its data. In the data directory of Node 3, edit `grastate.dat`:

   ```
   safe_to_bootstrap: 1
   ```

5. Write the Raft configuration of Node 3 with an empty cluster address:

   ```ini
   wsrep_cluster_address=gcomm://
   ```

6. Start Node 3 and wait until it is `Synced`. Then run [Start the Node and Upgrade the Data Directory](#start-the-node-and-upgrade-the-data-directory) and [Test the Node](#test-the-node). The Raft cluster has size 1.

   {% hint style="info" %}
   The Raft plugin starts the `mariadb-raft-server` program, which must be in the `PATH` of the server process. If it is not, the node does not start, and the error log shows `mariadb-raft-server not found in PATH`. Install the `mariadb-raft` package on the node first.
   {% endhint %}

7. Make Node 3 an asynchronous replica of Node 1. Use the GTID position of Node 3 as the start. Node 1 keeps accepting writes, and Node 3 receives them.

   ```sql
   SET GLOBAL gtid_slave_pos=@@GLOBAL.gtid_binlog_pos;
   CHANGE MASTER TO MASTER_HOST='node1', MASTER_PORT=3306,
     MASTER_USER='repl', MASTER_PASSWORD='repl_passwd',
     MASTER_USE_GTID=slave_pos;
   START SLAVE;
   ```

8. Wait until Node 3 has caught up:

   ```sql
   SHOW SLAVE STATUS\G
   ```

   `Slave_IO_Running` and `Slave_SQL_Running` must be `Yes`, and `Seconds_Behind_Master` must be `0` or `1`.

Node 1 and Node 2 are not affected. Writes are allowed on the Galera cluster only.

### Step 2: Convert Node 2 and Join It to the Raft Cluster

1. On Node 2, run [Stop the MariaDB Server](#stop-the-mariadb-server), [Remove the Old Version](#remove-the-old-version), and [Install the New Version](#install-the-new-version).
2. Check that Node 1 is now alone in the Galera cluster (`wsrep_cluster_size` is `1` on Node 1), and that Node 3 is still a one-node Raft cluster.
3. Write the Raft configuration of Node 2. Node 2 joins the Raft cluster of Node 3 and takes a copy of the data from Node 3:

   ```ini
   wsrep_cluster_address=gcomm://10.0.0.3:5208
   wsrep_sst_donor=node3
   ```

4. Start Node 2. The start takes as long as the copy of the data takes.
5. Run [Start the Node and Upgrade the Data Directory](#start-the-node-and-upgrade-the-data-directory) (the start is already done) and [Test the Node](#test-the-node) on Node 2. The Raft cluster has size 2 with one leader.
6. Check on Node 3 that it still follows Node 1 and has no lag (`SHOW SLAVE STATUS\G`).
7. Check that both Raft nodes accept writes. Create a test table on one node and read it on the other.

Node 1 is the only Galera node, so fault tolerance is lowest in this step.

### Step 3: Move the Writes to Node 2

Node 2 is a Raft node and is up to date. Move all writes from Node 1 to Node 2 in this order, so that no write is lost.

1. Stop the writes to Node 1. Change the write endpoint so that the application no longer connects to Node 1, and stop the open sessions that write to Node 1.
2. Wait until Node 3 has applied everything from Node 1. Run this on Node 3:

   ```sql
   SHOW SLAVE STATUS\G
   ```

   `Seconds_Behind_Master` must be `0`, and `Read_Master_Log_Pos` must not change on repeated runs. For a stricter check, compare `@@gtid_binlog_pos` on Node 1 with `Gtid_IO_Pos` on Node 3.
3. Stop the replication on Node 3 and remove its configuration:

   ```sql
   STOP SLAVE;
   RESET SLAVE ALL;
   ```

   Check that `SHOW ALL SLAVES STATUS` on Node 3 returns no row.
4. Point the write endpoint to Node 2. Check that the application writes to Node 2 and that Node 3 receives the rows.
5. Stop the MariaDB server on Node 1. See [Stop the MariaDB Server](#stop-the-mariadb-server).
6. Check on Node 2 and Node 3 that the Raft cluster has size 2, one leader, and that the writes continue.

After this step, the Raft cluster is the system of record. Node 2 and Node 3 hold the only current copy of the data, so do not remove their data directories.

### Step 4: Convert Node 1 and Join It to the Raft Cluster

1. On Node 1, run [Remove the Old Version](#remove-the-old-version) (the server is already stopped) and [Install the New Version](#install-the-new-version).
2. Write the Raft configuration of Node 1. The cluster address lists the other Raft nodes. Node 1 takes a copy of the data from Node 3, and the copy replaces the Galera data directory of Node 1.

   ```ini
   wsrep_cluster_address=gcomm://10.0.0.3:5208,10.0.0.2:5108
   wsrep_sst_donor=node3
   ```

3. Start Node 1 and wait until it is `Synced`. Run [Start the Node and Upgrade the Data Directory](#start-the-node-and-upgrade-the-data-directory) and [Test the Node](#test-the-node) on it. The Raft cluster has size 3.
4. Add Node 1 to the write endpoint again, if you want it to take writes.

## Final Checks

Run this on every node:

```sql
SHOW GLOBAL STATUS WHERE Variable_name IN
  ('wsrep_cluster_size', 'Raft_current_leader_node_id', 'wsrep_last_committed');
SHOW ALL SLAVES STATUS\G
```

* `wsrep_cluster_size` is `3` on all nodes.
* All nodes name the same leader, and exactly one node is the leader.
* `wsrep_last_committed` is the same on all nodes when no write is running.
* `SHOW ALL SLAVES STATUS` returns no row.

Compare the data. Run this on each node for your important tables, and compare the results:

```sql
SET SESSION wsrep_sync_wait=15;
CHECKSUM TABLE db1.t1;
```

Accept the migration when all checks pass and the checksums are identical on the three nodes.

## If a Step Fails

* **A node that does not start:** read its error log. Check the Raft ports, `raft_node_id`, `wsrep_cluster_name`, the TLS mode, and the cluster address.
* **A joining node that does not get a copy:** check that the donor is `Synced`, that the `sst` user exists on the donor, and that the Raft state transfer port of the donor is open. Start the join again.
* **A Raft node that does not become a leader:** all nodes must use the same `wsrep_cluster_name`. A cluster of two nodes needs both nodes to elect a leader.
* **A failure before Step 3:** Node 1 and Node 2 are still Galera nodes and still hold all data. Start the old server on Node 3 with its old configuration and with `wsrep_cluster_address` set to the Galera nodes. Restore from the backup when the data directory is damaged.
* **A failure after Step 3:** Node 2 and Node 3 hold the only current copy of the data. Do not remove their data directories.

## Tested Versions

Engineering tested the procedure with three nodes of MariaDB Enterprise Server on one host. The target was MariaDB Enterprise Server 12.3.3, and a workload with 20 percent writes ran during the whole migration and moved to Node 2 at the cutover.

| Galera Server Version | Raft Server Version 12.3.3 |
| --------------------- | -------------------------- |
| 10.6.29 | Pass. Requires `mariadb-upgrade`. |
| 11.4.13 | Pass |
| 11.8.7 | Pass |
| 12.3.3 | Pass, also with TLS (`VERIFY_CA`) |

The test has these limits:

* The test validates the procedure. It is not a performance test, and this page gives no performance figures.
* It ran on one host with a small data set. The state transfer time for large data sets was not measured.
* TLS with certificate verification (`VERIFY_CA`) for Galera, Raft, and state transfer was tested only for Galera 12.3.3 to Raft 12.3.3. The other version combinations ran without TLS.
* The client redirect at the cutover was done by restarting the workload on another node.

## See Also

* [MariaDB Raft Cluster Quickstart Guide](mariadb-raft-cluster-quickstart-guide.md)
* [Raft System Variables](raft-system-variables.md)
* [A CA for One Raft Cluster](raft-cluster-ca.md)
* [MariaDB Raft Cluster: Team FAQ & Architectural Guide](mariadb-raft-cluster-team-faq-and-architectural-guide.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
