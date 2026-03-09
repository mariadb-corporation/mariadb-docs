---
description: >-
  Complete Slow Query Log Overview guide for MariaDB. Complete reference
  documentation for implementation, configuration, and usage for production use.
---

# Slow Query Log Overview

The slow query log is a record of SQL queries that took a long time to perform. The log also provides the number of rows affected by slow queries.

{% hint style="info" %}
If your queries contain passwords, the slow query log can contain sensitive information, too. Ensure to store the log files in a safe location.

While MariaDB natively encrypts Binary Logs and Data files, it does not provide built-in encryption for the Slow Query or General Query logs. To secure these, administrators should either log to Internal Tables (combined with Data-at-Rest encryption) or utilize OS-level filesystem encryption.
{% endhint %}

## Enabling the Slow Query Log

The slow query log is disabled by default. To enable it, set [log\_slow\_query](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query) to `1`, using one of the following methods.

This turns on slow query logging immediately, but only until the next server restart:

```sql
SET GLOBAL slow_query_log=1;
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
slow_query_log
```

To verify that slow query logging is enabled, and to see which log file is used, issue this statement:

```sql
SHOW GLOBAL VARIABLES LIKE 'slow_query_log%';
+---------------------+-----------------------------------------------+
| Variable_name       | Value                                         |
+---------------------+-----------------------------------------------+
| slow_query_log      | ON                                            |
| slow_query_log_file | c525d37c-b2ff-4543-b06f-87012d142d44-slow.log |
+---------------------+-----------------------------------------------+
```

## Configuring the Filename

By default, the slow query log is written to `${hostname}-slow.log` (for instance, `c525d37c-b2ff-4543-b06f-87012d142d44-slow.log`), and stored in the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory. However, this can be changed.

Configure the slow query log filename by setting the [slow\_query\_log\_file](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file) system variable (or, from MariaDB 10.11, [log\_slow\_query\_file](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file)). It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL slow_query_log_file='mariadb-slow.log';
```

To make this permanent, configure it in a server [option group](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then restart the server:

```ini
[mariadb]
slow_query_log
slow_query_log_file=mariadb-slow.log
```

Setting a relative path, or just the filename, puts the log file in the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory. You can put it somewhere else by using an absolute path:

```ini
[mariadb]
slow_query_log
slow_query_log_file=/var/log/mysql/mariadb-slow.log
```

Another way to configure the slow query log filename is to set the [log-basename](../../starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) option, which configures MariaDB to use a common prefix for all log files (e.g. slow query log, [general query log](../general-query-log.md), [error log](../error-log.md), [binary logs](../binary-log/), etc.). The slow query log filename will be built by adding `-slow.log` to this prefix. This option cannot be set dynamically. It can be set in a server [option group](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```ini
[mariadb]
...
log-basename=mariadb
slow_query_log
```

{% hint style="info" %}
If you configure all log file basenames using [--log-basename](../../starting-and-stopping-mariadb/mariadbd-options.md#log-basename), you cannot use an absolute path – the log file name is always relative to the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory.
{% endhint %}

## Choosing the Output Destination

The slow query log can either be written to a file or to the [slow\_log](../../../reference/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) table in the [mysql](../../../reference/system-tables/the-mysql-database-tables/) database. To choose the slow query log output destination, set the [log\_output](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable.

To verify what logging method is used, issue this query:

```sql
SHOW GLOBAL VARIABLES LIKE 'log_output';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_output    | TABLE |
+---------------+-------+
```

### File Logging

File logging is the default. You can configure it explicitly by setting the [log\_output](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable to `FILE`. (For instance, to switch back from the [table logging](slow-query-log-overview.md#table-logging) method.)

Enable file logging until server restart:

```sql
SET GLOBAL log_output='FILE';
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
```

#### Parsing Specification (File Format)

When logging to a file, the Slow Query Log uses a multi-line format. Parsers must identify the start of a record and correctly separate the header metadata from the SQL query payload.

**Record Start Indicator:** Every log entry begins with the literal string: `# User@Host:`

