---
description: >-
  GridGain 9.1.25 introduces row-level security, adds experimental CDC support
  for Microsoft SQL Server as a source and a new GridGain 9 sink, and improves
  client data freshness.
---

# GridGain 9.1.25 Release Notes

## Overview

GridGain 9.1.25 introduces row-level security, adds experimental CDC support for Microsoft SQL Server as a source and a new GridGain 9 sink, and improves client data freshness.

## Major Changes

### Default Client Heartbeat Interval Reduced to 1 Second

The default thin-client heartbeat interval is reduced from 30 seconds to 1 second. More frequent heartbeats propagate the cluster's observable timestamp to idle client connections sooner, so reads issued after a period of inactivity observe fresher data. To keep the previous behavior, set the heartbeat interval explicitly when building the client.

## New Features

### Microsoft SQL Server CDC Source

{% hint style="warning" %}
This is an experimental feature. It may be changed in a later release.
{% endhint %}

GridGain 9.1.25 adds experimental support for using Microsoft SQL Server as a Change Data Capture source. Row changes captured by SQL Server native CDC are streamed into GridGain 9 tables in near real time using log sequence number-based polling. Both `NEW_DATA` (incremental) and `ALL` (initial snapshot, then incremental) replication modes are supported.

{% hint style="info" %}
Because the feature is experimental, creating or updating an `mssql` source requires the `--experimental` flag. Without it, the command fails.
{% endhint %}

```bash
cdc source create --name mssql_source --type mssql --tables dbo.ACCOUNTS \
  --parameters jdbcUrl="jdbc:sqlserver://localhost:1433;databaseName=testdb;encrypt=true;trustServerCertificate=true" \
  --parameters user=sa --parameters password=<password> \
  --experimental
```

See [Replicating from Microsoft SQL Server](../../administrators-guide/change-data-capture/change-data-capture.md#replicating-from-microsoft-sql-server-experimental) for setup steps, source parameters, and current limitations.

### GridGain 9 CDC Sink

{% hint style="warning" %}
This is an experimental feature. It may be changed in a later release.
{% endhint %}

This release also adds an experimental `gridgain_9` CDC sink that writes change events into an existing local GridGain 9 table: inserts and updates are applied as upserts, and deletes remove the corresponding rows. Together with the Microsoft SQL Server source, it enables replicating an external SQL Server database into GridGain 9. It can also serve as the destination for GridGain-to-GridGain replication.

{% hint style="info" %}
The `gridgain_9` sink does not create the destination table - the table must already exist with a compatible schema before replication starts. Set `targetTable` to a table different from the source table, otherwise replication fails to start. Because the sink is experimental, creating or updating it requires the `--experimental` flag.
{% endhint %}

```bash
cdc sink create --name gg9_sink --type gridgain_9 --parameters targetTable=PUBLIC.ACCOUNTS --experimental
```

See [GridGain 9 sink](../../administrators-guide/change-data-capture/change-data-capture.md#create-the-gridgain-9-sink) for details.

### Row-Level Security (RLS)

GridGain 9.1.25 introduces row-level security (RLS): per-table policies that restrict which rows a user can read or modify, enforced by the cluster across SQL, key-value, and scan access paths.

A policy is attached to a table, optionally scoped to one or more roles, and defines a boolean condition a row must satisfy for the user to see or change it. If no role is specified, the policy applies to everyone. Policies are managed with SQL:

```sql
-- The 'analyst' role can see only active ACCOUNTS rows
CREATE POLICY active_only ON ACCOUNTS TO analyst USING STATUS = 'ACTIVE';

-- Change the condition later
ALTER POLICY active_only USING STATUS = 'ACTIVE' AND REGION = 'EU';
```

Row filtering is applied consistently across read and write paths, including SQL queries, key-value and record views, table and index scans, continuous queries, the data streamer, and near caches.

The configured policies are exposed through the new [`POLICIES`](../../administrators-guide/metrics/system-views.md#policies) system view (schema, table, policy name, assigned roles, and condition).

See [Row-Level Security](../../administrators-guide/security/row-level-security.md) for the full policy syntax, the `POLICIES` system view, and the required privileges.

### Configurable Observable Timestamp Delay

A new node configuration property, `ignite.transaction.observableTimestampDelayMillis`, controls the delay subtracted from the current time when computing the observable timestamp used as the read timestamp for read-only transactions (`observableTimestamp = now - observableTimestampDelayMillis`). A larger delay lowers latency by letting clients read slightly older data (reducing the chance a request to a lagging node must wait for safe time to catch up); a smaller delay favors the freshest data. The default `-1` selects the delay automatically based on server configuration.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-49755 | Platforms & Clients | Fixed partition aware routing. Now node is chosen properly for the implicit client transaction instead of random node. |
| GG-49684 | General | Fixed a rare case that could lead to scan collision. |
| GG-49579 | Platforms & Clients | Client handler: Fixed pre-auth DoS via unbounded allocation in handshake. |
| GG-49421 | Cluster Data Replication | Replication of a table that outlasts the source's data-history retention now fails with a clear, actionable error instead of an opaque WATERMARK_TOO_OLD_ERR. |
| GG-49399 | Cluster Data Replication | Fixed DR connector failure on tombstone replication retry. |
| GG-49244 | CLI Tool | Fixed garbled EXPLAIN plan output in the GG9 CLI. |
| GG-49171 | Platforms & Clients | Added the ignite.transaction.observableTimestampDelayMillis configuration property to adjust the data freshness versus latency tradeoff. |
| GG-49164 | Platforms & Clients | Removed exception about failed transaction rollback in the C++ client in case of client close due to connectivity loss or cluster restart. |
| GG-49143 | Platforms & Clients | Reduced default client heartbeat interval from 30s to 1s to improve causality token freshness on idle connection. |
| GG-49140 | General | Fixed a scenario that caused hangs under high contention. |
| GG-49086 | Cluster Data Replication | Added experimental support for Microsoft SQL Server as a CDC source and a GridGain 9 CDC sink, gated behind the `--experimental` flag. |
| GG-48986 | Cluster Metrics & Monitoring | Added partition files size metrics. |
| GG-48969 | Cluster Storage Engine | Added outgoingSnapshotsThreadPoolSize configuration property to control the number of threads handling Raft snapshots. |
| GG-48771 | General | Reduced latency of read-only reads from primary replica. |
| GG-48740 | Platforms & Clients | JDBC connections now support a transactionTimeoutMillis property. |
| GG-48735 | General | Added a log hint about recovering a cluster when license has expired. |
| GG-48676 | Platforms & Clients | Fixed client buffer offset corruption in certain high load scenarios. |
| GG-47761 | Cluster Continuous Queries | Continuous Query: added overload with CancellationToken. |
| GG-47738 | Cluster SQL Engine | Added EXPIRE_COLUMN_NAME, ARCHIVE_COLUMN_NAME, PROPERTIES columns to TABLES system view. |
| GG-45513 | Cluster Data Snapshots and Recovery | Snapshot now save and restore table row-security policies. |
| GG-43745 | Cluster Security | Added row-level security (RLS): define per-table row access policies with SQL `CREATE`/`ALTER POLICY`, gated by the `ROW_SECURITY` license feature. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.20`, `9.1.21`, `9.1.22`, `9.1.23`, `9.1.24`

When updating from older versions, we recommend updating to version `9.1.20` first, before performing an update to current version.

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
