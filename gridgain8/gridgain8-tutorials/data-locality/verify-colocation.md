---
description: >-
  Colocation fails silently.
---

# Verify Colocation Is Working

## Introduction

Colocation has no compile-time guard and no runtime exception. The previous tutorial gave you three mechanisms that declare a parent-child colocation contract. All three mechanisms compile and produce working code, and none of them throws when the contract is wrong.

A misconfigured `@AffinityKeyMapped`, a `CacheKeyConfiguration` field name that drifted from the class, or a caller that forgot the two-argument `AffinityKey` constructor all look the same from outside the code. The put succeeds. The get returns the value. A JOIN issued weeks later returns wrong rows. A compute job runs at a fraction of the throughput it should. The cache had no way to know what you meant.

The verification toolkit closes the gap. Three techniques, each reading a different surface of the running cluster, each reporting a failure in a different idiom. You run all three before shipping colocation-dependent code and again as part of a pre-deploy check.

You build one Maven project with two reader-facing classes. `VerifyColocation` runs three verification acts against the annotation pair from the previous tutorial, and every invariant holds. `BrokenColocation` moves the `@AffinityKeyMapped` annotation to the wrong field and reruns the same three acts. The contract is still declared and the compile still succeeds, but the verification toolkit catches the bug three different ways.

## Prerequisites

- **Completion of [Design Keys for Colocation](design-keys-for-colocation.md).** You have read that tutorial and `Affinity.mapKeyToNode` is familiar. This tutorial builds its own `customers-verify` and `invoices-verify` caches, so the caches from the prior tutorial are not needed (each of the three mechanism programs destroyed its own caches at the end).
- **A running 3-node cluster** using `docker-compose-3nodes.yml` from [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md).
- **Java 11 or later** for the client runtime. The Maven project compiles to Java 8 bytecode to match the server JVM.
- **Maven 3.6** or later
- **Docker Compose 2.23** or later

This tutorial builds a fresh Maven project called `verify-colocation/` alongside `colocation-keys/` and `cache-distribution/`. The cluster setup is unchanged.

<details>
<summary>Returning to these tutorials? Verify the 3-node cluster is running.</summary>

```bash
docker ps --filter name=gridgain8-node --format "table {{.Names}}\t{{.Status}}"
```

You want three server containers in the `Up` state. If the cluster is stopped, start it with `docker compose -f cache-cluster/docker-compose-3nodes.yml up -d` and wait for the topology snapshot to report `servers=3`.

</details>

## What You Will Learn

- Build a verification project that proves colocation three ways against the same running data
- Assert colocation with `Affinity.mapKeyToPrimaryAndBackups` and read the per-invoice OK/MISMATCH shape that fails a unit test
- Query `SYS.CACHE_GROUPS` and `SYS.PARTITION_STATES` to describe the partition topology the cluster is running
- Broadcast a `ScanQuery.setLocal(true)` scan across every server and count orphan rows per node
- Recognize the three distinct failure signals: mismatch rows, silent-healthy structure, and named orphans

## Create the Verify-Colocation Project

Create a Maven project named `verify-colocation/` with the layout:

```text
verify-colocation/
├── pom.xml
└── src/main/java/com/example/verify/
    ├── Customer.java
    ├── Invoice.java
    ├── InvoiceKey.java
    ├── BrokenInvoiceKey.java
    ├── Labels.java
    ├── VerifyColocation.java
    └── BrokenColocation.java
```

The `pom.xml` targets Java 8 bytecode and suppresses the engine's startup logs so each act's output stands out:

{% code title="verify-colocation/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>verify-colocation</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>8</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.verify.VerifyColocation</exec.mainClass>
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

Create the two domain POJOs. Same shape as the previous tutorial. Both classes are used by `VerifyColocation` and `BrokenColocation`.

{% code title="verify-colocation/src/main/java/com/example/verify/Customer.java" %}
```java
package com.example.verify;

import java.io.Serializable;

/**
 * Value object for the Customer cache. Identical to the shape used in
 * the previous tutorial. The verification toolkit reads this class
 * back when Act 3 iterates each node's locally-owned customers.
 */
public class Customer implements Serializable {
    private static final long serialVersionUID = 1L;

    private String name;

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

{% code title="verify-colocation/src/main/java/com/example/verify/Invoice.java" %}
```java
package com.example.verify;

import java.io.Serializable;
import java.math.BigDecimal;

/**
 * Value object for the Invoice cache.
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

Create two composite key classes. `InvoiceKey` carries the annotation on `customerId`: the contract you declared in the previous tutorial. `BrokenInvoiceKey` carries the annotation on `invoiceId`: a deliberately miswired key the cache accepts without complaint. Both compile. The break-and-diagnose step uses `BrokenInvoiceKey` to show how each verification technique reports a silent contract failure.

{% code title="verify-colocation/src/main/java/com/example/verify/InvoiceKey.java" %}
```java
package com.example.verify;

import java.io.Serializable;
import java.util.Objects;

import org.apache.ignite.cache.affinity.AffinityKeyMapped;

/**
 * Composite invoice key with the colocation contract declared on
 * customerId. This is the known-good baseline: every verification
 * act run against it must report an intact invariant.
 */
public class InvoiceKey implements Serializable {
    private static final long serialVersionUID = 1L;

    private Integer invoiceId;

    // customerId is the affinity key. A second @AffinityKeyMapped on
    // any other field would be a configuration error the engine
    // rejects at cache-create time.
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
```
{% endcode %}

{% code title="verify-colocation/src/main/java/com/example/verify/BrokenInvoiceKey.java" %}
```java
package com.example.verify;

import java.io.Serializable;
import java.util.Objects;

import org.apache.ignite.cache.affinity.AffinityKeyMapped;

/**
 * A deliberately-miswired composite key. The annotation exists, marks
 * a field, and compiles clean. But the affinity field is invoiceId
 * instead of customerId, so invoices hash independently of their
 * customer and scatter across partitions.
 *
 * The engine accepts this key class. Puts succeed, gets succeed, the
 * mapper finds an @AffinityKeyMapped field and uses its value. The
 * mechanics are fine even though the contract is wrong. This is the
 * silent failure mode the verification toolkit exists to catch.
 */
public class BrokenInvoiceKey implements Serializable {
    private static final long serialVersionUID = 1L;

    // Wrong choice of affinity field. invoiceId is unique per invoice
    // and has no relationship to the customer, so the resulting
    // partition assignments are effectively random with respect to
    // the customer cache.
    @AffinityKeyMapped
    private Integer invoiceId;

    private Integer customerId;

    public BrokenInvoiceKey() {
    }

    public BrokenInvoiceKey(Integer invoiceId, Integer customerId) {
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
        if (!(o instanceof BrokenInvoiceKey)) return false;
        BrokenInvoiceKey that = (BrokenInvoiceKey) o;
        return Objects.equals(invoiceId, that.invoiceId)
            && Objects.equals(customerId, that.customerId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(invoiceId, customerId);
    }
}
```
{% endcode %}

The `Labels` utility produces stable `node1/node2/node3` synonyms so the tutorial's output never shows Docker-generated UUIDs. Same shape as the previous tutorial, with one added accessor for looking up a label from a raw `UUID` returned by a system view.

{% code title="verify-colocation/src/main/java/com/example/verify/Labels.java" %}
```java
package com.example.verify;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import org.apache.ignite.Ignite;
import org.apache.ignite.cluster.ClusterNode;

/**
 * Client-side synonym assignment for cluster nodes. The cluster does
 * not know these labels exist. They are for output formatting only.
 *
 * consistentId drives the label order so runs against the same
 * docker-compose cluster produce identical node1/node2/node3
 * assignments across restarts. ClusterNode.id() regenerates on every
 * container restart, but consistentId derives from host and discovery
 * port, which stay fixed.
 */
final class Labels {
    private final Map<UUID, String> byId = new HashMap<>();

    private Labels() {
    }

    static Labels forCluster(Ignite ignite) {
        Labels labels = new Labels();
        List<ClusterNode> servers = new ArrayList<>(ignite.cluster().forServers().nodes());
        servers.sort(Comparator.comparing(n -> n.consistentId().toString()));
        for (int i = 0; i < servers.size(); i++) {
            labels.byId.put(servers.get(i).id(), "node" + (i + 1));
        }
        return labels;
    }

    String of(ClusterNode node) {
        return node == null ? "(none)" : byId.getOrDefault(node.id(), "(unknown)");
    }

    // System views return node IDs as raw UUIDs in SQL result rows.
    // ofId bridges the raw UUID back to the synonym without needing
    // a ClusterNode handle.
    String ofId(UUID id) {
        return id == null ? "(none)" : byId.getOrDefault(id, "(unknown)");
    }
}
```
{% endcode %}

Compile the project. The main class arrives in the next step:

```bash
mvn -f verify-colocation/pom.xml compile
```

`mvn compile` only builds the Java files already present in `src/main/java/`, so this command finishes with `BUILD SUCCESS`. The `exec.mainClass` property in the pom is consumed by the `exec:exec` goal at run time. Until `VerifyColocation.java` exists, `mvn exec:exec` fails with `ClassNotFoundException`. The compile is independent of that property.

{% hint style="success" %}
**Checkpoint:** The four model classes are in place (`Customer`, `Invoice`, `InvoiceKey`, `BrokenInvoiceKey`) along with `Labels` and the `pom.xml`. The compile finishes with `BUILD SUCCESS`. A run attempt before the next step would fail at the main class.
{% endhint %}

## Act 1: Runtime API Verification

`Affinity.mapKeyToPrimaryAndBackups(key)` returns a collection of `ClusterNode`: primary first, backups next. For every invoice, the primary must match the primary of its customer. That is the colocation invariant as a one-line assertion, and it is the fastest of the three techniques.

The call is a pure function of the key plus the current topology. No network round-trip. No cache read. Appropriate for a unit test run in a CI pipeline against any live cluster.

Create `VerifyColocation.java` with the scaffolding, the first act, and `main`. The system-views and local-scan acts come in the next two steps.

{% code title="verify-colocation/src/main/java/com/example/verify/VerifyColocation.java" %}
```java
package com.example.verify;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.UUID;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.binary.BinaryObject;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.affinity.Affinity;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.cache.query.QueryCursor;
import org.apache.ignite.cache.query.ScanQuery;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.cluster.ClusterNode;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.lang.IgniteCallable;
import org.apache.ignite.resources.IgniteInstanceResource;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Three verification techniques that prove a colocation mechanism is
 * working. The schema is the annotation pair from the previous
 * tutorial: InvoiceKey with @AffinityKeyMapped on customerId. The
 * three acts run in sequence against the same data:
 *
 *   Act 1 - Runtime API. Compare mapKeyToPrimaryAndBackups per key,
 *           assert primary(customer) == primary(invoice).
 *   Act 2 - System views. Query SYS.CACHE_GROUPS and
 *           SYS.PARTITION_STATES to describe the cluster shape
 *           both caches are running under.
 *   Act 3 - Local scan. Broadcast a callable that reads each node's
 *           primary-owned customers and invoices via
 *           ScanQuery.setLocal and reports invoices whose customer
 *           lives elsewhere.
 *
 * Every invariant holds against InvoiceKey. BrokenColocation is the
 * sibling class where the annotation sits on the wrong field and
 * every technique surfaces the failure in its own idiom.
 */
public class VerifyColocation {

    // Cache names are unique to this tutorial so runs of the previous
    // tutorial's programs and this one coexist on the same cluster.
    private static final String CUSTOMERS = "customers-verify";
    private static final String INVOICES = "invoices-verify";
    private static final int PARTITIONS = 32;
    private static final int CUSTOMER_COUNT = 3;
    private static final int INVOICES_PER_CUSTOMER = 3;

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start(clientConfig())) {
            Labels labels = Labels.forCluster(ignite);

            IgniteCache<Integer, Customer> customers = ignite.getOrCreateCache(customerCfg());
            IgniteCache<InvoiceKey, Invoice> invoices = ignite.getOrCreateCache(invoiceCfg());

            seed(customers, invoices);

            Affinity<Integer> custAff = ignite.affinity(CUSTOMERS);
            Affinity<InvoiceKey> invAff = ignite.affinity(INVOICES);

            actOneRuntimeApi(labels, custAff, invAff);
            // Acts 2 and 3 are added in the next two steps.

            ignite.destroyCache(CUSTOMERS);
            ignite.destroyCache(INVOICES);
        }
    }

    /**
     * Act 1: runtime-API verification.
     *
     * For every customer and every invoice, the primary node returned
     * by mapKeyToPrimaryAndBackups must match. This runs entirely
     * from cached topology on the client. No network round-trip. No
     * cache reads. Suitable for a unit-test-style assertion.
     */
    private static void actOneRuntimeApi(Labels labels,
                                         Affinity<Integer> custAff,
                                         Affinity<InvoiceKey> invAff) {
        System.out.println();
        System.out.println("=== Act 1: Runtime API (mapKeyToPrimaryAndBackups) ===");
        System.out.println();
        System.out.printf("%-10s %-18s %-18s %s%n", "Invoice", "Customer primary", "Invoice primary", "Match");
        System.out.println("----------------------------------------------------------------");

        int matches = 0;
        int total = 0;
        for (int customerId = 1; customerId <= CUSTOMER_COUNT; customerId++) {
            Collection<ClusterNode> custOwners = custAff.mapKeyToPrimaryAndBackups(customerId);
            ClusterNode custPrimary = first(custOwners);
            for (int seq = 1; seq <= INVOICES_PER_CUSTOMER; seq++) {
                int invoiceId = customerId * 100 + seq;
                InvoiceKey key = new InvoiceKey(invoiceId, customerId);
                Collection<ClusterNode> invOwners = invAff.mapKeyToPrimaryAndBackups(key);
                ClusterNode invPrimary = first(invOwners);
                boolean match = sameNode(custPrimary, invPrimary);
                System.out.printf("%-10d %-18s %-18s %s%n",
                    invoiceId, labels.of(custPrimary), labels.of(invPrimary), match ? "OK" : "MISMATCH");
                total++;
                if (match) matches++;
            }
        }
        System.out.println();
        System.out.printf("Runtime API: %d of %d invoices share a primary with their customer.%n",
            matches, total);
    }

    private static void seed(IgniteCache<Integer, Customer> customers,
                             IgniteCache<InvoiceKey, Invoice> invoices) {
        customers.put(1, new Customer("Acme"));
        customers.put(2, new Customer("Globex"));
        customers.put(3, new Customer("Initech"));
        for (int c = 1; c <= CUSTOMER_COUNT; c++) {
            for (int s = 1; s <= INVOICES_PER_CUSTOMER; s++) {
                int id = c * 100 + s;
                invoices.put(new InvoiceKey(id, c),
                    new Invoice("Invoice " + id, new BigDecimal(100 + s)));
            }
        }
    }

    private static CacheConfiguration<Integer, Customer> customerCfg() {
        return new CacheConfiguration<Integer, Customer>(CUSTOMERS)
            .setCacheMode(CacheMode.PARTITIONED)
            .setBackups(1)
            .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS))
            // setSqlSchema attaches the cache to the PUBLIC SQL schema.
            // SYS.* queries reach any cache that has an SQL schema, and
            // the customers cache is the one the program uses to issue
            // them.
            .setSqlSchema("PUBLIC");
    }

    private static CacheConfiguration<InvoiceKey, Invoice> invoiceCfg() {
        return new CacheConfiguration<InvoiceKey, Invoice>(INVOICES)
            .setCacheMode(CacheMode.PARTITIONED)
            .setBackups(1)
            .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS))
            .setSqlSchema("PUBLIC");
    }

    /**
     * Thick-client configuration with peer class loading enabled so
     * InvoiceKey, BrokenInvoiceKey, and the broadcast callable ship
     * to the servers without a shared classpath. The discovery port
     * range spans 47500-47503 so the same code works against the
     * three-node and four-node compose files.
     */
    private static IgniteConfiguration clientConfig() {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Arrays.asList("127.0.0.1:47500..47503")));
        return new IgniteConfiguration()
            .setDiscoverySpi(disco)
            .setClientMode(true)
            .setPeerClassLoadingEnabled(true);
    }

    private static ClusterNode first(Collection<ClusterNode> nodes) {
        return nodes.isEmpty() ? null : nodes.iterator().next();
    }

    private static boolean sameNode(ClusterNode a, ClusterNode b) {
        return a != null && b != null && a.id().equals(b.id());
    }
}
```
{% endcode %}

Compile and run:

```bash
mvn -f verify-colocation/pom.xml compile
mvn -f verify-colocation/pom.xml exec:exec
```

Expected output (your specific node assignments vary because Docker regenerates node IDs on every restart):

```text
=== Act 1: Runtime API (mapKeyToPrimaryAndBackups) ===

