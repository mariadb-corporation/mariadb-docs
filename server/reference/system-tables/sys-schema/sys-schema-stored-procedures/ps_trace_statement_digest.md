---
description: >-
  This procedure traces a specific statement digest in the Performance Schema,
  capturing details about its execution for performance analysis.
---

# ps\_trace\_statement\_digest

## Syntax

```
ps_trace_statement_digest(in_digest, in_runtime, in_interval, in_start_fresh, in_auto_enable)
```

## Description

`ps_trace_statement_digest` is a [stored procedure](../../../../server-usage/stored-routines/stored-procedures/) available with the [Sys Schema](../).

Parameters:

* in\_digest `VARCHAR(32)`: The statement digest identifier to analyze.
* in\_runtime `INT`: Specifies the duration to run the analysis in seconds.
* in\_interval `DECIMAL(2,2)`: The analysis interval measured in seconds (including fraction values), at which snapshots are taken.
* in\_start\_fresh `BOOLEAN`: Determines whether to truncate the Performance Schema events\_statements\_history\_long and events\_stages\_history\_long tables before starting.
* in\_auto\_enable `BOOLEAN`: Determines whether to automatically enable required consumers.

## Examples

```sql
CALL sys.ps_trace_statement_digest('891ec6860f98ba46d89dd20b0c03652c', 5, 0.5, TRUE, TRUE);
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
