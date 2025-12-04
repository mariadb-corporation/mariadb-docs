# Spider Table Parameters

When a table uses the [Spider](./) storage engine, the following Spider table parameters can be set in the `COMMENT` clause of the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement. Many Spider table parameters have corresponding system variables, so they can be set for all Spider tables on the node. For additional information, see the [Spider System Variables](spider-system-variables.md) page.

From [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113), many table parameters can be set using dedicated Spider table options, see the Table Option Name fields below. From [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114), using the `COMMENT` clause is deprecated, as well as table parameters that do not have corresponding table options.

#### `access_balances`

* Description: Connection load balancing integer weight.
* Default Table Value: `0`
* DSN Parameter Name: `abl`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `active_link_count`

* Description: Number of active remote servers, for use in load balancing read connections
* Default Table Value: `all backends`
* DSN Parameter Name: `alc`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `auto_increment_mode`

* Description: The table level value of [spider\_auto\_increment\_mode](spider-system-variables.md#spider_auto_increment_mode)
* Table Option Name: `AUTO_INCREMENT_MODE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `bgs_mode`

* Description: The table level value of [spider\_bgs\_mode](spider-system-variables.md#spider_bgs_mode).
* Table Option Name: `BGS_MODE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `bulk_size`

* Description: The table level value of [spider\_bulk\_size](spider-system-variables.md#spider_bulk_size).
* Table Option Name: `BULK_SIZE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `bulk_update_size`

* Description: The table level value of [spider\_bulk\_update\_size](spider-system-variables.md#spider_bulk_update_size).
* Table Option Name: `BULK_UPDATE_SIZE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `casual_read`

* Description:
* Default Table Value:
* DSN Parameter Name:
* Introduced: Spider 3.2
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `connect_timeout`

* Description: The table level value of [spider\_connect\_timeout](spider-system-variables.md#spider_connect_timeout).
* Table Option Name: `CONNECT_TIMEOUT`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `database`

* Description: Database name for reference table that exists on remote backend server.
* Default Table Value: `local table database`
* DSN Parameter Name: `database`
* Table Option Name: `REMOTE_DATABASE`
* Table Option Introduced: [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes)

#### `default_file`

* Description: Configuration file used when connecting to remote servers. When the [default\_group](spider-table-parameters.md#default_group) table variable is set, this variable defaults to the values of the `--defaults-extra-file` or `--defaults-file` options. When the [default\_group](spider-table-parameters.md#default_group) table variable is not set, it defaults to `none`.
* Default Table Value: `none`
* DSN Parameter Name: `dff`
* Table Option Name: `DEFAULT_FILE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `default_group`

* Description: Group name in configuration file used when connecting to remote servers.
* Default Table Value: `none`
* DSN Parameter Name: `dfg`
* Table Option Name: `DEFAULT_GROUP`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `delete_all_rows_type`

* Description: The table level value of [spider\_delete\_all\_rows\_type](spider-system-variables.md#spider_delete_all_rows_type).
* Introduced: Spider 3.2
* Table Option Name: `DELETE_ALL_ROWS_TYPE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `force_bulk_delete`

* Description:
* Introduced: [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes)
* Table Option Name: `FORCE_BULK_DELETE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `force_bulk_update`

* Description:
* Introduced: [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes)
* Table Option Name: `FORCE_BULK_UPDATE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `host`

* Description: Host name of remote server.
* Default Table Value: `localhost`
* DSN Parameter Name: `host`
* Table Option Name: `REMOTE_HOST`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `idx000`

* Description: When using an index on Spider tables for searching, Spider uses this hint to search the remote table. The remote table index is related to the Spider table index by this hint. The number represented by `000` is the index ID, which is the number of the index shown by the [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) statement. `000` is the Primary Key. For instance, `idx000 "force index(PRIMARY)"` (in abbreviated format `idx000 "f PRIMARY"`).
  * `f` force index
  * `u` use index
  * `ig` ignore index
* Default Table Value: `none`
* Table Option Name: `IDX`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `link_status`

* Description: Change status of the remote backend server link.
  * `0` Doesn't change status.
  * `1` Changes status to `OK`.
  * `2` Changes status to `RECOVERY`.
  * `3` Changes status to no more in group communication.
* Default Table Value: `0`
* DSN Parameter Name: `lst`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `monitoring_bg_interval`

* Description: Interval of background monitoring in microseconds.
* Default Table Value: `10000000`
* DSN Parameter Name: `mbi`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `monitoring_bg_kind`

* Description: Kind of background monitoring to use.
  * `0` Disables background monitoring.
  * `1` Monitors connection state.
  * `2` Monitors state of table without `WHERE` clause.
  * `3` Monitors state of table with `WHERE` clause (currently unsupported).
* Default Table Value: `0`
* DSN Parameter Name: `mbk`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `monitoring_kind`

* Description: Kind of monitoring.
  * `0` Disables monitoring
  * `1` Monitors connection state.
  * `2` Monitors state of table without `WHERE` clause.
  * `3` Monitors state of table with `WHERE` clause (currently unsupported).
* Default Table Value: `0`
* DSN Parameter Name: `mkd`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `monitoring_limit`

* Description: Limits the number of records in the monitoring table. This is only effective when Spider monitors the state of a table, which occurs when the [monitoring\_kind](spider-table-parameters.md#monitoring_kind) table variable is set to a value greater than `1`.
* Default Table Value: `1`
* Range: `0` upwards
* DSN Parameter Name: `mlt`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `monitoring_server_id`

* Description: Preferred monitoring `@@server_id` for each backend failure. You can use this to geo-localize backend servers and set the first Spider monitoring node to contact for failover. In the event that this monitor fails, other monitoring nodes are contacted. For multiple copy backends, you can set a lazy configuration with a single MSI instead of one per backend.
* Default Table Value: `server_id`
* DSN Parameter Name: `msi`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `multi_split_read`

* Description: The table level value of [spider\_multi\_split\_read](spider-system-variables.md#spider_multi_split_read).
* Table Option Name: `MULTI_SPLIT_READ`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `net_read_timeout`

* Description: The table level value of [spider\_net\_read\_timeout](spider-system-variables.md#spider_net_read_timeout).
* Table Option Name: `NET_READ_TIMEOUT`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `net_write_timeout`

* Description: The table level value of [spider\_net\_write\_timeout](spider-system-variables.md#spider_net_write_timeout).
* Table Option Name: `NET_WRITE_TIMEOUT`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `password`

* Description: Remote server password.
* Default Table Value: `none`
* DSN Parameter Name: `password`
* Table Option Name: `REMOTE_PASSWORD`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `port`

* Description: Remote server port.
* Default Table Value: `3306`
* DSN Parameter Name: `port`
* Table Option Name: `REMOTE_PORT`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `priority`

* Description: Priority. Used to define the order of execution. For instance, Spider uses priority when deciding the order in which to lock tables on a remote server.
* Default Table Value: `1000000`
* DSN Parameter Name: `prt`
* Table Option Name: `PRIORITY`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `query_cache`

* Description: Uses the option for the [Query Cache](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) when issuing [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements to the remote server.
  * `0` No option used.
  * `1` Uses the [SQL\_CACHE](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md#sql_no_cache-and-sql_cache) option.
  * `2` Uses the [SQL\_NO\_CACHE](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md#sql_no_cache-and-sql_cache) option.
* Default Table Value: `0`
* DSN Parameter Name: `qch`
* Table Option Name: `QUERY_CACHE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `query_cache_sync`

* Description: A two-bit bitmap. Whether to pass the option for the [Query Cache](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) (if any) when issuing [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements to the remote server.
  * `0` No option passed.
  * `1` Passes the [SQL\_CACHE](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md#sql_no_cache-and-sql_cache) option, if specified in the query to the spider table.
  * `2` Passes the [SQL\_NO\_CACHE](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) option, if specified in the query to the spider table.
  * `3` Passes both the [SQL\_CACHE](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md#sql_no_cache-and-sql_cache) option and the [SQL\_NO\_CACHE](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) option, if specified in the query to the spider table.
* Default Table Value: `3`
* Table Option Name: `QUERY_CACHE_SYNC`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `read_rate`

* Description: Rate used to calculate the amount of time Spider requires when executing index scans.
* Default Table Value: `0.0002`
* DSN Parameter Name: `rrt`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `scan_rate`

* Description: Rate used to calculate the amount of time Spider requires when scanning tables.
* Default Table Value: `0.0001`
* DSN Parameter Name: `srt`
* Deprecated: [MariaDB 11.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-0-release-notes)

#### `server`

* Description: Server name. Used when generating connection information with [CREATE SERVER](../../../reference/sql-statements/data-definition/create/create-server.md) statements.
* Default Table Value: `none`
* DSN Parameter Name: `srv`
* Table Option Name: `REMOTE_SERVER`
* Table Option Introduced: [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes)

#### `skip_parallel_search`

* Description: The table level value of [spider\_skip\_parallel\_search](spider-system-variables.md#spider_skip_parallel_search).
* Table Option Name: `SKIP_PARALLEL_SEARCH`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `socket`

* Description: Remote server socket.
* Default Table Value: `none`
* DSN Parameter Name: `socket`
* Table Option Name: `REMOTE_SOCKET`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `ssl_ca`

* Description: Path to the Certificate Authority file.
* Default Table Value: `none`
* DSN Parameter Name: `sca`
* Table Option Name: `SSL_CA`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `ssl_capath`

* Description: Path to directory containing trusted TLS CA certificates in PEM format.
* Default Table Value: `none`
* DSN Parameter Name: `scp`
* Table Option Name: `SSL_CAPATH`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `ssl_cert`

* Description: Path to the certificate file.
* Default Table Value: `none`
* DSN Parameter Name: `scr`
* Table Option Name: `SSL_CERT`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `ssl_cipher`

* Description: List of allowed ciphers to use with [TLS encryption](../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md).
* Default Table Value: `none`
* DSN Parameter Name: `sch`
* Table Option Name: `SSL_CIPHER`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `ssl_key`

* Description: Path to the key file.
* Default Table Value: `none`
* DSN Parameter Name: `sky`
* Table Option Name: `SSL_KEY`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `ssl_verify_server_cert`

* Description: Enables verification of the server's Common Name value in the certificate against the host name used when connecting to the server.
  * `0` Disables verification.
  * `1` Enables verification.
* Default Table Value: `0`
* DSN Parameter Name: `svc`
* Table Option Name: `SSL_VSC`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `table`

* Description: Destination table name.
* Default Table Value: `Same table name`
* DSN Parameter Name: `tbl`
* Table Option Name: `REMOTE_TABLE`
* Table Option Introduced: [MariaDB 10.8.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-0-release-notes)

#### `table_count_mode`

* Description: for setting table flags HA\_STATS\_RECORDS\_IS\_EXACT and HA\_HAS\_RECORDS.
* Default Table Value: `0`
* Table Option Name: `TABLE_COUNT_MODE`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `username`

* Description: user name for the data node.
* Default Table Value: `Same user name`
* Table Option Name: `REMOTE_USERNAME`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `use_pushdown_udf`

* Description: The table level value of [spider\_use\_pushdown\_udf](spider-system-variables.md#spider_use_pushdown_udf).
* Table Option Name: `USE_PUSHDOWN_UDF`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `wrapper`

* Description: wrapper for the data node.
* Table Option Name: `WRAPPER`
* Table Option Introduced: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
