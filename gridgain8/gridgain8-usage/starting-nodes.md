---
description: >-
  How to start server and client nodes in GridGain, shut them down gracefully,
  set JVM options, and use node lifecycle events.
---

# Starting and Stopping Nodes

This chapter explains how to start server and client nodes.

There are two types of nodes: _server nodes_ and _client nodes_.
Server nodes participate in caching, compute execution, stream processing, etc.
Client nodes provide the ability to connect to the servers remotely.
Client nodes provide the whole set of Ignite APIs, including near caching, transactions, compute, streaming, services, etc. from the client side.

By default, all nodes are started as server nodes, and you should explicitly enable the client mode.

## Starting Server Nodes

To start a regular server node, use the following command or code snippet:

{% tabs %}
{% tab title="Shell" %}
```shell
ignite.sh path/to/configuration.xml
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
Ignite ignite = Ignition.start(cfg);
```

`Ignite` is an `AutoCloseable` object. You can use the _try-with-resource_ statement to close it automatically:

```java
IgniteConfiguration cfg = new IgniteConfiguration();

try (Ignite ignite = Ignition.start(cfg)) {
    //
}

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration();
IIgnite ignite = Ignition.Start(cfg);
```

`Ignite` is an `IDisposable` object. You can use the _using_ statement to close it automatically:

```csharp
var cfg = new IgniteConfiguration();
using (IIgnite ignite = Ignition.Start(cfg))
{
    //
}
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Starting Client Nodes

To start a client node, simply enable the client mode in the node configuration:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="clientMode" value="true"/>
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- prevent this client from reconnecting on connection loss -->
            <property name="clientReconnectDisabled" value="true"/>
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>

    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="slowClientQueueLimit" value="1000"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

// Enable client mode.
cfg.setClientMode(true);

// Start a client 
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    ClientMode = true
};
IIgnite ignite = Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Alternatively, for convenience, you can also enable or disable the client mode though the Ignition class to allow clients and servers to reuse the same configuration.

{% tabs %}
{% tab title="Java" %}
```java
Ignition.setClientMode(true);

// Start the node in client mode.
Ignite ignite = Ignition.start();
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
Ignition.ClientMode = true;
Ignition.Start();
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Shutting Down Nodes

When you perform a hard (forced) shutdown on a node, it can lead to data loss or data inconsistency and can even prevent the node from restarting.
Non-graceful shutdowns should be used as a last resort when the node is not responding and it cannot be shut down gracefully.

A graceful shutdown allows the node to finish critical operations and correctly complete its lifecycle.
The proper procedure to perform a graceful shutdown is as follows:

1. Stop the node using one of the following methods:
   - programmatically call `Ignite.close()`
   - send a user interrupt signal. GridGain uses a JVM shutdown hook to execute custom logic before the JVM stops. If you start the node by running `ignite.sh` and don't detach it from the terminal, you can stop the node by hitting `Ctrl+C`.
