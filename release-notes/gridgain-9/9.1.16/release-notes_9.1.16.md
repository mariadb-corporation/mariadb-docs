---
description: >-
  GridGain 9.1.16 brings a large number of new features, including a reworked
  JDBC driver, Java records support, custom object mapping in .NET, and new
  configuration options and metrics.
---

# GridGain 9.1.16 Release Notes

## Overview

GridGain 9.1.16 is a private release that brings a large number of new features, including reworked JDBC driver and record support in Java.

## Major Changes

### New JDBC Driver Implementation

This release includes a complete rework of the [JDBC driver](../../developers-guide/clients/jdbc-driver.md). The new driver provides improved reliability, better connection management, support for connection pools and enhanced batch processing capabilities.

The example below shows how you can connect to multiple endpoints:

```java
Connection conn = DriverManager.getConnection(
  "jdbc:ignite:thin://192.168.1.10:10800,192.168.1.11:10800,192.168.1.12:10800"
);
```

Additionally, the JDBC configuration was expanded with `backgroundReconnectInterval` and `partitionAwarenessCacheSize` properties, and units of measurement were added to `connectionTimeoutMillis` and `queryTimeoutSeconds` properties.

The previous JDBC driver is now deprecated and support for it will be removed in a later release. Make sure to migrate to the new JDBC driver.

## New Features

### Java Records Support

You can now use Java records to work with GridGain tables. The example below shows how you can create a simple record:

```java
public record Person(
    @Column("id") Integer id,
    @Column("name") String name,
    @Column("age") Integer age
) {}
```

For more information about using records, see [Record API documentation](../../developers-guide/table-api.md).

### Custom Object Mapping in .NET

This release adds interfaces for custom row mapping in .NET thin client. You can use them for complex mapping scenarios or when reflection is limited (Native AOT).

The example below shows how to use reflection-free mapping:

```csharp
public class PocoMapper : IMapper<Poco>
{
    public void Write(Poco obj, ref RowWriter rowWriter, IMapperSchema schema)
    {
        rowWriter.WriteLong(obj.Key);
        if (schema.Columns.Count > 1)
        {
            rowWriter.WriteString(obj.Val);
        }
    }
    public Poco Read(ref RowReader rowReader, IMapperSchema schema)
    {
        return new Poco
        {
            Key = rowReader.ReadLong()!.Value,
            Val = schema.Columns.Count > 1 ? rowReader.ReadString() : null
        };
    }
}
```

For more information about using improved mapping, see [.NET client documentation](../../developers-guide/clients/dotnet.md).

### Improved Configuration

In this release, cluster configuration is extended with a number of new configurations:

- `ignite.sql.statementMemoryQuota` and `ignite.sql.offloadingEnabled` parameters can now be used to fine-tune SQL memory usage.
- `ignite.sql.statistics.autoRefresh.staleRowsCheckIntervalSeconds` parameter can be used to fine-tune how often GridGain checks for stale rows.

### Distribution Zones Reset

With the release, a new distribution zones data nodes reset command was added to the CLI tool. You can use this command to force the cluster to recalculate data nodes for given zones immediately. GridGain will ignore given zones' scale up and down timers. Data nodes reset will check the state of cluster topology and will trigger partition rebalance if required.

```bash
zone datanodes reset --zone-names=ZONE_NAME_1,ZONE_NAME_2
```

### C++ Client Request Timeouts

C++ client now supports request timeouts. By default, request timeout is set to 0 (no timeout).

```cpp
ignite_client_configuration cfg{"127.0.0.1"};
cfg.set_operation_timeout(std::chrono::seconds{2});
auto client = ignite_client::start(cfg, std::chrono::seconds(5));
```

For more information, see [C++ client documentation](../../developers-guide/clients/cpp.md).

### ODBC Connection Heartbeats

You can now configure heartbeats in [ODBC driver](../../developers-guide/sql/odbc/odbc-driver.md) connection string with the `HEARTBEAT_INTERVAL` parameter. By default, heartbeat messages are sent every 30 seconds.

### String Configuration Support

When starting the node in [embedded mode](../../quick-start/embedded-mode.md), you can now provide configuration in string format. Previously, it was required to provide configuration as a path to the file.

For example:

```java
Path myWorkDir = Path.of("/home/gridgain");

IgniteServer node = IgniteServer.start("node", "{"ignite":{"network":{"port":3344,"nodeFinder":{"netClusterNodes":["localhost:3344"]}}}}", myWorkDir);
```

### Index Build Metrics

New metrics are available for monitoring secondary index building progress. The following `index.builder` metrics were added:

- `TotalIndexesBuilding` - Total number of indexes the node is currently building.
- `IndexesReadingStorage` - Number of indexes that are currently reading data from storage.
- `IndexesWaitingForTransactions` - Number of indexes that are currently waiting for transactions to complete.
- `TransactionsWaitingFor` - Number of transactions that indexes are currently waiting for.
- `IndexesWaitingForReplica` - Number of indexes that are currently waiting for replica response.

### SQL Virtual Column for Partition Information

A new virtual column `__PARTITION_ID` is now available in SQL queries. This column allows you to query which partition data resides in, enabling better partition-aware application logic.

