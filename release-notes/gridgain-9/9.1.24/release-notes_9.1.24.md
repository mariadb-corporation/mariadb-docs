---
description: >-
  GridGain 9.1.24 adds leaseholder balancing and improves the .NET cluster API.
  It also extends SQL system views, improves SQL planning and transaction
  handling, and fixes a number of issues across the SQL engine, thin clients,
  and continuous queries.
---

# GridGain 9.1.24 Release Notes

## Overview

GridGain 9.1.24 adds leaseholder balancing and improves .NET cluster API. It also extends SQL system views, improves SQL planning and transaction handling, and fixes a number of issues across the SQL engine, thin clients, and continuous queries.

## Major Changes

### JitPack Repository No Longer Required

GridGain no longer depends on artifacts published on JitPack. The dependency that previously required the `jitpack.io` repository (see the [9.1.21 release notes](../9.1.21/release-notes_9.1.21.md)) is now served from the GridGain Maven repository.

It is recommended to remove `jitpack.io` dependency from your `pom.xml` to keep your configuration clean. If not updated, GridGain will automatically switch to the new source, and leave an unnecessary dependency in configuration.

## New Features

### .NET Compute Executor Runtime Configuration

The new `ignite.compute.dotnet` node-configuration section lets you tune the .NET runtime of the compute executor (sidecar) process. You can toggle Server GC and cap the executor's memory with an absolute or percentage-based GC heap hard limit.

```javascript
ignite.compute.dotnet {
    serverGc = true               // enable .NET Server GC (default: true)
    gcHeapHardLimit = "512m"      // absolute GC heap hard limit; "" means no limit (default)
    gcHeapHardLimitPercent = 0    // GC heap hard limit as a percent of physical memory, 1-100; 0 means no limit (default)
}
```

