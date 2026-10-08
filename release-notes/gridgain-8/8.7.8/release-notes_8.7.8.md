---
description: >-
  GridGain 8.7.8 introduces hash joins, experimental partition awareness for thin
  clients, and major Data Center Replication improvements, along with many fixes.
hidden: true
---

# GridGain 8.7.8 Release Notes

## What's New in This Release

### Introduction

This release includes many improvements and introduces several new features covered below.

### New Features

- To boost the performance of join queries, GridGain now supports the [hash join algorithm](https://en.wikipedia.org/wiki/Hash_join).
Hash joins can be more efficient than nested loop joins in several scenarios, except for situations when the probe side of the join is
very small. However, hash joins can only be used with equi-joins - a type of join with equality comparison in the join predicate. For more details and usage examples, refer to the [Hash Joins](https://gridgain.com/docs/8.7.8/developers-guide/SQL/distributed-joins#hash-joins) documentation.

- C++ users can now create objects with fields of Enum type and store them in their GridGain cluster.

- We released an experimental version of the
[partition awareness](https://gridgain.com/docs/8.7.8/developers-guide/thin-clients/getting-started-with-thin-clients#partition-awareness)
feature that boosts the performance of the thin clients for .NET, C++, Python, and Node.js. The thin clients
become aware of the distribution of partitions in the cluster, which allows sending requests directly to the nodes that
keep primary copies of requested data. Partition awareness is also available for the
[JDBC Thin driver](https://gridgain.com/docs/8.7.8/developers-guide/SQL/JDBC/jdbc-driver#partition-awareness),
which can help optimize the performance of SQL queries.

### Improvements for Data Center Replication

#### Changes In Behavior

- The default implementation of the sender storage has changed from an in-memory store to a disk-based store. All updates in the master cluster are now stored on disk on the sender nodes before they are forwarded to the remote cluster. The directory on the file system where data updates are stored can be configured using the `DrSenderFsStore.directoryPath` property. The default value points to a directory inside the node's working directory. However, we recommend that you configure the directory explicitly.

  ```xml
  <bean class="org.gridgain.grid.configuration.DrSenderConfiguration">
      <!-- this node is part of group1 -->
      <property name="senderGroups">
          <list>
              <value>group1</value>
          </list>
      </property>
      <!-- connection configuration -->
      <property name="connectionConfiguration">
          <bean class="org.gridgain.grid.dr.DrSenderConnectionConfiguration">
              <!-- DR storage -->
              <property name="store">
                  <bean class="org.gridgain.grid.dr.store.fs.DrSenderFsStore">
                      <property name="directoryPath" value="/path/to/store"/>
                  </bean>
              </property>
              <!-- The ID of the remote cluster -->
              <property name="dataCenterId" value="2"/>
              <!-- Addresses of the remote cluster's receiver nodes -->
              <property name="receiverAddresses">
                  <list>
                      <value>172.25.4.200:50001</value>
                  </list>
              </property>
          </bean>
      </property>
  </bean>
  ```

- When the sender store gets full or corrupted, the replication process will stop.
You will have to start it manually and do a full state transfer after addressing the problem that caused the issue.

- The `GridDr.pause()`/`GridDr.resume()` methods are deprecated and replaced with `GridDr.stopReplication()`/`GridDr.startReplication()`.

  The `stopReplication()` method terminates the replication process, i. e. cache updates will stop being processed.

  The `startReplication()` method resumes the replication process, i. e. cache updates will start being processed again.
  Note that if during the break the data in the cache has changed, you will need to do a full state transfer.

- Added capability to pause/resume the replication process on the sender nodes. These operations can be performed via the JMX beans.

{% hint style="danger" %}
Do not confuse the pause/resume operations with the `GridDr.pause()`/`GridDr.resume()` methods, which have been
deprecated.
{% endhint %}

  Unlike the `GridDr.stopReplication()` method, the pause operation will not terminate the process; instead, the
  sender node where the method is called will stop sending the updates to the remote cluster.
  The updates will continue to be processed and will be accumulated in the sender storage on that node.
  To resume the process of sending the updates to the remote cluster, perform the resume operation on the sender node.

{% hint style="warning" %}
If you want to pause replication, you will have to pause and resume it on every sender node.
{% endhint %}

- Added adaptive throttling feature that, depending on the workload, allows for adjusting the data transfer rate between data nodes and sender nodes, and between sender nodes and receiver nodes

- Added several data replication event types. For the complete list of events, refer to the [DR Events](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication/managing-and-monitoring#data-replication-events) section.

- Added the ability to enable replication for existing caches.

### Removed/Deprecated

The `GridDr.pause()` and `GridDr.resume()` methods in the `GridDr` interface have been deprecated.
Use `GridDr.stopReplication()`/`GridDr.startReplication()` methods instead.

### H2 Database Engine Version Upgrade

H2 database engine is used to parse SQL and support execution of distributed SQL queries in GridGain. H2 ersion was upgraded from 1.4.197 to 1.4.199 and integrated as a separate module. This might lead to changes in SQL behaviour in certain cases, the list of known changes are:

- LIMIT/OFFSET keyword order in the SQL grammar cannot be changed now and is locked to `LIMIT expression [OFFSET expression]`

- INTERVAL type was introduced and is used as a return value type for arithmetic operations on date types. As an example, date subtraction was previously returning difference in days between two dates instead of complete time interval, which can be implemented now using DATEDIFF function. Please consider to replace arithmetic operations with corresponding function from Date and Time functions: https://apacheignite-sql.readme.io/docs/date-and-time-functions.

Please refer to http://www.h2database.com/html/changelog.html for versions 1.4.198 and 1.4.199 for the full list of changes.

## Installation and Upgrade Information

For information about how to perform automated upgrades and for details about version compatibility, see the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page.

### Upgrade from versions 8.4.4 and 8.4.5

There is a known compatibility issue found in version 8.7.8.

To upgrade from versions 8.4.4 or 8.4.5 to version 8.7.8, perform the following steps:

1. Stop one node and set the `IGNITE_PDS_WAL_REBALANCE_THRESHOLD` environment variable to `2147483647`; then start the node.
Repeat this procedure for all nodes in the cluster.
2. Then perform a regular rolling upgrade procedure.

## Known Issues

| Issue ID | Description |
| --- | --- |
| GG-25532 | There is a known vulnerability in the 'spark-ml-model-parser' module caused by the dependent library zookeeper v. 3.4.13. If you do not use this module, your cluster is not affected by this vulnerability. |
| GG-25828 | JDBC Driver version 8.7.7 cannot connect to cluster version 8.7.8 when authentication is enabled in the cluster. |
| GG-25723 | An attempt to change the baseline topology under load may raise a 'VisorIllegalStateException' exception. |

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| IGN-12835 | Cache | Improved speed of persistent node restart in case the node stopped during checkpoint. |
| IGN-11122 | Cache | All critical errors during tx commit failures are now handled by a failure handler. |
| IGN-11457 | Cache | Logical recovery phase is performed before a node joins the topology. |
| GG-19543 | Communication | Changed client reconnection logic to speed up the reconnect process in case of failures. |
| GG-18799 | Communication, Thin clients | Thin client: removed limitation of the length of credentials during handshake. |
| GG-18670 | Diagnostics | Added diagnostic tool of dumping WAL page history in case of B+Tree getting corrupted. |
| GG-18667 | Diagnostics | Added diagnostic ability for dumping page locks state like a thread dump. |
| GG-17442 | Diagnostics | List of files in the classpath is printed during the start of the node. It can be disabled by setting ignite system property `IGNITE_LOG_CLASSPATH_CONTENT_ON_STARTUP` to false. By default, it is enabled. |
| GG-14947 | Discovery | Client node cut off by communication from the rest of the cluster is stopped by Communication Failure Resolver. |
| IGN-7398 | JDBC Thin Driver | Added `Statement.cancel()` support. |
| IGN-7397 | JDBC Thin Driver | Added `Statement.setQueryTimeout()` support. |
| IGN-7193 | JDBC Thin Driver | Implemented `Connection.setNetworkTimeout` method. |
| GG-23437 | Rebalancing | Fixed the issue of resource utilization during rebalancing. |
| GG-18917 | Rebalancing | Rebalance properties were moved from CacheConfiguration to IgniteConfiguration level. Rebalance properties in CacheConfiguration were deprecated. |
| IGN-3517 | Storage Engine | Cache configurations are not explicitly deserialized on non-affinity nodes. |
| IGN-13624 | Storage Engine | Optimized amount of heap space used for affinity assignment history storing. |
| IGN-13478 | SQL | SqlQuery is deprecated. SqlFieldsQuery should be used instead. |
| GG-19125 | SQL | Added support for the row count statistics which helps with the local queries optimization. |
| GG-18538 | SQL | Supports hash index is built on the fly that is used for join when hash table can be placed in the memory. |
| IGN-12376 | SQL | Support partition pruning for SQL statements with joins. |
| IGN-8004 | SQL | Restricted DML execution when there is an active transaction over TRANSACTIONAL caches; can be overridden by using the `IGNITE_ALLOW_DML_INSIDE_TRANSACTION` system property. |
| GG-21272 | Transactions | Added ability to track system and user time for transactions. |
| GG-14890 | SQL | H2 database engine upgraded from 1.4.197 to 1.4.199. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-23261 | Data Center Replication | Default DrStore mode is changed to STOP. |
| GG-21367 | Data Center Replication | Added correctly named methods for DR start\stop methods. |
| GG-22491 | Data Center Replication | Added adaptive DR throttling. |
| GG-22626 | Data Center Replication | Added metrics to show DR sender/receiver pending queues size. |
| GG-21930 | Data Center Replication | Sender hub configuration uses a single port for localOutboundAddress. |
| GG-21368 | Data Center Replication | Fixed broken DR pause\resume semantic. |
| GG-12739 | Data Center Replication | Fixed data center replication for caches created via DDL. |
| GG-22661 | Data Center Replication | A file-system based implementation of Sender Store is now used by default. It has a default work directory, but we recommend to configure it explicitly for production environments. |

### GridGain Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-13635 | Snapshots | Added the ability to disable automatic snapshot creation after baseline changes. The behavior can be configured via `GG_DISABLE_SNAPSHOT_ON_BASELINE_CHANGE_WITH_ENABLED_PITR` parameter. |
| GG-13330 | Snapshots | Added `-check` option to `CATALOG` command. |
| GG-14095 | Snapshots | Fixed the issue when `MOVE` and `COPY` snapshot operation could be interrupted in the middle of the process if a large file was copied. |

## Related Information

Need more details? Please don't hesitate to reach out to the
GridGain Customer Support team.

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and
suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
