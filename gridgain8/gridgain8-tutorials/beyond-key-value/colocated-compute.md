---
description: >-
  Ship Java closures to the nodes that own the data instead of pulling the data to the client. Measure pull-to-client, broadcast, and affinityCall against the same question on a three-node cluster.
---

# Compute Where the Data Lives: The Round-Trip Problem

## Introduction

Not every question is a SQL aggregation. For custom risk scoring, batch enrichment, or log replay against a non-standard format, the Cache API leaves one option: pull every matching entry to the client and compute in Java. Bytes, heap, and wall time all scale with the dataset. A cache that cannot run arbitrary code on the data forces the same shape every time, no matter what is in front of the application.

This tutorial extends the [`sql-on-cache/`](from-keyvalue-to-sql.md) project. The Customer and Invoice caches stay loaded. You answer the same lifetime-spend question three ways: pull every entry to the client, broadcast a closure to every server, and target one customer's primary node. The numbers expose what each placement costs.

The Java code is identical across Apache Ignite 2 and GridGain 8.

## Prerequisites

- **Completion of [From Key-Value to SQL: The JOIN Problem](from-keyvalue-to-sql.md).** You have the `sql-on-cache/` Maven project on disk with `Customer`, `Invoice`, and `InvoiceKey` model classes and the `ConfigureCaches` and `SeedFromChinook` programs.
- **A running three-node cluster** using `cache-cluster/docker-compose-3nodes.yml` from [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md). The per-node configs in that compose pin discovery and communication ports and register a `BasicAddressResolver` so a host JVM thick client can reach each container through the loopback address. Peer class loading is enabled on every server.
- **Java 11 or later** for the client runtime. The Maven project compiles to Java 8 bytecode in this tutorial so closures are byte-compatible with the AI2 server JVM (Java 8) and the GG8 server JVM (Java 11).
- **Maven 3.6** or later.
- **Docker Compose 2.23** or later.

This tutorial does not introduce a fresh project. You add a new `compute/` package alongside the existing classes, change two lines in the `pom.xml`, and reuse the same Customer and Invoice caches.

<details>
<summary>Returning to this tutorial? Restart the three-node cluster and reseed the data.</summary>

The single-node cluster from the previous tutorial cannot run the work in this one. The round-trip story needs data on more than one node. Stop the single-node cluster if it is still running, start the three-node cluster from [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md), and reseed.

{% tabs %}
{% tab title="Apache Ignite 2" %}

```bash
docker compose -f cache-cluster/docker-compose.yml down
docker compose -f cache-cluster/docker-compose-3nodes.yml up -d
docker ps --filter name=ignite2-node --format "table {{.Names}}\t{{.Status}}"
```

{% endtab %}

{% tab title="GridGain 8" %}

```bash
docker compose -f cache-cluster/docker-compose.yml down
docker compose -f cache-cluster/docker-compose-3nodes.yml up -d
docker ps --filter name=gridgain8-node --format "table {{.Names}}\t{{.Status}}"
```

{% endtab %}

{% endtabs %}

Three server containers in the `Up` state. The cluster is in-memory, so the data does not survive the topology change. Rerun the seed step before running anything in this tutorial:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.ConfigureCaches
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.SeedFromChinook
```

The seed reports `Customer rows in cache: 59` and `Invoice rows in cache: 412`.

</details>

## What You Will Learn

In this tutorial, you:

- Write a pull-to-client class that iterates the Customer and Invoice caches and computes lifetime spend per Brazilian customer in Java
- Define an `IgniteCallable` that runs on each server and returns a partial spend map for the customers whose entries live on that node, then broadcast it
- Define an `IgniteCallable` that targets a single customer ID and run it via `affinityCall` against the primary node for that key
- Read each measurement's wall time and entries-on-the-wire and pick the right approach for a given question

## Update the Project for Compute Closures

The closures you will write in this tutorial run on the server JVM, not the client. The Apache Ignite 2.16.0 server image runs Java 8 (class file major version 52). The GridGain 8.9.32 server image runs Java 11 (class file major version 55). Java 8 bytecode is accepted by both. If you ship a closure compiled for Java 11 to the AI2 server, the server rejects it with `UnsupportedClassVersionError` at deploy time. Setting the project's bytecode target to 8 makes one set of class files work on every server you might run against.

Open `sql-on-cache/pom.xml` and change one line in `<properties>`:

{% code title="sql-on-cache/pom.xml" %}
```diff
     <properties>
