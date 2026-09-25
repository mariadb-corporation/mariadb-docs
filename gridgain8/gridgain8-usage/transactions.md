---
description: >-
  How to perform transactions in GridGain, including concurrency modes and
  isolation levels, deadlock detection, JTA, and handling failed transactions.
---

# Performing Transactions

## Overview

To enable transactional support for a specific cache, set the `atomicityMode` parameter in the cache configuration to `TRANSACTIONAL`.
See [Atomicity Modes](configuring-caches/atomicity-modes.md) for details.

Transactions allow you to group multiple cache operations, on one or more keys, into a single atomic transaction.
These operations are executed without any other interleaved operations on the specified keys, and either all succeed or all fail.
There is no partial execution of the operations.

You can enable transactions for a specific cache in the cache configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
        
    <property name="transactionConfiguration">
        <bean class="org.apache.ignite.configuration.TransactionConfiguration">
            <!--Set the timeout to 20 seconds-->
            <property name="TxTimeoutOnPartitionMapExchange" value="20000"/>
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

// Create a Transaction configuration
TransactionConfiguration txCfg = new TransactionConfiguration();

// Set the timeout to 20 seconds
txCfg.setTxTimeoutOnPartitionMapExchange(20000);

cfg.setTransactionConfiguration(txCfg);

// Start the node
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
        DefaultTimeoutOnPartitionMapExchange = TimeSpan.FromSeconds(20)
    }
};
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Executing Transactions

The key-value API provides an interface for starting and completing transactions as well as getting transaction-related metrics. The interface can be obtained from an instance of `Ignite`.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();

IgniteTransactions transactions = ignite.transactions();

try (Transaction tx = transactions.txStart()) {
    Integer hello = cache.get("Hello");

    if (hello == 1)
        cache.put("Hello", 11);

    cache.put("World", 22);

    tx.commit();
}
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
            var cfg = new IgniteConfiguration
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
                    new CacheConfiguration
                    {
                        Name = "cacheName",
                        AtomicityMode = CacheAtomicityMode.Transactional
                    }
                },
                TransactionConfiguration = new TransactionConfiguration
                {
                    DefaultTimeoutOnPartitionMapExchange = TimeSpan.FromSeconds(20)
                }
            };

            var ignite = Ignition.Start(cfg);
            var cache = ignite.GetCache<string, int>("cacheName");
            cache.Put("Hello", 1);
            var transactions = ignite.GetTransactions();

            using (var tx = transactions.TxStart())
            {
                int hello = cache.Get("Hello");

                if (hello == 1)
                {
                    cache.Put("Hello", 11);
                }

                cache.Put("World", 22);

                tx.Commit();
            }

            // Re-try the transaction a limited number of times
            var retryCount = 10;
            var retries = 0;

            // Start a transaction in the optimistic mode with the serializable isolation level
            while (retries < retryCount)
            {
                retries++;
                try
                {
                    using (var tx = ignite.GetTransactions().TxStart(TransactionConcurrency.Optimistic,
                        TransactionIsolation.Serializable))
                    {
                        // modify cache entries as part of this transaction.

                        // commit the transaction
                        tx.Commit();

                        // the transaction succeeded. Leave the while loop.
                        break;
                    }
                }
                catch (TransactionOptimisticException)
                {
                    // Transaction has failed. Retry.
                }

            }

            var intCache = ignite.GetOrCreateCache<int, int>("intCache");
            try
            {
                using (var tx = ignite.GetTransactions().TxStart(TransactionConcurrency.Pessimistic,
                    TransactionIsolation.ReadCommitted, TimeSpan.FromMilliseconds(300), 0))
                {
                    intCache.Put(1, 1);
                    intCache.Put(2, 1);
                    tx.Commit();
                }
            }
            catch (TransactionTimeoutException e)
            {
                Console.WriteLine(e.Message);
            }
            catch (TransactionDeadlockException e)
            {
                Console.WriteLine(e.Message);
            }

        }

        public static void TxTimeoutOnPme()
        {
            var cfg = new IgniteConfiguration
            {
                TransactionConfiguration = new TransactionConfiguration
                {
                    DefaultTimeoutOnPartitionMapExchange = TimeSpan.FromSeconds(20)
                }
            };
            Ignition.Start(cfg);
        }

        public static async Task TransactionAsyncExample()
        {
            using (var ignite = Ignition.Start(Util.getIngiteCfg()))
            {
                var cache = ignite.GetOrCreateCache<string, int>(
                    new CacheConfiguration("txCache")
                    {
                        AtomicityMode = CacheAtomicityMode.Transactional
                    });
                var transactions = ignite.GetTransactions();

                await using (var tx = transactions.TxStart())
                {
                    cache.Put("Hello", 11);
                    cache.Put("World", 22);

                    await tx.CommitAsync();
                }
            }
        }

        public static void DeadlockMetricsDemo(IIgnite ignite)
        {
            ITransactions transactions = ignite.GetTransactions();

            int deadlocks = transactions.GetMetrics().TxDeadlocks;

            Console.WriteLine(deadlocks);
        }
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
Transactions transactions = ignite.GetTransactions();

