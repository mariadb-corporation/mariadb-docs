---
description: >-
  How ACID transactions work in GridGain 9 — transaction types, guarantees,
  isolation, MVCC, locking, timeouts, coordination, and monitoring.
---

# Transactions

GridGain provides ACID transactions to ensure data consistency and isolation across your cluster. Understanding how transactions work is essential for configuring and troubleshooting, your cluster, and optimizing your application.

## Transaction Types

GridGain supports two types of transactions, each optimized for different workloads. The type of transaction you use determines how GridGain handles locks, replication, and coordination across partitions.

### Read-Write Transactions

Read-write transactions should be used when your application needs to modify data. When a read-write transaction begins, GridGain assigns it a begin timestamp that establishes the schema version that will be used for the transaction. As the transaction executes, it acquires exclusive locks on any rows it modifies, preventing other transactions from making conflicting changes. These modifications are initially stored as tentative versions called *write intents*. Additionally, the transaction acquires shared locks that are applied to rows read by the transaction.

Read-write transactions use consensus-based commit protocol to ensure atomicity across all affected partitions. This means that if your transaction modifies data in multiple partitions, GridGain coordinates with each partition to ensure either all changes are applied or none are. The transaction coordinator tracks which partitions have been enlisted (touched by the transaction) and manages the commit process across all of them using consensus to finalize the transaction state.

#### How Read-Write Transactions Work

When a read-write transaction begins, GridGain assigns it a begin timestamp using the coordinator's clock.

As your application executes operations within the transaction, GridGain tracks which partitions are involved. The first partition enlisted into the transaction becomes the commit partition. This partition plays a special role - it stores the durable transaction state (whether the transaction committed or aborted) and acts as the source of truth if the transaction coordinator fails.

During execution, each write operation creates a *write intent*. These are tentative versions of the data that are not yet visible to other transactions. Locks on the modified rows on the primary partition replicas to prevent other transactions from making conflicting changes. These locks are held until the transaction completes.

When your application commits the transaction, GridGain's transaction coordinator performs a consensus-based transaction finish. First, in case of commit, it generates a commit timestamp and verifies that all the primary replicas involved in the transaction are still valid - their leases have not expired. Then it writes the transaction's final state (either committed or aborted) to the commit partition, and this state is confirmed by consensus of commit partition group.

Once the transaction is committed or aborted, the commit partition sends write-intent-switch messages to all enlisted partitions. Each partition resolves write intents—converting them to committed versions with the commit timestamp, or removing them in case of a rollback. Lock release is synchronous: your application receives confirmation only after locks are released, ensuring that subsequent transactions can safely acquire locks on the same keys.

### Read-Only Transactions

Read-only transactions provide a lightweight mechanism for reading data without modifying it. Unlike read-write transactions, they do not acquire any locks, which makes them suitable for analytical queries and reporting workloads that need to scan large amounts of data.

When a read-only transaction begins, it receives a read timestamp. All reads within the transaction use this same timestamp, providing a consistent snapshot of the data as it existed at that point in time. Because read-only transactions do not modify data, they can read from any replica - primary or backup - without interfering with write operations happening concurrently.

Read-only transactions are particularly useful for long-running analytical queries because they do not hold locks and do not block other transactions. However, you need to ensure that old data versions are retained long enough for your longest queries to complete, which is controlled by the garbage collection configuration.

#### How Read-Only Transactions Work

Read-only transactions follow a much simpler path than read-write ones.

When they begin, GridGain client calculates a read timestamp that accounts for local timestamp (called *observable timestamp*), clock skew,  safe time propagation across the cluster. This ensures the transaction can safely read from any replica without seeing inconsistent data. Each client calculates the observable timestamp individually. The timestamp is set slightly in the past to account for data replication to other replicas and speed up request handling. As a result, the data becomes available to other clients once their local timestamp reaches the time of the transaction. When reading data from the same client data becomes visible immediately, as the timestamp is consistent.

Each RO transaction operates on it's own immutable snapshot, defined by read timestamp.

During execution, all reads use this same timestamp. GridGain's multi-version concurrency control (MVCC) system maintains multiple versions of each row, so the transaction can read the appropriate version without blocking concurrent writes. There's no need for locks, no need for a commit protocol, and no coordination across partitions.

