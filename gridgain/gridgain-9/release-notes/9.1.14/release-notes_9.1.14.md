---
description: >-
  GridGain 9.1.14 is an emergency release that fixes issues discovered in
  GridGain 9.1.13, including a metadata format incompatibility and missing
  columnar libraries. No new features are included.
---

# GridGain 9.1.14 Release Notes

## Overview

GridGain 9.1.14 is the emergency release fixing issues discovered in GridGain 9.1.13. No new features or additional changes are included.

## Fixed Known Issues

### Metadata Format Incompatibility

This version fixes metadata format incompatibility introduced in GridGain 9.1.13.

You can update to this version from both 9.1.13 and earlier versions.

### Limited Columnar Support

This release fixes a publishing issue that lead to missing columnar libraries. You can safely update to this version when using columnar storage.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-46234 | General | Fixed Raft snapshot compatibility with 9.1.12 and earlier. |
| GG-46190 | Builds and Deliveries | Fixed an issue with Gradle cache hash that caused the builds to muss columnar libraries. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`

{% hint style="warning" %}
When performing a rolling upgrade from GridGain 9.1.8 or 9.1.9, it is required to update to 9.1.10 first.
{% endhint %}

When updating from older versions, we recommend updating to version `9.1.8` first, before performing an update to current version.

## Known Limitations

### Rolling Upgrade Over 9.1.10

When performing a rolling upgrade from GridGain 9.1.9 or earlier, it is necessary to first upgrade to 9.1.10 before upgrading to 9.1.11 or a later version. This is caused by improvements in rolling upgrade procedure that make skipping 9.1.10 with a rolling upgrade impossible.

The upgrade to 9.1.10 must be performed for the whole cluster and committed before the next upgrade can be started.

You do not need to perform this intermediary upgrade when upgrading with downtime, as it only affects the rolling upgrade procedure.

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
