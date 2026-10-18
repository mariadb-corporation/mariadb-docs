---
description: >-
  Set up a 3-node GridGain 9 cluster with Docker Compose and load the Music Store sample dataset.
---

# Start Your Local GridGain 9 Development Cluster

## Introduction

Your application needs a local GridGain 9 cluster for development and testing. In this tutorial, you start a 3-node cluster with Docker Compose, create distribution zones and tables, and load the Music Store sample dataset. Every other tutorial in this section assumes you have completed this setup or have an equivalent environment running.

## Prerequisites

- **Docker** 20.10 or later
- **Docker Compose** 2.23.1 or later (ships with Docker Desktop)
- **curl** and [**jq**](https://jqlang.github.io/jq/download/) for verifying cluster health
- **Ports 10300-10302 and 10800-10802** available on your machine
- **12 GB of available RAM** for three cluster nodes (4 GB minimum; see the memory note in Step 1)
- **GridGain 9 only:** A GridGain 9 license file. If you are interested in trying out GridGain 9, contact our support. Save the license file as `gridgain-license.json` in your project directory alongside `docker-compose.yml`.

If you just need the cluster running and don't need the guided walkthrough, follow [How to Start a Cluster with Docker Compose](../../gridgain9-management/installation/start-cluster-docker-compose.md) instead.

## What You Will Learn

- How to start and initialize a multi-node GridGain 9 cluster
- How distribution zones control data replication and partitioning
- How colocation keeps related data on the same node for local joins
- How to load and verify a sample dataset with SQL

## What You Will Build

A running 3-node cluster with the Music Store sample dataset loaded and verified. The dataset contains 11 tables organized across 2 distribution zones, with over 15,000 records covering artists, albums, tracks, customers, invoices, and playlists. Three colocation chains keep related data on the same node: Artist to Album to Track, Customer to Invoice to InvoiceLine, and Playlist to PlaylistTrack.

## Step 1: Start a 3-Node Cluster

Create a directory for your project and add a file named `docker-compose.yml` with the following content.

Ensure your `gridgain-license.json` file (from the prerequisites) is in the same directory where you create `docker-compose.yml`.

{% code title="docker-compose.yml" %}
```yaml
name: gridgain9

x-gridgain-def: &gridgain-def
  image: gridgain/gridgain9:latest
  environment:
    JVM_MAX_MEM: "4g"
    JVM_MIN_MEM: "4g"
  configs:
    - source: node_config
      target: /opt/gridgain/etc/gridgain-config.conf

services:
  node1:
    <<: *gridgain-def
    container_name: gridgain9-node1
    command: --node-name node1
    ports:
      - "10300:10300"
      - "10800:10800"

  node2:
    <<: *gridgain-def
    container_name: gridgain9-node2
    command: --node-name node2
    ports:
      - "10301:10300"
      - "10801:10800"
    depends_on:
      - node1

  node3:
    <<: *gridgain-def
    container_name: gridgain9-node3
    command: --node-name node3
    ports:
      - "10302:10300"
      - "10802:10800"
    depends_on:
      - node1
      - node2

configs:
  node_config:
    content: |
      ignite {
        network {
          port: 3344
          nodeFinder.netClusterNodes = ["node1:3344", "node2:3344", "node3:3344"]
        }
      }
```
{% endcode %}

Each node exposes two ports: **10300** for the REST management API and **10800** for client connections (JDBC, ODBC, and thin client drivers). The GridGain CLI is bundled inside the server image, so you access it via `docker exec` on any running node. Port 3344 handles internal cluster communication over Docker's network.

{% hint style="info" %}
Reduce `JVM_MAX_MEM` and `JVM_MIN_MEM` to `1g` if your machine has less than 16 GB of RAM. Performance is adequate for development and tutorial workloads.
{% endhint %}

Start the cluster:

```bash
docker compose up -d
```

```text
[+] Running 4/4
 ✔ Network gridgain9_default  Created
 ✔ Container gridgain9-node1  Started
 ✔ Container gridgain9-node2  Started
 ✔ Container gridgain9-node3  Started
```

The nodes need 30-60 seconds to discover each other over port 3344 and form a topology. Wait for the REST API to become available, then initialize the cluster. Initialization is a one-time step that elects a leader, designates which nodes store cluster metadata, and opens client connection ports (10800).

Load the license file into a shell variable. `jq -Rs` reads the file and encodes it as a JSON string with proper escaping:

```bash
LICENSE=$(jq -Rs . gridgain-license.json)
```

Initialize the cluster with the license:

```bash
curl -X POST http://localhost:10300/management/v1/cluster/init \
  -H "Content-Type: application/json" \
  -d '{"metaStorageNodes":["node1","node2","node3"],"cmgNodes":["node1","node2","node3"],"clusterName":"my-cluster","license":'"$LICENSE"'}'
```

A successful initialization returns HTTP 200 with an empty response body. Verify all three nodes joined:

```bash
curl -s http://localhost:10300/management/v1/cluster/state | jq .
```

```json
{
  "cmgNodes": ["node1", "node2", "node3"],
  "msNodes": ["node1", "node2", "node3"],
  "igniteVersion": "3.1.0",
  "clusterTag": {
    "clusterName": "my-cluster",
    "clusterId": "0d7e610e-7363-40a2-97d5-1fb1433b82a0"
  }
}
```

Both `cmgNodes` (cluster management group) and `msNodes` (metastorage nodes) list all three nodes. The cluster is healthy and accepting client connections on ports 10800-10802.

For the full cluster setup procedure, lifecycle management (stop, restart, destroy), and troubleshooting, see [How to Start a Cluster with Docker Compose](../../gridgain9-management/installation/start-cluster-docker-compose.md).

Before moving on, download the sample data file you will load in Step 4. This file contains INSERT statements for over 15,000 records across all 11 tables:

* [music-store-data.sql](../../.gitbook/assets/music-store-data.sql)

If you plan to use the CLI via `docker exec` (the Docker CLI tab in the next steps), copy the file into the running node container so the CLI can access it:

```bash
docker cp music-store-data.sql gridgain9-node1:/tmp/music-store-data.sql
```

{% hint style="success" %}
**Checkpoint:** The cluster state response lists all three nodes in both `cmgNodes` and `msNodes`.
{% endhint %}

## Step 2: Create the Distribution Zones

With the cluster running, you define how data is distributed across nodes. Start the CLI and connect to the cluster:

{% tabs %}
{% tab title="Docker CLI: GridGain 9" %}

Open the CLI inside a running node with `docker exec`. The CLI is bundled in the server image at `/opt/gridgain9cli/bin/gridgain9`:

```bash
docker exec -it gridgain9-node1 /opt/gridgain9cli/bin/gridgain9
```

At the CLI prompt, connect. Inside the container, the REST API is on localhost:

```text
connect http://localhost:10300
```

{% endtab %}

{% tab title="Native CLI: GridGain 9" %}

If you installed the GridGain CLI on your host machine (see [How to Work with the GridGain CLI](../../gridgain9-management/cli-tool-step-by-step.md)), start it directly:

```bash
gridgain9
```

Connect to the cluster through the mapped host port:

```text
connect http://localhost:10300
```

{% endtab %}

{% endtabs %}

```text
Connected to http://localhost:10300
```

Enter the SQL sub-REPL:

```text
[node1]> sql
```

The prompt changes to `sql-cli>`. SQL statements must end with a semicolon.

A distribution zone defines the replication and partitioning policy for a set of tables. `REPLICAS` controls how many copies of each partition the cluster maintains across nodes. `PARTITIONS` controls how the data is split for parallel processing. Create two zones with different replication strategies:

```sql
CREATE ZONE IF NOT EXISTS MusicStore
  WITH REPLICAS=2, PARTITIONS=25, STORAGE_PROFILES='default';
```

```text
Updated 0 rows.
```

```sql
CREATE ZONE IF NOT EXISTS MusicStoreReplicated
  WITH REPLICAS=3, PARTITIONS=25, STORAGE_PROFILES='default';
```

```text
Updated 0 rows.
```

The two zones serve different access patterns:

- **`MusicStore`** stores business data with 2 replicas. Each partition lives on 2 of your 3 nodes, providing fault tolerance if one node goes down.
- **`MusicStoreReplicated`** stores reference data with 3 replicas (one per node). Lookups against reference tables like Genre and MediaType resolve locally without network hops.

Two replicas is sufficient for development. Size for your availability requirements in production.

Verify both zones were created by querying the system catalog:

```sql
SELECT NAME, PARTITIONS, REPLICAS FROM SYSTEM.ZONES;
```

```text
╔══════════════════════╤════════════╤══════════╗
║ NAME                 │ PARTITIONS │ REPLICAS ║
╠══════════════════════╪════════════╪══════════╣
║ Default              │ 25         │ 1        ║
╟──────────────────────┼────────────┼──────────╢
║ MUSICSTORE           │ 25         │ 2        ║
╟──────────────────────┼────────────┼──────────╢
║ MUSICSTOREREPLICATED │ 25         │ 3        ║
╚══════════════════════╧════════════╧══════════╝
```

Three zones appear.

- **`Default`** ships with every cluster and uses 1 replica. Tables assigned to `Default` have no fault tolerance, so you create explicit zones with the replication policy your data requires.
- **`MUSICSTORE`** has 2 replicas for partitioned business data.
- **`MUSICSTOREREPLICATED`** has 3 replicas (one per node) for reference data that every node needs locally.

{% hint style="success" %}
**Checkpoint:** The `SYSTEM.ZONES` query shows `MUSICSTORE` with 2 replicas and `MUSICSTOREREPLICATED` with 3 replicas.
{% endhint %}

## Step 3: Create the Music Store Tables

Now that the zones exist, create the tables that hold the Music Store data. The tables are organized into four groups based on their distribution strategy.

### Reference Data (replicated zone)

Genre and MediaType are small lookup tables that every query might need. Placing them in `MusicStoreReplicated` (3 replicas) means every node has a complete copy, so joins against reference data never require network round-trips.

```sql
CREATE TABLE IF NOT EXISTS Genre (
    GenreId INT NOT NULL,
    Name VARCHAR(120),
    PRIMARY KEY (GenreId)
) ZONE MusicStoreReplicated;
```

```text
Updated 0 rows.
```

```sql
CREATE TABLE IF NOT EXISTS MediaType (
    MediaTypeId INT NOT NULL,
    Name VARCHAR(120),
    PRIMARY KEY (MediaTypeId)
) ZONE MusicStoreReplicated;
```

### Music Entities (Partitioned Zone, Colocated)

In a distributed database, a JOIN between two partitioned tables is expensive by default. Each table partitions its rows independently by primary key, so the rows you need to join are scattered across different nodes. The cluster must shuffle data over the network to match them up. This is called a distributed join, and it gets slower as data volume and cluster size grow.

Colocation eliminates this cost. When two tables share a colocation key, the cluster places rows with the same key value on the same node. A JOIN between colocated tables executes locally on each node with no network traffic.

The tradeoff: you choose the colocation key at table creation time, and it optimizes joins along one relationship. Joins on other columns still require network shuffling.

Artist, Album, and Track form a colocation chain:

- **`Artist`** is the root of the chain.
- **`Album`** colocates by `ArtistId`, so all albums by the same artist live on the same node as that artist.
- **`Track`** colocates by `AlbumId`, placing tracks on the same node as their album.

A query that joins Artist to Album to Track for a given artist executes entirely on one node.

```sql
CREATE TABLE IF NOT EXISTS Artist (
    ArtistId INT NOT NULL,
    Name VARCHAR(120) NOT NULL,
    PRIMARY KEY (ArtistId)
) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS Album (
    AlbumId INT NOT NULL,
    ArtistId INT NOT NULL,
    Title VARCHAR(160) NOT NULL,
    PRIMARY KEY (AlbumId, ArtistId)
) COLOCATE BY (ArtistId) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS Track (
    TrackId INT NOT NULL,
    AlbumId INT,
    Name VARCHAR(200) NOT NULL,
    MediaTypeId INT NOT NULL,
    GenreId INT,
    Composer VARCHAR(220),
    Milliseconds INT NOT NULL,
    Bytes INT,
    UnitPrice DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (TrackId, AlbumId)
) COLOCATE BY (AlbumId) ZONE MusicStore;
```

The `COLOCATE BY` clause is GridGain-specific. It tells the cluster which column determines partition placement. Notice that Album's primary key is `(AlbumId, ArtistId)`, not just `AlbumId`. The colocation key (`ArtistId`) must be part of the primary key so the cluster can route rows to the correct partition.

### Business Entities (Partitioned Zone, Colocated)

Customer, Employee, Invoice, and InvoiceLine follow the same pattern. Customer is the root. Invoice colocates by `CustomerId`. InvoiceLine colocates by `InvoiceId`, which chains back to Customer through Invoice.

```sql
CREATE TABLE IF NOT EXISTS Customer (
    CustomerId INT NOT NULL,
    FirstName VARCHAR(40) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Company VARCHAR(80),
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60) NOT NULL,
    SupportRepId INT,
    PRIMARY KEY (CustomerId)
) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS Employee (
    EmployeeId INT NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    Title VARCHAR(30),
    ReportsTo INT,
    BirthDate DATE,
    HireDate DATE,
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60),
    PRIMARY KEY (EmployeeId)
) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS Invoice (
    InvoiceId INT NOT NULL,
    CustomerId INT NOT NULL,
    InvoiceDate DATE NOT NULL,
    BillingAddress VARCHAR(70),
    BillingCity VARCHAR(40),
    BillingState VARCHAR(40),
    BillingCountry VARCHAR(40),
    BillingPostalCode VARCHAR(10),
    Total DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (InvoiceId, CustomerId)
) COLOCATE BY (CustomerId) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS InvoiceLine (
    InvoiceLineId INT NOT NULL,
    InvoiceId INT NOT NULL,
    TrackId INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (InvoiceLineId, InvoiceId)
) COLOCATE BY (InvoiceId) ZONE MusicStore;
```

### Playlist Tables (Partitioned Zone, Colocated)

```sql
CREATE TABLE IF NOT EXISTS Playlist (
    PlaylistId INT NOT NULL,
    Name VARCHAR(120),
    PRIMARY KEY (PlaylistId)
) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS PlaylistTrack (
    PlaylistId INT NOT NULL,
    TrackId INT NOT NULL,
    PRIMARY KEY (PlaylistId, TrackId)
) COLOCATE BY (PlaylistId) ZONE MusicStore;
```

Each `CREATE TABLE` statement returns `Updated 0 rows.` (DDL statements report zero affected rows).

Verify all 11 tables and their colocation keys by querying the system catalog:

```sql
SELECT NAME, ZONE, COLOCATION_KEY_INDEX FROM SYSTEM.TABLES ORDER BY NAME;
```

```text
╔═══════════════╤══════════════════════╤══════════════════════╗
║ NAME          │ ZONE                 │ COLOCATION_KEY_INDEX ║
╠═══════════════╪══════════════════════╪══════════════════════╣
║ ALBUM         │ MUSICSTORE           │ ARTISTID             ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ ARTIST        │ MUSICSTORE           │ ARTISTID             ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ CUSTOMER      │ MUSICSTORE           │ CUSTOMERID           ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ EMPLOYEE      │ MUSICSTORE           │ EMPLOYEEID           ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ GENRE         │ MUSICSTOREREPLICATED │ GENREID              ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ INVOICE       │ MUSICSTORE           │ CUSTOMERID           ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ INVOICELINE   │ MUSICSTORE           │ INVOICEID            ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ MEDIATYPE     │ MUSICSTOREREPLICATED │ MEDIATYPEID          ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ PLAYLIST      │ MUSICSTORE           │ PLAYLISTID           ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ PLAYLISTTRACK │ MUSICSTORE           │ PLAYLISTID           ║
╟───────────────┼──────────────────────┼──────────────────────╢
║ TRACK         │ MUSICSTORE           │ ALBUMID              ║
╚═══════════════╧══════════════════════╧══════════════════════╝
```

The `COLOCATION_KEY_INDEX` column confirms the colocation chains:

- Artist and Album share `ARTISTID`, so they land on the same node.
- Customer and Invoice share `CUSTOMERID`.
- Playlist and PlaylistTrack share `PLAYLISTID`.

Tables without an explicit `COLOCATE BY` clause (Artist, Customer, Employee, Playlist) colocate by their primary key.

{% hint style="info" %}
`SYSTEM.TABLES` is one of several system catalog views. `SYSTEM.ZONES`, `SYSTEM.INDEXES`, and `SYSTEM.SYSTEM_VIEWS` are also available for inspecting cluster state from SQL. Query `SELECT * FROM SYSTEM.SYSTEM_VIEWS` to discover all available views.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The query returns 11 rows. Colocation chains are visible: Artist and Album share `ARTISTID`, Customer and Invoice share `CUSTOMERID`, Playlist and PlaylistTrack share `PLAYLISTID`.
{% endhint %}

## Step 4: Load the Sample Data

The schema is in place. Exit the SQL sub-REPL to return to the main CLI prompt to load the data file you downloaded in Step 1.

```text
sql-cli> exit;
[node1]>
```

The `sql --file` command only works from the main `[node1]>` prompt, not from inside the SQL sub-REPL.

{% tabs %}
{% tab title="Docker CLI" %}

The data file is at `/tmp/music-store-data.sql` inside the container where you copied it in Step 1.

```text
sql --file /tmp/music-store-data.sql
```

{% endtab %}

{% tab title="Native CLI" %}

The data file is in your project directory where you downloaded it in Step 1.

```text
sql --file ./music-store-data.sql
```

{% endtab %}

{% endtabs %}

The CLI reads the entire file and executes each INSERT statement sequentially. The output scrolls as each statement completes:

```text
Updated 25 rows.
Updated 5 rows.
Updated 275 rows.
Updated 347 rows.
...
```

A 15,000-row load takes approximately 10-30 seconds. The CLI is silent during processing.

Verify the data loaded by entering the SQL sub-REPL and checking the track count:

```text
[node1]> sql
```

```sql
SELECT COUNT(*) AS total_tracks FROM Track;
```

```text
╔══════════════╗
║ TOTAL_TRACKS ║
╠══════════════╣
║ 3503         ║
╚══════════════╝
```

3,503 tracks across 347 albums from 275 artists.

{% hint style="success" %}
**Checkpoint:** The track count query returns 3503.
{% endhint %}

## Step 5: Explore the Dataset

The cluster has data. Run a few queries to see how the distribution zones and colocation affect query behavior.

### Colocated Join: Artist to Album to Track

This query joins three tables in the Artist colocation chain. Because Artist, Album, and Track are colocated in the `MusicStore` zone, the join executes locally on each node without shuffling data across the network.

```sql
SELECT a.Name AS Artist, al.Title AS Album, COUNT(t.TrackId) AS Tracks
FROM Artist a
JOIN Album al ON a.ArtistId = al.ArtistId
JOIN Track t ON al.AlbumId = t.AlbumId
GROUP BY a.Name, al.Title
ORDER BY Tracks DESC
LIMIT 5;
```

```text
╔═══════════════╤════════════════╤════════╗
║ ARTIST        │ ALBUM          │ TRACKS ║
╠═══════════════╪════════════════╪════════╣
║ Lenny Kravitz │ Greatest Hits  │ 57     ║
╟───────────────┼────────────────┼────────╢
║ Chico Buarque │ Minha Historia │ 34     ║
╟───────────────┼────────────────┼────────╢
║ Eric Clapton  │ Unplugged      │ 30     ║
╟───────────────┼────────────────┼────────╢
║ Lost          │ Lost, Season 3 │ 26     ║
╟───────────────┼────────────────┼────────╢
║ Lost          │ Lost, Season 1 │ 25     ║
╚═══════════════╧════════════════╧════════╝
```

The three-table join executes efficiently because the `COLOCATE BY` clauses placed related rows on the same node. Without colocation, this query would require the cluster to redistribute data across the network for each join.

### Replicated Zone Query: Genre Distribution

Genre lives in the `MusicStoreReplicated` zone with 3 replicas (one per node). Every node has a complete copy, so this join between Track (partitioned) and Genre (replicated) resolves locally on each node.

```sql
SELECT g.Name AS Genre, COUNT(t.TrackId) AS Tracks
FROM Genre g
JOIN Track t ON g.GenreId = t.GenreId
GROUP BY g.Name
ORDER BY Tracks DESC
LIMIT 10;
```

```text
╔════════════════════╤════════╗
║ GENRE              │ TRACKS ║
╠════════════════════╪════════╣
║ Rock               │ 1297   ║
╟────────────────────┼────────╢
║ Latin              │ 579    ║
╟────────────────────┼────────╢
║ Metal              │ 374    ║
╟────────────────────┼────────╢
║ Alternative & Punk │ 332    ║
╟────────────────────┼────────╢
║ Jazz               │ 130    ║
╟────────────────────┼────────╢
║ TV Shows           │ 93     ║
╟────────────────────┼────────╢
║ Blues              │ 81     ║
╟────────────────────┼────────╢
║ Classical          │ 74     ║
╟────────────────────┼────────╢
║ Drama              │ 64     ║
╟────────────────────┼────────╢
║ R&B/Soul           │ 61     ║
╚════════════════════╧════════╝
```

Rock dominates the catalog at 1,297 tracks. The replicated zone strategy makes these reference-data joins fast regardless of which node handles the query.

### Cross-Chain Aggregation: Revenue by Country

This query joins Customer and Invoice from the Customer colocation chain and aggregates revenue across countries.

```sql
SELECT c.Country, COUNT(i.InvoiceId) AS Orders,
       CAST(SUM(i.Total) AS DECIMAL(10,2)) AS Revenue
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.Country
ORDER BY Revenue DESC
LIMIT 10;
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
╟────────────────┼────────┼─────────╢
║ Chile          │ 7      │ 46.62   ║
╚════════════════╧════════╧═════════╝
```

Customer and Invoice are colocated by `CustomerId`, so the join and aggregation execute locally on each node. The cluster combines per-node results to produce the final ranking.

Type `exit` to leave the SQL sub-REPL, then `exit` again to close the CLI.

## Summary

You built a 3-node GridGain 9 development cluster and loaded the Music Store dataset: 11 tables, over 15,000 records, organized across 2 distribution zones with 3 colocation chains. Along the way, you encountered three core GridGain concepts:

- **Cluster initialization** designates metastorage nodes, elects a leader, and opens client ports. It is a one-time step comparable to bootstrapping a consensus group.
- **Distribution zones** define per-table replication and partitioning policies. The `MusicStore` zone stores business data with 2 replicas for fault tolerance. The `MusicStoreReplicated` zone stores reference data with 3 replicas so every node has a complete copy.
- **Colocation** places related tables on the same node by a shared key, enabling local joins without network round-trips. The Music Store colocates Artist to Album to Track by artist and album ID.

This cluster and dataset are the foundation for every tutorial in this section. Keep it running as you continue to the next steps.

## Next Step

Continue to [Create Tables and Query Data with SQL](query-music-store-sql.md) to explore the Music Store dataset you just loaded. You'll write queries against the 11 tables, use `EXPLAIN` to see how GridGain routes operations across the cluster, and learn how colocation affects join performance.

## Related

- [How to Start a Cluster with Docker Compose](../../gridgain9-management/installation/start-cluster-docker-compose.md) for the full cluster lifecycle: stop, restart, destroy, troubleshooting
- [How to Work with the GridGain CLI](../../gridgain9-management/cli-tool-step-by-step.md) for deeper coverage of the CLI tool
