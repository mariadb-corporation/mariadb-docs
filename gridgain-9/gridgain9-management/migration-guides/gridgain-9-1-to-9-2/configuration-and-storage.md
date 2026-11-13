---
description: >-
  Configuration, storage, and metrics changes when upgrading from GridGain 9.1 to 9.2: removed and renamed configuration keys, the removed RocksDB engine, page replacement, and renamed metrics.
---

# Configuration, Storage, and Metrics Changes

GridGain 9.2 removes the legacy configuration key names and the deprecated keys of 9.1. It removes the RocksDB storage engine and the page replacement policies. It also renames the storage profile metrics.

## Removed and Renamed Configuration Keys

GridGain 9.1 accepted many keys under two names: the unit-less name, for example `delayDuration`, and the name with a unit, for example `delayDurationMillis`. GridGain 9.2 accepts only the name with a unit. It also removes the keys that 9.1 had deprecated.

A 9.2 node does not start if its node configuration file contains a key that 9.2 does not know. The node reports an error such as `Failed to parse HOCON: '<path>' configuration doesn't have the '<key>' sub-configuration`. A key in the stored cluster configuration that 9.2 does not know also prevents the node from starting.

Only two removed keys are still ignored: `ignite.license.signature` and the `ignite.storage.engines.rocksdb` section. Rename or delete every other key from the tables below before you start a node on 9.2.

{% hint style="warning" %}
The cluster configuration cannot be changed while a rolling upgrade is in progress. GridGain 9.1.29 converts the old key names when it loads the cluster configuration, so `cluster config show` normally lists only the new names. Check it before you run `upgrade start`, and fix any key from the tables that is still there.
{% endhint %}

The values, types, and defaults of the renamed keys do not change.

### Renamed Keys

Keys at the *node* level are in the node configuration file, and `node config` commands change them. Keys at the *cluster* level are in the cluster configuration, and `cluster config` commands change them.

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

GridGain 9.1 copied the value of these keys to the new key when it loaded the configuration. GridGain 9.2 does not know the old key.

| Level | Old key | New key |
| --- | --- | --- |
| Node | `ignite.nodeAttributes.nodeAttributes.<name>.attribute` | `ignite.userAttributes.<name>.attribute` |
| Cluster | `ignite.metaStorage.idleSyncTimeInterval` | `ignite.system.idleSafeTimeSyncIntervalMillis` |
| Node | `ignite.criticalWorkers.*` | `ignite.system.criticalWorkers.*` |
| Node | `ignite.snapshot.snapshotFlushBufferSize` | `ignite.snapshot.snapshotChunkSizeBytes` |
| Node | `ignite.raft.stripes` | `ignite.raft.disruptor.stripes` |
| Node | `ignite.raft.logStripesCount` | `ignite.raft.disruptor.logManagerStripes` |
| Cluster | `ignite.storageUpdate.batchByteLength` | `ignite.replication.batchSizeBytes` |

### Removed Keys Without a Replacement

Delete these keys.

| Level | Key |
| --- | --- |
| Cluster | `ignite.license.signature`. Still ignored. Use `ignite.license.content`. |
| Node | `ignite.compute.threadPoolStopTimeoutMillis` |
| Node | `ignite.storage.engines.columnar.mergeTreeConfiguration` and its `mergeTreeFanout` and `mergeTreeFirstLevelSize` |
| Cluster | `ignite.transaction.abandonedCheckTs` |
| Cluster | `ignite.transaction.timeout` |
| Cluster | `ignite.transaction.implicitTransactionTimeout` |
| Cluster | `ignite.transaction.attemptsObtainLock` |
| Cluster | `ignite.transaction.txnResourceTtl` |
| Cluster | `ignite.transaction.rpcTimeout` |
| Cluster | `ignite.transaction.deadlockPreventionPolicy` and its `txIdComparator` and `waitTimeout` |
| Node | `ignite.network.fileTransfer`, `ignite.network.ackConfigurationSchema`, and `ignite.storage.engines.aipersist.checkpoint.useAsyncFileIoFactory`. Keys of very old releases that 9.1 still ignored. |

For the current keys, see the [node configuration](../../../reference/configuration/node-configuration-parameters.md) and [cluster configuration](../../../reference/configuration/cluster-configuration-parameters.md) references.

## RocksDB Storage Engine Removed

The RocksDB partition storage engine is removed. The module, the `rocksdb` engine, and the profile type `engine = rocksdb` no longer exist.

- A node that starts with an `ignite.storage.engines.rocksdb` section in its configuration ignores the section.
- A node does not start if a storage profile uses `engine = rocksdb`. The error is `Failed to parse HOCON: Polymorphic configuration type is not correct: rocksdb`.
- There is no automatic migration for tables on a RocksDB profile.

If you have zones or tables on a RocksDB profile, re-create them on a profile of another engine before you upgrade:

1. Create a zone on an `aipersist` or `aimem` profile. See [Distribution Zones](../../../reference/sql/distribution-zones.md).
2. Create the new tables in that zone, and copy the data, for example with `INSERT INTO ... SELECT`.
3. Drop the old tables and zones.
4. Remove the RocksDB profiles from the node configuration files.

The RocksDB engine and the RocksDB-based Raft log are different features. This change affects only partition storage.

## Page Replacement Policies

The `RANDOM_LRU` and `SEGMENTED_LRU` page replacement policies are removed. The persistent page memory always uses the `CLOCK` policy, which was already the default.

The `replacementMode` property of an `aipersist` storage profile still exists and is deprecated. It still accepts `RANDOM_LRU`, `SEGMENTED_LRU`, and `CLOCK`, but 9.2 ignores the value and writes no warning. Remove `replacementMode` from your profiles so that the configuration states what the node does.

## Metric Changes

| 9.1 | 9.2 |
| --- | --- |
| Metric source `storage.aipersist.<profile>` | `storage.aipersist.profiles.<profile>`. The metrics in the source keep their names. |
| Metric `PageAcquireTime` | Removed. |

A storage profile that was named like an engine-level source, for example `checkpoint` or `io`, collided with it. The new `profiles` segment avoids that.

The engine-level sources `storage.aipersist`, `storage.aipersist.checkpoint`, and `storage.aipersist.io` keep their names. Update every dashboard, alert, exporter filter, and `metric source enable` or `metric source disable` command that uses the old source name, and remove `PageAcquireTime` from your dashboards.

GridGain 9.2 also adds the `raft.segstore.<storage-name>` metric source, because the segment log storage is now the default Raft log storage.

For the list of metrics, see [Metrics List](../../../reference/monitoring/metrics-list.md#storageaipersistprofilesprofile).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
