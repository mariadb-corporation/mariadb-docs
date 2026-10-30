---
description: >-
  Create tables, run queries, and use EXPLAIN to understand colocated query execution in GridGain SQL.
---

# Create Tables and Query Data With SQL

## Introduction

A multi-table JOIN in a single-node database is straightforward. In a distributed cluster, the same JOIN might execute locally on each node or move data across the network. The difference depends on how you designed your schema: colocation applies only between tables that are partitioned by the same join key. In this tutorial, you run both kinds of joins against the Music Store dataset from the [first tutorial](../../start-local-cluster.md), read the EXPLAIN plans, and see exactly where the data moves.

## Prerequisites

- **A running 3-node cluster with the Music Store dataset loaded** from [Start Your Local GridGain 9 Development Cluster](../../start-local-cluster.md)
- Familiarity with the GridGain CLI. See [How to Work with the GridGain CLI](../../cli-tool-step-by-step.md) for the full reference.

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

* [music-store-schema.sql](../../../.gitbook/assets/music-store-schema.sql)
* [music-store-data.sql](../../../.gitbook/assets/music-store-data.sql)

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

- How to create tables and assign them to distribution zones
- How to insert, update, and delete data with SQL
- How to query data with filters, joins, and aggregations
- How EXPLAIN reveals colocated vs. distributed query execution

## Step 1: Connect to the SQL CLI

If you are continuing directly from the previous tutorial, you are already at the `sql-cli>` prompt. Skip to Step 2.

Otherwise, open the GridGain CLI inside a running node:

```bash
docker exec -it gridgain9-node1 /opt/gridgain9cli/bin/gridgain9
```

At the CLI prompt, connect to the cluster and enter the SQL sub-REPL:

```text
connect http://localhost:10300
```

```text
Connected to http://localhost:10300
```

```text
[node1]> sql
```

The prompt changes to `sql-cli>`. Enter all SQL statements in this tutorial at this prompt. Each statement must end with a semicolon.

{% hint style="success" %}
**Checkpoint:** The `sql-cli>` prompt appears after entering the SQL sub-REPL.
{% endhint %}

## Step 2: Create a Scratch Table

The 11 Music Store tables already exist from the previous tutorial. To learn the DDL syntax without repeating that work, create a small scratch table that you can experiment with and drop at the end.

Create a `Bookmark` table in the `MusicStore` zone:

```sql
CREATE TABLE IF NOT EXISTS Bookmark (
    BookmarkId INT NOT NULL,
    TrackId INT NOT NULL,
    Label VARCHAR(100),
    PRIMARY KEY (BookmarkId)
) ZONE MusicStore;
```

```text
Updated 0 rows.
```

`Updated 0 rows.` is normal for DDL: it modifies schema, not data. `ZONE MusicStore` assigns the table to the same distribution zone as the other business data tables, giving it 2 replicas across the 3-node cluster.

Verify the table exists:

```sql
SELECT TABLE_NAME, ZONE_NAME, TABLE_COLOCATION_COLUMNS FROM SYSTEM.TABLES WHERE TABLE_NAME = 'BOOKMARK';
```

```text
╔════════════╤════════════╤══════════════════════════╗
║ TABLE_NAME │ ZONE_NAME  │ TABLE_COLOCATION_COLUMNS ║
╠════════════╪════════════╪══════════════════════════╣
║ BOOKMARK   │ MUSICSTORE │ BOOKMARKID               ║
╚════════════╧════════════╧══════════════════════════╝
```

`SYSTEM.TABLES` is one of several system catalog views (alongside `SYSTEM.ZONES` and `SYSTEM.INDEXES`) that you can query like regular tables.

{% hint style="warning" %}
GridGain normalizes all SQL identifiers to uppercase. The table name is `BOOKMARK` in the catalog, not `Bookmark` as typed in the DDL. This applies everywhere: column names in query results, `SqlRow` accessor methods in Java, and system catalog filters. Use uppercase when referencing identifiers programmatically.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The `SYSTEM.TABLES` query shows `BOOKMARK` in the `MUSICSTORE` zone with `BOOKMARKID` as the colocation key.
{% endhint %}

## Step 3: Insert, Update, and Delete Data

The table exists but is empty. Populate it with a few rows to see how DML works in GridGain SQL:

```sql
INSERT INTO Bookmark (BookmarkId, TrackId, Label) VALUES (1, 3402, 'Best guitar solo');
```

```text
Updated 1 rows.
```

Add several more rows in one statement:

```sql
INSERT INTO Bookmark (BookmarkId, TrackId, Label) VALUES
    (2, 2, 'Classic opener'),
    (3, 10, 'Smooth jazz'),
    (4, 150, 'Workout track');
```

```text
Updated 3 rows.
```

Multi-row INSERT sends all values in a single round-trip to the cluster. Verify:

```sql
SELECT * FROM Bookmark ORDER BY BookmarkId;
```

```text
╔════════════╤═════════╤══════════════════╗
║ BOOKMARKID │ TRACKID │ LABEL            ║
╠════════════╪═════════╪══════════════════╣
║ 1          │ 3402    │ Best guitar solo ║
╟────────────┼─────────┼──────────────────╢
║ 2          │ 2       │ Classic opener   ║
╟────────────┼─────────┼──────────────────╢
║ 3          │ 10      │ Smooth jazz      ║
╟────────────┼─────────┼──────────────────╢
║ 4          │ 150     │ Workout track    ║
╚════════════╧═════════╧══════════════════╝
```

