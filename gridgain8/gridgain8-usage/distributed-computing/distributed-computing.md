---
description: >-
  GridGain's distributed computing API distributes tasks across cluster nodes, with support for runnables, callables, closures, broadcasting, and asynchronous execution.
---

# Distributed Computing

GridGain provides an API for distributing computations across cluster nodes in a balanced and fault-tolerant manner. You can submit individual tasks for execution as well as implement the MapReduce pattern with automatic task splitting. The API provides fine-grained control over the [job distribution strategy](load-balancing.md).

## Getting the Compute Interface

The main entry point for running distributed computations is the compute interface, which can be obtained from an instance of `Ignite`.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

IgniteCompute compute = ignite.compute();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();
var compute = ignite.GetCompute();
```
{% endtab %}
{% tab title="C++" %}
```cpp
Ignite ignite = Ignition::Start(cfg);

Compute compute = ignite.GetCompute();
```
{% endtab %}
{% endtabs %}

The compute interface provides methods for distributing different types of tasks over cluster nodes and running [collocated computations](../colocating-computations.md).

## Specifying the Set of Nodes for Computations

Each instance of the compute interface is associated with a [set of nodes](cluster-groups.md) on which the tasks are executed.
When called without arguments, `ignite.compute()` returns the compute interface that is associated with all server nodes.
To obtain an instance for a specific subset of nodes, use `Ignite.compute(ClusterGroup group)`.
In the following example, the compute interface is bound to the remote nodes only, i.e. all nodes except for the one that runs this code.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

IgniteCompute compute = ignite.compute(ignite.cluster().forRemotes());
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();
var compute = ignite.GetCluster().ForRemotes().GetCompute();
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Executing Tasks

GridGain provides three interfaces that can be implemented to represent a task and executed via the compute interface:

- `IgniteRunnable` — an extension of `java.lang.Runnable` that can be used to implement calculations that do not have input parameters and return no result.
- `IgniteCallable` — an extension of `java.util.concurrent.Callable` that returns a specific value.
- `IgniteClosure` — a functional interface that accepts a parameter and returns a value.

You can execute a task once (on one of the nodes) or broadcast it to all nodes.

{% hint style="warning" %}
In order to run tasks on the remote nodes, make sure the class definitions of the tasks are available on the nodes.
You can do this in two ways:

- Add the classes to the classpath of the nodes;
- Enable [peer class loading](../code-deployment/peer-class-loading.md).
{% endhint %}

### Executing a Runnable Task

To execute a runnable task, use the `run(...)` method of the compute interface. The task is sent to one of the nodes associated with the compute instance.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCompute compute = ignite.compute();

// Iterate through all words and print
// each word on a different cluster node.
for (String word : "Print words on different cluster nodes".split(" ")) {
    compute.run(() -> System.out.println(word));
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class PrintWordAction : IComputeAction
{
    public void Invoke()
    {
        foreach (var s in "Print words on different cluster nodes".Split(" "))
        {
            Console.WriteLine(s);
        }
    }
}

public static void ComputeRunDemo()
{
    var ignite = Ignition.Start(
        new IgniteConfiguration
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
        }
    );
    ignite.GetCompute().Run(new PrintWordAction());
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
/*
 * Function class.
 */
class PrintWord : public compute::ComputeFunc<void>
{
    friend struct ignite::binary::BinaryType<PrintWord>;
public:
    /*
     * Default constructor.
     */
    PrintWord()
    {
        // No-op.
    }    
    
    /*
     * Constructor.
     *
     * @param text Text.
     */
    PrintWord(const std::string& word) :
        word(word)
    {
        // No-op.
    }

    /**
     * Callback.
     */
    virtual void Call()
    {
        std::cout << word << std::endl;
    }

    /** Word to print. */
    std::string word;

};

/**
 * Binary type structure. Defines a set of functions required for type to be serialized and deserialized.
 */
namespace ignite
{
    namespace binary
    {
        template<>
        struct BinaryType<PrintWord>
        {
            static int32_t GetTypeId()
            {
                return GetBinaryStringHashCode("PrintWord");
            }

            static void GetTypeName(std::string& dst)
            {
                dst = "PrintWord";
            }

            static int32_t GetFieldId(const char* name)
            {
                return GetBinaryStringHashCode(name);
            }

            static int32_t GetHashCode(const PrintWord& obj)
            {
                return 0;
            }

            static bool IsNull(const PrintWord& obj)
            {
                return false;
            }

            static void GetNull(PrintWord& dst)
            {
                dst = PrintWord("");
            }

            static void Write(BinaryWriter& writer, const PrintWord& obj)
            {
                writer.RawWriter().WriteString(obj.word);
            }

            static void Read(BinaryReader& reader, PrintWord& dst)
            {
                dst.word = reader.RawReader().ReadString();
            }
        };
    }
}

int main()
{
    IgniteConfiguration cfg;
    cfg.springCfgPath = "/path/to/configuration.xml";

    Ignite ignite = Ignition::Start(cfg);

    // Get binding instance.
    IgniteBinding binding = ignite.GetBinding();

    // Registering our class as a compute function.
    binding.RegisterComputeFunc<PrintWord>();

    // Get compute instance.
    compute::Compute compute = ignite.GetCompute();

    std::istringstream iss("Print words on different cluster nodes");
    std::vector<std::string> words((std::istream_iterator<std::string>(iss)),
        std::istream_iterator<std::string>());

    // Iterate through all words and print
    // each word on a different cluster node.
    for (std::string word : words)
    {
        // Run compute task.
        compute.Run(PrintWord(word));
    }
}
```
{% endtab %}
{% endtabs %}

