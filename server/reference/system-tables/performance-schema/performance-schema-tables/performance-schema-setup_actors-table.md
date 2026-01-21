---
description: >-
  The setup_actors table configures which foreground threads (users/hosts) are
  monitored, allowing for targeted instrumentation of specific accounts.
---

# Performance Schema setup\_actors Table

The `setup_actors` table contains information for determining whether monitoring should be enabled for new client connection threads.

The default size is 100 rows, which can be changed by modifying the [performance\_schema\_setup\_actors\_size](../performance-schema-system-variables.md#performance_schema_setup_actors_size) system variable at server startup.

If a row in the table matches a new foreground thread's client and host, the matching `INSTRUMENTED` column in the [threads](performance-schema-threads-table.md) table is set to either `YES` or`NO`, which allows selective application of instrumenting by host, by user, or combination thereof.

| Column | Description                                                           |
| ------ | --------------------------------------------------------------------- |
| HOST   | Host name, either a literal, or the % wildcard representing any host. |
| USER   | User name, either a literal or the % wildcard representing any name.  |
| ROLE   | Unused                                                                |

Initially, any user and host is matched:

```sql
SELECT * FROM performance_schema.setup_actors;
+------+------+------+
| HOST | USER | ROLE |
+------+------+------+
| %    | %    | %    |
+------+------+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