-        <maven.compiler.release>11</maven.compiler.release>
+        <maven.compiler.release>8</maven.compiler.release>
         <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
         <exec.mainClass>com.example.sqlquery.ConfigureCaches</exec.mainClass>
     </properties>
```
{% endcode %}

The optimized marshaller used during compute also needs reflective access to `java.net.InetSocketAddress`. Add one more `--add-opens` argument to the exec plugin's `<arguments>` block, alongside the others already declared in the project:

{% code title="sql-on-cache/pom.xml" %}
```diff
                         <argument>--add-opens</argument>
                         <argument>java.base/java.math=ALL-UNNAMED</argument>
+                        <argument>--add-opens</argument>
+                        <argument>java.base/java.net=ALL-UNNAMED</argument>
                         <argument>--add-opens</argument>
                         <argument>java.sql/java.sql=ALL-UNNAMED</argument>
```
{% endcode %}

Recompile to confirm the project still builds:

```bash
mvn -f sql-on-cache/pom.xml clean compile
```

A `BUILD SUCCESS` line. The model classes and the seeder and query classes are now compiled to Java 8 bytecode.

{% hint style="success" %}
**Checkpoint:** The `pom.xml` has `<maven.compiler.release>8</maven.compiler.release>`, the `--add-opens java.base/java.net=ALL-UNNAMED` argument is present, and `mvn compile` finishes without errors.
{% endhint %}

## The Pull-to-Client Baseline

The lifetime-spend question is "for every Brazilian customer, what is the sum of their invoice totals across all time?" The cross-cache JOIN from the previous tutorial already answers it with SQL. This tutorial deliberately uses the Cache API instead so the cost of pulling-and-computing-in-Java is visible alongside the alternatives.

Create the new `compute` subpackage and the first class:

```bash
mkdir -p sql-on-cache/src/main/java/com/example/sqlquery/compute
```

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/compute/PullToClientBaseline.java" %}
```java
package com.example.sqlquery.compute;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

import com.example.sqlquery.model.Customer;
import com.example.sqlquery.model.Invoice;
import com.example.sqlquery.model.InvoiceKey;

/**
 * Computes lifetime spend per Brazilian customer by pulling the
 * Customer and Invoice caches to the client and running the
 * aggregation in this JVM.
 *
 * Counts the entries that crossed the wire so the round-trip cost is
 * visible in the output. The next two classes (BroadcastTopSpend and
 * AffinityCallByCustomer) compute the same answer with the work
 * placed on the cluster instead.
 */
public class PullToClientBaseline {

    public static void main(String[] args) {
        // Discovery + client setup is identical across every class in
        // this project. The BasicAddressResolver on each server
        // advertises 127.0.0.1 so the host JVM reaches each node via
        // loopback. Address list spans the three pinned discovery ports.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500",
                "127.0.0.1:47501",
                "127.0.0.1:47502")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            IgniteCache<Integer, Customer> customers = ignite.cache("Customer");
            IgniteCache<InvoiceKey, Invoice> invoices = ignite.cache("Invoice");

            // Warm the communication SPI before timing. The first cache
            // op on a fresh client pays connection-setup cost.
            customers.size();
            invoices.size();

            long t0 = System.nanoTime();

            // Pass 1: pull every Customer to the client. The Cache API
            // iterator has no server-side predicate. The filter runs in
            // this JVM after each entry crosses the network.
            List<Integer> brazilianIds = new ArrayList<>();
            int customerEntriesScanned = 0;
            for (Cache.Entry<Integer, Customer> entry : customers) {
                customerEntriesScanned++;
                if ("Brazil".equals(entry.getValue().getCountry())) {
                    brazilianIds.add(entry.getKey());
                }
            }

