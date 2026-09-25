---
description: >-
  How GridGain uses operating-system swapping to move in-memory data to disk as
  an extension of RAM, and how to enable it in the data region configuration.
---

# Swapping

## Overview

When using a pure in-memory storage, it is possible that the size of data loaded into a node exceeds the physical RAM size, leading to out of memory errors (OOMEs).
If you do not want to use the native persistence or an external storage, you can enable swapping, in which case the in-memory data is moved to the swap space located on disk.
Please note that GridGain does not provide its own implementation of swap space.
Instead, it takes advantage of the swapping functionality provided by the operating system (OS).

When swap space is enabled, GridGain stores data in memory-mapped files (MMF) whose content is swapped to disk by the OS according to the current RAM consumption;
however, in that scenario the data access time is longer.
Moreover, there are no data durability guarantees.
Which means that the data from the swap space is available only as long as the node is alive.
Once the node where the swap space exists shuts down, the data is lost.
Therefore, you should use swap space as an extension to RAM only to give yourself enough time to add more nodes to the cluster in order to re-distribute data and avoid OOMEs which might happen if the cluster is not scaled in time.

{% hint style="warning" %}
Since swap space is located on disk, it should not be considered as a replacement to native persistence.
Data from the swap space is available as long as the node is active. Once the node shuts down, the data lost.
To ensure that data is available at all times, you should either enable [native persistence](native-persistence.md) or use an [external storage](../../gridgain8-usage/persistence/external-storage.md).
{% endhint %}

## Enabling Swapping

Data Region `maxSize` defines the total `maxSize` of the region.
You will get out of memory errors if your data size exceeds `maxSize` and neither native persistence nor an external database is used.
To avoid this situation with the swapping capabilities, you need to:

- Set `maxSize` to a value that is bigger than the total RAM size. In this case, the OS takes care of the swapping.
- Enable swapping in the data region configuration, as shown below.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <!-- Durable memory configuration. -->
    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
            <property name="dataRegionConfigurations">
                <list>
                    <!--
                    Defining a data region that will consume up to 5 GB of RAM
                    with swap enabled.
                    -->
                    <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                        <!-- Custom region name. -->
                        <property name="name" value="5GB_Region"/>
                        <!-- 100 MB initial size. -->
                        <property name="initialSize" value="#{100L * 1024 * 1024}"/>
                        <!-- Setting region max size equal to physical RAM size(5 GB). -->
                        <property name="maxSize" value="#{5L * 1024 * 1024 * 1024}"/>
                        <!-- Enabling swap space for the region. -->
                        <property name="swapPath" value="/path/to/some/directory"/>
                    </bean>
                </list>
            </property>
        </bean>
    </property>
    <!-- Other configurations. -->
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
// Node configuration.
IgniteConfiguration cfg = new IgniteConfiguration();

// Durable Memory configuration.
DataStorageConfiguration storageCfg = new DataStorageConfiguration();

// Creating a new data region.
DataRegionConfiguration regionCfg = new DataRegionConfiguration();

// Region name.
regionCfg.setName("5GB_Region");

// Setting initial RAM size.
regionCfg.setInitialSize(100L * 1024 * 1024);

// Setting region max size equal to physical RAM size(5 GB)
regionCfg.setMaxSize(5L * 1024 * 1024 * 1024);
                
// Enable swap space.
regionCfg.setSwapPath("/path/to/some/directory");
                
// Setting the data region configuration.
storageCfg.setDataRegionConfigurations(regionCfg);
                
// Applying the new configuration.
cfg.setDataStorageConfiguration(storageCfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    DataStorageConfiguration = new DataStorageConfiguration
    {
        DataRegionConfigurations = new[]
        {
            new DataRegionConfiguration
            {
                Name = "5GB_Region",
                InitialSize = 100L * 1024 * 1024,
                MaxSize = 5L * 1024 * 1024 * 1024,
                SwapPath = "/path/to/some/directory"
            }
        }
    }
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
