---
description: >-
  Perform basic GridGain cache operations, including creating and destroying caches, atomic operations, asynchronous execution, and resource injection.
---

# Basic Cache Operations

{% hint style="info" %}
To preclude issues with cache names, explicitly prohibit slashes, backslashes, line separators, and null characters in these names by setting the `IGNITE_VALIDATE_CACHE_NAMES` system property to `true`.
{% endhint %}

## Getting an Instance of a Cache

All operations on a cache are performed through an instance of `IgniteCache`.
You can obtain `IgniteCache` for an existing cache, or you can create a cache dynamically.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();

// Obtain an instance of the cache named "myCache".
// Note that different caches may have different generics.
IgniteCache<Integer, String> cache = ignite.cache("myCache");
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
IIgnite ignite = Ignition.Start();

// Obtain an instance of cache named "myCache".
// Note that generic arguments are only for your convenience.
// You can work with any cache in terms of any generic arguments.
// However, attempt to retrieve an entry of incompatible type
// will result in exception.
ICache<int, string> cache = ignite.GetCache<int, string>("myCache");
```
{% endtab %}
{% tab title="C++" %}
```cpp
IgniteConfiguration cfg;
cfg.springCfgPath = "/path/to/configuration.xml";

Ignite ignite = Ignition::Start(cfg);

// Obtain instance of cache named "myCache".
// Note that different caches may have different generics.
Cache<int32_t, std::string> cache = ignite.GetCache<int32_t, std::string>("myCache");
```
{% endtab %}
{% endtabs %}

## Creating Caches Dynamically

You can also create a cache dynamically:

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();

CacheConfiguration<Integer, String> cfg = new CacheConfiguration<>();

cfg.setName("myNewCache");
cfg.setAtomicityMode(CacheAtomicityMode.TRANSACTIONAL);

// Create a cache with the given name if it does not exist.
IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cfg);
```

Refer to the [Cache Configuration](../configuring-caches/configuration-overview.md) section for the list of cache parameters.
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
IIgnite ignite = Ignition.Start();

// Create cache with given name, if it does not exist.
var cache = ignite.GetOrCreateCache<int, string>("myNewCache");
```
{% endtab %}
{% tab title="C++" %}
```cpp
IgniteConfiguration cfg;
cfg.springCfgPath = "/path/to/configuration.xml";

Ignite ignite = Ignition::Start(cfg);

// Create a cache with the given name, if it does not exist.
Cache<int32_t, std::string> cache = ignite.GetOrCreateCache<int32_t, std::string>("myNewCache");
```
{% endtab %}
{% endtabs %}

The methods that create a cache throw an `org.apache.ignite.IgniteCheckedException` exception when called while the baseline topology is being changed.

```shell
javax.cache.CacheException: class org.apache.ignite.IgniteCheckedException: Failed to start/stop cache, cluster state change is in progress.
        at org.apache.ignite.internal.processors.cache.GridCacheUtils.convertToCacheException(GridCacheUtils.java:1323)
        at org.apache.ignite.internal.IgniteKernal.createCache(IgniteKernal.java:3001)
        at org.apache.ignite.internal.processors.platform.client.cache.ClientCacheCreateWithNameRequest.process(ClientCacheCreateWithNameRequest.java:48)
        at org.apache.ignite.internal.processors.platform.client.ClientRequestHandler.handle(ClientRequestHandler.java:51)
        at org.apache.ignite.internal.processors.odbc.ClientListenerNioListener.onMessage(ClientListenerNioListener.java:173)
        at org.apache.ignite.internal.processors.odbc.ClientListenerNioListener.onMessage(ClientListenerNioListener.java:47)
        at org.apache.ignite.internal.util.nio.GridNioFilterChain$TailFilter.onMessageReceived(GridNioFilterChain.java:278)
        at org.apache.ignite.internal.util.nio.GridNioFilterAdapter.proceedMessageReceived(GridNioFilterAdapter.java:108)
        at org.apache.ignite.internal.util.nio.GridNioAsyncNotifyFilter$3.body(GridNioAsyncNotifyFilter.java:96)
        at org.apache.ignite.internal.util.worker.GridWorker.run(GridWorker.java:119)

        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
        at java.base/java.lang.Thread.run(Thread.java:834)
