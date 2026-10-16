---
description: >-
  Reference data belongs in REPLICATED caches.
---

# When to Break Colocation

## Introduction

The previous three tutorials colocated Customer and Invoice caches so every invoice lands on the same primary node as its customer. That design is correct for fact tables that share a join key. It is wrong for the reference data the same query needs to enrich the result.

Reference tables are small and read-often: a country list, a genre catalog, a media-type lookup. Every analytical query joins against them, and none of them grow with the fact volume. Partitioning a 30-row Country table across 32 partitions and 3 nodes produces partitions that hold one row each and forces the SQL engine to shuffle rows across the network on every join. The cache mode that fits these tables is `CacheMode.REPLICATED`. Every node keeps a full copy, and every JOIN reads it locally.

This tutorial builds three versions of the same star-schema report and runs the identical query against each. Version A puts every cache in `CacheMode.PARTITIONED` without colocation. Version B adds fact-fact colocation but keeps the dimensions partitioned. Version C moves the dimensions to `CacheMode.REPLICATED`. All three versions return correct results with `SqlFieldsQuery.setDistributedJoins(true)`. Version C runs 1.8x to 2.8x faster than Version A (the ratio depends on product) because the dimension tables no longer shuffle.

Star schema is a standard dimensional-modeling pattern: one fact table surrounded by small dimension tables, each joining on one foreign key. Readers who need a refresher can check the [Wikipedia article on star schema](https://en.wikipedia.org/wiki/Star_schema). This tutorial uses the pattern as a vehicle for the cache-mode decision rather than as a lesson in dimensional modeling.

The Java code is identical across Apache Ignite 2 and GridGain 8. Product tabs cover only Maven coordinates and the Docker image.

## Prerequisites

- **Completion of [Affinity-Aware Compute at Scale](affinity-aware-compute.md).** You have declared colocation with `@AffinityKeyMapped`, verified it with runtime checks, and computed against it. You have a working 3-node cluster.
- **A running 3-node cluster** from the previous tutorials. No configuration change is required.
- **Java 11 or later** for the client runtime. The Maven project compiles to Java 8 bytecode to match the server JVM.
- **Maven 3.6** or later.
- **Docker Compose 2.23** or later.

This tutorial builds a fresh Maven project called `star-schema/` alongside `affinity-compute/`, `verify-colocation/`, and `colocation-keys/`. The cluster setup is unchanged.

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

- Create three cache-mode variants of the same star schema in one Maven project
- Observe the silent-wrong-answer failure mode when `setDistributedJoins(true)` is off on a multi-table JOIN
- Measure the cost of the flag with and without fact-fact colocation
- Move dimension tables to `CacheMode.REPLICATED` and measure the speedup
- Apply a decision framework for reference data: row count, write rate, access pattern

## Create the Star-Schema Project

Create a Maven project named `star-schema/` with the layout:

```text
star-schema/
├── pom.xml
└── src/main/java/com/example/star/
    ├── ClientConfig.java
    ├── Customer.java
    ├── Invoice.java
    ├── InvoiceKey.java
    ├── Country.java
    ├── Genre.java
    ├── MediaType.java
    ├── Dimensions.java
    ├── CacheConfigs.java
    ├── DataLoader.java
    └── ReportQuery.java
```

The `pom.xml` needs `ignite-indexing` in addition to `ignite-core`. The SQL engine lives in the indexing module, and this tutorial runs a four-table SQL query.

{% tabs %}
{% tab title="Apache Ignite 2" %}

{% code title="star-schema/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>star-schema</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>8</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.star.ReportQuery</exec.mainClass>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.apache.ignite</groupId>
            <artifactId>ignite-core</artifactId>
            <version>2.16.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.ignite</groupId>
            <artifactId>ignite-indexing</artifactId>
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

{% code title="star-schema/pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>star-schema</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>8</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.star.ReportQuery</exec.mainClass>
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

The client-side connection config matches the previous tutorials.

{% code title="star-schema/src/main/java/com/example/star/ClientConfig.java" %}
```java
package com.example.star;

import java.util.Arrays;

import org.apache.ignite.configuration.IgniteConfiguration;
import org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi;
import org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder;

/**
 * Thick-client boilerplate. Same shape as the previous tutorial.
 * Peer class loading is not required for this tutorial (no compute
 * closures). Leaving it enabled matches the server configuration.
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

The fact-side value objects carry the fields the SQL query needs. Customer has one foreign key to Country. Invoice has two foreign keys, one to Genre and one to MediaType. The `@QuerySqlField` annotations publish the fields to the SQL engine so the JOINs can reference them by name.

{% code title="star-schema/src/main/java/com/example/star/Customer.java" %}
```java
package com.example.star;

import java.io.Serializable;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

/**
 * Fact-side customer. countryCode joins to the Country dimension.
 */
public class Customer implements Serializable {
    private static final long serialVersionUID = 1L;

    @QuerySqlField(index = true)
    private Integer id;

    @QuerySqlField
    private String name;

    // Foreign key to the Country dimension. Indexed so the
    // fact-dimension join uses an index lookup.
    @QuerySqlField(index = true)
    private String countryCode;

    public Customer() {
    }

    public Customer(Integer id, String name, String countryCode) {
        this.id = id;
        this.name = name;
        this.countryCode = countryCode;
    }

    public Integer getId() { return id; }
    public String getName() { return name; }
    public String getCountryCode() { return countryCode; }
}
```
{% endcode %}

{% code title="star-schema/src/main/java/com/example/star/Invoice.java" %}
```java
package com.example.star;

import java.io.Serializable;
import java.math.BigDecimal;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

/**
 * Fact-side invoice. total drives the revenue aggregation. genreCode
 * and mediaTypeCode join to the Genre and MediaType dimensions.
 */
public class Invoice implements Serializable {
    private static final long serialVersionUID = 1L;

    @QuerySqlField(index = true)
    private Integer invoiceId;

    @QuerySqlField(index = true)
    private Integer customerId;

    @QuerySqlField
    private BigDecimal total;

    @QuerySqlField(index = true)
    private String genreCode;

    @QuerySqlField(index = true)
    private String mediaTypeCode;

    public Invoice() {
    }

    public Invoice(Integer invoiceId, Integer customerId, BigDecimal total,
                   String genreCode, String mediaTypeCode) {
        this.invoiceId = invoiceId;
        this.customerId = customerId;
        this.total = total;
        this.genreCode = genreCode;
        this.mediaTypeCode = mediaTypeCode;
    }

    public Integer getInvoiceId() { return invoiceId; }
    public Integer getCustomerId() { return customerId; }
    public BigDecimal getTotal() { return total; }
    public String getGenreCode() { return genreCode; }
    public String getMediaTypeCode() { return mediaTypeCode; }
}
```
{% endcode %}

{% code title="star-schema/src/main/java/com/example/star/InvoiceKey.java" %}
```java
package com.example.star;

import java.io.Serializable;
import java.util.Objects;

import org.apache.ignite.cache.affinity.AffinityKeyMapped;

/**
 * Composite key for the Invoice cache in Versions B and C. customerId
 * carries the colocation contract. @AffinityKeyMapped tells Ignite to
 * hash only on customerId when picking a partition, placing every
 * invoice on the same primary node as its customer.
 *
 * Version A uses a plain Integer key for the Invoice cache instead of
 * this class. Invoice entries are not colocated with their Customer,
 * so the fact-fact JOIN has to shuffle.
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

The dimension value objects are two-field POJOs. They look almost identical. Each has a code (the primary key) and a human-readable name.

{% code title="star-schema/src/main/java/com/example/star/Country.java" %}
```java
package com.example.star;

import java.io.Serializable;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

/**
 * Dimension table. ~30 rows. Read frequently, written rarely.
 * The candidate for CacheMode.REPLICATED in Version C.
 */
public class Country implements Serializable {
    private static final long serialVersionUID = 1L;

    @QuerySqlField(index = true)
    private String code;

    @QuerySqlField
    private String name;

    public Country() {
    }

    public Country(String code, String name) {
        this.code = code;
        this.name = name;
    }

    public String getCode() { return code; }
    public String getName() { return name; }
}
```
{% endcode %}

`Genre.java` and `MediaType.java` follow the same shape. Save all three value classes and the `Dimensions.java` utility below in the same directory.

<details>
<summary>Show Genre.java, MediaType.java, and Dimensions.java</summary>

{% code title="star-schema/src/main/java/com/example/star/Genre.java" %}
```java
package com.example.star;

import java.io.Serializable;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

/** Dimension table. 10 rows. REPLICATED in Version C. */
public class Genre implements Serializable {
    private static final long serialVersionUID = 1L;

    @QuerySqlField(index = true)
    private String code;

    @QuerySqlField
    private String name;

    public Genre() {}
    public Genre(String code, String name) { this.code = code; this.name = name; }
    public String getCode() { return code; }
    public String getName() { return name; }
}
```
{% endcode %}

{% code title="star-schema/src/main/java/com/example/star/MediaType.java" %}
```java
package com.example.star;

import java.io.Serializable;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

/** Dimension table. 5 rows. REPLICATED in Version C. */
public class MediaType implements Serializable {
    private static final long serialVersionUID = 1L;

    @QuerySqlField(index = true)
    private String code;

    @QuerySqlField
    private String name;

    public MediaType() {}
    public MediaType(String code, String name) { this.code = code; this.name = name; }
    public String getCode() { return code; }
    public String getName() { return name; }
}
```
{% endcode %}

{% code title="star-schema/src/main/java/com/example/star/Dimensions.java" %}
```java
package com.example.star;

import java.util.Arrays;
import java.util.List;

/**
 * Static sample data for the three dimension tables. Sizes match the
 * "small enough to replicate" range the decision framework names:
 * Country ~30 rows, Genre 10 rows, MediaType 5 rows.
 */
final class Dimensions {

    static final List<Country> COUNTRIES = Arrays.asList(
        new Country("US", "United States"),  new Country("CA", "Canada"),
        new Country("MX", "Mexico"),         new Country("GB", "United Kingdom"),
        new Country("DE", "Germany"),        new Country("FR", "France"),
        new Country("ES", "Spain"),          new Country("IT", "Italy"),
        new Country("NL", "Netherlands"),    new Country("PL", "Poland"),
        new Country("SE", "Sweden"),         new Country("NO", "Norway"),
        new Country("FI", "Finland"),        new Country("DK", "Denmark"),
        new Country("AT", "Austria"),        new Country("CH", "Switzerland"),
        new Country("IE", "Ireland"),        new Country("PT", "Portugal"),
        new Country("BR", "Brazil"),         new Country("AR", "Argentina"),
        new Country("CL", "Chile"),          new Country("JP", "Japan"),
        new Country("KR", "Korea"),          new Country("CN", "China"),
        new Country("IN", "India"),          new Country("AU", "Australia"),
        new Country("NZ", "New Zealand"),    new Country("ZA", "South Africa"),
        new Country("EG", "Egypt"),          new Country("IL", "Israel")
    );

    static final List<Genre> GENRES = Arrays.asList(
        new Genre("ROCK", "Rock"),    new Genre("POP", "Pop"),
        new Genre("JAZZ", "Jazz"),    new Genre("CLASS", "Classical"),
        new Genre("HIP", "Hip-Hop"),  new Genre("COUN", "Country"),
        new Genre("ELEC", "Electronic"), new Genre("METL", "Metal"),
        new Genre("FOLK", "Folk"),    new Genre("RNB", "R&B")
    );

    static final List<MediaType> MEDIA_TYPES = Arrays.asList(
        new MediaType("MP3", "MP3 Audio"),   new MediaType("AAC", "AAC Audio"),
        new MediaType("FLAC", "FLAC Lossless"), new MediaType("WAV", "WAV Uncompressed"),
        new MediaType("STRM", "Streaming")
    );

    private Dimensions() {
    }
}
```
{% endcode %}

</details>

{% hint style="success" %}
**Checkpoint:** The project compiles with `mvn -f star-schema/pom.xml compile`. Eight source files turn into `target/classes` with no errors (`ClientConfig`, `Customer`, `Invoice`, `InvoiceKey`, `Country`, `Genre`, `MediaType`, `Dimensions`).
{% endhint %}

## Three Cache Configurations, One Factory Class

Each of the three versions uses five caches: Customer, Invoice, Country, Genre, MediaType. Across versions, the cache names are suffixed with `_a`, `_b`, or `_c`. The configurations differ in two dimensions:

- **Invoice key.** Composite `InvoiceKey` for colocation with Customer, or plain `Integer` for no colocation.
- **Dimension cache mode.** `CacheMode.PARTITIONED` or `CacheMode.REPLICATED`.

{% code title="star-schema/src/main/java/com/example/star/CacheConfigs.java" %}
```java
package com.example.star;

import java.util.Arrays;
import java.util.List;

import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.QueryEntity;
import org.apache.ignite.cache.QueryIndex;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;
import org.apache.ignite.configuration.CacheConfiguration;

/**
 * Produces cache configurations for the three schema versions.
 *
 * Version A: all PARTITIONED, no colocation. Invoice uses Integer key.
 * Fact-fact and fact-dimension JOINs both need setDistributedJoins(true).
 *
 * Version B: all PARTITIONED. Invoice uses InvoiceKey with
 * @AffinityKeyMapped so fact-fact is colocated. Dimensions stay
 * PARTITIONED, so fact-dimension JOINs still need
 * setDistributedJoins(true).
 *
 * Version C: facts PARTITIONED with colocation, dimensions REPLICATED.
 * Fact-dimension JOINs read dimension rows from local memory on every
 * node and do not shuffle across the network.
 */
final class CacheConfigs {

    static final int PARTITIONS = 32;
    static final int BACKUPS = 1;

    // Version A: no colocation, Integer key for Invoice.
    static CacheConfiguration<Integer, Customer> customersA() {
        return partitionedCustomers("customers_a");
    }

    static CacheConfiguration<Integer, Invoice> invoicesA() {
        CacheConfiguration<Integer, Invoice> c = new CacheConfiguration<>("invoices_a");
        c.setCacheMode(CacheMode.PARTITIONED);
        c.setBackups(BACKUPS);
        c.setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));
        c.setQueryEntities(Arrays.asList(invoiceEntity("invoices_a", Integer.class)));
        return c;
    }

    static CacheConfiguration<String, Country> countriesA() {
        return partitioned("countries_a", Country.class, countryEntity("countries_a"));
    }

    static CacheConfiguration<String, Genre> genresA() {
        return partitioned("genres_a", Genre.class, genreEntity("genres_a"));
    }

    static CacheConfiguration<String, MediaType> mediaTypesA() {
        return partitioned("mediatypes_a", MediaType.class, mediaTypeEntity("mediatypes_a"));
    }

    // Version B: Invoice uses InvoiceKey for @AffinityKeyMapped
    // colocation with Customer. Dimensions stay PARTITIONED.
    static CacheConfiguration<Integer, Customer> customersB() {
        return partitionedCustomers("customers_b");
    }

    static CacheConfiguration<InvoiceKey, Invoice> invoicesB() {
        CacheConfiguration<InvoiceKey, Invoice> c = new CacheConfiguration<>("invoices_b");
        c.setCacheMode(CacheMode.PARTITIONED);
        c.setBackups(BACKUPS);
        c.setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));
        c.setQueryEntities(Arrays.asList(invoiceEntity("invoices_b", InvoiceKey.class)));
        return c;
    }

    static CacheConfiguration<String, Country> countriesB() {
        return partitioned("countries_b", Country.class, countryEntity("countries_b"));
    }

    static CacheConfiguration<String, Genre> genresB() {
        return partitioned("genres_b", Genre.class, genreEntity("genres_b"));
    }

    static CacheConfiguration<String, MediaType> mediaTypesB() {
        return partitioned("mediatypes_b", MediaType.class, mediaTypeEntity("mediatypes_b"));
    }

    // Version C: Invoice colocated, dimensions REPLICATED.
    static CacheConfiguration<Integer, Customer> customersC() {
        return partitionedCustomers("customers_c");
    }

    static CacheConfiguration<InvoiceKey, Invoice> invoicesC() {
        CacheConfiguration<InvoiceKey, Invoice> c = new CacheConfiguration<>("invoices_c");
        c.setCacheMode(CacheMode.PARTITIONED);
        c.setBackups(BACKUPS);
        c.setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));
        c.setQueryEntities(Arrays.asList(invoiceEntity("invoices_c", InvoiceKey.class)));
        return c;
    }

    // Version C switches Country, Genre, and MediaType to
    // CacheMode.REPLICATED. Every node holds a full copy of each
    // dimension table. This is the key difference between the
    // three schema versions.
    static CacheConfiguration<String, Country> countriesC() {
        return replicated("countries_c", Country.class, countryEntity("countries_c"));
    }

    static CacheConfiguration<String, Genre> genresC() {
        return replicated("genres_c", Genre.class, genreEntity("genres_c"));
    }

    static CacheConfiguration<String, MediaType> mediaTypesC() {
        return replicated("mediatypes_c", MediaType.class, mediaTypeEntity("mediatypes_c"));
    }

    // Helpers below: partitionedCustomers, partitioned, replicated, and
    // the QueryEntity builders. The per-version decisions are in the
    // methods above.

    private static CacheConfiguration<Integer, Customer> partitionedCustomers(String name) {
        CacheConfiguration<Integer, Customer> c = new CacheConfiguration<>(name);
        c.setCacheMode(CacheMode.PARTITIONED);
        c.setBackups(BACKUPS);
        c.setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));
        c.setQueryEntities(Arrays.asList(customerEntity(name)));
        return c;
    }

    private static <K, V> CacheConfiguration<K, V> partitioned(
            String name, Class<V> valueType, QueryEntity entity) {
        CacheConfiguration<K, V> c = new CacheConfiguration<>(name);
        c.setCacheMode(CacheMode.PARTITIONED);
        c.setBackups(BACKUPS);
        c.setAffinity(new RendezvousAffinityFunction(false, PARTITIONS));
        c.setQueryEntities(Arrays.asList(entity));
        return c;
    }

    private static <K, V> CacheConfiguration<K, V> replicated(
            String name, Class<V> valueType, QueryEntity entity) {
        CacheConfiguration<K, V> c = new CacheConfiguration<>(name);
        c.setCacheMode(CacheMode.REPLICATED);
        // Backups are irrelevant for REPLICATED. Every node already
        // has a full copy, and Ignite ignores this setting.
        c.setQueryEntities(Arrays.asList(entity));
        return c;
    }

    private static QueryEntity customerEntity(String tableName) {
        QueryEntity q = new QueryEntity(Integer.class, Customer.class);
        q.setTableName("Customer_" + suffix(tableName));
        q.addQueryField("id", "java.lang.Integer", null);
        q.addQueryField("name", "java.lang.String", null);
        q.addQueryField("countryCode", "java.lang.String", null);
        q.setIndexes(Arrays.asList(new QueryIndex("id"), new QueryIndex("countryCode")));
        return q;
    }

    private static QueryEntity invoiceEntity(String tableName, Class<?> keyType) {
        QueryEntity q = new QueryEntity(keyType, Invoice.class);
        q.setTableName("Invoice_" + suffix(tableName));
        q.addQueryField("invoiceId", "java.lang.Integer", null);
        q.addQueryField("customerId", "java.lang.Integer", null);
        q.addQueryField("total", "java.math.BigDecimal", null);
        q.addQueryField("genreCode", "java.lang.String", null);
        q.addQueryField("mediaTypeCode", "java.lang.String", null);
        q.setIndexes(Arrays.asList(
            new QueryIndex("invoiceId"), new QueryIndex("customerId"),
            new QueryIndex("genreCode"), new QueryIndex("mediaTypeCode")));
        return q;
    }

    private static QueryEntity countryEntity(String tableName) {
        QueryEntity q = new QueryEntity(String.class, Country.class);
        q.setTableName("Country_" + suffix(tableName));
        q.addQueryField("code", "java.lang.String", null);
        q.addQueryField("name", "java.lang.String", null);
        q.setIndexes(Arrays.asList(new QueryIndex("code")));
        return q;
    }

    private static QueryEntity genreEntity(String tableName) {
        QueryEntity q = new QueryEntity(String.class, Genre.class);
        q.setTableName("Genre_" + suffix(tableName));
        q.addQueryField("code", "java.lang.String", null);
        q.addQueryField("name", "java.lang.String", null);
        q.setIndexes(Arrays.asList(new QueryIndex("code")));
        return q;
    }

    private static QueryEntity mediaTypeEntity(String tableName) {
        QueryEntity q = new QueryEntity(String.class, MediaType.class);
        q.setTableName("MediaType_" + suffix(tableName));
        q.addQueryField("code", "java.lang.String", null);
        q.addQueryField("name", "java.lang.String", null);
        q.setIndexes(Arrays.asList(new QueryIndex("code")));
        return q;
    }

    private static String suffix(String cacheName) {
        int idx = cacheName.lastIndexOf('_');
        return cacheName.substring(idx + 1).toUpperCase();
    }

    static List<String> namesForVersion(String version) {
        return Arrays.asList(
            "customers_" + version, "invoices_" + version,
            "countries_" + version, "genres_" + version, "mediatypes_" + version);
    }

    private CacheConfigs() {
    }
}
```
{% endcode %}

The table-name suffix (`Customer_A`, `Customer_B`, `Customer_C`) keeps the three versions' SQL tables in separate namespaces so the report query can name exactly one version at a time without collision.

The data loader seeds one version's caches at a time. It reads the dimension rows from `Dimensions`, then streams 10,000 customers and 30,000 invoices into the fact caches. Customer country codes distribute round-robin across the 30 countries. Invoice genre and media-type codes distribute uniformly across their dimensions. Revenue is deterministic so the report query produces the same top-10 numbers across versions and runs.

{% code title="star-schema/src/main/java/com/example/star/DataLoader.java" %}
```java
package com.example.star;

