---
description: >-
  GridGain 9.1.23 adds disk-usage write protection, C++ client partition
  awareness, server-side continuous query filters, compute job cancellation
  tokens, and new metrics for storage, thread pools, and the Raft log.
---

# GridGain 9.1.23 Release Notes

## Overview

GridGain 9.1.23 adds disk-usage write protection, partition awareness in the C++ client, server-side filters for continuous queries, and cancellation tokens for compute jobs. It also adds memory quota block size in JDBC and .NET, local snapshot listing in the CLI, .NET 10 support in the compute executor, and new metrics for storage, thread pools, and the Raft log.

## Major Changes

### Log File Rollover Preserves Files Across Restarts

The default `java.util.logging` configuration now sets the `FileHandler.append` property to `true`. As a result, a node restart no longer triggers a log generation rollover. The pre-restart log stays in the current generation. Rollover now happens only when a file reaches the size limit (`100 MB` for the server log, `10 MB` for the CLI log by default).

If you parse logs by generation number, update your scripts to account for changed behavior.

## New Features

### Storage Drive Usage Limits

To protect a node from running out of disk space, GridGain 9.1.23 introduces hard drive-usage limits on both the Raft log and the partitions data directories. When usage on the local drive exceeds the configured limit - or when a quorum-breaking subset of a partition's peers report the same - incoming client writes for affected partitions are rejected with `StorageFullException` exception until usage drops back below the limit.

By default, the limits are set to `Long.MAX_VALUE`, effectively disabling them. You can reduce the limits in the node configuration:

```javascript
ignite.raft.logStorage {
    hardPartitionsLogDriveUsageLimitBytes = 9223372036854775807
    hardPartitionsDataDriveUsageLimitBytes = 9223372036854775807
}
```

See [hard disk usage limits](../../administrators-guide/config/node-config.md#hard-disk-usage-limits) for details.

### Raft Log Storage Size Limits

GridGain 9.1.23 introduces configurable soft limits on the size of Raft log storage. When the size of the persistent partitions' log files (or the volatile partitions' spillout files) exceeds its soft limit, the node triggers Raft snapshots on the affected nodes to truncate logs and reclaim disk space. These limits keep log growth bounded without rejecting client work.

You can configure soft limits in node configuration:

```javascript
ignite.raft.logStorage {
    softPartitionsLogSizeLimitBytes = 21474836470
    softPartitionsLogSpilloutSizeLimitBytes = 21474836470
}
```

