---
description: >-
  GridGain 9.1.13 adds WASM command mode and improved Kafka Sink configuration; due to known issues, avoid using this version.
---

# GridGain 9.1.13 Release Notes

{% hint style="danger" %}
Due to known issues, it is recommended to avoid using this version.
{% endhint %}

## Overview

GridGain 9.1.13 is a private release that is focused on stability, WASM and Kafka Sink improvements.

## Known Issues

### Metadata Format Incompatibility

This version introduced a change that caused incompatibility with GridGain 9.1.12 or earlier.

The exact behavior after the update depends on if the node had cluster metadata:

- If the node stores CMG metadata in a RAFT snapshot, it will crash on startup due to format incompatibility.
- If the node stores metastorage metadata in a RAFT snapshot, it will also crash on startup, but may affect metadata, preventing downgrade to 9.1.12 or earlier.
- If the node does not store metadata information in a RAFT snapshot, it will start, but may write CMG metadata, preventing downgrade to 9.1.12 or earlier.

New clusters started on 9.1.13 create metadata in the new format and cannot be downgraded to 9.1.12 or earlier.

It is recommended to avoid using this version. This issue will be fixed in the next release.

### Limited Columnar Support

Due to an issue during publishing, columnar storage is only supported on Linux x86 platforms in this release.

If you are using columnar on any platforms other than Linux x86, avoid using this version.

This issue will be resolved in the next release.

## Major Changes

### Lazy Default Zone creation

Starting with this release, the `default` [distribution zone](../../administrators-guide/storage/distribution-zones.md) is no longer created on startup. Instead, the zone is only created when no distribution zone is specified during table creation.

{% hint style="warning" %}
Explicitly specifying the `default` zone during table creation will not create the `default` zone if it does not yet exist.
{% endhint %}

When migrating to GridGain 9.1.13, make sure that your scripts do not specify the `default` zone without creating it. Alternatively, use a custom distribution zone for your data.

### Reworked Placement Driver Metrics

This release features a rework in [placement driver metrics](../../administrators-guide/metrics/metrics-list.md). Previously used metrics are no longer available and are replaced with the following metrics:

- AcceptedLeases - The number of active leases.
- LeaseNegotiations - The number of leases currently in negotiation.
- ReplicationGroups - The total number of replication groups.

If you were monitoring old metrics, make sure to update your monitoring software.

## New Features

### WASM Command Mode

With this release, your WASM compute jobs can be executed in *Command mode*. In this mode, the module is run as a standalone program that reads input from stdin and writes output to stdout. In this mode, you can run your compute jobs using the [py2wasm](https://github.com/wasmerio/py2wasm).

{% hint style="warning" %}
only `String` input and output types are supported in command mode.
{% endhint %}

To execute a job in command mode, use the commandBuilder to start your deployed wasm module

```java
JobDescriptor<String, String> helloDesc = WasmJobDescriptor.<String, String>commandBuilder("hello.wasm")
        .units(DEPLOYMENT_UNIT)
        .build();

JobTarget target = JobTarget.anyNode(client.cluster().nodes());
String helloRes = compute.execute(target, helloDesc, "World");
System.out.println("Python job result: " + helloRes);
```

For more information about the command mode, see the [WASM](../../developers-guide/compute/wasm.md) documentation.

### Improved Kafka Sink Configuration

This release adds new [Kafka Sink](../../extensions/kafka-sink.md) configuration properties that can be used to configure how unmapped fields are handled. An unmapped field is a Kafka record field that does not have a corresponding GridGain column.

The following properties were added:

- `unmapped.field.policy` - specifies if the sink fails when a Kafka record field does not map to any GridGain column.
- `drop.key.fields` - the list of key fields the sink will ignore.
- `drop.value.fields` - the list of value fields the sink will ignore.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-29373 | General | Fixed a rare event processing issue that could cause metastorage corruption. |
| IGN-29358 | Cluster Data Snapshots and Recovery | Fixed a rare data rebalance failure. |
| IGN-29339 | General | Fixed Raft snapshot installation failure due to a missing Catalog version. |
| IGN-29328 | Cluster SQL Engine | Fixed ClassCastException when querying DECIMAL columns with Criteria API. |
| IGN-29326 | Cluster Storage Engine | Fixed a rare error during writing of partition metadata during data rebalance. |
| IGN-29290 | General | Fixed a rare race between starting and stopping data rebalance. |
| IGN-29281 | Cluster SQL Engine | Fixed an issue that caused an exception when executing an SQL command for system views with aggregation. |
| IGN-29250 | Cluster Data Snapshots and Recovery | Reduced the amount of errors logged when a node leaves the running cluster and downgraded them to warnings. |
| IGN-29187 | General | Fixed a rare issue with writing aipersist metadata during data rebalance. |
| IGN-29155 | General | Fixed logs being flooded with useless warnings upon node recovery. |
| IGN-29004 | General | Placement driver metrics replaced by more relevant metrics (AcceptedLeases, LeaseNegotiations, ReplicationGroups). |
| IGN-28750 | General | Default zone is now only created when required. |
| IGN-28402 | Cluster SQL Engine | GridGain now rebuilds cached plans periodically based on data changes. |
| GG-46097 | Cluster Storage Engine | Fixed NPE during raft log destruction that prevented node from starting. |
| GG-45999 | Builds and Deliveries | Syntax highlighting is now disabled on unsupported platforms. |
| GG-45997 | Licenses | Fixed old license influencing blank nodes joining the cluster. |
| GG-45912 | Cluster Storage Engine | Removed excessive error logging when a node is stopping and a table on the node has secondary zone configured. |
| GG-45729 | Distributed Computing | Wasm Compute: added Command mode support with WasmCallingConvention.GENERIC_COMMAND. This enables py2wasm and other scenarios where reactor pattern (exported functions) is not supported. |
| GG-44929 | Cluster Data Replication | Improved error message when starting replication on a cluster without tables. |
| GG-43518 | Cluster Data Snapshots and Recovery | Added REST API to restore sequences and maps from snapshots. |
| GG-43354 | Licenses | Improved error message when starting the cluster without a valid license. |
| GG-42208 | Distributed Data Streamer | Kafka sink: added unmapped.field.policy, drop.key.fields, drop.value.fields configuration properties to improve flexibility of record conversion logic. |
| GG-40547 | Builds and Deliveries | The aswsdk-bundle dependency is replaced by the several individual dependencies, reducing the package size. |
| GG-38677 | Cluster Storage Engine | Fixed an issue that causes secondary storage to not be destroyed when a table is dropped. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`

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

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
