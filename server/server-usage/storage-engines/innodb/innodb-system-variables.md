# InnoDB System Variables

This page documents system variables related to the [InnoDB storage engine](./). For options that are not system variables, see [InnoDB Options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md).

See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.

Also see the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `have_innodb`

* Description: If the server supports [InnoDB tables](./), will be set to `YES`, otherwise will be set to `NO`. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), use the [Information Schema PLUGINS](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md) table or [SHOW ENGINES](../../../reference/sql-statements/administrative-sql-statements/show/show-engines.md) instead.
* Scope: Global
* Dynamic: No
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `ignore_builtin_innodb`

* Description: Setting this to `1` results in the built-in InnoDB storage engine being ignored. In some versions of MariaDB, XtraDB is the default and is always present, so this variable is ignored and setting it results in a warning. From [MariaDB 10.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes) to [MariaDB 10.0.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1008-release-notes), when InnoDB was the default instead of XtraDB, this variable needed to be set. Usually used in conjunction with the [plugin-load=innodb=ha\_innodb](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option to use the InnoDB plugin.
* Commandline: `--ignore-builtin-innodb`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_adaptive_checkpoint`

* Description: Replaced with [innodb\_adaptive\_flushing\_method](innodb-system-variables.md#innodb_adaptive_flushing_method). Controls adaptive checkpointing. InnoDB's fuzzy checkpointing can cause stalls, as many dirty blocks are flushed at once as the checkpoint age nears the maximum. Adaptive checkpointing aims for more consistent flushing, approximately `modified age / maximum checkpoint age`. Can result in larger transaction log files
  * `reflex` Similar to [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) flushing but flushes blocks constantly and contiguously based on the oldest modified age. If the age exceeds 1/2 of the maximum age capacity, flushing will be weak contiguous. If the age exceeds 3/4, flushing will be strong. Strength can be adjusted by the variable [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity).
  * `estimate` The default, and independent of [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity). If the oldest modified age exceeds 1/2 of the maximum age capacity, blocks will be flushed every second at a rate determined by the number of modified blocks, LSN progress speed and the average age of all modified blocks.
  * `keep_average` Attempts to keep the I/O rate constant by using a shorter loop cycle of one tenth of a second. Designed for SSD cards.
* Commandline: `--innodb-adaptive-checkpoint=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `estimate`
* Valid Values: `none` or `0`, `reflex` or `1`, `estimate` or `2`, `keep_average` or `3`
* Removed: XtraDB 5.5 - replaced with [innodb\_adaptive\_flushing\_method](innodb-system-variables.md#innodb_adaptive_flushing_method)

#### `innodb_adaptive_flushing`

* Description: If set to `1`, the default, the server will dynamically adjust the flush rate of dirty pages in the [InnoDB buffer pool](innodb-buffer-pool.md). This assists to reduce brief bursts of I/O activity. If set to `0`, adaptive flushing will only take place when the limit specified by [innodb\_adaptive\_flushing\_lwm](innodb-system-variables.md#innodb_adaptive_flushing_lwm) is reached.
* Commandline: `--innodb-adaptive-flushing={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_adaptive_flushing_lwm`

* Description: Adaptive flushing is enabled when this low water mark percentage of the [InnoDB redo log](innodb-redo-log.md) capacity is reached. Takes effect even if [innodb\_adaptive\_flushing](innodb-system-variables.md#innodb_adaptive_flushing) is disabled.
* Commandline: `--innodb-adaptive-flushing-lwm=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `double`
* Default Value: `10.000000`
* Range: `0` to `70`

#### `innodb_adaptive_flushing_method`

* Description: Determines the method of flushing dirty blocks from the InnoDB [buffer pool](innodb-buffer-pool.md). If set to `native` or `0`, the original InnoDB method is used. The maximum checkpoint age is determined by the total length of all transaction log files. When the checkpoint age reaches the maximum checkpoint age, blocks are flushed. This can cause lag if there are many updates per second and many blocks with an almost identical age need to be flushed. If set to `estimate` or `1`, the default, the oldest modified age will be compared with the maximum age capacity. If it's more than 1/4 of this age, blocks are flushed every second. The number of blocks flushed is determined by the number of modified blocks, the LSN progress speed and the average age of all modified blocks. It's therefore independent of the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) for the 1-second loop, but not entirely so for the 10-second loop. If set to `keep_average` or `2`, designed specifically for SSD cards, a shorter loop cycle is used in an attempt to keep the I/O rate constant. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 and replaced with InnoDB flushing method from MySQL 5.6.
* Commandline: `innodb-adaptive-flushing-method=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `estimate`
* Valid Values: `native` or `0`, `estimate` or `1`, `keep_average` or `2`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - replaced with InnoDB flushing method from MySQL 5.6

#### `innodb_adaptive_hash_index`

* Description: If set to `1`, the default until [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the [InnoDB](./) hash index is enabled. Based on performance testing ([MDEV-17492](https://jira.mariadb.org/browse/MDEV-17492)), the InnoDB adaptive hash index helps performance in mostly read-only workloads, and could slow down performance in other environments, especially [DROP TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md), [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md), [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md), or [DROP INDEX](../../../reference/sql-statements/data-definition/drop/drop-index.md) operations.
* Commandline: `--innodb-adaptive-hash-index={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF` (>= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)), `ON` (<= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104))

#### `innodb_adaptive_hash_index_partitions`

* Description: Specifies the number of partitions for use in adaptive searching. If set to `1`, no extra partitions are created. XtraDB-only. From [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB), this is an alias for [innodb\_adaptive\_hash\_index\_parts](innodb-system-variables.md#innodb_adaptive_hash_index_parts) to allow for easier upgrades.
* Commandline: `innodb-adaptive-hash-index-partitions=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `64`

#### `innodb_adaptive_hash_index_parts`

* Description: Specifies the number of partitions for use in adaptive searching. If set to `1`, no extra partitions are created.
* Commandline: `innodb-adaptive-hash-index-parts=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `512`

#### `innodb_adaptive_max_sleep_delay`

* Description: Maximum time in microseconds to automatically adjust the [innodb\_thread\_sleep\_delay](innodb-system-variables.md#innodb_thread_sleep_delay) value to, based on the workload. Useful in extremely busy systems with hundreds of thousands of simultaneous connections. `0` disables any limit. Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes).
* Commandline: `--innodb-adaptive-max-sleep-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `0` (>= [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes))
  * `150000` (<= [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes))
* Range: `0` to `1000000`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Deprecated: [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_additional_mem_pool_size`

* Description: Size in bytes of the [InnoDB](./) memory pool used for storing information about internal data structures. Defaults to 8MB, if your application has many tables and a large structure, and this is exceeded, operating system memory will be allocated and warning messages written to the error log, in which case you should increase this value. Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) and removed in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) along with InnoDB's internal memory allocator.
* Commandline: `--innodb-additional-mem-pool-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8388608`
* Range: `2097152` to `4294967295`
* Deprecated: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes)

#### `innodb_alter_copy_bulk`

* Description: Allow bulk insert operation for copy alter operation.
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-9-release-notes), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-3-release-notes), [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes), [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes)

#### `innodb_api_bk_commit_interval`

* Description: Time in seconds between auto-commits for idle connections using the InnoDB memcached interface (not implemented in MariaDB).
* Commandline: `--innodb-api-bk-commit-interval=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `5`
* Range: `1` to `1073741824`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)

#### `innodb_api_disable_rowlock`

* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `--innodb-api-disable-rowlock={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)

#### `innodb_api_enable_binlog`

* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `--innodb-api-enable-binlog={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)

#### `innodb_api_enable_mdl`

* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `--innodb-api-enable-mdl={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)

#### `innodb_api_trx_level`

* Description: For use with MySQL's memcached (not implemented in MariaDB)
* Commandline: `--innodb-api-trx-level=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)

#### `innodb_auto_lru_dump`

* Description: Renamed [innodb\_buffer\_pool\_restore\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_restore_at_startup) since XtraDB 5.5.10-20.1, which was in turn replaced by [innodb\_buffer\_pool\_load\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).
* Commandline: `--innodb-auto-lru-dump=#`
* Removed: XtraDB 5.5.10-20.1

#### `innodb_autoextend_increment`

* Description: Size in MB to increment an auto-extending shared tablespace file when it becomes full. If [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) was set to `1`, this setting does not apply to the resulting per-table tablespace files, which are automatically extended in their own way.
* Commandline: `--innodb-autoextend-increment=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `64` (from [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)) `8` (before [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)),
* Range: `1` to `1000`

#### `innodb_autoinc_lock_mode`

* Description: The lock mode that is used when generating [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) values for InnoDB tables.
  * Valid values are:
    * `0` is the traditional lock mode.
    * `1` is the consecutive lock mode.
    * `2` is the interleaved lock mode.
  * In order to use [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/), the lock mode needs to be set to `2`.
  * See [AUTO\_INCREMENT Handling in InnoDB: AUTO\_INCREMENT Lock Modes](auto_increment-handling-in-innodb.md) for more information.
* Commandline: `--innodb-autoinc-lock-mode=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `2`

#### `innodb_background_scrub_data_check_interval`

* Description: Check if spaces needs scrubbing every [innodb\_background\_scrub\_data\_check\_interval](innodb-system-variables.md#innodb_background_scrub_data_check_interval) seconds. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).
* Commandline: `--innodb-background-scrub-data-check-interval=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `3600`
* Range: `1` to `4294967295`
* Deprecated: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_background_scrub_data_compressed`

* Description: Enable scrubbing of compressed data by background threads (same as encryption\_threads). See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).
* Commandline: `--innodb-background-scrub-data-compressed={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Deprecated: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_background_scrub_data_interval`

* Description: Scrub spaces that were last scrubbed longer than this number of seconds ago. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).
* Commandline: `--innodb-background-scrub-data-interval=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `604800`
* Range: `1` to `4294967295`
* Deprecated: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_background_scrub_data_uncompressed`

* Description: Enable scrubbing of uncompressed data by background threads (same as encryption\_threads). See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).
* Commandline: `--innodb-background-scrub-data-uncompressed={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Deprecated: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_blocking_buffer_pool_restore`

* Description: If set to `1` (`0` is default), XtraDB will wait until the least-recently used (LRU) dump is completely restored upon restart before reporting back to the server that it has successfully started up. Available with XtraDB only, not InnoDB.
* Commandline: `innodb-blocking-buffer-pool-restore={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes)

#### `innodb_buf_dump_status_frequency`

* Description: Determines how often (as a percent) the buffer pool dump status should be printed in the logs. For example, `10` means that the buffer pool dump status is printed when every 10% of the number of buffer pool pages are dumped. The default is `0` (only start and end status is printed).
* Commandline: `--innodb-buf-dump-status-frequency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `100`

#### `innodb_buffer_pool_chunk_size`

* Description: Chunk size used for dynamically resizing the [buffer pool](innodb-buffer-pool.md). Note that changing this setting can change the size of the buffer pool. When [large-pages](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_pages) is used this value is effectively rounded up to the next multiple of [large-page-size](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_page_size). See [Setting Innodb Buffer Pool Size Dynamically](../../../ha-and-performance/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md). From [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes), the variable is autosized based on the [buffer pool size](innodb-buffer-pool.md).
* Commandline: `--innodb-buffer-pool-chunk-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:
  * `autosize (0)`, resulting in [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size)/64, if [large\_pages](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_pages) round down to multiple of largest page size, with 1MiB minimum (>= [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1081-release-notes))
  * `134217728` (<= [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes))
* Range:
  * `0`, as autosize, and then `1048576` to `18446744073709551615` (>= [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108))
  * `1048576` to [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size)/[innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances) (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107))
* Block size: `1048576`

#### `innodb_buffer_pool_dump_at_shutdown`

* Description: Whether to record pages cached in the [buffer pool](innodb-buffer-pool.md) on server shutdown, which reduces the length of the warmup the next time the server starts. The related [innodb\_buffer\_pool\_load\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) specifies whether the buffer pool is automatically warmed up at startup.
* Commandline: `--innodb-buffer-pool-dump-at-shutdown={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_buffer_pool_dump_now`

* Description: Immediately records pages stored in the [buffer pool](innodb-buffer-pool.md). The related [innodb\_buffer\_pool\_load\_now](innodb-system-variables.md#innodb_buffer_pool_load_now) does the reverse, and will immediately warm up the buffer pool.
* Commandline: `--innodb-buffer-pool-dump-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_buffer_pool_dump_pct`

* Description: Dump only the hottest N% of each [buffer pool](innodb-buffer-pool.md).
* Commandline: `--innodb-buffer-pool-dump-pct={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value:
  * `25`
* Range: `1` to `100`

#### `innodb_buffer_pool_evict`

* Description: Evict pages from the buffer pool. If set to "uncompressed" then all uncompressed pages are evicted from the buffer pool. Variable to be used only for testing. Only exists in DEBUG builds.
* Commandline: `--innodb-buffer-pool-evict=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `""`
* Valid Values: "" or "uncompressed"

#### `innodb_buffer_pool_filename`

* Description: The file that holds the [buffer pool](innodb-buffer-pool.md) list of page numbers set by [innodb\_buffer\_pool\_dump\_at\_shutdown](innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown) and [innodb\_buffer\_pool\_dump\_now](innodb-system-variables.md#innodb_buffer_pool_dump_now).
* Commandline: `--innodb-buffer-pool-filename=file`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `ib_buffer_pool`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_buffer_pool_instances`

* Description: If [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size) is set to more than 1GB, innodb\_buffer\_pool\_instances divides the [InnoDB](./) buffer pool into the specified number of instances. The default was 1 in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), but for large systems with buffer pools of many gigabytes, many instances could help reduce contention concurrency through [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102). The default is 8 in MariaDB 10 (except on Windows 32-bit, where it varies according to [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size), or from [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes), where it is set to 1 if [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size) < 1GB). Each instance manages its own data structures and takes an equal portion of the total buffer pool size, so for example if innodb\_buffer\_pool\_size is 4GB and innodb\_buffer\_pool\_instances is set to 4, each instance will be 1GB. Each instance should ideally be at least 1GB in size.\
  Starting with [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), performance improvements intended to reduce the overhead of context-switching between buffer pools changed the recommended number of innodb\_buffer\_pool\_instances to one for every 128GB of buffer pool size. Based on these changes, the variable is deprecated and ignored from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes), where the buffer pool runs in a single instance regardless of size.
* Commandline: `--innodb-buffer-pool-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: >= [MariaDB 10.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes): `8`, `1` (>= [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes) if [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size) < 1GB), or dependent on [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size) (Windows 32-bit)
* Deprecated: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_buffer_pool_load_abort`

