---
description: >-
  GridGain 9.1.19 brings more monitoring improvements, an experimental ML
  inference framework, a reworked distributed map API, and fixes for known
  issues, including the data center replication issue from 9.1.18.
---

# GridGain 9.1.19 Release Notes

## Overview

GridGain 9.1.19 is a private release that brings more monitoring improvements, ML inference framework and fixes for known issues.

## Resolved Known Issues

This release resolves the issue with Data Center Replication stopping early that appeared in GridGain 9.1.18.

## Major Changes

### Major Rework of Distributed Map API

Starting with this release, the `put()` and `remove()` methods in `IgniteMap` have been split into separate operations based on whether the previous value needs to be returned. The `put()` method now returns `void` for better performance when the previous value is not needed, and a new `getAndPut()` method returns the previous value. Similarly, `remove()` now returns a `boolean` to indicate if the key existed, and a new `getAndRemove()` method returns the removed value.

#### New Methods

New methods have been added to provide explicit control over return values:

**Put Operations**

- `void put(K key, V value)` - inserts or updates a value without returning the previous value;
- `CompletableFuture<Void> putAsync(K key, V value)` - async version of `put()`;
- `V getAndPut(K key, V value)` - inserts or updates a value and returns the previous value;
- `CompletableFuture<V> getAndPutAsync(K key, V value)` - async version of `getAndPut()`.

**Remove Operations**

- `boolean remove(K key)` - removes a mapping and returns `true` if the key existed;
- `CompletableFuture<Boolean> removeAsync(K key)` - async version of `remove()`;
- `V getAndRemove(K key)` - removes a mapping and returns the removed value;
- `CompletableFuture<V> getAndRemoveAsync(K key)` - async version of `getAndRemove()`;
- `void removeAll(Collection<K> keys)` - removes multiple mappings in a single operation;
- `CompletableFuture<Void> removeAllAsync(Collection<K> keys)` - async version of `removeAll()`.

**Map Destruction**

- `void destroy()` - destroys the map, removing all data and metadata;
- `CompletableFuture<Void> destroyAsync()` - async version of `destroy()`;
- `void destroyMap(String name)` - destroys a map by name via `IgniteStructures` interface;
- `CompletableFuture<Void> destroyMapAsync(String name)` - async version of `destroyMap()`.

**Type Safety**

A new `MapTypeMismatchException` is thrown when attempting to open an existing map with incompatible key or value types. The exception message clearly indicates which type (key or value) does not match.

#### Code Migration

All code that uses the return value from `IgniteMap.put()`, `IgniteMap.remove()`, or their async variants will no longer compile.

**Migrating put() with Return Value**

If your code uses the return value from `put()`, replace it with `getAndPut()`:

```java
// Before - will not compile
String previousValue = map.put(userId, userName);

// After - use getAndPut()
String previousValue = map.getAndPut(userId, userName);
```

If your code ignores the return value, no changes are required:

```java
// No change needed
map.put(userId, userName);
```

**Migrating remove() with Return Value**

If your code uses the removed value from `remove()`, replace it with `getAndRemove()`:

```java
// Before - will not compile
String removedValue = map.remove(userId);
if (removedValue != null) {
    processValue(removedValue);
}

// After - use getAndRemove()
String removedValue = map.getAndRemove(userId);
if (removedValue != null) {
    processValue(removedValue);
}
```

If your code only checks whether a key was removed, update to use the boolean return value:

```java
// Before - will not compile
if (map.remove(userId) != null) {
    System.out.println("User was removed");
}

// After - use boolean return
if (map.remove(userId)) {
    System.out.println("User was removed");
}
```

**Migrating Async Operations**

Async operations with return values must be updated to use the new methods:

```java
// Before - will not compile
map.putAsync(key, value).thenAccept(previousValue -> {
    if (previousValue != null) {
        handleUpdate(previousValue);
    }
});

// After - use getAndPutAsync()
map.getAndPutAsync(key, value).thenAccept(previousValue -> {
    if (previousValue != null) {
        handleUpdate(previousValue);
    }
});
```

Async operations that ignore return values should update lambda parameters:

```java
// Before
map.putAsync(key, value).thenCompose(prev -> {
    return map.getAsync(key);
});

// After - use ignored parameter
map.putAsync(key, value).thenCompose(ignored -> {
    return map.getAsync(key);
});
```

The same migration pattern applies to `removeAsync()` and `getAndRemoveAsync()`.

### Changed Default Failure Handler

In this release, the default failure handler policy was changed to `stop`. Previously, a `noop` failure handler was used.

This change means that the failure will now stop the node if an error occurs instead of logging the error and continuing.

