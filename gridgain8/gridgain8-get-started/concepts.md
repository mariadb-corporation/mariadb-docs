---
description: >-
  Overview of the core concepts and components shared by Apache Ignite and
  GridGain, from in-memory computing and clustering to partitioning,
  colocation, and multi-tiered storage.
---

# Concepts

These are main concepts and components of both Apache Ignite and GridGain. Taking a moment to familiarize yourself with
these can help ease you through coming up to speed with the product.

## In-memory Computing

With in-memory computing, processing happens in RAM instead of on disk, utilizing the faster performance inherent in memory architecture.
For (much) more about GridGain's memory architecture, see [Memory Architecture](../architecture/memory-architecture.md).

## Clustering, Servers and Clients

{% include "../.gitbook/includes/gg8-nodes-and-clustering.md" %}

For more information about clustering, see [Clustering](../architecture/clustering.md).

## Thick vs. Thin Clients

{% include "../.gitbook/includes/gg8-thick-and-thin-clients.md" %}

Refer to [this section](../gridgain8-management/installation/deployment-modes.md#choosing-a-client) to decide which type of client works better for you.

## Cache vs. Table

You can notice that both terms "cache" and "table" are used in relation to the structure that holds data sets in Apache Ignite and
GridGain. And both terms are valid because the concepts of a SQL table and a key-value cache are two equivalent
representations of the same (internal) data structure. You can model your applications and, consequently,
access the data using either the key-value APIs or SQL statements, or both.

Check this [documentation section](../architecture/data-modeling/introduction.md#key-value-cache-vs.-sql-table)
for a thorough explanation, but here let us share more insights on why two terms were coined in GridGain instead of
one. It was driven solely by product evolution. Originally (a long time before Apache Ignite and Apache Spark), GridGain
was used as a computation platform that supported map-reduce paradigm at scale and in memory (known as
Ignite/GridGain Compute Grid nowadays). Later, it became obvious that GridGain storage capabilities have to be
embedded into GridGain to avoid expensive data movement/loading into the cluster before the compute engine can kick
off tasks execution. The concept of in-memory **caches** was defined and GridGain turned into a distributed in-memory
cache that supported both the key-value and previously existing Compute Grid APIs. Before donating the original code to
ASF under the new project known as Apache Ignite, GridGain supported the first SQL commands that extended existing
capabilities of key-value caches. Later, Apache Ignite community extended SQL support introducing classical DDL and
DML commands pulling in the concept of relational **tables**. This led to co-existence of two terms and two different
[data modelling](../architecture/data-modeling/introduction.md) approaches in GridGain and Ignite.

Will this situation last forever? Certainly not.  As part of the product evolution,
both Apache Ignite community and GridGain are working on a next version of the APIs that will amalgamate the concepts of
caches and tables. Follow Apache Ignite 3.0 related discussions on Ignite dev list for more details.

## Multi-Tiered Storage

GridGain is based on distributed multi-tiered architecture that combines the performance and scale of
in-memory computing together with the disk durability and strong consistency in one system.

When native persistence is turned on, GridGain functions as a system of records, where most of the
processing happens in memory on cached data, but the superset of data and indexes is persisted to disk.

Alternatively, GridGain can persist changes to an underlying database like an RDBMS or NoSQL accelerating your existing
infrastructure and architectures. This enables the in-memory data grid (IMDG) use case, which is covered [below](#gridgain-as-an-in-memory-data-grid).

## Partitioning and Replication

Data partitioning is a method of subdividing large sets of data into smaller chunks and distributing them between all
server nodes in a balanced manner.

In the partitioned mode, all partitions are split equally between all server nodes. This mode is the most scalable
distributed cache mode and allows you to store as much data as will fit in the total memory (RAM and disk) available
across all nodes. Essentially, the more nodes you have, the more data you can store.

In the replicated mode, all the data (every partition) is replicated to every node in the cluster. This mode
provides the utmost availability of data as it is available on every node. However, every data update must be
propagated to all other nodes, which can impact performance and scalability.

Note that you can use both modes by having partitioned as well as replicated caches/tables in your cluster. For
instance, the replicated mode is advantageous for dictionary-like tables that are relatively small, not updated
frequently but used in many operations like SQL queries with JOINs.

For more information about partitioning and replication, see
[Data Partitioning](../architecture/data-modeling/data-partitioning.md) page.

## Affinity Colocation and Colocated Computations

The amount of data (and data sources) companies have is constantly increasing and is rapidly becoming too big to store
on a single machine, and too big to move over the network. The only way left to scale is horizontally. GridGain
accomplishes this by partitioning data across nodes as well as supporting built-in affinity mechanisms for related
data colocation.

For example, within the DDL used to define the schema, you can declare affinity keys such as foreign keys that
specify which data should be colocated together across two tables. Partitioning the data of two tables by the
foreign key ensures joins can happen on each node with minimal network traffic.

Once the data is colocated, not only complex SQL queries with JOINs will perform much better but advanced tasks and
compute logic you want to perform over a specific data set will be sent to the nodes where the required data is located  and only the results of the computations are sent back.

Refer to [Affinity Colocation](../architecture/data-modeling/affinity-colocation.md)
and [Colocating Computations with Data](../gridgain8-usage/colocating-computations.md) articles for more details.

## GridGain as an In-Memory Data Grid

GridGain's unique multi-tiered storage architecture allows for two primary use cases. The first one is the
in-memory data grid (IMDG) where GridGain slides in between your application layer and an external database
enabling in-memory computing for existing solutions in the most straightforward way.

Refer to [this section](../gridgain8-management/installation/deployment-modes.md#cluster-deployment-modes) for more details.

## GridGain as a System of Record

The second use case is where GridGain is used as a classical system of record. It both caches data
in RAM and persists it in a built-in transactional persistent storage.

In this use case, all of the data is stored on disk and as much as will fit is loaded into RAM. This allows for a much
larger data set as the data that does not fit in memory is still available. For example, if your data set is large
enough that only 10% of it can fit in memory, 100% of the data will be stored on disk and 10% is cached in memory
for performance. This configuration, where the data set is stored in bulk on disk, is called Ignite persistence (or
native persistence).

Refer to [this section](../gridgain8-management/installation/deployment-modes.md#cluster-deployment-modes) for more details.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
