---
description: >-
  Step-by-step procedure for upgrading a GridGain 9.1.29 cluster to 9.2 with a rolling or a full-cluster upgrade, with verification, troubleshooting, and the recovery options.
---

# Upgrading a Cluster from GridGain 9.1 to 9.2

This guide describes how to upgrade a GridGain 9.1.29 cluster to GridGain 9.2, and how to check that the upgrade worked.

Before you start, read [What to Know Before Upgrading](before-you-upgrade.md). It helps you choose between a rolling and a full-cluster upgrade and lists the changes that this guide refers to.

The procedure has five phases: prerequisites, compatibility check, preparation, the upgrade itself, and verification.

A downgrade from 9.2 to 9.1 is not supported. To recover 9.1, see the [Recovery Path](#recovery-path).

## Prerequisites

Confirm all of the following before you start:

- The cluster runs GridGain 9.1.29. If it runs another release, upgrade it to 9.1.29 first, or contact MariaDB [support](https://mariadb.com/support/).
- Java 21 or later is installed on every server host and every host that runs the CLI. You can keep the 9.1 nodes on their current Java until you restart them. Each node switches to Java 21 when you restart it from the 9.2 distribution, so set `JAVA_HOME` for the 9.2 start scripts before you start the node. See [Java 21 or Later](platform-and-packaging.md#java-21-or-later).
- A valid license is installed.
- You chose an [upgrade path](before-you-upgrade.md#choose-your-upgrade-path) and scheduled the downtime or the pause of the SQL workload that the path needs.
- On Ultimate Edition, storage for a [snapshot](../../snapshots/data-snapshots.md) is available. On other editions, storage for a copy of the `work` directory of every node is available. Take the backup before you upgrade. See [Recovery Path](#recovery-path).
- The 9.2 distribution is unpacked or available as a package or image. Keep the 9.1 distribution until the upgrade is validated, because recovery needs it.

## Check Compatibility

Most upgrade work is conditional. Each area below may or may not apply to your deployment. Review every area and record each item that applies:

1. *Review the platform changes.* Java 21, the CLI launchers, `JVM_GC`, and the Windows installer. See [Platform and Packaging Changes](platform-and-packaging.md).
2. *Review the configuration and storage changes.* Removed and renamed keys, RocksDB, page replacement, and metrics. See [Configuration, Storage, and Metrics Changes](configuration-and-storage.md).
3. *Review the SQL changes.* The `CREATE ZONE` syntax, system views, `__part`, `ADD`, and microseconds. See [SQL and System View Changes](sql-changes.md).
4. *Review the security changes.* Case-sensitive names, the role migration, LDAP mappings, and index privileges. See [Security and Authorization Changes](security-changes.md).
5. *Review the client and API changes.* Java 21 for clients, `PartitionManager`, and the replication REST API. See [Client and API Changes](clients-and-apis.md).

{% hint style="info" %}
You are done with this phase when you have gone through every area above and written down the items that apply to you. That list is your upgrade work list: every item on it must be addressed before you upgrade.
{% endhint %}

## Prepare the Distribution, Configuration, and Cluster

None of the following requires downtime, except where noted.

1. *Re-create the RocksDB tables.* If any zone or table uses a RocksDB storage profile, move it to another profile first. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed).
2. *Update the node configuration files.* Rename or delete every key from the tables in [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys), and remove the `replacementMode` property. 9.1.29 already accepts the new names of the renamed keys and the replacement keys, so you can update the files now. Test the final files on a 9.2 node in a staging cluster.
3. *Check the cluster configuration.* Run `cluster config show` and compare it with the tables. GridGain 9.1.29 converts the old key names when it loads the cluster configuration, so a cluster that runs 9.1.29 normally shows only the new names. If a key from the tables is still there, for example in a cluster that was initialized on an earlier 9.1 release, fix it before you run `upgrade start`, because cluster configuration changes are blocked during a rolling upgrade.
4. *Check `vars.env`.* Review `JVM_GC`, `JAVA_OPTS` for the CLI, and `GRIDGAIN9_EXIT_CONSOLE`. See [Platform and Packaging Changes](platform-and-packaging.md).
5. *Update SQL, scripts, and monitoring.* Change `CREATE ZONE ... WITH`, `schema.zone`, legacy system view columns, `__part`, unquoted `add`, and the metric source `storage.aipersist.<profile>`. The new system view column names and the new `CREATE ZONE` syntax already work on 9.1.29, so you can update these items before the upgrade.
6. *Prepare roles and users.* Write down the names of your users and roles, and the role names in LDAP `roleMapping` settings. Change applications and connection settings to the exact, lower-case user names that `SHOW USERS` prints on 9.2. See [User and Role Names Are Case-Sensitive](security-changes.md#user-and-role-names-are-case-sensitive) and [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase).
7. *Update the applications.* Move them to Java 21, and replace `PartitionManager` and `RecordSupportInternal`. Build and test them against the 9.2 client libraries.
8. *Back up the data.* On Ultimate Edition, take a snapshot and verify that it completed. See [Data Snapshots](../../snapshots/data-snapshots.md). On other editions, stop the cluster and copy the `work` directory of every node.

### When Is Preparation Complete?

{% hint style="info" %}
Preparation is complete only when all of these are true:

- Every item on your upgrade work list is addressed.
- No zone or table uses a RocksDB profile.
- The node configuration files and the cluster configuration contain none of the removed keys.
- Every server host and every application runs, or is ready to run, on Java 21 or later.
- A backup of the 9.1 data exists.

Do not begin the upgrade until all of these hold.
{% endhint %}

If you have a staging cluster, rehearse the whole procedure there first.

## Upgrade With a Rolling Upgrade

Use this path to restart the nodes one at a time. It needs the [Rolling Upgrade](../../upgrade/rolling-upgrade.md) feature of the Enterprise and Ultimate editions. Follow that page for the commands. The steps that are specific to 9.2 are:

1. *Pause the SQL workload.* Stop all SQL traffic, including JDBC, ODBC, scheduled queries, and tools. See [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed). Keep it paused until the commit finishes. Key-value and table API operations can continue.
2. *Start the upgrade.* Run `upgrade start --version <9.2 version>`. From now on, DDL and cluster configuration changes are rejected. You cannot cancel the upgrade after this point. See [Recovery Path](#recovery-path).
3. *Upgrade the nodes one at a time.* For each node, stop it, replace the binaries as described in [Rolling Upgrade](../../upgrade/rolling-upgrade.md), put the prepared 9.2 configuration in place, and start it on Java 21. Run `upgrade state` and confirm that the node appears in `nextVersionNodes` before you move to the next node.
4. *Commit the upgrade.* Run `upgrade commit`. The commit runs the role migration before it changes the cluster version. If the migration fails, the commit reports the error and the upgrade stays uncommitted. See [Role Names Are Migrated to Uppercase](security-changes.md#role-names-are-migrated-to-uppercase).
5. *Restart the nodes.* Restart the nodes after the commit, so that the system views get their 9.2 definitions. See [System View Columns Removed](sql-changes.md#system-view-columns-removed).
6. *Resume the SQL workload.*

{% hint style="info" %}
After the commit, the CLI command `upgrade state` can fail with `Expected the field `nextVersion` to be a primitive type in the JSON string but got `null``. This is a CLI display problem. The upgrade is committed.
{% endhint %}

## Upgrade With a Full-Cluster Upgrade

Use this path if you can stop the cluster. It does not need the Rolling Upgrade feature, and the SQL workload does not need a separate pause. Follow [Full-Cluster Upgrade](../../upgrade/full-cluster-upgrade.md). The steps that are specific to 9.2 are:

1. Take the backup, and stop the SQL workload and all nodes.
2. Replace the binaries on every node, put the prepared 9.2 configuration files in place, and set `JAVA_HOME` to Java 21 or later.
3. Start all nodes. The role migration runs when the cluster starts.
4. Continue with [Verify and Stabilize](#verify-and-stabilize).

## Verify and Stabilize

With the cluster running on 9.2, confirm it is healthy before you consider the upgrade complete:

1. *Check the cluster and the data.* Confirm that every node is a member of the cluster, run a query on a table, and compare row counts with the values before the upgrade.
2. *Check the logs.* Look for configuration errors and, if you use LDAP, for the message that an LDAP group is mapped to a role that does not exist.
3. *Check users and roles.* Log in with a legacy user, using its exact stored name, and with a user that has a migrated role. Change LDAP role mappings to the upper-case role names.
4. *Run the real workload.* Run your regression suite or production workload end to end, including SQL, and confirm it passes. Check the queries that depend on fractions of a second.
5. *Reconnect monitoring and tooling.* Update dashboards and alerts for the renamed storage profile metrics, and check the system view queries.
6. *Re-establish backups.* On Ultimate Edition, take a first snapshot on 9.2 and confirm it completes.

{% hint style="info" %}
The upgrade is complete when data integrity, application functionality, and monitoring all check out under the production workload. Keep the backup from before the upgrade and the 9.1 distribution until then.
{% endhint %}

## Troubleshooting

These are the problems that come up most often during the upgrade. If you hit something not covered here, contact MariaDB [support](https://mariadb.com/support/).

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| `ERROR: GridGain 9 requires Java 21 or newer, but <java> is Java <n>.` when a node or the CLI starts | `JAVA_HOME` or the `java` on the path is older than 21. | Set `JAVA_HOME` to Java 21 or later for the 9.2 scripts. |
| The Windows installer reports that GridGain 9 requires Java 21 or newer | The machine-wide `JAVA_HOME` points at an older Java. | Point the machine-wide `JAVA_HOME` at Java 21 or later, and run the installer again. |
| `Failed to parse HOCON: '<path>' configuration doesn't have the '<key>' sub-configuration` when a node starts | The node configuration file contains a key that 9.2 removed or renamed. | Rename or delete the key. See [Removed and Renamed Configuration Keys](configuration-and-storage.md#removed-and-renamed-configuration-keys). |
| `Failed to parse HOCON: Polymorphic configuration type is not correct: rocksdb` when a node starts | A storage profile uses `engine = rocksdb`. | Re-create the zones and tables on another engine, and remove the profile. See [RocksDB Storage Engine Removed](configuration-and-storage.md#rocksdb-storage-engine-removed). |
| `IGN-CMN-65535: Legacy query start protocol is no longer supported, the sending node must be upgraded` | A 9.1 node coordinated a SQL query that needs a 9.2 node. | Stop the SQL workload until the upgrade is committed. See [The Query Protocol Changed](sql-changes.md#the-query-protocol-changed). |
| `IGN-SQL-8: The query was mapped onto node '<node>' which runs version <version> and does not support latest query execution protocol ...` | A 9.2 node coordinated a SQL query that needs a 9.1 node during the rolling upgrade. | Wait for the upgrade to finish, and run the query again. |
| `upgrade commit` fails with `Legacy role names collide after uppercasing` or `Legacy role name conflicts with a built-in role` | Two roles differ only in case, or a role name becomes a built-in role name. | Rename or drop one of the roles on the 9.1 nodes, and run `upgrade commit` again. |
| `Authentication failed` for a user that worked on 9.1, or `GG-RBAC-2: User `<NAME>` is not found` | The name differs in case from the stored name. 9.2 nodes match user names exactly, and unquoted SQL names are converted to upper case. | Use the exact stored name, in double quotes in SQL. See [User and Role Names Are Case-Sensitive](security-changes.md#user-and-role-names-are-case-sensitive). |
| An LDAP user gets no privileges | An LDAP `roleMapping` names a role in a different case. | Change the mapping to the upper-case role name. See [LDAP Role Mappings](security-changes.md#ldap-role-mappings). |
| `Column 'NAME' not found in any table` on a system view, or `Column '__PART' not found in any table` | The query uses a column that 9.2 removed. | Use the replacement column. See [System View Columns Removed](sql-changes.md#system-view-columns-removed). |
| `SELECT * FROM system.zones` or another system view fails with `class java.lang.Integer cannot be cast to class java.lang.String` | The cluster went through a rolling upgrade, and the nodes were not restarted after the commit. | Restart the nodes. See [System View Columns Removed](sql-changes.md#system-view-columns-removed). |
| A 9.1 node does not start with `Some node has already been validated with a different version. Either use Rolling Upgrade or stop all nodes, then replace their binaries, then start them again` | The node runs a different version than the nodes that are already in the cluster, and no rolling upgrade is started, or the upgrade is already committed. | Start every node of the cluster on the same version, or start a rolling upgrade first. |
| A statement fails with `Failed to parse query` on `CREATE ZONE`, `DROP ZONE`, or an object named `add` | The statement uses the removed syntax, a qualified zone name, or the reserved word `ADD`. | See [SQL and System View Changes](sql-changes.md). |

## Recovery Path

GridGain does not provide a downgrade path from 9.2 to 9.1, and you cannot cancel a rolling upgrade. The `upgrade cancel` command and the matching REST call return `Cancel rolling upgrade is not implemented yet`. The role migration rewrites the stored cluster configuration, and 9.1 nodes cannot rejoin a cluster that runs 9.2 nodes.

The supported recovery depends on when you decide:

- *While the rolling upgrade is in progress.* You can stop an upgraded node and start it again from the 9.1 distribution, with the 9.1 configuration files. It rejoins the cluster. But the cluster stays in the upgrade state, and DDL and cluster configuration changes stay blocked, because nothing can end the upgrade except a commit. A commit needs every node to run 9.2. So the choice is to finish the upgrade, or to restore the backup.
- *After you commit, or after a full-cluster upgrade.* Restore the backup that you took before the upgrade into a 9.1 cluster. On Ultimate Edition, restore the snapshot, as described in [Data Snapshots](../../snapshots/data-snapshots.md). On other editions, stop all nodes and put the copies of the `work` directories back.

{% hint style="warning" %}
Restoring a backup replaces all data in the cluster with the data from the moment of the backup. Everything written after the backup is lost. Move the current data aside instead of deleting it if you may need it.
{% endhint %}

Restore the copies of all nodes together, and only copies that were taken at the same time. Do not restore only some of the nodes.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
