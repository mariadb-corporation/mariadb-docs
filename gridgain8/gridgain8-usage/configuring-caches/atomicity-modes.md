---
description: >-
  GridGain cache atomicity modes — ATOMIC, TRANSACTIONAL, and
  TRANSACTIONAL_SNAPSHOT — and how to enable transactional support for a cache.
---

# Atomicity Modes

By default, a cache supports only atomic operations, and bulk operations such as `putAll()` or `removeAll()` are executed as a sequence of individual puts and removes.
You can enable transactional support and group multiple cache operations, on one or more keys, into a single atomic transaction.
These operations are executed without any other interleaved operations on the specified keys, and either all succeed or all fail.
There is no partial execution of the operations.

To enable support for transactions for a cache, set the `atomicityMode` parameter in the cache configuration to `TRANSACTIONAL`.

{% hint style="warning" %}
If you configure multiple caches within one [cache group](cache-groups.md), the caches must be either all atomic, or all transactional. You cannot have both TRANSACTIONAL and ATOMIC caches in one cache group.
{% endhint %}

GridGain supports 3 atomicity modes, which are described in the following table.

| Atomicity Mode | Description |
|---|---|
| ATOMIC | The default mode. All operations are performed atomically, one at a time. Transactions are not supported. The `ATOMIC` mode provides better performance by avoiding transactional locks, whilst providing data atomicity and consistency for each single operation. Bulk writes, such as the `putAll(...)` and `removeAll(...)` methods, are not executed in one transaction and can partially fail. If this happens, a `CachePartialUpdateException` is thrown and contains a list of keys for which the update failed. |
| TRANSACTIONAL | Enables support for ACID-compliant transactions executed via the key-value API. SQL transactions are not supported. Transactions in this mode can have different [concurrency modes and isolation levels](../transactions.md#concurrency-modes-and-isolation-levels). Enable this mode only if you need support for ACID-compliant operations. For more information about transactions, see [Performing Transactions](../transactions.md).<br><br>**Note — Performance Considerations:** The `TRANSACTIONAL` mode adds a performance cost to cache operations and should be enabled only if you need transactions. |
| TRANSACTIONAL_SNAPSHOT | An experimental mode that implements multiversion concurrency control (MVCC) and supports both key-value transactions and SQL transactions. See [Multiversion Concurrency Control](../../architecture/mvcc.md) for details about and limitations of this mode.<br><br>**Warning:** MVCC implementation is in beta and is not ready for production use. |

You can enable transactions for a cache in the cache configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>

            <property name="atomicityMode" value="TRANSACTIONAL"/>
        </bean>
    </property>

    <!-- Optional transaction configuration. -->
    <property name="transactionConfiguration">
        <bean class="org.apache.ignite.configuration.TransactionConfiguration">
            <!-- Configure TM lookup here. -->
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
CacheConfiguration cacheCfg = new CacheConfiguration();

cacheCfg.setName("cacheName");

cacheCfg.setAtomicityMode(CacheAtomicityMode.TRANSACTIONAL);

IgniteConfiguration cfg = new IgniteConfiguration();

cfg = Util.getIgniteCfg();
cfg.setCacheConfiguration(cacheCfg);

// Optional transaction configuration. Configure TM lookup here.
TransactionConfiguration txCfg = new TransactionConfiguration();

cfg.setTransactionConfiguration(txCfg);

// Start a node
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    CacheConfiguration = new[]
    {
        new CacheConfiguration("txCache")
        {
            AtomicityMode = CacheAtomicityMode.Transactional
        }
    },
    TransactionConfiguration = new TransactionConfiguration
    {
        DefaultTransactionConcurrency = TransactionConcurrency.Optimistic
    }
};
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
