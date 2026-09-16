---
description: >-
  GridGain 9.0.1 improves cluster stability and performance and adds continuous
  query metrics for Java and .NET clients.
---

# GridGain 9.0.1 Release Notes

## Overview

GridGain 9.0.1 is the update focused on improving cluster stability and performance.

## New Features

### Continuous Query Client Metrics

In this release, client metrics for Java and .NET clients were expanded with support for continuous query metrics. You can use these metrics to track the number of received continuous query events received and sent.

For Java clients, make sure to enable metrics in configuration:

```java
IgniteClient.builder().metricsEnabled(true)
```

You can then use the standard JMX monitoring tools to track metrics.

For .NET clients, the metrics are exposed automatically and can be tracked without client modifications.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-39932 | General | Fixed possible issues with cluster initialization with invalid license. |
| GG-39918 | General | Reduced the time required to initialize the cluster in embedded mode. |
| GG-39918 | CLI | Fixed some CLI commands missing `--profile` parameter in non-REPL mode. |
| GG-39608 | General | Improved error messages for user create command. |
| GG-39058 | Clients | .NET: Added continuous query metrics. |
| GG-39057 | Clients | Java: Added continuous query metrics. |
| GG-38799 | Storage | Added support for RANDOM eviction mode. |
| GG-38716 | Data Center Replication | Added information on current progress of data center replication to the `status` command output. |

## Known Limitations

### Delay on DDL Requests

DDL requests, such as `CREATE TABLE`, take a few seconds each to complete. Because of that, large database initialization scripts may take longer than expected. This will be addressed in upcoming versions.

### Performance of GridGain 8 Applications

Some scenarios may see lower performance when moving to GridGain 9. This is a temporary limitation, and the performance in these scenarios will be improved in upcoming versions.

### High-Availability with Two Data Copies

When a partition loses majority of its copies, it becomes unavailable. This behavior is required for split-brain protection. Because of this, in a distribution zone with 2  data replicas, losing one node may lead to partial unavailability.

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
