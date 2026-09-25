---
description: >-
  Configuring GridGain data regions to control RAM usage per cache, including the
  default region, custom regions, system regions, and cache warm-up strategy.
---

# Configuring Data Regions

## Overview

GridGain uses the concept of _data regions_ to control the amount of RAM available to a cache or a group of caches. A data region is a logical extendable area in RAM in which cached data resides. You can control the initial size of the region and the maximum size it can occupy. In addition to the size, data regions control [persistence settings](../../architecture/storage/native-persistence.md) for caches.

By default, there is one data region that can take up to 20% of RAM available to the node, and all caches you create are placed in that region; but you can add as many regions as you want. There are a couple of reasons why you may want to have multiple regions:

* Regions allow you to configure the amount of RAM available to a cache or number of caches.
* Persistence parameters are configured per region. If you want to have both in-memory only caches and the caches that store their content to disk, you need to configure two (or more) data regions with different persistence settings: one for in-memory caches and one for persistent caches.
* Some memory parameters, such as [eviction policies](eviction-policies.md), are configured per data region.

See the following section to learn how to change the parameters of the default data region or configure multiple data regions.

## Configuring Default Data Region

By default, a new cache is added to the default data region. If you want to change the properties of the default data region, you can do so in the data storage configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
            <!--
            Default memory region that grows endlessly. Any cache will be bound to this memory region
            unless another region is set in the cache's configuration.
            -->
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="name" value="Default_Region"/>
                    <!-- 100 MB memory region with disabled eviction. -->
                    <property name="initialSize" value="#{100 * 1024 * 1024}"/>
                </bean>
            </property>
            <property name="dataRegionConfigurations">
                <list>
                    <!--
                    40MB memory region with eviction enabled.
                    -->
                    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                        <property name="name" value="40MB_Region_Eviction"/>
                        <!-- Memory region of 20 MB initial size. -->
                        <property name="initialSize" value="#{20 * 1024 * 1024}"/>
                        <!-- Maximum size is 40 MB. -->
                        <property name="maxSize" value="#{40 * 1024 * 1024}"/>
                        <!-- Enabling eviction for this memory region. -->
                        <property name="pageEvictionMode" value="RANDOM_2_LRU"/>
                    </bean>
                </list>
            </property>
        </bean>
    </property>
    <property name="cacheConfiguration">
        <list>
            <!-- Cache that is mapped to a specific data region. -->
            <bean class="org.apache.ignite.configuration.CacheConfiguration">

                <property name="name" value="SampleCache"/>
                <!--
                Assigning the cache to the `40MB_Region_Eviction` region.
                -->
                <property name="dataRegionName" value="40MB_Region_Eviction"/>
            </bean>
        </list>
    </property>
    <!-- other properties -->
    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
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
            <!--
            Default memory region that grows endlessly. Any cache will be bound to this memory region
            unless another region is set in the cache's configuration.
            -->
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="name" value="Default_Region"/>
                    <!-- 100 MB memory region with disabled eviction. -->
                    <property name="initialSize" value="#{100 * 1024 * 1024}"/>
                </bean>
            </property>
```
{% endtab %}

{% tab title="Java" %}
```java
DataStorageConfiguration storageCfg = new DataStorageConfiguration();

DataRegionConfiguration defaultRegion = new DataRegionConfiguration();
defaultRegion.setName("Default_Region");
defaultRegion.setInitialSize(100 * 1024 * 1024);

storageCfg.setDefaultDataRegionConfiguration(defaultRegion);
// 40MB memory region with eviction enabled.
DataRegionConfiguration regionWithEviction = new DataRegionConfiguration();
regionWithEviction.setName("40MB_Region_Eviction");
regionWithEviction.setInitialSize(20 * 1024 * 1024);
regionWithEviction.setMaxSize(40 * 1024 * 1024);
regionWithEviction.setPageEvictionMode(DataPageEvictionMode.RANDOM_2_LRU);

storageCfg.setDataRegionConfigurations(regionWithEviction);

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setDataStorageConfiguration(storageCfg);

CacheConfiguration cache1 = new CacheConfiguration("SampleCache");
//this cache will be hosted in the "40MB_Region_Eviction" data region
cache1.setDataRegionName("40MB_Region_Eviction");

cfg.setCacheConfiguration(cache1);

// Start the node.
Ignite ignite = Ignition.start(cfg);

DataRegionConfiguration defaultRegion = new DataRegionConfiguration();
defaultRegion.setName("Default_Region");
defaultRegion.setInitialSize(100 * 1024 * 1024);

storageCfg.setDefaultDataRegionConfiguration(defaultRegion);
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
            Name = "Default_Region",
            InitialSize = 100 * 1024 * 1024
        }
    }
};

// Start the node.
var ignite = Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Adding Custom Data Regions

