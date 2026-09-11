---
description: >-
  Reading ANALYZE TABLE statistics, forcing compaction with OPTIMIZE and REPAIR,
  and verifying integrity with CHECK on TideSQL tables.
---

# TideSQL Table Maintenance

## ANALYZE TABLE

`ANALYZE TABLE` refreshes the cached statistics and reports the column family internals as note-level rows in the result set, one block for the data CF and one for each secondary-index CF. Running it is optional for query planning, since the engine samples secondary-index cardinality automatically the first time a populated table is planned against, as described in Statistics and the Optimizer. `ANALYZE TABLE` re-samples the same figures on demand and surfaces the internals below:

```
[TIDESDB] CF 'demo__products'  total_keys=10  data_size=636 bytes  levels=5  read_amp=2.00
[TIDESDB] avg_key=18.8 bytes  avg_value=44.0 bytes
[TIDESDB] level 1  sstables=0  size=0 bytes  keys=0
[TIDESDB] level 2  sstables=1  size=636 bytes  keys=10
[TIDESDB] level 3  sstables=0  size=0 bytes  keys=0
[TIDESDB] idx CF 'demo__products__idx_idx_category'  keys=10  data_size=449 bytes  levels=5
```

The summary line reports the live key count (SSTable keys plus what is still in the memtable), the data size, the number of LSM levels, and the read amplification factor. Memtable and block-cache figures are database-level in TidesDB 10 and appear in `SHOW ENGINE TIDESDB STATUS` rather than per CF. Below the summary come the average key and value sizes and a per-level breakdown of SSTable count, size, and keys.

When a column family holds B+tree nodes, an extra note reports the tree shape:

```
[TIDESDB] btree  nodes=128  max_height=3  avg_height=2.40
```

When a column family keeps partition-range filters resident, a note reports their memory:

```
[TIDESDB] filters  resident=32768 bytes
```

This is the memory the family's per-SSTable routing directories hold outside the block cache, one directory per SSTable, so it grows with the SSTable count and shrinks as compaction merges them.

When a column family has committed any user bytes, a write-amplification note is emitted:

```
[TIDESDB] WA  user=4096  wal=4096  flush=8192  compact_write=12288 (1 ssts)  compact_read=8192  ratio=6.00x
```

`user` is the logical bytes the engine wrote through the library's API, `wal` is the WAL bytes attributed to this family, `flush` and `compact_write` are the bytes written to SSTables by flush and by compaction, `compact_write` also carries the number of SSTables compaction produced, `compact_read` is the bytes compaction pulled in as input, and `ratio` is `(wal + flush + compact_write) / user`. A high ratio with few compaction SSTables points at oversized flushes, and a high ratio with many points at L0 churn or an under-sized `L1_FILE_COUNT_TRIGGER`.

## OPTIMIZE TABLE

`OPTIMIZE TABLE` runs a synchronous compaction on every column family of the table, the data CF and each secondary-index CF, by calling `tidesdb_compact()` on each and blocking until it finishes. When no compaction is already running on those column families, the table is fully compacted once the statement returns, and the cached statistics are invalidated so the optimizer sees the post-compaction state promptly. If a background compaction already holds one of the column families, `OPTIMIZE` does not queue behind it. It returns a status asking the client to retry rather than blocking, since the compaction it wanted is usually already under way.

```sql
OPTIMIZE TABLE products;
```

This is the tool to reach for after bulk deletes or updates that leave a large tombstone backlog, or when `ANALYZE TABLE` reports high read amplification.

## CHECK TABLE and REPAIR TABLE

`CHECK TABLE` verifies that every column family of the table is readable by fetching metadata from all SSTables, which validates that manifests, block indexes, bloom filters, and metadata blocks are intact. An unreadable SSTable is reported as corruption.

```sql
CHECK TABLE orders;
```

`REPAIR TABLE` runs a full compaction (`tidesdb_compact()`) of every column family, close to `OPTIMIZE TABLE` but stricter about failure. Unlike `OPTIMIZE`, it does not defer when a column family is already compacting, and it treats a failure to compact the data column family as a repair failure rather than something to retry. The compaction reads and re-checksums every block, so a block that fails its checksum fails the repair rather than being dropped, and it drops expired TTL data and tombstones as it merges.

```sql
REPAIR TABLE orders;
```

<sub>_This page is licensed: GPLv2_</sub>
