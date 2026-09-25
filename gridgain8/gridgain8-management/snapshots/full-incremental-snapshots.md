---
description: >-
  How to create, restore, and secure full and incremental GridGain snapshots
  with the Java API and the snapshot utility, including the creation flow.
---

# Full and Incremental Snapshots

GridGain provides the ability to create snapshots of data stored cluster-wide, that can later be used for cluster recovery purposes. Snapshots taken from one cluster can also be applied on the second cluster. Snapshotting capability is tightly coupled with Ignite Native Persistence and can be used only when the latter is active.

Essentially, GridGain snapshots are similar to RDBMS backups. The main reason why GridGain snapshots are not called as backups is to avoid the confusion with GridGain backup copies of data stored in the cluster.

It's feasible to create full offline and online snapshots as well as incremental ones. Having snapshots at hand, they can be used to recover the cluster to a state recorded in a snapshot. Furthermore, the cluster that is planned to be recovered from a snapshot can be of different topology version (different number of data nodes) than the original one. For instance, you can create snapshots of a production cluster and use the snapshots in a testing environment with a different number of cluster nodes.

## Enabling Snapshots

Snapshot capabilities are based on and implemented with the usage of Ignite Native Persistence and overall Durable Memory architecture.

To enable the snapshots component, [Native Persistence](../../architecture/storage/native-persistence.md) has to be activated first, as shown below:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

   <!-- Enabling the Ignite Native Persistence. -->
  <property name="dataStorageConfiguration">
    <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
        <property name="defaultDataRegionConfiguration">
        <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
          <property name="persistenceEnabled" value="true"/>
        </bean>
      </property>
    </bean>
  </property>

  <!-- Enabling the snapshots. -->
  <property name="pluginConfigurations">
    <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
      <property name="snapshotConfiguration">
        <bean class="org.gridgain.grid.configuration.SnapshotConfiguration"/>
      </property>
    </bean>
  </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

//Enabling the Persistent Store.
DataStorageConfiguration dataStorageCfg = new DataStorageConfiguration();
dataStorageCfg.getDefaultDataRegionConfiguration().setPersistenceEnabled(true);
cfg.setDataStorageConfiguration(dataStorageCfg);

GridGainConfiguration ggCfg = new GridGainConfiguration();

SnapshotConfiguration snapshotCfg = new SnapshotConfiguration();

//Enabling the snapshots.
ggCfg.setSnapshotConfiguration(snapshotCfg);

cfg.setPluginConfigurations(ggCfg);
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
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

By default, snapshots are stored on a local file system of cluster nodes under `IGNITE_HOME\work\snapshot` folder. To change the snapshots location, use the `SnapshotConfiguration.setSnapshotsPath(...)` method as shown below:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

   <!-- Enabling the Ignite Native Persistence. -->
  <property name="dataStorageConfiguration">
    <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
        <property name="defaultDataRegionConfiguration">
        <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
          <property name="persistenceEnabled" value="true"/>
        </bean>
      </property>
    </bean>
  </property>

  <!-- Enabling the snapshots. -->
  <property name="pluginConfigurations">
    <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
      <property name="snapshotConfiguration">
        <bean class="org.gridgain.grid.configuration.SnapshotConfiguration">
          <property name="snapshotsPath" value="/etc/snapshots/"/>
        </bean>
      </property>
    </bean>
  </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

//Enabling the Persistent Store.
DataStorageConfiguration dataStorageCfg = new DataStorageConfiguration();
dataStorageCfg.getDefaultDataRegionConfiguration().setPersistenceEnabled(true);
cfg.setDataStorageConfiguration(dataStorageCfg);

GridGainConfiguration ggCfg = new GridGainConfiguration();

SnapshotConfiguration snapshotCfg = new SnapshotConfiguration();

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
            {
                // Changing default path.
                SnapshotsPath = "/local/snasphot/store/path"
            }
        }
    }
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Snapshots APIs and Tools

