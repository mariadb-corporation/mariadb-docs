---
description: >-
  GridGain 9.0.13 reworks the Compute API, disables fsync by default, and adds
  SQL memory offloading and partitioned compute jobs.
---

# GridGain 9.0.13 Release Notes

## Overview

GridGain 9.0.13 is a release that brings a large number of new features and several major behavior changes.

## Behavior Changes

### Compute API Rework

This release features a major rework of distributed computing API:

- The `submit()` method is no longer supported. Use `submitAsync()` instead.
- Colocated execution methods are no longer supported. Instead, other compute methods accept the `JobTarget.colocated` target to achieve the same result.
- Broadcast methods are no longer supported. Instead, other compute methods accept the new `BroadcastJobTarget` job target to achieve the same result.

Code that previously used colocated methods, broadcast methods or the `submit()` method is no longer supported and needs to be updated.

### Reworked listenAddress Property

The `listenAddress` property of node and client configurations has been reworked to support multiple addresses. Accordingly, the property was renamed to `listenAddresses`, and now accepts an array instead of a string.

### Fsync Disabled by Default

Prior to this release, GridGain used fsync to synchronize table data on each node after each operation by default. This provided data safety in case GridGain crashes, at the cost of performance. With this release, data is no longer synchronized by default, but this can still be re-enabled from the configuration when data safety is paramount.

## New Features

### SQL Memory Offloading

Previously, GridGain 9 introduced memory quotas that helped avoid crashes when executing extra large SQL queries. This release extends memory management functionality by introducing memory offloading, providing a way to handle large queries by offloading some of the data required for them to disk. Memory offloading can be enabled in cluster configuration:

```bash
cluster config update ignite.sql.offloadingEnabled=true
```

Then, on each node individual paths for offloaded data and data limits can be set up:

```bash
cluster config update ignite.sql.offloadingEnabled=true
```

### Partitioned Compute Jobs

This release provides a way to execute computing jobs colocated with table partitions. When executed this way, the job will automatically be run on every node that holds a partition for the table, speeding up job execution.

To execute a job this way, provide a `BroadcastJobTarget` object with a table that the job must be colocated with:

```java
public static void example() throws ExecutionException, InterruptedException {
    IgniteClient client = IgniteClient.builder().addresses("127.0.0.1:10800").build();

    String executionResult = client.compute().execute(BroadcastJobTarget.table("Person"),
        JobDescriptor.builder(NodeNameJob.class).build(), null
    );

    System.out.println(executionResult);
}
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-26617 | Platforms and Clients | IgniteTable.name() now returns the table name with correct letter casing. |
| IGN-26589 | General | Fsync is now disabled by default. |
| IGN-26587 | General | The listenAddress property is renamed to listenAddresses and now supports specifying multiple addresses. |
| IGN-26575 | General | Reduced the amount of information printed to log by default when a node joins the cluster. |
| IGN-26556 | Distributed Computing | Fixed an issue that could lead to compute jobs failing when multiple compute jobs are run simultaneously. |
| IGN-26513 | Distributed Computing | Compute API was unified under the same command list. |
| IGN-26488 | Platforms and Clients | .NET: Fixed "java.time.DateTimeException: Invalid ID for region-based ZoneId" on SQL query due to OS-dependent default zone ID. |
| IGN-25941 | Distributed Computing | Added support for performing compute jobs on nodes with partitions. |
| GG-41380 | Licenses | New license-related commands were added to CLI. |
| GG-41379 | Licenses | License-management API was added to REST. |

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
- Tracing
- Service Grid

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