* Description: Aborts the process of restoring [buffer pool](innodb-buffer-pool.md) contents started by [innodb\_buffer\_pool\_load\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) or [innodb\_buffer\_pool\_load\_now](innodb-system-variables.md#innodb_buffer_pool_load_now).
* Commandline: `--innodb-buffer-pool-load-abort={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_buffer_pool_load_at_startup`

* Description: Specifies whether the [buffer pool](innodb-buffer-pool.md) is automatically warmed up when the server starts by loading the pages held earlier. The related [innodb\_buffer\_pool\_dump\_at\_shutdown](innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown) specifies whether pages are saved at shutdown. If the buffer pool is large and taking a long time to load, increasing [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) at startup may help.
* Commandline: `--innodb-buffer-pool-load-at-startup={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_buffer_pool_load_now`

* Description: Immediately warms up the [buffer pool](innodb-buffer-pool.md) by loading the stored data pages. The related [innodb\_buffer\_pool\_dump\_now](innodb-system-variables.md#innodb_buffer_pool_dump_now) does the reverse, and immediately records pages stored in the buffer pool.
* Commandline: `--innodb-buffer-pool-load-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_buffer_pool_load_pages_abort`

* Description: Number of pages during a buffer pool load to process before signaling [innodb\_buffer\_pool\_load\_abort=1](innodb-system-variables.md#innodb_buffer_pool_load_abort). Debug builds only.
* Commandline: `--innodb-buffer-pool-load-pages-abort=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `9223372036854775807`
* Range: `1` to `9223372036854775807`

#### `innodb_buffer_pool_populate`

* Description: When set to `1` (`0` is default), XtraDB will preallocate pages in the buffer pool on starting up so that NUMA allocation decisions are made while the buffer cache is still clean. XtraDB only. This option was made ineffective in [MariaDB 10.0.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes). Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-buffer-pool-populate={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.0.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10023-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_buffer_pool_restore_at_startup`

* Description: Time in seconds between automatic buffer pool dumps. If set to a non-zero value, XtraDB will also perform an automatic restore of the [buffer pool](innodb-buffer-pool.md) at startup. If set to `0`, automatic dumps are not performed, nor automatic restores on startup. Replaced by [innodb\_buffer\_pool\_load\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).
* Commandline: `innodb-buffer-pool-restore-at-startup`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range - 32 bit: `0` to `4294967295`
* Range - 64 bit: `0` to `18446744073709547520`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - replaced by [innodb\_buffer\_pool\_load\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup)

#### `innodb_buffer_pool_shm_checksum`

* Description: Used with Percona's SHM buffer pool patch in XtraDB 5.5. Was shortly deprecated and removed in XtraDB 5.6. XtraDB only.
* Commandline: `innodb-buffer-pool-shm-checksum={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_buffer_pool_shm_key`

* Description: Used with Percona's SHM buffer pool patch in XtraDB 5.5. Later deprecated in XtraDB 5.5, and removed in XtraDB 5.6.
* Commandline: `innodb-buffer-pool-shm-key={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_buffer_pool_size`

* Description: InnoDB buffer pool size in bytes. The primary value to adjust on a database server with entirely/primarily [InnoDB](./) tables, can be set up to 80% of the total memory in these environments. See the [InnoDB Buffer Pool](innodb-buffer-pool.md) for more on setting this variable, and also [Setting InnoDB Buffer Pool Size Dynamically](../../../ha-and-performance/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md) if doing so dynamically.
* Commandline: `--innodb-buffer-pool-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `134217728` (128MiB)
* Range:
  * Minimum: `5242880` (5MiB ) for [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) <= 16k otherwise `25165824` (24MiB) for [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) > 16k (for versions less than next line)
  * Minimium: `2MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 4k, `3MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 8k, `5MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 16k, `10MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 32k, `20MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 64k, (>= [MariaDB 10.2.42](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10242-release-notes), >= [MariaDB 10.3.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10333-release-notes), >= [MariaDB 10.4.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10423-release-notes), >= [MariaDB 10.5.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10514-release-notes), >= [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1066-release-notes), >= [MariaDB 10.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1072-release-notes))
  * Minimum: 1GiB for [innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances) > 1 (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107))
  * Maximium: `9223372036854775807` (8192PB) (all versions)
* Block size: `1048576`

#### `innodb_change_buffer_dump`

* Description: If set, causes the contents of the InnoDB change buffer to be dumped to the server error log at startup. Only available in debug builds.
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.2.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10228-release-notes), [MariaDB 10.3.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10319-release-notes), [MariaDB 10.4.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1049-release-notes)

#### `innodb_change_buffer_max_size`

* Description: Maximum size of the [InnoDB Change Buffer](innodb-change-buffering.md) as a percentage of the total buffer pool. The default is 25%, and this can be increased up to 50% for servers with high write activity, and lowered down to 0 for servers used exclusively for reporting.
* Commandline: `--innodb-change-buffer-max-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `25`
* Range: `0` to `50`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Deprecated: [MariaDB 10.9.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1090-release-notes)
* Removed: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes)

#### `innodb_change_buffering`

* Description: Sets how [InnoDB](./) change buffering is performed. See [InnoDB Change Buffering](innodb-change-buffering.md) for details on the settings. Deprecated and ignored from [MariaDB 10.9.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1090-release-notes).
* Commandline: `--innodb-change-buffering=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration` (>= [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes)), `string` (<= [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes))
* Default Value:
  * > \= [MariaDB 10.5.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10515-release-notes), [MariaDB 10.6.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1067-release-notes), [MariaDB 10.7.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1073-release-notes), [MariaDB 10.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1082-release-notes): `none`
  * <= [MariaDB 10.5.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10514-release-notes), [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1066-release-notes), [MariaDB 10.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1072-release-notes), [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1081-release-notes):`all`
* Valid Values: `inserts`, `none`, `deletes`, `purges`, `changes`, `all`
* Deprecated: [MariaDB 10.9.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1090-release-notes)
* Removed: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes)

#### `innodb_change_buffering_debug`

* Description: If set to `1`, an [InnoDB Change Buffering](innodb-change-buffering.md) debug flag is set. `1` forces all changes to the change buffer, while `2` causes a crash at merge. `0`, the default, indicates no flag is set. Only available in debug builds.
* Commandline: `--innodb-change-buffering-debug=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2`

#### `innodb_checkpoint_age_target`

* Description: The maximum value of the checkpoint age. If set to `0`, has no effect. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 and replaced with InnoDB flushing method from MySQL 5.6.
* Commandline: `innodb-checkpoint-age-target=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` upwards
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - replaced with InnoDB flushing method from MySQL 5.6.

#### `innodb_checksum_algorithm`

* Description: Specifies how the InnoDB tablespace checksum is generated and verified.
  * `innodb`: Backwards compatible with earlier versions (<= [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)). Deprecated in [MariaDB 10.3.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10329-release-notes), [MariaDB 10.4.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10419-release-notes), [MariaDB 10.5.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10510-release-notes) and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106). If really needed, data files can still be converted with [innochecksum](../../../clients-and-utilities/administrative-tools/innochecksum.md).
  * `crc32`: A newer, faster algorithm, but incompatible with earlier versions. Tablespace blocks will be converted to the new format over time, meaning that a mix of checksums may be present.
  * `full_crc32` and `strict_full_crc32`: From [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes). Permits encryption to be supported over a [SPATIAL INDEX](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/sql-structure/geometry/spatial-index.md), which `crc32` does not support. Newly-created data files will carry a flag that indicates that all pages of the file will use a full CRC-32C checksum over the entire page contents (excluding the bytes where the checksum is stored, at the very end of the page). Such files will always use that checksum, no matter what parameter `innodb_checksum_algorithm` is assigned to. Even if `innodb_checksum_algorithm` is modified later, the same checksum will continue to be used. A special flag will be set in the FSP\_SPACE\_FLAGS in the first data page to indicate the new format of checksum and encryption/page\_compressed. ROW\_FORMAT=COMPRESSED tables will only use the old format.\
    These tables do not support new features, such as larger innodb\_page\_size or instant ADD/DROP COLUMN. Also cleans up the MariaDB tablespace flags - flags are reserved to store the page\_compressed compression algorithm, and to store the compressed payload length, so that checksum can be computed over the compressed (and possibly encrypted) stream and can be validated without decrypting or decompressing the page. In the full\_crc32 format, there no longer are separate before-encryption and after-encryption checksums for pages. The single checksum is computed on the page contents that is written to the file.See [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026) for details.
  * `none`: Writes a constant rather than calculate a checksum. Deprecated in [MariaDB 10.3.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10329-release-notes), [MariaDB 10.4.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10419-release-notes), [MariaDB 10.5.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10510-release-notes) and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) as was mostly used to disable the original, slow, page checksum for benchmarking purposes.
  * `strict_crc32`, `strict_innodb` and `strict_none`: The options are the same as the regular options, but InnoDB will halt if it comes across a mix of checksum values. These are faster, as both new and old checksum values are not required, but can only be used when setting up tablespaces for the first time.
* Commandline: `--innodb-checksum-algorithm=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value:
  * `full_crc32` (>= [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes))
  * `crc32` (>= [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes) to <= [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/storage-engines/innodb/broken-reference/README.md))
  * `innodb` (<= [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes))
* Valid Values:
  * > \= [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes): `crc32`, `full_crc32`, `strict_crc32`, `strict_full_crc32`
  * [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), >= [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes): `innodb`, `crc32`, `full_crc32`, `none`, `strict_innodb`, `strict_crc32`, `strict_none`, `strict_full_crc32`
  * <= [MariaDB 10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1042-release-notes): `innodb`, `crc32`, `none`, `strict_innodb`, `strict_crc32`, `strict_none`

#### `innodb_checksums`

* Description: By default, [InnoDB](./) performs checksum validation on all pages read from disk, which provides extra fault tolerance. You would usually want this set to `1` in production environments, although setting it to `0` can provide marginal performance improvements. Deprecated and functionality replaced by [innodb\_checksum\_algorithm](innodb-system-variables.md#innodb_checksum_algorithm) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), and should be removed to avoid conflicts. `ON` is equivalent to `--innodb_checksum_algorithm=innodb` and `OFF` to `--innodb_checksum_algorithm=none`.
* Commandline: `--innodb-checksums`, `--skip-innodb-checksums`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)

#### `innodb_cleaner_lsn_age_factor`

* Description: XtraDB has enhanced page cleaner heuristics, and with these in place, the default InnoDB adaptive flushing may be too aggressive. As a result, a new LSN age factor formula has been introduced, controlled by this variable. The default setting, `high_checkpoint`, uses the new formula, while the alternative, `legacy`, uses the original algorithm. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `--innodb-cleaner-lsn-age-factor=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value:
  * `deprecated`
* Valid Values:
  * `deprecated`, `high_checkpoint`, `legacy`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_cmp_per_index_enabled`

* Description: If set to `ON` (`OFF` is default), per-index compression statistics are stored in the [INFORMATION\_SCHEMA.INNODB\_CMP\_PER\_INDEX](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md) table. These are expensive to record, so this setting should only be changed with care, such as for performance tuning on development or replica servers.
* Commandline: `--innodb-cmp-per-index-enabled={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_commit_concurrency`

* Description: Limit to the number of transaction threads that can commit simultaneously. 0, the default, imposes no limit. While you can change from one positive limit to another at runtime, you cannot set this variable to 0, or change it from 0, while the server is running. Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes).
* Commandline: `--innodb-commit-concurrency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `1000`
* Deprecated: [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_compression_algorithm`

