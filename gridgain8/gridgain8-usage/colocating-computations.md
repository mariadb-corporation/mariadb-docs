---
description: >-
  How to colocate computations with data in GridGain using affinityCall and
  affinityRun, by key or partition, plus entry processors.
---

# Colocating Computations with Data

Colocated computation is type of distributed data processing wherein the computational task you want to perform over a specific data set is sent to the nodes where the required data is located and only the results of the computations are sent back. This approach minimizes data transfer between nodes and can significantly reduce the task execution time.

GridGain provides several ways to perform colocated computations, all of which use the affinity function to determine the location of the data.

The compute interface provides the `affinityCall(...)` and `affinityRun(...)` methods that colocate a task with data either by key or by partition.

{% hint style="warning" %}
The `affinityCall(...)` and `affinityRun(...)` methods guarantee that the data for the given key or partition is present on the target node for the duration of the task.
{% endhint %}

{% hint style="warning" %}
The class definitions of the task to be executed on remote nodes must be available on the nodes.
You can ensure this in two ways:

- Add the classes to the classpath of the nodes;
- Enable [peer class loading](code-deployment/peer-class-loading.md).
{% endhint %}

## Colocating by Key

To send a computational task to the node where a given key is located, use the following methods:

- `IgniteCompute.affinityCall(String cacheName, Object key, IgniteCallable<R> job)`
- `IgniteCompute.affinityRun(String cacheName, Object key, IgniteRunnable job)`

GridGain calls the configured affinity function to determine the location of the given key.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<Integer, String> cache = ignite.cache("myCache");

IgniteCompute compute = ignite.compute();

int key = 1;

// This closure will execute on the remote node where
// data for the given 'key' is located.
compute.affinityRun("myCache", key, () -> {
    // Peek is a local memory lookup.
    System.out.println("Co-located [key= " + key + ", value= " + cache.localPeek(key) + ']');
});

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp

class MyComputeAction : IComputeAction
{
    [InstanceResource] private readonly IIgnite _ignite;

    public int Key { get; set; }

    public void Invoke()
    {
        var cache = _ignite.GetCache<int, string>("myCache");
        // Peek is a local memory lookup
        Console.WriteLine("Co-located [key= " + Key + ", value= " + cache.LocalPeek(Key) + ']');
    }
}

