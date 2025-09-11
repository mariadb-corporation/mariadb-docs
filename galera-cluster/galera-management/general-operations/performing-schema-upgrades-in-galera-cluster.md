# Performing Schema Upgrades in Galera Cluster

Performing schema changes (i.e., Data Definition Language or DDL statements like `ALTER TABLE`, `CREATE INDEX`) in a MariaDB Galera Cluster requires special handling. Because Galera is a [multi-primary cluster](../../galera-architecture/introduction-to-galera-architecture.md) where all nodes must remain in sync, a schema change on one [node](../../high-availability/monitoring-mariadb-galera-cluster.md#checking-individual-node-status) must be safely replicated to all other nodes without causing inconsistencies or blocking the entire cluster for an extended period.

MariaDB Galera Cluster provides two methods for handling schema upgrades:

| Method                       | Description                                                                                                                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total Order Isolation (TOI)  | Default and safest method. The DDL statement is replicated to all nodes, blocking the entire cluster until all preceding transactions complete.           |
| Rolling Schema Upgrade (RSU) | Advanced, non-blocking method. The DDL is executed on the local node, with changes applied manually to each node in sequence, keeping the cluster online. |

The method used is controlled by the `wsrep_OSU_method` [session variable](../../reference/galera-cluster-system-variables.md#wsrep_osu_method).

## Total Order Isolation (TOI)

Total Order Isolation is the default method for schema upgrades (`wsrep_OSU_method = 'TOI'`). It ensures maximum data consistency by treating the DDL statement like any other [transaction that must be applied in the same order on all nodes](../../galera-architecture/certification-based-replication.md).

### How TOI Works

When you execute a DDL statement, such as `ALTER TABLE...`, on any node in a cluster, the following process occurs:

1. **Replication**: The statement is replicated across all nodes in the cluster.
2. **Transaction Wait**: Each node waits for any pre-existing transactions to complete before proceeding.
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