Invoice    Customer primary   Invoice primary    Match
----------------------------------------------------------------
101        node2              node2              OK
102        node2              node2              OK
103        node2              node2              OK
201        node2              node2              OK
202        node2              node2              OK
203        node2              node2              OK
301        node1              node1              OK
302        node1              node1              OK
303        node1              node1              OK

Runtime API: 9 of 9 invoices share a primary with their customer.
```

The assertion loop is the kernel of a test case. `mapKeyToPrimaryAndBackups` reads nothing from the cluster. It applies the rendezvous function to the key and walks the client's cached topology view. A thousand-row sweep finishes in milliseconds, which matters because this is the check you want running on every build.

{% hint style="info" %}

During a scale event or a node restart, a partition can temporarily report multiple owners as the engine moves primary responsibility. `mapKeyToPrimaryAndBackups` reflects the client's current topology view, not the cluster's in-flight state. A production verification test should tolerate a brief window of disagreement by retrying with a small delay, or should run against a stable baseline.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** The program prints `Runtime API: 9 of 9 invoices share a primary with their customer.` Every invoice in the table shows `OK` in the match column.
{% endhint %}

## Act 2: System Views Verification

The runtime API told you whether the contract is wired correctly. The system views tell you the shape the cluster is running. Operations teams watch them on a live system, and a schema audit reads them when the source code is not available.

Two views carry what you need. `SYS.CACHE_GROUPS` describes each cache's group: partition count, backups, cache mode, the group ID used to join against other SYS views. `SYS.PARTITION_STATES` is one row per partition per owner, with `IS_PRIMARY` and `STATE` columns. Both are available over SQL from any cache in the cluster, including the thick-client API's `cache.query(new SqlFieldsQuery(...))` path.

Add the `actTwoSystemViews` method to `VerifyColocation.java` below `actOneRuntimeApi`, and wire it into `main` after the `actOneRuntimeApi` call:

```java
// Add below actOneRuntimeApi in VerifyColocation.java
/**
 * Act 2: system-view verification.
 *
 * SYS.CACHE_GROUPS names partition count, backups, and cache mode
 * for each cache. SYS.PARTITION_STATES names the live
 * partition-to-node mapping with an IS_PRIMARY flag per row. These
 * views describe the cluster as operations sees it. They cannot
 * read the reader's intent, so they prove structural health (both
 * caches present, matching shape) but not colocation correctness.
 */