### Executing a Callable Task

To execute a callable task, use the `call(...)` method of the compute interface.

{% tabs %}
{% tab title="Java" %}
```java
Collection<IgniteCallable<Integer>> calls = new ArrayList<>();

// Iterate through all words in the sentence and create callable jobs.
for (String word : "How many characters".split(" "))
    calls.add(word::length);

// Execute the collection of callables on the cluster.
Collection<Integer> res = ignite.compute().call(calls);

// Add all the word lengths received from cluster nodes.
int total = res.stream().mapToInt(Integer::intValue).sum();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class CharCounter : IComputeFunc<int>
{
    private readonly string arg;

    public CharCounter(string arg)
    {
        this.arg = arg;
    }

    public int Invoke()
    {
        return arg.Length;
    }
}

public static void ComputeFuncDemo()
{
    var ignite = Ignition.Start(
        new IgniteConfiguration
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
        }
    );

    // Iterate through all words in the sentence and create callable jobs.
    var calls = "How many characters".Split(" ").Select(s => new CharCounter(s)).ToList();

    // Execute the collection of calls on the cluster.
    var res = ignite.GetCompute().Call(calls);

    // Add all the word lengths received from cluster nodes.
    var total = res.Sum();
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
/*
 * Function class.
 */
class CountLength : public compute::ComputeFunc<int32_t>
{
    friend struct ignite::binary::BinaryType<CountLength>;
public:
    /*
     * Default constructor.
     */
    CountLength()
    {
        // No-op.
    }

    /*
     * Constructor.
     *
     * @param text Text.
     */
    CountLength(const std::string& word) :
        word(word)
    {
        // No-op.
    }

    /**
     * Callback.
     * Counts number of characters in provided word.
     *
     * @return Word's length.
     */
    virtual int32_t Call()
    {
        return word.length();
    }

    /** Word to print. */
    std::string word;

};

/**
 * Binary type structure. Defines a set of functions required for type to be serialized and deserialized.
 */
namespace ignite
{
    namespace binary
    {
        template<>
        struct BinaryType<CountLength>
        {
            static int32_t GetTypeId()
            {
                return GetBinaryStringHashCode("CountLength");
            }

            static void GetTypeName(std::string& dst)
            {
                dst = "CountLength";
            }

            static int32_t GetFieldId(const char* name)
            {
                return GetBinaryStringHashCode(name);
            }

            static int32_t GetHashCode(const CountLength& obj)
            {
                return 0;
            }

            static bool IsNull(const CountLength& obj)
            {
                return false;
            }

            static void GetNull(CountLength& dst)
            {
                dst = CountLength("");
            }

            static void Write(BinaryWriter& writer, const CountLength& obj)
            {
                writer.RawWriter().WriteString(obj.word);
            }

            static void Read(BinaryReader& reader, CountLength& dst)
            {
                dst.word = reader.RawReader().ReadString();
            }
        };
    }
}

int main()
{
    IgniteConfiguration cfg;
    cfg.springCfgPath = "/path/to/configuration.xml";

    Ignite ignite = Ignition::Start(cfg);

    // Get binding instance.
    IgniteBinding binding = ignite.GetBinding();

    // Registering our class as a compute function.
    binding.RegisterComputeFunc<CountLength>();

    // Get compute instance.
    compute::Compute compute = ignite.GetCompute();

    std::istringstream iss("How many characters");
    std::vector<std::string> words((std::istream_iterator<std::string>(iss)),
        std::istream_iterator<std::string>());

    int32_t total = 0;

    // Iterate through all words in the sentence, create and call jobs.
    for (std::string word : words)
    {
        // Add word length received from cluster node.
        total += compute.Call<int32_t>(CountLength(word));
    }
}
```
{% endtab %}
{% endtabs %}

