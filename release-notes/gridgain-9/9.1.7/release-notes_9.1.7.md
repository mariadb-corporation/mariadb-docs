---
description: >-
  GridGain 9.1.7 improves cluster monitoring and migration tooling and adds Windows support for the C++ client.
---

# GridGain 9.1.7 Release Notes

## Overview

GridGain 9.1.7 is a release with multiple minor improvements, including better support for bootstrap implementations and extended cluster monitoring.

## Major Changes

### Extended Bootstrap Support

This release features extended backwards compatibility support for bootstrap configuration. You can now use docker compose files without providing explicit bootstrap file. This ensures compatibility with compose files created for all previous versions.

### Extended Critical Worker Timeouts

This release increases default timeout values for [critical workers](../../administrators-guide/config/node-config.md#system-configuration). The following values are changed:

- `ignite.system.criticalWorkers.livenessCheckIntervalMillis` changed from 200 to 2000 milliseconds,
- `ignite.system.criticalWorkers.maxAllowedLagMillis` changed from 500 to 5000 milliseconds,
- `ignite.system.criticalWorkers.nettyThreadsHeartbeatIntervalMillis` changed from 100 to 1000 milliseconds.

## New Features

### Improved Monitoring

This release features multiple improvements to cluster monitoring:

- New `ClockSkewExceedingMaxClockSkew` [metric](../../administrators-guide/metrics/metrics-list.md#clock-service) can be used to monitor clock drift.
- A set of new [compute events](../../developers-guide/events/events-list.md#compute-job-events) allows for easier monitoring of your distributed computing jobs.

### Improved Migration Tools

This release features major changes in migration tools:

- A new way of configuring mapping between caches and tables during [DCR from GridGain 8](../../migration-from-gg-8/dcr-from-gg8.md) was added. By using it, you can map key and value cache fields separately, as well as ignore the fields that are not required. The example below shows how you can configure mapping:
  ```
  dr-service-config = {
    cacheMapping = [
      {
        cache = "cacheName"
        table = "schemaName.tableName"
        keyFields = [
          { field = "K1", column = "COL_1" }
        ]
        valueFields = [
          { field = "K1", column = "COL_2" }
          { field = "V4", ignore = true }
        ]
      }
    ]
  }
  ```

- [Code adapter](../../migration-from-gg-8/codebase-migration.md) now supports migration of GridGain 8 ScanQueries.

### Windows Support for C++ Client

With this release, you can use the [C++ client](../../developers-guide/clients/cpp.md) on Windows systems with MSVC toolchain versions 2017, 2019 and 2022.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-28576 | General | Fixed a possible memory leak in event sink. |
| IGN-28535 | General | Increased default timeouts for critical workers. |
| IGN-28529 | Cluster SQL Engine | Improved the performance of SQL LEFT JOIN queries with non-equal predicates. |
| IGN-28527 | Cluster Storage Engine | Improved log information about possible thread blocking. |
| IGN-28452 | Cluster Storage Engine | Added a new metric for clock drift. |
| IGN-28451 | General | Warning is now printed to log when MAX_CLOCK_SKEW value is exceeded. |
| IGN-28447 | Distributed Computing | Added compute job events. |
| IGN-28284 | Cluster SQL Engine | Fixed output formatting for CAST AS VARCHAR FORMAT queries. |
| IGN-27447 | Platforms and Clients | Updated Netty from version 4.1.119.Final to version 4.2.4.Final. |
| GG-44820 | Cluster Storage Engine | BOOTSTRAP_NODE_CONFIG variable is no longer required to start GridGain via docker compose. |
| GG-44646 | Cluster Storage Engine | Updated RocksDB to version 10.2.1. |
| GG-44644 | Cluster SQL Engine | Added an ability to configure complex data mapping during data migration from GridGain 8. |
| GG-44631 | Cluster Storage Engine | Updated RocksDB to version 10.2.1. |
| GG-44330 | Cluster Data Snapshots and Recovery | Requesting a snapshot for a future timestamp now gets rejected. |
| GG-44067 | Cluster Continuous Queries | Added ContinuousQueryOptions.partitions option to query only certain partitions. |
| GG-43906 | Cluster Deployment | Added KEDA configuration to Helm chart. |
| GG-43854 | Platforms & Clients | Python Client: Introduced Heartbeats. |
| GG-43256 | Cluster Continuous Queries | C++: Added watermark API to the CQ event batches. Added options to process empty batches. |
| GG-39659 | Migration Tools | Added support for ScanQueries in GridGain 8 code adapter. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`, `9.1.1`, `9.1.2`, `9.1.3`, `9.1.4`, `9.1.5`, `9.1.6`

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
