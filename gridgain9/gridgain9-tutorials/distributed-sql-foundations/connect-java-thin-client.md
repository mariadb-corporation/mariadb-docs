---
description: >-
  Survey the GridGain 9 Java thin client: connect with partition awareness, define schema from annotations, navigate the Table package, and access data through RecordView, KeyValueView, and SQL.
---

# Connect With the Java Thin Client

## Introduction

You have a running cluster and a loaded dataset. In the first tutorial, you built the infrastructure with Docker and created 11 tables with SQL DDL. In the second, you explored the data through the SQL CLI. Now you connect a Java application and survey the API surface that the thin client provides.

The GridGain 9 Java thin client exposes four API surfaces through a single connection:

- **SQL** runs queries against tables in the cluster.
- **Tables** provides typed object operations over rows.
- **Catalog** manages schema from Java annotations.
- **Transactions** coordinates ACID operations across tables.

You start with the connection and work through four actions:

- **Define a table schema** from an annotated Java class.
- **Navigate the Table package** to reach different views of the same data.
- **Read the same row through each view** to see what the variants offer.
- **Close with a SQL query** that joins your new table with the existing Music Store catalog.

## Prerequisites

- **A running 3-node cluster with the Music Store dataset** from [Start Your Local GridGain 9 Development Cluster](start-local-cluster.md)
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

- How the thin client connects with partition awareness
- The four API surfaces: SQL, Tables, Catalog, and Transactions
- How annotations define distributed table schema (schema-as-code)
- How to navigate the Table package from client to view
- How RecordView, KeyValueView, and SQL access the same data differently

## What You Will Build

A Java application that connects to your 3-node cluster, creates a table from an annotated Java class, writes and reads data through RecordView, previews KeyValueView access to the same rows, and queries the data with SQL.

## Step 1: Create the Project

Create a directory for the project and add a `pom.xml` with the GridGain thin client dependency:

```bash
mkdir java-client-demo && cd java-client-demo
```

