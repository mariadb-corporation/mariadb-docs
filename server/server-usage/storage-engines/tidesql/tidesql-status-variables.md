---
description: >-
  Every TideSQL status variable exposed through SHOW GLOBAL STATUS, grouped by
  what it measures, from MVCC sequence and write amplification to block cache
  and tombstones.
---

# TideSQL Status Variables

```sql
SHOW GLOBAL STATUS LIKE 'tidesdb%';
```

These are the machine-readable counters for a monitoring agent such as a Prometheus exporter or PMM. [Monitoring](tidesql-monitoring.md) explains which of them matter and what healthy looks like. They are refreshed on demand behind a short coalescing window, so reading many of them in one statement costs a single stats pass.

All TideSQL status variables are global and are read through `SHOW GLOBAL STATUS`.

## Identity

#### `Tidesdb_version`

* Description: TideSQL plugin version string, for example `5.0.0`.
* Scope: Global
* Data Type: `string`

#### `Tidesdb_version_hex`

* Description: Plugin version as an integer, for example `327680` for `0x50000`.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_library_version`

* Description: Linked TidesDB library version string.
* Scope: Global
* Data Type: `string`

## Sequence and Transactions

#### `Tidesdb_column_families`

* Description: Number of active column families.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_global_sequence`

* Description: Global MVCC sequence number.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_min_snapshot_sequence`

* Description: Oldest pinned snapshot, the floor compaction cannot reclaim past.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_active_transactions`

* Description: Transactions currently joined to the MVCC registry.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_txn_memory_bytes`

* Description: Memory held by in-flight transactions in bytes.
* Scope: Global
* Data Type: `numeric`

## Memory and Storage

#### `Tidesdb_memtable_bytes`

* Description: Bytes in the active memtable.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_total_sstables`

* Description: Total SSTable count across all column families.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_open_sstables`

* Description: Open SSTable file handles.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_data_size_bytes`

* Description: Total on-disk data size in bytes.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_immutable_memtables`

* Description: Sealed memtables waiting to be flushed.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_flush_pending`

* Description: Flushes pending, the immutable memtable queue depth.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_compaction_queue`

* Description: Compaction jobs queued for the worker pool.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_memtable_is_flushing`

* Description: `1` while an immutable is queued or flushing.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_wal_generation`

* Description: Current write-ahead-log generation counter.
* Scope: Global
* Data Type: `numeric`

## Value Log

#### `Tidesdb_vlog_file_size`

* Description: On-disk size of the value log in bytes.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_vlog_value_count`

* Description: Values the value log currently indexes.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_vlog_used_bytes`

* Description: Uncompressed length those values represent.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_vlog_bytes_written`

* Description: Lifetime bytes appended to the value log, output the flush and compaction counters do not see once values separate.
* Scope: Global
* Data Type: `numeric`

## Encoding

Aggregate codec-chain totals summed across every chain, so `logical` divided by `stored` is the realized compression ratio for each log. The per-chain codec breakdown prints in `SHOW ENGINE TIDESDB STATUS`.

#### `Tidesdb_klog_logical_bytes`

* Description: Key-log bytes before encoding, summed across chains.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_klog_stored_bytes`

* Description: Key-log bytes after encoding as stored on disk.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_vlog_encoded_logical_bytes`

* Description: Value-log bytes before encoding, summed across chains.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_vlog_encoded_stored_bytes`

* Description: Value-log bytes after encoding as stored on disk.
* Scope: Global
* Data Type: `numeric`

## Device IO

Write accounting from the library's file-descriptor manager, which meters the SSTable and WAL devices. The value log keeps its own byte accounting in the value-log counters above. These counters are writes only, there is no read-side or syscall figure.

#### `Tidesdb_io_sstable_write_ops`

* Description: SSTable device writes issued since open.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_io_sstable_write_bytes`

* Description: Bytes written to the SSTable device since open.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_io_wal_write_ops`

* Description: WAL device writes issued since open.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_io_wal_write_bytes`

* Description: Bytes written to the WAL device since open.
* Scope: Global
* Data Type: `numeric`

## Write Amplification

#### `Tidesdb_user_bytes_written`

* Description: Logical committed bytes, the write-amplification denominator.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_flush_bytes_written`

* Description: Bytes written to SSTables by flush jobs.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_compaction_bytes_written`

* Description: Bytes written by compaction jobs.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_compaction_bytes_read`

* Description: Bytes compaction read as input.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_flush_count`

* Description: Flushes completed across all column families.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_compaction_count`

* Description: Compactions completed across all column families.
* Scope: Global
* Data Type: `numeric`

## Write Stalls

#### `Tidesdb_writes_throttled`

* Description: Commits the L0 admission policy made dwell before admitting.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_writes_blocked`

* Description: Commits it made wait for the flush queue to drain.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_write_stall_us`

* Description: Total microseconds commits spent held in admission.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_write_stall_ceiling_hits`

* Description: Commits admitted only because the wait ceiling expired. Any sustained increase means flush is not keeping up with ingest.
* Scope: Global
* Data Type: `numeric`

The aggregate counters above sum admission stall time. These per-reason counts split how often a commit stalled by cause, so backpressure can be attributed. The per-reason stall time prints in `SHOW ENGINE TIDESDB STATUS`.

#### `Tidesdb_stall_wal_append`

* Description: Commits that stalled appending to the write-ahead log.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_stall_rotate_lock`

* Description: Commits that stalled taking the memtable rotation lock.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_stall_rotate_work`

* Description: Commits that stalled while a memtable rotation was in progress.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_stall_admission`

* Description: Commits that stalled on the unflushed-backlog admission gate.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_stall_manifest_commit`

* Description: Commits that stalled waiting for a manifest commit.
* Scope: Global
* Data Type: `numeric`

## Block Cache

#### `Tidesdb_cache_entries`

* Description: Cached entry count.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_cache_bytes`

* Description: Bytes used by the block cache.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_cache_hits`

* Description: Cache hits since open.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_cache_misses`

* Description: Cache misses since open.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_cache_hit_rate`

* Description: Hit rate as a percentage.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_cache_partitions`

* Description: Number of cache shards.
* Scope: Global
* Data Type: `numeric`

## Tombstones

#### `Tidesdb_total_tombstones`

* Description: Total tombstones summed across every column family.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_tombstone_ratio`

* Description: Database-wide tombstone count divided by entry count, `0.0` to `1.0`.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_max_sst_tombstone_density`

* Description: Worst single-SSTable tombstone density observed.
* Scope: Global
* Data Type: `numeric`

#### `Tidesdb_max_sst_tombstone_density_level`

* Description: 1-based LSM level where the worst SSTable sits.
* Scope: Global
* Data Type: `numeric`

<sub>_This page is licensed: GPLv2_</sub>
