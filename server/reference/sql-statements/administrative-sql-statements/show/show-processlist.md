---
description: >-
  View currently executing threads. This statement displays the ID, user, host,
  database, statement, time, and state of active connections.
---

# SHOW PROCESSLIST

## Syntax

```sql
SHOW [FULL] PROCESSLIST
```

## Description

`SHOW PROCESSLIST` shows which threads are running. You can also get this information from the [information\_schema.PROCESSLIST](../../../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table or the [mariadb-admin processlist](../../../../clients-and-utilities/administrative-tools/mariadb-admin.md) command. If you have the [PROCESS privilege](show-privileges.md), you can see all threads. Otherwise, you can see only your own threads (that is, threads associated with the MariaDB account that you are using). If you do not use the `FULL` keyword, only the first 100 characters of each statement are shown in the Info field.

The columns shown in `SHOW PROCESSLIST` are:

| Name     | Description                                                                                                                                                |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Id       | The client's thread ID.                                                                                                                                    |
| User     | The username associated with the process.                                                                                                                  |
| Host     | The host the client is connected to.                                                                                                                       |
| db       | The default database of the process (`NULL` if no default).                                                                                                |
| Command  | The command type. See [Thread Command Values](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-command-values.md). |
| Time     | The amount of time, in seconds, the process has been in its current state.                                                                                 |
| State    | See [Thread States](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-states/).                                     |
| Info     | The statement being executed.                                                                                                                              |
| Progress | The total progress of the process (0-100%) (see [Progress Reporting](show-processlist.md)).                                                                |

The [information\_schema.PROCESSLIST](../../../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table contains a number of additional columns. See `TIME_MS` column in [information\_schema.PROCESSLIST](../../../system-tables/information-schema/time_ms-column-in-information_schemaprocesslist.md) for differences in the `TIME` column between MariaDB and MySQL.

Note that the `PROGRESS` field from the information schema, and the `PROGRESS` field from `SHOW PROCESSLIST` display different results. `SHOW PROCESSLIST` shows the total progress, while the information schema shows the progress for the current stage only.

Threads can be killed using their `thread_id` or their `query_id`, with the [KILL](../kill.md) statement.

Since queries on this table are locking, if the [performance\_schema](../../../system-tables/performance-schema/) is enabled, you may want to query the [THREADS](../../../system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md) table instead.

## Examples

```sql
SHOW PROCESSLIST;
+----+-----------------+-----------+------+---------+------+------------------------+------------------+----------+
| Id | User            | Host      | db   | Command | Time | State                  | Info             | Progress |
+----+-----------------+-----------+------+---------+------+------------------------+------------------+----------+
|  2 | event_scheduler | localhost | NULL | Daemon  | 2693 | Waiting on empty queue | NULL             |    0.000 |
|  4 | root            | localhost | NULL | Query   |    0 | Table lock             | SHOW PROCESSLIST |    0.000 |
+----+-----------------+-----------+------+---------+------+------------------------+------------------+----------+
```

## See Also

[CONNECTION\_ID()](../../../sql-functions/secondary-functions/information-functions/connection_id.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
