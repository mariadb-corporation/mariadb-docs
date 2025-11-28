---
description: >-
  The metrics view consolidates key performance metrics from Global Status,
  InnoDB Metrics, and memory summaries into a single unified table.
---

# metrics Sys Schema View

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

The `metrics` view contains global status variables (as found in the [Performance Schema global\_status Table](../../performance-schema/performance-schema-tables/performance-schema-global_status-table.md)), [InnoDB](../../../../server-usage/storage-engines/innodb/) metrics (as found in the [Information Schema INNODB\_METRICS Table](../../information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md), current and total memory allocation, based on the Performance Schema memory instrumentation, as well the current time in human readable and Unix timestamp formats.

It contains the following columns:

| Column          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Variable\_name  | The name of the metric. One of the [VARIABLE\_NAME column](../../performance-schema/performance-schema-tables/performance-schema-global_status-table.md) if a global\_status table, the [NAME column](../../information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) if an InnoDB metric, or a description for other metrics.                                                                                                                                                                                                                                                                                                                                                    |
| Variable\_value | The metric value. One of the [VARIABLE\_VALUE column](../../performance-schema/performance-schema-tables/performance-schema-global_status-table.md) if a global status variable, the [COUNT column](../../information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) for InnoDB metrics, the related column from the [Performance Schema memory\_summary\_global\_by\_event\_name table](../../performance-schema/performance-schema-tables/performance-schema-memory_summary_global_by_event_name-table.md), the value of [NOW(3)](../../../sql-functions/date-time-functions/now.md) or [UNIX\_TIMESTAMP(NOW(3))](../../../sql-functions/date-time-functions/unix_timestamp.md). |
| Type            | Metric type. One of Global Status, InnoDB Metrics - % (with % being the value of the [SUBSYSTEM column](../../information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) in the INNODB\_METRICS table, Performance Schema or System Time                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Enabled         | Whether the metric is enabled. Always YES for global status variables and the current time. For InnoDB metrics, YES only if the [STATUS column of the INNODB\_METRICS table](../../information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md), otherwise NO. For memory metrics: YES, NO or PARTIAL (for metrics where not all memory/% instruments are enabled). Performance Schema memory instruments are always enabled)                                                                                                                                                                                                                                                        |

## Example

```sql
SELECT * FROM sys.metrics\G
*************************** 1. row ***************************
 Variable_name: aborted_clients
Variable_value: 0
          Type: Global Status
       Enabled: YES
*************************** 2. row ***************************
 Variable_name: aborted_connects
Variable_value: 0
          Type: Global Status
       Enabled: YES

...

*************************** 578. row ***************************
 Variable_name: trx_undo_slots_used
Variable_value: 0
          Type: InnoDB Metrics - transaction
       Enabled: YES
*************************** 579. row ***************************
 Variable_name: NOW()
Variable_value: 2024-09-09 16:16:08.745
          Type: System Time
       Enabled: YES
*************************** 580. row ***************************
 Variable_name: UNIX_TIMESTAMP()
Variable_value: 1725891368.745
          Type: System Time
       Enabled: YES
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
