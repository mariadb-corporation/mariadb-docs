# Slow Query Log Extended Statistics

## Overview

* Added extra logging to slow log of 'Thread\_id, Schema, Query Cache hit, Rows sent and Rows examined'
* Added optional logging to slow log, through log\_slow\_verbosity, of query plan statistics
* Added new session variables log\_slow\_rate\_limit, log\_slow\_verbosity, log\_slow\_filter
* Added log-slow-file as synonym for 'slow-log-file', as most slow-log variables starts with 'log-slow'
* Added log-slow-time as synonym for long-query-time.

## Session Variables

### log\_slow\_verbosity

You can set the verbosity of what's logged to the slow query log by setting the [log\_slow\_verbosity](../../system-variables/server-system-variables.md#log_slow_verbosity) variable to a combination of the following values:

* `All` (From [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-16-release-notes))
  * Enable all verbosity options.
* `Query_plan`
  * For select queries, log information about the query plan. This includes "Full\_scan", "Full\_join", "Tmp\_table", "Tmp\_table\_on\_disk", "Filesort", "Filesort\_on\_disk" and number of "Merge\_passes during sorting"
* `explain`
  * EXPLAIN output is logged in the slow query log. See [explain-in-the-slow-query-log](../../../../server-management/server-monitoring-logs/slow-query-log/explain-in-the-slow-query-log.md) for details.
* `Innodb` (From [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-15-release-notes). Before that this option did nothing)
  * Kept for compatibility. Same as `engine`.
* `engine` (From [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-15-release-notes))
  * Writes statistics from the storage engine. This includes:

| Option            | Description                                                                | Engine |
| ----------------- | -------------------------------------------------------------------------- | ------ |
| Option            | Description                                                                | Engine |
| Pages\_accessed   | Number of pages accessed from page buffer (innodb-buffer-pool / key cache) | InnoDB |
| Pages\_updated    | Number of pages updated in memory                                          | InnoDB |
| Pages\_read\_time | Milliseconds spend reading pages from storage                              | InnoDB |
| Old\_rows\_read   | Number of retrieval of old versions of rows in the engine (versioning)     | InnoDB |
| Engine\_time      | Milliseconds spent inside engine calls (read\_row / read\_next\_row etc)   | All    |



* `Warnings` (From [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-16-release-notes))
  * Print all errors, warnings and notes related to statement, up to `log_slow_max_warnings` lines.
* `full`.
  * Old shortcut to enable all the verbosity options

The default value for `log_slow_verbosity` is ' ', to be compatible with MySQL 5.1.

The possible values for `log_slow_verbosity are`innodb,query\_plan,explain,engine,warnings`. Multiple options are separated by ','.`  log\_slow\_verbosity is not supported when log\_output='TABLE'.

In the future we will add more `engine` statistics and also support for other engines.

### log\_slow\_filter

You can define which queries to log to the slow query log by setting the variable [log\_slow\_filter](../../system-variables/server-system-variables.md#log_slow_filter) to a combination of the following values:

* `All` (From [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-16-release-notes))
  * Enable all filter options. `log_slow_filter` will be shown as having all options set.
* `admin`
  * Log administrative statements (create, optimize, drop etc...)
  * [log\_slow\_admin\_statements](../../system-variables/server-system-variables.md#log_slow_admin_statements) maps to this option.
* `filesort`
  * Log statement if it uses filesort
* `filesort_on_disk`
  * Log statement if it uses filesort that needs temporary tables on disk
* `filesort_priority_queue` (from [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes))
  * Log statement if it uses filesort with priority\_queue (filesort can either use disk or priority queue).
* `full_join`
  * Log statements that doesn't uses indexes to join tables
* `full_scan`
  * Log statements that uses full table scans
* `not_using_index` (From [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes))
  * Logs queries that don't use an index, or that perform a full index scan where the index doesn't limit the number of rows
  * Disregards long\_query\_time, unlike other options!
  * [log\_queries\_not\_using\_indexes](../../system-variables/server-system-variables.md#log_queries_not_using_indexes) maps to this option
* `query_cache`
  * Log statements that are resolved by the query cache
* `query_cache_miss`
  * Log statements that are not resolved by the query cache
* `tmp_table`
  * Log statements that uses in memory temporary tables
* `tmp_table_on_disk`
  * Log statements that uses temporary tables on disk

Multiple options are separated by ','. If you don't specify any options everything will be logged (same as setting the value to `All`

### log\_slow\_rate\_limit

The [log\_slow\_rate\_limit](../../system-variables/server-system-variables.md#log_slow_rate_limit) variable limits logging to the slow query log by not logging every query (only one query / log\_slow\_rate\_limit is logged). This is mostly useful when debugging and you get too much information to the slow query log.

Note that in any case, only queries that takes longer than **log\_slow\_time** or**long\_query\_time**' are logged (as before).

### log\_slow\_max\_warnings

**MariaDB starting with** [**10.6.16**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-16-release-notes)

If one enables the warning option for `log_slow_verbosity`, all notes and warnings for a slow query will also be added to the slow query log. This is very usable when one has enabled warnings for [Notes when an index cannot be used](https://github.com/mariadb-corporation/docs-server/blob/test/server/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/broken-reference/README.md).`log_slow_max_warnings` limits the number of warnings printed to the slow query log per query. The default value is 10.

## Credits

Part of this addition is based on the[microslow](https://www.percona.com/percona-builds/Percona-SQL-5.0/Percona-SQL-5.0-5.0.87-b20/patches/microslow_innodb.patch)\
patch from [Percona](https://www.percona.com/).

## See also

* [Notes when an index cannot be used because of type conversions](https://github.com/mariadb-corporation/docs-server/blob/test/server/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/broken-reference/README.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