See [.NET Compute Executor](../../developers-guide/compute/compute.md#configuring-the-net-compute-executor) for more information.

### .NET Client: Cluster API

The .NET client adds the `IIgnite.Cluster` API, which exposes the cluster topology. Use `Cluster.GetNodesAsync()` to retrieve all nodes in the logical topology, and `Cluster.LocalNode` to get the hosting node from inside a compute job or data streamer receiver (it returns `null` on the client side). The previous `IIgnite.GetClusterNodesAsync()` method is now deprecated in favor of `Cluster.GetNodesAsync()`.

```csharp
// From the client: list all nodes in the cluster.
IList<IClusterNode> nodes = await client.Cluster.GetNodesAsync();

// Inside a compute job: the node that runs the job.
IClusterNode? local = context.Ignite.Cluster.LocalNode;
```

See [Cluster API](../../developers-guide/clients/dotnet.md#cluster-api) for more information.

### CLI Command to Balance Leaseholders

GridGain 9 now lets you manually rebalance primary replica leaseholders across cluster nodes. The new `distribution balance-leases` CLI command tells the placement driver to redistribute leaseholders evenly - one leaseholder per replication group - forcing the move to a less-loaded node.

```bash
distribution balance-leases
```

See [CLI tool documentation](../../ignite-cli-tool.md#distribution-commands).

### Idempotent Cluster Initialization

The `cluster init` CLI command now accepts two optional flags that make it safe to re-run from scripts and automation. Use `--if-needed` to skip initialization and exit with code 0 when the cluster is already initialized instead of failing. Add `--if-nodes=<N>` (which requires `--if-needed`) to also defer initialization until at least N nodes are visible in the physical topology.

```bash
cluster init --name=myCluster --license=/path/to/license --if-needed --if-nodes=3
```

See [CLI tool documentation](../../ignite-cli-tool.md#cluster-init).

### Data Streamer and Continuous Query Cooperation

The data streamer can now control how same-key updates within a single batch are surfaced to continuous queries. The new `DataStreamerOptions.sameKeyUpdateMode` option takes a `DataStreamerSameKeyUpdateMode` value: `SQUASH` (default) conflates multiple updates to the same key within a batch into a single continuous query event for better performance, while `PRESERVE` splits the batch so that each update produces a separate continuous query event.

```java
var options = DataStreamerOptions.builder()
    .sameKeyUpdateMode(DataStreamerSameKeyUpdateMode.PRESERVE)
    .build();
```

See [same-key update mode](../../developers-guide/data-streamer.md#same-key-update-mode) and [continuous query events](../../developers-guide/continuous-queries.md#how-events-are-generated) for more information.

### Schema-Qualified Objects in SQL GRANT/REVOKE

SQL `GRANT`/`REVOKE PRIVILEGES ... ON <object>` now accepts a schema-qualified object name. A schema-qualified name such as `PUBLIC.MY_TABLE` grants the privilege on that single object, while a bare name such as `PUBLIC` still targets the whole schema. This lets you scope object-level privileges - for example, `CREATE_INDEX` on a specific table - directly from SQL.

```sql
GRANT PRIVILEGES CREATE_INDEX ON PUBLIC.MY_TABLE TO role1;
```

See [GRANT](../../sql-reference/access-control.md#grant-to-role) for details.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-49319 | General | Fixed a low-watermark leak that stalled MVCC garbage collection when an SQL cursor was left open on a read-only transaction. |
| GG-49316 | Platforms & Clients | C++ client: fixed a number of potential deadlocks. |
| GG-49234 | General | Added leaseholder balancing and a corresponding CLI command. |
| GG-49174 | Cluster SQL Engine | GridGain now always uses an index scan instead of a table scan when search boundaries are specified. |
| GG-49153 | Platforms & Clients | Fixed a NullPointerException in the .NET compute executor in non-standard deployments (fat JAR). Added the `ignite.compute.dotnet.executorPath` configuration property. |
| GG-49134 | CLI Tool | Removed the "Restart the node to apply changes" message when updating node configuration via the CLI. |
| GG-49126 | Builds and Deliveries | Updated netty-codec-http from version 4.2.12 to version 4.2.13. |
| GG-49039 | Cluster Security | SQL GRANT/REVOKE PRIVILEGES now accepts schema-qualified object names. |
| GG-49033 | Cluster Storage Engine | Fixed a bug that could break an index after a partition was rebalanced to another node. |
| GG-48933 | Cluster SQL Engine | The SQL_QUERIES system view now includes information about query retries. |
| GG-48880 | General | Added a new error code (IGN-TX-21) reported when the scope of user operations in a transaction is too large. |
| GG-48782 | Platforms & Clients | Fixed the thin client causality token getting stuck in the past in certain scenarios, causing stale reads. |
| GG-48696 | Cluster SQL Engine | Fixed a memory leak in QueryCancel when a query is retried multiple times. |
| GG-48691 | Distributed Computing | Added a compute executor configuration section to adjust .NET runtime settings, such as the GC heap limit. |
| GG-48690 | Platforms & Clients | .NET: added the IIgnite.Cluster API with LocalNode and GetNodesAsync(); deprecated IIgnite.GetClusterNodesAsync(). |
| GG-48663 | Platforms & Clients | C++ client: fixed a possible crash on client shutdown. |
| GG-48627 | Cluster SQL Engine | Fixed the VIEW_NAME column value in the SYSTEM_VIEW_COLUMNS system view. |
| GG-48604 | Platforms & Clients | .NET: fixed pooled buffer cleanup. |
| GG-48588 | Cluster SQL Engine | Added the collation attribute to EXPLAIN output for the Exchange node. |
| GG-48549 | Platforms & Clients | Added SQLRecoverableException for SQL operations. |
| GG-48469 | General | A transaction failure reason is no longer lost on rollback due to timeout; finishReason and code are now added to cleanup messages. |
| GG-48459 | Cluster Continuous Queries | Continuous Query: fixed event loss on node join. |
| GG-48346 | Platforms & Clients | Corrected JDBC metadata flag values to reflect the actual behavior of the connector. |
| GG-48304 | General | Client transaction load no longer hangs under high contention in SQL scenarios. |
| GG-48201 | Cluster Metrics & Monitoring | Added direct buffer metrics. |
| GG-47788 | General | Fixed a memory leak in Raft. |
| GG-47737 | Cluster SQL Engine | Added the DEFAULT_VALUE column to the TABLE_COLUMNS system view. |
| GG-47636 | Platforms & Clients | C++ client: fixed continuous query duplicate events when the enable_empty_batches option is enabled. |
| GG-46610 | CLI Tool | Added the --if-needed and --if-nodes=<N> flags for cluster initialization. |
| GG-46148 | Platforms & Clients | Added DataStreamerOptions.sameKeyUpdateMode with SQUASH (default, existing behavior) and PRESERVE modes. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`, `9.1.17`, `9.1.18`, `9.1.19`, `9.1.20`, `9.1.21`, `9.1.22`, `9.1.23`

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