import java.math.BigDecimal;
import java.util.Random;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.IgniteDataStreamer;

/**
 * Seeds the five caches for one schema version. The version argument
 * ("a", "b", or "c") selects cache names and picks between the
 * Integer-key and InvoiceKey-composite Invoice loaders.
 */
final class DataLoader {

    static void load(Ignite ignite, String version, int customerCount) {
        IgniteCache<Integer, Customer> customers = ignite.cache("customers_" + version);
        IgniteCache<String, Country> countries = ignite.cache("countries_" + version);
        IgniteCache<String, Genre> genres = ignite.cache("genres_" + version);
        IgniteCache<String, MediaType> mediaTypes = ignite.cache("mediatypes_" + version);

        for (Country c : Dimensions.COUNTRIES) countries.put(c.getCode(), c);
        for (Genre g : Dimensions.GENRES) genres.put(g.getCode(), g);
        for (MediaType m : Dimensions.MEDIA_TYPES) mediaTypes.put(m.getCode(), m);

        String[] countryCodes = Dimensions.COUNTRIES.stream()
            .map(Country::getCode).toArray(String[]::new);
        String[] genreCodes = Dimensions.GENRES.stream()
            .map(Genre::getCode).toArray(String[]::new);
        String[] mediaCodes = Dimensions.MEDIA_TYPES.stream()
            .map(MediaType::getCode).toArray(String[]::new);

        long t0 = System.currentTimeMillis();

        try (IgniteDataStreamer<Integer, Customer> cs =
                 ignite.dataStreamer("customers_" + version)) {
            cs.allowOverwrite(true);
            for (int id = 1; id <= customerCount; id++) {
                String cc = countryCodes[id % countryCodes.length];
                cs.addData(id, new Customer(id, "Customer-" + id, cc));
            }
        }

        if ("a".equals(version)) {
            loadInvoicesIntegerKey(ignite, version, customerCount, genreCodes, mediaCodes);
        } else {
            loadInvoicesCompositeKey(ignite, version, customerCount, genreCodes, mediaCodes);
        }

        long t1 = System.currentTimeMillis();
        System.out.printf("  Version %s loaded: %d customers + %d invoices + %d dimensions in %d ms%n",
            version.toUpperCase(), customerCount, customerCount * 3,
            countries.size() + genres.size() + mediaTypes.size(), (t1 - t0));
    }