**Header Specification:** The metadata section consists of several lines starting with a hash (`#`). These fields should be mapped as follows:

| Line  | Component Template                                | Key Fields                                              |
| ----- | ------------------------------------------------- | ------------------------------------------------------- |
| **1** | `# User@Host: {User}[{User}] @ {Host} [{IP}]`     | `User`, `Host`, `IP`                                    |
| **2** | `# Thread_id: {ID} Schema: {DB} QC_hit: {No/Yes}` | `Thread ID`, `Schema`, `QC_hit`                         |
| **3** | `# Query_time: {Float} Lock_time: {Float} ...`    | `Query_time`, `Lock_time`, `Rows_sent`, `Rows_examined` |

**SQL Payload:** The lines following the `#` headers contain the raw SQL statement.

* **Note:** The SQL query can span multiple lines.
* **Termination:** The record ends when the next `# User@Host:` indicator is encountered or the file ends.

**Parsing Example for Tool Developers**

A standard parser regex should look for the following sequence:

1. **Start:** `^# User@Host: .*`
2. **Metadata Capture:** Capture all lines starting with `#` until a line without a `#` is reached.
3. **Query Capture:** Everything from the first non-`#` line until the next record start.

### Table Logging

The slow query log can either be written to the [slow\_log](../../../reference/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) table in the [mysql](../../../reference/system-tables/the-mysql-database-tables/) database by setting the [log\_output](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable to `TABLE`. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL log_output='TABLE';
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
log_output=TABLE
slow_query_log
```

Display the slow query log by issuing this statement:

```sql
SELECT * FROM mysql.slow_log\G
...
*************************** 2. row ***************************
    start_time: 2014-11-11 07:56:28.721519
     user_host: root[root] @ localhost []
    query_time: 00:00:12.000215
     lock_time: 00:00:00.000000
     rows_sent: 1
 rows_examined: 0
            db: test
last_insert_id: 0
     insert_id: 0
     server_id: 1
      sql_text: SELECT SLEEP(12)
     thread_id: 74
...
```

See [Writing logs into tables](../writing-logs-into-tables.md) for more information.

## Disabling the Log for a Session

Any user can disable logging for a connection by setting the [slow\_query\_log](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log) system variable (or, from MariaDB 10.11, [log\_slow\_query](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query)) to `0`:

```sql
SET SESSION slow_query_log=0;
```

## Disabling the Log for Specific Statements

You can disable logging to the slow query log for specific types of statements by setting the [log\_slow\_disabled\_statements](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_disabled_statements) system variable. This option can only be set permanently, in a server [option group](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior, then restarting the server:

```ini
[mariadb]
log_output=FILE
slow_query_log
log_slow_disabled_statements='admin,call,slave,sp'
```

## Configuring the Slow Query Log Time

The time that defines a slow query can be configured by setting the [long\_query\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time) system variable (or, from MariaDB 10.11, [log\_slow\_query\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time)). It uses a units of seconds, with an optional milliseconds component. The default value is `10`. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL long_query_time=5.0;
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
slow_query_log
long_query_time=5.0
```

To verify this works as intended, you can force a "slow" query to happen. By default, MariaDB won't log a query unless it takes longer than a certain amount of time (10 seconds by default). Check your settings first (output abbreviated):

```sql
SHOW GLOBAL VARIABLES LIKE 'slow_query_log'; 
SHOW GLOBAL VARIABLES LIKE 'log_output'; 
SHOW GLOBAL VARIABLES LIKE 'long_query_time';
+----------------+-------+
| Variable_name  | Value |
+----------------+-------+
| slow_query_log | ON    |
+----------------+-------+
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_output    | TABLE |
+---------------+-------+
+-----------------+-----------+
| Variable_name   | Value     |
+-----------------+-----------+
| long_query_time | 10.000000 |
+-----------------+-----------+
```

Run a sleep statement longer than the threshhold of 10 seconds, then inspect the slow query log:

```sql
SELECT SLEEP(11);
+-----------+
| SLEEP(11) |
+-----------+
|         0 |
+-----------+
1 row in set (11.074 sec)

MariaDB [(none)]> SELECT * FROM mysql.slow_log \G
*************************** 1. row ***************************
    start_time: 2026-02-06 18:38:23.071314
     user_host: stefanhinz[stefanhinz] @ localhost []
    query_time: 00:00:11.073655
     lock_time: 00:00:00.000000
     rows_sent: 1
 rows_examined: 0
            db: 
last_insert_id: 0
     insert_id: 0
     server_id: 1
      sql_text: SELECT SLEEP(11)
     thread_id: 7
 rows_affected: 0
```

If you use [FILE logging](slow-query-log-overview.md#file-logging), check the contents of the log file in your terminal.

## Logging Queries That Don't Use Indexes

It can be beneficial to log queries that don't use indexes to the slow query log, since such queries can usually be optimized, either by adding an index or by doing a slight rewrite. The slow query log can be configured to log queries that don't use indexes regardless of their execution time, by adding the option `not_using_index` to [log\_slow\_filter](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter), or by setting the [log\_queries\_not\_using\_indexes](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes) system variable to `1`. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET @@log_slow_filter=concat(@@log_slow_filter,",not_using_index");
SET GLOBAL log_queries_not_using_indexes=ON;
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_queries_not_using_indexes=ON
```

As a significant number of queries can run quickly even without indexes, you can use the [min\_examined\_row\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit) system variable (or, from MariaDB 10.11, [log\_slow\_min\_examined\_row\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit)) with [log\_queries\_not\_using\_indexes](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes), to limit the logged queries to those having a material performance impact on the server.

## Excluding Queries That Examine Fewer Than a Minimum Row Limit

It can be beneficial to exclude queries that examine fewer than a minimum number of rows from the log. This can be done by setting the [min\_examined\_row\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit) system variable, or, from MariaDB 10.11, [log\_slow\_min\_examined\_row\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit). It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL min_examined_row_limit=100000;
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
min_examined_row_limit=100000
```

## Logging Slow Administrative Statements

By default, the slow query log logs administrative statements. To disable that, remove `admin` from the [log\_slow\_filter](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) system variable. Alternatively, set the [log\_slow\_admin\_statements](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements) system variable to `OFF`. The slow query log considers the following statements administrative: [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/), [ANALYZE TABLE](../../../reference/sql-statements/table-statements/analyze-table.md), [CHECK TABLE](../../../reference/sql-statements/table-statements/check-table.md), [CREATE INDEX](../../../reference/sql-statements/data-definition/create/create-index.md), [DROP INDEX](../../../reference/sql-statements/data-definition/drop/drop-index.md), [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md), and [REPAIR TABLE](../../../reference/sql-statements/table-statements/repair-table.md). This also includes [ALTER SEQUENCE](../../../reference/sql-structure/sequences/alter-sequence.md) statements.

You can dynamically enable this feature using a [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session) statement and setting it for just the current connection with `LOCAL`. Some examples:

```sql
SET SESSION log_slow_filter=replace(@@log_slow_filter,"admin","");
SET GLOBAL log_slow_admin_statements=ON;
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_admin_statements=ON
```

## Enabling the Slow Query Log for Specific Criteria

It is possible to enable logging to the slow query log for queries that meet specific criteria by configuring the [log\_slow\_filter](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) system variable. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

{% code overflow="wrap" %}
```sql
SET GLOBAL log_slow_filter='filesort,filesort_on_disk,tmp_table,tmp_table_on_disk';
```
{% endcode %}

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_filter=filesort,filesort_on_disk,tmp_table,tmp_table_on_disk
```

You can find all options for log\_slow\_filter at [log\_slow\_filter system variable](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) or at [Slow Query Log Extended Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics.md#log_slow_filter).

## Throttling the Slow Query Log

The slow query log can create a lot of I/O[^1], so it can be beneficial to throttle it in some cases. The slow query log can be throttled by configuring the [log\_slow\_rate\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit) system variable. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL log_slow_rate_limit=5;
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_rate_limit=5
```

## Configuring the Verbosity

There are a few optional pieces of information that can be included in the slow query log for each query. This optional information can be included by configuring the [log\_slow\_verbosity](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity) system variable. It can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL log_slow_verbosity='full';
```

{% include "../../../.gitbook/includes/to-make-this-permanent-con....md" %}

```ini
[mariadb]
...
log_output=FILE
slow_query_log
slow_query_log_file=slow-queries.log
long_query_time=5.0
log_slow_verbosity=query_plan,explain,engine
```

It is possible to have [EXPLAIN output printed in the slow query log](explain-in-the-slow-query-log.md).

## Viewing the Slow Query Log

Slow query logs written to file can be viewed with any text editor, or you can use the [mariadb-dumpslow](../../../clients-and-utilities/logging-tools/mariadb-dumpslow.md) tool, to ease the process by summarizing the information.

Queries that you find in the log are key queries to try to optimize by constructing a [more efficient query](../../../ha-and-performance/optimization-and-tuning/query-optimizations/) or by making [better use of indexes](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/).

For queries that appear in the log that cannot be optimized in the above ways, perhaps because they are simply very large selects, due to slow hardware, or very high lock/cpu/io contention, using shard/clustering/load balancing solutions, better hardware, or stats tables may help to improve these queries.

Slow query logs written to table can be viewed by querying the [slow\_log](../../../reference/system-tables/the-mysql-database-tables/mysql-slow_log-table.md) table.

## Variables Related to the Slow Query Log

* [slow\_query\_log](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log) - enable/disable the slow query log. Renamed to [log\_slow\_query](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query) from MariaDB 10.11.
* [log\_output](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output) - how the output will be written.
* [log\_slow\_admin\_statements](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements). Whether to log `OPTIMIZE`, `ANALYZE`, `ALTER`, and other administrative statements to the slow log. Deprecated from [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110), use [log\_slow\_filter](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) without admin.
* [slow\_query\_log\_file](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_query_log_file) - name of the slow query log file. Renamed to [log\_slow\_query\_file\_name](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_file_name) from MariaDB 10.11.0.
* [long\_query\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time) - time in seconds/microseconds defining a slow query. Renamed to [log\_slow\_query\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time) from MariaDB 10.11.0.
* [log\_queries\_not\_using\_indexes](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_queries_not_using_indexes) - whether or not to log queries that don't use indexes.
* [log\_slow\_admin\_statements](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements) - whether or not to log certain admin statements.
* [log\_slow\_disabled\_statements](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_disabled_statements) - types of statements that should not be logged in the slow query log.
* [min\_examined\_row\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#min_examined_row_limit) - minimum rows a query must examine to be slow. Renamed to [log\_slow\_min\_examined\_row\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit) from MariaDB 10.11.0.
* [log\_slow\_rate\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit) - permits a fraction of slow queries to be logged.
* [log\_slow\_verbosity](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity) - amount of detail in the log.
* [log\_slow\_filter](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_filter) - limit which queries to log.
* [log\_slow\_slave\_statements](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_slow_slave_statements) - log slow statements executed by replica thread to the slow log if it is open.

## Rotating the Slow Query Log on Unix and Linux

Unix and Linux distributions offer the [logrotate](https://linux.die.net/man/8/logrotate) utility, which makes it easy to rotate log files. See [Rotating Logs on Unix and Linux](../rotating-logs-on-unix-and-linux.md) for more information on how to use this utility to rotate the slow query log.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: I/O almost always refers to Disk I/O. Reading from and writing to storage is significantly slower than processing data in RAM. Therefore, excessive logging or poorly indexed queries increase "I/O Wait," which is often the primary bottleneck for database performance.
