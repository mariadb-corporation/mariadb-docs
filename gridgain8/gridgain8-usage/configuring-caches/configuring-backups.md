---
description: >-
  Configuring the number of partition backup copies for a GridGain cache and
  choosing between synchronous and asynchronous backup write modes.
---

# Configuring Partition Backups

Backup partitions are copies of primary partitions kept on other nodes so data survives a node failure. For the concept, see [Data Partitioning](../../architecture/data-modeling/data-partitioning.md#backup-partitions).

## Configuring Backups

To configure the number of backup copies, set the `backups` property in the cache configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <!-- Set the cache name. -->
            <property name="name" value="cacheName"/>
            <!-- Set the cache mode. -->
            <property name="cacheMode" value="PARTITIONED"/>
            <!-- Number of backup copies -->
            <property name="backups" value="1"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration();

cacheCfg.setName("cacheName");
cacheCfg.setCacheMode(CacheMode.PARTITIONED);
cacheCfg.setBackups(1);

IgniteConfiguration cfg = new IgniteConfiguration();

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
        new CacheConfiguration
        {
            Name = "myCache",
            CacheMode = CacheMode.Partitioned,
            Backups = 1
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

## Synchronous and Asynchronous Backups

You can configure whether updates of primary and backup copies should be synchronous or asynchronous by specifying a write synchronization mode.
You can set the write synchronization mode in the cache configuration:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <!-- Set the cache name. -->
            <property name="name" value="cacheName"/>
            <!-- Number of backup copies -->
            <property name="backups" value="1"/>

            <property name="writeSynchronizationMode" value="FULL_SYNC"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration();

cacheCfg.setName("cacheName");
cacheCfg.setBackups(1);
cacheCfg.setWriteSynchronizationMode(CacheWriteSynchronizationMode.FULL_SYNC);
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setCacheConfiguration(cacheCfg);

// Start the node.
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
            Name = "myCache",
            WriteSynchronizationMode = CacheWriteSynchronizationMode.FullSync,
            Backups = 1
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

The write synchronization mode can be set to the following values:

| Value | Description |
|---|---|
| FULL_SYNC | Client node will wait for write or commit to complete on all participating remote nodes (primary and backup). |
| FULL_ASYNC | Client node does not wait for responses from participating nodes, in which case remote nodes may get their state updated slightly after any of the cache write methods complete or after the Transaction.commit() method completes. |
| PRIMARY_SYNC | This is the default mode. Client node will wait for write or commit to complete on primary node, but will not wait for backups to be updated. |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