When the transaction finishes, it simply releases its timestamp (allowing old versions to be cleaned up) and completes. There's nothing to commit or roll back because no data was modified. The only consideration is that GridGain needs to ensure the old data versions the transaction might read are not garbage collected while the transaction is active.

## Transaction Guarantees

GridGain transactions provide full ACID guarantees. Atomicity ensures that either all operations within a transaction succeed or none do - there are no partial updates. Consistency means that transactions maintain all data integrity constraints defined in your schema. Isolation prevents concurrent transactions from interfering with each other, and durability guarantees that once a transaction commits, its changes survive any subsequent failures.

### Isolation Level

GridGain provides Strictly Serializable isolation level for read-write transactions. This means you will never see uncommitted data from other transactions (no dirty reads), if you read the same row multiple times within a transaction, you always see the same value (no non-repeatable reads), and if you re-execute the same query you will always see the same set of rows (no phantom reads). Other kinds of data anomalies are also prevented. Once a transaction is committed, all subsequent transactions will immediately see its effects, and the order of operations is preserved.

### Causality Preservation

GridGain preserves causality through Hybrid Logical Clock (HLC) timestamps and locking protocol. When a client reads data from transaction A and then starts transaction B, the system ensures B's timestamp is higher than A's timestamp, maintaining causal order.

For example, if transaction A commits with timestamp 100 and a client then starts transaction B after reading A's results, transaction B will automatically receive a timestamp of at least 101. This guarantees that B will always see A's committed changes, and that external observers will see these transactions in the correct causal order.

## Hybrid Logical Clock

GridGain uses Hybrid Logical Clock (HLC) to assign timestamps to transactions. HLC combines physical clock time with a logical counter, providing consistent timestamp ordering without requiring a centralized timestamp service.

Here is how HLC mechanism works:

- Each node maintains a local HLC value consisting of a physical time component and a logical counter;
- When sending a message, the node includes its current HLC value;
- When receiving a message, the node updates its local HLC to the maximum of its local value and the received value, then increments the logical counter;
- Timestamps advance monotonically even in the presence of clock skew.

This design eliminates the need for a centralized timestamp coordinator, which would be a single point of failure and a performance bottleneck. Instead, timestamps are assigned locally while still maintaining global ordering through the HLC protocol.

Transaction protocol provides bounded tolerance for clock skew. The cluster is configured with a maximum allowed clock skew through the `schemaSync.maxClockSkewMillis` parameter. All nodes in the cluster must have their clocks synchronized within this threshold, typically through NTP or a similar time synchronization service. If clock skew exceeds this threshold, transaction operations may fail.

## Multi-Version Concurrency Control

GridGain's MVCC system is what enables read-only transactions to run without acquiring locks. Every time a row is updated, GridGain does not immediately overwrite the old version. Instead, it adds a new version with a timestamp, creating a version chain. When a read-only transaction reads a row, GridGain finds the appropriate version based on the transaction's read timestamp. This allows read-only transactions to see consistent historical data without blocking concurrent writes.