            // Pass 2: pull every Invoice. Same iterator pattern.
            Map<Integer, BigDecimal> spendById = new HashMap<>();
            for (Integer id : brazilianIds) {
                spendById.put(id, BigDecimal.ZERO);
            }

            int invoiceEntriesScanned = 0;
            for (Cache.Entry<InvoiceKey, Invoice> entry : invoices) {
                invoiceEntriesScanned++;
                Integer customerId = entry.getKey().getCustomerId();
                if (spendById.containsKey(customerId)) {
                    spendById.merge(customerId, entry.getValue().getTotal(), BigDecimal::add);
                }
            }

            long elapsedMicros = (System.nanoTime() - t0) / 1000;

            List<Map.Entry<Integer, BigDecimal>> ranked = new ArrayList<>(spendById.entrySet());
            ranked.sort(Comparator.comparing(Map.Entry<Integer, BigDecimal>::getValue).reversed());

            System.out.println();
            System.out.println("=== Pull-to-client baseline ===");
            System.out.println("Brazilian customers: " + brazilianIds.size());
            System.out.println("Top 5 by lifetime spend:");
            int n = Math.min(5, ranked.size());
            for (int i = 0; i < n; i++) {
                Map.Entry<Integer, BigDecimal> e = ranked.get(i);
                Customer c = customers.get(e.getKey());
                System.out.printf("  %s %s -> $%s%n",
                    c.getFirstName(), c.getLastName(), e.getValue());
            }

            System.out.println();
            System.out.println("Wall time: " + elapsedMicros + " us ("
                + (elapsedMicros / 1000) + " ms)");
            System.out.println("Customer entries scanned: " + customerEntriesScanned);
            System.out.println("Invoice entries scanned:  " + invoiceEntriesScanned);
            System.out.println("Total entries pulled across the wire: "
                + (customerEntriesScanned + invoiceEntriesScanned));
        }
        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.compute.PullToClientBaseline
```

Expected output:

```text
=== Pull-to-client baseline ===
Brazilian customers: 5
Top 5 by lifetime spend:
  Luís Gonçalves -> $39.62
  Eduardo Martins -> $37.62
  Alexandre Rocha -> $37.62
  Roberto Almeida -> $37.62
  Fernanda Ramos -> $37.62

Wall time: 49460 us (49 ms)
Customer entries scanned: 59
Invoice entries scanned:  412
Total entries pulled across the wire: 471
```

Five Brazilian customers, ranked by lifetime spend. Luís Gonçalves leads at $39.62. The other four tie at $37.62. The numbers match the cross-cache JOIN output from the previous tutorial because the underlying data is identical and the question is the same.

The two metrics at the bottom of the output are what this class exists to expose. **Total entries pulled across the wire** is the durable measurement. 471 entries (59 customers + 412 invoices) crossed the network so the client could compute the answer. The wall time is the supporting measurement. On a development cluster with 471 entries the pull-and-compute path runs in under 50 ms, but the entries-on-the-wire count grows linearly with the dataset. At 100,000 invoices the same code transfers 100,000 entries every time the question is asked.

The Cache API has no `cache.iterator(predicate)` that pushes filtering to the server. SQL on cache from the previous tutorial does push filtering server-side, but SQL does not let you express custom Java logic. The next two classes show the third option. Keep the custom Java logic. Ship it to the data instead of pulling the data to the client.

{% hint style="info" %}

The 49 ms wall time above is one representative run on a developer Mac with Docker Desktop. Your reproduction will differ by hardware, Docker version, and current load. The entries-on-the-wire count (471) is the part that matches the underlying invariant. The Cache API pulls every entry the client iterates.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** Output shows 5 Brazilian customers ranked by lifetime spend, the top entry is Luís Gonçalves at $39.62, and the totals report 59 Customer entries and 412 Invoice entries scanned (471 total).
{% endhint %}

## Broadcast Aggregation

The pull-to-client baseline brought every entry to the client. The first alternative reverses the direction. The client ships one closure to every server, each server runs the closure against its own primary partitions, and three small partial results return.

Two classes handle this. The first is the closure itself: a serializable object that the Ignite runtime ships to each server and runs there. The second is the client-side driver that calls `compute.broadcast(callable)` and merges the per-node results.

Create `TopSpendCallable.java` in the `compute` package:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/compute/TopSpendCallable.java" %}
```java
package com.example.sqlquery.compute;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.binary.BinaryObject;
import org.apache.ignite.cache.CachePeekMode;
import org.apache.ignite.lang.IgniteCallable;
import org.apache.ignite.resources.IgniteInstanceResource;

