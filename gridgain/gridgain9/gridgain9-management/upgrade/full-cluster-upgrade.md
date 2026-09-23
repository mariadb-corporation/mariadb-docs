---
description: >-
  Upgrade a GridGain 9 cluster by stopping every node, replacing the binaries,
  and restarting the cluster on the new version.
---

# Full-Cluster Upgrade

{% hint style="warning" %}
A full-cluster upgrade requires shutting down the entire cluster. Use [Rolling Upgrade](rolling-upgrade.md) to upgrade without downtime.
{% endhint %}

A full-cluster upgrade stops every node in the cluster, replaces the binaries on each node, and starts the cluster back up on the new version. The cluster is unavailable for the duration of the procedure. This page also documents the per-platform mechanics of replacing binaries on a single node — those mechanics are referenced from [Rolling Upgrade](rolling-upgrade.md) for its per-node steps.

## Limitations

### Downtime Required for the Entire Cluster

The data plane is unavailable from the moment the first node stops until every node has been restarted on the new binaries and the cluster has formed.

### No Rollback to Pre-9 Versions

The procedure on this page upgrades from one 9.x version to another. There is no supported procedure for downgrading to versions older than 9.0.

### Mutual Exclusion with PITR

PITR cannot be in progress while the cluster is being restarted. PITR state survives a cluster restart, so a PITR that was in progress before stop will still be in progress after start. Resolve any pending PITR operation before stopping the cluster.

## The Full-Cluster Upgrade Procedure

### Phase 1 — Take a Snapshot

Take a [snapshot](../snapshots/data-snapshots.md) of your data before stopping the cluster. The snapshot is your only supported recovery path if a binary upgrade leaves persistent data unreadable on the new version. Verify that the snapshot completed successfully before proceeding.

### Phase 2 — Stop the Cluster

#### Stop Each Node Cleanly

Stop every node using your standard node-stop procedure (the package's `stop` script for DEB/RPM installs, container stop for Docker, or sending the appropriate signal to the JVM for ZIP installs).

#### Verify Clean Shutdown

Confirm that each node has fully exited and released its files before continuing. A subsequent restart on the new binaries against an unfinished shutdown can leave the persistent state inconsistent.

#### Preserve `work`, `etc`, and `log` Directories

These directories hold the cluster's persistent state, configuration, and logs. They must be preserved across the binary swap. The per-platform sections below describe how each packaging format handles them.

### Phase 3 — Replace Binaries on Every Node

Apply the platform-specific procedure below to every node. Do not start any node until all nodes have been updated; nodes are started together in phase 4.

#### ZIP Archive

1. If `work`, `etc`, and `log` are inside the install tree, move them outside before deleting the install tree. (If they are already outside the install tree, no action is needed.)
2. Replace the contents of the install directory with the unpacked new ZIP.
3. Copy `gridgain.properties` from the new install's `etc/` directory over the preserved file in your `etc/` directory, so that the version metadata matches the new binaries. This step is specific to ZIP installs; the DEB/RPM and Docker procedures handle the equivalent automatically.

#### DEB / RPM Package

1. With the node already stopped from phase 2, run the standard package-manager upgrade command for your distribution. The package upgrade preserves any existing `vars.env` and `gridgain-config.conf` files in a `backup/` subdirectory under the configuration directory, ensures the install, configuration, log, PID, and work directories exist with the correct ownership, and registers the service unit (systemd or Upstart) for the new binaries. The persistent `work` directory is left untouched, so existing cluster state is preserved.
2. Do not start the service yet — phase 4 starts every node together.

#### Docker

1. Update the image tag in your run command, Compose file, or Kubernetes manifest to the new version. The container itself is started in phase 4, against the same persistent volume that holds `work`, `etc`, and `log`.

### Phase 4 — Start the Cluster

#### Start Each Node

Start every node using its normal start procedure. Order does not matter — the cluster forms once a quorum of cluster-management nodes is up.

#### Verify Cluster Formation

Confirm that every node is an active member of the cluster and that the cluster reports a healthy state.

#### Verify Data Recovery

Run a sample of read operations against pre-existing tables to confirm that the data is accessible.

#### Verify Cluster Health Metrics

Check the standard cluster health metrics. Persistent state recovery happens during node startup; errors surfaced during this phase usually point at storage or cluster-state issues.

## What the Cluster Does at First Start on the New Version

When you start a cluster on new binaries against existing persistent state, the cluster:

- Restores cluster-management state from disk.
- Replays the cluster metadata log, re-applying schemas, indexes, and distribution zones.
- Reopens the persistent storage files. There is no on-disk format check; the cluster relies on the new binaries being able to read state written by the previous version.
- Re-forms the cluster topology over the standard inter-node connections.

### Note on the Recorded Cluster Version

The cluster's recorded version is updated only by the rolling-upgrade `commit` step. A full-cluster upgrade does not run that step, so after a full-cluster upgrade the recorded version reflects the version at which the cluster last completed a rolling upgrade — or the version at which the cluster was first initialised — not the version of the binaries currently running.
