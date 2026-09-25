---
description: >-
  Using GridGain cache groups to share internal structures between caches,
  reducing memory usage and speeding up topology events in large deployments.
---

# Cache Groups

For each cache deployed in the cluster, there is always overhead: the cache is split into partitions whose state must be tracked on every cluster node.

If [Native Persistence](../../architecture/storage/native-persistence.md) is enabled, then for every partition there is an open file on the disk that GridGain actively writes to and reads from. Thus, the more caches and partitions you have:

* The more Java heap is occupied by partition maps. Every cache has its own partition map.
* The longer it might take for a new node to join the cluster.
* The longer it might take to initiate rebalancing if a node leaves the cluster.
* The more partition files are kept open and the worse the performance of the checkpointing might be.

Usually, you will not spot any of these problems for deployments with dozens or several hundreds of caches. However, when it comes to thousands the impact can be noticeable.

To avoid this impact, consider using cache groups. Caches within a single cache group share various internal structures such as partitions maps, thus boosting topology events processing and decreasing overall memory usage. Note that from the API standpoint, there is no difference whether a cache is a part of a group or not.

You can create a cache group by setting the `groupName` property of `CacheConfiguration`.
Here is an example of how to assign caches to a specific group:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <list>
            <!-- Partitioned cache for Persons data. -->
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
                <property name="name" value="Person"/>
                <property name="backups" value="1"/>
                <!-- Group the cache belongs to. -->
                <property name="groupName" value="group1"/>
            </bean>
            <!-- Partitioned cache for Organizations data. -->
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
                <property name="name" value="Organization"/>
                <property name="backups" value="1"/>
                <!-- Group the cache belongs to. -->
                <property name="groupName" value="group1"/>
            </bean>
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
// Defining cluster configuration.
IgniteConfiguration cfg = new IgniteConfiguration();

// Defining Person cache configuration.
CacheConfiguration<Integer, Person> personCfg = new CacheConfiguration<Integer, Person>("Person");

personCfg.setBackups(1);

// Group the cache belongs to.
personCfg.setGroupName("group1");

// Defining Organization cache configuration.
CacheConfiguration orgCfg = new CacheConfiguration("Organization");

orgCfg.setBackups(1);

// Group the cache belongs to.
orgCfg.setGroupName("group1");

cfg.setCacheConfiguration(personCfg, orgCfg);

// Starting the node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    CacheConfiguration = new[]
    {
        new CacheConfiguration
        {
            Name = "Person",
            Backups = 1,
            GroupName = "group1"
        },
        new CacheConfiguration
        {
            Name = "Organization",
            Backups = 1,
            GroupName = "group1"
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

In the above example, the `Person` and `Organization` caches belong to `group1`.

{% hint style="info" %}
**How are key-value pairs distinguished?**

If a cache is assigned to a cache group, its data is stored in shared partitions' internal structures.
Every key you put into the cache is enriched with the unique ID of the cache the key belongs to.
The ID is derived from the cache name.
This happens automatically and allows storing data of different caches in the same partitions and B+tree structures.
{% endhint %}

The reason for grouping caches is simple — if you decide to group 1000 caches, then you have 1000x fewer structures that store partitions' data, partition maps, and open partition files.

{% hint style="info" %}
**Should cache groups be used all the time?**

With all the benefits cache groups have, they might impact the performance of read operations and indexes lookups.
This is caused by the fact that all data and indexes get mixed in shared data structures (partition maps, B+trees), and it will take more time to query over them.

Thus, consider using the cache groups if you have a cluster of dozens and hundreds of nodes and caches, and you spot increased Java heap usage by internal structures, checkpointing performance drop, slow node connectivity to the cluster.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
