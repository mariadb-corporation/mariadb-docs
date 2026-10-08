---
description: >-
  GridGain 8.5.9 introduces the Snapshot Security feature to protect snapshot
  integrity, along with numerous bug fixes across SQL, storage, discovery, and
  more.
hidden: true
---

# GridGain 8.5.9 Release Notes

## What's New in This Release

### Introduction

This release includes one new feature — Snapshot Security — and several bug fixes.

### New Feature: Snapshot Security

Snapshot Security helps ensure the integrity of each snapshot file and the overall snapshot process.

When enabled, Snapshot Security provides an additional layer of security, protecting data from modification and corruption and from snapshot file version mismatch. It helps eliminate the possibility of accidentally using files from multiple versions of snapshots. For example, suppose you have 2 snapshots: A and B. It may be possible to accidentally use file1.dat and file 2.dat from Snapshot A, and file3.dat from snapshot B by mistake.

Snapshot Security creates a file registry that contains a list of all of the files included in the snapshot, and their cryptographic hashes. Before being restored, snapshots are compared against this registry to ensure they contain the proper files.

Snapshot Security protects files from substitution; however, it does not protect against malicious actions by hackers/etc.

Enable Snapshot Security via the `GG_SNAPSHOT_SECURITY_LEVEL` system property.

| Parameter | Description |
|---|---|
| DISABLED | Snapshot file registry is not created and never validated if present (default). |
| IGNORE_EXISTING | Snapshot file registry is included in new snapshots. Existing file registries in snapshots are not verified. |
| IGNORE_MISSING | Snapshot file registry is included in new snapshots.<br>Existing file registries in snapshots DO GET verified.<br>Missing file registries in snapshots are tolerated. |
| REQUIRE | Snapshot file registry is included in new snapshots. Presence and validity of file registries in all snapshots are required. |

## Known Issues

| Issue ID | Description |
|---|---|
| GG-24105 | Conflicts in hashes of primary/backup partitions after node restart (in-memory caches) |
| GG-23120 | AssertionError Missing tails occurs in scenario with starting node after leaving while creating new index |

## Fixed Issues

