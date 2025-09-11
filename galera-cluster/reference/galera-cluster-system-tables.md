# Galera Cluster System Tables

Starting with Galera 4 (used in [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) and later), several system tables related to replication are available in the `mysql` database. These tables can be queried by administrators to get a real-time view of the cluster's layout, membership, and current operations.

You can view these tables with the following query:

```sql
SHOW TABLES FROM mysql LIKE 'wsrep%';
```

```
+---------------------------+
| Tables_in_mysql (wsrep%)  |
+---------------------------+
| wsrep_allowlist           |
| wsrep_cluster             |
| wsrep_cluster_members     |
| wsrep_streaming_log       |
+---------------------------+
```

{% hint style="warning" %}
`mysql` vs. `mariadb`

You'll see queries referencing the `mysql` database (e.g., `FROM mysql.wsrep_cluster`). This is intentional. MariaDB, a MySQL fork, retains the `mysql` name for its internal system schema to ensure historical and backward compatibility where it manages user permissions and system tables.

This is different from the command-line client, which should always be invoked as `mariadb`.
{% endhint %}

These tables are managed by the cluster itself and should not be modified by users, with the exception of `wsrep_allowlist`.

## `wsrep_allowlist`

This table stores a list of allowed IP addresses that can join the cluster and perform a state transfer (IST/SST). It is a security feature to prevent unauthorized nodes from joining.

```bash
MariaDB [mysql]> DESCRIBE wsrep_allowlist;
```

```
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| ip    | char(64) | NO   | PRI | NULL    |       |
+-------+----------+------+-----+---------+-------+
```

To add a new node to the allowlist, you can `INSERT` its IP address:

```sql
INSERT INTO mysql.wsrep_allowlist(ip) VALUES('18.193.102.155');
```

If a node attempts to join and its IP address is not in the allowlist, the join will fail. The DONOR nodes will log a warning similar to this:

```
[Warning] WSREP: Connection not allowed, IP 3.70.155.51 not found in allowlist.
```

The joining node will fail with a connection timeout error.

## `wsrep_cluster`

This table contains a single row with a high-level view of the cluster's identity, state, and capabilities.

| Attribute          | Description                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| `cluster_uuid`     | The unique identifier for the cluster.                                                                   |
| `view_id`          | Corresponds to the `wsrep_cluster_conf_id` status variable, representing the current membership view ID. |
| `view_seqno`       | The global transaction sequence number associated with this cluster view.                                |
| `protocol_version` | The wsrep protocol version in use.                                                                       |
| `capabilities`     | A bitmask of capabilities provided by the Galera library.                                                |

You can query its contents like this:

```sql
SELECT * FROM mysql.wsrep_cluster\G
```

```
*************************** 1. row ***************************
   cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
        view_id: 3
     view_seqno: 2956
protocol_version: 4
   capabilities: 184703
```

## `wsrep_cluster_members`

This table provides a real-time list of all the nodes that are currently members of the cluster component.

| Node                    | Description                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| `node_uuid`             | The unique identifier for each individual node.                              |
| `cluster_uuid`          | The UUID of the cluster this node belongs to.                                |
| `node_name`             | The human-readable name of the node, set by the `wsrep_node_name` parameter. |
| `node_incoming_address` | The IP address and port where the node is listening for client connections.  |

Querying this table gives you a quick overview of the current cluster membership:

```sql
SELECT * FROM mysql.wsrep_cluster_members ORDER BY node_name\G
```

```
*************************** 1. row ***************************
           node_uuid: e39d1774-7e2b-11e9-b5b2-7696f81d30fb
        cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
           node_name: galera1
node_incoming_address: AUTO
*************************** 2. row ***************************
           node_uuid: eb8fc512-7e2b-11e9-bb74-3281cf207f60
        cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
           node_name: galera2
node_incoming_address: AUTO
*************************** 3. row ***************************
           node_uuid: 2347a8ac-7e2c-11e9-b6f0-da90a2d0a563
        cluster_uuid: bd5fe1c3-7d80-11e9-8913-4f209d688a15
           node_name: galera3
node_incoming_address: AUTO
```

## `wsrep_streaming_log`

This table contains metadata for Streaming Replication transactions that are currently in progress. Each row represents a write-set fragment. The table is typically empty unless a large or long-running transaction with streaming enabled is active.

| Fragment    | Description                                                      |
| ----------- | ---------------------------------------------------------------- |
| `node_uuid` | The UUID of the node where the streaming transaction originated. |
| `trx_id`    | The transaction identifier.                                      |
| `seqno`     | The sequence number of the specific write-set fragment.          |
| `flags`     | Flags associated with the fragment.                              |
| `frag`      | The binary log events contained in the fragment.                 |

Example of querying the table during a streaming transaction:

```sql
-- Enable streaming for the session
SET SESSION wsrep_trx_fragment_unit='statements';
SET SESSION wsrep_trx_fragment_size=1;
```

```sql
-- Start a transaction
START TRANSACTION;
INSERT INTO my_table VALUES (100);
```

```sql
-- Query the log table in the same session
SELECT node_uuid, trx_id, seqno, flags
FROM mysql.wsrep_streaming_log;
```

```
+--------------------------------------+--------+-------+-------+
| node_uuid                            | trx_id | seqno | flags |
+--------------------------------------+--------+-------+-------+
| a006244a-7ed8-11e9-bf00-867215999c7c |     26 |     4 |     1 |
+--------------------------------------+--------+-------+-------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
