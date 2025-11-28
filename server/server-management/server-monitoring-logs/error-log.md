# Error Log

The error log contains a record of critical errors that occurred during the server's operation, table corruption, start and stop information.

SQL errors can also be logged in a separate file using the [SQL\_ERROR\_LOG plugin](sql-error-log-plugin.md).

## Configuring the Error Log Output Destination

MariaDB always writes its error log, but the destination is configurable.

### Writing the Error Log to a File

To configure the error log to be written to a file, you can set the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable. You can configure a specific file name. However, if a specific file name is not configured, the log will be written to the `${hostname}.err` file in the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory by default.

The [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable can be set in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example, to write the error log to the default `${hostname}.err` file, you could configure the following:

```ini
[mariadb]
...
log_error
```

If you configure a specific file name as the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable, and if it is not an absolute path, then it will be relative to the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory. For example, if you configured the following, then the error log would be written to `mariadb.err` in the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory:

```ini
[mariadb]
...
log_error=mariadb.err
```

If it is a relative path, then the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) is relative to the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory.

However, the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable can also be an absolute path:

```ini
[mariadb]
...
log_error=/var/log/mysql/mariadb.err
```

Another way to configure the error log file name is to set the [log-basename](../starting-and-stopping-mariadb/mariadbd-options.md) option, which configures MariaDB to use a common prefix for all log files (e.g. [general query log](general-query-log.md), [slow query log](slow-query-log/), error log, [binary logs](binary-log/), etc.). The error log file name will be built by adding a `.err` extension to this prefix. For example, if you configured the following, then the error log would still be written to `mariadb.err` in the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory:

```ini
[mariadb]
...
log-basename=mariadb
log_error
```

The [log-basename](../starting-and-stopping-mariadb/mariadbd-options.md) cannot be an absolute path. The log file name is relative to the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory.

### Writing the Error Log to Stderr on Unix

On Unix, if the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable is not set, errors are written to `stderr`, which usually means that the log messages are output to the terminal that started `mariadbd`.

If the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable was set in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) or on the command-line, it can still be unset by specifying `--skip-log-error`.

### Writing the Error Log to Syslog on Unix