    private static void loadInvoicesIntegerKey(Ignite ignite, String version, int customerCount,
                                               String[] genreCodes, String[] mediaCodes) {
        try (IgniteDataStreamer<Integer, Invoice> is =
                 ignite.dataStreamer("invoices_" + version)) {
            is.allowOverwrite(true);
            for (int c = 1; c <= customerCount; c++) {
                for (int s = 1; s <= 3; s++) {
                    int invoiceId = c * 10 + s;
                    String g = genreCodes[(c * 7 + s) % genreCodes.length];
                    String m = mediaCodes[(c * 3 + s) % mediaCodes.length];
                    is.addData(invoiceId, new Invoice(invoiceId, c, revenue(c, s), g, m));
                }
            }
        }
    }

    private static void loadInvoicesCompositeKey(Ignite ignite, String version, int customerCount,
                                                 String[] genreCodes, String[] mediaCodes) {
        try (IgniteDataStreamer<InvoiceKey, Invoice> is =
                 ignite.dataStreamer("invoices_" + version)) {
            is.allowOverwrite(true);
            for (int c = 1; c <= customerCount; c++) {
                for (int s = 1; s <= 3; s++) {
                    int invoiceId = c * 10 + s;
                    String g = genreCodes[(c * 7 + s) % genreCodes.length];
                    String m = mediaCodes[(c * 3 + s) % mediaCodes.length];
                    is.addData(new InvoiceKey(invoiceId, c),
                        new Invoice(invoiceId, c, revenue(c, s), g, m));
                }
            }
        }
    }

