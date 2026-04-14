---
description: MariaDB Galera Cluster usage guide
---

# MariaDB Galera Cluster Usage Guide

This guide provides essential information for effectively using and interacting with a running MariaDB Galera Cluster. It covers connection methods, operational considerations, monitoring, and best practices for applications.

## Connecting to the Cluster

Since Galera Cluster is multi-primary, any node can accept read and write connections.

### a. Using a Load Balancer (Recommended for Production):

Deploying a load balancer or proxy (like MariaDB MaxScale, ProxySQL, or HAProxy) is the recommended approach.

#### **MariaDB MaxScale**

* Provides intelligent routing (e.g., `readwritesplit`, `router`), connection pooling, and advanced cluster awareness (e.g., `binlogrouter` for replication clients, `switchover` for failover).

#### **Other Load Balancers**

Configure them to distribute connections across your Galera nodes, typically using health checks on port 3306 or other cluster-specific checks.

### b. Direct Connection:

You can connect directly to any individual node's IP address or hostname using standard MariaDB client tools or connectors (e.g., mariadb command-line client, MariaDB Connector/J, Connector/Python).

#### **Example (Command-line):**

```bash
mariadb -h <node_ip_address> -u <username> -p
```

While simple, this method lacks automatic failover; your application would need to handle connection retries and failover logic.

## Basic Operations (Reads & Writes)

{% hint style="warning" %}
Users should be aware that Galera's optimistic concurrency control may result in Lost Updates (P4) or Stale Reads even in healthy clusters. Common application patterns like Read-Modify-Write may require explicit locking (e.g., `SELECT ... FOR UPDATE`) or session-level causality checks (e.g., `wsrep_sync_wait = 1`) to ensure safety.
{% endhint %}

### **Active-Active**

You can perform both read and write operations on _any_ node in the cluster. All successful write operations are synchronously replicated to all other nodes.

### **Transactions**

Standard SQL transactions (`START TRANSACTION`, `COMMIT`, `ROLLBACK`) work as expected. Galera handles the replication of committed transactions.

## DDL (Data Definition Language) Operations

DDL operations (like `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`) require special attention in a synchronous multi-primary cluster to avoid conflicts and outages.

### **Total Order Isolation (TOI) - Default:**

* This is Galera's default DDL method.
* The DDL statement is executed on all nodes in the same order, and it temporarily blocks other transactions on all nodes while it applies.
* It ensures consistency but can cause brief pauses in application activity, especially on busy clusters.
* **Best Practice:** Execute DDL during maintenance windows or low-traffic periods.

### **Rolling Schema Upgrade (RSU) / Percona's `pt-online-schema-change`:**

* For large tables or critical production systems, use tools like `pt-online-schema-change` (from Percona Toolkit) which performs DDL without blocking writes.
* This tool works by creating a new table, copying data, applying changes, and then swapping the tables. It's generally preferred for minimizing downtime for `ALTER TABLE` operations.

### **Non-Blocking Operations (NBO)**

{% hint style="info" %}
Non-Blocking Operations (NBO) are exclusive to MariaDB Enterprise Server
{% endhint %}

* An advanced, automatic method that replicates DDL to all nodes while only blocking the target table, keeping the rest of the cluster operational.&#x20;
* The method requires specific syntax, such as an explicit `LOCK` clause, and is best suited for compatible `ALTER TABLE` statements.

### **`wsrep_OSU_method`:**

* The [system variable](../reference/galera-cluster-system-variables.md#wsrep_osu_method) controls how DDL operations are executed.

## Monitoring Cluster Status

Regularly monitor your Galera Cluster to ensure its health and consistency.

### **`wsrep_cluster_size`**

Number of nodes currently in the Primary Component.

```sql
SHOW STATUS LIKE 'wsrep_cluster_size';
```

Expected value: the total number of nodes configured (e.g., 3).

### **`wsrep_local_state_comment` / `wsrep_local_state`**

The state of the current node.

* `Synced` (4): Node is fully synchronized and operational.
* `Donor/Desync` (2): Node is transferring state to another node.
* `Joining` (1): Node is in the process of joining the cluster.
* `Donor/Stalled` (1): Node is stalled.

### **`wsrep_incoming_addresses`**

List of incoming connections from other cluster nodes.

### **`wsrep_cert_deps_distance`**

Indicates flow control. A high value suggests that this node is falling behind and flow control may activate.

### **`wsrep_flow_control_paused`**

Percentage of time the node was paused due to flow control. High values indicate a bottleneck.

### **`wsrep_local_recv_queue` / `wsrep_local_send_queue`**

Size of the receive/send queue. Ideally, these should be close to 0. Sustained high values indicate replication lag or node issues.

## Handling Node Failures and Recovery

Galera Cluster is designed for automatic recovery, but understanding the process is key.

### **Node Failure**

If a node fails, the remaining nodes continue to operate as the Primary Component. The failed node will automatically attempt to rejoin when it comes back online.

### **Split-Brain Scenarios**

If the network partitions the cluster, nodes will try to form a "Primary Component." The partition with the majority of nodes forms the new Primary Component. If no majority can be formed (e.g., a 2-node cluster splits), the cluster will become inactive. A 3-node or higher cluster is recommended to avoid this.

### **Manual Bootstrapping (Last Resort)**

If the entire cluster goes down or a split-brain occurs where no Primary Component forms, you might need to manually "bootstrap" a new Primary Component from one of the healthy nodes.

* Choose the node that was most up-to-date.
* Stop MariaDB on that node.
* Start it with: `sudo galera_new_cluster` or `sudo systemctl start mariadb --wsrep-new-cluster`.
* Start other nodes normally; they will rejoin the bootstrapped component.

## Application Best Practices

* **Use Connection Pooling:** Essential for managing connections efficiently in high-traffic applications.
* **Short Transactions:** Keep transactions as short and concise as possible to minimize conflicts and improve throughput. Long-running transactions increase the risk of rollbacks due to certification failures.
* **Primary Keys:** All tables should have a primary key. Galera relies on primary keys for efficient row-level replication. Tables without primary keys can cause performance degradation and issues.
* **Retry Logic:** Implement retry logic in your application for failed transactions (e.g., due to certification failures, deadlock, or temporary network issues).
* **Connect to a Load Balancer:** Always direct your application's connections through a load balancer or proxy to leverage automatic failover and intelligent routing.

By following these guidelines, you can effectively manage and operate your MariaDB Galera Cluster for high availability and performance.

## Further Resources:

* [MariaDB Galera Cluster Guide](https://mariadb.com/docs/galera-cluster/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide)
* [Galera Cluster Documentation - Operational Aspects](https://www.google.com/search?q=https://galeracluster.com/documentation/html_docs_galera/operational_aspects.html\&authuser=1)
* [MariaDB documentation - Galera Cluster Best Practices](mariadb-galera-cluster-usage-guide.md#id-6.-application-best-practices)
* [MariaDB documentation - Galera Cluster Monitor](https://mariadb.com/docs/maxscale/maxscale-archive/archive-of-2x.xx-versions/mariadb-maxscale-23-02/mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-galera-monitor)
