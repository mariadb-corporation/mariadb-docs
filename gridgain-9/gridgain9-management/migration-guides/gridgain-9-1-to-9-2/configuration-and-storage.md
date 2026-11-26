---
description: >-
  Configuration, storage, and metrics changes in the GridGain 9.1 to 9.2 upgrade: removed and renamed keys, the removed RocksDB engine, page replacement, and renamed metrics.
---

# Configuration, Storage, and Metrics Changes

GridGain 9.2 removes the legacy and deprecated configuration keys, the RocksDB storage engine, and the page replacement policies. It also renames the storage profile metrics and moves the Raft logs to a new storage.

## Removed and Renamed Configuration Keys

GridGain 9.1 accepted many keys under two names: an old name without a unit, such as `delayDuration`, and a new name with a unit, such as `delayDurationMillis`. GridGain 9.2 accepts only the new name. The tables below list each old and new name. 9.2 also removes the keys that 9.1 had deprecated. For how configuration works, see [Cluster and Node Configuration](../../cluster-configuration.md).

A 9.1.29 node converts old key names to the new ones and rewrites its node configuration file each time it starts. A file that a 9.1.29 node has already used may therefore contain only new names. Check the file before you rename anything.

A 9.2 node does not start if its node configuration file contains a key that 9.2 does not know. The node reports an error such as `Failed to parse HOCON: '<path>' configuration doesn't have the '<key>' sub-configuration`.

In the node configuration file, only the `ignite.storage.engines.rocksdb` section is still ignored. Rename or delete every other key from the tables below before you start a node on 9.2.

In the cluster configuration, 9.2 ignores the removed key `ignite.license.signature`. Use `ignite.license.content` instead.

{% hint style="warning" %}
The cluster configuration cannot be changed during a rolling upgrade. 9.1.29 converts old key names when it loads the cluster configuration, so `cluster config show` normally lists only the new names. Before you run `upgrade start`, check it and fix any key from the tables that is still there.
{% endhint %}

### Renamed Keys

The values, types, and defaults of the renamed keys do not change.

*Node* keys are in the node configuration file and are changed with `node config`. *Cluster* keys are in the cluster configuration and are changed with `cluster config`.

