---
description: GridGain 8.5.12 is a maintenance release that includes two bug fixes.
hidden: true
---

# GridGain 8.5.12 Release Notes

## What's New in This Release

This maintenance release includes two bug fixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-25260 | Security | Fixed NPE during processing message from a disconnected node when security is enabled (potentially able to cause cascade failure of nodes) |
| GG-25191 | Continuous Queries | Fix peer class loading for remote filters of continuous queries. |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