Transaction tx = transactions.TxStart();
int hello = cache.Get("Hello");

if (hello == 1)
    cache.Put("Hello", 11);

cache.Put("World", 22);

tx.Commit();
```
{% endtab %}
{% endtabs %}

## Closing a Transaction Asynchronously

In .NET, a transaction implements `IAsyncDisposable` in addition to `IDisposable`. Use an `await using` block to dispose of the transaction asynchronously: if the transaction is disposed without being committed, the rollback is sent to the cluster without blocking the calling thread.

{% tabs %}
{% tab title="C#/.NET" %}
```csharp
public static async Task TransactionAsyncExample()
{
    using (var ignite = Ignition.Start(Util.getIngiteCfg()))
    {
        var cache = ignite.GetOrCreateCache<string, int>(
            new CacheConfiguration("txCache")
            {
                AtomicityMode = CacheAtomicityMode.Transactional
            });
        var transactions = ignite.GetTransactions();

        await using (var tx = transactions.TxStart())
        {
            cache.Put("Hello", 11);
            cache.Put("World", 22);

            await tx.CommitAsync();
        }
    }
}
```
{% endtab %}

{% tab title="Java" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Concurrency Modes and Isolation Levels

Caches with the `TRANSACTIONAL` atomicity mode support both `OPTIMISTIC` and `PESSIMISTIC` concurrency modes for transactions. Concurrency mode determines when an entry-level transaction lock is acquired: at the time of data access or during the prepare phase. Locking prevents concurrent access to an object. For example, when you attempt to update a ToDo list item with pessimistic locking, the server places a lock on the object until you either commit or rollback the transaction and no other transaction or operation is allowed to update the same entry. Regardless of the concurrency mode used in a transaction, there exists a moment in time when all entries enlisted in the transaction are locked before the commit.

Isolation level defines how concurrent transactions 'see' and handle operations on the same keys. Ignite supports `READ_COMMITTED`, `REPEATABLE_READ` and `SERIALIZABLE` isolation levels.

All combinations of concurrency modes and isolation levels are allowed. Below is the description of the system behavior and the guarantees provided by each concurrency-isolation combination.

### Pessimistic Transactions

In `PESSIMISTIC` transactions, locks are acquired during the first read or write access (depending on the isolation level) and held by the transaction until it is committed or rolled back. In this mode locks are acquired on primary nodes first and then promoted to backup nodes during the prepare stage. The following isolation levels can be configured with the `PESSIMISTIC` concurrency mode:

- `READ_COMMITTED` - Data is read without a lock and is never cached in the transaction itself. The data may be read from a backup node if this is allowed in the cache configuration. In this isolation mode you can have the so-called Non-Repeatable Reads
- because a concurrent transaction can change the data when you are reading the data twice in your transaction. The lock is only acquired at the time of first write access (this includes `EntryProcessor` invocation). This means that an entry that has been read during the transaction may have a different value by the time the transaction is committed. No exception is thrown in this case.

- `REPEATABLE_READ` - Entry lock is acquired and data is fetched from the primary node on the first read or write access and stored in the local transactional map. All consecutive access to the same data is local and returns the last read or updated transaction value. This means no other concurrent transactions can make changes to the locked data, and you are getting Repeatable Reads for your transaction.

- `SERIALIZABLE` - In the `PESSIMISTIC` mode, this isolation level works the same way as `REPEATABLE_READ`.

Note that in the `PESSIMISTIC` mode, the order of locking is important. Moreover, locks are acquired sequentially and exactly in the specified order.

{% hint style="warning" %}
**Topology Change Restrictions**

Note that if at least one `PESSIMISTIC` transaction lock is acquired, it is impossible to change the cache topology until the transaction is committed or rolled back.
Therefore, you should avoid holding transaction locks for long periods of time.
{% endhint %}

### Optimistic Transactions

In `OPTIMISTIC` transactions, entry locks are acquired on primary nodes during the first phase of 2PC, at the `prepare` step, and then promoted to backup nodes and released once the transaction is committed. The locks are never acquired if you roll back the transaction and no commit attempt was made. The following isolation levels can be configured with the `OPTIMISTIC` concurrency mode:

- `READ_COMMITTED` - Changes that should be applied to the cache are collected on the originating node and applied upon the transaction commit. Transaction data is read without a lock and is never cached in the transaction. The data may be read from a backup node if this is allowed in the cache configuration. In this isolation you can have so-called Non-Repeatable Reads because a concurrent transaction can change the data when you are reading the data twice in your transaction. This mode combination does not check if the entry value has been modified since the first read or write access and never raises an optimistic exception.

- `REPEATABLE_READ` - Transactions at this isolation level work similar to `OPTIMISTIC` `READ_COMMITTED` transactions with only one difference: read values are cached on the originating node and all subsequent reads are guaranteed to be local. This mode combination does not check if the entry value has been modified since the first read or write access and never raises an optimistic exception.

- `SERIALIZABLE` - Stores an entry version upon first read access. Ignite fails a transaction at the commit stage if the Ignite engine detects that at least one of the entries used as part of the initiated transaction has been modified. In short, this means that if Ignite detects that there is a conflict at the commit stage of a transaction, it fails the transaction, throwing `TransactionOptimisticException` and rolling back any changes made. Make sure you handle this exception and retry the transaction.

{% tabs %}
{% tab title="Java" %}
```java
CacheConfiguration<Integer, String> cfg = new CacheConfiguration<>();
cfg.setAtomicityMode(CacheAtomicityMode.TRANSACTIONAL);
cfg.setName("myCache");
IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cfg);

