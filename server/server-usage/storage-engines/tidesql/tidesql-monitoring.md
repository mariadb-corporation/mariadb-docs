---
description: >-
  What SHOW ENGINE TIDESDB STATUS reports, the handful of numbers that tell you
  the TideSQL engine is healthy, and what to alert on.
---

# TideSQL Monitoring

TideSQL exposes engine state two ways. `SHOW ENGINE TIDESDB STATUS` prints a human-readable report, and `SHOW GLOBAL STATUS LIKE 'tidesdb%'` returns machine-readable counters for a monitoring agent. The full counter list is in [TideSQL Status Variables](tidesql-status-variables.md). This page is about which of them matter.

The counters are refreshed on demand behind a short coalescing window rather than by a background thread, so a burst of reads in one `SHOW` triggers a single stats pass and rapid polling reuses the snapshot. A counter can therefore be up to a couple of seconds stale, which is fine for monitoring and worth remembering if you sample immediately after a schema change.

## SHOW ENGINE TIDESDB STATUS

```sql
SHOW ENGINE TIDESDB STATUS\G
```

The report is organized into sections:

* **Identity**: data directory, column family count, global sequence, min snapshot sequence, and active transaction count.
* **Memory**: memtable bytes and transaction memory bytes.
* **Storage**: total SSTables, open SSTable handles, total data size, and immutable memtable count.
* **Background**: flush pending, compaction pending, whether a flush is in flight, the WAL generation, and the next column family index.
* **Write Amplification**: user bytes written, flush and compaction bytes with their SSTable counts, compaction bytes read, value-log bytes written, and the derived total WA ratio, whose numerator sums flush, compaction, and value-log output so value separation is not under-counted.
* **Value Log**: file size, indexed value count, used bytes, the stored, live, and dead byte totals, the segment count with how many are drainable or retired, and the reclaim calls and passes.
* **Write Stalls**: writes throttled, writes blocked, total stall time, and admission ceiling hits.
* **Block Cache**: enabled, entries, size, hits, misses, hit rate, and partitions.
* **IO Device Writes**: per-device write count, bytes, and average and worst write latency for the three devices the descriptor manager meters, the SSTable, WAL, and value-log devices, and these are write-side figures only.
* **Write Stalls By Reason**: the stall count with total and worst time for each cause a commit can stall on, splitting the aggregate stall time above across WAL append, memtable rotation, admission backlog, and manifest commit.
* **Key Log Encoding** and **Value Log Encoding**: the chain count with the logical and stored byte totals and the realized compression ratio for each log.
* **Tombstones**: total tombstones, the database-wide tombstone ratio, and the worst per-SSTable density with the level it sits at.
* **Column Families**: a per-family breakdown after the aggregate sections, with each family's level distribution, read amplification, B-tree shape, unflushed key count, and tombstone ratio, followed by a per-level line of SSTable count, keys, tombstones, and bytes.

## The Numbers to Watch

If you graph a few things, graph these.

### write_stall_ceiling_hits

Healthy is zero. Alert on any sustained increase. This counts commits admitted only because the backpressure wait ceiling expired, the point where the engine stopped waiting for flush to drain and let the write through to keep a stuck flush from becoming a stuck database. A non-zero value is the clearest single signal that ingest has outrun flush.

### immutable_memtables and flush_pending

Healthy is near zero, spiking briefly under load. These are sealed memtables waiting to be flushed. A count that sits above zero means flush is not keeping up with ingest, and it is the leading indicator for the stalls above. You will see it climb before writers start being held.

### writes_throttled and writes_blocked

These count commits the admission policy made dwell, and commits it made wait for the flush queue to drain. Rising values under a steady workload point at the same flush-behind-ingest condition as the two above, at an earlier stage.

### Block Cache hit_rate

Watch the trend rather than the value, since what is healthy depends on the workload. Because the hit and miss counts are cumulative since open, compare deltas between two samples rather than reading the absolute rate. A falling hit rate on a stable workload means the working set has outgrown `tidesdb_block_cache_size`.

### tombstone_ratio and max_sst_tombstone_density

A climbing tombstone ratio on a delete-heavy or update-heavy table means dead entries are accumulating faster than compaction reclaims them, which shows up as slower range scans. The [TideSQL Table Maintenance](tidesql-table-maintenance.md) page covers `OPTIMIZE TABLE` and the tombstone-density trigger for acting on it.

### min_snapshot_sequence versus global_sequence

`min_snapshot_sequence` is the oldest snapshot still pinned, the floor below which compaction cannot reclaim old versions. When it lags far behind `global_sequence` a long-running transaction is holding back garbage collection, which keeps old versions and their space alive. A large and growing gap is the signal to find and end that transaction.

### Encoding Ratio

Divide `Tidesdb_klog_logical_bytes` by `Tidesdb_klog_stored_bytes`, and the value-log pair the same way, for the realized compression ratio of each log. A ratio near 1.0 on data you expected to compress means the codec is spending CPU for little gain, so the encoding pipeline is worth revisiting for that workload. The per-chain codec breakdown in `SHOW ENGINE TIDESDB STATUS` shows which codecs are in play.

<sub>_This page is licensed: GPLv2_</sub>
