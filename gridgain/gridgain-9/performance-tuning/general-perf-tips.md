---
description: >-
  General performance considerations for GridGain 9, including deployment
  practices, colocation, heap and metadata placement, partitioning, and
  efficient data access.
---

# General Performance Considerations

GridGain and Ignite as distributed storage and computing platforms require certain optimization techniques. Before you dive
into more advanced techniques described in this and other articles, consider the following basic checklist:

- GridGain is designed and optimized for distributed computing scenarios. Deploy and benchmark a multi-node cluster
  rather than a single-node.

- GridGain can scale equally well horizontally and vertically.
  Thus, consider allocating all available CPU and RAM resources on a local machine to a GridGain node.
  A single node per physical machine is the recommended configuration.

- In cases where GridGain is deployed in a virtual or cloud environment, it is ideal (but not strictly required) to
  pin a GridGain node to a single host. This provides two benefits:

  - Avoids the "noisy neighbor" problem where GridGain VMs would compete for the host resources with other applications. This might cause performance spikes on your GridGain cluster.
  - Ensures high availability. If a host goes down, and you have two or more GridGain server node VMs pinned to it, it can lead to data loss.

- If resources allow, store the "hot" dataset in RAM to avoid cache thrashing.

- Ensure that the colocation key provides good partition hash distribution. Each colocation key column is hashed separately and combined with other column hashes.

- Adjust data colocation so related objects are placed on the same server node. For instance, if your data is properly colocated, you can run SQL queries with JOINs at massive scale and expect significant performance benefits.

- If Native Persistence is used, follow this [persistence optimization techniques](persistence-tuning.md).

- Make sure the host OS is properly [tuned](os-tuning.md).

- If you are going to run SQL with GridGain, see [SQL-related optimizations](sql-tuning.md) for more details.

{% hint style="warning" %}
Verify all performance recommendations from this paper in a test environment before delivering to the production environment.
{% endhint %}

## Enabling One-Way SSL

By default, all connections are secured with two-way SSL. You can switch to one-way SSL to improve connection speed by configuring the server not to verify client certificates. Set the `clientAuth=optional` property in [SSL settings](../administrators-guide/security/ssl-tls.md).

## Limiting Number of Active Compute Tasks

Compute tasks are deployed to the same JVM that executes data access operations. Make sure jobs are designed safely so they do not steal resources from the execution engine.

## Large Number of Columns in a Row

When GridGain accesses a column in a row, it reads the entire row. This may lead to excessive memory pressure when the row has a large number of columns or when columns contain large data.

To improve application performance, use rows that contain only relevant fields whenever possible.

## Avoiding Cluster Overload

Make sure you do not overload the cluster. If the cluster is saturated and throughput does not scale when adding new client nodes, add more server nodes. Conduct benchmarks to find the saturation point specific to your load.

## Using Metrics

Enabling [metrics](../administrators-guide/metrics/metrics-list.md) is helpful for cluster observability but may affect performance in a minor way. Enable only those metrics that are truly necessary.

## Separating Data and Metadata

To improve cluster stability, it is highly recommended to place metadata on separate hardware so metadata operations do not overlap with data operations.

For example, place metadata on separate fast storage while keeping data on larger capacity drives:

```javascript
ignite {
  system {
    metastoragePath = "/mnt/ssd/gridgain/metadata"
    cmgPath = "/mnt/ssd/gridgain/cmg"
    partitionsBasePath = "/mnt/hdd/gridgain/data"
    partitionsLogPath = "/mnt/hdd/gridgain/raft-logs"
  }
}
```

## Partition Configuration

GridGain automatically calculates the required number of partitions during cluster initialization using the following formula:

`nodes * cores * scale_coeff / replication_factor`

where `scale_coeff = 2`.

However, you can override the default number of partitions by using increased `scale_coeff` values, such as 3 or 4, if you plan to scale in the future. Generally, more partitions mean higher parallelism, but too many incur overhead due to partition maintenance.

## Distribution Zones Configuration

Each distribution zone adds additional overhead in maintaining its topology. Do not create many distribution zones with the same configuration. Instead, place tables in the same distribution zone whenever possible.

## Efficient Data Access

- Employ transaction [parallelism](../developers-guide/transactions.md#transaction-isolation-and-concurrency) whenever possible.
  - For example, for a money transfer between two accounts, both reads and writes for each account can be done concurrently.
- Use [read-only](../developers-guide/transactions.md#read-only-transactions), lockless transactions when possible.
- Prefer a single batch operation over many single-key operations.
- It is a good idea to mix a read-only transaction to prefetch a consistent snapshot, perform calculations, and use standard transactions to update modified rows.
- Use atomic table operations when possible.
  - For example, [`getAndPut`](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/KeyValueView.html#getAndPut\(org.apache.ignite.tx.Transaction,K,V\)) is more efficient than `get` and subsequent `put`.
- Avoid using low-selectivity SQL queries in read-write transactions. Such queries can quickly exhaust the lock table size. You might want to increase the lock table size if you get a "lock table overflow" error.
