---
description: >-
  How to use continuous queries in GridGain to monitor cache modifications,
  including local listeners, initial queries, remote filters and transformers.
---

# Using Continuous Queries

A continuous query is a query that monitors data modifications occurring in a cache.
Once a continuous query is started, you get notified of all the data changes that fall into your query filter.

All update events are propagated to the [local listener](#local-listener), which must be registered in the query.
Continuous query implementation guarantees exactly once delivery of an event to the local listener.

You can also specify a remote filter to narrow down the range of entries that are monitored for updates.

{% hint style="warning" %}
**Continuous Queries and MVCC**

Continuous queries have a number of [functional limitations](../architecture/mvcc.md) when used with MVCC-enabled caches.
{% endhint %}

## Local Listener

When you modify a cache (insert, update, or delete an entry), an event is sent to the continuous query's local listener so that your application can react accordingly. This event is sent regardless of how the modification is made, including [data center replication](../gridgain8-management/data-center-replication/introduction.md).
The local listener is executed on the node that initiated the query.

Note that the continuous query throws an exception if started without a local listener.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, String> cache = ignite.getOrCreateCache("myCache");

ContinuousQuery<Integer, String> query = new ContinuousQuery<>();

query.setLocalListener(new CacheEntryUpdatedListener<Integer, String>() {

    @Override
    public void onUpdated(Iterable<CacheEntryEvent<? extends Integer, ? extends String>> events)
        throws CacheEntryListenerException {
        // react to the update events here
    }
});

cache.query(query);

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
class LocalListener : ICacheEntryEventListener<int, string>
{
    public void OnEvent(IEnumerable<ICacheEntryEvent<int, string>> evts)
    {
        foreach (var cacheEntryEvent in evts)
        {
            //react to update events here
        }
    }
}
public static void ContinuousQueryListenerDemo()
{
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
        }
    });
    var cache = ignite.GetOrCreateCache<int, string>("myCache");

    var query = new ContinuousQuery<int, string>(new LocalListener());

    var handle = cache.QueryContinuous(query);

    cache.Put(1, "1");
    cache.Put(2, "2");
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
/**
 * Listener class.
 */
template<typename K, typename V>
class Listener : public event::CacheEntryEventListener<K, V>
{
public:
    /**
     * Default constructor.
     */
    Listener()
    {
        // No-op.
    }

    /**
     * Event callback.
     *
     * @param evts Events.
     * @param num Events number.
     */
    virtual void OnEvent(const CacheEntryEvent<K, V>* evts, uint32_t num)
    {
        for (uint32_t i = 0; i < num; ++i)
        {
            std::cout << "Queried entry [key=" << (evts[i].HasValue() ? evts[i].GetKey() : K())
                << ", val=" << (evts[i].HasValue() ? evts[i].GetValue() : V()) << ']'
                << std::endl;
        }
    }
};

int main()
{
    IgniteConfiguration cfg;
    cfg.springCfgPath = "/path/to/configuration.xml";

    Ignite ignite = Ignition::Start(cfg);

    Cache<int32_t, std::string> cache = ignite.GetOrCreateCache<int32_t, std::string>("myCache");

    // Declaring custom listener.
    Listener<int32_t, std::string> listener;

    // Declaring continuous query.
    continuous::ContinuousQuery<int32_t, std::string> query(MakeReference(listener));

    continuous::ContinuousQueryHandle<int32_t, std::string> handle = cache.QueryContinuous(query);
}
```
{% endtab %}
{% endtabs %}

Avoid using operations that could block execution thread inside the listener. This can lead to cluster-wide issues with cache processing. Cache operations such as `put`, `putAll`, `get`, etc., belong to the above category. Therefore, the following example is *unsafe*:

```java
qry.setLocalListener(new CacheEntryUpdatedListener<Integer, String>() {
   @Override public void onUpdated(Iterable<CacheEntryEvent<? extends Integer, ? extends String>> evts) {
      for (CacheEntryEvent<? extends Integer, ? extends String> e : evts) {
         // The following operation can block the current thread, so it's not safe:
         ignite.cache("other").put(e.getKey(), e.getValue());
      }
   }
});
```

To make the above operation safe, you can use the [@IgniteAsynCallback annotation](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/lang/IgniteAsyncCallback.html): 

```java
@IgniteAsyncCallback
private static class CacheEntryCopier implements CacheEntryUpdatedListener<Integer, String> {