```

You may want to retry the operation if you catch this exception.

## Clearing Caches

To clear data from cache, use the `clear()` or `removeAll()` method. The sections below will help you choose the correct method for your environment.

### Using clear Method

The clear method removes data from the cache without notifying any listeners (for example, `CacheEntryRemovedListener`). As a result, calling this method does not delete data from [external cache storage](../persistence/external-storage.md), and deletion is not replicated via [data center replication](../../gridgain8-management/data-center-replication/introduction.md).

This method is optimized for performance for bulk data removal.

The example below shows how you can call this method:

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();
IgniteCache<Integer, String> cache = ignite.cache("myCache");

// Clear all entries without notifying listeners or cache writers
cache.clear();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.GetIgnite();
var cache = ignite.GetCache<int, string>("myCache");

// Clear all entries without notifying listeners or cache writers
cache.Clear();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Using removeAll Method

The removeAll method methodically removes all data from the cache, calling all listeners for each key removed. Data removal will be propagated to [external cache storage](../persistence/external-storage.md), and other clusters via [data center replication](../../gridgain8-management/data-center-replication/introduction.md).

Due to invoking listeners and callbacks, this is potentially an expensive operation.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();
IgniteCache<Integer, String> cache = ignite.cache("myCache");

// Remove all entries with full lifecycle integration
cache.removeAll();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.GetIgnite();
var cache = ignite.GetCache<int, string>("myCache");

// Remove all entries with full lifecycle integration
cache.RemoveAll();
```
{% endtab %}
{% tab title="C++" %}
```cpp
using namespace ignite::thin;

void RemoveData()
{
    cache::CacheClient<int32_t, std::string> cache =
        client.GetOrCreateCache<int32_t, std::string>("TestCache");

    cache.RemoveAll();
}
```
{% endtab %}
{% endtabs %}

## Destroying Caches

To delete a cache from all cluster nodes, call the `destroy()` method.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();

IgniteCache<Long, String> cache = ignite.cache("myCache");

cache.destroy();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.GetIgnite();
ignite.DestroyCache("myCache");
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Atomic Operations

Once you get the instance of a cache, you can start performing get/put operations on it.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, String> cache = ignite.cache("myCache");

// Store keys in the cache (the values will end up on different cache nodes).
for (int i = 0; i < 10; i++)
    cache.put(i, Integer.toString(i));

