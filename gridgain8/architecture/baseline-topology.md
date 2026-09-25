---
description: >-
  The baseline topology is the set of server nodes that hold data and controls
  when data rebalancing happens, either manually or through autoadjustment.
---

# Baseline Topology

The _baseline topology_ is a set of nodes meant to hold data.
The concept of baseline topology was introduced to give you the ability to control when you want to
[rebalance the data in the cluster](data-modeling/data-partitioning.md#rebalancing). For example, if
you have a cluster of 3 nodes where the data is distributed between the nodes, and you add 2 more nodes, the rebalancing
process re-distributes the data between all 5 nodes. The rebalancing process happens when the
baseline topology changes, which can either happen automatically or be triggered manually.

The baseline topology only includes server nodes; client nodes are never included because they do not store data.

The purpose of the baseline topology is to:

- Avoid unnecessary data transfer when a server node leaves the cluster for a short period of time, for example, due to
occasional network failures or scheduled server maintenance.
- Give you the ability to control when you want to rebalance the data.

Baseline topology changes automatically when [Baseline Topology Autoadjustment](#baseline-topology-autoadjustment) is enabled. This is the default
behavior for pure in-memory clusters. For persistent clusters, the baseline topology autoadjustment feature must be enabled
manually. By default, it is disabled and you have to change the baseline topology manually. You can change the baseline
topology using the [control script](../reference/cli-tool/README.md#activation-deactivation-and-topology-management).

{% hint style="warning" %}
Any attempt to create a cache while the baseline topology is being changed results in an exception.
For more details, see [Creating Caches Dynamically](../gridgain8-usage/key-value-api/basic-cache-operations.md#creating-caches-dynamically).
{% endhint %}

## Baseline Topology in Pure In-Memory Clusters

In pure in-memory clusters, the default behavior is to adjust the baseline topology to the set of all server nodes
automatically when you add or remove server nodes from the cluster. The data is rebalanced automatically, too.
You can disable the baseline autoadjustment feature and manage baseline topology manually.

{% hint style="info" %}
In previous releases, baseline topology was relevant only to clusters with persistence. However, since version 8.7.14,
it applies to in-memory clusters as well. If you have a pure in-memory cluster, the transition should be transparent
for you because, by default, the baseline topology changes automatically when a server node leaves or joins the cluster.
{% endhint %}

## Baseline Topology in Persistent Clusters

If your cluster has at least one data region in which persistence is enabled, the cluster is inactive when you start it for the first time.
In the inactive state, all operations are prohibited.
The cluster must be activated before you can create caches and upload data.
Cluster activation sets the current set of server nodes as the baseline topology.
When you restart the cluster, it is activated automatically as soon as all nodes that are registered in the baseline topology join in.
However, if some nodes do not join after a restart, you must to activate the cluster manually.

You can activate the cluster using one of the following tools:

- [Control script](../reference/cli-tool/README.md)
- [REST API command](../reference/rest-api/README.md#activate)
- Programmatically:

  {% tabs %}
  {% tab title="Java" %}
  ```java
  Ignite ignite = Ignition.start();

  ignite.cluster().state(ClusterState.ACTIVE);
  ```
  {% endtab %}
  {% tab title="C#/.NET" %}
  ```csharp
  IIgnite ignite = Ignition.Start();
  ignite.GetCluster().SetActive(true);
  ```
  {% endtab %}
  {% tab title="C++" %}
  unsupported
  {% endtab %}
  {% endtabs %}

## Baseline Topology Autoadjustment

Instead of changing the baseline topology manually, you can let the cluster do it automatically. This feature is called
Baseline Topology Autoadjustment. When it is enabled, the cluster monitors the state of its server nodes and sets the
baseline on the current topology automatically when the cluster topology is stable for a configurable period of time.

Here is what happens when the set of nodes in the cluster changes:

- The cluster waits for a configurable amount of time (5 min by default).
- If there are no other topology changes during this period, GridGain sets the baseline topology to the current set of nodes.
- If the set of nodes changes during this period, the timeout is updated.

Each change in the set of nodes resets the timeout for autoadjustment.
When the timeout expires and the current set of nodes is different from the baseline topology (for example, new nodes
are present or some old nodes left), GridGain changes the baseline topology to match the current set of nodes.
This also triggers data rebalancing.

When Baseline Topology Autoadjustment removes a node from the baseline topology, that node is no longer part of the
cluster's data distribution. If you restart the node so that it tries to rejoin the cluster, GridGain treats it like a
new node joining the baseline. The node's local persistence is cleaned before it rejoins.

The data on an expelled node is considered irrelevant, so it is discarded to save time and resources rather than
attempting to reconcile it during rejoin. As a result, when the node rejoins,
it has its partitions cleared during full rebalance and reloads all necessary data from other nodes.

The autoadjustment timeout allows you to avoid data rebalancing when a node disconnects for a short period due to a
temporary network problem or when you want to quickly restart the node.
You can set the timeout to a higher value if you expect temporary changes in the set of nodes and don't want to change
the baseline topology.

Baseline topology is autoadjusted only if the cluster is in the active state.

To enable automatic baseline adjustment, you can use the
[control script](../reference/cli-tool/README.md) or the
programmatic API methods shown below:

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

ignite.cluster().baselineAutoAdjustEnabled(true);

ignite.cluster().baselineAutoAdjustTimeout(30000);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
IIgnite ignite = Ignition.Start();
ignite.GetCluster().SetBaselineAutoAdjustEnabledFlag(true);
ignite.GetCluster().SetBaselineAutoAdjustTimeout(30000);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Automatic bidirectional baseline adjustment is deprecated and is replaced by [Separate Autoadjustment for Scale-Up and Scale-Down](#separate-autoadjustment-for-scale-up-and-scale-down). By default, this API adjusts scale up and scale down autoadjustment separately, but sets the same values.
{% endhint %}

To disable automatic baseline adjustment, use the same method with `false` passed in:

{% tabs %}
{% tab title="Java" %}
```java
ignite.cluster().baselineAutoAdjustEnabled(false);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
ignite.GetCluster().SetBaselineAutoAdjustEnabledFlag(false);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Separate Autoadjustment for Scale-Up and Scale-Down

You can control baseline autoadjustment separately for _scale-up_ events (server nodes joining the cluster) and _scale-down_ events (server nodes leaving the cluster).

Use the `AutoAdjustMode` to select the direction:

- `AutoAdjustMode.SCALE_UP` — autoadjustment that runs when server nodes join.
- `AutoAdjustMode.SCALE_DOWN` — autoadjustment that runs when server nodes leave.

You can also control adjustment in each direction independently:

{% tabs %}
{% tab title="Java" %}
```java
IgniteCluster cluster = ignite.cluster();

// Enable scale-up autoadjustment with a 30-second timeout.
cluster.baselineAutoAdjustEnabled(AutoAdjustMode.SCALE_UP, true);
cluster.baselineAutoAdjustTimeout(AutoAdjustMode.SCALE_UP, 30_000);

// Enable scale-down autoadjustment with a 5-minute timeout.
cluster.baselineAutoAdjustEnabled(AutoAdjustMode.SCALE_DOWN, true);
cluster.baselineAutoAdjustTimeout(AutoAdjustMode.SCALE_DOWN, 300_000);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Monitoring Baseline Topology

You can use the following tools to monitor and/or manage the baseline topology:

- [Control Script](../reference/cli-tool/README.md)
- [JMX Beans](../reference/monitoring/jmx-metrics.md#monitoring-topology)
- [Control Center]({tools}/control-center/gg8/dashboard/my-cluster)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
