---
description: >-
  Official PURGE BINARY LOGS syntax: delete binlogs using TO 'log_name' or
  BEFORE datetime_expr, replica read constraints, and SHOW BINARY LOGS commands.
---

# PURGE BINARY LOGS

## Syntax

```sql
PURGE { BINARY | MASTER } LOGS
    { TO 'log_name' | BEFORE datetime_expr }
```

## Description

The `PURGE BINARY LOGS` statement deletes all the [binary log](../../../server-management/server-monitoring-logs/binary-log/) files listed in the log index file prior to the specified log file name ordate. `BINARY` and `MASTER` are synonyms.Deleted log files also are removed from the list recorded in the index file, sothat the given log file becomes the first in the list.

The datetime expression is in the format 'YYYY-MM-DD hh:mm:ss'.

If a replica is active but has yet to read from a binary log file you attempt to delete, the statement will fail with an error. However, if the replica is not connected and has yet to read from a log file you delete, the file will be deleted, but the replica will be unable to continue replicating once it connects again.

This statement has no effect if the server was not started with the [--log-bin](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin) option to enable binary logging.

{% tabs %}
{% tab title="Current" %}
To list the binary log files on the server, use [SHOW BINARY LOGS](show/show-binary-logs.md). To see which files they are reading, use [SHOW REPLICA STATUS](show/show-replica-status.md). You can only delete the files that are older than the oldest file that is used by the slaves.
{% endtab %}

{% tab title="< 10.5.1" %}
To list the binary log files on the server, use [SHOW BINARY LOGS](show/show-binary-logs.md). To see which files they are reading, use [SHOW SLAVE STATUS](show/show-replica-status.md). You can only delete the files that are older than the oldest file that is used by the slaves.
{% endtab %}
{% endtabs %}

To delete all binary log files, use [RESET MASTER](replication-statements/reset-master.md).To move to a new log file (for example if you want to remove the current log file), use [FLUSH LOGS](flush-commands/flush.md) before you execute `PURGE LOGS`.

If the [expire\_logs\_days](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#expire_logs_days) server system variable is not set to 0, the server automatically deletes binary log files after the given number of days. From MariaDB 10.6, the [binlog\_expire\_logs\_seconds](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_expire_logs_seconds) variable allows more precise control over binlog deletion, and takes precedence if both are non-zero.

{% tabs %}
{% tab title="Current" %}
Requires the [BINLOG ADMIN](../account-management-sql-statements/grant.md#binlog-admin) privilege.
{% endtab %}

{% tab title="< 10.5.2" %}
Requires the SUPER privilege.
{% endtab %}
{% endtabs %}

## Examples

```sql
PURGE BINARY LOGS TO 'mariadb-bin.000063';
```

```sql
PURGE BINARY LOGS BEFORE '2013-04-21';
```

```sql
PURGE BINARY LOGS BEFORE '2013-04-22 09:55:22';
```

## See Also

* [Using and Maintaining the Binary Log](../../../server-management/server-monitoring-logs/binary-log/using-and-maintaining-the-binary-log.md)
* [FLUSH LOGS](flush-commands/flush.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}

