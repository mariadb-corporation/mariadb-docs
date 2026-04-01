---
description: MariaDB Galera Cluster quickstart guide
---

# MariaDB Galera Cluster Guide

### Quickstart Guide: MariaDB Galera Cluster

MariaDB Galera Cluster provides a multi-primary (active-active) cluster solution for MariaDB, enabling high availability, read/write scalability, and true synchronous replication. This means any node can handle read and write operations, with changes are certified synchronously across the Primary Component before a transaction is committed. This ensures that nodes remain in a consistent logical order, though individual nodes may experience temporal 'apply lag' as changes are processed from their receive queues by slave threads. It's exclusively available on Linux.

#### 1. Prerequisites

Before starting, ensure you have:

* **At least three nodes:** For redundancy and avoiding split-brain scenarios (bare-metal or virtual machines).
* **Linux Operating System:** A compatible Debian-based (e.g., Ubuntu, Debian) or RHEL-based (e.g., CentOS, Fedora) distribution.
* **Synchronized Clocks:** All nodes should have NTP configured for time synchronization.
* **SSH Access:** Root or sudo access to all nodes for installation and configuration.
* **Network Connectivity:** All nodes must be able to communicate with each other over specific ports (see Firewall section). Low latency between nodes is ideal.
* **`rsync`:** Install `rsync` on all nodes, as it's commonly used for State Snapshot Transfers (SST).
  * `sudo apt install rsync` (Debian/Ubuntu)
  * `sudo yum install rsync` (RHEL/CentOS)

#### 2. Installation (on Each Node)

Install MariaDB Server and the Galera replication provider on **all nodes** of your cluster.

**a. Add MariaDB Repository:**

It's recommended to install from the official MariaDB repositories to get the latest stable versions. Use the MariaDB Repository Configuration Tool (search "MariaDB Repository Generator") to get specific instructions for your OS and MariaDB version.

**Example for Debian/Ubuntu (MariaDB 10.11):**

```bash
sudo apt update
sudo apt install dirmngr software-properties-common apt-transport-https ca-certificates curl -y
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
sudo apt update
```

**b. Install MariaDB Server and Galera:**

```bash
sudo apt install mariadb-server mariadb-client galera-4 -y # For MariaDB 10.4+ or later, galera-4 is the provider.
                                                           # For older versions (e.g., 10.3), use galera-3.
```

**c. Secure MariaDB Installation:**

Run the security script on each node to set the root password and remove insecure defaults.

```bash
sudo mariadb-secure-installation
```

* Set a strong root password.
* Answer `Y` to remove anonymous users, disallow remote root login, remove test database, and reload privilege tables.

#### 3. Firewall Configuration (on Each Node)

Open the necessary ports on each node's firewall to allow inter-node communication.

```bash
# Example for UFW (Ubuntu)
sudo ufw allow 3306/tcp  # MariaDB client connections
sudo ufw allow 4567/tcp  # Galera replication (multicast and unicast)
sudo ufw allow 4567/udp  # Galera replication (multicast)
sudo ufw allow 4568/tcp  # Incremental State Transfer (IST)
sudo ufw allow 4444/tcp  # State Snapshot Transfer (SST)
sudo ufw reload
sudo ufw enable # If firewall is not already enabled
```

Adjust for your firewall system (e.g., `firewalld` for RHEL-based systems).

#### 4. Configure Galera Cluster (`galera.cnf` on Each Node)

Create a configuration file (e.g., `/etc/mysql/conf.d/galera.cnf`) on **each node**. The content will be largely identical, with specific changes for each node's name and address.

**Example `galera.cnf` content:**

```toml
[mysqld]
# Basic MariaDB settings
binlog_format=ROW
default_storage_engine=InnoDB
innodb_autoinc_lock_mode=2
bind-address=0.0.0.0 # Binds to all network interfaces. Adjust if you have a specific private IP for cluster traffic.

# Galera Provider Configuration
wsrep_on=ON
wsrep_provider=/usr/lib/galera/libgalera_smm.so # Adjust path if different (e.g., /usr/lib64/galera-4/libgalera_smm.so)

# Galera Cluster Configuration
wsrep_cluster_name="my_galera_cluster" # A unique name for your cluster

# IP addresses of ALL nodes in the cluster, comma-separated.
# Use private IPs if available for cluster communication.
wsrep_cluster_address="gcomm://node1_ip_address,node2_ip_address,node3_ip_address"

# This node's specific configuration
wsrep_node_name="node1" # Must be unique for each node (e.g., node1, node2, node3)
wsrep_node_address="node1_ip_address" # This node's own IP address
```

**Important:**

* **`wsrep_cluster_address`:** List the IP addresses of _all_ nodes in the cluster on _every_ node.
* **`wsrep_node_name`:** Must be unique for each node (e.g., `node1`, `node2`, `node3`).
* **`wsrep_node_address`:** Set to the specific IP address of the node you are configuring.

#### 5. Start the Cluster

a. Bootstrapping the First Node:

Start MariaDB on the first node with the --wsrep-new-cluster option. This tells it to form a new cluster. Do this only once for the initial node of a new cluster.

```bash
sudo systemctl stop mariadb # Ensure it's stopped
sudo galera_new_cluster    # This command often wraps the systemctl start --wsrep-new-cluster
                           # Alternatively: sudo systemctl start mariadb --wsrep-new-cluster
```

b. Starting Subsequent Nodes:

For the second and third nodes, start the MariaDB service normally. They will discover and join the existing cluster using the wsrep\_cluster\_address specified in their configuration.

```bash
sudo systemctl start mariadb
```

#### 6. Verify Cluster Operation

After all nodes are started, verify that they have joined the cluster.

a. Check Cluster Size (on any node):

Connect to MariaDB on any node and check the cluster status:

```bash
sudo mariadb -u root -p
```

Inside the MariaDB shell:

```sql
SHOW STATUS LIKE 'wsrep_cluster_size';
```

The `Value` should match the number of nodes in your cluster (e.g., `3`).

**b. Test Replication:**

1.  On `node1`, create a new database and a table:

    ```sql
    CREATE DATABASE test_db;
    USE test_db;
    CREATE TABLE messages (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(255));
    INSERT INTO messages (text) VALUES ('Hello from node1!');
    ```
2.  On `node2` (or `node3`), connect to MariaDB and check for the new database and table:

    ```sql
    SHOW DATABASES; -- test_db should appear
    USE test_db;
    SELECT * FROM messages; -- 'Hello from node1!' should appear
    ```
3.  Insert data from `node2`:

    ```sql
    INSERT INTO messages (text) VALUES ('Hello from node2!');
    ```
4.  Verify on `node1` that the new data is present:

    ```sql
    USE test_db;
    SELECT * FROM messages; -- 'Hello from node2!' should appear
    ```

This confirms synchronous replication is working.

#### Further Resources:

* [How to Set up MariaDB Galera Clusters on Ubuntu 22.04 (Linode)](https://www.linode.com/docs/guides/how-to-set-up-mariadb-galera-clusters-on-ubuntu-2204/)
* [MariaDB Galera Cluster - Binary Installation (galeracluster.com)](https://galeracluster.com/documentation/html_docs_mariadb-installation/documentation/install-mariadb.html)
* [Getting Started with MariaDB Galera Cluster (MariaDB.com/kb)](../galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster.md)
