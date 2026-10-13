---
description: >-
  A complete reference for TideSQL system variables, grouped by scope: flush and
  compaction pool, block cache, memtable, durability, full-text search, and per-
  session table-option defaults.
---

# TideSQL System Variables

This page documents system variables related to the TideSQL storage engine. The read-only group is set at server startup and cannot change while the server runs. The dynamic global group can be changed at runtime with `SET GLOBAL`. The session group can be set per connection with `SET SESSION`, and its global value is the default that new sessions inherit.

## Global, Read-Only Variables

These variables are set at server startup and cannot be changed while the server runs.

#### `tidesdb_flush_threads`

* Description: Background threads flushing memtables to SSTables. `0` uses the library default of 2.
* Command line: `--tidesdb-flush-threads=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4`
* Range: `0` to `64`

#### `tidesdb_compaction_threads`

* Description: Background threads running LSM compaction.
* Command line: `--tidesdb-compaction-threads=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `64`

#### `tidesdb_log_level`

* Description: Library log level.
* Command line: `--tidesdb-log-level=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value: `TRACE`
* Valid Values: `TRACE`, `INFO`, `WARN`, `ERROR`, `NONE`

#### `tidesdb_block_cache_size`

* Description: Size in bytes of the global block cache shared across all column families. `0` uses the library default of 64 MB.
* Command line: `--tidesdb-block-cache-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `268435456` (256 MB)
* Range: `0` to `18446744073709551615`

#### `tidesdb_max_open_sstables`

* Description: Maximum SSTable file handles the library keeps open. `0` uses the library default of 1024. The library lowers the cap at open to fit the process open-file limit. When the cap is full and idle handles cannot be reclaimed in time, a read that has to open another SSTable fails with error 1205 (`ER_LOCK_WAIT_TIMEOUT`).
* Command line: `--tidesdb-max-open-sstables=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `65536`

#### `tidesdb_log_to_file`

* Description: Write library logs to a LOG file in the data directory instead of stderr.
* Command line: `--tidesdb-log-to-file={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `tidesdb_log_truncation_at`

* Description: Log file truncation size in bytes. `0` disables truncation.
* Command line: `--tidesdb-log-truncation-at=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `25165824` (24 MB)
* Range: `0` to `18446744073709551615`

#### `tidesdb_memtable_write_buffer_size`

* Description: Write buffer size in bytes for the shared memtable. `0` uses the library default of 64 MB.
* Command line: `--tidesdb-memtable-write-buffer-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `268435456` (256 MB)
* Range: `0` to `18446744073709551615`

#### `tidesdb_memtable_sync_mode`

* Description: WAL durability for every commit. See [Durability and Sync Modes](tidesql-durability-and-sync-modes.md).
* Command line: `--tidesdb-memtable-sync-mode=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value: `FULL`
* Valid Values: `NONE`, `INTERVAL`, `FULL`

#### `tidesdb_memtable_sync_interval`

* Description: WAL sync interval in microseconds, used only when the sync mode is `INTERVAL`. `0` uses the library default of one second.
* Command line: `--tidesdb-memtable-sync-interval=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `128000`
* Range: `0` to `18446744073709551615`

#### `tidesdb_memtable_skip_list_max_level`

* Description: Skip-list max level for the memtable. `0` keeps the library default of 12.
* Command line: `--tidesdb-memtable-skip-list-max-level=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `32`

#### `tidesdb_memtable_skip_list_probability`

* Description: Skip-list level-promotion probability for the memtable. `0.0` keeps the library default of 0.25.
* Command line: `--tidesdb-memtable-skip-list-probability=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0.0`
* Range: `0.0` to `1.0`

#### `tidesdb_vlog_segment_size`

* Description: Size in bytes at which the value log seals a segment and opens a fresh one. `0` keeps the library default of 256 MB.
* Command line: `--tidesdb-vlog-segment-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `tidesdb_value_separation_threshold`

* Description: Values at or above this size in bytes go to the shared value log instead of inline in the klog, so compaction rewrites only a reference. Database-wide, applied at open. `0` keeps the library default of 1024 bytes.
* Command line: `--tidesdb-value-separation-threshold=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `tidesdb_memtable_l0_queue_stall_threshold`

* Description: Sealed-memtable queue depth at which writes are paced for back-pressure. `0` keeps the library default of 16.
* Command line: `--tidesdb-memtable-l0-queue-stall-threshold=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `65535`

#### `tidesdb_memtable_idle_flush_seconds`

* Description: Seconds of write inactivity after which the shared memtable is flushed even before it fills. `0` turns the idle flush off and `-1` keeps the library default of 30 seconds.
* Command line: `--tidesdb-memtable-idle-flush-seconds=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `86400`

