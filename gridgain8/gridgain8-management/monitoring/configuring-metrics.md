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

## Disabling Data Region Metrics

Data region metrics expose information about data regions, including memory and storage size of the region.
Disable data region metrics for every region you do not need the metrics for.

Data region metrics can be disabled in two ways:

* in the [configuration of the region](../../gridgain8-usage/memory-configuration/data-regions.md)
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
See [Setting JVM Options](../../gridgain8-usage/starting-nodes.md#setting-jvm-options) to learn about different ways to set system properties.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
