---
description: >-
  Definitions of the core GridGain 8 terms used throughout this documentation —
  clusters, nodes, caches, partitioning, persistence, and more.
icon: spell-check
---

# Glossary

Core terms used throughout the GridGain 8 documentation.

**Affinity colocation**
Placing related data (and, optionally, computations) on the same node so that operations such as SQL joins run without moving data across the network. See [Affinity Colocation](../architecture/data-modeling/affinity-colocation.md).

**Atomicity mode**
The consistency guarantee configured on a cache — `ATOMIC` for the highest performance, or `TRANSACTIONAL` for full ACID transactions.

**Baseline topology**
The set of server nodes that persist data and are expected to be present in the cluster. See [Baseline Topology](../architecture/baseline-topology.md).

**Binary object**
GridGain's platform-independent representation of cached objects, allowing data written by one language client to be read by another without shared classes.

**Cache**
The primary data structure that holds key-value entries; equivalent to a SQL table. See [Cache vs. Table](../gridgain8-get-started/concepts.md#cache-vs.-table).

**Client node**
A node that connects to the cluster to run application logic but does not store data or contribute to computations by default.

**Cluster**
A group of interconnected nodes that pool their memory and CPU to store and process data.

**Data region**
A configurable block of memory that caches are assigned to, with its own size limits and persistence settings. See [Configuring Data Regions](../gridgain8-usage/memory-configuration/data-regions.md).

**Discovery**
The mechanism by which nodes find and join each other to form a cluster. See [Clustering](../architecture/clustering.md).

**Native persistence**
GridGain's built-in disk store that keeps a superset of the data on disk so the cluster survives restarts and crashes. See [Native Persistence](../architecture/storage/native-persistence.md).

**Partition**
A subset of a cache's data. Partitions are distributed across server nodes to balance storage and load. See [Data Partitioning](../architecture/data-modeling/data-partitioning.md).

**Rebalancing**
The redistribution of partitions across nodes when the cluster topology changes. See [Rebalancing](../architecture/rebalancing/README.md).

**Server node**
A node that stores data and performs computations; the base storage and compute unit of a cluster.

**Thick client**
A client that joins the cluster via its internal protocol, is aware of data distribution, and supports the full GridGain API.

**Thin client**
A lightweight client that connects over a binary protocol with a limited but broad API and no dependency on the JVM.

**WAL (write-ahead log)**
The log GridGain writes changes to before applying them, used to recover a consistent state after a crash when native persistence is enabled.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
