---
description: >-
  Steps to upgrade a GridGain 9.1 cluster to GridGain 9.2, verify the result, and recover if something fails.
---

# Upgrading a Cluster from GridGain 9.1 to 9.2

This guide describes how to upgrade a GridGain 9.1 cluster to GridGain 9.2 and how to check the result.

Before you start, read [What to Know Before Upgrading](before-you-upgrade.md). It lists the changes that this guide refers to and helps you choose an upgrade path:

- *Full-cluster upgrade.* You stop the cluster, replace the binaries, and start the cluster on 9.2. The cluster is unavailable during the upgrade. See [Full-Cluster Upgrade](../../upgrade/full-cluster-upgrade.md).
- *Rolling upgrade.* You restart the nodes one at a time. The cluster stays up, but SQL does not work during the upgrade. See [Rolling Upgrade](../../upgrade/rolling-upgrade.md).

Both paths use the same preparation, backup, and verification. If you have a staging cluster, rehearse the whole procedure there first.

## Prerequisites

Confirm all of the following before you start:

- The cluster runs GridGain 9.1.29. If it runs another release, upgrade it to 9.1.29 first, or contact MariaDB [support](https://mariadb.com/support/).
- Java 21 or later is installed on every server host and on every host that runs the CLI. Set `JAVA_HOME` for the 9.2 start scripts before you start each node. The 9.1 nodes can keep their current Java until you restart them. The Docker images use JDK 25 by default. See [Java 21 or Later](platform-and-packaging.md#java-21-or-later).
- A valid license is installed.
- You chose an [upgrade path](before-you-upgrade.md#choose-your-upgrade-path) and scheduled the downtime or the SQL pause that it needs.
- On Ultimate Edition, storage for a [snapshot](../../snapshots/data-snapshots.md) is available. On Enterprise Edition, storage for a copy of the `work` directory of every node is available. Take the backup before you upgrade. See [Recovery Path](#recovery-path).
- The 9.2 distribution, package, or Docker image is available. Keep the 9.1 distribution until the upgrade is validated, because recovery needs it.
- Every node has free disk space for the Raft log migration that runs when it first starts on 9.2. See [Raft Log Storage Changes](configuration-and-storage.md#raft-log-storage-changes).

## Prepare for the Upgrade

None of the following requires downtime, except where noted. Do all of it before you stop or upgrade any node.

1. *Re-create the RocksDB tables.* If any zone or table uses a RocksDB storage profile, move it to another profile first. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed). For the storage engines that remain, see [Storage Engines and Profiles](../../../architecture/storage/engines/README.md).
2. *Update the node configuration files.* Rename or delete every key from the tables in [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys), and remove the `replacementMode` property. 9.1.29 already accepts the new names of the renamed keys and the replacement keys, so you can update the files now. A node does not start on 9.2 if its file contains an old key. If you deploy with the Helm chart, see the chart note in [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys). If your files set only addresses, ports, and sizes, nothing changes. Test the final files on a 9.2 node in a staging cluster. For the current keys, see [Node Configuration Parameters](../../../reference/configuration/node-configuration-parameters.md).
3. *Check the cluster configuration.* Run `cluster config show` and compare it with the tables. GridGain 9.1.29 converts the old key names when it loads the cluster configuration, so a cluster that runs 9.1.29 normally shows only the new names. If a key from the tables is still there, for example in a cluster that was initialized on an earlier 9.1 release, fix it before you run `upgrade start`, because cluster configuration changes are blocked during a rolling upgrade. For the current keys, see [Cluster Configuration Parameters](../../../reference/configuration/cluster-configuration-parameters.md) and [Cluster and Node Configuration](../../cluster-configuration.md).
4. *Check `vars.env` and the CLI environment.* Review `JVM_GC` in `vars.env`. Review `JAVA_OPTS` for the Windows CLI and the CLI Docker image, and `GRIDGAIN9_EXIT_CONSOLE` on Windows, in the scripts that start the CLI. See [Platform and Packaging Changes](platform-and-packaging.md) and [Using the CLI Tool](../../using-the-cli-tool.md).
5. *Update SQL and scripts.* All of the new forms below also work on 9.1.29, so you can change them before the upgrade.
   - `CREATE ZONE ... WITH`. Use `CREATE ZONE z (PARTITIONS 25, REPLICAS 3) STORAGE PROFILES ['default']`. See [CREATE ZONE Syntax](sql-changes.md#create-zone-syntax) and [Distribution Zones](../../../reference/sql/distribution-zones.md).
   - Zone names with a schema, such as `public.my_zone`. Use `my_zone`. See [Zone Names Are Simple Identifiers](sql-changes.md#zone-names-are-simple-identifiers).
   - Removed columns of system views, such as `system.tables.schema` or `system.zones.name`. See [System View Columns Removed](sql-changes.md#system-view-columns-removed) and [System Views](../../../reference/monitoring/system-views.md).
   - The hidden column `__part`. Use `__partition_id`. See [The __part Alias Is Removed](sql-changes.md#the-__part-alias-is-removed) and [Partition-Specific SELECTs](../../../gridgain9-development/sql/sql-api.md#partition-specific-selects).
   - Identifiers named `add`. Write them as `"ADD"`, in upper case and double quotes. See [ADD Is a Reserved Word](sql-changes.md#add-is-a-reserved-word) and [Keywords](../../../reference/sql/keywords.md).
6. *Prepare roles and users.* Write down the names of your users and roles, and the role names in LDAP `roleMapping` settings. 9.1 stores user names in lower case, and 9.2 compares them exactly. Make sure that applications, scripts, and connection settings use the lower-case name, for example `alice`. Lower-case names work on both versions, and a 9.2 node rejects other spellings as soon as it joins, before the commit. Change LDAP role mappings to upper-case role names. 9.1.29 matches mapped roles without regard to case, so this works before the upgrade. The built-in super role is `system`, in lower case. See [User and Role Names Are Case-Sensitive](security-changes.md#user-and-role-names-are-case-sensitive), [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase), and [LDAP Role Mappings](security-changes.md#ldap-role-mappings). For the commands, see [User Permissions and Roles](../../../security/user-permissions-and-roles.md) and [Access Control Functions](../../../reference/sql/access-control-functions.md). For LDAP, see [User Authentication](../../../security/authentication.md#ldap-authentication).
7. *Update the applications.* Move them to Java 21 or later, and replace `PartitionManager` and `RecordSupportInternal`. `Table.partitionDistribution()` already exists in 9.1.29, so you can change the `PartitionManager` calls before the upgrade. Build and test them against the 9.2 client libraries. For the client dependencies, see [Project Setup](../../../gridgain9-development/project-setup.md), and for how clients and servers of different versions work together, see [Client Upgrade](../../upgrade/client-upgrade.md). See [Client and API Changes](clients-and-apis.md).
8. *Back up the data.* See [Back Up the Data](#back-up-the-data).

### Back Up the Data

On Ultimate Edition, take a full snapshot of all tables while the cluster is running, and check that it completed:

```bash
cluster snapshot create --type=full --all
cluster snapshot list
```

The snapshot is created in the background. If `cluster snapshot list` fails or does not show it right away, wait a few seconds and run the command again. Write down the snapshot ID. Store the snapshots outside the work directory if you can. See [Data Snapshots](../../snapshots/data-snapshots.md).

A snapshot contains the table data, the schemas, indexes, zones, and row-level security policies. It does not contain users, roles, privileges, or the cluster configuration. Save the output of `cluster config show` and the list of your users and roles, so that you can re-create them after a restore.

On Enterprise Edition there are no snapshots. Stop the cluster and copy the `work` directory of every node. For a rolling upgrade, this means a short stop of the whole cluster for the backup.

{% hint style="warning" %}
Do not start the upgrade without a backup. GridGain does not provide a downgrade path, and outside a rolling upgrade that is still in progress, a 9.1 node cannot join a cluster whose nodes run 9.2. The only way back is to restore the backup, and everything written after the backup is lost. See [Recovery Path](#recovery-path).
{% endhint %}

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

Do not start any node yet.

### Step 3: Start the Cluster

Start all nodes. The order does not matter. The cluster forms again by itself, with its data, and you do not run `cluster init`.

When the cluster starts, GridGain converts the stored role names to upper case. User names are not changed. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase).

Continue with [Verify and Stabilize](#verify-and-stabilize).

## Alternative: Rolling Upgrade

Use this path to restart the nodes one at a time. [Rolling Upgrade](../../upgrade/rolling-upgrade.md) describes the commands and the per-platform steps. For 9.2, note the following:

- *SQL needs a pause.* SQL, including JDBC and ODBC, fails when a query needs a node of the other version. Stop the SQL workload from `upgrade start` until the commit finishes. See [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed).
- *DDL and cluster configuration changes are rejected* from `upgrade start` until the commit.
- *You cannot cancel the upgrade.* The `upgrade cancel` command is not implemented. After `upgrade start`, finish the upgrade or restore the backup.

### Step 1: Start the Upgrade

1. Stop all SQL traffic. Key-value and table API operations continue while the nodes restart.
2. Run `upgrade start --version <version>`, where `<version>` is the exact version of the 9.2 nodes, for example `9.2.0`. Run `upgrade state` and check that all nodes are in `currentVersionNodes`.

### Step 2: Upgrade the Nodes One at a Time

For each node:

1. Stop the node.
2. Replace the binaries with the 9.2 ones, as described in [Rolling Upgrade](../../upgrade/rolling-upgrade.md). Keep the `work` directory, the `etc` directory, and the configuration files.
3. Put the node configuration file that you prepared in place, and set `JAVA_HOME` to Java 21 or later. For Docker, use the 9.2 image tag.
4. Start the node.
5. Run `upgrade state`, and check that the node is in `nextVersionNodes` before you go to the next node.

### Step 3: Commit the Upgrade

1. Run `upgrade commit`. The commit converts the stored role names to upper case before it changes the cluster version. User names are not changed. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase). If the conversion fails, the commit fails with an error.
2. Restart the nodes, so that the system views get their 9.2 definitions. See [System View Columns Removed](sql-changes.md#system-view-columns-removed).
3. Resume the SQL workload.

{% hint style="info" %}
After the commit, `upgrade state` can fail with ``Expected the field `nextVersion` to be a primitive type in the JSON string but got `null` ``. The CLI cannot parse the response. The upgrade is committed.
{% endhint %}

Continue with [Verify and Stabilize](#verify-and-stabilize).

## Verify and Stabilize

With the cluster running on 9.2, confirm it is healthy before you consider the upgrade complete:

1. *Check the cluster.* Run `cluster status`. The status is `active`, and the node count is the number of nodes that you started.
2. *Check the data.* Run a query on one of your tables, and compare the row count with the value before the upgrade.
3. *Check the logs.* Look for configuration errors. If you use LDAP, look for the message that a role in an LDAP `roleMapping` is not present in the authorization configuration.
4. *Check users and roles.* Run `SHOW USERS`, and connect with one of the names it prints. Run `SHOW GRANTS FOR "<user>"` for a user with a custom role, and check that the role name is in upper case. The built-in `system` role, which users such as `ignite` have, stays in lower case. See [SHOW USERS](../../../reference/sql/access-control-functions.md#show-users) and [SHOW GRANTS](../../../reference/sql/access-control-functions.md#show-grants).
5. *Check the system views.* Run `SELECT * FROM system.zones`, and run your monitoring queries. See [System Views](../../../reference/monitoring/system-views.md).
6. *Run the real workload.* Run your regression suite or production workload end to end, including SQL, and confirm it passes. Check the queries that compare or filter on fractions of a second. See [Date and Time Values Keep Microseconds](sql-changes.md#date-and-time-values-keep-microseconds).
7. *Reconnect monitoring and tooling.* Update dashboards and alerts for the renamed storage profile metrics. These names exist only in 9.2. See [Metric Changes](configuration-and-storage.md#metric-changes) and [Available Metrics](../../../reference/monitoring/metrics-list.md).
8. *Re-establish backups.* On Ultimate Edition, take a first snapshot on 9.2 and check that it completes.

{% hint style="info" %}
The upgrade is complete when data integrity, application functionality, and monitoring all check out under the production workload. Keep the backup from before the upgrade and the 9.1 distribution until then.
{% endhint %}

## Troubleshooting

Common errors during the upgrade. If you hit something not covered here, contact MariaDB [support](https://mariadb.com/support/).

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| `ERROR: GridGain 9 requires Java 21 or newer, but <java> is Java <n>.` when a node or the CLI starts | `JAVA_HOME` or the `java` on the path is older than 21. | Set `JAVA_HOME` to Java 21 or later for the 9.2 scripts. |
| The Windows installer reports that GridGain 9 requires Java 21 or newer | The machine-wide `JAVA_HOME` points at an older Java. | Point the machine-wide `JAVA_HOME` at Java 21 or later, and run the installer again. |
| `Failed to parse HOCON: '<path>' configuration doesn't have the '<key>' sub-configuration` when a node starts | The node configuration file contains a key that 9.2 removed or renamed. | Rename or delete the key. See [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys). |
| `Failed to parse HOCON: Polymorphic configuration type is not correct: rocksdb` when a node starts | A storage profile uses `engine = rocksdb`. | Re-create the zones and tables on another engine, and remove the profile. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed). |
| `IGN-CMN-65535: Legacy query start protocol is no longer supported, the sending node must be upgraded` | A 9.1 node coordinated a SQL query that needs a 9.2 node. | Stop the SQL workload until the upgrade is committed. See [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed). |
| `IGN-SQL-8: The query was mapped onto node '<node>' which runs version <version> and does not support latest query execution protocol ...` | A 9.2 node coordinated a SQL query that needs a 9.1 node during the rolling upgrade. | Stop the SQL workload until the upgrade is committed. |
| `upgrade commit` fails with `Legacy role names collide after uppercasing` or `Legacy role name conflicts with a built-in role` | Two roles differ only in case, or a role name becomes a built-in role name. | Fix the role names, and run `upgrade commit` again. If you cannot, contact MariaDB [support](https://mariadb.com/support/). |
| `Cannot commit rolling upgrade. Nodes not on target version <version>: {<node>=<version>, ...}` | `upgrade commit` ran while some nodes still run 9.1. | Upgrade the listed nodes, check `upgrade state`, and run `upgrade commit` again. |
| `Authentication failed` for a user that worked on 9.1, or ``GG-RBAC-2: User `<NAME>` is not found`` | The name differs in case from the stored name. Unquoted SQL names are converted to upper case. | Use the exact stored name, in double quotes in SQL. See [User and Role Names Are Case-Sensitive](security-changes.md#user-and-role-names-are-case-sensitive). |
| ``GG-RBAC-7: Role `SYSTEM` is not found``, or `GG-RBAC-9: Cannot assign the built-in role: system` | A script grants the super role with SQL. The built-in super role is `system` in lower case, and SQL cannot assign it. | Remove the statement. Put `system` in the `roles` list of the user in the authentication provider configuration. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase). |
| An LDAP user gets no privileges | An LDAP `roleMapping` names a role in a different case. | Change the mapping to the upper-case role name. See [LDAP Role Mappings](security-changes.md#ldap-role-mappings) and [User Authentication](../../../security/authentication.md#ldap-authentication). |
| `Failed to parse query` on `CREATE ZONE`, `DROP ZONE`, or an object named `add` | The statement uses the removed syntax, a zone name with a schema, or the reserved word `ADD`. | See [SQL and System View Changes](sql-changes.md). |
| `Column 'NAME' not found in any table` on a system view, or `Column '__PART' not found in any table` | The query uses a column that 9.2 removed. | Use the replacement column. See [System View Columns Removed](sql-changes.md#system-view-columns-removed). |
| `SELECT * FROM system.zones` or another system view fails with `class java.lang.Integer cannot be cast to class java.lang.String` (rolling upgrade) | The nodes were not restarted after the commit. | Restart the nodes. See [System View Columns Removed](sql-changes.md#system-view-columns-removed). |
| `Schema modification command was aborted because a cluster upgrade is currently in progress` or `Cannot change configuration while rolling upgrade is in progress` | A rolling upgrade is in progress. | Wait for the commit, and then run the statement or the update again. |
| A 9.1 node does not start with `Some node has already been validated with a different version` | A node on another version is trying to join a cluster that runs 9.2. | Start every node of the cluster on the same version, or start a rolling upgrade first. |

## Recovery Path

GridGain does not provide a downgrade path from 9.2 to 9.1, and `upgrade cancel` is not implemented. Once the nodes run 9.2, a 9.1 node is denied when it tries to join.

The supported recovery depends on when you decide:

- *While the rolling upgrade is in progress.* You can stop an upgraded node and start it again from the 9.1 distribution, with the 9.1 configuration files. It rejoins the cluster. But the cluster stays in the upgrade state, and DDL and cluster configuration changes stay blocked, because nothing can end the upgrade except a commit. A commit needs every node to run 9.2. So the choice is to finish the upgrade, or to restore the backup.
- *After you commit, or after a full-cluster upgrade.* Restore the backup that you took before the upgrade into a 9.1 cluster. On Ultimate Edition, restore the snapshot, as described in [Restoring Snapshots](../../snapshots/data-snapshots.md#restoring-snapshots), and then re-create the users, roles, privileges, and cluster configuration. On Enterprise Edition, stop all nodes and put the copies of the `work` directories back.

{% hint style="warning" %}
Restoring a backup replaces all data in the cluster with the data from the moment of the backup. Everything written after the backup is lost. Move the current data aside instead of deleting it if you may need it.
{% endhint %}

Restore the copies of all nodes together, and only copies that were taken at the same time. Do not restore only some of the nodes.

For other problems, contact MariaDB [support](https://mariadb.com/support/).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
