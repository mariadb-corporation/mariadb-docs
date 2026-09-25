---
description: >-
  How to restore GridGain snapshots and continuous archives on a cluster with a
  different size and topology, from local snapshots, network backups, or PITR.
---

# Heterogeneous Recovery

Heterogeneous recovery refers to restoring snapshots and continuous archives on a cluster with a different size and topology (a number of nodes) from the original one where the snapshots were taken.

For the user, heterogeneous recovery is a regular recovery and can be done using the same tools and techniques that you use to create regular snapshots. However, depending on the type of snapshot—local or network—there are different restrictions that you should consider beforehand.

## Recovering from Local Snapshot

When you create a local snapshot, each node backs the data into its own a local storage. If data replication is not configured (the default behavior) and some of the nodes are brought down, the data from these nodes will be unavailable. In this case, restoring to a cluster containing fewer nodes will fail. To avoid this (and also for increased reliability), you can instruct the cluster to replicate data on multiple nodes by specifying the backups parameter in the cache configuration.

If you are recovering on a cluster that includes all nodes from the old cluster (and, possibly, new ones), the process should run without issues. Each partition from the snapshot should find its node in the new topology.

As an example, here's how to take a snapshot on cluster A and restore it on cluster B, with cluster B having a different topology and location. The sequence of steps resembles the process of network backup creation:

1. Create a local snapshot for each node in cluster A.
2. Move the snapshots to a remote location (alternatively, you can perform steps 1 and 2 together by saving the snapshot directly into the remote location).

   {% hint style="info" %}
   Consolidation of all node snapshots in a single location helps you restore the entire cluster in another environment.
   {% endhint %}

   For instance, you can use the [Snapshots Management Tool](snapshots-management-tool.md)'s `move` command or the Java API as follows:

   {% tabs %}
   {% tab title="Shell" %}
   ```shell
{gridgain}/bin/snapshot-utility.sh move -id=123456 -dest=/shared/folder
   ```
   {% endtab %}
   {% tab title="Java" %}
   ```java
// Get a reference to GridGain plugin.
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to the Snapshots.
GridSnapshot storage = gg.snapshot();

storage.createFullSnapshot(null, "Snapshot created").get();

// Get the first snapshot from the list.
SnapshotInfo info = storage.listSnapshots(null).get(0);

// Get the snapshot ID.
long snapshotId = info.snapshotId();

// Move the snapshot with given ID to a shared folder.
SnapshotUpdateOperationParams operationParameters = new SnapshotUpdateOperationParams.Builder()
        .withDeleteSources(true).withChainMode(SnapshotChainMode.DEFAULT).build();
SnapshotFuture<Void> fut = storage.copySnapshot(snapshotId, new File("/shared/folder/path"),
        operationParameters, "Snapshot Moved");

// Wait for the operation to finish.
fut.get();
   ```
   {% endtab %}
   {% tab title="C#/.NET" %}
   ```csharp
var cfg = new IgniteConfiguration
{
    // Enabling the Persistent Store.
    DataStorageConfiguration = new DataStorageConfiguration
    {
        DefaultDataRegionConfiguration = new DataRegionConfiguration
        {
            Name = "Default_Region",
            PersistenceEnabled = true
        }
    },

    // Enabling the snapshots.
    PluginConfigurations = new[]
    {
        new GridGainPluginConfiguration()
        {
            SnapshotConfiguration = new SnapshotConfiguration()
        }
    }
};

var ignite = Ignition.Start(cfg);

// Get a reference to grid snapshot API.
var storage = ignite.GetSnapshot();

var task = storage.CreateFullSnapshotAsync(null, "Snapshot created");

// Wait while the snapshot is being created.
task.Task.Wait();

// Get the first snapshot from the list.
var en = storage.GetSnapshots(null).GetEnumerator();
en.MoveNext();
var info = en.Current;

// Get the snapshot ID.
long snapshotId = info.SnapshotId;

// Move the snapshot with given ID to a shared folder.
var fut = storage.MoveSnapshotAsync(snapshotId, "/shared/folder/path", "Snapshot Moved");

// Wait for the operation to finish.
fut.Task.Wait();
   ```
   {% endtab %}
   {% tab title="C++" %}
   unsupported
   {% endtab %}
   {% endtabs %}