private static void actTwoSystemViews(Ignite ignite, Labels labels) {
    System.out.println();
    System.out.println("=== Act 2: System Views (SYS.CACHE_GROUPS, SYS.PARTITION_STATES) ===");
    System.out.println();

    // Any SQL-enabled cache can run cross-cache SQL including the SYS
    // schema. The customers cache is the program's SQL entry point.
    IgniteCache<?, ?> anyCache = ignite.cache(CUSTOMERS);

    System.out.println("--- SYS.CACHE_GROUPS rows for the two caches ---");
    System.out.printf("%-22s %-11s %-8s %-17s %s%n",
        "CACHE_GROUP_NAME", "PARTITIONS", "BACKUPS", "CACHE_MODE", "CACHE_GROUP_ID");
    System.out.println("--------------------------------------------------------------------");

    SqlFieldsQuery groupsQry = new SqlFieldsQuery(
        "SELECT CACHE_GROUP_NAME, PARTITIONS_COUNT, BACKUPS, CACHE_MODE, CACHE_GROUP_ID " +
        "FROM SYS.CACHE_GROUPS " +
        "WHERE CACHE_GROUP_NAME IN (?, ?) " +
        "ORDER BY CACHE_GROUP_NAME"
    ).setArgs(CUSTOMERS, INVOICES);

    int customersGroupId = -1;
    int invoicesGroupId = -1;
    try (QueryCursor<List<?>> cur = anyCache.query(groupsQry)) {
        for (List<?> row : cur) {
            String name = (String) row.get(0);
            int parts = (Integer) row.get(1);
            int backups = (Integer) row.get(2);
            String mode = (String) row.get(3);
            int groupId = (Integer) row.get(4);
            System.out.printf("%-22s %-11d %-8d %-17s %d%n", name, parts, backups, mode, groupId);
            if (CUSTOMERS.equals(name)) customersGroupId = groupId;
            if (INVOICES.equals(name)) invoicesGroupId = groupId;
        }
    }

    System.out.println();
    System.out.println("--- SYS.PARTITION_STATES: primary partitions per node per cache ---");
    System.out.printf("%-22s %-12s %s%n", "CACHE", "NODE", "PRIMARY PARTITION COUNT");
    System.out.println("--------------------------------------------------------------");

    // Group-by on the partition-states view reduces 96 rows (32
    // partitions * 3 nodes) to one row per cache per node.
    SqlFieldsQuery partsQry = new SqlFieldsQuery(
        "SELECT CACHE_GROUP_ID, NODE_ID, COUNT(*) " +
        "FROM SYS.PARTITION_STATES " +
        "WHERE CACHE_GROUP_ID IN (?, ?) AND IS_PRIMARY = TRUE " +
        "GROUP BY CACHE_GROUP_ID, NODE_ID " +
        "ORDER BY CACHE_GROUP_ID, NODE_ID"
    ).setArgs(customersGroupId, invoicesGroupId);

    try (QueryCursor<List<?>> cur = anyCache.query(partsQry)) {
        for (List<?> row : cur) {
            int groupId = (Integer) row.get(0);
            UUID nodeId = (UUID) row.get(1);
            long count = (Long) row.get(2);
            String cacheName = (groupId == customersGroupId) ? CUSTOMERS : INVOICES;
            System.out.printf("%-22s %-12s %d%n", cacheName, labels.ofId(nodeId), count);
        }
    }

    System.out.println();
    System.out.println("System views show cache shape (partitions, backups) and live");
    System.out.println("partition distribution. They cannot tell you customerId was");
    System.out.println("supposed to drive placement. That is Act 1's job.");
}
```

Update `main` to call the new method:

```java
actOneRuntimeApi(labels, custAff, invAff);
actTwoSystemViews(ignite, labels);
// Act 3 still pending.
```

Compile and rerun:

```bash
mvn -f verify-colocation/pom.xml compile
mvn -f verify-colocation/pom.xml exec:exec
```

Act 1's output is unchanged. Act 2 appears after it:

```text
=== Act 2: System Views (SYS.CACHE_GROUPS, SYS.PARTITION_STATES) ===

--- SYS.CACHE_GROUPS rows for the two caches ---
CACHE_GROUP_NAME       PARTITIONS  BACKUPS  CACHE_MODE        CACHE_GROUP_ID
--------------------------------------------------------------------
customers-verify       32          1        PARTITIONED       -1085612815
invoices-verify        32          1        PARTITIONED       -39132864

--- SYS.PARTITION_STATES: primary partitions per node per cache ---
CACHE                  NODE         PRIMARY PARTITION COUNT
--------------------------------------------------------------
customers-verify       node1        13
customers-verify       node2        10
customers-verify       node3        9
invoices-verify        node1        13
invoices-verify        node2        10
invoices-verify        node3        9

System views show cache shape (partitions, backups) and live
partition distribution. They cannot tell you customerId was
supposed to drive placement. That is Act 1's job.
```

Look at the shape, not the specific counts. Both caches have the same partition count, the same backup count, the same mode, and identical per-node primary counts. That is structural health. It answers "are both caches alive and distributed across every server?" but not "does this invoice live with its customer?"

The system views describe the cluster. The cluster does not know the reader's intent. A miswired colocation contract can produce a perfectly uniform partition distribution. The break-and-diagnose step demonstrates that.

{% hint style="info" %}

You can run the same queries without writing Java. Open a SQL shell against any node (using the `gridgain8-node1` container and the `sqlline.sh` script under `/opt/gridgain/`). `SELECT CACHE_GROUP_NAME, PARTITIONS_COUNT, BACKUPS FROM SYS.CACHE_GROUPS;` returns the same data. The CLI query is a one-shot audit tool. The Java version belongs in the test suite, where it fails a build on regression.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** Both `customers-verify` and `invoices-verify` appear with 32 partitions, `backups=1`, `PARTITIONED` mode, and per-node primary counts that sum to 32 across three nodes.
{% endhint %}

## Act 3: Local Scan Verification

The third technique is what production does. A colocated JOIN or a colocated compute job runs on each server, reads that server's primary-owned data, and joins against other caches whose keys hash to the same node. If an invoice's customer lives on a different node, the join misses the row or returns a stale one.

You model that pattern with a scan. `ScanQuery.setLocal(true)` restricts a scan to the entries primary-owned by the node running the query. Only the thick client supports this flag, because a thin client cannot pin a query to a specific server. You broadcast a callable to every server, each callable scans its own customers and invoices, and each returns orphan invoices whose customer is not local.

The broadcast is a diagnostic-tool preview of compute gravity from the next tutorial in this path. Every server independently verifies that the data it owns is consistent with the contract.

Add `actThreeLocalScan`, the `LocalScanTask` callable, and the `NodeReport` record below Act 2. Wire `actThreeLocalScan` into `main`:

```java
// Add below actTwoSystemViews in VerifyColocation.java
/**
 * Act 3: cross-cache JOIN-quality verification via local scans.
 *
 * Broadcasts a callable to every server. Each server scans its own
 * primary-owned customers and invoices using ScanQuery.setLocal,
 * which is a thick-client-only API that the thin client rejects.
 * For each local invoice, the server checks whether that invoice's
 * customer is also local. An invoice whose customer lives elsewhere
 * is an orphan, and orphan count is the JOIN-correctness defect
 * measure.
 *
 * The same pattern generalizes to compute gravity: a job running
 * on each server, reading only its partition of the data,
 * coordinating nothing cross-node.
 */