Example usage:

```sql
SELECT id, name, __PARTITION_ID FROM my_table;
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-29654 | Distributed Data Streamer | Java client: fixed column order mix-up in DataStreamer in KeyValueView when key columns are not in the beginning of the schema. |
| IGN-29643 | Cluster SQL Engine | Improved JDBC driver error message. |
| IGN-29629 | Cluster SQL Engine | Fixed a rare issue when node runs into corrupted state and becomes unable to process SQL queries. |
| IGN-29594 | Platforms & Clients | C++ client now correctly handles void return type in compute jobs. |
| IGN-29589 | Cluster Storage Engine | The zone recalculate CLI tool command was renamed to zone reset. |
| IGN-29586 | Cluster SQL Engine | Improved string representation of the query type field across events, system views, logs, and exception messages. |
| IGN-29568 | General | Fixed a bug that prevented metrics from being published via Prometheus. |
| IGN-29559 | Cluster SQL Engine | Renamed connectionTimeout to connectionTimeoutMillis and queryTimeout to queryTimeoutSeconds. Old names are temporarily supported. |
| IGN-29556 | General | Fixed failure handler being triggered when zone resources stop due to network errors. |
| IGN-29552 | CLI Tool | Fixed an error with syntax highlighting on Alpine Linux. |
| IGN-29538 | General | Improved handling of raft snapshots. |
| IGN-29466 | CLI Tool | Fixed a rare scenario when running sql in CLI tool caused an NPE. |
| IGN-29440 | Cluster SQL Engine | Fixed an issue causing queries to get stuck in registry after script containing multiple DDL statements is cancelled. |
| IGN-29435 | General | Fixed possible node crash on start. |
| IGN-29434 | CLI Tool | Fixed an illegal reflective access warning in CLI tool. |
| IGN-29427 | General | Fixed IndexOutOfBoundsException exception on reading failed tx operation acknowledgment. |
| IGN-29425 | General | Updated placement driver metrics. |
| IGN-29422 | Cluster SQL Engine | Improved SQL EXPLAIN statement clarity for searchBounds. |
| IGN-29401 | CLI Tool | CLI tool now waits for the node to join the cluster before executing commands. |
| IGN-29394 | Platforms & Clients | You can now configure timeout for operations in C++ client. |
| IGN-29388 | Cluster SQL Engine | Added sql.statistics.autoRefresh.staleRowsCheckIntervalSeconds cluster-wide configuration option. |
| IGN-29387 | General | Memory configuration is now printed to logs at startup. |
| IGN-29353 | Cluster SQL Engine | The system virtual column for SQL partition filtering has been renamed from __PART to __PARTITION_ID and its type upgraded from INT32 to INT64. The old name __PART is now deprecated. |
| IGN-29351 | Platforms & Clients | ODBC Driver: Implemented Heartbeats feature. |
| IGN-29350 | CLI Tool | Partition API now exposes id() method. Introduced new PartitionDistribution API. Deprecated PartitionManager API. |
| IGN-29347 | Cluster Storage Engine | Added secondary indexes build metrics. |
| IGN-29346 | Cluster Storage Engine | Enhanced log output during index builds. |
| IGN-29323 | General | Added support for Java records in the Mapper API. |
| IGN-29201 | Compute Engine | Improved error handling for CachedDeploymentUnits. |
| IGN-29185 | General | Fixed an issue that caused the node to crash on startup if it was restarted during full data rebalance. |
| IGN-29181 | Platforms & Clients | Reworked JDBC Driver. |
| IGN-28872 | General | Added REST endpoint for data node recalculation. |
| IGN-28807 | General | Fixed an issue with the odbc shared library loading on the old linux systems. |
| IGN-28785 | General | Added an ability to explicitly trigger dataNodes recalculation via CLI command. |
| IGN-28743 | General | Fixed a memory leak caused by netty buffers during code deployment. |
| IGN-28702 | General | Data node history is now compacted. |
| IGN-28689 | General | You can now provide node configuration as a string when starting node in embedded mode. |
| IGN-27992 | General | Fixed possible data loss with explicit transactions in aipersist engine. |
| IGN-22878 | General | .NET: Added custom object mapping to table view APIs with IMapper<T>. |
| GG-46406 | Cluster SQL Engine | SCHEMA DROP command now also takes sequences into account. |
| GG-46358 | Cluster SQL Engine | Improved error message for RBAC commands. |
| GG-46312 | CLI Tool | Syntax highlighting is now correctly disabled on unsupported platforms. |
| GG-46187 | Cluster Data Snapshots and Recovery | Fixed encrypted snapshot resource leak. |
| GG-46073 | Cluster SQL Engine | Added memoryQuotaBlockSize cluster-wide sql configuration parameter that controls the reservation block size for a memory quota tracker. |
| GG-45913 | GridGain Integrations | Kafka sink: log error on client disconnect. |
| GG-45572 | Cluster SQL Engine | Improved marshaller error messages. |
| GG-45487 | Cluster Storage Engine | Fixed an issue where it will not be possible to get partition state if partition's engine is not present on one of the nodes. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`

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
