---
description: >-
  GridGain 8.7.15 adds memory quotas and query offloading, the .NET platform
  cache, protection against partition loss on shutdown, and communication with
  client nodes behind NAT, together with numerous fixes.
hidden: true
---

# GridGain 8.7.15 Release Notes

## New Features

**Memory Quotas and Query Offloading**

Memory Quotas prevent SQL queries from running out of memory. With memory quotas, the SQL engine doesn't allow a query to allocate more than a pre-configured amount of heap memory.
If the limit is reached, the query is either stopped or offloaded to disk depending on the configuration properties.
Refer to the [dedicated documentation section](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/memory-configuration/memory-quotas) for details.

**.NET Platform Cache**

.NET platform Cache is a cache that stores cache entries in a deserialized form in the CLR heap and improves performance of local operations from .NET clients.
Refer to the [.NET Platform Cache](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/net-specific/platform-cache) section.

**Preventing Partition Loss on Shutdown**

A [system property](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/starting-nodes#preventing-partition-loss-on-shutdown) was added to prevent partition loss on node shutdown.

**Communication with Client Nodes behind NAT**

An experimental option was added to enable a special mode of client-server communication when client nodes are deployed behind a NAT. Refer to the [Running Client Nodes Behind NAT](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/running-client-nodes-behind-nat) section for details.

## Known Issues

| Issue ID | Description |
|---|---|
| GG-28497 | The snapshot management tool requires incorrect permission (`ADMIN_CACHE`) when performing the CHECK operation. This will be fixed in the next release. |
| GG-28590 | If you rolling-upgrade from version 8.7.7 or earlier, you may see the following error in the log:<br>`class org.apache.ignite.IgniteCheckedException: Ignite cluster has nodes that don't support distributed metastorage feature. Writing cannot be completed.`<br>You can safely ignore this message. |

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-28131 | Communication | DNS reverse lookup will not be performed if node's 'localHost' property is set as an IP address. Add `IGNITE_TCP_COMM_SET_ATTR_HOST_NAMES=true` to the JVM startup options to return to old behavior (DNS lookup will be performed even if 'localHost' is set to an IP address). |
| GG-27306 | Communication | Added an ability to initiate client-server TCP connection from client side via discovery |
| GG-28241 | Control Script | Added the "--verbose" option to control.sh\|bat, which prints stacktrace when available. |
| GG-27458 | Control Script | Added "--check-sizes" option to the "validate_indexes" command to check whether index and cache size are equal. |
| GG-28383 | Metrics & Monitoring | Fixed incorrect calculation of the "indexBuildCountPartitionsLeft" metric. |
| GG-28088 | Metrics & Monitoring | Added histrogram metrics for get/put/remove cache operations. |
| GG-28445 | Platforms & Thin Clients | .NET: Use platform cache to execute local ScanQuery with partition. |
| GG-28305 | Platforms & Thin Clients | .NET: Added ICompute.WithExecutor. |
| GG-28303 | Platforms & Thin Clients | .NET Thin Client: Added ClusterGroup API. |
| GG-28251 | Platforms & Thin Clients | .NET: Added ICache.ClearStatistics, ICluster.ClearStatistics. |
| GG-27657 | Platforms & Thin Clients | .NET: Added ICache.EnableStatistics, ICluster.EnableStatistics. |
| GG-27289 | Platforms & Thin Clients | ODBC: SQLRowCount() now returns non-zero value for select queries. Returned value now depends on number of rows cached locally by driver. |
| GG-27288 | Platforms & Thin Clients | ODBC: Added support for cursor column-wise binding. This allows user application to fetch result set rows in batches (SQL_ATTR_ROW_ARRAY_SIZE > 1). |
| GG-27286 | Platforms & Thin Clients | ODBC: Some result set metadata such as returned by SQLNumResultCols() now can be called after SQLPrepare(), no need to call SQLExecute(). |
| GG-25083 | Platforms & Thin Clients | .NET: Added CLR heap caching layer. |
| GG-28149 | SQL | File-related SQL functions are now disabled. This does not affect the COPY command. |
| GG-28142 | SQL | OOM protection is now enabled by default. |
| GG-28007 | SQL | New columns to monitor memory usage were added to LOCAL_SQL_RUNNING_QUERIES and LOCAL_SQL_QUERY_HISTORY. |
| GG-26421 | SQL | Added a new field `INITIATOR_ID` to the `LOCAL_SQL_RUNNING_QUERIES` system view. This field indicates the originator of the query: thin client, JDBC/ODBC, compute task. |
| GG-28306 | SQL | New security permission 'SET_QUERY_MEMORY_QUOTA' was introduced to limit the scope of users who are able to modify memory quotas. |
| GG-28489 | Storage Engine | Baseline auto-adjust configuration methods were added to public API. |
| GG-28219 | Transactions | Deprecated `IgniteCache.lock()` family of methods in favor of Ignite.reentrantLock(). |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27933 | Snapshots & PITR | Fixed an issue when an incremental snapshot of a partition would always fail to be created, and a full snapshot would be taken instead. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Known Limitations

There is a compatibility issue that affects upgrade from version 8.7.13 and earlier to this version.
The issue affects GridGain Enterprise and Ultimate clusters with GridGain Authentication and Authorization enabled.
The issue will be fixed in a future version.
If your cluster is affected and you're planning to upgrade to this version, please contact GridGain Support for details.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
