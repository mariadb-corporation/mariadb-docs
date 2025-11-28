# Using and Maintaining the Binary Log

See [Overview of the Binary Log](overview-of-the-binary-log.md) for a general overview of what the binary log is and [Activating the Binary Log](activating-the-binary-log.md) for how to make sure it's running on your system.

For details on using the binary log for replication, see the [Replication](../../../ha-and-performance/standard-replication/) section.

## Purging Log Files

To delete all binary log files on the server, run the [RESET MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md) command. To delete all binary logs before a certain datetime, or up to a certain number, use [PURGE BINARY LOGS](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md).

If a replica is active but has yet to read from a binary log file you attempt to delete, the statement will fail with an error. However, if the replica is not connected and has yet to read from a log file you delete, the file will be deleted, but the replica will be unable to continue replicating once it connects again.

Log files can also be removed automatically with the [expire\_logs\_days](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days) system variable. This is set to 0 by default (no removal), but can be set to a time, in days, after which a binary log file will be automatically removed. Log files will only be checked for being older than [expire\_logs\_days](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days) upon log rotation, so if your binary log only fills up slowly and does not reach [max\_binlog\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_size) on a daily basis, you may see older log files still being kept. You can also force log rotation, and so expiry deletes, by running [FLUSH BINARY LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) on a regular basis.\
Always set [expire\_logs\_days](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days) higher than any possible replica lag.

From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6), the [binlog\_expire\_logs\_seconds](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_expire_logs_seconds) variable allows more precise control over binlog deletion and takes precedence if both are non-zero.

If the binary log index file has been removed, or incorrectly manually edited, all of the above forms of purging log files will fail. The .index file is a plain text file and can be manually recreated or edited so that it lists only the binary log files that are present, in numeric/age order.

### Examples

```sql
PURGE BINARY LOGS TO 'mariadb-bin.000063';
```

```sql
PURGE BINARY LOGS BEFORE '2013-04-22 09:55:22';
```

### Safely Purging Binary Log Files While Replicating

To be sure replication is not broken while deleting log files, perform the following steps:

* Get a listing of binary log files on the primary by running [SHOW BINARY LOGS](../../../reference/sql-statements/administrative-sql-statements/show/show-binary-logs.md).
* Go to each replica server and run [SHOW SLAVE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) to check which binary log file each replica is currently reading.
* Find the earliest log file still being read by a replica. No log files before this one will be needed.
* If you wish, make a backup of the log files to be deleted
* Purge all log files before (not including) the file identified above.

## Limiting the Binlog Size

**MariaDB starting with** [**11.4**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4)

From [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4), it's possible to limit the size of the binlog by setting the [max\_binlog\_total\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_total_size) system variable. If not set to zero, the total size of the binlog will be stored in the [binlog\_disk\_use](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_disk_use) status variable. It's also possible to limit the size of a single binlog file by setting [max\_binlog\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_size).

## Binary Log Format

There are three formats for the binary log. The default is statement-based logging, while row-based logging and a mix of the two formats are also possible. See [Binary Log Formats](binary-log-formats.md) for a full discussion.

## Selectively Logging to the Binary Log

By default, all changes to data or data structure are logged. This behavior can be changed by starting the server with the `--binlog-ignore-db=database_name` or `--binlog-do-db=database_name` [options](../../starting-and-stopping-mariadb/mariadbd-options.md).

`--binlog-ignore-db=database_name` specified a database to ignore for logging purposes, while `--binlog-do-db=database_name` will not log any statements unless they apply to the specified database.

Neither option accepts comma-delimited lists of multiple databases as an option, since a database name can contain a comma. To apply to multiple databases, use the option multiple times.

`--binlog-ignore-db=database_name` behaves differently depending on whether statement-based or row-based logging is used. For statement-based logging, the server will not log any statement where the _default database_ is database\_name. The default database is set with the [USE](../../../reference/sql-statements/administrative-sql-statements/use-database.md) statement.

Similarly, `--binlog-do-db=database_name` also behaves differently depending on whether statement-based or row-based logging is used.

For statement-based logging, the server will only log statement where the _default database_ is database\_name. The default database is set with the [USE](../../../reference/sql-statements/administrative-sql-statements/use-database.md) statement.

For row-based logging, the server will log any updates to any tables in the named database/s, irrespective of the current database.

### Examples

Assume the server has started with the option `--binlog-ignore-db=employees`. The following example _is_ logged if statement-based logging is used, and _is not_ logged with row-based logging.

```sql
USE customers;
UPDATE employees.details SET bonus=bonus*1.2;
```

This is because statement-based logging examines the default database, in this case, `customers`. Since `customers` is not specified in the ignore list, the statement will be logged. If row-based logging is used, the example will not be logged as updates are written to the tables in the `employees` database.

Assume instead the server started with the option `--binlog-do-db=employees`. The following example _is not_ logged if statement-based logging is used, and _is_ logged with row-based logging.

```sql
USE customers;
UPDATE employees.details SET bonus=bonus*1.2;
```

This is again because statement-based logging examines the default database, in this case, `customers`. Since `customers` is not specified in the do list, the statement will not be logged. If row-based logging is used, the example will be logged as updates are written to the tables in the `employees` database.

## Effects of Full Disk Errors on Binary Logging

If MariaDB encounters a full disk error while trying to write to a binary log file, then it will keep retrying the write every 60 seconds. Log messages will get written to the error log every 600 seconds. For example:

```
2018-11-27  2:46:46 140278181563136 [Warning] mysqld: Disk is full writing '/var/lib/mariadb-bin.00001' (Errcode: 28 "No space left on device"). Waiting for someone to free space... (Expect up to 60 secs delay for server to continue after freeing disk space)
2018-11-27  2:46:46 140278181563136 [Warning] mysqld: Retry in 60 secs. Message reprinted in 600 secs
```

However, if MariaDB encounters a full disk error while trying to open a new binary log file, then it will disable binary logging entirely. A log message like the following will be written to the error log:

```
2018-11-27  3:30:49 140278181563136 [ERROR] Could not open '/var/lib/mariadb-bin.00002 for logging (error 28). Turning logging off for the whole duration of the MySQL server process. To turn it on again: fix the cause, shutdown the MySQL server and restart it.
2018-11-27  3:30:49 140278181563136 [ERROR] mysqld: Error writing file '(null)' (errno: 9 "Bad file descriptor")
2018-11-27  3:30:49 140278181563136 [ERROR] mysqld: Error writing file '(null)' (errno: 28 "No space left on device")
```

## See Also

* [PURGE LOGS](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
