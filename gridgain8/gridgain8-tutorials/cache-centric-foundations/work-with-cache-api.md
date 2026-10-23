---
description: >-
  Connect a Java thick client to your cache-centric cluster, create distributed caches, and perform put, get, and bulk operations with IgniteCache.
---

# Work With the Cache API

<!-- TODO (release): the Maven version 8.10.0 is not yet published on the GridGain Nexus repository (it has no 8.10 version), so the pom in this page cannot resolve until it is; the version strings in the sample output and the download file name are placeholders; re-capture them from the released build. After the 8.10.0 release, check that each of these resolves, update this page if the final names differ, and delete this comment. -->

## Introduction

Your cluster is running. Now you connect a Java application and store data in it.

The central interface in the cache-centric architecture is `IgniteCache<K,V>`. If you have used `java.util.concurrent.ConcurrentMap`, the API will feel familiar: `put`, `get`, `remove`, `putAll`, `getAll`. The difference is that the data lives on the cluster instead of in a single JVM. By the end of this tutorial, you will see that the distributed cache follows the same Java collections contract applied across a cluster.

In this tutorial, you create a Maven project, connect a thick client to your single-node cluster, and perform individual and bulk cache operations using sample records from the Music Store dataset you work with throughout this learning path. The sample data is defined in the code, so no dataset loading is required. By the end, you will have a working Java application that stores and retrieves data from a distributed cache.

This tutorial labels itself "beginner" for GridGain 8. The surrounding Java stack (Maven, JDBC, Spring XML) is assumed prior knowledge. If any of those is new, skim the linked primer before starting.

## Prerequisites

- **A running single-node cluster** from [Start a Local Cache Development Cluster](start-local-cache-cluster.md)
- **Java 17** or later
- **Maven 3.6** or later
- **Comfort reading Spring bean XML.** The `ignite-config.xml` is Spring-formatted but you only edit a handful of properties.

<details>
<summary>Returning to these tutorials? Verify your cluster is running.</summary>

Check that the cluster container is up:

```bash
docker ps --filter name=gridgain8-node1 --format "table {{.Names}}\t{{.Status}}"
```

Expected output:

```text
NAMES             STATUS
gridgain8-node1   Up X hours
```

**If the container is stopped**, restart it from the directory containing your `docker-compose.yml`:

```bash
docker compose -f cache-cluster/docker-compose.yml start
```

**If the cluster was destroyed** (`docker compose down`), recreate it:

```bash
docker compose -f cache-cluster/docker-compose.yml up -d
```

The cluster runs in-memory. Destroying and recreating it starts with an empty cache.

</details>

## What You Will Learn

You will:

- Connect a thick client that joins the cluster ring
- Create a distributed cache and store data with `put` and `get`
- Remove entries and observe the result
- Store and retrieve multiple entries in a single call with `putAll` and `getAll`

## Set up the Maven Project

Create a project directory alongside your `cache-cluster` directory and add a `pom.xml`:

```bash
mkdir -p cache-client/src/main/java/com/example
```

Create `cache-client/pom.xml`:

{% code title="pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>cache-client</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.CacheConnect</exec.mainClass>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>gridgain-core</artifactId>
            <version>8.10.0</version>
        </dependency>
    </dependencies>

    <repositories>
        <repository>
            <id>GridGain External Repository</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <executable>java</executable>
                    <arguments>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.nio=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.io=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/sun.nio.ch=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.lang=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.util=ALL-UNNAMED</argument>
                        <argument>-classpath</argument>
                        <classpath/>
                        <argument>${exec.mainClass}</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
{% endcode %}

GridGain 8 artifacts are published to GridGain's Nexus repository, not Maven Central. The `<repositories>` block tells Maven where to find the `gridgain-core` dependency.

The `gridgain-core` artifact contains the thick client, the cache API, and the discovery layer. A single dependency is all you need to connect to the cluster and perform cache operations.

The `--add-opens` flags in the exec plugin give the GridGain client reflective access to JDK internals. The thick client uses `sun.nio.ch` for direct memory buffers and `java.nio` for network I/O, and `java.io` for object serialization. Without these flags, Java 16+ blocks the access and the client fails to start.

The `exec.mainClass` property in `<properties>` lets you override the main class from the command line with `-Dexec.mainClass=com.example.OtherClass`. You use this to run different classes in later steps.

{% hint style="info" %}
This project uses `exec:exec` (not `exec:java`). The `exec:exec` goal launches a separate JVM process, which is the only way to pass `--add-opens` flags. The `exec:java` goal runs inside Maven's JVM and ignores JVM arguments in the plugin configuration.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The `pom.xml` is in `cache-client/` and `mvn compile` succeeds with no errors.
{% endhint %}

## Connect a Thick Client to the Cluster

The GridGain thick client is a Java process that joins the cluster's discovery ring as a non-data member. It participates in the topology directly: it receives the partition map (the lookup table that maps each key's hash to a specific server node), routes operations to the node that owns the data, and can enable features like near-cache that keep frequently accessed data in the client's own memory.