private static void actThreeLocalScan(Ignite ignite, Labels labels) {
    System.out.println();
    System.out.println("=== Act 3: Local scan (ScanQuery.setLocal on each server) ===");
    System.out.println();
    System.out.printf("%-10s %-18s %-18s %s%n",
        "Node", "Local customers", "Local invoices", "Orphan invoices");
    System.out.println("----------------------------------------------------------------");

    Collection<NodeReport> reports = ignite.compute().broadcast(new LocalScanTask());

    List<NodeReport> sorted = new ArrayList<>(reports);
    sorted.sort((a, b) -> labels.ofId(a.nodeId).compareTo(labels.ofId(b.nodeId)));

    int totalOrphans = 0;
    int totalLocalInvoices = 0;
    for (NodeReport r : sorted) {
        System.out.printf("%-10s %-18d %-18d %s%n",
            labels.ofId(r.nodeId), r.localCustomers, r.localInvoices,
            r.orphanInvoiceIds.isEmpty() ? "(none)" : r.orphanInvoiceIds.toString());
        totalOrphans += r.orphanInvoiceIds.size();
        totalLocalInvoices += r.localInvoices;
    }
    System.out.println();
    System.out.printf("Local scan: %d orphan invoices across %d local invoices.%n",
        totalOrphans, totalLocalInvoices);
}

/**
 * Runs on each server during the broadcast. @IgniteInstanceResource
 * injects the server-local GridGain handle so the callable can reach
 * the caches without opening a client inside the server.
 */
private static final class LocalScanTask implements IgniteCallable<NodeReport> {
    private static final long serialVersionUID = 1L;

    @IgniteInstanceResource
    private Ignite local;

    @Override
    public NodeReport call() {
        UUID localId = local.cluster().localNode().id();

        // withKeepBinary avoids deserializing values and composite
        // keys on the server. The server's classpath has no
        // Customer, Invoice, or InvoiceKey class. BinaryObject.field
        // reads named fields from the binary representation without
        // needing the Java class. Integer keys deserialize because
        // they are a JDK type.
        IgniteCache<Integer, BinaryObject> customers =
            local.<Integer, Object>cache(CUSTOMERS).withKeepBinary();
        IgniteCache<BinaryObject, BinaryObject> invoices =
            local.<Object, Object>cache(INVOICES).withKeepBinary();

        Set<Integer> localCustomerIds = new HashSet<>();
        try (QueryCursor<Cache.Entry<Integer, BinaryObject>> cur =
                 customers.query(new ScanQuery<Integer, BinaryObject>().setLocal(true))) {
            for (Cache.Entry<Integer, BinaryObject> e : cur) {
                localCustomerIds.add(e.getKey());
            }
        }

        int localInvoices = 0;
        List<Integer> orphans = new ArrayList<>();
        try (QueryCursor<Cache.Entry<BinaryObject, BinaryObject>> cur =
                 invoices.query(new ScanQuery<BinaryObject, BinaryObject>().setLocal(true))) {
            for (Cache.Entry<BinaryObject, BinaryObject> e : cur) {
                localInvoices++;
                Integer custId = e.getKey().field("customerId");
                Integer invoiceId = e.getKey().field("invoiceId");
                // Orphan: invoice primary is on this node, but its
                // customer primary is not. The pair is not colocated.
                if (!localCustomerIds.contains(custId)) {
                    orphans.add(invoiceId);
                }
            }
        }
        Collections.sort(orphans);
        return new NodeReport(localId, localCustomerIds.size(), localInvoices, orphans);
    }
}

/** Per-node result returned by the broadcast. */
private static final class NodeReport implements Serializable {
    private static final long serialVersionUID = 1L;
    final UUID nodeId;
    final int localCustomers;
    final int localInvoices;
    final List<Integer> orphanInvoiceIds;

    NodeReport(UUID nodeId, int localCustomers, int localInvoices, List<Integer> orphanInvoiceIds) {
        this.nodeId = nodeId;
        this.localCustomers = localCustomers;
        this.localInvoices = localInvoices;
        this.orphanInvoiceIds = orphanInvoiceIds;
    }
}
```

Update `main` to invoke the third act:

```java
actOneRuntimeApi(labels, custAff, invAff);
actTwoSystemViews(ignite, labels);
actThreeLocalScan(ignite, labels);
```

Compile and rerun. The full output appears in sequence:

```bash
mvn -f verify-colocation/pom.xml compile
mvn -f verify-colocation/pom.xml exec:exec
```

Act 3's section:

```text
=== Act 3: Local scan (ScanQuery.setLocal on each server) ===

Node       Local customers    Local invoices     Orphan invoices
----------------------------------------------------------------
node1      1                  3                  (none)
node2      2                  6                  (none)
node3      0                  0                  (none)

Local scan: 0 orphan invoices across 9 local invoices.
```

Your per-node counts vary. The invariant to watch is `orphan invoices = 0`. Every invoice primary-owned by a node must have its customer primary-owned by the same node. `(none)` in every row means the contract holds for the data the cluster is serving.

Notice node3: zero customers and zero invoices. Three customers spread across 32 partitions on three nodes does not guarantee every node hosts a customer. Production data volumes eliminate the zero case, but small tutorial datasets surface the math. The invariant still holds across the two nodes that do have data.

{% hint style="info" %}

`ScanQuery.setLocal(true)` is a thick-client-only API. The thin client cannot pin a query to a specific server because it does not participate in the cluster's peer-to-peer transport. It talks to one node over a socket. Attempting the call against a thin client raises `IgniteClientException: Scan query flag setLocal is not supported by thin client`. A verification routine that uses local scans has to run from a thick client or as a compute broadcast target, both of which this code demonstrates.

{% endhint %}

{% hint style="info" %}

Open `VerifyColocation.java` and run **Find Usages** on the `customers-verify` string constant. The IDE finds every place the cache name appears. Then run Find Usages on the `@AffinityKeyMapped` annotation on `InvoiceKey.customerId`. The IDE finds every key class using the mechanism. Neither search finds the silent failure mode where a future refactor moves the annotation to the wrong field. That is the verification toolkit's job.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** The program reports `Local scan: 0 orphan invoices across 9 local invoices.` Every node's orphan column reads `(none)`.
{% endhint %}

## Break the Colocation and Diagnose it

The verification techniques all passed. A clean run proves nothing about whether the techniques can see a failure. You break the contract now and rerun each technique to see what each one says when something is wrong.

`BrokenColocation` is the sibling class. It uses `BrokenInvoiceKey` (annotation on `invoiceId` instead of `customerId`), builds its own caches, and runs the same three acts. Everything else is identical.

{% code title="verify-colocation/src/main/java/com/example/verify/BrokenColocation.java" %}
```java
package com.example.verify;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.UUID;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.binary.BinaryObject;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.affinity.Affinity;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.cache.query.QueryCursor;
import org.apache.ignite.cache.query.ScanQuery;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.cluster.ClusterNode;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.lang.IgniteCallable;
import org.apache.ignite.resources.IgniteInstanceResource;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Runs the same three verification acts against a miswired key.
 * BrokenInvoiceKey has @AffinityKeyMapped on invoiceId instead of
 * customerId. The compile succeeds. The puts succeed. The gets
 * succeed. The invariant is broken.
 *
 * Reading each act's output in sequence shows how the three
 * techniques complement each other.
 */
