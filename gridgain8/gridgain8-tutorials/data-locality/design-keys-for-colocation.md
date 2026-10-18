---
description: >-
  Three mechanisms control where related entries live in the cluster: composite keys with @AffinityKeyMapped, the AffinityKey wrapper, and CacheKeyConfiguration.
---

# Design Keys for Colocation

## Introduction

A partitioned cache distributes entries across nodes by hashing the key. That behavior works for lookups, but a production schema needs more control. When a customer has a hundred invoices, the cluster has no reason to keep them together. Invoice keys hash independently of the customer's key, so the invoices land on whichever nodes their hashes pick.

A cross-cache read walks the network. A cross-cache join ships rows between nodes. A compute job pulls bytes from wherever the data happens to be.

Colocation fixes this. You tell the cluster to hash each invoice by its customer ID instead of by the invoice's own key, so every invoice for customer 42 lands on the same partition as customer 42 itself. Reads, joins, and compute all stay local.

GridGain 8 exposes three mechanisms for declaring this relationship. All three produce the same runtime placement. They differ on one dimension, the location of the declaration: on the key class, at the call site, or on the cache configuration. Each location fails differently when something goes wrong. Picking among them is a design decision about which failure mode your team can catch.

You build three small programs in this tutorial, one per mechanism, against a Customer and Invoice schema. Each program creates two caches, puts three customers and three invoices per customer, and uses `Affinity.mapKeyToNode` to confirm every invoice lands on its customer's node. The comparison at the end turns the three mechanisms into a decision framework.

## Prerequisites

- **A running 3-node cluster** from [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md). Use the `docker-compose-3nodes.yml` file from that tutorial.
- **Familiarity with the Affinity API.** This tutorial uses `ignite.affinity(cacheName).mapKeyToNode(key)` as the confirmation tool without reintroducing it.
- **Java 11 or later** for the client runtime. The Maven project compiles to Java 8 bytecode to match the server JVM.
- **Maven 3.6** or later
- **Docker Compose 2.23** or later

This tutorial builds a fresh Maven project called `colocation-keys/` alongside `cache-distribution/`. The cluster setup is unchanged.

<details>
<summary>Returning to these tutorials? Verify the 3-node cluster is running.</summary>

```bash
docker ps --filter name=gridgain8-node --format "table {{.Names}}\t{{.Status}}"
```

Expected output:

```text
NAMES              STATUS
gridgain8-node1    Up X minutes
gridgain8-node2    Up X minutes
gridgain8-node3    Up X minutes
```

If the cluster is not running, start it:

```bash
docker compose -f cache-cluster/docker-compose-3nodes.yml up -d
```

Wait a few seconds and confirm the topology reports three servers:

```bash
docker logs gridgain8-node1 2>&1 | grep "Topology snapshot" | tail -1
```

You want `servers=3` in the snapshot line.

</details>

## What You Will Learn

- Build a Customer + Invoice schema with a shared client-side Labels utility for readable output
- Declare colocation with the `@AffinityKeyMapped` annotation on a composite key class
- Declare colocation with the `AffinityKey<K>` wrapper at the call site, using a plain `Integer` cache key
- Declare colocation with `CacheKeyConfiguration` on the cache, using a plain key class with no annotations
- Compare the three mechanisms and pick the one you would use for a real schema

## Create the Colocation-Keys Project

Create a Maven project named `colocation-keys/` with the following layout:

```text
colocation-keys/
├── pom.xml
└── src/main/java/com/example/colocation/
    ├── Customer.java
    ├── Invoice.java
    ├── Labels.java
    ├── AnnotationColocation.java
    ├── WrapperColocation.java
    └── ConfigurationColocation.java
```

You create three of the files in this step. The other three, one per mechanism, come in the steps that follow.

The `pom.xml` targets Java 8 bytecode and suppresses the engine's startup logs so the program output stands out:

{% code title="colocation-keys/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>colocation-keys</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>8</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.colocation.AnnotationColocation</exec.mainClass>
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

Create the two domain POJOs. They carry no affinity-related annotations because colocation is a key-side concern. The same Customer and Invoice value types work for all three mechanisms.

{% code title="colocation-keys/src/main/java/com/example/colocation/Customer.java" %}
```java
package com.example.colocation;

import java.io.Serializable;

/**
 * Value object stored in the Customer cache. The same class serves all
 * three mechanisms because colocation is declared on the key side, not
 * the value side. The key-construction shape changes between mechanisms.
 * The stored Customer is identical.
 *
 * Serializable is required because the cache moves values over the
 * network to remote nodes. serialVersionUID fixes a stable identity
 * so adding new fields later does not invalidate already-cached
 * entries.
 */
public class Customer implements Serializable {
    private static final long serialVersionUID = 1L;

    private String name;

    // No-arg constructor exists for deserialization. The engine
    // rebuilds the value on a remote node by calling the default
    // constructor and then populating fields.
    public Customer() {
    }

    public Customer(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Customer{" + name + "}";
    }
}
```
{% endcode %}

{% code title="colocation-keys/src/main/java/com/example/colocation/Invoice.java" %}
```java
package com.example.colocation;

import java.io.Serializable;
import java.math.BigDecimal;

/**
 * Value object stored in the Invoice cache. Like Customer, this POJO is
 * identical across all three mechanisms. The mechanism choice changes
 * how the invoice is keyed, not what is stored under the key.
 *
 * BigDecimal is used for the monetary total to avoid the precision loss
 * that float and double introduce for decimal fractions. Cached money
 * values should always use BigDecimal.
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

The `Labels` utility gives each cluster node a stable `node1/node2/node3` synonym so program output never shows Docker-generated UUIDs. Each of the three mechanism classes uses it to format its output.

{% code title="colocation-keys/src/main/java/com/example/colocation/Labels.java" %}
```java
package com.example.colocation;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import org.apache.ignite.Ignite;
import org.apache.ignite.cluster.ClusterNode;

/**
 * Client-side synonym assignment for cluster nodes. The cluster does not
 * know these labels exist. They are purely for output formatting so the
 * program never prints raw Docker-assigned UUIDs.
 *
 * Two identifiers per node matter. ClusterNode.id() returns a runtime
 * UUID that Docker regenerates on every container restart. The cache
 * uses this UUID at runtime, and the map below uses it as the lookup
 * key. ClusterNode.consistentId() derives from host and discovery port,
 * which stay fixed across restarts. The sort below uses this stable
 * value to assign node1/node2/node3 labels consistently.
 */
final class Labels {
    private final Map<UUID, String> byId = new HashMap<>();

    private Labels() {
    }

    /**
     * Build a label map from the cluster's current server nodes.
     * forServers() returns only nodes that host data, so the test
     * client this program runs inside stays out of the label table.
     */
    static Labels forCluster(Ignite ignite) {
        Labels labels = new Labels();
        List<ClusterNode> servers = new ArrayList<>(ignite.cluster().forServers().nodes());
        // Stable label order across runs. Two runs against the same
        // docker-compose cluster produce the same node1/node2/node3
        // assignments even though the runtime UUIDs differ each time.
        servers.sort(Comparator.comparing(n -> n.consistentId().toString()));
        for (int i = 0; i < servers.size(); i++) {
            labels.byId.put(servers.get(i).id(), "node" + (i + 1));
        }
        return labels;
    }

    String of(ClusterNode node) {
        return node == null ? "(none)" : byId.getOrDefault(node.id(), "(unknown)");
    }
}
```
{% endcode %}

Compile the project:

```bash
mvn -f colocation-keys/pom.xml compile
```

The build succeeds with only the three files above plus the `pom.xml`. The three mechanism classes come next.

{% hint style="success" %}
**Checkpoint:** The Maven build finishes with `BUILD SUCCESS` and the project contains `Customer.class`, `Invoice.class`, and `Labels.class`.
{% endhint %}

## Mechanism 1: Annotation on the Composite key

The first mechanism puts the colocation declaration on the key class. `InvoiceKey` carries two fields: `invoiceId` identifies the invoice, and `customerId` drives partition placement because of the `@AffinityKeyMapped` annotation. Every caller that constructs an `InvoiceKey` carries the colocation intent automatically.

If you came from [From Key-Value to SQL](../beyond-key-value/from-keyvalue-to-sql.md), this is the annotation you used to fix a JOIN. Here it is one of three mechanisms, and the reason it fixed the JOIN is the same reason it colocates any parent-child relationship in a real schema.

Create `AnnotationColocation.java`:

{% code title="colocation-keys/src/main/java/com/example/colocation/AnnotationColocation.java" %}
```java
package com.example.colocation;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.Objects;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.affinity.Affinity;
import org.apache.ignite.cache.affinity.AffinityKeyMapped;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Mechanism 1: declare colocation on the key class.
 *
 * The InvoiceKey class carries two fields. customerId is annotated with
 * @AffinityKeyMapped, so the default affinity mapper reads that field's
 * value and hands it to the cache's affinity function. Every invoice
 * lands on the same partition as the customer whose ID matches,
 * regardless of the invoiceId value.
 *
 * Every caller that constructs an InvoiceKey carries the colocation
 * intent automatically. The key class is the single source of truth.
 */
public class AnnotationColocation {

    // Cache names are per-mechanism so the three programs in this
    // tutorial can run in sequence without cache-name collisions.
    // Each program also destroys its caches at the end.
    private static final String CUSTOMERS = "customers-annotation";
    private static final String INVOICES = "invoices-annotation";

    // 32 partitions matches the prior tutorial. Low enough that the
    // per-node counts are countable by hand, high enough that three
    // customers can land on different nodes. Production defaults to
    // 1024. The 32 in this tutorial is a teaching number, not a
    // production one.
    //
    // Both caches in a colocation pair must use the same partition
    // count. Colocation holds only when both caches hash to the same
    // partition under the same affinity function, and that partition
    // is owned by the same primary node. Mismatch the counts (32 on
    // one cache, 1024 on its pair) and the keys land in different
    // partitions even when the affinity field is identical.
    private static final int PARTITIONS = 32;

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start(clientConfig())) {
            Labels labels = Labels.forCluster(ignite);

            // Customer key is a primitive Integer, so the default
            // affinity mapper uses the key itself; no override needed.
            CacheConfiguration<Integer, Customer> customerCfg =
                new CacheConfiguration<Integer, Customer>(CUSTOMERS)
                    .setCacheMode(CacheMode.PARTITIONED)
                    .setBackups(1)
                    .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));

            // Invoice cache needs no affinity override either. The
            // default mapper scans InvoiceKey for @AffinityKeyMapped,
            // finds customerId, and partitions on that field's value.
            // The annotation on the key class is the entire mechanism.
            CacheConfiguration<InvoiceKey, Invoice> invoiceCfg =
                new CacheConfiguration<InvoiceKey, Invoice>(INVOICES)
                    .setCacheMode(CacheMode.PARTITIONED)
                    .setBackups(1)
                    .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));

            IgniteCache<Integer, Customer> customers = ignite.getOrCreateCache(customerCfg);
            IgniteCache<InvoiceKey, Invoice> invoices = ignite.getOrCreateCache(invoiceCfg);

            customers.put(1, new Customer("Acme"));
            customers.put(2, new Customer("Globex"));
            customers.put(3, new Customer("Initech"));

            // Invoice IDs are synthetic (customerId*100 + seq). The ID
            // itself is unrelated to placement. @AffinityKeyMapped on
            // InvoiceKey.customerId drives partition selection.
            for (int customerId = 1; customerId <= 3; customerId++) {
                for (int seq = 1; seq <= 3; seq++) {
                    int invoiceId = customerId * 100 + seq;
                    invoices.put(new InvoiceKey(invoiceId, customerId),
                        new Invoice("Invoice " + invoiceId, new BigDecimal(100 + seq)));
                }
            }

            // ignite.affinity(cacheName) computes partition ownership
            // from the client's cached topology view as a pure function
            // of the key. No cache reads, no network round-trips.
            Affinity<Integer> custAff = ignite.affinity(CUSTOMERS);
            Affinity<InvoiceKey> invAff = ignite.affinity(INVOICES);

            System.out.println();
            System.out.println("=== Mechanism 1: @AffinityKeyMapped on composite key ===");
            System.out.println();
            System.out.printf("%-10s %-12s %-40s%n", "Customer", "Node", "Invoice nodes (per invoice)");
            System.out.println("-----------------------------------------------------------------");

            int colocated = 0;
            int total = 0;
            for (int customerId = 1; customerId <= 3; customerId++) {
                String custNode = labels.of(custAff.mapKeyToNode(customerId));
                StringBuilder invNodes = new StringBuilder();
                for (int seq = 1; seq <= 3; seq++) {
                    InvoiceKey key = new InvoiceKey(customerId * 100 + seq, customerId);
                    String invNode = labels.of(invAff.mapKeyToNode(key));
                    if (invNodes.length() > 0) invNodes.append(", ");
                    invNodes.append(invNode);
                    total++;
                    if (invNode.equals(custNode)) colocated++;
                }
                System.out.printf("%-10d %-12s %-40s%n", customerId, custNode, invNodes.toString());
            }
            System.out.println();
            System.out.printf("Colocated %d of %d invoices with their customer.%n", colocated, total);

            // Clean up so the next mechanism starts against an empty
            // cluster.
            ignite.destroyCache(CUSTOMERS);
            ignite.destroyCache(INVOICES);
        }
    }

    /**
     * Thick-client config. The address range 47500-47503 covers the
     * one-, three-, and four-node cluster shapes from the prior
     * tutorial; unreachable ports in the range are skipped at connect.
     */
    private static IgniteConfiguration clientConfig() {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList("127.0.0.1:47500..47503")));
        return new IgniteConfiguration()
            .setDiscoverySpi(disco)
            // Client mode. The JVM joins the cluster but does not host
            // partitions or participate in the baseline. Clients expose
            // the full thick-client API including the Affinity handle
            // used above.
            .setClientMode(true)
            // Peer class loading lets the client ship custom classes
            // (InvoiceKey, compute closures, EntryProcessors) to server
            // nodes without a shared classpath. Without this flag, the
            // server would reject InvoiceKey as an unknown class.
            .setPeerClassLoadingEnabled(true);
    }

    /**
     * Composite cache key. invoiceId identifies the invoice. customerId
     * drives partitioning because it carries the @AffinityKeyMapped
     * annotation.
     *
     * A key class for a partitioned cache needs four things:
     * Serializable implementation (keys move between nodes),
     * serialVersionUID (stable identity for the serialization format),
     * equals and hashCode over every identifying field (the cache uses
     * them for key uniqueness), and at most one @AffinityKeyMapped
     * field (the annotation is unique per class; a second one is a
     * configuration error that the engine rejects).
     */
    public static class InvoiceKey implements Serializable {
        private static final long serialVersionUID = 1L;

        private Integer invoiceId;

        // Marks customerId as the affinity key. The default affinity
        // mapper discovers this annotation via reflection on first use
        // and caches the result. The field name is arbitrary. The
        // mapper looks for the annotation, not the name.
        @AffinityKeyMapped
        private Integer customerId;

        public InvoiceKey() {
        }

        public InvoiceKey(Integer invoiceId, Integer customerId) {
            this.invoiceId = invoiceId;
            this.customerId = customerId;
        }

        public Integer getInvoiceId() {
            return invoiceId;
        }

        public Integer getCustomerId() {
            return customerId;
        }

        // equals and hashCode cover both fields. Two InvoiceKey
        // instances with the same invoiceId but different customerIds
        // reference different invoices and must not compare equal. The
        // affinity field participates in identity like any other field.
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof InvoiceKey)) return false;
            InvoiceKey that = (InvoiceKey) o;
            return Objects.equals(invoiceId, that.invoiceId)
                && Objects.equals(customerId, that.customerId);
        }

        @Override
        public int hashCode() {
            return Objects.hash(invoiceId, customerId);
        }
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f colocation-keys/pom.xml compile
mvn -f colocation-keys/pom.xml exec:exec -Dexec.mainClass=com.example.colocation.AnnotationColocation
```

Expected output:

```text
=== Mechanism 1: @AffinityKeyMapped on composite key ===

