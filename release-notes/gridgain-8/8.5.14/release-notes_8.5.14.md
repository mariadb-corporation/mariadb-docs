---
description: GridGain 8.5.14 includes a number of bug fixes and enhancements.
hidden: true
---

# GridGain 8.5.14 Release Notes

## What's New in This Release

This release includes a number of bug fixes and enhancements.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-25988 | Affinity and Baseline Topology | An issue with affinity history overflow that can lead to failed transactions has been fixed. This behavior can be observed in case of frequent topology change when nodes are joining and leaving cluster too often. |
| GG-26539 | Atomic Cache | In case DataRegion is filled, user can get the IgniteOutOfMemory exception, even for remove operations. The release fixes this behaviour, and cache cleanup should no longer cause any issues. |
| GG-26475 | Data Structures | Checkpoint throttling logic has been improved. In case of simultaneous rebalance and checkpoint process, checkpoint IO should be processed with the priority to decrease performance pressure from background tasks. |
| GG-26312 | Deployment | Scan query transformer can now be deployed using peer class loading in case if they are not deployed on cluster nodes. |
| GG-26272 | Diagnostics & Failure Handling | Failure handler will now handle index build exceptions. |
| GG-26193 | SQL | Log record level has been decreased form ERROR to INFO for SQL query cancel operation. It will prevent a significant number of log messages from being written in the logs in case of frequent cancel operations. |
| GG-25982 | SQL | Improve index inline usability. User will be notified by a warning log record in case if SQL index inline is not sufficient for effective queries execution. Optimal inline size will significantly decrease resource consumption, which will have positive effect on system performance. |
| GG-26135 | Storage Engine | Fixed an issue that caused a restart failure in case when WAL mode is FSYNC and no WAL archiver is configured. |
| GG-26248 | Transactions | Fixed tx recovery protocol behavior to prevent a race with concurrent rollback. |
| GG-26538 | Transactions | Prevent concurrent change of transactional entry in case if it is in rollback section. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-26493 | Data Replication | Data replication will not stop if one of DR senders has a store that is annotated with @DurableStore. |
| GG-26137 | Data Replication | New JMX method has been added to "Data center replication"."Sender hub" MBean. User can get pause status for selected DC. |
| GG-25108 | Security | If ADMIN_OPS permission is granted to a user, then TASK_EXECUTE is not needed for control.sh execution. |
| GG-26543 | Transactions | Unexpected DR stop is fixed if client with default configuration is connecting to "drUseCacheNames=true" cluster. |
| GG-25990 | Visor | Vizor query execution performance has been improved. The issue was related with large records processing on Vizor GUI. |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
