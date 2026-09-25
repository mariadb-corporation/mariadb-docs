---
description: >-
  How to set GridGain cache configuration parameters, with a configuration
  example, the full parameter reference, and cache templates.
---

# Overview

This chapter explains how you can set cache configuration parameters.
Once a cache is created, you cannot change its configuration parameters.

## Configuration Example

Below is an example of a cache configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>
            <property name="cacheMode" value="PARTITIONED"/>
            <property name="backups" value="2"/>
            <property name="rebalanceMode" value="SYNC"/>
            <property name="writeSynchronizationMode" value="FULL_SYNC"/>
            <property name="partitionLossPolicy" value="READ_ONLY_SAFE"/>
            <!-- Other parameters -->
        </bean>
    </property>
</bean>
```

For the full list of parameters, refer to the `CacheConfiguration` javadoc.

| Parameter | Description | Default Value |
|---|---|---|
| `name` | The cache name. | None. |
| `cacheMode` | The `cacheMode` parameter defines the way data is distributed in the cluster.<br><br>In the `PARTITIONED` mode (default), the overall data set is divided into partitions and all partitions are split between participating nodes in a balanced manner.<br><br>In the `REPLICATED` mode, all the data is replicated to every node in the cluster.<br><br>See the [Partitioned/Replicated Mode](../../architecture/data-modeling/data-partitioning.md#partitioned-replicated-mode) section for more details. | `PARTITIONED` |
| `writeSynchronizationMode` | Write synchronization mode. Refer to the [Configuring Partition Backups](configuring-backups.md) section. | `PRIMARY_SYNC` |
| `rebalanceMode` | This parameter controls the way the rebalancing process is performed. Possible values include:<br><br>`SYNC` -- Any requests to the cache's API are blocked until rebalancing is completed.<br>`ASYNC` (default) -- Rebalancing is performed in the background.<br>`NONE` -- Rebalancing is not triggered. | `ASYNC` |
| `backups` | The number of [backup partitions](../../architecture/data-modeling/data-partitioning.md#backup-partitions) for the cache. | `0` |
| `partitionLossPolicy` | [Partition loss policy](../../architecture/rebalancing/partition-loss-policy.md). | `IGNORE` |
| `readFromBackup` | Read requested cache entry from the backup partition if it is available on the local node instead of making a request to the primary partition (which can be located on the remote nodes).<br><br>**Note:** This property doesn't work with [SQL joins](../sql/distributed-joins.md). | `true` |
| `queryParallelism` | The number of threads in a single node to process a SQL query executed on the cache. Refer to the [Query Parallelism](../../ha-and-performance/performance-tuning/sql-tuning.md#query-parallelism) section in the Performance guide for more information. | 1 |
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration("myCache");

cacheCfg.setCacheMode(CacheMode.PARTITIONED);
cacheCfg.setBackups(2);
cacheCfg.setRebalanceMode(CacheRebalanceMode.SYNC);
cacheCfg.setWriteSynchronizationMode(CacheWriteSynchronizationMode.FULL_SYNC);
cacheCfg.setPartitionLossPolicy(PartitionLossPolicy.READ_ONLY_SAFE);

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setCacheConfiguration(cacheCfg);

// Start a node.
Ignition.start(cfg);
```

For the full list of parameters, refer to the `CacheConfiguration` javadoc.