2. Remove the node from the [baseline topology](../architecture/baseline-topology.md). This step may not be necessary if [baseline auto-adjustment](../architecture/baseline-topology.md#baseline-topology-autoadjustment) is enabled.

If you use these commands on a node that _is_ in the baseline topology,
the node shuts down without waiting for the completion of the rebalancing process.
You can set the `ShutdownPolicy` property to `GRACEFUL` if you want to wait for backup partitions to be moved to other nodes before the shutdown.
See the [next section](#preventing-partition-loss-on-shutdown) for details.

Removing the node from the baseline topology starts the rebalancing process on the remaining nodes.
If you plan to restart the node shortly after shutdown, you don't have to do the rebalancing.
In this case, do not remove the nodes from the baseline topology.

### Preventing Partition Loss on Shutdown

When you simultaneously stop more nodes than the number of partition backups, some partitions may become unavailable to the remaining nodes (because both the primary and backup copies of the partition happen to be on the nodes that were shut down).
For example, if the number of backups for a cache is set to 1 and you stop 2 nodes, there is a chance that both the primary and backup copy of a partition becomes unavailable to the rest of the cluster.
The proper way of dealing with this situation is to stop one node, rebalance the data, and then wait until the rebalancing is finished before stopping the next node, and so on.
However, when the shutdown is triggered automatically (for example, when you do rolling upgrades or scaling the cluster in Kubernetes), you have no mechanism to wait for the completion of the rebalancing process and so you may lose data.

To prevent this situation, you can define a property (`ShutdownPolicy.GRACEFUL`) that delays the shutdown of a node until the shutdown does not lead to a partition loss.
The node checks if all the partitions are available to the remaining nodes and only then exits the process.

In other words, when the property is set, you will not be able to stop more than `min(CacheConfiguration.backups) + 1` nodes at a time without waiting until the data is rebalanced.
This is only applicable if you have at least one cache with partition backups and the node is stopped properly, i.e. using the commands described in the previous section:

- programmatically call `Ignite.close()`
- send a user interrupt signal. GridGain uses a JVM shutdown hook to execute custom logic before the JVM stops. If you start the node by running `ignite.sh` and don't detach it from the terminal, you can stop the node by hitting `Ctrl+C`.

A non-graceful shutdown (`kill -9`) cannot be prevented.

To enable partition loss prevention, set the `ShutdownPolicy` property to `GRACEFUL`.

```java
IgniteConfiguration cfg;
cfg.setShutdownPolicy(ShutdownPolicy.GRACEFUL);
```

{% hint style="warning" %}
If you have a cache without partition backups and you stop a node (even with this property set), you will lose the partition of the cache that was kept on this node.
{% endhint %}

## Setting JVM Options

There are several ways you can set JVM options when starting a node with the `ignite.sh` script.
These ways are described in the following sections.

### JVM_OPTS System Variable

You can set the `JVM_OPTS` environment variable:

```shell
export JVM_OPTS="$JVM_OPTS -Xmx6G -DIGNITE_TO_STRING_INCLUDE_SENSITIVE=false"; $IGNITE_HOME/bin/ignite.sh
```

### Command Line Arguments

You can also pass JVM options by using the `-J` prefix:

```shell
./ignite.sh -J-Xmx6G -J-DIGNITE_TO_STRING_INCLUDE_SENSITIVE=false
```

## Node Lifecycle Events

Lifecycle events give you an opportunity to execute custom code at different stages of the node lifecycle.

There are 4 lifecycle events:

|Event Type |  Description|
|---|---|
|BEFORE_NODE_START |  Invoked before the node's startup routine is initiated.|
|AFTER_NODE_START  |  Invoked right after then node has started.|
|BEFORE_NODE_STOP |    Invoked right before the node's stop routine is initiated.|
|AFTER_NODE_STOP | Invoked right after then node has stopped.|

The following steps describe how to add a custom lifecycle event listener.

1. Create a custom lifecycle bean by implementing the `LifecycleBean` interface.
   The interface has the `onLifecycleEvent()` method, which is called for any lifecycle event.

   ```java
   public class MyLifecycleBean implements LifecycleBean {
       @IgniteInstanceResource
       public Ignite ignite;

       @Override
       public void onLifecycleEvent(LifecycleEventType evt) {
           if (evt == LifecycleEventType.AFTER_NODE_START) {

               System.out.format("After the node (consistentId = %s) starts.\n", ignite.cluster().node().consistentId());

           }
       }
   }

   ```

2. Register the implementation in the node configuration.

   {% tabs %}
   {% tab title="XML" %}
   ```xml
   <bean class="org.apache.ignite.configuration.IgniteConfiguration">
       <property name="lifecycleBeans">
           <list>
               <bean class="org.apache.ignite.snippets.MyLifecycleBean"/>
           </list>
       </property>
       <property name="discoverySpi">
           <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
               <property name="ipFinder">
                   <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                       <property name="addresses">
                           <list>
                               <value>127.0.0.1:47500..47509</value>
                           </list>
                       </property>
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

   // Specify a lifecycle bean in the node configuration.
   cfg.setLifecycleBeans(new MyLifecycleBean());

   // Start the node.
   Ignite ignite = Ignition.start(cfg);
   ```
   {% endtab %}

   {% tab title="C#/.NET" %}
   unsupported
   {% endtab %}

   {% tab title="C++" %}
   unsupported
   {% endtab %}
   {% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
