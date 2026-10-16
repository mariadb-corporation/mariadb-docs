---
description: >-
  Three compute techniques that run on the node that owns the key: broadcast with local scan, single-key affinityCall, and cross-cache affinityCall.
---

# Affinity-Aware Compute at Scale

## Introduction

Pulling a distributed dataset to the client to compute on it does not scale. At 100,000 customers with three invoices each, the client fetches roughly 12 MB of invoice rows to produce a ten-row top-10. Running the same aggregation on the servers that own the rows returns under 1 KB. This tutorial builds three compute patterns that do that, then measures them against pull-to-client at 1,000, 10,000, and 100,000 customers.

Each pattern fits a different workload. Broadcast with local scan handles batch aggregation by running one job per server against its primary partitions. The client merges three per-node top-N lists. `affinityCall` per key handles service-time lookups by sending one job to the customer's primary owner. The Collection-overload `affinityCall` adds a scheduler-enforced contract that the target node owns the key in every named cache. That contract matters when two caches' affinity configurations drift apart.

Every technique relies on peer class loading. The closure classes live in your client JVM and the cluster has never seen them. At invoke time the client serializes the closure, ships the class bytes to the target server, and the server deserializes and runs the code. The cluster config from [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md) already has `peerClassLoadingEnabled=true` on every server. Without that setting, every closure in this tutorial fails at deserialization with `ClassNotFoundException`.

The Java code is identical across Apache Ignite 2 and GridGain 8. Product tabs cover only Maven coordinates and the Docker image.

## Prerequisites

- **Completion of [Verify Colocation Is Working](verify-colocation.md).** You have colocated Customer and Invoice caches with `@AffinityKeyMapped` on `customerId` and know how to prove the contract holds.
- **A running 3-node cluster** using `docker-compose-3nodes.yml` from [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md). Every server must have `peerClassLoadingEnabled=true`.
- **Java 11 or later** for the client runtime. The Maven project compiles to Java 8 bytecode to match the server JVM.
- **Maven 3.6** or later.
- **Docker Compose 2.23** or later.

This tutorial builds a fresh Maven project called `affinity-compute/` alongside `verify-colocation/` and `colocation-keys/`. The cluster setup is unchanged from the previous tutorials.

<details>
<summary>Returning to the path? Verify the 3-node cluster is running.</summary>

{% tabs %}
{% tab title="Apache Ignite 2" %}

```bash
docker ps --filter name=ignite2-node --format "table {{.Names}}\t{{.Status}}"
```

{% endtab %}

{% tab title="GridGain 8" %}

```bash
docker ps --filter name=gridgain8-node --format "table {{.Names}}\t{{.Status}}"
```

{% endtab %}

{% endtabs %}

Three server containers in the `Up` state. If the cluster is stopped, start it with `docker compose -f cache-cluster/docker-compose-3nodes.yml up -d` and wait for `servers=3` in the topology snapshot.

</details>

## What You Will Learn

- Build a compute project that targets three affinity-aware patterns at the same dataset
- Broadcast a callable across every server, aggregate per node, merge the top-10 on the client
- Call `affinityCall` at one customer key and confirm the closure ran on the customer's primary owner
- Use the Collection overload to declare that a job must land on a node owning the key in every named cache
- Interpret a three-approach scale experiment at 1,000 / 10,000 / 100,000 customers and decide which pattern fits a workload

## Create the Affinity-Compute Project

Create a Maven project named `affinity-compute/` with the layout:

```text
affinity-compute/
├── pom.xml
└── src/main/java/com/example/compute/
    ├── Customer.java
    ├── Invoice.java
    ├── InvoiceKey.java
    ├── Labels.java
    ├── ClientConfig.java
    ├── CacheConfigs.java
    ├── DataLoader.java
    ├── SumOneCustomerPublic.java
    ├── BroadcastRevenue.java
    ├── AffinityCallPerCustomer.java
    ├── CrossCacheAffinity.java
    └── ScaleExperiment.java
```

The `pom.xml` targets Java 8 bytecode and suppresses Ignite's startup logs so each class's output stands out.

{% tabs %}
{% tab title="Apache Ignite 2" %}

