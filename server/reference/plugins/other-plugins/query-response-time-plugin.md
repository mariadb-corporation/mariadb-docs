# Query Response Time Plugin

The `query_response_time` plugin creates the [QUERY\_RESPONSE\_TIME](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-query_response_time-table.md) table in the [INFORMATION\_SCHEMA](../../sql-statements/administrative-sql-statements/system-tables/information-schema/) database. The plugin also adds the [SHOW QUERY\_RESPONSE\_TIME](../../sql-statements/administrative-sql-statements/show/show-query_response_time.md) and [FLUSH QUERY\_RESPONSE\_TIME\*](query-response-time-plugin.md#flushing-plugin-data) statements.

The [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) provides exact information about queries that take a long time to execute. However, sometimes there are a large number of queries that each take a very short amount of time to execute. This feature provides a tool for analyzing that information by counting and displaying the number of queries according to the length of time they took to execute.

This feature is based on Percona's [Response Time Distribution](https://www.percona.com/doc/percona-server/5.5/diagnostics/response_time_distribution.html).

## Installing the Plugin

This shared library actually consists of a number of different plugins. Prior to [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115):

* `QUERY_RESPONSE_TIME` - An INFORMATION\_SCHEMA plugin that exposes statistics.
* `QUERY_RESPONSE_TIME_AUDIT` - audit plugin, collects statistics.

Both plugins need to be installed to get meaningful statistics.

From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), there are the following additional plugins:

* `QUERY_RESPONSE_TIME_READ`
* `QUERY_RESPONSE_TIME_READ_WRITE`
* `QUERY_RESPONSE_TIME_WRITE`

Although the plugin's shared library is distributed with MariaDB by default, the plugins are not actually installed by MariaDB by default. There are two methods that can be used to install the plugins with MariaDB.

