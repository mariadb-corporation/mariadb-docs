---
description: >-
  GridGain 9.0.6 is a stability and performance release that adds a license
  metrics exporter.
---

# GridGain 9.0.6 Release Notes

## Overview

GridGain 9.0.6 is a release dedicated to stability and performance.

## New Features

### License Metrics

In this release, a new `license` metrics exporter was added. You can use it to check the details of the current license.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-25466 | General | Linux and Windows environment files are now consistent. |
| IGN-25409 | General | Lease duration is now configurable in cluster configuration. |
| IGN-25362 | Cluster Storage Engine | Improved stability of transactions that are run in parallel. |
| IGN-25351 | SQL | SQL AVG function now returns DECIMAL data type for exact numeric types and DOUBLE data type for approximate numeric types. |
| IGN-24870 | CLI Tool | Improved SQL script results processing in CLI tool. |
| IGN-24056 | Platforms and Clients | .NET: Fixed decimal cast precision loss in LINQ. |
| GG-40548 | Cluster SQL Engine | Updated awssdk to version 2.25.21. |
| GG-40530 | CLI Tool | You can now specify several source cluster addresses for DCR. |
| GG-40434 | Cluster Data Snapshots and Recovery | Fixed an issue with restoring indexes when snapshot is restored. |
| GG-39823 | Licenses | Added metrics for licenses. |
| GG-39752 | CLI Tool | COPY INTO command now properly handles invalid parameters. |

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
- Write-Behind Caching

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
