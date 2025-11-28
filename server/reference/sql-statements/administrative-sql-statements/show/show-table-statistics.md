---
description: >-
  View usage statistics for tables. This statement displays metrics like rows
  read, changed, and updated for each table.
---

# SHOW TABLE\_STATISTICS

## Syntax

```sql
SHOW TABLE_STATISTICS
```

## Description

{% tabs %}
{% tab title="Current" %}
The `SHOW TABLE_STATISTICS` statement is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. It was effectively replaced by the generic `SHOW TABLE STATISTICS` statement. The [information\_schema.TABLE\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) table shows statistics on table usage.
{% endtab %}

{% tab title="< 10.1.1" %}
The `SHOW TABLE_STATISTICS` statement is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. The [information\_schema.TABLE\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) table shows statistics on table usage.
{% endtab %}
{% endtabs %}

The [userstat](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information\_schema.TABLE\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) articles for more information.

## Example

```sql
SHOW TABLE_STATISTICS\G
*************************** 1. row ***************************
           Table_schema: mysql
             Table_name: proxies_priv
              Rows_read: 2
           Rows_changed: 0
Rows_changed_x_#indexes: 0
*************************** 2. row ***************************
           Table_schema: test
             Table_name: employees_example
              Rows_read: 7
           Rows_changed: 0
Rows_changed_x_#indexes: 0
*************************** 3. row ***************************
           Table_schema: mysql
             Table_name: user
              Rows_read: 16
           Rows_changed: 0
Rows_changed_x_#indexes: 0
*************************** 4. row ***************************
           Table_schema: mysql
             Table_name: db
              Rows_read: 2
           Rows_changed: 0
Rows_changed_x_#indexes: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