| Level | Old key | New key |
| --- | --- | --- |
| Cluster | `ignite.schemaSync.delayDuration` | `ignite.schemaSync.delayDurationMillis` |
| Cluster | `ignite.schemaSync.maxClockSkew` | `ignite.schemaSync.maxClockSkewMillis` |
| Node | `ignite.clientConnector.connectTimeout` | `ignite.clientConnector.connectTimeoutMillis` |
| Node | `ignite.clientConnector.idleTimeout` | `ignite.clientConnector.idleTimeoutMillis` |
| Node | `ignite.deployment.deploymentLocation` | `ignite.deployment.location` |
| Cluster | `ignite.eventlog.sinks.<name>.batchSendFrequency` (webhook sink) | `ignite.eventlog.sinks.<name>.batchSendFrequencyMillis` |
| Cluster | `ignite.eventlog.sinks.<name>.retryPolicy.initBackoff` | `ignite.eventlog.sinks.<name>.retryPolicy.initBackoffMillis` |
| Cluster | `ignite.eventlog.sinks.<name>.retryPolicy.maxBackoff` | `ignite.eventlog.sinks.<name>.retryPolicy.maxBackoffMillis` |
| Node | `ignite.failureHandler.oomBufferSizeBites` | `ignite.failureHandler.oomBufferSizeBytes` |
| Cluster | `ignite.metrics.exporters.<name>.period` (`otlp` and `logPush` exporters) | `ignite.metrics.exporters.<name>.periodMillis` |
| Node | `ignite.network.membership.membershipSyncInterval` | `ignite.network.membership.membershipSyncIntervalMillis` |
| Node | `ignite.network.membership.failurePingInterval` | `ignite.network.membership.failurePingIntervalMillis` |
| Node | `ignite.network.membership.scaleCube.gossipInterval` | `ignite.network.membership.scaleCube.gossipIntervalMillis` |
| Node | `ignite.network.membership.scaleCube.metadataTimeout` | `ignite.network.membership.scaleCube.metadataTimeoutMillis` |
| Node | `ignite.network.nodeFinder.resultWaitTime` (multicast finder) | `ignite.network.nodeFinder.resultWaitTimeMillis` |
| Node | `ignite.network.shutdownQuietPeriod` | `ignite.network.shutdownQuietPeriodMillis` |
| Node | `ignite.network.shutdownTimeout` | `ignite.network.shutdownTimeoutMillis` |
| Node | `ignite.raft.installSnapshotTimeout` | `ignite.raft.installSnapshotTimeoutMillis` |
| Node | `ignite.raft.retryTimeout` | `ignite.raft.retryTimeoutMillis` |
| Node | `ignite.raft.retryDelay` | `ignite.raft.retryDelayMillis` |
| Node | `ignite.raft.responseTimeout` | `ignite.raft.responseTimeoutMillis` |
| Cluster | `ignite.replication.idleSafeTimePropagationDuration` | `ignite.replication.idleSafeTimePropagationDurationMillis` |
| Cluster | `ignite.replication.rpcTimeout` | `ignite.replication.rpcTimeoutMillis` |
| Cluster | `ignite.replication.leaseAgreementAcceptanceTimeLimit` | `ignite.replication.leaseAgreementAcceptanceTimeLimitMillis` |
| Cluster | `ignite.replication.leaseExpirationInterval` | `ignite.replication.leaseExpirationIntervalMillis` |
| Cluster | `ignite.replication.replicaOperationRetryInterval` | `ignite.replication.replicaOperationRetryIntervalMillis` |
| Cluster | `ignite.gc.lowWatermark.dataAvailabilityTime` | `ignite.gc.lowWatermark.dataAvailabilityTimeMillis` |
| Cluster | `ignite.gc.lowWatermark.updateInterval` | `ignite.gc.lowWatermark.updateIntervalMillis` |
| Cluster | `ignite.sql.planner.maxPlanningTime` | `ignite.sql.planner.maxPlanningTimeMillis` |
| Node | `ignite.storage.engines.aipersist.checkpoint.interval` | `ignite.storage.engines.aipersist.checkpoint.intervalMillis` |
| Node | `ignite.storage.engines.aipersist.checkpoint.intervalDeviation` | `ignite.storage.engines.aipersist.checkpoint.intervalDeviationPercent` |
| Node | `ignite.storage.engines.aipersist.checkpoint.readLockTimeout` | `ignite.storage.engines.aipersist.checkpoint.readLockTimeoutMillis` |
| Node | `ignite.storage.engines.aipersist.checkpoint.logReadLockThresholdTimeout` | `ignite.storage.engines.aipersist.checkpoint.logReadLockThresholdTimeoutMillis` |
| Node | `ignite.storage.engines.aipersist.pageSize` | `ignite.storage.engines.aipersist.pageSizeBytes` |
| Node | `ignite.storage.engines.aimem.pageSize` | `ignite.storage.engines.aimem.pageSizeBytes` |
| Node | `ignite.storage.profiles.<name>.size` (`aipersist` profile) | `ignite.storage.profiles.<name>.sizeBytes` |
| Node | `ignite.storage.profiles.<name>.initSize` (`aimem` profile) | `ignite.storage.profiles.<name>.initSizeBytes` |
| Node | `ignite.storage.profiles.<name>.maxSize` (`aimem` profile) | `ignite.storage.profiles.<name>.maxSizeBytes` |
| Cluster | `ignite.transaction.readOnlyTimeout` | `ignite.transaction.readOnlyTimeoutMillis` |
| Cluster | `ignite.transaction.readWriteTimeout` | `ignite.transaction.readWriteTimeoutMillis` |
| Node | `ignite.system.criticalWorkers.livenessCheckInterval` | `ignite.system.criticalWorkers.livenessCheckIntervalMillis` |
| Node | `ignite.system.criticalWorkers.maxAllowedLag` | `ignite.system.criticalWorkers.maxAllowedLagMillis` |
| Node | `ignite.system.criticalWorkers.nettyThreadsHeartbeatInterval` | `ignite.system.criticalWorkers.nettyThreadsHeartbeatIntervalMillis` |

### Removed Keys With a Replacement

9.1 copied the value of these keys to the new key when it loaded the configuration. 9.2 does not know the old key.