// Re-try the transaction a limited number of times.
int retryCount = 10;
int retries = 0;

// Start a transaction in the optimistic mode with the serializable isolation
// level.
while (retries < retryCount) {
    retries++;
    try (Transaction tx = ignite.transactions().txStart(TransactionConcurrency.OPTIMISTIC,
            TransactionIsolation.SERIALIZABLE)) {
        // modify cache entries as part of this transaction.
        cache.put(1, "foo");
        cache.put(2, "bar");
        // commit the transaction
        tx.commit();

        // the transaction succeeded. Leave the while loop.
        break;
    } catch (TransactionOptimisticException e) {
        // Transaction has failed. Retry.
    }
}
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
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
        new CacheConfiguration
        {
            Name = "cacheName",
            AtomicityMode = CacheAtomicityMode.Transactional
        }
    },
    TransactionConfiguration = new TransactionConfiguration
    {
        DefaultTimeoutOnPartitionMapExchange = TimeSpan.FromSeconds(20)
    }
};

var ignite = Ignition.Start(cfg);
// Re-try the transaction a limited number of times
var retryCount = 10;
var retries = 0;

// Start a transaction in the optimistic mode with the serializable isolation level
while (retries < retryCount)
{
    retries++;
    try
    {
        using (var tx = ignite.GetTransactions().TxStart(TransactionConcurrency.Optimistic,
            TransactionIsolation.Serializable))
        {
            // modify cache entries as part of this transaction.

            // commit the transaction
            tx.Commit();

            // the transaction succeeded. Leave the while loop.
            break;
        }
    }
    catch (TransactionOptimisticException)
    {
        // Transaction has failed. Retry.
    }

}
```
{% endtab %}

{% tab title="C++" %}
```cpp
// Re-try the transaction a limited number of times.
int const retryCount = 10;
int retries = 0;
    