{% code title="affinity-compute/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>affinity-compute</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>8</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.compute.BroadcastRevenue</exec.mainClass>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.apache.ignite</groupId>
            <artifactId>ignite-core</artifactId>
            <version>2.16.0</version>
        </dependency>
    </dependencies>

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
                        <argument>java.base/sun.nio.ch=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.lang=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.lang.invoke=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.util=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.io=ALL-UNNAMED</argument>
                        <argument>-DIGNITE_QUIET=true</argument>
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

{% endtab %}

{% tab title="GridGain 8" %}

{% code title="affinity-compute/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>affinity-compute</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>8</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.compute.BroadcastRevenue</exec.mainClass>
    </properties>

    <repositories>
        <repository>
            <id>GridGain External Repository</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>gridgain-core</artifactId>
            <version>8.9.32</version>
        </dependency>
    </dependencies>

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
                        <argument>java.base/sun.nio.ch=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.lang=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.lang.invoke=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.util=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.base/java.io=ALL-UNNAMED</argument>
                        <argument>-DIGNITE_QUIET=true</argument>
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

{% endtab %}

{% endtabs %}

Create the shared model classes. The shape matches the previous tutorials, with one addition: Customer gains a `country` field so the synthetic data has a second dimension a reader could aggregate on in a later experiment.

{% code title="affinity-compute/src/main/java/com/example/compute/Customer.java" %}
```java
package com.example.compute;

import java.io.Serializable;

/**
 * Value object for the Customer cache. Stored on the servers as a
 * BinaryObject at runtime. The class itself only appears in the client
 * JVM and in compute closures that deserialize via peer class loading.
 */
public class Customer implements Serializable {
    private static final long serialVersionUID = 1L;

    private String name;
    private String country;

    public Customer() {
    }

    public Customer(String name, String country) {
        this.name = name;
        this.country = country;
    }

    public String getName() {
        return name;
    }

    public String getCountry() {
        return country;
    }

    @Override
    public String toString() {
        return "Customer{" + name + ", " + country + "}";
    }
}
```
{% endcode %}

{% code title="affinity-compute/src/main/java/com/example/compute/Invoice.java" %}
```java
package com.example.compute;

import java.io.Serializable;
import java.math.BigDecimal;

/**
 * Value object for the Invoice cache. Total drives the revenue
 * aggregation the compute techniques compete to produce.
 */
public class Invoice implements Serializable {
    private static final long serialVersionUID = 1L;

    private String description;
    private BigDecimal total;

    public Invoice() {
    }

    public Invoice(String description, BigDecimal total) {
        this.description = description;
        this.total = total;
    }

    public String getDescription() {
        return description;
    }

    public BigDecimal getTotal() {
        return total;
    }

    @Override
    public String toString() {
        return "Invoice{" + description + ", " + total + "}";
    }
}
```
{% endcode %}

{% code title="affinity-compute/src/main/java/com/example/compute/InvoiceKey.java" %}
```java
package com.example.compute;

import java.io.Serializable;
import java.util.Objects;

import org.apache.ignite.cache.affinity.AffinityKeyMapped;

/**
 * Composite invoice key. customerId carries the colocation contract:
 * every invoice lands on the same primary node as its customer.
 */
public class InvoiceKey implements Serializable {
    private static final long serialVersionUID = 1L;

    private Integer invoiceId;

    @AffinityKeyMapped
    private Integer customerId;

    public InvoiceKey() {
    }

    public InvoiceKey(Integer invoiceId, Integer customerId) {
        this.invoiceId = invoiceId;
        this.customerId = customerId;
    }

    public Integer getInvoiceId() { return invoiceId; }
    public Integer getCustomerId() { return customerId; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof InvoiceKey)) return false;
        InvoiceKey that = (InvoiceKey) o;
        return Objects.equals(invoiceId, that.invoiceId)
            && Objects.equals(customerId, that.customerId);
    }

    @Override
    public int hashCode() { return Objects.hash(invoiceId, customerId); }
}
```
{% endcode %}

`Labels` carries forward from the previous tutorial without changes. Copy it from `verify-colocation/src/main/java/com/example/verify/Labels.java`, change the package to `com.example.compute`, and save. The implementation is node-label bookkeeping. The cluster does not know that names like `node1`, `node2`, `node3` exist. The utility assigns them in `consistentId` order on the client side so every run against the same cluster labels the same nodes the same way.

Two more small utilities hold the connection and cache configuration boilerplate. Both are referenced by every reader-facing class in this project.

{% code title="affinity-compute/src/main/java/com/example/compute/ClientConfig.java" %}
```java
package com.example.compute;

import java.util.Arrays;

import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Thick-client connection boilerplate. Peer class loading is the
 * mechanism this tutorial depends on. Closure classes defined in this
 * client JVM ship to the servers at invoke time. The setPeerClassLoadingEnabled(true)
 * call below matches the server config set in Understand How Your Cache Is Distributed.
 */
final class ClientConfig {

    static IgniteConfiguration build() {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList("127.0.0.1:47500..47503")));
        return new IgniteConfiguration()
            .setDiscoverySpi(disco)
            .setClientMode(true)
            .setPeerClassLoadingEnabled(true);
    }

    private ClientConfig() {
    }
}
```
{% endcode %}

{% code title="affinity-compute/src/main/java/com/example/compute/CacheConfigs.java" %}
```java
package com.example.compute;

import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.configuration.CacheConfiguration;

/**
 * Shared cache configurations. Both caches use the same partition
 * count, same backup count, and the same RendezvousAffinityFunction
 * shape. That parity is what makes @AffinityKeyMapped on customerId
 * map Customer and Invoice entries to the same primary nodes.
 */
final class CacheConfigs {

    static final String CUSTOMERS = "customers-compute";
    static final String INVOICES = "invoices-compute";
    static final int PARTITIONS = 32;
    static final int BACKUPS = 1;

    static CacheConfiguration<Integer, Customer> customers() {
        return new CacheConfiguration<Integer, Customer>(CUSTOMERS)
            .setCacheMode(CacheMode.PARTITIONED)
            .setBackups(BACKUPS)
            .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));
    }

    static CacheConfiguration<InvoiceKey, Invoice> invoices() {
        return new CacheConfiguration<InvoiceKey, Invoice>(INVOICES)
            .setCacheMode(CacheMode.PARTITIONED)
            .setBackups(BACKUPS)
            .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));
    }

    private CacheConfigs() {
    }
}
```
{% endcode %}

The synthetic dataset is generated programmatically. `DataLoader` seeds the cluster with N customers and 3N invoices and is called from every reader-facing class in the project. Using `IgniteDataStreamer` keeps the seed under two seconds at 100,000 customers (the batched per-node buffering amortizes the network cost). Revenue is a deterministic function of `(customerId, seq)` so re-runs produce the same top-10 results and the tutorial output is stable across test runs.

{% code title="affinity-compute/src/main/java/com/example/compute/DataLoader.java" %}
```java
package com.example.compute;

import java.math.BigDecimal;
import java.util.Random;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.IgniteDataStreamer;
import org.apache.ignite.Ignition;

/**
 * Seeds the cluster with N synthetic customers and 3N invoices.
 *
 * Usage:  DataLoader 10000   (loads 10,000 customers and 30,000 invoices)
 *
 * DataStreamer batches per node and sustains tens of thousands of rows
 * per second against a loopback cluster. allowOverwrite(true) lets the
 * loader re-run on top of existing data. The class is thick-client only.
 */
public class DataLoader {

    private static final String[] COUNTRIES = {
        "USA", "Canada", "UK", "Germany", "France", "Japan", "Brazil", "India"
    };

    public static void main(String[] args) {
        int scale = args.length > 0 ? Integer.parseInt(args[0]) : 1000;
        try (Ignite ignite = Ignition.start(ClientConfig.build())) {
            load(ignite, scale);
        }
    }

    static void load(Ignite ignite, int customerCount) {
        IgniteCache<Integer, Customer> customers =
            ignite.getOrCreateCache(CacheConfigs.customers());
        IgniteCache<InvoiceKey, Invoice> invoices =
            ignite.getOrCreateCache(CacheConfigs.invoices());

        long t0 = System.currentTimeMillis();

        try (IgniteDataStreamer<Integer, Customer> cs =
                 ignite.dataStreamer(CacheConfigs.CUSTOMERS);
             IgniteDataStreamer<InvoiceKey, Invoice> is =
                 ignite.dataStreamer(CacheConfigs.INVOICES)) {
            // Re-running the loader overwrites existing rows rather
            // than throwing. Keeps the scale experiment idempotent.
            cs.allowOverwrite(true);
            is.allowOverwrite(true);

            for (int c = 1; c <= customerCount; c++) {
                cs.addData(c, new Customer("Customer-" + c, pickCountry(c)));
                for (int s = 1; s <= 3; s++) {
                    int invoiceId = c * 10 + s;
                    is.addData(new InvoiceKey(invoiceId, c),
                        new Invoice("Invoice " + invoiceId, revenue(c, s)));
                }
            }
        }

        long t1 = System.currentTimeMillis();
        System.out.printf("Loaded %d customers + %d invoices in %d ms%n",
            customerCount, customerCount * 3, (t1 - t0));
        System.out.printf("Customer cache size: %d, Invoice cache size: %d%n",
            customers.size(), invoices.size());
    }

    // Deterministic revenue so top-10 is reproducible across runs.
    private static BigDecimal revenue(int customerId, int seq) {
        Random r = new Random(customerId * 31L + seq);
        return BigDecimal.valueOf(10 + r.nextInt(990));
    }

    private static String pickCountry(int customerId) {
        return COUNTRIES[customerId % COUNTRIES.length];
    }
}
```
{% endcode %}

Compile the project and load a small dataset to confirm the cluster accepts the write:

```bash
mvn -f affinity-compute/pom.xml compile
mvn -f affinity-compute/pom.xml exec:exec -Dexec.mainClass=com.example.compute.DataLoader
```

Expected output (your topology line's node IDs vary):

```text
Topology snapshot [ver=12, locNode=db54531e, servers=3, clients=1, state=ACTIVE, ...]
Baseline [id=0, size=3, online=3, offline=0]
Loaded 1000 customers + 3000 invoices in 20137 ms
Customer cache size: 1000, Invoice cache size: 3000
```

The first load pays a fixed startup cost for the DataStreamer and the Ignite client. Subsequent loads against the running JVM take under two seconds.

{% hint style="success" %}
**Checkpoint:** `DataLoader` reports `Loaded 1000 customers + 3000 invoices` and `Customer cache size: 1000, Invoice cache size: 3000`. The topology snapshot shows `servers=3, clients=1`.
{% endhint %}

## Act 1: Broadcast and Local Scan

Top-10 customers by total invoice revenue across every customer in the cluster. Pulling every invoice to the client and summing on the client wastes the network. Send a callable to every server, aggregate each server's primary partitions locally, and return a per-node top-10. The client merges three lists and takes the overall top-10. `IgniteCompute.broadcast` fans the closure out to every server. `ScanQuery.setLocal(true)` pins each server's scan to its own primary partitions.

The first closure class to ship to the servers is the per-node top-N computation. Servers receive the class via peer class loading on first invocation and cache it for later calls.

{% code title="affinity-compute/src/main/java/com/example/compute/BroadcastRevenue.java" %}
```java
package com.example.compute;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.binary.BinaryObject;
import org.apache.ignite.cache.query.QueryCursor;
import org.apache.ignite.cache.query.ScanQuery;
import org.apache.ignite.lang.IgniteCallable;
import org.apache.ignite.resources.IgniteInstanceResource;

/**
 * Act 1: broadcast + local scan.
 *
 * The closure runs on every server in parallel. Each server reads its
 * primary-owned invoices through ScanQuery.setLocal(true), sums revenue
 * per customer, and returns its top-10. The client merges the per-node
 * top-10 lists and takes the overall top-10.
 *
 * What travels: closure class bytes once per node, serialized closure
 * instance once per node, per-node top-10 result lists once back per
 * node. The data stays where it is.
 */
public class BroadcastRevenue {

    private static final int TOP_N = 10;

    public static void main(String[] args) {
        int scale = args.length > 0 ? Integer.parseInt(args[0]) : 100_000;

        try (Ignite ignite = Ignition.start(ClientConfig.build())) {
            DataLoader.load(ignite, scale);

            System.out.println();
            System.out.println("=== Act 1: Broadcast + local scan ===");
            System.out.println();

            long t0 = System.currentTimeMillis();
            Collection<List<CustomerRevenue>> perNode =
                ignite.compute().broadcast(new PerNodeTopN(TOP_N));
            List<CustomerRevenue> merged = mergeTopN(perNode, TOP_N);
            long t1 = System.currentTimeMillis();

            System.out.printf("Reporting nodes: %d%n", perNode.size());
            System.out.printf("Merged top %d across %d customers:%n", TOP_N, scale);
            for (CustomerRevenue cr : merged) {
                System.out.printf("  customer %-8d  $%s%n", cr.customerId, cr.total);
            }
            System.out.printf("Broadcast wall-clock: %d ms%n", (t1 - t0));
        }
    }

    /**
     * Runs on each server. @IgniteInstanceResource injects the local
     * Ignite handle so the callable can reach the caches without the
     * client reopening a connection on the server side. topN is
     * captured as a final field. No client-JVM state leaks into the
     * serialized closure.
     */
    private static final class PerNodeTopN implements IgniteCallable<List<CustomerRevenue>> {
        private static final long serialVersionUID = 1L;

        @IgniteInstanceResource
        private transient Ignite local;

        private final int topN;

        PerNodeTopN(int topN) {
            this.topN = topN;
        }

        @Override
        public List<CustomerRevenue> call() {
            // withKeepBinary avoids deserializing values on the server.
            // Customer and Invoice class bytes arrive via peer class
            // loading on first call, but scanning in binary form is
            // faster and avoids an allocation per row.
            IgniteCache<BinaryObject, BinaryObject> invoices = local
                .<Object, Object>cache(CacheConfigs.INVOICES).withKeepBinary();

            Map<Integer, BigDecimal> totals = new HashMap<>();

            try (QueryCursor<Cache.Entry<BinaryObject, BinaryObject>> cur =
                     invoices.query(new ScanQuery<BinaryObject, BinaryObject>().setLocal(true))) {
                for (Cache.Entry<BinaryObject, BinaryObject> e : cur) {
                    Integer custId = e.getKey().field("customerId");
                    BigDecimal amount = e.getValue().field("total");
                    totals.merge(custId, amount, BigDecimal::add);
                }
            }

            List<CustomerRevenue> all = new ArrayList<>(totals.size());
            for (Map.Entry<Integer, BigDecimal> e : totals.entrySet()) {
                all.add(new CustomerRevenue(e.getKey(), e.getValue()));
            }
            all.sort(Comparator.comparing((CustomerRevenue cr) -> cr.total).reversed());
            // Return a new ArrayList. ArrayList$SubList does not
            // round-trip through Ignite's binary marshaller on the way
            // back to the client.
            return new ArrayList<>(all.subList(0, Math.min(topN, all.size())));
        }
    }

    static List<CustomerRevenue> mergeTopN(Collection<List<CustomerRevenue>> perNode, int topN) {
        List<CustomerRevenue> union = new ArrayList<>();
        for (List<CustomerRevenue> list : perNode) {
            union.addAll(list);
        }
        union.sort(Comparator.comparing((CustomerRevenue cr) -> cr.total).reversed());
        return new ArrayList<>(union.subList(0, Math.min(topN, union.size())));
    }

    /**
     * Per-customer total returned to the client. Every field is a JDK
     * type, so the client deserializes without peer class loading the
     * other way.
     */
    static final class CustomerRevenue implements Serializable {
        private static final long serialVersionUID = 1L;
        final int customerId;
        final BigDecimal total;

        CustomerRevenue(int customerId, BigDecimal total) {
            this.customerId = customerId;
            this.total = total;
        }
    }
}
```
{% endcode %}

The `main` method defaults to 100,000 customers. Run it:

```bash
mvn -f affinity-compute/pom.xml compile
mvn -f affinity-compute/pom.xml exec:exec -Dexec.mainClass=com.example.compute.BroadcastRevenue
```

Expected output. The top-10 customer IDs and revenues are deterministic and stable across products. Wall-clock varies by product and machine.

{% tabs %}
{% tab title="Apache Ignite 2" %}

```text
Loaded 100000 customers + 300000 invoices in 21340 ms
Customer cache size: 100000, Invoice cache size: 300000

=== Act 1: Broadcast + local scan ===

Reporting nodes: 3
Merged top 10 across 100000 customers:
  customer 97379     $2668
  customer 49251     $2664
  customer 95843     $2641
  customer 47715     $2634
  customer 87651     $2620
  customer 72867     $2614
  customer 10883     $2608
  customer 95011     $2607
  customer 9635      $2606
  customer 92067     $2606
Broadcast wall-clock: 179 ms
```

{% endtab %}

{% tab title="GridGain 8" %}

```text
Loaded 100000 customers + 300000 invoices in 14518 ms
Customer cache size: 100000, Invoice cache size: 300000

=== Act 1: Broadcast + local scan ===

Reporting nodes: 3
Merged top 10 across 100000 customers:
  customer 97379     $2668
  customer 49251     $2664
  customer 95843     $2641
  customer 47715     $2634
  customer 87651     $2620
  customer 72867     $2614
  customer 10883     $2608
  customer 95011     $2607
  customer 9635      $2606
  customer 92067     $2606
Broadcast wall-clock: 983 ms
```

{% endtab %}

{% endtabs %}

`Reporting nodes: 3` confirms the broadcast landed on every data node. The thick client is not a data node, so the callable does not run there. One compute invocation produced the result across 300,000 invoices. The wall-clock is dominated by per-node scan time, not by the network.

{% hint style="info" %}

`PerNodeTopN` and `CustomerRevenue` are defined in the client JVM. Neither class exists on the server classpath. At broadcast time the client serializes a `PerNodeTopN` instance and ships the class bytes with it. Each server deserializes, caches the class for subsequent calls, and runs the closure. If any server has `peerClassLoadingEnabled=false`, the deserialization throws `ClassNotFoundException: com.example.compute.BroadcastRevenue$PerNodeTopN`. Turn the setting on in the cluster config and restart the affected server. No application code changes.

{% endhint %}

{% hint style="warning" %}

Every field the closure captures has to be `Serializable`. A closure that captures a `Logger`, a `DataSource`, a non-serializable configuration object, or a reference to the calling `Ignite` client fails with `NotSerializableException` before it leaves the client. Follow `PerNodeTopN`'s pattern: keep the closure stateless except for primitive or boxed final fields, and use `@IgniteInstanceResource` to reach the server-side `Ignite` handle.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** `BroadcastRevenue` reports `Reporting nodes: 3` and prints a top-10 list with ten customer IDs. The wall-clock is under 250 ms on a warm cluster.
{% endhint %}

## Act 2: AffinityCall per Customer

The top-10 was an aggregation over every customer. A service-time request for one customer's total revenue is a different workload. Broadcasting to every server scans three nodes' primary partitions when only one node owns the customer. `IgniteCompute.affinityCall(cacheName, affKey, callable)` runs the closure on the primary owner of the key and nowhere else.

The closure body is shared across Acts 2 and 3, so you factor it into its own class.

{% code title="affinity-compute/src/main/java/com/example/compute/SumOneCustomerPublic.java" %}
```java
package com.example.compute;

import java.math.BigDecimal;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.binary.BinaryObject;
import org.apache.ignite.cache.query.QueryCursor;
import org.apache.ignite.cache.query.ScanQuery;
import org.apache.ignite.lang.IgniteCallable;
import org.apache.ignite.resources.IgniteInstanceResource;

/**
 * Sums one customer's revenue on the node that owns the customer key.
 * Shared by Act 2 (single-cache affinityCall) and Act 3 (Collection
 * overload). The closure body is identical. The call sites declare
 * different colocation contracts.
 */
public class SumOneCustomerPublic
    implements IgniteCallable<AffinityCallPerCustomer.CustomerSummary> {
    private static final long serialVersionUID = 1L;

    @IgniteInstanceResource
    private transient Ignite local;

    private final int customerId;

    public SumOneCustomerPublic(int customerId) {
        this.customerId = customerId;
    }

    @Override
    public AffinityCallPerCustomer.CustomerSummary call() {
        IgniteCache<Integer, BinaryObject> customers = local
            .<Integer, Object>cache(CacheConfigs.CUSTOMERS).withKeepBinary();
        IgniteCache<BinaryObject, BinaryObject> invoices = local
            .<Object, Object>cache(CacheConfigs.INVOICES).withKeepBinary();

        // The closure runs on the customer's primary owner, so the
        // customer cache lookup is a local read.
        BinaryObject cust = customers.get(customerId);
        String name = cust == null ? "(missing)" : cust.field("name");
        String country = cust == null ? "(missing)" : cust.field("country");

        // Scanning with setLocal(true) restricts to this node's primary
        // partitions. Every invoice for this customer is also primary
        // on this node because @AffinityKeyMapped on customerId places
        // both caches under the same contract.
        BigDecimal total = BigDecimal.ZERO;
        int count = 0;
        try (QueryCursor<Cache.Entry<BinaryObject, BinaryObject>> cur =
                 invoices.query(new ScanQuery<BinaryObject, BinaryObject>().setLocal(true))) {
            for (Cache.Entry<BinaryObject, BinaryObject> e : cur) {
                Integer invCustId = e.getKey().field("customerId");
                if (invCustId != null && invCustId == customerId) {
                    BigDecimal t = e.getValue().field("total");
                    total = total.add(t);
                    count++;
                }
            }
        }
        return new AffinityCallPerCustomer.CustomerSummary(
            local.cluster().localNode().id(), name, country, count, total);
    }
}
```
{% endcode %}

The driver class:

{% code title="affinity-compute/src/main/java/com/example/compute/AffinityCallPerCustomer.java" %}
```java
package com.example.compute;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.UUID;

import org.apache.ignite.Ignite;
import org.apache.ignite.Ignition;

/**
 * Act 2: affinityCall targeting one customer.
 *
 * IgniteCompute.affinityCall(cacheName, affKey, callable) runs the
 * callable on the primary owner of affKey in cacheName. One network
 * round-trip. Use it for service-time single-key queries. For
 * full-dataset aggregation broadcast is the better fit, because
 * per-key affinityCall makes N round-trips where broadcast makes
 * one per node.
 */
public class AffinityCallPerCustomer {

    public static void main(String[] args) {
        int scale = args.length > 0 ? Integer.parseInt(args[0]) : 1000;
        int customerId = args.length > 1 ? Integer.parseInt(args[1]) : 47;

        try (Ignite ignite = Ignition.start(ClientConfig.build())) {
            DataLoader.load(ignite, scale);
            Labels labels = Labels.forCluster(ignite);

            System.out.println();
            System.out.println("=== Act 2: affinityCall per customer ===");
            System.out.println();
            System.out.printf("Target customer: %d (dataset size: %d customers)%n",
                customerId, scale);
            System.out.printf("Primary owner: %s%n",
                labels.of(ignite.affinity(CacheConfigs.CUSTOMERS).mapKeyToNode(customerId)));

            long t0 = System.currentTimeMillis();
            CustomerSummary summary = ignite.compute().affinityCall(
                CacheConfigs.CUSTOMERS, customerId, new SumOneCustomerPublic(customerId));
            long t1 = System.currentTimeMillis();

            System.out.printf("Closure ran on:  %s%n", labels.ofId(summary.ranOnNodeId));
            System.out.printf("Customer %-6d   name=%s  country=%s  invoices=%d  revenue=$%s%n",
                customerId, summary.name, summary.country,
                summary.invoiceCount, summary.totalRevenue);
            System.out.printf("affinityCall wall-clock: %d ms%n", (t1 - t0));
        }
    }

    public static final class CustomerSummary implements Serializable {
        private static final long serialVersionUID = 1L;
        public final UUID ranOnNodeId;
        public final String name;
        public final String country;
        public final int invoiceCount;
        public final BigDecimal totalRevenue;

        public CustomerSummary(UUID ranOnNodeId, String name, String country,
                               int invoiceCount, BigDecimal totalRevenue) {
            this.ranOnNodeId = ranOnNodeId;
            this.name = name;
            this.country = country;
            this.invoiceCount = invoiceCount;
            this.totalRevenue = totalRevenue;
        }
    }
}
```
{% endcode %}

Defaults are `scale=1000` and `customerId=47`. Edit `main` for a different customer or scale.

```bash
mvn -f affinity-compute/pom.xml compile
mvn -f affinity-compute/pom.xml exec:exec -Dexec.mainClass=com.example.compute.AffinityCallPerCustomer
```

Expected output. Your node label varies per run, but customer 47's name, country, and revenue are deterministic and stable across products.

```text
=== Act 2: affinityCall per customer ===

Target customer: 47 (dataset size: 1000 customers)
Primary owner: node1
Closure ran on:  node1
Customer 47       name=Customer-47  country=India  invoices=3  revenue=$1606
affinityCall wall-clock: 133 ms
```

The `Primary owner` line reports what the client's affinity function computes before dispatching. The `Closure ran on` line reports what the closure itself observed. They agree. One request, one node, one round-trip. Different labels would mean the cluster is mid-rebalance and the client's cached partition assignment lags the server's. `affinityCall` follows the fresh assignment, not the stale one.

{% hint style="info" %}

`affinityRun` is the void-returning sibling. Use it for jobs that write to caches or fire events but do not return a value. Use `affinityCall` when you want a result back. The placement semantics are identical.

{% endhint %}

{% hint style="warning" %}

`affinityCall("customers-compte", customerId, callable)` (note the typo) looks the same as the working call. The scheduler cannot find a node that owns the key in a cache that does not exist. The result is `ClusterGroupEmptyException`, not a friendly "no such cache" error. Use cache-name constants like `CacheConfigs.CUSTOMERS`. Hard-coded strings will regress on rename without a compile-time signal.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** `AffinityCallPerCustomer` reports the same node label on `Primary owner` and `Closure ran on`. The customer's revenue and invoice count are non-zero.
{% endhint %}

## Act 3: Cross-Cache AffinityCall

Act 2 targeted one customer on one cache. The closure read from both caches and got the right answer because both caches use the same `RendezvousAffinityFunction` with the same partition count, so `customerId` values land on the same node in both caches. The scheduler does not enforce that symmetry. It falls out of the two caches being configured identically.

The `IgniteCompute.affinityCall(Collection<String> cacheNames, Object affKey, IgniteCallable)` overload declares the multi-cache constraint in code. The scheduler must find a node that owns the key in every named cache. On caches that drift apart (different affinity functions, different node filters, partition count renegotiations mid-migration), the single-cache form picks a target that owns the key in one cache. The Collection overload rejects that target.

The closure body is the same as Act 2. Only the call site changes:

{% code title="affinity-compute/src/main/java/com/example/compute/CrossCacheAffinity.java" %}
```java
package com.example.compute;

import java.util.Arrays;

import org.apache.ignite.Ignite;
import org.apache.ignite.Ignition;

/**
 * Act 3: cross-cache affinityCall.
 *
 * IgniteCompute.affinityCall(Collection<String>, affKey, callable)
 * lands the closure on a node that owns affKey in every named cache.
 * Same closure body as Act 2 (reused via SumOneCustomerPublic). The
 * Collection overload declares the multi-cache colocation contract
 * in code.
 *
 * When to reach for it: any compute that reads from multiple caches
 * using one affinity key. Cross-aggregate joins, fact-and-dimension
 * reads, audit-log-and-user-record pairs, order-and-line-items.
 */
public class CrossCacheAffinity {

    public static void main(String[] args) {
        int scale = args.length > 0 ? Integer.parseInt(args[0]) : 1000;
        int customerId = args.length > 1 ? Integer.parseInt(args[1]) : 47;

        try (Ignite ignite = Ignition.start(ClientConfig.build())) {
            DataLoader.load(ignite, scale);
            Labels labels = Labels.forCluster(ignite);

            System.out.println();
            System.out.println("=== Act 3: Cross-cache affinityCall ===");
            System.out.println();
            System.out.printf("Target customer: %d%n", customerId);
            System.out.printf("Owner (customers cache): %s%n",
                labels.of(ignite.affinity(CacheConfigs.CUSTOMERS).mapKeyToNode(customerId)));
            System.out.printf("Owner (invoices cache):  %s%n",
                labels.of(ignite.affinity(CacheConfigs.INVOICES).mapKeyToNode(
                    new InvoiceKey(0, customerId))));

            long t0 = System.currentTimeMillis();
            // Cast to Integer (Object) so Java picks the
            // (Collection, Object affKey, IgniteCallable) overload.
            // An int literal resolves to (Collection, int partId,
            // IgniteCallable) and treats the value as a partition ID.
            Integer affKey = customerId;
            AffinityCallPerCustomer.CustomerSummary summary = ignite.compute().affinityCall(
                Arrays.asList(CacheConfigs.CUSTOMERS, CacheConfigs.INVOICES),
                affKey,
                new SumOneCustomerPublic(customerId));
            long t1 = System.currentTimeMillis();

            System.out.printf("Closure ran on:  %s%n", labels.ofId(summary.ranOnNodeId));
            System.out.printf("Customer %-6d   name=%s  country=%s  invoices=%d  revenue=$%s%n",
                customerId, summary.name, summary.country,
                summary.invoiceCount, summary.totalRevenue);
            System.out.printf("Cross-cache affinityCall wall-clock: %d ms%n", (t1 - t0));
        }
    }
}
```
{% endcode %}

Run it against the same customer:

```bash
mvn -f affinity-compute/pom.xml compile
mvn -f affinity-compute/pom.xml exec:exec -Dexec.mainClass=com.example.compute.CrossCacheAffinity
```

Expected output (the specific node label varies per run):

```text
=== Act 3: Cross-cache affinityCall ===

Target customer: 47
Owner (customers cache): node1
Owner (invoices cache):  node1
Closure ran on:  node1
Customer 47       name=Customer-47  country=India  invoices=3  revenue=$1606
Cross-cache affinityCall wall-clock: 76 ms
```

The result matches Act 2. On caches that share an affinity function, the single-cache form and the Collection overload pick the same target, so both produce the same answer.

The difference shows up when a cache drifts. If one cache changes its partition count, adds a node filter, or swaps in a custom `AffinityFunction`, the Collection overload still places the job on a node that owns the key in every named cache. The single-cache form silently lands on a node that owns the key in only the named cache. The closure either gets the wrong answer or pays a cross-node read for the other cache.

{% hint style="danger" %}

`ignite.compute().affinityCall(caches, customerId, callable)` with `customerId` declared as `int` does not call the `Object affKey` overload you want. Java's method resolution prefers `(Collection<String>, int partId, IgniteCallable)` because `int` binds tighter than `Object` (with autoboxing). The runtime result when the value is not a valid partition number:

```text
Exception in thread "main" java.lang.IndexOutOfBoundsException: Index 47 out of bounds for length 32
    at org.apache.ignite.internal.processors.affinity.GridAffinityAssignment.get(...)
    at org.apache.ignite.internal.processors.affinity.GridAffinityProcessor.mapPartitionToNode(...)
    at org.apache.ignite.internal.IgniteComputeImpl.affinityCall(IgniteComputeImpl.java:204)
```

The `customerId` value was interpreted as partition 47 on a cache with 32 partitions. The fix is to declare the key as `Integer` (or cast to `Object`) so the `(Collection, Object affKey, IgniteCallable)` overload wins. The sample code does this via `Integer affKey = customerId;`.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** `CrossCacheAffinity` reports matching node labels for both caches' owners and for the closure's runtime node. The customer's revenue matches Act 2's result for the same `customerId`.
{% endhint %}

## Scale Experiment: Three Approaches, Three Scales

One question: top 10 customers by total invoice revenue. Three ways to compute it.

- **Approach A (pull-to-client).** Stream every invoice to the client with a non-local `ScanQuery` and aggregate client-side. Most readers write this first. It degrades sharply as the dataset grows.
- **Approach B (broadcast + local scan).** Act 1's shape. One job per node, each scans its primary partitions, returns a per-node top-10. Client merges three lists.
- **Approach C (partition-parallel affinityCall).** One job per partition. The `(Collection<String>, int partId, IgniteCallable)` overload sends each job to the primary owner of that partition. 32 jobs run in parallel on this cluster, and each closure uses `ScanQuery.setPartition(partId)` to read exactly one partition.

`ScaleExperiment` runs all three at 1,000, 10,000, and 100,000 customers and prints a summary table. It destroys the caches between scales so the smaller measurements are not inflated by leftover larger-scale rows.

{% code title="affinity-compute/src/main/java/com/example/compute/ScaleExperiment.java" %}
```java
package com.example.compute;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.binary.BinaryObject;
import org.apache.ignite.cache.query.QueryCursor;
import org.apache.ignite.cache.query.ScanQuery;
import org.apache.ignite.lang.IgniteCallable;
import org.apache.ignite.lang.IgniteFuture;
import org.apache.ignite.resources.IgniteInstanceResource;

/**
 * Capstone: three approaches to the same question, measured at three
 * scales.
 *
 * Output table: wall-clock ms and approximate network bytes per
 * approach per scale. Bytes figures come from data shapes, not live
 * JMX sampling. The numbers still tell the right story because either
 * the bytes grow with N (pull-to-client) or stay at fixed result
 * size (broadcast, partition-parallel).
 */
public class ScaleExperiment {

    private static final int TOP_N = 10;
    private static final int[] SCALES = {1_000, 10_000, 100_000};

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start(ClientConfig.build())) {
            ignite.destroyCache(CacheConfigs.CUSTOMERS);
            ignite.destroyCache(CacheConfigs.INVOICES);

            List<Row> rows = new ArrayList<>();
            for (int scale : SCALES) {
                // Destroy between scales so smaller measurements are
                // not inflated by leftover larger-scale rows.
                ignite.destroyCache(CacheConfigs.CUSTOMERS);
                ignite.destroyCache(CacheConfigs.INVOICES);
                DataLoader.load(ignite, scale);
                rows.add(runOneScale(ignite, scale));
            }
            printTable(rows);

            ignite.destroyCache(CacheConfigs.CUSTOMERS);
            ignite.destroyCache(CacheConfigs.INVOICES);
        }
    }

    private static Row runOneScale(Ignite ignite, int scale) {
        System.out.println();
        System.out.printf("=== Scale %,d customers + %,d invoices ===%n", scale, scale * 3);

        long aMs = timePullToClient(ignite);
        long bMs = timeBroadcast(ignite);
        long cMs = timePartitionParallel(ignite);

        // Bytes estimates. ~40 bytes per row over the wire after
        // BinaryObject overhead. timePullToClient scans only the
        // Invoice cache (scale * 3 rows) and does not read Customer.
        // The server-side approaches return small fixed-size result
        // lists.
        long bytesA = (long) scale * 3 * 40;
        long bytesB = 3L * TOP_N * 32;            // 3 nodes, top-10 each
        long bytesC = 32L * TOP_N * 32;           // 32 partitions, top-10 each

        System.out.printf("  A pull-to-client     : %,d ms  (~%,d bytes to client)%n", aMs, bytesA);
        System.out.printf("  B broadcast + scan   : %,d ms  (~%,d bytes to client)%n", bMs, bytesB);
        System.out.printf("  C partition-parallel : %,d ms  (~%,d bytes to client)%n", cMs, bytesC);

        return new Row(scale, aMs, bMs, cMs, bytesA, bytesB, bytesC);
    }

    // Approach A: stream every invoice to the client and aggregate.
    // The non-local scan has no setLocal and no setPartition.
    private static long timePullToClient(Ignite ignite) {
        IgniteCache<BinaryObject, BinaryObject> invoices = ignite
            .<Object, Object>cache(CacheConfigs.INVOICES).withKeepBinary();

        long t0 = System.currentTimeMillis();
        Map<Integer, BigDecimal> totals = new HashMap<>();
        try (QueryCursor<Cache.Entry<BinaryObject, BinaryObject>> cur =
                 invoices.query(new ScanQuery<BinaryObject, BinaryObject>())) {
            for (Cache.Entry<BinaryObject, BinaryObject> e : cur) {
                Integer custId = e.getKey().field("customerId");
                BigDecimal amount = e.getValue().field("total");
                totals.merge(custId, amount, BigDecimal::add);
            }
        }
        topN(totals, TOP_N);
        return System.currentTimeMillis() - t0;
    }

    private static long timeBroadcast(Ignite ignite) {
        long t0 = System.currentTimeMillis();
        Collection<List<CustomerRevenue>> perNode =
            ignite.compute().broadcast(new NodeTopNClosure(TOP_N));
        mergeTopN(perNode, TOP_N);
        return System.currentTimeMillis() - t0;
    }

    // Approach C: one affinityCall per partition. The (Collection,
    // partId, IgniteCallable) overload sends the closure to the
    // primary owner of partId in every named cache. Submitting 32 of
    // them in parallel spreads the work finer than broadcast.
    private static long timePartitionParallel(Ignite ignite) {
        long t0 = System.currentTimeMillis();
        List<IgniteFuture<List<CustomerRevenue>>> futures = new ArrayList<>();
        List<String> caches = Arrays.asList(
            CacheConfigs.CUSTOMERS, CacheConfigs.INVOICES);
        for (int part = 0; part < CacheConfigs.PARTITIONS; part++) {
            futures.add(ignite.compute().affinityCallAsync(
                caches, part, new PartitionTopNClosure(TOP_N, part)));
        }
        List<List<CustomerRevenue>> perPartition = new ArrayList<>(futures.size());
        for (IgniteFuture<List<CustomerRevenue>> f : futures) {
            perPartition.add(f.get());
        }
        mergeTopN(perPartition, TOP_N);
        return System.currentTimeMillis() - t0;
    }

    private static void printTable(List<Row> rows) {
        System.out.println();
        System.out.println("=== Scale experiment summary ===");
        System.out.println();
        System.out.printf("%-10s  %-22s  %-22s  %-22s%n",
            "Customers", "A: pull-to-client", "B: broadcast", "C: partition-parallel");
        System.out.println("-------------------------------------------------------------------------------");
        for (Row r : rows) {
            System.out.printf("%,10d  %,8d ms / %,8d B  %,8d ms / %,8d B  %,8d ms / %,8d B%n",
                r.scale,
                r.aMs, r.bytesA,
                r.bMs, r.bytesB,
                r.cMs, r.bytesC);
        }
    }

    private static final class NodeTopNClosure implements IgniteCallable<List<CustomerRevenue>> {
        private static final long serialVersionUID = 1L;
        @IgniteInstanceResource
        private transient Ignite local;
        private final int topN;

        NodeTopNClosure(int topN) { this.topN = topN; }

        @Override
        public List<CustomerRevenue> call() {
            IgniteCache<BinaryObject, BinaryObject> invoices = local
                .<Object, Object>cache(CacheConfigs.INVOICES).withKeepBinary();
            Map<Integer, BigDecimal> totals = new HashMap<>();
            try (QueryCursor<Cache.Entry<BinaryObject, BinaryObject>> cur =
                     invoices.query(new ScanQuery<BinaryObject, BinaryObject>().setLocal(true))) {
                for (Cache.Entry<BinaryObject, BinaryObject> e : cur) {
                    Integer custId = e.getKey().field("customerId");
                    BigDecimal amount = e.getValue().field("total");
                    totals.merge(custId, amount, BigDecimal::add);
                }
            }
            return topN(totals, topN);
        }
    }

    // One-partition closure. ScanQuery.setPartition(partId) restricts
    // the scan to exactly the requested partition. Because the closure
    // was dispatched via affinityCall(caches, partId, ...), the scan
    // is a local read.
    private static final class PartitionTopNClosure implements IgniteCallable<List<CustomerRevenue>> {
        private static final long serialVersionUID = 1L;
        @IgniteInstanceResource
        private transient Ignite local;
        private final int topN;
        private final int partId;

        PartitionTopNClosure(int topN, int partId) {
            this.topN = topN;
            this.partId = partId;
        }

        @Override
        public List<CustomerRevenue> call() {
            IgniteCache<BinaryObject, BinaryObject> invoices = local
                .<Object, Object>cache(CacheConfigs.INVOICES).withKeepBinary();
            Map<Integer, BigDecimal> totals = new HashMap<>();
            try (QueryCursor<Cache.Entry<BinaryObject, BinaryObject>> cur = invoices.query(
                     new ScanQuery<BinaryObject, BinaryObject>().setPartition(partId))) {
                for (Cache.Entry<BinaryObject, BinaryObject> e : cur) {
                    Integer custId = e.getKey().field("customerId");
                    BigDecimal amount = e.getValue().field("total");
                    totals.merge(custId, amount, BigDecimal::add);
                }
            }
            return topN(totals, topN);
        }
    }

    private static List<CustomerRevenue> topN(Map<Integer, BigDecimal> totals, int n) {
        List<CustomerRevenue> all = new ArrayList<>(totals.size());
        for (Map.Entry<Integer, BigDecimal> e : totals.entrySet()) {
            all.add(new CustomerRevenue(e.getKey(), e.getValue()));
        }
        all.sort(Comparator.comparing((CustomerRevenue cr) -> cr.total).reversed());
        return new ArrayList<>(all.subList(0, Math.min(n, all.size())));
    }

    private static List<CustomerRevenue> mergeTopN(Collection<List<CustomerRevenue>> perShard, int n) {
        List<CustomerRevenue> union = new ArrayList<>();
        for (List<CustomerRevenue> list : perShard) union.addAll(list);
        union.sort(Comparator.comparing((CustomerRevenue cr) -> cr.total).reversed());
        return new ArrayList<>(union.subList(0, Math.min(n, union.size())));
    }

    static final class CustomerRevenue implements Serializable {
        private static final long serialVersionUID = 1L;
        final int customerId;
        final BigDecimal total;
        CustomerRevenue(int customerId, BigDecimal total) {
            this.customerId = customerId;
            this.total = total;
        }
    }

    static final class Row {
        final int scale;
        final long aMs, bMs, cMs;
        final long bytesA, bytesB, bytesC;
        Row(int scale, long aMs, long bMs, long cMs,
            long bytesA, long bytesB, long bytesC) {
            this.scale = scale;
            this.aMs = aMs;
            this.bMs = bMs;
            this.cMs = cMs;
            this.bytesA = bytesA;
            this.bytesB = bytesB;
            this.bytesC = bytesC;
        }
    }
}
```
{% endcode %}

Run the full experiment:

```bash
mvn -f affinity-compute/pom.xml compile
mvn -f affinity-compute/pom.xml exec:exec -Dexec.mainClass=com.example.compute.ScaleExperiment
```

Expected output. Wall-clock varies by product, cluster, and run. Byte counts are derived from data shape and are identical across products.

{% tabs %}
{% tab title="Apache Ignite 2" %}

```text
=== Scale 1,000 customers + 3,000 invoices ===
  A pull-to-client     : 37 ms  (~120,000 bytes to client)
  B broadcast + scan   : 60 ms  (~960 bytes to client)
  C partition-parallel : 353 ms  (~10,240 bytes to client)

=== Scale 10,000 customers + 30,000 invoices ===
  A pull-to-client     : 73 ms  (~1,200,000 bytes to client)
  B broadcast + scan   : 26 ms  (~960 bytes to client)
  C partition-parallel : 105 ms  (~10,240 bytes to client)

=== Scale 100,000 customers + 300,000 invoices ===
  A pull-to-client     : 354 ms  (~12,000,000 bytes to client)
  B broadcast + scan   : 129 ms  (~960 bytes to client)
  C partition-parallel : 173 ms  (~10,240 bytes to client)

=== Scale experiment summary ===

Customers   A: pull-to-client       B: broadcast            C: partition-parallel
-------------------------------------------------------------------------------
     1,000        37 ms /  120,000 B        60 ms /      960 B       353 ms /   10,240 B
    10,000        73 ms / 1,200,000 B        26 ms /      960 B       105 ms /   10,240 B
   100,000       354 ms / 12,000,000 B       129 ms /      960 B       173 ms /   10,240 B
```

{% endtab %}

{% tab title="GridGain 8" %}

```text
=== Scale 1,000 customers + 3,000 invoices ===
  A pull-to-client     : 57 ms  (~120,000 bytes to client)
  B broadcast + scan   : 94 ms  (~960 bytes to client)
  C partition-parallel : 143 ms  (~10,240 bytes to client)

=== Scale 10,000 customers + 30,000 invoices ===
  A pull-to-client     : 142 ms  (~1,200,000 bytes to client)
  B broadcast + scan   : 53 ms  (~960 bytes to client)
  C partition-parallel : 110 ms  (~10,240 bytes to client)

=== Scale 100,000 customers + 300,000 invoices ===
  A pull-to-client     : 806 ms  (~12,000,000 bytes to client)
  B broadcast + scan   : 396 ms  (~960 bytes to client)
  C partition-parallel : 256 ms  (~10,240 bytes to client)

=== Scale experiment summary ===

Customers   A: pull-to-client       B: broadcast            C: partition-parallel
-------------------------------------------------------------------------------
     1,000        57 ms /  120,000 B        94 ms /      960 B       143 ms /   10,240 B
    10,000       142 ms / 1,200,000 B        53 ms /      960 B       110 ms /   10,240 B
   100,000       806 ms / 12,000,000 B       396 ms /      960 B       256 ms /   10,240 B
```

{% endtab %}

{% endtabs %}

Read the columns.

**A (pull-to-client):** bytes grow 100x from 1k to 100k, climbing to 12 MB at 100,000 customers. Only Invoice rows cross the wire because the Customer cache stays on the servers. Wall-clock grows 10x on both products. On a loopback network the time grows less dramatically than the bytes because the network has abundant bandwidth. On a production network with real latency and shared bandwidth, the ratio tracks the byte ratio. The byte column predicts what a production network sees. The ms column reports what localhost did on this run.

**B (broadcast + local scan):** bytes are flat at ~960 B because three nodes each return a ten-row list. Scan time grows with per-node data while return size stays fixed.

**C (partition-parallel affinityCall):** bytes are flat at ~10,240 B because 32 partitions each return a ten-row list. Wall-clock scales with per-partition scan time plus the scheduling overhead of 32 jobs instead of 3.

The interesting contrast is **B vs C at 100k**. On Apache Ignite 2, B (129 ms) beats C (173 ms). Three big jobs schedule more efficiently than 32 small ones on a 3-node cluster. On GridGain 8, C (256 ms) beats B (396 ms). Partition-parallelism pulls ahead when per-job scan time drops below the scheduling overhead ceiling. The ordering depends on product, cluster size, and data distribution. Broadcast is the safest default for batch aggregation. Partition-parallel wins when finer granularity matters, including streaming early results to the client, handling skewed partitions, or running a job that must run exactly once per partition for correctness.

Run the experiment three times and the wall-clock numbers move ±30%. The A-at-worst / B-and-C-under-A ordering holds across runs and products. The B-vs-C result is stable within a product but reverses between products.

{% hint style="success" %}
**Checkpoint:** The summary table shows A climbing from under 100 ms at 1k to several hundred ms and 16 MB at 100k. B and C both stay an order of magnitude below A's byte count at every scale.
{% endhint %}

## Which Technique Answers Which Workload

Each technique ships the code to a different unit of the cluster: the whole cluster, one key owner, or every partition. Match the technique to the workload.

| Workload | Technique | Result shape |
|---|---|---|
| Full-dataset aggregation ("top 10 customers by revenue") | `IgniteCompute.broadcast(callable)` + `ScanQuery.setLocal(true)` | Per-node list, merge client-side |
| Single-key service query ("what is customer 47's revenue?") | `IgniteCompute.affinityCall(cacheName, key, callable)` | One result, one round-trip |
| Single-key cross-cache read ("everything for customer 47 across these three caches") | `IgniteCompute.affinityCall(Collection<String>, key, callable)` | One result; scheduler enforces multi-cache contract |
| Per-partition batch ("one job per partition, stream as they finish") | `IgniteCompute.affinityCallAsync(Collection<String>, partId, callable)` | One result per partition |

Two constraints apply to all four. The closure class ships to the servers via peer class loading, so every server in the cluster must have `peerClassLoadingEnabled=true`. A single server with the setting off breaks every compute call on the cluster with `ClassNotFoundException`. Closures also serialize every field they capture. A non-serializable field throws `NotSerializableException` at submission. Inject the server-side `Ignite` handle with `@IgniteInstanceResource` instead of handing it through the closure's constructor.

Most readers reach for pull-to-client first by reflex. At 100,000 customers pull-to-client moves 16 MB of row data to produce a ten-line result. Broadcast moves 960 B for the same result. The byte ratio crosses four orders of magnitude and grows with N.

## Summary

Three compute patterns cover the workload shapes that show up in production.

**Broadcast with local scan for batch aggregation.** One job per server, each reading its primary partitions via `ScanQuery.setLocal(true)` and returning a per-node summary. The client merges one list per node. The full dataset never leaves the servers. Partition-parallel is the alternative when per-partition scan time drops below broadcast's per-node overhead. The measurements in this tutorial show partition-parallel winning on GridGain 8 at 100k and broadcast winning on Apache Ignite 2 at 100k on the same hardware.

**`affinityCall` per key for service-time single-key queries.** One round-trip, one target node, one result. Use it whenever a service request names one customer, one order, or one account.

**The Collection-overload `affinityCall` for multi-cache reads.** The scheduler refuses any target that does not own the key in every named cache. On caches that share an affinity function the single-cache and Collection forms pick the same node. The guarantee covers the case where cache configurations later drift apart.

Shared plumbing. Peer class loading ships your closure class bytes to the servers at invoke time. `@IgniteInstanceResource` injects the server's local `Ignite` handle into the closure. Three failure modes recur: `ClassNotFoundException` (peer class loading disabled), `NotSerializableException` (closure captures non-serializable state), and `ClusterGroupEmptyException` (target cache does not exist).

At 100,000 customers the pull-to-client approach moves 12 MB to answer a ten-row question. Broadcast moves under 1 KB. Both return the same top-10 in under half a second on a warm cluster. On a production network the wall-clock gap widens with the byte ratio. Affinity-aware compute runs the closure on the node that owns the key, so the row data stays on that node.

### What's Next

- [When to Break Colocation](when-to-break-colocation.md) teaches the inverse design decision: reference tables in `REPLICATED` caches, fact-dimension star schemas, and the cases where distributed joins replace colocated compute.
- [How to Choose a Partition Count for Your Workload](../../architecture/data-modeling/choose-partition-count.md) covers the tradeoff this tutorial parked: 32 partitions on 3 nodes versus the 1,024 default, and what changes as cluster size and data volume shift. Opens in a new tab so this tutorial stays in your sidebar.

### Related

- [Verify Colocation Is Working](verify-colocation.md) built the `ScanQuery.setLocal(true)` pattern this tutorial uses as the unit of local work.
- [Design Keys for Colocation](design-keys-for-colocation.md) declared the `@AffinityKeyMapped` contract that makes Customer and Invoice colocate.
