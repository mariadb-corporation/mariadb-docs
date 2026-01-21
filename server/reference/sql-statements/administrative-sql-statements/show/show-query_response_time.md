---
description: >-
  View the distribution of query execution times. This statement groups queries
  into time-based buckets to analyze performance.
---

# SHOW QUERY\_RESPONSE\_TIME

## Syntax

```sql
SHOW QUERY_RESPONSE_TIME
```

## Description

It is possible to use `SHOW QUERY_RESPONSE_TIME` as an alternative for retrieving information from the [QUERY\_RESPONSE\_TIME](../../../plugins/other-plugins/query-response-time-plugin.md) plugin.

This was introduced as part of the [Information Schema plugin extension](../../../system-tables/information-schema/information-schema-tables/all-plugins-table-information-schema.md).

## Example

```sql
SHOW QUERY_RESPONSE_TIME;
+----------------+-------+----------------+
| Time           | Count | Total          |
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
