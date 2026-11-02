---
description: >-
  Move a GridGain 9 cluster between versions without downtime by rolling nodes
  one at a time, then committing the upgrade.
---

# Rolling Upgrade

{% hint style="info" %}
This feature is only available as part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

A rolling upgrade moves the cluster from one product version to another while the data plane stays available. Nodes are restarted one at a time on the new binaries; the cluster runs in a mixed-version state for the duration of the upgrade and is promoted to the new version atomically when the operator commits.

{% hint style="info" %}
Take a [snapshot](../snapshots/data-snapshots.md) of your data before starting. If the update process fails, you will be able to restore your cluster state from snapshot.
{% endhint %}

## Limitations

### Cluster Configuration Changes Are Blocked

While an upgrade is in progress, the cluster rejects cluster-wide configuration changes. Local node-level configuration changes are still allowed. Cluster-wide configuration changes are accepted again after the upgrade is committed or cancelled.

### Schema Changes and DDL Are Blocked

While an upgrade is in progress, the cluster rejects all schema-modifying DDL: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, index changes, distribution-zone changes, and similar statements. Read and DML operations (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) continue to work normally. DDL is accepted again after the upgrade is committed or cancelled.

### Rolling Upgrade and PITR Are Mutually Exclusive

A rolling upgrade and a point-in-time recovery (PITR) cannot run concurrently. Once a rolling upgrade has started, attempts to start PITR fail with an error naming the conflicting operation, and vice versa. The block is released when the upgrade is committed or cancelled.

## Rolling Upgrade Procedure

### Phase 1 — Start the Upgrade

#### Run `upgrade start`

```bash
upgrade start --version <V>
```

#### What Happens When You Start

1. The target version is validated. If it is not a valid GridGain version, the command fails immediately.
2. The cluster checks that no other cluster-wide operation (such as PITR) is in progress. If one is, the command fails with an error naming that operation.
3. The cluster records the target version and marks the upgrade as in progress. From this point, cluster-wide configuration changes are rejected.
4. The `upgrade.rolling` metrics are updated: `State` becomes `IN_PROGRESS`, `InitialVersion` records the cluster's version at the time of the start, and `TargetVersion` records the target.

The upgrade state is now durable: it survives any node restart, including the restart of any cluster-management node.

### Phase 2 — Roll the Nodes

Repeat the platform-specific procedure below for each node in the cluster, one at a time. After each node, confirm it has rejoined at the target version before moving to the next.

#### ZIP Archive

1. Stop the node.
2. If `work`, `etc`, and `log` are inside the install tree, move them outside before deleting the install tree. (If they are already outside the install tree, no action is needed.)
3. Replace the contents of the install directory with the unpacked new ZIP.
4. Copy `gridgain.properties` from the new install's `etc/` directory over the preserved file in your `etc/` directory, so that the version metadata matches the new binaries.
5. Start the node back up using the start script from the new install tree.
6. Run `upgrade state` and confirm the node appears in the `nextVersionNodes` list.

#### DEB / RPM Package

1. Stop the node.
2. Run the standard package-manager upgrade command for your distribution. The package upgrade preserves your existing `vars.env` and `gridgain-config.conf` files in a `backup/` subdirectory under the configuration directory and registers the service unit for the new binaries. The persistent `work` directory is left untouched.
3. Restart the GridGain service using `systemctl` (or the equivalent for your init system).
4. Run `upgrade state` and confirm the node appears in the `nextVersionNodes` list.

#### Docker

1. Stop the container for this node.
2. Update the image tag in your run command, Compose file, or Kubernetes manifest to the new version.
3. Start the container against the same persistent volume that holds `work`, `etc`, and `log`.
4. Run `upgrade state` and confirm the node appears in the `nextVersionNodes` list.

After all nodes are upgraded, proceed to phase 3.

### Phase 3 — Complete the Upgrade

#### Run `upgrade commit`

```bash
upgrade commit
```

#### What Happens on Commit

1. The cluster reads the current upgrade state and the list of active nodes.
2. The cluster validates that every active node is running the target version. If any node is still on the source version, the commit fails with an error listing the offending nodes by name and reported version.
3. The cluster validates that every node it knows about has rejoined fully. If a node has not rejoined, the commit fails with an error.
4. The cluster's recorded version is set to the target version, the in-progress flag is cleared, and cluster-wide configuration changes are accepted again.
5. Cluster-wide features that depend on the new version are activated.
6. The `upgrade.rolling` metric `State` becomes `NOT_STARTED`.

## Monitoring Update Progress

### The `upgrade state` Command

Returns four fields:

- `currentVersion` — the cluster's recorded version (the source version while the upgrade is in progress).
- `nextVersion` — the target version, or `null` when no upgrade is in progress.
- `nextVersionNodes` — names of nodes whose running version equals `nextVersion`.
- `currentVersionNodes` — names of nodes whose running version equals `currentVersion`.

### Metrics

The metric source `upgrade.rolling` exposes the following gauges:

- `State` — `NOT_STARTED` or `IN_PROGRESS`.
- `InitialVersion` — cluster version at the time the upgrade started; empty when no upgrade is in progress.
- `TargetVersion` — target version; empty when no upgrade is in progress.
- `UpgradedNodes` — comma-separated list of node names that have reached the target version.
- `NotUpgradedNodes` — comma-separated list of node names still on the source version.

## Recovery and Abort

### Cancelling an In-Progress Upgrade

#### Run `upgrade cancel`

```bash
upgrade cancel
```

#### Preconditions for Cancel

The cancel operation validates that every active node is on the source version. If any node is still on the target version (that is, it has been rolled forward to the new binaries), the cancel fails with an error listing the offending nodes. To cancel after binaries have been swapped on some nodes, the operator must first roll those nodes back to the source binaries.

When cancel succeeds, the cluster clears the in-progress flag while leaving the recorded version unchanged, accepts cluster-wide configuration changes again, and releases the block that prevents PITR from starting.

### Resuming After a Coordinator or Cluster-Management Node Restart

The upgrade state is durable across cluster restarts and cluster-management leader failover. You can safely restart your CLI session, and any cluster-management node reboot during a roll does not require restarting the upgrade. When a node rejoins after a restart, it picks up the in-progress upgrade state from the cluster and applies the cluster-wide configuration block locally.

### Handling Dead or Unresponsive Nodes

#### Reviving a Node at the Target Version

A node that was upgraded but is currently down does not appear as an active cluster member and is not counted toward upgrade progress. Bring it back up on the target binaries; it will rejoin and `upgrade state` will surface it under `nextVersionNodes`.

#### Evicting an Unrecoverable Node

A node that the cluster knows about but that has not rejoined fully blocks `upgrade commit`. Remove the node from the cluster following the standard topology-management procedure, then retry commit.
