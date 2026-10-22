---
description: >-
  Master both Table API view types: CRUD operations, bulk processing, cache-aside patterns, and the unified storage model that eliminates separate caching infrastructure.
---

# Work With RecordView and KeyValueView

<!-- TODO (low): The "Java 17 or later" prerequisite is the tutorial's own choice. The GridGain 9.1.28 client is built for Java 11. Compiled with `javac --release 11`, the samples on this page build except `BulkOps` (it calls `Stream.toList()`, which needs Java 16). Decide whether to keep "Java 17" (one prerequisite for the whole tutorial series) or say "Java 11 or later" on the pages whose samples allow it, then delete this comment. -->

## Introduction

In the previous tutorial, you connected a Java application to the cluster and used RecordView and KeyValueView for basic reads and writes. You saw that both views access the same underlying data. Now you learn the full operation set and discover something more significant: KeyValueView gives you cache-like semantics backed directly by the system of record.

In a traditional architecture, you maintain a cache (Redis, Memcached) alongside your database and write invalidation logic to keep them synchronized. That synchronization is a source of bugs, staleness, and operational complexity.

With GridGain, there is no separate cache. A `put` through KeyValueView writes to the same distributed storage that SQL queries read. There is nothing to invalidate.

This tutorial starts with the API mechanics (operations, conditionals, bulk processing), moves to multi-column tables and partial POJO mapping, then pivots to the caching patterns that make this architecture practical.

## Prerequisites

- **A running 3-node cluster with the Music Store dataset** from [Start Your Local GridGain 9 Development Cluster](start-local-cluster.md)
- **Completed** [Connect with the Java Thin Client](connect-java-thin-client.md) (familiarity with the thin client, Maven project setup, and RecordView basics)
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

- How to perform single-record and bulk operations with RecordView
- How to access tables as key-value pairs with KeyValueView
- How both views share the same underlying data
- How to map partial POJOs to wide tables for efficient access
- How to use KeyValueView as a cache backed by the system of record
- When to choose RecordView vs KeyValueView for your use case

## What You Will Build

A structured Java project with domain model classes and a series of exploration classes that exercise the full RecordView and KeyValueView operation set against the Music Store dataset. The `model` package holds 3 stable POJO classes that map to cluster tables. Each step creates a new Java class file in the main package, so your previous code stays in the project for reference. You end up with 8 exploration classes plus the 3 model classes.

The progression starts with API mechanics on the 2-column Artist table. It then moves to partial POJO mapping on the 13-column Customer table. The final steps cover cache-aside patterns that show why GridGain's unified model eliminates the need for a separate caching layer. All write operations use Artist IDs above the existing dataset range and clean up after themselves.

## Set Up the Project

Create a new project directory and set up a Maven project with the GridGain thin client dependency. The structure is the same as the previous tutorial.

```bash
mkdir table-api-demo && cd table-api-demo
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
    <artifactId>table-api-demo</artifactId>
    <version>1.0.0</version>

    <properties>
        <maven.compiler.release>17</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.musicstore.ConnectAndVerify</exec.mainClass>
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
            <version>9.1.28</version>
        </dependency>
    </dependencies>

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

The group ID is `org.gridgain`, but the artifact name keeps the `ignite-` prefix. All Java packages remain `org.apache.ignite.*`.

{% hint style="info" %}
GridGain 9 artifacts are hosted on the GridGain Nexus repository, not Maven Central. The `<repositories>` block in the `pom.xml` above is required. Without it, Maven will fail with `Could not find artifact org.gridgain:ignite-client`.
{% endhint %}

Create the source directories:

```bash
mkdir -p src/main/java/com/example/musicstore/model
```

{% code title="src/main/java/com/example/musicstore/model/Artist.java" %}
```java
package com.example.musicstore.model;

/**
 * Domain model for the Music Store Artist table (2 columns).
 *
 * GridGain maps POJO fields to table columns by name (case-insensitive):
 *   artistId  ->  ARTISTID  (primary key, INT32)
 *   name      ->  NAME      (STRING / VARCHAR)
 *
 * No @Table or @Id annotations are needed because the Artist table already
 * exists in the cluster (created by the Music Store DDL in the start local cluster tutorial). Annotations
 * are only required when creating a table from code with the Catalog API.
 *
 * POJO requirements for GridGain table mapping:
 *   - No-arg constructor (GridGain calls this when deserializing rows from the cluster)
 *   - Getter/setter pair for each mapped field
 *   - Field names must match column names (case-insensitive)
 *   - Every field must map to a table column. A field with no matching
 *     column makes the call fail with a MarshallerException
 *     ("Fields [...] are not mapped to columns")
 *
 * For key-based lookups, only the primary key field needs a value.
 * new Artist(1, null) tells GridGain: find ARTISTID=1, fill in
 * NAME from storage. The client hashes the key to determine which
 * cluster node owns that partition and routes the request directly.
 */
public class Artist {
    private Integer artistId;
    private String name;

    /** Required: GridGain calls this when deserializing rows from the cluster. */
    public Artist() {}

    /**
     * Convenience constructor for creating lookup keys and test data.
     *
     * @param artistId primary key (required for all operations)
     * @param name     artist name (null for key-only lookups)
     */
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
        return "Artist{id=" + artistId + ", name='" + name + "'}";
    }
}
```
{% endcode %}

The `model` package holds your domain classes. These are stable artifacts that don't change as you explore different API operations. The `Artist` class maps to the existing `Artist` table in the cluster. Field names match column names (case-insensitive), and the no-arg constructor is required for GridGain to deserialize rows from the cluster.

Now create `ConnectAndVerify.java`:

{% code title="src/main/java/com/example/musicstore/ConnectAndVerify.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Artist;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.logging.Level;
import java.util.logging.Logger;

public class ConnectAndVerify {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            // Navigate the Table package: client.tables() -> table("Artist") -> recordView()
            // The Artist POJO in model/ maps fields to columns by name. RecordView<Artist>
            // gives typed access: each row becomes an Artist object.
            Table artistTable = client.tables().table("Artist");
            RecordView<Artist> artists = artistTable.recordView(Artist.class);

            // Key-based read: only the primary key field needs a value.
            // new Artist(1, null) tells GridGain: find ARTISTID=1, fill in NAME from storage.
            // The client hashes the key to route directly to the owning partition.
            Artist acdc = artists.get((Transaction) null, new Artist(1, null));
            System.out.println("Artist 1: " + acdc);
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

The project has two source files: the `Artist` model in the `model` package and `ConnectAndVerify` as the first exploration class. The model classes are stable artifacts that map your domain to the cluster. Each subsequent step creates a new Java class in the main package, so your previous code stays in the project for reference.

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.ConnectAndVerify -q
```