Four rows, and the column headers confirm the uppercase normalization from Step 2: `BOOKMARKID`, not `BookmarkId`.

Now modify existing data. Update a label:

```sql
UPDATE Bookmark SET Label = 'All-time favorite solo' WHERE BookmarkId = 1;
```

```text
Updated 1 rows.
```

```sql
SELECT BookmarkId, Label FROM Bookmark WHERE BookmarkId = 1;
```

```text
╔════════════╤════════════════════════╗
║ BOOKMARKID │ LABEL                  ║
╠════════════╪════════════════════════╣
║ 1          │ All-time favorite solo ║
╚════════════╧════════════════════════╝
```

And remove a row:

```sql
DELETE FROM Bookmark WHERE BookmarkId = 4;
```

```text
Updated 1 rows.
```

All DML operations report `Updated N rows.` in the CLI. Verify:

```sql
SELECT COUNT(*) AS remaining FROM Bookmark;
```

```text
╔═══════════╗
║ REMAINING ║
╠═══════════╣
║ 3         ║
╚═══════════╝
```

Three rows remain after deleting the workout track.

How did the engine find the row to update? `EXPLAIN` works on DML too:

```sql
EXPLAIN UPDATE Bookmark SET Label = 'changed' WHERE BookmarkId = 1;
```

```text
╔══════════════════════════════════════════════════════════════╗
║ PLAN                                                         ║
╠══════════════════════════════════════════════════════════════╣
║ KeyValueModify                                               ║
║     table: PUBLIC.BOOKMARK                                   ║
║     fieldNames: [ROWCOUNT]                                   ║
║     sourceExpression: [BOOKMARKID, TRACKID, _UTF-8'changed'] ║
║     type: UPDATE                                             ║
║     key: [1]                                                 ║
║     est: (rows=1)                                            ║
╚══════════════════════════════════════════════════════════════╝
```

`KeyValueModify` with `key: [1]` writes the row directly by its primary key. There is no scan, no `Exchange`, and no other partition involved. The `WHERE BookmarkId = 1` predicate routes the operation to the single node that owns that key. This is why primary key design matters in a distributed database: it determines which node handles the write.

{% hint style="success" %}
**Checkpoint:** The Bookmark table contains 3 rows after the INSERT, UPDATE, and DELETE operations. The EXPLAIN on UPDATE shows a `KeyValueModify` by primary key.
{% endhint %}

## Step 4: Query With Filters and Sorting

You know how to create, populate, and modify a table. Now turn to the 3,503-row Track table and see what the Music Store dataset looks like under real queries.

Find the five longest Rock tracks (Genre ID 1 is Rock):

```sql
SELECT TrackId, Name, Milliseconds
FROM Track
WHERE GenreId = 1
ORDER BY Milliseconds DESC
LIMIT 5;
```

```text
╔═════════╤═════════════════════════════════╤══════════════╗
║ TRACKID │ NAME                            │ MILLISECONDS ║
╠═════════╪═════════════════════════════════╪══════════════╣
║ 1666    │ Dazed And Confused              │ 1612329      ║
╟─────────┼─────────────────────────────────┼──────────────╢
║ 620     │ Space Truckin'                  │ 1196094      ║
╟─────────┼─────────────────────────────────┼──────────────╢
║ 1581    │ Dazed And Confused              │ 1116734      ║
╟─────────┼─────────────────────────────────┼──────────────╢
║ 2429    │ We've Got To Get Together/Jingo │ 1070027      ║
╟─────────┼─────────────────────────────────┼──────────────╢
║ 2432    │ Funky Piano                     │ 934791       ║
╚═════════╧═════════════════════════════════╧══════════════╝
```

"Dazed And Confused" appears twice: track IDs 1666 and 1581 are different recordings with different durations. The `Name` column has no uniqueness constraint and no index. How do you know? Prefix any query with `EXPLAIN` to see how the engine executes it:

```sql
EXPLAIN SELECT TrackId, Name, Milliseconds
FROM Track WHERE Name = 'Dazed And Confused';
```

{% hint style="info" %}
The `est` row counts in `EXPLAIN` output come from table statistics, which the cluster collects some time after a load. On a freshly loaded cluster you can see `est: (rows=1)` where the samples in this tutorial show real counts, and for larger queries the plan shape can differ until statistics are collected. The operators and what they tell you stay the same.
{% endhint %}

```text
╔══════════════════════════════════════════════════════╗
║ PLAN                                                 ║
╠══════════════════════════════════════════════════════╣
║ Exchange                                             ║
║     distribution: single                             ║
║     est: (rows=1166)                                 ║
║   TableScan                                          ║
║       table: PUBLIC.TRACK                            ║
║       predicate: =(NAME, _UTF-8'Dazed And Confused') ║
║       fieldNames: [TRACKID, NAME, MILLISECONDS]      ║
║       est: (rows=1166)                               ║
╚══════════════════════════════════════════════════════╝
```

`TableScan` with no index lookup: the engine reads every Track row on every partition to evaluate the predicate. The `est: (rows=1166)` is the planner's estimate of how many rows it scans, not how many it returns.

For 3,503 rows on a development cluster, this is fast enough. On a production dataset, you would create an index: `CREATE INDEX idx_track_name ON Track (Name);`