### Executing an IgniteClosure

To execute an `IgniteClosure`, use the `apply(...)` method of the compute interface. The method accepts a task and an input parameter for the task. The parameter is passed to the given `IgniteClosure` at the execution time.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCompute compute = ignite.compute();

// Execute closure on all cluster nodes.
Collection<Integer> res = compute.apply(String::length, Arrays.asList("How many characters".split(" ")));

// Add all the word lengths received from cluster nodes.
int total = res.stream().mapToInt(Integer::intValue).sum();
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class CharCountingFunc : IComputeFunc<string, int>
{
    public int Invoke(string arg)
    {
        return arg.Length;
    }
}

public static void Foo()
{
    var ignite = Ignition.Start(
        new IgniteConfiguration
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
        }
    );

    var res = ignite.GetCompute().Apply(new CharCountingFunc(), "How many characters".Split());

    int total = res.Sum();
}
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Broadcasting a Task

The `broadcast()` method executes a task on _all nodes_ associated with the compute instance.

{% tabs %}
{% tab title="Java" %}
```java
// Limit broadcast to remote nodes only.
IgniteCompute compute = ignite.compute(ignite.cluster().forRemotes());

// Print out hello message on remote nodes in the cluster group.
compute.broadcast(() -> System.out.println("Hello Node: " + ignite.cluster().localNode().id()));
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class PrintNodeIdAction : IComputeAction
{
    public void Invoke()
    {
        Console.WriteLine("Hello node: " +
                          Ignition.GetIgnite().GetCluster().GetLocalNode().Id);
    }
}

public static void BroadcastDemo()
{
    var ignite = Ignition.Start(
        new IgniteConfiguration
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
        }
    );

    // Limit broadcast to remote nodes only.
    var compute = ignite.GetCluster().ForRemotes().GetCompute();
    // Print out hello message on remote nodes in the cluster group.
    compute.Broadcast(new PrintNodeIdAction());
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
/*
 * Function class.
 */
class Hello : public compute::ComputeFunc<void>
{
    friend struct ignite::binary::BinaryType<Hello>;
public:
    /*
     * Default constructor.
     */
    Hello()
    {
        // No-op.
    }

    /**
     * Callback.
     */
    virtual void Call()
    {
        std::cout << "Hello" << std::endl;
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
        struct BinaryType<Hello>
        {
            static int32_t GetTypeId()
            {
                return GetBinaryStringHashCode("Hello");
            }

            static void GetTypeName(std::string& dst)
            {
                dst = "Hello";
            }

            static int32_t GetFieldId(const char* name)
            {
                return GetBinaryStringHashCode(name);
            }

            static int32_t GetHashCode(const Hello& obj)
            {
                return 0;
            }

            static bool IsNull(const Hello& obj)
            {
                return false;
            }

            static void GetNull(Hello& dst)
            {
                dst = Hello();
            }

            static void Write(BinaryWriter& writer, const Hello& obj)
            {
                // No-op.
            }

            static void Read(BinaryReader& reader, Hello& dst)
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

    Ignite ignite = Ignition::Start(cfg);

    // Get binding instance.
    IgniteBinding binding = ignite.GetBinding();

    // Registering our class as a compute function.
    binding.RegisterComputeFunc<Hello>();

    // Broadcast to all nodes.
    compute::Compute compute = ignite.GetCompute();

    // Declaring function instance.
    Hello hello;

    // Print out hello message on nodes in the cluster group.
    compute.Broadcast(hello);
}
```
{% endtab %}
{% endtabs %}