### GridGain Professional Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-20539 | .NET | Fixed .NET continuous query "Removed" event registration. |
| GG-19508 | Atomic Cache | Assertion error on near node when backup replica failed during atomic operation. |
| GG-20877 | Communication | U.getLocalHost must always returns physical network interface address. |
| GG-19216 | Communication | Fixed triggering of Failure Processor when exchange thread is blocked on sending message to client node. |
| GG-20871 | Communication | Fixed log reduction for case of long getting communication TCP client when client is already unavailable, now client information is logging properly. |
| GG-20167 | Diagnostics & Failure Handling | List of files containing in classpath is printed on the start of the node. It can be disabled by setting ignite system property 'IGNITE_LOG_CLASSPATH_CONTENT_ON_STARTUP' to false. By default, it is enabled. |
| GG-19222 | Diagnostics & Failure Handling | Added diagnostic ability for dumping page locks' state similar to thread dump. |
| GG-19974 | Diagnostics & Failure Handling | Added diagnostic tool of dumping WAL page history in case of B+Tree corrupting. |
| GG-19678 | Diagnostics and Failure Handling | Fixed false-positive failure handler triggering on exchange thread. |
| GG-19647 | Discovery | Implemented more precise timeouts calculations in Discovery and Communication SPI. |
| GG-19315, GG-20865 | Discovery | Client node cut off by communication from the rest of the cluster is stopped by Communication Failure Resolver. |
| GG-19640 | Discovery | Discovery events processing optimized by lazy initialization of discovery events names. |
| GG-20971 | Integrations | Upgrade jackson-databind library to version 2.9.9 |
| GG-20976 | Integrations | Upgrade commons-codec library to version 1.12 |
| GG-15000 | Metrics & Monitoring | Added IO statistics for logical and physical page reads. |
| GG-18754 | Partition Map Exchange | Fix several partition consistency issues arising on node failures. |
| GG-19991 | Partition Map Exchange | Added diagnostic output for coordinator change process. |
| GG-19910 | Rebalance | Rebalance properties were moved from CacheConfiguration to IgniteConfiguration level. Rebalance properties in CacheConfiguration were deprecated. |
| GG-20977 | Security | Upgrade Jetty library to version 9.4.18 |
| GG-20370 | Security | Fixed bug around failing to connect by JDBC with read-only permissions. |
| GG-20158 | SQL | Message "Indexes rebuilding completed for all caches." appears in log after all indexes are rebuilt. This requires at least one index to be rebuilt successfully. |
| GG-19156 | Storage Engine | Introduce multithreading recovery logic in order to improve node startup time. |
| GG-19964 | Storage Engine | Fixed "Compression of WAL segment was skipped due to unexpected error" spam on node start when WAL compaction is enabled. |
| GG-20849 | Storage Engine | WAL segments serialization compatibility fixed. |
| GG-21366 | Storage Engine | Fix threads parking for indefinite time during throttling after spurious wakeups. |
| GG-19949 | Thin Clients | Thin client: removed limitation of the length of credentials during handshake. |
| GG-19332 | Transactions | Prevent NPE on concurrent tx and cache destroy. |
| GG-23948 | Deployment | Added retries on peer class loading timeouts. |
| GG-23883 | SQL | Rename USE_POOL_FOR_LAZY property to IGNITE_USE_POOL_FOR_LAZY_QUERIES |
| GG-23833 | Common | Logging of partitions information during recovery disabled by default |
| GG-23811 | Common | Fix inconsistency between cache data and indexes when cache operation is interrupted |
| GG-23800 | Storage Engine | Fixed possible PDS corrupt during checkpoint |
| GG-23660 | Storage Engine | Fixed case when checkpoint tmp files were not removed on node start. |
| GG-23635 | Visor | Visor GUI: Fixed showing of metadata for the first cache. |
| GG-23569 | SQL | Lazy mode bugfux for local queries |
| GG-23385 | Common | Default system worker blocked timeout changed to 2 minutes |
| GG-23357 | Platforms & Thin Clients | Fixed OOM issue when invalid message was sent to thin client port |
| GG-23328 | SQL | Fix assertion error in case of usage several iterators of lazy queries |
| GG-23283 | SQL | Fix assertion error for several open iterator in lazy SQL mode |
| GG-23272 | Transactions | Fix concurrency race in PagesWriteThrottle |
| GG-23271 | SQL | Fix full indexes rebuild after each cluster's restart. |
| GG-23024 | SQL | H2 connection pool fix for reduce h2 connection timeouts. |
| GG-22943 | SQL | Correctly remove index metapage, fixes inline size change on index recreate operations. |
| GG-22856 | SQL | Fixed cost estimation bug for tree indexes. |
| GG-22811 | SQL | Fix bug at the lazy execution mode for local SQL queries |
| GG-22447 | Atomic Cache | Fixed possible StackOverflowError in scenario with huge batch within one transaction |
| GG-21726 | Data Structures | Fixed issue with colocated IgniteSet rebalancing when stored object class is not available |
| GG-21085 | SQL | Fix compatibility when JAVA_OBJECT is inlined to index |
| GG-20865 | Discovery | Client node cut off by communication from the rest of the cluster is stopped by Communication Failure Resolver |
| GG-19640 | Discovery | Discovery events processing optimized by lazy initialization of discovery events names. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-20162 | Data Center Replication | Make debug logs more verbose. |
| GG-19280 | Rolling Upgrade | Remove outdated compatibility tests. |

### GridGain Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-18733 | Snapshots & Point in Time Recovery | AssertionError upon starting a node caused by logging page delta record before page snapshot. |
| GG-19368 | Snapshots & Point in Time Recovery | Removed wrong "Can't find snapshot metadata" message from logging. |
| GG-19982 | Snapshots & Point in Time Recovery | Fixed NullPointerException in logs when server nodes leave cluster during snapshot. |

### Management and Monitoring Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-19203 | Control Utility | control.sh output is duplicated to control-utility.log. |
| GG-19149 | Control Utility | Added message that snapshot-utility is deprecated. Recommended using `control.sh --cache idle_verify` instead. |
| GG-19451 | Control Utility | Fixed formatting in control.sh in idle_verify output, also added logging of parsed parameters of idle_verify. |
| GG-20289 | Control Utility | `control.sh` string literal replaced with more common `control.(sh\|bat)`. |
| GG-20416 | Control Utility | Error message contains info about SSL connectivity problems if connection to secured cluster fails. |
| GG-20851 | Control Utility | `snapshot-utility.out` is stored in `${IGNITE_HOME}/work/log` |
| GG-20854 | Control Utility | UTC timezone is used in build dates now. |
| GG-20862 | Control Utility | Removed `caches` argument at restore command. |
| GG-19365 | Control Utility | Missing arguments added into usage section of `snapshot-utility.sh` help message. |
| GG-19995 | Control Utility | Fixed mismatch between idle_verify results with and without `-dump` option in some cases. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
