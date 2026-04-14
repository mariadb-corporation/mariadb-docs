# Performing Schema Upgrades in Galera Cluster

Performing schema changes (i.e., Data Definition Language or DDL statements like `ALTER TABLE`, `CREATE INDEX`) in a MariaDB Galera Cluster requires special handling. Because Galera is a [multi-primary cluster](../../galera-architecture/introduction-to-galera-architecture.md) where all nodes must remain in sync, a schema change on one [node](../../high-availability/monitoring-mariadb-galera-cluster.md#checking-individual-node-status) must be safely replicated to all other nodes without causing inconsistencies or blocking the entire cluster for an extended period.

MariaDB Galera Cluster provides two methods for handling schema upgrades:

| Method                                     | Description                                                                                                                                                                                              |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total Order Isolation (TOI)                | Default and safest method. The DDL statement is replicated to all nodes, blocking the entire cluster until all preceding transactions complete.                                                          |
| Rolling Schema Upgrade (RSU)               | Advanced, non-blocking method. The DDL is executed on the local node, with changes applied manually to each node in sequence, keeping the cluster online.                                                |
| Non-Blocking Operations (NBO)<sup>\*</sup> | Enterprise grade non-blocking method. The DDL replicates to all nodes in total order, using an efficient locking strategy that only blocks the specific table being altered, keeping the cluster online. |

{% hint style="info" %}
<sup>\*Only available for MariaDB Enterprise Server</sup>&#x20;
{% endhint %}

The method used is controlled by the `wsrep_OSU_method` [session variable](../../reference/galera-cluster-system-variables.md#wsrep_osu_method).

## Total Order Isolation (TOI)

Total Order Isolation is the default method for schema upgrades (`wsrep_OSU_method = 'TOI'`). It ensures maximum data consistency by treating the DDL statement like any other [transaction that must be applied in the same order on all nodes](../../galera-architecture/certification-based-replication.md).

### How TOI Works

When you execute a DDL statement, such as `ALTER TABLE...`, on any node in a cluster, the following process occurs:

1. **Replication**: The statement is replicated across all nodes in the cluster.
2. **Transaction Wait**: Each node waits for transactions that have already been certified (i.e., those already in commit mode) to complete. \
   Active transactions that have not been committed yet are terminated and rolled back immediately. On their next statement, the client will receive `ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction`, and the TOI operation proceeds without waiting.
3. **Execution**: Once caught up, the node executes the DDL statement.
4. **Resume Processing**: After execution, the node can process new transactions.

### Advantages of TOI

* Simplicity and Safety: It is the easiest and safest method. It guarantees that the schema is identical on all nodes at all times.
* Consistency: There is no risk of data drifting or replication errors due to schema mismatches.

### Disadvantages of TOI

A major drawback of DDL statements is that they [block the entire cluster](../performance-tuning/flow-control-in-galera-cluster.md#monitoring-flow-control), preventing any node from processing write transactions during a schema change. This can lead to significant application downtime, especially for large tables that take a long time to alter.

### When to Use TOI

TOI is the recommended method for:

* Schema changes that are known to be very fast.
* Environments where a short period of cluster-wide write unavailability is acceptable.
* Situations where schema consistency is the absolute highest priority.

## Rolling Schema Upgrade (RSU)

Rolling Schema Upgrade is a non-blocking method (`wsrep_OSU_method = 'RSU'`) that allows you to perform schema changes without taking the entire cluster offline.

### How RSU Works

The RSU method tells the cluster to not replicate the DDL statement. The change is only applied to the local node where you execute the command. It is then the administrator's responsibility to apply the same change to the other nodes one by one.

#### Steps to Apply Schema Changes to a Cluster

1. **Set the RSU Method:**\
   On the first node, set the session to `RSU` mode:\
   `SET SESSION wsrep_OSU_method = 'RSU';`
2. **Remove the Node from Rotation:**\
   Remove the node from the [load balancer](../../high-availability/load-balancing/load-balancing-in-mariadb-galera-cluster.md#id-2.-recommended-load-balancer-mariadb-maxscale) to stop it from receiving traffic.
3. **Apply the Schema Change:**\
   Execute the DDL statement (e.g., `ALTER TABLE...`) on the isolated node.
4. **Return the Node to Rotation:**\
   Once the `ALTER` statement is complete, add the node back to the load balancer.
5. **Repeat for All Nodes:**\
   Repeat steps 1-4 for each node in the cluster, one at a time, until all nodes have the updated schema.

### Advantages of RSU

* [High Availability](../../high-availability/understanding-quorum-monitoring-and-recovery.md): The cluster remains online and available to serve traffic throughout the entire process, as you only ever take one node out of rotation at a time.
* No Cluster-Wide Blocking: Application writes can continue on the active nodes.

### Disadvantages of RSU

* Complexity and Risk: The process is manual and more complex, which introduces a higher risk of human error.
* Temporary Inconsistency: For the duration of the upgrade, your cluster will have a mixed schema, where some nodes have the old schema and others have the new one. This can cause [replication errors](../../high-availability/understanding-quorum-monitoring-and-recovery.md) if a transaction that relies on the new schema is sent to a node that has not yet been upgraded.

### When to Use RSU

RSU is the best method for:

* Applying long-running schema changes to large tables where cluster downtime is not acceptable.
* Environments where high availability is the top priority.

It requires careful planning and a good understanding of your application's queries to ensure that no replication errors occur during the upgrade process.

## Non-Blocking Operations (NBO)

{% hint style="info" %}
Non-Blocking Operations is exclusive to MariaDB Enterprise Server.&#x20;
{% endhint %}

Non-Blocking Operations is an advanced, non-blocking method (`wsrep_OSU_method = 'NBO'`) that replicates schema changes automatically across the cluster while significantly reducing the impact on cluster availability.

### **How NBO Works**

Like the TOI method, NBO replicates DDL statements to all nodes in the cluster simultaneously. Nodes wait for all preceding transactions to commit before executing the schema change in the same total order sequence. However, NBO utilizes a much more efficient locking strategy that only blocks access to the specific table being altered, allowing the rest of the cluster to continue processing unrelated transactions.

#### **Steps to Apply Schema Changes to a Cluster using NBO**

1.  Set the NBO Method: It is highly recommended to set this at the session level to avoid accidentally running unsupported DDL (like `CREATE`) under this mode.

    ```sql
    SET SESSION wsrep_OSU_method = 'NBO';
    ```
2. Verify Application Connectivity: Ensure no clients have long-running open transactions that include the target table, as this can cause the initial table-locking phase to block the cluster.
3.  Execute the DDL with explicit LOCK: Execute your `ALTER TABLE` statement ensuring you include a mandatory `SHARED` or `EXCLUSIVE` lock clause.

    * Using SHARED: Allows other clients to read from the table during the alter, but blocks writes.
    * Using EXCLUSIVE: Blocks both reads and writes to that specific table.

    ```sql
    ALTER TABLE my_table LOCK SHARED, ADD COLUMN new_col INT;
    ```
4. Confirm Completion: The statement will complete automatically across all nodes in the same total order sequence. You can monitor the operation's persistence even if a node crashes during the process.
5.  Revert to Default Method (Optional): After the operation, return the session to the default method for safety.

    ```sql
    SET SESSION wsrep_OSU_method = 'TOI';
    ```

### **Advantages of NBO**

* Cluster Availability: You can continue to process DML (inserts, updates, deletes) on all tables in the cluster except for the one currently being modified.
* Automatic Consistency: Unlike RSU, changes are applied automatically and consistently across all nodes in total order without manual intervention.
* Parallel Operations: You can execute another NBO alter on a different table while an existing NBO operation is already in progress.
* Fault Tolerance: If one node crashes during the operation, the DDL will continue on the remaining nodes and persist if successful.

### **Disadvantages of NBO**

* Table-Level Locking: Writes to the table being altered are completely blocked until the operation is finished. If `LOCK EXCLUSIVE` is used, read operations are also blocked.
* SST and IST Impact: Nodes cannot serve as donors for State Snapshot Transfers (SST) while an NBO operation is running. Furthermore, any node that leaves the cluster during the DDL becomes inconsistent and can only rejoin via a full SST, not an IST.
* Syntax Requirements: NBO has strict requirements for SQL syntax and does not support many common DDL statements like `CREATE`, `DROP`, or `RENAME`.

### **Key Considerations for NBO Syntax**

To utilize NBO, the DDL statement must meet specific criteria:

* Explicit Locking: `ALTER TABLE` statements must include an explicit `LOCK SHARED` or `LOCK EXCLUSIVE` clause. Statements without a `LOCK` clause default to `DEFAULT` and are not supported.
* Supported Commands: Beyond specific `ALTER` statements, `ANALYZE TABLE` and `OPTIMIZE TABLE` are also supported.
* Single Table Limitation: Do not use NBO with statements that operate on more than one table at a time.

### **When to Use NBO**

NBO is the best method for:

* Applying long-running `ALTER TABLE` statements where you need to maintain global schema consistency automatically without manual steps.
* Environments that require high availability for the majority of the database while a specific table is being upgraded.
* Standard maintenance operations such as `ANALYZE` or `OPTIMIZE` on large tables.

To ensure cluster stability, it is recommended to enable NBO only for specific sessions running compatible DDL rather than on a server-wide basis. SQL statements such as `CREATE TABLE` and `DROP TABLE` should always be executed using the Total Order Isolation (TOI) method to avoid schema conflict

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
