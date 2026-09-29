---
description: >-
  GridGain 8.7.14 adds transaction support and certificate-based authentication
  to thin clients, baseline topology autoadjustment, and the FIRSTVALUE and
  LASTVALUE SQL functions, and removes the ML modules from the distribution.
hidden: true
---

# GridGain 8.7.14 Release Notes

## New Features

This release introduces the following features.

**Transaction Support in Java Thin Client**

Java thin client now supports the transaction API. Client transactions are similar to the Transaction API in GridGain core functionality and can be executed with different concurrency modes and isolation levels.
Refer to the [Transactions](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/java-thin-client#transactions) section for additional information.

**Certificate-based Authentication/Authorization for Thin Clients**

The thin clients can now use [SSL certificate-based authentication/authorization](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication#client-certificate-authentication). The information about the user is extracted from the certificate fields.

**Baseline Topology Autoadjustment**

There are two important changes related to baseline topology:

- Automatic baseline updating
- Introduction of baseline for in-memory caches

Automatic baseline adjustment provides an automated mechanism for updating a cluster's baseline topology without the need for manual intervention. In other words, the cluster monitors the state of its server nodes and sets the baseline on the current topology automatically when the cluster topology is stable for a configurable period of time.
Refer to the [Baseline Topology Autoadjustment](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/baseline-topology#baseline-topology-autoadjustment) section for details.

**New SQL Functions: FIRSTVALUE and LASTVALUE**

Two new aggregate functions were added:

- `FIRSTVALUE ([DISTINCT] <expression1>, <expression2>)` — returns the value of `expression1` associated with the smallest value of `expression2` in each group defined by the `group by` expression in the query. Refer to the [FIRSTVALUE](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/aggregate-functions#firstvalue) section for details.
- `LASTVALUE ([DISTINCT] <expression1>, <expression2>)` — returns the value of `expression1` associated with the largest value of `expression2` in each group defined by the `group by` expression in the query. Refer to the [LASTVALUE](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/aggregate-functions#lastvalue) section for details.

For example, the following query returns the list of companies and the youngest and oldest person in each company:

```sql
select company_id, firstvalue(name, age) as youngest, lastvalue(name, age) as oldest from person group by company_id;
```

## Removed/Deprecated

**GridGain ML Modules**

The GridGain ML modules were removed from the distribution package and can now be downloaded as a separate archive from https://gridgain.com/resources/download#extensions.
Refer to the [GridGain Machine Learning documentation](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/machine-learning/ml) for details.

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-21030 | Atomic Cache | Rebalancing of a cache will not be canceled in case of events that do not change partition assignment. |
| GG-27936 | Control Script | CRC check of pages is now performed only when a special flag (--check-crc) is passed to the `validate_indexes` command. |
| GG-27837 | Deployment | Fixed assertion error when unmarshalling a message from a failed node. |
| GG-21949 | Diagnostics & Failure Handling | Improved node start-up and periodic metrics logging. |
| GG-27929 | Discovery | Fixed an issue that caused TCP discovery to get stuck in reading from socket operation. |
| GG-27990 | ML | ML examples have been extracted to a separate module. |
| GG-27931 | Platforms & Thin Clients | Fixed .NET logging warnings for nullable signed primitives that could lead to runtime errors. |
| GG-24207 | Platforms & Thin Clients | Added transaction support to Java thin client. |
| GG-27882 | Security | Added support for client authorization using SSL certificates. |
| GG-27813 | SQL | Fixed hanging of the KILL QUERY command when original query cursor is left open. |
| GG-27648 | SQL | Fixed an issue where the `enforceJoinOrder` flag was ignored when one of the previous queries had the same SQL text and a different value of the flag. |
| GG-27604 | SQL | Fixed handling of the DATE, TIME, TIMESTAMP types in JDBC thin client when nodes and clients are launched in different time zones. |
| GG-27597 | SQL | Added a thread pool to create and rebuild indexes. Removed the `INDEX_REBUILDING_PARALLELISM` system property and added the `IgniteConfiguration#setBuildIndexThreadPoolSize` configuration property. |
| GG-27508 | SQL | Added supports of lazy mode for UPDATE / DELETE queries (may reduce memory consumption in some cases). |
| GG-27159 | SQL | Fixed an issue with executing distributed joins when the number of joined tables is more than 7. |
| GG-27130 | SQL | Fixed query cursors leak when JDBCv2 is used. |
| GG-23822 | SQL | Added FIRSTVALUE and LASTVALUE SQL aggregate functions. |
| GG-21884 | SQL | Two new metrics have been added: sql.parser.cache.hits - the number of hits for queries cache, and sql.parser.cache.misses - the number of misses for queries cache. |
| GG-28104 | Storage Engine | Added the `IGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN` system property to prevent unsafe node termination. |
| GG-27583 | Storage Engine | Fixed partition desynchronization after rebalancing if a partition was remapped to a historical supplier which lost the history. |
| GG-27526 | Storage Engine | Fixed corruption during high-intensity load on a cache with enabled TTL. |
| GG-27741 | Storage Engine | Optimized node recovery procedure. |
| GG-28109 | Transactions | Fixed a bug that could possibly cause a deadlock on concurrent putAll invocations. |
| GG-27941 | Transactions | The "Too many open files" error for socket connection now triggers a critical failure to prevent the cluster from hanging. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27264 | Data Replication | Added additional information about running full state transfer processes to `CacheDrStateTransfer`, which can be obtained via `GridDr.listStateTransfers()`. |
| GG-26639 | Data Replication | Introduced a synchronous full-state transfer mode with a separate in-memory buffer. |
| GG-27706 | Data Replication | Fixed an issue when a new sender node joining the cluster could cause the full state transfer to lose data. |
| GG-28062 | Snapshot utility | The `idle_verify` option was removed from the snapshot utility, use `control.sh --cache idle_verify` instead. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.4`, `8.5.5`, `8.5.5-p3`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.2`, `8.7.2-p12`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`

### Known Limitations

There is a compatibility issue that affects upgrade from version 8.7.13 and earlier to this version.
The issue affects GridGain Enterprise and Ultimate clusters with GridGain Authentication and Authorization enabled.
The issue will be fixed in a future version.
If your cluster is affected and you're planning to upgrade to this version, please contact GridGain Support for details.

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
