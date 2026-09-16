---
description: >-
  GridGain 9.0.11 adds high availability distribution zones alongside stability
  and performance improvements.
---

# GridGain 9.0.11 Release Notes

## Overview

GridGain 9.0.11 is a release that continues work on stability and performance while also bringing new and exciting features.

## New Features

### High Availability Zones

This release provides a way to configure consistency mode of distribution zones.

Previously, when losing the majority of nodes that hold data partitions for the distribution zone, the distribution zone would be switched into read-only mode to maintain strong data consistency and guarantee no data loss, as some changes could be only on the nodes that left the cluster.This behavior is now called `STRONG_CONSISTENCY`.

In this release, the `HIGH_AVAILABILITY` mode was added. If enabled, when losing the partition majority, the distribution zone will continue to operate normally. If updates happened on nodes that left the cluster, but were not fully propagated prior to them leaving, some data may be lost, but the cluster will continue operating normally.

You can only select the availability mode of the distribution zone during creation. It cannot be changed later. Below is the example of creating a high availability zone:

```sql
CREATE ZONE IF NOT EXISTS exampleZone WITH STORAGE_PROFILES='default', REPLICAS=3, CONSISTENCY_MODE='HIGH_AVAILABILITY'
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-26277 | General | CLI verbose mode is now more informative. |
| IGN-26276 | CLI Tool | Fixed an issue with cluster init command using a wrong configuration file when called repeatedly. |
| IGN-26255 | Platforms and Clients | SSL errors are now properly propagated to clients. |
| IGN-26164 | Distributed Computing | Fixed an issue with native compute job results deserialization. |
| IGN-26126 | Platforms and Clients | .NET: Fixed OverflowException in ErrorGroups.GetErrorCode. |
| IGN-25991 | Platforms and Clients | .NET: Added ServiceCollection extensions to simplify DI integration. |
| IGN-25796 | SQL | You can now cancel running SQL queries from JDBC. |
| IGN-25752 | General | Added decimalValue method. |
| IGN-25393 | General | Transactions from SQL operations are now properly retried on fail. |
| IGN-25371 | Platforms and Clients | .NET: Added Apache.Extensions.Caching.Ignite package with IDistributedCache implementation. |
| IGN-25080 | SQL | Updated calcite version to 1.38. |
| GG-41327 | GridGain Integrations | Added basic Kafka Source connector. |
| GG-41268 | Cluster Data Snapshots and Recovery | Snapshot commands performed via REST now correctly return 404 code when target is not found. |
| GG-41209 | Cluster Storage Engine | Calling "/partitions/reset" and "/partitions/restart" endpoints now require RESET_PARTITIONS and RESTART_PARTITIONS privileges accordingly. |

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