// Start a transaction in the optimistic mode with the serializable isolation level.
while (retries < retryCount)
{
    retries++;
    
    try
    {
        Transaction tx = ignite.GetTransactions().TxStart(
                TransactionConcurrency::OPTIMISTIC, TransactionIsolation::SERIALIZABLE);

        // commit the transaction
        tx.Commit();

        // the transaction succeeded. Leave the while loop.
        break;
    }
    catch (IgniteError e)
    {
        // Transaction has failed. Retry.
    }
}
```
{% endtab %}
{% endtabs %}

Another important point to note here is that a transaction fails even if an entry was read without being modified (`cache.put(...)`), since the value of the entry could be important to the logic within the initiated transaction.

Note that the key order is important for `READ_COMMITTED` and `REPEATABLE_READ` transactions since the locks are still acquired sequentially in these modes.

### Read Consistency

In order to achieve full read consistency in PESSIMISTIC mode, read-locks need to be acquired. This means that full consistency between reads in the PESSIMISTIC mode can be achieved only with PESSIMISTIC REPEATABLE_READ (or SERIALIZABLE) transactions.

When using OPTIMISTIC transactions, full read consistency can be achieved by disallowing potential conflicts between reads.
This behavior is provided by OPTIMISTIC SERIALIZABLE mode.
Note, however, that until the commit happens you can still read a partial transaction state, so the transaction logic must protect against it.
Only during the commit phase, in case of any conflict, a `TransactionOptimisticException` is thrown allowing you to retry the transaction.

{% hint style="warning" %}
If you are not using PESSIMISTIC REPEATABLE_READ or SERIALIZABLE transactions or OPTIMISTIC SERIALIZABLE transactions, then it is possible to see a partial transaction state. This means that if one transaction updates objects A and B, then another transaction may see the new value for A and the old value for B.
{% endhint %}

## Deadlock Detection

One major rule that you must follow when working with distributed transactions is that locks for the keys participating in a transaction must be acquired in the same order. Violating this rule can lead to a distributed deadlock.

GridGain does not avoid distributed deadlocks, but rather has built-in functionality that makes it easier to debug and fix such situations.

In the code snippet below, a transaction has been started with a timeout.
If the timeout expires, the deadlock detection procedure tries to find a possible deadlock that might have caused the timeout.
When the timeout expires, `TransactionTimeoutException` is generated and propagated to the application code as the cause of `CacheException` regardless of a deadlock.
However, if a deadlock is detected, the cause of the returned `TransactionTimeoutException` will be `TransactionDeadlockException` (at least for one transaction involved in the deadlock).

{% tabs %}
{% tab title="Java" %}
```java
CacheConfiguration<Integer, String> cfg = new CacheConfiguration<>();
cfg.setAtomicityMode(CacheAtomicityMode.TRANSACTIONAL);
cfg.setName("myCache");
IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cfg);

try (Transaction tx = ignite.transactions().txStart(TransactionConcurrency.PESSIMISTIC,
        TransactionIsolation.READ_COMMITTED, 300, 0)) {
    cache.put(1, "1");
    cache.put(2, "1");

    tx.commit();
} catch (CacheException e) {
    if (e.getCause() instanceof TransactionTimeoutException
            && e.getCause().getCause() instanceof TransactionDeadlockException)

        System.out.println(e.getCause().getCause().getMessage());
}
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
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
        new CacheConfiguration
        {
            Name = "cacheName",
            AtomicityMode = CacheAtomicityMode.Transactional
        }
    },
    TransactionConfiguration = new TransactionConfiguration
    {
        DefaultTimeoutOnPartitionMapExchange = TimeSpan.FromSeconds(20)
    }
};

