---
description: >-
  GridGain 9.1.11 adds a large number of new metrics and system views, query plan staleness configuration, and CDC failover.
---

# GridGain 9.1.11 Release Notes

## Overview

GridGain 9.1.11 is a private release that adds a large number of new metrics, as well as improved query staleness management and the ability to start a continuous query from transaction timestamp.

## New Features

### Extended Metrics and Monitoring

This release adds [new metrics](../../administrators-guide/metrics/metrics-list.md#storage-aipersist-checkpoint) for detailed checkpoint phase tracking. You can now also monitor total pages read and written to `aipersist` storage.

- `LastCheckpointBeforeLockDuration` - Time spent on pre-lock operations before the last checkpoint (ms).
- `LastCheckpointDuration` - Total duration of the last checkpoint (ms).
- `LastCheckpointFsyncDuration` - Time spent syncing data to disk during the last checkpoint (ms).
- `LastCheckpointLockHoldDuration` - Time the checkpoint lock was held (ms).
- `LastCheckpointLockWaitDuration` - Time spent waiting to acquire the checkpoint lock (ms).
- `LastCheckpointPagesWriteDuration` - Duration of the page write phase (ms).
- `LastCheckpointReplicatorLogSyncDuration` - Time spent syncing the replicator log (ms).
- `LastCheckpointSplitAndSortPagesDuration` - Duration of the split-and-sort dirty pages phase (ms).
- `LastCheckpointTotalPagesNumber` - Total number of pages written during the last checkpoint.
- `LastCheckpointWaitPageReplacementDuration` - Time spent waiting for page replacement (ms).
- `PagesRead` - Number of pages read from disk since the last restart.
- `PagesWritten` - Number of pages written to disk since the last restart.

A [new system view](../../administrators-guide/metrics/system-views.md#sql_cached_query_plans) has also been introduced to expose cached SQL query plans.

- `NODE_ID` - ID of the node where the plan is cached.
- `PLAN_ID` - Internal identifier of the prepared plan.
- `CATALOG_VERSION` - Catalog version used when the query was prepared.
- `QUERY_DEFAULT_SCHEMA` - Default schema applied during query preparation.
- `SQL` - Normalized SQL text of the query.
- `QUERY_TYPE` - Query type.
- `QUERY_PLAN` - Serialized or explain representation of the chosen query plan.
- `QUERY_PREPARE_TIME` - Time the plan was prepared on the node.

### Query Plan Staleness Configuration

With this release, you can configure how often the query plan for the table will be recalculated based on the number of updates. This is controlled by 2 new parameters:

- `min stale rows` parameter sets the minimum required number of updates to trigger replanning.
- `stale rows fraction` parameter sets the minimum fraction of the table that must be updated to trigger replanning.

Query plan will be recreated around the time the number of updates reaches the higher value. The timing depends on database load and is not guaranteed to happen immediately.

You can set these parameters when creating a table, or modify them with the ALTER TABLE DDL command.

The example below creates a table for which a plan is recalculated every time 1000 rows or 15% of the database is updated:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int PRIMARY KEY,
  city_id int,
  name varchar,
  age int,
  company varchar
) WITH (min stale rows 1000, stale rows fraction 0.15);
```

### Continuous Query Transaction Watermark

With this release, you can pass a read-only transaction to a continuous query to start it at exactly the transaction timestamp. This way, you can read the data from your cluster at a specific point in time, apply it and then start the continuous query at exactly the point in time you read the data. This approach ensures exactly once delivery of your data without accidental duplicates or missed updates.

```java
// Create a watermark at the transaction timestamp.
ContinuousQueryWatermark wm = ContinuousQueryWatermark.afterTransaction(tx);

// Pass the watermark to continuous query.
ContinuousQueryOptions options = ContinuousQueryOptions.builder().watermark(wm).build();

// Start the continuous query.
accounts.queryContinuously(subscriber, options);
```

For more information, see the [continuous query](../../developers-guide/continuous-queries.md) documentation.

### CDC Failover

With this release, [CDC](../../administrators-guide/change-data-capture/change-data-capture.md) will automatically switch to a different execution node from the list of execution nodes if the node it is currently running on exits the cluster. The CDC process will only be interrupted if no execution node is available.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-29072 | General | Non-colocated storage is now deprecated. This only affects clusters created in versions older than GridGain 9.1.4. |
| IGN-29024 | General | Fixed an issue that prevented updating storage profile configuration while the node is running. |
| IGN-29011 | General | Reduced the severity of a warning when a node tries to connect to itself. |
| IGN-28982 | General | Improved error message when embedded node is missing --add-opens. |
| IGN-28957 | Platforms and Clients | Improved error message when client attempts to connect to uninitialized cluster. |
| IGN-28933 | General | Added a TotalAllocatedSize metric. |
| IGN-28927 | General | Added data region metrics for aipersist storage. |
| IGN-28919 | Cluster Storage Engine | You can now specify a case-sensitive column name in an annotation by enclosing it in quotation marks. |
| IGN-28908 | General | Fixed an issue that prevented cluster from initializing right after the nodes come online. |
| IGN-28907 | General | You can now connect to secure clusters with Spring boot integration. |
| IGN-28903 | General | Added aipersist checkpoint metrics. |
| IGN-28814 | Cluster SQL Engine | You can now configure query plan statistics staleness for your tables. |
| IGN-28743 | Code Deployment | Fixed a memory leak caused by netty buffers during code deployment. |
| IGN-28510 | General | Added data region and data storage metrics. |
| IGN-28399 | Cluster SQL Engine | Cached query plans are now automatically replanned if data change is detected. |
| GG-45520 | Cluster Storage Engine | Updated RocksDB to version 10.2.1.2. |
| GG-45456 | Cluster Data Snapshots and Recovery | You can now choose to store maps and sequences in snapshots when configuring snapshots via REST. |
| GG-45441 | Cluster Storage Engine | Nodes will now not start if they contain profiles with secondary engine without a license that supports them. |
| GG-45356 | Cluster Security | Fixed wrong privilege requirement for select count statement. |
| GG-45022 | Distributed Computing | Wasm Compute: enabled Wasm to bytecode compilation. |
| GG-44260 | Cluster Continuous Queries | Continuous Query: added ContinuousQueryWatermark.afterTransaction to get a consistent view of existing table data and future updates. |
| GG-43853 | Platforms & Thin Clients | Python Client: Added support for Partition Awareness feature. |
| GG-42395 | Migration Tools | DDL generator and persistent data migration tools now account for SQL Schemas. |
| GG-39664 | Migration Tools | Migration tools now correctly handle field names overlapping in key and value fields. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`

{% hint style="warning" %}
When performing a rolling upgrade from GridGain 9.1.8 or 9.1.9, it is required to update to 9.1.10 first.
{% endhint %}

When updating from older versions, we recommend updating to version `9.1.8` first, before performing an update to current version.

## Known Limitations

### Nodes With Secondary Storage Cannot be Restarted

If a node that has a secondary storage zone configured for a table is restarted after a certain time period, it will not be able to start with a `Node is initialized with inconsistent log` error message. This issue does not affect nodes that do not use secondary storage.

If your node is affected this way, delete data from the persistent storage by deleting the `work` folder and restart the node.

This issue will be fixed in an upcoming release.

### Rolling Upgrade Over 9.1.10

When performing a rolling upgrade from GridGain 9.1.9 or earlier, it is necessary to first upgrade to 9.1.10 before upgrading to 9.1.11 or a later version. This is caused by improvements in rolling upgrade procedure that make skipping 9.1.10 with a rolling upgrade impossible.

The upgrade to 9.1.10 must be performed for the whole cluster and committed before the next upgrade can be started.

You do not need to perform this intermediary upgrade when upgrading with downtime, as it only affects the rolling upgrade procedure.

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
