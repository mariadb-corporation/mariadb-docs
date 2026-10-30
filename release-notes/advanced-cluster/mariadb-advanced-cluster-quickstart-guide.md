---
description: >-
  A step-by-step guide to deploying MariaDB Raft Cluster, covering
  installation, firewall, TLS and Raft configuration, cluster bootstrapping,
  and verifying replication across nodes
---

# MariaDB Raft Cluster Quickstart Guide

MariaDB Raft Cluster provides a highly available, strongly consistent, and fault-tolerant solution for database deployment. It utilizes the **Raft consensus protocol** to ensure that data is safely and synchronously replicated across all nodes, guaranteeing no lost transactions and providing a single, authoritative source of data through a **single active Leader** architecture.

Raft Cluster ships with MariaDB Enterprise Server 12.3.

{% hint style="warning" %}
Raft Cluster 1.0.0 is the first GA release. A rolling upgrade from an earlier (technical preview) release is not supported. A configuration from an earlier release does not start a node if it has no TLS settings, or if it uses the removed `raft_have_ssl` or `raft_ssl_verify_server_cert` variables. See [Choose a TLS Setup](#choose-a-tls-setup-on-each-node).
{% endhint %}

## Raft Protocol Overview

The Raft protocol is a consensus algorithm designed for managing replicated logs and ensuring data consistency across a distributed cluster. It simplifies the complexity of consensus by defining three key mechanisms: Leader Election, Log Replication, and Commit/Consensus via a Majority Quorum.

### Leader Election

Every node in the cluster exists in one of three states: **Follower**, **Candidate**, or **Leader**.

1. **Followers** are passive and only respond to requests from a Leader or Candidate
2. If a Follower does not receive a **heartbeat** from the current Leader within a set timeout, it transitions to a **Candidate** state and begins an election
3. The Candidate requests votes from the other nodes. The first Candidate to receive votes from a **majority quorum** of the total nodes wins the election and becomes the new **Leader**

### Log Replication

All write operations (transactions) must pass through the **Leader**.

1. The Leader appends the client’s request to its local log and then issues **AppendEntries** RPCs to all **Followers**
2. The Followers write the entry to their own local logs and acknowledge success back to the Leader
3. This mechanism ensures that all nodes maintain an identical, sequentially ordered transaction log

### Commit/Consensus via a Majority Quorum

A log entry is considered **committed** only after the Leader has successfully replicated the entry to, and received acknowledgments from, a **majority quorum** of the cluster nodes (i.e., (N/2) + 1, where N is the total number of nodes).

1. Once committed, the data is safely applied to the database state on the Leader and is guaranteed to be present on any future Leader, even in the event of failure. This majority rule ensures strong consistency and prevents split-brain scenarios

## Prerequisites

Before setting up your MariaDB Raft Cluster, ensure the following prerequisites are met on all nodes:

* **Three or more Nodes**: A minimum of three nodes is required to establish a majority quorum (e.g., 2 out of 3, 3 out of 5) and tolerate single node failure
* **Linux Operating System**: A compatible Linux distribution (e.g., Ubuntu, RHEL)
* **Synchronized Clocks**: Use NTP (Network Time Protocol) to ensure all nodes' system clocks are synchronized
* **SSH Access**: Root or sudo access to all nodes for configuration and installation
* **Network Connectivity**: All nodes must be able to communicate with each other over specific ports with low latency

## Installation (on Each Node)

Install MariaDB Enterprise Server and the associated Raft consensus provider on all nodes of your cluster.

<a id="download-the-advanced-cluster-technical-preview-tar-archive"></a>

Raft Cluster needs no installation procedure or package repository of its own. The Raft server ships as a separate package (`MariaDB-raft` on RHEL-based systems, `mariadb-raft` on Debian and Ubuntu) in the same MariaDB Enterprise repository as Enterprise Server, so installing it means following the standard Enterprise Server instructions and adding one package.

{% stepper %}
{% step %}
#### Configure the MariaDB Enterprise Repository for 12.3

Follow [MariaDB Package Repository Setup and Usage](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage) to download the `mariadb_es_repo_setup` script, verify its checksum, and run it with your Customer Download Token.

{% hint style="warning" %}
Pass `--mariadb-server-version="12.3"` when you run the script. It configures the latest GA series by default, which is **not** 12.3 — without this option you configure the wrong repository and install the wrong server version.
{% endhint %}

```bash
sudo ./mariadb_es_repo_setup --token="${token}" --apply \
   --mariadb-server-version="12.3"
```
{% endstep %}

{% step %}
#### Add the Raft Package

Include the Raft package in the install command alongside the Enterprise Server packages:

{% tabs %}
{% tab title="RHEL, CentOS & Rocky" %}
```bash
sudo yum install MariaDB-server MariaDB-backup galera-enterprise-4 MariaDB-raft
```

The earlier package name `mariadb-raft` also installs this package.
{% endtab %}

{% tab title="Debian & Ubuntu" %}
```bash
sudo apt install mariadb-server mariadb-backup galera-enterprise-4 mariadb-raft
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
The `galera-enterprise-4` package is required because of a dependency in the MariaDB Enterprise Server package.
{% endhint %}
{% endstep %}
{% endstepper %}

{% hint style="info" %}
If you install from a tar archive downloaded from the MariaDB download page rather than from a package repository, the Raft package is included in the MariaDB Enterprise RPM/DEB tar file. Extract the archive and install the Raft package (`MariaDB-raft` or `mariadb-raft`) alongside the server packages. See [Deploy with Package Tarballs](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/package-tarballs).
{% endhint %}

## Firewall Configuration (on Each Node)

Open the necessary ports on the firewall of each node to allow for both client connections and inter-node Raft communication.

| Port  | Protocol | Purpose                             |
| ----- | -------- | ----------------------------------- |
| 3306  | TCP      | Client connections to the database. |
| 50001 | TCP      | SST request listener                |
| 50002 | TCP      | Raft server internal communication  |

Example using UFW (Ubuntu/Debian):

```bash
# Allow client connections
sudo ufw allow 3306/tcp
# Allow RAFT cluster communication
sudo ufw allow 50001/tcp
sudo ufw allow 50002/tcp
sudo ufw reload
```

## Choose a TLS Setup (on Each Node)

The [raft\_tls\_mode](raft-system-variables.md#raft-tls-mode) variable sets the protection of the cluster connections. The default is `VERIFY_CA`. Under `VERIFY_CA`, a node does not start without a CA (`raft_ssl_ca` or `raft_ssl_capath`) and its own certificate and key. Thus a node with no TLS configuration does not start.

{% hint style="warning" %}
Choose the TLS mode before you deploy. You cannot change `raft_tls_mode` from `DISABLED` to `ENCRYPT` or `VERIFY_CA` with a rolling restart. The change needs a full cluster outage. If you may need TLS later, set up a cluster CA and use `VERIFY_CA` from the start.
{% endhint %}

Choose one of these setups.

### Option A: A CA for This Cluster Only (Recommended)

Use a root CA that signs only the node certificates of this cluster. Give each node one certificate with the extended key usages `serverAuth` and `clientAuth`. Configure a revocation list from the start: `raft_ssl_crl` is read-only, so adding it later needs a restart of each node. For the procedure, see [A CA for One Raft Cluster](raft-cluster-ca.md).

Add to the configuration file of each node, with the certificate and key of that node:

```ini
[mariadb]
raft_tls_mode = VERIFY_CA
raft_ssl_ca   = /etc/mysql/raft/ca.crt
raft_ssl_crl  = /etc/mysql/raft/ca.crl
raft_ssl_cert = /etc/mysql/raft/node1.crt
raft_ssl_key  = /etc/mysql/raft/node1.key
```

### Option B: No TLS, Isolated Network Only

{% hint style="danger" %}
Under `DISABLED`, the cluster connections are plaintext and no peer is authenticated. Use this setup only on a network that only the cluster nodes can reach.
{% endhint %}

Put the cluster connections on the isolated network, and bind the Raft listeners to it with [raft\_bind\_address](raft-system-variables.md#raft-bind-address). In this example, `192.0.2.11` is the client network address of the node, and `10.10.0.0/24` is the isolated cluster network. In the configuration file of the next step, use these values in place of the matching lines:

```ini
[mariadb]
bind_address          = 192.0.2.11
wsrep_cluster_address = "10.10.0.11,10.10.0.12,10.10.0.13"
wsrep_node_address    = 10.10.0.11
raft_bind_address     = 10.10.0.11
raft_tls_mode         = DISABLED
```

Accept the Raft ports only from the cluster network. Use these rules in place of the Raft rules in [Firewall Configuration](#firewall-configuration-on-each-node):

```bash
sudo ufw allow from 10.10.0.0/24 to any port 50001,50002 proto tcp
sudo ufw deny 50001/tcp
sudo ufw deny 50002/tcp
```

### ENCRYPT Mode

`ENCRYPT` encrypts the cluster connections, but does not authenticate the peer. It does not stop a man-in-the-middle attack. Use it only as a fallback. If you set no certificate and key, the node generates a self-signed certificate at startup. Only `ENCRYPT` can use it.

### Change from ENCRYPT to VERIFY\_CA

You can change a cluster from `ENCRYPT` to `VERIFY_CA` with rolling restarts, with no outage. A node under `ENCRYPT` presents its configured certificate, so a peer under `VERIFY_CA` accepts it if the cluster CA signed it.

1. On each node, install the CA and a node certificate that the CA signed. Set `raft_ssl_ca`, `raft_ssl_cert` and `raft_ssl_key`, and keep `raft_tls_mode=ENCRYPT`. Restart one node at a time.
2. On each node, set `raft_tls_mode=VERIFY_CA`. Restart one node at a time. Wait until each node has joined the cluster again before you restart the next node.
3. On each node, make sure that this query returns `verify_ca` and `OK` for each row:

   ```sql
   SELECT tls_mode, certificate_verification
   FROM INFORMATION_SCHEMA.WSREP_CONNECTIONS
   WHERE connection_scheme = 'ssl';
   ```

   This query shows only the connections that the local plugin opens. See [Monitoring Cluster Connections](#monitoring-cluster-connections).

## Configure Raft Cluster (mariadb-raft.cnf on Each Node)

If MariaDB is already running, stop it before proceeding with configuration

```bash
sudo systemctl stop mariadb
```

Create a configuration file (e.g., `/etc/mysql/mariadb.conf.d/mariadb-raft.cnf`) on each node. The configuration details will specify the cluster's identity and its peers.

Example `mariadb-raft.cnf` content (adjust IPs and names for each node):

```ini
[mariadb]
# Standard MariaDB settings
default_storage_engine=InnoDB
innodb_autoinc_lock_mode=2
bind_address=0.0.0.0

# MariaDB wsrep Configuration
# Binlog format must be ROW for wsrep
binlog_format=ROW
wsrep_provider=raft
wsrep_on=ON
wsrep_cluster_name="my_raft_cluster"

# MariaDB RAFT Configuration
plugin_load_add=raft
raft_node_id=node1
raft_log_level=INFO
raft_flow_control_drift_limit=1000
raft_flow_control_max_throttle_rate=1000

# TLS settings: option A from "Choose a TLS Setup"
raft_tls_mode=VERIFY_CA
raft_ssl_ca=/etc/mysql/raft/ca.crt
raft_ssl_crl=/etc/mysql/raft/ca.crl
raft_ssl_cert=/etc/mysql/raft/node1.crt
raft_ssl_key=/etc/mysql/raft/node1.key

# List of all nodes in the cluster (IP:Port)
wsrep_cluster_address="192.168.1.10,192.168.1.11,192.168.1.12"

```

For option B, replace the TLS settings and the address settings with the settings from [Option B](#option-b-no-tls-isolated-network-only).

{% hint style="info" %}
**Important:**

* raft\_node\_id: Must be a unique identifier for each node (e.g., "node1", "node2", "node3"). Only alphanumeric characters are allowed. The maximum length is 15.
* wsrep\_cluster\_address: Must list all nodes in the cluster on every node's configuration file.
{% endhint %}

## Start the Cluster

### Bootstrapping the First Node:

Start MariaDB Enterprise Server on the first node with a special option to bootstrap the cluster. This node will form the cluster, become the initial leader, and other nodes will join it.

```bash
sudo systemctl stop mariadb
# Start the first node of the cluster.
sudo mariadb-new-cluster
```

### Starting Subsequent Nodes:

For all remaining nodes (Node 2, Node 3, etc.), start the service normally. They will automatically discover and join the existing cluster using the cluster nodes listed in their `wsrep_cluster_address` configuration.

```bash
sudo systemctl start mariadb
```

## Verify Cluster Operation

After all nodes are started, verify that they have joined the cluster and consensus is operational.

### Check Cluster Status (on any node):

Connect to MariaDB Enterprise Server on any node and check the Raft status variables.

```bash
sudo mariadb -u root -p
```

Inside the MariaDB shell:

```sql
-- Check for the current Leader (the output will show the node_id of the Leader)
SHOW STATUS LIKE 'raft_current_leader_node_id';

-- Check the total number of nodes that have formed the cluster
SHOW STATUS LIKE 'wsrep_cluster_size';
-- The Value should match the number of nodes (e.g., 3).
```

### Test Replication (on the Leader):

Connect to the leader node and create a new database and table.

```sql
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE messages (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(255));
INSERT INTO messages (text) VALUES ('Hello from the Leader!');
```

### Verify Consistency (on a Follower):

Connect to any follower node, and confirm the data has been replicated and is visible.

```sql
SHOW DATABASES;
-- test_db should appear
USE test_db;
SELECT * FROM messages;
-- 'Hello from the Leader!' should appear
```

This confirms the strong synchronous replication and consistency provided by the MariaDB Raft Cluster.

## Leadership Priority

Leadership priority lets you influence which node the cluster elects as leader. Each node has a [raft-leadership-priority](raft-system-variables.md#raft-leadership-priority) value, which defaults to `0`. Nodes with a higher priority are preferred at election time.

A leader that detects a follower with a higher priority steps down immediately, rather than waiting for the heartbeat timeout to expire. Failover to the preferred node therefore happens as soon as that node is visible to the leader.

### Changing the Priority at Runtime

The priority can be changed while the cluster is running, using the `ChangeLeaderPriority` administrative command issued through `AdminCommandCall`. The new priority is broadcast to the cluster in the node's `ServerInfo`, so the change takes effect without restarting the session.

{% hint style="warning" %}
Leadership priority changes the cluster protocol, and is **not** backwards compatible with the 0.9.0 technical preview release. Upgrade all nodes to the same release.
{% endhint %}

## XA Transactions

`XA COMMIT` and `XA ROLLBACK` are fully supported. Standard Galera Cluster XA syntax and semantics apply — there are no Raft-specific differences in behavior.

## Non-Blocking Operations (NBO)

Non-Blocking Operations is an online schema upgrade method that replicates DDL to all nodes in total order, while only locking the specific table being altered. It is configured for Raft Cluster exactly as it is for Galera Cluster, through the `wsrep_OSU_method` session variable:

```sql
SET SESSION wsrep_OSU_method = 'NBO';
```

{% hint style="info" %}
Non-Blocking Operations is exclusive to MariaDB Enterprise Server.
{% endhint %}

For the full procedure, including the advantages and limitations of each schema upgrade method, see [Performing Schema Upgrades in Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster#non-blocking-operations-nbo).

## Monitoring Cluster Connections

The `INFORMATION_SCHEMA.WSREP_CONNECTIONS` table shows one row for each connection that the local plugin opens, and the TLS in force on a TLS connection. Galera uses the same table, and fills only the first eight columns.

| Column                     | Description                                                                                                                       |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `connection_id`            | Connection identifier.                                                                                                            |
| `connection_scheme`        | `tcp`, `unix` or `ssl`.                                                                                                           |
| `local_address`            | Local endpoint.                                                                                                                   |
| `remote_address`           | Remote endpoint.                                                                                                                  |
| `cipher`                   | Negotiated cipher suite.                                                                                                          |
| `certificate_subject`      | Subject of the peer certificate. Cut at 256 characters.                                                                           |
| `certificate_issuer`       | Issuer of the peer certificate. Cut at 256 characters.                                                                            |
| `certificate_version`      | Negotiated TLS protocol version, for example `TLSv1.3`.                                                                           |
| `tls_mode`                 | Mode in force on the connection: `disabled`, `encrypt` or `verify_ca`. The node reads it from the connection, not from `raft_tls_mode`. Raft only. |
| `certificate_verification` | `OK`, or the X509 error that rejected the peer. Empty under `encrypt`, which does not verify the peer. Raft only.                 |
| `certificate_not_before`   | Start of the validity period of the peer certificate. Raft only.                                                                  |
| `certificate_not_after`    | End of the validity period of the peer certificate. Raft only.                                                                    |

```sql
SELECT remote_address, tls_mode, certificate_verification,
       certificate_subject, certificate_not_after
FROM INFORMATION_SCHEMA.WSREP_CONNECTIONS
WHERE connection_scheme = 'ssl';
```

Each node also has two `unix` connections to its local Raft server process. They do not use TLS, so the columns from `cipher` on are empty.

{% hint style="info" %}
`WSREP_CONNECTIONS` does not show the connections between the Raft server processes of the nodes. These connections carry the replication traffic. [RAFT\_CLUSTER\_CONNECTIONS](#raft_cluster_connections) lists them, but has no TLS columns. For TLS errors on these connections, see the error log.
{% endhint %}

The TLS settings that apply to the cluster connections are described in [Raft System Variables: TLS](#raft-system-variables-tls).

## TLS Configuration Checks

The node checks the TLS configuration at startup. If a check fails, the node does not start, and the error log names the option and the path.

Under each mode, a path option can hold only the characters `A-Z`, `a-z`, `0-9`, `-`, `_`, `.` and `/`. `raft_ssl_cipher` and `raft_ssl_ciphersuites` can also hold `:`, `+`, `!`, `@`, `=` and `,`.

Under `ENCRYPT` and `VERIFY_CA`, the node also checks that:

* Each configured certificate and key file can be read and holds a certificate or a key. Each key goes with its certificate.
* The CA and revocation material can be loaded.
* `raft_tls_version`, `raft_ssl_cipher` and `raft_ssl_ciphersuites` select something that the TLS library supports.
* The key files are protected. The node does not start if all accounts can write a key file. It logs a warning if the group or other accounts have any access to it. A key must not have a passphrase.

Under `VERIFY_CA`, the node also validates its own certificates as a peer does: the `raft_ssl_cert` certificate for the connections it accepts, and the `raft_ssl_client_cert` certificate (or `raft_ssl_cert`) for the connections it initiates. The check finds, for example:

* A certificate that has expired, or that is not valid yet. Also check the system clock.
* A certificate that the configured CA does not sign. This includes a `raft_ssl_capath` directory without hashed names.
* A CA without a current revocation list, when revocation lists are configured.
* A revoked certificate.
* An extended key usage without `serverAuth` for accepted connections, or without `clientAuth` for initiated connections.

The Raft server process and the state transfer client do the certificate, key, CA and revocation checks too. The same checks run at `FLUSH SSL`.

## Reloading TLS Material

The node reads the certificate, key, CA and revocation files when it builds a TLS context. `FLUSH SSL` reads them again and puts them in force:

```sql
FLUSH SSL;
```

* The statement reloads the material of the plugin and of the Raft server process.
* It applies to the connections that start after it. Established connections keep their material. Thus a revocation or a new certificate takes effect when the cluster connections are made again.
* It applies only on the node where it runs. Run it on each node whose files changed.
* The paths, `raft_tls_mode`, and the version and cipher settings do not change. They are read-only and need a restart.
* If the new material fails the [TLS configuration checks](#tls-configuration-checks), the statement fails with `Failed to refresh WSREP SSL`. The node keeps the material that is in force, and the error log gives the reason.
* On a node that is not ready, for example a node without quorum, the statement fails with `WSREP has not yet prepared node for application use`. Set `wsrep_dirty_reads=ON` in the session to run it there.
* Under `DISABLED`, the statement does nothing for the cluster connections and does not fail.

## State Transfer and SQL Connections

The `raft_tls_mode` and `raft_ssl_*` options protect the cluster connections. Other connections have their own configuration:

* **State transfer request.** The joiner requests a state transfer through `mariadb-raft-sst`. It uses `raft_tls_mode` and the `raft_ssl_*` options, including the client certificate.
* **State transfer data.** The `rsync` and `mariabackup` methods send the data through the `wsrep_sst_<method>` script. The `raft_ssl_*` options do not apply to it. Configure its encryption in the `[sst]` section, as for Galera. See [Securing Communications in Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-security/securing-communications-in-galera-cluster).
* **SQL connections.** `ssl_ca`, `ssl_cert` and `ssl_key` apply to SQL clients. They are separate from the `raft_ssl_*` options.

## Raft Event Log Encryption

When [encrypt\_binlog](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#encrypt_binlog) is `ON`, the Raft server encrypts the new Raft event log files. It uses the keys of the configured encryption plugin, as for the binary log. When `encrypt_binlog` is `OFF`, new log files are not encrypted.

The plugin checks for a rotated master key at the interval that [raft\_key\_rotation\_check\_interval](raft-system-variables.md#raft-key-rotation-check-interval) sets, and gives the new key to the Raft server. You do not need to restart the node after a key rotation.

## Limitations

* **Allowlist.** The allowlist applies only to the connections that the plugin accepts, that is, to incoming SST requests. The Raft server does not apply the allowlist.
* **Performance Schema.** The `galera_group_members` table is not supported.

## Configuration Options

### Raft System Variables

| Raft System Variable                                                                                | Default | Description                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [raft-vote-timeout](raft-system-variables.md#raft-vote-timeout)                                     | 200     | Time candidate waits for a majority of granted votes during election. Uses exponential backoff up to raft\_max\_vote\_timeout.                                                                                          |
| [raft-data-dir](raft-system-variables.md#raft-data-dir)                                             | ./      | Data directory where to store replication logs and other node persistent state.                                                                                                                                            |
| [raft-event-store-file-size](raft-system-variables.md#raft-event-store-file-size)                   | 128MB   | Maximum size of single log file in bytes. When a log file reaches this size, a new file is created.                                                                                                                        |
| [raft-event-store-max-memory](raft-system-variables.md#raft-event-store-max-memory)                 | 32MB    | Maximum size of the in-memory event store buffer in bytes. Events are cached in memory for faster access before being written to disk.                                                                                     |
| [raft-event-store-max-size](raft-system-variables.md#raft-event-store-max-size)                     | 512MB   | Maximum total size of the event store on disk in bytes. Older log files are purged when this limit is exceeded.                                                                                                            |
| [raft-flow-control-drift-limit](raft-system-variables.md#raft-flow-control-drift-limit)             | 100     | Maximum index drift allowed between nodes before flow control throttling activates. When the difference between the slowest and fastest node commit positions exceeds this limit, the leader begins throttling requests.   |
| [raft-flow-control-max-throttle-rate](raft-system-variables.md#raft-flow-control-max-throttle-rate) | 100     | Maximum request rate (requests per second) to sustain when flow control throttling is active. Lower values provide more aggressive throttling.                                                                             |
| [raft-election-timeout](raft-system-variables.md#raft-election-timeout)                             | 5000    | Time follower waits without leader messages before starting election. Should be significantly larger than raft\_heartbeat\_timeout to avoid unnecessary elections.                                                       |
| [raft-heartbeat-timeout](raft-system-variables.md#raft-heartbeat-timeout)                           | 1000    | Interval at which leader sends heartbeat messages (milliseconds)                                                                                                                                                           |
| [raft-leadership-priority](raft-system-variables.md#raft-leadership-priority)                       | 0       | Priority for the current node to become leader. Nodes with a higher priority are preferred at election time, and can be changed at runtime.                                                                                |
| [raft-listen-port](raft-system-variables.md#raft-listen-port)                                       | 50002   | Port to listen for incoming cluster connections                                                                                                                                                                            |
| [raft-log-filter](raft-system-variables.md#raft-log-filter)                                         |         | In order to reduce amount of logging on DEBUG level, this filter can be used to select output from specific operations.                                                                                                    |
| [raft-log-level](raft-system-variables.md#raft-log-level)                                           | INFO    | Verbosity level for logging. Supported values are ERROR, WARN, INFO and DEBUG.                                                                                                                                             |
| [raft-max-vote-timeout](raft-system-variables.md#raft-max-vote-timeout)                             | 1500    | Upper bound for raft\_vote\_timeout after exponential backoff. Limits how long a candidate will wait between election attempts.                                                                                          |
| [raft-max-reconnect-attempts](raft-system-variables.md#raft-max-reconnect-attempts)                 | 5       | Number of attempts to reconnect to the cluster after ending up in non-primary state                                                                                                                                        |
| [raft-node-id](raft-system-variables.md#raft-node-id)                                               | auto    | Unique node identifier. The identifier can be either a human-readable string up to 15 characters long or a UUID. The special value 'auto' is reserved for generating a UUID whenever the server starts from a clean state. |
| [raft-liveness-timeout](raft-system-variables.md#raft-liveness-timeout)                             | 20000   | Timeout after which the node is considered unresponsive. If no replication events appear in the log within this period, the node moves to non-primary state.                                                               |
| [raft-eviction-timeout](raft-system-variables.md#raft-eviction-timeout)                             | 15000   | Timeout after which session to replication system is considered expired if there is no activity. If the node cannot communicate with the leader within this time period, it will be evicted from the cluster.              |
| [raft-sst-listen-port](raft-system-variables.md#raft-sst-listen-port)                               | 50001   | Port to listen for SST requests.                                                                                                                                                                                           |
| [raft-applied-event-memory-limit](raft-system-variables.md#raft-applied-event-memory-limit)         | 128MB   | Maximum size of received but not-yet-applied write set payloads before event delivery pauses. `0` disables the limit.                                                                                                      |
| [raft-bind-address](raft-system-variables.md#raft-bind-address)                                     |         | Local address for the Raft cluster connections and the SST listener. When empty, the node listens on all interfaces.                                                                                                       |
| [raft-key-rotation-check-interval](raft-system-variables.md#raft-key-rotation-check-interval)       | 60      | Interval, in seconds, at which the plugin checks for a rotated binary log master key. Effective only when `encrypt_binlog` is `ON`.                                                                                        |
| [raft-log-durability](raft-system-variables.md#raft-log-durability)                                 | FLUSH   | Durability level of Raft log writes: FLUSH or SYNC.                                                                                                                                                                        |
| [raft-node-weight](raft-system-variables.md#raft-node-weight)                                       | 1       | Node weight for replication and voting quorum. Unequal weights are unsafe in production.                                                                                                                                   |
| [raft-segment-id](raft-system-variables.md#raft-segment-id)                                         |         | Datacenter segment identifier. When unset, no segmentation is applied.                                                                                                                                                     |

#### Raft System Variables: TLS

[raft-tls-mode](raft-system-variables.md#raft-tls-mode) sets the protection of the Raft cluster connections: `DISABLED` (plaintext), `ENCRYPT` (TLS, the peer is not authenticated) or `VERIFY_CA` (TLS, the peer certificate is validated against the CA). The default is `VERIFY_CA`. The same mode applies to the connections of the plugin, of the Raft server process, and of the state transfer client. The node does not check a host name or a subject. See [Choose a TLS Setup](#choose-a-tls-setup-on-each-node).

| Raft System Variable                                                    | Default         | Description                                                                                                                                                                                                   |
| ----------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [raft-tls-mode](raft-system-variables.md#raft-tls-mode)                 | VERIFY\_CA      | Protection of the Raft cluster connections: DISABLED, ENCRYPT or VERIFY\_CA. Under VERIFY\_CA, a node without a CA and its own certificate and key does not start. Read-only.                                   |
| [raft-ssl-key](raft-system-variables.md#raft-ssl-key)                   |                 | Path to the SSL private key file in PEM format. This variable is read-only and must be set at server startup.                                                                                                 |
| [raft-ssl-cert](raft-system-variables.md#raft-ssl-cert)                 |                 | Path to the SSL certificate file in PEM format. This variable is read-only and must be set at server startup.                                                                                                 |
| [raft-ssl-client-cert](raft-system-variables.md#raft-ssl-client-cert)   |                 | Path to the certificate file in PEM format that the node presents on the connections it initiates. When unset, `raft_ssl_cert` is used. Read-only.                                                             |
| [raft-ssl-client-key](raft-system-variables.md#raft-ssl-client-key)     |                 | Path to the private key file in PEM format for `raft_ssl_client_cert`. Read-only.                                                                                                                             |
| [raft-ssl-ca](raft-system-variables.md#raft-ssl-ca)                     |                 | Path to the CA certificate file in PEM format used to verify peer certificates. This variable is read-only and must be set at server startup.                                                                 |
| [raft-ssl-capath](raft-system-variables.md#raft-ssl-capath)             |                 | Path to a directory containing CA certificate files in PEM format. This variable is read-only and must be set at server startup.                                                                              |
| [raft-ssl-cipher](raft-system-variables.md#raft-ssl-cipher)             |                 | OpenSSL cipher list for TLS 1.2 and below. Uses OpenSSL cipher string format. This variable is read-only and must be set at server startup.                                                                   |
| [raft-ssl-ciphersuites](raft-system-variables.md#raft-ssl-ciphersuites) |                 | List of permitted TLS 1.3 ciphersuites. This is separate from `raft_ssl_cipher` which applies to earlier TLS versions. This variable is read-only and must be set at server startup.                          |
| [raft-ssl-crl](raft-system-variables.md#raft-ssl-crl)                   |                 | Path to the Certificate Revocation List (CRL) file. This variable is read-only and must be set at server startup.                                                                                             |
| [raft-ssl-crlpath](raft-system-variables.md#raft-ssl-crlpath)           |                 | Path to a directory containing Certificate Revocation List files. This variable is read-only and must be set at server startup.                                                                               |
| [raft-ssl-verbose](raft-system-variables.md#raft-ssl-verbose)           | 0               | Verbose logging level for SSL context initialization, 0 to 2. This variable is read-only and must be set at server startup.                                                                                   |
| [raft-ssl-verify-depth](raft-system-variables.md#raft-ssl-verify-depth) | 9               | Maximum depth for certificate chain verification. This variable is read-only and must be set at server startup.                                                                                               |
| [raft-tls-version](raft-system-variables.md#raft-tls-version)           | TLSv1.2,TLSv1.3 | Comma-separated list of allowed TLS protocol versions: TLSv1.2 and TLSv1.3. This variable is read-only and must be set at server startup.                                                                     |

{% hint style="info" %}
The variables `raft_have_ssl` and `raft_ssl_verify_server_cert` were removed in Raft Cluster 1.0.0. Use `raft_tls_mode`.
{% endhint %}

### Raft Status Variables

| Raft Status Variable                     | Description                                                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `raft_current_log_index`                 | Index of the last processed replication event from the replication log.                                                         |
| `raft_current_leader_node_id`            | The node ID corresponding to current leader as reported by local Leader Tracker.                                                |
| `raft_current_leader_term`               | The current Raft term number. It is updated when the local node learns of a term change through a leader election or a heartbeat. |
| `raft_node_id`                           | The node identifier currently used by the local server.                                                                         |
| `raft_segment_id`                        | The segment ID currently used by the local server, as set by the `raft_segment_id` system variable.                             |
| `raft_server_version`                    | Version of the running Raft server process, `mariadb-raft-server`. `unknown` when the process is not running.                   |
| `raft_server_revision`                   | Build revision of the running Raft server process. `unknown` when the process is not running.                                   |
| `raft_applied_event_bytes`               | Current payload bytes of remote write sets handed to the server that are not reported committed yet.                            |
| `raft_applied_event_bytes_max`           | High water mark of `raft_applied_event_bytes` since server start.                                                               |
| `raft_applied_event_count`               | Number of write sets counted in `raft_applied_event_bytes`.                                                                     |
| `raft_applied_event_memory_paused`       | Non-zero while event delivery is paused because `raft_applied_event_bytes` exceeded `raft_applied_event_memory_limit`.          |
| `raft_applied_event_memory_pauses`       | Number of times event delivery was paused on `raft_applied_event_memory_limit`.                                                 |
| `raft_event_batch_mean`                  | Mean number of events in one replication batch, over a rolling sample window.                                                   |
| `raft_event_batch_max`                   | Maximum number of events in one replication batch, over a rolling sample window.                                                |
| `raft_flow_control_active`               | Boolean denoting whether the flow control is currently active. The value is updated only on Leader.                             |
| `raft_flow_control_requested`            | Number of times the flow control has been requested. The value is updated only on Leader.                                       |
| `raft_flow_control_queue_length`         | Number of requests currently queued in flow control. The value is updated only on Leader.                                       |
| `raft_flow_control_last_committed_drift` | The drift between minimum and maximum of last committed log indices reported by the nodes. The value is updated only on Leader. |
| `raft_event_store_disk_total_bytes`      | Total size in bytes of the event store on disk.                                                                                 |
| `raft_event_store_disk_bytes_read`       | Cumulative number of bytes read from the event store disk files since the Raft server process started.                          |
| `raft_event_store_disk_bytes_written`    | Cumulative number of bytes written to the event store disk files since the Raft server process started.                         |
| `raft_event_store_memory_bytes`          | Current amount of memory (in bytes) used by the in-memory portion of the event store.                                           |
| `raft_event_store_first_index`           | Log index of the oldest entry that is still retained in the event store.                                                        |
| `raft_event_store_last_index`            | Log index of the most recent entry persisted in the event store.                                                                |

### Raft Information Schema Tables

| Raft Information Schema Table | Description                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------ |
| `RAFT_CERT_FAILURES`          | Displays meta data from limited set of write set certification failures.       |
| `RAFT_CLUSTER_CONNECTIONS`    | Displays connections between cluster nodes and processes.                      |
| `RAFT_TIMERS`                 | Displays active timers on the node.                                            |
| `RAFT_RPC_SENT`               | Displays counts of sent RPC messages by type.                                  |
| `RAFT_STATUS`                 | Displays the Raft server and plugin status as JSON documents.                  |
| `RAFT_LATENCY_STATS`          | Displays latency percentiles for internal operations on the write-commit path. |
| `RAFT_SERVER_INSTANCES`       | Displays all servers in the cluster, active and inactive.                      |
| `RAFT_FOLLOWER_INFO`          | Displays replication progress and response latency of each active follower.    |

#### RAFT\_CERT\_FAILURES

| Column             | Type     | Description                                         |
| ------------------ | -------- | --------------------------------------------------- |
| `VICTIM_NODE_ID`   | VARCHAR  | Node of the write set that failed certification     |
| `VICTIM_LOG_INDEX` | BIGINT   | Log index of the write set that failed certification |
| `VICTIM_KEY_PATH`  | LONGTEXT | Conflicting key path of the write set that failed certification |
| `GRANTED_KEY_PATH` | LONGTEXT | Conflicting key path of the write set that was granted |
| `ANNOTATION`       | LONGTEXT | Optional annotation                                 |

#### RAFT\_CLUSTER\_CONNECTIONS

| Column             | Type     | Description                                                                                 |
| ------------------ | -------- | ------------------------------------------------------------------------------------------- |
| `ID`               | BIGINT   | Connection identifier                                                                       |
| `LOCAL_ENDPOINT`   | LONGTEXT | Local endpoint                                                                              |
| `REMOTE_ENDPOINT`  | LONGTEXT | Remote endpoint                                                                             |
| `SEND_BUFFER_SIZE` | BIGINT   | Size of the send buffer                                                                     |
| `SCOPE`            | VARCHAR  | `server` for a connection of the Raft server process, `plugin` for a connection of the plugin |

The table also lists the local connections between the plugin and its Raft server process. It has no TLS columns. For the TLS of the plugin connections, see [Monitoring Cluster Connections](#monitoring-cluster-connections).

#### RAFT\_TIMERS

| Column                | Type     | Description                                 |
| --------------------- | -------- | ------------------------------------------- |
| `NAME`                | LONGTEXT | Timer name                                  |
| `EXPIRES_FROM_NOW_US` | BIGINT   | Time until the timer expires, in microseconds |

#### RAFT\_RPC\_SENT

| Column              | Type            | Description                        |
| ------------------- | --------------- | ---------------------------------- |
| `MESSAGE_TYPE`      | LONGTEXT        | RPC message type                   |
| `MESSAGE_COUNT`     | BIGINT UNSIGNED | Number of messages sent            |
| `BYTES_TRANSFERRED` | BIGINT UNSIGNED | Number of bytes sent               |

#### RAFT\_SERVER\_INSTANCES

| Column                | Type    | Description                         |
| --------------------- | ------- | ----------------------------------- |
| `ID`                  | VARCHAR | Server identifier                   |
| `ADDRESS`             | VARCHAR | Network address of the server       |
| `LEADERSHIP_PRIORITY` | BIGINT  | Priority for becoming leader        |

#### RAFT\_FOLLOWER\_INFO

A follower is active if its next index is not zero.

| Column                     | Type            | Description                                                 |
| -------------------------- | --------------- | ----------------------------------------------------------- |
| `ID`                       | VARCHAR         | Server identifier                                           |
| `NEXT_INDEX`               | BIGINT          | Next log index to send to this follower                     |
| `MATCH_INDEX`              | BIGINT          | Highest log index known to be replicated on this follower   |
| `MIN_LOG_INDEX`            | BIGINT          | Minimum log index retained by this follower                 |
| `RESPONSE_LATENCY_COUNT`   | BIGINT UNSIGNED | Number of response latency samples                          |
| `RESPONSE_LATENCY_P50_US`  | BIGINT UNSIGNED | 50th-percentile response latency, in microseconds           |
| `RESPONSE_LATENCY_P99_US`  | BIGINT UNSIGNED | 99th-percentile response latency, in microseconds           |
| `RESPONSE_LATENCY_P999_US` | BIGINT UNSIGNED | 99.9th-percentile response latency, in microseconds         |
| `RESPONSE_LATENCY_MAX_US`  | BIGINT UNSIGNED | Maximum response latency, in microseconds                   |

#### RAFT_STATUS

The `INFORMATION_SCHEMA.RAFT_STATUS` table exposes the Raft server's internal status as two JSON documents — one from the server process, one from the plugin — for diagnostics and monitoring tools that need structured detail beyond the dedicated `RAFT_*` status variables and tables.

| Column               | Type     | Description                                                                                                                                                                             |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SERVER_STATUS_JSON` | LONGTEXT | JSON document describing the Raft server process's current status, including active network connections (peer endpoints and the local Unix socket used for plugin↔server communication) |
| `PLUGIN_STATUS_JSON` | LONGTEXT | JSON document describing the plugin's status                                                                                                                                            |

The table always has exactly one row.

```sql
SELECT JSON_PRETTY(SERVER_STATUS_JSON) FROM information_schema.RAFT_STATUS;
```

Example `SERVER_STATUS_JSON` content (abbreviated):

```
{"connections":[{"id":"0x...","local_endpoint":"127.0.0.1:51210","remote_endpoint":"127.0.0.1:46645"}, ...]}
```

#### RAFT_LATENCY_STATS

The `INFORMATION_SCHEMA.RAFT_LATENCY_STATS` table reports latency percentiles for internal operations on the write-commit path, one row per operation.

| Column    | Type            | Description                                |
| --------- | --------------- | ------------------------------------------ |
| `NAME`    | VARCHAR(64)     | The operation being measured               |
| `P50_US`  | BIGINT UNSIGNED | 50th-percentile latency, in microseconds   |
| `P99_US`  | BIGINT UNSIGNED | 99th-percentile latency, in microseconds   |
| `P999_US` | BIGINT UNSIGNED | 99.9th-percentile latency, in microseconds |
| `MAX_US`  | BIGINT UNSIGNED | Maximum observed latency, in microseconds  |

The table has one row for each of these operations: `local_write_set`, `apply`, `certification`, `log_write`, `log_flush`, `log_sync`, `flow_control_wait`, and `server_task`. The operation names reflect the internal implementation and can change.

```sql
SELECT * FROM information_schema.RAFT_LATENCY_STATS;
```

Example output (abbreviated):

```
NAME             P50_US  P99_US  P999_US  MAX_US
local_write_set       0       0        0       0
apply                 0       0        0       0
certification         52      52       52      52
log_write              7       7        7      17
log_flush             47      47       47      95
```

A row's values are all 0 until that operation has occurred at least once on the node.

### WSREP System Variables

MariaDB Raft Cluster configuration primarily relies on the [WSREP System Variables](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables). However, the `wsrep_provider_options` and `wsrep_ssl_mode` variables are an exception, as they are superseded by the Raft System Variables for configuring the cluster.

#### wsrep\_cluster\_name

Names the cluster, and safeguards against a node accidentally joining the wrong one. The value must match on every node in the cluster: if a joining node's `wsrep_cluster_name` does not match, all of its connections are declined.

| Property  | Value              |
| --------- | ------------------ |
| Scope     | Global             |
| Dynamic   | Yes                |
| Data Type | String             |
| Default   | `my_wsrep_cluster` |

{% hint style="info" %}
Exposed endpoints must contain the `wsrep_cluster_name` as the last path component, or as a query parameter.
{% endhint %}

### WSREP Status Variables

| WSREP Status Variable           | Description                                                                                                                                                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wsrep_applier_thread_count`    | Stores the current number of applier threads to make clear how many slave threads of this type there are.                                                                                                             |
| `wsrep_apply_waits`             | Number of times a prior transaction had to be waited before applying a write set.                                                                                                                                     |
| `wsrep_cert_deps_distance`      | Average distance between the highest and the lowest sequence numbers that can possibly be applied in parallel, or the potential degree of parallelization.                                                            |
| `wsrep_cert_interval`           | Average number of transactions received while a transaction replicates.                                                                                                                                               |
| `wsrep_checkpoint_position`     | The replication checkpoint position recorded by the node.                                                                                                                                                             |
| `wsrep_cluster_capabilities`    |                                                                                                                                                                                                                       |
| `wsrep_cluster_conf_id`         | Total number of cluster membership changes that have taken place.                                                                                                                                                     |
| `wsrep_cluster_size`            | Number of nodes currently in the cluster.                                                                                                                                                                             |
| `wsrep_cluster_state_uuid`      | UUID state of the cluster. If it matches the value in wsrep\_local\_state\_uuid, the local and cluster nodes are in sync.                                                                                             |
| `wsrep_cluster_status`          | Cluster component status. Possible values are PRIMARY (primary group configuration, quorum present), NON\_PRIMARY (non-primary group configuration, quorum lost), or DISCONNECTED (not connected to group, retrying). |
| `wsrep_connected`               | Whether or not MariaDB is connected to the wsrep provider. Possible values are ON or OFF.                                                                                                                             |
| `wsrep_desync_count`            | Returns the number of operations in progress that require the node to temporarily desync from the cluster.                                                                                                            |
| `wsrep_incoming_addresses`      | Comma-separated list of incoming server addresses in the cluster component.                                                                                                                                           |
| `wsrep_last_committed`          | Sequence number of the most recently committed transaction.                                                                                                                                                           |
| `wsrep_local_bf_aborts`         | Total number of high-priority local transactions aborts caused by replication applier threads.                                                                                                                        |
| `wsrep_local_cert_failures`     | Total number of local transactions that failed the certification test and consequently issued a voluntary rollback.                                                                                                   |
| `wsrep_local_index`             | The node's index in the cluster. The index is zero-based.                                                                                                                                                             |
| `wsrep_local_replays`           | Total number of transaction replays due to asymmetric lock granularity.                                                                                                                                               |
| `wsrep_local_state`             | Internal Galera Cluster FSM state number.                                                                                                                                                                             |
| `wsrep_local_state_comment`     | Human-readable explanation of the state.                                                                                                                                                                              |
| `wsrep_local_state_uuid`        | The node's UUID state. If it matches the value in wsrep\_cluster\_state\_uuid, the local and cluster nodes are in sync.                                                                                               |
| `wsrep_provider_capabilities`   |                                                                                                                                                                                                                       |
| `wsrep_provider_name`           | The name of the provider. The value is “raft" when Raft plugin is enabled.                                                                                                                                            |
| `wsrep_provider_vendor`         | The vendor string.                                                                                                                                                                                                    |
| `wsrep_provider_version`        | The version number of the Raft wsrep provider                                                                                                                                                                         |
| `wsrep_ready`                   | Whether or not the Galera wsrep provider is ready. Possible values are ON or OFF                                                                                                                                      |
| `wsrep_received`                | Total number of write sets received from other nodes.                                                                                                                                                                 |
| `wsrep_received_bytes`          | Total size in bytes of all write sets received from other nodes.                                                                                                                                                      |
| `wsrep_repl_data_bytes`         | Total size of data replicated.                                                                                                                                                                                        |
| `wsrep_repl_keys`               | Total number of keys replicated.                                                                                                                                                                                      |
| `wsrep_repl_keys_bytes`         | Total size of keys replicated.                                                                                                                                                                                        |
| `wsrep_replicated`              | Total size in bytes of all write sets replicated to other nodes.                                                                                                                                                      |
| `wsrep_rollbacker_thread_count` | Stores the current number of rollbacker threads to make clear how many slave threads of this type there are.                                                                                                          |
| `wsrep_se_checkpoint`           | The storage engine checkpoint recorded by the node, shown as the recovered XID.                                                                                                                                       |
| `wsrep_thread_count`            | Total number of wsrep (applier/rollbacker) threads.                                                                                                                                                                   |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