{% hint style="info" %}
GridGain 8 also offers a thin client (`IgniteClient`), which connects over a lightweight TCP socket without joining the topology. The thick client is the standard choice for this generation because it supports the full API surface: compute, service grid, continuous queries, and near-cache. The thin client was added later and covers a narrower set of operations.

In GridGain 9, the thin client is the primary client API. In GridGain 8, the thick client fills that role.
{% endhint %}

Create `cache-client/src/main/java/com/example/CacheConnect.java`:

{% code title="CacheConnect.java" %}
```java
package com.example;

import java.util.Collections;

import org.apache.ignite.Ignite;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Connects a thick client to the single-node cluster and prints
 * the topology snapshot.
 */
public class CacheConnect {
    public static void main(String[] args) {
        // Configure static IP discovery. The address matches the published
        // discovery port from your Docker Compose file. In a multi-node
        // cluster, you would list all server addresses here.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        // Client mode means this process joins the cluster ring but does not
        // store any data partitions. It routes operations to the server
        // nodes that own each key.
        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        // The flag must match the server's peerClassLoadingEnabled
        // setting (true in the ignite-config.xml you created earlier).
        cfg.setPeerClassLoadingEnabled(true);

        // Lower both failure-detection timeouts so the client fails fast
        // during the tutorial. Defaults on a client JVM are 10 seconds for
        // setFailureDetectionTimeout (node-level, applies to every SPI)
        // and 30 seconds for setClientFailureDetectionTimeout (cluster-
        // scope, used by the server to decide whether a client is dead).
        // Production networks keep the defaults because transient pauses
        // are common; localhost Docker has neither.
        // Also lower metricsUpdateFrequency. GridGain refuses to start
        // if clientFailureDetectionTimeout is below it and only logs a
        // warning for failureDetectionTimeout.
        cfg.setMetricsUpdateFrequency(1000);
        cfg.setFailureDetectionTimeout(1000);
        cfg.setClientFailureDetectionTimeout(1000);

        // Ignition.start() connects to the cluster and blocks until the
        // client joins the ring. try-with-resources ensures the client
        // leaves the ring cleanly when the block exits.
        try (Ignite ignite = Ignition.start(cfg)) {
            System.out.println();
            System.out.println("Client connected to the cluster.");
            System.out.println("Local node ID: " + ignite.cluster().localNode().id());

            // nodes() includes both server nodes and client nodes,
            // so the count is 2: one server + this client
            System.out.println("Cluster nodes: " + ignite.cluster().nodes().size());
        }

        // GridGain's internal threads can delay JVM shutdown.
        // System.exit(0) ensures a clean exit after the client disconnects.
        System.exit(0);
    }
}
```
{% endcode %}

The connection code has three parts:

- **`TcpDiscoveryVmIpFinder`** configures static IP discovery. The address `127.0.0.1:47500` matches the published discovery port from your Docker Compose file. In the cluster setup tutorial, the XML configuration used `node1:47500` because containers discover each other by Docker hostname. Here, your Java application runs on the host machine and connects through the published port.
- **`setClientMode(true)`** tells the node to join the ring without accepting data partitions (the subsets of cached data distributed across server nodes). Your client sends operations to the server, which handles all the storage.
- **`Ignition.start(cfg)`** starts the client node and blocks until it joins the ring. The `try-with-resources` block ensures the node leaves the ring cleanly when your program exits.

Compile and run:

```bash
mvn -f cache-client/pom.xml compile exec:exec
```

The GridGain client produces startup output before your application code runs. Most of it is informational. Look for the **topology snapshot** line:

```text
INFO: Topology snapshot [ver=2, locNode=7381eb44, servers=1, clients=1,
  state=ACTIVE, CPUs=22, offheap=3.5GB, heap=7.0GB,
  aliveNodes=[TcpDiscoveryNode [id=7381eb44-..., isClient=true, ver=8.10.0#...],
  TcpDiscoveryNode [id=6b54894d-..., isClient=false, ver=8.10.0#...]]]

Client connected to the cluster.
Local node ID: 7381eb44-1703-4a14-90de-b045728d6146
Cluster nodes: 2
```