public static void AffinityRunDemo()
{
    var cfg = new IgniteConfiguration();
    var ignite = Ignition.Start(cfg);

    var cache = ignite.GetOrCreateCache<int, string>("myCache");
    cache.Put(0, "foo");
    cache.Put(1, "bar");
    cache.Put(2, "baz");
    var keyCnt = 3;
            
    var compute = ignite.GetCompute();

    for (var key = 0; key < keyCnt; key++)
    {
        // This closure will execute on the remote node where
        // data for the given 'key' is located.
        compute.AffinityRun("myCache", key, new MyComputeAction {Key = key});
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
/*
 * Function class.
 */
struct FuncAffinityRun : compute::ComputeFunc<void>
{
    /*
    * Default constructor.
    */
    FuncAffinityRun()
    {
        // No-op.
    }

    /*
    * Parameterized constructor.
    */
    FuncAffinityRun(std::string cacheName, int32_t key) :
        cacheName(cacheName), key(key)
    {
        // No-op.
    }

    /**
     * Callback.
     */
    virtual void Call()
    {
        Ignite& node = GetIgnite();

        Cache<int32_t, std::string> cache = node.GetCache<int32_t, std::string>(cacheName.c_str());

        // Peek is a local memory lookup.
        std::cout << "Co-located [key= " << key << ", value= " << cache.LocalPeek(key, CachePeekMode::ALL) << "]" << std::endl;
    }

    std::string cacheName;
    int32_t key;
};

/**
 * Binary type structure. Defines a set of functions required for type to be serialized and deserialized.
 */
namespace ignite
{
    namespace binary
    {
        template<>
        struct BinaryType<FuncAffinityRun>
        {
            static int32_t GetTypeId()
            {
                return GetBinaryStringHashCode("FuncAffinityRun");
            }

            static void GetTypeName(std::string& dst)
            {
                dst = "FuncAffinityRun";
            }

            static int32_t GetFieldId(const char* name)
            {
                return GetBinaryStringHashCode(name);
            }

            static int32_t GetHashCode(const FuncAffinityRun& obj)
            {
                return 0;
            }

            static bool IsNull(const FuncAffinityRun& obj)
            {
                return false;
            }

            static void GetNull(FuncAffinityRun& dst)
            {
                dst = FuncAffinityRun();
            }

            static void Write(BinaryWriter& writer, const FuncAffinityRun& obj)
            {
                writer.WriteString("cacheName", obj.cacheName);
                writer.WriteInt32("key", obj.key);
            }

            static void Read(BinaryReader& reader, FuncAffinityRun& dst)
            {
                dst.cacheName = reader.ReadString("cacheName");
                dst.key = reader.ReadInt32("key");
            }
        };
    }
}

int main()
{
    IgniteConfiguration cfg;
    cfg.springCfgPath = "/path/to/configuration.xml";

    Ignite ignite = Ignition::Start(cfg);

    // Get cache instance.
    Cache<int32_t, std::string> cache = ignite.GetOrCreateCache<int32_t, std::string>("myCache");

    // Get binding instance.
    IgniteBinding binding = ignite.GetBinding();

    // Registering our class as a compute function.
    binding.RegisterComputeFunc<FuncAffinityRun>();

    // Get compute instance.
    compute::Compute compute = ignite.GetCompute();

    int key = 1;

    // This closure will execute on the remote node where
    // data for the given 'key' is located.
    compute.AffinityRun(cache.GetName(), key, FuncAffinityRun(cache.GetName(), key));
}
```
{% endtab %}
{% endtabs %}

## Colocating by Partition

The `affinityCall(Collection<String> cacheNames, int partId, IgniteRunnable job)` and `affinityRun(Collection<String> cacheNames, int partId, IgniteRunnable job)` send a given task to the node where the partition with a given ID is located. This is useful when you need to retrieve objects for multiple keys and you know that the keys belong to the same partition. In this case, you can create one task instead of multiple task for each key.

For example, let's say you want to calculate the arithmetic mean of a specific field for a specific subset of keys.
If you want to distribute the computation, you can group the keys by partitions and send each group of keys to the node where the partition is located to get the values.
The number of groups and, therefore, the number of tasks is no more than the total number of partitions (default is 1024).
Below is a code snippet that illustrates this example.

{% tabs %}
{% tab title="Java" %}
```java
// this task sums up the values of the salary field for the given set of keys
private static class SumTask implements IgniteCallable<BigDecimal> {
    private Set<Long> keys;

    public SumTask(Set<Long> keys) {
        this.keys = keys;
    }

    @IgniteInstanceResource
    private Ignite ignite;

    @Override
    public BigDecimal call() throws Exception {

        IgniteCache<Long, BinaryObject> cache = ignite.cache("person").withKeepBinary();

        BigDecimal sum = new BigDecimal(0);

        for (long k : keys) {
            BinaryObject person = cache.localPeek(k, CachePeekMode.PRIMARY);
            if (person != null)
                sum = sum.add(new BigDecimal((float) person.field("salary")));
        }

        return sum;
    }
}

public static void calculateAverage(Ignite ignite, Set<Long> keys) {

    // get the affinity function configured for the cache
    Affinity<Long> affinityFunc = ignite.affinity("person");

    // this map stores collections of keys for each partition
    HashMap<Integer, Set<Long>> partMap = new HashMap<>();
    keys.forEach(k -> {
        int partId = affinityFunc.partition(k);

        Set<Long> keysByPartition = partMap.computeIfAbsent(partId, key -> new HashSet<Long>());
        keysByPartition.add(k);
    });

    BigDecimal total = new BigDecimal(0);

    IgniteCompute compute = ignite.compute();

    List<String> caches = Arrays.asList("person");

    // iterate over all partitions
    for (Map.Entry<Integer, Set<Long>> pair : partMap.entrySet()) {
        // send a task that gets specific keys for the partition
        BigDecimal sum = compute.affinityCall(caches, pair.getKey().intValue(), new SumTask(pair.getValue()));
        total = total.add(sum);
    }

    System.out.println("the average salary is " + total.floatValue() / keys.size());
}

```
{% endtab %}

{% tab title="C#/.NET" %}

```csharp
ICache<long, Person> cache = ignite.GetOrCreateCache<long, Person>("person");
cache[1] = new("John Doe", 25_000);
cache[2] = new("Don Joe", 35_000);

long[] keys = { 1, 2 };
ICacheAffinity affinity = ignite.GetAffinity(cache.Name);

var keysByPartition = keys.GroupBy(affinity.GetPartition);
decimal total = 0;

// Perform one compute call for every partition.
foreach (IGrouping<int, long> part in keysByPartition)
{
    int partition = part.Key;
    List<long> partitionKeys = part.ToList();

    // Partition is reserved while the compute job executes, all keys are guaranteed to be local.
    total += ignite.GetCompute().AffinityCall(
        cacheNames: new[] { cache.Name }, partition, new SumTask(partitionKeys));
}

var averageSalary = total / keys.Length;
Console.WriteLine($"The average salary is {averageSalary}");

record SumTask(ICollection<long> Keys) : IComputeFunc<decimal>
{
    [InstanceResource]
    private readonly IIgnite _ignite;

    public decimal Invoke()
    {
        var cache = _ignite.GetCache<long, Person>("person");
        return Keys.Select(k => cache.LocalPeek(k).Salary).Sum();
    }
}

record Person(string Name, decimal Salary);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

If you want to process all the data in the cache, you can iterate over all cache partitions and send tasks that process the data stored on each individual partition.

{% tabs %}
{% tab title="Java" %}
```java
// this task sums up the value of the 'salary' field for all objects stored in
// the given partition
private static class SumByPartitionTask implements IgniteCallable<BigDecimal> {
    private int partId;

    public SumByPartitionTask(int partId) {
        this.partId = partId;
    }

    @IgniteInstanceResource
    private Ignite ignite;

    @Override
    public BigDecimal call() throws Exception {
        // use binary objects to avoid deserialization
        IgniteCache<Long, BinaryObject> cache = ignite.cache("person").withKeepBinary();

        BigDecimal total = new BigDecimal(0);
        try (QueryCursor<Cache.Entry<Long, BinaryObject>> cursor = cache
                .query(new ScanQuery<Long, BinaryObject>(partId).setLocal(true))) {
            for (Cache.Entry<Long, BinaryObject> entry : cursor) {
                total = total.add(new BigDecimal((float) entry.getValue().field("salary")));
            }
        }

        return total;
    }
}

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
record SumByPartitionTask(int Partition) : IComputeFunc<decimal>
{
[InstanceResource]
private readonly IIgnite _ignite;

    public decimal Invoke()
    {
        var cache = _ignite.GetCache<long, Person>("person");

        var query = new ScanQuery<long, Person>
        {
            Partition = Partition,
            Local = true
        };

        return cache.Query(query).Sum(x => x.Value.Salary);
    }
}
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Performance Considerations**

Colocated computations yield performance benefits when the amount of the data you want to process is sufficiently large. In some cases, when the amount of data is small, a [scan query](key-value-api/using-scan-queries.md) may perform better.
{% endhint %}

## Entry Processor

An entry processor is used to process cache entries on the nodes where they are stored and return the result of the processing. With an entry processor, you do not have to transfer the entire object to perform an operation with it, you can perform the operation remotely and only transfer the results.

If an entry processor sets the value for an entry that does not exist, the entry is added to the cache.

Entry processors are executed atomically within a lock on the given cache key.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<String, Integer> cache = ignite.cache("mycache");

// Increment the value for a specific key by 1.
// The operation will be performed on the node where the key is stored.
// Note that if the cache does not contain an entry for the given key, it will
// be created.
cache.invoke("mykey", (entry, args) -> {
    Integer val = entry.getValue();

    entry.setValue(val == null ? 1 : val + 1);

    return null;
});

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
void CacheInvoke()
{
    var ignite = Ignition.Start();

    var cache = ignite.GetOrCreateCache<int, int>("myCache");

    var proc = new Processor();

    // Increment cache value 10 times
    for (int i = 0; i < 10; i++)
        cache.Invoke(1, proc, 5);
}

class Processor : ICacheEntryProcessor<int, int, int, int>
{
    public int Process(IMutableCacheEntry<int, int> entry, int arg)
    {
        entry.Value = entry.Exists ? arg : entry.Value + arg;

        return entry.Value;
    }
}
```
{% endtab %}

{% tab title="C++" %}
```cpp
/**
 * Processor for invoke method.
 */
class IncrementProcessor : public cache::CacheEntryProcessor<std::string, int32_t, int32_t, int32_t>
{
public:
    /**
     * Constructor.
     */
    IncrementProcessor()
    {
        // No-op.
    }

    /**
     * Copy constructor.
     *
     * @param other Other instance.
     */
    IncrementProcessor(const IncrementProcessor& other)
    {
        // No-op.
    }

    /**
     * Assignment operator.
     *
     * @param other Other instance.
     * @return This instance.
     */
    IncrementProcessor& operator=(const IncrementProcessor& other)
    {
        return *this;
    }

    /**
     * Call instance.
     */
    virtual int32_t Process(MutableCacheEntry<std::string, int32_t>& entry, const int& arg)
    {
        // Increment the value for a specific key by 1.
        // The operation will be performed on the node where the key is stored.
        // Note that if the cache does not contain an entry for the given key, it will
        // be created.
        if (!entry.IsExists())
            entry.SetValue(1);
        else
            entry.SetValue(entry.GetValue() + 1);

        return entry.GetValue();
    }
};

/**
 * Binary type structure. Defines a set of functions required for type to be serialized and deserialized.
 */
namespace ignite
{
    namespace binary
    {
        template<>
        struct BinaryType<IncrementProcessor>
        {
            static int32_t GetTypeId()
            {
                return GetBinaryStringHashCode("IncrementProcessor");
            }

            static void GetTypeName(std::string& dst)
            {
                dst = "IncrementProcessor";
            }

            static int32_t GetFieldId(const char* name)
            {
                return GetBinaryStringHashCode(name);
            }

            static int32_t GetHashCode(const IncrementProcessor& obj)
            {
                return 0;
            }

            static bool IsNull(const IncrementProcessor& obj)
            {
                return false;
            }

            static void GetNull(IncrementProcessor& dst)
            {
                dst = IncrementProcessor();
            }

            static void Write(BinaryWriter& writer, const IncrementProcessor& obj)
            {
                // No-op.
            }

            static void Read(BinaryReader& reader, IncrementProcessor& dst)
            {
                // No-op.
            }
        };
    }
}

int main()
{
    IgniteConfiguration cfg;
    cfg.springCfgPath = "platforms/cpp/examples/put-get-example/config/example-cache.xml";

    Ignite ignite = Ignition::Start(cfg);

    // Get cache instance.
    Cache<std::string, int32_t> cache = ignite.GetOrCreateCache<std::string, int32_t>("myCache");

    // Get binding instance.
    IgniteBinding binding = ignite.GetBinding();

    // Registering our class as a cache entry processor.
    binding.RegisterCacheEntryProcessor<IncrementProcessor>();

    std::string key("mykey");
    IncrementProcessor inc;

    cache.Invoke<int32_t>(key, inc, NULL);
}
```
{% endtab %}
{% endtabs %}

Because entry processors are executed on individual nodes, all entry processors must be stateless and return the same result regardless of where they are executed. For example, timestamps and random values should be passed as in parameters of the invoke method rather than calculated on the node.

The example below will the entry value to the same random UUID across all nodes:

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache<String, UUID> cache = ignite.cache("mycache");

// Get a random UUID
UUID uuid = UUID.randomUUID();

cache.invoke("myKey", (entry, arguments) -> {
    entry.setValue((UUID)arguments[0]);

    return null;
}, uuid);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
void CacheInvoke()
{
    var ignite = Ignition.Start();
    var cache = ignite.GetOrCreateCache<string, Guid>("myCache");

    var uuid = Guid.NewGuid();
    var proc = new Processor();

    cache.Invoke("myKey", proc, uuid);
}

class Processor : ICacheEntryProcessor<string, Guid, Guid, Guid>
{
    public Guid Process(IMutableCacheEntry<string, Guid> entry, Guid arg)
    {
        entry.Value = arg;
        return entry.Value;
    }
}
```
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
