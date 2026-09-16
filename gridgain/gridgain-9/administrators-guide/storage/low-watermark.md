---
description: >-
  How the GridGain 9 low watermark controls data retention and garbage
  collection, how to configure and tune it, and how to recover a stalled low
  watermark.
---

# Low Watermark and Garbage Collection

GridGain keeps more than one version of each row so that transactions can read consistent data without blocking writers. Those older versions cannot be kept forever, so GridGain periodically removes the ones no transaction can still need. The point that separates "still needed" from "safe to remove" is called the *low watermark*.

## About Low Watermark

The low watermark is a cluster-wide timestamp that marks the boundary of data retention. Any data that became obsolete at or below the low watermark (overwritten row versions, deleted rows, or dropped tables) is considered garbage and will be permanently removed. Data that became obsolete above the low watermark is still retained, because a transaction may still need to read it.

The low watermark only ever moves forward in time, and it trails behind the current time by a configurable interval. By default, it sits roughly 10 minutes in the past, which means obsolete data remains available for about 10 minutes before it becomes eligible for cleanup.

Low watermark serves two purposes:

* It tells the garbage collector which old data is safe to delete.
* It defines how far into the past a read-only transaction can read. A read-only transaction reading data older than the low watermark is rejected, because that data may no longer exist.

### How Garbage Collection Uses Low Watermark

Every time a row is updated, GridGain does not overwrite the existing value. Instead, it adds a new version with a timestamp, forming a *version chain* within the partition. Read-only transactions use these versions to read a consistent snapshot of the data as it existed at their read timestamp. For details on how version chains are stored, see the [Version Storage](data-partitions.md#version-storage) section.

As the low watermark advances, GridGain identifies row versions, deleted rows, and dropped tables that became obsolete at or before the new low watermark and queues them for removal. The garbage collector then deletes this data in batches in the background. Cleanup is not instantaneous: data eligible for collection may remain on disk until the next collection cycle processes it.

GridGain also protects in-flight work. If a read-only transaction started before the low watermark advanced, the versions it relies on are kept available until that transaction completes, even if collection runs in the meantime. Before removing any data, GridGain confirms that it is not required anywhere else in the cluster.

### What Low Watermark Affects

The low watermark is the single retention boundary for all historical and obsolete data in the cluster, not just old row versions. As it advances, GridGain uses it to clean up:

* Obsolete row versions and deleted rows in the version chains.
* Dropped tables, which remain on disk until the low watermark passes the point at which they were dropped.
* Metadata for removed indexes, and cached SQL statistics for dropped tables.
* Obsolete versions of row-level security policies.
* Transaction resources that are no longer needed.

The low watermark also defines the consistency boundary for operations that read or reconstruct historical data. None of the following can read or recover data older than the low watermark:

* [Read-only transactions](../transactions.md#read-only-transactions) and time-travel queries.
* [Continuous queries](../../developers-guide/continuous-queries.md) that scan historical data.
* [Point-in-time recovery](../snapshots/point-in-time-recovery.md).
* [Data center replication](../data-center-replication/configuring-replication.md).

## Configuration

The low watermark and garbage collector are configured under `ignite.gc` in the cluster configuration. The most important settings are:

| Property | Default | Description |
|---|---|---|
| `gc.lowWatermark.dataAvailabilityTimeMillis` | `600000` (10 minutes) | How long obsolete data remains available before it is eligible for removal. The low watermark is calculated as the current time minus this value (adjusted for clock skew). |
| `gc.lowWatermark.updateIntervalMillis` | `300000` (5 minutes) | How often the low watermark is recalculated and advanced. |
| `gc.batchSize` | `5` | The number of entries removed per partition in a single garbage collection batch. |
| `gc.threads` | Number of available processors | The number of threads the garbage collector uses. Changing this value requires a node restart. |

For the complete property reference, including acceptable value ranges, see the [Garbage Collection Configuration](../config/cluster-config.md#garbage-collection-configuration) section.

To increase how long obsolete data is retained - for example, to 30 minutes - update the data availability time:

```shell
cluster config update ignite.gc.lowWatermark.dataAvailabilityTimeMillis=1800000
```

## Tuning Low Watermark

Low watermark configuration trades storage usage against how far into the past reads and recovery can reach. A larger `dataAvailabilityTimeMillis` keeps obsolete versions, deleted rows, and dropped tables on disk longer. As a result, read-only and time-travel queries, continuous queries, and [point-in-time recovery](../snapshots/point-in-time-recovery.md) can all reach further back, but the cluster requires more storage. A smaller value reclaims storage sooner at the cost of a shorter read horizon.

{% hint style="warning" %}
Keep `dataAvailabilityTimeMillis` at least as large as the read-only transaction timeout (`ignite.transaction.readOnlyTimeoutMillis`), or a long-running read-only transaction can outlive the data it depends on and fail. See the [Read-Only Transactions](../transactions.md#read-only-transactions) section.
{% endhint %}

`updateIntervalMillis` controls how often the watermark advances - a shorter interval spreads collection work out and frees data sooner, while a longer one lets more garbage accumulate between cycles. `batchSize` and `threads` tune collector throughput rather than the retention window. You should raise them on write-heavy clusters where garbage accumulates quickly.

## Recovering Stalled Low Watermark

The low watermark can only advance when data is not reserved. To keep the watermark from passing data still in use, GridGain places an internal lock for each reader (for example, an active read-only transaction), and releases it when the reader finishes. While a lock is held, the low watermark cannot move past the locked timestamp, and garbage collection of data below it is paused.

Under normal operation these locks are short-lived. In rare cases a lock can be left behind with no reader to release it. The low watermark then stops advancing, obsolete data is no longer collected, and storage usage grows over time.

TO keep track of LWM advancing, use the `mvgc.LastVacuumedLwm` metric. If you notice that the watermark has stalled, you can force the stale locks to be released with the [recovery low-watermark drop-locks](../../ignite-cli-tool.md#recovery-low-watermark-drop-locks) CLI command. The command removes low watermark locks older than a given age on all cluster nodes:

```shell
recovery low-watermark drop-locks 3600000
```

By default, the command performs a safety check and fails if a read-only transaction older than the cutoff is still active, or if a secondary storage full state transfer is in progress. Add the `--force` option to remove the locks unconditionally.

{% hint style="danger" %}
`--force` removes the locks but does not cancel the transactions or operations that own them. Removing a lock that an active reader still needs can cause that reader to fail or to read data that has since been collected. Use `--force` only for recovery, after confirming the affected readers are no longer needed.
{% endhint %}