    // Deterministic revenue keyed off (customerId, seq) so the top-10
    // report is stable across versions and across runs.
    private static BigDecimal revenue(int customerId, int seq) {
        Random r = new Random(customerId * 31L + seq);
        return BigDecimal.valueOf(10 + r.nextInt(990));
    }

    private DataLoader() {
    }
}
```
{% endcode %}

{% hint style="success" %}
**Checkpoint:** The project still compiles. Ten source files now (`CacheConfigs` and `DataLoader` joined the eight from the previous checkpoint).
{% endhint %}

## The Report Query and the Three-Version Runner

One class runs all three versions. `ReportQuery` creates each version's caches, loads the data, runs the query, destroys the caches, and moves to the next version. The SQL is identical across versions, and only the table-name suffix changes. Version A's first pass leaves the flag off to reproduce the wrong-answer failure mode. Every other pass turns the flag on.

{% code title="star-schema/src/main/java/com/example/star/ReportQuery.java" %}
```java
package com.example.star;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.query.FieldsQueryCursor;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.configuration.CacheConfiguration;

/**
 * Runs the same star-schema report query against three schema
 * versions in sequence. Prints a comparison table at the end.
 *
 * Version A: all PARTITIONED, no colocation. Runs twice: no flag
 * (shows silent wrong answer) and flag on (correct baseline).
 * Version B: facts colocated, dimensions PARTITIONED. Runs once
 * with the flag.
 * Version C: facts colocated, dimensions REPLICATED. Runs once
 * with the flag.
 *
 * All three correct passes produce the same top-10 revenue rows
 * because the data is the same. The wall-clock numbers differ.
 */
