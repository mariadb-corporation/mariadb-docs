---
description: >-
  The ClusterGroup interface represents a logical group of nodes used to limit GridGain operations to a subset of the cluster.
---

# Cluster Groups

The `ClusterGroup` interface represents a logical group of nodes, which can be used in many of GridGain's APIs when you want to limit the scope of specific operations to a subset of nodes (instead of the whole cluster). For example, you may wish to deploy a service only on remote nodes or execute a job only on the set of nodes that have a specific attribute.

{% hint style="info" %}
Note that the `IgniteCluster` interface is also a cluster group which includes all the nodes in the cluster.
{% endhint %}

You can limit job execution, service deployment, messaging, events, and
other tasks to run only on a specific set of node. For example, here is
how to broadcast a job only to remote nodes (excluding the local node).

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();

IgniteCluster cluster = ignite.cluster();

// Get compute instance which will only execute
// over remote nodes, i.e. all the nodes except for this one.
IgniteCompute compute = ignite.compute(cluster.forRemotes());

// Broadcast to all remote nodes and print the ID of the node
// on which this closure is executing.
compute.broadcast(() -> System.out.println("Hello Node: " + ignite.cluster().localNode().id()));
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class PrintNodeIdAction : IComputeAction
{
    public void Invoke()
    {
        Console.WriteLine("Hello node: " +
                          Ignition.GetIgnite().GetCluster().GetLocalNode().Id);
    }
}

public static void RemotesBroadcastDemo()
{
    var ignite = Ignition.Start();

    var cluster = ignite.GetCluster();

    // Get compute instance which will only execute
    // over remote nodes, i.e. all the nodes except for this one.
    var compute = cluster.ForRemotes().GetCompute();

    // Broadcast to all remote nodes and print the ID of the node
    // on which this closure is executing.
    compute.Broadcast(new PrintNodeIdAction());
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

For convenience, GridGain comes with a number of predefined cluster groups.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCluster cluster = ignite.cluster();

// All nodes on which the cache with name "myCache" is deployed,
// either in client or server mode.
ClusterGroup cacheGroup = cluster.forCacheNodes("myCache");

// All data nodes responsible for caching data for "myCache".
ClusterGroup dataGroup = cluster.forDataNodes("myCache");

// All client nodes that can access "myCache".
ClusterGroup clientGroup = cluster.forClientNodes("myCache");
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cluster = ignite.GetCluster();
            
// All nodes on which cache with name "myCache" is deployed,
// either in client or server mode.
var cacheGroup = cluster.ForCacheNodes("myCache");

// All data nodes responsible for caching data for "myCache".
var dataGroup = cluster.ForDataNodes("myCache");

// All client nodes that access "myCache".
var clientGroup = cluster.ForClientNodes("myCache");
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
