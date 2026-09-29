---
description: GridGain 8.7.7 is a maintenance release that includes many bug fixes.
hidden: true
---

# GridGain 8.7.7 Release Notes

## What's New in This Release

This maintenance release includes many bugfixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-24944 | Affinity & Baseline Topology | Fixed bug with affinity history overflow when too many clients leave or join the cluster |
| GG-24971 | Architecture | Added EVT_PAGE_REPLACEMENT_STARTED event |
| GG-20604 | Atomic Cache | Fixed possible StackOverflowError in scenario with huge batch within one transaction |
| GG-24983 | Communication | No thread dumps for tcp-comm-worker thread appear in server logs when client node fails abruptly |
| GG-24975 | Communication | Fast fail of client reconnection to server node |
| GG-25022 | Control Script | Idle-verify cache-filter ALL will validate system caches, added cache-filter USER |
| GG-24981 | .NET | Fixed .NET continuous query "Removed" event registration |
| GG-24988 | Integrations | Upgrade jackson-databind library to version 2.9.9 |
| GG-24987 | Integrations | Upgraded Jetty dependency to 9.4.18 |
| GG-24980 | Integrations | Upgrade version of commons-codec library to 1.12 |
| GG-18901 | JDBC | JDBC Thin Driver: added Statement.setQueryTimeout() support. |
| GG-18900 | JDBC | JDBC Thin Driver: implemented Connection.setNetworkTimeout method. |
| GG-18899 | JDBC | JDBC Thin Driver: added Statement.cancel() support |
| GG-24984 | Platforms & Thin Clients | Thin client: removed limitation of the length of credentials during handshake |
| GG-24952 | Platforms & Thin Clients | Fixed OOM issue when invalid message was sent to thin client port |
| GG-24946 | Platforms & Thin Clients | CPP: Added EventType field to CacheEntryEvent |
| GG-24982 | Rebalance | Rebalance properties were moved from CacheConfiguration to IgniteConfiguration level. Rebalance properties in CacheConfiguration were deprecated. |
| GG-25023 | Security | Fix false-positive detection of cluster in not idle state with enabled security. |
| GG-24881 | Storage Engine | Fixed possible PDS corrupt during checkpoint |
| GG-24970 | Storage Engine | Fixed case when checkpoint tmp files were not removed on node start. |
| GG-14875 | SQL | Improve error's logging for DDL statements. |
| GG-24945 | SQL | Fix inconsistency between cache data and indexes when cache operation is interrupted |
| GG-24962 | SQL | Fixed cost estimation bug for tree indexes. |
| GG-24958 | Transactions | Added DR_ACK_MISSING_CACHES to allow DR make progress in case there are errors on receiver due to missing caches |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-24977 | DR | Clean DR state for destroyed caches |
| GG-24989 | DR | Deprecated and ignored GridGainCacheConfiguration.drReceiverEnabled flag due to invalid behavior |
| GG-24974 | DR | Fixed data center replication for caches created via DDL |
| GG-24960 | DR | Data Replication now uses file-system based implementation of Sender Store by default. It has default work directory, but it is recommended to configure it explicitly on production environments. |
| GG-24966 | DR | Adaptive DR throttling added |
| GG-25025 | DR | Improve error's logging for DDL statements. |
| GG-25025 | DR | Fixed deadlock between partition map exchange and initialization of DR component |
| GG-25020 | DR | DR: Add correctly named methods for DR start\stop. |
| GG-24991 | DR | Added events for DR |
| GG-24990 | DR | Added DR full state transfer operation to cache MBean |
| GG-24985 | DR | DR: Make debug logs more verbose. |
| GG-24969 | DR | Logging a errors happened during DR replication on remote DC |
| GG-24963 | DR | Added metrics to show DR sender/receiver pending queues size |
| GG-24959 | DR | Stop DR replication in case sender hub with in memory store went down |
| GG-24957 | DR | New method named 'resetState' has been added to DrSender interface. It resets all internal state of sender hub including clearing store and internal queues. |
| GG-24956 | DR | Change default DrStore mode to STOP. |
| GG-24955 | DR | Improve logging for the Data Center Replication component. |
| GG-24954 | DR | Prevent possible deadlock in DR during node left and cache stop in the same moment |
| GG-22622 | DR | Added ability to change full state transfer throttle per node at runtime |
| GG-22535 | DR | DR: delete files with successfully sent (ACK is received) data |
| GG-17339 | SQL | Fix memory leak at the JDBC thin driver caused by executing any statement |
| GG-25024 | SQL | Fixed memory leak on unstable topology caused by partition reservation |
| GG-24702 | WC | Web Console: Fixed issue with caches selection. |
| GG-24949 | Transactions | Fixed TTL not being transferred via DR |
| GG-24947 | Transactions | Fixed unexpected DR stop when client with default configuration connects to "drUseCacheNames=true" cluster |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
