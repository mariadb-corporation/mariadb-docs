---
description: >-
  Enabling on-heap caching in GridGain and configuring on-heap eviction policies
  — LRU, FIFO, and Sorted — to manage the on-heap cache size.
---

# On-Heap Caching

GridGain uses off-heap memory to allocate memory regions outside of Java heap. However, you can enable on-heap caching  by setting `CacheConfiguration.setOnheapCacheEnabled(true)`.

On-heap caching is useful in scenarios when you do a lot of cache reads on server nodes that work with cache entries in [binary form](../../architecture/data-modeling/introduction.md#binary-object-format) or invoke cache entries' deserialization. For instance, this might happen when a distributed computation or deployed service gets some data from caches for further processing.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>
            <property name="onheapCacheEnabled" value="true"/>
        </bean>
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
CacheConfiguration cfg = new CacheConfiguration();
cfg.setName("myCache");
cfg.setOnheapCacheEnabled(true);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new CacheConfiguration
{
    Name = "myCache",
    OnheapCacheEnabled = true
};
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Configuring Eviction Policy

When on-heap caching is enabled, you can use one of the on-heap eviction policies to manage the growing on-heap cache.

Eviction policies control the maximum number of elements that can be stored in a cache's on-heap memory. Whenever the maximum on-heap cache size is reached, entries are evicted from Java heap.

{% hint style="info" %}
The on-heap eviction policies remove the cache entries from Java heap only. The entries stored in the off-heap region of the memory are not affected.
{% endhint %}

Some eviction policies support batch eviction and eviction by memory size limit. If batch eviction is enabled, then eviction starts when cache size becomes `batchSize` elements greater than the maximum cache size. In this case, `batchSize` entries are evicted. If eviction by memory size limit is enabled, then eviction starts when the size of cache entries in bytes becomes greater than the maximum memory size.

{% hint style="info" %}
Batch eviction is supported only if maximum memory limit isn't set.
{% endhint %}

Eviction policies are pluggable and are controlled via the `EvictionPolicy` interface. The implementation of eviction policy is notified of every cache change and defines the algorithm of choosing the entries to evict from the on-heap cache.

### Least Recently Used (LRU)

LRU eviction policy, based on the [Least Recently Used (LRU)](http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used) algorithm, ensures that the least recently used entry (i.e. the entry that has not been touched for the longest time) gets evicted first.

{% hint style="info" %}
LRU eviction policy nicely fits most of the use cases for on-heap caching. Use it whenever in doubt.
{% endhint %}

This eviction policy can be enabled in the cache configuration as shown in the example below. It supports batch eviction and eviction by memory size limit.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.cache.CacheConfiguration">
  <property name="name" value="myCache"/>

  <!-- Enabling on-heap caching for this distributed cache. -->
  <property name="onheapCacheEnabled" value="true"/>

  <property name="evictionPolicy">
    <!-- LRU eviction policy. -->
    <bean class="org.apache.ignite.cache.eviction.lru.LruEvictionPolicy">
        <!-- Set the maximum cache size to 1 million (default is 100,000). -->
      <property name="maxSize" value="1000000"/>
    </bean>
  </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration();

cacheCfg.setName("cacheName");

// Enabling on-heap caching for this distributed cache.
cacheCfg.setOnheapCacheEnabled(true);

// Set the maximum cache size to 1 million (default is 100,000).
cacheCfg.setEvictionPolicyFactory(() -> new LruEvictionPolicy(1000000));

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setCacheConfiguration(cacheCfg);
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
            Name = "cacheName",
            OnheapCacheEnabled = true,
            EvictionPolicy = new LruEvictionPolicy
            {
                MaxSize = 100000
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

### First In First Out (FIFO)

FIFO eviction policy, based on the [First-In-First-Out (FIFO)](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) algorithm, ensures that the entry that has been in the on-heap cache for the longest time is evicted first.
It is different from `LruEvictionPolicy` because it ignores the order in which the entries are accessed.

This eviction policy can be enabled in the cache configuration as shown in the example below.
It supports batch eviction and eviction by memory size limit.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.cache.CacheConfiguration">
  <property name="name" value="myCache"/>

  <!-- Enabling on-heap caching for this distributed cache. -->
  <property name="onheapCacheEnabled" value="true"/>

  <property name="evictionPolicy">
    <!-- FIFO eviction policy. -->
    <bean class="org.apache.ignite.cache.eviction.fifo.FifoEvictionPolicy">
        <!-- Set the maximum cache size to 1 million (default is 100,000). -->
      <property name="maxSize" value="1000000"/>
    </bean>
  </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration();

cacheCfg.setName("cacheName");

// Enabling on-heap caching for this distributed cache.
cacheCfg.setOnheapCacheEnabled(true);

// Set the maximum cache size to 1 million (default is 100,000).
cacheCfg.setEvictionPolicyFactory(() -> new FifoEvictionPolicy(1000000));

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setCacheConfiguration(cacheCfg);
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
            Name = "cacheName",
            OnheapCacheEnabled = true,
            EvictionPolicy = new FifoEvictionPolicy
            {
                MaxSize = 100000
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

### Sorted

Sorted eviction policy is similar to FIFO eviction policy with the difference that entries' order is defined by default or by a user defined comparator and ensures that the minimal entry (i.e. the entry that has an integer key with the smallest value) gets evicted first.

The default comparator uses cache entries' keys for comparison that imposes a requirement for keys to implement the `Comparable` interface. You can provide your own comparator implementation which can use keys, values, or both for entries comparison.

Enable sorted eviction policy in the cache configuration as shown below. It supports batch eviction and eviction by memory size limit.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.cache.CacheConfiguration">
  <property name="name" value="myCache"/>

  <!-- Enabling on-heap caching for this distributed cache. -->
  <property name="onheapCacheEnabled" value="true"/>

  <property name="evictionPolicy">
    <!-- Sorted eviction policy. -->
    <bean class="org.apache.ignite.cache.eviction.sorted.SortedEvictionPolicy">
      <!--
      Set the maximum cache size to 1 million (default is 100,000)
      and use default comparator.
      -->
      <property name="maxSize" value="1000000"/>
    </bean>
  </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration();

cacheCfg.setName("cacheName");

// Enabling on-heap caching for this distributed cache.
cacheCfg.setOnheapCacheEnabled(true);

// Set the maximum cache size to 1 million (default is 100,000).
cacheCfg.setEvictionPolicyFactory(() -> new SortedEvictionPolicy(1000000));

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setCacheConfiguration(cacheCfg);
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
