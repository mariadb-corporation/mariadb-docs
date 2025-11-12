# SHOW USER\_STATISTICS

## Syntax

```sql
SHOW USER_STATISTICS
```

## Description

{% tabs %}
{% tab title="Current" %}
The `SHOW USER_STATISTICS` statement is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. It was effectively replaced by the generic [SHOW information\_schema\_table](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/information-schema-plugins-show-and-flush-statements) statement. The [information\_schema.USER\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md) table holds statistics about user activity. You can use this table to find out such things as which user is causing the most load and which users are being abusive. You can also use this table to measure how close to capacity the server may be.
{% endtab %}

{% tab title="< 10.1.1" %}
The `SHOW USER_STATISTICS` statement is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. The [information\_schema.USER\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md) table holds statistics about user activity. You can use this table to find out such things as which user is causing the most load and which users are being abusive. You can also use this table to measure how close to capacity the server may be.
{% endtab %}
{% endtabs %}

The [userstat](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information\_schema.USER\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md) table for more information.

## Example

```sql
SHOW USER_STATISTICS\G
*************************** 1. row ***************************
                  User: root
     Total_connections: 1
Concurrent_connections: 0
        Connected_time: 3297
             Busy_time: 0.14113400000000006
              Cpu_time: 0.017637000000000003
        Bytes_received: 969
            Bytes_sent: 22355
  Binlog_bytes_written: 0
             Rows_read: 10
             Rows_sent: 67
          Rows_deleted: 0
         Rows_inserted: 0
          Rows_updated: 0
       Select_commands: 7
       Update_commands: 0
        Other_commands: 0
   Commit_transactions: 1
 Rollback_transactions: 0
    Denied_connections: 0
      Lost_connections: 0
         Access_denied: 0
         Empty_queries: 7
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
