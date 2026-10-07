---
description: >-
  GridGain 8.7.9 includes a number of critical bug fixes and a change to the public
  DrSenderStore interface.
hidden: true
---

# GridGain 8.7.9 Release Notes

## What's New in This Release

This release includes a number of critical bug fixes.

### Changes in Behavior

The public interface of `DrSenderStore` has been changed.
If you use a custom implementation of this interface, do not upgrade to this version of the product.
The old interface will be restored in a future release.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-25975 | Diagnostics & Failure Handling | Incorrect failure handler log messages were fixed. In case if error handler is disabled there will be no critical error messages. |
| GG-25818 | Diagnostics & Failure Handling | Confusing log message for blocked system critical thread has been changed to display threadName and workerName. |
| GG-23081 | Data Replication | DR full state transfer (FST) synchronous mode has been added. Now FST feature will be completed only after all data will be transferred to the remote data centers. |
| GG-25402 | SQL | Thread that is used for long running queries detection and logging has been updated. IgniteThread will be used instead of random one. |
| GG-25315 | SQL | Full scan instead of Index was used for some queries with SQL 'IN' clause. Query processing logic was updated to fix incorrect behaviour. |
| GG-24877 | Storage Engine | Binary metadata disk operations were moved off the discovery thread in order to avoid slowness of discovery messages processing. |
| GG-25649 | Storage Engine | Dirty pages calculation routine has been optimized to decrease performance impact on checkpoint. The update will minimize possibility of contention for data regions with high concurrency level. |
| GG-25422 | Storage Engine | Debug log records for asynchronous binary metadata update were added. |
| GG-23289 | Storage Engine | Potential Ignite OOM warning has been added to the log. User will be notified by warning message if cache with many partitions will be started in data region with insufficient size |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-25085 | Data Replication | New JMX method has been added to "Data center replication"."Sender hub" MBean. User can get pause status for selected DC. |
| GG-25994 | Platforms & Thin Clients | .NET Core 3.0 support. |
| GG-25664 | Web Console | Data center replication sender hub metrics were updated. Before the fix Visor and Web Console screens were not able to show DR metrics before data will be received on destination data centre. |
| GG-25681 | Visor GUI | Vizor query execution performance has been improved. The issue was related with large records processing on Vizor GUI. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
