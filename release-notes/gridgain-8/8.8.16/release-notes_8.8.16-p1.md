---
description: GridGain 8.8.16 Patch 1 fixes a rare data center replication issue.
hidden: true
---

# GridGain 8.8.16 Patch 1 Release Notes

In this patch release, a rare issue with [data center replication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/introduction) was fixed.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34909 | Cluster Data Replication | Fixed a rare case of CorruptedTree exception that could happen during data upload when using data streamer with ongoing data center replication. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34908 | Cluster Data Replication | Fix the issue when some entries were missed during incremental DR. |

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
