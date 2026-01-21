---
description: >-
  The mysql.slow_log table records details of queries that exceed the
  long_query_time threshold when slow query logging to tables is enabled.
---

# mysql.slow\_log Table

**System tables should not normally be edited directly. Use the related SQL statements instead.**

The `mysql.slow_log` table stores the contents of the [Slow Query Log](../../../server-management/server-monitoring-logs/slow-query-log/) if slow logging is active and the output is being written to table (see [Writing logs into tables](../../../server-management/server-monitoring-logs/writing-logs-into-tables.md)).

It contains the following fields:

| Field            | Type                | Null | Key | Default               | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---------------- | ------------------- | ---- | --- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start\_time      | timestamp(6)        | NO   |     | CURRENT\_TIMESTAMP(6) | Time the query began.                                                                                                                                                                                                                                                                                                                                                     |
| user\_host       | mediumtext          | NO   |     | NULL                  | User and host combination.                                                                                                                                                                                                                                                                                                                                                |
| query\_time      | time(6)             | NO   |     | NULL                  | Total time the query took to execute.                                                                                                                                                                                                                                                                                                                                     |
| lock\_time       | time(6)             | NO   |     | NULL                  | Total time the query was locked.                                                                                                                                                                                                                                                                                                                                          |
| rows\_sent       | int(11)             | NO   |     | NULL                  | Number of rows sent.                                                                                                                                                                                                                                                                                                                                                      |
| rows\_examined   | int(11)             | NO   |     | NULL                  | Number of rows examined.                                                                                                                                                                                                                                                                                                                                                  |
| db               | varchar(512)        | NO   |     | NULL                  | Default database.                                                                                                                                                                                                                                                                                                                                                         |
| last\_insert\_id | int(11)             | NO   |     | NULL                  | [last\_insert\_id](../../sql-functions/secondary-functions/information-functions/last_insert_id.md).                                                                                                                                                                                                                                                                      |
| insert\_id       | int(11)             | NO   |     | NULL                  | Insert id.                                                                                                                                                                                                                                                                                                                                                                |
| server\_id       | int(10) unsigned    | NO   |     | NULL                  | The server's id.                                                                                                                                                                                                                                                                                                                                                          |
| sql\_text        | mediumtext          | NO   |     | NULL                  | Full query.                                                                                                                                                                                                                                                                                                                                                               |
| thread\_id       | bigint(21) unsigned | NO   |     | NULL                  | Thread id.                                                                                                                                                                                                                                                                                                                                                                |
| rows\_affected   | int(11)             | NO   |     | NULL                  | Number of rows affected by an [UPDATE](../../sql-statements/data-manipulation/changing-deleting-data/update.md) or [DELETE](../../sql-statements/data-manipulation/changing-deleting-data/delete.md) (from [MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes)) |

## Example

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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