Customer   Node         Invoice nodes (per invoice)
-----------------------------------------------------------------
1          node1        node1, node1, node1
2          node2        node2, node2, node2
3          node2        node2, node2, node2

Colocated 9 of 9 invoices with their customer.
```

Your specific node assignments differ from the output above. Docker regenerates node IDs on every restart, so the rendezvous function picks different primaries. The invariant is what matters. For each customer, every invoice row in that customer's line shows the same node as the customer itself. Nine out of nine.

Delete the `@AffinityKeyMapped` annotation from `customerId`, rebuild, and rerun, and the colocation invariant breaks. The invoice key's default hash has nothing to do with the customer ID, so invoices scatter. The annotation is the contract.

{% hint style="info" %}

Open `InvoiceKey.java` and run **Find Usages** on the `@AffinityKeyMapped` annotation or on the `customerId` field. Every call site that constructs an `InvoiceKey` shows up. A schema audit can walk the call-site list and verify each one passes a real customer ID. The annotation makes the colocation contract discoverable from the key class outward.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** The program prints `Colocated 9 of 9 invoices with their customer.` Every invoice on each customer's line shows the same node as the customer's node.
{% endhint %}

## Mechanism 2: AffinityKey Wrapper at the Call Site

The second mechanism moves the declaration from the key class to the call site. `AffinityKey<K>` is a library-provided wrapper. You construct it with two values: the invoice ID (the cache key) and the customer ID (the affinity key). The invoice cache has no custom key class. Colocation is declared once per `put`, by the caller.

This is the right mechanism when the key class cannot be changed. Third-party types, generated code, or a legacy key that already ships in production all fit this shape. It is also useful when colocation is conditional on runtime state, where one code path wraps the invoice with the customer ID and another wraps it with a different value entirely.

Create `WrapperColocation.java`:

{% code title="colocation-keys/src/main/java/com/example/colocation/WrapperColocation.java" %}
```java
package com.example.colocation;

