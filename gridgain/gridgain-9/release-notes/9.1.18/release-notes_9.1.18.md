---
description: >-
  GridGain 9.1.18 brings major monitoring improvements, an improved CLI tool
  experience, and a reworked transaction API. It also documents known issues
  with data center replication and SQL performance in this release.
---

# GridGain 9.1.18 Release Notes

## Overview

GridGain 9.1.18 is a private release that brings major monitoring improvements, improved CLI tool experience and reworked transaction API.

## Known Issues

### Data Center Replication Stops Early

In this release, data center replication (DCR) between GridGain 9 clusters may unexpectedly stop on large data sets.

It is recommended to avoid using DCR in this release. If you are already using DCR, avoid using this version.

Clusters that do not have DCR configured are not affected, and it is safe to update to GridGain 9.1.18.

This issue will be fixed in an upcoming release.

### Inconsistent SQL Performance

This release features a significant change in how SQL engine handles complex queries. While the overall performance is significantly improved, especially on smaller datasets, some queries perform noticeably worse.

It is recommended to check your query performance before updating to this version, and delay the update if they perform worse.

This issue will be fixed in an upcoming release.

## Major Changes

### Transaction API Changes

{% hint style="warning" %}
Due to the changes to the transaction API, code changes will be required to compile your applications that use `IgniteSql.execute()` or `IgniteSql.executeAsync()` methods. Existing applications will continue to function and can connect to GridGain 9.1.18 clusters. See the [Code Migration](#code-migration) section below for details on required code changes.
{% endhint %}

Starting with this release, the methods in `RecordView`, `KeyValueView`, and `IgniteSql` no longer require passing a `null` transaction parameter when no transaction is needed. For more details please refer to the [SDK documentation](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/package-summary.html).

#### Deprecated Methods

The following methods have been deprecated and will not be supported in future releases:

**KeyValueView**

- `remove(Transaction, K, V)` - use `removeExact(Transaction, K, V)` instead;
- `removeAsync(Transaction, K, V)` - use `removeExactAsync(Transaction, K, V)` instead;
- `replace(Transaction, K, V, V)` - use `replaceExact(Transaction, K, V, V)` instead;
- `replaceAsync(Transaction, K, V, V)` - use `replaceExactAsync(Transaction, K, V, V)` instead.

**RecordView**

- `replace(Transaction, R, R)` - use `replaceExact(Transaction, R, R)` instead;
- `replaceAsync(Transaction, R, R)` - use `replaceExactAsync(Transaction, R, R)` instead.

#### New Methods

New overloads allow you to use `IgniteSql`, `KeyValueView` and `RecordView` API without passing unnecessary parameters. For example, before this API update you used `RecordView.getAsync(@Nullable Transaction tx, R keyRec)` and now you can just pass the key if transaction is not explicitly needed:

```java
CompletableFuture<R> rec = view.getAsync(R keyRec);
```

```java
KeyValueView.replace(K, V, V);
```

Same applies to `IgniteSql`:

```java
igniteSql.execute(query, arg0, arg1);
```

#### Code Migration

All `IgniteSql.execute()` and `IgniteSql.executeAsync()` methods that previously accepted `null` as a `Transaction` argument will no longer compile due to ambiguity introduced by the new overloads.

For example, the following method call will throw an error during compilation:

```java
igniteSql.execute(null, query, arg0, arg1);
```

To ensure your applications compiles correctly, modify your source code in one of the following ways:

- Either remove the `null` transaction argument and use the new overload:

  ```java
  igniteSql.execute(query, arg0, arg1);
  ```
- Or explicitly cast `null` to a `Transaction` type:

  ```java
  igniteSql.execute((Transaction) null, query, arg0, arg1);
  ```

The same applies to `IgniteSql.executeAsync()` calls.

## New Features

### Liveness and Readiness Probes

This release adds new REST `/health/liveness` and `/health/readiness` endpoints that can be used for monitoring cluster readiness.

- Liveness endpoint checks if the GridGain node has started.
- Readiness endpoint checks if the GridGain node has joined the cluster and is ready to receive data.

It is recommended to update your Kubernetes deployments to include liveness and readiness probes. The configuration extract below shows how to configure probes with recommended parameters:

```yaml
livenessProbe:
  failureThreshold: 3
  httpGet:
    path: /health/liveness
    port: 10300
    scheme: HTTP
  initialDelaySeconds: 5
  periodSeconds: 30
  successThreshold: 1
  timeoutSeconds: 10
readinessProbe:
  failureThreshold: 3
  httpGet:
    path: /health/readiness
    port: 10300
    scheme: HTTP
  initialDelaySeconds: 30
  periodSeconds: 10
  successThreshold: 1
  timeoutSeconds: 10
```

### Custom Transformations for DCR Connector

With this release, a new API was added for the [DCR Connector](../../migration-from-gg-8/dcr-from-gg8.md) that can be used for complex data mapping.

With it, instead of mapping GridGain 8 fields to GridGain 9 columns you can create a transformer class, and add it to the connector.

- The example below shows how you can set up a transformer in your code:

  ```java
  public class StringifyTransformerFactory {

      // This class must exist with this specific name.
      public static EntryTransformer create() {
          return (keyReader, valueReader) -> {
              // Read key fields and convert to strings
              Tuple key = Tuple.create();
              for (String fieldName : keyReader.fieldNames()) {
                  Object fieldValue = keyReader.readField(fieldName);
                  key.set(fieldName, String.valueOf(fieldValue));
              }

              // Handle deletions - valueReader is null for removed entries
              if (valueReader == null) {
                  return Result.remove(key);
              }

              // Read value fields and convert to strings
              Tuple value = Tuple.create();
              for (String fieldName : valueReader.fieldNames()) {
                  Object fieldValue = valueReader.readField(fieldName);
                  value.set(fieldName, String.valueOf(fieldValue));
              }

              return Result.upsert(key, value);
          };
      }
  }
  ```
- Then, package the class to a `.jar` file, and make it available to the DR connector:
  - For local installations, add the jar file to classpath (by default, the `libs` directory);
  - For Docker installations, mount the directory with the jar file, and use the new `EXTRA_CLASSPATH` environment variable to add the directory to the classpath in the container. The example below shows how you can start a docker container with a custom jar:

    ```bash
    docker run -p {host_port}:{inbound_port} \
      -v /host_config_path:/opt/gridgain-dr-connector/etc/custom \
      -v /host_libs_directory:/opt/custom-libs \
      -e EXTRA_CLASSPATH=/opt/custom-libs \
      gridgain/gridgain-dr-connector:9.1.18 \
      --config-path /opt/gridgain-dr-connector/etc/custom/config.conf
    ```
- Then, configure the mapping in the DCR connector's configuration to use the transformer:

  ```
  dr-service-config = {
    cacheMapping = [
      {
        cache = "cacheName"
        table = "tableName"
        transformerFactoryClassName = "com.example.MyTransformerFactory"
      }
    ]
  }
  ```

  {% hint style="info" %}
  You cannot mix mapping via transformer with direct mapping. Make sure all of your fields are mapped correctly.
  {% endhint %}

For more information about transformer configuration, see [DCR Connector](../../migration-from-gg-8/dcr-from-gg8.md) documentation.

### Improved CLI Tool Usability

This release significantly improves the CLI tool usability in interactive mode, bringing a number of features aiming to improve day-to-day experience:

- CLI tool now supports code highlighting for configuration.
- Four different themes that can now be used to better match CLI style to your environment:
  - `solarized-dark` - Default theme, aiming for readability on dark backgrounds.
  - `dark` - High-contrast theme for dark backgrounds. Same as the theme used previously.
  - `solarized-light` - Alternative theme, aiming for readability on light backgrounds.
  - `light` - Dark colors theme for light backgrounds.
- Long CLI tool outputs are now returned in pager format.
- Wide CLI tool outputs are now adjusted to console width if possible.

New configuration properties were added to control this behavior:

- The `ignite.cli.color-scheme` configuration to select the theme. `solarized-dark` by default;
- The `ignite.cli.pager.enabled` configuration to enable pager behavior. `true` by default on UNIX machines, `false` on others.
- The `ignite.cli.pager.command` configuration determines the command used for pager. `less -RFX` by default on UNIX machines, `more` on others.
- The `ignite.cli.sql.display-page-size` configuration determines the number of rows fetched per page. 1000 by default.

You can change these properties from the CLI tool with the `cli config set` command, for example:

```bash
cli config set ignite.cli.color-scheme=solarized-light
```

### Expanded Metrics

This release adds a large number of metrics. For more information about working with metrics, see [Metrics Configuration](../../administrators-guide/metrics/configuring-metrics.md) documentation.

#### Cache Metrics

A number of new metrics were added for monitoring cache operations. The following `caches.<cacheName>` metrics were added:

- `Hits` - Number of cache hits (key found in cache).
- `HitPercentage` - Percentage of successful cache hits.
- `Misses` - Number of cache misses (key not found in cache).
- `MissPercentage` - Percentage of cache misses.
- `Gets` - Total number of get operations.
- `Puts` - Total number of put operations.
- `Removals` - Total number of removal operations.

#### Page Memory Metrics

New metrics are available for monitoring page memory I/O and cache performance:

- `PagesRead` - Number of pages read from disk since last restart.
- `PagesWritten` - Number of pages written to disk since last restart.
- `PageCacheHits` - Number of times a page was found in the page cache.
- `PageCacheMisses` - Number of times a page had to be loaded from disk.
- `PageReplacements` - Number of times a page was evicted from cache.
- `PageAcquireTime` - Distribution of page acquisition time in nanoseconds (with bounds: 1µs, 100µs, 10ms, 100ms).
- `LoadedPages` - Current number of pages loaded in memory.
- `DirtyPages` - Current number of dirty pages in memory.
- `UsedCheckpointBufferPages` - Number of currently used pages in checkpoint buffer.
- `MaxCheckpointBufferPages` - The capacity of checkpoint buffer in pages.
- `MaxSize` - Maximum in-memory region size in bytes.

#### Transaction Write Intents Metric

A new `PendingWriteIntents` metric is available for monitoring unresolved write intents across all transactions.

#### Raft Leadership Metric

A new `groups.localLeadersCount` metric is available for monitoring raft group leadership distribution.

### Extended Transaction Information

Transaction labels are now included when transactions are referenced in [system views](../../administrators-guide/metrics/system-views.md) and logs.

### Long Polling for Continuous Queries

This release introduces the `longPollingWaitTimeMs` property for Continuous Queries. It defines how long the server waits for new events before returning an empty response. Configure it via `ContinuousQueryOptions.longPollingWaitTimeMs()` and use it together with `pollIntervalMs` to balance latency and throughput.

```java
var options = ContinuousQueryOptions.builder()
  .pollIntervalMs(10)
  .longPollingWaitTimeMs(3000)
  .pageSize(pageSize)
  .skipOldEntries(false)
  .build();
```

### Performance Improvements

### Low Latency Continuous Queries

This release significantly reduces [continuous query](../../developers-guide/continuous-queries.md) latency with the following improvements:

- Long polling, configurable with [`ContinuousQueryOptions.longPollingWaitTimeMs`](../../developers-guide/continuous-queries.md#continuous-query-parameters), immediately delivers new events when the table was previously idle;
- Parallel partition polling removes event delivery delays caused by other partitions;
- Active transactions no longer delay event delivery.

### Correlated SQL Subqueries

This release improves performance of correlated SQL queries by automatically converting them into join-based execution plans. Queries that use `EXISTS`, `NOT EXISTS`, and `IN/ANY` clauses with correlation will execute much faster, especially for large datasets.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-30122 | General | Fixed incorrect estimated size for aipersist tables. |
| IGN-30116 | General | Expected exceptions are no longer logged on connection attempt. |
| IGN-30073 | CLI Tool | Added theme configuration for CLI tool. |
| IGN-30072 | General | Extended log coverage for Placement Driver mechanism to track some edge cases during its recovery. |
| IGN-30054 | Platforms and Clients | .NET: Added predefined mappers for simple types, so that reflection and runtime codegen are not required for things like table.GetRecordView<long>() and table.GetKeyValueView<Guid, string>(). |
| IGN-30053 | General | Optimized read-only sql requests. |
| IGN-30052 | General | Fixed an issue where a critical system error was triggered when a command observed an unexpected but legitimate state change. |
| IGN-30051 | Cluster SQL Engine | Fixed an issue that caused queries to return result with duplicated rows when LEFT JOIN is performed. |
| IGN-30041 | Cluster Storage Engine | Fixed occasional data storage corruption after data rebalance in cases when partitions contained unfinished transactions. |
| IGN-30030 | Cluster SQL Engine | Fixed an issue where the result of a SELECT COUNT(*) query could be incorrect when it was followed by a DML statement modifying the same table within the same SQL script. |
| IGN-30024 | General | Increased DNS name resolution timeout when using StaticNodeFinder and made it configurable |
| IGN-30008 | General | Fixed a bug where placement driver metrics were not updated during placement driver unavailability. |
| IGN-29990 | Cluster Storage Engine | Fixed occasional partition corruption when a transaction is aborted. |
| IGN-29980 | Platforms and Clients | Java client: fixed lingering daemon thread when using mvn install exec:java `-Dexec.cleanupDaemonThreads=true` . |
| IGN-29969 | General | Fixed client transactions issue when an update could not be applied in some scenarios. |
| IGN-29950 | General | Fixed StackOverflow exception during transaction cleanup process. |
| IGN-29927 | CLI Tool | Improved rendering of lists in CLI tool. |
| IGN-29901 | CLI Tool | Added --recursive option for subdirectories deployment. |
| IGN-29884 | Platforms and Clients | Java client: Fixed circular exception chain in connection errors. |
| IGN-29870 | General | Columns in CLI tool input now adjust to terminal size. |
| IGN-29869 | General | Long CLI tool output is now returned in page format. |
| IGN-29857 | General | Added raft group metrics. |
| IGN-29855 | General | Extended metrics information printed to logs. |
| IGN-29701 | Cluster Storage Engine | Added new metrics for aipersist/aimem storage. |
| IGN-29695 | Cluster REST API | Added liveness and readiness probe endpoints for k8s. |
| IGN-29693 | Distributed Computing | Code deployment now validates deployed code for duplicate files. |
| IGN-29606 | Platforms and Clients | Added `IPartition.Id`, replaced `IPartitionManager` with `IPartitionDistribution`, added `GetPartitionsAsync()` and `GetPrimaryReplicasAsync(IClusterNode node)`. |
| IGN-29542 | Cluster REST API | Added inspect command that can be used to check files in the deployment unit. |
| IGN-29521 | Platforms and Clients | Java client: Fixed partition awareness connection failure handling. |
| IGN-29519 | Cluster Storage Engine | Added a metric for unresolved write intents. |
| IGN-29342 | General | Added transaction labels to transactions system view. |
| IGN-29341 | General | Transaction-related log messages now include transaction labels. |
| IGN-28572 | Cluster SQL Engine | Trailing zeroes now preserved when converting TIME/TIMESTAMP values to VARCHAR. |
| IGN-28047 | Distributed Computing | Fixed potential causality issues when executing compute jobs: now it is guaranteed that the compute job sees the changes made by the client before submitting that job. |
| IGN-27736 | General | Added no-transaction overloads to `IgniteSql`, `RecordView`, `KeyValueView`. |
| IGN-27357 | CLI Tool | CLI tool now supports profiles in interactive mode. |
| IGN-26312 | Platforms and Clients | .NET: Added full expiration support to IgniteDistributedCache: absolute, sliding, relative to now. |
| IGN-24700 | General | Node excluded from logical topology will now be stopped by failure handler if it re-enters the cluster after its segmentation. |
| IGN-24412 | SQL | Significantly improved performance of correlated sub-queries. |
| GG-47062 | General | Fixed incorrect org.apache.ignite.cache.Cache#load* behavior on cache stores with a small number of entries. |
| GG-46950 | Cluster Storage Engine | You can now configure polling in Near Cache. |
| GG-46876 | Cluster Continuous Queries | .NET: Continuous Query: reduced latency with concurrent partition polling. |
| GG-46863 | Cluster Continuous Queries | Continuous Query: reduced latency with concurrent partition polling. |
| GG-46848 | Cluster Continuous Queries | Improved CQ latency by removing the wait for active transactions. |
| GG-46807 | General | Added license attributions into GridGain deliveries. |
| GG-46700 | Cluster Continuous Queries | Continuous Query: reduced latency when current demand is 0 and Subscription.request is called. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`, `9.1.17`

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