In addition to the default data region, you can add more data regions with custom settings.
In the following example, we configure a data region that can take up to 40 MB and uses the [Random-2-LRU](eviction-policies.md#random-2-lru) eviction policy.
Note that further below in the configuration, we create a cache that resides in the new data region.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
            <!--
            Default memory region that grows endlessly. Any cache will be bound to this memory region
            unless another region is set in the cache's configuration.
            -->
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="name" value="Default_Region"/>
                    <!-- 100 MB memory region with disabled eviction. -->
                    <property name="initialSize" value="#{100 * 1024 * 1024}"/>
                </bean>
            </property>
            <property name="dataRegionConfigurations">
                <list>
                    <!--
                    40MB memory region with eviction enabled.
                    -->
                    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                        <property name="name" value="40MB_Region_Eviction"/>
                        <!-- Memory region of 20 MB initial size. -->
                        <property name="initialSize" value="#{20 * 1024 * 1024}"/>
                        <!-- Maximum size is 40 MB. -->
                        <property name="maxSize" value="#{40 * 1024 * 1024}"/>
                        <!-- Enabling eviction for this memory region. -->
                        <property name="pageEvictionMode" value="RANDOM_2_LRU"/>
                    </bean>
                </list>
            </property>
        </bean>
    </property>
    <property name="cacheConfiguration">
        <list>
            <!-- Cache that is mapped to a specific data region. -->
            <bean class="org.apache.ignite.configuration.CacheConfiguration">

                <property name="name" value="SampleCache"/>
                <!--
                Assigning the cache to the `40MB_Region_Eviction` region.
                -->
                <property name="dataRegionName" value="40MB_Region_Eviction"/>
            </bean>
        </list>
    </property>
    <!-- other properties -->
    <!-- Explicitly configure TCP discovery SPI to provide list of initial nodes. -->
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
            <property name="dataRegionConfigurations">
                <list>
                    <!--
                    40MB memory region with eviction enabled.
                    -->
                    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                        <property name="name" value="40MB_Region_Eviction"/>
                        <!-- Memory region of 20 MB initial size. -->
                        <property name="initialSize" value="#{20 * 1024 * 1024}"/>
                        <!-- Maximum size is 40 MB. -->
                        <property name="maxSize" value="#{40 * 1024 * 1024}"/>
                        <!-- Enabling eviction for this memory region. -->
                        <property name="pageEvictionMode" value="RANDOM_2_LRU"/>
                    </bean>
                </list>
            </property>
            <!--
            Default memory region that grows endlessly. Any cache will be bound to this memory region
            unless another region is set in the cache's configuration.
            -->
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="name" value="Default_Region"/>
                    <!-- 100 MB memory region with disabled eviction. -->
                    <property name="initialSize" value="#{100 * 1024 * 1024}"/>
                </bean>
            </property>
    <property name="cacheConfiguration">
        <list>
            <!-- Cache that is mapped to a specific data region. -->
            <bean class="org.apache.ignite.configuration.CacheConfiguration">

                <property name="name" value="SampleCache"/>
                <!--
                Assigning the cache to the `40MB_Region_Eviction` region.
                -->
                <property name="dataRegionName" value="40MB_Region_Eviction"/>
            </bean>
        </list>
    </property>
```

For the full list of properties, refer to the `DataStorageConfiguration` javadoc.
{% endtab %}

{% tab title="Java" %}
```java
DataStorageConfiguration storageCfg = new DataStorageConfiguration();

DataRegionConfiguration defaultRegion = new DataRegionConfiguration();
defaultRegion.setName("Default_Region");
defaultRegion.setInitialSize(100 * 1024 * 1024);

storageCfg.setDefaultDataRegionConfiguration(defaultRegion);
// 40MB memory region with eviction enabled.
DataRegionConfiguration regionWithEviction = new DataRegionConfiguration();
regionWithEviction.setName("40MB_Region_Eviction");
regionWithEviction.setInitialSize(20 * 1024 * 1024);
regionWithEviction.setMaxSize(40 * 1024 * 1024);
regionWithEviction.setPageEvictionMode(DataPageEvictionMode.RANDOM_2_LRU);

storageCfg.setDataRegionConfigurations(regionWithEviction);

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setDataStorageConfiguration(storageCfg);

CacheConfiguration cache1 = new CacheConfiguration("SampleCache");
//this cache will be hosted in the "40MB_Region_Eviction" data region
cache1.setDataRegionName("40MB_Region_Eviction");

cfg.setCacheConfiguration(cache1);

// Start the node.
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
            Name = "Default_Region",
            InitialSize = 100 * 1024 * 1024
        },
        DataRegionConfigurations = new[]
        {
            new DataRegionConfiguration
            {
                Name = "40MB_Region_Eviction",
                InitialSize = 20 * 1024 * 1024,
                MaxSize = 40 * 1024 * 1024,
                PageEvictionMode = DataPageEvictionMode.Random2Lru
            },
            new DataRegionConfiguration
            {
                Name = "30MB_Region_Swapping",
                InitialSize = 15 * 1024 * 1024,
                MaxSize = 30 * 1024 * 1024,
                SwapPath = "/path/to/swap/file"
            }
        }
    }
};
Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## System Data Regions

GridGain comes preconfigured with 3 system data regions. These data regions are used by GridGain to store data required for cluster operations.