{% hint style="info" %}
Use `EXPLAIN` liberally throughout this tutorial. It is the primary tool for understanding how GridGain routes queries across the cluster.
{% endhint %}

To disambiguate the two recordings, join to Album:

```sql
SELECT t.TrackId, t.Name, al.Title AS Album, t.Milliseconds
FROM Track t
JOIN Album al ON t.AlbumId = al.AlbumId
WHERE t.Name = 'Dazed And Confused'
ORDER BY t.Milliseconds DESC;
```

```text
╔═════════╤════════════════════╤════════════════════════════════════╤══════════════╗
║ TRACKID │ NAME               │ ALBUM                              │ MILLISECONDS ║
╠═════════╪════════════════════╪════════════════════════════════════╪══════════════╣
║ 1666    │ Dazed And Confused │ The Song Remains The Same (Disc 1) │ 1612329      ║
╟─────────┼────────────────────┼────────────────────────────────────┼──────────────╢
║ 1581    │ Dazed And Confused │ BBC Sessions [Disc 2] [Live]       │ 1116734      ║
╚═════════╧════════════════════╧════════════════════════════════════╧══════════════╝
```

Two live recordings from different albums. Track is partitioned by `AlbumId`, but Album is partitioned by `ArtistId`, so this join is not a colocated join and the cluster may move data to match the rows. For production workloads that filter by `Name` frequently, you would create an index: `CREATE INDEX idx_track_name ON Track (Name);`

Search for tracks by name using a pattern match:

```sql
SELECT TrackId, Name, UnitPrice
FROM Track
WHERE Name LIKE '%Love%'
ORDER BY Name
LIMIT 10;
```

```text
╔═════════╤═════════════════════════════════════════╤═══════════╗
║ TRACKID │ NAME                                    │ UNITPRICE ║
╠═════════╪═════════════════════════════════════════╪═══════════╣
║ 3045    │ (I Can't Help) Falling In Love With You │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 3471    │ (There Is) No Greater Love (Teo Licks)  │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 3084    │ Ain't Talkin' 'Bout Love                │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 3065    │ Ain't Talkin' 'bout Love                │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 1608    │ All My Love                             │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 3316    │ All My Love                             │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 3377    │ Arms Around Your Love                   │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 3294    │ Believe in Love                         │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 449     │ Calling Dr. Love                        │ 0.99      ║
╟─────────┼─────────────────────────────────────────┼───────────╢
║ 790     │ Cascades : I'm Not Your Lover           │ 0.99      ║
╚═════════╧═════════════════════════════════════════╧═══════════╝
```

`LIKE '%Love%'` matches "Love" anywhere in the track name. The search is case-sensitive: `%love%` would miss "All My Love."

Use arithmetic expressions in the SELECT list to convert milliseconds to minutes:

```sql
SELECT TrackId, Name, Milliseconds / 60000 AS minutes
FROM Track
WHERE Milliseconds > 600000
ORDER BY Milliseconds DESC
LIMIT 5;
```

```text
╔═════════╤═════════════════════════════╤═════════╗
║ TRACKID │ NAME                        │ MINUTES ║
╠═════════╪═════════════════════════════╪═════════╣
║ 2820    │ Occupation / Precipice      │ 88      ║
╟─────────┼─────────────────────────────┼─────────╢
║ 3224    │ Through a Looking Glass     │ 84      ║
╟─────────┼─────────────────────────────┼─────────╢
║ 3244    │ Greetings from Earth, Pt. 1 │ 49      ║
╟─────────┼─────────────────────────────┼─────────╢
║ 3242    │ The Man With Nine Lives     │ 49      ║
╟─────────┼─────────────────────────────┼─────────╢
║ 3227    │ Battlestar Galactica, Pt. 2 │ 49      ║
╚═════════╧═════════════════════════════╧═════════╝
```

The longest "tracks" are 49-88 minutes. These are TV show episodes stored alongside music in the catalog, not songs.

{% hint style="success" %}
**Checkpoint:** All three queries return results matching the expected output above.
{% endhint %}

## Step 5: Join Colocated Tables

So far, `EXPLAIN` has shown two patterns: direct primary key access (`KeyValueModify`) for primary key operations (Step 3), and `TableScan` for unindexed filters (Step 4). Joins introduce a third question: does the data need to move between nodes before the join can execute? The previous tutorial set up the Music Store tables with `COLOCATE BY` clauses. Artist and Album are a colocated pair by `ArtistId`, but Track is colocated by a different column, `AlbumId`. Join Artist, Album, and Track to see what that means for the plan:

```sql
SELECT a.Name AS Artist, al.Title AS Album, t.Name AS Track
FROM Artist a
JOIN Album al ON a.ArtistId = al.ArtistId
JOIN Track t ON al.AlbumId = t.AlbumId
WHERE a.Name = 'Led Zeppelin'
ORDER BY al.Title, t.Name
LIMIT 10;
```

```text
╔══════════════╤══════════════════════════════╤══════════════════════════════════════════════╗
║ ARTIST       │ ALBUM                        │ TRACK                                        ║
╠══════════════╪══════════════════════════════╪══════════════════════════════════════════════╣
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ Communication Breakdown                      ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ Communication Breakdown(2)                   ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ Communication Breakdown(3)                   ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ Dazed and Confused                           ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ How Many More Times                          ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ I Can't Quit You Baby                        ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ I Can't Quit You Baby(2)                     ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ Somethin' Else                               ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ The Girl I Love She Got Long Black Wavy Hair ║
╟──────────────┼──────────────────────────────┼──────────────────────────────────────────────╢
║ Led Zeppelin │ BBC Sessions [Disc 1] [Live] │ Travelling Riverside Blues                   ║
╚══════════════╧══════════════════════════════╧══════════════════════════════════════════════╝
```

