---
description: >-
  Step-by-step procedure for upgrading a GridGain 8.9.39 cluster to 8.10 with Rolling Upgrades or offline, with verification, troubleshooting, and a recovery path back to 8.9.
---

# Upgrading a Cluster from GridGain 8.9 to 8.10

This guide describes how to upgrade a GridGain 8.9.39 cluster to GridGain 8.10, and how to check that the upgrade worked.

Before you start, read [What to Know Before Upgrading](before-you-upgrade.md). It helps you choose between a rolling and an offline upgrade and lists the changes that this guide refers to.

The procedure has five phases: prerequisites, compatibility check, preparation, the upgrade itself, and verification.

GridGain does not support a downgrade from 8.10 to 8.9. If you need to go back to 8.9, see the [Recovery Path](#recovery-path).

## Prerequisites

Confirm all of the following before you start:

- The cluster runs GridGain 8.9.39. If it runs an earlier 8.9.x release, the behavior can differ in places. Read the [release notes](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/gridgain-8) for the releases between your version and 8.9.39 first.
- Java 17 or later is installed on every server host. You can keep running the 8.9 nodes on their current Java version until you restart them. Each node switches to Java 17 when you restart it from the 8.10 distribution, so set `JAVA_HOME` for the 8.10 scripts before you start the node.
- A valid GridGain license is installed, and it enables every feature that your configuration uses. See [Per-Feature License Checks](security-and-licensing.md#per-feature-license-checks).
- You chose an [upgrade path](before-you-upgrade.md#choose-your-upgrade-path) and scheduled a downtime window if the path needs one.
- Storage for a backup of the 8.9 data is available outside the work directory. The backup is recommended: it is the only way back to 8.9 after the upgrade is finished. See [Step 3](#step-3-back-up-the-data).
- The 8.10 distribution is unpacked next to the 8.9 one. Keep the 8.9 distribution until the upgrade is validated, because recovery needs it.

## Check Compatibility

Most upgrade work is conditional: each area below may or may not apply to your deployment. Review every area and record each item that applies:

1. *Review the platform and module changes.* Java 17, removed modules, upgraded dependencies, and packaging. See [Platform, Modules, and Packaging](platform-and-modules.md).
2. *Review the configuration changes.* Changed defaults, new limits, and removed system properties. See [Configuration and Default Value Changes](configuration-and-defaults.md).
3. *Review the security and license changes.* New permissions, closed-by-default features, and per-feature license checks. See [Security, Permission, and Licensing Changes](security-and-licensing.md).
4. *Review the client changes.* Thin client timeouts, DNS, transactions, .NET, and C++. See [Client and Driver Changes](clients-and-drivers.md).

{% hint style="info" %}
You are done with this phase when you have gone through every area above and written down the items that apply to you. That list is your upgrade work list: every item on it must be addressed before you upgrade.
{% endhint %}

## Prepare the Distribution, Configuration, and Cluster

None of the following requires downtime, except where noted.

### Preparation Tasks

1. *Build the 8.10 `libs` folder.* Do not copy the `libs` folder of 8.9 into the 8.10 distribution.
   - If you run only the modules that ship in `libs` by default, use the 8.10 `libs` folder exactly as shipped.
   - Otherwise, compare your 8.9 `libs` and `libs/optional` folders with a fresh 8.9 distribution to list the modules you added or moved by hand. Copy only those that you use and that still exist in 8.10.
   - A module that you enabled in 8.9 by moving it into `libs`, for example `ignite-opencensus`, is not enabled in 8.10 until you do the same there.
   - `control-center-agent` is in `libs/optional`. If you use it, move it into `libs`, and use Control Center 2026.2.

   See [Removed Modules and Integrations](platform-and-modules.md#removed-modules-and-integrations) and [Distribution and Packaging Changes](platform-and-modules.md#distribution-and-packaging-changes).
2. *Update applications and build files.* Apply the changes from your work list: Spring, Hibernate, removed modules, and client changes.
3. *Update the node configuration.* Remove unsupported system properties, resolve new limits, and set the new properties that your features need.
4. *Keep the persistent data in place.* Native persistence only. Each node must keep its consistent ID and the same `storagePath`, `walPath`, and `walArchivePath`. If you do not set these properties, the default location is the `work` folder, and the `work` folder of a new distribution is empty. Point the new node at the old one by setting the `IGNITE_WORK_DIR` environment variable or the paths in the configuration.
5. *Prepare the 8.9 cluster.* Rolling path: configure Rolling Upgrades and back up the data, as described in steps 1 to 3 of [Upgrade With Rolling Upgrades](#upgrade-with-rolling-upgrades). Offline path: back up the data as described in [Upgrade Without Rolling Upgrades](#upgrade-without-rolling-upgrades).
6. *Check caches that must stay available.* Configure at least one backup for them, or plan a maintenance window. See [Application Behavior During a Rolling Upgrade](#application-behavior-during-a-rolling-upgrade).

### When Is Preparation Complete?

{% hint style="warning" %}
Preparation is complete only when all of these are true:

- Every item on your upgrade work list is addressed.
- The 8.10 `libs` folder contains only modules that exist in 8.10.
- Every server host and every application runs, or is ready to run, on Java 17 or later.
- A backup of the 8.9 data exists (recommended). See [Step 3](#step-3-back-up-the-data).
- On the rolling path, every 8.9 node has `rollingUpdatesEnabled=true`, and caches that must stay available have at least one backup.

Do not begin the upgrade until all of these hold.
{% endhint %}

If you have a staging cluster, rehearse the whole procedure there first.

## Upgrade With Rolling Upgrades

Use this path to upgrade the nodes one at a time, without stopping the cluster for the upgrade itself. It needs [Rolling Upgrades](../../upgrade/rolling-upgrades.md). The steps are the same for both editions, except for the backup: Ultimate Edition takes a snapshot, and Enterprise Edition copies the persistence folders, which needs a short stop of the whole cluster. If you cannot use Rolling Upgrades, or you prefer to stop the cluster, see [Upgrade Without Rolling Upgrades](#upgrade-without-rolling-upgrades).

The procedure has three parts:

- [steps 1–3](#step-1-configure-rolling-upgrades) configure Rolling Upgrades on the 8.9 cluster and back up its data;
- [steps 4–6](#step-4-start-the-rolling-upgrade) start the rolling upgrade, upgrade the nodes one at a time, and finish it;
- the checks that follow are in [Verify and Stabilize](#verify-and-stabilize).

If authentication is enabled, pass the credentials to every command: `control.sh --user <user> --password <password> ...`, and on Ultimate Edition also `snapshot-utility.sh ... -user=<user> -password=<password>`.

### Step 1: Configure Rolling Upgrades

Every 8.9 node, on both editions, must have `rollingUpdatesEnabled=true` in its `GridGainConfiguration` *before* the upgrade. Replace the license path with your own, and skip the properties that you already have:

```xml
<bean class="org.gridgain.grid.configuration.GridGainConfiguration">
    <property name="licenseUrl" value="file:///path/to/gridgain-license.xml"/>
    <property name="rollingUpdatesEnabled" value="true"/>
</bean>
```

`GridGainConfiguration` is an element of `IgniteConfiguration.pluginConfigurations`. Enabling Rolling Upgrades adds a small amount of data to every network message. See [Performance Considerations](../../upgrade/rolling-upgrades.md#performance-considerations).

{% hint style="info" %}
*Ultimate Edition only.* To take a snapshot in [step 3](#step-3-back-up-the-data), also add a `snapshotConfiguration` to the `GridGainConfiguration` of every node:

```xml
<property name="snapshotConfiguration">
    <bean class="org.gridgain.grid.configuration.SnapshotConfiguration">
        <property name="snapshotsPath" value="/data/snapshots/node1"/>
    </bean>
</property>
```

Store the snapshots outside of the work directory, so that you can keep them when you remove the data. Nodes can use the same `snapshotsPath`, because each snapshot gets a subfolder for every node. This also works for nodes on different hosts if the folder is a shared file system that all hosts mount at the same path.
{% endhint %}

### Step 2: Restart the Cluster

You cannot add `rollingUpdatesEnabled` one node at a time. A node with `rollingUpdatesEnabled=true` is not allowed to join a cluster whose nodes do not have it, even if all nodes run the same version.

If the property is already set on every node, skip this step. Otherwise, stop the whole cluster, add the properties from [step 1](#step-1-configure-rolling-upgrades) to the configuration of every node, and start the cluster again. This is a planned downtime. With native persistence, the data and the baseline are kept.

{% hint style="info" %}
If you have to stop the whole cluster anyway, you can upgrade offline in the same window. See [Upgrade Without Rolling Upgrades](#upgrade-without-rolling-upgrades).
{% endhint %}

### Step 3: Back Up the Data

After the rolling upgrade is finished, the backup that you take now is your only way to return to 8.9. GridGain recommends that you take it. See [Recovery Path](#recovery-path). Follow the part for your edition.

#### Ultimate Edition: Take a Full Snapshot

When the cluster is running with the new configuration, take a full snapshot on 8.9:

```shell
snapshot-utility.sh snapshot -type=full
```

The command ends with `Command [SNAPSHOT] successfully finished in <n> seconds.` Like `control.sh`, `snapshot-utility.sh` connects to port 11211 of the local host by default. If your REST connector uses another port or host, pass `-port=<port>` and `-host=<host>`, for example `snapshot-utility.sh snapshot -type=full -port=11300`. Then list the snapshots and write down the ID of the one that you just took:

```shell
snapshot-utility.sh list
```

The line of the new snapshot shows its ID and the product version that took it:

```text
ID=<snapshot id>, CREATED=..., TYPE=FULL, ..., PRODUCT VERSIONS=[8.9.x#<build>-sha1:<hash>]
```

You need the ID if you decide to [recover the 8.9 state](#recover-from-a-snapshot).

{% hint style="info" %}
Snapshots that 8.9 created, both full and incremental, can be listed, checked, and restored with the 8.10 `snapshot-utility.sh` after the upgrade. A new incremental snapshot taken on 8.10 on top of the 8.9 full snapshot is also supported.
{% endhint %}

#### Enterprise Edition: Copy the Persistence Folders

Enterprise Edition has no snapshots. The backup is a copy of the persistence folders of every node. The upgrade itself runs without downtime, but the copy does not: it needs a short stop of the whole cluster.

Stop all nodes before you copy. Do not copy the folders of running nodes, and do not copy the nodes one at a time while the others keep working. Data changes between the moments that you copy each node, so a restore would mix primary partitions and backups from different moments, and the cluster would hold inconsistent data. Only a copy of stopped nodes, taken from a deactivated cluster, is consistent.

If you stopped the whole cluster in [step 2](#step-2-restart-the-cluster), take the copy in that window, before you start the nodes again. Otherwise, stop the cluster for it now:

1. Deactivate the cluster with `control.sh --set-state INACTIVE --yes`, and stop all nodes.
2. On every node, copy the folders that `storagePath`, `walPath`, and `walArchivePath` point to, to a location outside the work directory. If you do not set these properties, copy the `db` folder of the work directory instead. Keep the copy of each node apart from the copies of the others, and note which node it came from. Keep the node configuration and the consistent ID as well.
3. Start the nodes again with the 8.9 distribution and the configuration from [step 1](#step-1-configure-rolling-upgrades). With native persistence, the cluster activates with the old baseline when every baseline node is back. Check it with `control.sh --baseline`.

### Step 4: Start the Rolling Upgrade

```shell
control.sh --rolling-upgrade start --yes
```

Without the `--yes` option, the command asks for confirmation. When you run it from a script, always pass `--yes`.

The command prints `Rolling upgrade mode successfully enabled.` Check the status:

```shell
control.sh --rolling-upgrade status
```

Before you start, it shows `Rolling upgrade is disabled.` After `start`, it shows `Rolling upgrade is enabled.`, and every node is listed under the nodes that are not updated:

```text
Rolling upgrade is enabled.
Initial version: 8.9.x#<build>-sha1:<hash>
Target version: N/A
List of alive nodes in the cluster that are not updated yet:
  <node ID>
  <node ID>
  <node ID>
List of alive nodes in the cluster that are updated:
  none
```

Setting `rollingUpdatesEnabled` is not enough on its own. The status stays `disabled` until you run this command.

Start the first 8.10 node only after this command. Otherwise the node is rejected (see [Troubleshooting](#troubleshooting)).

{% hint style="warning" %}
All `control.sh --rolling-upgrade` commands exit with code 0 also when they fail (for example when `start` or `finish` is refused), so check the message and not the exit code.
{% endhint %}

From the first upgraded node on, use the `control.sh` of the 8.10 distribution for the `--rolling-upgrade` commands.

### Step 5: Upgrade the Nodes One at a Time

For each node, in any order:

1. Stop the node and wait until its process has exited.
2. Start the node from the 8.10 distribution with the same configuration, work directory, and consistent ID.
3. Wait until the node has joined and rebalancing has finished. Look in the log of the new node for the `Finish exchange future` message and then for either `Completed (final) rebalancing` (data moved to the node) or `Skipping rebalancing (nothing scheduled)` (no data changed while the node was down). Do not stop the next node before you see one of them. You can also use `control.sh --metric cluster`: the value `cluster.Rebalanced` is `false` while data moves and `true` when it is done. For a few seconds after the node joins, it can still show `true` before rebalancing starts, so wait until it shows `true` on several checks in a row, a few seconds apart.
4. Run `control.sh --rolling-upgrade status`. After each node, one node moves from the not-updated list to the updated list. When the first node is upgraded, the status looks like this, and `Target version` now shows the 8.10 build:

```text
Rolling upgrade is enabled.
Initial version: 8.9.x#<build>-sha1:<hash>
Target version: 8.10.x#<build>-sha1:<hash>
List of alive nodes in the cluster that are not updated yet:
  <node ID>
  <node ID>
List of alive nodes in the cluster that are updated:
  <node ID>
```

The status lists the first 8 characters of the node ID, and a restarted node gets a new ID, so check that the updated list grows by one and the not-updated list shrinks by one. To identify a node, take its new ID from the node log: the line `Local node [ID=...]` in the startup banner, or `locNode=...` in the `Topology snapshot` line.

The new node writes a warning to its log that the build versions differ, but that they are compatible. This is expected.

{% hint style="warning" %}
`control.sh` connects to the first node on port 11211 by default. During a rolling upgrade, that node can be the one you stopped, and the command fails with `Connection to cluster failed`. Use `--host` and `--port` to connect to a running node. The port is the one of the REST connector (11211 and above), not the thin client port.
{% endhint %}

{% hint style="warning" %}
Do not leave the cluster with mixed versions for long. See [Rolling Upgrades](../../upgrade/rolling-upgrades.md) for the performance considerations.
{% endhint %}

### Step 6: Finish the Rolling Upgrade

When the status shows `none` under the nodes that are not updated, finish the rolling upgrade:

```shell
control.sh --rolling-upgrade finish --yes
```

If you run `finish` while an 8.9 node is still in the cluster, it is refused with `Rolling Upgrade mode cannot be disabled` and lists the nodes of each version. The exit code is 0 in this case too.

A successful `finish` prints `Rolling upgrade mode successfully disabled.` Afterward, `control.sh --rolling-upgrade status` shows `Rolling upgrade is disabled.`, the initial version is the 8.10 build (for example `Initial version: 8.10.x#<build>-sha1:<hash>`), and `Target version` is `N/A`. New 8.10 features become available.

Continue with [Verify and Stabilize](#verify-and-stabilize).

### Application Behavior During a Rolling Upgrade

While the upgrade is in progress, the cluster stays available. Clients that are connected to a node that is being stopped see errors for a short time. Plan for the following:

- *Applications must reconnect and repeat the failed operation.* A JDBC connection that was open on a stopped node fails with `Failed to handle JDBC request because node is stopping`, and you must open a new one. Give the driver more than one address (for example `jdbc:ignite:thin://host1:10800,host2:10800,host3:10800`), so that a new connection does not go to the node that is down. The Java thin client reconnects and retries by itself.
- *Caches without backups are unavailable for the partitions on the stopped node.* A cache with `backups=0` (the default) fails with `CacheInvalidStateException`, and the errors continue after the node returns until you reset the lost partitions. The log of the nodes shows which cache is affected: `Detected lost partitions [grp=SQL_PUBLIC_NB, parts=[...]]`. Configure at least one backup for the caches that must stay available, or plan a maintenance window for the others.
- *With native persistence, the data is not lost.* After the node is back, run `control.sh --cache reset_lost_partitions <cache name>` (or `--all`), and the cache works again. You can reset the caches once, after the last node is back. The cache of an SQL table is named `SQL_<SCHEMA>_<TABLE>`, for example `SQL_PUBLIC_NB`, unless you set `CACHE_NAME` when you created the table.
- *Two features stay off while an 8.9 node is in the cluster.* A service with call interceptors is refused (`not all nodes in the cluster support service call interceptors`), and the separate scale-up and scale-down baseline auto-adjust commands (`control.sh --baseline scale_up_auto_adjust` and `scale_down_auto_adjust`) fail. Both start working when the last 8.9 node is replaced. GridGain 8.9.39 nodes advertise these two features without implementing them, and 8.10 does not rely on that advertisement.

Each node needs time to stop, join, and rebalance. Only the data that changed while the node was down is moved.

## Upgrade Without Rolling Upgrades

If you can stop the cluster, you do not need `rollingUpdatesEnabled` and you do not need `control.sh --rolling-upgrade`:

1. Back up the 8.9 data (recommended, see [Step 3](#step-3-back-up-the-data)), and stop all nodes.
   - *Ultimate Edition.* Take a full snapshot with `snapshot-utility.sh snapshot -type=full` while the cluster is running, then stop all nodes. The snapshot needs a `snapshotConfiguration` on the 8.9 nodes, as in [step 1](#step-1-configure-rolling-upgrades), but not `rollingUpdatesEnabled`. Write down the snapshot ID, as in [step 3](#ultimate-edition-take-a-full-snapshot).
   - *Enterprise Edition.* Deactivate the cluster, stop all nodes, and copy the persistence folders of every node, as in [step 3](#enterprise-edition-copy-the-persistence-folders). The cluster is stopped anyway, so the copy needs no extra downtime.
2. Install the 8.10 distribution and Java 17 or later. Do not copy the old `libs` folder, and review the [removed modules](platform-and-modules.md#removed-modules-and-integrations).
3. Start all nodes from the 8.10 distribution with the same configuration, work directory, and consistent IDs. You can start them together or one after another, in any order.
4. Continue with [Verify and Stabilize](#verify-and-stabilize).

With native persistence, the cluster activates by itself with the old baseline as soon as every baseline node is back, and all data is kept. You do not run any `control.sh --rolling-upgrade` command. To confirm, run `control.sh --baseline`: it shows `Cluster state: active` and every baseline node as `ONLINE`.

To go back to 8.9 after an offline upgrade, restore the backup from step 1, as described in [After Finish](#after-finish).

On Ultimate Edition, there is another way to upgrade: take the full snapshot on 8.9, start a new empty 8.10 cluster with the same number of nodes, and restore the snapshot into it with the 8.10 `snapshot-utility.sh restore -id=<snapshot id>`. The 8.10 utility can restore snapshots that 8.9 created. Use this way to move to new hosts, or to keep the old 8.9 cluster untouched.

## Verify and Stabilize

With the cluster running on 8.10, confirm it is healthy before you consider the upgrade complete:

1. *Check the cluster and the data.* Run `control.sh --baseline` and compare the node list with your baseline. The output starts with `Cluster state: active` and lists every node as `ONLINE`. Run a query from a client, compare row counts with the values before the upgrade, and run `control.sh --cache idle_verify`. A healthy run ends with `idle_verify check has finished, no conflicts have been found.`
2. *Reset lost partitions.* If you have caches without backups, look for `Detected lost partitions` in the node logs and reset them as described in [Application Behavior During a Rolling Upgrade](#application-behavior-during-a-rolling-upgrade).
3. *Run the real workload.* Run your regression suite or production workload end to end and confirm it passes.
4. *Reconnect monitoring and tooling.* Confirm that the nodes connect to Control Center 2026.2 (the agent must be in `libs`), check the node logs for license errors, and update tooling that reads JMX object metrics.
5. *Re-establish backups.* On Ultimate Edition, take a first snapshot on 8.10 and confirm it completes. On Enterprise Edition, plan your regular backups of the persistence folders.
6. *Optional: switch to Lucene 10.* If you plan to use it, switch every node after the upgrade is finished. See [Lucene](platform-and-modules.md#lucene).

{% hint style="warning" %}
The upgrade is complete when data integrity, application functionality, and monitoring all check out under the production workload. Keep the pre-upgrade backup and the 8.9 distribution until then: after `finish`, they are the only way back to 8.9.
{% endhint %}

## Troubleshooting

These are the problems that come up most often during the upgrade. If you hit something not covered here, contact [GridGain Support](https://mariadb.com/support/). Problems with `Connection to cluster failed`, a refused `finish`, a restarted node missing from the status, and lost partitions are described where they occur: see [Step 5](#step-5-upgrade-the-nodes-one-at-a-time), [Step 6](#step-6-finish-the-rolling-upgrade), and [Application Behavior During a Rolling Upgrade](#application-behavior-during-a-rolling-upgrade).

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| `Rolling Upgrade mode cannot be enabled. Consider changing 'GridGainConfiguration.rollingUpdatesEnabled' configuration property.` on `control.sh --rolling-upgrade start` | `rollingUpdatesEnabled` is not set on the nodes. The status also stays `disabled` until you run `start`, even when the property is set. | Set `rollingUpdatesEnabled=true` on every node and restart the cluster ([Step 2](#step-2-restart-the-cluster)), then run `start --yes`. |
| `Rolling updates are not properly configured` when a node starts | The node and the cluster it joins differ in `rollingUpdatesEnabled`. Either the node has it set and the cluster does not, or the cluster has it set and the node does not. The second case also hits applications that start a thick client (a node in client mode) while the rolling upgrade path is configured. | If the cluster lacks the property, stop the whole cluster, add the property to every node, and start the cluster again ([Step 2](#step-2-restart-the-cluster)). If a thick client lacks it, add `rollingUpdatesEnabled=true` to the `GridGainConfiguration` of the client. |
| `GridGain snapshots are not configured` (error 4400) from `snapshot-utility.sh` | `snapshotConfiguration` is not set in the `GridGainConfiguration` of the node. | Add `snapshotConfiguration` with a `snapshotsPath` to every node and restart the cluster ([Step 1](#step-1-configure-rolling-upgrades)). |
| `The node has been rejected due to disabled Rolling Upgrade` when a node starts | Either an 8.10 node joins before you ran `start`, or an 8.9 node joins after `finish`. | In the first case, run `control.sh --rolling-upgrade start --yes` before you start the 8.10 node. In the second case, an 8.9 node cannot rejoin after `finish`: see [Recovery Path](#recovery-path). |
| A node starts on an empty baseline with none of your caches | The node does not use the same consistent ID and persistence directories as the node it replaces. The `work` folder of the new distribution is empty. | Stop the node. Set the same consistent ID, and point `storagePath`, `walPath`, and `walArchivePath`, or `IGNITE_WORK_DIR`, at the existing data. Start the node again. |
| `ignite.sh`, `ignite.bat`, `control.sh`, or `control.bat` refuses to start | `JAVA_HOME` points at a JDK older than 17. | Set `JAVA_HOME` to Java 17 or later for the 8.10 scripts. |

## Recovery Path

GridGain does not support a downgrade from 8.10 to 8.9. An 8.9 node cannot join a cluster after the rolling upgrade is finished, and data that 8.10 writes may use formats that 8.9 does not read. For example, an 8.9 node does not start if the data has a `PARTITIONED` cache with a vector index: 8.9 supports a vector index only on a `REPLICATED` cache, and the node stops with `Failed to create vector index. Only REPLICATED cache mode is supported.`

The supported way back depends on when you decide:

- Before you finish the rolling upgrade, you revert it. No backup is needed: see [Before Finish](#before-finish).
- After `finish`, or after an offline upgrade, you restore the backup that you took before the upgrade: see [After Finish](#after-finish).

{% hint style="warning" %}
Restoring a backup replaces all data in the cluster with the data from the moment of the backup. Everything written after the backup is lost, including the data that 8.10 wrote. Move the current data aside instead of deleting it if you may need it.
{% endhint %}

If you use data center replication, read [Upgrade and Recovery to 8.9](other-changes.md#upgrade-and-recovery-to-8.9) before you recover.

The backup that you can restore depends on your edition:

| Edition | Backup you take before the upgrade | Recovery |
| --- | --- | --- |
| Ultimate | A full snapshot with `snapshot-utility.sh` | Restore the snapshot into an 8.9 cluster: [Recover From a Snapshot](#recover-from-a-snapshot). |
| Enterprise | A copy of `storagePath`, `walPath`, and `walArchivePath` of every node | Put the copies back and start 8.9: [Recover From a Copy of the Persistence Folders](#recover-from-a-copy-of-the-persistence-folders). |

### Before Finish

While the rolling upgrade is still in progress, you can revert it (see [Reverting Rolling Upgrades](../../upgrade/rolling-upgrades.md#reverting-rolling-upgrades)). Move the nodes that you already upgraded back to 8.9. For each of them, stop the node and start it again from the 8.9 distribution with the same configuration, work directory, consistent ID, and Java version. The node rebalances from the 8.10 nodes, and tables, columns, and indexes that you created through 8.10 nodes stay visible.

After all nodes are back on 8.9, the status still shows the target version 8.10 and lists all nodes as not updated. Run `control.sh --rolling-upgrade finish --yes` to leave the rolling upgrade mode. The initial version stays 8.9.x.

### After Finish

After `finish`, an 8.9 node cannot join the cluster any more. This section also applies after an offline upgrade, where there is no `finish`. Use one of the two recoveries below. Both return the cluster to the state at the time of the backup.

#### Recover From a Snapshot

Ultimate Edition only. Use the full snapshot that you took before the upgrade:

1. Stop all nodes.
2. Remove the data of the nodes, or move it to another location if you may need the 8.10 data. If you set `storagePath`, `walPath`, and `walArchivePath`, remove the folders they point to. The `db` folder of the work directory then holds only small binary metadata, and it can stay. If you did not set them, remove the `db` folder of the work directory. Keep the snapshot folder.
3. Start the nodes from the 8.9 distribution, with the 8.9 configuration. It must still have a `snapshotConfiguration` whose `snapshotsPath` points at the folder that holds your snapshots. Activate the cluster with `control.sh --set-state ACTIVE --yes`.
4. Find the snapshot ID. Run the 8.9 `snapshot-utility.sh list`, and choose the snapshot that you took before the upgrade: its `PRODUCT VERSIONS` shows 8.9.x. A snapshot whose `PRODUCT VERSIONS` shows 8.10.x was taken after the upgrade, so it does not hold the state that you validated on 8.9.
5. Restore the snapshot with the 8.9 `snapshot-utility.sh restore -id=<snapshot id>`. A successful restore prints `Restored: true`.
6. Check the data: compare row counts with the values before the upgrade and run `control.sh --cache idle_verify`.

#### Recover From a Copy of the Persistence Folders

Enterprise Edition only. Use the copies that you took before the upgrade, as described in [Step 3](#enterprise-edition-copy-the-persistence-folders). To recover the 8.9 state, restore the copies and start the cluster on 8.9:

1. Stop all nodes.
2. On every node, move the current `storagePath`, `walPath`, and `walArchivePath` folders aside, or the `db` folder if you did not set them. Remove them instead if you do not need the 8.10 data. Copy the backup of that same node back to the same paths.
3. Start the nodes from the 8.9 distribution, with the 8.9 configuration and the same consistent IDs. When every baseline node is back, the cluster activates with the old baseline.
4. Check the data: run `control.sh --baseline`, compare row counts with the values before the upgrade, and run `control.sh --cache idle_verify`.

Restore the copies of all nodes together, and only copies that were taken in the same stop of the cluster. Do not restore only some of the nodes, and do not mix copies from different moments.