#### `tidesdb_txn_timeout_seconds`

* Description: Seconds a transaction may run before the library aborts it, after which its statements fail with a lock wait timeout. `-1` keeps the library default of no timeout, and `0` also means no timeout.
* Command line: `--tidesdb-txn-timeout-seconds=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `2147483647`

#### `tidesdb_data_home_dir`

* Description: Directory for the data files.
* Command line: `--tidesdb-data-home-dir=path`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`
* Default Value: (empty). When unset, the engine uses `<mysql_datadir>/../tidesdb_data`.

## Global, Dynamic Variables

These variables are global and can be changed at runtime with `SET GLOBAL`.

#### `tidesdb_backup_dir`

* Description: Set to a path to trigger an online backup. The last directory of the path is created if missing and its parent must exist. The directory must be new or empty, and one that already holds files is refused. Clear with an empty string. See [Backup and Checkpoint](tidesql-backup-and-checkpoint.md).
* Command line: `--tidesdb-backup-dir=path`
* Scope: Global
* Dynamic: Yes
* Data Type: `directory name`
* Default Value: (empty)

#### `tidesdb_checkpoint_dir`

* Description: Set to a path to write a consistent checkpoint copy of the database there. The memtable is flushed and the WAL, value log, and manifest are synced, then the manifest, the value log, and every SSTable the manifest references are copied. The last directory of the path is created if missing and its parent must exist. The directory must be new or empty, and one that already holds files is refused. Clear with an empty string.
* Command line: `--tidesdb-checkpoint-dir=path`
* Scope: Global
* Dynamic: Yes
* Data Type: `directory name`
* Default Value: (empty)

#### `tidesdb_fts_min_word_len`

* Description: Minimum word length in characters for full-text indexing.
* Command line: `--tidesdb-fts-min-word-len=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `3`
* Range: `1` to `84`

#### `tidesdb_fts_max_word_len`

* Description: Maximum word length in characters for full-text indexing.
* Command line: `--tidesdb-fts-max-word-len=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `84`
* Range: `1` to `512`

#### `tidesdb_fts_bm25_k1`

* Description: BM25 k1 parameter, term-frequency saturation.
* Command line: `--tidesdb-fts-bm25-k1=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1.2`
* Range: `0` to `10`

#### `tidesdb_fts_bm25_b`

* Description: BM25 b parameter, document-length normalization.
* Command line: `--tidesdb-fts-bm25-b=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0.75`
* Range: `0` to `1`

#### `tidesdb_fts_blend_chars`

* Description: Characters treated as both separators and word characters. Set to `'` for Italian and French elision. See [Full-Text Search](tidesql-full-text-search.md).
* Command line: `--tidesdb-fts-blend-chars=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: (empty)

#### `tidesdb_ft_stopword_table`

* Description: Custom stop-word table in `db_name/table_name` form, with a `VARCHAR` column named `value`. `NULL` or an empty string uses the InnoDB default list. A value set in my.cnf is loaded at startup, and an unreadable table there logs a warning and keeps the default list. `SET GLOBAL` to a table that cannot be read fails with `ER_WRONG_VALUE_FOR_VAR` and keeps the old value.
* Command line: `--tidesdb-ft-stopword-table=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `NULL`

## Session Variables With a Global Default

These variables are session-scoped. Setting one globally changes the default that new sessions inherit. The `tidesdb_default_*` group supplies the default for the matching [table option](tidesql-table-options.md) when `CREATE TABLE` does not set it.

#### `tidesdb_ttl`

