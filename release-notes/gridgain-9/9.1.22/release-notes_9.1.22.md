---
description: >-
  GridGain 9.1.22 adds new metrics, improved performance and memory control for
  clients, and a beta release of the GridGain 9 Kubernetes operator.
---

# GridGain 9.1.22 Release Notes

## Overview

GridGain 9.1.22 is a private release with new metrics, improved performance and improved memory control for clients, and a beta release of Kubernetes operator.

## New Features

### Kubernetes Operator

{% hint style="warning" %}
This is an beta version release of kubernetes operator.
{% endhint %}

With this release, a preview version of GridGain 9 Kubernetes operator is available, and can be installed from [DockerHub](https://hub.docker.com/r/gridgain/gridgain9-k8s-operator).

Operator supports all common Kubernetes usage patterns, as well as updating GridGain 9 version. You can see the configuration example with all features enabled in one of [provided examples](https://github.com/gridgain/gridgain9-k8s-operator/blob/main/examples/all-features-reference.yaml).

To use Kubernetes operator, make sure you meet the prerequisites specified in the [operator GitHub repository](https://github.com/gridgain/gridgain9-k8s-operator?tab=readme-ov-file#prerequisites) and follow [installation instructions](https://github.com/gridgain/gridgain9-k8s-operator?tab=readme-ov-file#install-the-operator).

### Memory Quota Block Size Configuration in Java Clients

Java client now supports configuring memory quotas by using the `memoryQuotaBlockSize` [property](../../developers-guide/sql/sql-api.md#memory-quota-block-size) for SQL statements. The default value is 512 KB. Setting a larger block size can improve performance for memory-intensive queries by reducing synchronization overhead with the node-level memory tracker.

The example below shows how you can configure memory quotas:

```java
Statement statement = client.sql().statementBuilder()
    .query("SELECT * FROM large_table")
    .memoryQuotaBlockSize(1_048_576L)  // 1 MB blocks
    .build();
```

### SqlBatchException.UpdateCounters in .NET Clients

When a batch SQL execution fails, .NET clients [now expose](../../developers-guide/clients/dotnet.md#error-handling) `SqlBatchException.UpdateCounters` — a list containing the number of rows affected by each statement that completed successfully before the failure, in batch command order. If the failure occurs before any statement executes, the list is empty.

```csharp
try
{
    await Client.Sql.ExecuteBatchAsync(null, sql, args);
}
catch (SqlBatchException ex)
{
    // Check which operations succeeded before the error
    Console.WriteLine($"Succeeded: {ex.UpdateCounters.Count} operations");
    foreach (var count in ex.UpdateCounters)
    {
        Console.WriteLine($"Rows affected: {count}");
    }
}
```

### CLI Docker Image

A standalone Docker image for the GridGain CLI tool is now available. The image is significantly smaller than the full server image and is designed specifically for cluster management tasks.

To start the CLI tools, run the `gridgain/gridgain9-cli` image in your docker network:

```bash
docker run --network gridgain9_default gridgain/gridgain9-cli
```

The docker image also supports one-line commands for cluster management, for example:

```bash
docker run --rm -it --network gridgain9_default gridgain/gridgain9-cli \
  cluster init --url http://node1:10300 --name my-cluster
```

### Meta Storage Availability Metrics

This release adds new metrics that can be used to monitor Meta Storage health and schema synchronization performance:

**Meta Storage Metrics** ([`metastorage`](../../administrators-guide/metrics/metrics-list.md#metastorage)):

- `AvailablePeers` - Number of available Meta Storage voting peers in the current logical topology;
- `MajorityAvailable` - Binary flag (1/0) indicating whether Meta Storage can execute commands. Updated every 5 seconds.

**Schema Synchronization Metrics** ([`schema.sync`](../../administrators-guide/metrics/metrics-list.md#schema-sync)):

- `Waits` - Histogram of schema synchronization wait times in milliseconds. High values may indicate Meta Storage unavailability or slowness. Includes distribution buckets from 0-1ms to 5000ms+.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-30695 | General | Fixed incorrect transaction cleanup when commit state and enlisted table IDs were not properly propagated. |
| IGN-30686 | Platforms & Clients | Fixed potential double response to client request in case of server-side error. |
| IGN-30645 | Cluster Storage Engine | Reduced transaction lock contention on sorted indexes. |
| IGN-30612 | Cluster SQL Engine | Fixed the issue when SQL query used full index scan instead of cheaper table scan in some cases. |
| IGN-30608 | General | Reduced the amount of logs in case of authentication error. |
| IGN-30566 | General | Fixed the sending of txn cleanup requests to the stale node. |
| IGN-30537 | CLI Tool | Fixed infinite loop in CLI when stopping parent shell process. |
| IGN-30535 | Platforms & Clients | Java client: Fixed incorrect "Transaction context has been lost due to connection errors" error in some cases. |
| IGN-30326 | Cluster Storage Engine | You can now change cluster name from CLI tool. |
| IGN-30065 | Cluster SQL Engine | Added support for index hints in DML queries. |
| IGN-29952 | Code Deployment | Fixed compute job failure after a node is restarted with clean working directory. |
| IGN-29847 | Cluster Storage Engine | Improved write intent resolution for write intents on backup replicas. |
| IGN-25236 | General | Added metrics related to Meta Storage availability and Schema Sync wait time. |
| IGN-24898 | Platforms & Clients | .NET: Added SqlBatchException.UpdateCounters. |
| GG-47723 | Cluster Storage Engine | Fixed occasional "CorruptedTreeException" shortly after node restart. |
| GG-47460 | Platforms & Clients | Java client: added support for Statement.memoryQuotaBlockSize property. |
| GG-47241 | Cluster SQL Engine | Improved SQL query performance by enhancing filter pushdown for JOIN operations. |
| GG-46666 | Builds and Deliveries | Added a docker image for CLI tool. |
| GG-44544 | Platforms & Thin Clients | C++ Continuous query will continue to stream events for recently dropped tables. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`, `9.1.17`, `9.1.18`, `9.1.19`, `9.1.20`, `9.1.21`

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
