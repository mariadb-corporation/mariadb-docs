---
description: >-
  This procedure truncates all Performance Schema summary tables, effectively
  resetting all aggregated performance statistics.
---

# ps\_truncate\_all\_tables

## Syntax

```
ps_truncate_all_tables(bool display)
```

## Description

`ps_truncate_all_tables` is a [stored procedure](../../../../server-usage/stored-routines/stored-procedures/) available with the [Sys Schema](../).

The procedure resets all aggregated instrumentation as a snapshot, producing a result set indicating the number of truncated tables. The boolean parameter _display_ specifies whether to display each [TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) statement before execution.

## Examples

```sql
CALL sys.ps_truncate_all_tables(false);
+---------------------+
| summary             |
+---------------------+
| Truncated 44 tables |
+---------------------+
```

```sql
CALL sys.ps_truncate_all_tables(true);
+------------------------------------------------------------------+
| status                                                           |
+------------------------------------------------------------------+
| Running: TRUNCATE TABLE performance_schema.events_stages_history |
+------------------------------------------------------------------+

...

+------------------------------------------------------------------------------+
| status                                                                       |
+------------------------------------------------------------------------------+
| Running: TRUNCATE TABLE performance_schema.table_lock_waits_summary_by_table |
+------------------------------------------------------------------------------+

+---------------------+
| summary             |
+---------------------+
| Truncated 44 tables |
+---------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