var ignite = Ignition.Start(cfg);
var intCache = ignite.GetOrCreateCache<int, int>("intCache");
try
{
    using (var tx = ignite.GetTransactions().TxStart(TransactionConcurrency.Pessimistic,
        TransactionIsolation.ReadCommitted, TimeSpan.FromMilliseconds(300), 0))
    {
        intCache.Put(1, 1);
        intCache.Put(2, 1);
        tx.Commit();
    }
}
catch (TransactionTimeoutException e)
{
    Console.WriteLine(e.Message);
}
catch (TransactionDeadlockException e)
{
    Console.WriteLine(e.Message);
}

```
{% endtab %}

{% tab title="C++" %}
```cpp
try {
    Transaction tx = ignite.GetTransactions().TxStart(
        TransactionConcurrency::PESSIMISTIC, TransactionIsolation::READ_COMMITTED, 300, 0);
    cache.Put(1, 1);
    
    cache.Put(2, 1);
    
    tx.Commit();
}
catch (IgniteError& err)
{
    std::cout << "An error occurred: " << err.GetText() << std::endl;
    std::cin.get();
    return err.GetCode();
}
```
{% endtab %}
{% endtabs %}

The `TransactionDeadlockException` message contains useful information that can help you find the reason for the deadlock.

```shell
Deadlock detected:

K1: TX1 holds lock, TX2 waits lock.
K2: TX2 holds lock, TX1 waits lock.

Transactions:

TX1 [txId=GridCacheVersion [topVer=74949328, time=1463469328421, order=1463469326211, nodeOrder=1], nodeId=ad68354d-07b8-4be5-85bb-f5f2362fbb88, threadId=73]
TX2 [txId=GridCacheVersion [topVer=74949328, time=1463469328421, order=1463469326210, nodeOrder=1], nodeId=ad68354d-07b8-4be5-85bb-f5f2362fbb88, threadId=74]

Keys:

K1 [key=1, cache=default]
K2 [key=2, cache=default]
```

Deadlock detection is a multi-step procedure that can take many iterations depending on the number of nodes in the cluster, keys, and transactions that are involved in a possible deadlock. A deadlock detection initiator is a node where a transaction was started and failed with a `TransactionTimeoutException`.
This node investigates if a deadlock has occurred by exchanging requests/responses with other remote nodes, and then prepares a deadlock related report that is provided with the `TransactionDeadlockException`.
Each such message (request/response) is known as an iteration.

Since a transaction is not rolled back until the deadlock detection procedure is completed, it sometimes makes sense to tune the parameters (shown below), if you want to have a predictable time for a transaction's rollback.

- `IGNITE_TX_DEADLOCK_DETECTION_MAX_ITERS` - Specifies the maximum number of iterations for the deadlock detection procedure. If the value of this property is less than or equal to zero, deadlock detection is disabled (1000 by default);
- `IGNITE_TX_DEADLOCK_DETECTION_TIMEOUT` - Specifies the timeout for the deadlock detection mechanism (1 minute by default).

Note that if there are too few iterations, you may get an incomplete deadlock-report.

The number of transaction deadlocks detected on a node is exported as the `tx.txDeadlocks` metric
(see [Transactions](../reference/monitoring/generic-metrics.md#transactions)) and
can be read at run time through the transaction metrics API:

{% tabs %}
{% tab title="Java" %}
```java
IgniteTransactions transactions = ignite.transactions();

int deadlocks = transactions.metrics().txDeadlocks();
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
ITransactions transactions = ignite.GetTransactions();

int deadlocks = transactions.GetMetrics().TxDeadlocks;
```
{% endtab %}

{% tab title="C++" %}
```cpp
Transactions transactions = ignite.GetTransactions();