<details>
<summary>Your rows may differ. Here is why.</summary>

The `ORDER BY` is deterministic on the full result set (114 Led Zeppelin tracks across 14 albums). But when `LIMIT` is present, the optimizer pushes it into each partition's local sort. Each partition sorts its local rows and returns only 10. The coordinator collects these partial results and applies the final limit without re-sorting. The rows you see depend on which partition responds first.

The EXPLAIN plan below shows this: the `Sort` operator has `fetch: 10`, meaning the limit is pushed below the `Exchange`. Remove the `LIMIT` clause and run the query again to see all 114 rows in correct alphabetical order.

This is a general property of distributed `ORDER BY ... LIMIT`: the result set is bounded but the specific rows may vary across runs. If your application requires deterministic paging, add a unique tiebreaker column (like a primary key) to the `ORDER BY`.

</details>

Led Zeppelin has 114 tracks across 14 albums. Album colocates by `ArtistId`, so each Led Zeppelin album sits in the same partition as the artist row. Track colocates by `AlbumId`, so all tracks of one album share a partition with each other, but a track is not placed with its Album row or its Artist row. Colocation is decided only by the columns a table hashes for its own rows, and it does not chain through a middle table. The query returns correct results, but the join to Track moves data between nodes.

Start with the colocated pair. This two-table join of Artist and Album uses the same filter:

```sql
EXPLAIN SELECT a.Name AS Artist, al.Title AS Album
FROM Artist a
JOIN Album al ON a.ArtistId = al.ArtistId
WHERE a.Name = 'Led Zeppelin';
```

```text
╔═════════════════════════════════════════════════════════╗
║ PLAN                                                    ║
╠═════════════════════════════════════════════════════════╣
║ Exchange                                                ║
║     distribution: single                                ║
║     est: (rows=116)                                     ║
║   Project                                               ║
║       fieldNames: [ARTIST, ALBUM]                       ║
║       projection: [NAME, TITLE]                         ║
║       est: (rows=116)                                   ║
║     HashJoin                                            ║
║         predicate: =(ARTISTID$0, ARTISTID)              ║
║         fieldNames: [ARTISTID, TITLE, ARTISTID$0, NAME] ║
║         type: inner                                     ║
║         est: (rows=116)                                 ║
║       TableScan                                         ║
║           table: PUBLIC.ALBUM                           ║
║           fieldNames: [ARTISTID, TITLE]                 ║
║           est: (rows=347)                               ║
║       TableScan                                         ║
║           table: PUBLIC.ARTIST                          ║
║           predicate: =(NAME, _UTF-8'Led Zeppelin')      ║
║           fieldNames: [ARTISTID, NAME]                  ║
║           est: (rows=92)                                ║
╚═════════════════════════════════════════════════════════╝
```

The only `Exchange` sits at the top of the plan, where the coordinator collects the final rows. No `Exchange` appears between the two `TableScan` inputs of the `HashJoin`, so Artist and Album join locally on each node. Both tables are colocated by `ArtistId`, which is the join key.

Now add Track, which is colocated by `AlbumId`, a different column. `EXPLAIN` shows the difference:

```sql
EXPLAIN SELECT a.Name AS Artist, al.Title AS Album, t.Name AS Track
FROM Artist a
JOIN Album al ON a.ArtistId = al.ArtistId
JOIN Track t ON al.AlbumId = t.AlbumId
WHERE a.Name = 'Led Zeppelin'
ORDER BY al.Title, t.Name
LIMIT 10;
```

```text
╔═════════════════════════════════════════════════════════════════════════════════════════╗
║ PLAN                                                                                    ║
╠═════════════════════════════════════════════════════════════════════════════════════════╣
║ Limit                                                                                   ║
║     fetch: 10                                                                           ║
║     est: (rows=10)                                                                      ║
║   Exchange                                                                              ║
║       collation: [ALBUM ASC, TRACK ASC]                                                 ║
║       distribution: single                                                              ║
║       est: (rows=10)                                                                    ║
║     Sort                                                                                ║
║         collation: [ALBUM ASC, TRACK ASC]                                               ║
║         fetch: 10                                                                       ║
║         est: (rows=10)                                                                  ║
║       Project                                                                           ║
║           fieldNames: [ARTIST, ALBUM, TRACK]                                            ║
║           projection: [NAME$0, TITLE, NAME]                                             ║
║           est: (rows=60716)                                                             ║
║         HashJoin                                                                        ║
║             predicate: =(ALBUMID$0, ALBUMID)                                            ║
║             fieldNames: [ALBUMID, NAME, ALBUMID$0, ARTISTID, TITLE, ARTISTID$0, NAME$0] ║
║             type: inner                                                                 ║
║             est: (rows=60716)                                                           ║
║           TableScan                                                                     ║
║               table: PUBLIC.TRACK                                                       ║
║               fieldNames: [ALBUMID, NAME]                                               ║
║               est: (rows=3503)                                                          ║
║           Exchange                                                                      ║
║               distribution: table PUBLIC.TRACK in zone MUSICSTORE by [ALBUMID]          ║
║               est: (rows=116)                                                           ║
║             HashJoin                                                                    ║
║                 predicate: =(ARTISTID$0, ARTISTID)                                      ║
║                 fieldNames: [ALBUMID, ARTISTID, TITLE, ARTISTID$0, NAME]                ║
║                 type: inner                                                             ║
║                 est: (rows=116)                                                         ║
║               Exchange                                                                  ║
║                   distribution: single                                                  ║
║                   est: (rows=347)                                                       ║
║                 TableScan                                                               ║
║                     table: PUBLIC.ALBUM                                                 ║
║                     fieldNames: [ALBUMID, ARTISTID, TITLE]                              ║
║                     est: (rows=347)                                                     ║
║               Exchange                                                                  ║
║                   distribution: single                                                  ║
║                   est: (rows=92)                                                        ║
║                 TableScan                                                               ║
║                     table: PUBLIC.ARTIST                                                ║
║                     predicate: =(NAME, _UTF-8'Led Zeppelin')                            ║
║                     fieldNames: [ARTISTID, NAME]                                        ║
║                     est: (rows=92)                                                      ║
╚═════════════════════════════════════════════════════════════════════════════════════════╝
```

