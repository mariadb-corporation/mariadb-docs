---
description: >-
  Move beyond client-side joins. Annotate POJOs with @QuerySqlField, run SqlFieldsQuery on cached data, and use colocation for fast cross-cache JOINs.
---

# From Key-Value to SQL: The JOIN Problem

## Introduction

A customer support screen shows every invoice for a given customer. A monthly report pulls all orders billed from Brazil. Each screen starts with something you know (a customer ID, a country name) and returns records whose keys you do not know.

Cache API lookups need keys you already have. The Cache API can push a single-cache predicate to the server with `ScanQuery` and `IgniteBiPredicate`, and `cache.iterator()` can return every entry for client-side filtering. Neither helps when the question is "invoices joined to their customers filtered by country and grouped by month." This tutorial teaches the same caches to answer the harder questions with SQL: you load the Chinook music-store dataset (59 customers, 412 invoices) into two caches, ask one concrete question three ways, and finish with a cross-cache JOIN whose EXPLAIN plan shows how colocation keeps the JOIN local.

## Prerequisites

- **A running single-node cluster** from [Start a Local Cache Development Cluster](../cache-centric-foundations/start-local-cache-cluster.md)
- **Cache API familiarity** from [Work with the Cache API](../cache-centric-foundations/work-with-cache-api.md)
- **Java 11 or later** for the client runtime
- **Maven 3.6** or later
- **Docker Compose 2.23** or later

This tutorial builds a fresh Maven project called `sql-on-cache/`. It does not extend the `cache-client/` project from the Foundations path because the SQL engine needs the `ignite-indexing` dependency that the Cache API tutorials did not use.

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

If the container is stopped, restart it:

```bash
docker compose -f cache-cluster/docker-compose.yml start
```

If the cluster was destroyed (`docker compose down`), recreate it from the cache-cluster Docker Compose in the Foundations path. The cluster runs in-memory, so destroying it discards the cache. Running `ConfigureCaches` and `SeedFromChinook` in this tutorial will recreate the caches and reload the dataset.

</details>

## What You Will Learn

In this tutorial, you:

- Annotate POJOs with `@QuerySqlField` so the cache knows which fields are SQL columns
- Configure two caches with `setIndexedTypes` to register the SQL schema from the annotations
- Seed the caches from a Chinook dataset file using SQL `INSERT` statements through `SqlFieldsQuery`
- Answer "find all invoices for customer 17" with the Cache API alone and watch the client-side scan do the wrong thing
- Replace the scan with a parameterized `SqlFieldsQuery` and see the filter run server-side on an index
- Run a cross-cache JOIN between Customer and Invoice and read the H2 EXPLAIN plan that confirms it stayed local

## Define the Queryable Schema

Three POJOs carry the schema: `Customer`, `Invoice`, and the composite `InvoiceKey`. Annotations on their fields tell the cache which columns exist, which ones are indexed, and which one drives partitioning.

Create a Maven project called `sql-on-cache/`. The `pom.xml` adds two things the Foundations path did not need: the `ignite-indexing` dependency that brings the H2 SQL engine onto the classpath, and an extra `--add-opens` entry so the optimized marshaller can read `java.sql.Date`.

