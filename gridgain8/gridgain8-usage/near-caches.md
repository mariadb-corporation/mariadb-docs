---
description: >-
  Configuring near caches in GridGain to store recently or frequently accessed
  data on the local node, statically and dynamically.
---

# Near Caches

A near cache is a local cache that stores the most recently or most frequently accessed data on the local node. Let's say your application launches a client node and regularly queries reference data, such as country codes. Because client nodes do not store data, these queries always fetch data from the remote nodes. You can configure a near cache to keep the country codes on the local node while your application is running.

A near cache is configured for a specific regular cache and holds data for that cache only.

Near caches store data in the on-heap memory. You can configure the maximum size of the cache and eviction policy for near cache entries.

{% hint style="info" %}
Near caches are fully transactional and get updated or invalidated automatically whenever the data changes on the server nodes.
{% endhint %}

## Configuring Near Cache

You can configure a new near cache for a particular cache in the cache configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.CacheConfiguration">
    <property name="name" value="myCache"/>
    <property name="nearConfiguration">
        <bean class="org.apache.ignite.configuration.NearCacheConfiguration">
            <property name="nearEvictionPolicyFactory">
                <bean class="org.apache.ignite.cache.eviction.lru.LruEvictionPolicyFactory">
                    <property name="maxSize" value="100000"/>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// Create a near-cache configuration for "myCache".
NearCacheConfiguration<Integer, Integer> nearCfg = new NearCacheConfiguration<>();

// Use LRU eviction policy to automatically evict entries
// from near-cache whenever it reaches 100_000 entries
nearCfg.setNearEvictionPolicyFactory(new LruEvictionPolicyFactory<>(100_000));

CacheConfiguration<Integer, Integer> cacheCfg = new CacheConfiguration<Integer, Integer>("myCache");

cacheCfg.setNearConfiguration(nearCfg);

// Create a distributed cache on server nodes 
IgniteCache<Integer, Integer> cache = ignite.getOrCreateCache(cacheCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cacheCfg = new CacheConfiguration
{
    Name = "myCache",
    NearConfiguration = new NearCacheConfiguration
    {
        EvictionPolicy = new LruEvictionPolicy
        {
            MaxSize = 100_000
        }
    }
};

var cache = ignite.GetOrCreateCache<int, int>(cacheCfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Once configured in this way, the near cache is created on any node that requests data from the underlying cache, including both server nodes and client nodes. 
When you get an instance of the cache, as shown in the following example, the data requests go through the near cache.

{% code title="Java" %}
```java
IgniteCache<Integer, Integer> cache = ignite.cache("myCache");

int value = cache.get(1);
```
{% endcode %}

Most configuration parameters that are available in the cache configuration and make sense for the near cache are inherited from the underlying cache configuration.
For example, if the underlying cache has an [expiry policy](configuring-caches/expiry-policies.md) configured, entries in the near cache are expired based on the same policy.

The parameters listed in the table below are not inherited from the underlying cache configuration.

|Parameter | Description | Default Value|
|---|---|---|
|nearEvictionPolicy| The eviction policy for the near cache. See the [Eviction policies](memory-configuration/eviction-policies.md) page for details. | none|
|nearStartSize| The initial capacity of the near cache (the number of entries it can hold). | 375,000|

## Creating Near Cache Dynamically On Client Nodes

When making request from a client node to a cache that hasn't been configured to use a near cache and does not already have a local cache configured, you can create a near cache for that cache dynamically.
This increases performance by storing "hot" data locally on the client side. 
This cache is operable only on the node where it was created.

To do this, create a near cache configuration and pass it as an argument to the method that gets the instance of the cache.

{% tabs %}
{% tab title="Java" %}
```java
// Create a near-cache configuration
NearCacheConfiguration<Integer, String> nearCfg = new NearCacheConfiguration<>();

// Use LRU eviction policy to automatically evict entries
// from near-cache, whenever it reaches 100_000 in size.
nearCfg.setNearEvictionPolicyFactory(new LruEvictionPolicyFactory<>(100_000));

// get the cache named "myCache" and create a near cache for it
IgniteCache<Integer, String> cache = ignite.getOrCreateNearCache("myCache", nearCfg);

String value = cache.get(1);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start(new IgniteConfiguration
{
    DiscoverySpi = new TcpDiscoverySpi
    {
        LocalPort = 48500,
        LocalPortRange = 20,
        IpFinder = new TcpDiscoveryStaticIpFinder
        {
            Endpoints = new[]
            {
                "127.0.0.1:48500..48520"
            }
        }
    },
    CacheConfiguration = new[]
    {
        new CacheConfiguration {Name = "myCache"}
    }
});
var client = Ignition.Start(new IgniteConfiguration
{
    IgniteInstanceName = "clientNode",
    ClientMode = true,
    DiscoverySpi = new TcpDiscoverySpi
    {
        LocalPort = 48500,
        LocalPortRange = 20,
        IpFinder = new TcpDiscoveryStaticIpFinder
        {
            Endpoints = new[]
            {
                "127.0.0.1:48500..48520"
            }
        }
    }
});
// Create a near-cache configuration
var nearCfg = new NearCacheConfiguration
{
    // Use LRU eviction policy to automatically evict entries
    // from near-cache, whenever it reaches 100_000 in size.
    EvictionPolicy = new LruEvictionPolicy()
    {
        MaxSize = 100_000
    }
};

// get the cache named "myCache" and create a near cache for it
var cache = client.GetOrCreateNearCache<int, string>("myCache", nearCfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