import java.math.BigDecimal;
import java.util.Arrays;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.affinity.Affinity;
import org.apache.ignite.cache.affinity.AffinityKey;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Mechanism 2: declare colocation at the call site using AffinityKey.
 *
 * AffinityKey is a library-provided wrapper around any cache key. It
 * holds two values: the underlying key and a separate affinity key.
 * The wrapper's equals and hashCode delegate to the underlying key,
 * so the cache treats two wrappers with equal keys as identical. The
 * affinity key field only affects placement.
 *
 * No custom key class. No annotations. The declaration lives in the
 * new AffinityKey(key, affKey) call at each put site. The call site
 * owns the colocation contract.
 */
public class WrapperColocation {

    private static final String CUSTOMERS = "customers-wrapper";
    private static final String INVOICES = "invoices-wrapper";
    private static final int PARTITIONS = 32;

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start(clientConfig())) {
            Labels labels = Labels.forCluster(ignite);

            CacheConfiguration<Integer, Customer> customerCfg =
                new CacheConfiguration<Integer, Customer>(CUSTOMERS)
                    .setCacheMode(CacheMode.PARTITIONED)
                    .setBackups(1)
                    .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));

            // The Invoice cache's key type is AffinityKey<Integer>, not
            // Integer. The wrapper is itself the cache key and carries
            // the affinity field with each entry. No affinity override
            // on the cache itself.
            CacheConfiguration<AffinityKey<Integer>, Invoice> invoiceCfg =
                new CacheConfiguration<AffinityKey<Integer>, Invoice>(INVOICES)
                    .setCacheMode(CacheMode.PARTITIONED)
                    .setBackups(1)
                    .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));

            IgniteCache<Integer, Customer> customers = ignite.getOrCreateCache(customerCfg);
            IgniteCache<AffinityKey<Integer>, Invoice> invoices = ignite.getOrCreateCache(invoiceCfg);

            customers.put(1, new Customer("Acme"));
            customers.put(2, new Customer("Globex"));
            customers.put(3, new Customer("Initech"));

            for (int customerId = 1; customerId <= 3; customerId++) {
                for (int seq = 1; seq <= 3; seq++) {
                    int invoiceId = customerId * 100 + seq;
                    // Two-arg AffinityKey: (cache key, affinity key). The
                    // single-arg form silently uses the invoice ID for
                    // both and scatters the invoice off its customer.
                    invoices.put(new AffinityKey<>(invoiceId, customerId),
                        new Invoice("Invoice " + invoiceId, new BigDecimal(100 + seq)));
                }
            }

            Affinity<Integer> custAff = ignite.affinity(CUSTOMERS);
            Affinity<AffinityKey<Integer>> invAff = ignite.affinity(INVOICES);

            System.out.println();
            System.out.println("=== Mechanism 2: AffinityKey<K> wrapper ===");
            System.out.println();
            System.out.printf("%-10s %-12s %-40s%n", "Customer", "Node", "Invoice nodes (per invoice)");
            System.out.println("-----------------------------------------------------------------");

            int colocated = 0;
            int total = 0;
            for (int customerId = 1; customerId <= 3; customerId++) {
                String custNode = labels.of(custAff.mapKeyToNode(customerId));
                StringBuilder invNodes = new StringBuilder();
                for (int seq = 1; seq <= 3; seq++) {
                    AffinityKey<Integer> key = new AffinityKey<>(customerId * 100 + seq, customerId);
                    String invNode = labels.of(invAff.mapKeyToNode(key));
                    if (invNodes.length() > 0) invNodes.append(", ");
                    invNodes.append(invNode);
                    total++;
                    if (invNode.equals(custNode)) colocated++;
                }
                System.out.printf("%-10d %-12s %-40s%n", customerId, custNode, invNodes.toString());
            }
            System.out.println();
            System.out.printf("Colocated %d of %d invoices with their customer.%n", colocated, total);

            ignite.destroyCache(CUSTOMERS);
            ignite.destroyCache(INVOICES);
        }
    }

    private static IgniteConfiguration clientConfig() {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList("127.0.0.1:47500..47503")));
        return new IgniteConfiguration()
            .setDiscoverySpi(disco)
            .setClientMode(true)
            .setPeerClassLoadingEnabled(true);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f colocation-keys/pom.xml compile
