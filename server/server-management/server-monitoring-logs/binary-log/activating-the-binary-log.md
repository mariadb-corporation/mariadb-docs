---
description: >-
  Instructions for enabling the binary log using the `--log-bin` option and
  configuring the log file basename and index file.
---

# Activating the Binary Log

To enable binary logging, start the server with the `[--log-bin [=name](../../../server-usage/replication-cluster-multi-master/standard-replication/replication-and-binary-log-system-variables.md)]` option.

If you specify a filename with an extension (for example `.log`), the extension will be silently ignored.

If you don't provide a name (which can, optionally, include an absolute path), the default is `datadir/log-basename-bin`, `datadir/mysql-bin` or `datadir/mariadb-bin` (the latter two if [--log-basename](../../starting-and-stopping-mariadb/mariadbd-options.md#log-basename) is not specified, and dependent on server version). `Datadir` is determined by the value of the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) system variable.

We strongly recommend you use either [--log-basename](../../starting-and-stopping-mariadb/mariadbd-options.md#log-basename) or specify a filename to ensure that [replication](../../../ha-and-performance/standard-replication/) doesn't stop if the hostname of the computer changes.

The directory storing the binary logs contains a binary log index, as well as the individual binary log files.

The binary log files have a series of numbers as filename extensions. Each additional binary log increments the extension number, so the oldest binary logs have lower numbers, and the most recent ones have higher numbers.

A new binary log, with a new extension, is created every time the server starts, the logs are flushed, or the maximum size is reached (determined by [max\_binlog\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_size)).

The binary log index file contains a master list of all the binary logs, in order. From [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114), if [GTID binlog indexing](../../../ha-and-performance/standard-replication/gtid.md#binlog-indexing) is enabled (the default), an additional index file (`.idx`) is present.

A sample listing from a directory containing the binary logs:

```
shell> ls -l 
total 100
...
-rw-rw---- 1 mysql adm 2098 Apr 19 00:46 mariadb-bin.000079
-rw-rw---- 1 mysql adm  332 Apr 19 00:56 mariadb-bin.000080
-rw-rw---- 1 mysql adm  347 Apr 19 07:36 mariadb-bin.000081
-rw-rw---- 1 mysql adm  306 Apr 20 07:15 mariadb-bin.000082
-rw-rw---- 1 mysql adm  332 Apr 20 07:41 mariadb-bin.000083
-rw-rw---- 1 mysql adm  373 Apr 21 07:56 mariadb-bin.000084
-rw-rw---- 1 mysql adm  347 Apr 21 09:09 mariadb-bin.000085
-rw-rw---- 1 mysql adm  398 Apr 21 21:24 mariadb-bin.000086
-rw-rw---- 1 mysql adm  816 Apr 21 17:05 mariadb-bin.index
```

The binary log index file has, by default, the same name as the individual binary logs, with the extension .index. You can specify an alternative name with the `--log-bin-index [=filename]` [option](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_index).

Clients with the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege (or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [BINLOG ADMIN](../../../reference/sql-statements/account-management-sql-statements/grant.md#binlog-admin) privilege, can disable and re-enable the binary log for the current session by setting the [sql\_log\_bin](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) variable.

```sql
SET sql_log_bin = 0;

SET sql_log_bin = 1;
```

## Binary Log Format

There are three formats for the binary log. The default is [mixed logging](binary-log-formats.md#mixed-logging), which is a mix of [statement-based](binary-log-formats.md#statement-based-logging) and [row-based logging](binary-log-formats.md#row-based-logging). See [Binary Log Formats](binary-log-formats.md) for a full discussion.

## See Also

* [Setting sql\_log\_bin](../../../reference/sql-statements/administrative-sql-statements/set-commands/set-sql_log_bin.md)
* [PURGE LOGS](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md) - Delete logs
* [FLUSH LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) - Close and rotate logs
* [GTID binlog indexing](../../../ha-and-performance/standard-replication/gtid.md#binlog-indexing)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
