# Optimizer Trace Overview

## Usage

This feature produces a trace as a JSON document for any [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md)/[UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md)/[DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) containing information about decisions taken by the optimizer during the optimization phase (choice of table access method, various costs, transformations, etc). This feature helps to explain why some decisions were taken by the optimizer and why some were rejected.

## Associated System Variables

* [optimizer\_trace=’enabled=on/off’](../../system-variables/server-system-variables.md#optimizer_trace)
  * Default value is off
* [optimizer\_trace\_max\_mem\_size](../../system-variables/server-system-variables.md#optimizer_trace_max_mem_size)= value
  * Default value: 1048576
* [optimizer\_record\_context](../../system-variables/server-system-variables.md#optimizer_record_context){=1|0}
  * Default value: OFF. From [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1).

## INFORMATION\_SCHEMA.OPTIMIZER\_TRACE

Each connection stores a trace from the last executed statement. One can view the trace by reading the [Information Schema OPTIMIZER\_TRACE table](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-optimizer_trace-table.md).

Structure of the optimizer trace table:

```
SHOW CREATE TABLE INFORMATION_SCHEMA.OPTIMIZER_TRACE \G
*************************** 1. row ***************************
       Table: OPTIMIZER_TRACE
Create Table: CREATE TEMPORARY TABLE `OPTIMIZER_TRACE` (
  `QUERY` longtext NOT NULL DEFAULT '',
  `TRACE` longtext NOT NULL DEFAULT '',
  `MISSING_BYTES_BEYOND_MAX_MEM_SIZE` int(20) NOT NULL DEFAULT 0,
  `INSUFFICIENT_PRIVILEGES` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=Aria DEFAULT CHARSET=utf8 PAGE_CHECKSUM=0
```

## Optimizer Trace Contents

See [Optimizer Trace Guide](optimizer-trace-guide.md) for an overview of what one can find in the trace.

## Traceable Queries

These include [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md), [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md), [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) as well as their multi-table variants and all of the preceding prefixed by [EXPLAIN](../../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) and [ANALYZE](../../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement.md).

## Enabling Optimizer Trace

To enable optimizer trace run:

```
SET optimizer_trace='enabled=on';
```

## Memory Usage

Each trace is stored as a string. It is extended (with realloc()) as the optimization progresses and appends data to it. The [optimizer\_trace\_max\_mem\_size](../../system-variables/server-system-variables.md#optimizer_trace_max_mem_size) variable sets a limit on the total amount of memory used by the current trace.

\
If this limit is reached, the current trace isn't extended (so it will be incomplete), and the MISSING\_BYTES\_BEYOND\_MAX\_MEM\_SIZE column will show the number of bytes missing from this trace.

## Privilege Checking

In complex scenarios where the query uses SQL SECURITY DEFINER views or stored routines, it may be that a user is denied from seeing the trace of its query because it lacks some extra privileges on those objects. In that case, the trace will be shown as empty and the INSUFFICIENT\_PRIVILEGES column will show "1".

## Limitations

Currently, only one trace is stored. It is not possible to trace the sub-statements of a stored routine; only the statement at the top level is traced.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