TransactionMetrics metrics = transactions.GetMetrics();
int32_t deadlocks = metrics.GetDeadlocks();
```
{% endtab %}
{% endtabs %}

## Deadlock-free Transactions

For `OPTIMISTIC` `SERIALIZABLE` transactions, locks are not acquired sequentially. In this mode, keys can be accessed in any order because transaction locks are acquired in parallel with an additional check allowing Ignite to avoid deadlocks.

We need to introduce some concepts in order to describe how locks in `SERIALIZABLE` transactions work.
In Ignite, each transaction is assigned a comparable version called `XidVersion`.
Upon transaction commit, each entry that is written in the transaction is assigned a new comparable version called `EntryVersion`.
An `OPTIMISTIC` `SERIALIZABLE` transaction with version `XidVersionA` fails with a `TransactionOptimisticException` if:

- There is an ongoing `PESSIMISTIC` or non-serializable `OPTIMISTIC` transaction holding a lock on an entry of the `SERIALIZABLE` transaction.
- There is another ongoing `OPTIMISTIC` `SERIALIZABLE` transaction with version `XidVersionB` such that `XidVersionB > XidVersionA` and this transaction holds a lock on an entry of the `SERIALIZABLE` transaction.
- By the time the `OPTIMISTIC` `SERIALIZABLE` transaction acquires all required locks, there exists an entry with the current version different from the observed version before commit.

{% hint style="info" %}
In a highly concurrent environment, optimistic locking might lead to a high transaction failure rate but pessimistic locking can lead to deadlocks if locks are acquired in a different order by transactions.

However, in a contention-free environment optimistic serializable locking may provide better performance for large transactions because the number of network trips depends only on the number of nodes that the transaction spans and does not depend on the number of keys in the transaction.
{% endhint %}

## Handling Failed Transactions

A transaction might fail with the following exceptions:

| Exception | Description | Solution|
|---|---|---|
| `CacheException` caused by `TransactionTimeoutException` | `TransactionTimeoutException` is generated if the transaction times out.  | To solve this exception, increase the timeout or make the transaction shorter.|
| `CacheException` caused by `TransactionTimeoutException`, which is caused by `TransactionDeadlockException` | This exception is thrown if the optimistic transaction fails for some reason. In most cases, this exception occurs when the data the transaction was trying to update was changed concurrently.   | Rerun the transaction.|
| `TransactionOptimisticException` | This exception is thrown if the optimistic transaction fails for some reason. In most of the scenarios, this exception occurs when the data the transaction was trying to update was changed concurrently. | Rerun the transaction.|
|`TransactionRollbackException` | This exception occurs when a transaction is rolled back (automatically or manually). In this case, the data is consistent. | Since the data is in a consistent state, you can retry the transaction.|
| `TransactionHeuristicException` | An unlikely exception that happens due to an unexpected internal or communication issue. The exception exists to report problematic scenarios that were not foreseen by the transactional subsystem and were not handled by it properly. | The data might not stay consistent if the exception occurs. Reload the data and report to Ignite development community.|

## JTA Transactions

GridGain supports Java Transactions API for XA resources.  To perform the transactions, you set up a transaction manager and then pass the manager to transaction configuration:

```java
public class Main {
    public static void main(String[] args) throws Exception {
        // Three steps to use JTA with Ignite
        // 1. Set up your TransactionManager of choice (here we use JOTM).
        // 2. Pass the TransactionManager to Ignite TransactionConfiguration.
        // 3. Obtain UserTransaction (usually from DI container) and use it to perform transactions.
        var jotm = new Jotm(true, false, new RmiLocalConfiguration());
        var txCfg = new TransactionConfiguration().setTxManagerFactory(jotm::getTransactionManager);
        var igniteCfg = new IgniteConfiguration().setTransactionConfiguration(txCfg);

        var ignite = Ignition.start(igniteCfg);
        igniteJtaDemo(ignite, jotm.getUserTransaction());
    }