Read the plan from bottom to top. Two `TableScan` operators read ALBUM and ARTIST, and a `HashJoin` combines them on `ARTISTID`. An `Exchange` then redistributes the joined rows with `distribution: table PUBLIC.TRACK in zone MUSICSTORE by [ALBUMID]`, which sends each row to the partition that holds the matching Track rows. A second `HashJoin` combines that result with the Track `TableScan` on `ALBUMID`. The top `Exchange` collects the final rows on the coordinator. The `Exchange` operators with `distribution: single` above the ALBUM and ARTIST scans gather those rows on one node before the inner join. For this three-table query the planner picks a different strategy than for the two-table query, so you cannot read the locality of the Artist-Album pair from this plan alone. The `Exchange` by `[ALBUMID]` is the one that shows the colocation boundary.

{% hint style="info" %}
**HashJoin** builds an in-memory hash table from one input and probes it with the other. It handles unsorted inputs at the cost of memory proportional to the smaller input. Watch for HashJoin on large tables; it can cause memory pressure under high concurrency.

**Exchange** is the network operator. It transfers rows between nodes. Every Exchange in a plan represents data moving across the network. Its position relative to join operators tells you whether the engine moved data *before* the join (expensive: shuffles raw rows) or *after* (cheap: collects final results).

For the full operator reference, see the [EXPLAIN operators reference](../../../reference/sql/explain-operators-list.md).
{% endhint %}

In Step 4, the single-table plan had one `Exchange` that collected results. The two-table plan also has one Exchange, at the top, because Artist and Album are colocated by the join key. The three-table plan has more `Exchange` operators, including one between the Artist-Album join and the Track join that redistributes rows by `AlbumId`, because Track is partitioned by `AlbumId`, not `ArtistId`. Colocation helps the join it was designed for and does not extend to the next table.

What happens when colocation does not apply? Track is colocated by `AlbumId` and InvoiceLine is colocated by `InvoiceId`. Neither is placed by `TrackId`, so joining them by `TrackId` crosses colocation boundaries:

```sql
EXPLAIN SELECT t.Name AS Track, il.UnitPrice, il.Quantity
FROM Track t
JOIN InvoiceLine il ON t.TrackId = il.TrackId
WHERE t.GenreId = 1
LIMIT 10;
```

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║ PLAN                                                                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Limit                                                                        ║
║     fetch: 10                                                                ║
║     est: (rows=10)                                                           ║
║   Project                                                                    ║
║       fieldNames: [TRACK, UNITPRICE, QUANTITY]                               ║
║       projection: [NAME, UNITPRICE, QUANTITY]                                ║
║       est: (rows=391944)                                                     ║
║     HashJoin                                                                 ║
║         predicate: =(TRACKID$0, TRACKID)                                     ║
║         fieldNames: [TRACKID, UNITPRICE, QUANTITY, TRACKID$0, NAME, GENREID] ║
║         type: inner                                                          ║
║         est: (rows=391944)                                                   ║
║       Exchange                                                               ║
║           distribution: single                                               ║
║           est: (rows=2240)                                                   ║
║         TableScan                                                            ║
║             table: PUBLIC.INVOICELINE                                        ║
║             fieldNames: [TRACKID, UNITPRICE, QUANTITY]                       ║
║             est: (rows=2240)                                                 ║
║       Exchange                                                               ║
║           distribution: single                                               ║
║           est: (rows=1166)                                                   ║
║         TableScan                                                            ║
║             table: PUBLIC.TRACK                                              ║
║             predicate: =(GENREID, 1)                                         ║
║             fieldNames: [TRACKID, NAME, GENREID]                             ║
║             est: (rows=1166)                                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

The structure flipped. Two `Exchange` operators now appear below the `HashJoin`, one for each table input. The planner must pull all matching InvoiceLine rows (estimated 2,240) and all matching Track rows (estimated 1,166) to a single node before the join can execute. That is a full data shuffle for a query that returns 10 rows.

On this 3-node dev cluster with 3,503 tracks, the shuffle completes in milliseconds. In production with millions of rows across dozens of nodes, the cost scales linearly with data volume and cluster size. A colocated join stays constant: each node joins its local data regardless of how many nodes the cluster has.