mvn -f colocation-keys/pom.xml exec:exec -Dexec.mainClass=com.example.colocation.WrapperColocation
```

Expected output:

```text
=== Mechanism 2: AffinityKey<K> wrapper ===

Customer   Node         Invoice nodes (per invoice)
-----------------------------------------------------------------
1          node1        node1, node1, node1
2          node2        node2, node2, node2
3          node2        node2, node2, node2

Colocated 9 of 9 invoices with their customer.
```

Same invariant, same 9/9. The cache key here is a plain `Integer`. Colocation lives in the `new AffinityKey<>(invoiceId, customerId)` call. If a caller writes `new AffinityKey<>(invoiceId)` (single-argument constructor, no explicit affinity key), the wrapper falls back to using the invoice ID as the affinity key, and the invoice scatters off the customer.

{% hint style="info" %}

The wrapper mechanism fails at runtime, not at compile time. Nothing in the type system tells you the two-argument constructor is load-bearing. Tests and code review are the only gates. Teams that pick this mechanism usually wrap the `new AffinityKey<>(...)` call in a small factory method to keep the colocation contract in one place.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** The program prints `Colocated 9 of 9 invoices with their customer.` The invoice cache has no custom key class and no affinity annotation, yet the colocation holds.
{% endhint %}

## Mechanism 3: CacheKeyConfiguration on the Cache

The third mechanism moves the declaration off the key class entirely and onto the cache configuration. `CacheKeyConfiguration` names the affinity field by type name and field name. The key class stays a plain POJO with no annotations. The cache knows which field drives partitioning because the cache configuration says so.

This is the right mechanism when the same key class ships into caches with different colocation rules, when the key class is generated code that cannot carry annotations, or when operators and schema owners are different people and the colocation decision belongs in infrastructure rather than domain code.

Create `ConfigurationColocation.java`:

{% code title="colocation-keys/src/main/java/com/example/colocation/ConfigurationColocation.java" %}
```java
package com.example.colocation;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.Objects;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheKeyConfiguration;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.affinity.Affinity;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Mechanism 3: declare colocation on the cache configuration.
 *
 * The key class InvoiceCompositeKey is a plain POJO with no affinity
 * annotations. The invoice cache's CacheKeyConfiguration declares
 * "for this key type, use the field named customerId as the affinity
 * key." At put time, the default affinity mapper consults the
 * CacheKeyConfiguration list on the cache, finds a match for the
 * incoming key class, and reads the named field via reflection.
 *
 * The declaration is opaque to the compiler and IDE because the field
 * name is a string. Rename InvoiceCompositeKey.customerId without
 * updating the cache config and the affinity mapper silently falls
 * back to using the whole key, scattering invoices.
 */
