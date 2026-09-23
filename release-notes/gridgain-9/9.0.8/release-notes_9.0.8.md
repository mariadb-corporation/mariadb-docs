---
description: >-
  GridGain 9.0.8 changes BigDecimal type derivation and adds cache write-behind
  mode, system property configuration, and snapshot storage path configuration.
---

# GridGain 9.0.8 Release Notes

## Overview

GridGain 9.0.8 is a release that continues work on stability and performance while also bringing new and exciting features.

## Major Changes

### Changed BigDecimal Type Derivation

When handling `BigDecimal` data type, previously GridGain derived it as `DECIMAL(MAX_PRECISION, 0)`. Starting with this release, `BigDecimal` will be derived as `DECIMAL(28, 6)`. If there are more than 6 digits after the decimal point, they will be dropped.  If a value larger than precision is passed, out of range exception will occur.

To store larger decimal values, cast them with custom precision, for example `CAST(? as DECIMAL(100, 50))`.

## New Features

### Cache Write-Behind Mode

When using the caches as [external storage](../../developers-guide/cache.md#caches-as-external-storage), you can now choose the write mode to better fit your needs.

- If `SYNC` write mode is used, KeyValueView operations will wait until the cache store write is complete.
- If `ASYNC` write mode is used, data will be propagated in the background. The operations will proceed before the write to the external storage is completed.

For more information on using caches, see [Caches as External Storage](../../developers-guide/cache.md#caches-as-external-storage).

### Configuration for System Properties

You can now specify system properties in GridGain configuration instead of applying them system-wide. For example:

```bash
node config update ignite.system.cmgPath:etc/cmg
```

### Snapshot Storage Path Configuration

You can now specify the storage path for created snapshots in cluster configuration. If absolute path if provided, snapshots will be created in subdirectory with the node's name. If a relative path is provided, a subdirectory in node's `work` directory will be used.

Here is how you can update snapshots path:

```bash
cluster config update ignite.snapshot.snapshotsPath=newfolder
```

### Automatic Object Serialization

With this release, POJOs in compute jobs are automatically serialized to tuples. If custom serialization is configured for the object, it will be used instead.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-25840 | General | Added new configuration options for system properties. |
| IGN-25683 | SQL | Fixed an issue with COALESCE operator detecting a wrong data type if first argument is NULL. |
| IGN-25679 | SQL | Fixed an issue with CHAR comparison returning incorrect result. |
| IGN-25672 | General | .NET: Added BigDecimal type to support full range of values that Ignite can handle. |
| IGN-25650 | General | Fixed an issue that could stop the node from joining cluster after multiple consecutive restarts. |
| IGN-25598 | CLI Tool | Node URL can now include a trailing slash. |
| IGN-25586 | General | Client messages are now handled in the partition-operation thread. |
| IGN-25518 | SQL | SQL queries now take table size into account when planning execution. |
| IGN-25502 | SQL | Rules for type derivation of specific parameters were changed. |
| IGN-25422 | General | Nested Java objects are now automatically serialized when using Compute API. |
| IGN-25152 | General | Public error code numbers updated to keep numbers continuous. |
| IGN-25150 | General | A new STORAGE_BROKEN error code was added. |
| GG-40542 | Cluster Data Snapshots and Recovery | You can now configure snapshots storage path. |
| GG-40504 | Cluster Affinity and Baseline Topology | Decreased the number of rebalanced replicas on distribution zone scale up and scale down. |
| GG-40406 | Cluster Storage Engine | You can now change cache replication behavior to write-behind. |

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
