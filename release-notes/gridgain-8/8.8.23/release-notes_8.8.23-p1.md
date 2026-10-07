---
description: GridGain 8.8.23-p1 fixes a rare issue with thin client authentication.
hidden: true
---

# GridGain 8.8.23-p1 Release Notes

This release is dedicated to fixing a rare issue with thin client authentication.

## Complex SQL Operation With IN Operator Working Incorrectly

In GridGain 8.8.23-p1, complex SQL operations that evaluate index key prefix and index key suffix in the same operation will return duplicate values for non-aggregate functions, or incorrect values for aggregate functions. Here is the example of the condition that can trigger the issue for index with `a, b, c` columns:
```
a=X AND c in (Y, Z)
```
If you use similar conditions in your environment, avoid updating to GridGain 8.8.23-p1. An emergency 8.8.25-p1 patch release is scheduled soon.
If you already use it and encounter the issue, update to [GridGain 8.8.25-p1](../8.8.25/release-notes_8.8.25-p1.md) version as soon as possible to fix the issue.

## Improvements and Fixed Issues

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36002 | Cluster Continuous Queries | Fixed a rare issue that happened when data structures were updated during thin client authentication. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p2`, `8.8.16-p2`, `8.8.18-p1`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`, `8.8.19`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.23`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.7.2`, `2.11.0`, `2.12.0`, `2.13.0`

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