The pattern: in the colocated two-table plan, Exchange sits above the join (collecting results). In the three-table and non-colocated plans, Exchanges sit below a join (moving data). Where Exchange appears relative to Join tells you whether a join scales with your cluster or fights it.

{% hint style="info" %}

**Exchange above Join** = colocated. Data stays local; only the final results travel across the network.

**Exchange below Join** = usually non-colocated. Data must be shuffled across the network before the join can execute. As a rule of thumb only: the planner can also gather small inputs on one node, as the three-table plan above shows.

In production, this distinction determines whether query cost scales with data volume or stays constant per node.
{% endhint %}

When you design your own schema, you choose which join paths to optimize with colocation. The Music Store colocates Artist with Album, Customer with Invoice, and Playlist with PlaylistTrack. Those pairs are the hot paths for catalog browsing and revenue analysis. Colocation does not chain, so adding a third table such as Track or InvoiceLine, or joining Track to InvoiceLine, still works but pays the network cost. One colocation key per table, one optimized pair.

{% hint style="success" %}
**Checkpoint:** The two-table EXPLAIN plan shows no Exchange operators between the join inputs. The three-table plan shows an Exchange by `ALBUMID` between the two joins, and the non-colocated EXPLAIN plan shows Exchange operators below the HashJoin, one for each table.
{% endhint %}

## Step 6: Aggregate and Analyze

Now put those joins to work with aggregation. Genre lives in the `MusicStoreReplicated` zone (3 replicas, one per node), so the Track-to-Genre join resolves locally:

```sql
SELECT g.Name AS Genre, COUNT(t.TrackId) AS Tracks,
       CAST(AVG(t.Milliseconds) / 60000.0 AS DECIMAL(5,1)) AS AvgMinutes
FROM Genre g
JOIN Track t ON g.GenreId = t.GenreId
GROUP BY g.Name
ORDER BY Tracks DESC;
```

```text
╔════════════════════╤════════╤════════════╗
║ GENRE              │ TRACKS │ AVGMINUTES ║
╠════════════════════╪════════╪════════════╣
║ Rock               │ 1297   │ 4.7        ║
╟────────────────────┼────────┼────────────╢
║ Latin              │ 579    │ 3.8        ║
╟────────────────────┼────────┼────────────╢
║ Metal              │ 374    │ 5.1        ║
╟────────────────────┼────────┼────────────╢
║ Alternative & Punk │ 332    │ 3.9        ║
╟────────────────────┼────────┼────────────╢
║ Jazz               │ 130    │ 4.8        ║
╟────────────────────┼────────┼────────────╢
║ TV Shows           │ 93     │ 35.7       ║
╟────────────────────┼────────┼────────────╢
║ Blues              │ 81     │ 4.5        ║
╟────────────────────┼────────┼────────────╢
║ Classical          │ 74     │ 4.8        ║
╟────────────────────┼────────┼────────────╢
║ Drama              │ 64     │ 42.9       ║
╟────────────────────┼────────┼────────────╢
║ R&B/Soul           │ 61     │ 3.6        ║
╟────────────────────┼────────┼────────────╢
║ Reggae             │ 58     │ 4.1        ║
╟────────────────────┼────────┼────────────╢
║ Pop                │ 48     │ 3.8        ║
╟────────────────────┼────────┼────────────╢
║ Soundtrack         │ 43     │ 4.0        ║
╟────────────────────┼────────┼────────────╢
║ Alternative        │ 40     │ 4.4        ║
╟────────────────────┼────────┼────────────╢
║ Hip Hop/Rap        │ 35     │ 2.9        ║
╟────────────────────┼────────┼────────────╢
║ Electronica/Dance  │ 30     │ 5.0        ║
╟────────────────────┼────────┼────────────╢
║ World              │ 28     │ 3.7        ║
╟────────────────────┼────────┼────────────╢
║ Heavy Metal        │ 28     │ 4.9        ║
╟────────────────────┼────────┼────────────╢
║ Sci Fi & Fantasy   │ 26     │ 48.5       ║
╟────────────────────┼────────┼────────────╢
║ Easy Listening     │ 24     │ 3.1        ║
╟────────────────────┼────────┼────────────╢
║ Comedy             │ 17     │ 26.4       ║
╟────────────────────┼────────┼────────────╢
║ Bossa Nova         │ 15     │ 3.6        ║
╟────────────────────┼────────┼────────────╢
║ Science Fiction    │ 13     │ 43.7       ║
╟────────────────────┼────────┼────────────╢
║ Rock And Roll      │ 12     │ 2.2        ║
╟────────────────────┼────────┼────────────╢
║ Opera              │ 1      │ 2.9        ║
╚════════════════════╧════════╧════════════╝
```

Rock dominates at 1,297 tracks with a 4.7-minute average. TV Shows (35.7 min), Drama (42.9 min), and Sci Fi & Fantasy (48.5 min) have high averages because those genres contain video episodes, not songs.

Customer and Invoice are colocated by `CustomerId`, so revenue aggregation also runs locally. Use `HAVING` to keep only countries with 10 or more orders:

```sql
SELECT c.Country, COUNT(i.InvoiceId) AS Orders,
       CAST(SUM(i.Total) AS DECIMAL(10,2)) AS Revenue
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.Country
HAVING COUNT(i.InvoiceId) >= 10
ORDER BY Revenue DESC;
```

