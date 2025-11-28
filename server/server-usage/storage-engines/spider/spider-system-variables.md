# Spider System Variables

The following variables are available when the [Spider](./) storage engine has been installed.

See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

**MariaDB starting with** [**10.5.22**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-22-release-notes)

Starting from [MariaDB 10.5.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-22-release-notes), [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-15-release-notes), [MariaDB 10.9.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/mariadb-10-9-8-release-notes), [MariaDB 10.10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-6-release-notes), [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes), [MariaDB 11.0.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes), all spider system variables with the value -1 for deferring to table parameter values follow the correct overriding mechanism: table parameter (if set) overrides system variables (if not -1) overrides actual variable default. As a side effect, all such system variables in all versions have the same default value as the table param default value.\
Before this change, a non-minus-one system variable value would override the table parameter value. That is, if both the system variable value and the table parameter value were set to be non-minus-one, the system variable value would prevail. For [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107)+ where the system variable default values were the same as table param default instead of -1, this means that if the system variable were not set, but a table param is set to a non-default value, the default would override the non-default value.

#### `spider_auto_increment_mode`

* Description: The [auto increment](../../../reference/data-types/auto_increment.md) mode.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Normal Mode. Uses a counter that Spider gets from the remote backend server with an exclusive lock for the auto-increment value. This mode is slow. Use Quick Mode (`2`), if you use Spider tables with the table partitioning feature and the auto-increment column is the first column of the index.
  * `1` Quick Mode. Uses an internal Spider counter for the auto-increment value. This mode is fast, but it is possible for duplicates to occur when updating the same table from multiple Spider proxies.
  * `2` Set Zero Mode. The auto-increment value is given by the remote backend. Sets the column to `0`, even if you set the value to the auto-increment column in your statement. If you use the table with the table partitioning feature, it sets to zero after choosing an inserted partition.
  * `3` When the auto-increment column is set to `NULL`, the value is given by the remote backend server. If you set the auto-increment column to `0`,the value is given by the local server. Set [spider\_reset\_auto\_increment](spider-system-variables.md#spider_reset_auto_increment) to `2` or `3` if you want to use an auto-increment column on the remote server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `3`
* DSN Parameter Name: `aim`

#### `spider_bgs_first_read`

* Description: Number of first read records to use when performing a concurrent background search. To start a range scan on the remote backend, the storage engine first needs to send the first record. Fetching a second record in the same query can save a network round trip stopping the plan if the backend has a single record. The first and second reads are used to warm up for background search. When not using [spider\_split\_read](spider-system-variables.md#spider_split_read) and [spider\_semi\_split\_read](spider-system-variables.md#spider_semi_split_read), the third read fetches the remaining data source in a single fetch.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Records are usually retrieved.
  * `1` and greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2`
* Default Table Value: `2`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `bfr`

#### `spider_bgs_mode`

* Description: Background search mode. This enables the use of a thread per data server connection if the query is not shard-based and must be distributed across shards. The partitioning plugin scans partitions one after the other to optimize memory usage. Because the shards are external, reading all shards can be performed in parallel when the plan prunes multiple partitions.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Disables background search.
  * `1` Uses background search when searching without locks
  * `2` Uses background search when searching without locks or with shared locks.
  * `3` Uses background search regardless of locks.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `3`
* DSN Parameter Name: `bmd`

#### `spider_bgs_second_read`

* Description: Number of second read records on the backend server when using background search. When the first records are found from [spider\_bgs\_first\_read](spider-system-variables.md#spider_bgs_first_read), the engine continues scanning a range adding a `LIMIT` of [spider\_bgs\_first\_read](spider-system-variables.md#spider_bgs_first_read) and [spider\_bgs\_second\_read](spider-system-variables.md#spider_bgs_second_read).
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Records are usually retrieved.
  * `1` and greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Default Session Value: `100`
* Default Table Value: `100`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `bsr`

#### `spider_bka_engine`

* Description: Storage engine used with temporary tables when the [spider\_bka\_mode](spider-system-variables.md#spider_bka_mode) system variable is set to `1`. Defaults to the value of the [table parameter](spider-table-parameters.md), which is [MEMORY](../memory-storage-engine.md) by default.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Session Value: `""`
* Default Table Value: `Memory`
* DSN Parameter Name: `bke`

#### `spider_bka_mode`

* Description: Internal action to perform when multi-split reads are disabled. If the [spider\_multi\_split\_read](spider-system-variables.md#spider_multi_split_read) system variable is set to `0`, Spider uses this variable to determine how to handle statements when the optimizer resolves range retrieval to multiple conditions.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Uses "union all".
  * `1` Uses a temporary table, if it is judged acceptable.
  * `2` Uses a temporary table, if it is judged acceptable and avoids replication delay.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `2`
* DSN Parameter Name: `bkm`

#### `spider_bka_table_name_type`

* Description: The type of temporary table name for bka.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Range: `-1` to `1`

#### `spider_block_size`

* Description: Size of memory block used in MariaDB. Can usually be left unchanged.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `16384`
* Range: `0` to `4294967295`
* DSN Parameter Name: `bsz`

#### `spider_buffer_size`

* Description: Buffer size. `-1`, the default, will use the [table parameter](spider-table-parameters.md).
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `16000`
* Default Table Value: `16000`
* Range: `-1` to `2147483647`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `spider_bulk_size`

* Description: Size in bytes of the buffer when multiple grouping multiple `INSERT` statements in a batch, (that is, bulk inserts).
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `0` or greater: Size of the buffer.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `16000`
* Default Table Value: `16000`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `bsz`

#### `spider_bulk_update_mode`

* Description: Bulk update and delete mode. Note: If you use a non-default value for the [spider\_bgs\_mode](spider-system-variables.md#spider_bgs_mode) or [spider\_split\_read](spider-system-variables.md#spider_split_read) system variables, Spider sets this variable to `2`.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Sends `UPDATE` and `DELETE` statements one by one.
  * `1` Collects multiple `UPDATE` and `DELETE` statements, then sends the collected statements one by one.
  * `2` Collects multiple `UPDATE` and `DELETE` statements and sends them together.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `2`
* DSN Parameter Name: `bum`

#### `spider_bulk_update_size`

* Description: Size in bytes for `UPDATE` and `DELETE` queries when generating bulk updates.
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `0` or greater: Size of buffer.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `16000`
* Default Table Value: `16000`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `bus`

#### `spider_casual_read`

* Description: Casual Reads enables all isolation levels, (such as repeatable reads) to work with transactions on multiple backends. With auto-commit queries, you can relax read consistency and run on multiple connections to the backends. This enables parallel queries across partitions, even if multiple shards are stored on the same physical server. Deprecated in [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115) due to the complexity of the code for little benefit.
  * `-1` Use [table parameter](spider-table-parameters.md).
  * `0` Use casual read.
  * `1` Choose connection channel automatically.
  * `2` to `63` Number of connection channels.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `63`
* DSN Parameter Name: `##`
* Deprecated: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

#### `spider_conn_recycle_mode`

* Description: Connection recycle mode.
  * `0` Disconnect.
  * `1` Recycle by all sessions.
  * `2` Recycle in the same session.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Range: `0` to `2`
* Default Session Value: `0`

#### `spider_conn_recycle_strict`

* Description: Whether to force the creation of new connections.
  * `1` Don't force.
  * `0` Force new connection
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Range: `0` to `1`

#### `spider_conn_wait_timeout`

* Description: Max waiting time in seconds for Spider to get a remote connection.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `10`
* Range: `0` to `1000`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)

#### `spider_connect_error_interval`

* Description: Return same error code until interval passes if connection is failed
* Scope: Global,
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `4294967295`

#### `spider_connect_mutex`

* Description: Whether to serialize remote servers connections (use mutex at connecting). Use this parameter if you get an error or slowdown due to too many connection processes.
  * `0` Not serialized.
  * `1` : Serialized.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `0`

#### `spider_connect_retry_count`

* Description: Number of times to retry connections that fail due to too many connection processes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2` (>= [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-8-series/what-is-mariadb-118)), `1000` (<= [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117))
* Range: `0` to `2147483647`

#### `spider_connect_retry_interval`

* Description: Interval in microseconds for connection failure due to too many connection processes.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1000`
* Range: `-1` to `9223372036854775807`

#### `spider_connect_timeout`

* Description: Timeout in seconds to declare remote backend unresponsive when opening a connection. Change for high-latency networks.
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `0` Less than 1.
  * `1` and greater: Number of seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `6`
* Default Table Value: `0`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `cto`

#### `spider_crd_bg_mode`

* Description: Indexes cardinality statistics in the background. Disable when the [spider\_crd\_mode](spider-system-variables.md#spider_crd_mode) system variable is set to `3` or when the [spider\_crd\_interval](spider-system-variables.md#spider_crd_interval) variable is set to `0`.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Disables background confirmation.
  * `2` Enables background confirmation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2`
* Default Table Value: `1`
* Range: `-1` to `2`
* DSN Parameter Name: `cbm`

#### `spider_crd_interval`

* Description: Time interval in seconds of index cardinality statistics. Set to `0` to always get the latest information from remote servers.
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `1` or more: Interval in seconds table state confirmation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `51`
* Default Table Value: `51`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `civ`

#### `spider_crd_mode`

* Description: Mode for index cardinality statistics. By default, uses `SHOW` at the table-level.
  * `-1,0` Uses the [table parameter](spider-table-parameters.md).
  * `1` Uses the `SHOW` command.
  * `2` Uses the Information Schema.
  * `3` Uses the `EXPLAIN` command.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `3`
* DSN Parameter Name: `cmd`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_crd_sync`

* Description: Synchronize index cardinality statistics in partitioned tables.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Disables synchronization.
  * `1` Uses table state synchronization when opening a table, but afterwards performs no synchronization.
  * `2` Enables synchronization.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `2`
* DSN Parameter Name: `csy`

#### `spider_crd_type`

* Description: Type of cardinality calculation. Only effective when the [spider\_crd\_mode](spider-system-variables.md#spider_crd_mode) system variable is set to use `SHOW` (`1`) or to use the Information Schema (`2`).
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Uses the value of the [spider\_crd\_weight](spider-system-variables.md#spider_crd_weight) system variable, as a fixed value.
  * `1` Uses the value of the [spider\_crd\_weight](spider-system-variables.md#spider_crd_weight) system variable, as an addition value.
  * `2` Uses the value of the [spider\_crd\_weight](spider-system-variables.md#spider_crd_weight) system variable, as a multiplication value.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2`
* Default Table Value: `2`
* Range: `-1` to `2`
* DSN Parameter Name: `ctp`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_crd_weight`

* Description: Weight coefficient used to calculate effectiveness of index from the cardinality of column. For more information, see the description for the [spider\_crd\_type](spider-system-variables.md#spider_crd_type) system variable.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` or greater: Weight.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2`
* Default Table Value: `2`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `cwg`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_delete_all_rows_type`

* Description: The type of delete\_all\_rows.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Range: `-1` to `1`

#### `spider_direct_dup_insert`

* Description: Manages duplicate key check for [REPLACE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md), [INSERT IGNORE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/ignore.md) and [LOAD DATA LOCAL INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) to remote servers. This can save on network roundtrips if the key always maps to a single partition. For bulk operations, records are checked for duplicate key errors one by one on the remote server, unless you set it to avoid duplicate checks on local servers (`1`).
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Performs duplicate checks on the local server.
  * `1` Avoids duplicate checks on the local server.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `1`
* DSN Parameter Name: `ddi`

#### `spider_direct_order_limit`

* Description: Pushes `ORDER BY` and `LIMIT` operations to the remote server.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Uses local execution.
  * `1` Uses push down execution.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2`
* Default Table Value: `9223372036854775807`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `dol`

#### `spider_disable_group_by_handler`

* Description: Whether to disable the spider group by handler, which if created takes over the query execution after query optimization is done.
  * `OFF` Does not disable the spider group by handler.
  * `ON` Disables the spider group by handler.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-7-release-notes)

#### `spider_dry_access`

* Description: Simulates an empty result-set. No queries are sent to the backend. Use for performance tuning.
  * `0` Normal access.
  * `1` All access from Spider to data node is suppressed.
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `spider_error_read_mode`

* Description: Sends an empty result-set when reading a backend server raises an error. Useful with applications that don't implement transaction replays.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Returns an error.
  * `1` Returns an empty result.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `1`
* DSN Parameter Name: `erm`

#### `spider_error_write_mode`

* Description: Sends an empty result-set when writing to a backend server raises an error. Useful with applications that don't implement transaction replays.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Returns an error.
  * `1` Returns an empty result-set on error.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `1`
* DSN Parameter Name: `ewm`

#### `spider_first_read`

* Description: Number of first read records to start a range scan on the backend server. Spider needs to send the first record. Fetching the second record saves network round-trips, stopping the plan if the backend has a single record. First read and second read are used to warm up for background searches, third reads without using the [spider\_split\_read](spider-system-variables.md#spider_split_read) and [spider\_semi\_split\_read](spider-system-variables.md#spider_semi_split_read) system variables fetches the remaining data source in a single last fetch.
  * `-1` Use the [table parameter](spider-table-parameters.md).
  * `0` Usually retrieves records.
  * `1` and greater: Sets the number of first read records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `2`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `frd`

#### `spider_force_commit`

* Description: Behavior when error occurs on `XA PREPARE`, `XA COMMIT`, and `XA ROLLBACK` statements.
  * `0` Returns the error.
  * `1` Returns the error when the `xid` doesn't exist, otherwise it continues processing the XA transaction.
  * `2` Continues processing the XA transaction, disregarding all errors.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Range: `0` to `2`

#### `spider_general_log`

* Description: Whether Spider logs all commands to the General Log. Spider logs error codes according to the [spider\_log\_result\_errors](spider-system-variables.md#spider_log_result_errors) system variable.
  * `OFF` Logs no commands.
  * `ON` Logs commands to the General Log.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `OFF`

#### `spider_ignore_comments`

* Description: Whether to unconditionally ignore COMMENT and CONNECTION strings without checking whether table options are specified.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `spider_index_hint_pushdown`

* Description: Whether to use pushdown index hints, like `force_index`.
  * `0` Do not use pushdown hints
  * `1` Use pushdown hints
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `OFF`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)

#### `spider_init_sql_alloc_size`

* Description: Initial size of the local SQL buffer.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` or greater: Size of the buffer.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1024`
* Default Table Value: `1024`
* DSN Parameter Name: `isa`
* Range: `-1` to `2147483647`
* Deprecated: [MariaDB 10.7.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes), [MariaDB 10.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes), [MariaDB 10.9.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)

#### `spider_internal_limit`

* Description: Limits the number of records when acquired from a remote server.
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `0` or greater: Records limit.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `9223372036854775807`
* Default Table Value: `9223372036854775807`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `ilm`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_internal_offset`

* Description: Skip records when acquired from the remote server.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` or more : Number of records to skip.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `ios`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_internal_optimize`

* Description: Whether to perform push down operations for [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) statements.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Transmitted.
  * `1` Not transmitted.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `1`
* DSN Parameter Name: `iom`

#### `spider_internal_optimize_local`

* Description: Whether to transmit to remote servers when [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) statements are executed on the local server.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Not transmitted.
  * `1` Transmitted.
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `1`
* DSN Parameter Name: `iol`

#### `spider_internal_sql_log_off`

* Description: Whether to log SQL statements sent to the remote server in the [General Query Log](../../../server-management/server-monitoring-logs/general-query-log.md).
  * Explicitly setting this system variable to either `ON` or `OFF` causes the Spider node to send a `SET sql_log_off` statement to each of the data nodes using the `SUPER` privilege.
  * `-1` Don't know or does not matter; don't send 'SET SQL\_LOG\_OFF' statement
  * `0` Send 'SET SQL\_LOG\_OFF 0' statement to data nodes (logs SQL statements to the remote server)
  * `1` Send 'SET SQL\_LOG\_OFF 1' statement to data nodes (doesn't log SQL statements to the remote server)
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric` (previously `boolean`)
* Range: `-1` to `1`
* Default Session Value: `-1` (previously `ON`)

#### `spider_internal_unlock`

* Description: Whether to transmit unlock tables to the connection of the table used with `SELECT` statements.
  * `0` Not transmitted.
  * `1` Transmitted.
* Data Type: `boolean`
* Default Session Value: `0`

#### `spider_internal_xa`

* Description: Whether to implement XA at the server- or storage engine-level. When using the server-level, set different values for the [server\_id](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#server_id) system variable on all server instances to generate different `xid` values.
  * `OFF` Uses the storage engine protocol.
  * `ON` Uses the server protocol.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `OFF`

#### `spider_internal_xa_id_type`

* Description: The type of internal\_xa id.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Range: `-1` to `1`

#### `spider_internal_xa_snapshot`

* Description: Limitation for reading consistent data on all backend servers when using MariaDB's internal XA implementation and `START TRANSACTION WITH CONSISTENT SNAPSHOT`.
  * `0` Raise error when using a Spider table.
  * `1` Raise error when issued a `START TRANSACTION` statement.
  * `2` Takes a consistent snapshot on each backend, but loses global consistency.
  * `3` Starts transactions with XA, but removes `CONSISTENT SNAPSHOT`.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Range: `0` to `3`
* Default Session Value: `0`

#### `spider_load_crd_at_startup`

* Description: Whether to load CRD from the system table at startup.
  * `-1` Use [table parameter](spider-table-parameters.md)
  * `0` Do not load
  * `1` Load
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Range: `-1` to `1`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_load_sts_at_startup`

* Description: Whether to load STS from the system table at startup.
  * `-1` Use [table parameter](spider-table-parameters.md)
  * `0` Do not load
  * `1` Load
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `1`
* Range: `-1` to `1`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_local_lock_table`

* Description: Whether to push [LOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) statements down to the remote server.
  * `0` Transmitted.
  * `1` Not transmitted.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`

#### `spider_lock_exchange`

* Description:\
  Whether to convert [SELECT... LOCK IN SHARE MODE](../../../reference/sql-statements/data-manipulation/selecting-data/lock-in-share-mode.md) and [SELECT... FOR UPDATE](../../../reference/sql-statements/data-manipulation/selecting-data/for-update.md) statements into a [LOCK TABLE](../../../reference/sql-statements/transactions/lock-tables.md) statement.
  * `0` Not converted.
  * `1` Converted.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `0`

#### `spider_log_result_error_with_sql`

* Description: How to log SQL statements with result errors.
  * `0` No log
  * `1` Log error
  * `2` Log warning summary
  * `3` Log warning
  * `4` Log info (Added in [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes))
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4`

#### `spider_log_result_errors`

* Description: Log results from data nodes to the Spider node in the [Error Log](../../../server-management/server-monitoring-logs/error-log.md). Performs no logging by default.
  * `0` : Logs no errors from data nodes.
  * `1` : Logs errors from data nodes.
  * `2` : Logs errors from data nodes, as well as warning summaries.
  * `3` : Logs errors from data nodes, as well as warning summaries and details.
  * `4` : Logs errors from data nodes, as well as warning summaries and details, and result summaries.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4`

#### `spider_low_mem_read`

* Description: Whether to use low memory mode when executing queries issued internally to remote servers that return result-sets.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Doesn't use low memory mode.
  * `1` Uses low memory mode.
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `1`

#### `spider_max_connections`

* Description: Maximum number of connections from Spider to a remote MariaDB servers. Defaults to `0`, which is no limit.
* Command-line: `--spider-max-connections`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Range: `0` to `99999`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)

#### `spider_max_order`

* Description: Maximum number of columns for `ORDER BY` operations.
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `0` and greater: Maximum number of columns.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `32767`
* Default Table Value: `32767`
* Range: `-1` to `32767`
* DSN Parameter Name: `mod`

#### `spider_multi_split_read`

* Description:\
  Whether to divide a statement into multiple SQL statements sent to the remote backend server when the optimizer resolves range retrievals to multiple conditions.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Doesn't divide statements.
  * `1` Divides statements.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `100`
* Default Table Value: `100`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `msr`

#### `spider_net_read_timeout`

* Description: TCP timeout in seconds to declare remote backend servers unresponsive when reading from a connection. Change for high latency networks.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Less than 1 second timeout.
  * `1` and greater: Timeout in seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `600`
* Default Table Value: `600`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `nrt`

#### `spider_net_write_timeout`

* Description: TCP timeout in seconds to declare remote backend servers unresponsive when writing to a connection. Change for high latency networks.
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `0` Less than 1 second timeout.
  * `1` and more: Timeout in seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `600`
* Default Table Value: `600`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `nwt`

#### `spider_ping_interval_at_trx_start`

* Description: Resets the connection with keepalive timeout in seconds by sending a ping.
  * `0` At every transaction.
  * `1` and greater: Number of seconds.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `3600`
* Range: `0` to `2147483647`

#### `spider_quick_mode`

* Description: Sets the backend query buffering to cache on the remote backend server or in the local buffer.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Local buffering, it acquires records collectively with `store_result`.
  * `1` Remote buffering, it acquires records one by one. Interrupts don't wait and recovery on context switch back.
  * `2` Remote buffering, it acquires records one by one. Interrupts wait to the end of the acquisition.
  * `3` Local buffering, uses a temporary table on disk when the result-set is greater than the value of the [spider\_quick\_page\_size](spider-system-variables.md#spider_quick_page_size) system variable.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `3`
* Default Table Value: `3`
* Range: `-1` to `3`
* DSN Parameter Name: `qmd`

#### `spider_quick_page_byte`

* Description: Memory limit by size in bytes in a page when acquired record by record.
  * `-1` The [table parameter](spider-table-parameters.md) is used. When quick\_mode is 1 or 2, Spider stores at least 1 record even if quick\_page\_byte is smaller than 1 record. When quick\_mode is 3, quick\_page\_byte is used for judging using temporary tables. That is given priority when spider\_quick\_page\_byte is set.
  * `0` or greater: Memory limit.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `10485760`
* Range: `-1` to `9223372036854775807`
* Introduced: [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes), [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes)

#### `spider_quick_page_size`

* Description: Number of records in a page when acquired record by record.
  * `-1` The [table parameter](spider-table-parameters.md) is adopted.
  * `0` or greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1024` (>=[MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107)), `-1` (<= [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106))
* Default Table Value: `100`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `qps`

#### `spider_read_only_mode`

* Description: Whether to allow writes on Spider tables.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Allows writes to Spider tables.
  * `1` Makes tables read- only.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0` (>=[MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107)), `-1` (<= [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106))
* Default Table Value: `0`
* Range: `-1` to `1`
* DSN Parameter Name: `rom`

#### `spider_remote_access_charset`

* Description: Forces the specified session [character set](../../../reference/data-types/string-data-types/character-sets/) when connecting to the backend server. This can improve connection time performance.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Session Value: `null`

#### `spider_remote_autocommit`

* Description: Sets the auto-commit mode when connecting to backend servers. This can improve connection time performance.
  * `-1` Doesn't change the auto-commit mode.
  * `0` Sets the auto-commit mode to `0`.
  * `1` Sets the auto-commit mode to `1`.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `-1`
* Range: `-1` to `1`

#### `spider_remote_default_database`

* Description: Sets the local default database when connecting to backend servers. This can improve connection time performance.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Session Value: Empty string

#### `spider_remote_sql_log_off`

* Description: Sets the [sql\_log\_off](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_log_off) system variable to use when connecting to backend servers.
  * `-1` Doesn't set the value.
  * `0` Doesn't log Spider SQL statements to remote backend servers.
  * `1` Logs SQL statements on remote backend
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `-1`
* Range: `-1` to `1`

#### `spider_remote_time_zone`

* Description: Forces the specified [time zone](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) setting when connecting to backend servers.\
  This can improve connection performance when you know the time zone.
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Session Value: `null`

#### `spider_remote_trx_isolation`

* Description: Sets the [Transaction Isolation Level](../../../reference/sql-statements/transactions/set-transaction.md#isolation-levels) when connecting to the backend server.
  * `-1` Doesn't set the Isolation Level.
  * `0` Sets to the `READ UNCOMMITTED` level.
  * `1` Sets to the `READ COMMITTED` level.
  * `2` Sets to the `REPEATABLE READ` level.
  * `3` Sets to the `SERIALIZABLE` level.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `-1`
* Range: `-1` to `3`

#### `spider_remote_wait_timeout`

* Description: Wait timeout in seconds on remote server. `-1` means not set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `2147483647`
* Introduced: [MariaDB 10.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1045-release-notes)

#### `spider_reset_sql_alloc`

* Description: Resets the per connection SQL buffer after an SQL statement executes.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Doesn't reset.
  * `1` Resets.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `1`
* DSN Parameter Name: `rsa`

#### `spider_same_server_link`

* Description: Enables the linking of a table to the same local instance.
  * `0` Disables linking.
  * `1` Enables linking.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `OFF`

#### `spider_second_read`

* Description: Number of second read records on the backend server when the first records are found from the first read. Spider continues scanning a range, adding a `LIMIT` using the [spider\_first\_read](spider-system-variables.md#spider_first_read) and [spider\_second\_read](spider-system-variables.md#spider_second_read) variables.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Usually retrieves records.
  * `1` and greater: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `srd`

#### `spider_select_column_mode`

* Description: Mode for column retrieval from remote backend server.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Uses index columns when the `SELECT` statement can resolve with an index, otherwise uses all columns.
  * `1` Uses all columns judged necessary to resolve the query.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `1`
* DSN Parameter Name: `scm`

#### `spider_selupd_lock_mode`

* Description: Local lock mode on `INSERT SELECT`.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Takes no locks.
  * `1` Takes shared locks.
  * `2` Takes exclusive locks.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `2`
* DSN Parameter Name: `slm#`

#### `spider_semi_split_read`

* Description:\
  Whether to use chunk retrieval with offset and limit parameters on SQL statements sent to the remote backend server when using the [spider\_split\_read](spider-system-variables.md#spider_split_read) system variable.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Doesn't use chunk retrieval.
  * `1 or more` Uses chunk retrieval.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2`
* Default Table Value: `2`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `ssr#`

#### `spider_semi_split_read_limit`

* Description: Sets the limit value for the [spider\_semi\_split\_read](spider-system-variables.md#spider_semi_split_read) system variable.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` or more: The limit value.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `9223372036854775807`
* Default Table Value: `9223372036854775807`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `ssl#`

#### `spider_semi_table_lock`

* Description: Enables semi-table locking. This adds a [LOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) statement to SQL executions sent to the remote backend server when using non-transactional storage engines to preserve consistency between roundtrips.
  * `0` Disables semi-table locking.
  * `1` Enables semi-table locking.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0` (>=[MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108)), `1` (<= [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107))
* Range: `0` to `1`
* DSN Parameter Name: `stl#`

#### `spider_semi_table_lock_connection`

* Description: Whether to use multiple connections with semi-table locking. To enable semi-table locking, use the [spider\_semi\_table\_lock](spider-system-variables.md#spider_semi_table_lock) system variable.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Uses the same connection.
  * `1` Uses different connections.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `1`
* DSN Parameter Name: `stc#`

#### `spider_semi_trx`

* Description: Enables semi-transactions. This controls transaction consistency when an SQL statement is split into multiple statements issued to the backend servers. You can preserve or relax consistency as need. Spider encapsulates auto-committed SQL statements within a transaction on the remote backend server. When using `READ COMMITTED` or `READ UNCOMMITTED` [transaction isolation levels](../../../reference/sql-statements/transactions/set-transaction.md#isolation-levels) to force consistency, set the [spider\_semi\_trx\_isolation](spider-system-variables.md#spider_semi_trx_isolation) system variable to `2`.
  * `0` Disables semi-transaction consistency.
  * `1` Enables semi-transaction consistency.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `ON`

#### `spider_semi_trx_isolation`

* Description: Set consistency during range SQL execution when [spider\_sync\_trx\_isolation](spider-system-variables.md#spider_sync_trx_isolation) is 1
  * `-1` OFF
  * `0` READ UNCOMMITTED
  * `1` READ COMMITTED
  * `2` REPEATABLE READ
  * `3` SERIALIZABLE
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `-1`
* Range: `-1` to `3`

#### `spider_skip_default_condition`

* Description: Whether to compute condition push downs.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Computes condition push downs.
  * `1` Doesn't compute condition push downs.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `1`
* DSN Parameter Name: `sdc`

#### `spider_skip_parallel_search`

* Description: Whether to skip parallel search by specific conditions.
  * `-1` :use [table parameter](spider-table-parameters.md)
  * `0` :not skip
  * `1` :skip parallel search if query is not SELECT statement
  * `2` :skip parallel search if query has SQL\_NO\_CACHE
  * `3` :1+2
* Command line: `--spider-skip-parallel-search=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Range: `-1` to `3`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)

#### `spider_slave_trx_isolation`

* Description: Transaction isolation level when Spider table is used by slave SQL thread.
  * `-1` off
  * `0` read uncommitted
  * `1` read committed
  * `2` repeatable read
  * `3` serializable
* Command line: `--spider-slave-trx-isolation=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `-1`
* Range: `-1` to `3`
* Introduced: [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes), [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes)

#### `spider_split_read`

* Description: Number of records in chunk to retry the result when a range query is sent to remote backend servers.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` or more: Number of records.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `9223372036854775807`
* Default Table Value: `9223372036854775807`
* Range: `-1` to `9223372036854775807`
* DSN Parameter Name: `srd`

#### `spider_store_last_crd`

* Description: Whether to store last CRD result in the system table.
  * `-1` Use [table parameter](spider-table-parameters.md).
  * `0` Do not store last CRD result in the system table.
  * `1` Store last CRD result in the system table.
* Command line: `--spider-store-last-crd=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Range: `-1` to `1`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_store_last_sts`

* Description: Whether to store last STS result in the system table.
  * `-1` Use [table parameter](spider-table-parameters.md).
  * `0` Do not store last STS result in the system table.
  * `1` Store last STS result in the system table.
* Command line: `--spider-store-last-sts=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Range: `-1` to `1`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_strict_group_by`

* Description:\
  Whether to use columns in select clause strictly for group by clause
  * `-1` Use the [table parameter](spider-table-parameters.md).
  * `0` Do not strictly use columns in select clause for group by clause
  * `1` Use columns in select clause strictly for group by clause
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Range: `-1` to `1`
* Introduced: [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)

#### `spider_sts_bg_mode`

* Description:\
  Enables background confirmation for table statistics. When background confirmation is enabled, Spider uses one thread per partition to maintain table status. Disable when the [spider\_sts\_interval](spider-system-variables.md#spider_sts_interval) system variable is set to `0`, which causes Spider to always retrieve the latest information as need. It is effective, when the [spider\_sts\_interval](spider-system-variables.md#spider_sts_interval) system variable is set to `10`.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Disables background confirmation.
  * `1` Enables background confirmation (create thread per table/partition).
  * `2` Enables background confirmation (use static threads). (from MariaDB 10.)
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `2`
* Range: `-1` to `2`
* DSN Parameter Name: `sbm`

#### `spider_sts_interval`

* Description: Time interval of table statistics from the remote backend servers.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Retrieves the latest table statistics on request.
  * `1` or more: Interval in seconds for table state confirmation.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `10`
* Default Table Value: `10`
* Range: `-1` to `2147483647`
* DSN Parameter Name: `siv`

#### `spider_sts_mode`

* Description: Table statistics mode.\
  Mode for table statistics. The [SHOW](../../../reference/sql-statements/administrative-sql-statements/show/) command is used at the table level default.
  * `-1,0` Uses the [table parameter](spider-table-parameters.md).
  * `1` Uses the `SHOW` command.
  * `2` Uses the Information Schema.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `1`
* Default Table Value: `1`
* Range: `-1` to `2`
* DSN Parameter Name: `smd`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

#### `spider_sts_sync`

* Description: Synchronizes table statistics in partitioned tables.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Doesn't synchronize table statistics in partitioned tables.
  * `1` Synchronizes table state when opening a table, doesn't synchronize after opening.
  * `2` Synchronizes table statistics.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Session Value: `0`
* Default Table Value: `0`
* Range: `-1` to `2`
* DSN Parameter Name: `ssy`

#### `spider_support_xa`

* Description: XA Protocol for mirroring and for multi-shard transactions.
  * `1` Enables XA Protocol for these Spider operations.
  * `0` Disables XA Protocol for these Spider operations.
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Table Value: `1`

#### `spider_suppress_comment_ignored_warning`

* Description: Whether to suppress warnings that table COMMENT or CONNECTION strings are ignored due to specified table options.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `spider_sync_autocommit`

* Description: Whether to push down local auto-commits to remote backend servers.
  * `OFF` Pushes down local auto-commits.
  * `ON` Doesn't push down local auto-commits.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `ON`

#### `spider_sync_sql_mode`

* Description: Whether to sync [sql\_mode](../../../server-management/variables-and-modes/sql_mode.md).
  * `OFF` No sync
  * `ON` Sync
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes)

#### `spider_sync_time_zone`

* Description: Whether to push the local time zone down to remote backend servers.
  * `OFF` Doesn't synchronize time zones.
  * `ON` Synchronize time zones.
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `OFF`
* Removed: [MariaDB 10.3.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1039-release-notes)

#### `spider_sync_trx_isolation`

* Description: Pushes local transaction isolation levels down to remote backend servers.
  * `OFF` Doesn't push down local isolation levels.
  * `ON` Pushes down local isolation levels.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `ON`

#### `spider_table_crd_thread_count`

* Description: Static background thread count of table crd.
* Command line: `--spider-table-crd-thread-count=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:
  * `1` (>= [MariaDB 10.4.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10-4-33-release-notes), [MariaDB 10.5.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-24-release-notes), [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes))
  * `10` (<= [MariaDB 10.4.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10-4-32-release-notes), [MariaDB 10.5.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-23-release-notes), [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes), [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes))
* Range: `1` to `4294967295`
* Deprecated: [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117)

#### `spider_table_init_error_interval`

* Description: Interval in seconds where the same error code is returned if table initialization fails. Use to protect against infinite loops in table links.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `4294967295`

#### `spider_table_sts_thread_count`

* Description: Static background thread count of table sts.
* Command line: `--spider-table-sts-thread-count=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
  * `1` (>= [MariaDB 10.4.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10-4-33-release-notes), [MariaDB 10.5.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-24-release-notes), [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes))
  * `10` (<= [MariaDB 10.4.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10-4-32-release-notes), [MariaDB 10.5.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-23-release-notes), [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes), [MariaDB 11.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-3-release-notes), [MariaDB 11.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes))
* Range: `1` to `4294967295`
* Deprecated: [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117)

#### `spider_udf_ct_bulk_insert_interval`

* Description: Interval in milliseconds between bulk inserts at copying. For use with the UDF spider\_copy\_tables, which copies table data linked to a Spider table from the source server to destination server using bulk insert. If this interval is 0, it may cause higher write traffic.
  * `-1` Uses the UDF parameter.
  * `0` and more: Time in milliseconds.
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Default Table Value: `10`
* Range: `-1` to `2147483647`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_udf_ct_bulk_insert_rows`

* Description: Number of rows to insert at a time when copying during bulk inserts.
  * `-1, 0`: Uses the [table parameter](spider-table-parameters.md).
  * `1` and more: Number of rows
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `100`
* Default Table Value: `100`
* Range: `-1` to `9223372036854775807`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_udf_ds_bulk_insert_rows`

* Description: Number of rows inserted at a time during bulk inserts when the result-set is stored in a temporary table on executing a UDF.
  * `-1, 0` Uses the UDF parameter.
  * `1` or more: Number of rows
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `3000`
* Default Table Value: `3000`
* Range: `-1` to `9223372036854775807`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_udf_ds_table_loop_mode`

* Description: Whether to store the result-set in the same temporary table when the temporary table list count for UDF is less than the result-set count on UDF execution.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Drops records.
  * `1` Inserts the last table.
  * `2` Inserts the first table and loops again.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `-1` to `2`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_udf_ds_use_real_table`

* Description: Whether to use real table for temporary table list.
  * `-1` Use UDF parameter.
  * `0` Do not use real table.
  * `1` Use real table.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `-1` to `1`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_udf_table_lock_mutex_count`

* Description: Mutex count of table lock for Spider UDFs.
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `20`
* Range: `1` to `4294967295`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_udf_table_mon_mutex_count`

* Description: Mutex count of table mon for Spider UDFs.
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `20`
* Range: `1` to `4294967295`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_use_all_conns_snapshot`

* Description: Whether to pass `START TRANSACTION WITH SNAPSHOT` statements to all connections.
  * `OFF` Doesn't pass statement to all connections.
  * `ON` Passes statement to all connections.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Session Value: `OFF`

#### `spider_use_cond_other_than_pk_for_update`

* Description: Whether to use all conditions even if condition has a primary key.
  * `0` Don't use all conditions
  * `1` Use all conditions
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `1`
* Introduced: [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes), [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)

#### `spider_use_consistent_snapshot`

* Description:\
  Whether to push a local `START TRANSACTION WITH CONSISTENT` statement down to remote backend servers.
  * `OFF` Doesn't push the local statement down.
  * `ON` Pushes the local statement down.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `spider_use_default_database`

* Description: Whether to use the default database.
  * `OFF` Doesn't use the default database.
  * `ON` Uses the default database.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `spider_use_flash_logs`

* Description: Whether to push [FLUSH LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/) statements down to remote backend servers.
  * `OFF` Doesn't push the statement down.
  * `ON` Pushes the statement down.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `spider_use_handler`

* Description: Converts [HANDLER](../../../reference/sql-structure/nosql/handler/) SQL statements.\
  When the [spider\_sync\_trx\_isolation](spider-system-variables.md#spider_sync_trx_isolation) system variable is set to `0`, Spider disables [HANDLER](../../../reference/sql-structure/nosql/handler/) conversions to prevent use of the statement on the [SERIALIZABLE](../../../reference/sql-statements/transactions/set-transaction.md#serializable) isolation level.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Converts [HANDLER](../../../reference/sql-structure/nosql/handler/) statements into [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements.
  * `1` Passes [HANDLER](../../../reference/sql-structure/nosql/handler/) to the remote backend server.
  * `2` Converts SQL statements to [HANDLER](../../../reference/sql-structure/nosql/handler/) statements.
  * `3` Converts SQL statements to [HANDLER](../../../reference/sql-structure/nosql/handler/) statements and [HANDLER](../../../reference/sql-structure/nosql/handler/) statements to SQL statements.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Default Table Value: `0`
* Range: `-1` to `3`
* DSN Parameter Name: `uhd`
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `spider_use_pushdown_udf`

* Description:\
  When using a UDF function in a condition and the [engine\_condition\_pushdown](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#engine_condition_pushdown) system variable is set to `1`, whether to execute the UDF function locally or push it down.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Doesn't transmit the UDF
  * `1` Transmits the UDF.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `-1`
* Default Table Value: `1`
* Range: `-1` to `1`
* DSN Parameter Name: `upu`

#### `spider_use_snapshot_with_flush_tables`

* Description:\
  Whether to encapsulate [FLUSH LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/) and [UNLOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) statements when `START TRANSACTION WITH CONSISTENT` and `FLUSH TABLE WITH READ LOCK` statements are sent to the remote backend servers.
  * `0` : No encapsulation.
  * `1` : Encapsulates, only when the [spider\_use\_all\_conns\_snapshot](spider-system-variables.md#spider_use_all_conns_snapshot) system variable i set to `1`.
  * `2` :\
    Synchronizes the snapshot using a [LOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) statement and \[flush|FLUSH TABLES]] at the XA transaction level. This is only effective when the [spider\_use\_all\_cons\_snapshot](spider-system-variables.md#spider_use_all_cons_snapshot) system variable is set to `1`.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `2`

#### `spider_use_table_charset`

* Description: Whether to use the local table [character set](../../../reference/data-types/string-data-types/character-sets/) for the remote backend server connections.
  * `-1` Falls back to the default value, if the [table parameter](spider-table-parameters.md) is not set.
  * `0` Use `utf8`.
  * `1` Uses the table character set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Default Table Value: `1`
* Range: `-1` to `1`
* DSN Parameter Name: `utc`

#### `spider_version`

* Description: The current Spider version. Removed in [MariaDB 10.9.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes) when the Spider version number was matched with the server version.
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Removed: [MariaDB 10.9.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)

#### `spider_wait_timeout`

* Description: Wait timeout in seconds of setting to remote server. `-1` means not set.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `604800`
* Range: `-1` to `2147483647`
* Introduced: [MariaDB 10.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1045-release-notes)

#### `spider_xa_register_mode`

* Description: Mode of XA transaction register into system table.
  * `0` Register all XA transactions
  * `1` Register only write XA transactions
* Command-line: `--spider-xa-register-mode=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1`
* Range: `0` to `1`
* Introduced: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)
* Deprecated: [MariaDB 10.7.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1074-release-notes), [MariaDB 10.8.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1083-release-notes)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
