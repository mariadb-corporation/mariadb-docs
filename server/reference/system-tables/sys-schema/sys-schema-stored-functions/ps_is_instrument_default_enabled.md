---
description: >-
  This function checks if a given Performance Schema instrument is enabled by
  default, returning YES or NO.
---

# ps\_is\_instrument\_default\_enabled

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_is_instrument_default_enabled(instrument)
```

## Description

`ps_is_instrument_default_enabled` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It returns `YES` if the given Performance Schema _instrument_ is enabled by default, and `NO` if it is not, does not exist, or is a NULL value.

## Examples

```sql
SELECT sys.ps_is_instrument_default_enabled('statement/sql/select');
+--------------------------------------------------------------+
| sys.ps_is_instrument_default_enabled('statement/sql/select') |
+--------------------------------------------------------------+
| YES                                                          |
+--------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_enabled('memory/sql/udf_mem');
+------------------------------------------------------------+
| sys.ps_is_instrument_default_enabled('memory/sql/udf_mem') |
+------------------------------------------------------------+
| NO                                                         |
+------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_enabled('memory/sql/nonexistent');
+----------------------------------------------------------------+
| sys.ps_is_instrument_default_enabled('memory/sql/nonexistent') |
+----------------------------------------------------------------+
| NO                                                             |
+----------------------------------------------------------------+

SELECT sys.ps_is_instrument_default_enabled(NULL);
+--------------------------------------------+
| sys.ps_is_instrument_default_enabled(NULL) |
+--------------------------------------------+
| NO                                         |
+--------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
