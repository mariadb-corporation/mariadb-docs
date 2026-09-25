---
description: >-
  How GridGain redistributes partitions across nodes to keep data balanced,
  including rebalancing modes, thread pool, message throttling, and monitoring.
---

# Data Rebalancing

## Overview

Data rebalancing is the process of redistributing partitions across cluster nodes to maintain balanced data distribution. Rebalancing is triggered in two scenarios:

- When a new node permanently joins the cluster or an existing node permanently leaves, partitions are relocated to maintain equal distribution.
- When a node temporarily leaves the cluster and then rejoins, a [historical](historical-rebalancing.md) or full rebalance is initiated to restore partition consistency.

If an existing node permanently leaves the cluster and backups are not configured, you lose the partitions stored on this node.
When backups are configured, one of the backup copies of the lost partitions becomes a primary partition and the rebalancing process is initiated.

{% hint style="warning" %}
For permanent cluster changes, rebalancing is triggered by changes in the [Baseline Topology](../baseline-topology.md). In pure in-memory clusters, the baseline topology changes automatically, triggering immediate rebalancing when nodes join or leave. In clusters with persistence, the baseline topology must be changed manually, or can be changed automatically when [automatic baseline adjustment](../baseline-topology.md#baseline-topology-autoadjustment) is enabled.

For temporary node absences (where the node rejoins without baseline changes), see [Historical Rebalancing](historical-rebalancing.md).
{% endhint %}

Rebalancing is configured per cache.

## Configuring Rebalancing Mode

GridGain supports both synchronous and asynchronous rebalancing.
In the synchronous mode, any operation on the cache data is blocked until rebalancing is finished.
In the asynchronous mode, the rebalancing process is done asynchronously.
You can also disable rebalancing for a particular cache.

To change the rebalancing mode, set one of the following values in the cache configuration.

- `SYNC` — Synchronous rebalancing mode. In this mode, any call to the cache public API is blocked until rebalancing is finished.
- `ASYNC` — Asynchronous rebalancing mode. Distributed caches are available immediately and load all necessary data from other available cluster nodes in the background.
- `NONE` — In this mode no rebalancing takes place, which means that caches are either loaded on demand from the persistent storage whenever data is accessed, or populated explicitly.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">

    <property name="rebalanceThreadPoolSize" value="4"/>

    <property name="cacheConfiguration">
        <list>
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
                <property name="name" value="mycache"/>
                <!-- enable synchronous rebalance mode -->
                <property name="rebalanceMode" value="SYNC"/>
                <!-- Set batch size. -->
                <property name="rebalanceBatchSize" value="#{2 * 1024 * 1024}"/>
                <!-- Set throttle interval. -->
                <property name="rebalanceThrottle" value="100"/>
            </bean>
        </list>
    </property>
    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                   
                <!-- Uncomment static IP finder to enable static-based discovery of initial nodes. -->
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <!--bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder"-->
                    <property name="addresses">
                        <list>
                            <!-- In distributed environment, replace with actual host IP address. -->
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>
                <!-- enable synchronous rebalance mode -->
                <property name="rebalanceMode" value="SYNC"/>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setRebalanceThreadPoolSize(4);

CacheConfiguration cacheCfg = new CacheConfiguration("mycache");

cacheCfg.setRebalanceMode(CacheRebalanceMode.SYNC);

cfg.setRebalanceBatchSize(2 * 1024 * 1024);
cfg.setRebalanceThrottle(100);

cfg.setCacheConfiguration(cacheCfg);

// Start a node.
Ignite ignite = Ignition.start(cfg);

cacheCfg.setRebalanceMode(CacheRebalanceMode.SYNC);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
IgniteConfiguration cfg = new IgniteConfiguration
{
    CacheConfiguration = new[]
    {
        new CacheConfiguration
        {
            Name = "mycache",
            RebalanceMode = CacheRebalanceMode.Sync
        }
    }
};

// Start a node.
var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Historical Rebalancing**

When a node with Ignite Native Persistence temporarily leaves and rejoins the cluster without a baseline topology change,
[Historical rebalancing](historical-rebalancing.md) is used to speed up the rebalancing process by
transferring only the data changes that occurred during the node's absence, rather than copying all partition data.
{% endhint %}

## Configuring Rebalance Thread Pool

By default, rebalancing is performed in one thread on each node.
It means that at each point in time only one thread is used to transfer batches from one node to another, or to process batches coming from the remote node.

You can increase the number of threads that are taken from the system thread pool and used for rebalancing.
A system thread is taken from the pool every time a node needs to send a batch of data to a remote node or needs to process a batch that came from a remote node.
The thread is relinquished after the batch is processed.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">

    <property name="rebalanceThreadPoolSize" value="4"/>

    <property name="cacheConfiguration">
        <list>
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
                <property name="name" value="mycache"/>
                <!-- enable synchronous rebalance mode -->
                <property name="rebalanceMode" value="SYNC"/>
                <!-- Set batch size. -->
                <property name="rebalanceBatchSize" value="#{2 * 1024 * 1024}"/>
                <!-- Set throttle interval. -->
                <property name="rebalanceThrottle" value="100"/>
            </bean>
        </list>
    </property>
    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                   
                <!-- Uncomment static IP finder to enable static-based discovery of initial nodes. -->
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <!--bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder"-->
                    <property name="addresses">
                        <list>
                            <!-- In distributed environment, replace with actual host IP address. -->
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>

    <property name="rebalanceThreadPoolSize" value="4"/>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setRebalanceThreadPoolSize(4);

CacheConfiguration cacheCfg = new CacheConfiguration("mycache");

cacheCfg.setRebalanceMode(CacheRebalanceMode.SYNC);

cfg.setRebalanceBatchSize(2 * 1024 * 1024);
cfg.setRebalanceThrottle(100);

cfg.setCacheConfiguration(cacheCfg);

// Start a node.
Ignite ignite = Ignition.start(cfg);

cfg.setRebalanceThreadPoolSize(4);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
System thread pool is widely used internally by all the cache related operations (put, get, etc.), SQL engine, and other modules. Setting the size of the rebalancing thread pool to a large value may significantly increase rebalancing performance at the cost of decreased throughput.
{% endhint %}

## Rebalance Message Throttling

When data is transferred from one node to another, the whole data set is split into batches and each batch is sent in a separate message.
You can configure the batch size and the amount of time the node waits between messages.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="rebalanceBatchSize" value="#{2 * 1024 * 1024}"/>
    <property name="rebalanceThrottle" value="100"/>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setRebalanceThreadPoolSize(4);

CacheConfiguration cacheCfg = new CacheConfiguration("mycache");

cacheCfg.setRebalanceMode(CacheRebalanceMode.SYNC);

cfg.setRebalanceBatchSize(2 * 1024 * 1024);
cfg.setRebalanceThrottle(100);

cfg.setCacheConfiguration(cacheCfg);

// Start a node.
Ignite ignite = Ignition.start(cfg);

cfg.setRebalanceBatchSize(2 * 1024 * 1024);
cfg.setRebalanceThrottle(100);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
IgniteConfiguration cfg = new IgniteConfiguration
{
    CacheConfiguration = new[]
    {
        new CacheConfiguration
        {
            Name = "mycache",
            RebalanceBatchSize = 2 * 1024 * 1024,
            RebalanceThrottle = new TimeSpan(0, 0, 0, 0, 100)
        }
    }
};

// Start a node.
var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Other Properties

The following table lists the properties of `CacheConfiguration` related to rebalancing:

| Property | Description | Default Value |
|---|---|---|
| `rebalanceDelay` | A delay in milliseconds before the rebalancing process starts after a node joins or leaves the topology. Rebalancing delay is useful if you plan to restart nodes or start multiple nodes at once or one after another and don't want to repartition and rebalance the data until all nodes are started. | 0 (no delay) |
| `rebalanceOrder` | The order in which rebalancing should be done. Rebalance order can be set to a non-zero value for caches with SYNC or ASYNC rebalance modes only. Rebalancing for caches with smaller rebalance order is completed first. By default, rebalancing is not ordered. | 0 |

The following table lists the properties of `IgniteConfiguration` related to rebalancing:

| Property | Description | Default Value |
|---|---|---|
| `rebalanceBatchSize` | The size in bytes of a single rebalance message. The rebalancing algorithm splits the data on every node into multiple batches prior to sending it to other nodes. | 512KB |
| `rebalanceTimeout` | Timeout for pending rebalancing messages when they are exchanged between the nodes. | 10 seconds |
| `rebalanceBatchesPrefetchCnt` | The number of batches generated by supply node at the start of the rebalancing procedure. For better rebalancing performance, supplier node can provide more than one batch at the start of rebalancing and provide more for all later requests. | 2 |
| `rebalanceThreadPoolSize` | Maximum number of threads that are used in rebalancing process. | min(4, max(1, AVAILABLE_PROCESSOR_CNT / 4)) |
| `rebalanceThrottle` | Time between rebalance messages in milliseconds. | 0 (disabled) |

## Monitoring Rebalancing Process

You can monitor the [rebalancing process for specific caches using JMX](../../reference/monitoring/jmx-metrics.md#monitoring-rebalancing).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