* Description: Compression algorithm used for [InnoDB page compression](innodb-page-compression.md). The supported values are:
  * `none`: Pages are not compressed.
  * `zlib`: Pages are compressed using the bundled [zlib](https://www.zlib.net/) compression algorithm.
  * `lz4`: Pages are compressed using the [lz4](https://code.google.com/p/lz4/) compression algorithm.
  * `lzo`: Pages are compressed using the [lzo](https://www.oberhumer.com/opensource/lzo/) compression algorithm.
  * `lzma`: Pages are compressed using the [lzma](https://tukaani.org/xz/) compression algorithm.
  * `bzip2`: Pages are compressed using the [bzip2](https://www.bzip.org/) compression algorithm.
  * `snappy`: Pages are compressed using the [snappy](https://google.github.io/snappy/) algorithm.
  * On many distributions, MariaDB may not support all page compression algorithms by default. From [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107), libraries can be installed as a plugin. See [Compression Plugins](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md).
  * See [InnoDB Page Compression: Configuring the InnoDB Page Compression Algorithm](innodb-page-compression.md#configuring-the-innodb-page-compression-algorithm) for more information.
* Commandline: `--innodb-compression-algorithm=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `zlib`
* Valid Values:`none`, `zlib`, `lz4`, `lzo`, `lzma`, `bzip2` or `snappy`

#### `innodb_compression_default`

* Description: Whether or not [InnoDB page compression](innodb-page-compression.md) is enabled by default for new tables.
  * The default value is `OFF`, which means new tables are not compressed.
  * See [InnoDB Page Compression: Enabling InnoDB Page Compression by Default](innodb-page-compression.md#enabling-innodb-page-compression-by-default) for more information.
* Commandline: `--innodb-compression-default={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_compression_failure_threshold_pct`

* Description: Specifies the percentage cutoff for expensive compression failures during updates to a table that uses [InnoDB page compression](innodb-page-compression.md), after which free space is added to each new compressed page, dynamically adjusted up to the level set by [innodb\_compression\_pad\_pct\_max](innodb-system-variables.md#innodb_compression_pad_pct_max). Zero disables checking of compression efficiency and adjusting padding.
  * See [InnoDB Page Compression: Configuring the Failure Threshold and Padding](innodb-page-compression.md#configuring-the-failure-threshold-and-padding) for more information.
* Commandline: `--innodb-compression-failure-threshold-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `5`
* Range: `0` to `100`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_compression_level`

* Description: Specifies the default level of compression for tables that use [InnoDB page compression](innodb-page-compression.md).
  * Only a subset of InnoDB page compression algorithms support compression levels. If an InnoDB page compression algorithm does not support compression levels, then the compression level value is ignored.
  * The compression level can be set to any value between `1` and `9`. The default compression level is `6`. The range goes from the fastest to the most compact, which means that `1` is the fastest and `9` is the most compact.
  * See [InnoDB Page Compression: Configuring the Default Compression Level](innodb-page-compression.md#configuring-the-default-compression-level) for more information.
* Commandline: `--innodb-compression-level=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `6`
* Range: `1` to `9`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_compression_pad_pct_max`

* Description: The maximum percentage of reserved free space within each compressed page for tables that use [InnoDB page compression](innodb-page-compression.md). Reserved free space is used when the page's data is reorganized and might be recompressed. Only used when [innodb\_compression\_failure\_threshold\_pct](innodb-system-variables.md#innodb_compression_failure_threshold_pct) is not zero, and the rate of compression failures exceeds its setting.
  * See [InnoDB Page Compression: Configuring the Failure Threshold and Padding](innodb-page-compression.md#configuring-the-failure-threshold-and-padding) for more information.
* Commandline: `--innodb-compression-pad-pct-max=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `50`
* Range: `0` to `75`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_concurrency_tickets`

* Description: Number of times a newly-entered thread can enter and leave [InnoDB](./) until it is again subject to the limitations of [innodb\_thread\_concurrency](innodb-system-variables.md#innodb_thread_concurrency) and may possibly be queued. Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes).
* Commandline: `--innodb-concurrency-tickets=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `0` (>= [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes))
  * `5000` (<= [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes))
* Range: `1` to `18446744073709551615`
* Deprecated: [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_corrupt_table_action`

* Description: What action to perform when a corrupt table is found. XtraDB only.
  * When set to `assert`, the default, XtraDB will intentionally crash the server when it detects corrupted data in a single-table tablespace, with an assertion failure.
  * When set to `warn`, it will pass corruption as corrupt table instead of crashing, and disable all further I/O (except for deletion) on the table file.
  * If set to `salvage`, read access is permitted, but corrupted pages are ignored. [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) must be enabled for this option. Previously named `innodb_pass_corrupt_table`.
  * Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-corrupt-table-action=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value:
  * `assert` (<= [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1))
  * `deprecated` (<= [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes))
* Valid Values:
  * `deprecated`, `assert`, `warn`, `salvage`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_data_file_buffering`

* Description: Whether to enable the file system cache for data files. Set to `OFF` by default, will be set to `ON` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `fsync`, `littlesync`, `nosync`, or (Windows specific) `normal`.
* Commandline: `--innodb-data-file-buffering={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes)

#### `innodb_data_file_path`

* Description: Individual [InnoDB](./) data files, paths and sizes. The value of [innodb\_data\_home\_dir](innodb-system-variables.md#innodb_data_home_dir) is joined to each path specified by innodb\_data\_file\_path to get the full directory path. If innodb\_data\_home\_dir is an empty string, absolute paths can be specified here. A file size is specified (with K for kilobytes, M for megabytes and G for gigabytes). Also whether or not to `autoextend` the data file, and whether or not to [autoshrink](innodb-tablespaces/innodb-system-tablespaces.md#decreasing-the-size) on startup may also be specified.
* Commandline: `--innodb-data-file-path=name`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `ibdata1:12M:autoextend` (from [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)), `ibdata1:10M:autoextend` (before [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0))

#### `innodb_data_file_write_through`

* Description: Whether writes to InnoDB data files (including the temporary tablespace) are write through. Set to `OFF` by default, will be set to `ON` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `O_DSYNC`. On systems that support FUA it may make sense to enable write-through, to avoid extra system calls.
* Commandline: `--innodb-data-file-write-through={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes)

#### `innodb_data_home_dir`

* Description: Directory path for all [InnoDB](./) data files in the shared tablespace (assuming [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) is not enabled). File-specific information can be added in [innodb\_data\_file\_path](innodb-system-variables.md#innodb_data_file_path), as well as absolute paths if innodb\_data\_home\_dir is set to an empty string.
* Commandline: `--innodb-data-home-dir=path`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`
* Default Value: `The MariaDB data directory`

#### `innodb_deadlock_detect`

* Description: By default, the InnoDB deadlock detector is enabled. If set to off, deadlock detection is disabled and MariaDB will rely on [innodb\_lock\_wait\_timeout](innodb-system-variables.md#innodb_lock_wait_timeout) instead. This may be more efficient in systems with high concurrency as deadlock detection can cause a bottleneck when a number of threads have to wait for the same lock.
* Commandline: `--innodb-deadlock-detect`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `innodb_deadlock_report`

* Description: How to report deadlocks (if [innodb\_deadlock\_detect=ON](innodb-system-variables.md#innodb_deadlock_detect)).
  * `off`: Do not report any details of deadlocks.
  * `basic`: Report transactions and waiting locks.
  * `full`: Default. Report transactions, waiting locks and blocking locks.
* Commandline: `--innodb-deadlock-report=val`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `full`
* Valid Values: `off`, `basic`, `full`
* Introduced: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_default_page_encryption_key`

* Description: Encryption key used for page encryption.
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md) for more information.
* Commandline: `--innodb-default-page-encryption-key=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `255`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes)
* Removed: [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes)

#### `innodb_default_encryption_key_id`

* Description: ID of encryption key used by default to encrypt InnoDB tablespaces.
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md) for more information.
* Commandline: `--innodb-default-encryption-key-id=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `4294967295`

#### `innodb_default_row_format`

* Description: Specifies the default [row format](innodb-row-formats/innodb-row-formats-overview.md) to be used for InnoDB tables. The compressed row format cannot be set as the default.
  * See [InnoDB Row Formats Overview: Default Row Format](innodb-row-formats/innodb-row-formats-overview.md#default-row-format) for more information.
* Commandline: `--innodb-default-row-format=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `dynamic`
* Valid Values: `redundant`, `compact` or `dynamic`

#### `innodb_defragment`

* Description: When set to `1` (the default is `0`), InnoDB defragmentation is enabled. When set to FALSE, all existing defragmentation will be paused and new defragmentation commands will fail. Paused defragmentation commands will resume when this variable is set to true again. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `--innodb-defragment={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes)

#### `innodb_defragment_fill_factor`

* Description:. Indicates how full defragmentation should fill a page. Together with [innodb\_defragment\_fill\_factor\_n\_recs](innodb-system-variables.md#innodb_defragment_fill_factor_n_recs) ensures defragmentation won’t pack the page too full and cause page split on the next insert on every page. The variable indicating more defragmentation gain is the one effective. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `--innodb-defragment-fill-factor=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `double`
* Default Value: `0.9`
* Range: `0.7` to `1`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes)

#### `innodb_defragment_fill_factor_n_recs`

* Description: Number of records of space that defragmentation should leave on the page. This variable, together with [innodb\_defragment\_fill\_factor](innodb-system-variables.md#innodb_defragment_fill_factor), is introduced so defragmentation won't pack the page too full and cause page split on the next insert on every page. The variable indicating more defragmentation gain is the one effective. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `--innodb-defragment-fill-factor-n-recs=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `20`
* Range: `1` to `100`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes)

#### `innodb_defragment_frequency`

* Description: Maximum times per second for defragmenting a single index. This controls the number of times the defragmentation thread can request X\_LOCK on an index. The defragmentation thread will check whether 1/defragment\_frequency (s) has passed since it last worked on this index, and put the index back in the queue if not enough time has passed. The actual frequency can only be lower than this given number. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `--innodb-defragment-frequency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `integer`
* Default Value: `40`
* Range: `1` to `1000`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes)

#### `innodb_defragment_n_pages`

* Description: Number of pages considered at once when merging multiple pages to defragment. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `--innodb-defragment-n-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `7`
* Range: `2` to `32`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes)

#### `innodb_defragment_stats_accuracy`

* Description: Number of defragment stats changes there are before the stats are written to persistent storage. Defaults to zero, meaning disable defragment stats tracking. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Commandline: `--innodb-defragment-stats-accuracy=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-0-release-notes)

#### `innodb_dict_size_limit`

* Description: Size in bytes of a soft limit the memory used by tables in the data dictionary. Once this limit is reached, XtraDB will attempt to remove unused entries. If set to `0`, the default and standard InnoDB behavior, there is no limit to memory usage. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 and replaced by MySQL 5.6's new [table\_definition\_cache](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache) implementation.
* Commandline: `innodb-dict-size-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Default Value - 32 bit: `2147483648`
* Default Value - 64 bit: `9223372036854775807`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - replaced by MySQL 5.6's [table\_definition\_cache](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache) implementation.

#### `innodb_disable_sort_file_cache`

* Description: If set to `1` (`0` is default), the operating system file system cache for merge-sort temporary files is disabled.
* Commandline: `--innodb-disable-sort-file-cache={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_disallow_writes`

* Description: Tell InnoDB to stop any writes to disk.
* Commandline: None
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.3.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10335-release-notes), [MariaDB 10.4.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10425-release-notes), [MariaDB 10.5.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10516-release-notes), [MariaDB 10.6.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1068-release-notes), [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes)

#### `innodb_doublewrite`

* Description: If set to `1`, the default, to improve fault tolerance [InnoDB](./) first stores data to a [doublewrite buffer](innodb-doublewrite-buffer.md) before writing it to data file. Disabling will provide a marginal peformance improvement.
* Commandline: `--innodb-doublewrite`, `--skip-innodb-doublewrite`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_doublewrite_file`

* Description: The absolute or relative path and filename to a dedicated tablespace for the [doublewrite buffer](innodb-doublewrite-buffer.md). In heavy workloads, the doublewrite buffer can impact heavily on the server, and moving it to a different drive will reduce contention on random reads. Since the doublewrite buffer is mostly sequential writes, a traditional HDD is a better choice than SSD. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `innodb-doublewrite-file=filename`
* Scope: Global
* Dynamic: No
* Data Type: `filename`
* Default Value: `NULL`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_empty_free_list_algorithm`

* Description: XtraDB 5.6.13-61 introduced an algorithm to assist with reducing mutex contention when the buffer pool free list is empty, controlled by this variable. If set to `backoff`, the default until [MariaDB 10.1.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10124-release-notes), the new algorithm will be used. If set to `legacy`, the original InnoDB algorithm will be used. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades. See [#1651657](https://bugs.launchpad.net/percona-server/+bug/1651657) for the reasons this was changed back to `legacy` in XtraDB 5.6.36-82.0. When upgrading from 10.0 to 10.1 (>= 10.1.24), for large buffer pools the default will remain `backoff`, while for small ones it will be changed to `legacy`.
* Commandline: `innodb-empty-free-list-algorithm=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value:
  * `deprecated`
* Valid Values:
  * `deprecated`, `backoff`, `legacy`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_enable_unsafe_group_commit`

* Description: Unneeded after XtraDB 1.0.5. If set to `0`, the default, InnoDB will keep transactions between the transaction log and [binary log](../../../server-management/server-monitoring-logs/binary-log/)s in the same order. Safer, but slower. If set to `1`, transactions can be group-committed, but there is no guarantee of the order being kept, and a small risk of the two logs getting out of sync. In write-intensive environments, can lead to a significant improvement in performance.
* Commandline: `--innodb-enable-unsafe-group-commit`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `1`
* Removed: Not needed after XtraDB 1.0.5

#### `innodb_encrypt_log`

* Description: Enables encryption of the [InnoDB redo log](innodb-redo-log.md). This also enables encryption of some temporary files created internally by InnoDB, such as those used for merge sorts and row logs.
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling InnoDB Encryption: Enabling Encryption for the Redo Log](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-the-redo-log) for more information.
* Commandline: `--innodb-encrypt-log`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_encrypt_tables`

* Description: Enables automatic encryption of all InnoDB tablespaces.
  * `OFF` - Disables table encryption for all new and existing tables that have the [ENCRYPTED](../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`.
  * `ON` - Enables table encryption for all new and existing tables that have the [ENCRYPTED](../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`, but allows unencrypted tables to be created.
  * `FORCE` - Enables table encryption for all new and existing tables that have the [ENCRYPTED](../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`, and doesn't allow unencrypted tables to be created (CREATE TABLE ... ENCRYPTED=NO will fail).
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling InnoDB Encryption: Enabling Encryption for Automatically Encrypted Tablespaces](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-automatically-encrypted-tablespaces) for more information.
* Commandline: `--innodb-encrypt-tables={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Valid Values: `ON`, `OFF`, `FORCE`

#### `innodb_encrypt_temporary_tables`

* Description: Enables automatic encryption of the InnoDB [temporary tablespace](innodb-tablespaces/innodb-temporary-tablespaces.md).
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Enabling Encryption: Enabling Encryption for Temporary Tablespaces](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-temporary-tablespaces) for more information.
* Commandline: `--innodb-encrypt-temporary-tables={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Valid Values: `ON`, `OFF`
* Introduced: [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10226-release-notes), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10317-release-notes), [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes)

#### `innodb_encryption_rotate_key_age`

* Description: Re-encrypt in background any page having a key older than this number of key versions. When setting up encryption, this variable must be set to a non-zero value. Otherwise, when you enable encryption through [innodb\_encrypt\_tables](innodb-system-variables.md#innodb_encrypt_tables) MariaDB won't be able to automatically encrypt any unencrypted tables.
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys: Key Rotation](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md#key-rotation) for more information.
* Commandline: `--innodb-encryption-rotate-key-age=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `4294967295`

#### `innodb_encryption_rotation_iops`

* Description: Use this many iops for background key rotation operations performed by the background encryption threads.
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Encryption Keys: Key Rotation](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md#key-rotation) for more information.
* Commandline: `--innodb-encryption-rotation_iops=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `0` to `4294967295`

#### `innodb_encryption_threads`

* Description: Number of background encryption threads performing background key rotation and [scrubbing](innodb-data-scrubbing.md). When setting up encryption, this variable must be set to a non-zero value. Otherwise, when you enable encryption through [innodb\_encrypt\_tables](innodb-system-variables.md#innodb_encrypt_tables) MariaDB won't be able to automatically encrypt any unencrypted tables. Recommended never be set higher than 255.
  * See [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [InnoDB Background Encryption Threads](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/innodb-background-encryption-threads.md) for more information.
* Commandline: `--innodb-encryption-threads=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range:
  * `0` to `4294967295` (<= [MariaDB 10.1.45](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10145-release-notes), [MariaDB 10.2.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10232-release-notes), [MariaDB 10.3.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10323-release-notes), [MariaDB 10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10413-release-notes), [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1053-release-notes))
  * `0` to `255` (>= [MariaDB 10.1.46](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10146-release-notes), [MariaDB 10.2.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10233-release-notes), [MariaDB 10.3.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10324-release-notes), [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes), [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes))

#### `innodb_extra_rsegments`

* Description: Removed in XtraDB 5.5 and replaced by [innodb\_rollback\_segments](innodb-system-variables.md#innodb_rollback_segments). Usually there is one rollback segment protected by single mutex, a source of contention in high write environments. This option specifies a number of extra user rollback segments. Changing the default will make the data readable by XtraDB only, and is incompatible with InnoDB. After modifying, the server must be slow-shutdown. If there is existing data, it must be dumped before changing, and re-imported after the change has taken effect.
* Commandline: `--innodb-extra-rsegments=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `126`
* Removed: XtraDB 5.5 - replaced by [innodb\_rollback\_segments](innodb-system-variables.md#innodb_rollback_segments)

#### `innodb_extra_undoslots`

* Description: Usually, InnoDB has 1024 undo slots in its rollback segment, so 1024 transactions can run in parallel. New transactions will fail if all slots are used. Setting this variable to `1` expands the available undo slots to 4072. Not recommended unless you get the `Warning: cannot find a free slot for an undo log` error in the error log, as it makes data files unusable for ibbackup, or MariaDB servers not run with this option. See also [undo log](innodb-undo-log.md).
* Commandline: `--innodb-extra-undoslots={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: XtraDB 5.5

#### `innodb_fake_changes`

* Description: From [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) until [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1), XtraDB-only option that enables the fake changes feature. In [replication](../../../ha-and-performance/standard-replication/replication-overview.md), setting up or restarting a replica can cause a replication reads to perform more slowly, as MariaDB is single-threaded and needs to read the data before it can execute the queries. This can be speeded up by prefetching threads to warm the server, replaying the statements and then rolling back at commit. This however has an overhead from locking rows only then to undo changes at rollback. Fake changes attempts to reduce this overhead by reading the rows for INSERT, UPDATE and DELETE statements but not updating them. The rollback is then very fast with little or nothing to do. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades. Not present in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) and beyond.
* Commandline: `--innodb-fake-changes={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_fast_checksum`

* Description: Implements a more CPU efficient XtraDB checksum algorithm, useful for write-heavy loads with high I/O. If set to `1` on a server with tables that have been created with it set to `0`, reads will be slower, so tables should be recreated (dumped and reloaded). XtraDB will fail to start if set to `0` and there are tables created while set to `1`. Replaced with [innodb\_checksum\_algorithm](innodb-system-variables.md#innodb_checksum_algorithm) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6.
* Commandline: `--innodb-fast-checksum={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 - replaced with [innodb\_checksum\_algorithm](innodb-system-variables.md#innodb_checksum_algorithm)

#### `innodb_fast_shutdown`

* Description: The shutdown mode.
  * `0` - InnoDB performs a slow shutdown, including full purge (before [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes), not always, due to [MDEV-13603](https://jira.mariadb.org/browse/MDEV-13603)) and change buffer merge. Can be very slow, even taking hours in extreme cases.
  * `1` - the default, [InnoDB](./) performs a fast shutdown, not performing a full purge or an insert buffer merge.
  * `2`, the [InnoDB redo log](innodb-redo-log.md) is flushed and a cold shutdown takes place, similar to a crash. The resulting startup then performs crash recovery. Extremely fast, in cases of emergency, but risks corruption. Not suitable for upgrades between major versions!
  * `3` (from [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes)) - active transactions will not be rolled back, but all changed pages will be written to data files. The active transactions will be rolled back by a background thread on a subsequent startup. The fastest option that will not involve [InnoDB redo log](innodb-redo-log.md) apply on subsequent startup. See [MDEV-15832](https://jira.mariadb.org/browse/MDEV-15832).
* Commandline: `--innodb-fast-shutdown[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `3` (>= [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes)), `0` to `2` (<= [MariaDB 10.3.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes))

#### `innodb_fatal_semaphore_wait_threshold`

* Description: In MariaDB, the fatal semaphore timeout is configurable. This variable sets the maximum number of seconds for semaphores to time out in InnoDB.
* Commandline: `--innodb-fatal-semaphore-wait-threshold=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `600`
* Range: `1` to `4294967295`

#### `innodb_file_format`

* Description: File format for new [InnoDB](./) tables. Can either be `Antelope`, the default and the original format, or `Barracuda`, which supports [compression](innodb-page-compression.md). Note that this value is also used when a table is re-created with an [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md) which requires a table copy. See [XtraDB/InnoDB File Format](innodb-file-format.md) for more on the file formats. Removed in 10.3.1 and restored as a deprecated and unused variable in 10.4.3 for compatibility purposes.
* Commandline: `--innodb-file-format=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value:
  * `Barracuda`
* Valid Values: `Antelope`, `Barracuda`
* Deprecated: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes)
* Re-introduced: [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes) (for compatibility purposes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_file_format_check`

* Description: If set to `1`, the default, [InnoDB](./) checks the shared tablespace file format tag. If this is higher than the current version supported by XtraDB/InnoDB (for example Barracuda when only Antelope is supported), XtraDB/InnoDB will not start. If it the value is not higher, XtraDB/InnoDB starts correctly and the [innodb\_file\_format\_max](innodb-system-variables.md#innodb_file_format_max) value is set to this value. If innodb\_file\_format\_check is set to `0`, no checking is performed. See [XtraDB/InnoDB File Format](innodb-file-format.md) for more on the file formats.
* Commandline: `--innodb-file-format-check={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes)

#### `innodb_file_format_max`

* Description: The highest [XtraDB/InnoDB](./) file format. This is set to the value of the file format tag in the shared tablespace on startup (see [innodb\_file\_format\_check](innodb-system-variables.md#innodb_file_format_check)). If the server later creates a higher table format, innodb\_file\_format\_max is set to that value. See [XtraDB/InnoDB File Format](innodb-file-format.md) for more on the file formats.
* Commandline: `--innodb-file-format-max=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `Antelope`
* Valid Values: `Antelope`, `Barracuda`
* Deprecated: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes)

#### `innodb_file_per_table`

* Description: If set to `ON`, then new [InnoDB](./) tables are created with their own [InnoDB file-per-table tablespaces](innodb-tablespaces/innodb-file-per-table-tablespaces.md). If set to `OFF`, then new tables are created in the [InnoDB system tablespace](innodb-tablespaces/innodb-system-tablespaces.md) instead. [Page compression](innodb-page-compression.md) is only available with file-per-table tablespaces. Note that this value is also used when a table is re-created with an [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md) which requires a table copy. Deprecated in [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) as there's no benefit to setting to `OFF`, the original InnoDB default.
* Commandline: `--innodb-file-per-table`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes)

#### `innodb_fill_factor`

* Description: Percentage of B-tree page filled during bulk insert (sorted index build). Used as a hint rather than an absolute value. Setting to `70`, for example, reserves 30% of the space on each B-tree page for the index to grow in future.
* Commandline: `--innodb-fill-factor=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `10` to `100`

#### `innodb_flush_log_at_timeout`

* Description: Interval in seconds to write and flush the [InnoDB redo log](innodb-redo-log.md). Before MariaDB 10, this was fixed at one second, which is still the default, but this can now be changed. It's usually increased to reduce flushing and avoid impacting performance of binary log group commit.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `2700`

#### `innodb_flush_log_at_trx_commit`

* Description: Set to `1`, along with [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) for the greatest level of fault tolerance. The value of [innodb\_use\_global\_flush\_log\_at\_trx\_commit](innodb-system-variables.md#innodb_use_global_flush_log_at_trx_commit) determines whether this variable can be reset with a SET statement or not.
  * `1` The default, the log buffer is written to the [InnoDB redo log](innodb-redo-log.md) file and a flush to disk performed after each transaction. This is required for full ACID compliance.
  * `0` Nothing is done on commit; rather the log buffer is written and flushed to the [InnoDB redo log](innodb-redo-log.md) once a second. This gives better performance, but a server crash can erase the last second of transactions.
  * `2` The log buffer is written to the [InnoDB redo log](innodb-redo-log.md) after each commit, but flushing takes place every [innodb\_flush\_log\_at\_timeout](innodb-system-variables.md#innodb_flush_log_at_timeout) seconds (by default once a second). Performance is slightly better, but a OS or power outage can cause the last second's transactions to be lost.
  * `3` Emulates [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) [group commit](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) (3 syncs per group commit). See [Binlog group commit and innodb\_flush\_log\_at\_trx\_commit](binary-log-group-commit-and-innodb-flushing-performance.md). This option has not been working correctly since 10.2 and may be removed in future, see [1873](https://github.com/MariaDB/server/pull/1873)
* Commandline: `--innodb-flush-log-at-trx-commit[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `1`
* Valid Values: `0`, `1`, `2` or `3`

#### `innodb_flush_method`

* Description: [InnoDB](./) flushing method. Windows always uses async\_unbuffered and this variable then has no effect. On Unix, before [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes), by default fsync() is used to flush data and logs. Adjusting this variable can give performance improvements, but behavior differs widely on different filesystems, and changing from the default has caused problems in some situations, so test and benchmark carefully before adjusting. In MariaDB, Windows recognises and correctly handles the Unix methods, but if none are specified it uses own default - unbuffered write (analog of O\_DIRECT) + syncs (e.g FileFlushBuffers()) for all files.
  * `O_DSYNC` - O\_DSYNC is used to open and flush logs, and fsync() to flush the data files.
  * `O_DIRECT` - O\_DIRECT or directio(), is used to open data files, and fsync() to flush data and logs. Default on Unix from [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes).
  * `fsync` - Default on Unix until [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105). Can be specified directly, but if the variable is unset on Unix, fsync() will be used by default.
  * `O_DIRECT_NO_FSYNC` - introduced in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0). Uses O\_DIRECT during flushing I/O, but skips fsync() afterwards. Not suitable for XFS filesystems. Generally not recommended over O\_DIRECT, as does not get the benefit of [innodb\_use\_native\_aio=ON](innodb-system-variables.md#innodb_use_native_aio).
  * `ALL_O_DIRECT` - introduced in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) and available with XtraDB only. Uses O\_DIRECT for opening both data and logs and fsync() to flush data but not logs. Use with large InnoDB files only, otherwise may cause a performance degradation. Set [innodb\_log\_block\_size](innodb-system-variables.md#innodb_log_block_size) to 4096 on ext4 filesystems. This is the default log block size on ext4 and will avoid unaligned AIO/DIO warnings.
  * `unbuffered` - Windows-only default
  * `async_unbuffered` - Windows-only, alias for `unbuffered`
  * `normal` - Windows-only, alias for `fsync`
  * `littlesync` - for internal testing only
  * `nosync` - for internal testing only
* Deprecated in [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) and replaced by four boolean dynamic variables that can be changed while the server is running: [innodb\_log\_file\_buffering](innodb-system-variables.md#innodb_log_file_buffering) (disable O\_DIRECT, added by [MDEV-28766](https://jira.mariadb.org/browse/MDEV-28766) in 10.8.4, 10.9.2), [innodb\_data\_file\_buffering](innodb-system-variables.md#innodb_data_file_buffering) (disable O\_DIRECT on data files), [innodb\_log\_file\_write\_through](innodb-system-variables.md#innodb_log_file_write_through) (enable O\_DSYNC on the log), [innodb\_data\_file\_write\_through](innodb-system-variables.md#innodb_data_file_write_through) (enable O\_DSYNC on persistent data files)From [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110), if set to one of the following values, then the values of the four boolean flags will be set as follows:
  * `O_DSYNC`: [innodb\_log\_file\_write\_through=ON](innodb-system-variables.md#innodb_log_file_write_through), [innodb\_data\_file\_write\_through=ON](innodb-system-variables.md#innodb_data_file_write_through),[innodb\_data\_file\_buffering=OFF](innodb-system-variables.md#innodb_data_file_buffering), and (if supported) [innodb\_log\_file\_buffering=OFF](innodb-system-variables.md#innodb_log_file_buffering).
  * `fsync`, `littlesync`, `nosync`, or (Microsoft Windows specific) `normal`: [innodb\_log\_file\_write\_through=OFF](innodb-system-variables.md#innodb_log_file_write_through), [innodb\_data\_file\_write\_through=OFF](innodb-system-variables.md#innodb_data_file_write_through), and [innodb\_data\_file\_buffering=ON](innodb-system-variables.md#innodb_data_file_buffering).
* Commandline: `--innodb-flush-method=name`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration` (>= [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes)), `string` (<= [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes))
* Default Value:
  * `O_DIRECT` (Unix, >= [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes))
  * `fsync` (Unix, >= [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), <= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105))
  * Not set (<= [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes))
* Valid Values:
  * Unix: `fsync`, `O_DSYNC`, `littlesync`, `nosync`. `O_DIRECT`, `O_DIRECT_NO_FSYNC`
  * Windows: `unbuffered`, `async_unbuffered`, `normal`
* Deprecated: [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110)

#### `innodb_flush_neighbor_pages`

* Description: Determines whether, when dirty pages are flushed to the data file, neighboring pages in the data file are flushed at the same time. If set to `none`, the feature is disabled. If set to `area`, the default, the standard InnoDB behavior is used. For each page to be flushed, dirty neighboring pages are flushed too. If there's little head seek delay, such as SSD or large enough write buffer, one of the other two options may be more efficient. If set to `cont`, for each page to be flushed, neighboring contiguous blocks are flushed at the same time. Being contiguous, a sequential I/O is used, unlike the random I/O used in `area`. Replaced by [innodb\_flush\_neighbors](innodb-system-variables.md#innodb_flush_neighbors) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6.
* Commandline: `innodb-flush-neighbor-pages=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `area`
* Valid Values: `none` or `0`, `area` or `1`, `cont` or `2`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 - replaced by [innodb\_flush\_neighbors](innodb-system-variables.md#innodb_flush_neighbors)

#### `innodb_flush_neighbors`

* Description: Determines whether flushing a page from the [buffer pool](innodb-buffer-pool.md) will flush other dirty pages in the same group of pages (extent). In high write environments, if flushing is not aggressive enough, it can fall behind resulting in higher memory usage, or if flushing is too aggressive, cause excess I/O activity. SSD devices, with low seek times, would be less likely to require dirty neighbor flushing to be set. Since [MariaDB 10.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1044-release-notes) an attempt is made under Windows and Linux to determine SSD status which was exposed in [information\_schema.innodb\_tablespaces\_scrubbing\_table](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_scrubbing-table.md). This variable is ignored for table spaces that are detected as stored on SSD (and the `0` behavior applies).
  * `1`: The default, flushes contiguous dirty pages in the same extent from the buffer pool.
  * `0`: No other dirty pages are flushed.
  * `2`: Flushes dirty pages in the same extent from the buffer pool.
* Commandline: `--innodb-flush-neighbors=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `1`
* Valid Values: `0`, `1`, `2`

#### `innodb_flush_sync`

* Description: If set to `ON`, the default, the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) setting is ignored for I/O bursts occuring at checkpoints.
* Commandline: `--innodb-flush-sync={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_flushing_avg_loops`

* Description: Determines how quickly adaptive flushing will respond to changing workloads. The value is the number of iterations that a previously calculated flushing state snapshot is kept. Increasing the value smooths and slows the rate that the flushing operations change, while decreasing it causes flushing activity to spike quickly in response to workload changes.
* Commandline: `--innodb-flushing-avg-loops=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `30`
* Range: `1` to `1000`

#### `innodb_force_load_corrupted`

* Description: Set to `0` by default, if set to `1`, [InnoDB](./) will be permitted to load tables marked as corrupt. Only use this to recover data you can't recover any other way, or in troubleshooting. Always restore to `0` when the returning to regular use. Given that [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412) in [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes) aims to allow any metadata for a missing or corrupted table to be dropped, and given that [MDEV-17567](https://jira.mariadb.org/browse/MDEV-17567) and [MDEV-25506](https://jira.mariadb.org/browse/MDEV-25506) and related tasks made DDL operations crash-safe, the parameter no longer serves any purpose and was removed in [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1066-release-notes).
* Commandline: `--innodb-force-load-corrupted`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1066-release-notes)

#### `innodb_force_primary_key`

* Description: If set to `1` (`0` is default) CREATE TABLEs without a primary or unique key where all keyparts are NOT NULL will not be accepted, and will return an error.
* Commandline: `--innodb-force-primary-key`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_force_recovery`

* Description: [InnoDB](./) crash recovery mode. `0` is the default. The other modes are for recovery purposes only, and no data can be changed while another mode is active. Some queries relying on indexes are also blocked. See [InnoDB Recovery Modes](innodb-troubleshooting/innodb-recovery-modes.md) for more on mode specifics.
* Commandline: `--innodb-force-recovery=#`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value: `0`
* Range: `0` to `6`

#### `innodb_foreground_preflush`

* Description: Before XtraDB 5.6.13-61.0, if the checkpoint age is in the sync preflush zone while a thread is writing to the [XtraDB redo log](innodb-redo-log.md), it will try to advance the checkpoint by issuing a flush list flush batch if this is not already being done. XtraDB has enhanced page cleaner tuning, and may already be performing furious flushing, resulting in the flush simply adding unneeded mutex pressure. Instead, the thread now waits for the flushes to finish, and then has two options, controlled by this variable. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
  * `exponential_backoff` - thread sleeps while it waits for the flush list flush to occur. The sleep time randomly progressively increases, periodically reset to avoid runaway sleeps.
  * `sync_preflush` - thread issues a flush list batch, and waits for it to complete. This is the same as is used when the page cleaner thread is not running.
* Commandline: `innodb-foreground-preflush=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value:
  * `deprecated`
* Valid Values:
  * `deprecated`, `exponential_backoff`, `sync_preflush`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_ft_aux_table`

* Description: Diagnostic variable intended only to be set at runtime. It specifies the qualified name (for example `test/ft_innodb`) of an InnoDB table that has a [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), and after being set the INFORMATION\_SCHEMA tables [INNODB\_FT\_INDEX\_TABLE](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_index_table-table.md), [INNODB\_FT\_INDEX\_CACHE](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_index_cache-table.md), INNODB\_FT\_CONFIG, [INNODB\_FT\_DELETED](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_deleted-table.md), and [INNODB\_FT\_BEING\_DELETED](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_being_deleted-table.md) will contain search index information for the specified table.
* Commandline: `--innodb-ft-aux-table=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_ft_cache_size`

* Description: Cache size available for a parsed document while creating an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/).
* Commandline: `--innodb-ft-cache-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8000000`

#### `innodb_ft_enable_diag_print`

* Description: If set to `1`, additional [full-text](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) search diagnostic output is enabled.
* Commandline: `--innodb-ft-enable-diag-print={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_ft_enable_stopword`

* Description: If set to `1`, the default, a set of [stopwords](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) is associated with an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) when it is created. The stopword list comes from the table set by the session variable [innodb\_ft\_user\_stopword\_table](innodb-system-variables.md#innodb_ft_user_stopword_table), if set, otherwise the global variable [innodb\_ft\_server\_stopword\_table](innodb-system-variables.md#innodb_ft_server_stopword_table), if that is set, or the [built-in list](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) if neither variable is set.
* Commandline: `--innodb-ft-enable-stopword={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_ft_max_token_size`

* Description: Maximum length of words stored in an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). A larger limit will increase the size of the index, slowing down queries, but permit longer words to be searched for. In most normal situations, longer words are unlikely search terms.
* Commandline: `--innodb-ft-max-token-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `84`
* Range: `10` to `84`

#### `innodb_ft_min_token_size`

* Description: Minimum length of words stored in an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). A smaller limit will increase the size of the index, slowing down queries, but permit shorter words to be searched for. For data stored in a Chinese, Japanese or Korean [character set](../../../reference/data-types/string-data-types/character-sets/), a value of 1 should be specified to preserve functionality.
* Commandline: `--innodb-ft-min-token-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `3`
* Range: `0` to `16`

#### `innodb_ft_num_word_optimize`

* Description: Number of words processed during each [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) on an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). To ensure all changes are incorporated, multiple OPTIMIZE TABLE statements could be run in case of a substantial change to the index.
* Commandline: `--innodb-ft-num-word-optimize=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2000`
* Range: `1000` to `10000`

#### `innodb_ft_result_cache_limit`

* Description: Limit in bytes of the InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) query result cache per fulltext query. The latter stages of the full-text search are handled in memory, and limiting this prevents excess memory usage. If the limit is exceeded, the query returns an error.
* Commandline: `--innodb-ft-result-cache-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2000000000`
* Range: `1000000` to `18446744073709551615`

#### `innodb_ft_server_stopword_table`

* Description: Table name containing a list of stopwords to ignore when creating an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), in the format db\_name/table\_name. The specified table must exist before this option is set, and must be an InnoDB table with a single column, a [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) named VALUE. See also [innodb\_ft\_enable\_stopword](innodb-system-variables.md#innodb_ft_enable_stopword).
* Commandline: `--innodb-ft-server-stopword-table=db_name/table_name`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty

#### `innodb_ft_sort_pll_degree`

* Description: Number of parallel threads used when building an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). See also [innodb\_sort\_buffer\_size](innodb-system-variables.md#innodb_sort_buffer_size).
* Commandline: `--innodb-ft-sort-pll-degree=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `2`
* Range: `1` to `32`

#### `innodb_ft_total_cache_size`

* Description:Total memory allocated for the cache for all InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) tables. A force sync is triggered if this limit is exceeded.
* Commandline: `--innodb-ft-total-cache-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `640000000`
* Range: `32000000` to `1600000000`
* Introduced: [MariaDB 10.0.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes)

#### `innodb_ft_user_stopword_table`

* Description: Table name containing a list of stopwords to ignore when creating an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), in the format db\_name/table\_name. The specified table must exist before this option is set, and must be an InnoDB table with a single column, a [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) named VALUE. See also [innodb\_ft\_enable\_stopword](innodb-system-variables.md#innodb_ft_enable_stopword).
* Commandline: `--innodb-ft-user-stopword-table=db_name/table_name`
* Scope: Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty

#### `innodb_ibuf_accel_rate`

* Description: Allows the insert buffer activity to be adjusted. The following formula is used: \[real activity] = \[default activity] \* (innodb\_io\_capacity/100) \* (innodb\_ibuf\_accel\_rate/100). As `innodb_ibuf_accel_rate` is increased from its default value of `100`, the lowest setting, insert buffer activity is increased. See also [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity). This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `innodb-ibuf-accel-rate=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `100` to `999999999`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_ibuf_active_contract`

* Description: Specifies whether the insert buffer can be processed before it's full. If set to `0`, the standard InnoDB method is used, and the buffer is not processed until it's full. If set to `1`, the default, the insert buffer can be processed before it is full. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `innodb-ibuf-active-contract=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `1`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_ibuf_max_size`

* Description: Maximum size in bytes of the insert buffer. Defaults to half the size of the [buffer pool](innodb-buffer-pool.md) so you may want to reduce if you have a very large buffer pool. If set to `0`, the insert buffer is disabled, which will cause all secondary index updates to be performed synchronously, usually at a cost to performance. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `innodb-ibuf-max-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: 1/2 the size of the InnoDB buffer pool
* Range: `0` to 1/2 the size of the InnoDB buffer pool
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_idle_flush_pct`

* Description: Up to what percentage of dirty pages should be flushed when innodb finds it has spare resources to do so. Has had no effect since merging InnoDB 5.7 from mysql-5.7.9 ([MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes)). Deprecated in [MariaDB 10.2.37](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10237-release-notes), [MariaDB 10.3.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10328-release-notes), [MariaDB 10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10418-release-notes) and removed in [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1059-release-notes).
* Commandline: `--innodb-idle-flush-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `0` to `100`
* Deprecated: [MariaDB 10.2.37](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10237-release-notes), [MariaDB 10.3.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10328-release-notes), [MariaDB 10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10418-release-notes)
* Removed: [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1059-release-notes)

#### `innodb_immediate_scrub_data_uncompressed`

* Description: Enable scrubbing of data. See [Data Scrubbing](innodb-data-scrubbing.md).
* Commandline: `--innodb-immediate-scrub-data-uncompressed={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_import_table_from_xtrabackup`

* Description: If set to `1`, permits importing of .ibd files exported with the [XtraBackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) --export option. Previously named `innodb_expand_import`. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 and replaced with MySQL 5.6's transportable tablespaces.
* Commandline: `innodb-import-table-from-xtrabackup=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `1`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_instant_alter_column_allowed`

* Description:
  * If a table is altered using ALGORITHM=INSTANT, it can force the table to use a non-canonical\
    format: A hidden metadata record at the start of the clustered index is used to store each column's DEFAULT value. This makes it possible to add new columns that have default values without rebuilding the table. Starting with [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), a BLOB in the hidden metadata record is used to store column mappings. This makes\
    it possible to drop or reorder columns without rebuilding the table. This also makes it possible to add columns to any position or drop columns from any position in the table without rebuilding the table. If a column is dropped without rebuilding the table, old records will contain garbage in that column's former position, and new records\
    will be written with NULL values, empty strings, or dummy values.
  * This is generally not a problem. However, there may be cases where\
    you want to avoid putting a table into this format.\
    For example, to ensure that future UPDATE operations\
    after an ADD COLUMN will be performed in-place, to reduce write\
    amplification. (Instantly added columns are essentially always\
    variable-length.) Also avoid bugs similar to[MDEV-19916](https://jira.mariadb.org/browse/MDEV-19916), or to be able to export tables to\
    older versions of the server.
  * This variable has been introduced as a result, with the following values:
  * `never` (0): Do not allow instant add/drop/reorder,\
    to maintain format compatibility with MariaDB 10.x and MySQL 5.x.\
    If the table (or partition) is not in the canonical format, then\
    any ALTER TABLE (even one that does not involve instant column\
    operations) will force a table rebuild.
  * `add_last` (1, default in 10.3): Store a hidden metadata record that\
    allows columns to be appended to the table instantly ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)).\
    In 10.4 or later, if the table (or partition) is not in this format,\
    then any ALTER TABLE (even one that does not involve column changes)\
    will force a table rebuild.
  * `add_drop_reorder` (2, default): From [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) only. Like 'add\_last', but allow the\
    metadata record to store a column map, to support instant\
    add/drop/reorder of columns.
* Commandline: `--innodb-instant-alter-column-allowed=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Valid Values:
  * <= [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103): `never`, `add_last`
  * > \= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104): `never`, `add_last`, `add_drop_reorder`
* Default Value:
  * <= [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103): `add_last`
  * > \= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104): `add_drop_reorder`
* Introduced: [MariaDB 10.3.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10323-release-notes), [MariaDB 10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10413-release-notes), [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1053-release-notes)

#### `innodb_instrument_semaphores`

* Description: Enable semaphore request instrumentation. This could have some effect on performance but allows better information on long semaphore wait problems.
* Commandline: `--innodb-instrument-semaphores={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes) (treated as if `OFF`)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_io_capacity`

* Description: Limit on I/O activity for InnoDB background tasks, including merging data from the insert buffer and flushing pages. Should be set to around the number of I/O operations per second that system can handle, based on the type of drive/s being used. You can also set it higher when the server starts to help with the extra workload at that time, and then reduce for normal use. Ideally, opt for a lower setting, as at higher value data is removed from the buffers too quickly, reducing the effectiveness of caching. See also [innodb\_flush\_sync](innodb-system-variables.md#innodb_flush_sync).
  * See [InnoDB Page Flushing: Configuring the InnoDB I/O Capacity](innodb-page-flushing.md#configuring-the-innodb-io-capacity) for more information.
* Commandline: `--innodb-io-capacity=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `200`
* Range: `100` to `18446744073709551615` (2<sup>64</sup>-1)

#### `innodb_io_capacity_max`

* Description: Upper limit to which InnoDB can extend [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) in case of emergency. See [InnoDB Page Flushing: Configuring the InnoDB I/O Capacity](innodb-page-flushing.md#configuring-the-innodb-io-capacity) for more information.
* Commandline: `--innodb-io-capacity-max=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2000` or twice [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity), whichever is higher.
* Range : `100` to `18446744073709551615` (2<sup>64</sup>-1)

#### `innodb_kill_idle_transaction`

* Description: Time in seconds before killing an idle XtraDB transaction. If set to `0` (the default), the feature is disabled. Used to prevent accidental user locks. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `9223372036854775807`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_large_prefix`

* Description: If set to `1`, tables that use specific [row formats](innodb-row-formats/innodb-row-formats-overview.md) are permitted to have index key prefixes up to 3072 bytes (for 16k pages, [smaller otherwise](innodb-limitations.md#page-sizes)). If not set, the limit is 767 bytes.
  * This applies to the [DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md) and [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row formats.
  * Removed in 10.3.1 and restored as a deprecated and unused variable in 10.4.3 for compatibility purposes.
* Commandline: `--innodb-large-prefix`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value:
  * `ON`
* Deprecated: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* Removed: [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes)
* Re-introduced: [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes) (for compatibility purposes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_lazy_drop_table`

* Description: Deprecated and removed in XtraDB 5.6. [DROP TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md) processing can take a long time when [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) is set to 1 and there's a large [buffer pool](innodb-buffer-pool.md). If `innodb_lazy_drop_table` is set to `1` (`0` is default), XtraDB attempts to optimize [DROP TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md) processing by deferring the dropping of related pages from the [buffer pool](innodb-buffer-pool.md) until there is time, only initially marking them.
* Commandline: `innodb-lazy-drop-table={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`
* Deprecated: XtraDB 5.5.30-30.2
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1000-release-notes)

#### `innodb_lock_schedule_algorithm`

* Description: Removed in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes) due to problems with the VATS implementation ([MDEV-16664](https://jira.mariadb.org/browse/MDEV-16664)). Specifies the algorithm that InnoDB uses to decide which of the waiting transactions should be granted the lock once it has been released. The possible values are: `FCFS` (First-Come-First-Served) where locks are granted in the order they appear in the lock queue and `VATS` (Variance-Aware-Transaction-Scheduling) where locks are granted based on the Eldest-Transaction-First heuristic. Note that `VATS` should not be used with [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/), and InnoDB will refuse to start if `VATS` is used with Galera. It is also not recommended to set to `VATS` even in the general case ([MDEV-16664](https://jira.mariadb.org/browse/MDEV-16664)). From [MariaDB 10.2.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10212-release-notes), the value was changed to `FCFS` and a warning produced when using Galera.
* Commandline: `--innodb-lock-schedule-algorithm=#`
* Scope: Global
* Dynamic: No (>= [MariaDB 10.2.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10212-release-notes), [MariaDB 10.1.30](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10130-release-notes)), Yes (<= [MariaDB 10.2.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10211-release-notes), [MariaDB 10.1.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10129-release-notes))
* Data Type: `enum`
* Valid Values: `FCFS`, `VATS`
* Default Value: `FCFS` ([MariaDB 10.3.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1039-release-notes), [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes)), `VATS` ([MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes)), `FCFS` ([MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1))
* Deprecated: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10416-release-notes), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10326-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_lock_wait_timeout`

* Description: Time in seconds that an InnoDB transaction waits for an InnoDB record lock (or table lock) before giving up with the error `ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction`. When this occurs, the statement (not transaction) is rolled back. The whole transaction can be rolled back if the [innodb\_rollback\_on\_timeout](innodb-system-variables.md#innodb_rollback_on_timeout) option is used. Increase this for data warehousing applications or where other long-running operations are common, or decrease for OLTP and other highly interactive applications. This setting does not apply to deadlocks, which InnoDB detects immediately, rolling back a deadlocked transaction. `0` means no wait. See [WAIT and NOWAIT](../../../reference/sql-statements/transactions/wait-and-nowait.md). Setting to `100000000` or more (from [MariaDB 10.6.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1063-release-notes), `100000000` is the maximum) means the timeout is infinite.
* Commandline: `--innodb-lock-wait-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `INT UNSIGNED` (>= [MariaDB 10.6.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1063-release-notes)), `BIGINT UNSIGNED` (<= [MariaDB 10.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1062-release-notes))
* Default Value: `50`
* Range:
  * `0` to `100000000` (>= [MariaDB 10.6.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1063-release-notes))
  * `0` to `1073741824` (>= [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) to <= [MariaDB 10.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1062-release-notes))

#### `innodb_locking_fake_changes`

* Description: From [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) to [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1), XtraDB-only option that if set to `OFF`, fake transactions (see [innodb\_fake\_changes](innodb-system-variables.md#innodb_fake_changes)) don't take row locks. This is an experimental feature to attempt to deal with drawbacks in fake changes blocking real locks. It is not safe for use in all environments. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `--innodb-locking-fake-changes`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_locks_unsafe_for_binlog`

* Description: Set to `0` by default, in which case XtraDB/InnoDB uses [gap locking](innodb-lock-modes.md). If set to `1`, gap locking is disabled for searches and index scans. Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), and removed in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), use [READ COMMITTED transaction isolation level](../../../reference/sql-statements/transactions/transactions-read-committed.md) instead.
* Commandline: `--innodb-locks-unsafe-for-binlog`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)

#### `innodb_log_arch_dir`

* Description: The directory for [XtraDB redo log](innodb-redo-log.md) archiving. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `--innodb-log-arch-dir=name`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `./`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_log_arch_expire_sec`

* Description: Time in seconds since the last change after which the archived [XtraDB redo log](innodb-redo-log.md) should be deleted. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `--innodb-log-arch-expire-sec=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_log_archive`

* Description: Whether or not [XtraDB redo log](innodb-redo-log.md) archiving is enabled. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `--innodb-log-archive={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_log_block_size`

* Description: Size in bytes of the [XtraDB redo log](innodb-redo-log.md) records. Generally `512`, the default, or `4096`, are the only two useful values. If the server is restarted and this value is changed, all old log files need to be removed. Should be set to `4096` for SSD cards or if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `ALL_O_DIRECT` on ext4 filesystems. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-log-block-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `512`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_log_buffer_size`

* Description: Size in bytes of the buffer for writing [InnoDB redo log](innodb-redo-log.md) files to disk. Increasing this means larger transactions can run without needing to perform disk I/O before committing.
* Commandline: `--innodb-log-buffer-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `16777216` (16MB)
* Range: `262144` to `2147479552` (256KB to 2GB - 4K) (>= [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-8-release-notes))
* Range: `262144` to `18446744073709551615` (<= [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-7-release-notes)) - limit to the above maximium because this is an operating system limit.
* Block size: `4096`

#### `innodb_log_checksum_algorithm`

* Description: Experimental feature (as of [MariaDB 10.0.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1009-release-notes)), this variable specifies how to generate and verify [XtraDB redo log](innodb-redo-log.md) checksums. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
  * `none` - No checksum. A constant value is instead written to logs, and no checksum validation is performed.
  * `innodb` - The default, and the original InnoDB algorithm. This is inefficient, but compatible with all MySQL, MariaDB and Percona versions that don't support other checksum algorithms.
  * `crc32` - CRC32© is used for log block checksums, which also permits recent CPUs to use hardware acceleration (on SSE4.2 x86 machines and Power8 or later) for the checksums.
  * `strict_*` - Whether or not to accept checksums from other algorithms. If strict mode is used, checksums blocks will be considered corrupt if they don't match the specified algorithm. Normally they are considered corrupt only if no other algorithm matches.
* Commandline: `innodb-log-checksum-algorithm=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value:
  * `deprecated` (>= [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes))
  * `innodb` (<= [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1))
* Valid Values:
  * `deprecated`, `innodb`, `none`, `crc32`, `strict_none`, `strict_innodb`, `strict_crc32` (>= [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes))
  * `innodb`, `none`, `crc32`, `strict_none`, `strict_innodb`, `strict_crc32` (<= [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1))
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_log_checksums`

* Description: If set to `1`, the CRC32C for Innodb or `innodb_log_checksum_algorithm` for XtraDB algorithm is used for [InnoDB redo log](innodb-redo-log.md) pages. If disabled, the checksum field contents are ignored. From [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes), the variable is deprecated, and checksums are always calculated, as previously, the InnoDB redo log used the slow innodb algorithm, but with hardware or SIMD assisted CRC-32C computation being available, there is no reason to allow checksums to be disabled on the redo log.
* Commandline: `innodb-log-checksums={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_log_compressed_pages`

* Description: Whether or not images of recompressed pages are stored in the [InnoDB redo log](innodb-redo-log.md). Deprecated and ignored from [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1053-release-notes).
* Commandline: `--innodb-log-compressed-pages={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value:
  * `ON`
* Deprecated: [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1053-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_log_file_buffering`

* Description: Whether the file system cache for ib\_logfile0 is enabled. In [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes), MariaDB disabled the file system cache on the InnoDB write-ahead log file (ib\_logfile0) by default on Linux. With [innodb\_flush\_trx\_log\_at\_commit=2](innodb-system-variables.md#innodb_flush_log_at_trx_commit) in particular, writing to the log via the file system cache typically improves throughput, especially on slow storage or at a small number of concurrent transactions. For other values of innodb\_flush\_log\_at\_trx\_commit, direct writes were observed to be mostly but not always faster. Whether it pays off to disable the file system cache on the log may depend on the type of storage, the workload, and the operating system kernel version. If the server is started up with [innodb\_flush\_log\_at\_trx\_commit=2](innodb-system-variables.md#innodb_flush_log_at_trx_commit), the value will be changed to `ON`. Will be set to `OFF` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `O_DSYNC`. On Linux, when the physical block size cannot be determined to be a power of 2 between 64 and 4096 bytes, the file system cache cannot be disabled, and innodb\_log\_file\_buffering=ON cannot be changed. Linux and Windows only.
* Commandline: `--innodb-log-file-buffering={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-10-8-series/mariadb-1084-changelog), [MariaDB 10.9.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-109-series/mariadb-1092-changelog)

#### `innodb_log_file_mmap`

* Description: Whether ib\_logfile0 resides in persistent memory or should initially be memory-mapped. When using the default innodb\_log\_buffer\_size=2m, mariadb-backup --backup would spend a lot of time re-reading and re-parsing the log. For reading the log file during mariadb-backup --backup, it is beneficial to memory-map the entire ib\_logfile0 to the address space (typically 48 bits or 256 TiB) and read it from there,\
  both during --backup and --prepare. OFF by default on most platforms, to avoid aggressive read-ahead of the entire ib\_logfile0 in when only a tiny portion would be accessed. On Linux and FreeBSD the default is innodb\_log\_file\_mmap=ON, because those platforms define a specific mmap(2) option for enabling such read-ahead and therefore it can be assumed that the default wouldbe on-demand paging. This parameter will only have impact on the initial InnoDB startup and recovery. Any writes to the log will use regular I/O, except when the ib\_logfile0 is stored in a specially configured file system that is backed by persistent memory (Linux "mount -o dax").
* Commandline: `--innodb-log-file-mmap{=0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON` (Linux, FreeBSD), `OFF` (Other platforms)
* Introduced: [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes), [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes)

#### `innodb_log_file_size`

* Description: Size in bytes of each [InnoDB redo log](innodb-redo-log.md) file in the log group. The combined size can be no more than 512GB. Larger values mean less disk I/O due to less flushing checkpoint activity, but also slower recovery from a crash. In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), crash recovery has been improved and shouldn't run out of memory, so the default has been increased. It can safely be set higher to reduce checkpoint flushing, even larger than [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size).From [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109) the variable is dynamic, and the server no longer needs to be restarted for the resizing to take place. Unless the log is located in a persistent memory file system (PMEM), an attempt to [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) innodb\_log\_file\_size to less than [innodb\_log\_buffer\_size](innodb-system-variables.md#innodb_log_buffer_size) will be refused. Log resizing can be aborted by killing the connection that is executing the SET GLOBAL statement.
* Commandline: `--innodb-log-file-size=#`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109)), No (<= [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108))
* Data Type: `numeric`
* Default Value: `100663296` (96MB) (>= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)), `50331648` (48MB) (<= [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112))
* Range:
  * > \= [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes): `4194304` to `512GB` (4MB to 512GB)
  * <= [MariaDB 10.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1082-release-notes): `1048576` to `512GB` (1MB to 512GB)
* Block size: `4096`

#### `innodb_log_file_write_through`

* Description: Whether each write to ib\_logfile0 is write through (disabling any caching, as in O\_SYNC or O\_DSYNC). Set to `OFF` by default, will be set to `ON` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `O_DSYNC`. On systems that support FUA it may make sense to enable write-through, to avoid extra system calls.
* Commandline: `--innodb-log-file-write-through={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes)

#### `innodb_log_files_in_group`

* Description: Number of physical files in the [InnoDB redo log](innodb-redo-log.md). Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Commandline: `--innodb-log-files-in-group=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1` (>= [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105)), `2` (<= [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/storage-engines/innodb/broken-reference/README.md))
* Range: `1` to `100` (>= [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes))
* Deprecated: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_log_group_home_dir`

* Description: Path to the [InnoDB redo log](innodb-redo-log.md) files. If none is specified, [innodb\_log\_files\_in\_group](innodb-system-variables.md#innodb_log_files_in_group) files named ib\_logfile0 and so on, with a size of [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) are created in the data directory.
* Commandline: `--innodb-log-group-home-dir=path`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`

#### `innodb_log_optimize_ddl`

* Description: Whether [InnoDB redo log](innodb-redo-log.md) activity should be reduced when natively creating indexes or rebuilding tables. Reduced logging requires additional page flushing and interferes with [mariadb-backup](../../backup-and-restore/mariadb-backup/). Enabling this may slow down backup and cause delay due to page flushing. Deprecated and ignored from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes). Deprecated (but not ignored) from [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10416-release-notes), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10326-release-notes) and [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes).
* Commandline: `--innodb-log-optimize-ddl={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value:
  * `OFF` (>= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10416-release-notes), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10326-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes))
  * `ON` (<= [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes), [MariaDB 10.4.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10415-release-notes), [MariaDB 10.3.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10325-release-notes), [MariaDB 10.2.34](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10234-release-notes))
* Introduced: [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes), [MariaDB 10.3.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1039-release-notes)
* Deprecated: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10416-release-notes), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10326-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_log_spin_wait_delay`

* Description: Delay between log buffer spin lock polls (0 to use a blocking latch). Specifically, enables a spin lock that will execute that many MY\_RELAX\_CPU() operations (such as the x86 PAUSE instruction) between successive attempts of acquiring the spin lock. On some hardware with certain workloads (observed on write intensive workloads on NUMA systems), the default setting results in a significant amount of time being spent in native\_queued\_spin\_lock\_slowpath() in the Linux kernel, plus context switching between user and kernel address space, in which case changing from the default (for example, setting to `50`), may result in a performance improvement.
* Commandline: `--innodb-log-spin-wait-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `6000`
* Introduced: [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes), [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-2-release-notes), [MariaDB 11.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-1-release-notes)

#### `innodb_log_write_ahead_size`

* Description: [InnoDB redo log](innodb-redo-log.md) write ahead unit size to avoid read-on-write. Should match the OS cache block IO size. Removed in [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108), and instead on Linux and Windows, the physical block size of the underlying storage is detected and used. Reintroduced in [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-9-release-notes) and later versions. On Linux and Windows, the default or the specified innodb\_log\_write\_ahead\_size will be automatically adjusted to not be less than the physical block size (if it can be determined).
* Commandline: `--innodb-log-write-ahead-size=#`
* Scope: Global
* Dynamic: No (>= [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-9-release-notes)), Yes (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107))
* Data Type: `numeric`
* Default Value: `512` (>= [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-9-release-notes)), `8192` (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107))
* Range:
  * `512` to `4096` (>= [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-9-release-notes))
  * `512` to [innodb\_page\_size](innodb-system-variables.md#innodb_page_size) (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107))
* Removed: [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108)
* Re-introduced: [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-9-release-notes), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-3-release-notes), [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes)

#### `innodb_lru_flush_size`

* Description: Number of pages to flush on LRU eviction. Changes in [MariaDB 10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-18-release-notes), [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes) and [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-2-release-notes) made this setting superfluous, and it is no longer used.
* Commandline: `--innodb-lru-flush-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `32`
* Range: `1` to `18446744073709551615`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes)
* Deprecated: [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-20-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes) and [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-4-release-notes). [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes), [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes)

#### `innodb_lru_scan_depth`

* Description: Specifies how far down the buffer pool least-recently used (LRU) list the cleaning thread should look for dirty pages to flush. This process is performed once a second. In an I/O intensive-workload, can be increased if there is spare I/O capacity, or decreased if in a write-intensive workload with little spare I/O capacity.
  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Commandline: `--innodb-lru-scan-depth=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `1536` (>= [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes))
  * `1024` (<= [MariaDB 10.5.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1056-release-notes))
* Range - 32bit: `100` to `2^32-1`
* Range - 64bit: `100` to `2^64-1`

#### `innodb_max_bitmap_file_size`

* Description: Limit in bytes of the changed page bitmap files. For faster incremental backup with [Xtrabackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md), XtraDB tracks pages with changes written to them according to the [XtraDB redo log](innodb-redo-log.md) and writes the information to special changed page bitmap files. These files are rotated when the server restarts or when this limit is reached. XtraDB only. See also [innodb\_track\_changed\_pages](innodb-system-variables.md#innodb_track_changed_pages) and [innodb\_max\_changed\_pages](innodb-system-variables.md#innodb_max_changed_pages).
  * Deprecated and ignored in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-max-bitmap-file-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4096` (4KB)
* Range: `4096` (4KB) to `18446744073709551615` (16EB)
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)

#### `innodb_max_changed_pages`

* Description: Limit to the number of changed page bitmap files (stored in the [Information Schema INNODB\_CHANGED\_PAGES table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_changed_pages-table.md)). Zero is unlimited. See [innodb\_max\_bitmap\_file\_size](innodb-system-variables.md#innodb_max_bitmap_file_size) and [innodb\_track\_changed\_pages](innodb-system-variables.md#innodb_track_changed_pages). Previously named `innodb_changed_pages_limit`. XtraDB only.
  * Deprecated and ignored in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-max-changed-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000000`
* Range: `0` to `18446744073709551615`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)

#### `innodb_max_dirty_pages_pct`

* Description: Maximum percentage of unwritten (dirty) pages in the buffer pool.
  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Commandline: `--innodb-max-dirty-pages-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `90.000000` (>= [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes))
  * `75.000000` (<= [MariaDB 10.5.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1056-release-notes))
* Range: `0` to `99.999`

#### `innodb_max_dirty_pages_pct_lwm`

* Description: Low water mark percentage of dirty pages that will enable preflushing to lower the dirty page ratio. The value 0 (default) means 'refer to [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct)'. (Note that 0 meant 0 in 10.5.7 to 10.5.8, but was then reverted back to "same as innodb\_max\_dirty\_pages\_pct" again in 10.5.9)
  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Commandline: `--innodb-max-dirty-pages-pct-lwm=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `0` (>= [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes))
  * `0.001` (<= [MariaDB 10.2.0](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/storage-engines/innodb/broken-reference/README.md))
* Range: `0` to `99.999`

#### `innodb_max_purge_lag`

* Description: When purge operations are lagging on a busy server, setting innodb\_max\_purge\_lag can help. By default set to `0`, no lag, the figure is used to calculate a time lag for each INSERT, UPDATE, and DELETE when the system is lagging. InnoDB keeps a list of transactions with delete-marked index records due to UPDATE and DELETE statements. The length of this list is `purge_lag`, and the calculation, performed every ten seconds, is as follows: ((purge\_lag/innodb\_max\_purge\_lag)×10)–5 microseconds.
* Commandline: `--innodb-max-purge-lag=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`

#### `innodb_max_purge_lag_delay`

* Description: Maximum delay in milliseconds imposed by the [innodb\_max\_purge\_lag](innodb-system-variables.md#innodb_max_purge_lag) setting. If set to `0`, the default, there is no maximum.
* Commandline: `--innodb-max-purge-lag-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`

#### `innodb_max_purge_lag_wait`

* Description: Wait until History list length is below the specified limit.
* Commandline: `--innodb-max-purge-wait=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4294967295`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10416-release-notes), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10326-release-notes), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10235-release-notes)

#### `innodb_max_undo_log_size`

* Description: If an undo tablespace is larger than this, it will be marked for truncation if [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate) is set.
* Commandline: `--innodb-max-undo-log-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `10485760`
* Range: `10485760` to `18446744073709551615`

#### `innodb_merge_sort_block_size`

* Description: Size in bytes of the block used for merge sorting in fast index creation. Replaced in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 by [innodb\_sort\_buffer\_size](innodb-system-variables.md#innodb_sort_buffer_size).
* Commandline: `innodb-merge-sort-block-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1048576` (1M)
* Range: `1048576` (1M) to `1073741824` (1G)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - replaced by [innodb\_sort\_buffer\_size](innodb-system-variables.md#innodb_sort_buffer_size)

#### `innodb_mirrored_log_groups`

* Description: Unused. Restored as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Deprecated: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes) - [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes)

#### `innodb_mtflush_threads`

* Description: Sets the number of threads to use in Multi-Threaded Flush operations. For more information, see [Fusion-io Multi-threaded Flush](innodb-page-flushing.md).
  * InnoDB's multi-thread flush feature was deprecated in [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes) and removed from [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes). In later versions of MariaDB, use [innodb\_page\_cleaners](innodb-system-variables.md#innodb_page_cleaners) system variable instead.
  * See [InnoDB Page Flushing: Page Flushing with Multi-threaded Flush Threads](innodb-page-flushing.md#page-flushing-with-multi-threaded-flush-threads) for more information.
* Commandline: `--innodb-mtflush-threads=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `64`
* Deprecated: [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes)
* Removed: [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes)

#### `innodb_monitor_disable`

* Description: Disables the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Commandline: `--innodb-monitor-disable=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_monitor_enable`

* Description: Enables the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Commandline: `--innodb-monitor-enable=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_monitor_reset`

* Description: Resets the count value of the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table to zero.
* Commandline: `--innodb-monitor-reset=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_monitor_reset_all`

* Description: Resets all values for the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Commandline: `---innodb-monitor-reset-all=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_numa_interleave`

* Description: Whether or not to use the NUMA interleave memory policy to allocate the [InnoDB buffer pool](innodb-buffer-pool.md). Before [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes), required that MariaDB be compiled on a NUMA-enabled Linux system.
* Commandline: `innodb-numa-interleave={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.2.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10223-release-notes), [MariaDB 10.3.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10314-release-notes), [MariaDB 10.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1044-release-notes)

#### `innodb_old_blocks_pct`

* Description: Percentage of the [buffer pool](innodb-buffer-pool.md) to use for the old block sublist.
* Commandline: `--innodb-old-blocks-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `37`
* Range: `5` to `95`

#### `innodb_old_blocks_time`

* Description: Time in milliseconds an inserted block must stay in the old sublist after its first access before it can be moved to the new sublist. '0' means "no delay". Setting a non-zero value can help prevent full table scans clogging the [buffer pool](innodb-buffer-pool.md). See also [innodb\_old\_blocks\_pct](innodb-system-variables.md#innodb_old_blocks_pct).
* Commandline: `--innodb-old-blocks-time=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000`
* Range: `0` to `2^32-1`

#### `innodb_online_alter_log_max_size`

* Description: The maximum size for temporary log files during online DDL (data and index structure changes). The temporary log file is used for each table being altered, or index being created, to store data changes to the table while the process is underway. The table is extended by [innodb\_sort\_buffer\_size](innodb-system-variables.md#innodb_sort_buffer_size) up to the limit set by this variable. If this limit is exceeded, the online DDL operation fails and all uncommitted changes are rolled back. A lower value reduces the time a table could lock at the end of the operation to apply all the log's changes, but also increases the chance of the online DDL changes failing.
* Commandline: `--innodb-online-alter-log-max-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `134217728`
* Range: `65536` to `2^64-1`

#### `innodb_open_files`

* Description: Maximum .ibd files MariaDB can have open at the same time. Only applies to systems with multiple XtraDB/InnoDB tablespaces, and is separate to the table cache and [open\_files\_limit](innodb-system-variables.md#open_files_limit). The default, if [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) is disabled, is 300 or the value of [table\_open\_cache](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache), whichever is higher. It will also auto-size up to the default value if it is set to a value less than `10`.
* Commandline: `--innodb-open-files=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `autosized`
* Range: `10` to `4294967295`

#### `innodb_optimize_fulltext_only`

* Description: When set to `1` (`0` is default), [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) will only process InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) data. Only intended for use during fulltext index maintenance.
* Commandline: `--innodb-optimize-fulltext-only={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_page_cleaners`

* Description: Number of page cleaner threads. The default is `4`, but the value will be set to the number of [innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances) if this is lower. If set to `1`, only a single cleaner thread is used, as was the case until [MariaDB 10.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1021-release-notes). Cleaner threads flush dirty pages from the [buffer pool](innodb-buffer-pool.md), performing flush list and least-recently used (LRU) flushing. Deprecated and ignored from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes), as the original reasons for splitting the buffer pool have mostly gone away.
  * See [InnoDB Page Flushing: Page Flushing with Multiple InnoDB Page Cleaner Threads](innodb-page-flushing.md#page-flushing-with-multiple-innodb-page-cleaner-threads) for more information.
* Commandline: `--innodb-page-cleaners=#`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)), No (<= [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes))
* Data Type: `numeric`
* Default Value: `4` (or set to [innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances) if lower)
* Range: `1` to `64`
* Deprecated: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_page_size`

* Description: Specifies the page size in bytes for all InnoDB tablespaces. The default, `16k`, is suitable for most uses.
  * A smaller InnoDB page size might work more effectively in a situation with many small writes (OLTP), or with SSD storage, which usually has smaller block sizes.
  * A larger InnoDB page size can provide a larger [maximum row size](innodb-row-formats/innodb-row-formats-overview.md#maximum-row-size).
  * InnoDB's page size can be as large as `64k` for tables using the following [row formats](innodb-row-formats/innodb-row-formats-overview.md): [DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md), [COMPACT](innodb-row-formats/innodb-compact-row-format.md), and [REDUNDANT](innodb-row-formats/innodb-redundant-row-format.md).
  * InnoDB's page size must still be `16k` or less for tables using the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format.
  * This system variable's value cannot be changed after the `datadir` has been initialized. InnoDB's page size is set when a MariaDB instance starts, and it remains constant afterwards.
* Commandline: `--innodb-page-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value: `16384`
* Valid Values: `4k` or `4096`, `8k` or `8192`, `16k` or `16384`, `32k` and `64k`.

#### `innodb_pass_corrupt_table`

* Removed: XtraDB 5.5 - renamed [innodb\_corrupt\_table\_action](innodb-system-variables.md#innodb_corrupt_table_action).

#### `innodb_prefix_index_cluster_optimization`

* Description: Enable prefix optimization to sometimes avoid cluster index lookups. Deprecated and ignored from [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010), as the optimization is now always enabled.
* Commandline: `--innodb-prefix-index-cluster-optimization={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.10.1](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/storage-engines/innodb/broken-reference/README.md)

#### `innodb_print_all_deadlocks`

* Description: If set to `1` (`0` is default), all InnoDB transaction deadlock information is written to the [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Commandline: `--innodb-print-all-deadlocks={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_purge_batch_size`

* Description: Number of [InnoDB undo log](innodb-undo-log.md) pages to purge in one batch from the history list. Together with [innodb\_purge\_threads](innodb-system-variables.md#innodb_purge_threads) has a small effect on tuning.
* Commandline: `--innodb-purge-batch-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:
  * `127` (>= [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-20-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes))
  * `1000` (>= [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes) [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes))
  * `300` (<= [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-15-release-notes), [MariaDB 10.10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-6-release-notes), [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-5-release-notes), [MariaDB 11.0.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes), [MariaDB 11.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-2-release-notes) [MariaDB 11.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-1-release-notes))
* Range: `1` to `5000`

#### `innodb_purge_rseg_truncate_frequency`

* Description: Frequency with which undo records are purged. Set by default to every 128 times, reducing this increases the frequency at which rollback segments are freed. See also [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate). The motivation for introducing this in MySQL seems to have been to avoid stalls due to freeing undo log pages or truncating undo log tablespaces. In MariaDB, [innodb\_undo\_log\_truncate=ON](innodb-system-variables.md#innodb_undo_log_truncate) should be a much lighter operation because it will not involve any log checkpoint, hence this is deprecated and ignored from [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes) and [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes). ([MDEV-32050](https://jira.mariadb.org/browse/MDEV-32050))
* Commandline: `-- innodb-purge-rseg-truncate-frequency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `128`
* Range: `1` to `128`
* Deprecated: [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes), [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes)

#### `innodb_purge_threads`

* Description: Number of background threads dedicated to InnoDB purge operations. The range is `1` to `32`. At least one background thread is always used. Setting to a value greater than 1 creates that many separate purge threads. This can improve efficiency in some cases, such as when performing DML operations on many tables. See also [innodb\_purge\_batch\_size](innodb-system-variables.md#innodb_purge_batch_size).
* Commandline: `--innodb-purge-threads=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `32`

#### `innodb_random_read_ahead`

* Description: Originally, random read-ahead was always set as an optimization technique, but was removed in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5). `innodb_random_read_ahead` permits it to be re-instated if set to `1` (`0`) is default.
* Commandline: `--innodb-random-read-ahead={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_read_ahead`

* Description: If set to `linear`, the default, XtraDB/InnoDB will automatically fetch remaining pages if there are enough within the same extent that can be accessed sequentially. If set to `none`, read-ahead is disabled. `random` has been removed and is now ignored, while `both` sets to both `linear` and `random`. Also see [innodb\_read\_ahead\_threshold](innodb-system-variables.md#innodb_read_ahead_threshold) for more control on read-aheads. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 and replaced by MySQL 5.6's [innodb\_random\_read\_ahead](innodb-system-variables.md#innodb_random_read_ahead).
* Commandline: `innodb-read-ahead=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `linear`
* Valid Values: `none`, `random`, `linear`, `both`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 - replaced by MySQL 5.6's [innodb\_random\_read\_ahead](innodb-system-variables.md#innodb_random_read_ahead)

#### `innodb_read_ahead_threshold`

* Description: Minimum number of pages InnoDB must read sequentially from an extent of 64 before initiating an asynchronous read for the following extent.
* Commandline: `--innodb-read-ahead-threshold=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `56`
* Range: `0` to `64`

#### `innodb_read_io_threads`

* Description: Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), this was simply the number of I/O threads for InnoDB reads. From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), asynchronous I/O functionality in the InnoDB Background Thread Pool replaces the old InnoDB I/O Threads. This variable is now multipled by 256 to determine the maximum number of concurrent asynchronous I/O read requests that can be completed by the Background Thread Pool. The default is therefore 4\*256 = 1024 conccurrent asynchronous read requests. You may on rare occasions need to reduce this default on Linux systems running multiple MariaDB servers to avoid exceeding system limits, or increase if spending too much time waiting on I/O requests.
* Commandline: `--innodb-read-io-threads=#`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/what-is-mariadb-1011)), No (<= [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010))
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `64`

#### `innodb_read_only`

* Description: If set to `1` (`0` is default), the server will be read-only. For use in distributed applications, data warehouses or read-only media.
* Commandline: `--innodb-read-only={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_read_only_compressed`

* Description: If set (the default before [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1066-release-notes)), [ROW\_FORMAT=COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) tables will be read-only. This was intended to be the first step towards removing write support and deprecating the feature, but this plan has been abandoned.
* Commandline: `--innodb-read-only-compressed`, `--skip-innodb-read-only-compressed`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF` (>= [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1066-release-notes)), `ON` (<= [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1065-release-notes))
* Introduced: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_recovery_stats`

* Description: If set to `1` (`0` is default) and recovery is necessary on startup, the server will write detailed recovery statistics to the error log at the end of the recovery process. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: No
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `innodb_recovery_update_relay_log`

* Description: If set to `1` (`0` is default), the relay log info file will be overwritten on crash recovery if the information differs from the InnoDB record. Should not be used if multiple storage engine types are being replicated. Previously named `innodb_overwrite_relay_log_info`. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6 and replaced by MySQL 5.6's `relay-log-recovery`
* Commandline: `innodb-recovery-update-relay-log={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - replaced by MySQL 5.6's `relay-log-recovery`

#### `innodb_replication_delay`

* Description: Time in milliseconds for the replica server to delay the replication thread if [innodb\_thread\_concurrency](innodb-system-variables.md#innodb_thread_concurrency) is reached. Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes).
* Commandline: `--innodb-replication-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`
* Deprecated: [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_rollback_on_timeout`

* Description: InnoDB usually rolls back the last statement of a transaction that's been timed out (see [innodb\_lock\_wait\_timeout](innodb-system-variables.md#innodb_lock_wait_timeout)). If innodb\_rollback\_on\_timeout is set to 1 (0 is default), InnoDB will roll back the entire transaction. Before [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), rolling back the entire transaction was the default behavior.
* Commandline: `--innodb-rollback-on-timeout`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0`

#### `innodb_rollback_segments`

* Description: Specifies the number of rollback segments that XtraDB/InnoDB will use within a transaction (see [undo log](innodb-undo-log.md)). Deprecated and replaced by [innodb\_undo\_logs](innodb-system-variables.md#innodb_undo_logs) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0). Removed in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105) as part of an InnoDB cleanup, as it makes sense to always create and use the maximum number of rollback segments. |
* Commandline: `--innodb-rollback-segments=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `128`
* Range: `1` to `128`
* Deprecated: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)

#### `innodb_safe_truncate`

* Description: Use a backup-safe [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md) implementation and crash-safe rename operations inside InnoDB. This is not compatible with hot backup tools other than [mariadb-backup](../../backup-and-restore/mariadb-backup/mariadb-backup-overview.md). Users who need to use such tools may set this to `OFF`.
* Commandline: `--innodb-safe-truncate={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.2.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10219-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_scrub_log`

* Description: Enable [InnoDB redo log](innodb-redo-log.md) scrubbing. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes), as never really worked ([MDEV-13019](https://jira.mariadb.org/browse/MDEV-13019) and [MDEV-18370](https://jira.mariadb.org/browse/MDEV-18370)). If old log contents should be kept secret, then enabling [innodb\_encrypt\_log](innodb-system-variables.md#innodb_encrypt_log) or setting a smaller [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) could help.
* Commandline: `--innodb-scrub-log`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_scrub_log_interval`

* Description: Used with [Data Scrubbing](innodb-data-scrubbing.md) in 10.1.3 only - replaced in 10.1.4 by [innodb\_scrub\_log\_speed](innodb-system-variables.md#innodb_scrub_log_speed). [InnoDB redo log](innodb-redo-log.md) scrubbing interval in milliseconds.
* Commandline: `--innodb-scrub-log-interval=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `56`
* Range: `0` to `50000`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-3-release-notes)
* Removed: [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes)

#### `innodb_scrub_log_speed`

* Description: [InnoDB redo log](innodb-redo-log.md) scrubbing speed in bytes/sec. See [Data Scrubbing](innodb-data-scrubbing.md). Deprecated and ignored from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes).
* Commandline: `--innodb-scrub-log-speed=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `256`
* Range: `1` to `50000`
* Deprecated: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1052-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_sched_priority_cleaner`

* Description: Set a thread scheduling priority for cleaner and least-recently used (LRU) manager threads. The range from `0` to `39` corresponds in reverse order to Linux nice values of `-20` to `19`. So `0` is the lowest priority (Linux nice value `19`) and `39` is the highest priority (Linux nice value `-20`). XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-sched-priority-cleaner=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `19`
* Range: `0` to `39`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_show_locks_held`

* Description: Specifies the number of locks held for each InnoDB transaction to be displayed in [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-show-locks-held=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `1000`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_show_verbose_locks`

* Description: If set to `1`, and [innodb\_status\_output\_locks](innodb-system-variables.md#innodb_status_output_locks) is also ON, the traditional InnoDB behavior is followed and locked records will be shown in [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) output. If set to `0`, the default, only high-level information about the lock is shown. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-show-verbose-locks=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `1`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_simulate_comp_failures`

* Description: Simulate compression failures. Used for testing robustness against random compression failures. XtraDB only.
* Commandline: None
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `99`

#### `innodb_snapshot_isolation`

* Description: Use snapshot isolation (write-write conflict detection). If set, if an attempt to acquire a lock on a record that does not exist in the current read view is made, an error DB\_RECORD\_CHANGED (HA\_ERR\_RECORD\_CHANGED, ER\_CHECKREAD) will be raised. This error will be treated in the same way as a deadlock and the transaction will be rolled back. When set, the default isolation level, [REPEATABLE READ](../../../reference/sql-statements/transactions/transactions-repeatable-read.md) will become Snapshot Isolation. Prior to [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes), the default is OFF for backwards compatibility.
* Commandline: `--innodb-snapshot-isolation={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON` (>= [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes)), `OFF` (<= [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes))
* Introduced: [MariaDB 10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-18-release-notes), [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes), [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-2-release-notes)

#### `innodb_sort_buffer_size`

* Description: Size of the sort buffers used for sorting data when an InnoDB index is created, as well as the amount by which the temporary log file is extended during online DDL operations to record concurrent writes. The larger the setting, the fewer merge phases are required between buffers while sorting. When a [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md) creates a new index, three buffers of this size are allocated, as well as pointers for the rows in the buffer.
* Commandline: `--innodb-sort-buffer-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1048576` (1M)
* Range: `65536` to `67108864`

#### `innodb_log_spin_wait_delay`

* Description: Maximum delay (not strictly corresponding to a time unit) between spin lock polls. Default changed from `6` to `4` in [MariaDB 10.3.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes), as this was verified to give the best throughput by OLTP update index and read-write benchmarks on Intel Broadwell (2/20/40) and ARM (1/46/46).
* Commandline: `--innodb-log-spin-wait-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4` (>= [MariaDB 10.3.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes)), `6` (<= [MariaDB 10.3.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1034-release-notes))
* Range: `0` to `4294967295`

#### `innodb_stats_auto_recalc`

* Description: If set to `1` (the default), persistent statistics are automatically recalculated when the table changes significantly (more than 10% of the rows). Affects tables created or altered with STATS\_PERSISTENT=1 (see [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) ), or when [innodb\_stats\_persistent](innodb-system-variables.md#innodb_stats_persistent) is enabled. [innodb\_stats\_persistent\_sample\_pages](innodb-system-variables.md#innodb_stats_persistent_sample_pages) determines how much data to sample when recalculating. See [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `--innodb-stats-auto-recalc={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_stats_auto_update`

* Description: If set to `0` (`1` is default), index statistics will not be automatically calculated except when an [ANALYZE TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md) is run, or the table is first opened. Replaced by [innodb\_stats\_auto\_recalc](innodb-system-variables.md#innodb_stats_auto_recalc) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6.
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) - replaced by [innodb\_stats\_auto\_recalc](innodb-system-variables.md#innodb_stats_auto_recalc).

#### `innodb_stats_include_delete_marked`

* Description: Include delete marked records when calculating persistent statistics.
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_stats_method`

* Description: Determines how NULLs are treated for InnoDB index statistics purposes.
  * `nulls_equal`: The default, all NULL index values are treated as a single group. This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful.
  * `nulls_unequal`: The opposite approach to `nulls_equal` is taken, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable.
  * `nulls_ignored`: Ignore NULLs altogether from index group calculations.
  * See also [Index Statistics](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/index-statistics.md), [aria\_stats\_method](../aria/aria-system-variables.md) and [myisam\_stats\_method](../myisam-storage-engine/myisam-system-variables.md).
* Commandline: `--innodb-stats-method=name`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `nulls_equal`
* Valid Values: `nulls_equal`, `nulls_unequal`, `nulls_ignored`

#### `innodb_stats_modified_counter`

* Description: The number of rows modified before we calculate new statistics. If set to `0`, the default, current limits are used.
* Commandline: `--innodb-stats-modified-counter=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `innodb_stats_on_metadata`

* Description: If set to `1`, the default, XtraDB/InnoDB updates statistics when accessing the INFORMATION\_SCHEMA.TABLES or INFORMATION\_SCHEMA.STATISTICS tables, and when running metadata statements such as [SHOW INDEX](../../../reference/sql-statements/administrative-sql-statements/show/show-index.md) or [SHOW TABLE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md). If set to `0`, statistics are not updated at those times, which can reduce the access time for large schemas, as well as make execution plans more stable.
* Commandline: `--innodb-stats-on-metadata`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_stats_persistent`

* Description: [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) produces index statistics, and this setting determines whether they will be stored on disk, or be required to be recalculated more frequently, such as when the server restarts. This information is stored for each table, and can be set with the STATS\_PERSISTENT clause when creating or altering tables (see [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md)). See [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `--innodb-stats-persistent={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_stats_persistent_sample_pages`

* Description: Number of index pages sampled when estimating cardinality and statistics for indexed columns. Increasing this value will increases index statistics accuracy, but use more I/O resources when running [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md). See [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `--innodb-stats-persistent-sample-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `20`

#### `innodb_stats_sample_pages`

* Description: Gives control over the index distribution statistics by determining the number of index pages to sample. Higher values produce more disk I/O, but, especially for large tables, produce more accurate statistics and therefore make more effective use of the query optimizer. Lower values than the default are not recommended, as the statistics can be quite inaccurate.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is enabled, then the exact number of pages configured by this system variable will be sampled for statistics.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * If [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled, then the [innodb\_stats\_persistent\_sample\_pages](innodb-system-variables.md#innodb_stats_persistent_sample_pages) system variable applies instead. [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled with the [innodb\_stats\_persistent](innodb-system-variables.md#innodb_stats_persistent) system variable.
  * This system variable has been deprecated. The [innodb\_stats\_transient\_sample\_pages](innodb-system-variables.md#innodb_stats_transient_sample_pages) system variable should be used instead.
* Commandline: `--innodb-stats-sample-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `2^64-1`
* Deprecated: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)

#### `innodb_stats_traditional`

* Description: This system variable affects how the number of pages to sample for transient statistics is determined, in particular how [innodb\_stats\_transient\_sample\_pages](innodb-system-variables.md#innodb_stats_transient_sample_pages) is used.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is enabled, then the exact number of pages configured by the system variable will be sampled for statistics.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * This system variable does not affect the calculation of [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Commandline: `--innodb-stats-traditional={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_stats_transient_sample_pages`

* Description: Gives control over the index distribution statistics by determining the number of index pages to sample. Higher values produce more disk I/O, but, especially for large tables, produce more accurate statistics and therefore make more effective use of the query optimizer. Lower values than the default are not recommended, as the statistics can be quite inaccurate.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is enabled, then the exact number of pages configured by this system variable will be sampled for statistics.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * If [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled, then the [innodb\_stats\_persistent\_sample\_pages](innodb-system-variables.md#innodb_stats_persistent_sample_pages) system variable applies instead. [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled with the [innodb\_stats\_persistent](innodb-system-variables.md#innodb_stats_persistent) system variable.
* Commandline: `--innodb-stats-transient-sample-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `2^64-1`

#### `innodb_stats_update_need_lock`

* Description: Setting to `0` (`1` is default) may help reduce contention of the `&dict_operation_lock`, but also disables the Data\_free option in [SHOW TABLE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md). This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6

#### `innodb_status_output`

* Description: Enable [InnoDB monitor](innodb-monitors.md) output to the [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Commandline: `--innodb-status-output={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_status_output_locks`

* Description: Enable [InnoDB lock monitor](innodb-monitors.md) output to the [error log](../../../server-management/server-monitoring-logs/error-log.md) and [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md). Also requires [innodb\_status\_output=ON](innodb-system-variables.md#innodb_status_output) to enable output to the error log.
* Commandline: `--innodb-status-output-locks={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_strict_mode`

* Description: If set to `1` (the default), InnoDB will return errors instead of warnings in certain cases, similar to strict SQL mode. See [InnoDB Strict Mode](innodb-strict-mode.md) for details.
* Commandline: `--innodb-strict-mode={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_support_xa`

* Description: If set to `1`, the default, [XA transactions](../../../reference/sql-statements/transactions/xa-transactions.md) are supported. XA support ensures data is written to the [binary log](../../../server-management/server-monitoring-logs/binary-log/) in the same order to the actual database, which is critical for [replication](../../../ha-and-performance/standard-replication/replication-overview.md) and disaster recovery, but comes at a small performance cost. If your database is set up to only permit one thread to change data (for example, on a replication replica with only the replication thread writing), it is safe to turn this option off. Removed in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), XA transactions are always supported.
* Commandline: `--innodb-support-xa`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_sync_array_size`

* Description: By default `1`, can be increased to split internal thread co-ordinating, giving higher concurrency when there are many waiting threads.
* Commandline: `--innodb-sync-array-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `1024`
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_sync_spin_loops`

* Description: The number of times a thread waits for an InnoDB mutex to be freed before the thread is suspended.
* Commandline: `--innodb-sync-spin-loops=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `30`
* Range: `0` to `4294967295`

#### `innodb_table_locks`

* Description: If [autocommit](innodb-system-variables.md#autocommit) is set to `0` (`1` is default), setting innodb\_table\_locks to `1`, the default, will cause InnoDB to lock a table internally upon a [LOCK TABLE](../../../reference/sql-statements/transactions/lock-tables.md).
* Commandline: `--innodb-table-locks`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_thread_concurrency`

* Description: Once this number of threads is reached (excluding threads waiting for locks), XtraDB/InnoDB will place new threads in a wait state in a first-in, first-out queue for execution, in order to limit the number of threads running concurrently. A setting of `0`, the default, permits as many threads as necessary. A suggested setting is twice the number of CPU's plus the number of disks. Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes).
* Commandline: `--innodb-thread-concurrency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `1000`
* Deprecated: [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_thread_concurrency_timer_based`

* Description: If set to `1`, thread concurrency will be handled in a lock-free timer-based manner rather than the default mutex-based method. Depends on atomic op builtins being available. This Percona XtraDB variable has not been ported to XtraDB 5.6.
* Commandline: `innodb-thread-concurrency-timer-based={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6

#### `innodb_thread_sleep_delay`

* Description: Time in microseconds that InnoDB threads sleep before joining the queue. Setting to `0` disables sleep. Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes)
* Commandline: `--innodb-thread-sleep-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `0` (>= [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes).)
  * `10000` (<= [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes))
* Range: `0` to `1000000`
* Deprecated: [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1055-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_temp_data_file_path`

* Description: Path where to store data for [InnoDB](./) temporary tables. Argument is `filename:size` followed by options separated by ':' Multiple paths can be given separated by ';' A file size is specified (with K for kilobytes, M for megabytes and G for gigabytes). Also whether or not to `autoextend` the data file, `max` size and whether or not to [autoshrink](innodb-tablespaces/innodb-system-tablespaces.md#decreasing-the-size) on startup may also be specified.
* Commandline: `--innodb-temp-data-file-path=path`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `ibtmp1:12M:autoextend`
* Documentation & examples: [innodb-temporary-tablespaces](innodb-tablespaces/innodb-temporary-tablespaces.md)

#### `innodb_tmpdir`

* Description: Allows an alternate location to be set for temporary non-tablespace files. If not set (the default), files will be created in the usual [tmpdir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmpdir) location.\
  Alternate location must be outside of `datadir`
* Commandline: `--innodb-tmpdir=path`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty

#### `innodb_track_changed_pages`

* Description: For faster incremental backup with [Xtrabackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md), XtraDB tracks pages with changes written to them according to the [XtraDB redo log](innodb-redo-log.md) and writes the information to special changed page bitmap files. This read-only variable is used for controlling this feature. See also [innodb\_max\_changed\_pages](innodb-system-variables.md#innodb_max_changed_pages) and [innodb\_max\_bitmap\_file\_size](innodb-system-variables.md#innodb_max_bitmap_file_size). XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-track-changed-pages={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)

#### `innodb_track_redo_log_now`

* Description: Available on debug builds only. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-track-redo-log-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)

#### `innodb_truncate_temporary_tablespace_now`

* Description: Set to ON to shrink the temporary tablespace.
* Commandline: `innodb-truncate-temporary-tablespace-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `innodb_undo_directory`

* Description: Path to the directory (relative or absolute) that InnoDB uses to create separate tablespaces for the [undo logs](innodb-undo-log.md). `.` (the default value before 10.2.2) leaves the undo logs in the same directory as the other log files. From [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes), the default value is NULL, and if no path is specified, undo tablespaces will be created in the directory defined by [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir). Use together with [innodb\_undo\_logs](innodb-system-variables.md#innodb_undo_logs) and [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces). Undo logs are most usefully placed on a separate storage device.
* Commandline: `--innodb-undo-directory=name`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: NULL

#### `innodb_undo_log_truncate`

* Description: When enabled, [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces) that are larger than [innodb\_max\_undo\_log\_size](innodb-system-variables.md#innodb_max_undo_log_size) will be marked for truncation. See also [innodb\_purge\_rseg\_truncate\_frequency](innodb-system-variables.md#innodb_purge_rseg_truncate_frequency). Enabling this setting may cause stalls during heavy write workloads.
* Commandline: `--innodb-undo-log-truncate[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_undo_logs`

* Description: Specifies the number of rollback segments that XtraDB/InnoDB will use within a transaction (or the number of active [undo logs](innodb-undo-log.md)). By default set to the maximum, `128`, it can be reduced to avoid allocating unneeded rollback segments. See the [Innodb\_available\_undo\_logs](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md) status variable for the number of undo logs available. See also [innodb\_undo\_directory](innodb-system-variables.md#innodb_undo_directory) and [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces). Replaced [innodb\_rollback\_segments](innodb-system-variables.md#innodb_rollback_segments) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0). The [Information Schema XTRADB\_RSEG Table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-xtradb-tables/information-schema-xtradb_rseg-table.md) contains information about the XtraDB rollback segments. Deprecated and ignored in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes), as it always makes sense to use the maximum number of rollback segments.
* Commandline: `--innodb-undo-logs=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `128`
* Range: `0` to `128`
* Deprecated: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)
* Removed: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `innodb_undo_tablespaces`

* Description: Number of tablespaces files used for dividing up the [undo logs](innodb-undo-log.md). Zero (the default before [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110)) means that undo logs are all part of the system tablespace, which contains one undo tablespace more than the `innodb_undo_tablespaces` setting. A value of 1 is reset to 0 as 2 or more are needed for separate tablespaces. When the undo logs can grow large, splitting them over multiple tablespaces will reduce the size of any single tablespace. Until [MariaDB 10.11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/what-is-mariadb-114), must be set before InnoDB is initialized, or else MariaDB will fail to start, with an error saying that `InnoDB did not find the expected number of undo tablespaces`. The files are created in the directory specified by [innodb\_undo\_directory](innodb-system-variables.md#innodb_undo_directory), and are named `undoN`, N being an integer. The default size of an undo tablespace is 10MB.From [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110), multiple undo tablespaces are enabled by default, and the default is changed to 3 so that the space occupied by possible bursts of undo log records can be reclaimed after [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate) is set. Before [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106), [innodb\_undo\_logs](innodb-system-variables.md#innodb_undo_logs) must have a non-zero setting for `innodb_undo_tablespaces` to take effect.
* Commandline: `--innodb-undo-tablespaces=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `3` (>= [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110)), `0` (<= [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/what-is-mariadb-1011))
* Range: `0`, or `2` to `95`

#### `innodb_use_atomic_writes`

* Description: Implement atomic writes on supported SSD devices. See [atomic write support](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/atomic-write-support.md) for other variables affected when this is set.
* Commandline: `innodb-use-atomic-writes={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_use_fallocate`

* Description: Preallocate files fast, using operating system functionality. On POSIX systems, posix\_fallocate system call is used.
  * Automatically set to `1` when [innodb\_use\_atomic\_writes](innodb-system-variables.md#innodb_use_atomic_writes) is set - see [FusionIO DirectFS atomic write support](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/atomic-write-support.md).
  * See [InnoDB Page Compression: Saving Storage Space with Sparse Files](innodb-page-compression.md#saving-storage-space-with-sparse-files) for more information.
* Commandline: `innodb-use-fallocate={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes) (treated as if `ON`)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_use_global_flush_log_at_trx_commit`

* Description: Determines whether a user can set the variable [innodb\_flush\_log\_at\_trx\_commit](innodb-system-variables.md#innodb_flush_log_at_trx_commit). If set to `1`, a user cannot reset the value with a SET command, while if set to `1`, a user can reset the value of `innodb_flush_log_at_trx_commit`. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `innodb-use-global-flush-log-at-trx_commit={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_use_mtflush`

* Description: Whether to enable Multi-Threaded Flush operations.\
  For more information, see Fusion.
  * InnoDB's multi-thread flush feature was deprecated in [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes) and removed from [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes). In later versions of MariaDB, use [innodb\_page\_cleaners](innodb-system-variables.md#innodb_page_cleaners) system variable instead.
  * See [InnoDB Page Flushing: Page Flushing with Multi-threaded Flush Threads](innodb-page-flushing.md#page-flushing-with-multi-threaded-flush-threads) for more information.
* Commandline: `--innodb-use-mtflush={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes)
* Removed: [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes)

#### `innodb_use_native_aio`

* Description: For Linux systems only, specified whether to use Linux's asynchronous I/O subsystem. Set to `ON` by default, it may be changed to `0` at startup if InnoDB detects a problem, or from [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1065-release-notes)/[MariaDB 10.7.1](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/storage-engines/innodb/broken-reference/README.md), if a 5.11 - 5.15 Linux kernel is detected, to avoid an io-uring bug/incompatibility ([MDEV-26674](https://jira.mariadb.org/browse/MDEV-26674)). MariaDB-10.6.6/MariaDB-10.7.2 and later also consider 5.15.3+ as a fixed kernel and default to `ON`. To really benefit from the setting, the files should be opened in O\_DIRECT mode ([innodb\_flush\_method=O\_DIRECT](innodb-system-variables.md#innodb_flush_method), default from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106)), to bypass the file system cache. In this way, the reads and writes can be submitted with DMA, using the InnoDB buffer pool directly, and no processor cycles need to be used for copying data.
* Commandline: `--innodb-use-native-aio={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_use_purge_thread`

* Description: Usually with InnoDB, data changed by a transaction is written to an undo space to permit read consistency, and freed when the transaction is complete. Many, or large, transactions, can cause the main tablespace to grow dramatically, reducing performance. This option, introduced in XtraDB 5.1 and removed for 5.5, allows multiple threads to perform the purging, resulting in slower, but much more stable performance.
* Commandline: `--innodb-use-purge-thread=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `32`
* Removed: XtraDB 5.5

#### `innodb_use_stacktrace`

* Description: If set to `ON` (`OFF` is default), a signal handler for SIGUSR2 is installed when the InnoDB server starts. When a long semaphore wait is detected at sync/sync0array.c, a SIGUSR2 signal is sent to the waiting thread and thread that has acquired the RW-latch. For both threads a full stacktrace is produced as well as if possible. XtraDB only. Added as a deprecated and ignored option in [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes) (which uses InnoDB as default instead of XtraDB) to allow for easier upgrades.
* Commandline: `--innodb-use-stacktrace={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_use_sys_malloc`

* Description: If set the `1`, the default, XtraDB/InnoDB will use the operating system's memory allocator. If set to `0` it will use its own. Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) and removed in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) along with InnoDB's internal memory allocator.
* Commandline: `--innodb-use-sys-malloc={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)
* Removed: [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes)

#### `innodb_use_sys_stats_table`

* Description: If set to `1` (`0` is default), XtraDB will use the SYS\_STATS system table for extra table index statistics. When a table is opened for the first time, statistics will then be loaded from SYS\_STATS instead of sampling the index pages. Statistics are designed to be maintained only by running an [ANALYZE TABLE](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-usage/sql-statements/table-statements/analyze-table.md). Replaced by MySQL 5.6's Persistent Optimizer Statistics.
* Commandline: `innodb-use-sys-stats-table={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)/XtraDB 5.6

#### `innodb_use_trim`

* Description: Use trim to free up space of compressed blocks.
  * See [InnoDB Page Compression: Saving Storage Space with Sparse Files](innodb-page-compression.md#saving-storage-space-with-sparse-files) for more information.
* Commandline: `--innodb-use-trim={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)
* Removed: [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1030-release-notes)

#### `innodb_version`

* Description: InnoDB version number. From [MariaDB 10.3.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1037-release-notes), as the InnoDB implementation in MariaDB has diverged from MySQL, the MariaDB version is instead reported. For example, the InnoDB version reported in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) (which is based on MySQL 5.6) included encryption and variable-size page compression before MySQL 5.7 introduced them. [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) (based on MySQL 5.7) introduced persistent AUTO\_INCREMENT ([MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076)) in a GA release before MySQL 8.0. [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) (based on MySQL 5.7) introduced instant ADD COLUMN ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)) before MySQL.
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `innodb_write_io_threads`

* Description: Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), this was simply the number of I/O threads for InnoDB writes. From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), asynchronous I/O functionality in the InnoDB Background Thread Pool replaces the old InnoDB I/O Threads. This variable is now multipled by 256 to determine the maximum number of concurrent asynchronous I/O write requests that can be completed by the Background Thread Pool. The default is therefore 4\*256 = 1024 conccurrent asynchronous write requests. You may on rare occasions need to reduce this default on Linux systems running multiple MariaDB servers to avoid exceeding system limits, or increase if spending too much time waiting on I/O requests.
* Commandline: `--innodb-write-io-threads=#`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/what-is-mariadb-1011)), No (<= [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010))
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `64`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
