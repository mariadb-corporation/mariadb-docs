---
description: GridGain 8.8.16 Patch 2 fixes a large number of data center replication issues.
hidden: true
---

# GridGain 8.8.16 Patch 2 Release Notes

In this patch release, a large number of issues with [data center replication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/introduction) were fixed.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35095 | Cluster Compute Grid | Fixed an issue with potential node failure during cancelling of compute jobs with cache operations. |
| GG-35069 | Cluster Storage Engine | Added new system variable IGNITE_PARTITION_RELEASE_FUTURE_WARN_LIMIT that allows to reduce a number diagnostic messages. |
| GG-35068 | Cluster Storage Engine | Fixed an issue with clearing tombstones. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35073 | Cluster Data Replication | Fixed a rare issue when sender hub dropped connection to receiver under high load. |
| GG-35071 | Cluster Data Replication | Fixed an issue when full-state transfer could freeze in an incomplete state. |
| GG-35070 | Cluster Data Replication | Added a way to enable warning or error log messages instead of assertion errors. |
| GG-35067 | Cluster Data Replication | Fixed an issue related to tombstone TTL configuration. |
| GG-35066 | Cluster Data Replication | Fixed a rare issue that could lead to a DR livelock when multiple caches were in one sender group. |
| GG-35065 | Cluster Data Replication | Added a log message about lost tombstones. |
| GG-35064 | Cluster Data Replication | Fixed an issue when data could not be replicated in background to remote clusters. |
| GG-35048 | Cluster Data Replication | Prevent using remote senders if the local one is configured as preferred. |

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
