---
description: >-
  How storage engines and storage profiles work in GridGain 9, the engines
  available (aimem, aipersist, rocksdb, columnar), and how node-local
  configuration affects them.
---

# Storage Engines and Profiles

## Storage Engines

Storage engines in GridGain 9 are responsible for storing data on disk or in memory.

Storage engines are configured at the node level in the node configuration under the `ignite.storage.engines` section and are referenced by storage profiles, which are then used by distribution zones.

To check available storage engines on a node, use:

```
node config show ignite.storage.engines
```

## Storage Profiles

Storage profiles reference a specific engine and provide configuration parameters for that engine. Profiles are defined under the `ignite.storage.profiles` section and can be referenced by distribution zones when creating tables.

To check available storage profiles on a node, use:

```
node config show ignite.storage.profiles
```

## Scope of Configuration

Storage engine configuration is node-local, meaning each node in the cluster can have different engine configurations. While tables, zones, and profile names are cluster-wide, the actual implementation of a storage profile is specific to each node. This allows for flexibility in configuring storage characteristics based on the hardware capabilities of individual nodes.

When tables use a specific storage profile, they will be stored on each node according to that node's local configuration of the specified profile. If a node does not have a required profile configured, it will not be able to store the table data.

## Available Storage Engines

GridGain 9 provides the following storage engines:

|Engine|Description|Status|
|---|---|---|
|[aimem](in-memory-storage.md)|Volatile (in-memory) Apache Ignite page memory (B+ tree) for high-performance, non-persistent workloads|Core|
|[aipersist](native-persistent-storage.md)|Persistent Apache Ignite page memory (B+ tree) for durable storage with low latency access|Core|
|[rocksdb](rocksdb-persistent-storage.md)|Persistent RocksDB (LSM tree) optimized for high write throughput|Experimental|
|[columnar](columnar-storage.md)|Secondary storage optimized for analytical queries with column-oriented data organization|Add On|
