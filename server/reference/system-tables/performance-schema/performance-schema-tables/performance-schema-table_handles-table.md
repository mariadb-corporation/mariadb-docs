---
description: >-
  The table_handles table lists all open table handles, showing which threads
  are currently accessing which table instances and the locks they hold.
---

# Performance Schema table\_handles Table

{% hint style="info" %}
The `table_handles` table is available from MariaDB 10.5.2.
{% endhint %}

The `table_handles` table contains table lock information. It uses the `wait/lock/table/sql/handler` instrument, which is enabled by default.

Information includes which table handles are open, which sessions are holding the locks, and how they are locked.

The table is read-only, and [TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) cannot be performed on the table.

The maximum number of opened table objects is determined by the [performance\_schema\_max\_table\_handles](../performance-schema-system-variables.md#performance_schema_max_table_handles) system variable.

The table contains the following columns:

| Column                  | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| OBJECT\_TYPE            | The table opened by a table handle.                   |
| OBJECT\_SCHEMA          | The schema that contains the object.                  |
| OBJECT\_NAME            | The name of the instrumented object.                  |
| OBJECT\_INSTANCE\_BEGIN | The table handle address in memory.                   |
| OWNER\_THREAD\_ID       | The thread owning the table handle.                   |
| OWNER\_EVENT\_ID        | The event which caused the table handle to be opened. |
| INTERNAL\_LOCK          | The table lock used at the SQL level.                 |
| EXTERNAL\_LOCK          | The table lock used at the storage engine level.      |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