### Asynchronous Execution

All methods described in the previous sections have asynchronous counterparts:

- `callAsync(...)`
- `runAsync(...)`
- `applyAsync(...)`
- `broadcastAsync(...)`

The asynchronous methods return an `IgniteFuture` that represents the result of the operation. In the following example, a collection of callable tasks is executed asynchronously.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCompute compute = ignite.compute();

Collection<IgniteCallable<Integer>> calls = new ArrayList<>();

// Iterate through all words in the sentence and create callable jobs.
for (String word : "Count characters using a callable".split(" "))
    calls.add(word::length);

IgniteFuture<Collection<Integer>> future = compute.callAsync(calls);

future.listen(fut -> {
    // Total number of characters.
    int total = fut.get().stream().mapToInt(Integer::intValue).sum();

    System.out.println("Total number of characters: " + total);
});
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class CharCounter : IComputeFunc<int>
{
    private readonly string arg;

    public CharCounter(string arg)
    {
        this.arg = arg;
    }

    public int Invoke()
    {
        return arg.Length;
    }
}
public static void AsyncDemo()
{
    var ignite = Ignition.Start(
        new IgniteConfiguration
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
        }
    );

    var calls = "Count character using async compute"
        .Split(" ").Select(s => new CharCounter(s)).ToList();

    var future = ignite.GetCompute().CallAsync(calls);

    future.ContinueWith(fut =>
    {
        var total = fut.Result.Sum();
        Console.WriteLine("Total number of characters: " + total);
    });
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
/*
 * Function class.
 */
class CountLength : public compute::ComputeFunc<int32_t>
{
    friend struct ignite::binary::BinaryType<CountLength>;
public:
    /*
     * Default constructor.
     */
    CountLength()
    {
        // No-op.
    }

    /*
     * Constructor.
     *
     * @param text Text.
     */
    CountLength(const std::string& word) :
        word(word)
    {
        // No-op.
    }

    /**
     * Callback.
     * Counts number of characters in provided word.
     *
     * @return Word's length.
     */
    virtual int32_t Call()
    {
        return word.length();
    }

    /** Word to print. */
    std::string word;

};

/**
 * Binary type structure. Defines a set of functions required for type to be serialized and deserialized.
 */
namespace ignite
{
    namespace binary
    {
        template<>
        struct BinaryType<CountLength>
        {
            static int32_t GetTypeId()
            {
                return GetBinaryStringHashCode("CountLength");
            }

            static void GetTypeName(std::string& dst)
            {
                dst = "CountLength";
            }

            static int32_t GetFieldId(const char* name)
            {
                return GetBinaryStringHashCode(name);
            }

            static int32_t GetHashCode(const CountLength& obj)
            {
                return 0;
            }

            static bool IsNull(const CountLength& obj)
            {
                return false;
            }