The GridGain 8 topology snapshot includes an `aliveNodes` array listing every node in the cluster with its ID, client/server role, and version. The important fields to look for are `servers=1, clients=1, state=ACTIVE`.

The topology snapshot now shows `clients=1`. Your thick client has joined the ring. The "Cluster nodes: 2" count includes both the server node and your client node.

{% hint style="info" %}
The thick client prints performance suggestions, version checks, and configuration warnings on startup. These are safe to ignore. GridGain 8 is verbose: it logs the full configuration, classpath, exchange timings, and connection details at INFO level by default. Scan past the noise and look for the topology snapshot line showing `servers=1, clients=1`.
{% endhint %}

{% hint style="info" %}
The thick client may take a few seconds to connect on the first run. The client discovers the server node's internal Docker IP address (e.g., `172.20.0.2`), tries to connect to it, times out, and then falls back to `localhost`. The `setFailureDetectionTimeout(1000)` in the code above reduces this wait from the default 10 seconds to 1 second. You may still see a `Connection timed out` warning in the log. This is a Docker networking artifact, not a product performance issue. Production deployments where the client and server share a network do not experience this delay.
{% endhint %}

{% hint style="warning" %}
If the client fails to join the cluster, your Maven dependency does not match your running cluster. Verify that your `pom.xml` dependency is the GridGain 8 `gridgain-core` artifact and matches the Docker image you started in the previous tutorial.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The topology snapshot shows servers=1, clients=1, and your program prints "Client connected to the cluster."
{% endhint %}

## Create a Cache and Store Data

`IgniteCache<K,V>` is the primary interface for distributed key-value storage. It extends the same contract as `java.util.concurrent.ConcurrentMap`: you put a key-value pair, and you get the value back by its key. The difference is that the data is distributed across the cluster. With one server node, all data lives on that node. When you add nodes later, the data partitions across them automatically.

Each class in this tutorial includes the same connection setup. In a production application, you would extract this into a shared utility. Here, keeping each file self-contained means you can run any step independently.

Create `cache-client/src/main/java/com/example/CacheCrud.java`:

{% code title="CacheCrud.java" %}
```java
package com.example;

import java.util.Collections;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Creates a distributed cache and performs individual put, get,
 * and remove operations using sample Music Store customer records.
 */
public class CacheCrud {
    public static void main(String[] args) {
        // Same connection setup as CacheConnect. Each class is
        // self-contained so you can run any step independently.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        // The flag must match the server's peerClassLoadingEnabled
        // setting (true in the ignite-config.xml you created earlier).
        cfg.setPeerClassLoadingEnabled(true);
        cfg.setMetricsUpdateFrequency(1000);
        cfg.setFailureDetectionTimeout(1000);
        cfg.setClientFailureDetectionTimeout(1000);

        try (Ignite ignite = Ignition.start(cfg)) {
            // getOrCreateCache() creates a named cache on the cluster or
            // returns the existing one. The name "customers" is the cache's
            // identity: any client that asks for "customers" accesses the
            // same distributed data. The default mode is PARTITIONED with
            // zero backup copies.
            IgniteCache<Integer, String> cache =
                ignite.getOrCreateCache("customers");

            System.out.println();
            System.out.println("=== Individual Cache Operations ===");

            // put(key, value) stores one entry. Each call is a network
            // round-trip to the server node that owns the key.
            // Sample Music Store records, hardcoded here for simplicity.
            // Later tutorials load the full dataset into the cluster.
            cache.put(1, "Luis Goncalves");
            cache.put(2, "Leonie Kohler");
            cache.put(3, "Francois Tremblay");
            System.out.println("Stored 3 customers in the cache.");

            // get(key) retrieves one entry by key. The return type matches
            // the cache's value type (String here). Returns null if the
            // key does not exist, just like ConcurrentMap.get().
            System.out.println("Customer 1: " + cache.get(1));
            System.out.println("Customer 2: " + cache.get(2));
            System.out.println("Customer 3: " + cache.get(3));

            // put(key, value) on an existing key overwrites the value.
            // There is no separate update method. This is the same
            // behavior as ConcurrentMap.put().
            cache.put(3, "Francois Tremblay-Dupont");
            System.out.println("Updated customer 3: " + cache.get(3));

            // remove(key) deletes the entry from the cluster.
            // A subsequent get() for that key returns null.
            cache.remove(2);
            System.out.println("Removed customer 2.");
            System.out.println("Customer 2 after remove: " + cache.get(2));

            // removeAll() clears every entry in this cache.
            // This resets state so the next step starts clean.
            cache.removeAll();
            System.out.println("Cache cleared.");
        }

        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cache-client/pom.xml exec:exec -Dexec.mainClass=com.example.CacheCrud
```