/**
 * Closure that runs on each server during a broadcast and returns a
 * partial map of customerId to lifetime spend for customers from the
 * given country whose data lives on this node.
 *
 * The country is captured in the constructor and shipped with the
 * closure. The Ignite field is injected on each executing server.
 *
 * Both cache views use withKeepBinary so the closure reads fields
 * off BinaryObject without instantiating Customer or InvoiceKey
 * POJOs. The data was loaded via SQL and lives in the binary form on
 * the server. The QueryEntity schema is the only metadata the server
 * has. Reading fields by name keeps the closure free of model-class
 * dependencies on the server side.
 */
public class TopSpendCallable implements IgniteCallable<Map<Integer, BigDecimal>>, Serializable {

    private static final long serialVersionUID = 1L;

    private final String country;

    @IgniteInstanceResource
    private transient Ignite local;

    public TopSpendCallable(String country) {
        this.country = country;
    }

    @Override
    public Map<Integer, BigDecimal> call() {
        // localEntries(PRIMARY) iterates only the entries this node
        // owns the canonical copy of, so each entry is processed
        // exactly once across the cluster. withKeepBinary() returns
        // BinaryObject so the closure reads fields by name without
        // rehydrating to a POJO.
        IgniteCache<Integer, BinaryObject> customers =
            local.<Integer, Object>cache("Customer").withKeepBinary();
        IgniteCache<BinaryObject, BinaryObject> invoices =
            local.<Object, Object>cache("Invoice").withKeepBinary();

        Map<Integer, BigDecimal> partialSpend = new HashMap<>();

        // Pass 1: collect country-matching customer IDs from the local
        // primary set.
        for (Cache.Entry<Integer, BinaryObject> entry :
                customers.localEntries(CachePeekMode.PRIMARY)) {
            BinaryObject c = entry.getValue();
            if (country.equals(c.field("country"))) {
                partialSpend.put(entry.getKey(), BigDecimal.ZERO);
            }
        }

        // Pass 2: sum local primary invoices for the matching customers.
        // Because of the @AffinityKeyMapped declaration on
        // InvoiceKey.customerId, every invoice for customer X lives on
        // the same primary as Customer X, so every match is local.
        for (Cache.Entry<BinaryObject, BinaryObject> entry :
                invoices.localEntries(CachePeekMode.PRIMARY)) {
            Integer custId = entry.getKey().field("customerId");
            if (partialSpend.containsKey(custId)) {
                BigDecimal total = entry.getValue().field("total");
                partialSpend.merge(custId, total, BigDecimal::add);
            }
        }

        return partialSpend;
    }
}
```
{% endcode %}

Three Ignite-specific elements are worth naming.

`IgniteCallable<R>` is the closure type. It extends `java.util.concurrent.Callable<R>` and adds nothing but the Ignite-specific marker. The server-side runtime invokes `call()` and returns the value. A Java lambda also works where capture and serialization are simple, but `TopSpendCallable` uses a named class because the closure needs the `@IgniteInstanceResource` field.

`@IgniteInstanceResource` marks a field for cluster injection. When the closure executes on a server, the cluster fills in the field with that server's local `Ignite` instance. The closure uses it to access the local cache views. The annotation lives on a `transient` field so Java serialization does not try to ship a never-set value with the closure.

`localEntries(CachePeekMode.PRIMARY)` is the iteration that makes broadcast aggregation correct. The cluster stores each entry on a primary node and one or more backup nodes for fault tolerance. Asking each node to scan its local primary set means each entry is visited exactly once across the cluster, regardless of how many nodes there are.

Now the client-side driver. Create `BroadcastTopSpend.java`:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/compute/BroadcastTopSpend.java" %}
```java
package com.example.sqlquery.compute;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.IgniteCompute;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