```text
Connected to the cluster.
Artist 1: Artist{id=1, name='AC/DC'}
```

{% hint style="success" %}
**Checkpoint:** The application connects and prints Artist 1 as "AC/DC".
{% endhint %}

## RecordView Single-Record Operations

You can read an existing artist by key. Now work through the full set of single-record write operations. Each operation has different semantics for handling existing and missing records, and the distinction matters when multiple threads or services access the same data.

All write operations in this step use ArtistId values starting at 10001, safely above the 275 existing Music Store artists.

Create `RecordViewOps.java` in the same package:

{% code title="src/main/java/com/example/musicstore/RecordViewOps.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Artist;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.logging.Level;
import java.util.logging.Logger;

public class RecordViewOps {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            // Navigate the Table package: client.tables() -> table() -> recordView()
            Table artistTable = client.tables().table("Artist");
            RecordView<Artist> artists = artistTable.recordView(Artist.class);

            // RecordView offers four categories of single-record write operations:
            //
            //   upsert       - insert or update (idempotent, always succeeds)
            //   insert       - create only, returns false if key exists (lost-update prevention)
            //   replace      - update only, returns false if key missing (guards against phantom writes)
            //   delete       - remove by key, returns true if found
            //   getAndDelete - atomic read-and-remove in one round-trip
            //
            // Each has async (CompletableFuture) and bulk variants.

            // --- get: key-based read routes directly to the partition that owns ArtistId=1 ---
            // Only the primary key field needs a value; non-key fields are null in the lookup key
            Artist existing = artists.get((Transaction) null, new Artist(1, null));
            System.out.println("get(1): " + existing);

            // --- upsert: idempotent insert-or-update ---
            // Always succeeds: creates the row if missing, overwrites if present.
            // Safe for retries and idempotent event handlers.
            artists.upsert((Transaction) null, new Artist(10001, "Tutorial Artist"));
            Artist upserted = artists.get((Transaction) null, new Artist(10001, null));
            System.out.println("After upsert(10001): " + upserted);

            // Upsert again with a different name: the existing row is silently overwritten
            artists.upsert((Transaction) null, new Artist(10001, "Updated Tutorial Artist"));
            Artist updated = artists.get((Transaction) null, new Artist(10001, null));
            System.out.println("After upsert update: " + updated);

            // --- insert: create-only with lost-update prevention ---
            // Returns true on success, false if the key already exists.
            // The existing row is never touched. In concurrent systems, insert
            // prevents one thread from silently overwriting data written by another.
            boolean inserted = artists.insert((Transaction) null,
                    new Artist(10002, "Insert Test Artist"));
            System.out.println("insert(10002): " + inserted);

            // Second insert for the same key: returns false, original row unchanged
            boolean insertAgain = artists.insert((Transaction) null,
                    new Artist(10002, "Duplicate Insert"));
            System.out.println("insert(10002) again: " + insertAgain);

            // --- replace: update-only, guards against phantom writes ---
            // Returns true when the key exists and the row is updated.
            // Returns false when the key is missing; no row is created.
            // Use replace when updating a record that should already exist:
            // a false return means something unexpected happened upstream.
            boolean replaced = artists.replace((Transaction) null,
                    new Artist(10001, "Replaced Artist"));
            System.out.println("replace(10001): " + replaced);

            boolean replaceGhost = artists.replace((Transaction) null,
                    new Artist(10099, "Ghost Artist"));
            System.out.println("replace(10099 non-existent): " + replaceGhost);

            Artist afterReplace = artists.get((Transaction) null, new Artist(10001, null));
            System.out.println("After replace: " + afterReplace);

            // --- delete: remove by key ---
            // Returns true if the key existed and was removed, false if absent
            boolean deleted = artists.delete((Transaction) null, new Artist(10002, null));
            System.out.println("delete(10002): " + deleted);

            // Second delete for the same key: returns false (already removed)
            boolean deleteAgain = artists.delete((Transaction) null, new Artist(10002, null));
            System.out.println("delete(10002) again: " + deleteAgain);

            // --- getAndDelete: atomic read-and-remove in one network round-trip ---
            // Returns the complete record as it existed immediately before deletion.
            // After this call, get() for the same key returns null.
            // Useful for queue-like patterns where you need the data one last time.
            artists.insert((Transaction) null, new Artist(10003, "GetAndDelete Artist"));
            Artist gotAndDeleted = artists.getAndDelete((Transaction) null,
                    new Artist(10003, null));
            System.out.println("getAndDelete(10003): " + gotAndDeleted);

            Artist afterGetAndDelete = artists.get((Transaction) null,
                    new Artist(10003, null));
            System.out.println("get(10003) after getAndDelete: " + afterGetAndDelete);

            // Clean up remaining test data
            artists.delete((Transaction) null, new Artist(10001, null));
            System.out.println("\nCleaned up test data.");
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.RecordViewOps -q
```

Each step creates a new class and uses the `-Dexec.mainClass` flag to run it. Your previous step's code remains in the project for reference.

```text
Connected to the cluster.
get(1): Artist{id=1, name='AC/DC'}
After upsert(10001): Artist{id=10001, name='Tutorial Artist'}
After upsert update: Artist{id=10001, name='Updated Tutorial Artist'}
insert(10002): true
insert(10002) again: false
replace(10001): true
replace(10099 non-existent): false
After replace: Artist{id=10001, name='Replaced Artist'}
delete(10002): true
delete(10002) again: false
getAndDelete(10003): Artist{id=10003, name='GetAndDelete Artist'}
get(10003) after getAndDelete: null
Cleaned up test data.
```

Three distinct write strategies emerged from that output:

**`upsert`** always succeeds. It inserts a new row or overwrites an existing one. This is the right choice when you want idempotent writes and don't care whether the record existed before.

**`insert`** is the create-only counterpart. It returns `true` when it creates a new row and `false` when the key already exists. The existing row is never touched. In concurrent systems, `insert` prevents one thread from silently overwriting data written by another.

**`replace`** is the update-only counterpart. It returns `true` when it updates an existing row and `false` when the key is missing. It never creates a new row. Use `replace` when updating a record that should already exist: a missing row means something unexpected happened.

**`getAndDelete`** retrieves and removes a record in a single atomic operation. The returned `Artist` contains the data as it existed immediately before deletion. After the call, `get()` for the same key returns `null`. This is useful for queue-like patterns where you need the data one last time before removing it.

All operations pass `(Transaction) null` for the transaction parameter. The explicit `(Transaction)` cast ensures the code compiles across all GridGain 9 versions. The `null` value means each operation runs in its own implicit transaction. Explicit transactions are covered in the next tutorial.

{% hint style="success" %}
**Checkpoint:** Each operation prints its result. insert returns false on duplicate, replace returns false on missing key, getAndDelete returns the record then null on re-read.
{% endhint %}

## RecordView Bulk Operations

Single-record operations make one network round-trip per call. When you need to process multiple records, bulk operations send all of them in a single request. The cluster handles routing each record to the correct partition internally.

Create `BulkOps.java`:

{% code title="src/main/java/com/example/musicstore/BulkOps.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Artist;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.Collection;
import java.util.List;
import java.util.Objects;
import java.util.logging.Level;
import java.util.logging.Logger;

public class BulkOps {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            Table artistTable = client.tables().table("Artist");
            RecordView<Artist> artists = artistTable.recordView(Artist.class);

            // Bulk operations send all records in one network round-trip.
            // The client partitions the batch internally and routes each record
            // to the node that owns its partition. Compared to N individual calls,
            // a bulk operation is one round-trip instead of N.
            //
            // Bulk variants:
            //   upsertAll  - batch insert-or-update (idempotent)
            //   insertAll  - batch create-only, returns records whose keys already existed
            //   getAll     - batch read by key, returns null for missing keys
            //   deleteAll  - batch remove, returns records that were not found

            // --- upsertAll: write 5 records in a single network round-trip ---
            List<Artist> batch = List.of(
                    new Artist(10001, "Bulk Artist 1"),
                    new Artist(10002, "Bulk Artist 2"),
                    new Artist(10003, "Bulk Artist 3"),
                    new Artist(10004, "Bulk Artist 4"),
                    new Artist(10005, "Bulk Artist 5"));

            artists.upsertAll((Transaction) null, batch);
            System.out.println("upsertAll: inserted " + batch.size() + " artists.");

            // --- getAll: retrieve multiple records by key in one round-trip ---
            // The list includes ArtistId 10099, which does not exist
            List<Artist> keys = List.of(
                    new Artist(10001, null), new Artist(10002, null),
                    new Artist(10003, null), new Artist(10004, null),
                    new Artist(10005, null), new Artist(10099, null));

            Collection<Artist> results = artists.getAll((Transaction) null, keys);

            // getAll returns one entry per input key, including null for missing keys.
            // This differs from KeyValueView's getAll, which returns a Map that
            // simply omits missing keys. Filter nulls to find the records that exist.
            List<Artist> found = results.stream()
                    .filter(Objects::nonNull)
                    .toList();
            System.out.println("getAll (6 keys, 5 exist): found "
                    + found.size() + " records");
            for (Artist a : found) {
                System.out.println("  " + a);
            }

            // --- deleteAll: remove multiple records in one round-trip ---
            // Returns a collection of records that were NOT deleted (not found).
            // An empty return means every key was found and removed.
            List<Artist> deleteKeys = List.of(
                    new Artist(10001, null), new Artist(10002, null),
                    new Artist(10003, null), new Artist(10004, null),
                    new Artist(10005, null));

            Collection<Artist> notDeleted = artists.deleteAll(
                    (Transaction) null, deleteKeys);
            System.out.println("deleteAll: not-deleted count = " + notDeleted.size());

            // Verify: all test artists are gone
            Collection<Artist> verify = artists.getAll(
                    (Transaction) null, deleteKeys);
            long remaining = verify.stream()
                    .filter(Objects::nonNull)
                    .count();
            System.out.println("Verification: " + remaining
                    + " test artists remain.");
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.BulkOps -q
```

```text
Connected to the cluster.
upsertAll: inserted 5 artists.
getAll (6 keys, 5 exist): found 5 records
  Artist{id=10001, name='Bulk Artist 1'}
  Artist{id=10002, name='Bulk Artist 2'}
  Artist{id=10003, name='Bulk Artist 3'}
  Artist{id=10004, name='Bulk Artist 4'}
  Artist{id=10005, name='Bulk Artist 5'}
deleteAll: not-deleted count = 0
Verification: 0 test artists remain.
```

Key details in this code:

- **`upsertAll`** writes all 5 records in a single network request. The cluster routes each record to the node that owns its partition. Compared to 5 individual `upsert` calls, this is one round-trip instead of five.

- **`getAll`** returns a collection with one entry per input key. Keys that exist produce their corresponding `Artist` object; keys that do not exist produce `null`. The code filters nulls to count only the records that were found. This behavior differs from KeyValueView's `getAll`, which you see in the next step.

- **`deleteAll`** returns a collection of records that were **not** deleted (because they did not exist). An empty return collection means every key was found and removed.

{% hint style="success" %}
**Checkpoint:** The verification prints "0 test artists remain." All 5 records were written and deleted in single bulk calls.
{% endhint %}

## KeyValueView Operations

RecordView maps each table row to a complete POJO. KeyValueView offers an alternative: it splits each row into a separate key type and value type, providing a Map-like interface to the same underlying data.

For the Artist table with its two columns (ArtistId and Name), `KeyValueView<Integer, String>` maps the primary key column to `Integer` and the single non-key column to `String`. The table is the same; only the API shape changes.

Create `KeyValueViewOps.java`:

{% code title="src/main/java/com/example/musicstore/KeyValueViewOps.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.Collection;
import java.util.Map;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

public class KeyValueViewOps {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            Table artistTable = client.tables().table("Artist");

            // KeyValueView splits each row into a key type and a value type.
            // For Artist (2 columns): Integer maps to the ARTISTID primary key column,
            // String maps to the single non-key column NAME.
            // The table is the same as RecordView; only the API shape changes.
            KeyValueView<Integer, String> kvView =
                    artistTable.keyValueView(Integer.class, String.class);

            // KeyValueView offers the same four categories as RecordView,
            // with Map-like naming:
            //
            //   put          - insert or update (equivalent to RecordView.upsert)
            //   putIfAbsent  - create only, prevents concurrent overwrites (equivalent to insert)
            //   replace      - update only, guards against phantom writes
            //   remove       - delete by key (equivalent to delete)
            //   getAndRemove - atomic read-and-remove (equivalent to getAndDelete)
            //
            // The behavioral semantics are identical to RecordView counterparts.

            // --- get: returns just the value column, not a full POJO ---
            // The client routes directly to the partition that owns ArtistId=1
            String name = kvView.get((Transaction) null, 1);
            System.out.println("get(1): " + name);

            // --- put: idempotent insert-or-update (same as RecordView.upsert) ---
            kvView.put((Transaction) null, 10001, "KV Artist");
            String afterPut = kvView.get((Transaction) null, 10001);
            System.out.println("After put(10001): " + afterPut);

            // --- putIfAbsent: create-only with lost-update prevention ---
            // Returns false if the key already exists; the existing value is untouched.
            // Equivalent to RecordView.insert. Prevents concurrent overwrites.
            boolean absent = kvView.putIfAbsent((Transaction) null,
                    10001, "Should Not Overwrite");
            System.out.println("putIfAbsent(10001): " + absent);
            String afterPutIfAbsent = kvView.get((Transaction) null, 10001);
            System.out.println("Value after putIfAbsent: " + afterPutIfAbsent);

            // --- replace: update-only (fails if key is missing) ---
            boolean replaced = kvView.replace((Transaction) null,
                    10001, "Replaced KV Artist");
            System.out.println("replace(10001): " + replaced);

            boolean replaceGhost = kvView.replace((Transaction) null,
                    10099, "Ghost");
            System.out.println("replace(10099 non-existent): " + replaceGhost);

            // --- remove: delete by key, returns true if found ---
            boolean removed = kvView.remove((Transaction) null, 10001);
            System.out.println("remove(10001): " + removed);

            // --- Bulk operations: same round-trip optimization as RecordView ---
            System.out.println("\n--- Bulk Operations ---");

            // putAll: batch write in one round-trip (same as RecordView.upsertAll)
            Map<Integer, String> batch = Map.of(
                    10001, "KV Bulk 1",
                    10002, "KV Bulk 2",
                    10003, "KV Bulk 3");

            kvView.putAll((Transaction) null, batch);
            System.out.println("putAll: stored " + batch.size() + " entries.");

            // getAll returns a Map containing only keys that were found.
            // Missing keys are simply absent from the result.
            // This differs from RecordView's getAll, which returns null entries
            // for missing keys. Check Map.containsKey instead of filtering nulls.
            Set<Integer> lookupKeys = Set.of(10001, 10002, 10003, 10099);
            Map<Integer, String> found = kvView.getAll(
                    (Transaction) null, lookupKeys);
            System.out.println("getAll (4 keys, 3 exist): found "
                    + found.size() + " entries");
            found.forEach((k, v) -> System.out.println("  " + k + " -> " + v));

            // removeAll returns keys that were NOT found (not removed).
            // An empty return means every key was found and removed.
            Collection<Integer> notRemoved = kvView.removeAll(
                    (Transaction) null, Set.of(10001, 10002, 10003));
            System.out.println("removeAll: not-removed count = "
                    + notRemoved.size());

            // Final verification: original Music Store data is untouched
            String finalCheck = kvView.get((Transaction) null, 1);
            System.out.println("\nFinal check - Artist 1: " + finalCheck);
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.KeyValueViewOps -q
```

```text
Connected to the cluster.
get(1): AC/DC
After put(10001): KV Artist
putIfAbsent(10001): false
Value after putIfAbsent: KV Artist
replace(10001): true
replace(10099 non-existent): false
remove(10001): true

--- Bulk Operations ---
putAll: stored 3 entries.
getAll (4 keys, 3 exist): found 3 entries
  10001 -> KV Bulk 1
  10002 -> KV Bulk 2
  10003 -> KV Bulk 3
removeAll: not-removed count = 0

Final check - Artist 1: AC/DC
```

The KeyValueView operation names differ from RecordView, but the semantics are identical:

| KeyValueView | RecordView equivalent | Behavior |
|---|---|---|
| `put` | `upsert` | Insert or update (idempotent) |
| `putIfAbsent` | `insert` | Create only, returns `false` if key exists |
| `replace` | `replace` | Update only, returns `false` if key missing |
| `remove` | `delete` | Remove by key, returns `true` if found |
| `putAll` | `upsertAll` | Batch insert or update |
| `getAll` | `getAll` | Batch read by keys |
| `removeAll` | `deleteAll` | Batch remove by keys |

Notice how `get(1)` returned the string `"AC/DC"` directly, not an `Artist` POJO. KeyValueView strips away the object wrapper and gives you just the value column.

One behavioral difference to note between the two `getAll` calls:

- **`KeyValueView.getAll`** returns a `Map` containing only the keys that were found. The missing key (10099) is absent from the result.
- **`RecordView.getAll`** returns a collection that includes `null` entries for missing keys, in the same order as the input keys.

To detect missing records, filter nulls from the RecordView collection or call `Map.containsKey` on the KeyValueView result.

{% hint style="success" %}
**Checkpoint:** Artist 1 still reads "AC/DC". All test entries are removed. The getAll Map contains 3 entries (not 4).
{% endhint %}

## Both Views, Same Data

The previous steps used RecordView and KeyValueView in separate applications. In practice, you use both views in the same application, sometimes on the same table within the same method. A write through one view is immediately visible through the other because both are wrappers over the same distributed storage.

Create `CrossView.java`:

{% code title="src/main/java/com/example/musicstore/CrossView.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Artist;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.logging.Level;
import java.util.logging.Logger;

public class CrossView {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            Table artistTable = client.tables().table("Artist");

            // Both views are client-side wrappers over the same distributed storage.
            // recordView() and keyValueView() do not create separate data structures;
            // they provide different API shapes for the same underlying table rows.
            RecordView<Artist> recordView = artistTable.recordView(Artist.class);
            KeyValueView<Integer, String> kvView =
                    artistTable.keyValueView(Integer.class, String.class);

            // Write through RecordView, read through KeyValueView:
            // the upsert writes to distributed storage, and kvView.get reads
            // from the same storage. There is no replication lag or cache sync.
            recordView.upsert((Transaction) null,
                    new Artist(10001, "Cross-View Artist"));
            String viaKv = kvView.get((Transaction) null, 10001);
            System.out.println("Written via RecordView, read via KeyValueView: "
                    + viaKv);

            // Write through KeyValueView, read through RecordView:
            // the put writes to the same storage that RecordView reads from.
            // A service can use RecordView for writes (full POJO is natural)
            // and KeyValueView for reads (only the value column needed).
            kvView.put((Transaction) null, 10001, "Updated via KV");
            Artist viaRecord = recordView.get((Transaction) null,
                    new Artist(10001, null));
            System.out.println("Written via KeyValueView, read via RecordView: "
                    + viaRecord);

            // Clean up test data
            recordView.delete((Transaction) null, new Artist(10001, null));

            // Verify original Music Store data is untouched
            String acdc = kvView.get((Transaction) null, 1);
            System.out.println("Artist 1 still intact: " + acdc);
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.CrossView -q
```

```text
Connected to the cluster.
Written via RecordView, read via KeyValueView: Cross-View Artist
Written via KeyValueView, read via RecordView: Artist{id=10001, name='Updated via KV'}
Artist 1 still intact: AC/DC
```

Both views return a reference to the same table from `client.tables().table("Artist")`. The `recordView()` and `keyValueView()` calls create client-side wrappers over the same underlying data. A row upserted through RecordView is immediately readable through KeyValueView, and a value written through KeyValueView appears in the next RecordView read.

This has a practical consequence: you can use RecordView for writes (where the full POJO is natural) and KeyValueView for reads (where you only need one column), mixing both in the same service without synchronization.

{% hint style="success" %}
**Checkpoint:** A write through one view is readable through the other. Artist 1 remains "AC/DC".
{% endhint %}

## Multi-Column Tables With Partial POJOs

The Artist table has only two columns, so `KeyValueView<Integer, String>` maps one-to-one. Real applications have tables with many columns. The Customer table has 13 columns, including address, phone, email, and support representative fields. This is where the two views diverge meaningfully.

Just as you created `Artist.java` in the `model` package in Step 1, add two new model classes for the Customer table. The first maps all 13 columns; the second maps only 5 contact-related columns.

Create `model/Customer.java`:

{% code title="src/main/java/com/example/musicstore/model/Customer.java" %}
```java
package com.example.musicstore.model;

/**
 * Full domain model for the Music Store Customer table (13 columns).
 *
 * GridGain maps all 13 fields to their corresponding table columns by name:
 *   customerId   -> CUSTOMERID   (primary key, INT32)
 *   firstName    -> FIRSTNAME    (STRING)
 *   lastName     -> LASTNAME     (STRING)
 *   company      -> COMPANY      (STRING, nullable)
 *   address      -> ADDRESS      (STRING)
 *   city         -> CITY         (STRING)
 *   state        -> STATE        (STRING, nullable)
 *   country      -> COUNTRY      (STRING)
 *   postalCode   -> POSTALCODE   (STRING, nullable)
 *   phone        -> PHONE        (STRING, nullable)
 *   fax          -> FAX          (STRING, nullable)
 *   email        -> EMAIL        (STRING)
 *   supportRepId -> SUPPORTREPID (INT32)
 *
 * Use with RecordView to read and write complete customer records.
 * For services that only need a subset of columns, see
 * {@link CustomerContact} which maps only 5 contact-related fields.
 */
public class Customer {
    private Integer customerId;
    private String firstName;
    private String lastName;
    private String company;
    private String address;
    private String city;
    private String state;
    private String country;
    private String postalCode;
    private String phone;
    private String fax;
    private String email;
    private Integer supportRepId;

    /** Required: GridGain calls this when deserializing rows from the cluster. */
    public Customer() {}

    /**
     * Key-only constructor for lookups by primary key.
     * Non-key fields are left null; GridGain fills them from storage.
     */
    public Customer(Integer customerId) {
        this.customerId = customerId;
    }

    public Integer getCustomerId() { return customerId; }
    public void setCustomerId(Integer id) { this.customerId = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String v) { this.firstName = v; }
    public String getLastName() { return lastName; }
    public void setLastName(String v) { this.lastName = v; }
    public String getCompany() { return company; }
    public void setCompany(String v) { this.company = v; }
    public String getAddress() { return address; }
    public void setAddress(String v) { this.address = v; }
    public String getCity() { return city; }
    public void setCity(String v) { this.city = v; }
    public String getState() { return state; }
    public void setState(String v) { this.state = v; }
    public String getCountry() { return country; }
    public void setCountry(String v) { this.country = v; }
    public String getPostalCode() { return postalCode; }
    public void setPostalCode(String v) { this.postalCode = v; }
    public String getPhone() { return phone; }
    public void setPhone(String v) { this.phone = v; }
    public String getFax() { return fax; }
    public void setFax(String v) { this.fax = v; }
    public String getEmail() { return email; }
    public void setEmail(String v) { this.email = v; }
    public Integer getSupportRepId() { return supportRepId; }
    public void setSupportRepId(Integer v) { this.supportRepId = v; }

    @Override
    public String toString() {
        return "Customer{id=" + customerId
                + ", name='" + firstName + " " + lastName + "'"
                + ", email='" + email + "'"
                + ", city='" + city + "'"
                + ", country='" + country + "'}";
    }
}
```
{% endcode %}

Create `model/CustomerContact.java` for the partial 5-column mapping:

{% code title="src/main/java/com/example/musicstore/model/CustomerContact.java" %}
```java
package com.example.musicstore.model;

/**
 * Partial value POJO: maps only 5 of the 12 non-key Customer columns.
 *
 * GridGain matches fields to table columns by name. Columns not represented
 * in this POJO are skipped on reads. On writes they are NOT preserved:
 * a put or upsert sends a full row, so unmapped columns are set to their
 * default value (NULL unless the column has a DEFAULT). Use a partial POJO
 * for reads, or for writes only when the unmapped columns do not matter:
 *
 *   Mapped (5):    firstName, lastName, email, city, country
 *   Unmapped (7):  company, address, state, postalCode, phone, fax, supportRepId
 *
 * Use with KeyValueView<Integer, CustomerContact> to read only the
 * columns your code path needs. The Integer key type maps to the CUSTOMERID
 * primary key column. The smaller value object reduces memory per record and
 * makes the code's intent explicit: this service path cares about contact
 * data, not the full customer profile.
 *
 * This is "partial POJO mapping" - one of the key advantages of KeyValueView
 * on wide tables. Different service paths can define different value POJOs
 * for the same table, each mapping only the columns they need.
 */
public class CustomerContact {
    private String firstName;
    private String lastName;
    private String email;
    private String city;
    private String country;

    /** Required: GridGain calls this when deserializing rows from the cluster. */
    public CustomerContact() {}

    public String getFirstName() { return firstName; }
    public void setFirstName(String v) { this.firstName = v; }
    public String getLastName() { return lastName; }
    public void setLastName(String v) { this.lastName = v; }
    public String getEmail() { return email; }
    public void setEmail(String v) { this.email = v; }
    public String getCity() { return city; }
    public void setCity(String v) { this.city = v; }
    public String getCountry() { return country; }
    public void setCountry(String v) { this.country = v; }

    @Override
    public String toString() {
        return "CustomerContact{name='" + firstName + " " + lastName + "'"
                + ", email='" + email + "'"
                + ", city='" + city + "'"
                + ", country='" + country + "'}";
    }
}
```
{% endcode %}

Now create `PartialPojos.java`:

{% code title="src/main/java/com/example/musicstore/PartialPojos.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Customer;
import com.example.musicstore.model.CustomerContact;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.logging.Level;
import java.util.logging.Logger;

public class PartialPojos {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            Table customerTable = client.tables().table("Customer");

            // RecordView with full POJO: all 13 columns deserialized into one object.
            // The key (customerId) is part of the POJO itself.
            RecordView<Customer> recordView =
                    customerTable.recordView(Customer.class);
            Customer cust1 = recordView.get(
                    (Transaction) null, new Customer(1));
            System.out.println("RecordView (full):      " + cust1);

            // KeyValueView with partial value POJO: the key type (Integer) maps to
            // the CUSTOMERID primary key column; the value type (CustomerContact)
            // maps to only 5 of the 12 remaining columns. Unmapped columns
            // (company, address, state, etc.) are ignored by the client.
            KeyValueView<Integer, CustomerContact> kvView =
                    customerTable.keyValueView(
                            Integer.class, CustomerContact.class);
            CustomerContact contact1 = kvView.get(
                    (Transaction) null, 1);
            System.out.println("KeyValueView (partial): " + contact1);
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.PartialPojos -q
```

```text
Connected to the cluster.
RecordView (full):      Customer{id=1, name='Luís Gonçalves', email='luisg@embraer.com.br', city='São José dos Campos', country='Brazil'}
KeyValueView (partial): CustomerContact{name='Luís Gonçalves', email='luisg@embraer.com.br', city='São José dos Campos', country='Brazil'}
```

Both views return the same Customer 1 row, but the code structure reveals two different approaches:

- **RecordView** uses a single `Customer` POJO with all 13 fields. `customerId` is part of the object. This is natural when your code works with complete customer records.

- **KeyValueView** separates the key (`Integer` for CustomerId) from the value (`CustomerContact` POJO). The `CustomerContact` class maps only 5 of the 12 non-key columns: `firstName`, `lastName`, `email`, `city`, and `country`. GridGain matches POJO fields to table columns by name. Columns not represented in the POJO (`company`, `address`, `state`, `postalCode`, `phone`, `fax`, `supportRepId`) are skipped on reads. Do not use this partial POJO to write: a `put` sends a full row, so the unmapped columns are set to their defaults (NULL unless the column has a `DEFAULT`).

This partial mapping is the key advantage of KeyValueView on wide tables. A service that only needs contact information defines a 5-field POJO instead of mapping all 13 columns. The smaller object reduces memory overhead per record and makes the code's intent explicit: this code path cares about contact data, not the full customer record.

{% hint style="success" %}
**Checkpoint:** Both views return the same Customer 1 data. The KeyValueView maps 5 of 12 non-key columns through a partial POJO.
{% endhint %}

## Cache-Aside With KeyValueView

You have been using KeyValueView as a table access API. Now look at it from a different angle: KeyValueView is also a cache interface backed by the system of record.

In a traditional architecture, the cache-aside pattern works like this: check the cache (Redis), miss, query the database, write the result to the cache, serve the response. Two systems, two networks, and an invalidation strategy to keep them synchronized. Every write must update both the database and the cache, or stale data creeps in.

With GridGain, the "cache" and the "database" are the same storage:

- **`kvView.get()`** reads a row from distributed storage by primary key.
- **`kvView.put()`** writes a row to that same distributed storage.
- **SQL queries** read the rows written through either view.

There is no separate layer to synchronize and nothing to invalidate.

Create `CacheAside.java`:

{% code title="src/main/java/com/example/musicstore/CacheAside.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.Map;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

public class CacheAside {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            Table artistTable = client.tables().table("Artist");
            KeyValueView<Integer, String> kvView =
                    artistTable.keyValueView(Integer.class, String.class);

            // --- Cache read: get() reads from the system of record ---
            // There is no separate cache to check first. The distributed store
            // IS the cache. A null return means the data does not exist anywhere
            // in the system, not just "cache miss, try the database next."
            String artist1 = kvView.get((Transaction) null, 1);
            System.out.println("Cache read - Artist 1: " + artist1);

            String missing = kvView.get((Transaction) null, 99999);
            System.out.println("Cache read - Artist 99999: " + missing);

            // --- Batch warm-up: pre-load hot keys in one round-trip ---
            // In a Redis architecture, this would be a startup script that queries
            // the database and populates the cache. Here, getAll confirms which
            // keys exist and returns their values directly from the system of record.
            Set<Integer> hotKeys = Set.of(1, 2, 3, 4, 5);
            Map<Integer, String> warmCache = kvView.getAll(
                    (Transaction) null, hotKeys);
            System.out.println("Batch warm-up (" + hotKeys.size()
                    + " keys): loaded " + warmCache.size() + " entries");
            warmCache.forEach((k, v) ->
                    System.out.println("  " + k + " -> " + v));

            // --- Conditional population: putIfAbsent prevents concurrent overwrites ---
            // Two threads racing to populate the same key: the first succeeds,
            // the second gets false and the original value is untouched.
            // Equivalent to Redis SETNX but with ACID guarantees.
            boolean populated = kvView.putIfAbsent(
                    (Transaction) null, 10001, "Cache Populated Artist");
            System.out.println("putIfAbsent(10001): " + populated);

            boolean populatedAgain = kvView.putIfAbsent(
                    (Transaction) null, 10001, "Should Not Overwrite");
            System.out.println("putIfAbsent(10001) again: " + populatedAgain);

            String afterPopulate = kvView.get((Transaction) null, 10001);
            System.out.println("Value after two putIfAbsent calls: "
                    + afterPopulate);

            // --- Unified storage proof: SQL reads the same data ---
            // Data written through KeyValueView is immediately visible to SQL
            // because both access the same distributed storage. There is no
            // cache-to-database synchronization because there is no separation.
            try (var result = client.sql().execute((Transaction) null,
                    "SELECT ArtistId, Name FROM Artist WHERE ArtistId = 10001")) {
                if (result.hasNext()) {
                    var row = result.next();
                    System.out.println("SQL reads the same row: ArtistId="
                            + row.intValue("ArtistId") + ", Name="
                            + row.stringValue("Name"));
                }
            }

            // --- Existence check: contains() avoids deserializing the value ---
            // Useful for membership testing (does this session exist? is this
            // user active?) without the overhead of fetching the full record.
            boolean exists1 = kvView.contains((Transaction) null, 1);
            boolean exists99999 = kvView.contains((Transaction) null, 99999);
            System.out.println("contains(1): " + exists1);
            System.out.println("contains(99999): " + exists99999);

            // Clean up test data
            kvView.remove((Transaction) null, 10001);
            System.out.println("\nCleaned up test data.");
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.CacheAside -q
```

```text
Connected to the cluster.
Cache read - Artist 1: AC/DC
Cache read - Artist 99999: null
Batch warm-up (5 keys): loaded 5 entries
  1 -> AC/DC
  2 -> Accept
  3 -> Aerosmith
  4 -> Alanis Morissette
  5 -> Alice In Chains
putIfAbsent(10001): true
putIfAbsent(10001) again: false
Value after two putIfAbsent calls: Cache Populated Artist
SQL reads the same row: ArtistId=10001, Name=Cache Populated Artist
contains(1): true
contains(99999): false
Cleaned up test data.
```

The SQL query at ArtistId 10001 returned "Cache Populated Artist", the exact value written through `putIfAbsent`. This is the architectural point: there is no cache-to-database synchronization because there is no separation. The KeyValueView write and the SQL read access the same distributed storage.

Key operations for cache patterns:

- **`get()`** is the cache read. `null` means the data does not exist in the system, not just in the cache. There is no "cache miss" that requires a fallback to a separate database.

- **`getAll()`** is the batch warm-up. Pre-load a set of hot keys at application startup in one network round-trip. In a Redis-based architecture, this would be a `MGET` followed by conditional `SET` calls for misses. Here, the data is already in the system of record.

- **`putIfAbsent()`** is the conditional population. It writes only if the key does not exist, which prevents concurrent threads from overwriting each other. This is equivalent to Redis `SETNX` but with ACID guarantees and no separate cache layer.

- **`contains()`** checks whether a key exists without deserializing the value. This is useful for membership testing (does this session exist? is this user active?) without the overhead of fetching the full record.

{% hint style="success" %}
**Checkpoint:** SQL reads the same row written through putIfAbsent. contains(1) returns true, contains(99999) returns false.
{% endhint %}

## Production Caching Patterns

The previous step demonstrated the cache-aside pattern against existing Music Store data. This step shows three production patterns that replace infrastructure you would otherwise build with a separate caching system.

Create `CachePatterns.java`:

{% code title="src/main/java/com/example/musicstore/CachePatterns.java" %}
```java
package com.example.musicstore;

import com.example.musicstore.model.Artist;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.table.KeyValueView;
import org.apache.ignite.table.RecordView;
import org.apache.ignite.table.Table;
import org.apache.ignite.tx.Transaction;

import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

public class CachePatterns {

    public static void main(String[] args) {
        // Suppress GridGain's internal partition-assignment log messages
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        // Connect to all three cluster nodes for partition awareness
        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            System.out.println("Connected to the cluster.");

            Table artistTable = client.tables().table("Artist");
            KeyValueView<Integer, String> kvView =
                    artistTable.keyValueView(Integer.class, String.class);
            RecordView<Artist> recordView = artistTable.recordView(Artist.class);

            // --- Pattern 1: Batch warm-up (replaces Redis cache-warming scripts) ---
            // Load frequently accessed records at application startup in one
            // network round-trip. In a Redis architecture, a warm-up script queries
            // the database and writes results to Redis. Here, getAll reads directly
            // from the system of record. No separate cache to populate.
            Map<Integer, String> startup = kvView.getAll((Transaction) null,
                    Set.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
            System.out.println("Startup warm-up: loaded " + startup.size()
                    + " artists in one round-trip");

            // --- Pattern 2: Atomic read-and-remove (replaces Redis LPOP) ---
            // Process a record exactly once: read it and remove it in a single
            // atomic operation. No race condition between the read and the delete.
            // In Redis, LPOP on a list provides similar semantics but without
            // ACID guarantees or persistence. getAndDelete is fully durable.
            recordView.insert((Transaction) null,
                    new Artist(10001, "Queued Artist"));
            Artist dequeued = recordView.getAndDelete((Transaction) null,
                    new Artist(10001, null));
            System.out.println("Dequeued: " + dequeued);

            // Confirm removal: get returns null after atomic read-and-remove
            Artist afterDequeue = recordView.get((Transaction) null,
                    new Artist(10001, null));
            System.out.println("After dequeue: " + afterDequeue);

            // --- Pattern 3: Multi-get batch resolution (replaces Redis MGET) ---
            // Resolve a list of IDs to full objects in one round-trip.
            // The cluster routes each key to its owning partition internally.
            // RecordView.getAll returns full POJOs; KeyValueView.getAll returns
            // a Map. Choose based on the shape your code needs.
            List<Artist> lookupKeys = List.of(
                    new Artist(1, null),
                    new Artist(50, null),
                    new Artist(100, null),
                    new Artist(200, null),
                    new Artist(275, null));
            Collection<Artist> resolved = recordView.getAll(
                    (Transaction) null, lookupKeys);
            long found = resolved.stream()
                    .filter(Objects::nonNull)
                    .count();
            System.out.println("Multi-get (5 IDs): resolved " + found
                    + " artists in one round-trip");
            resolved.stream()
                    .filter(Objects::nonNull)
                    .forEach(a -> System.out.println("  " + a));

            // Verify original Music Store data is untouched
            String finalCheck = kvView.get((Transaction) null, 1);
            System.out.println("\nFinal check - Artist 1: " + finalCheck);
        }

        // Force JVM exit so Maven does not wait for GridGain's background threads
        System.exit(0);
    }
}
```
{% endcode %}

Run the application:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.CachePatterns -q
```

```text
Connected to the cluster.
Startup warm-up: loaded 10 artists in one round-trip
Dequeued: Artist{id=10001, name='Queued Artist'}
After dequeue: null
Multi-get (5 IDs): resolved 5 artists in one round-trip
  Artist{id=1, name='AC/DC'}
  Artist{id=50, name='Metallica'}
  Artist{id=100, name='Lenny Kravitz'}
  Artist{id=200, name='The Posies'}
  Artist{id=275, name='Philip Glass Ensemble'}

Final check - Artist 1: AC/DC
```

Each pattern replaces a piece of caching infrastructure:

- **Batch warm-up** (`getAll`) replaces the startup script that queries your database and populates Redis. The data is already in the distributed store. `getAll` is a single round-trip that confirms which keys are available and returns their values.

- **Atomic read-and-remove** (`getAndDelete`) replaces Redis `LPOP` for queue patterns. The record is read and removed in one atomic operation. No race condition between the read and the delete.

- **Multi-get** (`getAll` on RecordView or KeyValueView) replaces Redis `MGET`. Resolve a batch of IDs to full objects or key-value pairs in one round-trip. The cluster routes each key to the correct node internally.

In all three patterns, the data is authoritative. There is no stale cache to worry about, no TTL to tune, and no invalidation logic to debug.

{% hint style="success" %}
**Checkpoint:** The startup warm-up loads 10 artists. The dequeue returns the record then null. The multi-get resolves 5 artists including Metallica (50) and Philip Glass Ensemble (275).
{% endhint %}

## GridGain 9 Near-Cache

The patterns in the previous two steps eliminate the need for a separate caching system. Every `get()` call still makes a network round-trip to the cluster. For hot data that your application reads thousands of times per second, that round-trip adds up.

GridGain 9 adds `NearCacheOptions` to both RecordView and KeyValueView. The near-cache stores recently accessed records in the client JVM's memory. Repeated reads of the same key serve from local memory without a network round-trip.

```java
import org.apache.ignite.table.NearCacheOptions;
import org.apache.ignite.table.TableViewOptions;
import org.apache.ignite.table.mapper.Mapper;

// Near-cache configuration: store up to 1000 recently accessed entries
// in the client JVM's heap. Entries expire 10 seconds after last access.
// This eliminates network round-trips for hot reads while the cluster
// remains the authoritative system of record.
NearCacheOptions nearCache = NearCacheOptions.builder()
        .maxEntries(1000)         // LRU eviction when limit reached
        .expireAfterAccess(10_000) // TTL in ms, resets on each read
        .build();

TableViewOptions options = TableViewOptions.builder()
        .nearCacheOptions(nearCache)
        .build();

// The options overload requires Mapper.of() wrappers instead of bare
// Class parameters. The view behaves identically to a standard
// KeyValueView; the near-cache is transparent to application code.
KeyValueView<Integer, String> kvView = artistTable.keyValueView(
        Mapper.of(Integer.class),
        Mapper.of(String.class),
        options);

// First get: network round-trip to the cluster, result cached locally
String name = kvView.get((Transaction) null, 1);

// Second get within 10 seconds: served from client JVM memory (no network)
String nameAgain = kvView.get((Transaction) null, 1);
```

Key configuration options:

- **`maxEntries`** limits the number of cached records. When the limit is reached, the least recently accessed entry is evicted. Default: 0 (no limit).
- **`expireAfterAccess`** sets the TTL in milliseconds after the last read. Entries not accessed within this window are evicted. Default: 5000ms (5 seconds).
- **`expireAfterUpdate`** sets the TTL after a write. Use this when you want writes to refresh the TTL. Default: 5000ms (5 seconds).

The defaults matter: a near-cache created without explicit TTL values expires entries after 5 seconds. The code example above sets `expireAfterAccess` to 10 seconds to keep hot entries longer.

The near-cache is a read-through cache: when a key is not in the local cache, the `get()` call fetches from the cluster and populates the cache automatically. Writes through the same view go to the cluster and invalidate the local entry, so the next read through the view fetches the new value. A view with a near-cache does not accept explicit transactions: passing a transaction throws `UnsupportedOperationException`.

Near-cache also works on RecordView. The same `Mapper.of()` pattern applies:

```java
// Near-cache works on RecordView too. Same Mapper.of() pattern applies.
RecordView<Artist> cachedView = artistTable.recordView(
        Mapper.of(Artist.class), options);
```

{% hint style="info" %}
`NearCacheOptions` is a GridGain 9 feature. The `TableViewOptions` overload requires `Mapper.of()` wrappers instead of bare `Class` parameters.
{% endhint %}

## Choose the Right View

Both views access the same underlying data. The choice depends on your access pattern, not your data model.

| Scenario | Recommended view | Why |
|---|---|---|
| CRUD on domain objects (all columns) | RecordView | Type-safe POJOs, natural object-oriented code |
| Lookup by key, return a subset of columns | KeyValueView | Partial POJO maps only the columns you need |
| Cache-like patterns (has key? get value) | KeyValueView | Map-like API: `get`, `put`, `contains` |
| Complex records with many columns | RecordView | One POJO maps the full row |
| High-frequency lookups on hot data | KeyValueView + near-cache (GG9) | Client-side cache eliminates network round-trips |
| Batch loading or warm-up | Either (bulk ops) | RecordView `upsertAll` for full rows; KeyValueView `putAll` for key-value pairs |
| Queue-like processing | RecordView | `getAndDelete` provides atomic read-and-remove |

Production applications commonly use both views on the same table. A service might use RecordView for full CRUD operations during data ingestion and KeyValueView for fast lookups in the request path. The views are complementary, not competing.

The operational semantics are identical across both views. An `insert` through RecordView and a `putIfAbsent` through KeyValueView enforce the same create-only guarantee. A `deleteAll` through RecordView and a `removeAll` through KeyValueView return the same information (keys that were not found). Choose based on the shape of data your code works with: full objects or key-value pairs.

## Summary

You exercised the full RecordView and KeyValueView operation set across two Music Store tables: Artist (2 columns) for API mechanics and Customer (13 columns) for partial POJO mapping. Three write strategies (idempotent, create-only, update-only), bulk operations for throughput, and cross-view data sharing established the API foundation.

The caching steps revealed the architectural advantage: KeyValueView provides cache-like semantics (`get`, `put`, `putIfAbsent`, `contains`, `getAll`) backed directly by the system of record. There is no separate cache layer to synchronize, no invalidation logic to write, and no stale data to debug. A `putIfAbsent` through KeyValueView and a `SELECT` through SQL read from the same distributed storage. GridGain 9's near-cache adds client-side caching with TTL for hot read paths.

All operations in this tutorial used implicit transactions (the `null` transaction parameter). The next tutorial, [Use Transactions in GridGain 9](use-transactions.md), introduces explicit transactions: grouping multiple operations into an atomic unit so they succeed or fail together.

## Related

- [Start Your Local GridGain 9 Development Cluster](start-local-cluster.md) for the cluster setup and dataset this tutorial connects to
- [Connect with the Java Thin Client](connect-java-thin-client.md) for the thin client connection patterns and Table package hierarchy
- [How to Configure Logging for the Java Thin Client](../../gridgain9-development/configuring-java-client-logging.md) for controlling log output in your application