| Parameter | Description | Default Value |
|---|---|---|
| `name` | The cache name. | None. |
| `cacheMode` | The `cacheMode` parameter defines the way data is distributed in the cluster.<br><br>In the `PARTITIONED` mode (default), the overall data set is divided into partitions and all partitions are split between participating nodes in a balanced manner.<br><br>In the `REPLICATED` mode, all the data is replicated to every node in the cluster.<br><br>See the [Partitioned/Replicated Mode](../../architecture/data-modeling/data-partitioning.md#partitioned-replicated-mode) section for more details. | `PARTITIONED` |
| `writeSynchronizationMode` | Write synchronization mode. Refer to the [Configuring Partition Backups](configuring-backups.md) section. | `PRIMARY_SYNC` |
| `rebalanceMode` | This parameter controls the way the rebalancing process is performed. Possible values include:<br><br>`SYNC` -- Any requests to the cache's API are blocked until rebalancing is completed.<br>`ASYNC` (default) -- Rebalancing is performed in the background.<br>`NONE` -- Rebalancing is not triggered. | `ASYNC` |
| `backups` | The number of [backup partitions](../../architecture/data-modeling/data-partitioning.md#backup-partitions) for the cache. | `0` |
| `partitionLossPolicy` | [Partition loss policy](../../architecture/rebalancing/partition-loss-policy.md). | `IGNORE` |
| `readFromBackup` | Read requested cache entry from the backup partition if it is available on the local node instead of making a request to the primary partition (which can be located on the remote nodes).<br><br>**Note:** This property doesn't work with [SQL joins](../sql/distributed-joins.md). | `true` |
| `queryParallelism` | The number of threads in a single node to process a SQL query executed on the cache. Refer to the [Query Parallelism](../../ha-and-performance/performance-tuning/sql-tuning.md#query-parallelism) section in the Performance guide for more information. | 1 |
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
            Backups = 2,
            RebalanceMode = CacheRebalanceMode.Sync,
            WriteSynchronizationMode = CacheWriteSynchronizationMode.FullSync,
            PartitionLossPolicy = PartitionLossPolicy.ReadOnlySafe
        }
    }
};
Ignition.Start(cfg);
```
{% endtab %}

{% tab title="SQL" %}
```sql
CREATE TABLE IF NOT EXISTS Person (
  id int,
  city_id int,
  name varchar,
  age int,
  company varchar,
  PRIMARY KEY (id, city_id)
) WITH "cache_name=myCache,template=partitioned,backups=2";
```

For the full list of parameters, refer to the [CREATE TABLE](../../reference/sql/ddl.md#create-table) section.
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Cache Templates

A cache template is an instance of `CacheConfiguration` that can be registered in the cluster and used later as a basis for creating new caches or SQL tables. A cache or table created from a template inherits all the properties of the template.

Templates can be used in many contexts: on servers, clients (thin and thick), in SQL (e.g., CREATE TABLE), in commands such as `createCache` and `getOrCreateCache`, as well as in the REST API calls. For example, thin clients and SQL do not support some cache configuration properties, and cache templates can be used to work around this limitation.

To create a template, define a cache configuration and add it to the `Ignite` instance, as shown below. If you want do define a cache template in the XML configuration file, you must add an asterisk to the template's name. This is required to indicate that the configuration is a template and not an actual cache.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <list>
            <bean abstract="true" class="org.apache.ignite.configuration.CacheConfiguration" id="cache-template-bean">
                <!-- when you create a template via XML configuration, you must add an asterisk to the name of the template -->
                <property name="name" value="myCacheTemplate*"/>
                <property name="cacheMode" value="PARTITIONED"/>
                <property name="backups" value="2"/>
                <!-- Other cache parameters -->
            </bean>
        </list>
    </property>
</bean>

```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration igniteCfg = new IgniteConfiguration();
try (Ignite ignite = Ignition.start(igniteCfg)) {
    CacheConfiguration cacheCfg = new CacheConfiguration("myCacheTemplate");

    cacheCfg.setBackups(2);
    cacheCfg.setCacheMode(CacheMode.PARTITIONED);

    // Register the cache template 
    ignite.addCacheConfiguration(cacheCfg);
}
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();

var cfg = new CacheConfiguration
{
    Name = "myCacheTemplate*",
    CacheMode = CacheMode.Partitioned,
    Backups = 2
};

ignite.AddCacheConfiguration(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Once the cache template is registered in the cluster, as shown in the code snippet above, you can use it to create another cache with the same configuration.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