{% code title="sql-on-cache/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>sql-on-cache</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>11</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.sqlquery.ConfigureCaches</exec.mainClass>
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
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>ignite-indexing</artifactId>
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
                        <argument>--add-opens</argument>
                        <argument>java.base/java.math=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>java.sql/java.sql=ALL-UNNAMED</argument>
                        <argument>--add-opens</argument>
                        <argument>jdk.management/com.sun.management.internal=ALL-UNNAMED</argument>
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

{% hint style="info" %}

`ignite-indexing` is new here. The Foundations path used only `gridgain-core` because none of those tutorials ran SQL. Without `ignite-indexing` on the classpath, the first call to `setIndexedTypes` fails with `ClassNotFoundException: org.apache.ignite.internal.processors.query.h2.IgniteH2Indexing`.

The extra `--add-opens=java.sql/java.sql=ALL-UNNAMED` is also new. The optimized marshaller needs reflective access to `java.sql.Date` when an invoice's `invoiceDate` field serializes. Under Java 11 and later, the module system forbids that access unless the `java.sql` module is opened explicitly.

{% endhint %}

Create the three model classes under `src/main/java/com/example/sqlquery/model/`:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/model/Customer.java" %}
```java
package com.example.sqlquery.model;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

/**
 * Customer POJO stored in the "Customer" cache with an Integer key.
 *
 * Fields annotated with @QuerySqlField are visible to SQL as columns on
 * the Customer table. The customerId is the cache key (not a field on
 * this class); in SQL it is referenced as the _key pseudo-column.
 */
public class Customer {
    @QuerySqlField
    private String firstName;

    @QuerySqlField
    private String lastName;

    @QuerySqlField
    private String country;

    public Customer() {
    }

    public Customer(String firstName, String lastName, String country) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.country = country;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getCountry() {
        return country;
    }

    @Override
    public String toString() {
        return "Customer{firstName='" + firstName + "', lastName='" + lastName
            + "', country='" + country + "'}";
    }
}
```
{% endcode %}

Three fields, three `@QuerySqlField` annotations. Every annotated field becomes a SQL column with the same name as the field. Fields without the annotation are still stored on the cache entry, but they are invisible to SQL and cannot appear in `SELECT` column lists or `WHERE` predicates. The `customerId` is the cache key here, not a field. SQL references the cache key through a pseudo-column called `_key`, which the cross-cache JOIN later in this tutorial uses in its join predicate.

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/model/Invoice.java" %}
```java
package com.example.sqlquery.model;

import java.math.BigDecimal;
import java.sql.Date;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

/**
 * Invoice POJO stored in the "Invoice" cache with a composite InvoiceKey.
 *
 * The invoiceId and customerId fields live on InvoiceKey, not here.
 * Keeping them on the key class lets the same fields drive partitioning
 * (via @AffinityKeyMapped) and appear as SQL columns (via @QuerySqlField
 * on the key).
 */
public class Invoice {
    @QuerySqlField
    private Date invoiceDate;

    @QuerySqlField
    private String billingCountry;

    @QuerySqlField
    private BigDecimal total;

    public Invoice() {
    }

    public Invoice(Date invoiceDate, String billingCountry, BigDecimal total) {
        this.invoiceDate = invoiceDate;
        this.billingCountry = billingCountry;
        this.total = total;
    }

    public Date getInvoiceDate() {
        return invoiceDate;
    }

    public String getBillingCountry() {
        return billingCountry;
    }

    public BigDecimal getTotal() {
        return total;
    }

    @Override
    public String toString() {
        return "Invoice{invoiceDate=" + invoiceDate + ", billingCountry='"
            + billingCountry + "', total=" + total + "}";
    }
}
```
{% endcode %}

The Invoice POJO carries the fields that change per invoice: the date, the billing country, and the total. It does not carry `invoiceId` or `customerId`. Both of those fields live on the composite key class because the cache key in the Invoice cache is a composite of `(invoiceId, customerId)`. Putting `customerId` on the key lets one annotation do two jobs: drive partitioning so customer 17's invoices live on the same node as customer 17, and expose the field as a SQL column so queries can filter on it.

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/model/InvoiceKey.java" %}
```java
package com.example.sqlquery.model;

import java.util.Objects;

import org.apache.ignite.cache.affinity.AffinityKeyMapped;
import org.apache.ignite.cache.query.annotations.QuerySqlField;

/**
 * Composite key for the Invoice cache.
 *
 * Two annotations carry different roles on this class:
 *
 *   - @QuerySqlField exposes the field as a SQL column on the Invoice
 *     table. Composite-key fields must be annotated here to appear in
 *     SELECTs and INSERTs. The annotation on the value class is not
 *     enough.
 *   - @AffinityKeyMapped marks customerId as the colocation key. Every
 *     invoice lands on the same partition as the customer whose id
 *     matches. The cross-cache JOIN in ColocatedJoin relies on this.
 *
 * The index = true on customerId makes WHERE customerId = ? use an
 * index scan instead of a table scan.
 */
public class InvoiceKey {
    @QuerySqlField
    private Integer invoiceId;

    @QuerySqlField(index = true)
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
        if (o == null || getClass() != o.getClass()) return false;
        InvoiceKey that = (InvoiceKey) o;
        return Objects.equals(invoiceId, that.invoiceId)
            && Objects.equals(customerId, that.customerId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(invoiceId, customerId);
    }

    @Override
    public String toString() {
        return "InvoiceKey{invoiceId=" + invoiceId + ", customerId=" + customerId + "}";
    }
}
```
{% endcode %}

`InvoiceKey` is the most concept-dense class in the tutorial. Three annotations across two fields encode three separate decisions:

- **`@QuerySqlField` on `invoiceId`** surfaces the field as a SQL column. Without the annotation, `SELECT invoiceId FROM Invoice` fails with `Column "INVOICEID" not found`.
- **`@QuerySqlField(index = true)` on `customerId`** does two things at once: surfaces the column to SQL, and tells the SQL engine to maintain an index on it. Queries later in this tutorial filter on this column, and the index is what makes those queries an index scan rather than a table scan.
- **`@AffinityKeyMapped` on `customerId`** is the colocation declaration. The cache partitions entries by hashing this field, which places every invoice on the same node as the customer whose ID matches. The cross-cache JOIN relies on this. `@AffinityKeyMapped` alone does not expose the field to SQL, and `@QuerySqlField` alone does not influence partitioning. Both annotations stack on the colocation key so it does both jobs.

{% hint style="info" %}

Open `InvoiceKey` and hover on `@AffinityKeyMapped`. The IDE's JavaDoc popup names the default affinity mapper that reads the annotation: `GridCacheDefaultAffinityKeyMapper`. No `CacheConfiguration.setAffinityMapper()` call is needed to activate it. The mapper is the cluster's default and reflectively inspects every key class for the annotation.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** Three files exist under `src/main/java/com/example/sqlquery/model/`: `Customer.java`, `Invoice.java`, and `InvoiceKey.java`. The project compiles with `mvn compile`.
{% endhint %}

## Configure the Caches and Seed the Dataset

The caches need `QueryEntity` descriptions built from the annotations. After they exist, the Chinook dataset loads into them: 59 customers and 412 invoices.

Create `ConfigureCaches.java` in `com.example.sqlquery`:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/ConfigureCaches.java" %}
```java
package com.example.sqlquery;

import java.util.Collections;

import org.apache.ignite.Ignite;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

import com.example.sqlquery.model.Customer;
import com.example.sqlquery.model.Invoice;
import com.example.sqlquery.model.InvoiceKey;

/**
 * Creates the Customer and Invoice caches and registers the SQL
 * QueryEntity from the POJO annotations. Run once per cluster session.
 *
 * Each CacheConfiguration calls setIndexedTypes to register the key and
 * value classes with the SQL engine. setIndexedTypes scans the classes
 * for @QuerySqlField and @AffinityKeyMapped annotations and builds the
 * QueryEntity that makes SQL work against the cache.
 */
public class ConfigureCaches {

    public static void main(String[] args) {
        // VM IP finder: point discovery at the container's exposed port
        // (47500 default) so the client joins without multicast or DNS.
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);

        // Peer class loading must match across every node in the cluster.
        // The discovery attribute check rejects the join if the flag
        // differs. This class does not ship closures, but later tutorials
        // do, and the cluster config from the prior path enables it on
        // the server side.
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            CacheConfiguration<Integer, Customer> customerCfg =
                new CacheConfiguration<>("Customer");

            // setIndexedTypes turns this cache into a SQL-queryable one.
            // The engine inspects Customer for @QuerySqlField annotations,
            // builds a QueryEntity from them, and attaches it to the cache
            // configuration. Without this call, SELECTs against the
            // Customer table fail because the SQL engine has no schema.
            customerCfg.setIndexedTypes(Integer.class, Customer.class);
            ignite.getOrCreateCache(customerCfg);

            // setIndexedTypes on Invoice picks up the @QuerySqlField fields
            // and the @AffinityKeyMapped on InvoiceKey.customerId. The
            // affinity annotation partitions invoices by customerId rather
            // than by the InvoiceKey hash, which is what makes the cross-
            // cache JOIN later in this tutorial run locally per partition.
            CacheConfiguration<InvoiceKey, Invoice> invoiceCfg =
                new CacheConfiguration<>("Invoice");
            invoiceCfg.setIndexedTypes(InvoiceKey.class, Invoice.class);
            ignite.getOrCreateCache(invoiceCfg);

            System.out.println();
            System.out.println("=== Caches configured for SQL ===");
            System.out.println("Customer: " + ignite.cache("Customer").getName()
                + " (key=Integer, value=Customer)");
            System.out.println("Invoice:  " + ignite.cache("Invoice").getName()
                + " (key=InvoiceKey, value=Invoice, colocated by customerId)");
            System.out.println();
            System.out.println("Next: run SeedFromChinook to load 59 customers and 412 invoices.");
        }
        // GridGain's background threads keep the JVM alive for a few seconds
        // after the client closes. System.exit forces a clean shutdown.
        System.exit(0);
    }
}
```
{% endcode %}

Compile and run:

```bash
mvn -f sql-on-cache/pom.xml compile
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.ConfigureCaches
```

Expected output:

```text
=== Caches configured for SQL ===
Customer: Customer (key=Integer, value=Customer)
Invoice:  Invoice (key=InvoiceKey, value=Invoice, colocated by customerId)

Next: run SeedFromChinook to load 59 customers and 412 invoices.
```

Two caches exist. Both have `QueryEntity` descriptions built from the POJO annotations. Both are ready to accept SQL.

Now populate them. Run the curl from inside the `sql-on-cache/` directory so the SQL file lands next to the `pom.xml`. `SeedFromChinook` reads the file relative to the JVM's working directory, which is also `sql-on-cache/` when you run Maven from there.

The file contains 59 Customer INSERTs and 412 Invoice INSERTs, trimmed from the full Chinook music-store schema to the columns this tutorial queries. The dates use H2's `parsedatetime()` function because the cached SQL engine is H2.

Create `SeedFromChinook.java` in the same package:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/SeedFromChinook.java" %}
```java
package com.example.sqlquery;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Collections;
import java.util.List;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Loads the Chinook Customer and Invoice data into the two caches.
 *
 * The SQL file is read line by line and each INSERT statement is
 * executed as a SqlFieldsQuery. Each INSERT is routed to the cache
 * named in its target table. The dataset file uses H2's
 * parsedatetime() for invoice dates, which the H2 engine accepts at
 * INSERT time.
 *
 * Prerequisite: run ConfigureCaches first to create the caches. Also
 * download chinook-customers-invoices.sql into the project root
 * (sql-on-cache/) so the relative path below resolves under the JVM's
 * working directory.
 */
public class SeedFromChinook {

    private static final String SQL_FILE = "chinook-customers-invoices.sql";

    public static void main(String[] args) throws IOException {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            // ignite.cache(name) returns null when the cache does not
            // exist (unlike getOrCreateCache, which would create one).
            // This class depends on ConfigureCaches having run first.
            IgniteCache<?, ?> customers = ignite.cache("Customer");
            IgniteCache<?, ?> invoices = ignite.cache("Invoice");

            if (customers == null || invoices == null) {
                System.err.println("Caches not found. Run ConfigureCaches first.");
                System.exit(1);
            }

            // cache.clear() removes every entry without destroying the
            // cache or its QueryEntity registration, so the seed below
            // can re-run idempotently.
            customers.clear();
            invoices.clear();

            int customerCount = 0;
            int invoiceCount = 0;

            try (BufferedReader r = new BufferedReader(new FileReader(SQL_FILE))) {
                String line;
                while ((line = r.readLine()) != null) {
                    line = line.trim();
                    if (line.isEmpty() || line.startsWith("--")) {
                        continue;
                    }
                    // The cache that receives query() becomes the implicit
                    // SQL schema for unqualified table references, so route
                    // each INSERT to the owning cache.
                    if (line.startsWith("INSERT INTO Customer")) {
                        customers.query(new SqlFieldsQuery(line));
                        customerCount++;
                    } else if (line.startsWith("INSERT INTO Invoice")) {
                        invoices.query(new SqlFieldsQuery(line));
                        invoiceCount++;
                    }
                }
            }

            System.out.println();
            System.out.println("=== Seeded from " + SQL_FILE + " ===");
            System.out.println("Customer INSERTs executed: " + customerCount);
            System.out.println("Invoice INSERTs executed:  " + invoiceCount);

            long customerRows = count(customers, "\"Customer\".Customer");
            long invoiceRows = count(invoices, "\"Invoice\".Invoice");
            System.out.println("Customer rows in cache: " + customerRows);
            System.out.println("Invoice rows in cache:  " + invoiceRows);
        }
        System.exit(0);
    }

    /**
     * SELECT COUNT(*) returns one row with one Long column.
     */
    private static long count(IgniteCache<?, ?> cache, String table) {
        List<List<?>> rows = cache.query(new SqlFieldsQuery(
            "SELECT COUNT(*) FROM " + table)).getAll();
        return (long) rows.get(0).get(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.SeedFromChinook
```

Expected output:

```text
=== Seeded from chinook-customers-invoices.sql ===
Customer INSERTs executed: 59
Invoice INSERTs executed:  412
Customer rows in cache: 59
Invoice rows in cache:  412
```

`SqlFieldsQuery` runs DML, not just `SELECT`. The count queries also confirm that SQL and the Cache API share one storage. Rows inserted via SQL are the same entries `cache.get(1)` returns as a `Customer` POJO.

{% hint style="info" %}

Look at a Customer INSERT in the dataset file: `INSERT INTO Customer (_key, firstName, lastName, country) VALUES (1, 'Luís', 'Gonçalves', 'Brazil');`. The `_key` pseudo-column names the primitive cache key, which is not a field on the Customer POJO. Invoice INSERTs use the named fields directly (`INSERT INTO Invoice (invoiceId, customerId, ...) VALUES (...)`) because both fields of the composite `InvoiceKey` are visible as regular SQL columns thanks to `@QuerySqlField` on the key class.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** `Customer INSERTs executed: 59`, `Invoice INSERTs executed: 412`, and both counts match the rows in the caches.
{% endhint %}

## The Client-Side Filter

The caches hold 59 customers and 412 invoices. Consider the question that opened this tutorial: "find all invoices for customer 17." You know `customerId = 17`. You do not know the invoice IDs.

The Cache API has two iteration paths. `cache.iterator()` returns every entry to the client and the filter runs in Java. `cache.query(new ScanQuery<>(predicate))` pushes a single-cache `IgniteBiPredicate` to the server so only matches cross the network. This step uses the first path so the cost of pulling every entry is visible. Later steps move to SQL when the question outgrows a single-cache predicate.

Create `ClientSideFilter.java`:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/ClientSideFilter.java" %}
```java
package com.example.sqlquery;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import javax.cache.Cache;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

import com.example.sqlquery.model.Invoice;
import com.example.sqlquery.model.InvoiceKey;

/**
 * Answers "find all invoices for customer 17" using the Cache API
 * only.
 *
 * Uses cache.iterator() so every cache entry crosses the network
 * before the filter runs in Java. The Cache API also offers
 * ScanQuery + IgniteBiPredicate to push a single-cache predicate
 * to the server. This class deliberately picks the worst path so
 * the cost of pulling every entry is observable in the
 * scanned-count log line at the end. The next class (IndexedQuery)
 * moves to SQL when the question outgrows single-cache filtering.
 */
public class ClientSideFilter {

    public static void main(String[] args) {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            IgniteCache<InvoiceKey, Invoice> invoices = ignite.cache("Invoice");

            int targetCustomerId = 17;
            AtomicInteger scanned = new AtomicInteger();
            List<Cache.Entry<InvoiceKey, Invoice>> matches = new ArrayList<>();

            // cache.iterator() pulls every entry from each primary node
            // across the network into the client JVM. There is no
            // predicate argument that the cache could push to the server.
            // The filter below runs after each entry has already been
            // serialized and shipped. The scanned-count print at the end
            // exposes that cost.
            Iterator<Cache.Entry<InvoiceKey, Invoice>> it = invoices.iterator();
            while (it.hasNext()) {
                Cache.Entry<InvoiceKey, Invoice> entry = it.next();
                scanned.incrementAndGet();
                if (entry.getKey().getCustomerId() == targetCustomerId) {
                    matches.add(entry);
                }
            }

            System.out.println();
            System.out.println("=== Client-side filter: invoices for customer "
                + targetCustomerId + " ===");
            for (Cache.Entry<InvoiceKey, Invoice> entry : matches) {
                System.out.println("  " + entry.getKey() + " -> " + entry.getValue());
            }

            System.out.println();
            System.out.println("Scanned " + scanned.get() + " entries, matched "
                + matches.size() + ".");
            System.out.println("The client pulled every invoice across the wire "
                + "and threw " + (scanned.get() - matches.size()) + " of them away.");
        }
        System.exit(0);
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.ClientSideFilter
```

Expected output:

```text
=== Client-side filter: invoices for customer 17 ===
  InvoiceKey{invoiceId=232, customerId=17} -> Invoice{invoiceDate=2011-10-20, billingCountry='USA', total=1.98}
  InvoiceKey{invoiceId=14, customerId=17} -> Invoice{invoiceDate=2009-03-03, billingCountry='USA', total=1.98}
  InvoiceKey{invoiceId=59, customerId=17} -> Invoice{invoiceDate=2009-09-07, billingCountry='USA', total=5.94}
  InvoiceKey{invoiceId=111, customerId=17} -> Invoice{invoiceDate=2010-04-28, billingCountry='USA', total=0.99}
  InvoiceKey{invoiceId=37, customerId=17} -> Invoice{invoiceDate=2009-06-05, billingCountry='USA', total=3.96}
  InvoiceKey{invoiceId=243, customerId=17} -> Invoice{invoiceDate=2011-11-30, billingCountry='USA', total=13.86}
  InvoiceKey{invoiceId=298, customerId=17} -> Invoice{invoiceDate=2012-07-30, billingCountry='USA', total=10.91}

Scanned 412 entries, matched 7.
The client pulled every invoice across the wire and threw 405 of them away.
```

Customer 17 has seven invoices, all from the USA. The scanned-count line makes the cost visible: 412 entries crossed the wire, 405 were thrown away. Scale that ratio to millions of entries and the JVM runs out of heap before the scan finishes.

The Cache API can push a server-side predicate over a single cache with `ScanQuery` and `IgniteBiPredicate`, which would skip the wasted-entry shipping shown above. What the Cache API cannot do is join two caches in one query, run an aggregation, or accept the composable typed predicates a column-aware engine offers. The annotations you added in the last step gave the cache another way to answer those questions: SQL.

{% hint style="success" %}
**Checkpoint:** Output shows 7 invoices for customer 17 with the scanned count of 412 and the note about 405 entries thrown away.
{% endhint %}

## SQL on one Cache

Create `IndexedQuery.java`. The class runs three queries against the Invoice cache: a parameterized lookup by the indexed `customerId`, a two-predicate scan, and an aggregation.

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/IndexedQuery.java" %}
```java
package com.example.sqlquery;

import java.math.BigDecimal;
import java.util.Collections;
import java.util.List;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.query.FieldsQueryCursor;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Answers the same question ClientSideFilter asked, plus two
 * variations, with SqlFieldsQuery. The filter runs server-side, so
 * only matching rows cross the wire.
 *
 * Three queries demonstrate what the SQL surface adds:
 *   1. Parameterized WHERE on the indexed customerId column (index scan).
 *   2. Filter composition: two predicates combine naturally.
 *   3. Aggregation: the cache computes a summary instead of returning rows.
 */
public class IndexedQuery {

    public static void main(String[] args) {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            IgniteCache<?, ?> invoices = ignite.cache("Invoice");

            query1(invoices);
            query2(invoices);
            query3(invoices);
        }
        System.exit(0);
    }

    /**
     * Query 1: parameterized lookup on the indexed customerId column.
     *
     * @QuerySqlField(index = true) on InvoiceKey.customerId created a
     * B-tree index the H2 planner can use. With the index available,
     * WHERE customerId = ? turns into an index seek rather than a
     * table scan, so the cost of the query is O(log N) in the number
     * of invoices rather than O(N). Only matching rows cross the wire.
     * The scanning that ClientSideFilter did on the JVM now happens
     * inside the SQL engine.
     */
    private static void query1(IgniteCache<?, ?> invoices) {
        System.out.println();
        System.out.println("=== Query 1: invoices for customer 17 ===");

        // setArgs binds positional `?` placeholders. The planner can
        // cache the plan across different argument values, and the
        // engine quotes bound values safely. Close the cursor to release
        // server-side query resources.
        try (FieldsQueryCursor<List<?>> c = invoices.query(new SqlFieldsQuery(
            "SELECT invoiceId, invoiceDate, total FROM Invoice "
                + "WHERE customerId = ? ORDER BY invoiceDate")
            .setArgs(17))) {
            c.getAll().forEach(row ->
                System.out.println("  invoiceId=" + row.get(0)
                    + ", date=" + row.get(1)
                    + ", total=" + row.get(2)));
        }
    }

    /**
     * Query 2: two predicates, two bind arguments.
     *
     * Neither billingCountry nor total is declared with index = true,
     * so the planner has no index to use. It falls back to a full
     * scan of the Invoice data, applying both predicates as filters
     * per row. The two predicates combine on the server in one
     * declarative statement. In the Cache API version, a similar
     * question would need a custom loop with two if-checks, and both
     * fields would have to be deserialized on the client before the
     * checks ran.
     */
    private static void query2(IgniteCache<?, ?> invoices) {
        System.out.println();
        System.out.println("=== Query 2: Brazilian invoices over $3.00 ===");

        // BigDecimal for money matches the column type (DECIMAL), so the
        // server skips implicit conversion and arithmetic stays exact.
        try (FieldsQueryCursor<List<?>> c = invoices.query(new SqlFieldsQuery(
            "SELECT invoiceId, customerId, billingCountry, total FROM Invoice "
                + "WHERE billingCountry = ? AND total > ? ORDER BY total DESC")
            .setArgs("Brazil", new BigDecimal("3.00")))) {
            c.getAll().forEach(row ->
                System.out.println("  invoiceId=" + row.get(0)
                    + ", customerId=" + row.get(1)
                    + ", country=" + row.get(2)
                    + ", total=" + row.get(3)));
        }
    }

    /**
     * Query 3: aggregation.
     *
     * This is the biggest shift from the Cache API. COUNT(*),
     * SUM(total), and MAX(total) all run on the server, and the
     * client receives one row with three scalar columns. The Cache
     * API has no equivalent: there is no cache.count(predicate),
     * no cache.sum(field, predicate). To get a sum across 412
     * invoices with the Cache API, you would iterate them all and
     * add in Java (and ship 412 BigDecimals over the network to do
     * it). Aggregations are where the SQL-on-cache surface earns
     * its place.
     */
    private static void query3(IgniteCache<?, ?> invoices) {
        System.out.println();
        System.out.println("=== Query 3: customer 17 spend summary ===");
        try (FieldsQueryCursor<List<?>> c = invoices.query(new SqlFieldsQuery(
            "SELECT COUNT(*), SUM(total), MAX(total) FROM Invoice "
                + "WHERE customerId = ?")
            .setArgs(17))) {

            // COUNT(*) returns Long; SUM and MAX over a DECIMAL column
            // return BigDecimal.
            List<?> row = c.getAll().get(0);
            System.out.println("  count=" + row.get(0)
                + ", sum=" + row.get(1)
                + ", max=" + row.get(2));
        }
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.IndexedQuery
```

Expected output:

```text
=== Query 1: invoices for customer 17 ===
  invoiceId=14, date=2009-03-03, total=1.98
  invoiceId=37, date=2009-06-05, total=3.96
  invoiceId=59, date=2009-09-07, total=5.94
  invoiceId=111, date=2010-04-28, total=0.99
  invoiceId=232, date=2011-10-20, total=1.98
  invoiceId=243, date=2011-11-30, total=13.86
  invoiceId=298, date=2012-07-30, total=10.91

=== Query 2: Brazilian invoices over $3.00 ===
  invoiceId=68, customerId=11, country=Brazil, total=13.86
  invoiceId=327, customerId=1, country=Brazil, total=13.86
  invoiceId=166, customerId=12, country=Brazil, total=13.86
  invoiceId=383, customerId=10, country=Brazil, total=13.86
  invoiceId=264, customerId=13, country=Brazil, total=13.86
  invoiceId=123, customerId=11, country=Brazil, total=8.91
  invoiceId=382, customerId=1, country=Brazil, total=8.91
  invoiceId=25, customerId=10, country=Brazil, total=8.91
  invoiceId=221, customerId=12, country=Brazil, total=8.91
  invoiceId=319, customerId=13, country=Brazil, total=8.91
  invoiceId=297, customerId=11, country=Brazil, total=5.94
  invoiceId=80, customerId=13, country=Brazil, total=5.94
  invoiceId=143, customerId=1, country=Brazil, total=5.94
  invoiceId=395, customerId=12, country=Brazil, total=5.94
  invoiceId=199, customerId=10, country=Brazil, total=5.94
  invoiceId=98, customerId=1, country=Brazil, total=3.98
  invoiceId=121, customerId=1, country=Brazil, total=3.96
  invoiceId=373, customerId=12, country=Brazil, total=3.96
  invoiceId=177, customerId=10, country=Brazil, total=3.96
  invoiceId=275, customerId=11, country=Brazil, total=3.96
  invoiceId=58, customerId=13, country=Brazil, total=3.96

=== Query 3: customer 17 spend summary ===
  count=7, sum=39.62, max=13.86
```

**Query 1** returned the same seven invoices as the client-side scan, but the filter ran on the server against the `customerId` index. Only matching rows crossed the wire, and the `ORDER BY invoiceDate` clause also ran server-side.

**Query 2** applied two predicates. Neither `billingCountry` nor `total` has an index, so H2 scans the Invoice data and applies both conditions as filters during the scan. The predicates compose at the SQL layer in one statement. A Cache API version would need a custom loop evaluating both conditions per entry.

**Query 3** is the biggest shift. The cache computed `COUNT(*)`, `SUM(total)`, and `MAX(total)` for the seven matching invoices and returned one row with three columns. The Cache API has no `cache.count(predicate)` or `cache.sum(field, predicate)`. Aggregations are a SQL-only surface.

{% hint style="info" %}

Type `new SqlFieldsQuery("SELECT 1").` and let the IDE show the builder methods. Beyond `setArgs` (used here) the list includes `setSchema`, `setLazy`, `setDistributedJoins`, `setPageSize`, and `setTimeout`. Most tutorials use a small subset. The two you are most likely to reach for next are `setPageSize(int)` for large result sets and `setTimeout(long, TimeUnit)` for long-running analytical queries.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** All three queries run. Query 1 returns 7 rows for customer 17, Query 2 returns 21 rows for Brazilian invoices over $3.00, and Query 3 returns `count=7, sum=39.62, max=13.86`.
{% endhint %}

## Cross-Cache JOIN With Colocation

The next question spans two caches: which Brazilian customers have spent the most in total? Country lives on the Customer cache. Invoice totals live on the Invoice cache. One JOIN answers both.

`@AffinityKeyMapped` on `InvoiceKey.customerId` already aligns the two caches so each customer's invoices live on the same partition as the customer record. The JOIN below uses that alignment, and the EXPLAIN plan after confirms it.

Create `ColocatedJoin.java`:

{% code title="sql-on-cache/src/main/java/com/example/sqlquery/ColocatedJoin.java" %}
```java
package com.example.sqlquery;

import java.util.Collections;
import java.util.List;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.query.FieldsQueryCursor;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Runs a JOIN across the Customer and Invoice caches, then prints the
 * H2 execution plan for the same query.
 *
 * Two cache boundaries get crossed by this SQL:
 *
 *   1. The "Customer" and "Invoice" cache names are also SQL schema
 *      names. Unqualified table references look in the current cache's
 *      schema, and cross-cache queries must qualify with "Schema".Table.
 *
 *   2. The join predicate matches Customer's primary key to Invoice's
 *      @AffinityKeyMapped field. That match is what makes the join
 *      local. Each customer's invoices are already on the same
 *      partition as the customer record, so H2 can join without
 *      moving data between nodes.
 *
 * The EXPLAIN output is H2's two-statement map/reduce plan. The first
 * SELECT runs on each partition producing partial aggregates. The
 * second SELECT merges the partials at the coordinator.
 */
public class ColocatedJoin {

    // The JOIN query is defined once and reused for both the live run
    // and the EXPLAIN inspection. Using a constant keeps the two calls
    // guaranteed to match, which matters when you want the plan to
    // describe the same query that produced the result rows.
    //
    // Three pieces of this SQL are worth reading slowly:
    //
    //   1. "Customer".Customer and "Invoice".Invoice are
    //      schema-qualified table references. Each cache exposes
    //      one SQL schema whose name equals the cache name. The
    //      quotes preserve the cache name's case, because H2
    //      uppercases unquoted identifiers.
    //
    //   2. c._key = i.customerId is the join predicate. Customer's
    //      cache key is an Integer, which SQL sees through the _key
    //      pseudo-column. InvoiceKey.customerId is a composite-key
    //      field annotated @QuerySqlField, so it appears as a regular
    //      SQL column. Both sides of the equality are the customer's
    //      ID, stored once as Customer's key and once as Invoice's
    //      affinity field.
    //
    //   3. GROUP BY c._key, c.firstName, c.lastName groups by all
    //      non-aggregated columns of the SELECT, which is the SQL
    //      standard rule for GROUP BY. c._key is sufficient to
    //      uniquely group rows (it is the primary key), but H2
    //      requires every non-aggregated SELECT column to appear in
    //      the GROUP BY list.
    private static final String JOIN_SQL =
        "SELECT c.firstName, c.lastName, SUM(i.total) AS lifetime_spend "
            + "FROM \"Customer\".Customer c "
            + "JOIN \"Invoice\".Invoice i ON c._key = i.customerId "
            + "WHERE c.country = ? "
            + "GROUP BY c._key, c.firstName, c.lastName "
            + "ORDER BY lifetime_spend DESC";

    public static void main(String[] args) {
        TcpDiscoverySpi disco = new TcpDiscoverySpi();
        disco.setIpFinder(new TcpDiscoveryVmIpFinder()
            .setAddresses(Collections.singleton("127.0.0.1:47500")));

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setDiscoverySpi(disco);
        cfg.setClientMode(true);
        cfg.setPeerClassLoadingEnabled(true);

        try (Ignite ignite = Ignition.start(cfg)) {
            // Either cache can run a cross-cache query. The cache
            // the query() call is made on becomes the default schema
            // for unqualified table references. Running the query on
            // the Customer cache makes no difference for JOIN_SQL
            // because every table reference is schema-qualified.
            IgniteCache<?, ?> customers = ignite.cache("Customer");

            runJoin(customers);
            runExplain(customers);
        }
        System.exit(0);
    }

    /**
     * Runs the JOIN and prints the ranked customers.
     *
     * The result row has three columns: firstName, lastName,
     * and the SUM alias lifetime_spend. SUM on a DECIMAL column
     * returns a BigDecimal, which the println formats with the
     * default toString.
     */
    private static void runJoin(IgniteCache<?, ?> customers) {
        System.out.println();
        System.out.println("=== Cross-cache JOIN: Brazilian customers by lifetime spend ===");
        try (FieldsQueryCursor<List<?>> c = customers.query(new SqlFieldsQuery(JOIN_SQL)
            .setArgs("Brazil"))) {
            c.getAll().forEach(row ->
                System.out.println("  " + row.get(0) + " " + row.get(1)
                    + " -> $" + row.get(2)));
        }
    }

    /**
     * Runs EXPLAIN on the same JOIN and prints the plan.
     *
     * EXPLAIN is a SQL keyword, not an API call. Prepend it to the
     * query string. H2 returns one result row per SQL statement in
     * the final execution plan. For a distributed query like this
     * one, that is two rows: the map-phase statement (per partition)
     * and the reduce-phase statement (at the coordinator).
     *
     * Each plan row is a single VARCHAR column whose value is the
     * plan text. row.get(0) extracts that text. Printing it directly
     * reproduces H2's formatted output with comments that name the
     * indexes and scan types used.
     */
    private static void runExplain(IgniteCache<?, ?> customers) {
        System.out.println();
        System.out.println("=== EXPLAIN plan ===");
        try (FieldsQueryCursor<List<?>> c = customers.query(new SqlFieldsQuery(
            "EXPLAIN " + JOIN_SQL).setArgs("Brazil"))) {
            c.getAll().forEach(row -> System.out.println(row.get(0)));
        }
    }
}
```
{% endcode %}

Run it:

```bash
mvn -f sql-on-cache/pom.xml exec:exec \
  -Dexec.mainClass=com.example.sqlquery.ColocatedJoin
```

Expected output:

```text
=== Cross-cache JOIN: Brazilian customers by lifetime spend ===
  Luís Gonçalves -> $39.62
  Eduardo Martins -> $37.62
  Alexandre Rocha -> $37.62
  Roberto Almeida -> $37.62
  Fernanda Ramos -> $37.62

=== EXPLAIN plan ===
SELECT
    "C__Z0"."FIRSTNAME" AS "__C0_0",
    "C__Z0"."LASTNAME" AS "__C0_1",
    SUM("I__Z1"."TOTAL") AS "__C0_2",
    "C__Z0"."_KEY" AS "__C0_3"
FROM "Customer"."CUSTOMER" "C__Z0"
    /* Customer.CUSTOMER.__SCAN_ */
    /* WHERE C__Z0.COUNTRY = ?1
    */
INNER JOIN "Invoice"."INVOICE" "I__Z1"
    /* Invoice.INVOICEKEY_CUSTOMERID_IDX: CUSTOMERID = C__Z0._KEY */
    ON 1=1
WHERE ("C__Z0"."COUNTRY" = ?1)
    AND ("C__Z0"."_KEY" = "I__Z1"."CUSTOMERID")
GROUP BY "C__Z0"."_KEY", "C__Z0"."FIRSTNAME", "C__Z0"."LASTNAME"
SELECT
    "__C0_0" AS "FIRSTNAME",
    "__C0_1" AS "LASTNAME",
    CAST(CAST(SUM("__C0_2") AS DECIMAL(2147483647, 2147483647)) AS DECIMAL(2147483647, 2147483647)) AS "LIFETIME_SPEND"
FROM "PUBLIC"."__T0"
    /* Customer.merge_scan */
GROUP BY "__C0_3", "__C0_0", "__C0_1"
ORDER BY 3 DESC
```

Five Brazilian customers ranked by lifetime spend. Luís Gonçalves at $39.62 leads by a narrow margin. The other four tie at $37.62 because their Chinook purchase histories are nearly identical.

The EXPLAIN block shows two distinct SQL statements separated by the second `SELECT`. That structure is how distributed SQL executes. The first statement is the **map phase** that runs locally on each partition. The second statement is the **reduce phase** that runs at a single coordinator to merge the partial results. Read each block separately.

**Map phase (runs on each partition):**

- `FROM "Customer"."CUSTOMER" "C__Z0"` scans the local Customer partition with the comment `/* Customer.CUSTOMER.__SCAN_ */` and the predicate `WHERE C__Z0.COUNTRY = ?1`. The scan is a full read of the partition because `country` has no index. In a workload with many customers per country, adding `@QuerySqlField(index = true)` on `Customer.country` would turn this into an index scan.
- `INNER JOIN "Invoice"."INVOICE" "I__Z1"` with the comment `/* Invoice.INVOICEKEY_CUSTOMERID_IDX: CUSTOMERID = C__Z0._KEY */` probes the `INVOICEKEY_CUSTOMERID_IDX` index. That index is the one `@QuerySqlField(index = true)` on `InvoiceKey.customerId` created. Its name follows the pattern `{KeyClassName}_{fieldName}_IDX`.
- The critical absence is anything saying "distributed" or "broadcast." The JOIN runs on each partition against the partition's local Customer and Invoice rows. No data moves between partitions.

**Reduce phase (runs at the coordinator):**

- `FROM "PUBLIC"."__T0"` with the comment `/* Customer.merge_scan */` is the synthetic table that holds the partial aggregates from every partition's map phase. The coordinator groups them again and produces the final result. Because each partition only sends one small aggregate, the reduce phase stays cheap even for large tables.

{% hint style="info" %}

Some schemas cannot colocate. Order lines might need to be colocated with orders, not with customers. Product records might be referenced from every order without a natural colocation key. For those cases, `SqlFieldsQuery` has a `setDistributedJoins(true)` flag that tells the engine to move data between partitions to resolve the JOIN. The query returns correct results, but the cost model changes. The planner may stream rows between partitions, which is slower than a colocated JOIN. A later guide covers when to reach for the flag.

{% endhint %}

{% hint style="info" %}

The pinned version in this tutorial (GridGain 8.9.32) runs the H2 SQL engine.

{% endhint %}

{% hint style="success" %}
**Checkpoint:** The JOIN returns 5 Brazilian customers ranked by lifetime spend (Luís Gonçalves leads at $39.62), and the EXPLAIN plan shows the two-statement map/reduce structure with no cross-partition markers.
{% endhint %}

## Summary

You added two annotations and two new calls to a cache you already knew how to use. The cache went from "key lookups only" to "full SQL surface with indexes, aggregations, and cross-cache JOINs."

**The shape of the question selects the interface.** Lookups by a known key keep using `cache.get` at in-memory speed. Any predicate on a non-key field, any aggregation, any filter composition, and any JOIN uses `SqlFieldsQuery`. Both views exist on the same cache, over the same data. The choice is not a storage strategy. It is a query strategy made per call site.

**Colocation is a schema-design decision, not a runtime one.** A JOIN between two caches returns the same rows whether colocation is declared or not, but the cost model differs by orders of magnitude. `@AffinityKeyMapped` on the right key turns the JOIN into a local per-partition operation that scales with the number of partitions rather than the size of the data moved between them. Make the colocation decision when you define the cache, not when the query gets slow.

The deeper reframing is that the cache is a distributed database with two access surfaces. Key-value access handles single-key hot paths at in-memory speed. Everything else, filters, aggregations, JOINs, uses `SqlFieldsQuery` against the same data. One annotation on the POJO and one `setIndexedTypes` call replace the need for a separate query database alongside the cache.

### What's Next

- `setDistributedJoins(true)` for the case where colocation is not possible, covered in [When to Break Colocation](../data-locality/when-to-break-colocation.md).
- Secondary index strategies for high-cardinality columns and composite-index design (coming soon). In the meantime, see [Defining Indexes](../../gridgain8-development/sql/indexes.md).
- DDL-based cache creation (`CREATE TABLE ... WITH "CACHE_NAME=..., VALUE_TYPE=..."`), the alternative path that creates caches from SQL instead of Java configuration (coming soon). In the meantime, see [SQL and Key-Value Usage](../../gridgain8-development/sql/sql-key-value-storage.md).

The next tutorial in this learning path, [Atomic Operations Across Keys: The Transaction Problem](cross-partition-transactions.md), shifts from queries to writes. Cross-partition transactions solve the problem of atomically updating two keys that live on different nodes, a case single-shard `txStart()` does not cover.

### Related

- [Use Transactions with the Cache API](../cache-centric-foundations/cache-transactions.md) covers the atomicity tools that let multi-key writes succeed or fail together on a single partition.
- [Cache-Aside Under Load](../cache-centric-foundations/cache-aside-under-load.md) covers the mediation pattern where the cache sits in front of a source-of-truth database.