            static void GetNull(CountLength& dst)
            {
                dst = CountLength("");
            }

            static void Write(BinaryWriter& writer, const CountLength& obj)
            {
                writer.RawWriter().WriteString(obj.word);
            }

            static void Read(BinaryReader& reader, CountLength& dst)
            {
                dst.word = reader.RawReader().ReadString();
            }
        };
    }
}

int main()
{
    IgniteConfiguration cfg;
    cfg.springCfgPath = "/path/to/configuration.xml";

    Ignite ignite = Ignition::Start(cfg);

    // Get binding instance.
    IgniteBinding binding = ignite.GetBinding();

    // Registering our class as a compute function.
    binding.RegisterComputeFunc<CountLength>();

    // Get compute instance.
    compute::Compute asyncCompute = ignite.GetCompute();

    std::istringstream iss("Count characters using callable");
    std::vector<std::string> words((std::istream_iterator<std::string>(iss)),
        std::istream_iterator<std::string>());

    std::vector<Future<int32_t>> futures;

    // Iterate through all words in the sentence, create and call jobs.
    for (std::string word : words)
    {
        // Counting number of characters remotely.
        futures.push_back(asyncCompute.CallAsync<int32_t>(CountLength(word)));
    }

    int32_t total = 0;

    // Counting total number of characters.
    for (Future<int32_t> future : futures)
    {
        // Waiting for results.
        future.Wait();

        total += future.GetValue();
    }

    // Printing result.
    std::cout << "Total number of characters: " << total << std::endl;
}
```
{% endtab %}
{% endtabs %}

## Task Execution Timeout

You can set a timeout for task execution.
If the task does not finish within the given time frame, it be stopped and all jobs produced by this task are cancelled.

To execute a task with a timeout, use the `withTimeout(...)` method of the compute interface.
The method returns a compute interface that executes the first task given to it in a time-limited manner.
Consequent tasks do not have a timeout: you need to call `withTimeout(...)` for every task that should have a timeout.

{% code title="Java" %}
```java
IgniteCompute compute = ignite.compute();

compute.withTimeout(300_000).run(() -> {
    // your computation
    // ...
});
```
{% endcode %}

## Sharing State Between Jobs on Local Node

It is often useful to share a state between different compute jobs executed on one node. For this purpose, there is a shared concurrent local map available on each node.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCluster cluster = ignite.cluster();

ConcurrentMap<String, Integer> nodeLocalMap = cluster.nodeLocalMap();
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Node-local values are similar to thread local variables in that these values are not distributed and kept only on the local node.
Node-local data can be used to share the state between compute jobs.
It can also be used by deployed services.

In the following example, a job increments a node-local counter every time it executes on some node. As a result, the node-local counter on each node tells us how many times the job has executed on that node.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCallable<Long> job = new IgniteCallable<Long>() {
    @IgniteInstanceResource
    private Ignite ignite;

    @Override
    public Long call() {
        // Get a reference to node local.
        ConcurrentMap<String, AtomicLong> nodeLocalMap = ignite.cluster().nodeLocalMap();

        AtomicLong cntr = nodeLocalMap.get("counter");

        if (cntr == null) {
            AtomicLong old = nodeLocalMap.putIfAbsent("counter", cntr = new AtomicLong());

            if (old != null)
                cntr = old;
        }

        return cntr.incrementAndGet();
    }
};
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Accessing Data from Computational Tasks

If your computational task needs to access the data stored in caches, you can do it via the instance of `Ignite`:

{% tabs %}
{% tab title="Java" %}
```java
public class MyCallableTask implements IgniteCallable<Integer> {

    @IgniteInstanceResource
    private Ignite ignite;

    @Override
    public Integer call() throws Exception {

        IgniteCache<Long, Person> cache = ignite.cache("person");

        // Get the data you need
        Person person = cache.get(1L);

        // do with the data what you need to do

        return 1;
    }
}
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
class FuncWithDataAccess : IComputeFunc<int>
{
    [InstanceResource] private IIgnite _ignite;