public class ConfigurationColocation {

    private static final String CUSTOMERS = "customers-config";
    private static final String INVOICES = "invoices-config";
    private static final int PARTITIONS = 32;

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start(clientConfig())) {
            Labels labels = Labels.forCluster(ignite);

            CacheConfiguration<Integer, Customer> customerCfg =
                new CacheConfiguration<Integer, Customer>(CUSTOMERS)
                    .setCacheMode(CacheMode.PARTITIONED)
                    .setBackups(1)
                    .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));

            // CacheKeyConfiguration binds a type to an affinity field.
            // The type is named by its fully-qualified class name,
            // resolved via Class.getName() so the compiler catches a
            // missing class. The field name is a string the compiler
            // cannot verify. A rename on InvoiceCompositeKey.customerId
            // breaks this mapping silently.
            CacheKeyConfiguration keyCfg =
                new CacheKeyConfiguration(InvoiceCompositeKey.class.getName(), "customerId");

            // setKeyConfiguration accepts a varargs list. One cache can
            // register affinity-field mappings for several key types.
            // This is the main reason teams reach for this mechanism.
            // Several related key classes can share a cache and each
            // bring its own affinity declaration.
            CacheConfiguration<InvoiceCompositeKey, Invoice> invoiceCfg =
                new CacheConfiguration<InvoiceCompositeKey, Invoice>(INVOICES)
                    .setCacheMode(CacheMode.PARTITIONED)
                    .setBackups(1)
                    .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS))
                    .setKeyConfiguration(keyCfg);

            IgniteCache<Integer, Customer> customers = ignite.getOrCreateCache(customerCfg);
            IgniteCache<InvoiceCompositeKey, Invoice> invoices = ignite.getOrCreateCache(invoiceCfg);

            customers.put(1, new Customer("Acme"));
            customers.put(2, new Customer("Globex"));
            customers.put(3, new Customer("Initech"));

            for (int customerId = 1; customerId <= 3; customerId++) {
                for (int seq = 1; seq <= 3; seq++) {
                    int invoiceId = customerId * 100 + seq;
                    // The key is a bare POJO. Nothing about the call
                    // hints at colocation. Only the cache's
                    // CacheKeyConfiguration makes customerId
                    // load-bearing.
                    invoices.put(new InvoiceCompositeKey(invoiceId, customerId),
                        new Invoice("Invoice " + invoiceId, new BigDecimal(100 + seq)));
                }
            }

            Affinity<Integer> custAff = ignite.affinity(CUSTOMERS);
            Affinity<InvoiceCompositeKey> invAff = ignite.affinity(INVOICES);

            System.out.println();
            System.out.println("=== Mechanism 3: CacheKeyConfiguration on the cache ===");
            System.out.println();
            System.out.printf("%-10s %-12s %-40s%n", "Customer", "Node", "Invoice nodes (per invoice)");
            System.out.println("-----------------------------------------------------------------");

            int colocated = 0;
            int total = 0;
            for (int customerId = 1; customerId <= 3; customerId++) {
                String custNode = labels.of(custAff.mapKeyToNode(customerId));
                StringBuilder invNodes = new StringBuilder();
                for (int seq = 1; seq <= 3; seq++) {
                    InvoiceCompositeKey key =
                        new InvoiceCompositeKey(customerId * 100 + seq, customerId);
                    String invNode = labels.of(invAff.mapKeyToNode(key));
                    if (invNodes.length() > 0) invNodes.append(", ");
                    invNodes.append(invNode);
                    total++;
                    if (invNode.equals(custNode)) colocated++;
                }
                System.out.printf("%-10d %-12s %-40s%n", customerId, custNode, invNodes.toString());
            }
            System.out.println();
            System.out.printf("Colocated %d of %d invoices with their customer.%n", colocated, total);

            ignite.destroyCache(CUSTOMERS);
            ignite.destroyCache(INVOICES);
        }
    }

    private static IgniteConfiguration clientConfig() {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList("127.0.0.1:47500..47503")));
        return new IgniteConfiguration()
            .setDiscoverySpi(disco)
            .setClientMode(true)
            .setPeerClassLoadingEnabled(true);
    }

    /**
     * Composite cache key with no affinity annotations. The colocation
     * contract lives on the cache, not on the type. Only the annotation
     * is missing compared with the annotated key class.
     */
    public static class InvoiceCompositeKey implements Serializable {
        private static final long serialVersionUID = 1L;

        private Integer invoiceId;
        private Integer customerId;

        public InvoiceCompositeKey() {
        }

        public InvoiceCompositeKey(Integer invoiceId, Integer customerId) {
            this.invoiceId = invoiceId;
            this.customerId = customerId;
        }

        public Integer getInvoiceId() {
            return invoiceId;
        }

        public Integer getCustomerId() {
            return customerId;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof InvoiceCompositeKey)) return false;
            InvoiceCompositeKey that = (InvoiceCompositeKey) o;
            return Objects.equals(invoiceId, that.invoiceId)
                && Objects.equals(customerId, that.customerId);
        }

        @Override
        public int hashCode() {
            return Objects.hash(invoiceId, customerId);
        }
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f colocation-keys/pom.xml compile
mvn -f colocation-keys/pom.xml exec:exec -Dexec.mainClass=com.example.colocation.ConfigurationColocation
```

Expected output:

```text
=== Mechanism 3: CacheKeyConfiguration on the cache ===

