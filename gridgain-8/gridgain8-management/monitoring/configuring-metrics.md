---
description: >-
  How to enable or disable GridGain metrics — cache, data region, persistence,
  and index operation metrics — through configuration, JMX beans, or system properties.
---

# Configuring Metrics

Metrics can provide information about cluster performance and potential issues. As such, metrics are enabled by default.

Metric collection is not a free operation, so you may want to disable some metrics for additional performance.

## Disabling Cache Metrics

Cache metrics show statistics on the amount of data stored in caches, the total number and frequency of cache operations, etc. as well as some cache configuration properties for information purposes.

You can disable cache metrics to save on performance expenses for gathering them. To do this, use one of the methods described below for each cache you want to monitor.

{% tabs %}
{% tab title="XML" %}
```xml
<property name="cacheConfiguration">
    <list>
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="mycache"/>
            <!-- Disable statistics for the cache. -->
            <property name="statisticsEnabled" value="false"/>
        </bean>
    </list>
</property>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

CacheConfiguration cacheCfg = new CacheConfiguration("test-cache");

// Enable statistics for the cache.
cacheCfg.setStatisticsEnabled(true);

cfg.setCacheConfiguration(cacheCfg);

// Start the node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    CacheConfiguration = new[]
    {
        new CacheConfiguration("my-cache")
        {
            EnableStatistics = false
        }
    }
};

var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Enabling Cache Metrics at Runtime

You can turn cache metrics on and off in a running cluster dynamically. The change takes effect immediately and does not require a restart.

Use the `IgniteCache.enableStatistics()` method:

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, Person> cache = ignite.cache("myCache");

// Start collecting metrics for this cache.
cache.enableStatistics(true);

// Stop collecting them.
cache.enableStatistics(false);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
ICache<int, Person> cache = ignite.GetCache<int, Person>("myCache");

cache.EnableStatistics(true);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can also change several caches in a single call by using `IgniteCluster.enableStatistics()`:

{% tabs %}
{% tab title="Java" %}
```java
ignite.cluster().enableStatistics(Arrays.asList("myCache", "myOtherCache"), true);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
ignite.GetCluster().EnableStatistics(new[] { "myCache", "myOtherCache" }, true);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Every cache you name must already be started on the node that makes the call, otherwise the call fails with a `Cache not found` error.
{% endhint %}

The new value is also saved to the cache configuration. For a cache in a data region with persistence enabled, the setting survives a cluster restart.

## Reading Cache Metrics

To read the latest metrics snapshot of a specific cache, use one of the `IgniteCache` methods:

- `IgniteCache.metrics()` — gets the metrics snapshot of the whole cluster where the cache is deployed.
- `IgniteCache.metrics(ClusterGroup grp)` — gets the metrics snapshot for the nodes that belong to the given cluster group.
- `IgniteCache.localMetrics()` — gets the local node's metrics snapshot for the cache.

```java
IgniteCache<Integer, Person> cache = ignite.getOrCreateCache("myCache");

// Get cache metrics
CacheMetrics cm = cache.metrics();

System.out.println("Avg put time: " + cm.getAveragePutTime());

System.out.println("Avg get time: " + cm.getAverageGetTime());
```

