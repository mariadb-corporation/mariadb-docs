---
description: >-
  A list of MyRocks-specific status variables providing metrics on cache hits,
  compaction statistics, block cache usage, and other internal operations.
---

# MyRocks Status Variables

This page documents status variables related to the [MyRocks](./) storage engine. See [Server Status Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md).

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `Rocksdb_block_cache_add`

* Description: Number of blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_add_failures`

* Description: Number of failures when adding blocks to Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_bytes_read`

* Description: Bytes read from Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_bytes_write`

* Description: Bytes written to Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_data_add`

* Description: Number of data blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_data_bytes_insert`

* Description: Bytes added to the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_data_hit`

* Description: Number of hits when accessing the data block from the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_data_miss`

* Description: Number of misses when accessing the data block from the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_filter_add`

* Description: Number of bloom filter blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_filter_bytes_evict`

* Description: Bytes of bloom filter blocks evicted from the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_filter_bytes_insert`

* Description: Bytes of bloom filter blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_filter_hit`

* Description: Number of hits when accessing the filter block from the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_filter_miss`

* Description: Number of misses when accessing the filter block from the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_hit`

* Description: Total number of hits for the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_index_add`

* Description: Number of index blocks added to Block Cache index.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_index_bytes_evict`

* Description: Bytes of index blocks evicted from the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_index_bytes_insert`

* Description: Bytes of index blocks added to the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_block_cache_index_hit`

* Description: Number of hits for the Block Cache index.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_index_miss`

* Description: Number of misses for the Block Cache index.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cache_miss`

* Description: Total number of misses for the Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cachecompressed_hit`

* Description: Number of hits for the compressed Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_block_cachecompressed_miss`

* Description: Number of misses for the compressed Block Cache.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_bloom_filter_full_positive`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.18), [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.10)

#### `Rocksdb_bloom_filter_full_true_positive`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.18), [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.10)

#### `Rocksdb_bloom_filter_prefix_checked`

* Description: Number of times the Bloom Filter checked before creating an iterator on a file.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_bloom_filter_prefix_useful`

* Description: Number of times the Bloom Filter check used to avoid creating an iterator on a file.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_bloom_filter_useful`

* Description: Number of times the Bloom Filter used instead of reading form file.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_bytes_read`

* Description: Total number of uncompressed bytes read from memtables, cache or table files.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_bytes_written`

* Description: Total number of uncompressed bytes written.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_compact_read_bytes`

* Description: Number of bytes read during compaction.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_compact_write_bytes`

* Description: Number of bytes written during compaction.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_compaction_key_drop_new`

* Description: Number of keys dropped during compaction due their being overwritten by new values.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_compaction_key_drop_obsolete`

* Description: Number of keys dropped during compaction due to their being obsolete.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_compaction_key_drop_user`

* Description: Number of keys dropped during compaction due to user compaction.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_covered_secondary_key_lookups`

* Description: Incremented when avoiding reading a record via a keyread. This indicates lookups that were performed via a secondary index containing a field that is only a prefix of the [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) column, and that could return all requested fields directly from the secondary index.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_flush_write_bytes`

* Description: Number of bytes written during flush.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_get_hit_l0`

* Description: Number of times reads got data from the L0 compaction layer.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_get_hit_l1`

* Description: Number of times reads got data from the L1 compaction layer.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_get_hit_l2_and_up`

* Description: Number of times reads got data from the L2 and up compaction layer.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_getupdatessince_calls`

* Description: Number of calls to the `GetUpdatesSince` function. You may find this useful when monitoring refreshes of the transaction log.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_iter_bytes_read`

* Description: Total uncompressed bytes read from an iterator, including the size of both key and value.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_l0_num_files_stall_micros`

* Description: Shows how long in microseconds throttled due to too mnay files in L0.
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.1), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.8)

#### `Rocksdb_l0_slowdown_micros`

* Description: Total time spent waiting in microseconds while performing L0-L1 compactions.
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.1), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.8)

#### `Rocksdb_manual_compactions_processed`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.18), [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.10)

#### `Rocksdb_manual_compactions_running`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.18), [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.10)

#### `Rocksdb_memtable_compaction_micros`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.1), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.8)

#### `Rocksdb_memtable_hit`

* Description: Number of memtable hits.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_memtable_miss`

* Description: Number of memtable misses.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_memtable_total`

* Description: Memory used, in bytes, of all memtables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_memtable_unflushed`

* Description: Memory used, in bytes, of all unflushed memtables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_no_file_closes`

* Description: Number of times files were closed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_no_file_errors`

* Description: Number of errors encountered while trying to read data from an SST file.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_no_file_opens`

* Description: Number of times files were opened.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_num_iterators`

* Description: Number of iterators currently open.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_block_not_compressed`

* Description: Number of uncompressed blocks.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_db_next`

