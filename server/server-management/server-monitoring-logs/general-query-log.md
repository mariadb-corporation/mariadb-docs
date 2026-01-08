---
description: >-
  Describes the General Query Log, a comprehensive record of every query and
  connection event received by the server, useful for auditing and debugging but
  potentially high-volume.
---

# General Query Log

The general query log is a log of every SQL query received from a client, as well as each client connect and disconnect. Since it's a record of every query received by the server, it can grow large quite quickly.

However, if you only want a record of queries that change data, it might be better to use the [binary log](binary-log/) instead. One important difference is that the [binary log](binary-log/) only logs a query when the transaction is committed by the server, but the general query log logs a query immediately when it is received by the server.

## Enabling the General Query Log

The general query log is disabled by default.

To enable the general query log, set the [general\_log](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#general_log) system variable to `1`. It can be changed dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```
SET GLOBAL general_log=1;
```

It can also be set in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
general_log
```

## Configuring the General Query Log Filename

By default, the general query log is written to `${hostname}.log` in the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory. However, this can be changed.

One way to configure the general query log filename is to set the [general\_log\_file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file) system variable. It can be changed dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```
SET GLOBAL general_log_file='mariadb.log';
```

It can also be set in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
general_log
general_log_file=mariadb.log
```

If it is a relative path, then the [general\_log\_file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file) is relative to the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory.

However, the [general\_log\_file](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#general_log_file) system variable can also be an absolute path. For example:

```
[mariadb]
...
general_log
general_log_file=/var/log/mysql/mariadb.log
```

Another way to configure the general query log filename is to set the [log-basename](../starting-and-stopping-mariadb/mariadbd-options.md#log-basename) option, which configures MariaDB to use a common prefix for all log files (e.g. general query log, [slow query log](slow-query-log/), [error log](error-log.md), [binary logs](binary-log/), etc.). The general query log filename will be built by adding a `.log` extension to this prefix. This option cannot be set dynamically. It can be set in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
log-basename=mariadb
general_log
```

The [log-basename](../starting-and-stopping-mariadb/mariadbd-options.md#log-basename) cannot be an absolute path. The log file name is relative to the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) directory.

## Choosing the General Query Log Output Destination

The general query log can either be written to a file on disk, or it can be written to the [general\_log](../../reference/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md) table in the [mysql](../../reference/system-tables/the-mysql-database-tables/) database. To choose the general query log output destination, set the [log\_output](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable.

### Writing the General Query Log to a File

The general query log is output to a file by default. However, it can be explicitly chosen by setting the [log\_output](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable to `FILE`. It can be changed dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```
SET GLOBAL log_output='FILE';
```

It can also be set in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
log_output=FILE
general_log
general_log_file=queries.log
```

### Writing the General Query Log to a Table

The general query log can either be written to the [general\_log](../../reference/system-tables/the-mysql-database-tables/mysqlgeneral_log-table.md) table in the [mysql](../../reference/system-tables/the-mysql-database-tables/) database by setting the [log\_output](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output) system variable to `TABLE`. It can be changed dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```
SET GLOBAL log_output='TABLE';
```

It can also be set in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
log_output=TABLE
general_log
```

Some rows in this table might look like this:

```
SELECT * FROM mysql.general_log\G
*************************** 1. row ***************************
  event_time: 2014-11-11 08:40:04.117177
   user_host: root[root] @ localhost []
   thread_id: 74
   server_id: 1
command_type: Query
    argument: SELECT * FROM test.s
*************************** 2. row ***************************
  event_time: 2014-11-11 08:40:10.501131
   user_host: root[root] @ localhost []
   thread_id: 74
   server_id: 1
command_type: Query
    argument: SELECT * FROM mysql.general_log
...
```

See [Writing logs into tables](writing-logs-into-tables.md) for more information.

## Disabling the General Query Log for a Session

A user with the [SUPER](../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege can disable logging to the general query log for a connection by setting the [SQL\_LOG\_OFF](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_log_off) system variable to `1`. For example:

```
SET SESSION SQL_LOG_OFF=1;
```

## Disabling the General Query Log for Specific Statements

In [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes) and later, it is possible to disable logging to the general query log for specific types of statements by setting the [log\_disabled\_statements](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_disabled_statements) system variable. This option cannot be set dynamically. It can be set in a server [option group](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
log_output=FILE
general_log
general_log_file=queries.log
log_disabled_statements='slave,sp'
```

## Rotating the General Query Log on Unix and Linux

Unix and Linux distributions offer the [logrotate](https://linux.die.net/man/8/logrotate) utility, which makes it very easy to rotate log files. See [Rotating Logs on Unix and Linux](rotating-logs-on-unix-and-linux.md) for more information on how to use this utility to rotate the general query log.

## See Also

* [MariaDB audit plugin](../../reference/plugins/mariadb-audit-plugin/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
