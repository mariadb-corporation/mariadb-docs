---
description: GridGain 8.5.15 includes a number of critical bug fixes.
hidden: true
---

# GridGain 8.5.15 Release Notes

## What's New in This Release

This release includes a number of critical bugfixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Known Issues

We don't recommend configuring caches with ATOMIC and TRANSACTIONAL atomicity modes within one cache group. Such configurations will be forbidden in future releases.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-26748 | Binary Objects | Fixed an issue preventing copying of an enum field of BinaryObject without enum value deserialization. |
| GG-26311 | Deployment | The Scan Query Transformer class is now deployed using peer class loading when missing on server nodes. |
| GG-27218 | Diagnostics & Failure Handling | Added ability to enable extra logging for index rebuild process. Extra logging can be enabled by setting the IGNITE_ENABLE_EXTRA_INDEX_REBUILD_LOGGING system property to true. |
| GG-26735 | Diagnostics & Failure Handling | Added failure handler thread dump generation throttling to prevent continuous stop-the-world pauses. |
| GG-26711 | Diagnostics & Failure Handling | Fixed confusing failure handler log messages about ignored errors. |
| GG-26974 | Platforms & Thin Clients | C++: Added Clang compiler support. |
| GG-26812 | Security | Updated dependencies to address CVEs 2018-1000654, 2019-12900, 2019-14697. |
| GG-26793 | SQL | Added a warning when an index with the set of fields identical to those of an existing index is created. |
| GG-26634 | SQL | JDBC thin: SSL cipher suites can now be configured via the url parameter 'sslCipherSuites'. |
| GG-26629 | SQL | SQL execution threads are added to starvation monitoring subsystem to report threads that are potentially blocked for a configurable period of time. |
| GG-24265 | SQL | Optimized the deletion procedure for large SQL indexes. Deletion of a large index blocked the checkpointing operations and caused other operations to wait until the deletion is completed. Now large index deletion does not delay checkpointing. |
| GG-27194 | Storage Engine | Fixed an invalid assertion triggered by an intensive rebalancing leading to node crash. |
| GG-27151 | Storage Engine | Fixed a possible IgniteOutOfMemoryException when a large cache in a cache group is destroyed. |
| GG-26555 | Storage Engine | Fixed a bug which triggered full rebalancing instead of historical rebalancing when a client and server nodes concurrently join the cluster. |
| GG-26527 | Storage Engine | Fixed a bug causing an AssertionError after historical rebalancing is completed. |
| GG-22164 | Storage Engine | GridGain will now print all partitions that will be evicted with the eviction reason to the log. |
| GG-26092 | Storage Engine | Improved the performance of free list management. |
| GG-26838 | Transactions | Performance improvement for transactional caches in PRIMARY_SYNC mode. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-26948 | Data Replication | Fixed an issue where a server node configured as a sender did not replicate some data due to errors. |
| GG-26488 | Data Replication | Fixed incorrect DrFsStore size calculation. |
| GG-24268 | Data Replication | Data Replication sender and receiver metrics are now exposed via the JMX interface. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
