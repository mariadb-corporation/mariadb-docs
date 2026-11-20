---
description: >-
  Step-by-step procedure for upgrading a GridGain 9.1.29 cluster to 9.2, with verification, troubleshooting, and a recovery path back to 9.1.
---

# Upgrading a Cluster from GridGain 9.1 to 9.2

This guide describes how to upgrade a GridGain 9.1.29 cluster to GridGain 9.2, and how to check that the upgrade worked.

Before you start, read [What to Know Before Upgrading](before-you-upgrade.md). It helps you choose between a full-cluster and a rolling upgrade and lists the changes that this guide refers to. If you have a staging cluster, rehearse the whole procedure there first.

The procedure has these phases: prerequisites, preparation, the upgrade itself, and verification. Troubleshooting and the recovery path follow.

A downgrade from 9.2 to 9.1 is not supported. To recover 9.1, see the [Recovery Path](#recovery-path).

## Prerequisites

Confirm all of the following before you start:

- The cluster runs a supported 9.1.x release, 9.1.21 to 9.1.29. See [Supported Starting Versions](before-you-upgrade.md#supported-starting-versions).
- Java 21 or later is installed on every server host and on every host that runs the CLI. See [Java 21 or Later](platform-and-packaging.md#java-21-or-later).
- A valid license is installed.
- You chose an [upgrade path](before-you-upgrade.md#choose-your-upgrade-path) and scheduled the downtime or the SQL pause that it needs.
- Storage for the backup is available: a [snapshot](../../snapshots/data-snapshots.md) on Ultimate Edition, or a copy of the `work` directory of every node on Enterprise Edition. See [Back Up the Data](#back-up-the-data).
- The 9.2 distribution, package, or Docker image is available. Keep the 9.1 distribution until the upgrade is validated, because recovery needs it.
- Every node has free disk space for both the old and the new Raft logs. See [Raft Log Storage Changes](configuration-and-storage.md#raft-log-storage-changes).

## Prepare for the Upgrade

Do all of the following before you stop or upgrade any node. Only the backup on Enterprise Edition needs downtime.

1. *Re-create the RocksDB tables.* If any zone or table uses a RocksDB storage profile, move it to another profile, wait for the dropped tables to be cleaned up, and remove the profile from every node. Do this on 9.1.29, before the upgrade. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed). For the storage engines that remain, see [Storage Engines and Profiles](../../../architecture/storage/engines/README.md).
2. *Update the node configuration files.* Rename or delete every key from the tables in [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys), and remove the `replacementMode` property. A node does not start on 9.2 if its file contains an old key. 9.1.29 already accepts the new key names, so you can update the files now. Test the final files on a 9.2 node in a staging cluster. If you deploy with the `gridgain/gridgain9` Helm chart, also check the chart version. See [Helm Chart Versions](configuration-and-storage.md#helm-chart-versions).
3. *Check the cluster configuration.* Run `cluster config show` and compare it with the same tables. If an old key is still there, fix it before you run `upgrade start`, because cluster configuration changes are blocked during a rolling upgrade.
4. *Check `vars.env` and the CLI environment.* Check that `JVM_GC` in `vars.env` has a supported value. In the scripts that start the CLI, review `JAVA_OPTS`, and on Windows `GRIDGAIN9_EXIT_CONSOLE`. See [Platform and Packaging Changes](platform-and-packaging.md).
5. *Update SQL and scripts.* The new forms below also work on 9.1.29.
   - Replace `CREATE ZONE ... WITH` with `CREATE ZONE z (PARTITIONS 25, REPLICAS 3) STORAGE PROFILES ['default']`. See [CREATE ZONE Syntax](sql-changes.md#create-zone-syntax).
   - Replace zone names that include a schema, such as `public.my_zone`, with `my_zone`. See [Zone Names Are Simple Identifiers](sql-changes.md#zone-names-are-simple-identifiers).
   - Replace the removed system view columns, such as `system.tables.schema` or `system.zones.name`, with the new columns. See [System View Columns Removed](sql-changes.md#system-view-columns-removed).
   - Replace the hidden column `__part` with `__partition_id`. See [The __part Alias Is Removed](sql-changes.md#the-__part-alias-is-removed).
   - Write identifiers named `add` as `"ADD"`, in uppercase and double quotes. See [ADD Is a Reserved Word](sql-changes.md#add-is-a-reserved-word).
6. *Prepare roles and users.* 9.1 matches user names without regard to case, and 9.2 compares them exactly.
   - Find the stored name of each user. See [How to Find the Stored Name](security-changes.md#how-to-find-the-stored-name).
   - Make sure that applications, scripts, and connection settings use exactly that name. It works on both versions, and a 9.2 node rejects other spellings as soon as it joins.
   - Change the role names in LDAP `roleMapping` settings to uppercase, which 9.1.29 also accepts. See [LDAP Role Mappings](security-changes.md#ldap-role-mappings).
   - Check the role names for case-only duplicates, such as `Reader` and `READER`. The role migration that runs on first start fails if two role names differ only in case. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase).
7. *Update the applications.* Move them to Java 21 or later, replace `PartitionManager` and `RecordSupportInternal`, and test them against the 9.2 client libraries. See [Client and API Changes](clients-and-apis.md), [Project Setup](../../../gridgain9-development/project-setup.md), and [Client Upgrade](../../upgrade/client-upgrade.md).
8. *Back up the data.* See [Back Up the Data](#back-up-the-data).

### Back Up the Data

On Ultimate Edition, take a full snapshot of all tables while the cluster is running, and check that it completed:

```bash
cluster snapshot create --type=full --all
cluster snapshot list
```

The snapshot is created in the background. If `cluster snapshot list` fails or does not show it, wait a few seconds and run it again. Write down the snapshot ID, and store snapshots outside the work directory if you can. See [Data Snapshots](../../snapshots/data-snapshots.md).

A snapshot contains the table data, the schemas, indexes, zones, and row-level security policies. It does not contain users, roles, privileges, or the cluster configuration. Save the output of `cluster config show` and the list of your users and roles, so that you can re-create them after a restore. Use the stored user names, not the `SHOW USERS` output of 9.1, which prints uppercase.

On Enterprise Edition there are no snapshots. Stop the cluster and copy the `work` directory of every node. Take the copies at the same time. For a rolling upgrade, this means a short stop of the whole cluster for the backup.

{% hint style="warning" %}
Do not start the upgrade without a backup. The only way back to 9.1 is to restore it, and everything written after the backup is lost. See [Recovery Path](#recovery-path).
{% endhint %}

### When Is Preparation Complete?

Preparation is complete when the node configuration files start on 9.2 in staging, the backup is verified, and the applications run against the 9.2 client libraries.

## Full-Cluster Upgrade

Use this path if you can stop the cluster. For the commands for ZIP, DEB, RPM, and Docker installations, see [Full-Cluster Upgrade](../../upgrade/full-cluster-upgrade.md).

### Step 1: Stop the Cluster

1. Stop all SQL traffic and all applications that use the cluster.
2. Stop every node. Wait until every node has exited.

### Step 2: Replace the Binaries

On every node:

1. Replace the binaries with the 9.2 ones, as described in [Full-Cluster Upgrade](../../upgrade/full-cluster-upgrade.md). Keep the `work` directory, the `etc` directory, and the configuration files.
2. Put the node configuration file that you prepared in place.
3. Set `JAVA_HOME` to Java 21 or later. For Docker, use the 9.2 image tag.

For DEB and RPM, do steps 2 and 3 before you run `apt` or `dnf`, because the package upgrade starts the node at once. The package upgrade is then also the start of that node, so the node starts before you reach [Step 3](#step-3-start-the-cluster).

On the other platforms, do not start any node yet.

### Step 3: Start the Cluster

Start all nodes in any order. The cluster forms again with its data, and you do not run `cluster init`. On the first start, GridGain converts the stored role names to uppercase. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase).

Continue with [Verify and Stabilize](#verify-and-stabilize).

## Rolling Upgrade

Use this path to restart the nodes one at a time. [Rolling Upgrade](../../upgrade/rolling-upgrade.md) describes the commands and the per-platform steps. For 9.2, note the following:

- *Pause SQL* from `upgrade start` until the commit finishes. See [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed).
- *DDL and cluster configuration changes are rejected* until the commit.
- *You cannot cancel the upgrade.* 9.2 has no `upgrade cancel` command. After `upgrade start`, finish the upgrade or restore the backup.

### Step 1: Start the Upgrade

1. Stop all SQL traffic. Key-value and table API operations can continue.
2. Run `upgrade start --version <version>`, where `<version>` is the exact version of the 9.2 nodes, for example `9.2.0`. Run `upgrade state` and check that all nodes are in `currentVersionNodes`.

### Step 2: Upgrade the Nodes One at a Time

For each node:

1. Stop the node.
2. Replace the binaries with the 9.2 ones, as described in [Rolling Upgrade](../../upgrade/rolling-upgrade.md). Keep the `work` directory, the `etc` directory, and the configuration files.
3. Put the node configuration file that you prepared in place, and set `JAVA_HOME` to Java 21 or later. For Docker, use the 9.2 image tag. For DEB and RPM, do this before you run `apt` or `dnf`, because the package upgrade restarts the node at once.
4. Start the node.
5. Run `upgrade state`, and check that the node is in `nextVersionNodes`. The node can take about a minute to show up, so run the command again if the list is empty.
6. Run `recovery partition states --global`, and check that every partition is `Available` before you stop the next node. If you stop a node while another node still catches up, a partition can lose its majority.

### Step 3: Commit the Upgrade

1. Run `upgrade commit`. The commit converts the stored role names to uppercase. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase).
2. Restart one node, so that the system views get their 9.2 definitions for the whole cluster. The other nodes need no restart. See [Restart a Node After a Rolling Upgrade](sql-changes.md#restart-a-node-after-a-rolling-upgrade).
3. Resume the SQL workload.

{% hint style="info" %}
After the commit, `upgrade state` can fail with ``Expected the field `nextVersion` to be a primitive type in the JSON string but got `null` ``. The CLI cannot parse the response. The upgrade is committed.
{% endhint %}

Continue with [Verify and Stabilize](#verify-and-stabilize).

## Verify and Stabilize

With the cluster running on 9.2, check the following:

1. *Check the cluster.* Run `cluster status`. The status is `active`, and the node count is the number of nodes that you started.
2. *Check the data.* Compare the row count of one of your tables with the value before the upgrade.
3. *Check the logs.* Look for configuration errors. If you use LDAP, look for the warning that a role in a `roleMapping` is not present in the authorization configuration.
4. *Check users and roles.* Run `SHOW USERS`, and connect with one of the names it prints. Run `SHOW GRANTS FOR "<user>"` for a user with a custom role, and check that the role name is in uppercase. The built-in `system` role stays in lowercase. See [SHOW USERS](../../../reference/sql/access-control-functions.md#show-users) and [SHOW GRANTS](../../../reference/sql/access-control-functions.md#show-grants).
5. *Check the system views.* Run `SELECT * FROM system.zones`, and run your monitoring queries. See [System Views](../../../reference/monitoring/system-views.md).
6. *Run the real workload.* Run your regression suite or production workload end to end, including SQL. Check the queries that compare or filter on fractions of a second. See [Date and Time Values Keep Microseconds](sql-changes.md#date-and-time-values-keep-microseconds).
7. *Reconnect monitoring.* Update dashboards and alerts for the renamed storage profile metrics, which exist only in 9.2. See [Metric Changes](configuration-and-storage.md#metric-changes) and [Available Metrics](../../../reference/monitoring/metrics-list.md).

{% hint style="info" %}
The upgrade is complete when data, applications, and monitoring all check out under the production workload. Keep the backup and the 9.1 distribution until then. Afterward, on Ultimate Edition, take a first snapshot on 9.2 and check that it completes.
{% endhint %}

## Troubleshooting

The tables list common errors during the upgrade, grouped by when you see them. For anything else, contact MariaDB [support](https://mariadb.com/support/).

### Node Start and Join

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| `ERROR: GridGain 9 requires Java 21 or newer, but <java> is Java <n>.` when a node or the CLI starts | `JAVA_HOME` or the `java` on the path is older than 21. | Set `JAVA_HOME` to Java 21 or later for the 9.2 scripts. |
| The Windows installer reports that GridGain 9 requires Java 21 or newer | The machine-wide `JAVA_HOME` points at an older Java. | Point the machine-wide `JAVA_HOME` at Java 21 or later, and run the installer again. |
| `Failed to parse HOCON: '<path>' configuration doesn't have the '<key>' sub-configuration` when a node starts | The node configuration file contains a key that 9.2 removed or renamed. | Rename or delete the key. See [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys). |
| `Failed to parse HOCON: Polymorphic configuration type is not correct: rocksdb` when a node starts | A storage profile uses `engine = rocksdb`. | Re-create the zones and tables on another engine, and remove the profile. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed). |
| `Table uses an unknown storage profile or engine` when a node starts, and the node stops | A table on a RocksDB profile still exists, or was dropped and not yet cleaned up. | Restore the 9.1 backup, finish the cleanup on 9.1.29, and upgrade again. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed) and [Recovery Path](#recovery-path). |
| A 9.1 node does not start with `Some node has already been validated with a different version` | A node on another version is trying to join a cluster that runs 9.2. | Start every node of the cluster on the same version, or start a rolling upgrade first. |

### Rolling Upgrade

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| `IGN-CMN-65535: Legacy query start protocol is no longer supported, the sending node must be upgraded` | A 9.1 node coordinated a SQL query that needs a 9.2 node. | Stop the SQL workload until the upgrade is committed. See [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed). |
| `IGN-SQL-8: The query was mapped onto node '<node>' which runs version <version> and does not support latest query execution protocol ...` | A 9.2 node coordinated a SQL query that needs a 9.1 node during the rolling upgrade. | Stop the SQL workload until the upgrade is committed. |
| `Schema modification command was aborted because a cluster upgrade is currently in progress` or `Cannot change configuration while rolling upgrade is in progress` | A rolling upgrade is in progress. | Wait for the commit, and then run the statement or the update again. |
| `Cannot commit rolling upgrade. Nodes not on target version <version>: {<node>=<version>, ...}` | `upgrade commit` ran while some nodes still run 9.1. | Upgrade the listed nodes, check `upgrade state`, and run `upgrade commit` again. |
| `upgrade commit` fails with `Legacy role names collide after uppercasing` or `Legacy role name conflicts with a built-in role` | Two role names in the cluster configuration differ only in case, or a role name becomes a built-in role name. | Contact MariaDB [support](https://mariadb.com/support/). See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase). |
| `SELECT * FROM system.zones` or another system view fails with `class java.lang.Integer cannot be cast to class java.lang.String` (rolling upgrade) | No node has restarted since the commit. | Restart one node. See [Restart a Node After a Rolling Upgrade](sql-changes.md#restart-a-node-after-a-rolling-upgrade). |

### SQL

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| `Failed to parse query: Encountered "WITH"` on `CREATE ZONE` | The statement uses the removed `CREATE ZONE ... WITH` syntax. | Use `CREATE ZONE z (PARTITIONS 25, REPLICAS 3) STORAGE PROFILES ['default']`. See [CREATE ZONE Syntax](sql-changes.md#create-zone-syntax). |
| `Failed to parse query: Encountered "."` on `CREATE ZONE`, `ALTER ZONE`, or `DROP ZONE` | The zone name includes a schema, such as `public.my_zone`. | Use the zone name alone, such as `my_zone`. See [Zone Names Are Simple Identifiers](sql-changes.md#zone-names-are-simple-identifiers). |
| `Failed to parse query: Incorrect syntax near the keyword` on a statement with an object named `add` | `ADD` is a reserved word in 9.2. | Write the name as `"ADD"`, in uppercase and double quotes. See [ADD Is a Reserved Word](sql-changes.md#add-is-a-reserved-word). |
| `Column '__PART' not found in any table` | The query uses the `__part` alias, which 9.2 removed. | Use `__partition_id`. See [The __part Alias Is Removed](sql-changes.md#the-__part-alias-is-removed). |
| `Column 'NAME' not found in any table` on a system view | The query uses a system view column that 9.2 removed. | Use the replacement column, such as `table_name`, `schema_name`, or `zone_name`. See [System View Columns Removed](sql-changes.md#system-view-columns-removed). |

### Users and Roles

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| `Authentication failed` for a user that worked on 9.1, or ``GG-RBAC-2: User `<NAME>` is not found`` | The name differs in case from the stored name. Unquoted SQL names are converted to uppercase. | Use the exact stored name, in double quotes in SQL. See [How to Find the Stored Name](security-changes.md#how-to-find-the-stored-name). |
| ``GG-RBAC-7: Role `SYSTEM` is not found``, or `GG-RBAC-9: Cannot assign the built-in role: system` | A script grants the super role with SQL. The built-in super role is `system` in lowercase, and SQL cannot assign it. | Remove the statement. Put `system` in the `roles` list of the user in the authentication provider configuration. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase). |
| An LDAP user gets no privileges | An LDAP `roleMapping` names a role in a different case. | Change the mapping to the uppercase role name. See [LDAP Role Mappings](security-changes.md#ldap-role-mappings) and [User Authentication](../../../security/authentication.md#ldap-authentication). |

## Recovery Path

GridGain does not provide a downgrade path from 9.2 to 9.1, and 9.2 has no `upgrade cancel` command. Once a rolling upgrade is committed, or after a full-cluster upgrade, a 9.1 node cannot join a cluster whose nodes run 9.2.

The supported recovery depends on when you decide:

- Before the commit of a rolling upgrade, you roll the upgraded nodes back. See [Before the Commit](#before-the-commit).
- After the commit, or after a full-cluster upgrade, you restore the backup that you took before the upgrade. See [After the Commit](#after-the-commit).

{% hint style="warning" %}
Restoring a backup replaces all data in the cluster with the data from the moment of the backup. Everything written after the backup is lost, including the data that 9.2 wrote. Move the current data aside instead of deleting it if you may need it.
{% endhint %}

The backup that you can restore depends on your edition:

| Edition | Backup you take before the upgrade | Recovery |
| --- | --- | --- |
| Ultimate | A full snapshot, plus the saved cluster configuration and the list of users and roles | Restore the snapshot into a 9.1 cluster: [Recover From a Snapshot](#recover-from-a-snapshot). |
| Enterprise | A copy of the `work` directory of every node | Put the copies back and start 9.1: [Recover From a Copy of the Work Directories](#recover-from-a-copy-of-the-work-directories). |

### Before the Commit

You can roll a node back by stopping it and starting it again from the 9.1 distribution and configuration files, and it rejoins the cluster. This does not end the upgrade. Only a commit does, and a commit needs every node on 9.2. Until then, DDL and cluster configuration changes stay blocked. Finish the upgrade or restore the backup.

### After the Commit

After the commit, a 9.1 node cannot join the cluster any more. This section also applies after a full-cluster upgrade, where there is no commit. Use one of the two recoveries below. Both return the cluster to the state at the time of the backup.

#### Recover From a Snapshot

Ultimate Edition only. Restore the full snapshot that you took before the upgrade into a 9.1 cluster, as described in [Restoring Snapshots](../../snapshots/data-snapshots.md#restoring-snapshots). A snapshot does not contain users, roles, privileges, or the cluster configuration, so re-create them from the output that you saved before the upgrade.

#### Recover From a Copy of the Work Directories

Enterprise Edition only. Use the copies that you took before the upgrade, as described in [Back Up the Data](#back-up-the-data):

1. Stop all nodes.
2. On every node, move the current `work` directory aside. Remove it instead if you do not need the 9.2 data. Copy the backup of that same node back to the same path.
3. Replace the 9.2 binaries with the 9.1 distribution, and put back the node configuration files that you used on 9.1.
4. Start all nodes in any order. The cluster forms again with the data of the backup, and you do not run `cluster init`.
5. Run `cluster status` and check that the status is `active` and the node count is the number of your nodes. Compare the row count of one of your tables with the value before the upgrade.

Restore the copies of all nodes together, and only copies that you took at the same time. Do not restore only some of the nodes, and do not mix copies from different moments.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
