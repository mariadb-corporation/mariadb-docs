---
description: >-
  The TIME_MS column in the INFORMATION_SCHEMA.PROCESSLIST table displays the
  time a thread has been in its current state in milliseconds, offering higher
  precision than the standard TIME column.
---

# TIME\_MS column in INFORMATION\_SCHEMA.PROCESSLIST

In MariaDB, an extra column `TIME_MS` was added to the [INFORMATION\_SCHEMA.PROCESSLIST](information-schema-tables/information-schema-processlist-table.md) table. This column shows the same information as the column '`TIME`', but in units of milliseconds with microsecond precision (the unit and precision of the`TIME` column is one second).

For details about microseconds support in MariaDB, see [microseconds in MariaDB](../../sql-functions/date-time-functions/microseconds-in-mariadb.md).

The value displayed in the `TIME` and`TIME_MS` columns is the period of time that the given thread has been in its current state. Thus, it can be used to check for example how long a thread has been executing the current query, or for how long it has been idle.

```sql
SELECT id, TIME, time_ms, command, state FROM
   information_schema.processlist, (SELECT sleep(2)) t;
+----+------+----------+---------+-----------+
| id | time | time_ms  | command | state     |
+----+------+----------+---------+-----------+
| 37 |    2 | 2000.493 | Query   | executing |
+----+------+----------+---------+-----------+
```

Note that as a difference to MySQL, in MariaDB the `TIME` column (and also the `TIME_MS` column) are not affected by any setting of [@TIMESTAMP](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp). This means that it can be reliably used also for threads that change `@TIMESTAMP` (such as the [replication](../../../ha-and-performance/standard-replication/) SQL thread). See also [MySQL Bug #22047](https://bugs.mysql.com/bug.php?id=22047).

As a consequence of this, the `TIME` column of`SHOW FULL PROCESSLIST` and`INFORMATION_SCHEMA.PROCESSLIST` cannot be used to determine if a slave is lagging behind. For this, use instead the`Seconds_Behind_Master` column in the output of [SHOW SLAVE STATUS](../../sql-statements/administrative-sql-statements/show/show-replica-status.md).

The addition of the `TIME_MS` column is based on the microsec\_process patch, developed by [Percona](https://www.percona.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
