---
description: >-
  Build a high-throughput pipeline that streams hundreds of thousands of records with the DataStreamer API, including backpressure handling and multi-table referential integrity.
---

# Stream Data With the Data Streamer API

## Introduction

Every write operation in the previous tutorials used individual `upsert()` calls or SQL `INSERT` statements. Each call is a network round-trip: the client sends one record, waits for the server to acknowledge it, then sends the next. At 59 customers and 2,240 invoice lines, this approach works fine. At 10,000 customers or 500,000 invoice lines, it becomes a bottleneck.

The DataStreamer API replaces that one-at-a-time pattern with a streaming pipeline. Records flow from your application through an internal buffer, get batched into pages, and ship to the cluster in parallel across partitions. The cluster processes pages concurrently while your application continues producing records. The result is throughput measured in tens of thousands of records per second instead of hundreds.

This tutorial builds a commerce data generator that streams Customer, Invoice, and InvoiceLine records into the Music Store tables. The DataStreamer pattern applies to any scenario where individual writes are too slow: bulk data migration, cache warming after restarts, ETL from legacy systems, event ingestion from Kafka, test fixture generation for CI pipelines, and audit trail storage.

## Prerequisites

- **A running 3-node cluster with the Music Store dataset** from [Start Your Local GridGain 9 Development Cluster](../distributed-sql-foundations/start-local-cluster.md)
- **Completed** [Connect a Java Thin Client](../distributed-sql-foundations/connect-java-thin-client.md) (familiarity with `IgniteClient`, `RecordView`, and `Tuple`)
- **Java 17** or later
- **Maven 3.8** or later

<details>
<summary>Returning to these tutorials? Verify your environment.</summary>

Check that the cluster is running and the Music Store data is loaded:

```bash
docker exec gridgain9-node1 /opt/gridgain9cli/bin/gridgain9 sql \
  "SELECT COUNT(*) AS tracks FROM Track;"
```

**Expected result: 3503.** If the query succeeds, your environment is ready.

**If the containers are stopped**, restart them from the directory containing your `docker-compose.yml`:

```bash
docker compose up -d
```

Data persists across restarts. Wait 15-30 seconds for the nodes to rejoin, then re-run the check above.

**If the cluster was destroyed** (`docker compose down`), start the containers and re-initialize:

```bash
docker compose up -d
```

Wait 10 seconds for the nodes to start, then load the license and initialize the cluster:

```bash
LICENSE=$(jq -Rs . gridgain-license.json)
```

```bash
curl -X POST http://localhost:10300/management/v1/cluster/init \
  -H "Content-Type: application/json" \
  -d '{"metaStorageNodes":["node1","node2","node3"],"cmgNodes":[],"clusterName":"my-cluster","license":'"$LICENSE"'}'
```

Download the schema and data files:

* [music-store-schema.sql](../../.gitbook/assets/music-store-schema.sql)
* [music-store-data.sql](../../.gitbook/assets/music-store-data.sql)

Copy the files into the container and load them:

```bash
docker cp music-store-schema.sql gridgain9-node1:/tmp/
docker cp music-store-data.sql gridgain9-node1:/tmp/
docker exec gridgain9-node1 /opt/gridgain9cli/bin/gridgain9 sql --file /tmp/music-store-schema.sql
docker exec gridgain9-node1 /opt/gridgain9cli/bin/gridgain9 sql --file /tmp/music-store-data.sql
```

The schema loader prints "Updated 0 rows" for each DDL statement. The data loader prints row counts per batch. Both commands emit jline reflection warnings that are cosmetic and safe to ignore.

Re-run the check above to verify 3503 tracks are loaded.

</details>

## What You Will Learn

You will build a commerce data generator that streams over 1,000,000 records across three related tables into the Music Store cluster. Along the way you will learn:

- How the DataStreamer API delivers orders-of-magnitude faster writes than individual upserts
- How to configure batch size, parallelism, and flush intervals for throughput
- How to stream parent-child tables in the correct order to maintain referential integrity
- How backpressure works in SubmissionPublisher and when to replace it with a custom Flow.Publisher

## Set Up the Project

Create a new directory called `data-streaming-demo` alongside your earlier tutorial projects. Add the following `pom.xml`:

{% code title="pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>data-streaming-demo</artifactId>
    <version>1.0.0</version>

    <properties>
        <maven.compiler.release>17</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.streaming.UpsertVsStream</exec.mainClass>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>ignite-client</artifactId>
            <!-- Use the latest GridGain 9 version -->
            <version>LATEST_GRIDGAIN_9_VERSION</version>
        </dependency>
    </dependencies>

    <repositories>
        <repository>
            <id>gridgain-external</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.4.1</version>
                <configuration>
                    <mainClass>${exec.mainClass}</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
{% endcode %}

Create the source directory:

```bash
mkdir -p src/main/java/com/example/streaming
```

Verify the project compiles:

```bash
mvn compile
```

The first build downloads the ignite-client dependency. Subsequent builds use the cached artifact:

```
[INFO] BUILD SUCCESS
```

{% hint style="success" %}
**Checkpoint:** Maven prints `BUILD SUCCESS`. If using GridGain 9, the GridGain Nexus repository resolves without authentication errors.
{% endhint %}

## Load Customers With Individual Upserts

Before introducing the DataStreamer, establish a baseline. Load 1,000 synthetic customers using the `upsert()` call from the RecordView tutorial and measure the throughput.

Create `src/main/java/com/example/streaming/UpsertVsStream.java`:

{% code title="UpsertVsStream.java" %}
```java
package com.example.streaming;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.DataStreamerItem;
import org.apache.ignite.table.DataStreamerOptions;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Tuple;
import org.apache.ignite.tx.Transaction;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.SubmissionPublisher;

/**
 * Compares individual upsert() calls against DataStreamer for the same data.
 * The throughput difference demonstrates why DataStreamer exists.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.streaming.UpsertVsStream -q
 */
public class UpsertVsStream {

    // ID offset above Chinook data (59 customers) to prevent collisions
    private static final int CUSTOMER_ID_OFFSET = 100_000;
    private static final int RECORD_COUNT = 1_000;

    private static final String[] FIRST_NAMES = {
        "James", "Mary", "Robert", "Patricia", "John", "Jennifer",
        "Michael", "Linda", "David", "Elizabeth", "William", "Barbara",
        "Carlos", "Maria", "Yuki", "Hans"
    };

    private static final String[] LAST_NAMES = {
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
        "Miller", "Davis", "Rodriguez", "Martinez", "Mueller", "Tanaka",
        "Kumar", "Chen", "Kim", "Johansson"
    };

    private static final String[] COUNTRIES = {
        "USA", "Canada", "Brazil", "United Kingdom", "Germany",
        "France", "Australia", "Japan", "India", "Sweden"
    };

    public static void main(String[] args) throws Exception {
        // Suppress GridGain client partition-assignment logs
        java.util.logging.LogManager.getLogManager().reset();
        java.util.logging.Logger.getLogger("org.apache.ignite")
            .setLevel(java.util.logging.Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800")
                .build()) {

            System.out.println("Connected to cluster");

            // Generate 1,000 synthetic customers in memory
            List<Tuple> customers = generateCustomers(RECORD_COUNT);

            RecordView<Tuple> view = client.tables().table("Customer").recordView();
            var sql = client.sql();

            // Clean up any records from a previous run
            cleanup(sql);

            // ---- Upsert loop: one network round-trip per record ----
            System.out.printf("%nLoading %,d customers with individual upsert() calls...%n",
                RECORD_COUNT);

            long upsertStart = System.currentTimeMillis();
            for (Tuple customer : customers) {
                view.upsert((Transaction) null, customer);
            }
            long upsertElapsed = System.currentTimeMillis() - upsertStart;
            double upsertRate = RECORD_COUNT / (upsertElapsed / 1000.0);

            System.out.printf("Upsert:      %,d rows in %.1fs (%,.0f rows/sec)%n",
                RECORD_COUNT, upsertElapsed / 1000.0, upsertRate);

            // Verify
            System.out.printf("Verified:    %,d rows in Customer table%n", countGenerated(sql));

            // Clean up before the DataStreamer test
            cleanup(sql);

            // ---- DataStreamer: batched, pipelined writes ----
            System.out.printf("%nLoading %,d customers with DataStreamer...%n", RECORD_COUNT);

            long streamStart = System.currentTimeMillis();

            // SubmissionPublisher is Java's built-in Flow.Publisher implementation.
            // It buffers items internally and delivers them to the DataStreamer subscriber.
            SubmissionPublisher<DataStreamerItem<Tuple>> publisher = new SubmissionPublisher<>();

            // streamData connects the publisher to the cluster. It returns a future
            // that completes when all records have been written.
            CompletableFuture<Void> streamFuture = view.streamData(
                publisher, DataStreamerOptions.DEFAULT);

            // Submit each customer wrapped in a DataStreamerItem.
            // DataStreamerItem.of() creates a PUT operation (insert or update).
            for (Tuple customer : customers) {
                publisher.submit(DataStreamerItem.of(customer));
            }

            // close() signals that no more items will be submitted.
            // The DataStreamer flushes any remaining buffered records.
            publisher.close();

            // join() blocks until every record has reached the cluster.
            streamFuture.join();

            long streamElapsed = System.currentTimeMillis() - streamStart;
            double streamRate = RECORD_COUNT / (streamElapsed / 1000.0);

            System.out.printf("DataStreamer: %,d rows in %.1fs (%,.0f rows/sec)%n",
                RECORD_COUNT, streamElapsed / 1000.0, streamRate);

            // Data Streamer writes are committed immediately for key-value access.
            // SQL queries need a brief pause for indexing to catch up.
            Thread.sleep(1500);

            System.out.printf("Verified:    %,d rows in Customer table%n", countGenerated(sql));

            // Summary
            double speedup = (double) upsertElapsed / Math.max(1, streamElapsed);
            System.out.printf("%nDataStreamer was %.0fx faster%n", speedup);

            // Clean up
            cleanup(sql);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }

        System.exit(0);
    }

    /** Generates synthetic customer records with a fixed random seed for reproducibility. */
    static List<Tuple> generateCustomers(int count) {
        Random rng = new Random(42);
        List<Tuple> customers = new ArrayList<>(count);

        for (int i = 0; i < count; i++) {
            int id = CUSTOMER_ID_OFFSET + i;
            String firstName = FIRST_NAMES[rng.nextInt(FIRST_NAMES.length)];
            String lastName = LAST_NAMES[rng.nextInt(LAST_NAMES.length)];
            String country = COUNTRIES[rng.nextInt(COUNTRIES.length)];
            String email = firstName.toLowerCase() + "." + lastName.toLowerCase()
                + id + "@example.com";

            customers.add(Tuple.create()
                .set("CUSTOMERID", id)
                .set("FIRSTNAME", firstName)
                .set("LASTNAME", lastName)
                .set("COUNTRY", country)
                .set("EMAIL", email));
        }

        return customers;
    }

    static void cleanup(org.apache.ignite.sql.IgniteSql sql) {
        sql.execute((Transaction) null,
            "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_ID_OFFSET);
    }

    static long countGenerated(org.apache.ignite.sql.IgniteSql sql) {
        try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                "SELECT COUNT(*) AS CNT FROM Customer WHERE CustomerId >= ?",
                CUSTOMER_ID_OFFSET)) {
            return rs.next().longValue("CNT");
        }
    }
}
```
{% endcode %}

Run the comparison:

```bash
mvn compile exec:java -q
```

**Expected output:**

```
Connected to cluster

Loading 1,000 customers with individual upsert() calls...
Upsert:      1,000 rows in 0.9s (1,124 rows/sec)
Verified:    1,000 rows in Customer table

Loading 1,000 customers with DataStreamer...
DataStreamer: 1,000 rows in 0.0s (50,000 rows/sec)
Verified:    1,000 rows in Customer table

DataStreamer was 45x faster
```

{% hint style="info" %}
Throughput depends on your machine's CPU, Docker resource allocation, and network stack. The absolute numbers matter less than the ratio: DataStreamer should be at least an order of magnitude faster than the upsert loop. On a 3-node Docker cluster, typical upsert throughput is 400-1,400 rows/sec. DataStreamer throughput is 15,000-100,000 rows/sec for the same data.
{% endhint %}

The upsert loop sends one record per network round-trip. At 1,000 records, the round-trip latency dominates. The cluster spends most of its time waiting for the next record. DataStreamer eliminates that wait by batching records into pages. It sends those pages in parallel across partitions, so the cluster processes pages concurrently while your application keeps producing records.

{% hint style="info" %}
Hover over `streamData` in your IDE. The signature shows `Flow.Publisher<DataStreamerItem<T>>` as the first parameter. `SubmissionPublisher` implements `Flow.Publisher`, and `DataStreamerItem.of()` wraps each Tuple. The type chain connects: your Tuple goes into a DataStreamerItem, which goes into a SubmissionPublisher, which feeds `streamData`.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** Both approaches load 1,000 customers with matching verified counts. DataStreamer is at least 10x faster.
{% endhint %}

## Configure DataStreamer Options

The default `DataStreamerOptions` work well for moderate volumes. For higher throughput, four settings control how records flow from your application to the cluster:

| Option | Default | Effect |
|---|---|---|
| `pageSize` | 1,000 | Records batched into one network request. Larger pages mean fewer round-trips but more client memory. |
| `perPartitionParallelOperations` | 1 | Concurrent in-flight requests per partition. Higher values increase throughput but add cluster load. |
| `autoFlushInterval` | 5,000 ms | How often to flush a partial page. Prevents records from waiting in the buffer when the producer is slower than the page size. |
| `retryLimit` | 16 | Automatic retries for failed pages before the stream aborts. Handles transient network issues and primary replica changes. |

Create `src/main/java/com/example/streaming/TunedStreaming.java`:

{% code title="TunedStreaming.java" %}
```java
package com.example.streaming;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.DataStreamerItem;
import org.apache.ignite.table.DataStreamerOptions;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Tuple;
import org.apache.ignite.tx.Transaction;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.SubmissionPublisher;

/**
 * Streams 10,000 customers with tuned DataStreamerOptions and measures throughput.
 * Uses SubmissionPublisher for buffered delivery to the DataStreamer.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.streaming.TunedStreaming -q
 */
public class TunedStreaming {

    static final int CUSTOMER_ID_OFFSET = 100_000;
    private static final int RECORD_COUNT = 10_000;

    public static void main(String[] args) throws Exception {
        java.util.logging.LogManager.getLogManager().reset();
        java.util.logging.Logger.getLogger("org.apache.ignite")
            .setLevel(java.util.logging.Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800")
                .build()) {

            var sql = client.sql();
            RecordView<Tuple> view = client.tables().table("Customer").recordView();

            // Clean up any records from a previous run
            sql.execute((Transaction) null,
                "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_ID_OFFSET);

            // Generate 10,000 synthetic customers
            List<Tuple> customers = generateCustomers(RECORD_COUNT);

            // Tuned options: smaller pages with more parallelism and faster flushing
            DataStreamerOptions options = DataStreamerOptions.builder()
                .pageSize(500)                        // 500 records per network call
                .perPartitionParallelOperations(4)    // 4 concurrent requests per partition
                .autoFlushInterval(1000)              // flush partial pages every second
                .retryLimit(16)                       // retry failed pages up to 16 times
                .build();

            System.out.printf("Streaming %,d customers with tuned options...%n", RECORD_COUNT);
            System.out.println("  pageSize=500, parallelOps=4, autoFlush=1000ms");

            long start = System.currentTimeMillis();
            streamRecords(view, customers, options);
            long elapsed = System.currentTimeMillis() - start;

            System.out.printf("Streamed %,d rows in %.2fs (%,.0f rows/sec)%n",
                RECORD_COUNT, elapsed / 1000.0, RECORD_COUNT / (elapsed / 1000.0));

            // SQL verification
            Thread.sleep(1500);
            long count = countWhere(sql, "Customer", "CustomerId", CUSTOMER_ID_OFFSET);
            System.out.printf("Verified: %,d customers in cluster%n", count);

            // Clean up
            sql.execute((Transaction) null,
                "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_ID_OFFSET);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }

        System.exit(0);
    }

    // --- Reusable streaming method ---

    /** Streams a list of Tuples using SubmissionPublisher. */
    static void streamRecords(RecordView<Tuple> view, List<Tuple> records,
                               DataStreamerOptions options) {
        SubmissionPublisher<DataStreamerItem<Tuple>> publisher = new SubmissionPublisher<>();
        CompletableFuture<Void> future = view.streamData(publisher, options);
        for (Tuple record : records) {
            publisher.submit(DataStreamerItem.of(record));
        }
        publisher.close();
        future.join();
    }

    // --- Data generation ---

    /** Generates customers with a fixed seed (for standalone use). */
    static List<Tuple> generateCustomers(int count) {
        return generateCustomers(count, new Random(42));
    }

    /** Generates customers using a shared Random (for reproducible multi-table pipelines). */
    static List<Tuple> generateCustomers(int count, Random rng) {
        String[] firstNames = {"James", "Mary", "Robert", "Patricia", "John", "Jennifer",
            "Michael", "Linda", "David", "Elizabeth", "William", "Barbara",
            "Carlos", "Maria", "Yuki", "Hans", "Pierre", "Sophie",
            "Raj", "Priya", "Wei", "Mei", "Ahmed", "Fatima"};
        String[] lastNames = {"Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
            "Miller", "Davis", "Rodriguez", "Martinez", "Mueller", "Tanaka",
            "Kumar", "Chen", "Kim", "Johansson", "Silva", "Rossi"};
        String[] countries = {"USA", "Canada", "Brazil", "United Kingdom", "Germany",
            "France", "Australia", "Japan", "India", "Sweden", "Italy", "Spain"};

        List<Tuple> customers = new ArrayList<>(count);

        for (int i = 0; i < count; i++) {
            int id = CUSTOMER_ID_OFFSET + i;
            String first = firstNames[rng.nextInt(firstNames.length)];
            String last = lastNames[rng.nextInt(lastNames.length)];

            customers.add(Tuple.create()
                .set("CUSTOMERID", id)
                .set("FIRSTNAME", first)
                .set("LASTNAME", last)
                .set("COUNTRY", countries[rng.nextInt(countries.length)])
                .set("EMAIL", first.toLowerCase() + "." + last.toLowerCase()
                    + id + "@example.com"));
        }
        return customers;
    }

    static long countWhere(org.apache.ignite.sql.IgniteSql sql, String table,
                           String column, int minValue) {
        try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                "SELECT COUNT(*) AS CNT FROM " + table + " WHERE " + column + " >= ?",
                minValue)) {
            return rs.next().longValue("CNT");
        }
    }
}
```
{% endcode %}

Run the tuned streaming test:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.streaming.TunedStreaming -q
```

**Expected output:**

```
Streaming 10,000 customers with tuned options...
  pageSize=500, parallelOps=4, autoFlush=1000ms
Streamed 10,000 rows in 0.15s (65,359 rows/sec)
Verified: 10,000 customers in cluster
```

{% hint style="info" %}
At 10,000 records, both default and tuned options finish in under a second. The tuning knobs make a bigger difference when streaming hundreds of thousands of records, running multiple streams concurrently, or streaming to a cluster under load. The values used here (pageSize=500, parallelOps=4, autoFlush=1000ms) are a good starting point for most workloads.
{% endhint %}

DataStreamer provides at-least-once delivery. If a page fails and the retry succeeds, but the original page also committed, duplicate records are possible. Because Customer uses `CustomerId` as the primary key, a duplicate upsert overwrites the same row. Applications that stream into append-only tables (event logs, audit trails) should include a unique key for deduplication.

{% hint style="success" %}
**Checkpoint:** 10,000 customers streamed and verified in the cluster.
{% endhint %}

## Stream Invoices With Parent-Child Order

The Music Store schema has a foreign key chain: Customer -> Invoice -> InvoiceLine. When streaming related tables, the parent table must load before its children. If you stream Invoice records that reference a CustomerId before that customer exists, the records will still land (GridGain does not enforce foreign keys at write time), but your verification queries and application logic will encounter orphaned rows.

DataStreamer follows the same constraint: stream parents first, then children.

Create `src/main/java/com/example/streaming/InvoiceStreaming.java`. This class generates Invoice records for 10,000 customers using a Zipf distribution that mimics real e-commerce patterns: most customers place a few orders, but a small percentage account for a large share of the volume.

{% code title="InvoiceStreaming.java" %}
```java
package com.example.streaming;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.DataStreamerItem;
import org.apache.ignite.table.DataStreamerOptions;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Tuple;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Flow;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Streams Customer and Invoice records in parent-child order.
 * Demonstrates multi-table streaming with referential integrity.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.streaming.InvoiceStreaming -q
 */
public class InvoiceStreaming {

    private static final int CUSTOMER_ID_OFFSET = 100_000;
    private static final int INVOICE_ID_OFFSET = 100_000;
    private static final int CUSTOMER_COUNT = 10_000;

    public static void main(String[] args) throws Exception {
        java.util.logging.LogManager.getLogManager().reset();
        java.util.logging.Logger.getLogger("org.apache.ignite")
            .setLevel(java.util.logging.Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800")
                .build()) {

            var sql = client.sql();

            // Clean up from previous runs (children first, then parents)
            sql.execute((Transaction) null,
                "DELETE FROM Invoice WHERE InvoiceId >= ?", INVOICE_ID_OFFSET);
            sql.execute((Transaction) null,
                "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_ID_OFFSET);

            DataStreamerOptions options = DataStreamerOptions.builder()
                .pageSize(500)
                .perPartitionParallelOperations(4)
                .autoFlushInterval(1000)
                .build();

            // ---- Step 1: Stream Customers (parent table) ----
            Random rng = new Random(42);
            List<Tuple> customers = TunedStreaming.generateCustomers(CUSTOMER_COUNT);

            System.out.printf("Streaming %,d customers...%n", customers.size());
            RecordView<Tuple> customerView = client.tables().table("Customer").recordView();

            long custStart = System.currentTimeMillis();
            streamRecords(customerView, customers, options);
            long custElapsed = System.currentTimeMillis() - custStart;

            System.out.printf("  %,d customers in %.1fs%n", customers.size(),
                custElapsed / 1000.0);

            // ---- Step 2: Generate and stream Invoices (child table) ----
            // Each customer gets 1-50 invoices based on a Zipf distribution:
            //   40% casual buyers (1-3 invoices)
            //   30% regular buyers (4-10 invoices)
            //   20% frequent buyers (11-25 invoices)
            //   10% power buyers (26-50 invoices)
            List<Tuple> invoices = generateInvoices(customers, rng);

            System.out.printf("Streaming %,d invoices for %,d customers...%n",
                invoices.size(), CUSTOMER_COUNT);
            RecordView<Tuple> invoiceView = client.tables().table("Invoice").recordView();

            long invStart = System.currentTimeMillis();
            streamRecords(invoiceView, invoices, options);
            long invElapsed = System.currentTimeMillis() - invStart;

            System.out.printf("  %,d invoices in %.1fs (%,.0f rows/sec)%n",
                invoices.size(), invElapsed / 1000.0,
                invoices.size() / (invElapsed / 1000.0));

            // ---- Verify the parent-child relationship ----
            Thread.sleep(1500);

            System.out.println("\nTop 5 customers by invoice count:");
            try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                    "SELECT c.FirstName, c.LastName, COUNT(*) AS InvoiceCount " +
                    "FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId " +
                    "WHERE c.CustomerId >= ? " +
                    "GROUP BY c.CustomerId, c.FirstName, c.LastName " +
                    "ORDER BY InvoiceCount DESC LIMIT 5", CUSTOMER_ID_OFFSET)) {
                while (rs.hasNext()) {
                    SqlRow row = rs.next();
                    System.out.printf("  %s %s: %d invoices%n",
                        row.stringValue("FIRSTNAME"),
                        row.stringValue("LASTNAME"),
                        row.longValue("INVOICECOUNT"));
                }
            }

            // Clean up
            sql.execute((Transaction) null,
                "DELETE FROM Invoice WHERE InvoiceId >= ?", INVOICE_ID_OFFSET);
            sql.execute((Transaction) null,
                "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_ID_OFFSET);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }

        System.exit(0);
    }

    /** Generates invoices for each customer using a Zipf distribution. */
    static List<Tuple> generateInvoices(List<Tuple> customers, Random rng) {
        List<Tuple> invoices = new ArrayList<>();
        int invoiceId = INVOICE_ID_OFFSET;
        LocalDate startDate = LocalDate.of(2024, 1, 1);

        for (Tuple customer : customers) {
            int customerId = customer.intValue("CUSTOMERID");
            String country = customer.stringValue("COUNTRY");

            // Zipf distribution: most customers are casual, few are power buyers
            int invoiceCount = zipfInvoiceCount(rng);

            for (int inv = 0; inv < invoiceCount; inv++) {
                LocalDate date = startDate.plusDays(rng.nextInt(730));
                // Placeholder total; CommerceDataGenerator calculates from line items
                BigDecimal total = new BigDecimal(rng.nextInt(50) + 1)
                    .add(new BigDecimal("0.99"));

                invoices.add(Tuple.create()
                    .set("INVOICEID", invoiceId)
                    .set("CUSTOMERID", customerId)
                    .set("INVOICEDATE", date)
                    .set("BILLINGCOUNTRY", country)
                    .set("TOTAL", total));
                invoiceId++;
            }
        }
        return invoices;
    }

    /**
     * Returns 1-50 invoices per customer following a Zipf-like distribution.
     * This distribution mirrors real e-commerce: a few power buyers generate
     * most of the order volume.
     */
    static int zipfInvoiceCount(Random rng) {
        double r = rng.nextDouble();
        if (r < 0.40) return 1 + rng.nextInt(3);   // 40%: casual (1-3)
        if (r < 0.70) return 4 + rng.nextInt(7);   // 30%: regular (4-10)
        if (r < 0.90) return 11 + rng.nextInt(15);  // 20%: frequent (11-25)
        return 26 + rng.nextInt(25);                 // 10%: power (26-50)
    }

    // Reuse the SubmissionPublisher streaming method from TunedStreaming
    static void streamRecords(RecordView<Tuple> view, List<Tuple> records,
                               DataStreamerOptions options) {
        TunedStreaming.streamRecords(view, records, options);
    }
}
```
{% endcode %}

Run the multi-table streaming test:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.streaming.InvoiceStreaming -q
```

**Expected output:**

```
Streaming 10,000 customers...
  10,000 customers in 0.3s
Streaming 102,893 invoices for 10,000 customers...
  102,893 invoices in 1.3s (80,700 rows/sec)

Top 5 customers by invoice count:
  James Kim: 50 invoices
  Yuki Williams: 50 invoices
  Hans Miller: 50 invoices
  Barbara Chen: 50 invoices
  Patricia Williams: 50 invoices
```

The Zipf distribution produces a realistic spread: power buyers at the top with 50 invoices, casual buyers at the bottom with 1. Your specific customer names will differ (many customers tie at 50 invoices, and the tiebreaker depends on partition assignment), but the invoice count of 50 and the total of ~102,000 invoices are consistent across runs.

The JOIN query proves that every Invoice references a valid Customer. If you reversed the streaming order (invoices before customers), the JOIN would still work (GridGain does not enforce foreign keys), but the data would be logically inconsistent until the parent table loaded.

{% hint style="success" %}
**Checkpoint:** ~100,000 invoices streamed and verified via a Customer-Invoice JOIN. The top-5 query shows power buyers with 50 invoices.
{% endhint %}

## Build the Full Three-Table Pipeline

The final table in the chain is InvoiceLine. Each InvoiceLine references an InvoiceId (from the invoices you just streamed) and a TrackId (from the Chinook catalog already in the cluster). Unlike the Customer-Invoice step, InvoiceLine joins newly streamed data to existing catalog data. The generator loads the Track catalog first so it can select valid TrackIds when generating line items.

Create `src/main/java/com/example/streaming/CommerceDataGenerator.java`:

{% code title="CommerceDataGenerator.java" %}
```java
package com.example.streaming;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.DataStreamerItem;
import org.apache.ignite.table.DataStreamerOptions;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Tuple;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CompletableFuture;

/**
 * Full three-table commerce data generator using the DataStreamer API.
 * Streams Customer, Invoice, and InvoiceLine with referential integrity
 * and realistic data distributions.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.streaming.CommerceDataGenerator -q
 */
public class CommerceDataGenerator {

    private static final int CUSTOMER_OFFSET = 100_000;
    private static final int INVOICE_OFFSET = 100_000;
    private static final int INVOICELINE_OFFSET = 1_000_000;
    private static final int CUSTOMER_COUNT = 15_000;

    public static void main(String[] args) throws Exception {
        java.util.logging.LogManager.getLogManager().reset();
        java.util.logging.Logger.getLogger("org.apache.ignite")
            .setLevel(java.util.logging.Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800")
                .build()) {

            var sql = client.sql();
            System.out.println("=== Commerce Data Generator");

            // Clean up from previous runs (children first)
            cleanup(sql);

            // Load the Track catalog for InvoiceLine cross-references.
            // InvoiceLines reference TrackIds from the existing Chinook dataset,
            // not from streamed data. The generator must know which TrackIds
            // are valid before generating line items.
            System.out.print("Loading catalog TrackIds... ");
            List<Integer> trackIds = loadTrackIds(sql);
            System.out.printf("%,d tracks%n", trackIds.size());

            // ---- Phase 1: Generate all records in memory ----
            // Generating everything first lets the generator calculate accurate
            // invoice totals (sum of line items) and maintain sequential IDs
            // without interleaving with network I/O.
            System.out.print("Generating records... ");
            long genStart = System.currentTimeMillis();
            // Single Random instance shared across all generation so the
            // fixed seed (42) produces identical data on every run.
            Random rng = new Random(42);

            List<Tuple> customers = TunedStreaming.generateCustomers(CUSTOMER_COUNT, rng);
            List<Tuple> invoices = new ArrayList<>();
            List<Tuple> invoiceLines = new ArrayList<>();
            generateCommerceData(customers, invoices, invoiceLines, trackIds, rng);

            long genElapsed = System.currentTimeMillis() - genStart;
            int totalRows = customers.size() + invoices.size() + invoiceLines.size();
            System.out.printf("%,d records (%.1fs)%n", totalRows, genElapsed / 1000.0);
            System.out.printf("  %,d customers, %,d invoices, %,d invoice lines%n",
                customers.size(), invoices.size(), invoiceLines.size());

            // ---- Phase 2: Stream tables in parent-child order ----
            DataStreamerOptions options = DataStreamerOptions.builder()
                .pageSize(500)
                .perPartitionParallelOperations(4)
                .autoFlushInterval(1000)
                .build();

            System.out.println("Streaming to cluster...");
            long streamStart = System.currentTimeMillis();

            long custTime = streamTable(client, "Customer", customers, options);
            System.out.printf("  Customer:    %,10d rows (%.1fs)%n",
                customers.size(), custTime / 1000.0);

            long invTime = streamTable(client, "Invoice", invoices, options);
            System.out.printf("  Invoice:     %,10d rows (%.1fs)%n",
                invoices.size(), invTime / 1000.0);

            long lineTime = streamTable(client, "InvoiceLine", invoiceLines, options);
            System.out.printf("  InvoiceLine: %,10d rows (%.1fs)%n",
                invoiceLines.size(), lineTime / 1000.0);

            long streamElapsed = System.currentTimeMillis() - streamStart;
            double rowsPerSec = totalRows / (streamElapsed / 1000.0);
            System.out.printf("Streamed %,d rows in %.1f seconds (%,.0f rows/sec)%n",
                totalRows, streamElapsed / 1000.0, rowsPerSec);

            // ---- Verify data integrity ----
            Thread.sleep(2000);
            System.out.println("\nVerification:");

            long custCount = countWhere(sql, "Customer", "CustomerId", CUSTOMER_OFFSET);
            long invCount = countWhere(sql, "Invoice", "InvoiceId", INVOICE_OFFSET);
            long lineCount2 = countWhere(sql, "InvoiceLine", "InvoiceLineId",
                INVOICELINE_OFFSET);
            System.out.printf("  Customer:    %,d rows%n", custCount);
            System.out.printf("  Invoice:     %,d rows%n", invCount);
            System.out.printf("  InvoiceLine: %,d rows%n", lineCount2);

            // Cross-table JOIN: Customer -> Invoice -> InvoiceLine -> Track
            // This proves referential integrity across all three streamed tables
            // and the existing Chinook catalog.
            System.out.println("\nCross-table JOIN (Customer -> Invoice -> InvoiceLine -> Track):");
            try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                    "SELECT c.FirstName, c.LastName, i.InvoiceDate, " +
                    "t.Name AS TrackName, il.UnitPrice, il.Quantity " +
                    "FROM Customer c " +
                    "JOIN Invoice i ON c.CustomerId = i.CustomerId " +
                    "JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId " +
                    "JOIN Track t ON il.TrackId = t.TrackId " +
                    "WHERE c.CustomerId >= ? " +
                    "ORDER BY c.LastName, c.FirstName, i.InvoiceDate " +
                    "LIMIT 5", CUSTOMER_OFFSET)) {
                while (rs.hasNext()) {
                    SqlRow row = rs.next();
                    System.out.printf("  %s %s | %s | %s | $%s x%d%n",
                        row.stringValue("FIRSTNAME"),
                        row.stringValue("LASTNAME"),
                        row.dateValue("INVOICEDATE"),
                        row.stringValue("TRACKNAME"),
                        row.value("UNITPRICE"),
                        row.intValue("QUANTITY"));
                }
            }

            // Clean up
            cleanup(sql);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }

        System.exit(0);
    }

    /**
     * Generates all commerce records (invoices + invoice lines) for a list
     * of customers. Reusable by other classes that need the same dataset.
     */
    static void generateCommerceData(List<Tuple> customers, List<Tuple> invoices,
                                      List<Tuple> invoiceLines,
                                      List<Integer> trackIds, Random rng) {
        int invoiceId = INVOICE_OFFSET;
        int invoiceLineId = INVOICELINE_OFFSET;
        LocalDate startDate = LocalDate.of(2024, 1, 1);

        for (Tuple customer : customers) {
            int customerId = customer.intValue("CUSTOMERID");
            String country = customer.stringValue("COUNTRY");
            int invoiceCount = InvoiceStreaming.zipfInvoiceCount(rng);

            for (int inv = 0; inv < invoiceCount; inv++) {
                LocalDate date = startDate.plusDays(rng.nextInt(730));
                int lineCount = 1 + rng.nextInt(10);
                BigDecimal total = BigDecimal.ZERO;

                for (int ln = 0; ln < lineCount; ln++) {
                    BigDecimal price = new BigDecimal("0.99");
                    int qty = 1 + rng.nextInt(3);
                    int trackId = trackIds.get(rng.nextInt(trackIds.size()));

                    invoiceLines.add(Tuple.create()
                        .set("INVOICELINEID", invoiceLineId)
                        .set("INVOICEID", invoiceId)
                        .set("TRACKID", trackId)
                        .set("UNITPRICE", price)
                        .set("QUANTITY", qty));

                    total = total.add(price.multiply(BigDecimal.valueOf(qty)));
                    invoiceLineId++;
                }

                invoices.add(Tuple.create()
                    .set("INVOICEID", invoiceId)
                    .set("CUSTOMERID", customerId)
                    .set("INVOICEDATE", date)
                    .set("BILLINGCOUNTRY", country)
                    .set("TOTAL", total));
                invoiceId++;
            }
        }
    }

    static List<Integer> loadTrackIds(org.apache.ignite.sql.IgniteSql sql) {
        List<Integer> ids = new ArrayList<>();
        try (ResultSet<SqlRow> rs = sql.execute(
                (Transaction) null, "SELECT TrackId FROM Track")) {
            while (rs.hasNext()) {
                ids.add(rs.next().intValue("TRACKID"));
            }
        }
        return ids;
    }

    static long streamTable(IgniteClient client, String tableName,
                             List<Tuple> records, DataStreamerOptions options) {
        RecordView<Tuple> view = client.tables().table(tableName).recordView();
        long start = System.currentTimeMillis();
        TunedStreaming.streamRecords(view, records, options);
        return System.currentTimeMillis() - start;
    }

    static long countWhere(org.apache.ignite.sql.IgniteSql sql, String table,
                           String column, int minValue) {
        try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                "SELECT COUNT(*) AS CNT FROM " + table + " WHERE " + column + " >= ?",
                minValue)) {
            return rs.next().longValue("CNT");
        }
    }

    static void cleanup(org.apache.ignite.sql.IgniteSql sql) {
        // Delete children before parents
        sql.execute((Transaction) null,
            "DELETE FROM InvoiceLine WHERE InvoiceLineId >= ?", INVOICELINE_OFFSET);
        sql.execute((Transaction) null,
            "DELETE FROM Invoice WHERE InvoiceId >= ?", INVOICE_OFFSET);
        sql.execute((Transaction) null,
            "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_OFFSET);
    }
}
```
{% endcode %}

Run the full pipeline:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.streaming.CommerceDataGenerator -q
```

**Expected output:**

```
=== Commerce Data Generator
Loading catalog TrackIds... 3,503 tracks
Generating records... 1,029,502 records (0.4s)
  15,000 customers, 156,222 invoices, 858,280 invoice lines
Streaming to cluster...
  Customer:        15,000 rows (0.5s)
  Invoice:        156,222 rows (1.2s)
  InvoiceLine:    858,280 rows (9.5s)
Streamed 1,029,502 rows in 11.1 seconds (92,398 rows/sec)

Verification:
  Customer:    15,000 rows
  Invoice:     156,222 rows
  InvoiceLine: 858,280 rows

Cross-table JOIN (Customer -> Invoice -> InvoiceLine -> Track):
  Ahmed Brown | 2024-01-01 | The Unforgiven II | $0.99 x3
  Ahmed Brown | 2024-01-01 | Dead And Broken | $0.99 x1
  Ahmed Brown | 2024-01-01 | Truth Hurts | $0.99 x3
  Ahmed Brown | 2024-01-01 | Siva | $0.99 x3
  Ahmed Brown | 2024-01-01 | Around The World | $0.99 x3
```

Over one million rows across three related tables, streamed in under 15 seconds. The individual `upsert()` approach would take over 12 minutes for the same data at ~1,400 rows/sec. The four-table JOIN confirms referential integrity: every InvoiceLine references a valid Invoice, every Invoice references a valid Customer, and every InvoiceLine references a valid Track from the original catalog.

{% hint style="info" %}
The JOIN results show randomly selected tracks from the Chinook catalog. The specific track names depend on partition assignment, which varies between cluster restarts. The row counts (15,000 customers, 156,222 invoices, 858,280 invoice lines) are identical on every run because the generator uses a fixed random seed.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** 1,000,000+ rows streamed across three tables. The four-table JOIN returns results with real track names from the Chinook catalog.
{% endhint %}

## Observe Backpressure With SubmissionPublisher

`SubmissionPublisher` is Java's built-in `Flow.Publisher` implementation. It maintains an internal buffer (256 items by default) and delivers items to the subscriber asynchronously. When the buffer fills because the producer is faster than the consumer, `submit()` blocks the calling thread until space opens.

The `submit()` method returns a `long` value called the *lag*: the estimated number of items buffered but not yet consumed by the subscriber. A lag of 0 means the subscriber is keeping up. A growing lag means the producer is outpacing the consumer. When the lag reaches the buffer capacity, the next `submit()` call blocks.

Create `src/main/java/com/example/streaming/BackpressureDemo.java`:

{% code title="BackpressureDemo.java" %}
```java
package com.example.streaming;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.DataStreamerItem;
import org.apache.ignite.table.DataStreamerOptions;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Tuple;
import org.apache.ignite.tx.Transaction;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.SubmissionPublisher;

/**
 * Demonstrates SubmissionPublisher's backpressure behavior when streaming
 * to the DataStreamer. Observe the lag metric and understand when blocking
 * is acceptable versus when a non-blocking publisher is needed.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.streaming.BackpressureDemo -q
 */
public class BackpressureDemo {

    private static final int CUSTOMER_ID_OFFSET = 200_000;
    private static final int RECORD_COUNT = 10_000;

    public static void main(String[] args) throws Exception {
        java.util.logging.LogManager.getLogManager().reset();
        java.util.logging.Logger.getLogger("org.apache.ignite")
            .setLevel(java.util.logging.Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800")
                .build()) {

            var sql = client.sql();
            RecordView<Tuple> view = client.tables().table("Customer").recordView();

            // Clean up
            sql.execute((Transaction) null,
                "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_ID_OFFSET);

            System.out.printf("Streaming %,d records, observing SubmissionPublisher lag...%n%n",
                RECORD_COUNT);

            // SubmissionPublisher with default buffer (256 items)
            SubmissionPublisher<DataStreamerItem<Tuple>> publisher =
                new SubmissionPublisher<>();
            CompletableFuture<Void> future = view.streamData(
                publisher, DataStreamerOptions.DEFAULT);

            long maxLag = 0;

            for (int i = 0; i < RECORD_COUNT; i++) {
                Tuple customer = Tuple.create()
                    .set("CUSTOMERID", CUSTOMER_ID_OFFSET + i)
                    .set("FIRSTNAME", "BP" + i)
                    .set("LASTNAME", "Test")
                    .set("COUNTRY", "USA")
                    .set("EMAIL", "bp" + i + "@example.com");

                // submit() returns the estimated lag: items buffered but not yet consumed
                long lag = publisher.submit(DataStreamerItem.of(customer));

                if (lag > maxLag) maxLag = lag;

                // Print lag at key milestones
                if (i < 5 || i % 2000 == 0 || i == RECORD_COUNT - 1) {
                    System.out.printf("  record %,6d  lag = %,d%n", i, lag);
                }
            }

            publisher.close();
            future.join();

            Thread.sleep(1500);
            long verified = countCustomers(sql);
            System.out.printf("%nMax lag observed: %,d (buffer capacity: 256)%n", maxLag);
            System.out.printf("Verified: %,d rows%n", verified);

            // Clean up
            sql.execute((Transaction) null,
                "DELETE FROM Customer WHERE CustomerId >= ?", CUSTOMER_ID_OFFSET);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }

        System.exit(0);
    }

    static long countCustomers(org.apache.ignite.sql.IgniteSql sql) {
        try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                "SELECT COUNT(*) AS CNT FROM Customer WHERE CustomerId >= ?",
                CUSTOMER_ID_OFFSET)) {
            return rs.next().longValue("CNT");
        }
    }
}
```
{% endcode %}

{% hint style="info" %}
`submit()` returns the estimated lag (items buffered but not yet consumed) for observability. The code captures it here so you can watch the buffer fill and drain. You don't need to check the lag and decide when to block. When the buffer is full, `submit()` blocks the calling thread automatically until the DataStreamer consumes items and frees space. Backpressure works the same whether you capture the return value or ignore it.
{% endhint %}

Run the backpressure test:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.streaming.BackpressureDemo -q
```

**Expected output:**

```
Streaming 10,000 records, observing SubmissionPublisher lag...

  record      0  lag = 1
  record      1  lag = 2
  record      2  lag = 3
  record      3  lag = 4
  record      4  lag = 5
  record  2,000  lag = 1
  record  4,000  lag = 2
  record  6,000  lag = 1
  record  8,000  lag = 1
  record  9,999  lag = 1

Max lag observed: 164 (buffer capacity: 256)
Verified: 10,000 rows
```

The DataStreamer's internal subscriber consumes items fast enough that the 256-item buffer never fills at this volume. The lag peaks early (while the subscriber initializes partition buffers) and settles near 1 for the rest of the run. No `submit()` calls blocked.

For batch jobs, migrations, and data generators, `SubmissionPublisher` is the right choice. It handles backpressure transparently: if the cluster slows down, the producer thread pauses automatically.

The calling thread resumes when buffer space opens. This blocking behavior is acceptable when the producer has nothing else to do while waiting.

For event-driven systems, the blocking model is a problem. A Kafka consumer that blocks on `submit()` stops polling, which triggers consumer group rebalancing. An IoT gateway that blocks on `submit()` drops incoming sensor readings. A real-time feed that blocks on `submit()` falls behind and may never recover. These producers cannot pause.

The non-blocking alternative is a custom `Flow.Publisher` that produces items only when the DataStreamer requests them.

{% hint style="success" %}
**Checkpoint:** The lag metric shows SubmissionPublisher managing backpressure automatically. All 10,000 records verified in the cluster.
{% endhint %}

## Stream With a Custom Flow.Publisher

`SubmissionPublisher` buffers items and delivers them asynchronously, but it blocks when the buffer fills. A custom `Flow.Publisher` implements demand-based delivery instead: it produces items only when the DataStreamer's internal subscriber calls `request(n)`. The custom publisher never buffers, never blocks, and adds real-time progress tracking for long-running data loads.

The reactive streams contract is a collaboration between two parties:

1. **The subscriber** (DataStreamer's internal `StreamerSubscriber`) calls `request(n)` to signal how many items it can accept. The value of n depends on the `pageSize` and `perPartitionParallelOperations` settings.
2. **The publisher** delivers up to n items via `onNext()`, then waits for the next `request(n)` call. When all items are delivered, it calls `onComplete()`.

Neither side overwhelms the other. The producer never buffers, never blocks, and never overflows. Kafka consumer frameworks, R2DBC drivers, and Project Reactor use the same contract.

{% hint style="info" %}
After building the `ProgressSubscription` below, use Find Usages on the `request()` method. The call comes from GridGain's internal `StreamerSubscriber`, not from your code. The DataStreamer controls the pace; your publisher responds to demand.
{% endhint %}

Create `src/main/java/com/example/streaming/StreamingWithProgress.java`:

{% code title="StreamingWithProgress.java" %}
```java
package com.example.streaming;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.DataStreamerItem;
import org.apache.ignite.table.DataStreamerOptions;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Tuple;
import org.apache.ignite.tx.Transaction;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Flow;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Full three-table pipeline with a custom Flow.Publisher that reports
 * real-time progress per table. Non-blocking: the publisher delivers
 * items only when the DataStreamer requests them.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.streaming.StreamingWithProgress -q
 */
public class StreamingWithProgress {

    private static final int CUSTOMER_OFFSET = 100_000;
    private static final int INVOICE_OFFSET = 100_000;
    private static final int INVOICELINE_OFFSET = 1_000_000;
    private static final int CUSTOMER_COUNT = 15_000;

    private static final int BAR_WIDTH = 30;
    // ANSI escape: carriage return + clear entire line
    private static final String CLEAR_LINE = "\r\033[2K";

    public static void main(String[] args) throws Exception {
        java.util.logging.LogManager.getLogManager().reset();
        java.util.logging.Logger.getLogger("org.apache.ignite")
            .setLevel(java.util.logging.Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800")
                .build()) {

            var sql = client.sql();
            System.out.println("=== Streaming with Progress Tracking");

            // Clean up
            CommerceDataGenerator.cleanup(sql);

            // Load catalog and generate data (reuse from CommerceDataGenerator)
            System.out.print("Loading catalog TrackIds... ");
            List<Integer> trackIds = CommerceDataGenerator.loadTrackIds(sql);
            System.out.printf("%,d tracks%n", trackIds.size());

            System.out.print("Generating records... ");
            long genStart = System.currentTimeMillis();
            Random rng = new Random(42);
            // Reuse the generation logic from CommerceDataGenerator
            List<Tuple> customers = TunedStreaming.generateCustomers(CUSTOMER_COUNT, rng);
            List<Tuple> invoices = new ArrayList<>();
            List<Tuple> invoiceLines = new ArrayList<>();
            CommerceDataGenerator.generateCommerceData(
                customers, invoices, invoiceLines, trackIds, rng);

            long genElapsed = System.currentTimeMillis() - genStart;
            int totalRows = customers.size() + invoices.size() + invoiceLines.size();
            System.out.printf("%,d records (%.1fs)%n", totalRows, genElapsed / 1000.0);
            System.out.printf("  %,d customers, %,d invoices, %,d invoice lines%n",
                customers.size(), invoices.size(), invoiceLines.size());

            // Stream with progress tracking
            DataStreamerOptions options = DataStreamerOptions.builder()
                .pageSize(500)
                .perPartitionParallelOperations(4)
                .autoFlushInterval(1000)
                .build();

            System.out.println("Streaming to cluster...");
            long streamStart = System.currentTimeMillis();

            long custTime = streamWithProgress(client, "Customer", customers, options);
            System.out.printf("%s>>> %-14s %,10d rows (%.1fs)%n",
                CLEAR_LINE, "Customer", customers.size(), custTime / 1000.0);

            long invTime = streamWithProgress(client, "Invoice", invoices, options);
            System.out.printf("%s>>> %-14s %,10d rows (%.1fs)%n",
                CLEAR_LINE, "Invoice", invoices.size(), invTime / 1000.0);

            long lineTime = streamWithProgress(client, "InvoiceLine",
                invoiceLines, options);
            System.out.printf("%s>>> %-14s %,10d rows (%.1fs)%n",
                CLEAR_LINE, "InvoiceLine", invoiceLines.size(), lineTime / 1000.0);

            long streamElapsed = System.currentTimeMillis() - streamStart;
            double rowsPerSec = totalRows / (streamElapsed / 1000.0);
            System.out.printf("Streamed %,d rows in %.1f seconds (%,.0f rows/sec)%n",
                totalRows, streamElapsed / 1000.0, rowsPerSec);

            Thread.sleep(2000);

            System.out.println("\nVerification:");
            System.out.printf("  Customer:    %,d rows%n",
                CommerceDataGenerator.countWhere(sql, "Customer",
                    "CustomerId", CUSTOMER_OFFSET));
            System.out.printf("  Invoice:     %,d rows%n",
                CommerceDataGenerator.countWhere(sql, "Invoice",
                    "InvoiceId", INVOICE_OFFSET));
            System.out.printf("  InvoiceLine: %,d rows%n",
                CommerceDataGenerator.countWhere(sql, "InvoiceLine",
                    "InvoiceLineId", INVOICELINE_OFFSET));

            // Clean up
            CommerceDataGenerator.cleanup(sql);
        }

        System.exit(0);
    }

    static long streamWithProgress(IgniteClient client, String tableName,
                                    List<Tuple> records, DataStreamerOptions options) {
        RecordView<Tuple> view = client.tables().table(tableName).recordView();
        ProgressPublisher publisher = new ProgressPublisher(records, tableName);

        long start = System.currentTimeMillis();
        CompletableFuture<Void> future = view.streamData(publisher, options);
        future.join();
        return System.currentTimeMillis() - start;
    }

    // ---- Progress-tracking publisher ----

    /**
     * A Flow.Publisher that delivers records on demand and renders a progress
     * bar to the console. The progress bar updates every 100ms to avoid
     * excessive console I/O.
     *
     * This publisher never buffers items. It produces a record only when the
     * DataStreamer's subscriber calls request(n). No blocking, no overflow.
     */
    static class ProgressPublisher implements Flow.Publisher<DataStreamerItem<Tuple>> {
        private final List<Tuple> records;
        private final String tableName;

        ProgressPublisher(List<Tuple> records, String tableName) {
            this.records = records;
            this.tableName = tableName;
        }

        @Override
        public void subscribe(
                Flow.Subscriber<? super DataStreamerItem<Tuple>> subscriber) {
            subscriber.onSubscribe(
                new ProgressSubscription(subscriber, records, tableName));
        }
    }

    /**
     * Delivers records one at a time in response to request(n) calls from the
     * DataStreamer subscriber. Tracks delivery progress and renders a console
     * progress bar.
     */
    static class ProgressSubscription implements Flow.Subscription {
        private final Flow.Subscriber<? super DataStreamerItem<Tuple>> subscriber;
        private final List<Tuple> records;
        private final String tableName;
        private final AtomicLong index = new AtomicLong(0);
        private final AtomicLong demand = new AtomicLong(0);
        private final AtomicBoolean cancelled = new AtomicBoolean(false);
        private final AtomicBoolean delivering = new AtomicBoolean(false);
        private long lastProgressUpdate = 0;

        ProgressSubscription(
                Flow.Subscriber<? super DataStreamerItem<Tuple>> subscriber,
                List<Tuple> records, String tableName) {
            this.subscriber = subscriber;
            this.records = records;
            this.tableName = tableName;
        }

        @Override
        public void request(long n) {
            if (n <= 0) {
                subscriber.onError(
                    new IllegalArgumentException("Request must be positive"));
                return;
            }
            if (cancelled.get()) return;
            demand.addAndGet(n);
            deliver();
        }

        @Override
        public void cancel() {
            cancelled.set(true);
        }

        private void deliver() {
            // Prevent concurrent delivery from multiple request() calls
            if (!delivering.compareAndSet(false, true)) return;

            try {
                while (demand.get() > 0 && !cancelled.get()) {
                    long idx = index.get();
                    if (idx >= records.size()) {
                        subscriber.onComplete();
                        return;
                    }

                    subscriber.onNext(
                        DataStreamerItem.of(records.get((int) idx)));
                    index.incrementAndGet();
                    demand.decrementAndGet();

                    // Update progress bar at most every 100ms
                    long now = System.currentTimeMillis();
                    if (now - lastProgressUpdate > 100) {
                        System.out.print(CLEAR_LINE
                            + progressBar(tableName, idx + 1, records.size()));
                        lastProgressUpdate = now;
                    }
                }
            } catch (Exception e) {
                subscriber.onError(e);
            } finally {
                delivering.set(false);
            }

            // Check for demand that arrived during delivery
            if (demand.get() > 0 && !cancelled.get()
                    && index.get() < records.size()) {
                deliver();
            }
        }
    }

    /** Renders a 30-character progress bar with percentage and row counts. */
    static String progressBar(String tableName, long completed, int total) {
        double pct = (double) completed / total;
        int filled = (int) (pct * BAR_WIDTH);

        StringBuilder bar = new StringBuilder();
        bar.append(String.format("  %-14s [", tableName));
        for (int i = 0; i < BAR_WIDTH; i++) {
            if (i < filled) bar.append('#');
            else if (i == filled) bar.append('>');
            else bar.append(' ');
        }
        bar.append(String.format("] %3.0f%%  %,d / %,d",
            pct * 100, completed, total));
        return bar.toString();
    }
}
```
{% endcode %}

Run the full pipeline with progress tracking:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.streaming.StreamingWithProgress -q
```

**Expected output:**

```
=== Streaming with Progress Tracking
Loading catalog TrackIds... 3,503 tracks
Generating records... 1,029,502 records (0.4s)
  15,000 customers, 156,222 invoices, 858,280 invoice lines
Streaming to cluster...
>>> Customer           15,000 rows (0.2s)
>>> Invoice           156,222 rows (1.3s)
>>> InvoiceLine       858,280 rows (13.3s)
Streamed 1,029,502 rows in 14.8 seconds (69,434 rows/sec)

Verification:
  Customer:    15,000 rows
  Invoice:     156,222 rows
  InvoiceLine: 858,280 rows
```

During the InvoiceLine stream (858,280 rows), the progress bar advances in real time as the DataStreamer pulls records from the publisher. The Invoice stream (156,222 rows) also shows meaningful progress. Customer completes too quickly for the progress bar to advance, which is expected at 15,000 rows.

The `ProgressPublisher` pattern gives you operational visibility into long-running data loads. In production, you would replace the console progress bar with metrics (Micrometer, Prometheus) or structured logging, but the underlying `Flow.Publisher` contract is the same.

{% hint style="success" %}
**Checkpoint:** 1,000,000+ rows streamed with real-time progress tracking. All three table counts match the generated data.
{% endhint %}

## Summary

You built a commerce data generator that streams over 1,000,000 records across three related tables into the Music Store cluster. The DataStreamer API replaced individual `upsert()` calls with a streaming pipeline that delivers 40-70x higher throughput on the same hardware.

The patterns from this tutorial apply wherever individual writes are too slow:

| Scenario | Pattern from this tutorial |
|---|---|
| **Bulk data migration** | Full pipeline: generate or read records, stream in parent-child order, verify with JOINs |
| **Cache warming** | Stream hot data from a backing store into GridGain at startup using tuned DataStreamerOptions |
| **ETL from legacy systems** | Load source data, transform to Tuples, stream via SubmissionPublisher |
| **Event ingestion (Kafka, IoT)** | Custom Flow.Publisher with demand-based delivery to avoid blocking the consumer thread |
| **CI test fixtures** | Fixed-seed generator for reproducible datasets at any scale |

`SubmissionPublisher` buffers and blocks, which works for batch jobs where the producer has nothing else to do while waiting. Event-driven systems need demand-based delivery instead: a custom `Flow.Publisher` that never blocks the producer thread. Both strategies use the same `streamData()` method and `DataStreamerOptions`.

The `commerce-data-generator.jar` used in the schema design tutorial applies the same pattern at 50,000 customers, producing over 2.5 million rows.

**What's next.** To process data where it lives instead of moving it to the client, see [About Distributed Computing](../../gridgain9-development/distributed-computing/about-distributed-computing.md).
