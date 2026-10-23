---
description: GridGain 8.5.8-p2 is a maintenance release with several bug fixes, mostly in SQL and the storage engine.
hidden: true
---

# GridGain 8.5.8-p2 Release Notes

## What's New in This Release

### Introduction

This maintenance release includes several bug fixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://docs.gridgain.com/docs/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-22442 | SQL | H2 new connection contention stub fix. |
| GG-22652 | SQL | SQL: Fixed an issue where a sub-optimal index could be used in a SQL query. |
| GG-22551 | SQL | Inline index compatibility was broken from 8.4.9 to 8.5.7 if POJO primary key was used. |
| GG-22646 | SQL | Silently fail while trying to recreate a pre-existing index with different `inline_size`. |
| GG-22701 | SQL | `GridH2QueryContext` is cleared after a result set is returned, which causes issues for queries with modes `local=true` & `lazy=true`. |
| GG-23070 | SQL | Partial index rebuild fails when an indexed cache contains different datatypes. |
| GG-22907 | Storage Engine | Threads may be parked for indefinite time during throttling after spurious wakeups. |
| GG-22911 | Storage Engine | Improved speed of checkpoint finalization on binary memory recovery. |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