for (int i = 0; i < 10; i++)
    System.out.println("Got [key=" + i + ", val=" + cache.get(i) + ']');
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
using (var ignite = Ignition.Start("examples/config/example-cache.xml"))
{
    var cache = ignite.GetCache<int, string>("cache_name");

    for (var i = 0; i < 10; i++)
    {
        cache.Put(i, i.ToString());
    }

    for (var i = 0; i < 10; i++)
    {
        Console.Write("Got [key=" + i + ", val=" + cache.Get(i) + ']');
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
IgniteConfiguration cfg;
cfg.springCfgPath = "/path/to/configuration.xml";

try
{
    Ignite ignite = Ignition::Start(cfg);

    Cache<int32_t, std::string> cache = ignite.GetOrCreateCache<int32_t, std::string>(CACHE_NAME);

    // Store keys in the cache (the values will end up on different cache nodes).
    for (int32_t i = 0; i < 10; i++)
    {
        cache.Put(i, std::to_string(i));
    }

    for (int i = 0; i < 10; i++)
    {
        std::cout << "Got [key=" << i << ", val=" + cache.Get(i) << "]" << std::endl;
    }
}
catch (IgniteError& err)
{
    std::cout << "An error occurred: " << err.GetText() << std::endl;
    return err.GetCode();
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Bulk operations such as `putAll()` or `removeAll()` are executed as a sequence of atomic operations and can partially fail. 
If this happens, a `CachePartialUpdateException` is thrown and contains a list of keys for which the update failed.

To update a collection of entries within a single operation, consider using [transactions](../transactions.md).
{% endhint %}

Below are more examples of basic atomic operations:

{% tabs %}
{% tab title="Java" %}
```java
// Put-if-absent which returns previous value.
String oldVal = cache.getAndPutIfAbsent(11, "Hello");

// Put-if-absent which returns boolean success flag.
boolean success = cache.putIfAbsent(22, "World");

// Replace-if-exists operation (opposite of getAndPutIfAbsent), returns previous
// value.
oldVal = cache.getAndReplace(11, "New value");

// Replace-if-exists operation (opposite of putIfAbsent), returns boolean
// success flag.
success = cache.replace(22, "Other new value");

// Replace-if-matches operation.
success = cache.replace(22, "Other new value", "Yet-another-new-value");

// Remove-if-matches operation.
success = cache.remove(11, "Hello");
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
using (var ignite = Ignition.Start("examples/config/example-cache.xml"))
{
    var cache = ignite.GetCache<string, int>("cache_name");

    // Put-if-absent which returns previous value.
    var oldVal = cache.GetAndPutIfAbsent("Hello", 11);

    // Put-if-absent which returns boolean success flag.
    var success = cache.PutIfAbsent("World", 22);

    // Replace-if-exists operation (opposite of getAndPutIfAbsent), returns previous value.
    oldVal = cache.GetAndReplace("Hello", 11);

    // Replace-if-exists operation (opposite of putIfAbsent), returns boolean success flag.
    success = cache.Replace("World", 22);

    // Replace-if-matches operation.
    success = cache.Replace("World", 2, 22);

    // Remove-if-matches operation.
    success = cache.Remove("Hello", 1);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
IgniteConfiguration cfg;
cfg.springCfgPath = "/path/to/configuration.xml";

Ignite ignite = Ignition::Start(cfg);

Cache<std::string, int32_t> cache = ignite.GetOrCreateCache<std::string, int32_t>("myNewCache");

// Put-if-absent which returns previous value.
int32_t oldVal = cache.GetAndPutIfAbsent("Hello", 11);

// Put-if-absent which returns boolean success flag.
boolean success = cache.PutIfAbsent("World", 22);

// Replace-if-exists operation (opposite of getAndPutIfAbsent), returns previous value.
oldVal = cache.GetAndReplace("Hello", 11);

// Replace-if-exists operation (opposite of putIfAbsent), returns boolean success flag.
success = cache.Replace("World", 22);

// Replace-if-matches operation.
success = cache.Replace("World", 2, 22);

// Remove-if-matches operation.
success = cache.Remove("Hello", 1);
```
{% endtab %}
{% endtabs %}

## Asynchronous Execution

Most of the cache operations have asynchronous counterparts that have the "Async" suffix in their names.

{% tabs %}
{% tab title="Java" %}
```java
// a synchronous get
V get(K key);

// an asynchronous get
IgniteFuture<V> getAsync(K key);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
// a synchronous get
TV Get(TK key);

// an asynchronous get
Task<TV> GetAsync(TK key);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The asynchronous operations return an object that represents the result of the operation. You can wait for the completion of the operation in either blocking or non-blocking manner.

To wait for the results in a non-blocking fashion, register a closure using the `IgniteFuture.listen()` or `IgniteFuture.chain()` method. The closure is called when the operation is completed.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCompute compute = ignite.compute();

// Execute a closure asynchronously.
IgniteFuture<String> fut = compute.callAsync(() -> "Hello World");

// Listen for completion and print out the result.
fut.listen(f -> System.out.println("Job result: " + f.get()));
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class HelloworldFunc : IComputeFunc<string>
{
    public string Invoke()
    {
        return "Hello World";
    }
}
        
public static void AsynchronousExecution()
{
    var ignite = Ignition.Start();
    var compute = ignite.GetCompute();
            
    //Execute a closure asynchronously
    var fut = compute.CallAsync(new HelloworldFunc());
            
    // Listen for completion and print out the result
    fut.ContinueWith(Console.Write);
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Closures Execution and Thread Pools**

If an asynchronous operation is completed by the time the closure is passed to either the `IgniteFuture.listen()` or `IgniteFuture.chain()` method, then the closure is executed synchronously by the calling thread. Otherwise, the closure is executed asynchronously when the operation is completed.

Depending on the type of operation, the closure might be called by a thread from the system pool (asynchronous cache operations) or by a thread from the public pool (asynchronous compute operations). Therefore, you should avoid calling synchronous cache and compute operations from inside the closure, because it may lead to a deadlock due to pools starvation.

To achieve nested execution of asynchronous compute operations, you can take advantage of [custom thread pools](../../ha-and-performance/performance-tuning/thread-pools-tuning.md#creating-custom-thread-pool).
{% endhint %}

## Resource Injection

Ignite allows dependency injection of pre-defined Ignite resources, and supports field-based as well as method-based injection. Resources with proper annotations will be injected into the corresponding task, job, closure, or SPI before it is initialized.

You can inject resources by annotating either a field or a method. When you annotate a field, Ignite simply sets the value of the field at injection time (disregarding an access modifier of the field). If you annotate a method with a resource annotation, it should accept an input parameter of the type corresponding to the injected resource. If it does, then the method is invoked at injection time with the appropriate resource passed as an input argument.

Below is an example of a field injection.

{% code title="Java" %}
```java
Ignite ignite = Ignition.ignite();

Collection<String> res = ignite.compute().broadcast(new IgniteCallable<String>() {
    // Inject Ignite instance.
    @IgniteInstanceResource
    private Ignite ignite;

    @Override
    public String call() throws Exception {
        IgniteCache<Object, Object> cache = ignite.getOrCreateCache(CACHE_NAME);

        // Do some stuff with the cache.
    }
});
```
{% endcode %}

And this is an example of a method-based injection:

{% code title="Java" %}
```java
public class MyClusterJob implements ComputeJob {

    private Ignite ignite;

    // Inject an Ignite instance.
    @IgniteInstanceResource
    public void setIgnite(Ignite ignite) {
        this.ignite = ignite;
    }

}
```
{% endcode %}

There are a number of pre-defined resources that you can inject:

| Resource | Description |
|---|---|
| `CacheNameResource` | Injects the cache name provided via `CacheConfiguration.getName()`. |
| `CacheStoreSessionResource` | Injects the current `CacheStoreSession` instance. |
| `IgniteInstanceResource` | Injects the current instance of `Ignite`. |
| `JobContextResource` | Injects an instance of `ComputeJobContext`. A job context holds useful information about a particular job execution. For example, you can get the name of the cache containing the entry for which a job was colocated. |
| `LoadBalancerResource` | Injects an instance of `ComputeLoadBalancer` that can be used by a task to do the load balancing. |
| `ServiceResource` | Injects the service specified by the given name. |
| `SpringApplicationContextResource` | Injects Spring's `ApplicationContext` resource. |
| `SpringResource` | Injects resource from Spring's `ApplicationContext`. Use it whenever you would like to access a bean specified in Spring's application context XML configuration. |
| `TaskContinuousMapperResource` | Injects an instance of `ComputeTaskContinuousMapper`. Continuous mapping allows emitting jobs from the task at any point, even after the initial map phase. |
| `TaskSessionResource` | Injects an instance of the `ComputeTaskSession` resource, which defines a distributed session for a particular task execution. |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