On Unix, the error log can also be redirected to the [syslog](https://linux.die.net/man/8/rsyslogd). How this is done depends on how you [start](https://mariadb.com/kb/en/) MariaDB.

#### Syslog with mariadbd-safe

If you [start](https://mariadb.com/kb/en/) MariaDB with [mariadbd-safe](../starting-and-stopping-mariadb/mariadbd-safe.md), the error log can be redirected to the syslog. See [mariadbd-safe: Configuring MariaDB to Write the Error Log to Syslog](../starting-and-stopping-mariadb/mariadbd-safe.md#configuring-mariadb-to-write-the-error-log-to-syslog) for more information.

#### Syslog with Systemd

If you [start](https://mariadb.com/kb/en/) MariaDB with [systemd](../starting-and-stopping-mariadb/systemd.md), the error log can also be redirected to the syslog. See [Systemd: Configuring MariaDB to Write the Error Log to Syslog](../starting-and-stopping-mariadb/systemd.md#configuring-mariadb-to-write-the-error-log-to-syslog) for more information.

[systemd](../starting-and-stopping-mariadb/systemd.md) also has its own logging system called the `journal`, and some errors may get logged there instead. See [Systemd:Systemd Journal](../starting-and-stopping-mariadb/systemd.md#systemd-journal) for more information.

### Writing the Error Log to Console on Windows

On Windows, if the [console](../starting-and-stopping-mariadb/mariadbd-options.md) option is specified, and if the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variable is not used, errors are written to the console. If both options are specified, the last option takes precedence.

### Writing the Error Log to the Windows Event Viewer

On Windows, error log messages are also written to the Windows Event Viewer. You can find MariaDB's error log messages by browsing **Windows Logs**, then selecting **Application** or **Application Log**, depending on the Windows version.

You can find MariaDB's error log messages by searching for the **Source** `MariaDB` (prior to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series), this was `MySQL`).

## Finding the Error Log

To find where the error log is stored, one can find the options used for the error log with:

```bash
mariadbd --print-defaults
```

or (from [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11))

```bash
my_print_defaults --mariadbd | grep log-error
```

or

```bash
my_print_defaults --mysqld | grep log-error
```

If the above don't help, check also if your system is set to [write to syslog](../starting-and-stopping-mariadb/systemd.md#configuring-mariadb-to-write-the-error-log-to-syslog), in which case you need to use [journalctl](../starting-and-stopping-mariadb/systemd.md#systemd-journal) to access it.

## Configuring the Error Log Verbosity

The default value of the [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) system variable is `2`.

The [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) system variable can be used to configure the verbosity of the error log. It can be changed dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL log_warnings=3;
```

It can also be set either on the command-line or in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```ini
[mariadb]
...
log_warnings=3
```

Some of the warnings included in each verbosity level are described below.

The [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) system variable only has an effect on some log messages. Some log messages are **always** written to the error log, regardless of the error log verbosity. For example, most warnings from the InnoDB storage engine are not affected by [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings). For a complete list of log messages affected by [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings), see the description of the [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) system variable.

### Verbosity Level 0

If [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) is `0`, many optional warnings will not be logged. However, this does not prevent all warnings from being logged, because there are certain core warnings that will always be written to the error log. For example:

* If [InnoDB strict mode](../../server-usage/storage-engines/innodb/innodb-strict-mode.md) is disabled, and if DDL is performed on a table that triggers a ["Row size too large" error](../../server-usage/storage-engines/innodb/innodb-row-formats/troubleshooting-row-size-too-large-errors-with-innodb.md), InnoDB logs a warning:

```
[Warning] InnoDB: Cannot add field col25 in table db1.tab because after 
  adding it, the row size is 8477 which is greater than maximum allowed 
  size (8126) for a record on index leaf page.
```

However, if [InnoDB strict mode](../../server-usage/storage-engines/innodb/innodb-strict-mode.md) is enabled, the same message will be logged as an error.

### Verbosity Level 1

Default until [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes). If [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) is `1`, many types of warnings are logged. Some useful warnings are:

* Replication-related messages:

```
[Note] Error reading relay log event: slave SQL thread was killed
[Note] Slave SQL thread exiting, replication stopped in log 
  'dbserver-2-bin.000033'   at position 181420; 
  GTID position '0-263316466-368886'
[Note] Slave I/O thread exiting, read up to log 
  'dbserver-2-bin.000034', position 642; 
  GTID position 0-263316466-368887
```

* Messages related to DNS lookup failures:

```
[Warning] IP address '192.168.1.193' 
  could not be resolved: Name or service not known
```

* Messages related to the [event scheduler](../../server-usage/triggers-events/event-scheduler/):

```
[Note] Event Scheduler: Loaded 0 events
```

* Messages related to [unsafe statements for statement-based replication](../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md):

```
[Warning] Unsafe statement written to the binary log using statement format since 
  BINLOG_FORMAT = STATEMENT. The statement is unsafe because 
  it uses a LIMIT clause. This 
  is unsafe because the set of rows included cannot be predicted.
```

Frequent warnings about [unsafe statements for statement-based replication](../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md) can cause the error log to grow very large. MariaDB will automatically detect frequent duplicate warnings about [unsafe statements for statement-based replication](../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md). After 10 identical warnings are detected, MariaDB will prevent that same warning from being written to the error log again for the next 5 minutes.

### Verbosity Level 2

Default from [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes). If [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) is `2`, a couple other different kinds of warnings are printed. For example:

* Messages related to access denied errors:

```
[Warning] Access denied for user 'root'@'localhost' (using password: YES)
```

* Messages related to connections that are aborted due to errors or timeouts:

```
[Warning] Aborted connection 35 to db: 'unconnected' user: 
  'user1@host1' host: '192.168.1.40' (Got an error writing communication packets)
[Warning] Aborted connection 36 to db: 'unconnected' user: 
  'user1@host2' host: '192.168.1.230' (Got an error writing communication packets)
[Warning] Aborted connection 38 to db: 'db1' user: 
  'user2' host: '192.168.1.60' (Unknown error) 
[Warning] Aborted connection 51 to db: 'db1' user: 
  'user2' host: '192.168.1.50' (Got an error reading communication packets)
[Warning] Aborted connection 52 to db: 'db1' user: 
  'user3' host: '192.168.1.53' (Got timeout reading communication packets)
```

* Messages related to table handler errors:

```
[Warning] Can't find record in 'tab1'.
[Warning] Can't write; duplicate key in table 'tab1'.
[Warning] Lock wait timeout exceeded; try restarting transaction.
[Warning] The number of locks exceeds the lock table size.
[Warning] Update locks cannot be acquired during a READ UNCOMMITTED transaction.
```

* Messages related to the files used to [persist replication state](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence):
  * Either the default `master.info` file or the file that is configured by the [master\_info\_file](../starting-and-stopping-mariadb/mariadbd-options.md) option.
  * Either the default `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_info_file) system variable.

```
[Note] Reading Master_info: '/mariadb/data/master.info'  
  Relay_info:'/mariadb/data/relay-log.info'
[Note] Initialized Master_info from '/mariadb/data/master.info'
[Note] Reading of all Master_info entries succeded
[Note] Deleted Master_info file '/mariadb/data/master.info'.
[Note] Deleted Master_info file '/mariadb/data/relay-log.info'.
```

* Messages about a master's [binary log dump thread](../../ha-and-performance/standard-replication/replication-threads.md#binary-log-dump-thread):

```
[Note] Start binlog_dump to slave_server(263316466), pos(, 4)
```

### Verbosity Level 3

If [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) is `3`, a couple other different kinds of warnings are printed. For example:

* Messages related to old-style language options:

```
[Warning] An old style --language value with language specific 
  part detected: /usr/local/mysql/data/
[Warning] Use --lc-messages-dir without language specific part instead.
```

* Messages related to [progress of InnoDB online DDL](https://mariadb.org/monitoring-progress-and-temporal-memory-usage-of-online-ddl-in-innodb/):

```
[Note] InnoDB: Online DDL : Start
[Note] InnoDB: Online DDL : Start reading clustered index of the table and 
  create temporary files
[Note] InnoDB: Online DDL : End of reading clustered index of the table and 
  create temporary files
[Note] InnoDB: Online DDL : Start merge-sorting index PRIMARY (1 / 3), 
  estimated cost : 18.0263
[Note] InnoDB: Online DDL : merge-sorting has estimated 33 runs
[Note] InnoDB: Online DDL : merge-sorting current run 1 estimated 33 runs
[Note] InnoDB: Online DDL : merge-sorting current run 2 estimated 17 runs
[Note] InnoDB: Online DDL : merge-sorting current run 3 estimated 9 runs
[Note] InnoDB: Online DDL : merge-sorting current run 4 estimated 5 runs
[Note] InnoDB: Online DDL : merge-sorting current run 5 estimated 3 runs
[Note] InnoDB: Online DDL : merge-sorting current run 6 estimated 2 runs
[Note] InnoDB: Online DDL : End of  merge-sorting index PRIMARY (1 / 3)
[Note] InnoDB: Online DDL : Start building index PRIMARY (1 / 3), 
  estimated cost : 27.0395
[Note] InnoDB: Online DDL : End of building index PRIMARY (1 / 3)
[Note] InnoDB: Online DDL : Completed
[Note] InnoDB: Online DDL : Start merge-sorting index ux1 (2 / 3), 
  estimated cost : 5.7895
[Note] InnoDB: Online DDL : merge-sorting has estimated 2 runs
[Note] InnoDB: Online DDL : merge-sorting current run 1 estimated 2 runs
[Note] InnoDB: Online DDL : End of  merge-sorting index ux1 (2 / 3)
[Note] InnoDB: Online DDL : Start building index ux1 (2 / 3), 
  estimated cost : 8.6842
[Note] InnoDB: Online DDL : End of building index ux1 (2 / 3)
[Note] InnoDB: Online DDL : Completed
[Note] InnoDB: Online DDL : Start merge-sorting index ix1 (3 / 3), 
  estimated cost : 6.1842
[Note] InnoDB: Online DDL : merge-sorting has estimated 3 runs
[Note] InnoDB: Online DDL : merge-sorting current run 1 estimated 3 runs
[Note] InnoDB: Online DDL : merge-sorting current run 2 estimated 2 runs
[Note] InnoDB: Online DDL : End of  merge-sorting index ix1 (3 / 3)
[Note] InnoDB: Online DDL : Start building index ix1 (3 / 3), 
  estimated cost : 9.2763
[Note] InnoDB: Online DDL : End of building index ix1 (3 / 3)
[Note] InnoDB: Online DDL : Completed
```

### Verbosity Level 4

If [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) is `4`, a couple other different kinds of warnings are printed. For example:

* Messages related to killed connections:

```
[Warning] Aborted connection 53 to db: 'db1' user: 
  'user2' host: '192.168.1.50' (KILLED)
```

* Messages related to all closed connections:

```
[Warning] Aborted connection 56 to db: 'db1' user: 
  'user2' host: '192.168.1.50' (CLOSE_CONNECTION)
```

* Messages related to released connections, such as when a transaction is committed and [completion\_type](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#completion_type) is set to `RELEASE`:

```
[Warning] Aborted connection 58 to db: 'db1' user: 
  'user2' host: '192.168.1.50' (RELEASE)
```

### Verbosity Level 9

If [log\_warnings](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings) is `9`, some **very** verbose warnings are printed. For example:

* Messages about initializing plugins:

```
[Note] Initializing built-in plugins
[Note] Initializing plugins specified on the command line
[Note] Initializing installed plugins
```

### MySQL's log\_error\_verbosity

MariaDB does not support the [log\_error\_verbosity](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_log_error_verbosity) system variable added in MySQL 5.7.

## Format

The error log begins with a line indicating where the data is being read from, for example:

```
240919 22:58:50 mysqld_safe Starting mariadbd daemon with databases from /home/ian/sandboxes/msb_11_7_0/data
```

Then, each item (note, warning or error) consists of a single line, containing the date (yyyy-mm-dd) and time, the thread ID, followed by the type of error (Note, Warning or Error) and the error message, for example:

```
2016-06-15 16:53:33 139651251140544 [Note] InnoDB: The InnoDB memory heap is disabled
```

Until [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes), the format only consisted of the date (yymmdd) and time, followed by the type of error (Note, Warning or Error) and the error message, for example:

```
160615 16:53:08 [Note] InnoDB: The InnoDB memory heap is disabled
```

The first item will always contain the source revision, a unique server id (from [MariaDB 10.5.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10-5-26-release-notes), [MariaDB 10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.19), [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.3), [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes), [MariaDB 11.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes)) and the process\_id, for example:

```
2024-09-19 22:58:50 0 [Note] Starting MariaDB 11.7.0-preview-MariaDB source revision 
  7391f7143b462b29ecdaee049c5ebdfd1aefa6d7 server_uid UdJQ5BCzAQiTopMoCz3yYsfU1lA= 
  as process 2307166
```

or

```
2024-05-18 16:05:33 0 [Note] Starting MariaDB 10.11.8-MariaDB source revision 
  3a069644682e336e445039e48baae9693f9a08ee as process 50774
```

## Rotating the Error Log on Unix and Linux

Unix and Linux distributions offer the [logrotate](https://linux.die.net/man/8/logrotate) utility, which makes it very easy to rotate log files. See [Rotating Logs on Unix and Linux](rotating-logs-on-unix-and-linux.md) for more information on how to use this utility to rotate the error log.

## Error Messages File

Many error messages are read from an error message file that contains localized error messages. If the server can't find this file when it starts up, you might see errors like the following:

```
[ERROR] Can't find messagefile '/usr/share/errmsg.sys'
```

If this error is occurring because the file is in a custom location, you can configure this location by setting the [lc\_messages\_dir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages_dir) system variable either on the command-line or in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```ini
[mariadb]
...
lc_messages_dir=/usr/share/mysql/
```

If you want to use a different locale for error messages, you can also set the [lc\_messages](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_messages) system variable:

```ini
[mariadb]
...
lc_messages_dir=/usr/share/mysql/
lc_messages=en_US
```

See [Setting the Language for Error Messages](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages.md) for more\
information.

## See Also

* [sql error log plugin](sql-error-log-plugin.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
