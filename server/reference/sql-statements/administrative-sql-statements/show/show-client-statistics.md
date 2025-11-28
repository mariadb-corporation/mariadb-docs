---
description: >-
  View statistics on client connections. This statement displays metrics like
  bytes sent/received and busy time for connected clients.
---

# SHOW CLIENT\_STATISTICS

## Syntax

```sql
SHOW CLIENT_STATISTICS
```

## Description

{% tabs %}
{% tab title="Current" %}
The `SHOW CLIENT_STATISTICS` statement has effectively been replaced by the generic [SHOW TABLE STATISTICS](show-table-statistics.md) statement. The [information\_schema.CLIENT\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md) table holds statistics about client connections.
{% endtab %}

{% tab title="< 10.1.1" %}
The `SHOW CLIENT_STATISTICS` statement is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature. The [information\_schema.CLIENT\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md) table holds statistics about client connections.
{% endtab %}
{% endtabs %}

The [userstat](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#userstat) system variable must be set to 1 to activate this feature. See the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) and [information\_schema.CLIENT\_STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md) articles for more information.

## Example

```sql
SHOW CLIENT_STATISTICS\G
*************************** 1. row ***************************
                Client: localhost
     Total_connections: 35
Concurrent_connections: 0
        Connected_time: 708
             Busy_time: 2.5557979999999985
              Cpu_time: 0.04123740000000002
        Bytes_received: 3883
            Bytes_sent: 21595
  Binlog_bytes_written: 0
             Rows_read: 18
             Rows_sent: 115
          Rows_deleted: 0
         Rows_inserted: 0
          Rows_updated: 0
       Select_commands: 70
       Update_commands: 0
        Other_commands: 0
   Commit_transactions: 1
 Rollback_transactions: 0
    Denied_connections: 0
      Lost_connections: 0
         Access_denied: 0
         Empty_queries: 35
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
