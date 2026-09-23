---
description: >-
  GridGain 9.1.21 is a stability and performance release. It requires an explicit
  JitPack repository declaration when running GridGain in embedded mode.
---

# GridGain 9.1.21 Release Notes

## Overview

GridGain 9.1.21 is a private release focused on stability and performance, without introducing major new features.

## Major Changes

### Explicit JitPack Dependency

With this release, when running GridGain in [embedded mode](../../quick-start/embedded-mode.md), you need to explicitly specify the `jitpack.io` repository to allow GridGain to resolve transitive JitPack dependency. Starting from 9.1.21, GridGain depends on an artifact published only on JitPack, so the repository must be reachable from your build.

Add the following entry to the `<repositories>` section of your `pom.xml`:

```xml
<repository>
    <id>jitpack.io</id>
    <url>https://jitpack.io</url>
</repository>
```

If you do not update your dependencies, the build will fail to resolve GridGain's transitive dependencies.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-30536 | General | Fixed a rare bug where a node would not start due to a gap in Raft indices for partitions. |
| IGN-30523 | General | Fixed a rare bug where a node would not start due to a gap in Raft indices for Metastorage. |
| IGN-30518 | Cluster SQL Engine | Fixed an issue where casting a NULL value of type DATE to TIMESTAMP returned an incorrect default value (1970-01-01T00:00) instead of NULL. |
| IGN-30433 | Platforms & Clients | Fixed buffer leak in client connector when handling invalid messages. |
| IGN-30429 | Platforms & Clients | .NET: fixed exception on transaction rollback if the connection is closed. |
| IGN-30386 | CLI Tool | Fixed non-REPL connect command causing an error. |
| IGN-30198 | Distributed Computing | If compute job ignores cancel request and completes, its status is now COMPLETED. |
| IGN-30003 | General | Java client: improved transaction cleanup on client connection loss. |
| IGN-29876 | Platforms & Clients | Java client: added a warning when multiple configured endpoints point to the same server node. |
| IGN-29733 | General | Improved transaction error reporting: the system now returns more specific completion reasons (error, timeout, or unknown) instead of a generic message. |
| GG-47449 | Builds and Deliveries | Added docker images with .NET 10 runtime. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`, `9.1.12`, `9.1.13`, `9.1.14`, `9.1.15`, `9.1.16`, `9.1.17`, `9.1.18`, `9.1.19`, `9.1.20`

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

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