public class BrokenColocation {

    private static final String CUSTOMERS = "customers-broken";
    private static final String INVOICES = "invoices-broken";
    private static final int PARTITIONS = 32;
    private static final int CUSTOMER_COUNT = 3;
    private static final int INVOICES_PER_CUSTOMER = 3;

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start(clientConfig())) {
            Labels labels = Labels.forCluster(ignite);

            IgniteCache<Integer, Customer> customers = ignite.getOrCreateCache(customerCfg());
            IgniteCache<BrokenInvoiceKey, Invoice> invoices = ignite.getOrCreateCache(invoiceCfg());

            seed(customers, invoices);

            Affinity<Integer> custAff = ignite.affinity(CUSTOMERS);
            Affinity<BrokenInvoiceKey> invAff = ignite.affinity(INVOICES);

            actOneRuntimeApi(labels, custAff, invAff);
            actTwoSystemViews(ignite, labels);
            actThreeLocalScan(ignite, labels);

            ignite.destroyCache(CUSTOMERS);
            ignite.destroyCache(INVOICES);
        }
    }

    private static void actOneRuntimeApi(Labels labels,
                                         Affinity<Integer> custAff,
                                         Affinity<BrokenInvoiceKey> invAff) {
        System.out.println();
        System.out.println("=== Act 1: Runtime API (mapKeyToPrimaryAndBackups) ===");
        System.out.println();
        System.out.printf("%-10s %-18s %-18s %s%n", "Invoice", "Customer primary", "Invoice primary", "Match");
        System.out.println("----------------------------------------------------------------");

        int matches = 0;
        int total = 0;
        for (int customerId = 1; customerId <= CUSTOMER_COUNT; customerId++) {
            Collection<ClusterNode> custOwners = custAff.mapKeyToPrimaryAndBackups(customerId);
            ClusterNode custPrimary = first(custOwners);
            for (int seq = 1; seq <= INVOICES_PER_CUSTOMER; seq++) {
                int invoiceId = customerId * 100 + seq;
                BrokenInvoiceKey key = new BrokenInvoiceKey(invoiceId, customerId);
                Collection<ClusterNode> invOwners = invAff.mapKeyToPrimaryAndBackups(key);
                ClusterNode invPrimary = first(invOwners);
                boolean match = sameNode(custPrimary, invPrimary);
                System.out.printf("%-10d %-18s %-18s %s%n",
                    invoiceId, labels.of(custPrimary), labels.of(invPrimary), match ? "OK" : "MISMATCH");
                total++;
                if (match) matches++;
            }
        }
        System.out.println();
        System.out.printf("Runtime API: %d of %d invoices share a primary with their customer.%n",
            matches, total);
    }

    private static void actTwoSystemViews(Ignite ignite, Labels labels) {
        System.out.println();
        System.out.println("=== Act 2: System Views (SYS.CACHE_GROUPS, SYS.PARTITION_STATES) ===");
        System.out.println();

        IgniteCache<?, ?> anyCache = ignite.cache(CUSTOMERS);

        System.out.println("--- SYS.CACHE_GROUPS rows for the two caches ---");
        System.out.printf("%-22s %-11s %-8s %-17s %s%n",
            "CACHE_GROUP_NAME", "PARTITIONS", "BACKUPS", "CACHE_MODE", "CACHE_GROUP_ID");
        System.out.println("--------------------------------------------------------------------");

        SqlFieldsQuery groupsQry = new SqlFieldsQuery(
            "SELECT CACHE_GROUP_NAME, PARTITIONS_COUNT, BACKUPS, CACHE_MODE, CACHE_GROUP_ID " +
            "FROM SYS.CACHE_GROUPS " +
            "WHERE CACHE_GROUP_NAME IN (?, ?) " +
            "ORDER BY CACHE_GROUP_NAME"
        ).setArgs(CUSTOMERS, INVOICES);

        int customersGroupId = -1;
        int invoicesGroupId = -1;
        int customersParts = -1;
        int invoicesParts = -1;
        try (QueryCursor<List<?>> cur = anyCache.query(groupsQry)) {
            for (List<?> row : cur) {
                String name = (String) row.get(0);
                int parts = (Integer) row.get(1);
                int backups = (Integer) row.get(2);
                String mode = (String) row.get(3);
                int groupId = (Integer) row.get(4);
                System.out.printf("%-22s %-11d %-8d %-17s %d%n", name, parts, backups, mode, groupId);
                if (CUSTOMERS.equals(name)) {
                    customersGroupId = groupId;
                    customersParts = parts;
                }
                if (INVOICES.equals(name)) {
                    invoicesGroupId = groupId;
                    invoicesParts = parts;
                }
            }
        }

        System.out.println();
        System.out.println("--- SYS.PARTITION_STATES: primary partitions per node per cache ---");
        System.out.printf("%-22s %-12s %s%n", "CACHE", "NODE", "PRIMARY PARTITION COUNT");
        System.out.println("--------------------------------------------------------------");

        SqlFieldsQuery partsQry = new SqlFieldsQuery(
            "SELECT CACHE_GROUP_ID, NODE_ID, COUNT(*) " +
            "FROM SYS.PARTITION_STATES " +
            "WHERE CACHE_GROUP_ID IN (?, ?) AND IS_PRIMARY = TRUE " +
            "GROUP BY CACHE_GROUP_ID, NODE_ID " +
            "ORDER BY CACHE_GROUP_ID, NODE_ID"
        ).setArgs(customersGroupId, invoicesGroupId);

        try (QueryCursor<List<?>> cur = anyCache.query(partsQry)) {
            for (List<?> row : cur) {
                int groupId = (Integer) row.get(0);
                UUID nodeId = (UUID) row.get(1);
                long count = (Long) row.get(2);
                String cacheName = (groupId == customersGroupId) ? CUSTOMERS : INVOICES;
                System.out.printf("%-22s %-12s %d%n", cacheName, labels.ofId(nodeId), count);
            }
        }

        System.out.println();
        // Partition counts come from the query, not from a hardcoded
        // literal. A reader who configures a different partition count
        // sees the actual number in this print rather than a stale
        // string from the tutorial's reference run.
        if (customersParts == invoicesParts) {
            System.out.printf("Both caches report %d partitions and healthy distribution.%n",
                customersParts);
        } else {
            System.out.printf("Caches report %d (%s) and %d (%s) partitions; colocation requires matching counts.%n",
                customersParts, CUSTOMERS, invoicesParts, INVOICES);
        }
        System.out.println("The system views cannot tell that invoices are hashing on");
        System.out.println("the wrong field. Structural health and colocation health");
        System.out.println("are two different questions.");
    }

    private static void actThreeLocalScan(Ignite ignite, Labels labels) {
        System.out.println();
        System.out.println("=== Act 3: Local scan (ScanQuery.setLocal on each server) ===");
        System.out.println();
        System.out.printf("%-10s %-18s %-18s %s%n",
            "Node", "Local customers", "Local invoices", "Orphan invoices");
        System.out.println("----------------------------------------------------------------");

        Collection<NodeReport> reports = ignite.compute().broadcast(new LocalScanTask());

        List<NodeReport> sorted = new ArrayList<>(reports);
        sorted.sort((a, b) -> labels.ofId(a.nodeId).compareTo(labels.ofId(b.nodeId)));

        int totalOrphans = 0;
        int totalLocalInvoices = 0;
        for (NodeReport r : sorted) {
            System.out.printf("%-10s %-18d %-18d %s%n",
                labels.ofId(r.nodeId), r.localCustomers, r.localInvoices,
                r.orphanInvoiceIds.isEmpty() ? "(none)" : r.orphanInvoiceIds.toString());
            totalOrphans += r.orphanInvoiceIds.size();
            totalLocalInvoices += r.localInvoices;
        }
        System.out.println();
        System.out.printf("Local scan: %d orphan invoices across %d local invoices.%n",
            totalOrphans, totalLocalInvoices);
    }

    private static final class LocalScanTask implements IgniteCallable<NodeReport> {
        private static final long serialVersionUID = 1L;

        @IgniteInstanceResource
        private Ignite local;

        @Override
        public NodeReport call() {
            UUID localId = local.cluster().localNode().id();

            IgniteCache<Integer, BinaryObject> customers =
                local.<Integer, Object>cache(CUSTOMERS).withKeepBinary();
            IgniteCache<BinaryObject, BinaryObject> invoices =
                local.<Object, Object>cache(INVOICES).withKeepBinary();

            Set<Integer> localCustomerIds = new HashSet<>();
            try (QueryCursor<Cache.Entry<Integer, BinaryObject>> cur =
                     customers.query(new ScanQuery<Integer, BinaryObject>().setLocal(true))) {
                for (Cache.Entry<Integer, BinaryObject> e : cur) {
                    localCustomerIds.add(e.getKey());
                }
            }

            int localInvoices = 0;
            List<Integer> orphans = new ArrayList<>();
            try (QueryCursor<Cache.Entry<BinaryObject, BinaryObject>> cur =
                     invoices.query(new ScanQuery<BinaryObject, BinaryObject>().setLocal(true))) {
                for (Cache.Entry<BinaryObject, BinaryObject> e : cur) {
                    localInvoices++;
                    Integer custId = e.getKey().field("customerId");
                    Integer invoiceId = e.getKey().field("invoiceId");
                    if (!localCustomerIds.contains(custId)) {
                        orphans.add(invoiceId);
                    }
                }
            }
            Collections.sort(orphans);
            return new NodeReport(localId, localCustomerIds.size(), localInvoices, orphans);
        }
    }

    private static final class NodeReport implements Serializable {
        private static final long serialVersionUID = 1L;
        final UUID nodeId;
        final int localCustomers;
        final int localInvoices;
        final List<Integer> orphanInvoiceIds;

        NodeReport(UUID nodeId, int localCustomers, int localInvoices, List<Integer> orphanInvoiceIds) {
            this.nodeId = nodeId;
            this.localCustomers = localCustomers;
            this.localInvoices = localInvoices;
            this.orphanInvoiceIds = orphanInvoiceIds;
        }
    }

    private static void seed(IgniteCache<Integer, Customer> customers,
                             IgniteCache<BrokenInvoiceKey, Invoice> invoices) {
        customers.put(1, new Customer("Acme"));
        customers.put(2, new Customer("Globex"));
        customers.put(3, new Customer("Initech"));
        for (int c = 1; c <= CUSTOMER_COUNT; c++) {
            for (int s = 1; s <= INVOICES_PER_CUSTOMER; s++) {
                int id = c * 100 + s;
                invoices.put(new BrokenInvoiceKey(id, c),
                    new Invoice("Invoice " + id, new BigDecimal(100 + s)));
            }
        }
    }

    private static CacheConfiguration<Integer, Customer> customerCfg() {
        return new CacheConfiguration<Integer, Customer>(CUSTOMERS)
            .setCacheMode(CacheMode.PARTITIONED)
            .setBackups(1)
            .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS))
            .setSqlSchema("PUBLIC");
    }

    private static CacheConfiguration<BrokenInvoiceKey, Invoice> invoiceCfg() {
        return new CacheConfiguration<BrokenInvoiceKey, Invoice>(INVOICES)
            .setCacheMode(CacheMode.PARTITIONED)
            .setBackups(1)
            .setAffinity(new RendezvousAffinityFunction(false, PARTITIONS))
            .setSqlSchema("PUBLIC");
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

    private static ClusterNode first(Collection<ClusterNode> nodes) {
        return nodes.isEmpty() ? null : nodes.iterator().next();
    }

    private static boolean sameNode(ClusterNode a, ClusterNode b) {
        return a != null && b != null && a.id().equals(b.id());
    }
}
```
{% endcode %}

Run the broken variant:

```bash
mvn -f verify-colocation/pom.xml compile
mvn -f verify-colocation/pom.xml exec:exec -Dexec.mainClass=com.example.verify.BrokenColocation
```

Expected output:

```text
=== Act 1: Runtime API (mapKeyToPrimaryAndBackups) ===

