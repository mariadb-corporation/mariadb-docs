---
description: >-
  This function checks if a specific Performance Schema instrument is timed by
  default, returning YES or NO based on the server's default configuration.
---

# ps\_is\_instrument\_default\_timed

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_is_instrument_default_timed(instrument)
```

## Description

`ps_is_instrument_default_timed` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It returns `YES` if the given Performance Schema _instrument_ is timed by default, and `NO` if it is not, does not exist, or is a `NULL` value.

## Examples

```sql
SELECT sys.ps_is_instrument_default_timed('statement/sql/select');
+------------------------------------------------------------+
| sys.ps_is_instrument_default_timed('statement/sql/select') |
+------------------------------------------------------------+
| YES                                                        |
+------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_timed('memory/sql/udf_mem');
+----------------------------------------------------------+
| sys.ps_is_instrument_default_timed('memory/sql/udf_mem') |
+----------------------------------------------------------+
| NO                                                       |
+----------------------------------------------------------+

SELECT sys.ps_is_instrument_default_timed('memory/sql/nonexistent');
+-------------------------------------------------------------+
| sys.ps_is_instrument_default_timed('memory/sql/udf_memsds') |
+-------------------------------------------------------------+
| NO                                                          |
+-------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_timed(NULL);
+------------------------------------------+
| sys.ps_is_instrument_default_timed(NULL) |
+------------------------------------------+
| NO                                       |
+------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
