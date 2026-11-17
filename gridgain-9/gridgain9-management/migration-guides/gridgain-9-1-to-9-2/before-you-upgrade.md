---
description: >-
  Planning reference for upgrading from GridGain 9.1 to 9.2: choosing a full-cluster or rolling upgrade, upgrade constraints, and the scope and effort of each change.
---

# What to Know Before Upgrading to GridGain 9.2

Read this page before you upgrade a cluster from GridGain 9.1.29 to 9.2. It helps you choose an upgrade path, find the changes that affect you, and estimate the work. When you are ready, follow the [Upgrade Procedure](upgrade-procedure.md).

{% hint style="info" %}
This guide uses 9.1.29 for the primary starting version, 9.1.x for behavior across the 9.1 line, and 9.1 for a cluster or node that you work with.
{% endhint %}

## Supported Starting Versions

You can upgrade to 9.2 from the following 9.1.x releases.

<details>

<summary>Show supported releases</summary>

`9.1.21`, `9.1.22`, `9.1.23`, `9.1.24`, `9.1.25`, `9.1.26`, `9.1.27`, `9.1.28`, `9.1.29`

</details>

{% hint style="info" %}
If your cluster runs a release that is not listed, contact MariaDB [support](https://mariadb.com/support/) before you upgrade.
{% endhint %}

## Choose Your Upgrade Path

- *Full-cluster upgrade.* You stop the cluster, replace the binaries on every node, and start it again. Use it if you can schedule downtime. It is simpler, because no node runs a different version. See [Full-Cluster Upgrade](../../upgrade/full-cluster-upgrade.md).
- *Rolling upgrade.* You upgrade the nodes one at a time. Use it if the applications must keep using the key-value and table APIs. SQL does not work while the cluster runs both versions, so you must pause it. See [Rolling Upgrade](../../upgrade/rolling-upgrade.md) and [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed).

| | Full-cluster upgrade | Rolling upgrade |
| --- | --- | --- |
| Key-value and table API operations | Unavailable while the cluster is stopped | Continue |
| SQL, including JDBC and ODBC | Unavailable while the cluster is stopped | Pause from `upgrade start` to the commit |
| DDL and cluster configuration changes | Unavailable while the cluster is stopped | Rejected until the commit |
| Cancel | No commit point. To go back, restore the backup | Not possible. Finish the upgrade or restore the backup |
| Restart after the commit | Included, because every node restarts on 9.2 | One node, so that the system views get their 9.2 definitions |

## Upgrade Constraints

- *Downgrade is not supported.* After you start the cluster on 9.2, the only way back is to restore a backup, and everything written after the backup is lost. On Ultimate Edition, take a full snapshot of all tables. On Enterprise Edition, which has no snapshots, stop the cluster and copy the `work` directory of every node. Also save the cluster configuration and the list of users and roles, because a snapshot does not contain them. See [Back Up the Data](upgrade-procedure.md#back-up-the-data) and [Recovery Path](upgrade-procedure.md#recovery-path).
- *Java 21 or later is required* on every server host, on the CLI host, and for every application that uses the Java client, JDBC, Spring, Hibernate, or Kafka Connect. See [Java 21 or Later](platform-and-packaging.md#java-21-or-later).
- *A removed configuration key stops the node.* A node refuses to start when its node configuration file contains a key that 9.2 does not know. See [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys).
- *Tables on the RocksDB engine have no migration path.* Re-create them on another storage profile before you upgrade. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed).
- *User names are case-sensitive as soon as a 9.2 node joins,* even before a rolling upgrade is committed. A login whose case differs from the stored name fails. See [User and Role Names Are Case-Sensitive](security-changes.md#user-and-role-names-are-case-sensitive).

## Which Pages Apply to You

- *Cluster administrators* install, configure, and run the server nodes. Read the whole guide, starting with the [Upgrade Procedure](upgrade-procedure.md).
- *Application developers* embed GridGain clients or connect to a cluster that someone else administers. Read [Client and API Changes](clients-and-apis.md), [SQL and System View Changes](sql-changes.md), and the user name and privilege changes in [Security and Authorization Changes](security-changes.md). Coordinate the switch with the cluster administrators.
- *Teams that maintain monitoring, scripts, or automation* read [Configuration, Storage, and Metrics Changes](configuration-and-storage.md), [Platform and Packaging Changes](platform-and-packaging.md), and the system view changes in [SQL and System View Changes](sql-changes.md#system-view-columns-removed).

## Upgrade Scope and Effort

The tables list each change, when it applies to you, and the effort it needs. If an item does not apply to your deployment, skip it.

*Effort* is one of the following:

- *Mechanical.* A rename or similar update with no logic changes.
- *Config-only.* Set, remove, or rename a configuration property. No code changes.
- *Code.* A contained code change, such as a renamed API call or SQL statement.
- *Redesign.* Adopt a different storage engine or approach. Expect design work and retesting.
- *Planning.* A change to how you run the upgrade, such as a pause of the SQL workload. No change to your code or configuration.

### For Application Developers

| What changes | Applies if | Effort | Details |
| --- | --- | --- | --- |
| Java 21 or later | Your application uses the Java client, JDBC, Spring Boot, Spring Data, Hibernate, or Kafka Connect | Mechanical | [Java 21 or Later](platform-and-packaging.md#java-21-or-later) |
| `CREATE ZONE ... WITH` removed | Your scripts, tools, or code create zones with SQL | Code | [CREATE ZONE Syntax](sql-changes.md#create-zone-syntax) |
| Zone names are simple identifiers | You write `schema.zone` in `CREATE`, `ALTER`, or `DROP ZONE` | Mechanical | [Zone Names Are Simple Identifiers](sql-changes.md#zone-names-are-simple-identifiers) |
| System view columns removed | Your queries read system views with the old column names | Code | [System View Columns Removed](sql-changes.md#system-view-columns-removed) |
| `__part` alias removed | Your queries use `__part` or `"__PART"` | Mechanical | [The __part Alias Is Removed](sql-changes.md#the-__part-alias-is-removed) |
| `ADD` is reserved | An identifier is named `add` | Mechanical | [ADD Is a Reserved Word](sql-changes.md#add-is-a-reserved-word) |
| Microsecond precision | Your queries compare or order on fractions of a second | Code | [Date and Time Values Keep Microseconds](sql-changes.md#date-and-time-values-keep-microseconds) |
| `EXPLAIN` output | You parse `EXPLAIN` output | Code | [EXPLAIN Output Changed](sql-changes.md#explain-output-changed) |
| SQL does not work across versions | Your application runs SQL during a rolling upgrade | Planning | [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed) |
| User and role names are case-sensitive | Your applications log in with a user name or run `GRANT` and `CREATE ROLE` | Code | [User and Role Names Are Case-Sensitive](security-changes.md#user-and-role-names-are-case-sensitive) |
| Index privileges are checked on the table | Your users hold `CREATE_INDEX` or `DROP_INDEX` on an index name | Config-only | [Index Privileges Are Checked on the Table](security-changes.md#index-privileges-are-checked-on-the-table) |
| `PartitionManager` removed | You call `table.partitionManager()` or `ITable.PartitionManager` | Code | [PartitionManager Removed](clients-and-apis.md#partitionmanager-removed) |
| `RecordSupportInternal` removed | Your code imports `org.apache.ignite.table.mapper.RecordSupportInternal` | Code | [RecordSupportInternal Removed](clients-and-apis.md#recordsupportinternal-removed) |
| Data center replication REST API | Your requests send `tableList`, `sourceClusterAuthConfig`, or `sourceClusterSslConfig` | Mechanical | [Data Center Replication REST API](clients-and-apis.md#data-center-replication-rest-api) |

### For Cluster Administrators

| What changes | Applies if | Effort | Details |
| --- | --- | --- | --- |
| Java 21 or later on every server host | Always | Mechanical | [Java 21 or Later](platform-and-packaging.md#java-21-or-later) |
| Windows installer checks Java | You install on Windows with the MSI | Mechanical | [Windows Installer](platform-and-packaging.md#windows-installer) |
| CLI launchers ignore `JAVA_OPTS` | You pass JVM options to the CLI through `JAVA_OPTS` on any platform, or set `GRIDGAIN9_EXIT_CONSOLE` on Windows | Config-only | [CLI Launchers](platform-and-packaging.md#cli-launchers) |
| Unsupported `JVM_GC` value | You set `JVM_GC` | Config-only | [JVM_GC Fallback](platform-and-packaging.md#jvm_gc-fallback) |
| Removed and renamed configuration keys | Your node configuration files or cluster configuration use any key in the tables | Config-only | [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys) |
| RocksDB engine removed | A storage profile uses `engine = rocksdb` | Redesign | [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed) |
| Page replacement policies | A profile sets `replacementMode` | Config-only | [Page Replacement Policies](configuration-and-storage.md#page-replacement-policies) |
| Raft logs migrate to a new log storage, and every node needs free disk space for the old and new logs | Always | Planning | [Raft Log Storage Changes](configuration-and-storage.md#raft-log-storage-changes) |
| Storage profile metrics renamed, `PageAcquireTime` removed | Dashboards or alerts use `storage.aipersist.<profile>` or `PageAcquireTime` | Mechanical | [Metric Changes](configuration-and-storage.md#metric-changes) |
| SQL does not work across versions | You use a rolling upgrade | Planning | [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed) |
| System view columns removed | Dashboards, scripts, or monitoring queries read system views | Code | [System View Columns Removed](sql-changes.md#system-view-columns-removed) |
| User names are case-sensitive | Your scripts or tooling create users, run `GRANT`, or log in | Code | [User and Role Names Are Case-Sensitive](security-changes.md#user-and-role-names-are-case-sensitive) |
| Role names are migrated to uppercase | You use roles. Two role names that differ only in case make the migration fail | Planning | [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase) |
| LDAP role mappings | You map LDAP groups to roles | Config-only | [LDAP Role Mappings](security-changes.md#ldap-role-mappings) |
| Index privileges | You grant `CREATE_INDEX` or `DROP_INDEX` | Config-only | [Index Privileges Are Checked on the Table](security-changes.md#index-privileges-are-checked-on-the-table) |
| Stopping a table that is already stopped returns an error | Your automation stops specific tables of a replication | Code | [Data Center Replication REST API](clients-and-apis.md#data-center-replication-rest-api) |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
