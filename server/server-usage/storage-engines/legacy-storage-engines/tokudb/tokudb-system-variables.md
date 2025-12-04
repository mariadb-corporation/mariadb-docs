# TokuDB System Variables

{% include "../../../../.gitbook/includes/tokudb-has-been-deprecated-....md" %}

This page lists system variables that are related to [TokuDB](./).

See [Server System Variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them, and [Full list of MariaDB options, system and status variables](../../../../reference/full-list-of-mariadb-options-system-and-status-variables.md) for a complete list of all options, statis variable and system variables in MariaDB.

## System Variables

#### `tokudb_alter_print_error`

* Description: Print errors for alter table operations.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `OFF`

#### `tokudb_analyze_time`

* Description: Time in seconds that [ANALYZE](../../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement.md) operations spend on each index when calculating cardinality. Accurate cardinality helps in particular with the performance of complex queries. If no analyzes are run, cardinality are 1 for primary indexes, and unknown (NULL) for other types of indexes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `5`
* Range: `0` to `4294967295`

#### `tokudb_block_size`

* Description: Uncompressed size of internal fractal tree and leaf nodes. Changing will only affect tables created after the new setting is in effect. Existing tables will keep the setting they were created with unless the table is dumped and reloaded.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `4194304` (4MB)
* Range: `0` to `18446744073709551615`

#### `tokudb_bulk_fetch`

* Description: If set to `1` (the default), the bulk fetch algorithm is used for SELECT's and DELETE's, including related statements such as INSERT INTO.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_cache_size`

* Description: Size in bytes of the TokuDB cache. This variable is read-only and cannot be changed dynamically. To change the value, either set the value in the `my.cnf` file prior to loading TokuDB or\
  restart MariaDB after modifying the configuration. If you have loaded the\
  plugin but not used TokuDB yet, you can unload the plugin then reload it and\
  MariaDB will reload the plugin with the setting from the configuration file. Setting to at least half of the available memory is recommended, although if using directIO instead of buffered IO (see [tokudb\_directio](tokudb-system-variables.md#tokudb_directio)) , up to 80% of the available memory is recommended. Decrease if other applications require significant memory or swapping is degrading performance.
* Dynamic: No
* Data Type: numeric
* Default Value: Half of the total system memory

#### `tokudb_check_jemalloc`

* Description: Check if jemalloc is linked.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `1`
* Valid Values: `0` and `1`

#### `tokudb_checkpoint_lock`

* Description: Mechanism to lock out TokuDB checkpoints. When set to `1`, TokuDB checkpoints are locked out. Setting to `0`, or disconnecting the client, releases the lock.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `OFF`

#### `tokudb_checkpoint_on_flush_logs`

* Description: TokuDB checkpoint on flush logs.
* Scope: Global
* Dynamic: Yes
* Data Type: boolean
* Default Value: `OFF`

#### `tokudb_checkpointing_period`

* Description: Time in seconds between the beginning of each checkpoint. It is recommended to leave this at the default setting of 1 minute.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `60`
* Range: `0` to `4294967295`

#### `tokudb_cleaner_iterations`

* Description: Number of internal nodes processed in each cleaner thread period (see [tokudb\_cleaner\_period](tokudb-system-variables.md#tokudb_cleaner_period)). Setting to `0` turns off cleaner threads.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `5`
* Range: `0` to `18446744073709551615`

#### `tokudb_cleaner_period`

* Description: Frequency in seconds for the running of the cleaner thread. Setting to `0` turns off cleaner threads.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `1`
* Range: `0` to `18446744073709551615`

#### `tokudb_commit_sync`

* Description: Whether or not the transaction log is flushed upon transaction commit. Flushing has a minor performance penalty, but switching it off means that committed transactions may not survive a server crash.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_create_index_online`

* Description: Whether indexes are hot or not. Hot, or online, indexes (the default) mean that the table is available for inserting and updates while the index is being created. It is slower to create hot indexes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_data_dir`

* Description: Directory where the TokuDB data is stored. By default the variable is empty, in which case the regular [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) is used.
* Dynamic: No
* Data Type: string
* Default Value: Empty (the MariaDB datadir is used)

#### `tokudb_debug`

* Description: Setting to a non-zero value turns on various TokuDB debug traces.
* Scope: Global
* Dynamic: Yes
* Data Type: numeric
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `tokudb_directio`

* Description: When set to ON, TokuDB writes use Direct IO instead of Buffered IO. [tokudb\_cache\_size](tokudb-system-variables.md#tokudb_cache_size) should be adjusted when using DirectIO.
* Dynamic: No
* Data Type: boolean
* Default Value: `OFF`

#### `tokudb_disable_hot_alter`

* Description: If set to `ON` (`OFF` is default), hot alter table is disabled.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `OFF`

#### `tokudb_disable_prefetching`

* Description: If prefetching is not disabled (the default), range queries usually benefit from aggressive prefetching of blocks of rows. For range queries with LIMIT clauses, this can create unnecessary IO, and so prefetching can be disabled if these make up a majority of range queries.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `OFF`

#### `tokudb_disable_slow_alter`

* Description: Usually, TokuDB permits column addition, deletion, expansion, and renaming with minimal locking, very quickly. This variable determines whether certain slow \[alter|ALTER]] table statements that cannot take advantage of this feature are permitted. Statements that are slow are those that include a mix of column additions, deletions or expansions, for example, `ALTER TABLE t1 ADD COLUMN c1 int, DROP COLUMN c2`.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `OFF`

#### `tokudb_empty_scan`

* Description: TokuDB algorithm to check if the table is empty when opened. Setting to `disabled` will reduce this overhead.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: enum
* Default Value: `rl`
* Valid Values: `lr`, `rl`, `disabled`

#### `tokudb_fs_reserve_percent`

* Description: If this percentage of the filesystem is not free, inserts are prohibited. Recommended value is half the size of the available memory. Once disabled, inserts are re-enabled once twice the reserve is available. TokuDB will freeze entirely if the disk becomes entirely full.
* Scope: Global
* Dynamic: No
* Data Type: numeric
* Default Value: `5`

#### `tokudb_fsync_log_period`

* Description: fsync() operations frequency in milliseconds. If set to `0`, the default, [tokudb\_commit\_sync](tokudb-system-variables.md#tokudb_commit_sync) control fsync() behavior.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `0`
* Range: `0` to `18446744073709551615`

**Warning**: currently values in the 1000-2000 range seem to cause server crashes, see [MDEV-16732](https://jira.mariadb.org/browse/MDEV-16732)

#### `tokudb_hide_default_row_format`

* Description: Hide the default row format.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_killed_time`

* Description: Control lock tree kill callback frequency.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `4000`
* Range: `0` to `18446744073709551615`
* Introduced: TokuDB 7.1.5

#### `tokudb_last_lock_timeout`

* Description: Empty by default, when a lock deadlock is detected, or a lock request times out, set to a JSON document describing the most recent lock conflict. Only set when the first bit of [tokudb\_lock\_timeout\_debug](tokudb-system-variables.md#tokudb_lock_timeout_debug) is set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: text
* Default Value: Empty

#### `tokudb_load_save_space`

* Description: If set to `1`, the default, bulk loader intermediate data is compressed, otherwise it is uncompressed. Also see [tokudb\_tmp\_dir](tokudb-system-variables.md#tokudb_tmp_dir).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_loader_memory_size`

* Description: Memory limit for each loader instance used by the TokuDB bulk loader. Memory is taken from the TokuDB cache ([tokudb\_cache\_size](tokudb-system-variables.md#tokudb_cache_size)), so current cache data may need to be cleared for the loader to begin. Increase if tables are very larger, with multiple secondary indexes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `100000000` (100M)
* Range: `0` to `18446744073709551615`

#### `tokudb_lock_timeout`

* Description: Time in milliseconds that a transaction will wait for a lock held by another transaction to be released before timing out with a `lock wait timeout` error (-30994). Setting to `0` disables lock waits.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `4000` (4 seconds)
* Range: `0` to `18446744073709551615`

#### `tokudb_lock_timeout_debug`

* Description: When bit zero is set (default `1`), a JSON document describing the most recent lock conflict is reported to [tokudb\_last\_lock\_timeout](tokudb-system-variables.md#tokudb_last_lock_timeout). When set to `0`, no lock conflicts are reported. When bit one is set, the JSON document is printed to the [error log](../../../../server-management/server-monitoring-logs/error-log.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `1`

#### `tokudb_log_dir`

* Description: Directory where the TokuDB log files are stored. By default the variable is empty, in which case the regular [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) is used.
* Dynamic: No
* Data Type: string
* Default Value: Empty (the MariaDB datadir is used)

#### `tokudb_max_lock_memory`

* Description: Max memory for locks.
* Scope: Global, Session
* Dynamic: No
* Data Type: numeric
* Default Value: `130653952`

#### `tokudb_optimize_index_fraction`

* Description: When deleting a percentage of the tree (useful when the left side of the tree has many deletions, such as a pattern with increasing ids or dates), it's possible to optimize a subset of the fractal tree, as determined by the value of this variable, which ranges from `0.0` to `1.0` (indicating the whole tree).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `1.000000`
* Range: `0.0` to `1.0`
* Introduced: TokuDB 7.5.5

#### `tokudb_optimize_index_name`

* Description: If set to an index name, will optimize that single index in a table. Empty by default.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: string
* Default Value: None
* Introduced: TokuDB 7.5.5

#### `tokudb_optimize_throttle`

* Description: Table optimization utilizes all available resources by default. This variable allows the table optimization speed to be limited in order to reduce the overall resources used. The limit places an upper bound on the number of fractal tree leaf nodes that are optimized per second. `0`, the default, imposes no limit.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `0`
* Range: `0` to `18446744073709551615`
* Introduced: TokuDB 7.5.5

#### `tokudb_pk_insert_mode`

* Description: Mode for primary key inserts using either REPLACE INTO or [INSERT IGNORE](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-ignore.md) on tables with no secondary index, or where all columns in the secondary index are in the primary key. For example `PRIMARY KEY (a,b,c), key (b,c)`
  * `0`: Fast inserts. [Triggers](../../../triggers-events/triggers/) may not work, and [row-based replication](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) will not work
  * `1`: Fast inserts if no triggers are defined, otherwise inserts may be slow. Row-based replication will not work.
  * `2`: Slow inserts. Triggers and row-based replication work normally.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: enumerated
* Default Value: `1`
* Valid Values: `0`, `1`, `2`

#### `tokudb_prelock_empty`

* Description: If set to `0` (`1` is default), fast bulk loading are switched off. Usually, TokuDB obtains a table lock on empty tables. If, as is usual, only one transaction is loading the table, this speeds up the inserts. However, if many transactions are loading, only one can have access at a time, so setting this to `0`, avoiding the lock, will speed inserts up in that situation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_read_block_size`

* Description: Uncompressed size in bytes of the read blocks of the fractal tree leaves. Changing will only affect tables created after the new setting is in effect. Existing tables will keep the setting they were created with unless the table is dumped and reloaded. Larger values are better for large range scans and higher compressions, while smaller values are better for point and small range scans.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `65536` (64KB)
* Range: `4096` to `4294967295`

#### `tokudb_read_buf_size`

* Description: Per-client size in bytes of the buffer used for storing bulk fetched values as part of a large range query. Reduce if there are many simultaneous clients. Setting to `0` disables bulk fetching.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `131072` (128KB)
* Range: `0` to `1048576`

#### `tokudb_read_status_frequency`

* Description: Progress is measured every this many reads for display by [SHOW PROCESSLIST](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/sql-statements/administrative-sql-statements/show/show-processlist.md). Useful to set to `1` to examine slow queries.
* Scope: Global,
* Dynamic: Yes
* Data Type: numeric
* Default Value: `10000`
* Range: `0` to `4294967295`

#### `tokudb_row_format`

* Description: Compression algorithm used by default to compress data. Can be overridden by a row format specified in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement. note that the library can be specified directly, or an alias used, the mapping of which may change in future. Note that in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), and before [MariaDB 10.0.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes), the compression type did not default to this value. See [TokuDB Differences](tokudb-differences.md).
  * `tokudb_default`, `tokudb_zlib`: Use the zlib library,
  * `tokudb_fast`, `tokudb_quicklz`: Use the quicklz library, the lightest compression with low CPU usage,
  * `tokudb_small`, `tokudb_lzma`: Use the lzma library. the highest compression and highest CPU usage
  * `tokudb_uncompressed`: No compression is used.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: enumerated
* Default Value: `tokudb_zlib`
* Valid Values: `tokudb_default`, `tokudb_fast`, `tokudb_small`, `tokudb_zlib`, `tokudb_quicklz`, `tokudb_lzma`, `tokudb_uncompressed`

#### `tokudb_rpl_check_readonly`

* Description: By default, when the slave is in read only mode, row events are run from the binary log using TokuDB's read-free replication (RFR). Setting this variable to `OFF` turns off the slave read only check, allowing RFR to run when the slave is not read-only. Be careful that you understand the consequences if setting this variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_rpl_lookup_rows`

* Description: If set to `OFF` (`ON` is default), and [binlog\_format](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) to `ROW` and [read\_only](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) to `ON`, TokuDB replication slaves will not perform row lookups for update or delete row log events, removing the need for the associated IO.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_rpl_lookup_rows_delay`

* Description: Can be used to simulate long disk reads by sleeping for the specified time, in microseconds, before the row lookup query. Only useful to change in a test environment.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `0`

#### `tokudb_rpl_unique_checks`

* Description: If set to `OFF` (`ON` is default), and [binlog\_format](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) to `ROW` and [read\_only](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) to `ON`, TokuDB replication slaves will skip uniqueness checks on inserts and updates, removing the associated IO.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_rpl_unique_checks_delay`

* Description: Can be used to simulate long disk reads by sleeping for the specified time, in microseconds, before the row lookup query. Only useful to change in a test environment.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `0`

#### `tokudb_support_xa`

* Description: Whether or not the prepare phase of an XA transaction performs an fsync().
* Scope: Global, Session
* Dynamic: Yes
* Data Type: boolean
* Default Value: `ON`

#### `tokudb_tmp_dir`

* Description: Directory where the TokuDB bulk loaders temporary files are stored. Can be very large, and useful to place on a separate disk. By default the variable is empty, in which case the regular [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) is used. [tokudb\_load\_save\_space](tokudb-system-variables.md#tokudb_load_save_space) determines whether the data is compressed or not. The error message `ERROR 1030 (HY000): Got error 1 from storage engine` could indicate that the disk has run out of space.
* Dynamic: No
* Data Type: `directory name`
* Default Value: Empty (the MariaDB datadir is used)

#### `tokudb_version`

* Description: The TokuDB version of the plugin included on MariaDB.
* Dynamic: No
* Data Type: `string`

#### `tokudb_write_status_frequency`

* Description: Progress is measured every this many writes for display by [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md). Useful to set to `1` to examine slow queries.
* Scope: Global,
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000`
* Range: `0` to `4294967295`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
