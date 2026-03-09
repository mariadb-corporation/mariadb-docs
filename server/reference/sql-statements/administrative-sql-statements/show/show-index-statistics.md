---
description: >-
  View usage statistics for table indexes. This statement displays how often
  specific indexes are used, helping optimize query performance.
---

# SHOW INDEX\_STATISTICS

## Syntax

```sql
SHOW INDEX_STATISTICS
```

## Description

The [information\_schema.INDEX\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md) table shows statistics on index usage and makes it possible to do such things as locating unused indexes and generating the commands to remove them.

{% tabs %}
{% tab title="Current" %}
`SHOW INDEX_STATISTICS` is replaced by the generic [SHOW TABLE STATISTICS](show-table-statistics.md) statement.
{% endtab %}

{% tab title="< 10.1.1 / 5.3" %}
The `SHOW INDEX_STATISTICS` statement was introduced in [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.2/changes-improvements-in-mariadb-5-2) as part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. It was removed as a separate statement in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1), but effectively replaced by the generic [SHOW TABLE STATISTICS](show-table-statistics.md) statement.
{% endtab %}
{% endtabs %}

The [userstat](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information\_schema.INDEX\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md) table for more information.

## Example

```sql
SHOW INDEX_STATISTICS;
+--------------+-------------------+------------+-----------+
| Table_schema | Table_name        | Index_name | Rows_read |
+--------------+-------------------+------------+-----------+
| test         | employees_example | PRIMARY    |         1 |
+--------------+-------------------+------------+-----------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
