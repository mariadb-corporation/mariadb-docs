---
description: >-
  GridGain 9.1.26 tightens access control for administrative operations, changes
  how read-only SQL queries are routed, and adds cluster-wide and per-statement
  control over follower reads.
---

# GridGain 9.1.26 Release Notes

## Overview

GridGain 9.1.26 tightens access control for administrative operations, changes how read-only SQL queries are routed, and adds cluster-wide and per-statement control over follower reads.

## Major Changes

### New Permissions Required for Administrative Operations

Several administrative operations that previously required no dedicated privilege are now protected by role-based access control. The following actions were added:

| Action | Required for |
|---|---|
| `WRITE_SECURITY_CONFIG` | Modifying the cluster security configuration subtree. |
| `MANAGE_DCR` | Managing data center replication. |
| `RENAME_CLUSTER` | Renaming the cluster. |
| `ENABLE_METRICS`, `DISABLE_METRICS`, `LIST_METRICS` | Enabling, disabling, and listing cluster metrics. |

When you upgrade a cluster to 9.1.26, the built-in `system` role receives the new actions automatically, so a user with that role keeps full access to the operations listed above.

Custom roles are not updated. A role that holds `WRITE_CLUSTER_CONFIG`, for example, can no longer modify the cluster security configuration until you also grant it `WRITE_SECURITY_CONFIG`, and the first attempt to do so after the upgrade fails with an authorization error.

Review your roles before upgrading and grant the new actions to the roles that need them:

```sql
GRANT PRIVILEGES WRITE_SECURITY_CONFIG TO cluster_admin;
```

