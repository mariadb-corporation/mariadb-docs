---
description: GridGain 8.5.8-p3 is a maintenance release with several bug fixes in the storage engine and SQL.
hidden: true
---

# GridGain 8.5.8-p3 Release Notes

## What's New in This Release

### Introduction

This maintenance release includes several bug fixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://docs.gridgain.com/docs/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-23250 | Storage Engine | Fixed a concurrency problem in `PagesWriteThrottle`. |
| GG-23292, GG-23253 | SQL | Fixed an issue where lazy SQL queries with several open iterators could lead to an assertion error. |
| GG-23248 | SQL | Wrong system property naming `USE_POOL_FOR_LAZY`. |
| GG-23239 | SQL | Cluster restart caused all indexes to rebuild. |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