   @IgniteInstanceResource
   private Ignite ignite;

   @Override public void onUpdated(CacheEntryEvent<? extends Integer, ? extends String> e) throws CacheEntryListenerException {
      for (CacheEntryEvent<? extends Integer, ? extends String> e : evts) {
         // This cache operation is safe because the listener has the Ignite @IgniteAsyncCallback annotation:
         ignite.cache("other").put(e.getKey(), e.getValue());      
      }
   }
}
```

## Initial Query

You can specify an initial query that is executed before the continuous query gets registered in the cluster and before you start to receive updates.
To specify an initial query, use the `ContinuousQuery.setInitialQuery(...)` method.

Just like scan queries, a continuous query is executed via the `query()` method that returns a cursor. When an initial query is set, you can use that cursor to iterate over the results of the initial query.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, String> cache = ignite.getOrCreateCache("myCache");

ContinuousQuery<Integer, String> query = new ContinuousQuery<>();

// Setting an optional initial query.
// The query will return entries for the keys greater than 10.
query.setInitialQuery(new ScanQuery<>((k, v) -> k > 10));

//mandatory local listener
query.setLocalListener(events -> {
});

try (QueryCursor<Cache.Entry<Integer, String>> cursor = cache.query(query)) {
    // Iterating over the entries returned by the initial query 
    for (Cache.Entry<Integer, String> e : cursor)
        System.out.println("key=" + e.getKey() + ", val=" + e.getValue());
}
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cache = ignite.GetCache<int, string>("myCache");
var query = new ContinuousQuery<int, string>(new LocalListener());
var initialQuery = new SqlFieldsQuery("select * from myTable");

using (IContinuousQueryHandleFields handle = cache.QueryContinuous(query, initialQuery))
{
    IFieldsQueryCursor initialCursor = handle.GetInitialQueryCursor();
    IList<IList<object>> initialEntries = initialCursor.GetAll();
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
Cache<int32_t, std::string> cache = ignite.GetOrCreateCache<int32_t, std::string>("myCache");

// Custom listener
Listener<int32_t, std::string> listener;

// Declaring continuous query.
continuous::ContinuousQuery<int32_t, std::string> query(MakeReference(listener));

// Declaring optional initial query
ScanQuery initialQuery = ScanQuery();

continuous::ContinuousQueryHandle<int32_t, std::string> handle = cache.QueryContinuous(query, initialQuery);

// Iterating over existing data stored in the cache.
QueryCursor<int32_t, std::string> cursor = handle.GetInitialQueryCursor();

while (cursor.HasNext())
{
    std::cout << cursor.GetNext().GetKey() << std::endl;
}
```
{% endtab %}
{% endtabs %}

## Remote Filter

This filter is executed for each updated key and evaluates whether the update should be propagated to the query's local listener.
If the filter returns `true`, then the local listener is notified about the update.

For redundancy reasons, the filter is executed for both primary and backup versions (if backups are configured) of the key.
Because of this, a remote filter can be used as a remote listener for update events.

