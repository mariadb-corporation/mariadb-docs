---
description: >-
  GridGain 8.7.4 is a maintenance release that adds on-the-fly service redeployment, cluster activation and deactivation events, JMX node exclusion, and JAR support in UriDeploymentSpi.
hidden: true
---

# GridGain 8.7.4 Release Notes

## What's New in This Release

### Introduction

This maintenance release includes many bug fixes, updates, and improvements to GridGain. In addition to the Fixed Issues, this release includes:

- Added support for redeploying services on the fly.
- Added events on cluster activation and deactivation.
- Added JMX ability to exclude nodes from topology.
- Added support of JAR files to `UriDeploymentSpi`.
- Updated Cassandra Store Driver version to 3.2
- Better Java 11 support.
- Several improvements and fixes for Web Console.
- Improved performance and stability (memory leak fixes, fixes for SQL, indexes, etc.)

### Changes in Behavior

#### Services Redeployment and JAR File Support

Now you can redeploy services on the fly (without having to restart the node) via
[DeploymentSpi](https://apacheignite.readme.io/docs/deployment-spi).

If you have a service in a cluster and you want to update its implementation:

1. Update the JAR file(s) in the repository where the service is stored (pointed to by your
`UriDeploymentSpi` configuration's `uriList` property).
2. Call the `services().cancel()` method to stop the service.
3. Redeploy the service.

This is the same process currently used to redeploy tasks. For more information, see
[Service Updates (Redeployment)](https://apacheignite.readme.io/docs/service-grid-28#service-updates-redeployment).

{% hint style="info" %}
As part of this change, `UriDeploymentSpi` now supports JAR files.
{% endhint %}

#### Fixed: Dynamic Changes to Cache Configurations (IGNITE-11541)

Prior to version 8.7.4, if you had a cache configured via XML configuration and changed it dynamically with a
DDL statement (for example, alter a table or create/drop indexes), restarting the node would cause the cache to
load its configuration from the XML configuration, ignoring the changes made dynamically.

If you have changed a cache configuration dynamically and have to restart a node, there are a couple of workarounds
to the issue described above:

Remove the cache configuration from the configuration file before restarting the node. In this case the cache
configuration will be loaded from the metadata.
Change the XML configuration the same way you changed the cache dynamically. For example, if you dropped a column,
remove that column from the cache configuration.

Beginning in version 8.7.4, changes made dynamically will persist after a node restart. If you want to keep the
old behavior (i.e. always load static cache configuration after a restart), add the following property to the
node's startup command:

`-DIGNITE_KEEP_STATIC_CACHE_CONFIGURATION=true`

## Installation and Upgrade Information

See the [Rolling Upgrades](https://docs.gridgain.com/docs/rolling-upgrades) page for information about how to
perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| IGN-13796 | Cache | Fixed possible PME hang on concurrent coordinator fail and client join. |
| IGN-13792 | Cache | Fixed transaction hang when sessionEnd throws an exception. |
| IGN-13516 | Cache | Fixed: `cache.get()` sporadically returns 'null' if a remove with skip store is invoked concurrently. |
| IGN-13293 | Cache | First node in new cluster filters out cache configurations received from old cluster. |
| IGN-12977 | Cache | Reduced memory footprint and allocation pressure of affinity assignments. |
| IGN-11847 | Cache | Fixed possible failure during async partition cleanup. |
| IGN-6961 | Cache | Fixed hanging parallel write&evict in `CacheWriteBehindStore`. |
| GG-17479 | Cache | Fixed memory leak on unstable topology caused by partition reservation. |
| IGN-13811 | Cassandra Integration | Fixed missing dependencies in cassandra-store module. |
| IGN-13137 | Communication | Fixed SSL bug when ignite concurrently sends message and close GridNioSession. |
| IGN-13030 | Compute Grid | Fix deserialization error of cache metrics with `OptimizedMarshaller`. |
| IGN-12385 | Control Utilities | Fixed invalid message for control.sh utility when removing node from baseline on an inactive cluster. |
| IGN-10934 | Control Utilities | Added coordinator information to control.sh output. |
| IGN-12317 | Data Structures | Fixed sporadic IgniteQueue hang caused by an incorrect CQ listener notification logic. |
| IGN-13527 | Deployment | Add support of JAR files to `UriDeploymentSpi`. |
| IGN-13540 | Diagnostic | Improved LRT diagnostic messages: now request from local node is sent to near node to get the dump of a thread that started the transaction. |
| IGN-13466 | Diagnostic | Added consistentId to "Node FAILED" message. |
| IGN-13290 | Diagnostic | Improved error message with advice about required JVM parameters for Java 9+. |
| IGN-8573 | Diagnostic | Added limit of diagnostic warnings. |
| IGN-13611 | Discovery | Fixed race on client re-connection that can lead to client segmentation. |
| IGN-13543 | Discovery | Fixed infinite 'no next node in topology' loop in `TcpDiscoverySpi`. |
| IGN-13509 | Discovery | Implemented: healthy node must ignore a list of failed nodes received from segmented nodes. |
| IGN-13430 | Discovery | Fixed detection of leaving server nodes if SSL is on. |
| IGN-13404 | Discovery | Data packet will be compressed on joining nodes to topology. |
| IGN-13184 | Discovery | `TcpDiscoverySpi` discard queue heap usage optimization. |
| IGN-13334 | Discovery | Added additional logging for client-server connections in TCP-discovery. |
| IGN-13145 | Discovery | Improve join process, when marshaller's folder has many files. |
| IGN-13040 | Discovery | Fixed 'Invalid node order' assertion in discovery. |
| IGN-13038 | Discovery | Fixed potential discovery hang when a joining node receives a client reconnect message. |
| IGN-7529 | Discovery | Node considered failed by cluster is forced to shut down when sending another Join Request. |
| IGN-12732 | General | Fixed node hanging in case node is stopped right after start and concurrent grid utility client connecting. |
| IGN-13116 | Metrics & Monitoring | Added `getTotalUsedPages` property for DataRegionMetrics, which shows the total number of pages used for storing the data. |
| IGN-12198 | Metrics & Monitoring | Provided description for `org.apache.ignite.mxbean.TransactionMetricsMxBean`. |
| IGN-8559 | Metrics & Monitoring | CacheSize cluster metrics now aggregates all nodes local metrics. |
| IGN-13721 | Partition Map Exchange | Fixed PME hang on coordinator failure. |
| IGN-13341 | Partition Map Exchange | Fixed PME hang when merged exchange node leaves before sending single message. |
| IGN-13260 | Partition Map Exchange | Fixed uncaught exception in TTL during PME. |
| IGN-12976 | Partition Map Exchange | Apply affinity changes on coordinator in multi-threaded mode. |
| GG-17327 | Partition Map Exchange | Avoid keeping metrics-related data in exchange history. |
| IGN-13783 | Persistence | Fixed case when index rebuild broke consistency between partition and index itself. |
| IGN-13704 | Persistence | Static cache configuration should not override persisted cache configuration. |
| IGN-13699 | Persistence | Information about possible long GC pauses during waiting and holding checkpoint write lock. |
| IGN-13645 | Persistence | Pages processing moved to isolated ForkJoinPool. |
| IGN-13033 | Persistence | Avoid to start WAL compressor in recovery mode. |
| IGN-12806 | Persistence | Reduced checkpoint write lock hold time by optimistically saving metadata outside of checkpoint write lock. |
| IGN-10411 | Persistence | Support events on cluster activation and deactivation. |
| IGN-13814 | Persistence | Fixed unsuccessful node recovery after incomplete WAL write when no-archiver mode is enabled. |
| IGN-13813 | Persistence | Fixed NPE on node startup with enabled PDS and SSL. |
| GG-17383 | Platform..NET | Added .NET Core framework dependent binaries and .NET Docker image |
| IGN-13051 | Plugins | Added discovery data to `PluginProvider.validateNewNode`, deprecated old method. |
| GG-14807 | Security | Avoid to remove expired session from cache if cluster deactivated. |
| IGN-13951 | SQL | SQL: Fixed memory leak in connection manager. |
| IGN-13641 | SQL | Fixed races on mvcc cache start-up. |
| IGN-13818 | SQL | Fixed deserialization issue during DELETE query execution. |
| IGN-13286 | SQL | Fixed potential memory leak. |
| IGN-13093 | SQL | Fixed TransactionException handling in mvcc mode. |
| IGN-12973 | SQL | Fixed indexes corruption on node stop under load. |
| IGN-12661 | SQL | Fix failure after node restart with mvcc cache and persistence enabled. |
| IGN-12637 | SQL | Fixed broken rebalance for MVCC caches. |
| IGN-12447 | SQL | Fixed query exception handling. |
| IGN-12429 | SQL | MVCC: Fix EntryProcessor P2P deployment. |
| IGN-11361 | SQL | Automatic deadlock detection and resolution for MVCC caches |
| IGN-13306 | Transactions | Fixed assertion error in preparing state transaction. |
| GG-17328 | Transactions | Fixed memory leak in the `GridCacheTxFinishSync#threadMap`. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-17490 | Data Center Replication | Fixed possible deadlock at startup in DR. |
| GG-13166 | Rolling Upgrade | Added version information in rolling update compatibility message. |

### GridGain Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| IGN-13709 | Point-in-Time Recovery | Fixed page store corruption that may be caused by early file downloader close during PITR. |
| GG-14526 | Point-in-Time Recovery | Attempt to PITR recovery with list of caches lead to exception. |
| GG-14777 | Snapshots | Fixed: issue with hanging automatic snapshot when system property is set inconsistent in the cluster. |
| GG-14733 | Snapshots | Fixed: Incremental snapshot fails if checkpointer writes pages of partition which was empty on snapshot start. |
| GG-14708 | Snapshots | Fixed: zero-sized partition file created in snapshot for an empty cache or cache group. |
| GG-14662 | Snapshots | Output of all password arguments in snapshot-utility are masked. |
| GG-14587 | Snapshots | Snapshot utility now logs hostname and IP-address of node from which it was launched. |
| GG-13944 | Snapshots | Fixed assertion error of on snapshot cancel command. |

### Management and Monitoring Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-14568 | Visor GUI | Implemented queries cancellation. |
| IGN-13476 | WebConsole | Added ability to exclude node from topology via JMX beans. |
| IGN-13462 | WebConsole | Changed scaling on mobile devices. |
| IGN-13226 | WebConsole | Web Agent: Implemented support for "--disable-demo". |
| IGN-13112 | WebConsole | Implemented queries cancellation. |
| IGN-13071 | WebConsole | Added more countries. |
| IGN-12614 | WebConsole | Refactored all screens to show "no-data" message instead of blocking modal. |
| GG-17784 | WebConsole | Fixed usability issue when cluster has caches with groups. |
| GG-17375 | WebConsole | Implemented support for Mongo 4.x and latest Ubuntu. |
| GG-14863 | Visor GUI | Fixed creation of snapshot in case when PITR is enabled. |
| GG-14745 | Visor | Added user login to "Visor connected" message. |
| GG-14135 | Visor GUI | Disconnect from secure cluster if cluster was restarted or user idle. |
| GG-18487 | WebConsole | Added missing DR properties on "Configuration" screen. |
| GG-18320 | WebConsole | Updated landing page with new design. |
| GG-17758 | WebConsole | Fixed snapshot availability detection logic. |
| GG-14633 | Visor GUI | Fixed "Snapshots" tab refresh logic. |
| GG-18097 | WebConsole | Added confirmation on changing snapshot schedule enabled state. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://apacheignite.readme.io/docs) for more information.