import com.example.sqlquery.model.Customer;

/**
 * Sends one TopSpendCallable to every server in the cluster. Each
 * server returns a partial map of customerId to lifetime spend for
 * the Brazilian customers whose data lives on that server. The client
 * merges the per-node maps and prints the top 5.
 *
 * The first invocation pays peer class loading. The cluster has
 * never seen the closure class until the client ships it. The
 * second invocation reuses the cached class on each server.
 */
public class BroadcastTopSpend {

    public static void main(String[] args) {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500",
                "127.0.0.1:47501",
                "127.0.0.1:47502")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            // forServers() restricts the broadcast to data nodes. The
            // client joined topology but holds no primary partitions.
            IgniteCompute compute = ignite.compute(ignite.cluster().forServers());

            int serverCount = ignite.cluster().forServers().nodes().size();

            // First invoke pays peer class loading. The cluster fetches
            // the closure class bytes from the client over the
            // communication SPI before running the job.
            long t0 = System.nanoTime();
            Collection<Map<Integer, BigDecimal>> coldResults =
                compute.broadcast(new TopSpendCallable("Brazil"));
            long coldMicros = (System.nanoTime() - t0) / 1000;

            // Warm invoke. The class is already on every server, so the
            // timing isolates broadcast plus per-node execution.
            long t1 = System.nanoTime();
            Collection<Map<Integer, BigDecimal>> warmResults =
                compute.broadcast(new TopSpendCallable("Brazil"));
            long warmMicros = (System.nanoTime() - t1) / 1000;

            // Per-node partial maps merge with addition. Primaries are
            // disjoint, so keys do not overlap in practice.
            Map<Integer, BigDecimal> total = new HashMap<>();
            for (Map<Integer, BigDecimal> partial : warmResults) {
                for (Map.Entry<Integer, BigDecimal> e : partial.entrySet()) {
                    total.merge(e.getKey(), e.getValue(), BigDecimal::add);
                }
            }

            IgniteCache<Integer, Customer> customers = ignite.cache("Customer");
            List<Map.Entry<Integer, BigDecimal>> ranked = new ArrayList<>(total.entrySet());
            ranked.sort(Comparator.comparing(Map.Entry<Integer, BigDecimal>::getValue).reversed());

            System.out.println();
            System.out.println("=== Broadcast aggregation ===");
            System.out.println("Server nodes: " + serverCount);
            System.out.println("Top 5 by lifetime spend:");
            int n = Math.min(5, ranked.size());
            for (int i = 0; i < n; i++) {
                Map.Entry<Integer, BigDecimal> e = ranked.get(i);
                Customer c = customers.get(e.getKey());
                System.out.printf("  %s %s -> $%s%n",
                    c.getFirstName(), c.getLastName(), e.getValue());
            }

            System.out.println();
            System.out.println("Wall time (cold, includes peer class load): "
                + coldMicros + " us");
            System.out.println("Wall time (warm, closure class cached):     "
                + warmMicros + " us");
            System.out.println("Per-node partial maps returned: " + warmResults.size());
            int totalCustomers = 0;
            for (Map<Integer, BigDecimal> partial : warmResults) {
                totalCustomers += partial.size();
            }
            System.out.println("Total customer entries in returned maps: " + totalCustomers);
        }
        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.compute.BroadcastTopSpend
```

Expected output:

```text
=== Broadcast aggregation ===
Server nodes: 3
Top 5 by lifetime spend:
  Luís Gonçalves -> $39.62
  Eduardo Martins -> $37.62
  Alexandre Rocha -> $37.62
  Roberto Almeida -> $37.62
  Fernanda Ramos -> $37.62

