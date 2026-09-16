---
description: >-
  GridGain 9.0.10 improves Data Center Replication and adds an OpenTelemetry
  exporter and the IgniteClientGroup .NET API.
---

# GridGain 9.0.10 Release Notes

## Overview

GridGain 9.0.10 is a release that continues work on stability while also bringing new and exciting features.

## New Features

### Improved Data Center Replication

This release features multiple improvements to [Data Center Replication](../../administrators-guide/data-center-replication/README.md):

- Time-based conflict resolution during active-active replication is significantly more reliable.
- You can now run data replication on clusters secured via SSL.
- You can now specify addresses of multiple nodes, that will be used for failover and data transfer optimization.

### OpenTelemetry Exporter

In this release, a new [OpenTelemetry](https://opentelemetry.io/) metrics exporter was added. When enabled, all nodes in the cluster send metrics to the specified OpenTelemetry endpoint.

You can enable the OpenTelemetry exporter from CLI:

```bash
cluster config update ignite.metrics.exporters.test: {exporterName:otlp, endpoint:"http://localhost:9090/api/v1/otlp/v1/metrics", protocol:"http/protobuf"}
```

For more information about configuring OpenTelemetry exporter, see [metrics configuration](../../administrators-guide/metrics/configuring-metrics.md#opentelemetry) topic.

### IgniteClientGroup in .NET

The `IgniteClientGroup` API was added to the .NET client. This API can be used to simplify `IgniteClient` usage in [DI containers](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection), for example:

```csharp
// Register in DI container
builder.Services.AddSingleton<IgniteClientGroup>(_ => new IgniteClientGroup(
        new IgniteClientGroupConfiguration
        {
            Size = 3,
            ClientConfiguration = new("localhost"),
        }));

...

// Invoke in a controller
public async Task<IActionResult> Index([FromServices] IgniteClientGroup igniteGroup)
{
    IIgnite ignite = await igniteGroup.GetIgniteAsync();
    var tables = await ignite.Tables.GetTablesAsync();
    return Ok(tables);
}
```

### System View Extensions

As part of continued work to improve system views, this release features multiple system view improvements:

- A new `LOCKS` system view was added, that can be used to track currently active locks.
- A `LOCAL_PARTITION_STATES` column was added to the `ESTIMATED_ROWS` system view.
- A `USERNAME` column was added to the `SQL_QUERIES` system view.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-26141 | Configuration | Improved error message when an invalid HOCON configuration is provided. |
| IGN-26094 | General | Initialized nodes will no longer stop trying to rejoin the cluster. |
| IGN-26079 | CLI Tool | You can now pass parameter values with spaces when using the CLI tool. |
| IGN-26043 | Platforms and Clients | .NET: Added IgniteClientGroup to simplify DI integration. |
| IGN-25766 | SQL | A new LOCKS view was added. |
| IGN-25735 | General | Unused error codes were removed. |
| IGN-25267 | General | Added a new LOCAL_PARTITION_STATES column to ESTIMATED_ROWS system view. |
| GG-41216 | Cluster Security | Removed GET_JOB_STATES privilege. GET_JOB_STATE should be used instead. |
| GG-41150 | Cluster Data Snapshots and Recovery | Snapshot-related CLI commands now provide human-readable time instead on a timestamp. |
| GG-40958 | Cluster SQL Engine | Added USERNAME column to SQL_QUERIES system view. |

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