Invoice    Customer primary   Invoice primary    Match
----------------------------------------------------------------
101        node2              node3              MISMATCH
102        node2              node2              OK
103        node2              node2              OK
201        node2              node2              OK
202        node2              node1              MISMATCH
203        node2              node2              OK
301        node1              node1              OK
302        node1              node1              OK
303        node1              node3              MISMATCH

Runtime API: 6 of 9 invoices share a primary with their customer.

=== Act 2: System Views (SYS.CACHE_GROUPS, SYS.PARTITION_STATES) ===

--- SYS.CACHE_GROUPS rows for the two caches ---
CACHE_GROUP_NAME       PARTITIONS  BACKUPS  CACHE_MODE        CACHE_GROUP_ID
--------------------------------------------------------------------
customers-broken       32          1        PARTITIONED       -1646277555
invoices-broken        32          1        PARTITIONED       -599797604

--- SYS.PARTITION_STATES: primary partitions per node per cache ---
CACHE                  NODE         PRIMARY PARTITION COUNT
--------------------------------------------------------------
customers-broken       node1        13
customers-broken       node2        10
customers-broken       node3        9
invoices-broken        node1        13
invoices-broken        node2        10
invoices-broken        node3        9

Both caches report 32 partitions and healthy distribution.
The system views cannot tell that invoices are hashing on
the wrong field. Structural health and colocation health
are two different questions.