public class ReportQuery {

    private static final int CUSTOMERS = 10_000;

    private static final String REPORT_SQL_TEMPLATE =
        "SELECT co.name AS country, g.name AS genre, SUM(i.total) AS revenue " +
        "FROM \"%s\".%s i " +
        "JOIN \"%s\".%s c ON i.customerId = c.id " +
        "JOIN \"%s\".%s co ON c.countryCode = co.code " +
        "JOIN \"%s\".%s g ON i.genreCode = g.code " +
        "GROUP BY co.name, g.name " +
        "ORDER BY revenue DESC " +
        "LIMIT 10";

    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start(ClientConfig.build())) {
            List<Result> results = new ArrayList<>();

            results.addAll(runVersionA(ignite));
            results.add(runVersionB(ignite));
            results.add(runVersionC(ignite));

            printSummary(results);
        }
    }

    private static List<Result> runVersionA(Ignite ignite) {
        System.out.println();
        System.out.println("=== Version A: all PARTITIONED, no colocation ===");
        createCaches(ignite, Arrays.asList(
            CacheConfigs.customersA(), CacheConfigs.invoicesA(),
            CacheConfigs.countriesA(), CacheConfigs.genresA(), CacheConfigs.mediaTypesA()));
        DataLoader.load(ignite, "a", CUSTOMERS);

        String sql = buildSql("a");
        // Pass 1: no flag. Shows the silent-partial-result failure mode
        // when a multi-cache JOIN runs across PARTITIONED caches whose
        // join key does not match the affinity key.
        Result r1 = runQuery(ignite, sql, false, "A", "no flag");
        // Pass 2: flag on. Correct answer, full shuffle cost.
        Result r2 = runQuery(ignite, sql, true, "A", "flag on");

        destroyCaches(ignite, CacheConfigs.namesForVersion("a"));
        return Arrays.asList(r1, r2);
    }

    private static Result runVersionB(Ignite ignite) {
        System.out.println();
        System.out.println("=== Version B: facts colocated, dimensions PARTITIONED ===");
        createCaches(ignite, Arrays.asList(
            CacheConfigs.customersB(), CacheConfigs.invoicesB(),
            CacheConfigs.countriesB(), CacheConfigs.genresB(), CacheConfigs.mediaTypesB()));
        DataLoader.load(ignite, "b", CUSTOMERS);

        String sql = buildSql("b");
        // The fact-fact JOIN now runs local on each node because Invoice
        // carries @AffinityKeyMapped on customerId. The fact-dimension
        // JOINs still cross PARTITIONED caches with different affinity
        // keys, so the flag is still required for correctness.
        Result r = runQuery(ignite, sql, true, "B", "flag on");
        destroyCaches(ignite, CacheConfigs.namesForVersion("b"));
        return r;
    }

    private static Result runVersionC(Ignite ignite) {
        System.out.println();
        System.out.println("=== Version C: facts colocated, dimensions REPLICATED ===");
        createCaches(ignite, Arrays.asList(
            CacheConfigs.customersC(), CacheConfigs.invoicesC(),
            CacheConfigs.countriesC(), CacheConfigs.genresC(), CacheConfigs.mediaTypesC()));
        DataLoader.load(ignite, "c", CUSTOMERS);

        String sql = buildSql("c");
        // Flag still required. Multi-way JOINs across PARTITIONED caches
        // need setDistributedJoins(true) for correctness even when the
        // dimension tables are REPLICATED. The payoff is in the cost of
        // the flag, not its absence. Fact-dimension JOINs now read
        // dimension rows from local memory instead of shuffling.
        Result r = runQuery(ignite, sql, true, "C", "flag on");
        destroyCaches(ignite, CacheConfigs.namesForVersion("c"));
        return r;
    }

    private static String buildSql(String version) {
        String suffix = version.toUpperCase();
        return String.format(REPORT_SQL_TEMPLATE,
            "invoices_" + version, "Invoice_" + suffix,
            "customers_" + version, "Customer_" + suffix,
            "countries_" + version, "Country_" + suffix,
            "genres_" + version, "Genre_" + suffix);
    }

    private static Result runQuery(Ignite ignite, String sql, boolean distributedJoins,
                                   String version, String flagLabel) {
        String cacheName = "customers_" + version.toLowerCase();
        IgniteCache<?, ?> cache = ignite.cache(cacheName);
        SqlFieldsQuery q = new SqlFieldsQuery(sql).setDistributedJoins(distributedJoins);

        long t0 = System.currentTimeMillis();
        List<List<?>> rows;
        try (FieldsQueryCursor<List<?>> cur = cache.query(q)) {
            rows = cur.getAll();
        }
        long t1 = System.currentTimeMillis();

        BigDecimal topTen = BigDecimal.ZERO;
        System.out.printf("  [%s, %s] returned %d rows in %d ms%n",
            version, flagLabel, rows.size(), (t1 - t0));
        for (List<?> row : rows) {
            BigDecimal rev = (BigDecimal) row.get(2);
            topTen = topTen.add(rev);
            System.out.printf("    %-18s %-12s $%s%n", row.get(0), row.get(1), rev);
        }
        return new Result(version, flagLabel, rows.size(), (t1 - t0), topTen);
    }

    private static void createCaches(Ignite ignite, List<CacheConfiguration<?, ?>> configs) {
        for (CacheConfiguration<?, ?> cfg : configs) {
            ignite.getOrCreateCache(cfg);
        }
    }

    private static void destroyCaches(Ignite ignite, List<String> names) {
        for (String name : names) {
            ignite.destroyCache(name);
        }
    }

    private static void printSummary(List<Result> results) {
        System.out.println();
        System.out.println("=== Summary ===");
        System.out.println();
        System.out.printf("%-24s  %-10s  %-8s  %-10s  %s%n",
            "Version / flag", "rows", "time ms", "top-10 $", "note");
        System.out.println("------------------------------------------------------------------------");
        for (Result r : results) {
            System.out.printf("%-24s  %-10d  %-8d  %-10s  %s%n",
                r.version + " (" + r.flag + ")", r.rowCount, r.wallClockMs,
                r.topTenRevenue.toPlainString(), describe(r));
        }
    }

    // "no flag" on any version of this multi-way join returns partial
    // results on GridGain 8 8.9.32 and Apache Ignite 2 2.16.0. The
    // flag is required for correctness.
    private static String describe(Result r) {
        if ("no flag".equals(r.flag)) {
            return "wrong answer: silent partial results";
        }
        return "correct";
    }

    static final class Result {
        final String version;
        final String flag;
        final int rowCount;
        final long wallClockMs;
        final BigDecimal topTenRevenue;

        Result(String version, String flag, int rowCount, long wallClockMs,
               BigDecimal topTenRevenue) {
            this.version = version;
            this.flag = flag;
            this.rowCount = rowCount;
            this.wallClockMs = wallClockMs;
            this.topTenRevenue = topTenRevenue;
        }
    }
}
```
{% endcode %}

Run the full experiment:

```bash
mvn -f star-schema/pom.xml compile
mvn -f star-schema/pom.xml exec:exec
```

The first run pays startup costs for the DataStreamer client, so the first version's load is slower than the next two. Wall-clock times for the queries vary ±10% across back-to-back runs, but the ordering is stable.

Expected output. Row totals are identical across products because the data generator is deterministic. Wall-clock times differ. Apache Ignite 2 runs the query faster than GridGain 8 on the same hardware. Version A's no-flag wrong-answer sums also differ between products because the SQL engine's partial-aggregation path is planner-dependent.

{% tabs %}
{% tab title="Apache Ignite 2" %}

```text
=== Version A: all PARTITIONED, no colocation ===
  Version A loaded: 10000 customers + 30000 invoices + 45 dimensions in 1032 ms
  [A, no flag] returned 10 rows in 75 ms
    Switzerland        Metal        $35094
    Netherlands        Electronic   $33927
    Brazil             Country      $31938
    Chile              Hip-Hop      $30612
    Poland             Hip-Hop      $30186
    Argentina          Country      $29823
    Italy              Rock         $29712
    Sweden             Classical    $28993
    Mexico             Metal        $28765
    Germany            R&B          $28405
  [A, flag on] returned 10 rows in 300 ms
    United Kingdom     Jazz         $178479
    Italy              Rock         $176791
    Egypt              R&B          $175432
    Argentina          Country      $174776
    Poland             Hip-Hop      $173494
    Sweden             Classical    $173458
    Germany            R&B          $173222
    Argentina          Electronic   $173056
    Australia          Metal        $172986
    Germany            Rock         $172456

