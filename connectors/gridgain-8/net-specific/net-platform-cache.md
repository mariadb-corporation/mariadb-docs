---
hidden: true
description: >-
  Configure the GridGain.NET platform cache, an experimental CLR-heap caching layer
  that keeps deserialized cache entries to speed up reads.
---

# .NET Platform Cache

{% hint style="danger" %}
Experimental API
{% endhint %}

GridGain.NET provides an additional layer of caching in the [CLR](https://docs.microsoft.com/en-us/dotnet/standard/clr) heap. The platform cache keeps a deserialized copy of every cache entry that is present on the current node, thus greatly improving cache read performance at the cost of increased memory usage.

{% hint style="info" %}
Platform caches are bypassed within transactions: when a transaction is active, `cache.Get` and the other APIs listed below do not use the platform cache. Transaction support is coming soon.
{% endhint %}

## Configuring Platform Cache

### Server Nodes

Platform cache is configured once for all server nodes by setting `CacheConfiguration.PlatformCacheConfiguration` to a non-null value. Platform cache on server nodes stores **all primary and backup cache entries assigned to the given node** in .NET memory.
Entries are updated in real time and they are guaranteed to be up to date at any given moment, even before user code accesses them.

{% hint style="danger" %}
Platform cache effectively doubles memory usage on server nodes, every cache entry is stored twice: serialized in unmanaged (offheap) memory, and deserialized in CLR heap.
{% endhint %}

```csharp
var cacheCfg = new CacheConfiguration("my-cache")
{
    PlatformCacheConfiguration = new PlatformCacheConfiguration()
};

var cache = ignite.CreateCache<int, string>(cacheCfg);
```

### Client Nodes

Platform caches on client nodes require a [Near Cache](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/near-cache) to be configured, since client nodes do not store data otherwise. The platform cache on a client node keeps the same set of entries as the near cache on that node. the near cache eviction policy effectively applies to the platform cache.

```csharp
var nearCacheCfg = new NearCacheConfiguration
{
    // Keep up to 1000 most recently used entries in Near and Platform caches.
    EvictionPolicy = new LruEvictionPolicy
    {
        MaxSize = 1000
    }
};
            
var cache = ignite.CreateNearCache<int, string>("my-cache",
    nearCacheCfg,
    new PlatformCacheConfiguration());
```

## Supported APIs

The following `ICache<K, V>` APIs use a platform cache (including the corresponding async versions):

- `Get`, `TryGet`, indexer (`ICache[k]`)
- `GetAll` (reads from the platform cache first and falls back to the distributed cache when necessary)
- `ContainsKey`, `ContainsKeys`
- `LocalPeek`, `TryLocalPeek`
- `GetLocalEntries`
- `GetLocalSize`
- `Query` with `ScanQuery`
  - Uses the platform cache to pass values to `ScanQuery.Filter`
  - Iterates over the platform cache directly when `ScanQuery.Local` is `true` and `ScanQuery.Partition` is not null

## Access Platform Cache Data Directly

You don't need to change your code to take advantage of a Platform Cache. Existing calls to `ICache.Get` and other APIs listed above will be served from the platform cache when possible, improving performance. When a given entry is not present in the platform cache, Ignite falls back to a normal path and retrieves the value from the cluster.

However, in some cases we may wish to access the platform cache exclusively, avoiding Java and network calls. `Local` APIs in combination with `CachePeekMode.Platform` allow us to do just that:

```csharp
var cache = ignite.GetCache<int, string>("my-cache");
            
// Get value from platform cache.
bool hasKey = cache.TryLocalPeek(1, out var val, CachePeekMode.Platform);
            
// Get platform cache size (current number of entries on local node).
int size = cache.GetLocalSize(CachePeekMode.Platform);
            
// Get all values from platform cache.
IEnumerable<ICacheEntry<int, string>> entries = cache.GetLocalEntries(CachePeekMode.Platform);
            
```

## Advanced Configuration

### Binary Mode

In order to use [Binary Objects](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/binary-objects) together with platform cache, set `PlatformCacheConfiguration.KeepBinary` to `true`:

```csharp
var cacheCfg = new CacheConfiguration("people")
{
    PlatformCacheConfiguration = new PlatformCacheConfiguration
    {
        KeepBinary = true
    }
};

var cache = ignite.CreateCache<int, Person>(cacheCfg)
    .WithKeepBinary<int, IBinaryObject>();

IBinaryObject binaryPerson = cache.Get(1);
```

### Key and Value Types

When using Ignite cache with [Value Types](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types), you should set `PlatformCacheConfiguration.KeyTypeName` and `ValueTypeName` accordingly to achieve maximum performance and reduce GC pressure:

```csharp
var cacheCfg = new CacheConfiguration("people")
{
    PlatformCacheConfiguration = new PlatformCacheConfiguration
    {
        KeyTypeName = typeof(long).FullName,
        ValueTypeName = typeof(Guid).FullName
    }
};

var cache = ignite.CreateCache<long, Guid>(cacheCfg);
```

Ignite uses `ConcurrentDictionary<object, object>` by default to store platform cache data, because the actual types are  unknown beforehand. This results in [boxing and unboxing](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/types/boxing-and-unboxing) for value types, reducing performance and allocating more memory. When `KeyTypeName` and `ValueTypeName` are set in `PlatformCacheConfiguration`, Ignite uses those types to create an internal `ConcurrentDictionary` instead of the default `object`.

{% hint style="danger" %}
Incorrect `KeyTypeName` and/or `ValueTypeName` settings can cause runtime cast exceptions.
{% endhint %}
</content>