Wall time (cold, includes peer class load): 20144096 us
Wall time (warm, closure class cached):     17029 us
Per-node partial maps returned: 3
Total customer entries in returned maps: 5
```

Same five Brazilian customers, same totals. The closure ran on each of the three server nodes, the client received three partial maps, and the merge produced one row per customer. The bottom four lines name the cost.

The cold time (about 20 seconds) is the first broadcast invocation. It pays peer class loading. The client serializes the closure, ships the class bytes to each server over the communication SPI, and the servers deserialize and run the code. The warm time (17 ms) is the steady state. The class is already cached on each server, so the cluster runs the closure directly and ships back the result. Subsequent invocations from the same client JVM all run at the warm cost.

The other two metrics are the durable ones. **Per-node partial maps returned** is 3, one per server. **Total customer entries in returned maps** is 5: the entire result of the per-node aggregations. Compared to the pull-to-client baseline's 471 entries on the wire, the broadcast variant moves two orders of magnitude less data across the network.

{% hint style="info" %}

Open `TopSpendCallable.java` and place the cursor on `IgniteCallable`. The IDE shows the interface declaration with a single method, `R call() throws Exception`. The Ignite-specific contract is just the marker that lets `IgniteCompute` ship and execute it. Everything else is JDK-shaped.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** Output shows 3 server nodes, the same 5 Brazilian customers as the baseline, the cold timing in the seconds range, the warm timing in the tens-of-milliseconds range, and exactly 3 partial maps with 5 total customer entries.
{% endhint %}

## Targeted AffinityCall

Broadcast asks every server to do its share. The next pattern is for keyed questions. The answer comes from one customer's data, so the closure should run on the one node that owns that customer.

`IgniteCompute.affinityCall(cacheName, key, callable)` does exactly that. The cluster maps the key to its primary partition in the named cache, looks up the partition's primary node, and ships the closure there. Only one node executes. Use this when the question is "give me X for this specific entity" and the answer is computable from data colocated with that entity.

Create the closure:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/compute/InvoiceSpendCallable.java" %}
```java
package com.example.sqlquery.compute;

import java.io.Serializable;
import java.math.BigDecimal;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.binary.BinaryObject;
import org.apache.ignite.cache.CachePeekMode;
import org.apache.ignite.lang.IgniteCallable;
import org.apache.ignite.resources.IgniteInstanceResource;

/**
 * Closure that runs on the primary node for a single customerId and
 * returns the lifetime spend for that customer.
 *
 * Because of the @AffinityKeyMapped declaration on
 * InvoiceKey.customerId, the customer's invoices are colocated with
 * the customer entry on the same node. The local primary scan finds
 * every invoice for that customer without any cross-node fetch.
 *
 * withKeepBinary so the closure reads fields off BinaryObject
 * without instantiating InvoiceKey or Invoice POJOs on the server.
 */
public class InvoiceSpendCallable implements IgniteCallable<BigDecimal>, Serializable {

    private static final long serialVersionUID = 1L;

    private final Integer customerId;

    @IgniteInstanceResource
    private transient Ignite local;

    public InvoiceSpendCallable(Integer customerId) {
        this.customerId = customerId;
    }

    @Override
    public BigDecimal call() {
        IgniteCache<BinaryObject, BinaryObject> invoices =
            local.<Object, Object>cache("Invoice").withKeepBinary();

        BigDecimal sum = BigDecimal.ZERO;
        for (Cache.Entry<BinaryObject, BinaryObject> entry :
                invoices.localEntries(CachePeekMode.PRIMARY)) {
            Integer custId = entry.getKey().field("customerId");
            if (customerId.equals(custId)) {
                BigDecimal total = entry.getValue().field("total");
                sum = sum.add(total);
            }
        }
        return sum;
    }
}
```
{% endcode %}

The closure is deliberately small. It scans local primary invoices, filters by `customerId`, and sums totals. The `customerId` field is captured in the constructor and shipped with the closure.

Now the driver. It picks customer 1 (Luís Gonçalves, the top-spending Brazilian customer from the broadcast result), prints the routing decision, and calls the closure twice to separate the cold and warm costs:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/compute/AffinityCallByCustomer.java" %}
```java
package com.example.sqlquery.compute;

import java.math.BigDecimal;
import java.util.Arrays;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.IgniteCompute;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.affinity.Affinity;
import org.apache.ignite.cluster.ClusterNode;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

import com.example.sqlquery.model.Customer;

