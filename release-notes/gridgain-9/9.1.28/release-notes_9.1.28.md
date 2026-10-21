---
description: >-
  GridGain 9.1.28 hardens security around the distributed map, thin-client
  metadata, and LDAP role mapping, corrects the REST transactions API path, and
  deprecates the RocksDB partition storage engine.
hidden: true
---

# GridGain 9.1.28 Release Notes

## Overview

GridGain 9.1.28 hardens security around the distributed map, thin-client metadata, and LDAP role mapping, corrects the management REST transactions API path and deprecates the RocksDB partition storage engine.

## Major Changes

### Security Hardening

Several access checks that were previously missing are now enforced. Review them before upgrading, because a client or role that relied on the earlier, looser behavior may begin to be denied:

- Thin-client index and table metadata requests now check privileges, so a client can no longer read index or table metadata it has no privilege to see.
- The distributed map API is now checks user privileges.
- Unmapped LDAP group names are no longer trusted as GridGain roles.
- Renaming the cluster now requires the new `RENAME_CLUSTER` privilege, so a routine authenticated user can no longer rename the cluster.
- Enabling, disabling, or listing cluster-wide metrics now requires the corresponding metrics privilege (`ENABLE_METRICS`, `DISABLE_METRICS`, or `LIST_METRICS`).

### REST Transactions API Path Corrected

The management REST API served its transactions endpoints on a path that differed from the published OpenAPI specification. The endpoints are now served on the path the specification documents. A client that hard-coded the previous path must be updated. See [management REST API](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/BfPLkyMnD0BAfMCRhZKr/gridgain9-development/accessing-data/rest-api).

### Deprecations and Removals

The RocksDB partition storage engine is now deprecated and will be removed in a future release. Migrate profiles that use it to the `aipersist` or `aimem` storage engines. See [RocksDB storage engine](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/BfPLkyMnD0BAfMCRhZKr/architecture/storage/engines/rocksdb-persistent-storage).

## New Features

### .NET Entity Framework Core Provider

The .NET client now ships an Entity Framework Core provider, letting you use GridGain through EF Core.

### Receiver Execution Options in the Java Thin Client

The Java thin client data streamer now accepts `ReceiverExecutionOptions`, giving you control over how a stream receiver runs. See [Data Streamer](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/BfPLkyMnD0BAfMCRhZKr/gridgain9-development/accessing-data/data-streaming).

### LDAP Connect and Read Timeouts

LDAP binds are now bounded by JNDI connect and read timeouts, so a slow or unresponsive directory server can no longer stall authentication indefinitely. See [Authentication](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/BfPLkyMnD0BAfMCRhZKr/security/authentication-and-authorization/authentication).