{% code title="pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>java-client-demo</artifactId>
    <version>1.0.0</version>

    <properties>
        <maven.compiler.release>17</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <repositories>
        <repository>
            <id>gridgain-external</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>ignite-client</artifactId>
            <!-- Use the latest GridGain 9 version -->
            <version>LATEST_GRIDGAIN_9_VERSION</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.4.1</version>
                <configuration>
                    <mainClass>com.example.musicstore.MusicStoreClient</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
{% endcode %}

The group ID is `org.gridgain`, but the artifact name keeps the `ignite-` prefix. All Java packages remain `org.apache.ignite.*`.

{% hint style="info" %}
GridGain 9 artifacts are hosted on the GridGain Nexus repository, not Maven Central. The `<repositories>` block in the `pom.xml` above is required. Without it, Maven will fail with `Could not find artifact org.gridgain:ignite-client`.
{% endhint %}

The `ignite-client` dependency is the only one you need. It pulls in `ignite-api` (which contains the annotation classes and table interfaces) as a transitive dependency.

Create the source directory and an empty main class:

```bash
mkdir -p src/main/java/com/example/musicstore
```

{% code title="src/main/java/com/example/musicstore/MusicStoreClient.java" %}
```java
package com.example.musicstore;

public class MusicStoreClient {
    public static void main(String[] args) {
        System.out.println("Project compiles.");
    }
}
```
{% endcode %}

Verify the project compiles:

```bash
mvn compile exec:java
```

```text
Project compiles.
```

{% hint style="success" %}
**Checkpoint:** The project compiles and prints "Project compiles." with `mvn compile exec:java`.
{% endhint %}

## Step 2: Connect and Survey the Client

Replace the contents of `MusicStoreClient.java` with the connection code:

{% code title="src/main/java/com/example/musicstore/MusicStoreClient.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.tx.Transaction;
import java.util.logging.Level;
import java.util.logging.Logger;

public class MusicStoreClient {
    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            // The IgniteClient exposes four API surfaces:
            //
            //   client.sql()          - execute SQL queries and DML statements
            //   client.tables()       - access tables and their typed views (RecordView, KeyValueView)
            //   client.catalog()      - manage schema: create and drop tables and zones from code
            //   client.transactions() - begin explicit ACID transactions (covered later)
            //
            // This tutorial uses the first three. Each operates on the same
            // distributed catalog, so a table created through catalog() is
            // immediately queryable through sql() and accessible through tables().

            // Verify the connection by querying Music Store data loaded earlier
            try (var result = client.sql().execute((Transaction) null,
                    "SELECT COUNT(*) AS track_count FROM Track")) {
                System.out.println("Music Store tracks: "
                        + result.next().longValue("track_count"));
            }
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Key details in this code:

- **`try-with-resources`** creates the client and closes it when the block exits. The inner `try` around `execute()` closes the `ResultSet`, which releases server-side cursor resources.
- **`IgniteClient.builder().addresses(...)`** accepts multiple node addresses. The client connects to the first available node, discovers the full topology, and opens direct connections to every node. This is **partition awareness**: each operation routes directly to the node that owns the data. If a node fails, the client reconnects to the remaining nodes.
- **`client.sql().execute((Transaction) null, ...)`** runs a SQL query. The explicit `(Transaction)` cast ensures the code compiles across all GridGain 9 versions. The `null` value means the query runs in its own implicit transaction. This is the same SQL API you used through the CLI in the previous tutorial.

`System.exit(0)` after the try block forces the JVM to shut down immediately. Without it, the GridGain client's background timer thread keeps the process alive for 15 seconds after the connection closes.

Run the application:

```bash
mvn compile exec:java -q
```

```text
Connected to the cluster.
Music Store tracks: 3503
```

The `-q` flag suppresses Maven's build output so you see only the application's `System.out` lines.

{% hint style="success" %}
**Checkpoint:** The application connects to the cluster and prints "Music Store tracks: 3503".
{% endhint %}

## Step 3: Define a Table Schema With Annotations

In the first tutorial, you created tables with `CREATE TABLE` statements. The Catalog API offers an alternative: define the schema as an annotated Java class and deploy it with `client.catalog().createTable()`. This is **schema-as-code**.

Replace the contents of `MusicStoreClient.java`:

{% code title="src/main/java/com/example/musicstore/MusicStoreClient.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.catalog.annotations.Column;
import org.apache.ignite.catalog.annotations.Id;
import org.apache.ignite.catalog.annotations.Table;
import org.apache.ignite.tx.Transaction;
import java.util.logging.Level;
import java.util.logging.Logger;

public class MusicStoreClient {

    /**
     * Schema definition for the Favorite table.
     *
     * Each annotation maps to a distributed schema concept:
     *   @Table("Favorite")  - names the table in the cluster catalog
     *   @Id                 - primary key, determines which node owns each row
     *   @Column             - column definition (SQL type inferred from Java type)
     *   @Column(length=200) - adds a VARCHAR(200) constraint
     *
     * This class produces the same result as:
     *   CREATE TABLE Favorite (
     *       FavoriteId INT PRIMARY KEY,
     *       TrackId    INT,
     *       Note       VARCHAR(200)
     *   );
     *
     * Additional annotations available but not used here:
     *   @Zone        - assign to a specific distribution zone (replication, partitions)
     *   @Index       - define secondary indexes for query performance
     *   @ColumnRef   - reference columns in colocation and index definitions
     */
    @Table("Favorite")
    static class Favorite {
        @Id
        private Integer favoriteId;

        @Column
        private Integer trackId;

        @Column(length = 200)
        private String note;

        // Default constructor required for deserialization from the cluster
        Favorite() {}

        Favorite(Integer favoriteId, Integer trackId, String note) {
            this.favoriteId = favoriteId;
            this.trackId = trackId;
            this.note = note;
        }

        public Integer getFavoriteId() { return favoriteId; }
        public void setFavoriteId(Integer favoriteId) { this.favoriteId = favoriteId; }
        public Integer getTrackId() { return trackId; }
        public void setTrackId(Integer trackId) { this.trackId = trackId; }
        public String getNote() { return note; }
        public void setNote(String note) { this.note = note; }

        @Override
        public String toString() {
            return "Favorite{favoriteId=" + favoriteId
                    + ", trackId=" + trackId
                    + ", note='" + note + "'}";
        }
    }

    public static void main(String[] args) {
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            // Verify the connection against existing Music Store data
            try (var countResult = client.sql().execute((Transaction) null,
                    "SELECT COUNT(*) AS track_count FROM Track")) {
                System.out.println("Music Store tracks: "
                        + countResult.next().longValue("track_count"));
            }

            // Clean slate: drop the table if a previous run left it behind
            client.sql().execute((Transaction) null, "DROP TABLE IF EXISTS Favorite").close();

            // Deploy the schema from the annotated POJO (Catalog API)
            client.catalog().createTable(Favorite.class);
            System.out.println("Created the Favorite table from annotations.");

            // Verify: the table appears in the cluster's system catalog
            try (var tableCheck = client.sql().execute((Transaction) null,
                    "SELECT NAME, ZONE FROM SYSTEM.TABLES WHERE NAME = 'FAVORITE'")) {
                var row = tableCheck.next();
                System.out.println("Catalog entry: " + row.stringValue("NAME")
                        + " in zone " + row.stringValue("ZONE"));
            }
        }

        System.exit(0);
    }
}
```
{% endcode %}

The `@Table` annotation transforms a Java class into a distributed table definition. Three annotations define the schema:

- **`@Table("Favorite")`** names the table in the cluster catalog. Without a `@Zone` annotation, the table lands in the `Default` zone with a single replica. For development, this is fine. The Music Store tables you created in the first tutorial use an explicit `MusicStore` zone with 3 replicas, which is what you would use in production.
- **`@Id`** marks the primary key. In a distributed system, the primary key determines **partition routing**: the cluster hashes this value to decide which node owns each row. When you look up favoriteId=2, the client routes directly to the node that owns that partition.
- **`@Column`** maps a Java field to a table column. The SQL type is inferred from the Java type: `Integer` becomes `INT`, `String` becomes `VARCHAR`. The optional `length` parameter constrains the string size.

Three more annotations are available for production use:

- **`@Zone`** assigns the table to a specific distribution zone (replication factor, partition count, storage profile).
- **`@Index`** defines secondary indexes for query performance.
- **`@ColumnRef`** references columns in colocation and index definitions.

You saw the effect of colocation on join performance in the previous tutorial's EXPLAIN plans.

`DROP TABLE IF EXISTS` before `createTable()` keeps the application re-runnable. `catalog().dropTable()` has no "if exists" guard, so the SQL API handles the idempotent cleanup instead.

Run the application:

```bash
mvn compile exec:java -q
```

```text
Connected to the cluster.
Music Store tracks: 3503
Created the Favorite table from annotations.
Catalog entry: FAVORITE in zone Default
```

The annotated class produced the same result as a `CREATE TABLE` statement. The table is now in the cluster catalog alongside the 11 Music Store tables, queryable through SQL and accessible through the Table API.

{% hint style="success" %}
**Checkpoint:** The application prints "Catalog entry: FAVORITE in zone Default".
{% endhint %}

## Step 4: The Table Package

The Favorite table is in the catalog. Every interaction with table data follows a three-level path:

1. **`client.tables()`** returns the `IgniteTables` interface, the entry point for all table operations.
2. **`.table("Favorite")`** returns a `Table` object representing the physical table in the cluster.
3. From the `Table` object, you choose a **view** that determines how you interact with the data.

A single `Table` offers four primary view types, organized into two families:

| View | Method | Description |
|---|---|---|
| **RecordView&lt;Favorite&gt;** | `.recordView(Favorite.class)` | Each row is a complete typed POJO |
| **RecordView&lt;Tuple&gt;** | `.recordView()` | Each row is a dynamic Tuple (no POJO needed) |
| **KeyValueView&lt;K, V&gt;** | `.keyValueView(K.class, V.class)` | Each row split into typed key and value objects |
| **KeyValueView&lt;Tuple, Tuple&gt;** | `.keyValueView()` | Each row split into key and value Tuples |

RecordView treats each row as a single object. KeyValueView splits each row into a separate key (the `@Id` columns) and value (everything else). Both families offer typed (POJO) and untyped (Tuple) variants. All four views read and write the same underlying data. The next tutorial covers the full RecordView and KeyValueView operation set.

Add the following code after the `System.out.println("Catalog entry: ..."` line, before the closing `}` of the try block:

```java
            // Add after the catalog entry verification, inside the try block

            // --- Navigate the Table package ---

            // Level 1: IgniteTables - entry point for all table operations
            var tables = client.tables();

            // Level 2: Table - represents the physical table in the cluster
            var favoriteTable = tables.table("Favorite");

            // Level 3: RecordView - typed POJO access to table rows
            var favorites = favoriteTable.recordView(Favorite.class);

            // RecordView offers four categories of write operations:
            //   upsert / upsertAll   - insert or update (idempotent)
            //   insert / insertAll   - insert only, returns false if the key exists
            //   replace              - update only, returns false if the key is missing
            //   delete / deleteAll   - remove by key
            //
            // Each category has sync, async (CompletableFuture), and bulk variants.
            // This tutorial uses upsert and get. The next tutorial covers the full set.

            // Batch write: upsertAll sends all records in a single network round-trip
            var favList = java.util.List.of(
                    new Favorite(1, 1613, "Eight minutes of rock history"),
                    new Favorite(2, 2254, "Six sections, zero repetition"),
                    new Favorite(3, 1990, "Four chords that ended the 1980s"));
            favorites.upsertAll(null, favList);
            System.out.println("Saved " + favList.size() + " favorites via RecordView.");

            // Key-based read: get routes directly to the partition that owns favoriteId=2
            // Only the @Id field needs a value; non-key fields are null in the lookup key
            Favorite retrieved = favorites.get(null, new Favorite(2, null, null));
            System.out.println("RecordView lookup: " + retrieved);
```

`upsertAll()` writes all three records in a single call. The operation is idempotent: running the application twice overwrites existing rows instead of failing on duplicate keys. The first parameter is the transaction context: `null` means each operation runs in its own implicit transaction.

`get()` performs a key-based lookup. The client uses the `@Id` field to compute the partition hash and routes the request directly to the node that owns that partition. Only the key field needs a value in the lookup object; the cluster fills in the remaining columns from storage and returns the complete record.

The three TrackIds (1613, 2254, 1990) reference real rows in the Music Store's `Track` table. Step 5 resolves these IDs to track names with a SQL JOIN.

Run the application:

```bash
mvn compile exec:java -q
```

```text
Connected to the cluster.
Music Store tracks: 3503
Created the Favorite table from annotations.
Catalog entry: FAVORITE in zone Default
Saved 3 favorites via RecordView.
RecordView lookup: Favorite{favoriteId=2, trackId=2254, note='Six sections, zero repetition'}
```

{% hint style="success" %}
**Checkpoint:** The application prints "Saved 3 favorites via RecordView." and retrieves favorite 2 with trackId 2254.
{% endhint %}

## Step 5: Access the Same Data Through KeyValueView and SQL

The three favorites you wrote through RecordView are visible to every other view of the same table. This step reads the same data through an untyped KeyValueView lookup and a SQL JOIN that crosses zone boundaries.

Add the following code after the `System.out.println("RecordView lookup: ..."` line, before the closing `}` of the try block:

```java
            // Add after the RecordView lookup, inside the try block

            // --- KeyValueView: the same table, split into key and value ---

            // The untyped KeyValueView uses Tuple instead of POJOs.
            // Key Tuple contains only the @Id columns.
            // Value Tuple contains the remaining columns.
            var kvView = favoriteTable.keyValueView();

            var key = org.apache.ignite.table.Tuple.create()
                    .set("favoriteId", 2);
            var value = kvView.get(null, key);
            System.out.println("KeyValueView lookup: trackId="
                    + value.intValue("trackId")
                    + ", note=" + value.stringValue("note"));

            // --- SQL: the same table, accessed through queries ---

            // SQL joins the Favorite table (Default zone, created from annotations)
            // with the Track table (MusicStore zone, created from DDL earlier).
            // Zone assignment controls replication policy, not query interoperability.
            System.out.println("\nFavorites with track names (SQL JOIN):");
            try (var joinResult = client.sql().execute((Transaction) null,
                    "SELECT f.FavoriteId, t.Name AS Track, f.Note "
                    + "FROM Favorite f "
                    + "JOIN Track t ON f.TrackId = t.TrackId "
                    + "ORDER BY f.FavoriteId")) {

                while (joinResult.hasNext()) {
                    var r = joinResult.next();
                    System.out.println("  " + r.intValue("FavoriteId") + ": "
                            + r.stringValue("Track") + " - "
                            + r.stringValue("Note"));
                }
            }
```

Three access patterns, one table:

- **KeyValueView** splits each row into a **key** (the `@Id` columns) and a **value** (everything else). The `keyValueView()` call here returns the untyped `KeyValueView<Tuple, Tuple>`. A typed variant, `keyValueView(Key.class, Value.class)`, maps to POJOs instead. The next tutorial covers both.
- **Tuple** is GridGain's dynamic column container. Write with `.set("favoriteId", 2)`. Read with typed accessors: `.intValue("trackId")`, `.stringValue("note")`. No POJO class required.
- **SQL JOIN** confirms that data written through RecordView appears immediately in SQL queries. It also confirms that tables in different zones (Favorite in Default, Track in MusicStore) join without additional configuration.

Run the application:

```bash
mvn compile exec:java -q
```

```text
Connected to the cluster.
Music Store tracks: 3503
Created the Favorite table from annotations.
Catalog entry: FAVORITE in zone Default
Saved 3 favorites via RecordView.
RecordView lookup: Favorite{favoriteId=2, trackId=2254, note='Six sections, zero repetition'}
KeyValueView lookup: trackId=2254, note=Six sections, zero repetition

Favorites with track names (SQL JOIN):
  1: Stairway To Heaven - Eight minutes of rock history
  2: Bohemian Rhapsody - Six sections, zero repetition
  3: Smells Like Teen Spirit - Four chords that ended the 1980s
```

The same favoriteId=2 record appears three times across three access patterns: as a `Favorite` POJO from RecordView, as a key-value Tuple pair from KeyValueView, and as a joined SQL row with the track name resolved. One schema, multiple views.

{% hint style="success" %}
**Checkpoint:** The KeyValueView lookup returns trackId=2254. The SQL JOIN returns all 3 favorites with track names from the Music Store.
{% endhint %}

## Step 6: Clean Up

In Step 3, you used `client.catalog().createTable()` to deploy a schema. The Catalog API also handles the reverse: `dropTable()` removes a table from the cluster. Drop the Favorite table so future tutorials start with a clean 11-table schema.

Add the following code after the `while` loop that prints the favorites, before the closing `}` of the try block:

```java
            // Add after the SQL JOIN loop, inside the try block

            // Clean up: drop the Favorite table using the Catalog API
            client.catalog().dropTable("Favorite");
            System.out.println("\nDropped the Favorite table.");

            // Verify: Favorite is gone, Music Store tables are intact
            try (var verifyDrop = client.sql().execute((Transaction) null,
                    "SELECT COUNT(*) AS remaining FROM SYSTEM.TABLES "
                    + "WHERE NAME = 'FAVORITE'")) {
                System.out.println("Favorite table count: "
                        + verifyDrop.next().longValue("remaining"));
            }

            try (var totalTables = client.sql().execute((Transaction) null,
                    "SELECT COUNT(*) AS total FROM SYSTEM.TABLES")) {
                System.out.println("Total tables: "
                        + totalTables.next().longValue("total"));
            }
```

The Catalog API also includes methods not used in this tutorial:

- **`createZone(ZoneDefinition)`** and **`dropZone(String)`** manage distribution zones programmatically, the same zones you created with `CREATE ZONE` in the first tutorial.
- **`tableDefinition(String)`** and **`zoneDefinition(String)`** inspect existing schema definitions.

Every Catalog and Table API method has an async variant that returns `CompletableFuture` for non-blocking workflows.

Run the complete application one final time:

```bash
mvn compile exec:java -q
```

```text
Connected to the cluster.
Music Store tracks: 3503
Created the Favorite table from annotations.
Catalog entry: FAVORITE in zone Default
Saved 3 favorites via RecordView.
RecordView lookup: Favorite{favoriteId=2, trackId=2254, note='Six sections, zero repetition'}
KeyValueView lookup: trackId=2254, note=Six sections, zero repetition

Favorites with track names (SQL JOIN):
  1: Stairway To Heaven - Eight minutes of rock history
  2: Bohemian Rhapsody - Six sections, zero repetition
  3: Smells Like Teen Spirit - Four chords that ended the 1980s

Dropped the Favorite table.
Favorite table count: 0
Total tables: 11
```

The `Favorite` table is gone and all 11 Music Store tables remain intact.

{% hint style="success" %}
**Checkpoint:** The Favorite table count is 0. The total table count is 11.
{% endhint %}

## Summary

You connected a Java application to the GridGain 9 cluster and exercised the thin client's four API surfaces. Here is a map of every API call you made, organized by the surface it belongs to.

### DDL, DML, and Where SQL Fits

The thin client separates schema management from data operations:

- **`client.catalog()`** is the **DDL surface**. It manages tables and zones from Java code.
- **`client.tables()`** is the **DML surface**. It reads and writes data through typed views.
- **`client.sql()`** **crosses both**. `CREATE TABLE` is DDL through SQL. `SELECT` is DML through SQL.
- **`client.transactions()`** coordinates ACID transactions across multiple operations.

| Operation | Surface | Step |
|---|---|---|
| `catalog().createTable(Favorite.class)` | DDL via Catalog API | Step 3 |
| `catalog().dropTable("Favorite")` | DDL via Catalog API | Step 6 |
| `sql().execute("DROP TABLE IF EXISTS ...")` | DDL via SQL API | Step 3 |
| `sql().execute("SELECT COUNT(*) ...")` | DML via SQL API | Steps 2, 5, 6 |
| `favorites.upsertAll(...)` | DML via Table API (RecordView) | Step 4 |
| `favorites.get(...)` | DML via Table API (RecordView) | Step 4 |
| `kvView.get(...)` | DML via Table API (KeyValueView) | Step 5 |

### Schema-as-code

Annotations define the schema in Java:

- **`@Table`** names the table that the Catalog API creates.
- **`@Id`** marks the primary key, which determines partition routing.
- **`@Column`** maps each field to a column in the table.

`client.catalog().createTable(Favorite.class)` deploys the schema. The result is identical to the `CREATE TABLE` statements you wrote in the first tutorial. Additional annotations (`@Zone`, `@Index`, `@ColumnRef`) handle distribution zones, secondary indexes, and colocation.

### The Table Package Hierarchy

Every data interaction follows the same three-level path: `client.tables()` returns `IgniteTables`, `.table("Favorite")` returns the physical `Table`, and from there you choose a **view**. A single `Table` offers four primary view types across two families: **RecordView** (each row is one object) and **KeyValueView** (each row split into key and value). Both families offer typed (POJO) and untyped (Tuple) variants.

### One table, Multiple Access Patterns

You accessed the same favoriteId=2 record three ways: as a `Favorite` POJO through RecordView, as a key-value Tuple pair through KeyValueView, and as a joined SQL row with the track name resolved. All views read and write the same underlying data. Choose RecordView for type-safe business logic, KeyValueView for key-oriented access patterns, and SQL for queries that are easier to express relationally (joins, aggregations, filtering across tables).

## Next Step

Continue to [Work with RecordView and KeyValueView](recordview-keyvalueview.md) to work with the Music Store dataset: insert, replace, delete, bulk operations, and the criteria for choosing between views.

## Related

- [Start Your Local GridGain 9 Development Cluster](start-local-cluster.md) for the cluster setup and dataset this tutorial connects to
- [Create Tables and Query Data with SQL](query-music-store-sql.md) for the SQL patterns you saw through the CLI
- [How to Configure Logging for the Java Thin Client](../../gridgain9-development/configuring-java-client-logging.md) for controlling log output in your application