3. Make sure the remote location is available to all nodes of cluster B and has the same absolute path.
4. Restore from the remote location on cluster B. Cluster B will distribute the data across the new topology:

   {% tabs %}
   {% tab title="Shell" %}
   ```shell
{gridgain}/bin/snapshot-utility.sh restore -id=123456 -src=/shared/folder/path
   ```
   {% endtab %}
   {% tab title="Java" %}
   ```java
// Get a reference to GridGain plugin.
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to GridSnapshot.
GridSnapshot storage = gg.snapshot();

// Get the first snapshot from the list.
SnapshotInfo info = storage.listSnapshots(Collections.singleton(new File("/shared/folder/path"))).get(0);

// Get the snapshot ID.
long snapshotId = info.snapshotId();

// Replace content of all the caches with the content from the snapshot.
SnapshotFuture<Void> fut = storage.restoreSnapshot(snapshotId,
        Collections.singleton(new File("/shared/folder/path")), null, "Cluster Restored!");

// Wait until the operation finishes.
fut.get();
   ```
   {% endtab %}
   {% tab title="C#/.NET" %}
   ```csharp
var cfg = new IgniteConfiguration
{
    // Enabling the Persistent Store.
    DataStorageConfiguration = new DataStorageConfiguration
    {
        DefaultDataRegionConfiguration = new DataRegionConfiguration
        {
            Name = "Default_Region",
            PersistenceEnabled = true
        }
    },

    // Enabling the snapshots.
    PluginConfigurations = new[]
    {
        new GridGainPluginConfiguration()
        {
            SnapshotConfiguration = new SnapshotConfiguration()
        }
    }
};

var ignite = Ignition.Start(cfg);

// Get a reference to grid snapshot API.
var storage = ignite.GetSnapshot();

// Get the first snapshot from the list.
var en = storage.GetSnapshots(new[] { "/shared/folder/path" }).GetEnumerator();
en.MoveNext();
var info = en.Current;

// Get the snapshot ID.
long snapshotId = info.SnapshotId;

// Replace content of all the caches with the content from the snapshot.
var task = storage.RestoreSnapshotAsync(snapshotId, new[] { "/shared/folder/path" }, null, "Cluster Restored!");

// Wait for the operation to finish.
task.Task.Wait();
   ```
   {% endtab %}
   {% endtabs %}

## Recovering from Network Backup

A network backup contains a snapshot of all data and can be restored to any location. You just need to be sure that a new cluster has enough RAM and disk capacity to hold all the data from the snapshot.

See [Network Backups](network-backups.md) for details on how to create and recover from network snapshots.

## Recovering to Point in Time

When used together with [Point-in-Time Recovery (PITR)](point-in-time-recovery.md), heterogeneous recovery enables you to restore your cluster to some point in the past and on a different topology. Simply enable PITR and any network backup will contain all the data required for recovery to a required time (because it will contain both snapshots and WAL archives). To learn more about PITR, please visit [Point-in-Time Recovery](point-in-time-recovery.md).

{% hint style="info" %}
**Partition Reshuffle and SQL Rebuilding**

Note that when restoring a snapshot on a cluster with a different topology, the partition distribution on the new and original clusters will differ. Given that SQL indexes span all partitions on one node, restoring the snapshot on a different topology will require the GridGain cluster to rebuild SQL indexes. The index rebuilding procedure is triggered automatically after the snapshot is restored. That may result in reduced performance while the index is recreated because GridGain will be doing a full scan of all the data.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
