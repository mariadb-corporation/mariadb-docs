---
hidden: true
description: >-
  How to use the GridGain 8 Java thin client: connecting to a cluster, partition awareness, key-value and SQL APIs, transactions, compute, services, data streaming, SSL/TLS, and authentication.
---

# Java Thin Client

## Overview

The Java thin client is a lightweight client that connects to the cluster via a standard socket connection. It does not become a part of the cluster topology, never holds any data, and is not used as a destination for compute calculations. The thin client simply establishes a socket connection to a standard node​ and performs all operations through that node.

To start a single node cluster that you can use to run examples, refer to the [Java Quick Start Guide](https://www.gridgain.com/docs/gridgain8/latest/getting-started/quick-start/java).

The Java thin client supports a variety of data structures, including [atomicLong](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-structures/atomic-types), [set](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-structures/queue-and-set), etc.

## Setting Up

If you use maven or gradle, add the `ignite-core` dependency to your application:

{% tabs %}
{% tab title="Maven" %}
```xml
<properties>
    <ignite.version>8.10</ignite.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-core</artifactId>
        <version>${ignite.version}</version>
    </dependency>
</dependencies>
```
{% endtab %}

{% tab title="Gradle" %}
```groovy
def igniteVersion = '8.10'

dependencies {
    compile group: 'org.gridgain', name: 'ignite-core', version: igniteVersion
}
```
{% endtab %}
{% endtabs %}

Alternatively, you can use the `ignite-core-8.10.jar` library from the GridGain distribution package.

## Connecting to Cluster

To initialize a thin client, use the `Ignition.startClient(ClientConfiguration)` method. The method accepts a `ClientConfiguration` object, which defines client connection parameters.

The method returns the `IgniteClient` interface, which provides various methods for accessing data. `IgniteClient` is an auto-closable resource. Use the _try-with-resources_ statement to close the thin client and release the resources associated with the connection.

```java
ClientConfiguration cfg = new ClientConfiguration().setAddresses("127.0.0.1:10800");
try (IgniteClient client = Ignition.startClient(cfg)) {
    ClientCache<Integer, String> cache = client.cache("myCache");
    // Get data from the cache
}
```

You can provide addresses of multiple nodes. In this case, the thin client randomly tries all the servers in the list and throws `ClientConnectionException` if none is available.

```java
try (IgniteClient client = Ignition.startClient(new ClientConfiguration().setAddresses("node1_address:10800",
        "node2_address:10800", "node3_address:10800"))) {
} catch (ClientConnectionException ex) {
    // All the servers are unavailable
}
```

Note that the code above provides a failover mechanism in case of server node failures but with a caveat that cache queries may return duplicate results. Refer to the [Handling Node Failures](#handling-node-failures) section for more information.

### Automatic Server Node Discovery

Thin clients connect to one or more servers. The set of endpoints is defined in `ClientConfiguration` and cannot change after a client starts. However, clusters can change their topology dynamically: nodes can start and stop, IP addresses can change, etc. To account for that, thin clients can discover server nodes automatically when connected to any of them, and maintain an up to date list of servers at all times.

The automatic node discovery is enabled by default. To disable this behavior, set the `ClientConfiguration.clusterDiscoveryEnabled` property to "false".

The client performs the discovery as follows:

1. Connects to one or more endpoints from `ClientConfiguration`.
2. Retrieves the current topology.
3. Connects to every server from Step 2 it hasn't connected to before:
   1. Uses node UUID to make sure it doesn't connect to the same node twice.
   2. Drops the connection in case of a UUID mismatch.
4. For every response to every operation, compares the topology version from the header to the topology version from Step 2.
5. Connects to the newly discovered servers, removes connections to the removed servers.
6. Repeats Step 4.

Server discovery is an asynchronous process - it happens in the background. Moreover, thin client receives topology updates only when it performs operations (to minimize server load and network traffic from idle connections).

{% hint style="danger" %}
We recommend disabling server node discovery if servers reside on a different subnet (behind a NAT server or a proxy, in a different cloud, etc.).
Server nodes provide their addresses and ports to the client, but when the client is in a different subnet, those addresses won't work.
{% endhint %}

### DNS Address Resolution

When you configure addresses as host names, the client resolves each host name through DNS and uses every returned IP address as a separate endpoint. One host name that maps to several nodes therefore produces one endpoint per resolved address.

DNS records may change as nodes start and stop. To pick up those changes, the client re-resolves the configured host names in the background and connects to newly discovered addresses. Set the interval with the `ClientConfiguration.backgroundReResolveAddressesInterval` property, in milliseconds. The default is 30000, or 30 seconds. Set it to `0` to turn background re-resolution off.

```java
ClientConfiguration cfg = new ClientConfiguration()
        .setAddresses("gridgain-service.default.svc.cluster.local:10800")
        .setClusterDiscoveryEnabled(false)
        .setBackgroundReResolveAddressesInterval(10_000);
```

Background re-resolution runs only when all of the following are true:

- Automatic node discovery is off. When discovery is on, the client uses the endpoints that the servers report instead.
- `backgroundReResolveAddressesInterval` is greater than `0`.
- You have not set a custom address finder, or the finder you set is a `DnsClientAddressFinder`. See [Partition Awareness](#partition-awareness) for details on address finders.

Addresses accept the same formats as `ClientConfiguration.setAddresses()`: `host`, `host:port`, `host:portFrom..portTo`, an IPv4 or IPv6 literal, and `[ipv6]:port`. If you omit the port, the client uses the default port 10800. A host name that fails to resolve is used as it is, so a temporary DNS outage does not break a working configuration.

{% hint style="info" %}
DNS resolution and background re-resolution apply to the Java thin client only.
{% endhint %}

### Host Names and TLS

By default, server nodes advertise their IP addresses during discovery.
If clients must connect using host names (for example, when TLS is enabled and certificates contain host names),
configure each server node to advertise its host name by setting `IgniteConfiguration#localHost` on the **server** side.

```java
IgniteConfiguration cfg = new IgniteConfiguration()
        .setLocalHost("my-server1-hostname");
```

### Connection Timeouts

You can configure two independent timeouts:

- **Handshake timeout** — the maximum time to establish a connection to a server node, including protocol negotiation. Set it with `ClientConfiguration.setHandshakeTimeout(int)`.
- **Request timeout** — the maximum time to wait for a response to an individual operation on an established connection. Set it with `ClientConfiguration.setRequestTimeout(int)`.

Both values are in milliseconds, and `0` (the default) means no timeout. Setting them separately lets you allow a longer window to connect while keeping a tighter bound on each operation.

```java
ClientConfiguration cfg = new ClientConfiguration()
        .setAddresses("127.0.0.1:10800")
        .setHandshakeTimeout(10_000)
        .setRequestTimeout(5_000);
```

{% hint style="info" %}
The single `setTimeout(int)`/`getTimeout()` property is deprecated. `setTimeout(value)` now applies `value` to both the handshake and request timeouts, so existing configurations keep working. Migrate to `setHandshakeTimeout` and `setRequestTimeout` to tune the two phases independently.
{% endhint %}

## Client Atomic Sequence

_Atomic sequence_ is a suitable and efficient data structure for the implementation of a distributed ID generator. For instance, such a generator can be used to produce unique primary keys across the whole cluster.

Here is an example of how atomic sequence can be created:

```java
IgniteClient client = Ignition.startClient(...);

ClientAtomicSequence seq = client.atomicSequence(
        "seqName", // Sequence name.
        0,       // Initial value for sequence.
        true     // Create if it does not exist.
);

// Increment atomic sequence.
for (int i = 0; i < 20; i++) {
    long currentValue = seq.get();
    long newValue = seq.incrementAndGet();

    ...
}
```

## Partition Awareness

{% include "../.gitbook/includes/gg8-partition-awareness.md" %}

The partition awareness functionality helps avoid an additional network hop in the following scenarios:

- Single-key operations API, like put(), get(), etc.

- Bulk key operations, like getAll(), which group the requested keys by their primary node and send each group directly to the owning node in a single request.

- ScanQuery and IndexQuery accept a partition number as a parameter with which the query is routed to a server node that stores the requested data. Refer to [Executing Scan Queries](#executing-scan-queries) and [Executing Index Queries](https://ignite.apache.org/docs/latest/key-value-api/using-cache-queries#executing-index-queries) sections for more information.

The following code sample illustrates how to use the partition awareness feature with the java thin client.

```java
ClientConfiguration cfg = new ClientConfiguration()
        .setAddresses("node1_address:10800", "node2_address:10800", "node3_address:10800")
        .setAffinityAwarenessEnabled(true);

try (IgniteClient client = Ignition.startClient(cfg)) {
    ClientCache<Integer, String> cache = client.cache("myCache");
    // Put, get or remove data from the cache...
} catch (ClientException e) {
    System.err.println(e.getMessage());
}
```

If a list of server nodes is dynamically changing or scaling, then it is possible to configure the connection with custom implementation of `ClientAddressFinder`. It should provide a number of current server addresses every time a client asks for them.
The following code sample illustrates how to use it.

```java
ClientAddressFinder finder = () -> {
    String[] dynamicServerAddresses = fetchServerAddresses();

    return dynamicServerAddresses;
};

ClientConfiguration cfg = new ClientConfiguration()
    .setAddressesFinder(finder)
    .setAffinityAwarenessEnabled(true);

try (IgniteClient client = Ignition.startClient(cfg)) {
    ClientCache<Integer, String> cache = client.cache("myCache");
    // Put, get, or remove data from the cache...
} catch (ClientException e) {
    System.err.println(e.getMessage());
}
```

The code snippet shows how an example implementation might look like if you want clients to retrieve server addresses dynamically.

- The `ClientAddressFinder` is a functional interface that provides the only method `getAddresses()`.
- The `fetchServerAddress()` is a custom function that dynamically provides server addresses.
- Configure client with `ClientConfiguration.setAddressesFinder(finder)`.

If your addresses change only because of DNS updates, you do not need a custom finder. The client uses the built-in `DnsClientAddressFinder` when you leave the finder unset. See [DNS Address Resolution](#dns-address-resolution).

Also, you can check a [real example](https://github.com/apache/ignite/blob/master/examples/src/main/java/org/apache/ignite/examples/client/ClientKubernetesPutGetExample.java#L50) of the interface implementation. `ThinClientKubernetesAddressFinder` is created to handle scalable Kubernetes environment.

## Affinity Function

You can configure affinity function for caches created from thin clients.

The following limitations apply when configuring it from thin clients:

- Only `RendezvousAffinityFunction` is supported.
- `BackupFilter` configuration is not supported.

To apply these properties, set them from a thick client.

The example below sets the custom affinity function and creates a cache on the server:

```java
try (IgniteClient client = Ignition.startClient(clientCfg)) {
    RendezvousAffinityFunction aff = new RendezvousAffinityFunction()
            .setPartitions(512)
            .setExcludeNeighbors(true);

    ClientCacheConfiguration cacheCfg = new ClientCacheConfiguration()
            .setAffinity(aff)
            .setName("custom-affinity-cache");

    ClientCache<Object, Object> cache = client.createCache(cacheCfg);
}
```

## Using Key-Value API

The Java thin client supports most of the key-value operations available in the thick client.
To execute key-value operations on a specific cache, you need to get an instance of the cache and use one of its methods.

### Getting a Cache Instance

The `ClientCache` interface provides the key-value API. You can use the following methods to obtain an instance of `ClientCache`:

- `IgniteClient.cache(String)`: assumes a cache with the specified name exists. The method does not communicate with the cluster to check if the cache really exists. Subsequent cache operations fail if the cache does not exist.
- `IgniteClient.getOrCreateCache(String)`, `IgniteClient.getOrCreateCache(ClientCacheConfiguration)`: get existing cache with the specified name or create the cache if it does not exist. The former operation creates a cache with default configuration.
- `IgniteClient.createCache(String)`, `IgniteClient.createCache(ClientCacheConfiguration)`: create a cache with the specified name and fail if the cache already exists.

Use `IgniteClient.cacheNames()` to list all existing caches.

```java
ClientCacheConfiguration cacheCfg = new ClientCacheConfiguration().setName("References")
        .setCacheMode(CacheMode.REPLICATED)
        .setWriteSynchronizationMode(CacheWriteSynchronizationMode.FULL_SYNC);

ClientCache<Integer, String> cache = client.getOrCreateCache(cacheCfg);
```

### Destroying Caches

To destroy a single cache and remove all of its data from the cluster, use `IgniteClient.destroyCache(String)`. This deallocates all resources associated with the cache on every node in the cluster and cannot be undone.

To destroy several caches at once, use `IgniteClient.destroyCaches(Collection<String>)` or its asynchronous counterpart `IgniteClient.destroyCachesAsync(Collection<String>)`.
The client removes all of the listed caches in a single request, which reduces the cluster-side overhead compared to destroying the caches one by one in a loop.

```java
// Destroy a single cache.
client.destroyCache("myCache");

// Destroy multiple caches in a single request.
client.destroyCaches(Arrays.asList("cache1", "cache2", "cache3"));
```

{% hint style="info" %}
Destroying a cache is irreversible: the data cannot be recovered afterwards.

If the collection is `null` or contains a `null` or empty cache name, `destroyCaches()` throws `IllegalArgumentException` and no caches are destroyed.
If any of the specified caches does not exist, it throws `ClientException`.
{% endhint %}

### Basic Cache Operations

The following code snippet demonstrates how to execute basic cache operations from the thin client.

```java
Map<Integer, String> data = IntStream.rangeClosed(1, 100).boxed()
        .collect(Collectors.toMap(i -> i, Object::toString));

cache.putAll(data);

assert !cache.replace(1, "2", "3");
assert "1".equals(cache.get(1));
assert cache.replace(1, "1", "3");
assert "3".equals(cache.get(1));

cache.put(101, "101");

cache.removeAll(data.keySet());
assert cache.size() == 1;
assert "101".equals(cache.get(101));

cache.removeAll();
assert 0 == cache.size();
```

### Skipping Cache Store

When [cache store](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/persistence/external-storage) is set up, cache operations always read from and write to that storage. In certain scenarios, you may need to bypass it instead. For this, use the `ClientCache.withSkipStore()` method to get a cache instance that bypasses cache store.

The example below shows how you can set it up:

```java
ClientCache<Integer, String> cache = client.cache("myCache");

// Reads and writes go through the cache store.
cache.put(1, "1");

ClientCache<Integer, String> cacheSkipStore = cache.withSkipStore();

// The cache store is not updated.
cacheSkipStore.put(2, "2");

// Entries that exist only in the cache store are not loaded: returns null.
cacheSkipStore.get(3);
```

The method returns a new cache instance and does not modify the original one, so you can keep using both. You can combine `withSkipStore()` with `withKeepBinary()` and `withExpiryPolicy()` methods.

### Getting the Cache Size

Use `ClientCache.sizeLong()` to get the number of entries in a cache as a `long` value. By default, if you do not provide a peek mode, the method returns the number of primary copies across all nodes, which is equivalent to passing `CachePeekMode.PRIMARY`. This is a distributed operation that queries all participating nodes.

```java
long size = cache.sizeLong();

// Number of backup entries across all nodes
long backups = cache.sizeLong(CachePeekMode.BACKUP);
```

An asynchronous variant, `sizeLongAsync()`, returns an `IgniteClientFuture<Long>`. See [Async APIs](#async-apis).

{% hint style="info" %}
The `size()` and `sizeAsync()` methods, which return an `int`, are deprecated. Use `sizeLong()` and `sizeLongAsync()` instead. For a cache with more than `Integer.MAX_VALUE` (about 2.1 billion) entries, `size()` and `sizeAsync()` throw a `ClientException` because the result cannot be represented as an `int`.
{% endhint %}

### Entry Processor

An entry processor is used to process cache entries on the nodes where they are stored. An entry processor does not require the entry to be transferred to the client in order to perform an operation on it. The operation is performed remotely, and only the results are transmitted to the client.

Define an entry processor as follows:

```java
public class IncrementProcessor implements EntryProcessor<Integer, Integer, Integer> {
    @Override public Integer process(MutableEntry<Integer, Integer> entry, Object... arguments) {
        entry.setValue(entry.getValue() == null ? 1 : entry.getValue() + 1);
        return entry.getValue();
    }
}
```

{% hint style="info" %}
The classes of the entry processors must be available on the server nodes of the cluster.
{% endhint %}

Then invoke the entry processor:

```java
ClientCache<Integer, Integer> cache = client.getOrCreateCache("myCache");
cache.invoke(0, new IncrementProcessor());
```

### Executing Scan Queries

Use the `ScanQuery<K, V>` class to get a set of entries that satisfy a given condition. The thin client sends the query to the cluster node where it is executed as a normal [scan query](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/using-scan-queries).

The query condition is specified by an `IgniteBiPredicate<K, V>` object that is passed to the query constructor as an argument. The predicate is applied on the server side. If you don't provide any predicate, the query returns all cache entries.

{% hint style="info" %}
The classes of the predicates must be available on the server nodes of the cluster.
{% endhint %}

The results of the query are transferred to the client page by page. Each page contains a specific number of entries and is fetched to the client only when the entries from that page are requested. To change the number of entries in a page, use the `ScanQuery.setPageSize(int pageSize)` method (default value is 1024).

```java
ClientCache<Integer, Person> personCache = client.getOrCreateCache("personCache");

Query<Cache.Entry<Integer, Person>> qry = new ScanQuery<Integer, Person>(
        (i, p) -> p.getName().contains("Smith"));

try (QueryCursor<Cache.Entry<Integer, Person>> cur = personCache.query(qry)) {
    for (Cache.Entry<Integer, Person> entry : cur) {
        // Process the entry ...
    }
}
```

The `IgniteClient.query(...)` method returns an instance of `FieldsQueryCursor`. Make sure to always close the cursor after you obtain all results.

### Transactions

Client transactions are supported for caches with `AtomicityMode.TRANSACTIONAL` mode.

#### Executing Transactions

To start a transaction, obtain the `ClientTransactions` object from `IgniteClient`.
`ClientTransactions` has a number of  `txStart(...)` methods, each of which starts a new transaction and returns an object (`ClientTransaction`) that represents the transaction.
Use this object to commit or rollback the transaction.

{% hint style="info" %}
Starting with GridGain 8.10, explicit client transactions are partition aware when partition awareness is enabled (see [Partition Awareness](#partition-awareness)).
The client defers starting the transaction on the server until the first cache operation joins it, then starts the transaction on the node that owns the data accessed by that operation.
This lets the owning node coordinate the transaction and avoids an additional network hop.
No configuration or code changes are required — existing transactional code benefits automatically.
{% endhint %}

```java
ClientCache<Integer, String> cache = client.cache("my_transactional_cache");

ClientTransactions tx = client.transactions();

try (ClientTransaction t = tx.txStart()) {
    cache.put(1, "new value");

    t.commit();
}
```

#### Transaction Configuration

Client transactions can have different [concurrency modes, isolation levels](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/transactions#concurrency-modes-and-isolation-levels), and execution timeout, which can be set for all transactions or on a per transaction basis.

The `ClientConfiguration` object supports setting the default concurrency mode, isolation level, and timeout for all transactions started with this client interface.

```java
ClientConfiguration cfg = new ClientConfiguration();
cfg.setAddresses("localhost:10800");

cfg.setTransactionConfiguration(new ClientTransactionConfiguration().setDefaultTxTimeout(10000)
        .setDefaultTxConcurrency(TransactionConcurrency.OPTIMISTIC)
        .setDefaultTxIsolation(TransactionIsolation.REPEATABLE_READ));

IgniteClient client = Ignition.startClient(cfg);

```

You can specify the concurrency mode, isolation level, and timeout when starting an individual transaction.
In this case, the provided values override the default settings.

```java
ClientTransactions tx = client.transactions();
try (ClientTransaction t = tx.txStart(TransactionConcurrency.OPTIMISTIC,
        TransactionIsolation.REPEATABLE_READ)) {
    cache.put(1, "new value");
    t.commit();
}
```

### Working with Binary Objects

The thin client fully supports Binary Object API described in the [Working with Binary Objects](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/binary-objects) section.
Use `CacheClient.withKeepBinary()` to switch the cache to binary mode and start working directly with binary objects to avoid serialization/deserialization.
Use `IgniteClient.binary()` to get an instance of `IgniteBinary` and build an object from scratch.

```java
IgniteBinary binary = client.binary();

BinaryObject val = binary.builder("Person").setField("id", 1, int.class).setField("name", "Joe", String.class)
        .build();

ClientCache<Integer, BinaryObject> cache = client.cache("persons").withKeepBinary();

cache.put(1, val);

BinaryObject value = cache.get(1);
```

Refer to the [Working with Binary Objects](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/binary-objects) page for detailed information.

## Data Streaming

The Java thin client can load large volumes of data into a cache with a data streamer. The streamer
buffers entries, maps them to the primary nodes for their keys, and sends them in batches, which
keeps data movement to a minimum. Updates that fail because the cluster topology changed are
retried automatically.

Obtain a streamer from `IgniteClient.dataStreamer()` and close it when you are done. Closing flushes
any remaining data to the cache.

```java
IgniteClient client = Ignition.startClient(...);

try (ClientDataStreamer<Integer, String> streamer = client.dataStreamer("myCache")) {
    streamer.addData(1, "value1");
    streamer.addData(2, "value2");
}
```

A streamer is thread-safe, so you can add data from several threads. Entries are sent
asynchronously, so the cache can apply updates in a different order than you added them.

To remove an entry, call `removeData()`, or pass a `null` value to `addData()`.

### Data Streamer Parameters

Set these parameters before the first `addData()` call:

| Parameter | Default | Description |
| --- | --- | --- |
| `allowOverwrite` | `false` | Whether the streamer overwrites entries that already exist in the cache. The streamer performs better while this is disabled. While it is `false`, updates do not reach the cache store, because the streamer applies `skipStore` implicitly. The parameter has no effect when a custom receiver is set. |
| `skipStore` | `false` | Whether to disable write-through for streamed data. |
| `keepBinary` | `false` | Whether to pass objects to the stream receiver in binary format. |
| `perNodeBufferSize` | `512` | Number of key-value pairs buffered for each node. |
| `perNodeParallelOperations` | `4` | Maximum number of stream operations that run in parallel for a single node. |
| `autoFlushFrequency` | `0` | How often, in milliseconds, the streamer flushes buffered data. `0` disables automatic flushing. |
| `timeout` | Disabled | Maximum time, in milliseconds, to wait when adding data, flushing, or closing. |

To process streamed entries on the server with your own logic, set a stream receiver with
`receiver()`. The receiver class must already be available on the cluster nodes, because the client
does not deploy it.

For the general concepts behind data streaming, see [Data Streaming](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-streaming).

## Executing SQL Statements

The Java thin client provides a SQL API to execute SQL statements. SQL statements are declared using the `SqlFieldsQuery` objects and executed through the `IgniteClient.query(SqlFieldsQuery)` method.

```java
client.query(new SqlFieldsQuery(String.format(
        "CREATE TABLE IF NOT EXISTS Person (id INT PRIMARY KEY, name VARCHAR) WITH \"VALUE_TYPE=%s\"",
        Person.class.getName())).setSchema("PUBLIC")).getAll();

int key = 1;
Person val = new Person(key, "Person 1");

client.query(new SqlFieldsQuery("INSERT INTO Person(id, name) VALUES(?, ?)").setArgs(val.getId(), val.getName())
        .setSchema("PUBLIC")).getAll();

FieldsQueryCursor<List<?>> cursor = client
        .query(new SqlFieldsQuery("SELECT name from Person WHERE id=?").setArgs(key).setSchema("PUBLIC"));

// Get the results; the `getAll()` methods closes the cursor; you do not have to
// call cursor.close();
List<List<?>> results = cursor.getAll();

results.stream().findFirst().ifPresent(columns -> {
    System.out.println("name = " + columns.get(0));
});
```

The `query(SqlFieldsQuery)` method returns an instance of `FieldsQueryCursor`, which can be used to iterate over the results. After getting the results, the cursor must be closed to release the resources associated with it.

{% hint style="info" %}
The `getAll()` method retrieves the results from the cursor and closes it.
{% endhint %}

Read more about using `SqlFieldsQuery` and SQL API in the [Using SQL API](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/sql-api) section.

## Logical Nodes Grouping

You can use the `ClientClusterGroup` interface of the cluster APIs to create various groups of cluster nodes. For instance,
one group can comprise all servers nodes, while the other group can include only those nodes that match a specific
TCP/IP address format. The example below shows how to create a group of server nodes located in the `dc1` data center:

```java
try (IgniteClient client = Ignition.startClient(clientCfg)) {
    ClientClusterGroup serversInDc1 = client.cluster().forServers().forAttribute("dc", "dc1");
    serversInDc1.nodes().forEach(n -> System.out.println("Node ID: " + n.id()));
}
```

Refer to the main [cluster groups](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/distributed-computing/cluster-groups) documentation page for more details on the capability.

## Executing Compute Tasks

The Java thin client supports basic [compute capabilities](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/distributed-computing/distributed-computing)
by letting you execute those compute tasks that are **already deployed** in the cluster. You can either run a task across all
cluster nodes or a specific [cluster group](#logical-nodes-grouping). The deployment
assumes that you create a JAR file with the compute tasks and add the JAR to the cluster nodes' classpath.

By default, the execution of tasks, triggered by the thin client, is disabled on the cluster side. You need to set the
`ThinClientConfiguration.maxActiveComputeTasksPerConnection` parameter to a non-zero value in the configuration of your
server nodes and thick clients:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="thinClientConfiguration">
                <bean class="org.apache.ignite.configuration.ThinClientConfiguration">
                    <property name="maxActiveComputeTasksPerConnection" value="100" />
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
ThinClientConfiguration thinClientCfg = new ThinClientConfiguration()
        .setMaxActiveComputeTasksPerConnection(100);

ClientConnectorConfiguration clientConnectorCfg = new ClientConnectorConfiguration()
        .setThinClientConfiguration(thinClientCfg);

IgniteConfiguration igniteCfg = new IgniteConfiguration()
        .setClientConnectorConfiguration(clientConnectorCfg);

Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}
{% endtabs %}

The example below shows how to get access to the compute APIs via the `ClientCompute` interface and execute the compute
task named `MyTask`:

```java
ThinClientConfiguration thinClientCfg = new ThinClientConfiguration()
        .setMaxActiveComputeTasksPerConnection(100);

ClientConnectorConfiguration clientConnectorCfg = new ClientConnectorConfiguration()
        .setThinClientConfiguration(thinClientCfg);

IgniteConfiguration igniteCfg = new IgniteConfiguration()
        .setClientConnectorConfiguration(clientConnectorCfg);

Ignite ignite = Ignition.start(igniteCfg);
```

## Executing Ignite Services

You can use the `ClientServices` APIs of the Java thin client to invoke an [Ignite Service](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services) that is **already deployed** in the cluster.

The example below shows how to invoke the service named `MyService`:

```java
try (IgniteClient client = Ignition.startClient(clientCfg)) {
    // Executing the service named MyService
    // that is already deployed in the cluster.
    client.services().serviceProxy(
        "MyService", MyService.class).myServiceMethod();
}
```

The deployed service can be implemented using Java or .NET.

## Handling Exceptions

### Handling Node Failures

When you provide the addresses of multiple nodes in the client configuration, the client automatically switches to the next node if the current connection fails and retries any ongoing operation.

In the case of atomic operations, failover to another node is transparent to the user.  However, if you execute a scan query or a SELECT query, it may return duplicate results. This can happen because queries return data in pages, and if the node that the client is connected to goes down while the client retrieves the pages, the client connects to another node and executes the query again. To avoid this, you have to write some code in your application that checks if the entries returned by the client are duplicated. Consider the following code:

```java
Query<Cache.Entry<Integer, Person>> qry = new ScanQuery<Integer, Person>(
        (i, p) -> p.getName().contains("Smith"));

try (QueryCursor<Cache.Entry<Integer, Person>> cur = cache.query(qry)) {
    // Collecting the results into a map removes the duplicates
    Map<Integer, Person> res = cur.getAll().stream()
            .collect(Collectors.toMap(Cache.Entry::getKey, Cache.Entry::getValue));
}
```

## Enabling Logging

You can enable logging of thin client's events with the a logger implementation of your choice:

```java
ClientConfiguration cfg = new ClientConfiguration()
    .setAddresses("127.0.0.1:10800")
    .setLogger(new JavaLogger());
IgniteClient client = Ignition.startClient(cfg);
```

## Listening to Events

### Connection Events

You can listen to events that are happening on cluster by using the `ConnectionEventListener` class. Create the event listener object and set it as event listener for the client configuration:

```java
ConnectionEventListener lsnr = new ConnectionEventListener() {
    @Override public void onHandshakeSuccess(HandshakeSuccessEvent event) {
        System.out.println("onHandshakeSuccess: " + event.connectionDescription().serverNodeId());
    }

    @Override public void onConnectionClosed(ConnectionClosedEvent event) {
        System.out.println("onConnectionClosed: " + event.connectionDescription().serverNodeId());
    }
};

ClientConfiguration cfg = new ClientConfiguration().setAddresses("127.0.0.1:10800").setEventListeners(lsnr);

try (IgniteClient client = Ignition.startClient(cfg)) {
    // ...
}
```

For more information about the events, see the [Events](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/events/events) page.

### Client Lifecycle Events

You can also react to the client's own lifecycle — when it starts, fails to start, or stops — by registering a `ClientLifecycleEventListener`. Implement only the callbacks you need; each one has a default no-op implementation.

```java
ClientLifecycleEventListener lsnr = new ClientLifecycleEventListener() {
    @Override public void onClientStart(ClientStartEvent event) {
        System.out.println("onClientStart: " + event.client());
    }

    @Override public void onClientFail(ClientFailEvent event) {
        System.out.println("onClientFail: " + event.throwable());
    }

    @Override public void onClientStop(ClientStopEvent event) {
        System.out.println("onClientStop: " + event.client());
    }
};

ClientConfiguration cfg = new ClientConfiguration().setAddresses("127.0.0.1:10800").setEventListeners(lsnr);

try (IgniteClient client = Ignition.startClient(cfg)) {
    // ...
}
```

`onClientStart` fires after the client connects successfully, `onClientStop` fires when the client is closed, and `onClientFail` fires if the client fails to start — the cause is available from `ClientFailEvent.throwable()`. If a listener throws an exception, it is logged and ignored; it does not interrupt the client's startup or shutdown.

## Security

### SSL/TLS

To use encrypted communication between the thin client and the cluster, you have to enable SSL/TLS in both the cluster configuration and the client configuration. Refer to the [Enabling SSL/TLS for Thin Clients](getting-started-with-thin-clients.md#enabling-ssl-tls-for-thin-clients) section for the instruction on the cluster configuration.

To enable encrypted communication in the thin client, provide a keystore that contains the encryption key and a truststore with the trusted certificates in the thin client configuration.

```java
ClientConfiguration clientCfg = new ClientConfiguration().setAddresses("127.0.0.1:10800");

clientCfg.setSslMode(SslMode.REQUIRED).setSslClientCertificateKeyStorePath(KEYSTORE)
        .setSslClientCertificateKeyStoreType("PKCS12").setSslClientCertificateKeyStorePassword("123456")
        .setSslTrustCertificateKeyStorePath(TRUSTSTORE).setSslTrustCertificateKeyStorePassword("123456")
        .setSslTrustCertificateKeyStoreType("PKCS12").setSslKeyAlgorithm("SunX509").setSslTrustAll(false)
        .setSslProtocol(SslProtocol.TLS);

try (IgniteClient client = Ignition.startClient(clientCfg)) {
    // ...
}
```

The following table explains encryption parameters of the client configuration:

| Parameter | Description | Default Value |
| --- | --- | --- |
| sslMode | Either  `REQUIRED` or `DISABLED`. | `DISABLED` |
| sslClientCertificateKeyStorePath | The path to the keystore file with the private key. | N/A |
| sslClientCertificateKeyStoreType | The type of the keystore. | `JKS` |
| sslClientCertificateKeyStorePassword | The password to the keystore. | N/A |
| sslTrustCertificateKeyStorePath | The path to the truststore file. | N/A |
| sslTrustCertificateKeyStoreType | The type of the truststore. | `JKS` |
| sslTrustCertificateKeyStorePassword | The password to the truststore. | N/A |
| sslKeyAlgorithm | Sets the key manager algorithm that is used to create a key manager. | `SunX509` |
| sslTrustAll | If this parameter is set to `true`, the certificates are not validated. | N/A |
| sslProtocol | The name of the protocol that is used for data encryption. | `TLS` |

### Authentication

Configure [authentication on the cluster side](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) and provide the user name and password in the client configuration.

```java
ClientConfiguration clientCfg = new ClientConfiguration().setAddresses("127.0.0.1:10800").setUserName("joe")
        .setUserPassword("passw0rd!");

try (IgniteClient client = Ignition.startClient(clientCfg)) {
    // ...
} catch (ClientAuthenticationException e) {
    // Handle authentication failure
}
```

### Authorization

For information about authorizing thin client connections, see the [Client Authorization](authorization.md) page.

## Async APIs

Most network-bound thin client APIs have an async counterpart, for example, `ClientCache.get` and `ClientCache.getAsync`.

```java
IgniteClient client = Ignition.startClient(clientCfg);
ClientCache<Integer, String> cache = client.getOrCreateCache("cache");

IgniteClientFuture<Void> putFut = cache.putAsync(1, "hello");
putFut.get(); // Blocking wait.

IgniteClientFuture<String> getFut = cache.getAsync(1);
getFut.thenAccept(val -> System.out.println(val)); // Non-blocking continuation.
```

- Async methods do not block the calling thread;
- Async methods return `IgniteClientFuture<T>`, which is a combination of `Future<T>` and `CompletionStage<T>`;
- Async continuations are executed using `ClientConfiguration.AsyncContinuationExecutor`, which defaults to `ForkJoinPool#commonPool()`. For example, `cache.getAsync(1).thenAccept(val -> System.out.println(val))` executes the `println` call using a thread from the `commonPool`.

## Data Center Replication

### Sender Groups

Configure sender groups for [sender nodes](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/configuring-replication#sender-nodes) by using the ClientCacheDrSenderConfiguration.

The below example adds the node to the `group1` sender group:

```java
IgniteClient client = Ignition.startClient(
        new ClientConfiguration().setAddresses("localhost"));

ClientCacheConfiguration cacheCfg = new ClientCacheConfiguration()
        .setName("dr-cache")
        .setPluginConfigurations(new GridGainClientCacheConfiguration()
                .setDrSenderConfiguration(new ClientCacheDrSenderConfiguration()
                        .setSenderGroup("foo-bar")));

ClientCache<Integer, Integer> cache = client.createCache(cacheCfg);
```