After the GridGain startup output, you see:

```text
=== Individual Cache Operations ===
Stored 3 customers in the cache.
Customer 1: Luis Goncalves
Customer 2: Leonie Kohler
Customer 3: Francois Tremblay
Updated customer 3: Francois Tremblay-Dupont
Removed customer 2.
Customer 2 after remove: null
Cache cleared.
```

Key behaviors to note:

- **`getOrCreateCache("customers")`** creates a named cache on the cluster or returns the existing one. The name is the cache's identity across the cluster. Any client that connects and requests `"customers"` accesses the same distributed data
- **Cache naming** works like connecting to a named database or collection. The name is a string, and the cache persists on the cluster as long as the cluster is running
- **Default configuration** creates a PARTITIONED cache with zero backup copies. The [cache modes section](#cache-modes-and-backups) below explains what this means
- **Each `put` and `get`** is a network round-trip to the server node. After `remove(2)`, a `get(2)` returns `null` because the entry no longer exists

{% hint style="success" %}
**Checkpoint:** The output shows three customers stored and retrieved, and `null` after removing customer 2.
{% endhint %}

## Perform Bulk Operations

The previous step stored three customers with three separate `put` calls. Each call was a network round-trip to the server. Storing 10 customers the same way means 10 round-trips. Storing 1,000 means 1,000 round-trips.

`putAll` and `getAll` batch multiple entries into a single network call. The cost model shifts from one round-trip per entry to one round-trip for the entire batch. This is the same principle behind JDBC batch inserts: amortize network latency across many operations instead of paying it once per row.

Create `cache-client/src/main/java/com/example/CacheBulk.java`:

{% code title="CacheBulk.java" %}
```java
package com.example;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Demonstrates bulk cache operations with putAll and getAll.
 * Stores and retrieves 10 customers in a single network call each.
 */
public class CacheBulk {
    public static void main(String[] args) {
        // Same connection setup as the previous classes.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        // The flag must match the server's peerClassLoadingEnabled
        // setting (true in the ignite-config.xml you created earlier).
        cfg.setPeerClassLoadingEnabled(true);
        cfg.setMetricsUpdateFrequency(1000);
        cfg.setFailureDetectionTimeout(1000);
        cfg.setClientFailureDetectionTimeout(1000);

        try (Ignite ignite = Ignition.start(cfg)) {
            IgniteCache<Integer, String> cache =
                ignite.getOrCreateCache("customers");

            System.out.println();
            System.out.println("=== Bulk Cache Operations ===");

            // putAll() sends all 10 entries to the cluster in a single
            // network call. Compare this to 10 individual put() calls,
            // each requiring its own round-trip. With a multi-node cluster,
            // putAll() partitions the batch by key hash and sends each
            // subset to the owning node in parallel.
            Map<Integer, String> customers = sampleCustomers();
            cache.putAll(customers);
            System.out.println(
                "Stored " + customers.size() + " customers with putAll.");

            // getAll() retrieves multiple keys in a single cluster call.
            // It returns a Map<K,V> of the results. The order is not
            // guaranteed, so TreeMap sorts by key for consistent display.
            Map<Integer, String> retrieved = new TreeMap<>(
                cache.getAll(customers.keySet()));

            System.out.println(
                "Retrieved " + retrieved.size() + " customers with getAll:");
            for (Map.Entry<Integer, String> entry : retrieved.entrySet()) {
                System.out.println(
                    "  Customer " + entry.getKey() + ": " + entry.getValue());
            }

            // Clear the cache for a clean state
            cache.removeAll();
            System.out.println("Cache cleared.");
        }

        System.exit(0);
    }

    /**
     * Returns sample Music Store customer records.
     * Keys are CustomerIds, values are "FirstName LastName".
     */
    static Map<Integer, String> sampleCustomers() {
        Map<Integer, String> customers = new LinkedHashMap<>();
        customers.put(1, "Luis Goncalves");
        customers.put(2, "Leonie Kohler");
        customers.put(3, "Francois Tremblay");
        customers.put(4, "Bjorn Hansen");
        customers.put(5, "Frantisek Wichterlova");
        customers.put(6, "Helena Holy");
        customers.put(7, "Astrid Gruber");
        customers.put(8, "Daan Peeters");
        customers.put(9, "Kara Nielsen");
        customers.put(10, "Eduardo Martins");
        return customers;
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f cache-client/pom.xml exec:exec -Dexec.mainClass=com.example.CacheBulk
```

```text
=== Bulk Cache Operations ===
Stored 10 customers with putAll.
Retrieved 10 customers with getAll:
  Customer 1: Luis Goncalves
  Customer 2: Leonie Kohler
  Customer 3: Francois Tremblay
  Customer 4: Bjorn Hansen
  Customer 5: Frantisek Wichterlova
  Customer 6: Helena Holy
  Customer 7: Astrid Gruber
  Customer 8: Daan Peeters
  Customer 9: Kara Nielsen
  Customer 10: Eduardo Martins
Cache cleared.
```

`putAll` takes a `Map<K,V>` and stores every entry on the cluster. This method comes from the `Map` interface, the same `putAll` that `HashMap` provides. `getAll` is a GridGain addition that retrieves multiple keys in a single cluster call and returns a `Map<K,V>` of the results. The `TreeMap` wrapper sorts the retrieved entries by key so the output is deterministic regardless of the order the server returns them.

With a single server node, both calls go to the same node. In a multi-node cluster, the client partitions the batch by key hash and sends each subset to the owning node in parallel. The bulk methods handle the fan-out and collection transparently.

{% hint style="success" %}
**Checkpoint:** The output shows 10 customers stored with `putAll` and retrieved with `getAll`, listed in order by customer ID.
{% endhint %}

## Cache Modes and Backups

Every cache has a **mode** that determines how data is distributed across the cluster. The two modes are PARTITIONED and REPLICATED.

**PARTITIONED** (the default) assigns each key to one primary node by hashing the key. With multiple server nodes, different keys land on different nodes. This is how the cache scales horizontally: adding nodes increases total memory and throughput because each node holds a fraction of the data. With a single node, all keys land on the same node, so you do not observe the partitioning effect yet.

**REPLICATED** stores a full copy of every entry on every server node. Reads are always local because every node holds the full dataset. Writes carry higher cost since each entry must propagate to every server node. Replicated caches work well for small, read-heavy datasets like lookup tables or configuration data.

**Backups** are redundant copies of each partition. The default is zero backups, which means losing a node loses the data on that node. Production deployments typically set backups to 1 or higher. Cache configuration (including mode and backups) is covered in a later tutorial when you work with `CacheConfiguration`.

{% hint style="info" %}
The cache you created in this tutorial used the default: PARTITIONED mode with zero backups. All the operations worked the same way they would on a multi-node cluster. The only difference is that a multi-node cluster distributes the keys across nodes, which you observe when you add nodes in a later tutorial.
{% endhint %}

<details>
<summary>How does this compare to a database?</summary>

A common question when evaluating a caching layer is whether it is faster than the database for simple lookups.

A warm MariaDB primary-key lookup on a localhost hop is typically faster than a single cache hop for the same query. A prepared statement on an indexed primary key over a fully cached buffer pool is the best-case scenario for a relational database. The cache adds latency that a direct database call avoids: partition mapping, serialization through the binary object format, and topology awareness checks. On a single node with a small dataset, these costs are not offset by any distributed advantage.

The cache's value here is not the single-operation latency. It is the ability to absorb volume so the database has capacity for everything else. Caching wins in different scenarios:

- **Read amplification**: When multiple application instances read the same data, the cache absorbs the load instead of the database. This is the most common reason to add a caching layer
- **Distributed scale**: With data partitioned across nodes, each node handles a fraction of the requests. Total throughput scales with node count

Later tutorials in this path cover additional capabilities where the performance gap reverses:

- **Near-cache**: The thick client keeps frequently accessed data in its own JVM memory, eliminating the network hop entirely
- **Compute colocation**: Processing logic runs on the node that holds the data, avoiding network transfer

A later tutorial in this path connects the cache to a MariaDB database under sustained read load and demonstrates the cache-aside pattern where these advantages become measurable.

</details>

## Summary

You built a Java application that connects to your cache-centric cluster as a thick client and performs distributed cache operations. The key concepts:

- **Thick client** joins the cluster ring as a non-data member, routing operations directly to the owning server node
- **`IgniteCache<K,V>`** is the distributed equivalent of `ConcurrentMap`. The same `put`, `get`, `remove` methods work whether the data lives in one JVM or across a cluster
- **Bulk operations** (`putAll`, `getAll`) amortize network round-trips. One call for N entries instead of N calls for N entries
- **PARTITIONED mode** (the default) distributes keys by hash. REPLICATED mode copies all data to every node

## Next Step

The next tutorial, [Cache Sizing and Expiry](cache-sizing-and-expiry.md), solves the two problems that make an unbounded cache unusable in production. You add LRU eviction to bound the on-heap tier, set TTL with a JCache `ExpiryPolicy`, and watch a real-time snapshot of the cache shrinking itself as entries leave under both rules.
