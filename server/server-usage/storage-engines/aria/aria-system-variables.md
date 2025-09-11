# Aria System Variables

This page documents system variables related to the [Aria storage engine](./). For options that are not system variables, see [Aria Options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md).

See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for instructions on setting system variables.

{% include "../../../.gitbook/includes/for-a-full-list-of-server-v....md" %}

#### `aria_block_size`

* Description: Block size to be used for Aria index pages. Changing this requires dumping, deleting old tables and deleting all log files, and then restoring your Aria tables. If key lookups take too long (and one has to search roughly 8192/2 by default to find each key), can be made smaller, e.g. `4096`.
* Command line: `--aria-block-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `8192`
* Range:
  * > \= [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes): `4096` to `32768` in increments of `1024`
  * <= [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes): `1024` to `32768` in increments of `1024`

#### `aria_checkpoint_interval`

* Description: Interval in seconds between automatic checkpoints. 0 means 'no automatic checkpoints' which makes sense only for testing.
* Command line: `--aria-checkpoint-interval=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `30`
* Range: `0` to `4294967295`

#### `aria_checkpoint_log_activity`

* Description: Number of bytes that the transaction log has to grow between checkpoints before a new checkpoint is written to the log.
* Command line: `aria-checkpoint-log-activity=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1048576`
* Range `0` to `4294967295`

#### `aria_encrypt_tables`