=== Act 3: Local scan (ScanQuery.setLocal on each server) ===

Node       Local customers    Local invoices     Orphan invoices
----------------------------------------------------------------
node1      1                  3                  [202]
node2      2                  4                  (none)
node3      0                  2                  [101, 303]

Local scan: 3 orphan invoices across 9 local invoices.
```

Read each act. The same contract failure produces three different signals.

**Act 1 names the failing rows.** The summary line prints how many of nine invoices share a primary with their customer, and the exact split is topology-dependent. Three invoices in this reference run print `MISMATCH` with the specific customer primary and invoice primary. A test harness that iterates nine keys and asserts the match fails at exactly the right line. This is the signal you want from CI.

**Act 2 looks identical to the good run.** Same partition counts. Same per-node distribution. Same cache shape. Both caches are running correctly as independent PARTITIONED caches with 32 partitions, so the cluster is structurally healthy. The system views describe what the cluster is doing, not what the reader intended. A schema audit that relies on SYS queries alone sees nothing wrong in this output.

**Act 3 names the orphans.** On the reference run captured above, node1 hosts one invoice (202) whose customer lives on node2, and node3 hosts two invoices (101 and 303) whose customers live on node2 and node1. Specific invoice IDs and per-node counts vary with topology and seed. The shape (a `[id, id, ...]` orphan list) is what a broken JOIN returns as missing rows at production scale.

The three signals compound. If Act 1 runs in a test on every build, a regression fails the build before it merges. If Act 3 runs in a smoke test before deploy, a regression that somehow reached staging fails the smoke test. Act 2 is the audit that tells an operator the cluster is alive when none of the contract-level checks are running at all.

{% hint style="success" %}
**Checkpoint:** `BrokenColocation` reports some `OK` rows and some `MISMATCH` rows on Act 1, the same partition distribution as the good run on Act 2, and one or more orphan invoices with specific invoice IDs on Act 3. The exact counts depend on the 3-node topology and the seed used by the data loader, but the failure pattern is the same on any topology.
{% endhint %}

## Which Technique Answers Which Question

The three techniques look at the same cluster through three different lenses. Pick by the question you are answering.

| Question | Technique | Failure signal |
|---|---|---|
| Is my colocation contract wired correctly? | Runtime API (`mapKeyToPrimaryAndBackups`) | OK/MISMATCH per key with specific primary nodes named |
| What is the cluster running? | System views (`SYS.CACHE_GROUPS`, `SYS.PARTITION_STATES`) | Structural description only; cannot see contract intent |
| Will a cross-cache JOIN or compute job return correct rows? | Local scan broadcast (`ScanQuery.setLocal(true)`) | Named orphan rows per node |

**Runtime API** runs from any process with a client handle, returns in milliseconds, and reads nothing from the cluster itself. It catches a miswired contract the fastest and is the only technique that belongs in a unit test. It cannot detect problems that only manifest with real data in place, like a customer ID that never appears in the invoice cache.

**System views** tell you the cluster is alive and both caches are distributed. They do not read intent. Two caches with unrelated affinity contracts can produce identical partition distributions. Use them to confirm operations are healthy and to collect the CACHE_GROUP_ID values you need to correlate to partition-level data. Do not use them to prove colocation.

**Local scan broadcast** is the closest mirror of what a colocated JOIN does at runtime. The thick-client-only `setLocal(true)` flag pins each server's scan to its own primary partitions. The callable has to handle binary keys and values because domain classes do not live on the server classpath. `withKeepBinary` plus `BinaryObject.field` reads composite key fields without a Java class. Use it as a pre-deploy smoke test, and use it on a production sample when diagnosing a wrong-answer JOIN in the wild.

Ship all three. Each catches a category of failure the others miss, and the cost of running them compounds the other way. If one technique regresses, the others still hold the line.

## Summary

Colocation fails silently because the cache has no path to reject an incorrect contract. Every put succeeds, every get returns a value, and a wrong answer looks identical to a right answer until a JOIN or a compute job exposes it. The verification toolkit is what closes the gap.

**Runtime API assertions run in milliseconds and fail per-row.** `mapKeyToPrimaryAndBackups` reads cached topology and compares expected versus actual primary ownership. Nine keys, nine assertions, one verdict. That belongs in a unit test run on every build.

**System views describe what the cluster is running.** `SYS.CACHE_GROUPS` gives you partition count, backups, and cache mode per group, while `SYS.PARTITION_STATES` gives you the partition-to-node map with an `IS_PRIMARY` flag. Together they answer "is the cluster healthy and correctly provisioned?" They cannot answer "are these two caches colocated correctly?"

**Local scan broadcasts verify what the JOIN sees.** `ScanQuery.setLocal(true)` is thick-client only and reads one node's primary partitions. Broadcast the scan to every server, have each server check its own data against the contract, and count orphans. An orphan count of zero is the only safe number to ship.

The three techniques are not redundant. They probe different surfaces of the same cluster and fail in different ways. A production-grade verification story runs all three. The runtime API fails fast on wiring bugs, the system views confirm operational health, and the local scan catches the residual case where a wiring bug passes review but the data itself is inconsistent.

### What's Next

- Affinity-Aware Compute at Scale (coming soon) builds compute gravity on top of the local-scan pattern. Every server runs jobs against its own partition of the data, coordinating nothing cross-node.
- When to Break Colocation (coming soon) teaches the inverse design decision: reference tables that belong in `REPLICATED` caches, fact-dimension star schemas, and `setDistributedJoins(true)` for the cases where colocation is not the right answer.

### Related

- [Design Keys for Colocation](design-keys-for-colocation.md) built the three mechanisms this tutorial verifies.
- [Understand How Your Cache Is Distributed](../cache-centric-foundations/understand-cache-distribution.md) introduced `Affinity<K>` and the 3-node cluster.
