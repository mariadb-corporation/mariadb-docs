---
description: >-
  Definitions of the terms the TideSQL pages use for how the engine maps SQL
  tables, indexes, and transactions onto the TidesDB library.
---

# TideSQL Glossary

This glossary covers terms as TideSQL uses them. The TidesDB library has its own vocabulary for SSTable internals, compaction, and recovery, which the library's documentation covers.

## Column Family

An independent ordered keyspace inside TidesDB, with its own LSM-tree. A TideSQL table is one column family for its rows plus one more for each secondary index. See [TideSQL Data Model](tidesql-data-model.md).

## Comparable Key

The memcmp-comparable byte encoding TideSQL uses for keys, so byte order equals logical order. Integers are stored big-endian with the sign bit flipped, and strings use the collation sort key. See [TideSQL Storage Internals](tidesql-storage-internals.md).

## Conflict Footprint

The keys a transaction records so the library can check it at commit, the keys it writes at `SNAPSHOT` and above, plus the keys and ranges it reads at `SERIALIZABLE`. A concurrent commit to a key in the footprint makes the losing transaction fail its commit. See [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

## Covering Read

A query whose columns are all carried by the index key, so the engine builds the row from the index bytes without a point lookup into the data CF. See [TideSQL Data Model](tidesql-data-model.md).

## Data CF

The column family that holds a table's row data, as opposed to the secondary-index column families.

## Dividing Level

The LSM level, placed relative to the largest level by the `DIVIDING_LEVEL_OFFSET` table option, where a merge writes its output partitioned to the largest level's file boundaries, so later merges can take one group of overlapping files at a time. See [TideSQL Table Options](tidesql-table-options.md).

## First-Committer-Wins

The write-write conflict rule, where the first transaction to commit a change to a row succeeds, and a second transaction that changed the same row fails at commit. It applies from `SNAPSHOT` isolation upward. `SERIALIZABLE` keeps it and adds read-set tracking for full serializable isolation. See [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

## Foreign Key

A referential constraint TideSQL enforces in the engine, checked on every write and persisted in the reserved `__tidesdb_fk_catalog` column family. The supported referential actions are `CASCADE`, `SET NULL`, `RESTRICT`, and `NO ACTION`, and `SET DEFAULT` is checked the same way as `RESTRICT`. See [TideSQL Foreign Keys](tidesql-foreign-keys.md).

## Klog and Vlog

The key log of an SSTable and the database's shared value log. A value smaller than the database's `tidesdb_value_separation_threshold` is stored inline in the klog, and a value at or above it goes to the vlog with a reference left in the klog. A table created with `KEEP_VALUES_INLINE` keeps every value in the klog whatever its size. See [TideSQL Table Options](tidesql-table-options.md).

## Memtable

The in-memory skip list that absorbs writes before they flush to an SSTable. In TidesDB 10 it is shared across the whole database, so its sizing and WAL durability are set by the `tidesdb_memtable_*` system variables rather than per table. See [TideSQL Storage Internals](tidesql-storage-internals.md).

## Optimistic MVCC

The concurrency model, where readers and writers never block each other and a write-write conflict is detected at commit rather than prevented by a lock. See [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

## Prepared Transaction

A transaction durably logged under an XID by the first phase of two-phase commit, waiting for a commit or rollback that can arrive from another connection or, after a restart, through XA recovery. See [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

## Read Amplification

The number of SSTables a worst-case point lookup may probe. The library reports it, and the cost model uses it. See [TideSQL Statistics and the Optimizer](tidesql-statistics-and-optimizer.md).

## Single-Delete

A delete primitive that lets compaction cancel a put and its matching tombstone together the first time they meet, at any level. TideSQL uses it automatically for secondary-index entries, and the primary CF opts in through `tidesdb_single_delete_primary`. Cancelling at any level needs TidesDB 10.1.1 or later, since earlier releases turned a single-delete into a plain tombstone at its first merge. See [TideSQL Write-Path Optimizations](tidesql-write-path-optimizations.md).

## Tombstone

The marker a delete writes to hide an older value until compaction reclaims it. A high tombstone density slows range scans, which the tombstone-density trigger acts on. See [TideSQL Table Options](tidesql-table-options.md).

## Uniqueness Sentinel

A key naming a table, a `UNIQUE` secondary index, and a value, which every write of that value also stores in the reserved `__tidesdb_uniq` column family, so two concurrent writers of the same value collide on one key at commit. See [TideSQL Data Model](tidesql-data-model.md).

## Write-Intent Map

The process-wide record of each uncommitted write's key, which lets a Galera applier find and brute-force abort a local transaction it conflicts with. It is the lock-free analogue of a row lock. See [TideSQL Replication and High Availability](tidesql-replication-and-ha.md).

<sub>_This page is licensed: GPLv2_</sub>