```text
╔════════════════╤════════╤═════════╗
║ COUNTRY        │ ORDERS │ REVENUE ║
╠════════════════╪════════╪═════════╣
║ USA            │ 91     │ 523.06  ║
╟────────────────┼────────┼─────────╢
║ Canada         │ 56     │ 303.96  ║
╟────────────────┼────────┼─────────╢
║ France         │ 35     │ 195.10  ║
╟────────────────┼────────┼─────────╢
║ Brazil         │ 35     │ 190.10  ║
╟────────────────┼────────┼─────────╢
║ Germany        │ 28     │ 156.48  ║
╟────────────────┼────────┼─────────╢
║ United Kingdom │ 21     │ 112.86  ║
╟────────────────┼────────┼─────────╢
║ Czech Republic │ 14     │ 90.24   ║
╟────────────────┼────────┼─────────╢
║ Portugal       │ 14     │ 77.24   ║
╟────────────────┼────────┼─────────╢
║ India          │ 13     │ 75.26   ║
╚════════════════╧════════╧═════════╝
```

Nine countries have 10 or more orders. The USA leads with 91 orders and $523.06 in revenue. How does the engine handle aggregation across a distributed dataset? EXPLAIN the revenue query:

```sql
EXPLAIN SELECT c.Country, COUNT(i.InvoiceId) AS Orders,
       CAST(SUM(i.Total) AS DECIMAL(10,2)) AS Revenue
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.Country
HAVING COUNT(i.InvoiceId) >= 10
ORDER BY Revenue DESC;
```

```text
╔════════════════════════════════════════════════════════════════════════════╗
║ PLAN                                                                       ║
╠════════════════════════════════════════════════════════════════════════════╣
║ Sort                                                                       ║
║     collation: [REVENUE DESC]                                              ║
║     est: (rows=41)                                                         ║
║   Project                                                                  ║
║       fieldNames: [COUNTRY, ORDERS, REVENUE]                               ║
║       projection: [COUNTRY, ORDERS, CAST($f2):DECIMAL(10, 2) NOT NULL]     ║
║       est: (rows=41)                                                       ║
║     Filter                                                                 ║
║         predicate: >=(ORDERS, 10)                                          ║
║         est: (rows=41)                                                     ║
║       Project                                                              ║
║           fieldNames: [COUNTRY, ORDERS, $f2]                               ║
║           projection: [f0, CAST(f0_1):BIGINT NOT NULL, f0_2]               ║
║           est: (rows=82)                                                   ║
║         ReduceHashAggregate                                                ║
║             fieldNames: [f0, f0_1, f0_2]                                   ║
║             group: [COUNTRY]                                               ║
║             aggregation: [$SUM0(_ACC0), SUM(_ACC1)]                        ║
║             est: (rows=82)                                                 ║
║           Exchange                                                         ║
║               distribution: single                                         ║
║               est: (rows=82)                                               ║
║             MapHashAggregate                                               ║
║                 fieldNames: [COUNTRY, _ACC0, _ACC1, _GROUP_ID]             ║
║                 group: [COUNTRY]                                           ║
║                 aggregation: [COUNT(), SUM(TOTAL)]                         ║
║                 est: (rows=82)                                             ║
║               Project                                                      ║
║                   fieldNames: [COUNTRY, TOTAL]                             ║
║                   projection: [COUNTRY, TOTAL]                             ║
║                   est: (rows=412)                                          ║
║                 HashJoin                                                   ║
║                     predicate: =(CUSTOMERID$0, CUSTOMERID)                 ║
║                     fieldNames: [CUSTOMERID, TOTAL, CUSTOMERID$0, COUNTRY] ║
║                     type: inner                                            ║
║                     est: (rows=412)                                        ║
║                   TableScan                                                ║
║                       table: PUBLIC.INVOICE                                ║
║                       fieldNames: [CUSTOMERID, TOTAL]                      ║
║                       est: (rows=412)                                      ║
║                   TableScan                                                ║
║                       table: PUBLIC.CUSTOMER                               ║
║                       fieldNames: [CUSTOMERID, COUNTRY]                    ║
║                       est: (rows=59)                                       ║
╚════════════════════════════════════════════════════════════════════════════╝
```

A new pattern. Read from the bottom:

- The `HashJoin` between INVOICE and CUSTOMER has no Exchange between its inputs (colocated by `CustomerId`).
- Above that, `MapHashAggregate` runs the COUNT and SUM locally on each node.
- The results cross the Exchange to `ReduceHashAggregate`, which combines the per-node partial aggregates into the final answer.
- The `Filter` at the top applies the `HAVING` clause after the aggregation is complete.

This is a map-reduce pattern: compute locally, combine centrally.

{% hint style="info" %}

**MapHashAggregate** computes partial results (COUNT, SUM) on each node using only local data.

**ReduceHashAggregate** collects those partial results across the Exchange and combines them into the final answer.

This two-phase pattern means each node processes only its own partition, regardless of cluster size. See the [EXPLAIN operators reference](../../../reference/sql/explain-operators-list.md) for the full list of aggregation operators.
{% endhint %}

Combine the three-table join with aggregation to rank the top 10 artists by catalog value:

```sql
SELECT a.Name AS Artist, COUNT(t.TrackId) AS Tracks,
       CAST(SUM(t.UnitPrice) AS DECIMAL(10,2)) AS CatalogValue
FROM Artist a
JOIN Album al ON a.ArtistId = al.ArtistId
JOIN Track t ON al.AlbumId = t.AlbumId
GROUP BY a.ArtistId, a.Name
ORDER BY CatalogValue DESC
LIMIT 10;
```

```text
╔═════════════════╤════════╤══════════════╗
║ ARTIST          │ TRACKS │ CATALOGVALUE ║
╠═════════════════╪════════╪══════════════╣
║ Iron Maiden     │ 213    │ 210.87       ║
╟─────────────────┼────────┼──────────────╢
║ Lost            │ 92     │ 183.08       ║
╟─────────────────┼────────┼──────────────╢
║ U2              │ 135    │ 133.65       ║
╟─────────────────┼────────┼──────────────╢
║ Led Zeppelin    │ 114    │ 112.86       ║
╟─────────────────┼────────┼──────────────╢
║ Metallica       │ 112    │ 110.88       ║
╟─────────────────┼────────┼──────────────╢
║ The Office      │ 53     │ 105.47       ║
╟─────────────────┼────────┼──────────────╢
║ Deep Purple     │ 92     │ 91.08        ║
╟─────────────────┼────────┼──────────────╢
║ Pearl Jam       │ 67     │ 66.33        ║
╟─────────────────┼────────┼──────────────╢
║ Lenny Kravitz   │ 57     │ 56.43        ║
╟─────────────────┼────────┼──────────────╢
║ Various Artists │ 56     │ 55.44        ║
╚═════════════════╧════════╧══════════════╝
```

Iron Maiden leads with 213 tracks across their discography. "Lost" and "The Office" rank high because the dataset includes TV show episodes priced at $1.99 each, which inflates their catalog value relative to $0.99 music tracks.

The `GROUP BY` includes both `a.ArtistId` and `a.Name`. Grouping by `ArtistId` (the unique identifier) avoids collisions if two artists share the same name; `a.Name` is included so it can appear in the SELECT list.

{% hint style="success" %}
**Checkpoint:** The genre query returns 25 rows. The revenue query returns 9 countries. The catalog value query shows Iron Maiden at the top with 213 tracks.
{% endhint %}

## Step 7: Clean Up the Scratch Table

The scratch table has served its purpose. Drop it so future tutorials start with a clean 11-table schema:

```sql
DROP TABLE IF EXISTS Bookmark;
```

```text
Updated 0 rows.
```

Verify the table is gone:

```sql
SELECT COUNT(*) AS bookmark_exists FROM SYSTEM.TABLES WHERE NAME = 'BOOKMARK';
```

```text
╔═════════════════╗
║ BOOKMARK_EXISTS ║
╠═════════════════╣
║ 0               ║
╚═════════════════╝
```

The Music Store data remains intact for future tutorials. Type `exit;` to leave the SQL sub-REPL, then `exit` again to close the CLI.

{% hint style="success" %}
**Checkpoint:** `SYSTEM.TABLES` returns 0 for the BOOKMARK count. The 11 Music Store tables are unaffected.
{% endhint %}

## Summary

Throughout this tutorial, `EXPLAIN` revealed how the engine handles each type of operation:

- **Primary key operations** use direct key access (`KeyValueModify` for writes) to route straight to the owning node (Step 3).
- **Unindexed filters** produce a `TableScan` across every partition. Create indexes for columns you filter on frequently (Step 4).
- **Colocated joins** (tables partitioned by the same join key, such as Artist and Album) execute locally with no Exchange between the join inputs. Joins that add a table partitioned by a different column, such as Track, shuffle data through an Exchange below the join. Colocation does not chain through a middle table (Step 5).
- **Distributed aggregation** uses a map-reduce pattern: `MapHashAggregate` computes locally, `ReduceHashAggregate` combines results across the Exchange (Step 6).

Two other GridGain-specific behaviors to remember:

- **System catalog views** (`SYSTEM.TABLES`, `SYSTEM.ZONES`, `SYSTEM.INDEXES`) expose cluster metadata as queryable tables.
- **Uppercase normalization** applies to all SQL identifiers in the catalog and query results, regardless of the case used in DDL.

Data locality is the thread running through every plan you read in this tutorial:

- **Colocated joins** between a true pair, such as Artist and Album, execute on each node without crossing the network between join inputs.
- **Map-reduce aggregation** computes partial results locally, then combines them across the Exchange.
- **Primary key operations** route directly to the node that owns the key.

The same principle extends beyond SQL: the Compute API pushes application code to the node that owns the data, eliminating the network round-trip. See [About Distributed Computing](../../../gridgain9-development/distributed-computing/about-distributed-computing.md) for that pattern.

The cluster and dataset are ready for the next step: writing a Java application that connects to the cluster and works with the same data through the thin client API.

## Next Step

Continue to [Connect with the Java Thin Client](connect-java-thin-client.md) to build a Java application that connects to this cluster and works with the same data through the Table API. You'll use RecordView, KeyValueView, and SQL from Java code.

## Related

- [Start Your Local GridGain 9 Development Cluster](../../start-local-cluster.md) for the cluster setup and dataset loading this tutorial builds on
- [How to Work with the GridGain CLI](../../cli-tool-step-by-step.md) for the full CLI reference: file loading, output formatting, cluster inspection

- [Connect with the Java Thin Client](connect-java-thin-client.md) for the Java thin client, Table API, and RecordView