To calculate the size of a cache, see [Memory Usage Calculation](monitoring-memory.md#memory-usage-calculation).

## JMX Beans

For each cache on a node, GridGain creates two JMX Beans: one with cache information specific to the node, and one with global (cluster-wide) information about the cache.

**Local cache information MBean:**

```
group=<Cache_Name>,name="org.apache.ignite.internal.processors.cache.CacheLocalMetricsMXBeanImpl"
```

**Global cache information MBean:**

```
group=<Cache_Name>,name="org.apache.ignite.internal.processors.cache.CacheClusterMetricsMXBeanImpl"
```

The more common and useful beans and metrics are:

- [CacheMetricsMXBean](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/mxbean/CacheMetricsMXBean.html):
  - CacheGets (total number of requests to the cache)
  - AverageGetTime (mean time to execute gets)
  - AverageTxCommitTime (mean time to execute a transaction commit)
- [CacheGroupMetricsMXBean](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/mxbean/CacheGroupMetricsMXBean.html):
  - LocalNodeMovingPartitionsCount (count of partitions where state = MOVING for this cache group located on this node)
  - ClusterMovingPartitionsCount (count of partitions where state = MOVING for this cache group in the entire cluster)
  - ClusterOwningPartitionsCount (count of partitions where state = OWNING for this cache group in the entire cluster)

You can access cache metrics via the `CacheMetricsMXBean` interface. You can connect to the bean from any JMX-compliant tool or API. If you need to work with the bean from your application, use `IgniteCache.mxBean()` or `IgniteCache.localMxBean()` to get a bean reference.

Use the `enableStatistics()` and `disableStatistics()` methods exposed by the bean to start and stop collecting cache metrics, and `clear()` to reset the counters.

For a complete list of metrics available, refer to the [CacheMetricsMXBean](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/mxbean/CacheMetricsMXBean.html) javadoc.

To change the configuration of other metrics at runtime, or to reset a metric registry, use the [MetricsMxBean](#configuring-metrics-with-metricsmxbean) MBean.

## Disabling Data Region Metrics

Data region metrics expose information about data regions, including memory and storage size of the region.
Disable data region metrics for every region you do not need the metrics for.

Data region metrics can be disabled in two ways:

* in the [configuration of the region](../../gridgain8-development/memory-configuration/data-regions.md)
* via JMX Beans

The following example illustrates how to enable metrics for the default data region and one custom data region.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <!-- disable mertrics for the default data region -->
                    <property name="metricsEnabled" value="false"/>
                    <!-- other properties -->
                </bean>
            </property>
            <property name="dataRegionConfigurations">
                <list>
                    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                        <!-- Custom region name. -->
                        <property name="name" value="myDataRegion"/>
                        <!-- Disable metrics for this data region  -->
                        <property name="metricsEnabled" value="false"/>

                        <property name="persistenceEnabled" value="true"/>
                        <!-- other properties -->
                    </bean>
                </list>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

DataStorageConfiguration storageCfg = new DataStorageConfiguration();

DataRegionConfiguration defaultRegion = new DataRegionConfiguration();
defaultRegion.setMetricsEnabled(false);

storageCfg.setDefaultDataRegionConfiguration(defaultRegion);

// Create a new data region.
DataRegionConfiguration regionCfg = new DataRegionConfiguration();

// Region name.
regionCfg.setName("myDataRegion");

// Disable metrics for this region.
regionCfg.setMetricsEnabled(false);

// Set the data region configuration.
storageCfg.setDataRegionConfigurations(regionCfg);

// Other properties

// Apply the new configuration.
cfg.setDataStorageConfiguration(storageCfg);

Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    DataStorageConfiguration = new DataStorageConfiguration
    {
        DefaultDataRegionConfiguration = new DataRegionConfiguration
        {
            Name = DataStorageConfiguration.DefaultDataRegionName,
            MetricsEnabled = false
        },
        DataRegionConfigurations = new[]
        {
            new DataRegionConfiguration
            {
                Name = "myDataRegion",
                MetricsEnabled = false
            }
        }
    }
};

var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Data region metrics can be enabled/disabled at runtime via the following JMX Bean:

**Data Region MBean**

```
org.apache:group=DataRegionMetrics,name=<Data Region Name>
```

## Disabling Persistence-related Metrics

Persistence-related metrics can be enabled/disabled in the data storage configuration:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">

          <!-- persistent storage metrics -->
            <property name="metricsEnabled" value="true"/>

            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="persistenceEnabled" value="true"/>

                    <!-- enable mertrics for the default data region -->
                    <!--property name="metricsEnabled" value="true"/-->
                    <!-- other properties -->
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

DataStorageConfiguration storageCfg = new DataStorageConfiguration();
storageCfg.setMetricsEnabled(false);

// Apply the new configuration.
cfg.setDataStorageConfiguration(storageCfg);

Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    DataStorageConfiguration = new DataStorageConfiguration
    {
        MetricsEnabled = false
    }
};

var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can enable or disable "Persistent Store" metrics at runtime via the following MXBean:

**Persistent Store MBean**

```
org.apache:group="Persistent Store",name=DataStorageMetrics
```

| Operation | Description |
|---|---|
| EnableMetrics | Enable persistent data storage metrics. |

## Configuring Metrics with MetricsMxBean

Some metric parameters, such as the time interval of a rate metric, can be changed at runtime through the `MetricsMxBean` MBean. Use it from any JMX-compliant tool or API.

**Metrics MBean**

```
org.apache:group=Metrics,name=MetricsMxBeanImpl
```

| Operation | Parameters | Description |
|---|---|---|
| `configureHitRateMetric` | `name`, `cfg` | Changes the time interval, in milliseconds, of a hit-rate metric. |
| `configureHistogramMetric` | `name`, `cfg` | Changes the bounds of a histogram metric. |
| `configureMaxValueMetric` | `name`, `cfg` | Changes the time interval, in milliseconds, of a maximum-value metric. |
| `resetMetrics` | `registry` | Resets all metrics in the specified metric registry. |

In the `configure*` operations, `name` is the full metric name, and `cfg` is the new value. For `configureHitRateMetric` and `configureMaxValueMetric`, the value is the time interval in milliseconds and must be positive. For `configureHistogramMetric`, the value is a non-empty array of bounds in ascending order.

A `configure*` operation changes the metric on all nodes in the cluster. If a metric with the specified name does not exist, the operation has no effect on it.

For example, `io.dataregion.{data_region_name}.AllocationRate` is a hit-rate metric that uses a 60-second interval by default, and `io.datastorage.CheckpointHistogram` is a histogram metric with the default bounds of 100, 500, 1000, 5000, and 30000 milliseconds. For the metric names, see the [metrics reference](../../reference/monitoring/generic-metrics.md).

### Configuring Maximum-Value Metrics

Some metrics, such as `communication.tcp.maxOutboundMessagesQueueSize` and `io.discovery.MaxMsgQueueSize`, report the maximum value observed over a time interval. The default interval is 60 seconds.

To change the interval, call the `configureMaxValueMetric` operation, where `name` is the full metric name and `cfg` is the new interval in milliseconds.

## Disabling Index Operation Metrics

GridGain collects [index operation metrics](../../reference/monitoring/generic-metrics.md#index-operations) for every SQL secondary index.
Because these metrics time individual B+tree page operations, they add overhead to index reads and writes.

The metrics are collected only for caches that have statistics enabled, so disabling statistics for a cache also stops them.
To switch the metrics off for all indexes on a node, regardless of the cache statistics setting, start the node with the `IGNITE_BPLUS_TREE_DISABLE_METRICS` system property set to `true`:

```shell
./ignite.sh -J-DIGNITE_BPLUS_TREE_DISABLE_METRICS=true
```

The default value is `false`.
The property is read when an index tree is created, so set it before you start the node.
See [Setting JVM Options](../cluster-configuration/starting-nodes.md#setting-jvm-options) to learn about different ways to set system properties.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
