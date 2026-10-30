---
description: >-
  Reading ANALYZE TABLE statistics, forcing compaction with OPTIMIZE and REPAIR,
  and what CHECK TABLE verifies on TideSQL tables.
---

# TideSQL Table Maintenance

## ANALYZE TABLE

`ANALYZE TABLE` refreshes the cached statistics and reports the column family internals as note-level rows in the result set, one block for the data CF and one for each secondary-index CF. Running it is optional for query planning, since the engine samples secondary-index cardinality automatically the first time a populated table is planned against, as described in [TideSQL Statistics and the Optimizer](tidesql-statistics-and-optimizer.md). `ANALYZE TABLE` re-samples the same figures on demand and surfaces the internals below:

```
[TIDESDB] CF 'demo__products'  total_keys=10  data_size=636 bytes  levels=3  read_amp=1.00
[TIDESDB] avg_key=18.8 bytes  avg_value=44.0 bytes
[TIDESDB] level 1  sstables=0  size=0 bytes  keys=0
[TIDESDB] level 2  sstables=0  size=0 bytes  keys=0
[TIDESDB] level 3  sstables=1  size=636 bytes  keys=10
[TIDESDB] idx CF 'demo__products__idx_idx_category'  keys=10  data_size=449 bytes  levels=3
[TIDESDB] idx 'idx_category' sampled=10 distinct=4 rec_per_key=2
```

The summary line reports the key count (SSTable entries, which can still include superseded versions of a key, plus what is still in the memtable), the data size, the deepest level that holds an SSTable, and the read amplification factor. Memtable and block-cache figures are database-level in TidesDB 10 and appear in `SHOW ENGINE TIDESDB STATUS` rather than per CF. Below the summary come the average key and value sizes and a per-level breakdown of SSTable count, size, and keys. Each secondary index then gets a line with its column family's key count, data size, and levels, and each non-unique index gets a line with the entries sampled (up to 100,000), the distinct index prefixes seen, and the resulting `rec_per_key`. An index whose sample hits a read error keeps the statistics it had and gets a `could not sample index` note instead.

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
[TIDESDB] WA  user=4096  wal=4096  flush=8192  compact_write=12288 (3 compactions)  compact_read=8192  ratio=6.00x
```

`user` is the logical bytes the engine wrote through the library's API, `wal` is the WAL bytes attributed to this family, `flush` and `compact_write` are the bytes written to SSTables by flush and by compaction, the count in parentheses after `compact_write` is the number of compactions the family has run, `compact_read` is the bytes compaction pulled in as input, and `ratio` is `(wal + flush + compact_write) / user`. Comparing `flush` with `compact_write` shows where the amplification comes from. A high ratio driven mostly by `compact_write` over many compactions points at L1 churn or an under-sized `L1_FILE_COUNT_TRIGGER`, while one driven mostly by `wal` and `flush` points at the cost of getting writes to disk rather than at compaction.

## OPTIMIZE TABLE

`OPTIMIZE TABLE` runs a synchronous compaction on every column family of the table, the data CF and each secondary-index CF, by calling `tidesdb_compact()` on each and blocking until it finishes. `tidesdb_compact()` runs one forced compaction pass, merging even when no trigger is due. It does not flush the memtable first, so rows still in the memtable are not part of the pass. The cached statistics are invalidated afterwards so the optimizer sees the post-compaction state promptly.

If a background compaction already holds one of the column families, `tidesdb_compact()` does not queue behind it and reports the family busy. `OPTIMIZE` then pushes a note saying a compaction was already in flight and returns `HA_ADMIN_TRY_ALTER`, which MariaDB answers by recreating the table and analyzing it ("Table does not support optimize, doing recreate + analyze instead"). On a busy table, the statement can therefore turn into a full table rebuild. Any other compaction error is logged as a warning in the error log, and the statement still reports `OK`.

```sql
OPTIMIZE TABLE products;
```

This is the tool to reach for after bulk deletes or updates that leave a large tombstone backlog, or when `ANALYZE TABLE` reports high read amplification.

## CHECK TABLE and REPAIR TABLE

`CHECK TABLE` fetches the statistics of every column family of the table, the data CF and each secondary-index CF, through `tidesdb_get_cf_stats()`, and reports the table as corrupt if any of those calls fails. The library builds these statistics from the SSTable metadata it already holds in memory, so the check is cheap but shallow. It does not read data blocks or verify their checksums.

```sql
CHECK TABLE orders;
```

`REPAIR TABLE` runs the same forced compaction pass (`tidesdb_compact()`) on every column family, close to `OPTIMIZE TABLE` but stricter about failure. Any failure to compact the data column family, including a background compaction already holding it, fails the repair rather than falling back to a rebuild. A failure on a secondary-index column family is logged as a warning, and the repair still reports OK. A read or corruption error in the SSTables the data CF merge reads fails the repair rather than being skipped. As with any merge, expired TTL entries are rewritten as tombstones, and tombstones become eligible to drop once the merge reaches the largest level.

```sql
REPAIR TABLE orders;
```

<sub>_This page is licensed: GPLv2_</sub>
