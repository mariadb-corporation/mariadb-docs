---
description: MariaDB MaxScale installation quickstart guide
---

# MariaDB MaxScale Installation Guide

### Quickstart Guide: MariaDB MaxScale

MariaDB MaxScale is an advanced, open-source database proxy that provides intelligent routing, load balancing, high availability, and security features for your MariaDB and MySQL deployments. It acts as an intermediary, forwarding database statements to one or more backend database servers based on configured rules and server roles, all transparently to your applications.

#### 1. Key Concepts

To understand MaxScale, familiarize yourself with these core components:

* **Servers:** These are your backend MariaDB or MySQL instances that MaxScale will manage traffic to.
* **Monitors:** Plugins that observe the health and state of your backend servers (e.g., primary, replica, down).
* **Routers:** Plugins that determine how client queries are directed to backend servers (e.g., `readwritesplit` router for directing writes to a primary and reads to replicas).
* **Services:** Define a combination of a router and a set of servers, along with any filters.
* **Listeners:** Define how clients connect to MaxScale (port, protocol) and which service they connect to.
* **Filters:** Optional components that can inspect, modify, or log queries as they pass through MaxScale (e.g., `qlafilter` for auditing).

#### 2. Installation

MariaDB MaxScale is typically installed from the official MariaDB repositories.

**a. Add MariaDB Repository:**

Use the MariaDB Repository Configuration Tool (search "MariaDB Repository Generator") to get specific instructions for your OS and MaxScale version.

**Installation for Debian/Ubuntu:**

```bash
sudo apt update
sudo apt install -y curl
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
sudo apt install -y maxscale
```

**Installation for RHEL/Rocky Linux/Alma Linux:**

```bash
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
sudo dnf install -y maxscale
```

#### 3. Basic Configuration (`/etc/maxscale.cnf`)

MaxScale's configuration is primarily done in its main configuration file in `/etc/maxscale.cnf`.

**a. Define Servers:**

Add a section for each of your backend MariaDB servers.

```ini
[server1]
type=server
# IP address or hostname of your first MariaDB server
address=192.168.1.101

[server2]
type=server
# IP address or hostname of your second MariaDB server
address=192.168.1.102
# Set the port if MariaDB is listening on a non-default port
port=3307
```

**b. Define a Monitor:**

This section tells MaxScale how to monitor your backend servers' health and roles and groups them into a cluster of servers.

```ini
[MariaDB-Cluster]
type=monitor
# The  MariaDB asynchronous replication monitoring module
module=mariadbmon
# List of servers to monitor
servers=server1,server2
# The user used for monitoring
user=maxscale_monitor
password=monitor_password
# Check every 5 seconds
monitor_interval=5s
```

**Important:** Create the `maxscale_monitor` user on your _backend MariaDB servers_ with appropriate privileges:

```sql
CREATE USER 'maxscale_monitor'@'%' IDENTIFIED BY 'monitor_password';
GRANT BINLOG ADMIN, CONNECTION ADMIN EVENT, PROCESS, READ_ONLY ADMIN, RELOAD, REPLICA MONITOR, REPLICATION CLIENT, REPLICATION SLAVE ADMIN, SET USER, SHOW DATABASES, ON *.* TO 'maxscale_monitor'@'%';
GRANT SELECT ON mysql.global_priv TO 'maxscale_monitor'@'%';
GRANT SELECT ON mysql.global_priv TO 'maxscale_monitor'@'%';
```

**c. Define a Service (e.g., Read-Write Split):**

This configures how MaxScale routes queries. The readwritesplit router is very common for replication setups as it load balances read while routing writes to the primary node.

```ini
[Read-Write-Service]
type=service
# The readwritesplit router module load balances reads and routes writes to the primary node
router=readwritesplit
# Servers available for this service
cluster=MariaDB-Cluster
# The user account used to fetch the user information from MariaDB
user=maxscale_user
password=maxscale_password
```

**Important:** Create the `maxscale_user` on your _backend MariaDB servers_ with the following privileges:

```sql
CREATE USER 'maxscale_user'@'%' IDENTIFIED BY 'maxscale_password';
GRANT SELECT ON mysql.user TO 'maxscale_user'@'%';
GRANT SELECT ON mysql.db TO 'maxscale_user'@'%';
GRANT SELECT ON mysql.tables_priv TO 'maxscale_user'@'%';
GRANT SELECT ON mysql.columns_priv TO 'maxscale_user'@'%';
GRANT SELECT ON mysql.procs_priv TO 'maxscale_user'@'%';
GRANT SELECT ON mysql.proxies_priv TO 'maxscale_user'@'%';
GRANT SELECT ON mysql.roles_mapping TO 'maxscale_user'@'%';
GRANT SHOW DATABASES ON *.* TO 'maxscale_user'@'%';
```

**d. Define a Listener:**

This specifies the port and protocol MaxScale will listen on for incoming client connections and which service to direct them to.

```ini
[Read-Write-Listener]
type=listener
# The service that this listener connects to
service=Read-Write-Service
# The port that MaxScale will listen on for client applications
port=3306
```

**e. Global MaxScale Configuration (usually at the top of `maxscale.cnf`):**

```ini
[maxscale]
# Select the number of worker threads automatically based on the CPU thread count
threads=auto
```

#### 4. Complete Configuration

Your `/etc/maxscale.cnf` should now look like this:

```ini
[maxscale]
threads=auto

[server1]
type=server
address=192.168.1.101

[server2]
type=server
address=192.168.1.102
port=3307

[MariaDB-Cluster]
type=monitor
module=mariadbmon
servers=server1,server2
user=maxscale_monitor
password=monitor_password
monitor_interval=5s

[Read-Write-Service]
type=service
router=readwritesplit
cluster=MariaDB-Cluster
user=maxscale_user
password=maxscale_password

[Read-Write-Listener]
type=listener
service=Read-Write-Service
port=3306
```

#### 5. Start and Enable MaxScale

After configuring `maxscale.cnf`, start and enable the MaxScale service.

```bash
sudo systemctl start maxscale
sudo systemctl enable maxscale
sudo systemctl status maxscale # Check status
```

#### 6. Basic Usage and Verification

Once MaxScale is running, configure your applications to connect to MaxScale's listener port instead of directly to a MariaDB server.

**Example (Connect with `mariadb` client from the MaxScale server):**

```bash
mariadb -h 127.0.0.1 -P 3306 -u my-user -p
```

**Verify Read-Write Split (if configured):**

1. Connect to MaxScale (`127.0.0.1:3306`).
2. Execute a `WRITE` query (e.g., `INSERT INTO your_table ...`). This should be routed to the primary server.
3. Execute a `READ` query (e.g., `SELECT * FROM your_table`). This should be load-balanced across your replica servers.
4. You can use `maxctrl list servers` and `maxctrl show servers` to observe routing in action.

#### Further Resources:

* [MariaDB MaxScale Installation Guide](https://www.google.com/search?q=https://mariadb.com/docs/maxscale/latest/install/\&authuser=1)
* [MariaDB MaxScale Configuration Guide](https://www.google.com/search?q=https://mariadb.com/docs/maxscale/latest/config/\&authuser=1)
* [MariaDB MaxScale GitHub Repository](https://github.com/mariadb-corporation/MaxScale)
* [DigitalOcean: How To Install and Configure MariaDB MaxScale (Tutorial)](https://www.google.com/search?q=https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-mariadb-maxscale-on-ubuntu-22-04\&authuser=1)
