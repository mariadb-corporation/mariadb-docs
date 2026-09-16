---
description: >-
  GridGain 9.0.12 adds high availability distribution zones, network backups,
  cancellation of queries, transactions and compute jobs, and cluster catalog
  pruning.
---

# GridGain 9.0.12 Release Notes

## Overview

GridGain 9.0.12 is a release that brings a large number of new features.

## New Features

### High Availability Distribution Zones

With this release, a new high availability mode was added to distribution zones. When this mode is enabled, GridGain prioritizes data availability. If a majority of data partitions are lost (for example, multiple nodes left the cluster), the cluster will continue to operate after a short delay, while assuming that all data on those nodes was lost. This may lead to data loss, but guarantees better cluster availability.

Distribution zone consistency mode must be set when zone is created and cannot be changed:

```sql
CREATE ZONE IF NOT EXISTS exampleZone WITH STORAGE_PROFILES='default', REPLICAS=3, CONSISTENCY_MODE='HIGH_AVAILABILITY'
```

### Network Backups

With this release, you can specify a destination where to store the snapshot, or restore the snapshot from a source at a specified destination. Destination configuration is cluster-wide, and can only be changed for the whole cluster, for example:

```bash
cluster config update ignite.snapshot.paths: {example:{uri:"file://snapshots", type: LOCAL, default: true}}
```

The destination can be defined as either `LOCAL` or `REMOTE`.

- LOCAL snapshots are not shared between nodes. Every node saves the snapshot metadata and all partition files.
- REMOTE snapshots save only one copy of snapshot metadata and partition files. The location where this copy is saved must be accessible by all nodes with the use of the same base URI.

Once a snapshot path is created, you can create a snapshot at the specified destination:

```bash
cluster snapshot create --type=full --tables=PERSON --destination=example
```

Then the snapshot can be restored from the same path by specifying it in the restore command:

```bash
cluster snapshot restore --id=8eb10b48-6885-4922-a1af-c28d8473ba28 --source=relative-path-example
```

### Stopping SQL Queries, Transactions and Compute Jobs

This release provides the initial implementation of stopping running queries, transactions and compute jobs. GridGain 9 approaches the problem from two sides:

- On embedded nodes, you can use the `CancelHandle` object to get cancel tokens and pass them to your queries and jobs. Then, you can cancel all jobs linked to the same `CancelHandle`, for example:

  ```java
  CancelHandle cancelHandle = CancelHandle.create();
  CancellationToken cancelToken = cancelHandle.token();

  ignite.sql().execute(null, cancelToken, "CREATE TABLE IF NOT EXISTS Person (id int primary key, name varchar, age int);");

  CompletableFuture<Void> cancelled = cancelHandle.cancelAsync();
  ```

- When managing the cluster, you can use the recently added [system views](../../administrators-guide/metrics/system-views.md) to get information about individual operations and cancel them with the `KILL QUERY`, `KILL TRANSACTION`, or `KILL COMPUTE` commands.

Support for stopping queries from client code will be added in one of the upcoming releases.

### Cluster Catalog Pruning

GridGain 9 stores cluster metainformation in the cluster catalog. Prior to this release, there was no mechanism for safely removing data from the catalog, which meant it would eventually grow in size and could cause issues. With this release, data that is considered safe to delete will be removed from the catalog when low watermark changes, preventing its growth beyond a certain size.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-26518 | CLI Tool | SQL execution errors are now correctly reported in CLI tool. |
| IGN-26488 | Platforms and Clients | .NET: Fixed "java.time.DateTimeException: Invalid ID for region-based ZoneId" on SQL query due to OS-dependent default zone ID. |
| IGN-26448 | Platforms and Clients | Client metrics can now be accessed by Java monitoring tools. |
| IGN-26419 | CLI Tool | CLI tool now checks if path to configuration file is provided in the config command. |
| IGN-26401 | General | Added a IGNITE_LOG_THROTTLE_INTERVAL_MS JVM property to configure log throttle interval. |
| IGN-26353 | General | Changed the way node attributes and system properties are represented in the configuration. |
| IGN-26259 | General | Node is now stopped gracefully when the process is terminated. |
| IGN-26230 | Platforms and Clients | Java thin: removed legacy reconnectThrottlingPeriod and reconnectThrottlingRetries config properties. Use RetryPolicy instead. |
| IGN-25799 | General | Accelerated rollback abandoned transactions on a lock conflict with another transaction. |
| IGN-25517 | Distributed Computing | Added Collection<Tuple> support as a Compute job argument and result. |
| GG-41601 | CLI Tool | Fixed an issue preventing failed DCR replication from being stopped. |
| GG-41583 | Cluster Data Snapshots and Recovery | Snapshots now lock low watermark until data is no longer required. |
| GG-41543 | GridGain Integrations | Kafka sink: added configurable temporal types handling. |
| GG-41535 | CLI Tool | Improved error message when invalid data center replication is created. |
| GG-41271 | Cluster Data Snapshots and Recovery | Snapshot start time field now correctly reports when the operation was started. |

## Known Limitations

### Delay on DDL Requests

DDL requests, such as `CREATE TABLE`, take a few seconds each to complete. Because of that, large database initialization scripts may take longer than expected. This will be addressed in an upcoming release.

### Performance of GridGain 8 Applications

Some scenarios may see lower performance when moving to GridGain 9. This is a temporary limitation, and the performance in these scenarios will be improved in upcoming versions.

### High-Availability with Two Data Copies

When a partition loses majority of its copies, it becomes unavailable. This behavior is required for split-brain protection. Because of this, in a distribution zone with 2 data replicas, losing one node may lead to partial unavailability.

To achieve both split-brain protection and full availability with one node down, use 3 or more replicas.

Upcoming versions will add a high-availability mode that support full availability with one node down when using 2 replicas.

### Data Center Replication with Multiple Data Centers

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming release.

### GridGain 8 Features

The following features of GridGain 8 are not available in this version, and will be added in upcoming versions:

- Rack-Awareness
- SQL Offloading
- Tracing
- Service Grid

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
