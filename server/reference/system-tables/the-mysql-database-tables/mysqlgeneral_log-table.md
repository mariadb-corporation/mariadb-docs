---
description: >-
  The mysql.general_log table captures a record of all SQL statements received
  by the server when general query logging is enabled and written to tables.
---

# mysql.general\_log Table

The `mysql.general_log` table stores the contents of the [General Query Log](../../../server-management/server-monitoring-logs/general-query-log.md) if general logging is active and the output is being written to table (see [Writing logs into tables](../../../server-management/server-monitoring-logs/writing-logs-into-tables.md)).

It contains the following fields:

| Field         | Type             | Null | Key | Default               | Description                  |
| ------------- | ---------------- | ---- | --- | --------------------- | ---------------------------- |
| event\_time   | timestamp(6)     | NO   |     | CURRENT\_TIMESTAMP(6) | Time the query was executed. |
| user\_host    | mediumtext       | NO   |     | NULL                  | User and host combination.   |
| thread\_id    | int(11)          | NO   |     | NULL                  | Thread id.                   |
| server\_id    | int(10) unsigned | NO   |     | NULL                  | Server id.                   |
| command\_type | varchar(64)      | NO   |     | NULL                  | Type of command.             |
| argument      | mediumtext       | NO   |     | NULL                  | Full query.                  |

## Example

```sql
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
