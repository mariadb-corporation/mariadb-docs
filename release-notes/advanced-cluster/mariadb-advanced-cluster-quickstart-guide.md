# MariaDB Advanced Cluster Quickstart Guide

MariaDB Advanced Cluster (built on RAFT) provides a highly available, strongly consistent, and fault-tolerant solution for database deployment. It utilizes the **RAFT consensus protocol** to ensure that data is safely and synchronously replicated across all nodes, guaranteeing no lost transactions and providing a single, authoritative source of data through a **single active Leader** architecture.

## RAFT Protocol Overview

The RAFT Protocol is a consensus algorithm designed for managing replicated logs and ensuring data consistency across a distributed cluster. It simplifies the complexity of consensus by defining three key mechanisms: Leader Election, Log Replication, and Commit/Consensus via a Majority Quorum.

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

Before setting up your MariaDB Advanced Cluster, ensure the following prerequisites are met on all nodes:

* **Three or more Nodes**: A minimum of three nodes is required to establish a majority quorum (e.g., 2 out of 3, 3 out of 5) and tolerate single node failure
* **Linux Operating System**: A compatible Linux distribution (e.g., Ubuntu, RHEL)
* **Synchronized Clocks**: Use NTP (Network Time Protocol) to ensure all nodes' system clocks are synchronized
* **SSH Access**: Root or sudo access to all nodes for configuration and installation
* **Network Connectivity**: All nodes must be able to communicate with each other over specific ports with low latency

## Installation (on Each Node)

Install MariaDB Enterprise Server and the associated RAFT consensus provider on all nodes of your cluster.

{% stepper %}
{% step %}
### Download the Advanced Cluster Technical Preview tar archive

