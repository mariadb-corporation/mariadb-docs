---
description: >-
  GridGain 9.1.17 brings monitoring improvements and new .NET features, removes
  APIs and REST endpoints for table-based partitions, and notes a Control Center
  compatibility requirement.
---

# GridGain 9.1.17 Release Notes

## Overview

GridGain 9.1.17 is a private release that brings monitoring improvements and exciting new .NET features.

## Major Changes

### Removal of Table-Based Partitions

This release starts removing APIs and system views that were used for working with table-based partitions that are no longer supported since [GridGain 9.1.15](../9.1.15/release-notes_9.1.15.md#partition-colocation).

#### Removed System Views

In this release, the `GLOBAL_PARTITION_STATES` and `LOCAL_PARTITION_STATES` [system views](../../administrators-guide/metrics/system-views.md) were removed. Make sure to use the `GLOBAL_ZONE_PARTITION_STATES` and `LOCAL_ZONE_PARTITION_STATES` zone-based system views instead.

#### Removed REST Endpoints

In this release, table-based data recovery REST endpoints were removed.

- The `/management/v1/recovery/partitions/restartWithCleanup` is replaced by `/management/v1/recovery/zone/partitions/restartWithCleanup`,
- The `/management/v1/recovery/partitions/reset` is replaced by `/management/v1/recovery/zone/partitions/reset`,
- The `/management/v1/recovery/state/global` is replaced by `/management/v1/recovery/zone/state/global`,
- The `/management/v1/recovery/state/local` is replaced by `/management/v1/recovery/zone/state/local`,
- The `/management/v1/recovery/partitions/restart` is replaced by `/management/v1/recovery/zone/partitions/restart`.

If you were using the removed endpoints for monitoring and managing your partitions, make sure to switch to the new ones. As the new endpoints use zone-based partitions, all table-related fields are no longer applicable and have been removed. Make sure to modify your requests appropriately. For more information on the new request and response fields, see the [OpenAPI](https://www.gridgain.com/sdk/gridgain9/latest/openapi.html#tag/recovery) specification.

### Control Center Incompatibility

Due to the changes in the sections above, Control Center 2025.5 and earlier are not compatible with GridGain 9.1.17. The Control Center 2025.5.2 patch release addressed these compatibility issues.

If you are using Control Center to monitor your GridGain 9 cluster, upgrade your Control Center to version [2025.5.2](https://www.gridgain.com/docs/control-center/latest/release-notes/control-center/2025.5.2) and before updating to GridGain 9.1.17.

## New Features

### Timed SQL Requests

A new `--timed` option has been added to the CLI, and can be used to measure the execution time of SQL queries and other CLI commands. When enabled, the timing information includes the total execution time for the command. The timing information is displayed after the query results in the CLI.

Example usage:

```bash
sql --timed "select * from system.system_views;"
```

### Improved Snapshots Monitoring

A new `snapshot list` CLI command has been added to help administrators monitor and manage cluster snapshots. This command provides visibility into all available snapshots, including those stored on remote paths.

```bash
ignite3 snapshot list
```

### Expanded Metrics

This release adds new metrics to improve monitoring *aipersist* storage. The metrics cover [checkpoint](../../administrators-guide/metrics/metrics-list.md#storage-aipersist-checkpoint) behavior.

Another set of new metrics helps monitor [Raft snapshots](../../administrators-guide/metrics/metrics-list.md#raft) activity, providing better visibility into the snapshot lifecycle. These metrics help detect stalled replication, slow recovery and excessive snapshot load.

#### Storage Metrics

- Checkpoint Metrics
  - ReadLockAcquisitionTime – Time from requesting the checkpoint read lock until acquisition, in nanoseconds.
  - ReadLockHoldTime – Duration between checkpoint read lock acquisition and release, in nanoseconds.
  - ReadLockWaitingThreads – Current number of threads waiting for the checkpoint read lock.

#### Raft Snapshot Metrics

- IncomingSnapshots – Number of incoming Raft snapshots currently in progress.
- IncomingSnapshotsLoadingMeta – Number of incoming Raft snapshots loading metadata.
- IncomingSnapshotsWaitingCatalog – Number of incoming Raft snapshots waiting for catalog availability.
- IncomingSnapshotsPreparingStorages – Number of incoming Raft snapshots preparing storages.
- IncomingSnapshotsPreparingIndexForBuild – Number of incoming Raft snapshots preparing indexes for build.
- IncomingSnapshotsLoadingMvData – Number of incoming Raft snapshots loading multi-versioned data.
- IncomingSnapshotsLoadingTxMeta – Number of incoming Raft snapshots loading transaction metadata.
- OutgoingSnapshots – Number of outgoing Raft snapshots currently in progress.

### .NET Improvements

#### .NET Custom Mapping Support

This release introduces new `IMapper<T>` support to SQL, Compute and PartitionManager .NET APIs, enabling custom object mapping for serialization and deserialization, including AOT-friendly scenarios where reflection-based mapping is not suitable.

For example, that is how you use it to create a colocated [compute](../../developers-guide/compute/compute.md#running-net-compute-jobs) job target for a specific table and key:

```csharp
public sealed class PocoMapper : IMapper<Poco> {}
IJobTarget<Poco> target = JobTarget.Colocated("PUBLIC.MY_TABLE", key, new PocoMapper());
```

For more details on usage of `IMapper<T>` see corresponding [SQL](../../developers-guide/clients/dotnet.md#sql-api) and [Partition Manager](../../developers-guide/clients/dotnet.md#partition-management) API sections.

#### .NET Client AOT Compilation

This release adds official support for [Native AOT](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot). Applications using the .NET client can be compiled in AOT mode. Most client APIs are supported. Unsupported APIs (LINQ and reflection-based mappers) will produce trim warnings during build.

#### .NET Continuous Query API

Continuous Query .NET [API](../../developers-guide/continuous-queries.md#continuous-query-watermark) is extended with the new `IContinuousQueryWatermark.AfterTransaction` interface to allow the user to obtain a consistent view of table data and future updates.

This is how to start a continuous query with transaction watermark:

```csharp
var watermark = IContinuousQueryWatermark.AfterTransaction(tx);
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-29969 | General | Fixed client transactions issue when an update could not be applied in some scenarios. |
| IGN-29830 | General | Fixed a crash on start due to stored LWM falling behind compacted Catalog. |
| IGN-29805 | General | Added --timed option to CLI. |
| IGN-29780 | Platforms & Clients | .NET: Fix potentially inconsistent data seen by different client instances within one IgniteClientGroup. |
| IGN-29776 | Platforms & Clients | .NET: IgniteServiceCollectionExtensions.AddIgniteClientGroup now integrates with available logger by injecting ILoggerFactory automatically. |
| IGN-29756 | Platforms & Clients | C++ client compilation fixed for gcc-15 compiler. |
| IGN-29735 | CLI Tool | Added CLI-only Docker image. |
| IGN-29718 | Cluster REST API | Fixed resource leak in a rare scenario of deploying multiple files with wrong version format. |
| IGN-29708 | Cluster SQL Engine | Fixed an issue when wrong result is returned if result of aggregation is used in division. |
| IGN-29699 | Cluster Storage Engine | Added new metrics under "storage.<aipersist/aimem>.checkpoint" source. |
| IGN-29694 | Platforms & Clients | Fixed a rare deadlock in C++ client during compute job execution. |
| IGN-29688 | General | Fixed NPE if write intent switch happens after the table is already dropped. |
| IGN-29678 | Distributed Data Streamer | Thin clients (all): Fixed data streamer changes not being immediately visible. |
| IGN-29667 | Cluster Storage Engine | Fixed a potential deadlock on the invocation of "stop node" failure handler. |
| IGN-29664 | Cluster SQL Engine | Fixed an issue causing DML queries to fail when executing within explicit RW transaction. |
| IGN-29642 | CLI Tool | CLI tool maximum heap size is now limited to 256 Mb. |
| IGN-29639 | General | Fixed an issue that could lead to an error during the registration of table metrics when a node restarts. |
| IGN-29631 | General | Fixed command timestamp reordering in raft state machine on unstable group topology. |
| IGN-29621 | Platforms & Clients | .NET: Added custom object mapping to Compute, SQL, and PartitionManager APIs with IMapper<T>. |
| IGN-29599 | General | Multi node disaster recovery operations are completed when all participating nodes finish processing. |
| IGN-29596 | General | Fixed possible TxIdMismatchException in case of primary replica switch. |
| IGN-29541 | Cluster REST API | Added a new /management/v1/deployment/node/units/structure/{unitId}/{unitVersion} REST endpoint that can be used to fetch deployment unit file structure on the node. |
| IGN-29529 | Platforms & Clients | Java client: fixed reconnect to restarted node. |
| IGN-29499 | Platforms & Clients | Python DB API: Added support for Python 3.14 and removed support for Python 3.9. |
| IGN-29491 | Cluster Data Snapshots and Recovery | Added new metrics related to partition Raft snapshots. |
| IGN-29230 | Platforms & Clients | .NET: Improved hostname resolution logic. GridGain now re-resolve provides hostnames periodically to allow using DNS as node finder in orchestrator and other scenarios. |
| IGN-28745 | Cluster SQL Engine | Fixed the issue where ResultSetMetadata.indexOf failed when called for a case-sensitive column name. |
| IGN-28167 | Platforms & Clients | Fixed exceptions in the server log when cancelling SQL queries or compute jobs. |
| IGN-28148 | Cluster SQL Engine | Updated Apache Calcite to version 1.41. |
| IGN-27158 | Platforms and Clients | Java client: Improved exception handling and logging on server node disconnect. |
| IGN-26685 | General | Zone partitions are now correctly dropped after drop moment is below LWM. |
| IGN-25556 | General | Fixed service descriptor when deployment failed. |
| IGN-24449 | General | System Raft groups, like CMG and Metastorage, now do not share threads for their Log Managers disruptors. |
| IGN-23405 | Platforms and Clients | .NET: Added Native AOT support. |
| GG-46923 | General | Transaction timeout in the dr connector is now set to 30 seconds. |
| GG-46858 | General | Adds missing jvm flag to the start.sh script of the DR connector. |
| GG-46743 | General | Fixed expiration not working when a large number of entries expire. |
| GG-46805 | Platforms & Clients | Python Client: Fixed Windows wheels for Python versions other than 3.11. |
| GG-46718 | Cluster SQL Engine | Fixed getObject(column, class) to return null when a value was null instead of coercing it to 0.0. |
| GG-46715 | Cluster Continuous Queries | .NET: Added ContinuousQueryTransactionWatermark. |
| GG-46585 | Cluster SQL Engine | DR connector now displays GridGain version and system information. |
| GG-46584 | Platforms & Thin Clients | Fixed CQ failing to request next batch because of incorrect partition assignment state. |
| GG-46551 | Cluster Security | Tables API in compute jobs now returns nulls if table is not found. |
| GG-46400 | Cluster SQL Engine | DR connector no longer prints stacktrace at info level for marshaller errors. |
| GG-46310 | Cluster SQL Engine | Fixed incorrect type mapping from legacy temporal types to Java Time API in DR-connector component. |
| GG-46296 | Cluster Data Snapshots and Recovery | Added a new cli command to get a list of snapshots. |
| GG-46123 | Platforms & Thin Clients | Clients: Fixed a race condition, that could result in a sudden connection termination right after establishment. |
| GG-46096 | Cluster Continuous Queries | Fixed ContinuousQueryTransactionWatermark serialization. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`

{% hint style="warning" %}
When performing a rolling upgrade from GridGain 9.1.8 or 9.1.9, it is required to update to 9.1.10 first.
{% endhint %}

When updating from older versions, we recommend updating to version `9.1.8` first, before performing an update to current version.

### Client Compatibility

#### GridGain Clients

GridGain clients and servers are both backward and forward compatible. An older client can connect to a newer server, and a newer client can connect to an older server. As a result, clients and servers can be upgraded independently and in any order.

#### GridGain JDBC Driver

GridGain JDBC driver was reworked in GridGain 9.1.16. The new driver is only compatible with GridGain 9.1.16 or newer. Previously used JDBC driver is forwards-compatible with newer server, however it is deprecated and support for it will be removed in a later release.

#### Apache Ignite 3 Clients

Apache Ignite thin clients are not compatible with GridGain. When switching to GridGain, change the dependency to GridGain client as described in the [GridGain client documentation](../../developers-guide/clients/java.md).

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