* Description: Per-session TTL in seconds applied to `INSERT` and `UPDATE`. `0` uses the table default. Works with `SET SESSION` and `SET STATEMENT`. See [Time-To-Live](tidesql-time-to-live.md).
* Command line: `--tidesdb-ttl=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `tidesdb_skip_unique_check`

* Description: Skip uniqueness checks on the primary key and unique secondary indexes during `INSERT` and `UPDATE`. It also skips the sentinel key each `UNIQUE` secondary value writes to the reserved `__tidesdb_uniq` column family, which is what makes two concurrent transactions writing the same `UNIQUE` value collide at commit, so the second to commit fails its `COMMIT` with `ER_ERROR_DURING_COMMIT` (1180) wrapping handler error 149. Because the sentinel is skipped, rows written with this on are not protected from a concurrent duplicate later either. Safe only when the application guarantees no duplicates.
* Command line: `--tidesdb-skip-unique-check={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `tidesdb_single_delete_primary`

* Description: Use single-delete semantics on the primary row column family for this session's `DELETE` statements, so compaction can drop a deleted row and its tombstone together. Enabling it is a promise that the session runs no `UPDATE` of non-key columns, no `REPLACE INTO`, and no `INSERT ... ON DUPLICATE KEY UPDATE` on tables without secondary indexes, so leave it `OFF` unless the session only inserts and deletes. This is safe only when the workload meets the contract described in [TideSQL Write-Path Optimizations](tidesql-write-path-optimizations.md).
* Command line: `--tidesdb-single-delete-primary={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `tidesdb_compact_after_range_delete_min_rows`

* Description: After a multi-row `DELETE` touching at least this many rows, flush the memtable and compact the touched primary-key range once its transaction commits. A rolled back `DELETE` compacts nothing. `0` disables it.
* Command line: `--tidesdb-compact-after-range-delete-min-rows=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `tidesdb_default_compression`

* Description: Default `COMPRESSION` for new tables.
* Command line: `--tidesdb-default-compression=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `LZ4`
* Valid Values: `NONE`, `SNAPPY`, `LZ4`, `ZSTD`, `LZ4_FAST`

#### `tidesdb_default_bloom_filter`

* Description: Default `BLOOM_FILTER` for new tables.
* Command line: `--tidesdb-default-bloom-filter={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `tidesdb_default_bloom_fpr`

* Description: Default `BLOOM_FPR` in parts per 10,000, 100 is 1%.
* Command line: `--tidesdb-default-bloom-fpr=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `1` to `10000`

#### `tidesdb_default_keep_values_inline`

* Description: Default `KEEP_VALUES_INLINE` for new tables. When `ON`, a table holds every value in its klog whatever its size, ignoring `tidesdb_value_separation_threshold`.
* Command line: `--tidesdb-default-keep-values-inline={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `tidesdb_default_btree_klog_block_size`

* Description: Default `BTREE_KLOG_BLOCK_SIZE` in bytes for new tables. Sizing a node to the block manager first-read window avoids a second read per access.
* Command line: `--tidesdb-default-btree-klog-block-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4096`
* Range: `512` to `18446744073709551615`

#### `tidesdb_default_l1_file_count_trigger`

* Description: Default `L1_FILE_COUNT_TRIGGER`.
* Command line: `--tidesdb-default-l1-file-count-trigger=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `1024`

#### `tidesdb_default_level_size_ratio`

* Description: Default `LEVEL_SIZE_RATIO`.
* Command line: `--tidesdb-default-level-size-ratio=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Range: `2` to `100`

#### `tidesdb_default_min_levels`

* Description: Default `MIN_LEVELS`.
* Command line: `--tidesdb-default-min-levels=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `64`

#### `tidesdb_default_dividing_level_offset`

* Description: Default `DIVIDING_LEVEL_OFFSET`.
* Command line: `--tidesdb-default-dividing-level-offset=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `64`

#### `tidesdb_default_isolation_level`

* Description: Default `ISOLATION_LEVEL`. See [Transactions and Isolation](tidesql-transactions-and-isolation.md).
* Command line: `--tidesdb-default-isolation-level=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `REPEATABLE_READ`
* Valid Values: `READ_UNCOMMITTED`, `READ_COMMITTED`, `REPEATABLE_READ`, `SNAPSHOT`, `SERIALIZABLE`

#### `tidesdb_default_tombstone_density_trigger`

* Description: Default `TOMBSTONE_DENSITY_TRIGGER` in parts per 10,000, `0` disables it. When set, compaction is escalated when any SSTable at any level has a tombstone count divided by entry count at or above the ratio.
* Command line: `--tidesdb-default-tombstone-density-trigger=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `10000`

#### `tidesdb_default_tombstone_density_min_entries`

* Description: Default `TOMBSTONE_DENSITY_MIN_ENTRIES`, the minimum entry count for an SSTable to be judged by the tombstone-density trigger.
* Command line: `--tidesdb-default-tombstone-density-min-entries=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1024`
* Range: `0` to `18446744073709551615`

## Setting Defaults in my.cnf

{% code title="my.cnf" %}
```ini
[mysqld]
plugin-load-add=ha_tidesdb.so
tidesdb_memtable_sync_mode=NONE
tidesdb_default_compression=NONE
tidesdb_default_bloom_fpr=10
tidesdb_value_separation_threshold=64
```
{% endcode %}

```sql
-- new tables inherit the global defaults
CREATE TABLE t1 (id INT PRIMARY KEY) ENGINE=TIDESDB;

-- override one option for one table
CREATE TABLE t2 (id INT PRIMARY KEY) ENGINE=TIDESDB COMPRESSION='ZSTD';

-- change a default for this session only
SET SESSION tidesdb_default_bloom_fpr = 50;
```

<sub>_This page is licensed: GPLv2_</sub>
