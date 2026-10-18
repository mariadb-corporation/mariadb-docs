---
description: >-
  Build a data access layer that selects KeyValueView, RecordView, or SQL at every call site based on key availability, operation shape, and safety requirements.
---

# Choose the Right Data Access Pattern

## Introduction

The entity classes from the previous tutorial carry two responsibilities: they define the schema, and they map fields to columns at runtime. The `@Id` annotations that declared composite primary keys for colocation have a third effect that surfaces the moment your application makes its first data access call. Those annotations constrain which API calls are possible, which write operations are safe, and which consistency guarantees are available.

In this tutorial, you build a data access layer for the Music Store: nine service methods, each selecting its API based on key availability, operation shape, and safety requirements.

{% hint style="info" %}
GridGain 9 provides the RecordView, KeyValueView, SQL, and transaction APIs used in this tutorial, and adds near-cache for client-side caching, covered in a dedicated section at the end.
{% endhint %}

## Prerequisites

- **A running 3-node cluster with the Music Store dataset** from [Start Your Local GridGain 9 Development Cluster](../distributed-sql-foundations/start-local-cluster.md)
- **Completed** [Implement Schema with Java Annotations](schema-java-annotations.md) (you need the entity classes and familiarity with composite primary keys)
- **Java 17+** and a Java IDE (IntelliJ IDEA, VS Code with Java extensions, or similar)

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

**If the cluster was destroyed** (`docker compose down`), start the containers and re-initialize. See [Start Your Local GridGain 9 Development Cluster](../distributed-sql-foundations/start-local-cluster.md) for the full setup process.

</details>

## What you Will Learn

- Why RecordView and KeyValueView require the full composite primary key for point lookups
- How to select the right API based on key availability, operation shape, and safety needs
- When to use `insert` instead of `upsert` for write safety
- How to mix RecordView, KeyValueView, and SQL in a single transaction
- How to evaluate the near-cache consistency tradeoff (GridGain 9)

## Set Up the Project

Create a new Maven project in your IDE. This is a separate project from the annotations tutorial. A fresh project avoids dependencies on any modifications you may have made, and the entity classes are portable because the annotations carry the schema definition with the class.

Replace the generated `pom.xml` with the following:

{% code title="pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>music-store-access</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
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
            <id>GridGain External Repository</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>
</project>
```
{% endcode %}

{% hint style="info" %}
GridGain 9 artifacts are published to the GridGain external Nexus repository, not Maven Central. The `<repositories>` block is required for all GridGain 9 projects.
{% endhint %}

Copy four entity classes from the annotations tutorial into a `model` package (`src/main/java/com/example/musicstore/model/`): `Artist`, `Album`, `Customer`, and `Invoice`. These are the tables the service class operates on through the programmatic APIs. SQL queries reference other tables (Track, InvoiceLine) by name without needing entity classes.

As you paste each class, count the `@Id` annotations. Artist has one. Album has two. Customer has one. Invoice has two. That count determines what your application must provide for every programmatic data access call.

<details>
<summary>Entity classes (copy from the annotations tutorial)</summary>

{% code title="src/main/java/com/example/musicstore/model/Artist.java" %}
```java
package com.example.musicstore.model;

import org.apache.ignite.catalog.annotations.Column;
import org.apache.ignite.catalog.annotations.Id;
import org.apache.ignite.catalog.annotations.Table;
import org.apache.ignite.catalog.annotations.Zone;

@Table(zone = @Zone(value = "MusicStore", storageProfiles = "default",
                     partitions = 25, replicas = 2))
public class Artist {
    @Id
    @Column(value = "ArtistId", nullable = false)
    private Integer artistId;

    @Column(value = "Name", nullable = false, length = 120)
    private String name;

    public Artist() {}
    public Artist(Integer artistId, String name) {
        this.artistId = artistId;
        this.name = name;
    }

    public Integer getArtistId() { return artistId; }
    public void setArtistId(Integer artistId) { this.artistId = artistId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    @Override
    public String toString() {
        return "Artist{artistId=" + artistId + ", name='" + name + "'}";
    }
}
```
{% endcode %}

{% code title="src/main/java/com/example/musicstore/model/Album.java" %}
```java
package com.example.musicstore.model;

import org.apache.ignite.catalog.annotations.*;

@Table(zone = @Zone(value = "MusicStore", storageProfiles = "default",
                     partitions = 25, replicas = 2),
       colocateBy = @ColumnRef("ArtistId"),
       indexes = @Index(value = "IFK_AlbumArtistId",
                        columns = @ColumnRef("ArtistId")))
public class Album {
    @Id
    @Column(value = "AlbumId", nullable = false)
    private Integer albumId;

    @Id
    @Column(value = "ArtistId", nullable = false)
    private Integer artistId;

    @Column(value = "Title", nullable = false, length = 160)
    private String title;

    public Album() {}
    public Album(Integer albumId, Integer artistId, String title) {
        this.albumId = albumId;
        this.artistId = artistId;
        this.title = title;
    }

    public Integer getAlbumId() { return albumId; }
    public void setAlbumId(Integer albumId) { this.albumId = albumId; }
    public Integer getArtistId() { return artistId; }
    public void setArtistId(Integer artistId) { this.artistId = artistId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    @Override
    public String toString() {
        return "Album{albumId=" + albumId + ", artistId=" + artistId
            + ", title='" + title + "'}";
    }
}
```
{% endcode %}

{% code title="src/main/java/com/example/musicstore/model/Customer.java" %}
```java
package com.example.musicstore.model;

import org.apache.ignite.catalog.annotations.*;

@Table(zone = @Zone(value = "MusicStore", storageProfiles = "default",
                     partitions = 25, replicas = 2))
public class Customer {
    @Id
    @Column(value = "CustomerId", nullable = false)
    private Integer customerId;

    @Column(value = "FirstName", nullable = false, length = 40)
    private String firstName;

    @Column(value = "LastName", nullable = false, length = 20)
    private String lastName;

    @Column(value = "Company", length = 80)
    private String company;

    @Column(value = "Address", length = 70)
    private String address;

    @Column(value = "City", length = 40)
    private String city;

    @Column(value = "State", length = 40)
    private String state;

    @Column(value = "Country", length = 40)
    private String country;

    @Column(value = "PostalCode", length = 10)
    private String postalCode;

    @Column(value = "Phone", length = 24)
    private String phone;

    @Column(value = "Fax", length = 24)
    private String fax;

    @Column(value = "Email", nullable = false, length = 60)
    private String email;

    @Column(value = "SupportRepId")
    private Integer supportRepId;

    public Customer() {}

    public Integer getCustomerId() { return customerId; }
    public void setCustomerId(Integer customerId) { this.customerId = customerId; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public String getCompany() { return company; }
    public void setCompany(String company) { this.company = company; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
    public String getState() { return state; }
    public void setState(String state) { this.state = state; }
    public String getCountry() { return country; }
    public void setCountry(String country) { this.country = country; }
    public String getPostalCode() { return postalCode; }
    public void setPostalCode(String postalCode) { this.postalCode = postalCode; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getFax() { return fax; }
    public void setFax(String fax) { this.fax = fax; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public Integer getSupportRepId() { return supportRepId; }
    public void setSupportRepId(Integer supportRepId) { this.supportRepId = supportRepId; }

    @Override
    public String toString() {
        return "Customer{customerId=" + customerId + ", name='"
            + firstName + " " + lastName + "'}";
    }
}
```
{% endcode %}

{% code title="src/main/java/com/example/musicstore/model/Invoice.java" %}
```java
package com.example.musicstore.model;

import java.math.BigDecimal;
import java.time.LocalDate;
import org.apache.ignite.catalog.annotations.*;

@Table(zone = @Zone(value = "MusicStore", storageProfiles = "default",
                     partitions = 25, replicas = 2),
       colocateBy = @ColumnRef("CustomerId"),
       indexes = @Index(value = "IFK_InvoiceCustomerId",
                        columns = @ColumnRef("CustomerId")))
public class Invoice {
    @Id
    @Column(value = "InvoiceId", nullable = false)
    private Integer invoiceId;

    @Id
    @Column(value = "CustomerId", nullable = false)
    private Integer customerId;

    @Column(value = "InvoiceDate", nullable = false)
    private LocalDate invoiceDate;

    @Column(value = "BillingAddress", length = 70)
    private String billingAddress;

    @Column(value = "BillingCity", length = 40)
    private String billingCity;

    @Column(value = "BillingState", length = 40)
    private String billingState;

    @Column(value = "BillingCountry", length = 40)
    private String billingCountry;

    @Column(value = "BillingPostalCode", length = 10)
    private String billingPostalCode;

    @Column(value = "Total", nullable = false, precision = 10, scale = 2)
    private BigDecimal total;

    public Invoice() {}

    public Integer getInvoiceId() { return invoiceId; }
    public void setInvoiceId(Integer invoiceId) { this.invoiceId = invoiceId; }
    public Integer getCustomerId() { return customerId; }
    public void setCustomerId(Integer customerId) { this.customerId = customerId; }
    public LocalDate getInvoiceDate() { return invoiceDate; }
    public void setInvoiceDate(LocalDate invoiceDate) { this.invoiceDate = invoiceDate; }
    public String getBillingAddress() { return billingAddress; }
    public void setBillingAddress(String billingAddress) { this.billingAddress = billingAddress; }
    public String getBillingCity() { return billingCity; }
    public void setBillingCity(String billingCity) { this.billingCity = billingCity; }
    public String getBillingState() { return billingState; }
    public void setBillingState(String billingState) { this.billingState = billingState; }
    public String getBillingCountry() { return billingCountry; }
    public void setBillingCountry(String billingCountry) { this.billingCountry = billingCountry; }
    public String getBillingPostalCode() { return billingPostalCode; }
    public void setBillingPostalCode(String billingPostalCode) { this.billingPostalCode = billingPostalCode; }
    public BigDecimal getTotal() { return total; }
    public void setTotal(BigDecimal total) { this.total = total; }

    @Override
    public String toString() {
        return "Invoice{invoiceId=" + invoiceId + ", customerId=" + customerId
            + ", date=" + invoiceDate + ", total=" + total + "}";
    }
}
```
{% endcode %}

</details>

{% hint style="success" %}
**Checkpoint:** The project compiles. Your model package contains Artist (1 `@Id`), Album (2 `@Id`), Customer (1 `@Id`), and Invoice (2 `@Id`).
{% endhint %}

## Discover the Composite Key Constraint

You need to display Album 5 on a detail page. You know the AlbumId from the URL, but not the ArtistId. Try looking it up through RecordView, the same way the foundations tutorials accessed single-key tables.

Create `ExploreKeys.java` in the `com.example.musicstore` package:

{% code title="src/main/java/com/example/musicstore/ExploreKeys.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Album;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.table.Tuple;
import org.apache.ignite.tx.Transaction;

public class ExploreKeys {
    public static void main(String[] args) {
        try (IgniteClient client = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build()) {

            Table albumTable = client.tables().table("Album");
            RecordView<Album> albums = albumTable.recordView(Album.class);

            // --- Attempt 1: look up Album 5 by AlbumId alone ---
            // Album has a composite PK (AlbumId + ArtistId) because
            // ArtistId is the colocation column. Try with only AlbumId.
            System.out.println("--- Partial key: RecordView ---");
            Album partialKey = new Album();
            partialKey.setAlbumId(5);  // ArtistId is null
            try {
                Album result = albums.get((Transaction) null, partialKey);
                System.out.println("Result: " + result);
            } catch (Exception e) {
                System.out.println(e.getClass().getSimpleName()
                    + ": " + e.getMessage());
            }

            // --- Attempt 2: provide the full composite key ---
            // Both @Id fields set. Album 5 is "Big Ones" by Aerosmith (ArtistId = 3).
            System.out.println("\n--- Full key: RecordView ---");
            Album fullKey = new Album();
            fullKey.setAlbumId(5);
            fullKey.setArtistId(3);
            Album album = albums.get((Transaction) null, fullKey);
            System.out.println(album);

            // --- Same constraint on KeyValueView ---
            KeyValueView<Tuple, Tuple> kvAlbums = albumTable.keyValueView();

            System.out.println("\n--- Partial key: KeyValueView ---");
            Tuple partialTupleKey = Tuple.create().set("AlbumId", 5);
            try {
                kvAlbums.get((Transaction) null, partialTupleKey);
            } catch (Exception e) {
                System.out.println(e.getClass().getSimpleName()
                    + ": " + e.getMessage());
            }

            System.out.println("\n--- Full key: KeyValueView ---");
            Tuple fullTupleKey = Tuple.create()
                .set("AlbumId", 5).set("ArtistId", 3);
            Tuple value = kvAlbums.get((Transaction) null, fullTupleKey);
            System.out.println(value);

            // --- EXPLAIN plans: three routing behaviors on the same table ---
            System.out.println("\n--- EXPLAIN: Full PK ---");
            explain(client,
                "EXPLAIN PLAN FOR SELECT * FROM Album "
                + "WHERE AlbumId = 5 AND ArtistId = 1");

            System.out.println("--- EXPLAIN: Colocation column only ---");
            explain(client,
                "EXPLAIN PLAN FOR SELECT * FROM Album WHERE ArtistId = 1");

            System.out.println("--- EXPLAIN: Non-colocation column only ---");
            explain(client,
                "EXPLAIN PLAN FOR SELECT * FROM Album WHERE AlbumId = 5");
        }
        System.exit(0);
    }

    private static void explain(IgniteClient client, String query) {
        try (ResultSet<SqlRow> rs = client.sql()
                .execute((Transaction) null, query)) {
            while (rs.hasNext()) {
                System.out.println("  " + rs.next().stringValue(0));
            }
        }
        System.out.println();
    }
}
```
{% endcode %}

Run ExploreKeys. The first output is the most important:

{% code title="ExploreKeys output" %}
```text
--- Partial key: RecordView ---
MarshallerException: Column 'ARTISTID' does not allow NULLs

--- Full key: RecordView ---
Album{albumId=5, artistId=3, title='Big Ones'}

--- Partial key: KeyValueView ---
MarshallerException: Missed key column: ARTISTID

--- Full key: KeyValueView ---
ClientTuple [TITLE=Big Ones]
```
{% endcode %}

Album 5 exists. You loaded it in the annotations tutorial. But the partial-key call never reaches the cluster.

The client's `MarshallerException` tells you exactly what went wrong: ArtistId is null, and the `@Column(nullable = false)` annotation on that `@Id` field prohibits it.

This is three design decisions converging into one exception. In the schema tutorial, you made ArtistId the colocation column for Album. That required ArtistId in the composite primary key. In the annotations tutorial, you marked every `@Id` field with `@Column(nullable = false)` because PK columns cannot be nullable. Now, at runtime, the marshaller enforces that annotation before the request leaves the client.

KeyValueView throws the same exception class with a different message ("Missed key column") because the Tuple marshaller checks for missing key columns explicitly rather than checking nullable constraints. Both reject the request before it reaches the cluster. The error messages differ, but the constraint is the same: the schema's composite primary key requires all key columns.

**Open Album.java in your IDE and count the `@Id` annotations.** Two: `albumId` and `artistId`. Every RecordView and KeyValueView operation on this table needs both values. Now open Artist.java. One `@Id`. Artist lookups need only one value. The number of `@Id` annotations on a class tells you how many fields your application must provide for a point lookup.

The EXPLAIN plans reveal what SQL does differently. These are the same three routing behaviors from the schema tutorial, but the question has shifted from how the engine routes a query to which API your application should use.

{% code title="EXPLAIN output (trimmed)" %}
```text
--- EXPLAIN: Full PK ---
  KeyValueGet
      table: PUBLIC.ALBUM
      key: [5, 1]

--- EXPLAIN: Colocation column only ---
  Exchange
      distribution: single
    IndexScan
        table: PUBLIC.ALBUM
        index: IFK_ALBUMARTISTID
        predicate: =(ARTISTID, 1)

--- EXPLAIN: Non-colocation column only ---
  Exchange
      distribution: single
    TableScan
        table: PUBLIC.ALBUM
        predicate: =(ALBUMID, 5)
```
{% endcode %}

Three queries on the same table produce three different routing strategies:

1. **Full primary key**: the engine performs a direct `KeyValueGet` to the exact partition.
2. **Colocation column only (ArtistId)**: the engine scans a single partition using the secondary index.
3. **Non-colocation column only (AlbumId)**: the engine scans all partitions because it cannot determine which node holds the data without the colocation column.

SQL accepts any column combination in a WHERE clause. RecordView and KeyValueView require the full primary key. When your caller does not have the full key, SQL is the only option.

{% hint style="success" %}
**Checkpoint:** ExploreKeys runs successfully. Partial-key lookups throw `MarshallerException` on both RecordView and KeyValueView. Full-key lookups return Album 5. The three EXPLAIN plans show `KeyValueGet`, `IndexScan`, and `TableScan`.
{% endhint %}

## Create the Service Class

The exploration showed three situations where different APIs are the right choice: RecordView and KeyValueView for point lookups with the full key, SQL for everything else. A realistic data access layer holds references to all three and selects the API at each call site based on the operation.

Create `MusicStoreService.java` in a `service` package (`src/main/java/com/example/musicstore/service/`):

{% code title="src/main/java/com/example/musicstore/service/MusicStoreService.java (skeleton)" %}
```java
package com.example.musicstore.service;

import com.example.musicstore.model.Album;
import com.example.musicstore.model.Artist;
import com.example.musicstore.model.Customer;
import com.example.musicstore.model.Invoice;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.IgniteSql;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.IgniteTransactions;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class MusicStoreService {

    private final RecordView<Artist> artists;
    private final RecordView<Album> albums;
    private final RecordView<Customer> customers;
    private final RecordView<Invoice> invoices;
    private final KeyValueView<Integer, String> artistNames;
    private final IgniteSql sql;
    private final IgniteTransactions transactions;

    public MusicStoreService(IgniteClient client) {
        Table artistTable = client.tables().table("Artist");
        Table albumTable = client.tables().table("Album");
        Table customerTable = client.tables().table("Customer");
        Table invoiceTable = client.tables().table("Invoice");

        // RecordView: full-entity access with type-safe POJOs
        this.artists = artistTable.recordView(Artist.class);
        this.albums = albumTable.recordView(Album.class);
        this.customers = customerTable.recordView(Customer.class);
        this.invoices = invoiceTable.recordView(Invoice.class);

        // KeyValueView: key-to-single-value access. Maps ArtistId -> Name
        // without deserializing the full Artist object.
        this.artistNames = artistTable.keyValueView(
            Integer.class, String.class);

        this.sql = client.sql();
        this.transactions = client.transactions();
    }

    // Helper: create a Customer key object from an ID
    private Customer customerKey(int customerId) {
        Customer key = new Customer();
        key.setCustomerId(customerId);
        return key;
    }

    // --- Methods added in the following steps ---
}
```
{% endcode %}

The constructor obtains four RecordView references, one KeyValueView, the SQL interface, and the transaction manager. Keeping all view types in one class makes the API comparisons visible side by side. A production application would typically separate by domain boundary: a CatalogService for artists and albums, a CommerceService for invoices and customers.

{% hint style="success" %}
**Checkpoint:** The `MusicStoreService` class compiles. Your IDE resolves all imports.
{% endhint %}

## Implement Read Methods

{% hint style="warning" %}
This step and the next add methods to `MusicStoreService.java` one at a time. Add each method inside the class body, after the constructor and before the closing brace. The complete file is provided in a verification block at the end of the next step.
{% endhint %}

**A sidebar displays the artist name next to each album listing.** The caller knows the ArtistId and needs only the name, not the full Artist record. Add this method to `MusicStoreService.java` after the `customerKey` helper:

{% code title="Add to MusicStoreService.java" %}
```java
    // Artist has a single-column primary key, so a KeyValueView
    // lookup reaches the right partition directly. Only the name
    // is needed for display, so KeyValueView avoids deserializing
    // the full Artist object.
    public String getArtistName(int artistId) {
        return artistNames.get((Transaction) null, artistId);
    }
```
{% endcode %}

**A user clicks an album to see its details.** The page URL encodes both the AlbumId and ArtistId. Add the next method below `getArtistName`:

{% code title="Add to MusicStoreService.java" %}
```java
    // Album has a composite primary key: AlbumId + ArtistId.
    // Both @Id fields must be set on the key object. RecordView
    // returns the full typed POJO with all mapped fields.
    public Album getAlbum(int albumId, int artistId) {
        Album key = new Album();
        key.setAlbumId(albumId);
        key.setArtistId(artistId);
        return albums.get((Transaction) null, key);
    }
```
{% endcode %}

**A user browses AC/DC's discography.** The application knows the ArtistId but not the AlbumIds. RecordView and KeyValueView cannot help because Album requires both key columns. SQL handles any column combination in a WHERE clause. Add `findAlbumsByArtist` below `getAlbum`:

{% code title="Add to MusicStoreService.java" %}
```java
    // The caller has only the colocation column (ArtistId). The
    // engine routes this query to a single partition because
    // ArtistId is the colocation column for Album. All albums by
    // this artist share a partition with the Artist row.
    public List<Album> findAlbumsByArtist(int artistId) {
        List<Album> results = new ArrayList<>();
        try (ResultSet<SqlRow> rs = sql.execute(
                (Transaction) null,
                "SELECT AlbumId, ArtistId, Title FROM Album "
                + "WHERE ArtistId = ?",
                artistId)) {
            while (rs.hasNext()) {
                SqlRow row = rs.next();
                results.add(new Album(
                    row.intValue("AlbumId"),
                    row.intValue("ArtistId"),
                    row.stringValue("Title")));
            }
        }
        return results;
    }
```
{% endcode %}

**A customer shares an album link.** The URL contains only the AlbumId. Without the colocation column, the engine cannot determine which partition holds this album, so it scans all partitions. This full scan is the tradeoff for optimizing Artist-to-Album colocated joins: browsing by artist (the common case) is fast, while direct album-by-ID lookups (the rare case) cost more. Add `findAlbumById` next:

{% code title="Add to MusicStoreService.java" %}
```java
    // The caller has only AlbumId (the non-colocation column).
    // The engine scans all partitions because it cannot determine
    // which node holds the album without ArtistId.
    public Album findAlbumById(int albumId) {
        try (ResultSet<SqlRow> rs = sql.execute(
                (Transaction) null,
                "SELECT AlbumId, ArtistId, Title FROM Album "
                + "WHERE AlbumId = ?",
                albumId)) {
            if (rs.hasNext()) {
                SqlRow row = rs.next();
                return new Album(
                    row.intValue("AlbumId"),
                    row.intValue("ArtistId"),
                    row.stringValue("Title"));
            }
        }
        return null;
    }
```
{% endcode %}

**A dashboard shows the top-selling tracks across the entire catalog.** This query joins four tables across both colocation chains: InvoiceLine to Track to Album to Artist. No programmatic API supports joins. Add `getTopSellingTracks` as the last read method:

{% code title="Add to MusicStoreService.java" %}
```java
    // This join spans both colocation chains. EXPLAIN shows
    // Exchange nodes where data moves from the commerce chain
    // (InvoiceLine) to the catalog chain (Track, Album, Artist).
    public List<String> getTopSellingTracks(int limit) {
        List<String> results = new ArrayList<>();
        try (ResultSet<SqlRow> rs = sql.execute(
                (Transaction) null,
                "SELECT a.Name AS ArtistName, t.Name AS TrackName, "
                + "COUNT(il.InvoiceLineId) AS TimesSold, "
                + "SUM(il.UnitPrice * il.Quantity) AS Revenue "
                + "FROM InvoiceLine il "
                + "JOIN Track t ON il.TrackId = t.TrackId "
                + "JOIN Album al ON t.AlbumId = al.AlbumId "
                + "JOIN Artist a ON al.ArtistId = a.ArtistId "
                + "GROUP BY a.Name, t.Name "
                + "ORDER BY Revenue DESC LIMIT ?",
                limit)) {
            while (rs.hasNext()) {
                SqlRow row = rs.next();
                results.add(String.format(
                    "%-30s %-40s sold: %d  revenue: %s",
                    row.stringValue("ArtistName"),
                    row.stringValue("TrackName"),
                    row.longValue("TimesSold"),
                    row.decimalValue("Revenue")));
            }
        }
        return results;
    }
```
{% endcode %}

Five read methods, and the pattern is already visible:

- **Full primary key, one field**: KeyValueView returns the value without deserializing the full entity.
- **Full primary key, whole entity**: RecordView returns the typed POJO with every mapped field.
- **Partial key with the colocation column**: SQL reaches a single partition because the engine knows where the data lives.
- **Partial key without the colocation column**: SQL scans all partitions because the engine has no routing hint.
- **Join across tables**: SQL is the only option, and colocation decides whether rows stay on their nodes or cross the network.

Verify your progress by adding a temporary `main` method to `MusicStoreService` (or a quick test class) that calls the first two methods:

```java
// Quick verification (remove after confirming)
public static void main(String[] args) {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800").build()) {
        MusicStoreService svc = new MusicStoreService(client);
        System.out.println(svc.getArtistName(1));
        System.out.println(svc.getAlbum(5, 3));
    }
    System.exit(0);
}
```

Expected output:

```text
AC/DC
Album{albumId=5, artistId=3, title='Big Ones'}
```

{% hint style="success" %}
**Checkpoint:** `getArtistName(1)` returns `AC/DC` and `getAlbum(5, 3)` returns `Album{albumId=5, artistId=3, title='Big Ones'}`. All five read methods compile.
{% endhint %}

## Implement Write Methods

Write operations add a second dimension to API selection: beyond which API can reach the data, what safety guarantees does the operation require? The next four methods each demonstrate a different answer. Continue adding them to `MusicStoreService.java` below the read methods.

**An editor corrects a typo in an album title.** The application has both the AlbumId and ArtistId, so RecordView is technically possible. But the operation touches a single column. RecordView would need a get-modify-upsert cycle: fetch the entire Album, change the title, write the whole object back. That is two network round-trips and a full-entity write for a one-column change.

{% code title="Add to MusicStoreService.java" %}
```java
    // SQL is the right choice for writing a single column even
    // when the full primary key is available. One statement, one
    // round-trip, one column touched. RecordView would require
    // get() + setTitle() + upsert() for the same result.
    public void updateAlbumTitle(
            int albumId, int artistId, String newTitle) {
        sql.execute((Transaction) null,
            "UPDATE Album SET Title = ? "
            + "WHERE AlbumId = ? AND ArtistId = ?",
            newTitle, albumId, artistId);
    }
```
{% endcode %}

This is the method that breaks the assumption that "full key means programmatic API." When the operation only touches a subset of columns, SQL does the job in one statement without loading the full entity. The shape of the operation overrides the routing answer.

**An order arrives from the payment gateway.** The application needs to create an invoice, but duplicate messages are possible. If the same invoice arrives twice, the second attempt must be rejected, not silently overwritten.

{% code title="Add to MusicStoreService.java" %}
```java
    // insert() returns false if the invoice already exists.
    // Unlike upsert(), which silently overwrites, insert() detects
    // duplicates. In an event-processing pipeline, insert() is the
    // deduplication primitive: process the event only if insert()
    // returns true.
    //
    // insert() is not idempotent. The first call returns true; the
    // second returns false. upsert() is idempotent and safe to
    // retry. Choose based on whether the workflow needs to detect
    // duplicates (insert) or tolerate retries (upsert).
    public boolean createInvoice(Invoice invoice) {
        return invoices.insert((Transaction) null, invoice);
    }
```
{% endcode %}

The foundations tutorials used `upsert` for every write. Here, `insert` is the right choice because the business logic demands duplicate detection. Two write methods exist on RecordView because they serve different safety requirements.

**A checkout flow creates an invoice and updates the customer's billing address.** Both operations must succeed or both must roll back. If the insert succeeds but the address update fails, the invoice references a stale address.

{% code title="Add to MusicStoreService.java" %}
```java
    // Creating an invoice and updating the customer's billing
    // address must happen atomically. runInTransaction() wraps the
    // closure in an explicit transaction with automatic retry on
    // lock conflicts, timeouts, or primary replica changes.
    //
    // The closure may execute more than once, so it must not have
    // side effects outside the database: no emails, no external
    // API calls, no console output. The transaction guarantees
    // atomicity for the database operations; external side effects
    // are not covered.
    //
    // All three APIs (RecordView, KeyValueView, SQL) accept the
    // same Transaction object. This method uses insert() and
    // upsert() from RecordView, but SQL writes work in the same
    // transaction.
    public boolean createInvoiceWithBillingUpdate(
            Invoice invoice, String newAddress) {
        return transactions.runInTransaction(tx -> {
            // Create the invoice. If it already exists, return false.
            boolean created = invoices.insert(tx, invoice);
            if (!created) {
                return false;
            }

            // Read the customer to update the billing address.
            Customer customer = customers.get(
                tx, customerKey(invoice.getCustomerId()));
            customer.setAddress(newAddress);

            // Write the updated customer. Both the insert and this
            // upsert commit atomically when the closure returns.
            customers.upsert(tx, customer);
            return true;
        });
    }
```
{% endcode %}

Every tutorial before this one passed `null` as the transaction parameter. This method shows why the parameter exists: when business logic demands that multiple operations succeed or fail together, an explicit transaction is the only way to guarantee it. The `runInTransaction` wrapper handles retry logic, so the application code stays focused on the business rule.

**A personalization feature tags each customer with their favorite artist.** This operation reads from one API and writes through another. The artist name is a single field (best served by KeyValueView), but the customer update needs all fields for validation before saving (RecordView).

{% code title="Add to MusicStoreService.java" %}
```java
    // This method applies the API decision independently to the
    // read side and the write side. The artist name is one field
    // (KeyValueView). The customer needs all fields for the
    // read-modify-write cycle (RecordView). Using two APIs in one
    // operation is not inconsistent; each call site chooses its
    // own best API.
    //
    // This method is intentionally not transactional. The company
    // field stores display metadata, not financial state, so a
    // lost update from a concurrent writer is acceptable. For
    // operations where concurrent writes matter, wrap the
    // read-modify-write cycle in runInTransaction as shown in
    // createInvoiceWithBillingUpdate.
    public void updateCustomerWithArtistReference(
            int customerId, int favoriteArtistId) {
        String artistName = artistNames.get(
            (Transaction) null, favoriteArtistId);

        Customer customer = customers.get(
            (Transaction) null, customerKey(customerId));
        if (customer == null) {
            throw new IllegalArgumentException(
                "Customer " + customerId + " not found");
        }

        customer.setCompany("Fan of " + artistName);
        customers.upsert((Transaction) null, customer);
    }
```
{% endcode %}

Four write methods, and two distinct reasons why the "obvious" API choice was wrong:

- **`updateAlbumTitle`** shows that the shape of the operation can override key availability. The full primary key was available, but SQL was still the right choice for a single-column write.
- **`createInvoice`** writes a full entity through RecordView and uses `insert` for duplicate detection in an event-processing pipeline.
- **`createInvoiceWithBillingUpdate`** also writes through RecordView, but wraps the work in an explicit transaction for multi-table atomicity.
- **`updateCustomerWithArtistReference`** confirms that each call site within a single operation makes its own independent API decision. The read uses KeyValueView, the write uses RecordView.

<details>
<summary>Complete MusicStoreService.java (for verification)</summary>

{% code title="src/main/java/com/example/musicstore/service/MusicStoreService.java" %}
```java
package com.example.musicstore.service;

import com.example.musicstore.model.Album;
import com.example.musicstore.model.Artist;
import com.example.musicstore.model.Customer;
import com.example.musicstore.model.Invoice;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.IgniteSql;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.IgniteTransactions;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class MusicStoreService {

    private final RecordView<Artist> artists;
    private final RecordView<Album> albums;
    private final RecordView<Customer> customers;
    private final RecordView<Invoice> invoices;
    private final KeyValueView<Integer, String> artistNames;
    private final IgniteSql sql;
    private final IgniteTransactions transactions;

    public MusicStoreService(IgniteClient client) {
        Table artistTable = client.tables().table("Artist");
        Table albumTable = client.tables().table("Album");
        Table customerTable = client.tables().table("Customer");
        Table invoiceTable = client.tables().table("Invoice");

        this.artists = artistTable.recordView(Artist.class);
        this.albums = albumTable.recordView(Album.class);
        this.customers = customerTable.recordView(Customer.class);
        this.invoices = invoiceTable.recordView(Invoice.class);
        this.artistNames = artistTable.keyValueView(
            Integer.class, String.class);
        this.sql = client.sql();
        this.transactions = client.transactions();
    }

    public String getArtistName(int artistId) {
        return artistNames.get((Transaction) null, artistId);
    }

    public Album getAlbum(int albumId, int artistId) {
        Album key = new Album();
        key.setAlbumId(albumId);
        key.setArtistId(artistId);
        return albums.get((Transaction) null, key);
    }

    public List<Album> findAlbumsByArtist(int artistId) {
        List<Album> results = new ArrayList<>();
        try (ResultSet<SqlRow> rs = sql.execute(
                (Transaction) null,
                "SELECT AlbumId, ArtistId, Title FROM Album "
                + "WHERE ArtistId = ?",
                artistId)) {
            while (rs.hasNext()) {
                SqlRow row = rs.next();
                results.add(new Album(
                    row.intValue("AlbumId"),
                    row.intValue("ArtistId"),
                    row.stringValue("Title")));
            }
        }
        return results;
    }

    public Album findAlbumById(int albumId) {
        try (ResultSet<SqlRow> rs = sql.execute(
                (Transaction) null,
                "SELECT AlbumId, ArtistId, Title FROM Album "
                + "WHERE AlbumId = ?",
                albumId)) {
            if (rs.hasNext()) {
                SqlRow row = rs.next();
                return new Album(
                    row.intValue("AlbumId"),
                    row.intValue("ArtistId"),
                    row.stringValue("Title"));
            }
        }
        return null;
    }

    public List<String> getTopSellingTracks(int limit) {
        List<String> results = new ArrayList<>();
        try (ResultSet<SqlRow> rs = sql.execute(
                (Transaction) null,
                "SELECT a.Name AS ArtistName, t.Name AS TrackName, "
                + "COUNT(il.InvoiceLineId) AS TimesSold, "
                + "SUM(il.UnitPrice * il.Quantity) AS Revenue "
                + "FROM InvoiceLine il "
                + "JOIN Track t ON il.TrackId = t.TrackId "
                + "JOIN Album al ON t.AlbumId = al.AlbumId "
                + "JOIN Artist a ON al.ArtistId = a.ArtistId "
                + "GROUP BY a.Name, t.Name "
                + "ORDER BY Revenue DESC LIMIT ?",
                limit)) {
            while (rs.hasNext()) {
                SqlRow row = rs.next();
                results.add(String.format(
                    "%-30s %-40s sold: %d  revenue: %s",
                    row.stringValue("ArtistName"),
                    row.stringValue("TrackName"),
                    row.longValue("TimesSold"),
                    row.decimalValue("Revenue")));
            }
        }
        return results;
    }

    public void updateAlbumTitle(
            int albumId, int artistId, String newTitle) {
        sql.execute((Transaction) null,
            "UPDATE Album SET Title = ? "
            + "WHERE AlbumId = ? AND ArtistId = ?",
            newTitle, albumId, artistId);
    }

    public boolean createInvoice(Invoice invoice) {
        return invoices.insert((Transaction) null, invoice);
    }

    public boolean createInvoiceWithBillingUpdate(
            Invoice invoice, String newAddress) {
        return transactions.runInTransaction(tx -> {
            boolean created = invoices.insert(tx, invoice);
            if (!created) {
                return false;
            }
            Customer customer = customers.get(
                tx, customerKey(invoice.getCustomerId()));
            customer.setAddress(newAddress);
            customers.upsert(tx, customer);
            return true;
        });
    }

    public void updateCustomerWithArtistReference(
            int customerId, int favoriteArtistId) {
        String artistName = artistNames.get(
            (Transaction) null, favoriteArtistId);
        Customer customer = customers.get(
            (Transaction) null, customerKey(customerId));
        if (customer == null) {
            throw new IllegalArgumentException(
                "Customer " + customerId + " not found");
        }
        customer.setCompany("Fan of " + artistName);
        customers.upsert((Transaction) null, customer);
    }

    private Customer customerKey(int customerId) {
        Customer key = new Customer();
        key.setCustomerId(customerId);
        return key;
    }
}
```
{% endcode %}

</details>

{% hint style="success" %}
**Checkpoint:** All nine methods compile. The `MusicStoreService` class has five read methods, three write methods, and one mixed-API method.
{% endhint %}

## Run and Verify All Methods

Create `RunService.java` to exercise every method and verify the results. Test data uses IDs above 9000 to avoid conflicts with the existing Music Store dataset. Each test cleans up after itself so you can run the program multiple times.

{% code title="src/main/java/com/example/musicstore/RunService.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Album;
import com.example.musicstore.model.Customer;
import com.example.musicstore.model.Invoice;
import com.example.musicstore.service.MusicStoreService;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

public class RunService {

    public static void main(String[] args) {
        try (IgniteClient client = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build()) {

            MusicStoreService service = new MusicStoreService(client);

            // --- Read methods ---

            System.out.println("--- getArtistName(1) ---");
            String name = service.getArtistName(1);
            System.out.println("Result: " + name);

            System.out.println("\n--- getAlbum(5, 3) ---");
            Album album = service.getAlbum(5, 3);
            System.out.println("Result: " + album);

            System.out.println("\n--- findAlbumsByArtist(1) ---");
            List<Album> albums = service.findAlbumsByArtist(1);
            System.out.println("Found " + albums.size() + " albums:");
            albums.forEach(a -> System.out.println("  " + a));

            System.out.println("\n--- findAlbumById(5) ---");
            Album found = service.findAlbumById(5);
            System.out.println("Result: " + found);

            System.out.println("\n--- getTopSellingTracks(5) ---");
            List<String> tracks = service.getTopSellingTracks(5);
            tracks.forEach(t -> System.out.println("  " + t));

            // --- Write methods ---

            System.out.println("\n--- updateAlbumTitle ---");
            service.updateAlbumTitle(5, 3, "Big Ones (Remastered)");
            Album updated = service.getAlbum(5, 3);
            System.out.println("After SQL update: " + updated);
            service.updateAlbumTitle(5, 3, "Big Ones");
            System.out.println("Restored:         "
                + service.getAlbum(5, 3));

            System.out.println("\n--- createInvoice ---");
            Invoice testInvoice = new Invoice();
            testInvoice.setInvoiceId(9001);
            testInvoice.setCustomerId(1);
            testInvoice.setInvoiceDate(LocalDate.now());
            testInvoice.setBillingCity("Sao Paulo");
            testInvoice.setBillingCountry("Brazil");
            testInvoice.setTotal(new BigDecimal("9.99"));
            boolean first = service.createInvoice(testInvoice);
            System.out.println("First insert:  " + first);
            boolean second = service.createInvoice(testInvoice);
            System.out.println("Second insert: " + second);
            client.tables().table("Invoice")
                .recordView(Invoice.class)
                .delete((Transaction) null, testInvoice);
            System.out.println("Cleanup: test invoice deleted");

            System.out.println(
                "\n--- createInvoiceWithBillingUpdate ---");
            Invoice txInvoice = new Invoice();
            txInvoice.setInvoiceId(9002);
            txInvoice.setCustomerId(1);
            txInvoice.setInvoiceDate(LocalDate.now());
            txInvoice.setBillingCity("Rio de Janeiro");
            txInvoice.setTotal(new BigDecimal("15.99"));
            Customer before = readCustomer(client, 1);
            String originalAddress = before.getAddress();
            boolean txResult =
                service.createInvoiceWithBillingUpdate(
                    txInvoice, "456 New Billing St");
            System.out.println("Transaction result: " + txResult);
            Customer after = readCustomer(client, 1);
            System.out.println("Address after: "
                + after.getAddress());
            // Restore original state
            client.tables().table("Invoice")
                .recordView(Invoice.class)
                .delete((Transaction) null, txInvoice);
            after.setAddress(originalAddress);
            client.tables().table("Customer")
                .recordView(Customer.class)
                .upsert((Transaction) null, after);
            System.out.println("Cleanup: invoice deleted, "
                + "address restored");

            // --- Mixed API ---

            System.out.println(
                "\n--- updateCustomerWithArtistReference ---");
            Customer beforeMix = readCustomer(client, 1);
            String originalCompany = beforeMix.getCompany();
            System.out.println("Before: company='"
                + originalCompany + "'");
            service.updateCustomerWithArtistReference(1, 1);
            Customer afterMix = readCustomer(client, 1);
            System.out.println("After:  company='"
                + afterMix.getCompany() + "'");
            afterMix.setCompany(originalCompany);
            client.tables().table("Customer")
                .recordView(Customer.class)
                .upsert((Transaction) null, afterMix);
            System.out.println("Cleanup: restored original company");

            // --- EXPLAIN verification ---

            System.out.println(
                "\n--- EXPLAIN: findAlbumsByArtist ---");
            try (ResultSet<SqlRow> rs = client.sql().execute(
                    (Transaction) null,
                    "EXPLAIN PLAN FOR "
                    + "SELECT AlbumId, ArtistId, Title "
                    + "FROM Album WHERE ArtistId = 1")) {
                while (rs.hasNext()) {
                    System.out.println(
                        "  " + rs.next().stringValue(0));
                }
            }
        }
        System.exit(0);
    }

    private static Customer readCustomer(
            IgniteClient client, int id) {
        Customer key = new Customer();
        key.setCustomerId(id);
        return client.tables().table("Customer")
            .recordView(Customer.class)
            .get((Transaction) null, key);
    }
}
```
{% endcode %}

Run the program. Here is the expected output:

{% code title="RunService output" %}
```text
--- getArtistName(1) ---
Result: AC/DC

--- getAlbum(5, 3) ---
Result: Album{albumId=5, artistId=3, title='Big Ones'}

--- findAlbumsByArtist(1) ---
Found 2 albums:
  Album{albumId=4, artistId=1, title='Let There Be Rock'}
  Album{albumId=1, artistId=1, title='For Those About To Rock We Salute You'}

--- findAlbumById(5) ---
Result: Album{albumId=5, artistId=3, title='Big Ones'}

--- getTopSellingTracks(5) ---
  Iron Maiden                    The Trooper                              sold: 5  revenue: 4.95
  Heroes                         How to Stop an Exploding Man             sold: 2  revenue: 3.98
  Aquaman                        Pilot                                    sold: 2  revenue: 3.98
  Battlestar Galactica           The Woman King                           sold: 2  revenue: 3.98
  Heroes                         The Fix                                  sold: 2  revenue: 3.98

--- updateAlbumTitle ---
After SQL update: Album{albumId=5, artistId=3, title='Big Ones (Remastered)'}
Restored:         Album{albumId=5, artistId=3, title='Big Ones'}

--- createInvoice ---
First insert:  true
Second insert: false
Cleanup: test invoice deleted

--- createInvoiceWithBillingUpdate ---
Transaction result: true
Address after: 456 New Billing St
Cleanup: invoice deleted, address restored

--- updateCustomerWithArtistReference ---
Before: company='Embraer - Empresa Brasileira de Aeronáutica S.A.'
After:  company='Fan of AC/DC'
Cleanup: restored original company

--- EXPLAIN: findAlbumsByArtist ---
  Exchange
      distribution: single
      est: (rows=116)
    IndexScan
        table: PUBLIC.ALBUM
        index: IFK_ALBUMARTISTID
        type: SORTED
        predicate: =(ARTISTID, 1)
        searchBounds: [ExactBounds [bound=1]]
        fieldNames: [ALBUMID, ARTISTID, TITLE]
        collation: [ARTISTID ASC]
        est: (rows=116)
```
{% endcode %}

{% hint style="info" %}
The `findAlbumsByArtist` and `getTopSellingTracks` results may appear in a different order on your cluster. SQL queries without an ORDER BY clause do not guarantee row ordering.
{% endhint %}

Walk through the output section by section:

The **read methods** show the three API paths in action. `getArtistName` returns a single string through KeyValueView. `getAlbum` returns a full POJO through RecordView, requiring both key columns. `findAlbumsByArtist` and `findAlbumById` both use SQL, but the colocation column determines whether one partition or all partitions are scanned. `getTopSellingTracks` joins four tables across both colocation chains.

The **updateAlbumTitle** result confirms cross-API visibility: the SQL UPDATE writes the new title, and the subsequent RecordView `get()` reads it back. All three APIs operate on the same underlying storage. A write through one API is immediately visible to reads through any other API.

The **createInvoice** output shows the safety distinction. The first `insert()` returns `true` (new record created). The second call with the same key returns `false` (duplicate detected, no overwrite). Compare this to `upsert()`, which would silently overwrite the existing record without returning any signal.

The **createInvoiceWithBillingUpdate** result demonstrates an explicit transaction spanning two tables. The invoice insert and the customer address update either both commit or both roll back. The cleanup restores the original address so subsequent runs produce the same output.

The **EXPLAIN plan** at the bottom confirms the routing for `findAlbumsByArtist`: an `IndexScan` on `IFK_ALBUMARTISTID` within a single partition. The `Exchange` node with `distribution: single` means the engine knew to route the query to exactly one partition based on the colocation column. The colocation decisions from the schema tutorial are visible in the query plan.

**Open `MusicStoreService.java` in your IDE and use Find Usages on `sql.execute`.** Every SQL call exists because the caller either lacked the full primary key or because SQL was more efficient for the operation's shape (the single-column update). Now search for `albums.get` and `artistNames.get`. Every programmatic API call exists because the caller had the full key and needed either the complete entity or a single field.

{% hint style="success" %}
**Checkpoint:** RunService completes with all methods returning correct results. `createInvoice` returns `true` then `false`. The EXPLAIN plan shows `IndexScan` on `IFK_ALBUMARTISTID` with `distribution: single`.
{% endhint %}

## Near-Cache: Trading Consistency for Speed

GridGain 9 adds client-side caching through `NearCacheOptions`. A near-cached KeyValueView stores recently accessed entries in the client JVM's heap. The first read for a key fetches from the cluster; subsequent reads for the same key return from local memory until the time-to-live (TTL) expires.

The speed gain is real, but it comes with constraints that affect API selection.

Create `NearCacheDemo.java` in the `com.example.musicstore` package:

{% code title="src/main/java/com/example/musicstore/NearCacheDemo.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.NearCacheOptions;
import org.apache.ignite.table.Table;
import org.apache.ignite.table.TableViewOptions;
import org.apache.ignite.table.mapper.Mapper;
import org.apache.ignite.tx.Transaction;

public class NearCacheDemo {
    public static void main(String[] args) {
        try (IgniteClient client = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build()) {

            Table artistTable = client.tables().table("Artist");

            // Standard KeyValueView: every get() goes to the cluster
            KeyValueView<Integer, String> standardKv =
                artistTable.keyValueView(
                    Integer.class, String.class);
            // Warm the connection
            standardKv.get((Transaction) null, 1);

            System.out.println("--- Standard KeyValueView ---");
            long t1 = System.nanoTime();
            String n1 = standardKv.get((Transaction) null, 1);
            long e1 = (System.nanoTime() - t1) / 1_000_000;
            long t2 = System.nanoTime();
            String n2 = standardKv.get((Transaction) null, 1);
            long e2 = (System.nanoTime() - t2) / 1_000_000;
            System.out.println("First get:  " + n1
                + " (" + e1 + "ms)");
            System.out.println("Second get: " + n2
                + " (" + e2 + "ms)");

            // Near-cached KeyValueView: first get fetches from the
            // cluster, subsequent gets serve from client JVM memory
            NearCacheOptions nearCache = NearCacheOptions.builder()
                .maxEntries(500)
                .expireAfterAccess(30_000)  // 30s TTL
                .build();
            TableViewOptions options = TableViewOptions.builder()
                .nearCacheOptions(nearCache)
                .build();
            // Mapper.of() wrappers are required for the
            // TableViewOptions overload
            KeyValueView<Integer, String> cachedKv =
                artistTable.keyValueView(
                    Mapper.of(Integer.class),
                    Mapper.of(String.class),
                    options);

            System.out.println("\n--- Near-cached KeyValueView ---");
            long tc1 = System.nanoTime();
            String c1 = cachedKv.get((Transaction) null, 1);
            long ec1 = (System.nanoTime() - tc1) / 1_000_000;
            long tc2 = System.nanoTime();
            String c2 = cachedKv.get((Transaction) null, 1);
            long ec2 = (System.nanoTime() - tc2) / 1_000_000;
            long tc3 = System.nanoTime();
            String c3 = cachedKv.get((Transaction) null, 1);
            long ec3 = (System.nanoTime() - tc3) / 1_000_000;
            System.out.println("First get:  " + c1
                + " (" + ec1 + "ms) - cache miss");
            System.out.println("Second get: " + c2
                + " (" + ec2 + "ms) - cache hit");
            System.out.println("Third get:  " + c3
                + " (" + ec3 + "ms) - cache hit");

            // Staleness demonstration: write through standard view,
            // read through cached view
            System.out.println("\n--- Staleness ---");
            standardKv.put((Transaction) null, 9001,
                "Test Artist");
            String fresh = cachedKv.get(
                (Transaction) null, 9001);
            System.out.println("Write 'Test Artist', "
                + "cached read: " + fresh);
            standardKv.put((Transaction) null, 9001,
                "Updated Artist");
            String stale = cachedKv.get(
                (Transaction) null, 9001);
            System.out.println("Write 'Updated Artist', "
                + "cached read: " + stale);
            standardKv.remove((Transaction) null, 9001);

            // Transaction constraint
            System.out.println("\n--- Transaction constraint ---");
            try {
                Transaction tx = client.transactions().begin();
                cachedKv.get(tx, 1);
                tx.commit();
            } catch (UnsupportedOperationException e) {
                System.out.println("Exception: "
                    + e.getMessage());
            }
        }
        System.exit(0);
    }
}
```
{% endcode %}

Run NearCacheDemo:

{% code title="NearCacheDemo output" %}
```text
--- Standard KeyValueView ---
First get:  AC/DC (7ms)
Second get: AC/DC (2ms)

--- Near-cached KeyValueView ---
First get:  AC/DC (6ms) - cache miss
Second get: AC/DC (1ms) - cache hit
Third get:  AC/DC (0ms) - cache hit

--- Staleness ---
Write 'Test Artist', cached read: Test Artist
Write 'Updated Artist', cached read: Test Artist

--- Transaction constraint ---
Exception: Explicit transactions are not supported on views with Near Cache.
```
{% endcode %}

{% hint style="info" %}
Exact timing values vary by machine and network conditions. The pattern is what matters: standard KeyValueView shows consistent network latency on every call, while near-cached KeyValueView drops to 0-1ms after the first fetch.
{% endhint %}

The staleness result is the critical observation. The second `put` writes "Updated Artist" through the standard view, but the cached view still returns "Test Artist" from its local cache. The cache entry does not expire until the TTL fires (30 seconds in this configuration). Any other client that updates the same key is invisible to this view until the cache refreshes.

The transaction constraint is equally important. Passing a non-null `Transaction` to a near-cached view throws `UnsupportedOperationException`. If an operation needs transactional guarantees, it cannot use near-cache.

Near-cache is not a faster version of KeyValueView. It is a different consistency model. Standard KeyValueView guarantees that every `get()` returns the latest committed value. Near-cached KeyValueView guarantees that `get()` returns a value that was correct within the last N seconds. For artist names on a catalog page, 30 seconds of staleness is invisible to users. For an account balance in a transfer workflow, any staleness is dangerous.

{% hint style="info" %}
The near-cache polling mode uses ContinuousQuery internally to receive change events from the server. ContinuousQuery is a GridGain 9 feature that provides real-time change notifications with event filtering, column projection, and watermark-based exactly-once resumption.

ContinuousQuery is also the change-capture primitive that powers the GG9 streaming stack: Kafka Connect source connectors stream table changes to Kafka topics. Data Center Replication copies data across clusters. Change Data Capture feeds changes to Apache Iceberg tables. All of these operate on the same tables and colocation chains you designed in the schema tutorials.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** NearCacheDemo shows sub-millisecond reads after the first fetch, staleness on cross-client writes, and an `UnsupportedOperationException` on transactional access.
{% endhint %}

## The Access Pattern Matrix

Nine methods, three APIs, and every choice was driven by the same three considerations: does the caller have the full primary key, what does the operation need, and what safety guarantees does it require. The matrix below maps each method to its decision:

| Operation | Full Key? | What's Needed | Safety | API |
|---|---|---|---|---|
| Get artist name (sidebar) | Yes | One field (read) | Auto-commit | KeyValueView |
| Get album details (detail page) | Yes | Full entity (read) | Auto-commit | RecordView |
| Find albums by artist (browse) | No (colocation col) | Query result | Auto-commit | SQL (single partition) |
| Find album by ID (shared link) | No (non-coloc col) | Query result | Auto-commit | SQL (all partitions) |
| Top-selling tracks (dashboard) | No (join) | Aggregation | Auto-commit | SQL (cross-chain) |
| Update album title (editor fix) | Yes | One column (write) | Auto-commit | SQL |
| Create invoice (order intake) | Yes | Full entity (write) | Create-only (dedup) | RecordView `insert` |
| Invoice + billing update (checkout) | Yes | Two-table write | Explicit transaction | RecordView in tx |
| Tag customer with artist (personalization) | Yes | Mixed read/write | Auto-commit | KV read + RV write |
| High-frequency artist lookup (GridGain 9) | Yes | One field (read) | Tolerates staleness | KV + near-cache |

The Album table appears four times with four different APIs. The table does not determine the API. The call site does.

Look at the "Update album title" row. The full primary key is available, which makes RecordView possible. But the operation only changes one column, so SQL is more efficient. The shape of the write overrides the key availability.

Look at "Create invoice" and "Invoice + billing update." Both have the full key and write full entities. Without the safety column, both would be "RecordView with auto-commit." The safety requirement differentiates them: duplicate detection needs `insert`, and multi-table atomicity needs an explicit transaction.

The last row (GridGain 9 only) introduces a consistency tradeoff. Near-cache makes reads faster by accepting staleness and giving up transaction support. For stable reference data like artist names, this tradeoff is invisible to users. For rapidly changing data like account balances, it would be dangerous.

Every sync method in the service has an async counterpart (`getAsync`, `putAsync`, `executeAsync`). The API selection logic is the same for async operations. Bulk variants (`upsertAll`, `putAll`, `getAll`) follow the same full-key requirement.

{% hint style="success" %}
**Checkpoint:** The access pattern matrix maps all nine service methods to their API choices. Each row's API follows from the three columns to its left.
{% endhint %}

## Summary

### What you Built

A data access layer with nine methods using KeyValueView, RecordView, and SQL on the same Music Store schema. Read methods, write methods, a transactional method, and a mixed-API method, each demonstrating a different combination of key availability, operation shape, and safety requirements.

### Schema Design has Three Consequences

The schema tutorial established that schema design is performance design: colocation determines which queries are fast. The annotations tutorial expressed that design as code, with annotations carrying the schema alongside the application. This tutorial revealed two more consequences of those same decisions.

**Colocation shapes your API options.** Composite primary keys, created to enable colocated joins, require the full key for every RecordView and KeyValueView operation. When the caller does not have the full key, SQL is the only path. The number of `@Id` annotations on an entity class tells you what every programmatic call site must provide.

**Safety requirements drive the final choice.** Even when the full key is available and the operation shape fits RecordView, the business logic may demand `insert` instead of `upsert` (for duplicate detection), an explicit transaction (for multi-table atomicity), or SQL (for single-column writes that avoid a read-modify-write cycle). On GridGain 9, near-cache adds a consistency dimension: client-side speed at the cost of staleness and the loss of transaction support.

At every call site, three considerations determine the API: key availability, operation shape, and safety requirements. The colocation decisions made during schema design set the boundaries: they determine which API paths are available, which operations are efficient, and which safety guarantees are practical.

**What's next:** [Stream Data with the Data Streamer API](../data-pipeline-apis/data-streaming.md) covers the maximum-throughput write path. Data Streamer provides at-least-once delivery with automatic batching and backpressure, building on the same schema and colocation chains.

## Related

- [Work with RecordView and KeyValueView](../distributed-sql-foundations/recordview-keyvalueview.md) covers the full operation set for both APIs
- [Use Transactions in GridGain 9](../distributed-sql-foundations/use-transactions.md) covers explicit transactions, read-only snapshots, and auto-retry closures
- [Design a Schema for Distributed SQL](schema-distributed-sql.md) covers the colocation decisions that shape API selection
