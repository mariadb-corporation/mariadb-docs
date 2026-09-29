---
description: >-
  GridGain 8.7.2-p14 is a maintenance release that reduces cache memory
  consumption when no caches use the TRANSACTIONAL_SNAPSHOT atomicity mode.
hidden: true
---

# GridGain 8.7.2-p14 Release Notes

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-30463 | Cache | Reduced memory consumption in cases when the cluster does not have caches with the `TRANSACTIONAL_SNAPSHOT` atomicity mode. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