=== Version B: facts colocated, dimensions PARTITIONED ===
  Version B loaded: 10000 customers + 30000 invoices + 45 dimensions in 965 ms
  [B, flag on] returned 10 rows in 241 ms
    United Kingdom     Jazz         $178479
    Italy              Rock         $176791
    Egypt              R&B          $175432
    Argentina          Country      $174776
    Poland             Hip-Hop      $173494
    Sweden             Classical    $173458
    Germany            R&B          $173222
    Argentina          Electronic   $173056
    Australia          Metal        $172986
    Germany            Rock         $172456

=== Version C: facts colocated, dimensions REPLICATED ===
  Version C loaded: 10000 customers + 30000 invoices + 45 dimensions in 879 ms
  [C, flag on] returned 10 rows in 163 ms
    United Kingdom     Jazz         $178479
    Italy              Rock         $176791
    Egypt              R&B          $175432
    Argentina          Country      $174776
    Poland             Hip-Hop      $173494
    Sweden             Classical    $173458
    Germany            R&B          $173222
    Argentina          Electronic   $173056
    Australia          Metal        $172986
    Germany            Rock         $172456

=== Summary ===

Version / flag            rows        time ms   top-10 $    note
------------------------------------------------------------------------
A (no flag)               10          75        363564      wrong answer: silent partial results
A (flag on)               10          300       1744150     correct
B (flag on)               10          241       1744150     correct
C (flag on)               10          163       1744150     correct
```

{% endtab %}

{% tab title="GridGain 8" %}

```text
=== Version A: all PARTITIONED, no colocation ===
  Version A loaded: 10000 customers + 30000 invoices + 45 dimensions in 1632 ms
  [A, no flag] returned 10 rows in 103 ms
    Australia          Metal        $46814
    Chile              Classical    $45794
    China              Classical    $43688
    Italy              Pop          $43656
    Mexico             Metal        $43270
    Denmark            Jazz         $42471
    France             Metal        $41786
    Finland            Metal        $41621
    Switzerland        Electronic   $40950
    United Kingdom     Classical    $40624
  [A, flag on] returned 10 rows in 9422 ms
    United Kingdom     Jazz         $178479
    Italy              Rock         $176791
    Egypt              R&B          $175432
    Argentina          Country      $174776
    Poland             Hip-Hop      $173494
    Sweden             Classical    $173458
    Germany            R&B          $173222
    Argentina          Electronic   $173056
    Australia          Metal        $172986
    Germany            Rock         $172456