{% tabs %}
{% tab title="Java" %}
```java
ContinuousQuery<Integer, String> qry = new ContinuousQuery<>();

qry.setLocalListener(events ->
    events.forEach(event -> System.out.format("Entry: key=[%s] value=[%s]\n", event.getKey(), event.getValue()))
);

qry.setRemoteFilterFactory(new Factory<CacheEntryEventFilter<Integer, String>>() {
    @Override
    public CacheEntryEventFilter<Integer, String> create() {
        return new CacheEntryEventFilter<Integer, String>() {
            @Override
            public boolean evaluate(CacheEntryEvent<? extends Integer, ? extends String> e) {
                System.out.format("the value for key [%s] was updated from [%s] to [%s]\n", e.getKey(), e.getOldValue(), e.getValue());
                return true;
            }
        };
    }
});

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
class LocalListener : ICacheEntryEventListener<int, string>
{
    public void OnEvent(IEnumerable<ICacheEntryEvent<int, string>> evts)
    {
        foreach (var cacheEntryEvent in evts)
        {
            //react to update events here
        }
    }
}
class RemoteFilter : ICacheEntryEventFilter<int, string>
{
    public bool Evaluate(ICacheEntryEvent<int, string> e)
    {
        if (e.Key == 1)
        {
            return false;
        }
        Console.WriteLine("the value for key {0} was updated from {1} to {2}", e.Key, e.OldValue, e.Value);
        return true;
    }
}
public static void ContinuousQueryFilterDemo()
{
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
        }
    });
    var cache = ignite.GetOrCreateCache<int, string>("myCache");

    var query = new ContinuousQuery<int, string>(new LocalListener(), new RemoteFilter());

    using (var handle = cache.QueryContinuous(query))
    {
        cache.Put(1, "1");
        cache.Put(2, "2");
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
template<typename K, typename V>
struct RemoteFilter : event::CacheEntryEventFilter<int32_t, std::string>
{
    /**
     * Default constructor.
     */
    RemoteFilter()
    {
        // No-op.
    }

    /**
     * Destructor.
     */
    virtual ~RemoteFilter()
    {
        // No-op.
    }

    /**
     * Event callback.
     *
     * @param event Event.
     * @return True if the event passes filter.
     */
    virtual bool Process(const CacheEntryEvent<K, V>& event)
    {
        std::cout << "The value for key " << event.GetKey() <<
            " was updated from " << event.GetOldValue() << " to " << event.GetValue() << std::endl;
        return true;
    }
};

namespace ignite
{
    namespace binary
    {
        template<>
        struct BinaryType< RemoteFilter<int32_t, std::string> >
        {
            static int32_t GetTypeId()
            {
                return GetBinaryStringHashCode("RemoteFilter<int32_t,std::string>");
            }

            static void GetTypeName(std::string& dst)
            {
                dst = "RemoteFilter<int32_t,std::string>";

            }

            static int32_t GetFieldId(const char* name)
            {
                return GetBinaryStringHashCode(name);
            }

            static bool IsNull(const RemoteFilter<int32_t, std::string>&)
            {
                return false;
            }

            static void GetNull(RemoteFilter<int32_t, std::string>& dst)
            {
                dst = RemoteFilter<int32_t, std::string>();
            }

            static void Write(BinaryWriter& writer, const RemoteFilter<int32_t, std::string>& obj)
            {
                // No-op.
            }

            static void Read(BinaryReader& reader, RemoteFilter<int32_t, std::string>& dst)
            {
                // No-op.
            }
        };
    }
}

int main()
{
    IgniteConfiguration cfg;
    cfg.springCfgPath = "/path/to/configuration.xml";

    // Start a node.
    Ignite ignite = Ignition::Start(cfg);

    // Get binding.
    IgniteBinding binding = ignite.GetBinding();

    // Registering remote filter.
    binding.RegisterCacheEntryEventFilter<RemoteFilter<int32_t, std::string>>();

    // Get cache instance.
    Cache<int32_t, std::string> cache = ignite.GetOrCreateCache<int32_t, std::string>("myCache");

    // Declaring custom listener.
    Listener<int32_t, std::string> listener;

    // Declaring filter.
    RemoteFilter<int32_t, std::string> filter;

    // Declaring continuous query.
    continuous::ContinuousQuery<int32_t, std::string> qry(MakeReference(listener), MakeReference(filter));
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
In order to use remote filters, make sure the class definitions of the filters are available on the server nodes.
You can do this in two ways:

- Add the classes to the classpath of every server node;
- Enable [peer class loading](code-deployment/peer-class-loading.md).
{% endhint %}

## Remote Transformer

By default, continuous queries send the whole updated object to the local listener. This can lead to excessive network usage, especially if the object is very large. Moreover, applications often need only a subset of fields of the object.

To address these cases, you can use a continuous query with a transformer. A transformer is a function that is executed on remote nodes for every updated object and sends back only the results of the transformation.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, Person> cache = ignite.getOrCreateCache("myCache");

// Create a new continuous query with a transformer.
ContinuousQueryWithTransformer<Integer, Person, String> qry = new ContinuousQueryWithTransformer<>();

// Factory to create transformers.
Factory factory = FactoryBuilder.factoryOf(
    // Return one field of a complex object.
    // Only this field will be sent over to the local listener.
    (IgniteClosure<CacheEntryEvent, String>)
        event -> ((Person)event.getValue()).getName()
);

qry.setRemoteTransformerFactory(factory);

// Listener that will receive transformed data.
qry.setLocalListener(names -> {
    for (String name : names)
        System.out.println("New person name: " + name);
});
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="info" %}
In order to use transformers, make sure the class definitions of the transformers are available on the server nodes.
You can do this in two ways:

- Add the classes to the classpath of every server node;
- Enable [peer class loading](code-deployment/peer-class-loading.md).
{% endhint %}

## Asynchronous Continuous Queries (.NET)

The .NET client can expose a continuous query as an
[`IAsyncEnumerable<T>`](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerable-1),
so you consume cache update events with `await foreach` instead of registering a local listener.
This gives you idiomatic, non-blocking async iteration over the event stream.

Use one of the `ICache.QueryContinuousAsync(...)` overloads. The overload without an initial query
returns the event stream directly:

```csharp
public static async Task AsyncContinuousQuery(ICache<int, string> cache)
{
    // Consume cache update events as an async stream.
    await foreach (ICacheEntryEvent<int, string> e in cache.QueryContinuousAsync())
    {
        Console.WriteLine("Event: {0}, key={1}, value={2}", e.EventType, e.Key, e.Value);
    }
}
```

The query starts lazily when enumeration begins. Ending the `await foreach` loop, disposing the
enumerator, or cancelling the supplied `CancellationToken` stops the query and releases the
associated server-side resources. The stream can be enumerated only once; a second attempt throws
`InvalidOperationException`.

You can narrow the monitored entries with a server-side filter and tune server-side batching with
`ContinuousQueryOptions`:

```csharp
public static async Task AsyncContinuousQueryWithOptions(
    ICache<int, string> cache, CancellationToken cancellationToken)
{
    var options = new ContinuousQueryOptions { BufferSize = 64, IncludeExpired = true };

    await foreach (var e in cache.QueryContinuousAsync(options, new RemoteFilter(), cancellationToken))
    {
        Console.WriteLine("Event: {0}, key={1}", e.EventType, e.Key);
    }
}
```

{% hint style="info" %}
There is no backpressure. Events that arrive faster than they are consumed are buffered in memory
without bound. Use `ContinuousQueryOptions.BufferSize` and `ContinuousQueryOptions.TimeInterval` to
control server-side batching.
{% endhint %}

### Query handle

To also iterate over the entries that already exist when the query starts, pass an initial query:
`ScanQuery`, `SqlQuery`, `TextQuery`, or `SqlFieldsQuery`.

These overloads return an `IContinuousQueryHandleAsync` handle instead of a stream. The handle
exposes two methods:

- `GetInitialQueryCursor()` reads the pre-existing entries.
- `GetEvents()` returns the subsequent updates as an `IAsyncEnumerable`.

You can call each method only once. Disposing the handle stops the query.

```csharp
public static async Task AsyncContinuousQueryWithInitialQuery(ICache<int, string> cache)
{
    await using var handle = cache.QueryContinuousAsync(initialQry: new ScanQuery<int, string>());

    // Read entries that already existed when the query started.
    await using (var cursor = handle.GetInitialQueryCursor())
    {
        foreach (ICacheEntry<int, string> entry in cursor)
        {
            Console.WriteLine("Initial: key={0}, value={1}", entry.Key, entry.Value);
        }
    }

    // Consume subsequent updates.
    await foreach (var e in handle.GetEvents())
    {
        Console.WriteLine("Event: {0}, key={1}", e.EventType, e.Key);
    }
}
```

## Events Delivery Guarantees

Continuous queries ensure the exactly-once semantic for the delivery of events to the clients' local listeners.

Both primary and backup nodes maintain an update queue that holds events that are processed by continuous queries  on the server side but yet to be delivered to the clients. Suppose a primary node crashes or the cluster topology changes for any reason. In that case, every backup node flushes the content of its update queue to the client, making sure that every event is delivered to the client's local listener.

GridGain manages a special per-partition update counter that helps to avoid duplicate notifications. Once an entry in some partition is updated, a counter for this partition is incremented on both primary and backup nodes. The value of this counter is also sent along with the event notification to the client. Thus, the client can skip already-processed events. Once the client confirms that an event is received, the primary and backup nodes remove the record for this event from their backup queues.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