Once you enabled snapshotting, use one of the following approaches for snapshot creation, management, and recovery:

- Java API - Snapshots related API is provided through the `GridSnapshot` interface. To see how to use this API in practice, refer to `org.gridgain.examples.snapshots.SnapshotsExample`, included with the GridGain Ultimate Edition examples.
- [Snapshots Management Tool](snapshots-management-tool.md)
- [Control Center Snapshots Management]({tools}/control-center/gg8/snapshots/snapshots)

{% hint style="info" %}
Snapshots are very much tied to your cluster topography and shutting down any node could cause issues. If you plan on removing or shutting down nodes from you cluster, first [move your snapshots to the network](network-backups.md).
{% endhint %}

## Full Snapshots

A full snapshot holds a full copy of the cluster data at a given point of time. By default, data of all the caches will be stored in a snapshot. However, GridGain provides the option to make a full snapshot including the content of specific caches only.

{% hint style="info" %}
When [Point-In-Time-Recovery](point-in-time-recovery.md) is enabled, you cannot create snapshots with a subset of caches.
{% endhint %}

### Creating Full Snapshots

To create a full snapshot programmatically, use the `GridDatabase.createFullSnapshot(...)` method:

**Full Snapshot**

{% tabs %}
{% tab title="Java" %}
```java
// Get a reference to GridGain plugin.
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to the Snapshots.
GridSnapshot storage = gg.snapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
SnapshotFuture snapshotFut = storage.createFullSnapshot(null,
    "Snapshot has been created!");

// Wait while the snapshot is being created.
snapshotFut.get();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start(cfg);

// Get a reference to grid snapshot API.
var snap = ignite.GetSnapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
var task = snap.CreateFullSnapshotAsync(null, "Snapshot has been created!");

// Wait while the snapshot is being created.
task.Task.Wait();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

**Full Snapshot for Specific Caches**

{% tabs %}
{% tab title="Java" %}
```java
// Get a reference to GridGain plugin.

IgniteCache<Integer, String> orgCache = ignite.getOrCreateCache("organization");
orgCache.put(1, "first_org");

GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to the Snapshots.
GridSnapshot storage = gg.snapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
SnapshotFuture snapshotFut = storage.createFullSnapshot(Collections.singleton("organization"),
    "Snapshot has been created!");

// Wait while the snapshot is being created.
snapshotFut.get();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start(cfg);

var orgCache = ignite.GetOrCreateCache<int, string>("organization");
orgCache.Put(1, "first_org");

// Get a reference to grid snapshot API.
var snap = ignite.GetSnapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
var task = snap.CreateFullSnapshotAsync(new[] {orgCache.Name}, "Snapshot has been created!");

// Wait while the snapshot is being created.
task.Task.Wait();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Once this method is called on one of the cluster nodes, GridGain will take the cluster-wide snapshot asking every individual node to provide its part of the overall snapshot's data set.

Alternatively, the [Snapshots Management Tool](snapshots-management-tool.md) can be used for the same purpose. At the implementation layer, these tools use the same Java API shown above.

For instance, to create a full snapshot with Snapshots Management Tool, the following command needs to be sent to the cluster.

**Full Snapshot**

{% tabs %}
{% tab title="shell" %}
```shell
{gridgain}/bin/snapshot-utility.sh snapshot -type=full
```
{% endtab %}
{% endtabs %}

**Full Snapshot for Specific Caches**

{% code title="Shell" %}
```shell
{gridgain}/bin/snapshot-utility.sh snapshot -type=full -caches=organization
```
{% endcode %}

### Preparing for Restoration from Full Snapshot

To make sure your snapshot is restored correctly, follow these guidelines:

- Make sure that all the nodes from the baseline topology are online before restore. Otherwise, the stopped node will not be able to join the cluster until the PDS files for the restored caches are manually deleted for that node.

  {% hint style="info" %}
  Restoring the cache with lost partitions from the snapshot is not possible. A snapshot restoration containing such caches will be cancelled. In this case you must return the offline node or remove it from the baseline topology.
  {% endhint %}

