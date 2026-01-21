---
description: >-
  This diagnostic procedure creates a report of the statements currently running
  or recently run on the server, aiding in performance troubleshooting.
---

# statement\_performance\_analyzer

## Syntax

```
statement_performance_analyzer(in_action,in_table, in_views)

# in_action ENUM('snapshot', 'overall', 'delta', 'create_tmp', 
                 'create_table', 'save', 'cleanup')
# in_table VARCHAR(129)
# in_views SET ('with_runtimes_in_95th_percentile', 'analysis', 
                'with_errors_or_warnings', 'with_full_table_scans', 
                'with_sorting', 'with_temp_tables', 'custom')
```

## Description

`statement_performance_analyzer` is a [stored procedure](../../../../server-usage/stored-routines/stored-procedures/) available with the [Sys Schema](../) which returns a report on running statements.

The following options from the [sys\_config](../sys-schema-sys_config-table.md) table impact the output:

* statement\_performance\_analyzer.limit - maximum number of rows (default `100`) returned for views that have no built-in limit.
* statement\_performance\_analyzer.view - custom query/view to be used (default `NULL`). If the statement\_performance\_analyzer.limit configuration option is greater than 0, there can't be a `LIMIT` clause in the query/view definition.

If the debug option is set (default `OFF`), the procedure will also produce debugging output.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
