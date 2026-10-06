---
description: >-
  Complete guide to InnoDB system variables for MariaDB. Complete reference for
  buffer pool, I/O tuning, transaction settings, and optimization for production
  use.
---

# InnoDB System Variables

This page documents system variables related to the [InnoDB storage engine](./). For options that are not system variables, see [InnoDB Options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md).

See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.

Also see the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `ignore_builtin_innodb`

* Description: Setting this to `1` disables the initialization of the built-in InnoDB storage engine. Usually used in conjunction with the [plugin-load=innodb=ha\_innodb](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option to use the InnoDB plugin.
* Command line: `--ignore-builtin-innodb`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_adaptive_flushing`

* Description: If set to `1`, the default, the server will dynamically adjust the flush rate of dirty pages in the [InnoDB buffer pool](innodb-buffer-pool.md). This assists to reduce brief bursts of I/O activity. If set to `0`, adaptive flushing will only take place when the limit specified by [innodb\_adaptive\_flushing\_lwm](innodb-system-variables.md#innodb_adaptive_flushing_lwm) is reached.
* Command line: `--innodb-adaptive-flushing={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_adaptive_flushing_lwm`

* Description: Adaptive flushing is enabled when this low water mark percentage of the [InnoDB redo log](innodb-redo-log.md) capacity is reached. Takes effect even if [innodb\_adaptive\_flushing](innodb-system-variables.md#innodb_adaptive_flushing) is disabled.
* Command line: `--innodb-adaptive-flushing-lwm=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `double`
* Default Value: `10.000000`
* Range: `0` to `70`

#### `innodb_adaptive_hash_index`

* Description: If set to `1`, the [InnoDB](./) hash index is enabled. Based on performance testing ([MDEV-17492](https://jira.mariadb.org/browse/MDEV-17492)), the InnoDB adaptive hash index helps performance in mostly read-only workloads, and could slow down performance in other environments, especially [DROP TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md), [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md), [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/), or [DROP INDEX](../../../reference/sql-statements/data-definition/drop/drop-index.md) operations. From [MariaDB 13.1.1](https://jira.mariadb.org/browse/MDEV-37070), this variable is an enumeration. The `IF_SPECIFIED` value enables the adaptive hash index only for tables and indexes whose [ADAPTIVE\_HASH\_INDEX](../../../reference/sql-statements/data-definition/create/create-table.md#adaptive_hash_index) option is set to `YES`.
* Command line: `--innodb-adaptive-hash-index[={OFF|ON|IF_SPECIFIED}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration` (`boolean` before [MariaDB 13.1.1](https://jira.mariadb.org/browse/MDEV-37070))
* Valid Values: `OFF`, `ON`, `IF_SPECIFIED` (from [MariaDB 13.1.1](https://jira.mariadb.org/browse/MDEV-37070))
* Default Value: `OFF`

#### **`innodb_adaptive_hash_index_cells`**

* Description: Further improves the performance of the InnoDB adaptive hash index (AHI) when `innodb_adaptive_hash_index` is enabled. This variable allows for manual configuration of the hash table size to resolve contention on the `btr_sea::partition::latch` during high-concurrency workloads. The specified value is effectively multiplied by the number of partitions defined in `innodb_adaptive_hash_index_parts`, as each partition maintains its own hash table. Increasing this value can reduce the length of hash bucket chains, which helps avoid performance "hiccups" and "avalanche effects" caused by multiple threads spinning for AHI lookups.
* Command line: `--innodb-adaptive-hash-index-cells=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `134217728`
* Introduced: [MariaDB 11.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/11.8/11.8.4), [MariaDB 12.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/12.1/12.1.2), [MariaDB 12.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/12.2/12.2.1)

#### `innodb_adaptive_hash_index_parts`

* Description: Specifies the number of partitions for use in adaptive searching. If set to `1`, no extra partitions are created.
* Command line: `innodb-adaptive-hash-index-parts=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `512`

#### `innodb_alter_copy_bulk`

* Description: Allow bulk insert operation for copy alter operation.
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.6), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.5), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.3), [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/11.5.2), [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/11.6.1)

#### `innodb_autoextend_increment`

* Description: Size in MB to increment an auto-extending shared tablespace file when it becomes full. If [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) was set to `1`, this setting does not apply to the resulting per-table tablespace files, which are automatically extended in their own way.
* Command line: `--innodb-autoextend-increment=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `64`
* Range: `1` to `1000`

#### `innodb_autoinc_lock_mode`

* Description: The lock mode that is used when generating [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) values for InnoDB tables.
  * Valid values are:
    * `0` is the traditional lock mode.
    * `1` is the consecutive lock mode.
    * `2` is the interleaved lock mode.
  * In order to use [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/), the lock mode needs to be set to `2`.
  * See [AUTO\_INCREMENT Handling in InnoDB: AUTO\_INCREMENT Lock Modes](auto_increment-handling-in-innodb.md) for more information.
* Command line: `--innodb-autoinc-lock-mode=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `2`

#### `innodb_buf_dump_status_frequency`

* Description: Determines how often (as a percent) the buffer pool dump status should be printed in the logs. For example, `10` means that the buffer pool dump status is printed when every 10% of the number of buffer pool pages are dumped. The default is `0` (only start and end status is printed).
* Command line: `--innodb-buf-dump-status-frequency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `100`

#### `innodb_buffer_pool_chunk_size`

* Description: Chunk size used for dynamically resizing the [buffer pool](innodb-buffer-pool.md). Note that changing this setting can change the size of the buffer pool. When [large-pages](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_pages) is used this value is effectively rounded up to the next multiple of [large-page-size](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_page_size). See [Setting Innodb Buffer Pool Size Dynamically](../../../ha-and-performance/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md). From [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.0), the variable is autosized based on the [buffer pool size](innodb-buffer-pool.md).
* Command line: `--innodb-buffer-pool-chunk-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:
  * `autosize (0)`, resulting in [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size)/64, if [large\_pages](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_pages) round down to multiple of largest page size, with 1MiB minimum (from [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1))
  * `134217728` (until [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.0))
* Range:
  * `0`, as autosize, and then `1048576` to `18446744073709551615` (from [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108))
  * `1048576` to [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size) (until [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107))
* Block size: `1048576`
* Deprecated and ignored from MariaDB 10.11.12, MariaDB 11.4.6, MariaDB 11.8.2

#### `innodb_buffer_pool_dump_at_shutdown`

* Description: Whether to record pages cached in the [buffer pool](innodb-buffer-pool.md) on server shutdown, which reduces the length of the warmup the next time the server starts. The related [innodb\_buffer\_pool\_load\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) specifies whether the buffer pool is automatically warmed up at startup.
* Command line: `--innodb-buffer-pool-dump-at-shutdown={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_buffer_pool_dump_now`

* Description: Immediately records pages stored in the [buffer pool](innodb-buffer-pool.md). The related [innodb\_buffer\_pool\_load\_now](innodb-system-variables.md#innodb_buffer_pool_load_now) does the reverse, and will immediately warm up the buffer pool.
* Command line: `--innodb-buffer-pool-dump-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `innodb_buffer_pool_dump_pct`

* Description: Dump only the hottest N% of each [buffer pool](innodb-buffer-pool.md).
* Command line: `--innodb-buffer-pool-dump-pct={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value:
  * `25`
* Range: `1` to `100`

#### `innodb_buffer_pool_evict`

* Description: Evict pages from the buffer pool. If set to "uncompressed" then all uncompressed pages are evicted from the buffer pool. Variable to be used only for testing. Only exists in DEBUG builds.
* Command line: `--innodb-buffer-pool-evict=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `""`
* Valid Values: "" or "uncompressed"

#### `innodb_buffer_pool_filename`

* Description: The file that holds the [buffer pool](innodb-buffer-pool.md) list of page numbers set by [innodb\_buffer\_pool\_dump\_at\_shutdown](innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown) and [innodb\_buffer\_pool\_dump\_now](innodb-system-variables.md#innodb_buffer_pool_dump_now).
* Command line: `--innodb-buffer-pool-filename=file`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `ib_buffer_pool`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `innodb_buffer_pool_load_abort`

* Description: Aborts the process of restoring [buffer pool](innodb-buffer-pool.md) contents started by [innodb\_buffer\_pool\_load\_at\_startup](innodb-system-variables.md#innodb_buffer_pool_load_at_startup) or [innodb\_buffer\_pool\_load\_now](innodb-system-variables.md#innodb_buffer_pool_load_now).
* Command line: `--innodb-buffer-pool-load-abort={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_buffer_pool_load_at_startup`

* Description: Specifies whether the [buffer pool](innodb-buffer-pool.md) is automatically warmed up when the server starts by loading the pages held earlier. The related [innodb\_buffer\_pool\_dump\_at\_shutdown](innodb-system-variables.md#innodb_buffer_pool_dump_at_shutdown) specifies whether pages are saved at shutdown. If the buffer pool is large and taking a long time to load, increasing [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) at startup may help.
* Command line: `--innodb-buffer-pool-load-at-startup={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_buffer_pool_load_now`

* Description: Immediately warms up the [buffer pool](innodb-buffer-pool.md) by loading the stored data pages. The related [innodb\_buffer\_pool\_dump\_now](innodb-system-variables.md#innodb_buffer_pool_dump_now) does the reverse, and immediately records pages stored in the buffer pool.
* Command line: `--innodb-buffer-pool-load-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_buffer_pool_load_pages_abort`

* Description: Number of pages during a buffer pool load to process before signaling [innodb\_buffer\_pool\_load\_abort=1](innodb-system-variables.md#innodb_buffer_pool_load_abort). Debug builds only.
* Command line: `--innodb-buffer-pool-load-pages-abort=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `9223372036854775807`
* Range: `1` to `9223372036854775807`

#### `innodb_buffer_pool_size`

* Description: InnoDB buffer pool size in bytes. The primary value to adjust on a database server with entirely/primarily [InnoDB](./) tables, can be set up to 80% of the total memory in these environments. See the [InnoDB Buffer Pool](innodb-buffer-pool.md) for more on setting this variable, and also [Setting InnoDB Buffer Pool Size Dynamically](../../../ha-and-performance/optimization-and-tuning/system-variables/setting-innodb-buffer-pool-size-dynamically.md) if doing so dynamically.
* Command line: `--innodb-buffer-pool-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `134217728` (128MiB)
* Range:
  * Minimum: `5242880` (5MiB ) for [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) <= 16k otherwise `25165824` (24MiB) for [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) > 16k (for versions less than next line)
  * Minimum: `2MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 4k, `3MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 8k, `5MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 16k, `10MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 32k, `20MiB` [InnoDB Page Size](innodb-system-variables.md#innodb_page_size) = 64k, (>= [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6), >= [MariaDB 10.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.2))
  * Maximum: `9223372036854775807` (8192PB) (all versions)
* Block size: `1048576`

#### `innodb_buffer_pool_size_auto_min`

* Description: Minimum `innodb_buffer_pool_size` in bytes for dynamic shrinking on memory pressure. Only available on Linux, and on debug builds on other platforms. If a memory pressure event is reported by Linux, the `innodb_buffer_pool_size` may be automatically shrunk towards this value. By default, set to [`innodb_buffer_pool_size_max`](innodb-system-variables.md#innodb_buffer_pool_size_max), that is, memory pressure events will be ignored. `0` sets no minimum value.
* Command line: `--innodb-buffer-pool-size-auto-min=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`, which is replaced at startup by [`innodb_buffer_pool_size_max`](innodb-system-variables.md#innodb_buffer_pool_size_max). A value greater than `innodb_buffer_pool_size_max` is also replaced by it.
* Range: `0` to `18446744073701163008`
* Block size: `8388608` (8 MB on 64-bit systems)
* Introduced: MariaDB 10.11.12, MariaDB 11.4.6, MariaDB 11.8.2

#### `innodb_buffer_pool_size_max`

{% hint style="danger" %}
`innodb_buffer_pool_size_max` is a **read-only** variable, so it can only be set at startup. Attempts to raise [`innodb_buffer_pool_size`](innodb-system-variables.md#innodb_buffer_pool_size) above it at runtime result in _Warning 1292_.
{% endhint %}

{% hint style="info" %}
From MariaDB 10.11.17, 11.4.11, 11.8.7 and 12.3.2, `innodb_buffer_pool_size_max` defaults to 8 TiB of reserved virtual address space on 64-bit systems other than IBM AIX, so the buffer pool can be grown at runtime without configuring anything at startup ([MDEV-38671](https://jira.mariadb.org/browse/MDEV-38671)). Before those releases it defaulted to the initial `innodb_buffer_pool_size` on every system, which meant `SET GLOBAL innodb_buffer_pool_size` could not increase the buffer pool unless `innodb_buffer_pool_size_max` had been set explicitly.
{% endhint %}

{% hint style="warning" %}
Automatic upward dynamic resizing is not implemented ([MDEV-36197](https://jira.mariadb.org/browse/MDEV-36197)). This variable serves only as a pre-allocated virtual address ceiling for **manual** resizing operations.
{% endhint %}

* Description: Maximum `innodb_buffer_pool_size` value. On 64-bit systems other than IBM AIX, the default is 8 TiB, and the minimum 8 MiB. On other systems, the default and minimum are `0`, and the value `0` is replaced with the initial `innodb_buffer_pool_size` rounded up to the allocation unit (2 MiB or 8 MiB). The maximum value is 4GiB-2MiB on 32-bit systems and 16EiB-8MiB on 64-bit systems. This maximum is likely to be limited further by the operating system.\
  On 64-bit systems the default 8 TiB only reserves virtual address space; no memory is committed until the buffer pool actually grows into it. The default is reduced automatically in two cases. If the address-space limit [`RLIMIT_AS`](#user-content-fn-2)[^2] is set and a quarter of it is less than 8 TiB, the default is lowered to that quarter. On architectures whose usable virtual address space can be narrower than 8 TiB — ARM64, RISC-V, MIPS and LoongArch — a failed reservation is retried with 128 GiB, or with the initial `innodb_buffer_pool_size` if that is larger, so that the server can still start. On any other architecture, a failed reservation is a startup error, and a smaller `innodb_buffer_pool_size_max` has to be configured explicitly.
* Command line: `--innodb-buffer-pool-size-max=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8796093022208` (8 TiB) on 64-bit systems other than IBM AIX, from MariaDB 10.11.17, 11.4.11, 11.8.7 and 12.3.2. Otherwise `0`, which is replaced at startup by the initial [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size) rounded up to the block size of that variable. See [the section about buffer pool changes](innodb-buffer-pool.md#buffer-pool-changes).
* Range: `0` to `18446744073701163008`
* Block size: `8388608` (8 MB on 64-bit systems)
* Introduced: MariaDB 10.11.12, MariaDB 11.4.6, MariaDB 11.8.2

#### `innodb_change_buffer_dump`

* Description: If set, causes the contents of the InnoDB change buffer to be dumped to the server error log at startup. Only available in debug builds.
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.2.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.28), [MariaDB 10.3.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.19), [MariaDB 10.4.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.9)

#### `innodb_change_buffer_max_size`

* Description: Maximum size of the [InnoDB Change Buffer](innodb-change-buffering.md) as a percentage of the total buffer pool. The default is 25%, and this can be increased up to 50% for servers with high write activity, and lowered down to 0 for servers used exclusively for reporting.
* Command line: `--innodb-change-buffer-max-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `25`
* Range: `0` to `50`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)
* Deprecated: [MariaDB 10.9.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/10.9.0)
* Removed: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.0)

#### `innodb_change_buffering`

* Description: Sets how [InnoDB](./) change buffering is performed. See [InnoDB Change Buffering](innodb-change-buffering.md) for details on the settings. Deprecated and ignored from [MariaDB 10.9.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/10.9.0).
* Command line: `--innodb-change-buffering=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value:
  * > \= [MariaDB 10.6.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.7), [MariaDB 10.7.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.3), [MariaDB 10.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.2): `none`
  * <= [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6), [MariaDB 10.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.2), [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1):`all`
* Valid Values: `inserts`, `none`, `deletes`, `purges`, `changes`, `all`
* Deprecated: [MariaDB 10.9.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/10.9.0)
* Removed: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.0)

#### `innodb_change_buffering_debug`

* Description: If set to `1`, an [InnoDB Change Buffering](innodb-change-buffering.md) debug flag is set. `1` forces all changes to the change buffer, while `2` causes a crash at merge. `0`, the default, indicates no flag is set. Only available in debug builds.
* Command line: `--innodb-change-buffering-debug=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2`

#### `innodb_checksum_algorithm`

* Description: Specifies how the InnoDB tablespace checksum is generated and verified.
  * `crc32`: A newer, faster algorithm, but incompatible with earlier versions. Tablespace blocks are converted to the new format over time, meaning that a mix of checksums may be present.
  * `full_crc32` and `strict_full_crc32`: Permit encryption to be supported over a [SPATIAL INDEX](../../../reference/sql-structure/geometry/spatial-index.md), which `crc32` does not support. Newly-created data files will carry a flag that indicates that all pages of the file will use a full CRC-32C checksum over the entire page contents (excluding the bytes where the checksum is stored, at the very end of the page). Such files will always use that checksum, no matter what parameter `innodb_checksum_algorithm` is assigned to. Even if `innodb_checksum_algorithm` is modified later, the same checksum will continue to be used. A special flag are set in the FSP\_SPACE\_FLAGS in the first data page to indicate the new format of checksum and encryption/page\_compressed. ROW\_FORMAT=COMPRESSED tables will only use the old format.\
    These tables do not support new features, such as larger innodb\_page\_size or instant ADD/DROP COLUMN. Also cleans up the MariaDB tablespace flags - flags are reserved to store the page\_compressed compression algorithm, and to store the compressed payload length, so that checksum can be computed over the compressed (and possibly encrypted) stream and can be validated without decrypting or decompressing the page. In the full\_crc32 format, there no longer are separate before-encryption and after-encryption checksums for pages. The single checksum is computed on the page contents that is written to the file.See [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026) for details.
  * `strict_crc32` and `strict_full_crc32`: The options are the same as the regular options, but InnoDB will halt if it comes across a mix of checksum values. These are faster, as both new and old checksum values are not required, but can only be used when setting up tablespaces for the first time.
* Command line: `--innodb-checksum-algorithm=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `full_crc32`
* Valid Values: `crc32`, `full_crc32`, `strict_crc32`, `strict_full_crc32`

#### `innodb_cmp_per_index_enabled`

* Description: If set to `ON` (`OFF` is default), per-index compression statistics are stored in the [INFORMATION\_SCHEMA.INNODB\_CMP\_PER\_INDEX](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md) table. These are expensive to record, so this setting should only be changed with care, such as for performance tuning on development or replica servers.
* Command line: `--innodb-cmp-per-index-enabled={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `innodb_compression_algorithm`

* Description: Compression algorithm used for [InnoDB page compression](innodb-page-compression.md). The supported values are:
  * `none`: Pages are not compressed.
  * `zlib`: Pages are compressed using the bundled [zlib](https://www.zlib.net/) compression algorithm.
  * `lz4`: Pages are compressed using the [lz4](https://lz4.org/) compression algorithm.
  * `lzo`: Pages are compressed using the [lzo](https://www.oberhumer.com/opensource/lzo/) compression algorithm.
  * `lzma`: Pages are compressed using the [lzma](https://tukaani.org/xz/) compression algorithm.
  * `bzip2`: Pages are compressed using the [bzip2](http://www.bzip.org/) compression algorithm.
  * `snappy`: Pages are compressed using the [snappy](https://google.github.io/snappy/) algorithm.
  * On many distributions, MariaDB may not support all page compression algorithms by default. From [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107), libraries can be installed as a plugin. See [Compression Plugins](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md).
  * See [InnoDB Page Compression: Configuring the InnoDB Page Compression Algorithm](innodb-page-compression.md#configuring-the-innodb-page-compression-algorithm) for more information.
* Command line: `--innodb-compression-algorithm=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `zlib`
* Valid Values:`none`, `zlib`, `lz4`, `lzo`, `lzma`, `bzip2` or `snappy`

#### `innodb_compression_default`

* Description: Whether or not [InnoDB page compression](innodb-page-compression.md) is enabled by default for new tables.
  * The default value is `OFF`, which means new tables are not compressed.
  * See [InnoDB Page Compression: Enabling InnoDB Page Compression by Default](innodb-page-compression.md#enabling-innodb-page-compression-by-default) for more information.
* Command line: `--innodb-compression-default={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_compression_failure_threshold_pct`

* Description: Specifies the percentage cutoff for expensive compression failures during updates to a table that uses [InnoDB page compression](innodb-page-compression.md), after which free space is added to each new compressed page, dynamically adjusted up to the level set by [innodb\_compression\_pad\_pct\_max](innodb-system-variables.md#innodb_compression_pad_pct_max). Zero disables checking of compression efficiency and adjusting padding.
  * See [InnoDB Page Compression: Configuring the Failure Threshold and Padding](innodb-page-compression.md#configuring-the-failure-threshold-and-maximum-padding) for more information.
* Command line: `--innodb-compression-failure-threshold-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `5`
* Range: `0` to `100`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `innodb_compression_level`

* Description: Specifies the default level of compression for tables that use [InnoDB page compression](innodb-page-compression.md).
  * Only a subset of InnoDB page compression algorithms support compression levels. If an InnoDB page compression algorithm does not support compression levels, then the compression level value is ignored.
  * The compression level can be set to any value between `1` and `9`. The default compression level is `6`. The range goes from the fastest to the most compact, which means that `1` is the fastest and `9` is the most compact.
  * See [InnoDB Page Compression: Configuring the Default Compression Level](innodb-page-compression.md#configuring-the-default-compression-level) for more information.
* Command line: `--innodb-compression-level=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `6`
* Range: `1` to `9`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `innodb_compression_pad_pct_max`

* Description: The maximum percentage of reserved free space within each compressed page for tables that use [InnoDB page compression](innodb-page-compression.md). Reserved free space is used when the page's data is reorganized and might be recompressed. Only used when [innodb\_compression\_failure\_threshold\_pct](innodb-system-variables.md#innodb_compression_failure_threshold_pct) is not zero, and the rate of compression failures exceeds its setting.
  * See [InnoDB Page Compression: Configuring the Failure Threshold and Padding](innodb-page-compression.md#configuring-the-failure-threshold-and-maximum-padding) for more information.
* Command line: `--innodb-compression-pad-pct-max=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `50`
* Range: `0` to `75`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `innodb_data_file_buffering`

* Description: Whether to enable the file system cache for data files. Set to `OFF` by default, are set to `ON` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `fsync`, `littlesync`, `nosync`, or (Windows specific) `normal`.
* Command line: `--innodb-data-file-buffering={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.0)

#### `innodb_data_file_path`

* Description: Individual [InnoDB](./) data files, paths and sizes. The value of [innodb\_data\_home\_dir](innodb-system-variables.md#innodb_data_home_dir) is joined to each path specified by innodb\_data\_file\_path to get the full directory path. If innodb\_data\_home\_dir is an empty string, absolute paths can be specified here. A file size is specified (with K for kilobytes, M for megabytes and G for gigabytes). Also whether or not to `autoextend` the data file, and whether or not to [autoshrink](innodb-tablespaces/innodb-system-tablespaces.md#decreasing-the-size) on startup may also be specified.
* Command line: `--innodb-data-file-path=name`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `ibdata1:12M:autoextend`

#### `innodb_data_file_write_through`

* Description: Whether writes to InnoDB data files (including the temporary tablespace) are write through. Set to `OFF` by default, are set to `ON` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `O_DSYNC`. On systems that support FUA it may make sense to enable write-through, to avoid extra system calls. See [InnoDB Flush Method](innodb-flush-method.md) for a discussion of FUA and write-through behavior.
* Command line: `--innodb-data-file-write-through={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.0)

#### `innodb_data_home_dir`

* Description: Directory path for all [InnoDB](./) data files in the shared tablespace (assuming [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) is not enabled). File-specific information can be added in [innodb\_data\_file\_path](innodb-system-variables.md#innodb_data_file_path), as well as absolute paths if innodb\_data\_home\_dir is set to an empty string.
* Command line: `--innodb-data-home-dir=path`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`
* Default Value: `The MariaDB data directory`

#### `innodb_deadlock_detect`

* Description: By default, the InnoDB deadlock detector is enabled. If set to off, deadlock detection is disabled and MariaDB will rely on [innodb\_lock\_wait\_timeout](innodb-system-variables.md#innodb_lock_wait_timeout) instead. This may be more efficient in systems with high concurrency as deadlock detection can cause a bottleneck when a number of threads have to wait for the same lock.
* Command line: `--innodb-deadlock-detect`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `1`

#### `innodb_deadlock_report`

* Description: How to report deadlocks (if [innodb\_deadlock\_detect=ON](innodb-system-variables.md#innodb_deadlock_detect)).
  * `off`: Do not report any details of deadlocks.
  * `basic`: Report transactions and waiting locks.
  * `full`: Default. Report transactions, waiting locks and blocking locks.
* Command line: `--innodb-deadlock-report=val`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `full`
* Valid Values: `off`, `basic`, `full`
* Introduced: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0)

#### `innodb_default_encryption_key_id`

* Description: ID of encryption key used by default to encrypt InnoDB tablespaces.
  * See [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) and [InnoDB Encryption Keys](../../../security/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md) for more information.
* Command line: `--innodb-default-encryption-key-id=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `4294967295`

#### `innodb_default_row_format`

* Description: Specifies the default [row format](innodb-row-formats/innodb-row-formats-overview.md) to be used for InnoDB tables. The compressed row format cannot be set as the default.
  * See [InnoDB Row Formats Overview: Default Row Format](innodb-row-formats/innodb-row-formats-overview.md#default-row-format) for more information.
* Command line: `--innodb-default-row-format=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `dynamic`
* Valid Values: `redundant`, `compact` or `dynamic`

#### `innodb_defragment`

* Description: When set to `1` (the default is `0`), InnoDB defragmentation is enabled. When set to FALSE, all existing defragmentation are paused and new defragmentation commands will fail. Paused defragmentation commands will resume when this variable is set to true again. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Command line: `--innodb-defragment={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.1)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.0)

#### `innodb_defragment_fill_factor`

* Description:. Indicates how full defragmentation should fill a page. Together with [innodb\_defragment\_fill\_factor\_n\_recs](innodb-system-variables.md#innodb_defragment_fill_factor_n_recs) ensures defragmentation won’t pack the page too full and cause page split on the next insert on every page. The variable indicating more defragmentation gain is the one effective. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Command line: `--innodb-defragment-fill-factor=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `double`
* Default Value: `0.9`
* Range: `0.7` to `1`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.1)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.0)

#### `innodb_defragment_fill_factor_n_recs`

* Description: Number of records of space that defragmentation should leave on the page. This variable, together with [innodb\_defragment\_fill\_factor](innodb-system-variables.md#innodb_defragment_fill_factor), is introduced so defragmentation won't pack the page too full and cause page split on the next insert on every page. The variable indicating more defragmentation gain is the one effective. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Command line: `--innodb-defragment-fill-factor-n-recs=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `20`
* Range: `1` to `100`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.1)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.0)

#### `innodb_defragment_frequency`

* Description: Maximum times per second for defragmenting a single index. This controls the number of times the defragmentation thread can request X\_LOCK on an index. The defragmentation thread will check whether 1/defragment\_frequency (s) has passed since it last worked on this index, and put the index back in the queue if not enough time has passed. The actual frequency can only be lower than this given number. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Command line: `--innodb-defragment-frequency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `integer`
* Default Value: `40`
* Range: `1` to `1000`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.1)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.0)

#### `innodb_defragment_n_pages`

* Description: Number of pages considered at once when merging multiple pages to defragment. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Command line: `--innodb-defragment-n-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `7`
* Range: `2` to `32`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.1)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.0)

#### `innodb_defragment_stats_accuracy`

* Description: Number of defragment stats changes there are before the stats are written to persistent storage. Defaults to zero, meaning disable defragment stats tracking. See [Defragmenting InnoDB Tablespaces](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md).
* Command line: `--innodb-defragment-stats-accuracy=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.1)
* Removed: [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.0)

#### `innodb_disable_sort_file_cache`

* Description: If set to `1` (`0` is default), the operating system file system cache for merge-sort temporary files is disabled.
* Command line: `--innodb-disable-sort-file-cache={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_disallow_writes`

* Description: Tell InnoDB to stop any writes to disk.
* Command line: None
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.3.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.35), [MariaDB 10.4.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.25), [MariaDB 10.5.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.16), [MariaDB 10.6.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.8), [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.4)

#### `innodb_doublewrite`

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From MariaDB 11.0.6:
{% endhint %}

*   Description: If set to `ON`, the default, to improve fault tolerance [InnoDB](./) first stores data to a [doublewrite buffer](innodb-doublewrite-buffer.md) before writing it to data file. Disabling will provide a marginal performance improvement, and assumes that writes of [innodb\_page\_size](innodb-system-variables.md#innodb_page_size) are atomic. `fast` is available from [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.6), and is like `ON`, but writes are not synchronized to data files. The deprecated start-up parameter [innodb\_flush\_method=NO\_FSYNC](innodb-system-variables.md#innodb_flush_method) will cause `innodb_doublewrite=ON` to be changed to `innodb_doublewrite=fast`, which will prevent InnoDB from making any durable writes to data files. This is normally done right before the log checkpoint LSN is updated. Depending on the file systems being used and their configuration, this may or may not be safe.

    The value `innodb_doublewrite=fast` differs from the previous combination of `innodb_doublewrite=ON` and `innodb_flush_method=O_DIRECT_NO_FSYNC` by always invoking `os_file_flush()` on the doublewrite buffer itself in `buf_dblwr_t::flush_buffered_writes_completed()`. This is safer when there are multiple doublewrite batches between checkpoints.

    Typically, once per second, `buf_flush_page_cleaner()` writes out up to `innodb_io_capacity` pages and advance the log checkpoint. Also typically, `innodb_io_capacity`>`128`, which is the size of the doublewrite buffer in pages. If `os_file_flush_func()` is not invoked between doublewrite batches, writes may be reordered in an unsafe way.

    The setting `innodb_doublewrite=fast` can be safe when the doublewrite buffer (the first file of the system tablespace) and the data files reside on the same file system.
* Command line: `--innodb-doublewrite{=val}`, `--skip-innodb-doublewrite`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `fast`
{% endtab %}

{% tab title="< 11.0.6" %}
{% hint style="info" %}
Before MariaDB 11.0.6:
{% endhint %}

* Description: If set to `1`, the default, to improve fault tolerance [InnoDB](./) first stores data to a [doublewrite buffer](innodb-doublewrite-buffer.md) before writing it to data file. Disabling will provide a marginal performance improvement.
* Command line: `--innodb-doublewrite`, `--skip-innodb-doublewrite`
* Scope: Global
* Dynamic:No
* Data Type: `boolean`
* Default Value: `ON`
{% endtab %}
{% endtabs %}

#### `innodb_encrypt_log`

* Description: Enables encryption of the [InnoDB redo log](innodb-redo-log.md). This also enables encryption of some temporary files created internally by InnoDB, such as those used for merge sorts and row logs.
  * See [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) and [Enabling InnoDB Encryption: Enabling Encryption for the Redo Log](../../../security/encryption/data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-the-redo-log) for more information.
* Command line: `--innodb-encrypt-log`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_encrypt_tables`

* Description: Enables automatic encryption of all InnoDB tablespaces.
  * `OFF` - Disables table encryption for all new and existing tables that have the [ENCRYPTED](../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`.
  * `ON` - Enables table encryption for all new and existing tables that have the [ENCRYPTED](../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`, but allows unencrypted tables to be created.
  * `FORCE` - Enables table encryption for all new and existing tables that have the [ENCRYPTED](../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`, and doesn't allow unencrypted tables to be created (`CREATE TABLE ... ENCRYPTED=NO` fails).
  * See [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) and [Enabling InnoDB Encryption: Enabling Encryption for Automatically Encrypted Tablespaces](../../../security/encryption/data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-automatically-encrypted-tablespaces) for more information.
* Command line: `--innodb-encrypt-tables={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Valid Values: `ON`, `OFF`, `FORCE`

#### `innodb_encrypt_temporary_tables`

* Description: Enables automatic encryption of the InnoDB [temporary tablespace](innodb-tablespaces/innodb-temporary-tablespaces.md).
  * See [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) and [InnoDB Enabling Encryption: Enabling Encryption for Temporary Tablespaces](../../../security/encryption/data-at-rest-encryption/innodb-encryption/innodb-enabling-encryption.md#enabling-encryption-for-temporary-tablespaces) for more information.
* Command line: `--innodb-encrypt-temporary-tables={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Valid Values: `ON`, `OFF`
* Introduced: [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.26), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.17), [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.7)

#### `innodb_encryption_rotate_key_age`

* Description: Re-encrypt in background any page having a key older than this number of key versions. When setting up encryption, this variable must be set to a non-zero value. Otherwise, when you enable encryption through [innodb\_encrypt\_tables](innodb-system-variables.md#innodb_encrypt_tables) MariaDB won't be able to automatically encrypt any unencrypted tables.
  * See [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) and [InnoDB Encryption Keys: Key Rotation](../../../security/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md#key-rotation) for more information.
* Command line: `--innodb-encryption-rotate-key-age=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `4294967295`

#### `innodb_encryption_rotation_iops`

* Description: Use this many iops for background key rotation operations performed by the background encryption threads.
  * See [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) and [InnoDB Encryption Keys: Key Rotation](../../../security/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md#key-rotation) for more information.
* Command line: `--innodb-encryption-rotation_iops=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `0` to `4294967295`

#### `innodb_encryption_threads`

* Description: Number of background encryption threads performing background key rotation and [scrubbing](innodb-data-scrubbing.md). When setting up encryption, this variable must be set to a non-zero value. Otherwise, when you enable encryption through [innodb\_encrypt\_tables](innodb-system-variables.md#innodb_encrypt_tables) MariaDB won't be able to automatically encrypt any unencrypted tables. Recommended never be set higher than 255.
  * See [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-tde-fundamentals.md) and [InnoDB Background Encryption Threads](../../../security/encryption/data-at-rest-encryption/innodb-encryption/innodb-background-encryption-threads.md) for more information.
* Command line: `--innodb-encryption-threads=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `255`

#### `innodb_fast_shutdown`

* Description: The shutdown mode:
  * `0` - InnoDB performs a slow shutdown, including full purge and change buffer merge. Can be very slow, even taking hours in extreme cases.
  * `1` - the default, [InnoDB](./) performs a fast shutdown, not performing a full purge or an insert buffer merge.
  * `2`, the [InnoDB redo log](innodb-redo-log.md) is flushed and a cold shutdown takes place, similar to a crash. The resulting startup then performs crash recovery. Extremely fast, in cases of emergency, but risks corruption. Not suitable for upgrades between major versions!
  * `3` - active transactions will not be rolled back, but all changed pages are written to data files. The active transactions are rolled back by a background thread on a subsequent startup. The fastest option that will not involve [InnoDB redo log](innodb-redo-log.md) apply on subsequent startup. See [MDEV-15832](https://jira.mariadb.org/browse/MDEV-15832).
* Command line: `--innodb-fast-shutdown[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `3`

#### `innodb_fatal_semaphore_wait_threshold`

* Description: In MariaDB, the fatal semaphore timeout is configurable. This variable sets the maximum number of seconds for semaphores to time out in InnoDB.
* Command line: `--innodb-fatal-semaphore-wait-threshold=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `600`
* Range: `1` to `4294967295`

#### `innodb_file_per_table`

* Description: If set to `ON`, then new [InnoDB](./) tables are created with their own [InnoDB file-per-table tablespaces](innodb-tablespaces/innodb-file-per-table-tablespaces.md). If set to `OFF`, then new tables are created in the [InnoDB system tablespace](innodb-tablespaces/innodb-system-tablespaces.md) instead. [Page compression](innodb-page-compression.md) is only available with file-per-table tablespaces. Note that this value is also used when a table is re-created with an [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) which requires a table copy. Deprecated in [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110) as there's no benefit to setting to `OFF`, the original InnoDB default.
* Command line: `--innodb-file-per-table`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Deprecated: [MariaDB 11.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.1)

#### `innodb_fill_factor`

* Description: Percentage of B-tree page filled during bulk insert (sorted index build). Used as a hint rather than an absolute value. Setting to `70`, for example, reserves 30% of the space on each B-tree page for the index to grow in future.
* Command line: `--innodb-fill-factor=#`
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

* Description: Set to `1`, along with [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) for the greatest level of fault tolerance.
  * `1` The default, the log buffer is written to the [InnoDB redo log](innodb-redo-log.md) file and a flush to disk performed after each transaction. This is required for full ACID[^3] compliance.
  * `0` Nothing is done on commit; rather the log buffer is written and flushed to the [InnoDB redo log](innodb-redo-log.md) once a second. This gives better performance, but a server crash can erase the last second of transactions.
  * `2` The log buffer is written to the [InnoDB redo log](innodb-redo-log.md) after each commit, but flushing takes place every [innodb\_flush\_log\_at\_timeout](innodb-system-variables.md#innodb_flush_log_at_timeout) seconds (by default once a second). Performance is slightly better, but a OS or power outage can cause the last second's transactions to be lost.
  * `3` The log buffer is written to the [InnoDB redo log](innodb-redo-log.md) file and flushed to disk at both the prepare and the commit phase of each transaction. This is slower than `1`, and the extra flush at prepare is usually redundant. Like `1`, it guarantees that after a crash, committed transactions are not lost and remain consistent with the binary log and other transactional engines. See [Binlog group commit and innodb\_flush\_log\_at\_trx\_commit](binary-log-group-commit-and-innodb-flushing-performance.md).
* Command line: `--innodb-flush-log-at-trx-commit[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `1`
* Valid Values: `0`, `1`, `2` or `3`

**Note**: When the [InnoDB-based Binary Log](../../../ha-and-performance/standard-replication/innodb-based-binary-log.md) is enabled (`--binary-storage-engine=innodb`), this option manages the durability of commits for both binlog files and InnoDB table data. Also, in this configuration, there is no separate binlog `fsync` step and no two-phase commit between InnoDB and the binary log.

#### `innodb_flush_method`

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From MariaDB 11.0:
{% endhint %}

* Description: [InnoDB](./) flushing method. **Deprecated from** [**MariaDB 11.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110)**.** The variable can still be set, but the preferred way to control flushing behavior is to use `SET GLOBAL` on the four replacement Boolean dynamic parameters, which can be changed while the server is running:
  * [innodb\_log\_file\_buffering](innodb-system-variables.md#innodb_log_file_buffering) (enable file system cache on the InnoDB write-ahead log; added in 10.8.4, 10.9.2)
  * [innodb\_data\_file\_buffering](innodb-system-variables.md#innodb_data_file_buffering) (enable file system cache on data files)
  * [innodb\_log\_file\_write\_through](innodb-system-variables.md#innodb_log_file_write_through) (enable write-through on the log)
  * [innodb\_data\_file\_write\_through](innodb-system-variables.md#innodb_data_file_write_through) (enable write-through on persistent data files)
* For the full discussion of buffering, write-through, FUA, and the flag names used as values, see [InnoDB Flush Method](innodb-flush-method.md) and [Storage I/O: Buffering and Persistence](../../../ha-and-performance/optimization-and-tuning/operating-system-optimizations/storage-io-buffering-and-persistence.md).
* When `innodb_flush_method` is set, the value is translated into the four Boolean parameters as follows:
  * `O_DSYNC`: [innodb\_log\_file\_write\_through=ON](innodb-system-variables.md#innodb_log_file_write_through), [innodb\_data\_file\_write\_through=ON](innodb-system-variables.md#innodb_data_file_write_through), [innodb\_data\_file\_buffering=OFF](innodb-system-variables.md#innodb_data_file_buffering), and (if supported) [innodb\_log\_file\_buffering=OFF](innodb-system-variables.md#innodb_log_file_buffering).
  * `fsync`, `littlesync`, `nosync`, or (on Windows) `normal`: [innodb\_log\_file\_write\_through=OFF](innodb-system-variables.md#innodb_log_file_write_through), [innodb\_data\_file\_write\_through=OFF](innodb-system-variables.md#innodb_data_file_write_through), and [innodb\_data\_file\_buffering=ON](innodb-system-variables.md#innodb_data_file_buffering).
* Command line: `--innodb-flush-method=name`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value:
  * `O_DIRECT` (Unix, >= MariaDB 10.6.0)
* Valid Values:
  * Unix: `fsync`, `O_DSYNC`, `littlesync`, `nosync`, `O_DIRECT`, `O_DIRECT_NO_FSYNC`
  * Windows: `unbuffered`, `async_unbuffered`, `normal`
* Deprecated: [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110)
{% endtab %}

{% tab title="< 11.0" %}
{% hint style="info" %}
Before MariaDB 11.0:
{% endhint %}

* Description: [InnoDB](./) flushing method. Windows always uses `async_unbuffered`, meaning that this variable has no effect. Adjusting this variable can give performance improvements, but behavior differs widely on different filesystems. Changing from the default value may cause problems in some situations, so test and benchmark carefully before adjusting. In MariaDB, Windows recognizes and correctly handles the Unix methods, but if no methods are specified, it uses its own default – unbuffered write (analog of `O_DIRECT`) plus syncs (for instance, `FileFlushBuffers()`) for all files.
* A detailed description of the variable and its effects can be found [on this page](innodb-flush-method.md).
  * `O_DSYNC` is used to open and flush logs, and `fsync()` to flush the data files.
  * `O_DIRECT` is used to open data files, and `fsync()` to flush data and logs. This is the default on Unix from MariaDB 10.6.
  * `O_DIRECT_NO_FSYNC` uses `O_DIRECT` during flushing I/O, but skips `fsync()` afterwards. Not suitable for XFS filesystems. Generally not recommended over `O_DIRECT`, as it does not get the benefit of [innodb\_use\_native\_aio=ON](innodb-system-variables.md#innodb_use_native_aio).
  * `unbuffered` - Windows-only default
  * `async_unbuffered` - Windows-only, alias for `unbuffered`
  * `normal` - Windows-only, alias for `fsync`
  * `littlesync` - for internal testing only
  * `nosync` - for internal testing only
* Command line: `--innodb-flush-method=name`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value:
  * `O_DIRECT` (Unix, >= MariaDB 10.6.0)
* Valid Values:
  * Unix: `fsync`, `O_DSYNC`, `littlesync`, `nosync`, `O_DIRECT`, `O_DIRECT_NO_FSYNC`
  * Windows: `unbuffered`, `async_unbuffered`, `normal`
{% endtab %}
{% endtabs %}

#### `innodb_flush_neighbors`

* Description: Determines whether flushing a page from the [buffer pool](innodb-buffer-pool.md) will flush other dirty pages in the same group of pages (extent). In high write environments, if flushing is not aggressive enough, it can fall behind resulting in higher memory usage, or if flushing is too aggressive, cause excess I/O activity. SSD devices, with low seek times, would be less likely to require dirty neighbor flushing to be set. An attempt is made under Windows and Linux to determine SSD status. This variable is ignored for table spaces that are detected as stored on SSD (and the `0` behavior applies).
  * `1`: The default, flushes contiguous dirty pages in the same extent from the buffer pool.
  * `0`: No other dirty pages are flushed.
  * `2`: Flushes dirty pages in the same extent from the buffer pool.
* Command line: `--innodb-flush-neighbors=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `1`
* Valid Values: `0`, `1`, `2`

#### `innodb_flush_sync`

* Description: If set to `ON`, the default, the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) setting is ignored for I/O bursts occurring at checkpoints.
* Command line: `--innodb-flush-sync={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_flushing_avg_loops`

* Description: Determines how quickly adaptive flushing will respond to changing workloads. The value is the number of iterations that a previously calculated flushing state snapshot is kept. Increasing the value smooths and slows the rate that the flushing operations change, while decreasing it causes flushing activity to spike quickly in response to workload changes.
* Command line: `--innodb-flushing-avg-loops=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `30`
* Range: `1` to `1000`

#### `innodb_force_load_corrupted`

* Description: Set to `0` by default, if set to `1`, [InnoDB](./) are permitted to load tables marked as corrupt. Only use this to recover data you can't recover any other way, or in troubleshooting. Always restore to `0` when the returning to regular use. Given that [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412) aims to allow any metadata for a missing or corrupted table to be dropped, and given that [MDEV-17567](https://jira.mariadb.org/browse/MDEV-17567) and [MDEV-25506](https://jira.mariadb.org/browse/MDEV-25506) and related tasks made DDL operations crash-safe, the parameter no longer serves any purpose and was removed in [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6).
* Command line: `--innodb-force-load-corrupted`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Removed: [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6)

#### `innodb_force_primary_key`

* Description: If set to `1` (`0` is default) CREATE TABLEs without a primary or unique key where all keyparts are NOT NULL will not be accepted, and will return an error.
* Command line: `--innodb-force-primary-key`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_force_recovery`

* Description: [InnoDB](./) crash recovery mode. `0` is the default. The other modes are for recovery purposes only, and no data can be changed while another mode is active. Some queries relying on indexes are also blocked. See [InnoDB Recovery Modes](innodb-troubleshooting/innodb-recovery-modes.md) for more on mode specifics.
* Command line: `--innodb-force-recovery=#`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value: `0`
* Range: `0` to `6`

#### `innodb_ft_aux_table`

* Description: Diagnostic variable intended only to be set at runtime. It specifies the qualified name (for example `test/ft_innodb`) of an InnoDB table that has a [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), and after being set the INFORMATION\_SCHEMA tables [INNODB\_FT\_INDEX\_TABLE](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_index_table-table.md), [INNODB\_FT\_INDEX\_CACHE](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_index_cache-table.md), INNODB\_FT\_CONFIG, [INNODB\_FT\_DELETED](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_deleted-table.md), and [INNODB\_FT\_BEING\_DELETED](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_ft_being_deleted-table.md) will contain search index information for the specified table.
* Command line: `--innodb-ft-aux-table=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_ft_cache_size`

* Description: Cache size available for a parsed document while creating an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/).
* Command line: `--innodb-ft-cache-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8000000`

#### `innodb_ft_enable_diag_print`

* Description: If set to `1`, additional [full-text](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) search diagnostic output is enabled.
* Command line: `--innodb-ft-enable-diag-print={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_ft_enable_stopword`

* Description: If set to `1`, the default, a set of [stopwords](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) is associated with an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) when it is created. The stopword list comes from the table set by the session variable [innodb\_ft\_user\_stopword\_table](innodb-system-variables.md#innodb_ft_user_stopword_table), if set, otherwise the global variable [innodb\_ft\_server\_stopword\_table](innodb-system-variables.md#innodb_ft_server_stopword_table), if that is set, or the [built-in list](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-stopwords.md) if neither variable is set.
* Command line: `--innodb-ft-enable-stopword={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_ft_max_token_size`

* Description: Maximum length of words stored in an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). A larger limit will increase the size of the index, slowing down queries, but permit longer words to be searched for. In most normal situations, longer words are unlikely search terms.
* Command line: `--innodb-ft-max-token-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `84`
* Range: `10` to `84`

#### `innodb_ft_min_token_size`

* Description: Minimum length of words stored in an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). A smaller limit will increase the size of the index, slowing down queries, but permit shorter words to be searched for. For data stored in a Chinese, Japanese or Korean [character set](../../../reference/data-types/string-data-types/character-sets/), a value of 1 should be specified to preserve functionality.
* Command line: `--innodb-ft-min-token-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `3`
* Range: `1` to `16`

#### `innodb_ft_num_word_optimize`

* Description: Number of words processed during each [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) on an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). To ensure all changes are incorporated, multiple OPTIMIZE TABLE statements could be run in case of a substantial change to the index.
* Command line: `--innodb-ft-num-word-optimize=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2000`
* Range: `1000` to `10000`

#### `innodb_ft_result_cache_limit`

* Description: Limit in bytes of the InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) query result cache per fulltext query. The latter stages of the full-text search are handled in memory, and limiting this prevents excess memory usage. If the limit is exceeded, the query returns an error.
* Command line: `--innodb-ft-result-cache-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2000000000`
* Range: `1000000` to `18446744073709551615`

#### `innodb_ft_server_stopword_table`

* Description: Table name containing a list of stopwords to ignore when creating an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), in the format db\_name/table\_name. The specified table must exist before this option is set, and must be an InnoDB table with a single column, a [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) named VALUE. See also [innodb\_ft\_enable\_stopword](innodb-system-variables.md#innodb_ft_enable_stopword).
* Command line: `--innodb-ft-server-stopword-table=db_name/table_name`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty

#### `innodb_ft_sort_pll_degree`

* Description: Number of parallel threads used when building an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/). See also [innodb\_sort\_buffer\_size](innodb-system-variables.md#innodb_sort_buffer_size).
* Command line: `--innodb-ft-sort-pll-degree=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `2`
* Range: `1` to `32`

#### `innodb_ft_total_cache_size`

* Description:Total memory allocated for the cache for all InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) tables. A force sync is triggered if this limit is exceeded.
* Command line: `--innodb-ft-total-cache-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `640000000`
* Range: `32000000` to `1600000000`
* Introduced: [MariaDB 10.0.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.9)

#### `innodb_ft_user_stopword_table`

* Description: Table name containing a list of stopwords to ignore when creating an InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), in the format db\_name/table\_name. The specified table must exist before this option is set, and must be an InnoDB table with a single column, a [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) named VALUE. See also [innodb\_ft\_enable\_stopword](innodb-system-variables.md#innodb_ft_enable_stopword).
* Command line: `--innodb-ft-user-stopword-table=db_name/table_name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty

#### `innodb_immediate_scrub_data_uncompressed`

* Description: Enable scrubbing of data. See [Data Scrubbing](innodb-data-scrubbing.md).
* Command line: `--innodb-immediate-scrub-data-uncompressed={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_index_shrink`

* Description: Whether InnoDB may shrink a B-tree, by merging or reorganizing pages, on an `UPDATE` that grows a record, such as one that changes a value from `NULL` to not-`NULL`. The default `ON` matches the behavior of earlier releases. Setting this to `OFF` makes InnoDB favor page splits in those cases, which reduces index tree latch upgrades and the contention they cause, at the cost of slightly sparser pages.
* Command line: `--innodb-index-shrink={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 11.8.9](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.9), [MariaDB 12.3.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/12.3.3)

#### `innodb_instant_alter_column_allowed`

* Description:
  * If a table is altered using `ALGORITHM=INSTANT`, it can force the table to use a non-canonical format: A hidden metadata record at the start of the clustered index is used to store each column's `DEFAULT` value. This makes it possible to add new columns that have default values without rebuilding the table. A `BLOB` in the hidden metadata record is used to store column mappings. This makes
    it possible to drop or reorder columns without rebuilding the table. This also makes it possible to add columns to any position or drop columns from any position in the table without rebuilding the table. If a column is dropped without rebuilding the table, old records will contain garbage in that column's former position, and new records are written with `NULL` values, empty strings, or dummy values.
  * This is generally not a problem. However, there may be cases where
    you want to avoid putting a table into this format. For example, to ensure that future `UPDATE` operations after an `ADD COLUMN` are performed in-place, to reduce write amplification. (Instantly added columns are essentially always variable-length.) Also avoid bugs similar to [MDEV-19916](https://jira.mariadb.org/browse/MDEV-19916), or to be able to export tables to older versions of the server.
  * This variable has been introduced as a result, with the following values:
  * `never` (0): Do not allow instant add/drop/reorder, to maintain format compatibility with MariaDB 10.x and MySQL 5.x. If the table (or partition) is not in the canonical format, then any ALTER TABLE (even one that does not involve instant column operations) will force a table rebuild.
  * `add_last` (1): Store a hidden metadata record that
    allows columns to be appended to the table instantly ([MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)).\
    If the table (or partition) is not in this format, then any ALTER TABLE (even one that does not involve column changes)
    will force a table rebuild.
  * `add_drop_reorder` (2, default): Like 'add\_last', but allow the metadata record to store a column map, to support instant
    add/drop/reorder of columns.
* Command line: `--innodb-instant-alter-column-allowed=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Valid Values: `never`, `add_last`, `add_drop_reorder`
* Default Value: `add_drop_reorder`
* Introduced: [MariaDB 10.3.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.23), [MariaDB 10.4.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.13), [MariaDB 10.5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.3)

#### `innodb_io_capacity`

* Description: Limit on I/O activity for InnoDB background tasks, including merging data from the insert buffer and flushing pages. Should be set to around the number of I/O operations per second that system can handle, based on the type of drive/s being used. You can also set it higher when the server starts to help with the extra workload at that time, and then reduce for normal use. Ideally, opt for a lower setting, as at higher value data is removed from the buffers too quickly, reducing the effectiveness of caching. See also [innodb\_flush\_sync](innodb-system-variables.md#innodb_flush_sync).
  * See [InnoDB Page Flushing: Configuring the InnoDB I/O Capacity](innodb-page-flushing.md#configuring-the-innodb-i-o-capacity) for more information.
* Command line: `--innodb-io-capacity=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `200`
* Range: `100` to `4294967295` (2<sup>32</sup>-1)

#### `innodb_io_capacity_max`

* Description: Upper limit to which InnoDB can extend [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) in case of emergency. See [InnoDB Page Flushing: Configuring the InnoDB I/O Capacity](innodb-page-flushing.md#configuring-the-innodb-i-o-capacity) for more information.
* Command line: `--innodb-io-capacity-max=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `2000` or twice [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity), whichever is higher.
* Range : `100` to `4294967295` (2<sup>32</sup>-1)

#### `innodb_lock_wait_timeout`

* Description: Time in seconds that an InnoDB transaction waits for an InnoDB record lock (or table lock) before giving up with the error `ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction`. When this occurs, the statement (not transaction) is rolled back. The whole transaction can be rolled back if the [innodb\_rollback\_on\_timeout](innodb-system-variables.md#innodb_rollback_on_timeout) option is used. Increase this for data warehousing applications or where other long-running operations are common, or decrease for OLTP and other highly interactive applications. This setting does not apply to deadlocks, which InnoDB detects immediately, rolling back a deadlocked transaction. `0` means no wait. See [WAIT and NOWAIT](../../../reference/sql-statements/transactions/wait-and-nowait.md). Setting to `100000000` or more (from [MariaDB 10.6.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.3), `100000000` is the maximum) means the timeout is infinite.
* Command line: `--innodb-lock-wait-timeout=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `INT UNSIGNED` (>= [MariaDB 10.6.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.3)), `BIGINT UNSIGNED` (<= [MariaDB 10.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.2))
* Default Value: `50`
* Range:
  * `0` to `100000000` (>= [MariaDB 10.6.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.3))
  * `0` to `1073741824` (<= [MariaDB 10.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.2))

#### `innodb_log_archive`

* Description: Controls the InnoDB log archiving format. When set to `ON`, the InnoDB write-ahead log is written to a sequence of files named `ib_`_`lsn`_`.log` instead of the circular ring buffer (`ib_logfile0`). Each file is pre-allocated to [`innodb_log_file_size`](innodb-system-variables.md#innodb_log_file_size); when one fills up, the server creates and pre-allocates the next file. After the first checkpoint completes in a new file, the previous file is marked read-only, signaling that it can be moved to long-term storage. This format makes a continuous log history available, which is necessary for point-in-time recovery and incremental backups.
* Details:
  * File Naming: Archive files use the naming convention `ib_`_`lsn`_`.log`, where _lsn_ is a 16-character hexadecimal representation of the Log Sequence Number (LSN) at offset 12288 (0x3000) of the file.
  * Log Resizing: When archiving is enabled, changes to [`innodb_log_file_size`](innodb-system-variables.md#innodb_log_file_size) take effect when the current log file is filled and a new file is allocated. This differs from the standard resizing logic used when `innodb_log_archive` is `OFF`.
  * Encryption: While `innodb_log_archive` is `ON`, the value of [`innodb_encrypt_log`](innodb-system-variables.md#innodb_encrypt_log) and related encryption parameters cannot be changed. To change encryption, set `innodb_log_archive=OFF` and restart the server — this permanently discards the archived log history.
  * Startup: With `innodb_log_archive=ON`, the server refuses to start if `ib_logfile0` exists in the data directory.
  * Data Dictionary: This feature tracks InnoDB changes only. It does not cover `.frm` files or other non-InnoDB metadata.
  * Backup tooling: No shipped tool yet generates or restores backups in this format. [`mariadb-backup`](../../backup-and-restore/mariadb-backup/) only supports the legacy `ib_logfile0` format and fails when the server is running with `innodb_log_archive=ON`.
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: MariaDB 13.0

#### `innodb_log_buffer_size`

* Description: Size in bytes of the buffer for writing [InnoDB redo log](innodb-redo-log.md) files to disk. Increasing this means larger transactions can run without needing to perform disk I/O before committing.
* Command line: `--innodb-log-buffer-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `16777216` (16MB)
* Range: `262144` to `2147479552` (256KB to 2GB - 4K) (>= [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.8))
* Range: `262144` to `18446744073709551615` (<= [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.7)) - limit to the above maximum because this is an operating system limit.
* Block size: `4096`

#### `innodb_log_checkpoint_now`

* Description: Write back dirty pages from the [buffer pool](innodb-buffer-pool.md) and update the log checkpoint. Prior to [MariaDB 10.11.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.12), [MariaDB 11.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.6), [MariaDB 11.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.2) was only available in debug builds. Introduced in order to force checkpoints before a backup, allowing mariadb-backup to create much smaller incremental backups. However, this comes at the cost of heavy I/O usage and it is now disabled by default.
* Command line: `--innodb-log-checkpoint{=1|0}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.11.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.12), [MariaDB 11.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.6), [MariaDB 11.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.2)

#### `innodb_log_file_buffering`

* Description: Whether the file system cache for ib\_logfile0 is enabled. In [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.3), MariaDB disabled the file system cache on the InnoDB write-ahead log file (ib\_logfile0) by default on Linux. With [innodb\_flush\_trx\_log\_at\_commit=2](innodb-system-variables.md#innodb_flush_log_at_trx_commit) in particular, writing to the log via the file system cache typically improves throughput, especially on slow storage or at a small number of concurrent transactions. For other values of innodb\_flush\_log\_at\_trx\_commit, direct writes were observed to be mostly but not always faster. Whether it pays off to disable the file system cache on the log may depend on the type of storage, the workload, and the operating system kernel version. If the server is started up with [innodb\_flush\_log\_at\_trx\_commit=2](innodb-system-variables.md#innodb_flush_log_at_trx_commit), the value are changed to `ON`. Will be set to `OFF` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `O_DSYNC`. On Linux, when the physical block size cannot be determined to be a power of 2 between 64 and 4096 bytes, the file system cache cannot be disabled, and innodb\_log\_file\_buffering=ON cannot be changed. Linux and Windows only.
* Command line: `--innodb-log-file-buffering={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.8/10.8.4), [MariaDB 10.9.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.9/10.9.2)

{% hint style="info" %}
A change requested with `SET GLOBAL innodb_log_file_buffering` takes effect only when InnoDB is holding a single log file open, which is the case most of the time. It is ignored while a `SET GLOBAL innodb_log_file_size` resize is in progress on a circular-format log (`ib_logfile0`). From MariaDB 13.0 ([MDEV-39862](https://jira.mariadb.org/browse/MDEV-39862)), it is also ignored while a log file switch is in progress with [`innodb_log_archive`](innodb-system-variables.md#innodb_log_archive) set to `ON`, because InnoDB then has more than one log file open; when this occurs, and how long it lasts, is hard to predict, as it depends on `innodb_log_file_size` and the workload. The setting also has no effect when the log is mapped to persistent memory (PMEM).

Because the request can be silently ignored, confirm that it took effect by reading the value back:

```sql
SELECT @@GLOBAL.innodb_log_file_buffering;
```
{% endhint %}

#### `innodb_log_file_mmap`

* Description: Whether ib\_logfile0 resides in persistent memory or should initially be memory-mapped. When using the default innodb\_log\_buffer\_size=2m, mariadb-backup --backup would spend a lot of time re-reading and re-parsing the log. For reading the log file during mariadb-backup --backup, it is beneficial to memory-map the entire ib\_logfile0 to the address space (typically 48 bits or 256 TiB) and read it from there,
  both during --backup and --prepare. OFF by default on most platforms, to avoid aggressive read-ahead of the entire ib\_logfile0 in when only a tiny portion would be accessed. On Linux and FreeBSD the default is innodb\_log\_file\_mmap=ON, because those platforms define a specific mmap(2) option for enabling such read-ahead and therefore it can be assumed that the default wouldbe on-demand paging. This parameter will only have impact on the initial InnoDB startup and recovery. Any writes to the log will use regular I/O, except when the ib\_logfile0 is stored in a specially configured file system that is backed by persistent memory (Linux "mount -o dax").
* Command line: `--innodb-log-file-mmap{=0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON` (Linux, FreeBSD), `OFF` (Other platforms)
* Introduced: [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.10), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.6), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.4), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/11.6.2), [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.7/11.7.1)

#### `innodb_log_file_size`

* Description: Size in bytes of each [InnoDB redo log](innodb-redo-log.md) file in the log group. The combined size can be no more than 512GB. Larger values mean less disk I/O due to less flushing checkpoint activity, but also slower recovery from a crash. Crash recovery doesn't run out of memory, so it can safely be set higher to reduce checkpoint flushing, even larger than [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size).From [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109) the variable is dynamic, and the server no longer needs to be restarted for the resizing to take place. Unless the log is located in a persistent memory file system (PMEM), an attempt to [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) innodb\_log\_file\_size to less than [innodb\_log\_buffer\_size](innodb-system-variables.md#innodb_log_buffer_size) are refused. Log resizing can be aborted by killing the connection that is executing the SET GLOBAL statement.
* Command line: `--innodb-log-file-size=#`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109)), No (<= [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108))
* Data Type: `numeric`
* Default Value: `100663296` (96MB)
* Range:
  * > \= [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.3): `4194304` to `512GB` (4MB to 512GB)
  * <= [MariaDB 10.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.2): `1048576` to `512GB` (1MB to 512GB)
* Block size: `4096`

#### `innodb_log_file_write_through`

* Description: Whether each write to ib\_logfile0 is write through (disabling any caching, as in O\_SYNC or O\_DSYNC). Set to `OFF` by default, are set to `ON` if [innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is set to `O_DSYNC`. On systems that support FUA it may make sense to enable write-through, to avoid extra system calls. See [InnoDB Flush Method](innodb-flush-method.md) for a discussion of FUA and write-through behavior.
* Command line: `--innodb-log-file-write-through={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.0)

{% hint style="info" %}
A change requested with `SET GLOBAL innodb_log_file_write_through` takes effect only when InnoDB is holding a single log file open, which is the case most of the time. It is ignored while a `SET GLOBAL innodb_log_file_size` resize is in progress on a circular-format log (`ib_logfile0`). From MariaDB 13.0 ([MDEV-39862](https://jira.mariadb.org/browse/MDEV-39862)), it is also ignored while a log file switch is in progress with [`innodb_log_archive`](innodb-system-variables.md#innodb_log_archive) set to `ON`, because InnoDB then has more than one log file open; when this occurs, and how long it lasts, is hard to predict, as it depends on `innodb_log_file_size` and the workload. The setting also has no effect when the log is mapped to persistent memory (PMEM).

Because the request can be silently ignored, confirm that it took effect by reading the value back:

```sql
SELECT @@GLOBAL.innodb_log_file_write_through;
```
{% endhint %}

#### `innodb_log_group_home_dir`

* Description: Path to the [InnoDB redo log](innodb-redo-log.md) files. If none is specified, a redo log file named `ib_logfile0`, with a size of [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size), is created in the data directory.
* Command line: `--innodb-log-group-home-dir=path`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`

#### `innodb_log_recovery_start`

* Description: Specifies the Log Sequence Number (LSN) at which the recovery process begins. Only meaningful when recovering a backup that contains log files in the [`innodb_log_archive`](innodb-system-variables.md#innodb_log_archive)`=ON` format.
* Usage: Set this variable to limit the scope of a recovery operation. The server expects to find an optional sequence of `FILE_MODIFY` records followed by a `FILE_CHECKPOINT` record at the specified _lsn_. This is typically used when restoring a backup, by setting the variable to the LSN that points to the start checkpoint of the backup.
* Special value: `0` (the default) means start recovery from the latest completed checkpoint. The latest checkpoint is guaranteed to live in one of the last two `ib_`_`lsn`_`.log` files in the data directory, typically the last one.
* Property: Set at startup
* Data Type: `numeric` (64-bit unsigned integer)
* Default Value: `0`
* Introduced: MariaDB 13.0

#### `innodb_log_recovery_target`

* Description: Specifies the target Log Sequence Number (LSN) at which the recovery process ends. Only meaningful when recovering a backup that contains log files in the [`innodb_log_archive`](innodb-system-variables.md#innodb_log_archive)`=ON` format.
* Usage: Use this variable to define a recovery point objective. The server replays archived logs up to the specified _lsn_ and stops. When this variable is non-zero, all persistent InnoDB tables become read-only and no log writes are allowed.
* Special value: `0` (the default) performs an unlimited recovery — the server replays the log to its end.
* Property: Set at startup
* Data Type: `numeric` (64-bit unsigned integer)
* Default Value: `0`
* Introduced: MariaDB 13.0

{% hint style="warning" %}
**No data file may carry an LSN newer than `innodb_log_recovery_target`.** Crash recovery's role is to bring every database page to the same logical point in time (the same LSN). If any data file is newer than the target, recovery completes in an inconsistent state where some pages carry an LSN past the requested target — that is, the database is corrupted. The server cannot validate every such impossible target, and the resulting corruption may not be detected until the affected pages are accessed (see [MDEV-34830](https://jira.mariadb.org/browse/MDEV-34830)). Choose a target that lies at or beyond the highest page LSN you intend to retain.

If you set a target that is unreachable in the other direction (for example, lower than the current checkpoint), the server terminates with an error message containing the available LSN range.
{% endhint %}

#### `innodb_log_spin_wait_delay`

* Description: Delay between log buffer spin lock polls (0 to use a blocking latch). Specifically, enables a spin lock that will execute that many MY\_RELAX\_CPU() operations (such as the x86 PAUSE instruction) between successive attempts of acquiring the spin lock. On some hardware with certain workloads (observed on write intensive workloads on NUMA[^1] systems), the default setting results in a significant amount of time being spent in native\_queued\_spin\_lock\_slowpath() in the Linux kernel, plus context switching between user and kernel address space, in which case changing from the default (for example, setting to `50`), may result in a performance improvement.
* Command line: `--innodb-log-spin-wait-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `6000`
* Introduced: [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.8), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.6), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.5), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.4), [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.2), [MariaDB 11.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/11.5.1)

#### `innodb_log_write_ahead_size`

* Description: [InnoDB redo log](innodb-redo-log.md) write ahead unit size to avoid read-on-write. Should match the OS cache block IO size. Removed in [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108), and instead on Linux and Windows, the physical block size of the underlying storage is detected and used. Reintroduced in [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9) and later versions. On Linux and Windows, the default or the specified innodb\_log\_write\_ahead\_size are automatically adjusted to not be less than the physical block size (if it can be determined).
* Command line: `--innodb-log-write-ahead-size=#`
* Scope: Global
* Dynamic: No (>= [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9)), Yes (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107))
* Data Type: `numeric`
* Default Value: `512` (>= [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9)), `8192` (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107))
* Range:
  * `512` to `4096` (>= [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9))
  * `512` to [innodb\_page\_size](innodb-system-variables.md#innodb_page_size) (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107))
* Removed: [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108)
* Re-introduced: [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.6), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.5), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.3), [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/11.5.2)

#### `innodb_lru_flush_size`

* Description: Number of pages to flush on LRU eviction. Changes in [MariaDB 10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.18), [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.8), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.6), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.5), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.4) and [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.2) made this setting superfluous, and it is no longer used.
* Command line: `--innodb-lru-flush-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `0 (>=`[MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.20), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.10), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.6), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.4). [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/11.6.1), [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.7/11.7.1))
  * `32 (<=` [MariaDB 10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.19), [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.5), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.3))
* Range: `1` to `18446744073709551615`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.7)
* Deprecated: [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.20), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.10), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.6) and [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.4). [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/11.6.1), [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.7/11.7.1)

#### `innodb_lru_scan_depth`

* Description: Specifies how far down the buffer pool least-recently used (LRU) list the cleaning thread should look for dirty pages to flush. This process is performed once a second. In an I/O intensive-workload, can be increased if there is spare I/O capacity, or decreased if in a write-intensive workload with little spare I/O capacity.
  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Command line: `--innodb-lru-scan-depth=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1536`
* Range - 32bit: `100` to `2^32-1`
* Range - 64bit: `100` to `2^64-1`

#### `innodb_max_dirty_pages_pct`

* Description: Maximum percentage of unwritten (dirty) pages in the buffer pool.
  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Command line: `--innodb-max-dirty-pages-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `90.000000`
* Range: `0` to `99.999`

#### `innodb_max_dirty_pages_pct_lwm`

* Description: Low water mark percentage of dirty pages that will enable preflushing to lower the dirty page ratio. The value 0 (default) means 'refer to [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct)'.
  * See [InnoDB Page Flushing](innodb-page-flushing.md) for more information.
* Command line: `--innodb-max-dirty-pages-pct-lwm=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `99.999`

#### `innodb_max_purge_lag`

* Description: When purge operations are lagging on a busy server, setting innodb\_max\_purge\_lag can help. By default set to `0`, no lag, the figure is used to calculate a time lag for each INSERT, UPDATE, and DELETE when the system is lagging. InnoDB keeps a list of transactions with delete-marked index records due to UPDATE and DELETE statements. The length of this list is `purge_lag`, and the calculation, performed every ten seconds, is as follows: ((purge\_lag/innodb\_max\_purge\_lag)×10)–5 microseconds.
* Command line: `--innodb-max-purge-lag=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`

#### `innodb_max_purge_lag_delay`

* Description: Maximum delay in milliseconds imposed by the [innodb\_max\_purge\_lag](innodb-system-variables.md#innodb_max_purge_lag) setting. If set to `0`, the default, there is no maximum.
* Command line: `--innodb-max-purge-lag-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`

#### `innodb_max_purge_lag_wait`

* Description: Wait until History list length is below the specified limit.
* Command line: `--innodb-max-purge-wait=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4294967295`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.7), [MariaDB 10.4.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.16), [MariaDB 10.3.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.26), [MariaDB 10.2.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.35)

#### `innodb_max_undo_log_size`

* Description: If an undo tablespace is larger than this, it is marked for truncation if [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate) is set.
* Command line: `--innodb-max-undo-log-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value:
  * `10485760`
* Range: `10485760` to `18446744073709551615`

#### `innodb_monitor_disable`

* Description: Disables the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Command line: `--innodb-monitor-disable=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_monitor_enable`

* Description: Enables the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Command line: `--innodb-monitor-enable=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_monitor_reset`

* Description: Resets the count value of the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table to zero.
* Command line: `--innodb-monitor-reset=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_monitor_reset_all`

* Description: Resets all values for the specified counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table.
* Command line: `---innodb-monitor-reset-all=string`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`

#### `innodb_numa_interleave`

* Description: Whether or not to use the NUMA[^1] interleave memory policy to allocate the [InnoDB buffer pool](innodb-buffer-pool.md).
* Command line: `innodb-numa-interleave={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Availability: Only in builds compiled with NUMA support (`WITH_NUMA`). Official MariaDB release packages are built without it ([MDEV-18954](https://jira.mariadb.org/browse/MDEV-18954)).

#### `innodb_old_blocks_pct`

* Description: Percentage of the [buffer pool](innodb-buffer-pool.md) to use for the old block sublist.
* Command line: `--innodb-old-blocks-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `37`
* Range: `5` to `95`

#### `innodb_old_blocks_time`

* Description: Time in milliseconds an inserted block must stay in the old sublist after its first access before it can be moved to the new sublist. '0' means "no delay". Setting a non-zero value can help prevent full table scans clogging the [buffer pool](innodb-buffer-pool.md). See also [innodb\_old\_blocks\_pct](innodb-system-variables.md#innodb_old_blocks_pct).
* Command line: `--innodb-old-blocks-time=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000`
* Range: `0` to `2^32-1`

#### `innodb_online_alter_log_max_size`

* Description: The maximum size for temporary log files during online DDL (data and index structure changes). The temporary log file is used for each table being altered, or index being created, to store data changes to the table while the process is underway. The table is extended by [innodb\_sort\_buffer\_size](innodb-system-variables.md#innodb_sort_buffer_size) up to the limit set by this variable. If this limit is exceeded, the online DDL operation fails and all uncommitted changes are rolled back. A lower value reduces the time a table could lock at the end of the operation to apply all the log's changes, but also increases the chance of the online DDL changes failing.
* Command line: `--innodb-online-alter-log-max-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `134217728`
* Range: `65536` to `2^64-1`

#### `innodb_open_files`

* Description: Maximum .ibd files MariaDB can have open at the same time. Only applies to systems with multiple XtraDB/InnoDB tablespaces, and is separate to the table cache and [open\_files\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit). The default, if [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) is disabled, is 300 or the value of [table\_open\_cache](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache), whichever is higher. It will also auto-size up to the default value if it is set to a value less than `10`.
* Command line: `--innodb-open-files=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `autosized`
* Range: `10` to `4294967295`

#### `innodb_optimize_fulltext_only`

* Description: When set to `1` (`0` is default), [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) will only process InnoDB [FULLTEXT index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) data. Only intended for use during fulltext index maintenance.
* Command line: `--innodb-optimize-fulltext-only={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_page_size`

* Description: Specifies the page size in bytes for all InnoDB tablespaces. The default, `16k`, is suitable for most uses.
  * A smaller InnoDB page size might work more effectively in a situation with many small writes (OLTP), or with SSD storage, which usually has smaller block sizes.
  * A larger InnoDB page size can provide a larger [maximum row size](innodb-row-formats/innodb-row-formats-overview.md#maximum-row-size).
  * InnoDB's page size can be as large as `64k` for tables using the following [row formats](innodb-row-formats/innodb-row-formats-overview.md): [DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md), [COMPACT](innodb-row-formats/innodb-compact-row-format.md), and [REDUNDANT](innodb-row-formats/innodb-redundant-row-format.md).
  * InnoDB's page size must still be `16k` or less for tables using the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format.
  * This system variable's value cannot be changed after the `datadir` has been initialized. InnoDB's page size is set when a MariaDB instance starts, and it remains constant afterwards.
* Command line: `--innodb-page-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value: `16384`
* Valid Values: `4k` or `4096`, `8k` or `8192`, `16k` or `16384`, `32k` and `64k`.

#### `innodb_prefix_index_cluster_optimization`

* Description: Enable prefix optimization to sometimes avoid cluster index lookups. Deprecated and ignored from [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010), as the optimization is now always enabled.
* Command line: `--innodb-prefix-index-cluster-optimization={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Deprecated: [MariaDB 10.10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.1)

#### `innodb_print_all_deadlocks`

* Description: If set to `1` (`0` is default), all InnoDB transaction deadlock information is written to the [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Command line: `--innodb-print-all-deadlocks={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_purge_batch_size`

* Description: Number of [InnoDB undo log](innodb-undo-log.md) pages to purge in one batch from the history list. Together with [innodb\_purge\_threads](innodb-system-variables.md#innodb_purge_threads) has a small effect on tuning.
* Command line: `--innodb-purge-batch-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:
  * `127` (>= [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.20), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.10), [MariaDB 11.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.6), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.4), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/11.6.2))
  * `1000` (>= [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.16), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.7), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.6), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.4), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.3) [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.2))
  * `300` (<= [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.15), [MariaDB 10.10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.6), [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.5), [MariaDB 11.0.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.3), [MariaDB 11.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.2) [MariaDB 11.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.1))
* Range: `1` to `5000`

#### `innodb_purge_rseg_truncate_frequency`

* Description: Frequency with which undo records are purged. Set by default to every 128 times, reducing this increases the frequency at which rollback segments are freed. See also [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate). The motivation for introducing this in MySQL seems to have been to avoid stalls due to freeing undo log pages or truncating undo log tablespaces. In MariaDB, [innodb\_undo\_log\_truncate=ON](innodb-system-variables.md#innodb_undo_log_truncate) should be a much lighter operation because it will not involve any log checkpoint, hence this is deprecated and ignored from [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.16), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.7), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.6), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.4), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.3) and [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.2). ([MDEV-32050](https://jira.mariadb.org/browse/MDEV-32050))
* Command line: `-- innodb-purge-rseg-truncate-frequency=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `128`
* Range: `1` to `128`
* Deprecated: [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.16), [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.7), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.6), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/11.0.4), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.3), [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.2)

#### `innodb_purge_threads`

* Description: Number of background threads dedicated to InnoDB purge operations. The range is `1` to `32`. At least one background thread is always used. Setting to a value greater than 1 creates that many separate purge threads. This can improve efficiency in some cases, such as when performing DML operations on many tables. See also [innodb\_purge\_batch\_size](innodb-system-variables.md#innodb_purge_batch_size).
* Command line: `--innodb-purge-threads=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `32`

#### `innodb_random_read_ahead`

* Description: Enables random read-ahead, an optimization technique that InnoDB does not use by default, if set to `1`. The default is `0`.
* Command line: `--innodb-random-read-ahead={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_read_ahead_threshold`

* Description: Minimum number of pages InnoDB must read sequentially from an extent of 64 before initiating an asynchronous read for the following extent.
* Command line: `--innodb-read-ahead-threshold=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `56`
* Range: `0` to `64`

#### `innodb_read_io_threads`

* Description: InnoDB read requests are completed by asynchronous I/O in the InnoDB Background Thread Pool. This variable is multiplied by 256 to determine the maximum number of concurrent asynchronous I/O read requests that can be completed by the Background Thread Pool. The default is therefore 4\*256 = 1024 conccurrent asynchronous read requests. You may on rare occasions need to reduce this default on Linux systems running multiple MariaDB servers to avoid exceeding system limits, or increase if spending too much time waiting on I/O requests.
* Command line: `--innodb-read-io-threads=#`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011)), No (<= [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010))
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `64`

#### `innodb_read_only`

* Description: If set to `1` (`0` is default), the server are read-only. For use in distributed applications, data warehouses or read-only media.
* Command line: `--innodb-read-only={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_read_only_compressed`

* Description: If set (the default before [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6)), [ROW\_FORMAT=COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) tables are read-only. This was intended to be the first step towards removing write support and deprecating the feature, but this plan has been abandoned.
* Command line: `--innodb-read-only-compressed`, `--skip-innodb-read-only-compressed`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF` (>= [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6)), `ON` (<= [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.5))
* Introduced: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0)

#### `innodb_rollback_on_timeout`

* Description: InnoDB usually rolls back the last statement of a transaction that's been timed out (see [innodb\_lock\_wait\_timeout](innodb-system-variables.md#innodb_lock_wait_timeout)). If innodb\_rollback\_on\_timeout is set to 1 (0 is default), InnoDB will roll back the entire transaction.
* Command line: `--innodb-rollback-on-timeout`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `0`

#### `innodb_snapshot_isolation`

* Description: Whether or not to use snapshot isolation (write/write conflict detection within InnoDB).\
  If enabled (set to `ON`), an error `DB_RECORD_CHANGED` (`HA_ERR_RECORD_CHANGED`, [`ER_CHECKREAD`](../../../reference/error-codes/mariadb-error-codes-1000-to-1099/e1020.md)) is raised if an attempt is made to acquire a lock on a record that does not exist in the current read view. This error is treated in the same way as a deadlock, and the transaction is rolled back. This affects the default isolation level, [REPEATABLE READ](../../../reference/sql-statements/transactions/transactions-repeatable-read.md).\
  In MariaDB 11.8 and later, changes to snapshot handling may affect how conflicts are detected in transactions that use the [Repeatable Read](../../../reference/sql-statements/transactions/transactions-repeatable-read.md) isolation level. Specifically, `DELETE` and `UPDATE` statements can cause a rollback of the transaction, and return with [ERROR 1020](../../../reference/error-codes/mariadb-error-codes-1000-to-1099/e1020.md). This occurs when a transaction tries to modify rows using a snapshot that is inconsistent with the database's current state as a result of simultaneous modifications. In other words, this variable is designed to prevent non-repeatable reads and anomalies (like lost updates) by rejecting `UPDATE` or `DELETE` operations on rows that were modified by a concurrent transaction after the current transaction's snapshot was taken.
* Command line: `--innodb-snapshot-isolation={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON` (>= MariaDB 11.6.2), `OFF` (<= MariaDB 11.6.1)
* Introduced: MariaDB 10.6.18, MariaDB 10.11.8, MariaDB 11.0.6, MariaDB 11.1.5, MariaDB 11.2.4, MariaDB 11.4.2

#### `innodb_sort_buffer_size`

* Description: Size of the sort buffers used for sorting data when an InnoDB index is created, as well as the amount by which the temporary log file is extended during online DDL operations to record concurrent writes. The larger the setting, the fewer merge phases are required between buffers while sorting. When a [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) creates a new index, three buffers of this size are allocated, as well as pointers for the rows in the buffer.
* Command line: `--innodb-sort-buffer-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1048576` (1M)
* Range: `65536` to `67108864`

#### `innodb_spin_wait_delay`

* Description: Maximum delay (not strictly corresponding to a time unit) between spin lock polls. The default, `4`, was verified to give the best throughput by OLTP update index and read-write benchmarks on Intel Broadwell (2/20/40) and ARM (1/46/46).
* Command line: `--innodb-log-spin-wait-delay=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4`
* Range: `0` to `4294967295`

#### `innodb_stats_auto_recalc`

* Description: If set to `1` (the default), persistent statistics are automatically recalculated when the table changes significantly (more than 10% of the rows). Affects tables created or altered with STATS\_PERSISTENT=1 (see [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) ), or when [innodb\_stats\_persistent](innodb-system-variables.md#innodb_stats_persistent) is enabled. [innodb\_stats\_persistent\_sample\_pages](innodb-system-variables.md#innodb_stats_persistent_sample_pages) determines how much data to sample when recalculating. See [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Command line: `--innodb-stats-auto-recalc={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

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
* Command line: `--innodb-stats-method=name`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `nulls_equal`
* Valid Values: `nulls_equal`, `nulls_unequal`, `nulls_ignored`

#### `innodb_stats_modified_counter`

* Description: The number of rows modified before we calculate new statistics. If set to `0`, the default, current limits are used.
* Command line: `--innodb-stats-modified-counter=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`

#### `innodb_stats_on_metadata`

* Description: If set to `ON`, XtraDB/InnoDB updates statistics when accessing the INFORMATION\_SCHEMA.TABLES or INFORMATION\_SCHEMA.STATISTICS tables, and when running metadata statements such as [SHOW INDEX](../../../reference/sql-statements/administrative-sql-statements/show/show-index.md) or [SHOW TABLE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md). If set to `OFF` (the default), statistics are not updated at those times, which can reduce the access time for large schemas, as well as make execution plans more stable.
* Command line: `--innodb-stats-on-metadata`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_stats_persistent`

* Description: [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md) produces index statistics, and this setting determines whether they are stored on disk, or be required to be recalculated more frequently, such as when the server restarts. This information is stored for each table, and can be set with the STATS\_PERSISTENT clause when creating or altering tables (see [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md)). See [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Command line: `--innodb-stats-persistent={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_stats_persistent_sample_pages`

* Description: Number of index pages sampled when estimating cardinality and statistics for indexed columns. Increasing this value will increases index statistics accuracy, but use more I/O resources when running [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md). See [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Command line: `--innodb-stats-persistent-sample-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `20`

#### `innodb_stats_traditional`

* Description: This system variable affects how the number of pages to sample for transient statistics is determined, in particular how [innodb\_stats\_transient\_sample\_pages](innodb-system-variables.md#innodb_stats_transient_sample_pages) is used.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is enabled, then the exact number of pages configured by the system variable are sampled for statistics.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * This system variable does not affect the calculation of [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md).
* Command line: `--innodb-stats-traditional={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_stats_transient_sample_pages`

* Description: Gives control over the index distribution statistics by determining the number of index pages to sample. Higher values produce more disk I/O, but, especially for large tables, produce more accurate statistics and therefore make more effective use of the query optimizer. Lower values than the default are not recommended, as the statistics can be quite inaccurate.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is enabled, then the exact number of pages configured by this system variable are sampled for statistics.
  * If [innodb\_stats\_traditional](innodb-system-variables.md#innodb_stats_traditional) is disabled, then the number of pages to sample for statistics is calculated using a logarithmic algorithm, so the exact number can change depending on the size of the table. This means that more samples may be used for larger tables.
  * If [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled, then the [innodb\_stats\_persistent\_sample\_pages](innodb-system-variables.md#innodb_stats_persistent_sample_pages) system variable applies instead. [persistent statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) are enabled with the [innodb\_stats\_persistent](innodb-system-variables.md#innodb_stats_persistent) system variable.
* Command line: `--innodb-stats-transient-sample-pages=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `8`
* Range: `1` to `2^64-1`

#### `innodb_status_output`

* Description: Enable [InnoDB monitor](innodb-monitors.md) output to the [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Command line: `--innodb-status-output={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_status_output_locks`

* Description: Enable [InnoDB lock monitor](innodb-monitors.md) output to the [error log](../../../server-management/server-monitoring-logs/error-log.md) and [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md). Also requires [innodb\_status\_output=ON](innodb-system-variables.md#innodb_status_output) to enable output to the error log.
* Command line: `--innodb-status-output-locks={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_strict_mode`

* Description: If set to `1` (the default), InnoDB will return errors instead of warnings in certain cases, similar to strict SQL mode. See [InnoDB Strict Mode](innodb-strict-mode.md) for details.
* Command line: `--innodb-strict-mode={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_sync_spin_loops`

* Description: The number of times a thread waits for an InnoDB mutex to be freed before the thread is suspended.
* Command line: `--innodb-sync-spin-loops=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `30`
* Range: `0` to `4294967295`

#### `innodb_table_locks`

* Description: If [autocommit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is set to `0` (`1` is default), setting innodb\_table\_locks to `1`, the default, will cause InnoDB to lock a table internally upon a [LOCK TABLE](../../../reference/sql-statements/transactions/lock-tables.md).
* Command line: `--innodb-table-locks`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_tablespace_size_warning_pct`

* Description: Percentage of [innodb\_tablespace\_size\_warning\_threshold](innodb-system-variables.md#innodb_tablespace_size_warning_threshold) at which InnoDB starts emitting tablespace size warnings to the [error log](../../../server-management/server-monitoring-logs/error-log.md) as a tablespace grows. Once a tablespace reaches this percentage, a warning is written on each further one-percent increase, up to 100%. Has no effect when the threshold is `0`.
* Command line: `--innodb-tablespace-size-warning-pct=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `85`
* Range: `0` to `100`
* Introduced: MariaDB 13.1

#### `innodb_tablespace_size_warning_threshold`

* Description: Size threshold in bytes at which InnoDB begins emitting tablespace size warnings to the [error log](../../../server-management/server-monitoring-logs/error-log.md) as a tablespace file grows. `0`, the default, disables the warnings entirely (no overhead). The percentage of this threshold at which warnings start is controlled by [innodb\_tablespace\_size\_warning\_pct](innodb-system-variables.md#innodb_tablespace_size_warning_pct). Warnings are emitted per tablespace and tracked individually, resetting when the tablespace is truncated or dropped, or when either variable is changed. The warning message has the form `Tablespace '<name>' size <N> bytes reached <P>% of configured threshold of <T> bytes`.
* Command line: `--innodb-tablespace-size-warning-threshold=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `18446744073709551615`
* Introduced: MariaDB 13.1

#### `innodb_temp_data_file_path`

* Description: Path where to store data for [InnoDB](./) temporary tables. Argument is `filename:size` followed by options separated by ':' Multiple paths can be given separated by ';' A file size is specified (with K for kilobytes, M for megabytes and G for gigabytes). Also whether or not to `autoextend` the data file, `max` size and whether or not to [autoshrink](innodb-tablespaces/innodb-system-tablespaces.md#decreasing-the-size) on startup may also be specified.
* Command line: `--innodb-temp-data-file-path=path`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: `ibtmp1:12M:autoextend`
* Documentation & examples: [innodb-temporary-tablespaces](innodb-tablespaces/innodb-temporary-tablespaces.md)

#### `innodb_tmpdir`

* Description: Allows an alternate location to be set for temporary non-tablespace files. If not set (the default), files are created in the usual [tmpdir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmpdir) location.\
  Alternate location must be outside of `datadir`
* Command line: `--innodb-tmpdir=path`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: Empty

#### `innodb_truncate_temporary_tablespace_now`

* Description: Set to ON to shrink the temporary tablespace.
* Command line: `innodb-truncate-temporary-tablespace-now={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/11.3.0)

#### `innodb_undo_directory`

* Description: Path to the directory (relative or absolute) that InnoDB uses to create separate tablespaces for the [undo logs](innodb-undo-log.md). The default value is NULL: if no path is specified, undo tablespaces are created in the directory defined by [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir). `.` leaves the undo logs in the same directory as the other log files. Use together with [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces). Undo logs are most usefully placed on a separate storage device.
* Command line: `--innodb-undo-directory=name`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: NULL

#### `innodb_undo_log_truncate`

* Description: When enabled, [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces) that are larger than [innodb\_max\_undo\_log\_size](innodb-system-variables.md#innodb_max_undo_log_size) are marked for truncation. See also [innodb\_purge\_rseg\_truncate\_frequency](innodb-system-variables.md#innodb_purge_rseg_truncate_frequency). Enabling this setting may cause stalls during heavy write workloads.
* Command line: `--innodb-undo-log-truncate[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `innodb_undo_tablespaces`

* Description: Number of tablespaces files used for dividing up the [undo logs](innodb-undo-log.md). Zero (the default before [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110)) means that undo logs are all part of the system tablespace, which contains one undo tablespace more than the `innodb_undo_tablespaces` setting. A value of 1 is reset to 0 as 2 or more are needed for separate tablespaces. When the undo logs can grow large, splitting them over multiple tablespaces will reduce the size of any single tablespace. Until [MariaDB 10.11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114), must be set before InnoDB is initialized, or else MariaDB will fail to start, with an error saying that `InnoDB did not find the expected number of undo tablespaces`. The files are created in the directory specified by [innodb\_undo\_directory](innodb-system-variables.md#innodb_undo_directory), and are named `undoN`, N being an integer. The default size of an undo tablespace is 10MB.From [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110), multiple undo tablespaces are enabled by default, and the default is changed to 3 so that the space occupied by possible bursts of undo log records can be reclaimed after [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate) is set.
* Command line: `--innodb-undo-tablespaces=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `3` (>= [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110)), `0` (<= [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011))
* Range: `0`, or `2` to `95`

#### `innodb_use_atomic_writes`

* Description: Implement atomic writes on supported SSD devices. See [atomic write support](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/atomic-write-support.md) for other variables affected when this is set.
* Command line: `innodb-use-atomic-writes={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_use_native_aio`

* Description: For Linux systems only, specified whether to use Linux's asynchronous I/O subsystem. Set to `ON` by default, it may be changed to `0` at startup if InnoDB detects a problem, or from [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.5)/[MariaDB 10.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.1), if a 5.11 - 5.15 Linux kernel is detected, to avoid an io-uring bug/incompatibility ([MDEV-26674](https://jira.mariadb.org/browse/MDEV-26674)). MariaDB-10.6.6/MariaDB-10.7.2 and later also consider 5.15.3+ as a fixed kernel and default to `ON`. To really benefit from the setting, the files should be opened in O\_DIRECT mode ([innodb\_flush\_method=O\_DIRECT](innodb-system-variables.md#innodb_flush_method), default from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/what-is-mariadb-106)), to bypass the file system cache. In this way, the reads and writes can be submitted with DMA, using the InnoDB buffer pool directly, and no processor cycles need to be used for copying data.
* Command line: `--innodb-use-native-aio={0|1}`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `innodb_version`

* Description: InnoDB version number. As the InnoDB implementation in MariaDB has diverged from MySQL, the MariaDB version is reported instead.
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `innodb_write_io_threads`

* Description: InnoDB write requests are completed by asynchronous I/O in the InnoDB Background Thread Pool. This variable is multiplied by 256 to determine the maximum number of concurrent asynchronous I/O write requests that can be completed by the Background Thread Pool. The default is therefore 4\*256 = 1024 conccurrent asynchronous write requests. You may on rare occasions need to reduce this default on Linux systems running multiple MariaDB servers to avoid exceeding system limits, or increase if spending too much time waiting on I/O requests.
* Command line: `--innodb-write-io-threads=#`
* Scope: Global
* Dynamic: Yes (>= [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011)), No (<= [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010))
* Data Type: `numeric`
* Default Value: `4`
* Range: `1` to `64`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: NUMA (Non-Uniform Memory Access): A hardware architecture where a processor accesses its own local memory faster than non-local memory, requiring database optimization for efficiency.

[^2]: RLIMIT\_AS stands for Resource Limit: Address Space. It is one of the "ulimits" (user limits) that a system administrator can set to prevent a single process from going rogue.

[^3]: ACID compliance refers to a set of properties—Atomicity, Consistency, Isolation, and Durability—that ensure database transactions are processed reliably and maintain data integrity.\
    Atomicity guarantees that a transaction is treated as a single, indivisible unit, where all operations succeed or the entire transaction is rolled back.\
    Consistency ensures that a transaction brings the database from one valid state to another, adhering to all defined rules and constraints.\
    Isolation mandates that concurrent transactions do not interfere with each other, preserving data accuracy during simultaneous operations.\
    Durability ensures that once a transaction is committed, its changes are permanently stored and survive system failures such as crashes or power outages.\
    These properties are essential for mission-critical applications in industries like banking, healthcare, and e-commerce, where data accuracy and reliability are paramount.\
    While ACID compliance enhances data integrity and user confidence, it can impact performance, particularly under high load, due to the overhead of maintaining strict consistency and concurrency control.\
    Some modern systems, such as data warehouses, may relax isolation requirements to improve read performance, though they still typically maintain atomicity, consistency, and durability.