- `metastoreMemPlc` - a persistent data region that is used to store cluster metainformation.
- `sysMemPlc` - system data region that is used to store system caches. This region is persistent if at least one user-configured persistent data region exists.
- `volatileDsMemPlc` - an in-memory data region that stores volatile data structures ([lock](../data-structures/locks.md), [latch](../data-structures/countdownlatch.md), and [semaphore](../data-structures/semaphore.md)).

All three regions are sized by the system data region configuration. By default, each region starts at 40 MB and can grow to 100 MB.

The example below shows how you can configure the size of these data regions:

{% tabs %}
{% tab title="XML" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
           http://www.springframework.org/schema/beans
           http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="grid.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="dataStorageConfiguration">
            <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
                <property name="systemDataRegionConfiguration">
                    <bean class="org.apache.ignite.configuration.SystemDataRegionConfiguration">
                        <property name="initialSize" value="#{50 * 1024 * 1024}"/>
                        <property name="maxSize" value="#{200 * 1024 * 1024}"/>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</beans>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
DataStorageConfiguration storageCfg = new DataStorageConfiguration();

// Set system region sizes
storageCfg.setSystemDataRegionConfiguration(new SystemDataRegionConfiguration()
    .setInitialSize(50L * 1024 * 1024)
    .setMaxSize(200L * 1024 * 1024));

cfg.setDataStorageConfiguration(storageCfg);

// Start the node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    DataStorageConfiguration = new DataStorageConfiguration
    {
        SystemDataRegionConfiguration = new SystemDataRegionConfiguration
        {
            InitialSize = 50L * 1024 * 1024,
            MaxSize = 200L * 1024 * 1024,
        }
    }
};

Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
The `systemDataRegionConfiguration` property is available starting from GridGain 8.10.0. In earlier versions, set the sizes with the `systemRegionInitialSize` and `systemRegionMaxSize` properties of `DataStorageConfiguration`. Starting from GridGain 8.10.0, these properties are deprecated. They still work and delegate to the corresponding `systemDataRegionConfiguration` properties, so existing configurations keep working. Use `systemDataRegionConfiguration` in new configurations.
{% endhint %}

## Cache Warm-Up Strategy

The cache warm-up strategy provides an ability to load data from the disk to the node before it is joined to the cluster. This prevents performance loss when the node is restarted.

{% hint style="info" %}
The cache warm-up strategy is applicable only to the data regions. It can be configured both for all regions (by default) or for each region separately.
{% endhint %}

The warm-up strategy implies loading data into the region until it runs out of free space. GridGain plans partition loading based on index-partition priority within each cache group, then loads the planned partitions concurrently using a configurable number of worker threads.

### Java Configuration

To warm up all data regions, pass the configuration parameter `LoadAllWarmUpStrategy` to the `DataStorageConfiguration#setDefaultWarmUpConfiguration` as follows:

```java
setDefaultWarmUpConfiguration(loadAllWarmUpStrategy)
```

To warm up a specific data region, pass the configuration parameter `LoadAllWarmUpStrategy` to the `DataStorageConfiguration#setWarmUpConfiguration` as follows:

```java
setWarmUpConfiguration(loadAllWarmUpStrategy)
```

To control the number of threads used to load pages in parallel, use the `LoadAllWarmUpConfiguration#setThreads` method. The value must be positive. When not set, it defaults to `max(8, Runtime.getRuntime().availableProcessors())`.

```java
LoadAllWarmUpConfiguration loadAllWarmUpStrategy = new LoadAllWarmUpConfiguration()
    .setThreads(16);
```

To stop warming up all data regions, pass the configuration parameter `NoOpWarmUpStrategy` to the `DataStorageConfiguration#setDefaultWarmUpConfiguration` as follows:

```java
setDefaultWarmUpConfiguration(noOpWarmUpStrategy)
```

To stop warming up a specific data region, pass the configuration parameter `NoOpWarmUpStrategy` to the `DataStorageConfiguration#setWarmUpConfiguration` as follows:

```java
setWarmUpConfiguration(noOpWarmUpStrategy)
```

### XML Configuration

You can use the XML configuration to set up your warm-up strategy:

```xml
<property name="dataStorageConfiguration">
    <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
        <!-- Default policy for all regions -->
        <property name="defaultWarmUpConfiguration">
            <bean class="org.apache.ignite.configuration.LoadAllWarmUpConfiguration">
                <property name="threads" value="16"/>
            </bean>
        </property>
        <property name="defaultDataRegionConfiguration">
            <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                <!-- Default policy for all regions -->
                <property name="warmUpConfiguration">
                    <bean class="org.apache.ignite.configuration.LoadAllWarmUpConfiguration">
                        <property name="threads" value="16"/>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</property>
```

### Control Script Management

You can also stop the cache warming up process by using `control.sh` and JMX.

To stop the warming up using `control.sh`:

{% tabs %}
{% tab title="Linux" %}
```shell
control.sh --warm-up --stop --yes
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat --warm-up --stop --yes
```
{% endtab %}
{% endtabs %}

To stop the warming up using `JMX`, use the method below:

```java
org.apache.ignite.mxbean.WarmUpMXBean#stopWarmUp
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
