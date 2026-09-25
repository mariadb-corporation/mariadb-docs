---
description: >-
  Methods for tracking GridGain data rebalance progress and status using the
  control script, cache-group metrics, cache-level metrics, and log patterns.
---

# Monitoring Rebalance Progress

[Data rebalancing](../architecture/rebalancing/data-rebalancing.md) is a process of redistributing partition data across nodes after a topology change. Depending on data volume and network throughput, the rebalance process can take anywhere from seconds to hours. This page lists common methods of tracking the rebalance process and its status.

## Checking Whether the Cluster Is Fully Rebalanced

To find out if the cluster is currently performing data rebalance, check the cluster-wide rebalance state using the control script:

```bash
control.sh --metric 'cluster.Rebalanced'
```

This returns `true` when all partitions across the cluster are in `OWNING` state.

## Monitoring With Cache-Group Metrics

Data rebalance metrics are available under `cacheGroups.<groupName>` registry and are updated in real time by the demander as the rebalance progresses.

Metric registry values can be read via JMX under the following ObjectName pattern:

```
org.apache.ignite:group=<IgniteInstanceName>,name=<CacheGroupName>,type=CacheGroupMetrics
```

### Key Metrics

Use the following metrics to assess rebalance progress for a cache group.

#### Partition Progress

| Metric | Description |
|---|---|
| `RebalancingPartitionsLeft` | Partitions the demander has not yet finished pulling. Decrements to `0` as each partition completes the rebalance process. |
| `RebalancingPartitionsTotal` | Total partitions involved in the current rebalance. |

When `RebalancingPartitionsLeft` reaches `0`, the group rebalance is complete.

#### Throughput and Volume

| Metric | Description |
|---|---|
| `RebalancingReceivedKeys` | Cumulative keys received at the group level since rebalancing started. Aggregates across all caches in the group. |
| `RebalancingReceivedBytes` | Cumulative bytes received at the group level since rebalancing started. |
| `RebalancingFullReceivedKeys` | Keys received via full rebalance, broken down per supplier. |
| `RebalancingHistReceivedKeys` | Keys received via historical rebalance, broken down per supplier. |
| `RebalancingFullReceivedBytes` | Bytes received via full rebalance, broken down per supplier. |
| `RebalancingHistReceivedBytes` | Bytes received via historical rebalance, broken down per supplier. |

#### Timing

| Metric | Description |
|---|---|
| `RebalancingStartTime` | Timestamp when the first demand message was sent. |
| `RebalancingEndTime` | Timestamp when rebalancing completed. Populated only after completion. |
| `RebalancingLastCancelledTime` | Timestamp of the most recent rebalancing cancellation, if any. |

## Monitoring With Cache-Level Metrics

You can also use the metrics accessed through the programmatic API to monitor the rebalance process on cache level. The `CacheMetrics` object is obtained per-cache via `cache.localMetrics()`. All values reflect the local node only.

The example below shows how you can get the metrics object:

```java
IgniteCache<K, V> cache = ignite.cache("cacheName");
CacheMetrics metrics = cache.localMetrics();
```

### Checking Partition State

```java
int movingPartitions = metrics.getRebalancingPartitionsCount(); // partitions in MOVING state
int totalPartitions  = metrics.getTotalPartitionsCount();       // all partitions on this node
```

When `getRebalancingPartitionsCount()` returns `0`, there are no `MOVING` partitions on the local node for this cache.

### Tracking Key Progress

```java
long rebalancedKeys = metrics.getRebalancedKeys();
long estimatedKeys  = metrics.getEstimatedRebalancingKeys();
long keysLeft       = metrics.getKeysToRebalanceLeft();   // estimatedKeys - rebalancedKeys
```

Note that:

- `RebalancedKeys` and `RebalancingKeysRate` metrics work only for caches where the cache group
is explicitly specified in the cache configuration. If no cache group is set, they will not update.
- `EstimatedRebalancingKeys` metric provides an estimate calculated from partition counters at rebalance start
and does not reflect subsequent compaction or deletes. In a shared cache group, the value represents the sum
of deltas across all caches in the group, not just the cache being queried.
- `KeysToRebalanceLeft` metric does not update in real time via JMX during an active rebalance.
For live progress tracking, use `RebalancingPartitionsLeft` from the metric registry instead.

### Tracking Throughput

```java
long keysPerSecond  = metrics.getRebalancingKeysRate();   // sliding window rate
long bytesPerSecond = metrics.getRebalancingBytesRate();  // sliding window rate
```

Both rates are calculated over a sliding window defined by the `IGNITE_REBALANCE_STATISTICS_TIME_INTERVAL`
system property (default: `60000` ms).
If you need more responsive rate readings during an incident, reduce this value before starting the node:

```java
// Must be set before Ignition.start()
System.setProperty("IGNITE_REBALANCE_STATISTICS_TIME_INTERVAL", "10000");
```

### Checking Partition Clearing

```java
long clearingLeft = metrics.getRebalanceClearingPartitionsLeft();
```

Partitions must be cleared before they can accept incoming data.
If `getRebalanceClearingPartitionsLeft()` is non-zero and not decreasing,
clearing may be stalled. Check GC pressure and I/O throughput on the affected node.

### Checking Timing

```java
long startTime       = metrics.getRebalancingStartTime();           // -1 if not started
long estimatedFinish = metrics.getEstimatedRebalancingFinishTime(); // -1 if unavailable
```

Both return `-1` when the value is not yet available.
`getEstimatedRebalancingFinishTime()` is computed from current throughput and remaining keys,
so it will be inaccurate or unavailable early in the rebalance.

## Additional Monitoring Methods

The following methods provide supplementary information but are not the primary tools for live rebalance monitoring.

### Event Listeners

`EventType.EVTS_CACHE_REBALANCE` delivers lifecycle events (partition loaded, partition supplied,
rebalance started/stopped). For more information about using events, see the [Events documentation](../gridgain8-usage/events/events.md#cache-rebalancing-events).

### Cluster and Partition State

While the control script does not provide dedicated tools for monitoring rebalance process, you can still assess cluster status by retrieving information about cluster state and its topology:

```bash
# Overall cluster state
control.sh --state

# Baseline topology
control.sh --baseline

# Partition distribution across nodes
control.sh --cache distribution null
```

### Log Patterns

To identify which partitions are being rebalanced and via which method (full vs. historical), you can analyse the node log:

- Search for `Starting rebalance` text for information about how rebalance started.
- Search for `Completed rebalance` text for information about how rebalance finished.

### Partition Topology

`CacheGroupMetricsMXBean` provides a cluster-wide view of partition state distribution
(`OWNING`, `MOVING`, `RENTING`) at the cache group level.
This is useful for confirming that all nodes have converged after rebalancing completes.

{% hint style="info" %}
This bean is deprecated. Monitor cache group metrics instead.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