| Level | Old key | New key |
| --- | --- | --- |
| Node | `ignite.nodeAttributes.nodeAttributes.<name>.attribute` | `ignite.userAttributes.<name>.attribute` |
| Cluster | `ignite.metaStorage.idleSyncTimeInterval` | `ignite.system.idleSafeTimeSyncIntervalMillis` |
| Node | `ignite.criticalWorkers.*` | `ignite.system.criticalWorkers.*` |
| Node | `ignite.snapshot.snapshotFlushBufferSize` | `ignite.snapshot.snapshotChunkSizeBytes` |
| Node | `ignite.raft.stripes` | `ignite.raft.disruptor.stripes` |
| Node | `ignite.raft.logStripesCount` | `ignite.raft.disruptor.logManagerStripes` |
| Cluster | `ignite.storageUpdate.batchByteLength` | `ignite.replication.batchSizeBytes` |

### Transaction Keys

These transaction keys are removed. Three of them are now system properties, which you set in the `ignite.system.properties` section of the cluster configuration. An unset property uses its default.

| Level | Old key | New setting | Default of the new setting |
| --- | --- | --- | --- |
| Cluster | `ignite.transaction.abandonedCheckTs` | System property `txnAbandonedCheckTs` | `5000` |
| Cluster | `ignite.transaction.attemptsObtainLock` | System property `txnLockRetryCount` | `3` |
| Cluster | `ignite.transaction.txnResourceTtl` | System property `txnResourceTtl` | `60000` |
| Cluster | `ignite.transaction.timeout` | `ignite.transaction.readWriteTimeoutMillis` | `30000` |

Two of these settings need extra care:

- `txnLockRetryCount` is read when the node starts, so restart the node after you change it.
- The old `ignite.transaction.timeout` defaulted to `10000`, not `30000`. If you set the old key, set `readWriteTimeoutMillis` to the same value.

For the properties, see the [cluster configuration](../../../reference/configuration/cluster-configuration-parameters.md) reference.

### Removed Keys Without a Replacement

Delete these keys.

| Level | Key |
| --- | --- |
| Node | `ignite.compute.threadPoolStopTimeoutMillis` |
| Node | `ignite.storage.engines.columnar.mergeTreeConfiguration` and its `mergeTreeFanout` and `mergeTreeFirstLevelSize` |
| Cluster | `ignite.transaction.implicitTransactionTimeout` |
| Cluster | `ignite.transaction.rpcTimeout` |
| Cluster | `ignite.transaction.deadlockPreventionPolicy` and its `txIdComparator` and `waitTimeout` |
| Node | `ignite.network.fileTransfer`, `ignite.network.ackConfigurationSchema`, and `ignite.storage.engines.aipersist.checkpoint.useAsyncFileIoFactory` |

The last row lists keys of very old releases. 9.1 ignored them, but 9.2 rejects them.

For the current keys, see the [node configuration](../../../reference/configuration/node-configuration-parameters.md) and [cluster configuration](../../../reference/configuration/cluster-configuration-parameters.md) references.

### Helm Chart Versions

If you deploy with the `gridgain/gridgain9` Helm chart, use chart version 1.1.12 or later. The default configuration of versions 1.1.10 and 1.1.11 contains `ignite.raft.logStripesCount` and `ignite.raft.stripes`, so the pods restart in a loop with `Failed to parse HOCON: 'ignite.raft' configuration doesn't have the 'logStripesCount' sub-configuration`. The chart's `appVersion` is still a 9.1 release, so set `image.tag` to the 9.2 version. See [Installing GridGain 9 on Kubernetes using Helm Chart](../../installation/installing-with-helm.md).

## RocksDB Storage Engine Removed

This section applies if a storage profile uses the `rocksdb` engine.

The RocksDB partition storage engine and the `engine = rocksdb` profile type are removed. This change affects only partition storage, not the RocksDB-based Raft log. There is no automatic migration for tables on a RocksDB profile. For the remaining engines, see [Storage Engines and Profiles](../../../architecture/storage/engines/README.md) and [Storage Profiles](../../../architecture/storage/storage-profiles.md).

A node ignores an `ignite.storage.engines.rocksdb` section, but it does not start if a storage profile uses `engine = rocksdb`. The error is `Failed to parse HOCON: Polymorphic configuration type is not correct: rocksdb`.

Before you upgrade, move zones and tables from a RocksDB profile to another engine, and remove the profile. Do all of this while the cluster still runs 9.1.29:

1. Create a zone with an `aipersist` or `aimem` storage profile. Use `aipersist` if the data must survive a restart, because `aimem` keeps data in memory only. See [Distribution Zones](../../../reference/sql/distribution-zones.md) and [Persistent Storage](../../../architecture/storage/engines/native-persistent-storage.md).
2. Create the new tables in that zone, and copy the data, for example with `INSERT INTO ... SELECT`.
3. Drop the old tables and zones.
4. Wait for the dropped tables to be cleaned up. A dropped table keeps its storage until the garbage collector low watermark passes the time of the drop. With the defaults (`ignite.gc.lowWatermark.dataAvailabilityTimeMillis=600000` and `updateIntervalMillis=300000`), this takes at least 15 minutes. To shorten the wait, lower both values, and set the defaults back afterward:

   ```bash
   cluster config update 'ignite.gc.lowWatermark{dataAvailabilityTimeMillis=30000,updateIntervalMillis=15000}'
   ```

5. Remove the RocksDB profile from the node configuration files, after step 4. A node that starts without the profile stops with `Table uses an unknown storage profile or engine` if a table on it still exists, or if a dropped table is not cleaned up yet (see step 4). How you remove the profile depends on how you prepare the files for 9.2:

   - *Reuse the 9.1.29 files.* On each node, stop the node, delete the profile from `ignite.storage.profiles`, and start the node on 9.1.29. Stop the node before you edit the file, because a running node rewrites the file from memory on the next configuration update. If the node stops with the error above, put the profile back, start the node, wait a few more minutes, and repeat.
   - *Create new files for 9.2.* Leave the 9.1.29 files unchanged, and write the new files without the profile. If you start from a copy of a 9.1.29 file, delete the profile from the copy.

6. Check that the profile is gone:

   - If you reuse your 9.1.29 files, run the following command against every node after the restart. The output lists only the profiles of the remaining engines, for example `engine=aipersist`. If the RocksDB profile is listed, contact MariaDB [support](https://mariadb.com/support/).

     ```bash
     node config show ignite.storage.profiles
     ```

   - If you create new files, search them for `rocksdb`. The new files must not contain the profile.

   In both cases, check that no zone uses the profile. The query must return no rows:

   ```sql
   SELECT zone_name, storage_profile FROM system.zone_storage_profiles WHERE storage_profile = '<profile_name>';
   ```

7. Upgrade as described in the [Upgrade Procedure](upgrade-procedure.md). A 9.2 node does not start if its node configuration file contains a RocksDB profile.

Dropping the tables does not free the disk space of the old RocksDB storage. The old `rocksdb-*` directory under `work/partitions/db` stays on each node after the upgrade.

## Page Replacement Policies

This section applies if a storage profile sets `replacementMode`.

The `RANDOM_LRU` and `SEGMENTED_LRU` page replacement policies are removed. The persistent page memory always uses the `CLOCK` policy. The deprecated `replacementMode` property of an `aipersist` profile still accepts the old values, but 9.2 ignores it, so remove it from your profiles. See [Persistent Storage](../../../architecture/storage/engines/native-persistent-storage.md).

## Metric Changes

- The metric source `storage.aipersist.<profile>` is now `storage.aipersist.profiles.<profile>`. The metrics in the source keep their names.
- The metric `PageAcquireTime` is removed.

The engine-level sources `storage.aipersist`, `storage.aipersist.checkpoint`, and `storage.aipersist.io` keep their names. Update every dashboard, alert, exporter filter, and `metric source enable` or `disable` command that uses the old source name, and remove `PageAcquireTime`.

For the list of metrics, see [Metrics List](../../../reference/monitoring/metrics-list.md#storage.aipersist.profiles.-profile). For how to enable metric sources, see [Configuring Metrics](../../monitoring/configuring-metrics.md).

## Raft Log Storage Changes

GridGain 9.2 stores the Raft logs in the segment-based log storage (SegStore) by default, replacing the RocksDB-based log storage that 9.1 used and that is deprecated in 9.2.

- *Migration.* The logs migrate automatically. A node starts writing to the new storage once the cluster version is 9.2, at the commit of a rolling upgrade or when all cluster management nodes have joined on 9.2 in a full-cluster upgrade.
- *Disk space.* The new logs are stored in a `segstore` directory inside the Raft log directories, so they follow the paths in `ignite.system.partitionsLogPath`, `ignite.system.metastoragePath`, and `ignite.system.cmgPath`. The [data directories](upgrade-procedure.md#back-up-the-data) list shows the default locations. Make sure that the disks of these directories have free space for both the old and the new logs.
- *Metrics.* 9.2 adds a `raft.segstore.<name>` metric source for each log, for example `raft.segstore.meta-storage-log`. See [Metrics List](../../../reference/monitoring/metrics-list.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