Old versions are retained until the low watermark passes them, after which garbage collection removes them. The retention window therefore determines how long a read-only transaction can run before the versions it relies on are cleaned up; the default is 10 minutes. For how to configure this window and the trade-offs involved, see [Low Watermark and Garbage Collection](storage/low-watermark.md). For how version chains are stored and managed, see the [Version Storage](storage/data-partitions.md#version-storage) section.

## Locking and Concurrency

GridGain uses row-level locks to control concurrent access to data. When a read-write transaction modifies a row, it acquires an exclusive lock on that row. This prevents other transactions from reading or modifying that row until the lock is released at commit or rollback time. The locks are managed automatically - your application doesn't need to explicitly request or release them.

When multiple transactions try to access the same rows, GridGain needs to determine which transaction proceeds and which must wait or abort. The system uses a priority-based scheme where older transactions (those with earlier begin timestamps) have higher priority. If an older transaction requests a row locked by a younger one, the younger transaction is aborted and retried so the older transaction can proceed; a younger transaction that requests a row locked by an older one waits for the lock to be released. This prevents deadlocks - circular waits where transactions are each waiting for locks held by the other. For the full algorithm, see [Deadlock Prevention](../developers-guide/transactions.md#deadlock-prevention).

## Transaction Timeouts

To prevent transactions from holding resources indefinitely, GridGain enforces configurable timeouts. Read-write transactions default to a 30-second timeout, which is appropriate for short-lived transactional operations. Read-only transactions default to a 10-minute timeout to accommodate longer analytical queries.

When a transaction exceeds its timeout, GridGain automatically aborts it, releases all locks, removes any write intents, and returns an error to the application. The timeout values can be adjusted based on your workload characteristics. For example, if you have a fast OLTP workload where all transactions should complete quickly, you might reduce the read-write timeout to 5 seconds to quickly identify problematic queries:

```bash
cluster config update ignite.transaction.readWriteTimeoutMillis=5000
```

Conversely, if you have long-running analytical queries, you might increase the read-only timeout:

```bash
cluster config update ignite.transaction.readOnlyTimeoutMillis=1800000  # 30 minutes
```

It's important to keep the timeout configuration aligned with garbage collection settings. The `dataAvailabilityTimeMillis` should be at least as large as `readOnlyTimeoutMillis` to ensure that old data versions are not garbage collected while read-only transactions that might need them are still active.

## Distributed Transaction Coordination

When a transaction modifies data in multiple partitions, GridGain must coordinate the commit across all of them to maintain atomicity. This coordination happens through partition enlistment and the two-phase commit protocol.

As a transaction executes, each partition it writes to is enlisted - added to the list of partitions involved in the transaction. The first partition enlisted becomes the commit partition, which has special responsibilities. It stores the durable transaction state and serves as the authoritative source if the transaction coordinator fails.

During the commit process, the coordinator first generates a commit timestamp and verifies that all the primary replicas involved in the transaction are still valid. This verification checks that the leases have not expired and that the transaction is working with the current partition leaders. Then the coordinator writes the transaction state (committed or aborted) to the commit partition, where it's replicated through RAFT to ensure durability. If any primary replica involved in the transaction expires, it becomes impossible to commit the transaction.

Once the transaction is durable (either commit or rollback was performed), the coordinator enters the cleanup phase. It sends messages to each enlisted partition instructing them to process their write intents and release locks. For committed transactions, write intents are converted to committed versions. For rolled back transactions, write intents are deleted. This cleanup happens asynchronously - the application receives confirmation as soon as the transaction finish is durable, without waiting for all cleanup operations to complete.

The consensus-based transaction finishing protocol ensures atomicity even in the face of failures. If the coordinator crashes before completing the commit, other nodes detect the failure and query the commit partition to determine the transaction's final state. If the transaction was committed, the changes are applied everywhere. If it wasn't committed, the transaction is rolled back and all write intents are removed.

## Transaction Failure Handling

GridGain handles various failure scenarios automatically without requiring administrator intervention. Understanding these failure modes helps you design resilient applications.

If a transaction coordinator node fails while a transaction is in progress, other nodes eventually detect the coordinator is offline and mark the transaction as abandoned. They then query the commit partition to determine what should happen to the transaction. If the transaction reached the point where its final state was written to the commit partition, that state is honored - committed transactions stay committed, aborted transactions stay aborted. If the transaction never reached that point, it's rolled back to maintain consistency.

If a replica that holds data for a transaction fails, the RAFT protocol automatically handles the failover. The remaining replicas elect a new leader, and because the transaction's write intents were replicated to the majority, the new leader has all the necessary data to continue. The transaction proceeds normally from the application's perspective.

If a commit partition group involved in the transaction fails (for example, by losing the quorum), the transaction cannot be finished until the partition group is operational.

When a transaction times out, GridGain automatically cleans up all resources associated with it. The coordinator releases locks, removes write intents, and marks the transaction as aborted. The application receives a timeout error, and depending on your application logic, you can retry the transaction with a longer timeout if needed.

## Monitoring Transactions

You can monitor active transactions by querying the system views. The `system.transactions` view shows all currently active transactions, including their begin timestamps and which partitions they've enlisted:

```sql
SELECT * FROM system.transactions;
```

GridGain also provides [metrics](metrics/metrics-list.md) for transaction monitoring. These metrics track the count of active, committed, and aborted transactions, measure lock wait times, and calculate conflict rates. You can use these metrics to identify patterns in transaction behavior and spot potential issues.

Common issues include high abort rates, which typically indicate lock contention between transactions. Review your transaction access patterns to see if transactions are consistently accessing the same hot rows. Timeout errors suggest either that your timeout configuration is too aggressive or that queries need optimization. Slow commits can indicate network latency issues or problems with replication health.
