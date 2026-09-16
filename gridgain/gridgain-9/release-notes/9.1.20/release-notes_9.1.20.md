---
description: >-
  GridGain 9.1.20 brings improved AIPersist storage and rolling upgrade
  monitoring, new client connection events, and multiple API improvements
  including an editable cluster name.
---

# GridGain 9.1.20 Release Notes

## Overview

GridGain 9.1.20 is a private release that brings improved AIPersist storage and rolling upgrade monitoring, new events and multiple API improvements.

## Major Changes

### Partition Statistics Metrics Disabled by Default

Starting with this release, [partition modification counter metrics](../../administrators-guide/metrics/metrics-list.md#table-partition) are disabled by default. These metrics track the number of modifications to each partition and can create unexpected monitoring load in large deployments.

If you use these metrics, re-enable them via configuration.

### Partition Calculation in Default Zones

Previously, when a distribution zone was created lazily, it was set to use 25 partitions. Starting with this release, partition count will be calculated automatically based on [default partitioning rules](../../administrators-guide/storage/data-partitions.md#partition-number).

## New Features

### Expanded Metrics

#### AIPersist Storage Metrics

This release adds more [metrics](../../administrators-guide/metrics/metrics-list.md) for the `aipersist` storage engine:

**New Region Metrics** (`storage.aipersist.default`):

- `TotalEmptySize` - Specifies the amount of empty space in the region;
- `TotalDataSize` - Specifies the amount of space occupied by data;
- `PagesFillFactor` - Ratio of used space to total space (0.0 to 1.0).

**New Consistency Metrics** (`storage.aipersist.checkpoint`):

- `ReadLockAcquisitionTime` - Time spent waiting for checkpoint read lock, in nanoseconds;
- `ReadLockHoldTime` - Time the checkpoint read lock is held, in nanoseconds;
- `ReadLockWaitingThreads` - Number of threads currently waiting for checkpoint read lock.

These metrics help identify storage fragmentation, checkpoint contention, and overall storage health.

#### Rolling Upgrade Metrics

New metrics are now available for monitoring rolling upgrade progress (`upgrade.rolling`):

- `InitialVersion` - Initial cluster version before rolling upgrade;
- `TargetVersion` - Target cluster version for rolling upgrade;
- `State` - State of rolling upgrade;
- `UpgradedNodes` - Comma-separated list of nodes that have been upgraded to target version;
- `NotUpgradedNodes` - Comma-separated list of nodes that have not been upgraded yet.

### Client Connection Events

This release adds two new event types for monitoring client connections:

- `CLIENT_CONNECTION_ESTABLISHED` - Fired when a client successfully connects to the node;
- `CLIENT_CONNECTION_CLOSED` - Fired when a client disconnects from the node.

For more information on working with events, see the [Events](../../developers-guide/events/README.md) documentation.

### Paged SQL Results in CLI Tool

The CLI tool now supports paged result fetching for SQL queries. Results are fetched incrementally and displayed with a pager.

The following [CLI tool configuration options](../../administrators-guide/config/cli-config.md) were added:

- `ignite.cli.sql.display-page-size` - Number of rows to fetch per page. Default value: 1000;
- `ignite.cli.pager.enabled` - Enable/disable pager for long outputs. Default value: `true` on Unix, `false` on Windows;
- `ignite.cli.pager.command` - Command to use for paging. Default value: `less -RFX` on Unix, `more` on Windows.

You can configure these settings by using the `cli config set` command, for example:

```bash
cli config set ignite.cli.sql.display-page-size=500
```

### Enhanced Mapper Support

#### MapperBuilder Inheritance Support

The `MapperBuilder` now supports [mapping fields](../../developers-guide/table-api.md#working-with-mappers) inherited from superclasses when using manual mapping. This enhancement allows you to work with object hierarchies more naturally:

```java
Mapper<ChildClass> mapper = Mapper.builder(ChildClass.class)
    .map("parentField", "PARENT_COL")  // Field from parent class
    .map("childField", "CHILD_COL")    // Field from child class
    .build();
```

### C++ Client Continuous Query Options

The C++ client now supports the `skipOldEntries` option for continuous queries. This option allows you to skip historical data and only receive new updates:

```cpp
// Configure continuous query to skip old entries
continuous_query_options opts;
opts.set_skip_old_entries(true);  // Only receive new changes
opts.set_poll_interval_ms(100);

// Start continuous query with the options
auto continuous_query = table_view.query_continuously(opts);

// Process events - only new changes will be included
for (auto batch : continuous_query) {
    for (auto event : batch) {
        // Process event
    }
}
```

When `skipOldEntries` is set to `true`, the continuous query skips entries that existed before the query started, and only returns events for new modifications. This is particularly useful when monitoring real-time changes without processing the entire existing dataset.

### Editable Cluster Name

You can now change the cluster name after cluster initialization by using the new `cluster/name` endpoint:

```bash
curl -X PATCH http://localhost:10300/management/v1/cluster/name \
  -H "Content-Type: application/json" \
  -d '{"name": "new-cluster-name"}'
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-43847 | Rolling Upgrade | Added rolling upgrade metrics. |
| GG-44872 | Cluster Continuous Queries | C++ client: Added support for skipping old entries in continuous queries. |
| GG-47151 | Migration Tools | The migration-tools-adapter now supports fields from superclasses. |
| GG-47342 | Integrations | Improved Kafka connector logging. |
| GG-47422 | Cluster Data Replication | Improved the output format for DR connector logs. |
| IGN-28670 | General | Improved error handling during a node startup. |
| IGN-29429 | Platforms & Clients | Java client: fixed exception on transaction rollback if the connection is closed. |
| IGN-29702 | Cluster Storage Engine | Added "aipersist" storage consistency metrics. |
| IGN-29871 | CLI Tool | Added iterative cursor reading for SQL in CLI tool. |
| IGN-29987 | Cluster SQL Engine | Improved an error message displayed when INSERT command has incorrect number of arguments. |
| IGN-30037 | Distributed Computing | Clarified error message when marshallers are improperly defined. |
| IGN-30039 | Cluster Storage Engine | Added new metrics for the "aipersist" Storage Engine. |
| IGN-30077 | Cluster SQL Engine | Fixed an issue that sometimes caused errors when a NOT NULL column was added to a table. |
| IGN-30102 | Platforms & Clients | Added CLIENT_CONNECTION_ESTABLISHED and CLIENT_CONNECTION_CLOSED ignite events. |
| IGN-30158 | Cluster SQL Engine | Partition statistics metrics disabled by default. |
| IGN-30179 | General | Directly mapped client-side transactions could leave rows locked for some time in case of enlistment failure on a coordinator. |
| IGN-30283 | General | Fixed runInTransaction to actually do retries for a client-side transaction. |
| IGN-30296 | General | MapperBuilder now allows mapping fields inherited from superclasses. Shadowed fields are not supported; only fields from Class can be mapped. |
| IGN-30322 | General | You can now change cluster name. |
| IGN-30327 | Cluster Metrics & Monitoring | Fixed some metrics having a . in their name. |
| IGN-30341 | Platforms & Clients | Clients: Fixed a race condition, that could result in a sudden connection termination right after establishment. |
| IGN-30355 | General | Fixed a transaction abortion error on transaction coordinator. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`, `9.1.17`, `9.1.18`, `9.1.19`

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