See [GRANT](../../sql-reference/access-control.md#grant-to-role) for the statement syntax, and [User Permissions and Roles](../../administrators-guide/security/permissions.md) for the full list of actions.

### SQL Follower Reads Disabled by Default

Read-only SQL queries no longer read from non-primary replicas by default. In earlier releases, every read-only SQL query could be served by any replica of a partition. Starting with this release, such queries are mapped to primary replicas only, governed by the new cluster-wide [`sql.allowFollowerReads`](../../administrators-guide/config/cluster-config.md#sql-configuration) property, which defaults to `false`.

This changes how read-only queries are routed. Read load that was previously spread across all replicas now concentrates on primaries, and a query that a single node could previously serve entirely from its local replicas may now require a network hop. In exchange, these queries no longer wait for a follower replica to catch up.

To restore the previous behavior, enable follower reads cluster-wide:

```bash
cluster config update ignite.sql.allowFollowerReads=true
```

You can also allow or disallow follower reads for an individual statement or JDBC connection - see [Per-Statement Control Over Follower Reads](#per-statement-control-over-follower-reads) and [Controlling Follower Reads](../../developers-guide/clients/jdbc-driver.md#controlling-follower-reads).

## New Features

### Per-Statement Control Over Follower Reads

You can now control, for an individual SQL statement, whether the SQL engine may read from non-primary replicas. The new `allowFollowerReads` [statement property](../../developers-guide/sql/sql-api.md#using-statements) overrides the cluster-wide setting for that statement only, and applies to read-only statements.

Enabling follower reads spreads read load across all replicas and lets a query read from a local replica, avoiding a network hop. The trade-off is latency, because reading from a follower replica may introduce delays while the replica catches up. Disabling it forces the statement to always read from primary replicas. Leaving the property unset keeps the cluster-wide setting, which is the default behavior.

The cluster-wide setting itself is new in this release and defaults to disallowing follower reads - see [SQL Follower Reads Disabled by Default](#sql-follower-reads-disabled-by-default).

```java
Statement stmt = client.sql().statementBuilder()
    .query("SELECT * FROM ACCOUNTS WHERE STATUS = 'ACTIVE'")
    .allowFollowerReads(false)
    .build();
```

For the JDBC equivalent, see [Controlling Follower Reads](../../developers-guide/clients/jdbc-driver.md#controlling-follower-reads). For how follower reads relate to read-only transactions, see [Consistency Model](../../administrators-guide/storage/consistency-model.md).

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-50536 | Cluster SQL Engine | Fixed a query with a range predicate under `OR` returning incomplete results. |
| GG-50257 | Cluster SQL Engine | Improved performance of certain `UPDATE` queries. |
| GG-50225 | Cluster Storage Engine | Fixed partition rebalance failing to transfer partitions that contain deleted rows (tombstones). |
| GG-50190 | General | Fixed incorrect auto-commit when closing a read-write scan cursor of an explicit transaction. |
| GG-50080 | Cluster Continuous Queries | Java client: fixed a further case of continuous query event loss when the underlying table is dropped. |
| GG-50076 | Cluster Continuous Queries | .NET: Fixed a continuous query losing events when the underlying table is dropped. |
| GG-50068 | Cluster SQL Engine | Fixed a memory leak when a query timeout is set. |
| GG-50033 | Platforms & Clients | C++: Fixed a possible crash during client shutdown on Windows. |
| GG-49967 | Cluster SQL Engine | Reduced allocations when returning single-row result sets. |
| GG-49952 | Cluster SQL Engine | Removed primitive boxing when sorting rows in SQL. |
| GG-49944 | Cluster Storage Engine | Reduced heap allocations in the MVCC garbage collector. |
| GG-49865 | Cluster SQL Engine | Fixed excessive CPU usage caused by the query execution root node busy-looping while waiting for its source. |
| GG-49835 | Cluster SQL Engine | Improved performance of SQL queries that use index scans inside read-write transactions. |
| GG-49689 | Cluster Continuous Queries | Fixed a continuous query losing events when the underlying table is dropped. |
| GG-49688 | Cluster SQL Engine | The optimizer now prefers a primary key index lookup over a secondary index scan when possible. |
| GG-49619 | Cluster Security | Renaming the cluster now requires the new `RENAME_CLUSTER` action. |
| GG-49617 | Cluster Security | Deployment units now carry an integrity manifest that is validated on deployment, so a unit whose contents were altered after packaging is rejected. |
| GG-49614 | Cluster Security | Enabling, disabling, or listing cluster-wide metrics now requires the corresponding metrics action (`ENABLE_METRICS`, `DISABLE_METRICS`, or `LIST_METRICS`). |
| GG-49613 | Cluster Security | Writing the cluster security configuration (`ignite.security`) through the REST configuration endpoint now requires the new `WRITE_SECURITY_CONFIG` action in addition to `WRITE_CLUSTER_CONFIG`. |
| GG-49609 | Cluster Security | Hardened code deployment against path-traversal entries in deployment unit archives. |
| GG-49582 | Cluster Security | Managing data center replication now requires the new `MANAGE_DCR` action. |
| GG-49569 | General | Colocated nodes that share a network interface are now counted as a single host for license CPU and host limits. Set the `GG_LICENSE_HOST_MAC_INTERSECTION` system property to `false` to restore the previous counting. |
| GG-49413 | Cluster SQL Engine | Reduced memory pressure during SQL query execution. |
| GG-49379 | Cluster SQL Engine | SQL reads from non-primary replicas are now disabled by default. Added the `allowFollowerReads` property, cluster-wide and per-statement, to re-enable them. |
| GG-49302 | Cluster Storage Engine | Added an API to advance the low watermark past orphaned locks. |
| GG-49086 | Cluster Data Replication | Added an experimental Microsoft SQL Server CDC source that reads native SQL Server change data capture, gated behind the `--experimental` flag. |
| GG-49085 | Cluster Data Replication | Added a GridGain 9 CDC sink that writes change events into a local GridGain 9 table. Use the `targetTable` parameter to remap the destination; replicating a table to itself is rejected. |
| GG-48647 | Platforms & Clients | .NET: Added `DataStreamerOptions.SameKeyUpdateMode` with `Squash` and `Preserve` modes. |
| GG-48432 | CLI Tool | Added the `--tx-timeout` option to the CLI `sql` command, which overrides the cluster-wide read-write transaction timeout for the current session. |
| GG-48408 | Cluster Rolling Upgrade | Unless a rolling upgrade is in progress, all cluster nodes must now run the same version. During a rolling upgrade, only the base and target versions are accepted. |
| GG-48391 | Cluster Data Snapshots and Recovery | Fixed an out-of-memory error during snapshot restore. |
| GG-47963 | Platforms & Clients | C++: Added a configurable retry policy for client operations, bringing the C++ client in line with the Java and .NET clients. |
| GG-47911 | Platforms & Clients | C++: Optimized table schema retrieval. |
| GG-47814 | Migration Tools | Migration Tools adapter can now read `java.time.Instant` values serialized in the extra column. |
| GG-46020 | Distributed Computing | .NET: Added `JobExecutorType.WasmEmbedded` and `WasmJobDescriptor` to execute Wasm jobs. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.20`, `9.1.21`, `9.1.22`, `9.1.23`, `9.1.24`, `9.1.25`

When updating from older versions, we recommend updating to version `9.1.20` first, before performing an update to current version.

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
