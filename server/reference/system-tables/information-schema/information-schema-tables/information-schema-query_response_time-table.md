---
description: >-
  The Information Schema QUERY_RESPONSE_TIME table displays the distribution of
  query execution times, helping to identify performance bottlenecks.
---

# Information Schema QUERY\_RESPONSE\_TIME Table

## Description

The [Information Schema](../) `QUERY_RESPONSE_TIME` table contains information about queries that take a long time to execute . It is only available if the [QUERY\_RESPONSE\_TIME](../../../plugins/other-plugins/query-response-time-plugin.md) plugin has been installed.

It contains the following columns:

| Column | Description                                           |
| ------ | ----------------------------------------------------- |
| TIME   | Time interval                                         |
| COUNT  | Count of queries falling into the time interval       |
| TOTAL  | Total execution time of all queries for this interval |

See [QUERY\_RESPONSE\_TIME](../../../plugins/other-plugins/query-response-time-plugin.md) plugin for a full description.

The table is not a standard Information Schema table, and is a MariaDB extension.

[SHOW QUERY\_RESPONSE\_TIME](../../../sql-statements/administrative-sql-statements/show/show-query_response_time.md) is available as an alternative for retrieving the data.

## Example

```sql
SELECT * FROM information_schema.QUERY_RESPONSE_TIME;
+----------------+-------+----------------+
| TIME           | COUNT | TOTAL          |
+----------------+-------+----------------+
|       0.000001 |     0 |       0.000000 |
|       0.000010 |    17 |       0.000094 |
|       0.000100 |  4301         0.236555 |
|       0.001000 |  1499 |       0.824450 |
|       0.010000 | 14851 |      81.680502 |
|       0.100000 |  8066 |     443.635693 |
|       1.000000 |     0 |       0.000000 |
|      10.000000 |     0 |       0.000000 |
|     100.000000 |     1 |      55.937094 |
|    1000.000000 |     0 |       0.000000 |
|   10000.000000 |     0 |       0.000000 |
|  100000.000000 |     0 |       0.000000 |
| 1000000.000000 |     0 |       0.000000 |
| TOO LONG       |     0 | TOO LONG       |
+----------------+-------+----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