Customer   Node         Invoice nodes (per invoice)
-----------------------------------------------------------------
1          node1        node1, node1, node1
2          node2        node2, node2, node2
3          node2        node2, node2, node2

Colocated 9 of 9 invoices with their customer.
```

Same 9/9. The `InvoiceCompositeKey` class is indistinguishable from any other two-field POJO. The colocation declaration lives entirely in the `CacheKeyConfiguration` argument to `setKeyConfiguration`. Rename `customerId` to `customerIdRef` in the key class without updating the string in the cache config, and the affinity field is no longer resolvable. The cache still creates and the puts still succeed, but the invariant silently breaks.

{% hint style="info" %}

Open `ConfigurationColocation.java` and run **Find Usages** on the string literal `"customerId"` inside the `CacheKeyConfiguration` constructor. The IDE finds nothing. The string is opaque to refactoring tools. This is the tradeoff for moving the declaration off the key class. The schema audit has to include the cache config, and a rename on `InvoiceCompositeKey.customerId` does not propagate.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** The program prints `Colocated 9 of 9 invoices with their customer.` The key class has no affinity annotation, yet the cache config produces the same colocation as the other two mechanisms.
{% endhint %}

## Compare the Three Mechanisms

You have three programs that produce the same runtime outcome. The differences are about code structure and where the declaration breaks when something goes wrong.

| Dimension | `@AffinityKeyMapped` | `AffinityKey<K>` wrapper | `CacheKeyConfiguration` |
|---|---|---|---|
| Where the declaration lives | On the key class | At each call site | On the cache configuration |
| Carrier type | Custom key class | Library wrapper on plain key | Plain key class |
| Discoverable by IDE Find Usages | Yes (on the annotation or field) | Yes (on the `AffinityKey` constructor) | No (the field name is a string) |
| Fails when... | The annotation is removed or moved to a different field (runtime, silent) | A caller omits the two-arg constructor (runtime, silent) | The field name and cache config drift apart (runtime, silent) |
| Same key used by multiple caches with different affinity | Not possible. One annotation per class. | Possible. Each caller picks its own affinity key. | Possible. Each cache has its own `CacheKeyConfiguration`. |
| Default when nothing applies | The whole key drives affinity | The whole key drives affinity | The whole key drives affinity |

The three mechanisms are not a ranking. They are three places to put the colocation decision. Pick by the failure mode your team can catch:

- If the key class owns the schema and survives unchanged, `@AffinityKeyMapped` puts the declaration somewhere `git blame` and IDE refactoring can reason about. This is the common case.
- If you cannot modify the key class, or colocation is decided by runtime context, `AffinityKey<K>` lets the call site carry the decision. Wrap the construction in a factory method and tests become the gate.
- If the same key type lives in multiple caches with different affinity needs, or the key class is generated, or cache configuration belongs to a different team than the domain model, `CacheKeyConfiguration` puts the decision in infrastructure. Document the contract because tools will not find it.

{% hint style="info" %}

You may see a fourth mechanism in older GridGain 8 codebases: a custom `AffinityKeyMapper` implementation passed to `CacheConfiguration.setAffinityMapper(...)`. As of 2.16.0 this interface is deprecated. The Javadoc recommends replacing it with one of the three mechanisms above: `@AffinityKeyMapped`, the `AffinityKey<K>` wrapper, or `CacheKeyConfiguration.setAffinityKeyFieldName(String)`. New schemas should pick from those three.

{% endhint %}

## Summary

Three mechanisms declare cache-to-cache colocation. All three produce identical runtime placement. The mechanism you pick decides where the colocation contract lives, and therefore how it fails when the contract is wrong.

**The annotation puts the contract on the key class.** Discoverable by IDE and tied to the schema. The contract breaks silently when the annotation is removed or moved to a different field; the project still compiles and tests still pass. The next tutorial, Verify Colocation Is Working, builds the verification toolkit that catches this. The annotation is the default choice when you own the key.

**The wrapper puts the contract at the call site.** No custom key class, per-put flexibility, silent at runtime if a caller forgets the two-argument constructor. The choice when the key is someone else's or colocation depends on runtime state.

**The configuration puts the contract on the cache.** No annotations on the key, multiple affinity policies for the same key type, opaque to IDE refactoring. The choice when schema and infrastructure are owned by different teams or the same key serves multiple caches.

`mapKeyToNode` is the same confirmation tool either way. Nine out of nine in every program, regardless of which mechanism put it there.

### What's Next

- Verify Colocation Is Working (coming soon) teaches the verification pattern that proves colocation is holding across a running cluster, including the system views and the diagnostic queries for catching silent breakage.
- Affinity-Aware Compute at Scale (coming soon) uses colocation for compute gravity: running the job where the data already lives, without pulling bytes to the client.
- When to Break Colocation (coming soon) teaches the inverse decision: reference tables that belong in `REPLICATED` caches and fact-dimension patterns.

### Related

- [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md) introduced the `Affinity` API and the 3-node cluster used here.
- [From Key-Value to SQL: The JOIN Problem](../beyond-key-value/from-keyvalue-to-sql.md) uses `@AffinityKeyMapped` as a JOIN-correctness fix, the same mechanism from a different direction.
