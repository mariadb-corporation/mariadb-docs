---
description: GridGain 8.5.8-p7 is a maintenance release with a fix for one critical storage engine issue.
hidden: true
---

# GridGain 8.5.8-p7 Release Notes

## What's New in This Release

This release includes a fix for one critical issue.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27165 | Storage Engine | Fixed a possible `IgniteOutOfMemoryException` that could happen when destroying a large cache from a cache group with many caches. |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