    public int Invoke()
    {
        var cache = _ignite.GetCache<int, string>("someCache");

        // get the data you need
        string cached = cache.Get(1);
                
        // do with data what you need to do, for example:
        Console.WriteLine(cached);

        return 1;
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
/*
 * Function class.
 */
class GetValue : public compute::ComputeFunc<void>
{
    friend struct ignite::binary::BinaryType<GetValue>;
public:
    /*
     * Default constructor.
     */
    GetValue()
    {
        // No-op.
    }

    /**
     * Callback.
     */
    virtual void Call()
    {
        Ignite& node = GetIgnite();

        // Get the data you need
        Cache<int64_t, Person> cache = node.GetCache<int64_t, Person>("person");

        // do with the data what you need to do
        Person person = cache.Get(1);
    }
};
```
{% endtab %}
{% endtabs %}

Note that the example shown above may not be the most effective way.
The reason is that the person object that corresponds to key `1` may be located on a node that is different from the node where the task is executed.
In this case, the object is fetched via network. This can be avoided by [colocating the task with the data](../colocating-computations.md).

{% hint style="warning" %}
If you want to use the key and value objects inside `IgniteCallable` and `IgniteRunnable` tasks, make sure the key and value classes are deployed on all cluster nodes.
{% endhint %}

## Enabling Extended Support

By default, a number of internal properties and parameters are not exposed to the user and run at default settings. Use the `@ComputeTaskSessionFullSupport` annotation to access all [ComputeTaskSession](https://www.gridgain.com/sdk/ee/latest/javadoc/org/apache/ignite/compute/ComputeTaskSession.html) attributes. With it, you can work with task attributes, for example, change tasks priorities or set up a listener for events.

{% code title="Java" %}
```java
// Exposing additional attributes.
@ComputeTaskSessionFullSupport
public static class AttrCompute implements ComputeTask<String, String> {
    @TaskSessionResource
    private ComputeTaskSession ses;

    // Temporary storage.
    private Map<String, String> attrs = new HashMap<>();

    // A method for setting attributes.
    public void setAttribute(String key, String val) {
        attrs.put(key, val);
    }

    @Override
    public Map<? extends ComputeJob, ClusterNode> map(List<ClusterNode> subgrid, String arg) throws IgniteException {
        ses.setAttributes(attrs);

        ClusterNode node = subgrid.get(0);

        return Collections.singletonMap(new ComputeJobAdapter(arg) {
            /** Ignite instance. */
            @IgniteInstanceResource
            private Ignite ignite;

                @Override
                public Serializable execute() {

                // This job does not return any result.
                return "OK";
            }
        }, node);
    }

    @Override
    public ComputeJobResultPolicy result(ComputeJobResult res, List<ComputeJobResult> rcvd) throws IgniteException {
        return ComputeJobResultPolicy.WAIT;
    }

    @Override
    public String reduce(List<ComputeJobResult> results) throws IgniteException {
        return ses.getAttributes().toString();
    }
}
```
{% endcode %}

## Other Distributed Computing Interfaces

GridGain also provides a number of interfaces that can be used to provide additional control over how your distributed computing tasks are executed:

- The scope of the nodes used in the execution can be adjusted by using the [ClusterGroup](cluster-groups.md) interface;
- Tasks can be submitted to the server node to be automatically distributed across the cluster by using the [ExecutorService](executor-service.md) interface;
- The `ComputeTask` interface can be used to implement custom map and reduce logic as described in the [MapReduce API](map-reduce.md) topic;
- GridGain handles load balancing automatically, but you can adjust the type of load balancing used and the balancing configuration by using the [loadBalancingSpi](load-balancing.md);
- GridGain reroutes failed jobs to other nodes by default. You can change the [failoverSpi](fault-tolerance.md) property to handle failed jobs in a different way;
- Job priority can be configured by using the [CollisionSpi](job-scheduling.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
