---
description: >-
  How GridGain handles lost partitions through partition loss policies, how to
  listen for loss events, reset lost partitions, and recover in each cluster type.
---

# Partition Loss Policy

Throughout the cluster’s lifecycle, it may happen that some data partitions are lost due to the failure of the primary and backup nodes for the partitions.
Such a situation leads to a partial data loss and needs to be addressed according to your use case.

A partition is lost when both the primary copy and all backup copies of the partition are not available to the cluster, i.e. when the primary and backup nodes for the partition become unavailable. It means that for a given cache, you cannot afford to lose more than `number_of_backups` nodes.
You can set the number of backup partitions for a cache in the [cache configuration](../../gridgain8-usage/configuring-caches/configuring-backups.md).

When the cluster topology changes, GridGain checks if the change resulted in a partition loss, and, depending on the configured partition loss policy and baseline autoadjustment settings, allows or prohibits operations on caches.
See the description of each policy in the next section.

For pure in-memory caches, when a partition is lost, the data from the partition cannot be recovered unless you load it into the cluster again.
For persistent caches, the data is not physically lost, because it has been persisted to disk.
When the nodes that failed or disconnected return to the cluster (after a restart), the data is loaded from the disk.
In this case, you need to reset the state of the lost partitions in order to continue to use the data. See [Handling Partition Loss](#handling-partition-loss).

## Configuring Partition Loss Policy

GridGain supports the following partition loss policies:

| Policy | Description |
|---|---|
| `IGNORE` | Partition loss is ignored.  The cluster treats lost partitions as if they are empty. When you request data from such partitions, the cluster returns empty values as if the data was never there.<br><br>This policy can only be used in pure in-memory clusters where baseline autoadjustment is enabled with a 0 timeout, and is the default value for such configurations.<br>In all other configurations (the clusters where there is at least one data region with persistence), the `IGNORE` policy is replaced with `READ_WRITE_SAFE` even if you explicitly set `IGNORE` in the cache configuration. |
| `READ_WRITE_SAFE` | Any attempt to read from or write to a lost partition of the cache results in an exception. However, you can read/write to the available partitions. |
| `READ_ONLY_SAFE` | The cache is available in read-only mode. Write operations to the cache result in an exception. Read operations from the lost partitions result in an exception as well. See the [Handling Partition Loss](#handling-partition-loss) section below. |

Partition loss policy is configured per cache.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>

            <property name="partitionLossPolicy" value="READ_ONLY_SAFE"/>
        </bean>
    </property>
    <!-- other properties -->

</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration("myCache");

cacheCfg.setPartitionLossPolicy(PartitionLossPolicy.READ_ONLY_SAFE);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Listening to Partition Loss Events

You can listen to the `EVT_CACHE_REBALANCE_PART_DATA_LOST` event to be notified when a partition loss occurs.
This event is fired for every partition that is lost and contains the number of the lost partition and ID of the node that held the partition.
Partition loss events are triggered only when either `READ_WRITE_SAFE` or `READ_ONLY_SAFE` policy is used.

Enable the event in the cluster configuration first.
See [Enabling Events](../../gridgain8-usage/events/listening-to-events.md#enabling-events).

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

IgnitePredicate<Event> locLsnr = evt -> {
    CacheRebalancingEvent cacheEvt = (CacheRebalancingEvent) evt;

    int lostPart = cacheEvt.partition();

    ClusterNode node = cacheEvt.discoveryNode();

    System.out.println(lostPart);

    return true; // Continue listening.
};

ignite.events().localListen(locLsnr, EventType.EVT_CACHE_REBALANCE_PART_DATA_LOST);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

See [Cache Rebalancing Events](../../gridgain8-usage/events/events.md#cache-rebalancing-events) for the information about other events related to rebalancing of partitions.

## Handling Partition Loss

If data is not physically lost, you can return the nodes that left the cluster and reset the state of the lost partitions so that you can continue to work with the data.
You can reset the state of lost partition by calling `Ignite.resetLostPartitions(cacheNames)` for specific caches or via the control script.

{% tabs %}
{% tab title="Java" %}
```java
ignite.resetLostPartitions(Arrays.asList("myCache"));
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The control script command:

```bash
control.sh --cache reset_lost_partitions cache_name
```

If you don't reset lost partitions, read and write operations (depending on the policy configured for the cache) from the lost partitions will throw a `CacheException`.
You can check if the exception is due to the state of the partitions by analyzing its root cause, like so:

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, Integer> cache = ignite.cache("myCache");

try {
    Integer value = cache.get(3);
    System.out.println(value);
} catch (CacheException e) {
    if (e.getCause() instanceof CacheInvalidStateException) {
        System.out.println(e.getCause().getMessage());
    } else {
        e.printStackTrace();
    }
}
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can get the list of lost partitions for a cache via `IgniteCache.lostPartitions()`.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, String> cache = ignite.cache("myCache");

cache.lostPartitions();
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Bypassing Partition Loss Protection

Under the `READ_WRITE_SAFE` and `READ_ONLY_SAFE` policies, a read of a key that belongs to a lost
partition throws an exception, so an application that does not know which partitions were lost
must be ready for any read to fail.
If you would rather have such reads return an empty result instead, call `withPartitionRecover()`
to get a cache view that ignores partition loss protection.

Reads through that view do not throw an exception.
A key that belongs to a lost partition returns `null`.
Keys in the surviving partitions return their values normally.
Write operations are not affected.

`withPartitionRecover()` returns a new view, so the original cache instance keeps its normal
behavior.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, Integer> cache = ignite.cache("myCache");

// Does not throw if key 3 is in a lost partition; returns null instead.
Integer value = cache.withPartitionRecover().get(3);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The Java thin client provides the same method on `ClientCache`:

{% tabs %}
{% tab title="Java" %}
```java
ClientCache<Integer, Integer> cache = client.cache("myCache");

Integer value = cache.withPartitionRecover().get(3);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Recovering From a Partition Loss

The following sections explain how you can recover from a partition loss in different cluster configurations.

### Pure In-memory Cluster with IGNORE policy

In this configuration, the `IGNORE` policy is only applicable when baseline autoadjustment is enabled with a 0 timeout, which is the default setting for in-memory clusters.
For such configurations, partition loss is ignored.
The cache continues to be operational with the lost partitions treated as empty.

When baseline autoadjustment is disabled or when the timeout is greater than 0, the `IGNORE` policy is replaced with `READ_WRITE_SAFE`.

### Pure In-memory Cluster with READ_WRITE_SAFE or READ_ONLY_SAFE policy

User operations are blocked until you reset the lost partitions.
After the reset, continue using the cache but the data will be lost.

When baseline autoadjustment is disabled or when the timeout is greater than 0, you must return the nodes (at least one partition owner for each partition) to the baseline topology before resetting the lost partitions.
Otherwise, `Ignite.resetLostPartitions(cacheNames)` throws a `ClusterTopologyCheckedException` with a message `Cannot reset lost partitions because no baseline nodes are online [cache=someCahe, partition=someLostPart]` indicating that safe recovery is not possible.
If you cannot return the nodes for some reason (e.g. hardware failure), exclude them from the baseline topology manually before attempting to reset the lost partitions.

### Clusters with Persistence

In clusters where all data regions are configured to persist data on disk (there is no in-memory regions), there are two ways to recover from a partition loss (provided the data is not damaged physically):

1. Return _all_ nodes to the baseline topology,
2. Reset lost partitions (call `Ignite.resetLostPartitions(...)` for all caches).

or

1. Stop all nodes,
2. Start all nodes including those that failed and activate the cluster.

If some nodes cannot be returned, exclude them from the baseline topology before attempting to reset the state of lost partitions.

### Clusters with Both In-memory and Persistent Caches

In clusters where there are both in-memory regions and persistent regions, in-memory caches are treated the same way as in pure in-memory clusters with partition loss policy set to `READ_WRITE_SAFE`, and persistent caches are treated the same way as in persistent clusters.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