* Description: Number of `next` calls.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_number_db_next_found`

* Description: Number of `next` calls that returned data.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_number_db_prev`

* Description: Number of `prev` calls.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_number_db_prev_found`

* Description: Number of `prev` calls that returned data.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_number_db_seek`

* Description: Number of `seek` calls.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_number_db_seek_found`

* Description: Number of `seek` calls that returned data.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_number_deletes_filtered`

* Description: Number of deleted records were not written to storage due to a nonexistent key.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_keys_read`

* Description: Number of keys have been read.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_keys_updated`

* Description: Number of keys have been updated.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_keys_written`

* Description: Number of keys have been written.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_merge_failures`

* Description: Number of failures encountered while performing merge operator actions.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_multiget_bytes_read`

* Description: Number of bytes read during RocksDB `MultiGet()` calls.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_multiget_get`

* Description: Number of RocksDB `MultiGet()` requests made.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_multiget_keys_read`

* Description: Number of keys read through RocksDB `MultiGet()` calls.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_reseeks_iteration`

* Description: Number of reseeks that have occurred inside an iteration that skipped over a large number of keys with the same user key.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_sst_entry_delete`

* Description: Number of delete markers written.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_sst_entry_merge`

* Description: Number of merge keys written.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_sst_entry_other`

* Description: Number of keys written that are not delete, merge or put keys.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_sst_entry_put`

* Description: Number of put keys written.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_sst_entry_singledelete`

* Description: Number of single-delete keys written.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_superversion_acquires`

* Description: Number of times the superversion structure acquired. This is useful when tracking files for the database.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_superversion_cleanups`

* Description: Number of times the superversion structure performed cleanups.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_number_superversion_releases`

* Description: Number of times the superversion structure released.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_queries_point`

* Description: Number of single-row queries.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_queries_range`

* Description: Number of multi-row queries.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_row_lock_deadlocks`

* Description: Number of deadlocks.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_row_lock_wait_timeouts`

* Description: Number of row lock wait timeouts.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_rows_deleted`

* Description: Number of rows deleted.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_rows_deleted_blind`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_rows_expired`

* Description: Number of expired rows.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_rows_filtered`

* Description: Number of TTL filtered rows.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.15), [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.7)

#### `Rocksdb_rows_inserted`

* Description: Number of rows inserted.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_rows_read`

* Description: Number of rows read.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_rows_updated`

* Description: Number of rows updated.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_snapshot_conflict_errors`

* Description: Number of snapshot conflict errors that have occurred during transactions that forced a rollback.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_l0_file_count_limit_slowdowns`

* Description: Write slowdowns due to L0 being near to full.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_l0_file_count_limit_stops`

* Description: Write stops due to L0 being to full.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_locked_l0_file_count_limit_slowdowns`

* Description: Write slowdowns due to L0 being near to full and L0 compaction in progress.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_locked_l0_file_count_limit_stops`

* Description: Write stops due to L0 being full and L0 compaction in progress.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_memtable_limit_slowdowns`

* Description: Write slowdowns due to approaching maximum permitted number of memtables.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.10), [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3)

#### `Rocksdb_stall_memtable_limit_stops`

* Description: \* Description: Write stops due to reaching maximum permitted number of memtables.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.10), [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3)

#### `Rocksdb_stall_micros`

* Description: Time in microseconds that the writer had to wait for the compaction or flush to complete.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_pending_compaction_limit_slowdowns`

* Description: Write slowdowns due to nearing the limit for the maximum number of pending compaction bytes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_pending_compaction_limit_stops`

* Description: Write stops due to reaching the limit for the maximum number of pending compaction bytes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_total_slowdowns`

* Description: Total number of write slowdowns.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_stall_total_stops`

* Description: Total number of write stops.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_system_rows_deleted`

* Description: Number of rows deleted from system tables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_system_rows_inserted`

* Description: Number of rows inserted into system tables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_system_rows_read`

* Description: Number of rows read from system tables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_system_rows_updated`

* Description: Number of rows updated for system tables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_wal_bytes`

* Description: Number of bytes written to WAL.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_wal_group_syncs`

* Description: Number of group commit WAL file syncs have occurred. This is provided by MyRocks and is not a view of a RocksDB counter. Increased in `rocksdb_flush_wal()` when doing the `rdb->FlushWAL()` call.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_wal_synced`

* Description: Number of syncs made on RocksDB WAL file.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_write_other`

* Description: Number of writes processed by a thread other than the requesting thread.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_write_self`

* Description: Number of writes processed by requesting thread.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_write_timedout`

* Description: Number of writes that timed out.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rocksdb_write_wal`

* Description: Number of write calls that requested WAL.
* Scope: Global, Session
* Data Type: `numeric`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
