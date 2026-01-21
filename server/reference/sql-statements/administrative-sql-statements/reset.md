---
description: >-
  Clears internal server buffers, caches, and status variables. Resets state
  information like the query cache or replication status without a restart.
---

# RESET

## Syntax

```sql
RESET reset_option [, reset_option] ...
```

## Description

The `RESET` statement is used to clear the state of various server operations. You must have the [RELOAD privilege](../account-management-sql-commands/grant.md) to execute`RESET`.

`RESET` acts as a stronger version of the [FLUSH](flush-commands/flush.md) statement.

The different `RESET` options are:

| Option                                           | Description                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SLAVE \["connection\_name"] \[ALL]               | Deletes all [relay logs](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) from the slave and reset the replication position in the master [binary log](../../../server-management/server-monitoring-logs/binary-log/).                                                                                                                                                      |
| [MASTER](replication-statements/reset-master.md) | Deletes all old binary logs, makes the binary index file ([--log-bin-index](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md)) empty and creates a new binary log file. This is useful when you want to reset the master to an initial state. If you want to just delete old, not used binary logs, you should use the [PURGE BINARY LOGS](purge-binary-logs.md) command. |
| QUERY CACHE                                      | Removes all queries from [the query cache](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md). See also [FLUSH QUERY CACHE](flush-commands/flush-query-cache.md).                                                                                                                                                                                         |

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
