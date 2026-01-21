---
description: >-
  The setup_consumers table controls which consumers (destinations) are enabled
  to store event data, managing the flow of metrics to history tables.
---

# Performance Schema setup\_consumers Table

Lists the types of consumers for which event information is available.

The `setup_consumers` table contains the following columns:

| Column  | Description                                                                                                                                  |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| NAME    | Consumer name                                                                                                                                |
| ENABLED | YES or NO for whether or not the consumer is enabled. You can modify this column to ensure that event information is added, or is not added. |

The table can be modified directly, or the server started with the option enabled, for example:

```ini
performance-schema-consumer-events-waits-history=ON
```

## Example

```sql
SELECT * FROM performance_schema.setup_consumers;

+--------------------------------+---------+
| NAME                           | ENABLED |
+--------------------------------+---------+
| events_stages_current          | NO      |
| events_stages_history          | NO      |
| events_stages_history_long     | NO      |
| events_statements_current      | YES     |
| events_statements_history      | NO      |
| events_statements_history_long | NO      |
| events_waits_current           | NO      |
| events_waits_history           | NO      |
| events_waits_history_long      | NO      |
| global_instrumentation         | YES     |
| thread_instrumentation         | YES     |
| statements_digest              | YES     |
+--------------------------------+---------+
```

## See Also

* [Sys Schema ps\_is\_consumer\_enabled function](../../sys-schema/sys-schema-stored-functions/ps_is_consumer_enabled.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
