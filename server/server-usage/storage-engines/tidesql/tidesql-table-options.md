---
description: >-
  The per-table options that configure a TideSQL table's column family at CREATE
  TABLE, their defaults, and the session variables that set those defaults.
---

# TideSQL Table Options

Per-table options set at `CREATE TABLE` are baked into the column family at creation time and shown in `SHOW CREATE TABLE`. Most have a `tidesdb_default_*` session variable, so a deployment can set the policy once and let every `CREATE TABLE` inherit it, with an explicit option overriding the default for one table. The exceptions, noted below, are `TTL`, `ENCRYPTED`, `ENCRYPTION_KEY_ID`, and `ISOLATION_LEVEL`, which are covered in their own pages.

The complete set of options is `COMPRESSION`, `BLOOM_FILTER`, `BLOOM_FPR`, `KEEP_VALUES_INLINE`, `BTREE_KLOG_BLOCK_SIZE`, `LEVEL_SIZE_RATIO`, `MIN_LEVELS`, `DIVIDING_LEVEL_OFFSET`, `L1_FILE_COUNT_TRIGGER`, `TOMBSTONE_DENSITY_TRIGGER`, `TOMBSTONE_DENSITY_MIN_ENTRIES`, `TTL`, `ENCRYPTED`, `ENCRYPTION_KEY_ID`, and `ISOLATION_LEVEL`.

## Compression

```sql
CREATE TABLE archive (id INT PRIMARY KEY, data TEXT) ENGINE=TIDESDB COMPRESSION='ZSTD';
```

The choices are `NONE`, `SNAPPY`, `LZ4`, `ZSTD`, and `LZ4_FAST`, and the default is `LZ4`. `ZSTD` gives the best ratio, while `LZ4` and `LZ4_FAST` favor speed. An encrypted table is the exception: its data column family is created with compression forced to `NONE` regardless of this option, because the rows are already ciphertext by the time they reach the library and ciphertext does not compress. The table's secondary-index column families hold unencrypted comparable keys and keep whatever algorithm was selected. The session default is `tidesdb_default_compression`.

Every backend except `NONE` has to be compiled into the linked TidesDB library, which is a build option there, so a library built without a given backend rejects a table that asks for it and the `CREATE` fails. `NONE` is always available. On a build that omits the default `LZ4`, set `tidesdb_default_compression` to a backend the library carries, or to `NONE`, before creating tables.

## Bloom Filters

```sql
CREATE TABLE no_bloom (id INT PRIMARY KEY, v INT) ENGINE=TIDESDB BLOOM_FILTER=0;
CREATE TABLE precise  (id INT PRIMARY KEY, v INT) ENGINE=TIDESDB BLOOM_FPR=10;
```

Bloom filters let a point lookup skip SSTables that cannot contain the key. `BLOOM_FILTER` enables them, and is on by default. `BLOOM_FPR` is the false-positive rate in parts per 10,000, with a default of 100 for a 1% rate. The session defaults are `tidesdb_default_bloom_filter` and `tidesdb_default_bloom_fpr`.

## Keeping Values Inline

```sql
CREATE TABLE inline_vals (id INT PRIMARY KEY, val VARCHAR(200))
  ENGINE=TIDESDB KEEP_VALUES_INLINE=1;
```

Each SSTable has a key log and a value log. Value separation is a database-wide policy set by `tidesdb_value_separation_threshold`, so a value at or above that size goes to the shared value log with a pointer left in the key log, and a smaller one stays inline. Separating a large value keeps it out of every later merge, which is the whole point of the threshold, at the cost of one value-log read per row on a scan. `KEEP_VALUES_INLINE=1` overrides the policy for one table and holds every value in the key log whatever its size, which is worth it for a table that is scanned far more than it is merged. The session default is `tidesdb_default_keep_values_inline`.

`BTREE_KLOG_BLOCK_SIZE` sets the block size in bytes of the key log's B-tree nodes, with a default of 4096. The default matches the block manager's first-read window so a node is read in one go, and sizing a node just above that window costs a second read on every access. The session default is `tidesdb_default_btree_klog_block_size`.

## LSM-Tree Tuning

```sql
CREATE TABLE tuned (id INT PRIMARY KEY, v VARCHAR(200)) ENGINE=TIDESDB
  LEVEL_SIZE_RATIO=8
  MIN_LEVELS=3
  DIVIDING_LEVEL_OFFSET=1
  L1_FILE_COUNT_TRIGGER=4;
```

`LEVEL_SIZE_RATIO` is how much larger each level is than the previous one, with a default of 10. `MIN_LEVELS` is the minimum tree depth, with a default of 1. `DIVIDING_LEVEL_OFFSET` sets the offset used to compute the dividing level, the primary compaction target, calculated as `num_levels - 1 - DIVIDING_LEVEL_OFFSET`, with a default of 1. `L1_FILE_COUNT_TRIGGER` is how many SSTables may accumulate at level 1 before compaction merges them down, with a default of 4. TidesDB does not use a selectable compaction policy. It chooses among full preemptive merge, dividing merge, and partitioned merge automatically from the tree's state relative to the dividing level. The session defaults are `tidesdb_default_level_size_ratio`, `tidesdb_default_min_levels`, `tidesdb_default_dividing_level_offset`, and `tidesdb_default_l1_file_count_trigger`.

## Tombstone Density Trigger

```sql
CREATE TABLE events (
  id BIGINT PRIMARY KEY, ts DATETIME, body TEXT, KEY (ts)
) ENGINE=TIDESDB
  TOMBSTONE_DENSITY_TRIGGER=5000
  TOMBSTONE_DENSITY_MIN_ENTRIES=2048;
```

After each flush the engine can escalate compaction for any level-1 SSTable whose tombstone count divided by entry count exceeds a ratio, provided the SSTable has enough entries to matter. `TOMBSTONE_DENSITY_TRIGGER` is that ratio in parts per 10,000, so `5000` means 0.50, and the default `0` disables the check. `TOMBSTONE_DENSITY_MIN_ENTRIES` is the entry-count floor, with a default of 1024, that stops a tiny SSTable from firing compaction. `ALTER TABLE ... TOMBSTONE_DENSITY_TRIGGER=N` updates the live column family so the new ratio applies on the next post-flush check without a restart. The session defaults are `tidesdb_default_tombstone_density_trigger` and `tidesdb_default_tombstone_density_min_entries`.

## Options Covered Elsewhere

* `TTL` at the table level and `` `TTL` `` on a column set row expiration. See [Time-To-Live](tidesql-time-to-live.md).
* `ENCRYPTED` and `ENCRYPTION_KEY_ID` turn on data-at-rest encryption. See [Data-at-Rest Encryption](tidesql-encryption.md).
* `ISOLATION_LEVEL` pins the per-table isolation level. See [Transactions and Isolation](tidesql-transactions-and-isolation.md).

## Combining Options

```sql
CREATE TABLE optimized (id INT PRIMARY KEY, val VARCHAR(100)) ENGINE=TIDESDB
  COMPRESSION='ZSTD'
  BLOOM_FILTER=1
  BLOOM_FPR=50
  KEEP_VALUES_INLINE=1
  ISOLATION_LEVEL='REPEATABLE_READ';
```

<sub>_This page is licensed: GPLv2_</sub>
