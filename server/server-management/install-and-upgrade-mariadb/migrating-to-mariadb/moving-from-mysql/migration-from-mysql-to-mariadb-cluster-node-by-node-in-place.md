---
description: >-
  Instructions for a rolling migration where individual nodes in a MySQL cluster
  are taken offline, wiped, and replaced with MariaDB nodes, eventually forming
  a new cluster.
---

# Migration from MySQL to MariaDB Cluster (Node-by-Node In-Place)

{% hint style="warning" %}
**Version Requirement**

This guide provides instructions for migrating a **MySQL 8.0 Galera Cluster** to a **MariaDB Galera Cluster 11.4**. Ensure that your systems meet or exceed these version requirements before proceeding. Please refer to the [Prerequisites](migration-from-mysql-to-mariadb-cluster-node-by-node-in-place.md#prerequisites) for detailed version information.

The **End-of-Life (EOL)** date for continued maintenance and regular binary releases of MySQL Galera Cluster will be **September 30, 2026**.
{% endhint %}

This guide outlines the procedure for migrating a live MySQL Galera Cluster to a MariaDB Galera Cluster. It follows the process for migrating a live MySQL Galera Cluster to a MariaDB Galera Cluster by replacing the binaries on each node sequentially. This "In-Place" method maintains cluster availability during the migration, although the cluster capacity will be reduced while individual nodes are being processed.

## Prerequisites

* **Source:** MySQL Galera Cluster 8.0.43-26.4.24 or later.
* **Target:** MariaDB Community Server 11.4 (LTS) or later.
* **Library:** MariaDB Galera library 26.4.24 or latest stable edition.
* **Tools:**
  * `mysqldump` (installed with the server).
  * `mariadb-backup` (installed with MariaDB).
* **Access:** Root access to the operating system and the database.

{% hint style="danger" %}
**Cluster Backup**

This migration involves uninstalling software and wiping data directories on live nodes. **A full cluster backup (using Xtrabackup or Volume Snapshot) is mandatory before proceeding.**
{% endhint %}

## Incompatibility Check & Data Preparation

{% hint style="warning" %}
**Perform these steps on the running MySQL Cluster BEFORE shutting down any nodes.**
{% endhint %}

### Incompatibilities and Feature Differences

MariaDB maintains high levels of compatibility with MySQL, but you still need to [check for incompatibilities and feature differences](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/incompatibilities-and-feature-differences-between-mariadb-rolling-and-mysql) to select the most suitable MariaDB version compatible with your current MySQL server.

While MariaDB and MySQL share a common history, they have diverged significantly. You must "clean" the schema and configurations to ensure data compatibility before the migration begins.

#### 1. Authentication Protocol

MySQL 8.0 defaults to `caching_sha256_password`. MariaDB does not support the `caching_sha256_password` authentication protocol in all released versions (which is cumbersome and not secure for in-house attacks, since clear-text passwords are available inside the server).

**Support Status:**

* Implemented via [MDEV-9804](https://www.google.com/search?q=https://jira.mariadb.org/browse/MDEV-9804) for version 12.1.1.
* Available in the CS release based on [MDEV-37600](https://jira.mariadb.org/browse/MDEV-37600).
* Already supported in 11.8 Enterprise Server via [MENT-2359](https://jira.mariadb.org/browse/MENT-2359).
* Available in 11.4 Enterprise Server with the December 2025 release as a rebase of [MDEV-37600](https://jira.mariadb.org/browse/MDEV-37600).

{% hint style="info" %}
**For MySQL 8.4 Users**&#x20;

Ensure `mysql_native_password=ON` is set in your configuration, or you will receive the error: `Plugin 'mysql_native_password' is not loaded`.
{% endhint %}

You can check which MySQL users are using SHA-256 or caching\_sha256\_password by executing:

```sql
SELECT user, plugin FROM mysql.user WHERE plugin LIKE "%sha%";
```

You can change the user to use a protocol compatible with both MySQL and MariaDB with:

{% code overflow="wrap" %}
```sql
ALTER USER user_name IDENTIFIED WITH mysql_native_password BY 'new_password';
```
{% endcode %}

#### 2. JSON Column Conversion

MySQL stores JSON as a native binary type. MariaDB stores JSON as an alias for `LONGTEXT` with constraint checks. Galera replication may break if you attempt to replicate binary JSON objects from MySQL to MariaDB.

Check if you have tables that use the MySQL JSON type:

```sql
SELECT table_schema, table_name FROM information_schema.COLUMNS
WHERE data_type="JSON";
```

You can convert the JSON column to text with:

```sql
ALTER TABLE table_name MODIFY json_column LONGTEXT;
```

#### 3. Encryption and Compression

Encryption and compression table options are very different in MySQL compared to MariaDB. Logical dump will naturally de-encrypt/de-compress table contents but syntax used for creating tables is not supported by MariaDB.

For example:

{% code overflow="wrap" %}
```sql
CREATE TABLE `t1` (
`c1` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMPRESSION='lz4'
```
{% endcode %}

leads to: `ERROR 1911 (HY000) at line 1174: Unknown option 'COMPRESSION'`

Therefore, encrypted/compressed tables need to be de-encrypted/de-compressed before starting the conversion, and then encrypted/compressed again afterwards using MariaDB syntax.

**Detect encrypted tables:**

{% code overflow="wrap" %}
```sql
SELECT table_schema, table_name, create_options FROM information_schema.TABLES WHERE
create_options LIKE "%ENCRYPT%";
```
{% endcode %}

**Detect compressed tables:**

{% code overflow="wrap" %}
```sql
SELECT table_schema, table_name, create_options FROM information_schema.TABLES WHERE
create_options LIKE "%COMP%";
```
{% endcode %}

**Action:** Run `ALTER TABLE` to remove the conflicting **`ENCRYPTION`** and **`COMPRESSION`** attributes. They can be re-enabled using MariaDB syntax after the full migration is complete.

#### 4. General Tablespaces

MariaDB does not support MySQL general tablespaces. In MySQL, these are used to store tables in specific external files rather than the default data directory. During migration, this `TABLESPACE` argument is ignored.

**Example Scenario:** In MySQL, a user creates a custom tablespace file at a specific path and assigns a table to it:

```sql
-- MySQL: Creating a tablespace in a custom file location
mysql> CREATE TABLESPACE `ts1` ADD DATAFILE '/home/jan/galeradb/node1/ts1.ibd' Engine=InnoDB;

-- MySQL: Creating a table assigned to that tablespace
mysql> CREATE TABLE t1 (c1 INT PRIMARY KEY) TABLESPACE ts1;
```

If you examine the table definition in MySQL, you will see the tablespace assignment:

```sql
mysql> show create table t1;
| t1 | CREATE TABLE `t1` (
 `c1` int NOT NULL,
 PRIMARY KEY (`c1`)
) /*!50100 TABLESPACE `ts1` */ ENGINE=InnoDB ... |
```

**Migration Behavior:** When this table is migrated to MariaDB (via `mysqldump`), the `TABLESPACE 'ts1'` attribute is ignored.

* **Result:** The table `t1` will be created as a standard file-per-table in the default MariaDB data directory (e.g., `/var/lib/mysql/dbname/t1.ibd`).
* **Loss of Path:** It will **not** use the custom path `/home/jan/galeradb/node1/ts1.ibd`.sq

{% hint style="warning" %}
During cluster migration make sure that **no new tablespaces are created** and **no new tables created inside a general tablespaces**.
{% endhint %}

#### 5. XA Transactions

Ensure no XA transactions are in a `PREPARED` state, as these cannot be migrated cleanly.

```sql
XA RECOVER; -- Should return an empty set
```

## Global Cluster Preparation

{% hint style="info" %}
**Perform these steps on the running MySQL Cluster.**
{% endhint %}

### 1. Create the SST User (Crucial)

The `mysql.user` system table structure differs between vendors and **will not migrate automatically**. You must create the SST user now so it exists in the data stream before the switch.

```sql
-- Create user compatible with both engines
CREATE USER 'sst_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'strong_password';
GRANT ALL PRIVILEGES ON *.* TO 'sst_user'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Configure InnoDB Settings

Ensure these settings are active on the MySQL cluster.

* **`innodb_file_per_table = 1`**
  * This is the default setting for MySQL and MariaDB. If this is not set, you must use `mysqldump` for the entire migration, as specific recommendations regarding tablespaces will not work.
* **`innodb_flush_log_at_trx_commit = 1`**
  * InnoDB writes the log buffer to the log file and flushes it to disk after every transaction commit. This is the safest option, ensuring no data loss in a crash, though it comes at the cost of slower performance due to frequent disk I/O.

### 3. Galera Provider Options

* **`gcache.size`**: Should be large enough to avoid SST (State Snapshot Transfer) when a node is temporarily out of the cluster. A larger cache increases the chance of a faster IST (Incremental State Transfer).
  * [See: Customizing gcache.size](https://galeracluster.com/documentation/html_docs_remove-wsrep-new-cluster/kb/customizing-gcache-size.html)

## Migrating the First Node ("The Bridge")

This is the most complex step. This node will bridge the gap between the MySQL cluster and the new MariaDB environment.

{% stepper %}
{% step %}
### Isolate and Shutdown

1. **Remove from Load Balancer:** Ensure no application traffic is hitting this node.
2.  **Clean Shutdown Prep:**

    <pre class="language-sql" data-title="Requirement: This is required when upgrading between major versions of both MySQL and MariaDB as the format of the undo or redo files can change between major versions."><code class="lang-sql">SET GLOBAL innodb_fast_shutdown = 0;
    </code></pre>
3.  **Stop the Service:**

    ```bash
    mysqladmin -u root -p shutdown
    ```
{% endstep %}

{% step %}
### Swap Binaries & Wipe Data

1. **Uninstall MySQL:** Remove all MySQL server and client packages using your OS package manager (e.g., `apt remove`, `dnf remove`).
2.  **Clean Data Directory:** One way is to move all files under `datadir` to a new directory.

    ```bash
    mv /var/lib/mysql /var/lib/mysql_backup_timestamp
    mkdir /var/lib/mysql
    chown mysql:mysql /var/lib/mysql
    ```
3. **Install MariaDB:** Install `mariadb-server` and `mariadb-backup`.
{% endstep %}

{% step %}
### Configure MariaDB (`my.cnf`)

Update the configuration file to work with both MariaDB and MySQL.

**Verify Configuration:** Before starting the service, verify that your configuration file does not contain unsupported options (such as `regexp-time-limit`).

```bash
mariadbd --help --verbose > /tmp/log 2>&1
```

Check `/tmp/log` for any errors or warnings about unknown variables and adjust your configuration files if needed.

**Required Settings:** You **must** add these specific settings for the first node:

{% code overflow="wrap" %}
```ini
[galera]
# ... standard galera settings ...

# 1. IGNORE PROTOCOL MISMATCH
# Required to avoid application protocol mismatch messages during migration.
wsrep_provider_options="gcs.check_appl_proto=0;gcache.size=2G"

# 2. USE LOGICAL SST (First Node Only)
# wsrep_sst_method should be set to mysqldump for the first MariaDB node 
# to join the MySQL cluster.
wsrep_sst_method=mysqldump

# 3. SST AUTHENTICATION
# Should contain user and password and this user should exist on both 
# MySQL and MariaDB databases with sufficient access rights.
wsrep_sst_auth=sst_user:strong_password
```
{% endcode %}
{% endstep %}

{% step %}
### Start and Join

Start the MariaDB service:

```bash
systemctl start mariadb
```

When initiated, the node connects to the MySQL cluster and automatically triggers a `mysqldump` on a designated MySQL donor node. It then imports the SQL dump stream, effectively reconstructing the database in MariaDB's native format.
{% endstep %}

{% step %}
### Post-Join Upgrade

Once the node is `Synced`, run `mariadb-upgrade` to fix system tables.

{% hint style="warning" %}
Manually re-create the `sst_user` (and other system users) if `mariadb-upgrade` reports issues, as the `mysql.user` table structure is not fully compatible.
{% endhint %}
{% endstep %}
{% endstepper %}

## Migrating Subsequent Nodes

Once the first node (Node A) is successfully running MariaDB, you can migrate Node B, Node C, etc.

{% stepper %}
{% step %}
### Shutdown and Replace

1.  **Set Fast Shutdown:**

    ```sql
    SET GLOBAL innodb_fast_shutdown = 0;
    ```

    _Required because undo/redo log formats may change between versions._
2. **Shutdown:** `mysqladmin -u root -p shutdown`
3. **Wipe & Install:** Uninstall MySQL, Wipe Datadir, Install MariaDB.
{% endstep %}

{% step %}
### Configure MariaDB

The configuration differs slightly for subsequent nodes. We switch back to **Physical Backups** for speed.

{% code overflow="wrap" %}
```sql
[galera]
# ... standard galera settings ...

# 1. Point to the MariaDB Donor
# After the first MariaDB node has successfully joined, this variable 
# should be set on all other nodes to the value of wsrep_node_name 
# on the first MariaDB node.
wsrep_sst_donor=Name_of_First_MariaDB_Node

# 2. Use Binary SST
# For other joining nodes, mariabackup value should be used.
wsrep_sst_method=mariabackup
wsrep_sst_auth=sst_user:strong_password

wsrep_provider_options="gcs.check_appl_proto=0"
```
{% endcode %}
{% endstep %}

{% step %}
### Start and Join

Start the service. The node will perform a binary snapshot transfer (`mariabackup`) from the first MariaDB node.

Repeat the above 3 steps for all remaining nodes.
{% endstep %}
{% endstepper %}

## Finalization

Once all nodes are running MariaDB:

1. **Cleanup Config:** Remove `gcs.check_appl_proto=0` and `wsrep_sst_donor` from `my.cnf` on all nodes. Reset `wsrep_sst_method` to `mariabackup` on the first node.
2. **Security:** Run `mariadb-secure-installation` to secure the root account and remove anonymous users.
3. **Features:** Re-enable encryption or compression using MariaDB-supported syntax if required.

## Known Issues & Limitations

#### 1. `mysql.user` Migration

The `mysql.user` table structure is not fully compatible and cannot be migrated automatically.

* **Impact:** The administrator must create necessary users for the MariaDB database manually.
* **Workaround:** In testing, using `--skip-table=mysql.user` during dump/restore and manually creating the necessary SST user was required.
* **Reference:** [MDEV-33486](https://jira.mariadb.org/browse/MDEV-33486)

#### 2. `regexp-time-limit` Parameter

MariaDB currently does not support the `regexp-time-limit` parameter.

* **Impact:** If this variable exists in your configuration or scripts, the server may fail to start or throw errors.
* **Reference:** [MySQL Sysvar: regexp\_time\_limit](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_regexp_time_limit), [MDEV-37403](https://jira.mariadb.org/browse/MDEV-37403)

#### 3. `wsrep_start_position` Mismatch

MariaDB does not understand the `wsrep_start_position` format provided by MySQL due to GTID formatting differences.

* **Example:** MySQL node will use a set `wsrep_start_position` like: `”60e63a7-734c-11f0-bd90-97669e82ccf4:2284/2281/11/0747b7c5-734c-11f0-a69b-00e04ca2f8fe”`
* **Reference:** [MGL-57](https://jira.mariadb.org/browse/MGL-57)

#### 4. Replication Direction

Replication from MariaDB → MySQL is **not supported**.

* **Impact:** During migration, there can be **no load** directed to the MariaDB nodes until the entire cluster is migrated.

#### 5. Testing Scope

Currently, migration from 8.0.x has been verified to work on a simple `sysbench` database workload.

#### Required Code Changes (References)

For developers or those compiling from source, the following changes were relevant to this migration path:

* [codership-mariadb-server Pull Request #519](https://github.com/mariadb-corporation/codership-mariadb-server/pull/519)
* [codership-mysql Pull Request #2062](https://github.com/mariadb-corporation/codership-mysql/pull/2062)