- Stop traffic to the cluster during restoration to avoid possible inconsistencies and failed operations. It is also possible that the data you get from the cache when restoring is incomplete.

### Restoring From Full Snapshot

To restore the content of all or specific caches from a previously created snapshot, the snapshot has to be available to the `GridSnapshot` interface.

The default implementation of this SPI assumes that the content of the snapshot will be spread out across the cluster and every node will hold a part of the snapshot that includes content for partitions for which the node is primary. Removing nodes from the cluster can break snapshots. If you plan on removing nodes from your cluster, first create a [network backup](network-backups.md).

If the snapshot is going to be restored in a cluster with the same topology version (same number of nodes and same partitions distribution) from the time the snapshot was taken, then you can use the existing APIs and tools. Restoring to a larger cluster (if you have added nodes to the existing cluster) is also supported.

If the number of nodes or the partitions distribution varies in the cluster where the snapshot is to be applied, run the [CHECK](snapshots-management-tool.md#check) command before restoring.

If there is a problem, the CHECK command shows the issue. For example:

```shell
$ snapshot-utility.sh check -id=1565692737236
Command [CHECK -id=1565692737236 -caches=cache1,corruptedCache] started at [2019-08-13 13:38:58]...
Snapshot ID 1565692737236 is broken. Found 1 issues:
 Cache: corruptedCache. Found 1 issues:
   Partition ID: 1. Issue: Partition was not found!
Command [CHECK] failed with error: 6510 - snapshot is broken.
GridGain Snapshots utility [ver. 2.7.127-SNAPSHOT#20190813-sha1:DEV]
2019 Copyright(C) GridGain Systems
```

Example of a valid snapshot:

```shell
$ snapshot-utility.sh check -id=1565692737236
Command [CHECK -id=1565692737236] started at [2019-08-13 13:38:58]...
Snapshot ID 1565692737236 is valid
Command [CHECK] successfully finished in 0 seconds.
GridGain Snapshots utility [ver. 2.7.127-SNAPSHOT#20190813-sha1:DEV]
2019 Copyright(C) GridGain Systems
```

{% hint style="warning" %}
**Recovering on Different Topologies Without Manual Snapshot Files Reshuffling**

To avoid having the snapshot's files manually reshuffled while recovering on a different cluster topology,  set the `SnapshotConfiguration.setSnapshotsPath(...)` parameter to a centralized file storage, such as NAS or a network file system.
{% endhint %}

As soon as the content of the snapshot is spread out properly across the cluster, the cluster can be restored from the snapshot programmatically via `GridDatabase.restoreSnapshot(...)`.

**Restoring All Caches**

{% tabs %}
{% tab title="shell" %}
```shell
# Getting a list of all the available snapshots.
# The output will include snapshots' IDs.
{gridgain}/bin/snapshot-utility.sh list

# Restoring the cluster to a specific snapshot passing its ID.
{gridgain}/bin/snapshot-utility.sh restore -id=1483663276482
```
{% endtab %}
{% endtabs %}

**Restoring Specific Caches**

{% code title="Shell" %}
```shell
# Getting a list of all the available snapshots.
# The output will include snapshots' IDs.
{gridgain}/bin/snapshot-utility.sh list

# Restoring the cluster to a specific snapshot passing its ID.
{gridgain}/bin/snapshot-utility.sh restore -id=1483663276482 -caches=organization
```
{% endcode %}

## Incremental Snapshots

In incremental snapshots, successive copies of the data contain only that portion that has changed since the preceding full or incremental snapshot copy. When a full recovery is needed, the restoration process needs the last full snapshot, plus all the incremental snapshots up to the point of restoration.

### Creating Incremental Snapshots

To create an incremental snapshot programmatically, use `GridDatabase.createSnapshot(...)`:

**Incremental Snapshot**

{% tabs %}
{% tab title="Java" %}
```java
// Get a reference to GridGain plugin.
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to the Snapshots.
GridSnapshot storage = gg.snapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
SnapshotFuture snapshotFut = storage.createSnapshot(null,
    "Snapshot has been created!");

// Wait while the snapshot is being created.
snapshotFut.get();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start(cfg);

// Get a reference to grid snapshot API.
var snap = ignite.GetSnapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
var task = snap.CreateSnapshotAsync(null, "Snapshot has been created!");

// Wait while the snapshot is being created.
task.Task.Wait();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

**Incremental Snapshot for Specific Caches**

{% tabs %}
{% tab title="Java" %}
```java
// Get a reference to GridGain plugin.

IgniteCache<Integer, String> orgCache = ignite.getOrCreateCache("organization");
orgCache.put(1, "first_org");

GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

// Get a reference to the Snapshots.
GridSnapshot storage = gg.snapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
SnapshotFuture snapshotFut = storage.createSnapshot(Collections.singleton("organization"),
    "Snapshot has been created!");

// Wait while the snapshot is being created.
snapshotFut.get();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start(cfg);

var orgCache = ignite.GetOrCreateCache<int, string>("organization");
orgCache.Put(1, "first_org");

// Get a reference to grid snapshot API.
var snap = ignite.GetSnapshot();

// Create the snapshot. Data of all the caches will be added to the snapshot.
var task = snap.CreateSnapshotAsync(new[] {orgCache.Name}, "Snapshot has been created!");

// Wait while the snapshot is being created.
task.Task.Wait();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Alternatively, Snapshots Management Tool can be used for the same purpose.

For instance, to create an incremental snapshot via the Snapshot Management Tool, send the following command to the cluster:

**Incremental Snapshot**

{% tabs %}
{% tab title="shell" %}
```shell
{gridgain}/bin/snapshot-utility.sh snapshot
```
{% endtab %}
{% endtabs %}

**Incremental Snapshot for Specific Caches**

{% code title="Shell" %}
```shell
{gridgain}/bin/snapshot-utility.sh snapshot -caches=organization
```
{% endcode %}

### Restoring From Incremental Snapshot

The same API methods and commands described for full snapshots above are used to restore a cluster from an incremental snapshot. The only extra requirement is that you need to provide both the last full snapshot plus all the incremental snapshots up to the point of restoration to the snapshotting API or tool.

## Snapshots Creation Flow

### Full Snapshot Creation

_Snapshot_ is a distributed operation that is performed with no need to stop your cluster. The transactions can continue while the snapshot is running.

All nodes communicate at the start of the snapshot and agree which transactions will be included in that snapshot. The algorithm ensures that the snapshot is transactionally consistent; i.e., it will not include unfinished or rolled back transactions.

For full snapshots, all data is being copied to a snapshot. When a full snapshot is restored, all of its data is simply copied to the cluster.

{% hint style="info" %}
Snapshot puts an additional load on the system in terms of the disk i/o, as well as CPU (because the snapshot files are being written to the disk).
{% endhint %}

### Incremental Snapshot Creation

For incremental snapshots, the system maintains information about which data pages were modified after the last snapshot. When an incremental snapshot is being created, only these pages are being copied into the snapshot. Because each incremental snapshot is based on another snapshot, a snapshot chain is formed - a series of one full snapshot and a number of subsequent incremental snapshots. 

When an incremental snapshot is restored, all of the snapshots in its chain are restored first, one by one, and then the incremental changes from the incremental snapshot are copied to the cluster.

## Snapshot Restoration Flow

This section provides low-level details regarding how snapshot restoration is handled cluster-wide.

Regardless of whether a full or incremental snapshot is restored, the grid first determines the partition distribution across all nodes. After each node determines the set of local partitions, each node fetches the history of incremental snapshots starting with the requested snapshot back to the last full snapshot in the cluster.

Then, given the number of pages in the snapshot for each partition, incremental and full backups are merged to the target working directory to assemble a consistent snapshot state. Pages from the last incremental snapshot are copied first to avoid unnecessary copies of the pages that changed multiple times.

Once each node has completed the assembly process, the cache being restored is created cluster-wide.

## Changing Parameters During Restoration

During snapshot restoration, you can change cache configuration. This may be useful if, for example, you want to change the parameter that caused an issue while restoring the snapshot.

To do this, you pass a `conversionClosure` to the `RestoreSnapshotParams` class. For example, if you have clashing cache names you first create a closure for changing cache name:

```java
static class AlterCacheNamesClosure implements IgniteBiClosure<String, CacheConfiguration, CacheConfiguration> {

  private final Map<String, String> mapping = new HashMap<>();

  public AlterCacheNamesClosure addMapping(String oldCacheName, String newCacheName) {
    if (oldCacheName != null && newCacheName != null && !oldCacheName.equals(newCacheName))
      mapping.put(oldCacheName, newCacheName);

      return this;
    }

  @Override
  public CacheConfiguration apply(String s, CacheConfiguration cacheConfiguration) {
    String alteredName = mapping.get(s);
    if (alteredName != null) {
      return new CacheConfiguration(cacheConfiguration).setName(alteredName);
    }

    return cacheConfiguration;
  }
}
```

Then, you pass it to `RestoreSnapshotParams` instance like this:

```java
RestoreSnapshotParams restoreOptions = prepareRestoreParams(snapshotId)
  .forceRestore(true)
  .conversionClosure(new AlterCacheNamesClosure().addMapping(CACHE_NAME, ALTERED_CACHE_NAME));
```

There are the following limitations:

- To avoid issues with restoration, cache name cannot be changed when restoring to the same cluster. You need to create a snapshot on one cluster, move it to a shared location and then to restore it to another cluster that does not contain a cache with clashing name.

- Changing cache name is only supported for caches that are not in a cache group. If you try to rename a cache in a cache group, a new empty cache will be created, but no data is transferred.

This approach can be used to change other snapshot parameters, depending on the new [configuration](https://www.gridgain.com/sdk/latest/javadoc/index.html) passed to the `conversionClosure`. For example, you can change the number of backups instead of changing cache name:

```java
return new CacheConfiguration(cacheConfiguration).setBackups(3);
```

## Snapshot Security

Snapshot Security helps ensure the integrity of each snapshot file and the overall snapshot process.

When enabled, Snapshot Security provides an additional layer of security, protecting data from modification and corruption and from snapshot file version mismatch. It helps eliminate the possibility of accidentally using files from multiple versions of snapshots. For example, suppose you have 2 snapshots: A and B. It may be possible to accidentally use file1.dat and file 2.dat from Snapshot A, and file3.dat from snapshot B by mistake.

Snapshot Security creates a file registry that contains a list of all of the files included in the snapshot, and their cryptographic hashes. Before being restored, snapshots are compared against this registry to ensure they contain the proper files.

Snapshot Security protects files from substitution; however, it does not protect against malicious actions by hackers/etc.

Enable Snapshot Security via the `GG_SNAPSHOT_SECURITY_LEVEL` system property.

| Parameter | Description |
|---|---|
| DISABLED | Snapshot file registry is not created and never validated if present (default). |
| IGNORE_EXISTING | Snapshot file registry is included in new snapshots. Existing file registries in snapshots are not verified. |
| IGNORE_MISSING | Snapshot file registry is included in new snapshots. Existing file registries in snapshots DO GET verified. Missing file registries in snapshots are tolerated. |
| REQUIRE | Snapshot file registry is included in new snapshots. Presence and validity of file registries in all snapshots are required. |

## Example

Refer to `org.gridgain.examples.snapshots.SnapshotsExample` delivered as part of the GridGain Ultimate Edition to see how to work with snapshots.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
