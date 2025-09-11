# Using Streaming Replication for Large Transactions

Streaming Replication optimizes replication of large or long-running transactions in MariaDB Galera Cluster. Typically, a node executes a transaction fully and replicates the complete [write-set](../../galera-architecture/introduction-to-galera-architecture.md#the-wsrep-api) to other nodes at [COMMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/commit) time. Although efficient for most workloads, this approach can be challenging for very large or lengthy transactions.

With Streaming Replication, the initiating node divides the transaction into smaller fragments. These fragments are certified and replicated to other nodes while the transaction is ongoing. Once a fragment is certified and applied to the replicas, it becomes immune to abortion by conflicting transactions, thus improving the chances of the entire transaction succeeding. This method also supports processing of transaction write-sets over two Gigabytes.

{% hint style="info" %}
Streaming Replication is available in Galera Cluster 4.0 and later versions. Both [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/10-4) and newer, and [MariaDB Community Server 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server) and newer, on supported platforms, include Galera 4.
{% endhint %}

## When to Use Streaming Replication

In most cases, the standard replication method is sufficient. Streaming Replication is a specialized tool for specific scenarios. The best practice is to enable it only at the session level for the specific transactions that require it.

### Large Data Transactions

This is the primary use case. When performing a massive [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete), or [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), normal replication requires the originating node to hold the entire transaction locally and then send a very large write-set at commit time. This can cause two problems:

1. A significant replication lag, as the entire cluster waits for the large write-set to be transferred and applied.
2. The replica nodes, while busy applying the large transaction, cannot commit other transactions, which can trigger [Flow Control](flow-control-in-galera-cluster.md) and throttle the entire cluster.

With Streaming Replication, the node replicates the data in fragments throughout the transaction's lifetime. This spreads the network load and allows replica nodes to apply other concurrent transactions between fragments, minimizing the impact on the overall [cluster performance.](./)

### Long-Running Transactions

A transaction that remains open for a long time has a higher chance of [conflicting with a smaller, faster transaction](../../galera-architecture/certification-based-replication.md#how-the-process-works) that commits first. When this happens, the long-running transaction is aborted.

Streaming Replication mitigates this by committing the transaction in fragments. Once a fragment is [certified](../../galera-architecture/certification-based-replication.md), it is "locked in" and cannot be aborted by a new conflicting transaction.

{% hint style="danger" %}
Certification keys derive from record locks, not gap locks. If a streaming transaction holds a gap lock, another node's transaction can still apply a [write-set](../../galera-architecture/introduction-to-galera-architecture.md#the-wsrep-api) in that gap, potentially aborting the streaming transaction.
{% endhint %}

### High-Contention ("Hot") Records

For applications that frequently update the same row (e.g., a counter, a job queue, or a locking scheme), Streaming Replication can be used to force a critical update to replicate immediately. This effectively locks the ["hot record" on all nodes](../../high-availability/load-balancing/load-balancing-in-mariadb-galera-cluster.md#read-write-splitting-recommended), preventing other transactions from modifying it and increasing the chance that the critical transaction will commit successfully.

## How to Enable and Use Streaming Replication

Streaming Replication should be enabled at the session level just for the transactions that need it. This is controlled by two session variables:

* [wsrep\_trx\_fragment\_unit](../../reference/galera-cluster-system-variables.md#wsrep_trx_fragment_unit) defines what a "unit" of replication is.
* [wsrep\_trx\_fragment\_size](../../reference/galera-cluster-system-variables.md#wsrep_trx_fragment_size) defines how many units make up a fragment.

To enable streaming, you set both variables:

```sql
SET SESSION wsrep_trx_fragment_unit = 'statements';
SET SESSION wsrep_trx_fragment_size = 10;
```

In the above example, the node will create, certify, and replicate a fragment after every 10 SQL statements within the transaction.

The available fragment units for `wsrep_trx_fragment_unit` are:

| Parameter    | Description                                                            |
| ------------ | ---------------------------------------------------------------------- |
| `bytes`      | The fragment size is defined in bytes of the write-set.                |
| `rows`       | The fragment size is defined by the number of rows affected.           |
| `statements` | The fragment size is defined by the number of SQL statements executed. |

To disable Streaming Replication, you can set `wsrep_trx_fragment_size` back to `0`.

## _Managing_ a "Hot Record"

Consider an application that manages a work order queue. To prevent two users from getting the same queue position, you can use Streaming Replication for the single critical update.

1.  Begin the transaction:

    ```sql
    START TRANSACTION;
    ```
2.  After reading necessary data, enable Streaming Replication for just the next statement:

    ```sql
    SET SESSION wsrep_trx_fragment_unit = 'statements';
    SET SESSION wsrep_trx_fragment_size = 1;
    ```
3.  Perform the critical update. This statement will be immediately fragmented and replicated:

    ```sql
    UPDATE work_orders
       SET queue_position = queue_position + 1;
    ```
4.  Immediately disable Streaming Replication for the rest of the transaction:

    ```sql
    SET SESSION wsrep_trx_fragment_size = 0;
    ```
5.  Perform other, non-critical tasks for the work order, and then commit:

    ```sql
    COMMIT;
    ```

This ensures the `queue_position` update is replicated and certified across the cluster before the rest of the transaction proceeds, preventing [race conditions](../../high-availability/understanding-quorum-monitoring-and-recovery.md#quorum-calculation).

## Limitations and Performance Considerations

Before using Streaming Replication, consider the following limitations:

### Performance Overhead

When Streaming Replication is enabled, Galera records all write-sets to a log table ([mysql.wsrep\_streaming\_log](../../reference/galera-cluster-system-tables.md#wsrep_streaming_log)) on every node to ensure persistence in case of a crash. This adds write overhead and can impact performance, which is why it should only be used when necessary.

### Cost of Rollbacks

If a streaming transaction needs to be rolled back after some fragments have already been applied, the rollback operation consumes system resources on all nodes as they undo the previously applied fragments. Frequent rollbacks of streaming transactions can become a performance problem.

For these reasons, it is always a good application design policy to use shorter, smaller transactions whenever possible.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