/**
 * Picks one customer ID and ships the closure to the node that owns
 * the corresponding Customer cache entry. The closure scans local
 * primary invoices for that customer and returns the sum.
 *
 * Customer 1 is Luís Gonçalves (Brazil), the top-spending Brazilian
 * customer from the broadcast result.
 */
public class AffinityCallByCustomer {

    public static void main(String[] args) {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList(
                "127.0.0.1:47500",
                "127.0.0.1:47501",
                "127.0.0.1:47502")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            int customerId = 1;
            IgniteCompute compute = ignite.compute();

            // Affinity maps the key to its partition, then the partition
            // to its primary. affinityCall ships the closure to that one
            // primary.
            Affinity<Integer> affinity = ignite.affinity("Customer");
            int partition = affinity.partition(customerId);
            ClusterNode primary = affinity.mapKeyToNode(customerId);

            IgniteCache<Integer, Customer> customers = ignite.cache("Customer");
            Customer c = customers.get(customerId);

            // Cold call pays peer class loading on the target primary
            // when the closure class has not landed there yet.
            long t0 = System.nanoTime();
            BigDecimal coldSpend = compute.affinityCall("Customer", customerId,
                new InvoiceSpendCallable(customerId));
            long coldMicros = (System.nanoTime() - t0) / 1000;

            long t1 = System.nanoTime();
            BigDecimal warmSpend = compute.affinityCall("Customer", customerId,
                new InvoiceSpendCallable(customerId));
            long warmMicros = (System.nanoTime() - t1) / 1000;

            System.out.println();
            System.out.println("=== AffinityCall for one customer ===");
            System.out.printf("Customer %d: %s %s (%s)%n",
                customerId, c.getFirstName(), c.getLastName(), c.getCountry());
            System.out.println("Routing: partition " + partition
                + " primary=" + primary.consistentId());
            System.out.println();
            System.out.println("Lifetime spend: $" + warmSpend);
            System.out.println("Wall time (cold, may include peer class load): "
                + coldMicros + " us");
            System.out.println("Wall time (warm, closure class cached):       "
                + warmMicros + " us");
            if (!coldSpend.equals(warmSpend)) {
                System.err.println("Cold and warm sums diverged: "
                    + coldSpend + " vs " + warmSpend);
                System.exit(2);
            }
        }
        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.compute.AffinityCallByCustomer
```

Expected output:

```text
=== AffinityCall for one customer ===
Customer 1: Luís Gonçalves (Brazil)
Routing: partition 1 primary=0:0:0:0:0:0:0:1%lo,127.0.0.1,172.18.0.3:47502

Lifetime spend: $39.62
Wall time (cold, may include peer class load): 54513 us
Wall time (warm, closure class cached):       11910 us
```

The routing line names the cluster's decision. Customer 1 maps to partition 1, and the primary node for partition 1 advertises the addresses shown. The closure ran on that one server. The result is a single `BigDecimal` with the same $39.62 the broadcast and pull-to-client paths produced for the top-of-list customer.

The warm wall time is around 12 ms. That covers one round trip to ship the closure (already cached as a class on the target node) plus the closure's local primary scan. The cold time is higher because the first invoke also pays peer class loading on the target primary.

Compared to the broadcast variant, the affinityCall variant ships the closure to one node instead of three, processes a smaller subset of the local primary set (only invoices for one customer), and returns one value instead of three partial maps. The trade-off is that the question must be keyed. Broadcast is the right pattern when the answer needs every customer. AffinityCall is the cheapest path when the answer is for a specific customer.

{% hint style="success" %}
**Checkpoint:** Output shows customer 1 is Luís Gonçalves (Brazil), the routing line names a primary node, the lifetime spend is $39.62, and the warm time is under 15 ms.
{% endhint %}

## Compare and Decide

The three classes answer the same question with different placements of the work. Putting the numbers side by side makes the trade-offs concrete.

| Approach | Wall time (warm) | Entries on the wire | Closure shipped |
| --- | --- | --- | --- |
| Pull-to-client baseline | 49 ms | 471 (every customer + every invoice) | n/a |
| Broadcast (3 nodes) | 17 ms | 3 partial maps, 5 customers total | 1 to each node |
| AffinityCall (1 customer) | 12 ms | 1 BigDecimal | 1 to one node |

The wall-time column is one representative run on a developer machine. Your reproduction will land on different absolute numbers. The ordering and the order-of-magnitude gaps are what hold.

The entries-on-the-wire column is the durable measurement. Pull-to-client transfers data linearly with the cache size: on this dataset 471 entries, on a million-row cache a million entries, every time the question is asked. Broadcast transfers data linearly with the result size: 3 partial maps regardless of dataset, with a per-map size that depends on how many rows survived the per-node filter. AffinityCall transfers a single value: the closure plus one return.

Two decision rules fall out of the comparison.

**Result size relative to input size selects the placement.** When the question reduces a large input to a small output (top-N, sum, custom score), shipping the closure beats shipping the data. When the result is a large fraction of the input (return every record matching X without aggregation), the round trip is unavoidable, and pull-to-client is honest. The pull-to-client default applies when the closure overhead exceeds the data transfer it would save.

**The shape of the question selects between broadcast and affinityCall.** Broadcast fans out a global reduction in which every server contributes a partial result that the client merges. AffinityCall targets a single key by shipping the closure to the one node that owns the data. A given service uses both patterns at different call sites. A "lifetime spend across all Brazilian customers" question broadcasts. A "lifetime spend for customer 17" question uses affinityCall.

The choice is per-question, not per-application.

## Summary

You added five classes in a new `compute` package. The same question that the SQL surface answered in the previous tutorial ran three different ways, and the numbers exposed the cost of each placement.

**Pull-to-client when the result is large relative to the input. Otherwise ship the closure.** The Cache API forces the round trip every time the predicate is custom Java. Compute lets you keep the custom Java and skip the round trip.

**Broadcast for global reductions, affinityCall for keyed lookups.** Broadcast runs the closure on every server and merges partial results at the client. AffinityCall picks one primary by key and runs the closure there. The framework is per-question. A service may use both at different call sites.

The deeper reframing is this. The cluster is not just storage. It is a Java runtime that hosts your code on demand. Peer class loading hides the deployment problem. You write `IgniteCallable`, the cluster fetches the closure class bytes from the client over the communication SPI on first invoke, and the closure runs on the server JVM. The `peerClassLoadingEnabled=true` flag in the cluster config is the setting that makes this work.

### What's Next

[Affinity-Aware Compute at Scale](../data-locality/affinity-aware-compute.md) is the design-driven companion to this tutorial. It runs the same APIs (`broadcast`, single-cache `affinityCall`) plus the multi-cache `affinityCall` colocation contract and partition-parallel `affinityCallAsync`, then measures the same approaches at 1,000, 10,000, and 100,000 customers. If you finished this tutorial with the round-trip cost framework, that one gives you the design framework for picking which compute target the schema implies.

Other surfaces this tutorial deferred:

- **`ComputeTask` and `ComputeTaskAdapter`**, the task-based form of compute that supports failover and multi-stage workflows. The closure pattern you used (`IgniteCallable`) is sufficient for stateless one-shot work. Tasks are the right shape for jobs that need retry and partial-failure semantics (coming soon).
- **Failover and retry semantics for compute**, including job timeouts, node failure handling, and split-brain considerations (coming soon).
- **Custom load balancing SPIs** that pick which node receives a given closure when broadcast targeting is too coarse and affinity targeting does not fit (coming soon).

The next tutorial in this learning path takes a different angle. After running queries and shipping compute, the question that has not been asked yet is what happens to the cache when the cluster restarts. Native persistence answers that (coming soon).

### Related

- [From Key-Value to SQL: The JOIN Problem](from-keyvalue-to-sql.md) is the project this tutorial extends. It teaches the SQL surface and colocation declaration this tutorial reuses.
- [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md) is the cluster topology this tutorial runs against. It introduces the partition mental model and ships the three-node compose with the `BasicAddressResolver` configuration.
- [Affinity-Aware Compute at Scale](../data-locality/affinity-aware-compute.md) is the design-driven companion. Same APIs, scale experiment from 1,000 to 100,000 customers.