The first method can be used to install the plugin library without restarting the server. You can install the plugins dynamically by executing [INSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```
INSTALL SONAME 'query_response_time';
```

The second method can be used to tell the server to load the plugin library when it starts up. The plugins can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = query_response_time
```

Note that in both cases you have to activate data collection by changing the [query\_response\_time\_stats](query-response-time-plugin.md#query_response_time_stats) setting to ON, it is OFF by default even when the plugin library is loaded.

You can change the setting at runtime with

```
SET GLOBAL query_response_time_stats=ON;
```

or in the options file after the plugin has been loaded:

```
[mariadb]
...
plugin_load_add = query_response_time
query_response_time_stats=ON;
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```
UNINSTALL SONAME 'query_response_time';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Response Time Distribution

The user can define time intervals that divide the range 0 to positive infinity into smaller intervals and then collect the number of commands whose execution times fall into each of those intervals.

Each interval is described as:

```
(range_base ^ n; range_base ^ (n+1)]
```

The range\_base is some positive number (see Limitations). The interval is defined as the difference between two nearby powers of the range base.

For example, if the range base=10, we have the following intervals:

```
(0; 10 ^ -6], (10 ^ -6; 10 ^ -5], (10 ^ -5; 10 ^ -4], ..., 
  (10 ^ -1; 10 ^1], (10^1; 10^2]...(10^7; positive infinity]
```

or

```
(0; 0.000001], (0.000001; 0.000010], (0.000010; 0.000100], ..., 
  (0.100000; 1.0]; (1.0; 10.0]...(1000000; positive infinity]
```

For each interval, a count is made of the queries with execution times that fell into that interval.

You can select the range of the intervals by changing the range base. For example, for base range=2 we have the following intervals:

```
(0; 2 ^ -19], (2 ^ -19; 2 ^ -18], (2 ^ -18; 2 ^ -17], ..., 
  (2 ^ -1; 2 ^1], (2 ^ 1; 2 ^ 2]...(2 ^ 25; positive infinity]
```

or

```
(0; 0.000001], (0.000001, 0.000003], ..., 
  (0.25; 0.5], (0.5; 2], (2; 4]...(8388608; positive infinity]
```

Small numbers look strange (i.e., don’t look like powers of 2), because we lose precision on division when the ranges are calculated at runtime. In the resulting table, you look at the high boundary of the range.

For example, you may see:

```
SELECT * FROM INFORMATION_SCHEMA.QUERY_RESPONSE_TIME;
+----------------+-------+----------------+
| TIME           | COUNT | TOTAL          |
+----------------+-------+----------------+
|       0.000001 |     0 |       0.000000 |
|       0.000010 |    17 |       0.000094 |
|       0.000100 |  4301         0.236555 |
|       0.001000 |  1499 |       0.824450 |
|       0.010000 | 14851 |      81.680502 |
|       0.100000 |  8066 |     443.635693 |
|       1.000000 |     0 |       0.000000 |
|      10.000000 |     0 |       0.000000 |
|     100.000000 |     1 |      55.937094 |
|    1000.000000 |     0 |       0.000000 |
|   10000.000000 |     0 |       0.000000 |
|  100000.000000 |     0 |       0.000000 |
| 1000000.000000 |     0 |       0.000000 |
| TOO LONG       |     0 | TOO LONG       |
+----------------+-------+----------------+
```

This means there were:

```
* 17 queries with 0.000001 < query execution time < = 0.000010 seconds; total execution time of the 17 queries = 0.000094 seconds

* 4301 queries with 0.000010 < query execution time < = 0.000100 seconds; total execution time of the 4301 queries = 0.236555 seconds

* 1499 queries with 0.000100 < query execution time < = 0.001000 seconds; total execution time of the 1499 queries = 0.824450 seconds

* 14851 queries with 0.001000 < query execution time < = 0.010000 seconds; total execution time of the 14851 queries = 81.680502 seconds

* 8066 queries with 0.010000 < query execution time < = 0.100000 seconds; total execution time of the 8066 queries = 443.635693 seconds

* 1 query with 10.000000 < query execution time < = 100.0000 seconds; total execution time of the 1 query = 55.937094 seconds
```

## Using the Plugin

### Using the Information Schema Table

You can get the distribution by querying the [QUERY\_RESPONSE\_TIME](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-query_response_time-table.md) table in the [INFORMATION\_SCHEMA](../../sql-statements/administrative-sql-statements/system-tables/information-schema/) database. For example:

```
SELECT * FROM INFORMATION_SCHEMA.QUERY_RESPONSE_TIME;
```

You can also write more complex queries. For example:

```
SELECT c.count, c.time,
(SELECT SUM(a.count) FROM INFORMATION_SCHEMA.QUERY_RESPONSE_TIME as a 
   WHERE a.count != 0) as query_count,
(SELECT COUNT(*)     FROM INFORMATION_SCHEMA.QUERY_RESPONSE_TIME as b 
  WHERE b.count != 0) as not_zero_region_count,
(SELECT COUNT(*)     FROM INFORMATION_SCHEMA.QUERY_RESPONSE_TIME) as region_count
FROM INFORMATION_SCHEMA.QUERY_RESPONSE_TIME as c 
  WHERE c.count > 0;
```

Note: If [query\_response\_time\_stats](query-response-time-plugin.md#query_response_time_stats) is set to `ON`, then the execution times for these two SELECT queries will also be collected.

### Using the SHOW Statement

As an alternative to the [QUERY\_RESPONSE\_TIME](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-query_response_time-table.md) table in the [INFORMATION\_SCHEMA](../../sql-statements/administrative-sql-statements/system-tables/information-schema/) database, you can also use the [SHOW QUERY\_RESPONSE\_TIME](../../sql-statements/administrative-sql-statements/show/show-query_response_time.md) statement. For example:

```
SHOW QUERY_RESPONSE_TIME;
```

### Flushing Plugin Data

Flushing the plugin data does two things:

* Clears the collected times from the [QUERY\_RESPONSE\_TIME](../../sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-query_response_time-table.md) table in the [INFORMATION\_SCHEMA](../../sql-statements/administrative-sql-statements/system-tables/information-schema/) database.
* Reads the value of [query\_response\_time\_range\_base](query-response-time-plugin.md#query_response_time_range_base) and uses it to set the range base for the table.

Plugin data can be flushed with the [FLUSH QUERY\_RESPONSE\_TIME](../../sql-statements/administrative-sql-statements/flush-commands/flush.md) statement. For example:

```
FLUSH QUERY_RESPONSE_TIME;
```

Setting the [query\_response\_time\_flush](query-response-time-plugin.md#query_response_time_flush) system variable has the same effect. For example:

```
SET GLOBAL query_response_time_flush=1;
```

From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), it is possible to specify flushing read and/or write statements with the `FLUSH QUERY_RESPONSE_TIME_READ`, `FLUSH QUERY_RESPONSE_TIME_WRITE` and `FLUSH QUERY_RESPONSE_TIME_READ_WRITE` statements.

## Versions

| Version | Status | Introduced                                                                                                                                                                          |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Version | Status | Introduced                                                                                                                                                                          |
| 1.0     | Stable | [MariaDB 10.1.13](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/plugins/other-plugins/broken-reference/README.md)                                   |
| 1.0     | Gamma  | [MariaDB 10.0.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes) |
| 1.0     | Alpha  | [MariaDB 10.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1004-release-notes)   |

## System Variables

### `query_response_time_flush`

* Description: Updating this variable flushes the statistics and re-reads [query\_response\_time\_range\_base](query-response-time-plugin.md#query_response_time_range_base).
* Commandline: None
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

### `query_response_time_range_base`

* Description: Select base of log for `QUERY_RESPONSE_TIME` ranges. WARNING: variable change takes affect only after flush.
* Commandline: `--query-response-time-range-base=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10`
* Range: `2` to `1000`

### `query_response_time_exec_time_debug`

* Description: Pretend queries take this many microseconds. When 0 (the default) use the actual execution time.
  * This system variable is only available when the plugin is a [debug build](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/compiling-mariadb-for-debugging).
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `31536000`

### `query_response_time_session_stats`

* Description: Controls query response time statistics collection for the current session: ON - enable, OFF - disable, GLOBAL (default) - use [query\_response\_time\_stats](query-response-time-plugin.md#query_response_time_stats) value.
* Commandline: `query-response-time-session-stats=val]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `GLOBAL`
* Valid Values: `GLOBAL`, `ON`, `OFF`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

### `query_response_time_stats`

* Description: Enable or disable query response time statistics collecting.
* Commandline: `query-response-time-stats[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

## Options

### `query_response_time`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--query-response-time=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

### `query_response_time_audit`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--query-response-time-audit=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