    public static void igniteJtaDemo(Ignite ignite, UserTransaction userTx) throws Exception {
        var cacheCfg = new CacheConfiguration<Integer, Integer>("c")
                .setAtomicityMode(CacheAtomicityMode.TRANSACTIONAL);

        var cache = ignite.getOrCreateCache(cacheCfg);

        userTx.begin();
        cache.put(1, 1);
    }
}
```

The example above uses the following dependencies:

```xml
<dependency>
    <groupId>org.ow2.jotm</groupId>
    <artifactId>jotm-core</artifactId>
    <version>2.3.1-M1</version>
</dependency>

<dependency>
    <groupId>javax.resource</groupId>
    <artifactId>connector-api</artifactId>
    <version>1.5</version>
</dependency>

<dependency>
    <groupId>javax.transaction</groupId>
    <artifactId>jta</artifactId>
    <version>1.1</version>
</dependency>
```

## Long Running Transactions Termination

Some cluster events trigger partition map exchange process and data rebalancing within an Ignite cluster to ensure even data distribution cluster-wide. An example of one such event is the cluster-topology-change event that takes place whenever a new node joins the cluster or an existing one leaves it. Plus, every time a new cache or SQL table is created, the partition map exchange gets triggered.

When the partition map exchange starts, Ignite acquires a global lock at a particular stage. The lock can't be obtained while incomplete transactions are running in parallel. These transactions prevent the partition map exchange process from moving forward, thus blocking some operations such as a new node join process.

Use the `TransactionConfiguration.setTxTimeoutOnPartitionMapExchange(...)` method to set the maximum time allowed for your long-running transactions to block the partition map exchange. Once the timeout fires, all incomplete transactions are rolled back letting the partition map exchange proceed.

The example below shows how to configure the timeout:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
        
    <property name="transactionConfiguration">
        <bean class="org.apache.ignite.configuration.TransactionConfiguration">
            <!--Set the timeout to 20 seconds-->
            <property name="TxTimeoutOnPartitionMapExchange" value="20000"/>
        </bean>
    </property>

</bean>

```
{% endtab %}

{% tab title="Java" %}
```java
// Create a configuration
IgniteConfiguration cfg = new IgniteConfiguration();

// Create a Transaction configuration
TransactionConfiguration txCfg = new TransactionConfiguration();

// Set the timeout to 20 seconds
txCfg.setTxTimeoutOnPartitionMapExchange(20000);

cfg.setTransactionConfiguration(txCfg);

// Start the node
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    TransactionConfiguration = new TransactionConfiguration
    {
        DefaultTimeoutOnPartitionMapExchange = TimeSpan.FromSeconds(20)
    }
};
Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Also, consider using the `TransactionConfiguration.setDefaultTxTimeout(...)` method to modify the default transaction timeout in milliseconds. Initially, this value is defined by `DFLT_TRANSACTION_TIMEOUT`, which defaults to 0 - so there is no actual "default" timeout for transactions. 

Examples:

{% tabs %}
{% tab title="XML" %}
```xml
<bean id="grid.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">

        ...
        
        <property name="transactionConfiguration">
            <bean class="org.apache.ignite.configuration.TransactionConfiguration">
                <property name="defaultTxTimeout" value="30000"/>
            </bean>
        </property>
        
        ...
        
</bean>

```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration c = new IgniteConfiguration();
        TransactionConfiguration txCfg = c.getTransactionConfiguration();
        txCfg.setDefaultTxTimeout(30000)

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    TransactionConfiguration = new TransactionConfiguration
    {
        DefaultTimeout = TimeSpan.FromSeconds(30)
    }
};
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Monitoring Transactions

Refer to the [Monitoring Transactions](../reference/monitoring/jmx-metrics.md#monitoring-transactions) section for the list of metrics that expose some transaction-related information.

You can also use the [control script](../reference/cli-tool/README.md#transaction-management) to get information about, or cancel, specific transactions being executed in the cluster.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
