---
description: >-
  How historical rebalancing transfers only the WAL delta accumulated while a
  persistent node was offline, its requirements, sizing, and configuration.
---

# Historical Rebalancing

## Overview

Ignite supports two rebalancing modes. A mode is selected based on your cluster configuration:

- Full rebalancing — this is a default rebalancing mode supported for both pure in-memory clusters and clusters with
Ignite Native Persistence. In this mode, a new or restarted node clears all its partitions and transfers data from
remote nodes. The node has to empty its partitions only if you use Ignite Native Persistence, and the node was restarted.

- Historical rebalancing - this mode is supported for the cluster with Ignite Native Persistence. Consider this mode if
nodes leave a cluster for a short time and store large data sets on disk. With historical rebalancing, a partition receives
only the delta of updates that happened while the partition's node was offline.

## Historical Rebalancing Requirements

Historical rebalancing relies on the history of updates stored in the write-ahead-log files (WALs) of cluster nodes.
The WALs' history must keep updates of all the partitions which deltas need to be rebalanced to a restarted node.

The maximum size of the WALs' archives should be influenced by the amount of time a node can go offline. You need to
estimate a potential offline time and configure the archive size accordingly:

{% code title="Java" %}
```java
IgniteConfiguration cfg;
DataStorageConfiguration storageCfg = cfg.getDataStorageConfiguration();
storageCfg.setMaxWalArchiveSize(512L * 1024 * 1024);
```
{% endcode %}

The default size of the WAL archive is `1Gb`. Also, suppose you configure the point-in-time recovery feature. In that case,
the archive's size becomes unlimited, and the depth of the history, which is transferred through the historical rebalancing,
is regulated by the `IGNITE_PDS_MAX_CHECKPOINT_MEMORY_HISTORY_SIZE` property (set in the number of checkpoints, `100` by default).

### Estimating the WAL History Size

For a more precise estimate of the required disk space, you need to consider several parameters:

- How quickly the WALs are populated on a particular node
- The time period a node can go offline
- If the WAL compression is used

Use the `DataStorageMetrics#getWalWritingRate` metric to estimate the first parameter. This metric returns the average
number of bytes written during the last minute. Note, observe this metric under a load comparable to the production one.

The second parameter, the potential offline time, should be derived from your maintenance procedures. Usually, administrators
document the time of cluster repairs or maintenance restarts.

Finally, the WAL compression parameter can decrease the size of the WAL history by two times and more. The final ratio
depends on your data pattern.

Overall, you can use the following formula to calculate a minimum WAL archive size for the historical rebalancing needs
- `wal_archive_size = wal_write_rate * node_offline_time * compression_coefficient`, where the `compression_coefficient` is
set to `1` if the compression is disabled, or to `[0.1-0.5]` depending on your data pattern.

Refer to this calculation example for reference:

{% code title="Archive Size Estimation" %}
```bash
wal_write_rate = 209715200 bytes (200 Mb of WAL files per second)

node_offline_time = 1800 seconds (the node can be unavailable for a half an hour)

compression_coefficient = 0.5 (that is the most pessimistic prediction of compression coefficient)

wal_archive_size = 209715200 * 1800 * 0.5 = 188743680000 bytes ~ 176 Gb
```
{% endcode %}

## Configuring Historical Rebalancing Behavior

In most cases, when a node returns to the cluster, the historical rebalancing is more effective than the full one,
as long as Ignite will transfer fewer data over the network. However, if the write-rate to the cluster is high, the WAL
size can grow much faster than the number of records stored in partitions. In such scenarios, the full rebalancing might
be more effective.

Ignite uses particular heuristics to decide which rebalancing mode to select for a given partition. Ignite falls back to the
full rebalancing mode if the number of records of the partition is fewer than the number of WAL updates that need to be
transferred. Otherwise, Ignite uses the historical rebalancing.

Several parameters can influence the heuristics:

- `IGNITE_PDS_WAL_REBALANCE_THRESHOLD` - if the number of records in the partition is less than the value of this property
(`500` by default), Ignite will use the full rebalancing. The historical rebalancing can be fully disabled by setting a
large number to this property (e.g., Integer.MAX_VALUE).
- `IGNITE_PREFER_WAL_REBALANCE` - set this property to `true` to request Ignite to disregard the heuristics and use the
historical rebalancing regardless of the number of records stored in the partition.

### Using ShutdownPolicy.GRACEFUL

After a node re-joined the cluster after leaving it for some time, it's not guaranteed that all outdated partitions
will be rebalanced in the historical fashion, even if the cluster kept the full delta in WALs. It happens if another
rebalancing process has changed the states of the partitions while the node was absent or some nodes haven't stored
partitions states on a disk yet.

Use the `ShutdownPolicy.GRACEFUL` policy to enforce the historical rebalancing even in the conditions mentioned above:

```java
IgniteConfiguration cfg;
cfg.setShutdownPolicy(ShutdownPolicy.GRACEFUL);
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
