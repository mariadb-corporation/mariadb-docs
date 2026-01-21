---
description: >-
  The Information Schema PROCESSLIST table contains detailed information about
  running threads, including their current state and execution time.
---

# Information Schema PROCESSLIST Table

The [Information Schema](../) `PROCESSLIST` table contains information about running threads.

Similar information can also be returned with the [SHOW \[FULL\] PROCESSLIST](../../../sql-statements/administrative-sql-statements/show/show-processlist.md) statement, or the [mariadb-admin processlist](../../../../clients-and-utilities/administrative-tools/mariadb-admin.md) command.

It contains the following columns:

| Column            | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                | Connection identifier.                                                                                                                                                                                                                                                                                                                                                                          |
| USER              | MariaDB User.                                                                                                                                                                                                                                                                                                                                                                                   |
| HOST              | The hostname from which this client is connected.For Unix socket connections, this is `localhost`. For TCP/IP connections, the TCP port is appended (for instance, `192.168.1.17:58061` or `other-host.company.com:58061`). For the system user, this column is blank (`''`).                                                                                                                   |
| DB                | Default database, or `NULL` if none.                                                                                                                                                                                                                                                                                                                                                            |
| COMMAND           | Type of command running, corresponding to the Com\_ [status variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md). See [Thread Command Values](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-command-values.md).                                                                            |
| TIME              | Seconds that the thread has spent on the current `COMMAND` so far.                                                                                                                                                                                                                                                                                                                              |
| STATE             | Current state of the thread. See [Thread States](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-states/).                                                                                                                                                                                                                                             |
| INFO              | Statement the thread is executing, or `NULL` if none.                                                                                                                                                                                                                                                                                                                                           |
| TIME\_MS          | Time in milliseconds with microsecond precision that the thread has spent on the current `COMMAND` so far ([see more](../time_ms-column-in-information_schemaprocesslist.md)).                                                                                                                                                                                                                  |
| STAGE             | The stage the process is currently in.                                                                                                                                                                                                                                                                                                                                                          |
| MAX\_STAGE        | The maximum number of stages.                                                                                                                                                                                                                                                                                                                                                                   |
| PROGRESS          | The progress of the process within the current stage (0-100%).                                                                                                                                                                                                                                                                                                                                  |
| MEMORY\_USED      | Memory in bytes used by the thread.                                                                                                                                                                                                                                                                                                                                                             |
| MAX\_MEMORY\_USED | Maximum memory in bytes used by the thread.                                                                                                                                                                                                                                                                                                                                                     |
| EXAMINED\_ROWS    | Rows examined by the thread. Only updated by `UPDATE`, `DELETE`, and similar statements. For `SELECT` and other statements, the value remains zero.                                                                                                                                                                                                                                             |
| SENT\_ROWS        | Number of rows sent by the statement being executed. From [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes).                                                                                                                                                              |
| QUERY\_ID         | Query ID.                                                                                                                                                                                                                                                                                                                                                                                       |
| INFO\_BINARY      | Binary data information                                                                                                                                                                                                                                                                                                                                                                         |
| TID               | Thread ID ([MDEV-6756](https://jira.mariadb.org/browse/MDEV-6756))                                                                                                                                                                                                                                                                                                                              |
| TMP\_SPACE\_USED  | See [Limiting Size of Created Disk Temporary Files and Tables Overview](../../../../security/limiting-size-of-created-disk-temporary-files-and-tables/limiting-size-of-created-disk-temporary-files-and-tables-overview.md). From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115). |

Note that as a difference to MySQL, in MariaDB the `TIME`column (and also the `TIME_MS` column) are not affected by any setting of [@TIMESTAMP](../../../sql-functions/date-time-functions/timestamp-function.md). This means that it can be reliably used also for threads that change `@TIMESTAMP` (such as the [replication](../../../../ha-and-performance/standard-replication/) SQL thread). See also [MySQL Bug #22047](https://bugs.mysql.com/bug.php?id=22047).

As a consequence of this, the `TIME` column of`SHOW FULL PROCESSLIST` and`INFORMATION_SCHEMA.PROCESSLIST` cannot be used to determine if a slave is lagging behind. For this, use instead the`Seconds_Behind_Master` column in the output of [SHOW REPLICA STATUS](../../../sql-statements/administrative-sql-statements/show/show-replica-status.md).

Note that the `PROGRESS` field from the information schema, and the `PROGRESS` field from `SHOW PROCESSLIST` display different results. `SHOW PROCESSLIST` shows the total progress, while the information schema shows the progress for the current stage only. To retrieve a similar "total" Progress value from `information_schema.PROCESSLIST` as the one from `SHOW PROCESSLIST`, issue this statement:

```sql
SELECT CASE WHEN Max_Stage < 2 THEN Progress ELSE (Stage-1)/Max_Stage*100+Progress/Max_Stage END 
  AS Progress FROM INFORMATION_SCHEMA.PROCESSLIST;
```

## Example

```sql
SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST\G
*************************** 1. row ***************************
           ID: 9
         USER: msandbox
         HOST: localhost
           DB: NULL
      COMMAND: Query
         TIME: 0
        STATE: Filling schema table
         INFO: SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST
      TIME_MS: 0.351
        STAGE: 0
    MAX_STAGE: 0
     PROGRESS: 0.000
  MEMORY_USED: 85392
EXAMINED_ROWS: 0
     QUERY_ID: 15
  INFO_BINARY: SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST
          TID: 11838
*************************** 2. row ***************************
           ID: 5
         USER: system user
         HOST: 
           DB: NULL
      COMMAND: Daemon
         TIME: 0
        STATE: InnoDB shutdown handler
         INFO: NULL
      TIME_MS: 0.000
        STAGE: 0
    MAX_STAGE: 0
     PROGRESS: 0.000
  MEMORY_USED: 24160
EXAMINED_ROWS: 0
     QUERY_ID: 0
  INFO_BINARY: NULL
          TID: 3856
...
```

## See Also

* [TIME\_MS column in Information Schema SHOW PROCESSLIST](../time_ms-column-in-information_schemaprocesslist.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