See [soft disk usage limits](../../administrators-guide/config/node-config.md#soft-disk-usage-limits) for details.

### C++ Client: Partition Awareness

The C++ client now supports partition-aware routing for single-record operations. When enabled, the client computes the target partition for each key locally and routes the request directly to the primary node, avoiding an extra network hop for misrouted requests.

The example below shows how you can configure your requests to use partition awareness:

```cpp
auto preferred = ignite::detail::make_typed_preferred_node_fn(
    table_impl, key_tuple);

auto value = table.get(transaction, key_tuple, preferred).get();
```

For more information, see [C++ client documentation](../../developers-guide/clients/cpp.md).

### Partition-Operation Backpressure

A new cluster configuration [option](../../administrators-guide/config/cluster-config.md#replication-configuration) limits the percentage of node heap memory that the partition request-processing queue is allowed to occupy. When the limit is exceeded, the node stops admitting new partition operations until in-flight work drains, preventing a single hot node from accepting more requests than it can hold in memory.

```javascript
ignite.replication {
    partitionOperationHeapUsagePercent = 20   // default: 20 (percent of max JVM heap)
}
```

### Server-Side Remote Filter for Continuous Queries

Continuous queries can now filter events on the server side, reducing network traffic when subscribers are only interested in a subset of changes. The filter is evaluated before events leave the source node.

**Java.** Set a `Criteria`-based filter on `ContinuousQueryOptions` and reference event values through three virtual table names - `CUR`, `OLD`, and `EVENT`:

```java
var options = ContinuousQueryOptions.builder()
    .remoteFilter(Criteria.and(
        Criteria.columnValue("EVENT", "TYPE_ID",
            Criteria.equalTo(TableRowEventType.UPDATED.id())),
        Criteria.columnValue("CUR", "STATUS", Criteria.equalTo("active")),
        Criteria.columnValue("OLD", "PRICE", Criteria.greaterThan(300))))
    .build();

view.queryContinuously(subscriber, options);
```

In addition to user columns, the `EVENT` pseudo-table exposes `PARTITION_ID` (`BIGINT`), `TYPE_ID` (`INT`: `0=CREATED, 1=UPDATED, 2=REMOVED, 3=ARCHIVED`), and `COMMIT_TIMESTAMP` (`BIGINT` Unix-time milliseconds).

**.NET.** Two new `QueryContinuouslyAsync` overloads expose the same filter - one taking a SQL string with positional parameters, and one taking a typed LINQ expression that is translated to SQL on the client:

```csharp
// SQL form
await foreach (var batch in view.QueryContinuouslyAsync(
    "CUR.PRICE > ? AND EVENT.TYPE_ID = ?",
    [300, (int)TableRowEventType.Updated]))
{
    // process batch
}

// LINQ form
await foreach (var batch in view.QueryContinuouslyAsync(
    x => x.Entry.Value.Price > 300))
{
    // process batch
}
```

The LINQ overload is not available in AOT-compiled .NET builds; use the SQL form there.

See [remote filter](../../developers-guide/continuous-queries.md#remote-filter) in the continuous queries documentation.

### Support for Listing Local Snapshot Paths

The `snapshot list` CLI command can now list the locally stored snapshots. Each node reports the snapshots it holds locally and the results are aggregated for display.

See [CLI tool documentation](../../ignite-cli-tool.md#cluster-snapshot-list).

### Compute Job Cancellation Token

The compute API now exposes the cancellation token to running jobs. Jobs can now obtain the same `CancellationToken` that triggers their cancellation and forward it to APIs that accept one. For example, you can propagate cancellation to SQL statements:

```java
public class MyJob implements ComputeJob<MyArg, MyResult> {
    @Override
    public CompletableFuture<MyResult> executeAsync(JobExecutionContext ctx, MyArg arg) {
        return ctx.ignite().sql().executeAsync(
                null,
                ctx.cancellationToken(),  // propagates job cancel to SQL
                "SELECT ...");
    }
}
```

See [propagating cancellation from a job](../../developers-guide/compute/compute.md#propagating-cancellation-from-a-job) for more information.

### Memory Quota Block Size for JDBC and .NET

The `memoryQuotaBlockSize` option introduced for the Java client in 9.1.22 is now available in JDBC and .NET clients. Setting a larger block size reduces synchronization overhead with the node-level memory tracker for memory-intensive queries.

#### JDBC

The option is exposed on `IgniteJdbcStatement`:

```java
IgniteJdbcStatement stmt = conn.createStatement().unwrap(IgniteJdbcStatement.class);
stmt.setMemoryQuotaBlockSize(1_048_576L);  // 1 MB blocks
```

#### .NET.

A nullable `MemoryQuotaBlockSize` init-only property is exposed on `SqlStatement`:

```csharp
var stmt = new SqlStatement("SELECT * FROM large_table")
{
    MemoryQuotaBlockSize = 1_048_576L  // 1 MB blocks
};
```

In both clients, the default is `null` (use the node-level setting). Negative values are rejected. See [memory quota block size](../../developers-guide/sql/sql-api.md#memory-quota-block-size) for more information.

### New Metrics

This release adds three new metrics groups for storage, thread-pool, and Raft-log observability. The following metrics were added:

- [Storage consistency](../../administrators-guide/metrics/metrics-list.md#storage-aipersist-consistency) (`storage.aipersist.consistency`):
  - `RunConsistentlyDuration` - the time spent in `runConsistently` closures, in nanoseconds.
  - `RunConsistentlyStarted` - the total number of `runConsistently` invocations started.
  - `RunConsistentlyActiveCount` - current number of active `runConsistently` calls.
- [Striped thread-pool aggregated metrics](../../administrators-guide/metrics/metrics-list.md#thread-pools-thread-pool-executor-name):
  - `ConcurrencyLevel` - number of stripes in the executor.
  - `ActiveCount` - approximate total number of threads currently executing tasks across all stripes.
  - `IdleCount` - approximate number of idle threads across all stripes.
  - `QueueSize` - current total size of the execution queue across all stripes.
- [Raft log storage](../../administrators-guide/metrics/metrics-list.md#raft):
  - `PartitionsLogStorageSpilloutSize` - the number of bytes occupied on disk by the spillout of volatile-zone partition-group logs.

### .NET 10 Support in Compute Executor

With this release, the .NET compute job executor supports .NET 10, so a server node can host .NET compute jobs on either runtime. See [.NET compute jobs](../../developers-guide/compute/compute.md#net-compute-jobs) for more information.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-30807 | General | Fixed a rare network connection issue. |
| IGN-30800 | Cluster SQL Engine | Added table-scope for SQL hints. Added support for hints' overriding. |
| IGN-30795 | General | Reduced the amount of logs generated when a transaction is handled while a node is stopping. |
| IGN-30791 | General | Fixed connection errors when a cluster node restarts. |
| IGN-30787 | Cluster Metrics & Monitoring | Removed PageAcquireTime metric. |
| IGN-30767 | Cluster SQL Engine | Fixed an issue preventing partition pruning to apply on predicates over dynamic parameters of temporal types. |
| IGN-30721 | Platforms & Clients | Java client: fixed race condition and potential data corruption when decoding large responses. |
| IGN-30704 | General | Fixed non-legitimate "Lease update invocation failed because of outdated lease data" exceptions on leases prolongations causing leases interruptions. |
| IGN-30657 | Distributed Computing | Future returned from a compute job is not automatically canceled to allow normal completion even if a cancellation was requested. |
| IGN-30626 | Platforms & Clients | Client connector: fixed correctness and performance of stack trace reporting in sendServerExceptionStackTraceToClient=true mode. |
| IGN-30622 | Platforms & Clients | Fixed negative TransactionsActive metric for direct transactions. |
| IGN-30619 | Platforms & Clients | Java and .NET clients: never retry authentication errors. |
| IGN-30446 | Cluster Storage Engine | Added new storage consistency metrics. |
| IGN-30425 | Cluster SQL Engine | Fixed client observable timestamp skew in multistatement query cases. |
| IGN-30328 | Platforms & Clients | Java client: reduced verbosity of error stack traces. |
| IGN-30282 | Platforms & Clients | Java client: fixed piggyback transaction rollback. |
| IGN-30197 | Distributed Computing | Added a callback for cancellation API. |
| IGN-30196 | Distributed Computing | Cancellation token is passed to the job execution context to allow streamlined usage of other APIs that take it as an argument. |
| IGN-28683 | Platforms & Clients | Python DB API Driver: Implemented heartbeats. |
| IGN-28412 | General | REST API tags for disaster recovery and system disaster recovery were fixed. |
| IGN-28155 | General | Improved latency for transactions which span multiple partitions |
| IGN-24461 | Platforms & Clients | C++ client: Added support for partition awareness. |
| GG-48879 | General | Fixed a race in low watermark logic. |
| GG-48796 | General | Fixed a possible garbage-collected timestamp in outdated read-only transactions and improved related logging. |
| GG-48759 | Platforms & Clients | Added .NET 10 support to the compute executor. |
| GG-48744 | Platforms & Clients | Fixed .NET runtime version in -dotnet10 Docker images. |
| GG-48657 | Cluster SQL Engine | Fixed an issue causing duplicate rows to be returned when a HASH index is used in query processing. |
| GG-48612 | Cluster SQL Engine | Fixed an issue executing a correlated subquery with the SORT operator. |
| GG-48536 | Cluster SQL Engine | Fixed an issue where queries utilizing the sort aggregate could fail with "AssertionError: Input not sorted". |
| GG-48449 | Cluster SQL Engine | Fixes issue with virtual columns in correlated subqueries. |
| GG-48444 | CLI Tool | Fixed cluster unit deploy ignoring authentication credentials from the CLI secret config file. |
| GG-48421 | Cluster SQL Engine | Fixed an issue with executing a correlated subquery with the LIMIT operator. |
| GG-48378 | Cluster Security | Fixed error that happened when calling Tables API from another thread in the compute job. |
| GG-48351 | Configuration | Added hardLogSizeLimitBytes configuration. |
| GG-48349 | Cluster Metrics & Monitoring | Added raft.log.storage.PartitionsLogStorageSpilloutSize metric. |
| GG-48325 | Distributed Computing | Fixed IgniteCluster.nodesAsync() to return the logical topology (matching nodes()) instead of physical topology, so nodes that have left the cluster or not yet fully joined are no longer included. |
| GG-48294 | Platforms & Clients | C++ Client: Fixed a bug that was blocking GridGain from setting column value to nullptr explicitly. |
| GG-48284 | Builds and Deliveries | Update Spring Boot dependency from 3.5.13 to 3.5.14. |
| GG-48275 | Cluster Data Snapshots and Recovery | Fixed encrypted snapshot buffers allocation. |
| GG-48234 | Distributed Computing | .NET: Added IJobExecutionContext.LoggerFactory and IDataStreamerReceiverContext.LoggerFactory to write to the node log from .NET compute jobs and receivers. |
| GG-48232 | Platforms & Clients | Fixed race condition and improved performance of client message decoding on large payloads. |
| GG-48226 | General | Fixed possible data loss when a disk with Raft log is out of free space. |
| GG-48215 | Platforms & Clients | C++ Client: Added examples. |
| GG-48200 | Cluster Metrics & Monitoring | Added aggregated metrics for a striped thread pool. |
| GG-48193 | Platforms & Clients | Fixed an issue caused ReadOnly flag on JDBC Connection to be ignored. |
| GG-48179 | Cluster Data Replication | Fixed DCR error handling. |
| GG-48175 | Platforms & Clients | Thin clients: fixed potential update visibility issues on implicit tx retry. |
| GG-48167 | Platforms & Clients | Added reporting of multi-statement execution errors when the user closes a Statement without iterating through all results. |
| GG-48165 | Cluster Data Replication | DCR: deletes made on the source while replication was offline are now applied on the target after restart. |
| GG-48145 | Cluster Storage Engine | Fixed a rare partition corruption that occurred when primary replica is lagging or being restarted under load. |
| GG-48137 | General | Fixed an error when a node could not join the cluster after cluster rename. |
| GG-48109 | Configuration | Added new configuration option partitionOperationHeapUsagePercent that limits the percentage of node heap memory allocated for the user request processing queue, preventing a node from accepting too many operations and exhausting available memory. |
| GG-48091 | Builds and Deliveries | Log files now roll over only when the maximum file size is exceeded, and existing log files are preserved across restarts. |
| GG-48031 | Builds and Deliveries | Added Java 26 support to Docker images. |
| GG-47978 | Cluster SQL Engine | Improved warning for unsupported COPY INTO direction. |
| GG-47976 | Cluster SQL Engine | Fixed COPY INTO command allowing to bypass user permissions. |
| GG-47951 | Cluster Data Replication | Java client: fixed exception message on auth failure. |
| GG-47949 | Cluster Data Replication | DCR replications stuck in the replicating state are now recovered when worker node is restarted. |
| GG-47940 | General | Fixed a race where rolled-back transactions could block a partition by leaving behind a shared lock (S-lock). |
| GG-47934 | General | Implicit transactions can now be retried in case of unexpected retriable intercluster network issues |
| GG-47916 | CLI Tool | Improved UX when connecting to a node during the initialization process. |
| GG-47905 | Platforms & Clients | Java client: Fixed initial connection fail if retry policy is null and the first address is unavailable. |
| GG-47870 | Cluster Data Replication | DCR is now retried correctly if source cluster is not available. |
| GG-47866 | Cluster Data Snapshots and Recovery | Fixed data inconsistency when restoring snapshot on a zone with multiple replicas. |
| GG-47834 | Configuration | Old configurations are now properly migrated. |
| GG-47820 | Cluster Storage Engine | Metric PageAcquireTime is deprecated and will always have 0 value until removed. To be removed in 9.2. |
| GG-47810 | Configuration | Some configuration values from old versions are now properly migrated. |
| GG-47809 | Cluster SQL Engine | Added support for non-default schema in COPY FROM command. |
| GG-47807 | Cluster Security | RBAC: corrected username display to use the actual username instead of the display name. |
| GG-47805 | Platforms & Clients | Java client: fixed connection leak when client initialization fails. |
| GG-47787 | General | REST endpoints no longer return 409 while cluster is initializing. |
| GG-47747 | Cluster Continuous Queries | Added remote filter for continuous queries. |
| GG-47720 | Cluster Continuous Queries | Continuous Query: optimized long polling logic. |
| GG-47668 | Migration Tools | Ignore attribute is no longer skipped on key fields in cache mapping. |
| GG-47591 | Platforms & Clients | .NET: Added Statement.MemoryQuotaBlockSize. |
| GG-47580 | Platforms & Clients | Memory Quota Block Size option is now available in JDBC Statements. |
| GG-47578 | Cluster Storage Engine | Fixed rare index build failures when many indexes are created at the same time. |
| GG-47557 | Cluster Security | Optimized number of heap allocations in RBAC. |
| GG-47544 | CLI Tool | Improved user list command output. |
| GG-47543 | Cluster Security | Added support for ALTER USER SQL command. |
| GG-47541 | Cluster Storage Engine | GridGain now pauses client writes when configured storage size limits are exceeded. |
| GG-47539 | General | Added soft limits for log storage that trigger log storage compaction. |
| GG-47455 | Cluster Security | You can now specify multiple user attributes in LDAP. |
| GG-47384 | Cluster Data Snapshots and Recovery | Fixed error when expiration runs during snapshot restoration. |
| GG-47262 | Cluster Continuous Queries | .NET: Continuous Query: added overloads with `remoteFilter` - SQL expression and LINQ expression - to filter events on the server side. |
| GG-47141 | Platforms & Clients | Added JDBC driver property that permits running DDL statements in a session with active explicit transaction. |
| GG-47093 | Platforms & Clients | Implicit transactions with SQL will be retried in case primary replica expiration during the execution. |
| GG-46575 | CLI Tool | Added a new CLI command to list local snapshots. |
| GG-46396 | Builds and Deliveries | Added new docker images for GG9 based on amazoncorretto:17-al2023 and rockylinux:9. |
| GG-44871 | Cluster Continuous Queries | .NET: Added ContinuousQueryOptions.SkipOldEntries. |
| GG-44065 | Cluster Continuous Queries | Continuous Query: added remoteFilter option to filter events on the server side. |
| GG-38308 | Cluster Data Snapshots and Recovery | Missing schemas are now automatically created when restoring a snapshot |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`, `9.1.17`, `9.1.18`, `9.1.19`, `9.1.20`, `9.1.21`, `9.1.22`

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