[https://mariadb.com/downloads/enterprise/advanced-cluster/](https://mariadb.com/downloads/enterprise/advanced-cluster/)

Download the correct version for your Linux Distribution
{% endstep %}

{% step %}
### Uninstall MariaDB Enterprise

If you already have MariaDB Enterprise Server Installed you will need to uninstall it prior to installing the MariaDB Advanced Cluster technical preview packages
{% endstep %}

{% step %}
### Install Advanced Cluster technical preview

{% tabs %}
{% tab title="RHEL 9 & 10" %}
```bash
tar -xvf mariadb-advanced-cluster*.tar
cd mariadb-advanced-cluster*/
sudo dnf install ./MariaDB-common* ./MariaDB-client* ./MariaDB-shared*
sudo dnf install ./MariaDB-server* ./galera-enterprise-4* ./mariadb-raft*
```

There are other packages included in the package tarball that you can optionally install, such as MariaDB-backup.
{% endtab %}

{% tab title="Debian & Ubuntu" %}
```bash
tar -xvf mariadb-advanced-cluster*.tar
cd mariadb-advanced-cluster*/
sudo apt install ./mariadb-common_* ./mariadb-client* ./libmysqlclient18_* ./libmariadb3* ./libmariadbclient18_*
sudo apt install ./mariadb-server* ./galera-enterprise-4_* ./mariadb-raft_*
```

There are other packages included in the package tarball that you can optionally install, such as mariadb-backup.
{% endtab %}
{% endtabs %}
{% endstep %}
{% endstepper %}

## Firewall Configuration (on Each Node)

Open the necessary ports on the firewall of each node to allow for both client connections and inter-node RAFT communication.

| Port  | Protocol | Purpose                             |
| ----- | --- | ----------------------------------- |
| 3306  | TCP | Client connections to the database. |
| 50001 | TCP | SST request listener                |
| 50002 | TCP | RAFT server internal communication  |

Example using UFW (Ubuntu/Debian):

```bash
# Allow client connections
sudo ufw allow 3306/tcp
# Allow RAFT cluster communication
sudo ufw allow 50001/tcp
sudo ufw allow 50002/tcp
sudo ufw reload
```

## Configure RAFT Cluster (mariadb-raft.cnf on Each Node)

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
plugin_maturity=gamma
plugin_load_add=raft
raft_node_id=node1
raft_log_level=INFO
raft_flow_control_drift_limit=1000
raft_flow_control_max_throttle_rate=1000

# List of all nodes in the cluster (IP:Port)
wsrep_cluster_address="192.168.1.10,192.168.1.11,192.168.1.12"

```

{% hint style="info" %}
#### Important:

* raft\_node\_id: Must be a unique identifier for each node (e.g., "node1", "node2", "node3"). Only alphanumeric characters are allowed. The maximum length is 15.
* wsrep\_cluster\_address: Must list all nodes in the cluster on every node's configuration file.
{% endhint %}

## Start the Cluster

### Bootstrapping the First Node:

Start MariaDB Enterprise Server on the first node with a special option to bootstrap the cluster. This node will form the cluster, become the initial leader, and other nodes will join it.&#x20;

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

Connect to MariaDB Enterprise Server on any node and check the RAFT status variables.

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

This confirms the strong synchronous replication and consistency provided by the MariaDB Advanced Cluster.

## Configuration Options

### RAFT System Variables

| RAFT System Variable                  | Default     | Description                                                                                                                                                                                                                 |
| ------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `raft-candidate-timeout`              | 200         | IInitial timeout for candidate waiting for votes during election (milliseconds). Uses exponential backoff up to raft\_max\_candidate\_timeout.                                                                              |
| `raft-data-dir`                       | ./          | Data directory where to store replication logs and other node persistent state.                                                                                                                                             |
| `raft-event-store-file-size`          | 128MB       | Maximum size of single log file in bytes. When a log file reaches this size, a new file is created.                                                                                                                         |
| `raft-event-store-max-memory`         | 32MB        | Maximum size of the in-memory event store buffer in bytes. Events are cached in memory for faster access before being written to disk.                                                                                      |
| `raft-event-store-max-size`           | 512MB       | Maximum total size of the event store on disk in bytes. Older log files are purged when this limit is exceeded.                                                                                                             |
| `raft-flow-control-drift-limit`       | 100         | Maximum index drift allowed between nodes before flow control throttling activates. When the difference between the slowest and fastest node commit positions exceeds this limit, the leader begins throttling requests.    |
| `raft-flow-control-max-throttle-rate` | 100         | Maximum request rate (requests per second) to sustain when flow control throttling is active. Lower values provide more aggressive throttling.                                                                              |
| `raft-follower-timeout`               | 5000        | Time follower waits without leader messages before starting election (milliseconds).                                                                                                                                        |
| `raft-heartbeat-timeout`              | 1000        | Interval at which leader sends heartbeat messages (milliseconds)                                                                                                                                                            |
| `raft-listen-port`                    | 50002       | Port to listen for incoming cluster connections                                                                                                                                                                             |
| `raft-log-filter`                     |   | In order to reduce amount of logging on DEBUG level, this filter can be used to select output from specific operations.                                                                                                     |
| `raft-log-level`                      | INFO        | Verbosity level for logging. Supported values are ERROR, WARN, INFO and DEBUG.                                                                                                                                              |
| `raft-max-candidate-timeout`          | 1500        | Maximum candidate timeout after exponential backoff (milliseconds).                                                                                                                                                         |
| `raft-max-reconnect-attempts`         | 5           | Number of attempts to reconnect to the cluster after ending up in non-primary state                                                                                                                                         |
| `raft-node-id`                        | auto        | Unique node identifier. The identifier can be either a human-readable string up to 15 characters long or a UUID.  The special value 'auto' is reserved for generating a UUID whenever the server starts from a clean state. |
| `raft-non-primary-timeout`            | 20          | Timeout after which the node is considered to be in non-primary state. If no replication events appear in the log within this time period, the node will be considered to be in non-primary state (seconds).                |
| `raft-session-timeout`                | 15          | Timeout after which session to replication system is considered expired if there is no activity. If the node cannot communicate with the leader within this time period, it will be evicted from the cluster (seconds).     |
| `raft-sst-listen-port`                | 50001       | Port to listen for SST requests.                                                                                                                                                                                            |

SSL is enabled by default for all Raft Cluster connections. If the certificate information is not provided, a self-signed certificate is created at startup. Notice that `VERIFY_PEER` cannot be used with self-signed certificates.

| RAFT System Variable  | Default         | Description                                                                                                                                                                                                   |
| --------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| raft-have-ssl         | YES             | Indicates whether SSL/TLS is enabled for cluster communication. Possible values are YES, NO, DISABLED, or VERIFY\_PEER. This is a read-only variable that reflects the current SSL state                      |
| raft-ssl-key          |       | Path to the SSL private key file in PEM format. This variable is read-only and must be set at server startup.                                                                                                 |
| raft-ssl-cert         |       | Path to the SSL certificate file in PEM format. This variable is read-only and must be set at server startup.                                                                                                 |
| raft-ssl-ca           |       | Path to the CA certificate file in PEM format used to verify peer certificates. This variable is read-only and must be set at server startup.                                                                 |
| raft-ssl-capath       |       | Path to a directory containing CA certificate files in PEM format. This variable is read-only and must be set at server startup.                                                                              |
| raft-ssl-cipher       |       | OpenSSL cipher list for TLS 1.2 and below. Uses OpenSSL cipher string format. This variable is read-only and must be set at server startup.                                                                   |
| raft-ssl-ciphersuites |       | List of permitted TLS 1.3 ciphersuites. This is separate from `raft_ssl_cipher` which applies to earlier TLS versions. This variable is read-only and must be set at server startup.          |
| raft-ssl-crl          |       | Path to the Certificate Revocation List (CRL) file. This variable is read-only and must be set at server startup.                                                                                             |
| raft-ssl-crlpath      |       | Path to a directory containing Certificate Revocation List files. This variable is read-only and must be set at server startup.                                                                               |
| raft-ssl-verify-depth | 9               | Maximum depth for certificate chain verification. This variable is read-only and must be set at server startup.                                                                                               |
| raft-tls-version      | TLSv1.2,TLSv1.3 | Comma-separated list of allowed TLS protocol versions. Supported values include TLSv1.2 and TLSv1.3. Default includes both TLSv1.2 and TLSv1.3. This variable is read-only and must be set at server startup. |

### RAFT Status Variables

| RAFT Status Variable                     | Description                                                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `raft_current_log_index`                 | Index of the last processed replication event from the replication log.                                                         |
| `raft_current_leader_node_id`            | The node ID corresponding to current leader as reported by local Leader Tracker.                                   |
| `raft_node_id`                           | The node identifier currently used by the local server.                                                                         |
| `raft_flow_control_active`               | Boolean denoting whether the flow control is currently active. The value is updated only on Leader.                |
| `raft_flow_control_requested`            | Number of times the flow control has been requested. The value is updated only on Leader.                          |
| `raft_flow_control_queue_length`         | Number of requests currently queued in flow control. The value is updated only on Leader.                          |
| `raft_flow_control_last_committed_drift` | The drift between minimum and maximum of last committed log indices reported by the nodes. The value is updated only on Leader. |
| `raft_event_store_disk_total_bytes`      | Total size in bytes of the event store on disk.                                                                                 |
| `raft_event_store_disk_bytes_written`    | Cumulative number of bytes written to the event store disk files since the Raft server process started.                         |
| `raft_event_store_memory_bytes`          | Current amount of memory (in bytes) used by the in-memory portion of the event store.                                           |
| `raft_event_store_first_index`           | Log index of the oldest entry that is still retained in the event store.                                           |
| `raft_event_store_last_index`            | Log index of the most recent entry persisted in the event store.                                                                |

### RAFT Information Schema Tables

| RAFT Information Schema Table   | Description                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `RAFT_CERT_FAILURES`       | Displays meta data from limited set of write set certification failures. |
| `RAFT_CLUSTER_CONNECTIONS` | Displays connections between cluster nodes and processes.                             |
| `RAFT_TIMERS`              | Displays active timers on the node.                                                   |
| `RAFT_RPC_SENT`            | Displays counts of sent RPC messages by type.                                         |

### WSREP System Variables

MariaDB Advanced Cluster configuration primarily relies on the [WSREP System Variables](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables). However, the `wsrep_provider_options` and `wsrep_ssl_mode` variables are an exception, as they are  superseded by the RAFT System Variables for configuring the cluster.

### WSREP Status Variables

| WSREP Status Variable           | Description                                                                                                                                                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wsrep_applier_thread_count`    | Stores the current number of applier threads to make clear how many slave threads of this type there are.                                                                                                             |
| `wsrep_apply_waits`             | Number of times a prior transaction had to be waited before applying a write set.                                                                                                                                     |
| `wsrep_cert_deps_distance`      | Average distance between the highest and the lowest sequence numbers that can possibly be applied in parallel, or the potential degree of parallelization.                                                            |
| `wsrep_cert_interval`           | Average number of transactions received while a transaction replicates.                                                                                                                                               |
| `wsrep_cluster_capabilities`    |                                                                                                                                                                                                             |
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
| `wsrep_provider_capabilities`   |                                                                                                                                                                                                             |
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
| `wsrep_thread_count`            | Total number of wsrep (applier/rollbacker) threads.                                                                                                                                                                   |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