To continue operating using the `noop` handler, set it explicitly in [failure handler configuration](../../administrators-guide/config/node-config.md#failure-handler-configuration).

## New Features

### GridGain ML Inference Framework

This release introduces GridGain ML, an experimental module (preview) that brings machine learning inference directly to the database layer. Rather than exporting data to a separate model-serving service, you can deploy trained ML models to GridGain and run predictions where your data already lives.

GridGain ML provides a unified API for running inference against models built with PyTorch, TensorFlow, or ONNX, without requiring conversion or retraining. Models are packaged and deployed to the cluster as standard GridGain deployment units using the CLI or REST API.

Four prediction modes are available:

**Simple predictions** — Run inference on a single input, suitable for real-time scoring or validating model behavior.

**Batch predictions** — Submit multiple inputs in a single operation, for example scoring hundreds of customer profiles in one call.

**SQL-based predictions** — Execute inference directly against the results of a SQL query, so you can run a model over filtered table data without any additional data movement logic.

**Colocated predictions** — Process data on the specific cluster node where it is stored, fully eliminating network transfer for partition-local data.

All prediction modes also have asynchronous variants.

For more information about GridGain ML, see the [ML documentation section](../../developers-guide/machine-learning/gridgain-ml-quickstart.md).

#### Setup Requirements

GridGain ML uses Deep Java Library (DJL) as its runtime. The native engine libraries for PyTorch and TensorFlow are not bundled with the GridGain distribution and are automatically downloaded on the first inference.

**Air-gapped environments** — Use the official GridGain ML Docker image (`gridgain/gridgain9:<VERSION>-ml`), which ships with all engine libraries pre-loaded. For other options, see the GridGain ML documentation.

**Thread pool** — Configure the ML thread pool size in `gridgain-config.conf` before starting the node; a restart is required for changes to take effect.

#### Limitations

**SQL predictions** — Limited to a single column and a maximum of 5,000 rows.

**Colocated predictions** — Supports key-based inference for a single value column only.

### Improved Logging

### Partition Awareness for .NET Client

With this release, [.NET clients](../../developers-guide/clients/dotnet.md#partition-awareness) will benefit from partition awareness for SQL queries, significantly improving their performance.

### Transaction Labels

With this release, you can add labels when creating your transactions. This simplifies finding the specific transaction, and allows you to filter the `TRANSACTIONS` system view based on their labels.

```java
TransactionOptions options = new TransactionOptions()
    .label("order-checkout-user-12345");

try (Transaction tx = client.transactions().begin(options)) {
    // Perform transactional operations
    orderTable.recordView().insert(tx, orderRecord);
    inventoryTable.recordView().update(tx, inventoryRecord);

    tx.commit();
}
```

### Expanded Default Metrics

The following metrics are now enabled by default:

- `client.handler` - Client connection handling.
- `clock.service` - Clock service for distributed time management.
- `index.builder` - Index building and maintenance.
- `raft*` - All Raft consensus metrics (log replication, leader election, etc.).
- `sql.plan.cache` - SQL plan cache hit/miss rates and performance.
- `storage.aipersist` - Persistent storage I/O.
- `storage.aipersist.checkpoint` - Checkpoint frequency, duration, and performance.
- `thread.pools*` - All thread pool metrics.
- `topology*` - All topology-related metrics (local and cluster-wide).
- `transactions` - Transaction execution and coordination.

### New Metrics

This release continues to add new metrics to GridGain 9. The following metrics were added:

#### Log Storage Metrics

- `CmgLogStorageSize` - Bytes occupied on disk by the CMG (Cluster Management Group) log.
- `MetastorageLogStorageSize` - Bytes occupied on disk by the Metastorage group log.
- `PartitionsLogStorageSize` - Bytes occupied on disk by partition groups logs.
- `TotalLogStorageSize` - Total bytes occupied on disk by logs of all replication groups.

#### MessageService Metrics

- `messageHandlingFailures` - Total number of message handling failures.
- `messageRecipientNotFound` - Total number of message recipient resolution failures.
- `invokeTimeouts` - Total number of invocation timeouts.
- `slowResponses` - Total number of responses that took longer than 100ms to generate.

#### AIPersist IO Metrics

- `TotalBytesRead` - Cumulative bytes read from disk since startup.
- `TotalBytesWritten` - Cumulative bytes written to disk since startup.
- `ReadsTime` - Time spent in disk read operations (µs), as a histogram with buckets at 10µs, 100µs, 1ms, and 10ms.
- `WritesTime` - Time spent in disk write operations (µs), as a histogram with buckets at 10µs, 100µs, 1ms, and 10ms.

#### Data Center Replication Connector (DR Connector)  Metrics

{% hint style="info" %}
These metrics were added for [DR connector](../../migration-from-gg-8/dcr-from-gg8.md) only.
{% endhint %}

Per-cache metrics (`DrReceiverCacheMetricsMxBean`):

- `entriesAcked` - Number of successfully processed entries (current window).
- `bytesReceived` - Bytes received from replication source (current window).

Global metrics (`DrReceiverMxBean`):

- `totalEntriesAcked` - Total number of successfully processed entries since startup.
- `totalBatchesAcked` - Total number of successfully processed batches since startup.
- `totalBatchesFailed` - Total number of failed batch processing attempts since startup.
- `totalBytesReceived` - Total bytes received from replication source since startup.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-30234 | General | LogPushExporter changes are applied to DEB/RPM packages. |
| IGN-30230 | General | Fixed retries of transaction cleanup. |
| IGN-30215 | General | Added Unknown error group to Java and .NET clients to report new error groups added by future versions of the clients. |
| IGN-30223 | General | Fixed bug in .NET client feature decoding for large feature codes. |
| IGN-30217 | General | The --profile option was added to CLI config commands. |
| IGN-30205 | General | Fixed TxIdMismatchException after write intent resolution. |
| IGN-30190 | Cluster Metrics & Monitoring | LogPushExporter now exports logs to files. |
| IGN-30184 | General | Fixed unintentional "IGN-STORAGE-1 Index not built yet" error on a secondary index after it's built. |
| IGN-30156 | General | Added support for Spring Data 4. |
| IGN-30154 | Cluster SQL Engine | Added support for IF NOT EXISTS keyword for ALTER TABLE COLUMN ADD and IF EXISTS keyword for ALTER TABLE COLUMN DROP. |
| IGN-30114 | General | Transaction rollback is no longer blocked by waiting for pending locks. |
| IGN-30098 | General | Mappers now support inherited fields. |
| IGN-30094 | Code Deployment | Fixed deploying zip files containing folders different in case only on case-insensitive filesystems. |
| IGN-30085 | Platforms & Clients | Fixed a bug that caused decimal precision to be ignored by Table Views in some cases. |
| IGN-30068 | General | Optimized heap space consumption on unstable cluster topology. |
| IGN-29964 | Cluster SQL Engine | Fixed column type validation when reading a tuple value in the embedded java client. |
| IGN-29856 | General | Fixed an issue that could lead to an exception when a raft group majority is lost. |
| IGN-29724 | Cluster Metrics & Monitoring | Added MessageService metrics. |
| IGN-29700 | Cluster Storage Engine | Added IO metrics for aipersist storage engine. |
| IGN-29343 | General | You can now set transaction labels. |
| IGN-29271 | Distributed Computing | It's now possible to deploy jar files that do not have .jar extension. |
| IGN-29189 | Platforms & Clients | .NET: Added SQL partition awareness, which sends some SQL queries directly to the node which holds the relevant data. New IgniteClientConfiguration.SqlPartitionAwarenessMetadataCacheSize property controls the cache size for those queries. |
| IGN-28683 | Platforms & Clients | Python DB API Driver: Implemented heartbeats. |
| IGN-28512 | General | Added metrics for log storage sizes. |
| IGN-28278 | General | Reduced the amount of raft messages printed to log. |
| IGN-28272 | Platforms & Clients | .NET: Added ContainsAllKeys to table views. |
| IGN-28184 | Cluster REST API | Added events for monitoring REST requests. |
| IGN-26948 | CLI Tool | Verbose mode is now supported for the sql command in CLI tool. |
| IGN-26925 | CLI Tool | Improved help messages in CLI tool. |
| IGN-25753 | Cluster REST API | Uninitialized cluster now correctly returns 404 on REST endpoints. |
| IGN-23765 | General | The 'stop' failure handler policy is now used by default. |
| GG-47306 | Cluster Continuous Queries | Continuous Query: fixed possible reentrant Subscriber.onNext calls when subscriber delegates to SubmissionPublisher. |
| GG-47245 | Builds and Deliveries | Renamed CLI logs from ignite.log to gridgain.log. Added gridgain9db-metrics logs. |
| GG-47208 | Cluster Storage Engine | Fixed the known issue with DCR stopping early. |
| GG-47125 | Cluster Data Replication | You can now filter what tables to include in DCR based on schema. |
| GG-47124 | Cluster Continuous Queries | Continuous Query: fixed long polling response delay with explicit transactions. |
| GG-47101 | Cluster SQL Engine | Added new metrics for DR connector. |
| GG-47023 | Cluster Data Replication | DCR now uses long polling CQ if flush point is not set when replication is started. |
| GG-46960 | Cluster Continuous Queries | .NET: Continuous Query: added long polling to reduce latency and round trips on slow-moving tables. Configurable with ContinuousQueryOptions.LongPollingWaitTime. |
| GG-46899 | Cluster Storage Engine | The TABLES system view now includes secondary storage information. |
| GG-46066 | General | Unified Map structure public API to be similar to Table API. |
| GG-45951 | Cluster Storage Engine | Expired data is now removed by individual transactions, fixing a possible deadlock. |
| GG-45286 | General | GG8 CDC sink now uses Deployment API classloading infrastructure instead of custom classloader. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`, `9.1.17`, `9.1.18`

{% hint style="warning" %}
When performing a rolling upgrade from GridGain 9.1.8 or 9.1.9, it is required to update to 9.1.10 first.
{% endhint %}

When updating from older versions, we recommend updating to version `9.1.8` first, before performing an update to current version.

## Known Limitations

### Rolling Upgrade Over 9.1.10

When performing a rolling upgrade from GridGain 9.1.9 or earlier, it is necessary to first upgrade to 9.1.10 before upgrading to 9.1.11 or a later version. This is caused by improvements in rolling upgrade procedure that make skipping 9.1.10 with a rolling upgrade impossible.

The upgrade to 9.1.10 must be performed for the whole cluster and committed before the next upgrade can be started.

You do not need to perform this intermediary upgrade when upgrading with downtime, as it only affects the rolling upgrade procedure.

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