## Improvements and Fixed Issues

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-52265 | Cluster SQL Engine | Fixed an issue where the MERGE operator failed under some conditions. |
| GG-51913 | General | The management REST transactions API is now served on the path published in the OpenAPI specification. |
| GG-51820 | Cluster Storage Engine | Segstore log records are now validated before they are interpreted. |
| GG-51795 | Cluster Storage Engine | Fixed page replacement writing a page of a destroyed partition. |
| GG-51772 | Cluster Storage Engine | Raft log storages opened by a start after node stop has begun are now closed. |
| GG-51758 | General | Absent logical topology members are now probed before they are removed. |
| GG-51757 | General | A restarted node's previous launch is now removed from the logical topology. |
| GG-51756 | General | Logical topology leaps are now propagated to the network topology service. |
| GG-51738 | Cluster Storage Engine | The write-intents list head is now kept when unlinking a detached row version. |
| GG-51737 | General | Bounded the recovery queue and the sends waiting for a channel. |
| GG-51721 | Cluster Storage Engine | The RocksDB partition storage engine is now deprecated. |
| GG-51675 | Cluster Continuous Queries | Pending continuous query requests now fail when the target node leaves. |
| GG-51598 | Migration Tools | Fixed the migration-tools CLI crashing instead of printing its version. |
| GG-51595 | General | Fixed the wrong MBean attribute type for UuidGauge metrics. |
| GG-51565 | General | Fixed Closeable views #close delegation. |
| GG-51516 | General | Fixed a race in the log storage size limiter. |
| GG-51505 | Cluster Continuous Queries | Continuous Query: Fixed poll delay on new demand. |
| GG-51493 | Cluster SQL Engine | Fixed statistics refresh and plan invalidation reliability. |
| GG-51492 | Migration Tools | The migration-tools adapter no longer ships the AI3 API stub JAR on runtime classpaths. |
| GG-51491 | Platforms & Clients | The client channel now stays alive when a server error class cannot be linked. |
| GG-51439 | Cluster SQL Engine | Continuations of key-value plans now execute on the completing thread when possible. |
| GG-51436 | Platforms & Clients | C++ client: A send operation now reports failure on EAGAIN while the packet stays queued. |
| GG-51425 | Cluster SQL Engine | Fused a trimming projection into the required columns for primary-key lookups. |
| GG-51422 | Platforms & Clients | Java thin client: Added support for ReceiverExecutionOptions in the data streamer. |
| GG-51418 | General | Resources acquired by a bootstrap compute job are now released. |
| GG-51416 | Migration Tools | The migration-tools adapter is now deployed as three deployment units instead of one per JAR. |
| GG-51391 | Cluster Security | The authentication thread pool is now sized from authentication.threadPoolSize. |
| GG-51390 | Cluster Security | LDAP binds now honor JNDI connect and read timeouts. |
| GG-51388 | Cluster Storage Engine | Partition storages left in the rebalance state are now cleared. |
| GG-51386 | General | Reduced write latency when a partition's primary replica and Raft leader are on different nodes. |
| GG-51377 | Platforms & Clients | C++: Fixed a race in the Windows network code. |
| GG-51284 | General | A failing cloud license probe no longer stops node start. |
| GG-51189 | Migration Tools | Updated the GridGain 8 dependency to 8.9.37. |
| GG-51135 | Platforms & Clients | Fixed corner cases in direct client transaction error processing. |
| GG-51131 | General | Tables are now enlisted into an existing partition enlistment under the enlist lock. |
| GG-50977 | Platforms & Clients | C++: Transaction commit is now sent in the last message of the transaction. |
| GG-50940 | Cluster Continuous Queries | Removed the deprecated ContinuousQueryTransactionWatermark.transaction() method. |
| GG-50921 | Platforms & Clients | Fixed a direct-mapped thin-client transaction leaking a lock when aborted before its enlistment reached the coordinator. |
| GG-50918 | General | Catalog compaction now responds to the coordinator even when an unexpected exception occurs. |
| GG-50902 | Cluster Data Replication | The data replication connector now stores multiple entries within a single transaction. |
| GG-50861 | Platforms & Clients | Thin client: Fixed heartbeatInterval validation. |
| GG-50772 | Platforms & Clients | C++ extension: Catalog-snapshot schemas are now published into the client cache. |
| GG-50629 | Cluster Storage Engine | The Raft meta storage of evicted partitions is now destroyed when their zone is dropped. |
| GG-50488 | Cluster Data Replication | The DR connector now logs a warning if metadata has not arrived within 30 seconds. |
| GG-50381 | Cluster Security | Unmapped LDAP group names are no longer trusted as GridGain roles. |
| GG-50377 | Cluster Security | The distributed map API is now secured with privilege checks. |
| GG-50376 | Cluster Security | Thin-client index and table metadata requests now check privileges. |
| GG-50375 | Platforms & Clients | Added JDBC error codes for transaction serialization failures. |
| GG-50358 | General | The Catalog DSL now reads a zone name the way CREATE ZONE does. |
| GG-50250 | Cluster Storage Engine | Evicted partition replicas are now destroyed on recovery. |
| GG-50208 | Cluster Data Replication | Transaction cleanup is now moved off the saturated pool, preventing a full-state-transfer stall on large tables. |
| GG-50070 | General | Abandoned resources for destroyed zones are now handled in the catalog. |
| GG-49982 | General | Fixed a rare case where a primary replica change during transaction cleanup could leave duplicate rows for the same primary key. |
| GG-49937 | Cluster SQL Engine | An implicit SQL transaction is now finalized when plan validation fails. |
| GG-49878 | Platforms & Clients | Java client: Fixed compatible schema-change retry within a transaction. |
| GG-49726 | Cluster Security | LDAP credential rejections are now classified as expected authentication failures. |
| GG-49675 | General | Reduced the zone-creation safe-time stall under fsync. |
| GG-49621 | General | Compute: Job, task, and receiver classes are now resolved without initializing them before the type check. |
| GG-49619 | Cluster Security | Renaming the cluster now requires the new RENAME_CLUSTER privilege. |
| GG-49614 | Cluster Security | Enabling, disabling, or listing cluster-wide metrics now requires the corresponding metrics privilege. |
| GG-49163 | Platforms & Clients | C++: The client now returns the same Unknown Error Code as other clients. |
| GG-48995 | General | Fixed a possible ignoring of a write intent by a late-committed transaction. |
| GG-48531 | General | MetaStorage unavailability is no longer treated as a critical failure. |
| GG-48180 | Cluster Storage Engine | The GC/vacuum pipeline now resolves a null column gracefully instead of failing with a critical error when processing orphaned write intents after a schema version change. |
| GG-47996 | Cluster Continuous Queries | Fixed a continuous query event batch being reused asynchronously in the near-cache subscriber. |
| GG-44292 | Platforms & Clients | C++: Added a source-code distribution package for building on non-glibc or non-x86-64 Linux. |
| GG-42272 | General | Improved how nodes choose their advertised addresses on machines with more than one network interface. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.21`, `9.1.22`, `9.1.23`, `9.1.24`, `9.1.25`, `9.1.26`, `9.1.27`

When updating from older versions, we recommend updating to version `9.1.21` first, before performing an update to current version.

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://mariadb.com/support/.
