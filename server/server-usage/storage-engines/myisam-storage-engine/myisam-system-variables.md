# MyISAM System Variables

This page documents system variables related to the [MyISAM](./) storage engine. For options, see [MyISAM Options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md).

See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `key_buffer_size`

* Description: Size of the buffer for the index blocks used by MyISAM tables and shared for all threads. See [Optimizing key\_buffer\_size](../../../ha-and-performance/optimization-and-tuning/system-variables/optimizing-key_buffer_size.md) for more on selecting the best value.
* Command line: `--key-buffer-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `134217728`
* Range: `8` upwards (upper limit determined by operating system per process limit)

#### `key_cache_age_threshold`

* Description: The lower the setting, the more quickly buffers move from the hot key cache sublist to the warm sublist.
* Command line: `--key-cache-age-threshold=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `300`
* Range: `100` to `4294967295`

#### `key_cache_block_size`

* Description: [MyISAM](./) key cache block size in bytes .
* Command line: `--key-cache-block-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1024`
* Range: `512` to `16384`

#### `key_cache_division_limit`

* Description: Percentage to use for the warm key cache buffer list (the remainder is allocated between the hot and cold caches).
* Command line: `--key-cache-division-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `1` to `100`

#### `key_cache_file_hash_size`

* Description: Number of hash buckets for open and changed files. If you have many MyISAM files open you should increase this for faster flushing of changes. A good value is probably 1/10th of the number of possible open MyISAM files.
* Command line: `--key-cache-file-hash-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `512`
* Range: `128` to `16384`

#### `key_cache_segments`

* Description: The number of segments in a key cache. See [Segmented Key Cache](../../../ha-and-performance/optimization-and-tuning/system-variables/segmented-key-cache.md).
* Command line: `--key-cache-segments=#`
* Scope: Global
* Dynamic: Yes
* Type: numeric
* Default Value: `0` (non-segmented)
* Range: `0` to `64`

#### `myisam_block_size`

* Description: Block size to be used for MyISAM index pages.
* Command line: `--myisam-block-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1024`

#### `myisam_data_pointer_size`

* Description: Size in bytes of the default pointer, used in a [MyISAM](./) [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) with no MAX\_ROWS option.
* Command line: `--myisam-data-pointer-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `6`
* Range: `2` to `7`

#### `myisam_max_extra_sort_file_size`

* Description: Removed in MySQL 5.0.6, was used as a way to force long character keys in large tables to use the key cache method.
* Removed: MySQL 5.0.6

#### `myisam_max_sort_file_size`

* Description: Maximum size in bytes of the temporary file used while recreating a MyISAM index. If the this size is exceeded, the slower process of using the key cache is done instead.
* Command line: `--myisam-max-sort-file-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value - 32 bit: `2147483648`
* Default Value - 64 bit: `9223372036854775807`

#### `myisam_mmap_size`

* Description: Maximum memory in bytes that can be used for memory mapping compressed MyISAM files. Too high a value may result in swapping if there are many compressed MyISAM tables.
* Command line: `--myisam-mmap-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value - 32 bit: `4294967295`
* Default Value - 64 bit: `18446744073709547520`
* Range - 32-bit: `7` to `4294967295`
* Range - 64-bit: `7` to `18446744073709547520`

#### `myisam_recover_options`

* Description: MyISAM recovery mode. Multiple options can be selected, comma-delimited. Using no argument is equivalent to specifying `DEFAULT`, while specifying "" is equivalent to `OFF`. If enabled each time the server opens a MyISAM table, it checks whether it has been marked as crashed, or wasn't closed properly. If so, mysqld will run a check and then attempt to repair the table, writing to the error log beforehand.
  * OFF: No recovery.
  * BACKUP: If the data file is changed while recovering, saves a backup of the .MYD data file. t.MYD are saved as t.MYD-datetime.BAK.
  * BACKUP\_ALL: Same as `BACKUP` but also backs up the .MYI index file. t.MYI are saved as t.MYI-datetime.BAK.
  * DEFAULT: Recovers without backing up, forcing, or quick checking.
  * FORCE: Runs the recovery even if it determines that more than one row from the data file are lost.
  * QUICK: Does not check rows in the table if there are no delete blocks.
* Command line: `--myisam-recover-options[=name]`
* Scope: Global
* Dynamic: No
* Data Type: `enumeration`
* Default Value:
  * `BACKUP,QUICK` (>= [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes))
  * `DEFAULT` (<= [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes))
  * `OFF`
* Valid Values: `OFF`, `DEFAULT`, `BACKUP`, `BACKUP_ALL`, `FORCE` or `QUICK`

#### `myisam_repair_threads`

* Description: If set to more than `1`, the default, MyISAM table indexes each have their own thread during repair and sorting. Increasing from the default will usually result in faster repair, but will use more CPU and memory.
* Command line: `--myisam-repair-threads=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range - 32-bit: `1` to `4294967295`
* Range - 64-bit: `1` to `18446744073709547520`

#### `myisam_sort_buffer_size`

* Description: Size in bytes of the buffer allocated when creating or sorting indexes on a MyISAM table. Increase for better [myisamchk -r, --recover](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md#repairing-tables) performance.
* Command line: `--myisam-sort-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `BIGINT UNSIGNED`                 
* Default Value: `134216704`
* Range: 
  * `(`>= [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes), [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-15-release-notes))`: 4096` to `1152921504606846975`
  * `(<`= [MariaDB 10.11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-4-release-notes), [MariaDB 10.6.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-14-release-notes))`: 4096` to `18446744073709551615`

#### `myisam_stats_method`

* Description: Determines how NULLs are treated for the purposes of [MyISAM](./) index statistics. If set to `nulls_equal`, all NULL index values are treated as a single group. This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful. If set to `nulls_unequal`, the default, the opposite approach is taken, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable. Setting to `nulls_ignored` ignores NULLs altogether from index group calculations. See also [Index Statistics](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/index-statistics.md#dealing-with-nulls), [aria\_stats\_method](../aria/aria-system-variables.md#aria_stats_method), [innodb\_stats\_method](../innodb/innodb-system-variables.md#innodb_stats_method).
* Command line: `--myisam-stats-method=name`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `NULLS_UNEQUAL`
* Valid Values: `NULLS_UNEQUAL, NULLS_EQUAL, NULLS_IGNORED`

#### `myisam_use_mmap`

* Description: If set to `1` (0 is default), memory mapping are used to reading and writing MyISAM tables.
* Command line: `--myisam-use-mmap`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