=== Version B: facts colocated, dimensions PARTITIONED ===
  Version B loaded: 10000 customers + 30000 invoices + 45 dimensions in 824 ms
  [B, flag on] returned 10 rows in 9434 ms
    United Kingdom     Jazz         $178479
    Italy              Rock         $176791
    Egypt              R&B          $175432
    Argentina          Country      $174776
    Poland             Hip-Hop      $173494
    Sweden             Classical    $173458
    Germany            R&B          $173222
    Argentina          Electronic   $173056
    Australia          Metal        $172986
    Germany            Rock         $172456

=== Version C: facts colocated, dimensions REPLICATED ===
  Version C loaded: 10000 customers + 30000 invoices + 45 dimensions in 845 ms
  [C, flag on] returned 10 rows in 3317 ms
    United Kingdom     Jazz         $178479
    Italy              Rock         $176791
    Egypt              R&B          $175432
    Argentina          Country      $174776
    Poland             Hip-Hop      $173494
    Sweden             Classical    $173458
    Germany            R&B          $173222
    Argentina          Electronic   $173056
    Australia          Metal        $172986
    Germany            Rock         $172456

=== Summary ===

Version / flag            rows        time ms   top-10 $    note
------------------------------------------------------------------------
A (no flag)               10          103       430674      wrong answer: silent partial results
A (flag on)               10          9422      1744150     correct
B (flag on)               10          9434      1744150     correct
C (flag on)               10          3317      1744150     correct
```

{% endtab %}

{% endtabs %}

{% hint style="success" %}
**Checkpoint:** Four result rows in the summary. The correct top-10 sum is $1,744,150 on both products. Version A no-flag sums to roughly one-fifth to one-quarter of correct (about one-fifth on Apache Ignite 2 at $363,564 and about one-quarter on GridGain 8 at $430,674). Version C is the fastest correct run on both products: about 1.8x faster than Version A on Apache Ignite 2, and about 2.8x faster on GridGain 8.
{% endhint %}

## Read the Three Versions

**Version A, no flag.** Top-10 revenue cells sit below $50,000 each. Every correct version shows cells around $175,000. The no-flag pass returns a real top-10 sorted correctly, but the underlying sums are wrong. The wall-clock is fast because the query does less work. The SQL engine on each node joins only local primary partitions and does not shuffle rows across the network. The partitioned Country and Genre caches each hold 30 or 10 rows split across three nodes, so any given node's map phase finds only some of the dimension rows it needs. The per-node partial aggregates do not merge into the correct global total.

This is the same failure mode the earlier tutorials called out. PARTITIONED caches joined without colocation and without `setDistributedJoins(true)` return silent partial results. A reader who trusts the output ships the revenue figure in a report and discovers weeks later that half the countries are undercounted.

**Version A, flag on.** Same schema, correct answer. The flag tells the SQL engine to shuffle rows across the network so every JOIN sees the full dataset. Every fact-fact and fact-dimension pair gets a cross-node merge. The dominant cost is the fact-dimension shuffle. Four tables with 30,000 invoice rows, 10,000 customers, and tiny partitioned dimension tables all move over the network to satisfy the query planner. This is the slowest correct design.

**Version B, flag on.** Invoice now colocates with Customer via `@AffinityKeyMapped`, so the fact-fact JOIN runs locally on each node instead of shuffling. The fact-dimension JOINs against partitioned Country, Genre, and MediaType caches still cross the network under the flag. The wall-clock improvement is modest on both products. The fact-fact JOIN was a small share of the total cost, and the fact-dimension shuffle remains the main cost.

**Version C, flag on.** The fact-fact JOIN is still colocated. The dimension caches are now REPLICATED, so every node has a full copy of Country, Genre, and MediaType. The fact-dimension JOINs read dimension rows from local memory, and no dimension row crosses the network. `setDistributedJoins(true)` is still set because the SQL engine requires it for correctness on this query shape, but the flag's cost drops because the dimension rows stopped moving. This is the fastest correct design on both products.

Both products tell the same qualitative story. Version A is the slowest correct run, Version C is the fastest, and the no-flag runs are wrong. The absolute speedup ratio differs by product. On Apache Ignite 2 the query is already cheap at this scale, and Version C runs about 1.8x faster than Version A. On GridGain 8 the base cost is higher, and Version C is about 2.8x faster. The REPLICATED design pays off more on the platform where the shuffle was more expensive.

{% hint style="success" %}
**Checkpoint:** Versions A (flag on), B (flag on), and C (flag on) return identical top-10 rows. Their wall-clock times differ because their schemas give the SQL engine different amounts of work to do.
{% endhint %}

## The "Small Enough" Decision Framework

`CacheMode.REPLICATED` puts every row on every node. That is fast for reads and expensive for writes. A 30-row Country table costs almost nothing to replicate: 30 × number-of-nodes is still tiny. A 30-million-row product catalog would multiply by node count into billions of rows of duplicated memory and amplify every write by three, thirty, or three hundred depending on cluster size.

Three questions decide whether a table should be REPLICATED:

| Question | Answer that favors REPLICATED | Answer that favors PARTITIONED |
|---|---|---|
| Row count | Under ~10,000 rows | Above ~100,000 rows |
| Write rate | Rare (updates per day or per week) | Frequent (updates per second) |
| Access pattern | Joined by many queries | Rarely joined |

Between those extremes, measure. The GridGain 8 cluster used for this tutorial has three nodes, and adding a 10,000-row dimension to REPLICATED costs ~10,000 rows times three nodes of memory. On a 30-node cluster the same cache costs ten times as much memory. Write amplification grows with cluster size. One write to a REPLICATED cache hits every node, so on a 30-node cluster one write becomes thirty writes.

Concrete examples from the dimensions in this tutorial and from real applications:

| Dimension | Row count | Write rate | Decision |
|---|---|---|---|
| ISO country codes | ~30 | Yearly | REPLICATED |
| Music genres | ~10-100 | Quarterly | REPLICATED |
| User roles | ~10-50 | Rare | REPLICATED |
| Feature flags | ~100-500 | Per-release | REPLICATED |
| Product catalog (e-commerce) | 10k-10M | Hourly | PARTITIONED |
| Customer master | 100k-100M | Per-request | PARTITIONED |
| Audit log | grows forever | Per-second | PARTITIONED |

Reference data that changes slowly and participates in many queries is the canonical fit. Frequently-written tables or tables that grow with user activity are not.

**REPLICATED cache startup cost.** A new node joining the cluster must receive the full content of every REPLICATED cache before it can serve reads. On a slow network or with a large REPLICATED cache, node startup stretches from seconds to minutes. Keep REPLICATED caches small enough that the cluster tolerates a node restart within its availability budget.

**Write amplification.** Every write to a REPLICATED cache applies on every node. On a 3-node cluster, one write is three writes. On a 30-node cluster, one write is thirty. A table with even a few writes per second becomes an expensive cache mode choice as cluster size grows.

**Silent partial results without `setDistributedJoins(true)`.** Any multi-table JOIN on this query shape needs the flag for correctness, regardless of whether the dimensions are REPLICATED. The REPLICATED design reduces the cost of the flag, but it does not eliminate the need for it. Production code that runs multi-cache analytical queries should always set the flag, and rely on REPLICATED dimensions to keep its cost manageable.

{% hint style="success" %}
**Checkpoint:** The decision table covers every dimension in the tutorial. Country (30 rows, yearly changes), Genre (10 rows, quarterly), and MediaType (5 rows) all fit the REPLICATED criteria. A 10-million-row product catalog or customer master does not.
{% endhint %}

## What This Means

Four tutorials close the Design for Data Locality arc.

[Design Keys for Colocation](design-keys-for-colocation.md) declared the colocation contract on fact tables. [Verify Colocation Is Working](verify-colocation.md) proved the contract held at runtime. [Affinity-Aware Compute at Scale](affinity-aware-compute.md) ran compute jobs on the nodes that owned the facts. This tutorial closed the loop by showing which tables belong outside the colocation contract.

The schema that results matches what a production cache-centric system looks like: partitioned fact tables with colocation chains where they share keys, replicated dimension tables for reference data, and `setDistributedJoins(true)` on the multi-cache analytical queries that cross the boundary. The reader who built all four tutorials can design that schema end-to-end, verify it at runtime, and reason about its cost under load.

## Summary

`CacheMode.REPLICATED` and `CacheMode.PARTITIONED` are both correct, for different tables. Facts go in PARTITIONED caches with colocation chains declared by `@AffinityKeyMapped` or an equivalent mechanism. Reference tables go in REPLICATED caches when they are small, written rarely, and joined often. The three-version experiment in this tutorial moves a schema through three designs and measures a 1.8x to 2.8x speedup between the naive partitioned-everywhere design and the partitioned-facts plus replicated-dimensions design, depending on whether the reader runs Apache Ignite 2 or GridGain 8.

`SqlFieldsQuery.setDistributedJoins(true)` is the correctness flag for multi-cache JOINs. On GridGain 8 8.9.32 and Apache Ignite 2 2.16.0, the flag is required whenever a query crosses two or more caches whose join keys do not all share an affinity chain. Without it, the query returns silent partial results. The no-flag Version A run in this tutorial returned top-10 revenue rows with totals at roughly one-fifth to one-quarter of correct, a failure mode that looks like a normal result unless the reader sums the numbers against a baseline.

REPLICATED dimensions do not remove the need for the flag. They reduce its cost. Version C runs the same multi-table JOIN 1.8x to 2.8x faster than Version A because the dimension rows live on every node instead of shuffling across the network. The decision framework for REPLICATED is three questions: row count, write rate, access pattern. Tables at the small-and-stable end of all three belong in REPLICATED caches. Tables that fail any one of the three belong in PARTITIONED.

### What's Next

This is the final tutorial in the Design for Data Locality path. Two supporting guides build on it:

- [How to Choose a Partition Count for Your Workload](../../architecture/data-modeling/choose-partition-count.md) covers the tradeoffs between the 32-partition setup used in this path and the 1,024 default, and how the decision shifts as cluster size grows. Opens in a new tab so this tutorial stays in your sidebar.
- [How to Debug a Hot Partition](../../tuning-and-troubleshooting/debug-hot-partition.md) diagnoses the failure mode where one node carries most of the load because an affinity key skews toward one partition. Opens in a new tab.

### Related

- [Design Keys for Colocation](design-keys-for-colocation.md) introduced `@AffinityKeyMapped` and the composite-key mechanism this tutorial reuses for Versions B and C.
- [Verify Colocation Is Working](verify-colocation.md) taught the runtime checks for affinity contracts. Apply them to Version B and Version C to confirm Invoice colocates with Customer as expected.
- [Affinity-Aware Compute at Scale](affinity-aware-compute.md) covered three affinity-aware compute patterns that run against PARTITIONED caches. They compose with REPLICATED dimensions when the compute needs to enrich results.
