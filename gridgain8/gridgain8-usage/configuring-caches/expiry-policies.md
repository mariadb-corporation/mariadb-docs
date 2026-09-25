---
description: >-
  Configuring expiry policies for GridGain caches, including eager TTL and
  resetting the expiration timeout with the touch operation.
---

# Expiry Policies

## Overview

Expiry Policy specifies the amount of time that must pass before an entry is considered expired. Time can be counted from creation, last access, or modification time.

Depending on the memory configuration, the expiration policies remove entries from either RAM or disk:

* **In-Memory Mode** (data is stored solely in RAM): expired entries are purged from RAM.
* **In-Memory + Native persistence**: expired entries are removed from both memory and disk. Note that expiry policies  remove entries from the partition files on disk without freeing up space. The space is reused to write subsequent entries.
* **In-Memory + External Storage**: expired entries are removed from memory only (in GridGain) and left untouched in the external storage (RDBMS, NoSQL, and other databases).
* **In-Memory + Swap**: expired entries are removed from both RAM and swap files.

To set up an expiration policy, you can use any of the standard implementations of `javax.cache.expiry.ExpiryPolicy` or implement your own.

Unless [Eager TTL](#eager-ttl) is enabled, expired entries are made unavailable, but are not physically removed until they are touched by an operation, or an operation overwrites the entry in the cache.

{% hint style="info" %}
SQL SELECT operations to not reset expiration policy timeout. Entries only touched by SELECT operations may be removed due to TTL. Use the `cache.touch()` method to reset the timeout.
{% endhint %}

## Configuration

Below is an example expiry policy configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.CacheConfiguration">
    <property name="name" value="myCache"/>
    <property name="expiryPolicyFactory">
        <bean class="javax.cache.expiry.CreatedExpiryPolicy" factory-method="factoryOf">
            <constructor-arg>
                <bean class="javax.cache.expiry.Duration">
                    <constructor-arg value="MINUTES"/>
                    <constructor-arg value="5"/>
                </bean>
            </constructor-arg>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration<Integer, String> cfg = new CacheConfiguration<Integer, String>();
cfg.setName("myCache");
cfg.setExpiryPolicyFactory(CreatedExpiryPolicy.factoryOf(Duration.FIVE_MINUTES));
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
class ExpiryPolicyFactoryImpl : IFactory<IExpiryPolicy>
{
    public IExpiryPolicy CreateInstance()
    {
        return new ExpiryPolicy(TimeSpan.FromMilliseconds(100), TimeSpan.FromMilliseconds(100),
            TimeSpan.FromMilliseconds(100));
    }
}

public static void Example()
{
    var cfg = new CacheConfiguration
    {
        Name = "cache_name",
        ExpiryPolicyFactory = new ExpiryPolicyFactoryImpl()
    };
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

You can also change or set Expiry Policy for individual cache operations. This policy is used for each operation invoked on the returned cache instance.

```java
CacheConfiguration<Integer, String> cacheCfg = new CacheConfiguration<Integer, String>("myCache");

ignite.createCache(cacheCfg);

IgniteCache cache = ignite.cache("myCache")
        .withExpiryPolicy(new CreatedExpiryPolicy(new Duration(TimeUnit.MINUTES, 5)));

// if the cache does not contain key 1, the entry will expire after 5 minutes
cache.put(1, "first value");
```

## Eager TTL

Eager TTL prioritizes proactively removing expired data, instead of waiting for the entry to be touched. The expired entries are made unavailable as soon as TTL expires, and are quickly cleaned up as well. On average, enabling eager TTL means that individual operations will be faster, but the extra workload is generated during cleanup.

If there is at least one cache with eager TTL enabled, GridGain creates one thread that is used to clean up expired entries  in the background, active only for caches with eager TTL enabled. Every 500ms, the thread will perform a batch cleanup. Additionally, some expired entries will be removed after each operation on the cache to avoid overloading the cleanup process. By default, 5 entries are removed, this amount can be configured by using the `IGNITE_TTL_EXPIRE_BATCH_SIZE` property.

Eager TTL can be enabled or disabled via the `CacheConfiguration.eagerTtl` property (the default value is `true`):

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.CacheConfiguration">
    <property name="eagerTtl" value="true"/>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration<Integer, String> cfg = new CacheConfiguration<Integer, String>();
cfg.setName("myCache");

cfg.setEagerTtl(true);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new CacheConfiguration
{
    Name = "cache_name",
    EagerTtl = true
};
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Resetting Expiration Timeout

{% hint style="warning" %}
Touch operation is an experimental feature and can be changed in future releases.
{% endhint %}

You can reset expiration timeout for the cache without loading it into memory by using the `cache.touch()` method:

{% code title="Java" %}
```java
Ignite ignite = Ignition.ignite();

IgniteCache<CityKey, City> cache = ignite.cache("City").withExpiryPolicy(new TouchedExpiryPolicy(new Duration(SECONDS, 5)));

CityKey key = new CityKey(5, "NLD");

// Reset expiration timeout
cache.touch(key);
```
{% endcode %}

Like with most cache operations, touch can also be performed asynchronously by using the cache.touchAsync() method:

{% code title="Java" %}
```java
Ignite ignite = Ignition.ignite();

IgniteCache<CityKey, City> cache = ignite.cache("City").withExpiryPolicy(new TouchedExpiryPolicy(new Duration(SECONDS, 5)));

CityKey key = new CityKey(5, "NLD");

IgniteFuture<Boolean> fut = cache.touchAsync(key);

fut.listen(f -> System.out.println("Time-to-live value was " + (f.get() ? "successfully" : "not") + " updated."));
```
{% endcode %}

Currently, these methods have the following limitations:

- Touch operations are only supported for [Atomic caches](atomicity-modes.md).
- Touch operation is guaranteed to omit loading the entry into memory for in-memory clusters only.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