* Description: Enables automatic encryption of all user-created Aria tables that have the [ROW\_FORMAT](../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option set to [PAGE](aria-storage-formats.md#page). See [Data at Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md) and [Enabling Encryption for User-created Tables](../../../security/securing-mariadb/encryption/data-at-rest-encryption/aria-encryption/aria-encryption-overview.md).
* Command line: `aria-encrypt-tables={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `aria_force_start_after_recovery_failures`

* Description: Number of consecutive log recovery failures after which logs are automatically deleted to cure the problem; 0 (the default) disables the feature.
* Command line: `--aria-force-start-after-recovery-failures=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `0`

#### `aria_group_commit`

* Description: Specifies Aria [group commit mode](aria-group-commit.md).
* Command line: `--aria_group_commit="value"`
* Alias: `maria_group_commit`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Valid values:
  * `none` - Group commit is disabled.
  * `hard` - Wait the number of microseconds specified by\
    aria\_group\_commit\_interval before actually doing the commit. If the interval\
    is 0 then just check if any other threads have requested a commit during the\
    time this commit was preparing (just before sync() file) and send their data to\
    disk also before sync().
  * `soft` - The service thread will wait the specified time and then sync()\
    to the log. If the interval is 0 then it won't wait for any commits (this is\
    dangerous and should generally not be used in production)
* Default Value: `none`

#### `aria_group_commit_interval`

* Description: Interval between [Aria group commits](aria-group-commit.md) in microseconds (1/1000000 second) for other threads to come and do a commit in "hard" mode and sync()/commit at all in "soft" mode. Option only has effect if [aria\_group\_commit](aria-system-variables.md#aria_group_commit) is used.
* Command line: `--aria_group_commit_interval=#`
* Alias: `maria_group_commit_interval`
* Scope: Global
* Dynamic: No
* Type: numeric
* Valid Values:
  * Default Value: `0` (no waiting)
  * Range: `0-4294967295`

#### `aria_log_dir_path`

* Description: Path to the directory where transactional log should be stored
* Command line: `--aria-log-dir-path=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: Same as DATADIR
* Introduced: [MariaDB 10.5.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-20-release-notes), [MariaDB 10.6.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-13-release-notes), [MariaDB 10.11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-3-release-notes) (as a system variable, existed as an option only before that)

#### `aria_log_file_size`

* Description: Limit for Aria transaction log size
* Command line: `--aria-log-file-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1073741824`

#### `aria_log_purge_type`

* Description: Specifies how the Aria transactional log are purged. Set to `at_flush` to keep a copy of the transaction logs (good as an extra backup). The logs will stay until the next [FLUSH LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md);
* Command line: `--aria-log-purge-type=name`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `immediate`
* Valid Values: `immediate`, `external`, `at_flush`

#### `aria_max_sort_file_size`

* Description: Don't use the fast sort index method to created index if the temporary file would get bigger than this.
* Command line: `--aria-max-sort-file-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `9223372036853727232`
* Range: `0` to `9223372036854775807`

#### `aria_page_checksum`

* Description: Determines whether index and data should use page checksums for extra safety. Can be overridden per table with PAGE\_CHECKSUM clause in [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md).
* Command line: `--aria-page-checksum=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `aria_pagecache_age_threshold`

* Description: This characterizes the number of hits a hot block has to be untouched until it is considered aged enough to be downgraded to a warm block. This specifies the percentage ratio of that number of hits to the total number of blocks in the page cache.
* Command line: `--aria-pagecache-age-threshold=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `300`
* Range: `100` to `9999900`

#### `aria_pagecache_buffer_size`

* Description: The size of the buffer used for index and data blocks for Aria tables. This can include explicit Aria tables, system tables, and temporary tables. Increase this to get better handling and measure by looking at [aria-status-variables/#aria\_pagecache\_reads](aria-status-variables.md#aria_pagecache_reads) (should be small) vs [aria-status-variables/#aria\_pagecache\_read\_requests](aria-status-variables.md#aria_pagecache_read_requests).
* Command line: `--aria-pagecache-buffer-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `134217720` (128MB)
* Range: `131072` (128KB) upwards

#### `aria_pagecache_division_limit`

* Description: The minimum percentage of warm blocks in the key cache.
* Command line: `--aria-pagecache-division-limit=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Range: `1` to `100`

#### `aria_pagecache_file_hash_size`

* Description: Number of hash buckets for open and changed files. If you have many Aria files open you should increase this for faster flushing of changes. A good value is probably 1/10th of the number of possible open Aria files.
* Command line: `--aria-pagecache-file-hash-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `512`
* Range: `128` to `16384`

#### `aria_pagecache_segments`

* Description: The number of segments in the page\_cache. Each file is put in their own segments of size pagecache\_buffer\_size / segments. Having many segments improves parallel performance.
* Command line: `--aria-pagecache-segments=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1`
* Range: `1` to `128`
* Introduced: [MariaDB Community Server 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1), [MariaDB Enterprise Server 11.4.8-5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.4/11.4.8-5)

#### `aria_recover`

* Description: `aria_recover` has been renamed to `aria_recover_options` in [MariaDB 10.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1020-release-notes). See [aria\_recover\_options](aria-system-variables.md#aria_recover_options) for the description.

#### `aria_recover_options`

* Description: Specifies how corrupted tables should be automatically repaired. More than one option can be specified, for example `FORCE,BACKUP`.
  * `NORMAL`: Normal automatic repair, the default until [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes)
  * `OFF`: Autorecovery is disabled, the equivalent of not using the option
  * `QUICK`: Does not check rows in the table if there are no delete blocks.
  * `FORCE`: Runs the recovery even if it determines that more than one row from the data file are lost.
  * `BACKUP`: Keeps a backup of the data files.
* Command line: `--aria-recover-options[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value:
  * `BACKUP,QUICK` (>= [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes))
  * `NORMAL` (<= [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes))
* Valid Values: `NORMAL`, `BACKUP`, `FORCE`, `QUICK`, `OFF`
* Introduced: [MariaDB 10.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1020-release-notes)

#### `aria_repair_threads`

* Description: Number of threads to use when repairing Aria tables. The value of 1 disables parallel repair. Increasing from the default will usually result in faster repair, but will use more CPU and memory.
* Command line: `--aria-repair-threads=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`

#### `aria_sort_buffer_size`

* Description: The buffer that is allocated when sorting the index when doing a [REPAIR](../../../reference/sql-statements/table-statements/repair-table.md) or when creating indexes with [CREATE INDEX](../../../reference/sql-statements/data-definition/create/create-index.md) or [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/).
* Command line: `--aria-sort-buffer-size=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `268434432`

#### `aria_stats_method`

* Description: Determines how NULLs are treated for Aria index statistics purposes. If set to `nulls_equal`, all NULL index values are treated as a single group. This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful. If set to `nulls_unequal`, the default, the opposite approach is taken, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable. Setting to `nulls_ignored` ignores NULLs altogether from index group calculations. Statistics need to be recalculated after this method is changed. See also [Index Statistics](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/index-statistics.md), [myisam\_stats\_method](../myisam-storage-engine/myisam-system-variables.md) and [innodb\_stats\_method](../innodb/innodb-system-variables.md).
* Command line: `--aria-stats-method=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `nulls_unequal`
* Valid Values: `nulls_equal`, `nulls_unequal`, `nulls_ignored`

#### `aria_sync_log_dir`

* Description: Controls syncing directory after log file growth and new file creation.
* Command line: `--aria-sync-log-dir=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `enumeration`
* Default Value: `NEWFILE`
* Valid Values: `NEWFILE`, `NEVER`, `ALWAYS`

#### `aria_used_for_temp_tables`

* Description: Readonly variable indicating whether the [Aria](./) storage engine is used for temporary tables. If set to `ON`, the default, the Aria storage engine is used. If set to `OFF`, MariaDB reverts to using [MyISAM](../myisam-storage-engine/) for on-disk temporary tables. The [MEMORY](../memory-storage-engine.md) storage engine is used for temporary tables regardless of this variable's setting where appropriate. The default can be changed by not using the `--with-aria-tmp-tables` option when building MariaDB.
* Command line: No
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `deadlock_search_depth_long`

* Description: Long search depth for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](./) storage engine.
* Command line: `--deadlock-search-depth-long=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `15`
* Range: `0` to `33`

#### `deadlock_search_depth_short`

* Description: Short search depth for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](./) storage engine.
* Command line: `--deadlock-search-depth-short=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `4`
* Range: `0` to `32`

#### `deadlock_timeout_long`

* Description: Long timeout in microseconds for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](./) storage engine.
* Command line: `--deadlock-timeout-long=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `50000000`
* Range: `0` to `4294967295`

#### `deadlock_timeout_short`

* Description: Short timeout in microseconds for the [two-step deadlock detection](aria-two-step-deadlock-detection.md). Only used by the [Aria](./) storage engine.
* Command line: `--deadlock-timeout-short=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10000`
* Range: `0` to `4294967295`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
