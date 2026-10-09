---
description: >-
  GridGain 8.5.8 is a maintenance release with many bug fixes, improved
  messaging, monitoring, and logging, memory-leak and performance fixes, and
  several Web Console improvements.
hidden: true
---

# GridGain 8.5.8 Release Notes

## What's New in This Release

### Introduction

This maintenance release includes many bug fixes, updates, and improvements to GridGain. In addition to the Fixed Issues, this release includes:

- Improved/augmented messages, monitoring, and logging for various components.
- Fixed memory leaks, improved performance.
- Several improvements to Web Console (see [Management and Monitoring Changes](#management-and-monitoring-changes) below).

### Changes in Behavior

#### Detailed Transaction Information Flag

We added a new flag (`--tx --info <id>`) to the `control.sh|bat` command to get additional information about a specified transaction.

`<id>` can be any single transaction identifier in one of several formats. `xid` or `nearXid` can be passed as GridCacheVersion or UUID.

`control.sh --tx --info 2abc7b6aa61-00000000-0a13-93b4-0000-000000000007`

`control.sh --tx --info GridCacheVersion [topVer=169335904, order=1557855907152, nodeOrder=3]`

The information returned includes:

1. Initiator node
2. Transaction parameters: isolation, concurrency, timeout, topology version on which the transaction is/was executed, used caches and groups, transaction states (which can differ across the cluster)
3. Transaction topology (affected nodes):
   - Transaction mappings
     - Each node can handle several mappings where a mapping is a subset of keys affected the by transaction. A mapping can be either:
       - NEAR - local node is a transaction initiator
       - DHT - current keys subset belongs to primary partitions
       - REMOTE - current keys subset belongs to backup partitions
     - Dependencies between mappings (e.g. each REMOTE mapping has primary node which owns the same keys in primary partitions)
     - Mapped keys for each mapping and their parameters. Mappings include:
       - Affected keys
       - Their type of access (can be write or read) and their lock ownership status (can be either NO_LOCK - lock is not acquired yet, OWNS_LOCK - key lock is acquired by requested transaction and AWAITS_LOCK - means transaction is waiting for when another transaction will release lock for corresponding key). Example: `Write [lock=OWNS_LOCK]: IgniteTxKey [key=KeyCacheObjectImpl [part=108, val=108, hasValBytes=true], cacheId=1544803905]`

This can also work for transactions that have already finished. If the specified transaction persists in the commit/rollback history, all occurrences of the transaction will be printed to output. Example:

{% code title="Output" %}
```text
Control utility [ver. 2.7.0-SNAPSHOT#20190415-sha1:DEV]
2019 Copyright(C) Apache Software Foundation
User: JUser
Time: 2019-05-15T04:44:48.586
--------------------------------------------------------------------------------
Active transactions not found.
Will try to peek history to find out whether transaction was committed / rolled back.
Transaction was found in completed versions history of the following nodes:
TcpDiscoveryNode [id=b0168b23-ff69-41e6-a044-8ce189800000, addrs=[127.0.0.1], order=1, ver=2.7.0#20190415-sha1:00000000, isClient=false, consistentId=bltTest0]:
State: COMMITTED
TcpDiscoveryNode [id=cc9953a2-2a3e-47c3-83c8-329259900001, addrs=[127.0.0.1], order=2, ver=2.7.0#20190415-sha1:00000000, isClient=false, consistentId=bltTest1]:
State: COMMITTED

...
```
{% endcode %}

## Known Issue

There's a compatibility issue between 8.5.8 and version 8.4.4.

Issue GG-18858: The file `<dbpath>/<cache_name>/cache_data.dat` is not deleted on 8.4.4 on IgniteEx#destroyCache0.

**Workaround**: Do not execute DROP TABLE queries and do not destroy caches when performing a rolling upgrade from 8.4.4 to 8.5.8.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://docs.gridgain.com/docs/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| IGN-13929 | Cache | Avoid potential `ClassNotFoundException` when replacing null value. |
| IGN-13811 | Cache | Fixed missing dependencies in cassandra-store module. |
| IGN-13594 | Cache | Fixed issue with TTL manager sometimes not cleaning entries from the underlying store. |
| IGN-13516 | Cache | Fixed: `cache.get()` sporadically returns 'null' if a remove with skip store is invoked concurrently. |
| IGN-6961 | Cache | Fixed hanging parallel write&evict in `CacheWriteBehindStore`. |
| GG-18877 | Communication | No thread dumps for tcp-comm-worker thread appear in server logs when client node fails abruptly. |
| IGN-13950 | Control Utilities | Improved error message when connecting to secured cluster without credentials. |
| GG-17426 | Control Utilities | Fixed exception when snapshot-utility accesses a file of zero size. |
| GG-17344 | Control Utilities | Idle-verify: cache-filter 'ALL' will validate system caches, added cache-filter 'USER'. |
| IGN-12317 | Data Structures | Fixed sporadic `IgniteQueue` hang caused by an incorrect CQ listener notification logic. |
| IGN-13891 | Deployment | Fixed an issue with loading different class loaders through p2p. |
| IGN-13699 | Diagnostic | Added Information about possible long GC pauses during waiting and holding checkpoint write lock. |
| IGN-13540 | Diagnostic | Improved LRT diagnostic messages: now request from local node is sent to the nearest node to get the dump of a thread that started the transaction. |
| IGN-13466 | Diagnostic | Added `consistentId` to "Node FAILED" message. |
| IGN-13334 | Diagnostic | Added additional logging for client-server connections in TCP-discovery. |
| IGN-13276 | Diagnostic | Added `--tx --info` command which provides the ability to retrieve verbose information about a specific transaction: key lock ownership, state and topology. See [Detailed Transaction Information Flag](#detailed-transaction-information-flag). |
| GG-14951 | Diagnostics & Failure Handling | Improvements in checking to see if an Exchange worker is alive. |
| GG-14950 | Diagnostics & Failure Handling | Added configuration parameters for checking to see if system workers are alive. |
| GG-14857 | Diagnostics & Failure Handling | Added monitoring of critical system workers. |
| IGN-13543 | Discovery | Fixed infinite 'no next node in topology' loop in `TcpDiscoverySpi`. |
| IGN-13131 | Discovery | Grid components of a joining node are initialized with configurations from the grid at the end of join. |
| GG-18567 | Discovery | Fixed compatibility with old versions. |
| IGN-13116 | Metrics | Added `getTotalUsedPages` property for `DataRegionMetrics`, which shows the total number of pages used for storing the data. |
| IGN-13260 | Partition Map Exchange | Fixed uncaught exception in TTL during partition map exchange. |
| GG-17327 | Partition Map Exchange | Avoid keeping metrics-related data in exchange history. |
| GG-18846 | Persistent Storage (WAL, Recovery) | Fixed "Compression of WAL segment was skipped due to unexpected error" spam on node start when WAL compaction enabled. |
| GG-18738 | Persistent Storage (WAL, Recovery) | Fixed possible data storage corruption on start in no-WAL-archiver mode. |
| GG-18736 | Persistent Storage (WAL, Recovery) | Introduced `SYSTEM_CRITICAL_OPERATION_TIMEOUT` failure type. |
| GG-18860 | Platform .NET | Fixed LINQ support for .NET Core 2.1. |
| IGN-13941 | Rebalance | Fixed node distribution of demanded cache partitions during rebalancing. |
| GG-18587 | Security | Fix false-positive detection of cluster in not idle state with enabled security. |
| GG-17465 | Security | Fixed false-positive detection of cluster in not idle state with enabled security. |
| GG-14807 | Security | Avoid removing expired session from cache on a deactivated cluster. |
| IGN-13951 | SQL | Fixed memory leak in connection manager. |
| IGN-13783 | SQL | Fixed case when index rebuild broke consistency between partition and index itself. |
| IGN-13704 | SQL | Static cache configuration should not override persisted cache configuration. |
| GG-18857 | SQL | Fixed example `CacheClientBinaryQueryExample`. |
| GG-17434 | SQL | Fixed memory leak on unstable topology caused by partition reservation. |
| GG-17339 | SQL | Fixed memory leak at the JDBC Thin Driver caused when executing any statement. |
| GG-17326 | SQL | Removed field from internal stored schema properly when the DROP COLUMN statement is executed. |
| GG-14963 | SQL | Fixed hang on cancel query when the query is executed in `lazy` and `distributed joins` modes. |
| GG-14873 | SQL | Avoid key/val ownership resolution of a field in runtime. |
| IGN-13002 | Tooling | Added ability to use multiple cache filter options for `idle_verify` command simultaneously, also support for using regular expressions instead of cache names. |
| IGN-13792 | Transactions | Fixed transaction hang when `sessionEnd` throws an exception. |
| IGN-13624 | Transactions | Optimized amount of heap space used for affinity assignment history storing. |
| IGN-13286 | Transactions | Fixed potential memory leak. |
| IGN-12198 | Transactions | Provided description for `org.apache.ignite.mxbean.TransactionMetricsMxBean`. |
| GG-17488 | Transactions | Fixed memory leak in the `GridCacheTxFinishSync#threadMap`. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-17429 | Data Center Replication | Fixed deadlock between partition map exchange and the initialization of the Data Center Recovery component. |

### GridGain Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-18658 | Point-in-Time Recovery | Fixed null pointer exception in logs when server nodes leave cluster during snapshot. |
| GG-14777 | Point-in-Time Recovery | Fixed: issue with hanging automatic snapshot when system property is set inconsistent in the cluster. |
| GG-14760 | Point-in-Time Recovery | Fixed possible hang on snapshot operation. |

### Management and Monitoring Changes

| Issue ID | Category | Description |
|---|---|---|
| IGN-12276 | Web Console | Improved support for JDBC drivers on project generation. |
| GG-18097 | Web Console | Added confirmation on changing snapshot schedule enabled state. |
| GG-18011 | Web Console | Added column with node type: coordinator/server on "Baseline" screen. |
| GG-17784 | Web Console | Fixed usability issue when cluster has caches with groups. |
| GG-18511 | Web Console | Added "Pause/Resume/Bootstrap" actions on "Data Center Replication" screen. |
| GG-17375 | Web Console | Implemented support for Mongo 4.x and latest Ubuntu. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
