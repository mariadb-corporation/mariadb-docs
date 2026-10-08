---
description: >-
  The sys_get_config function retrieves the value of a specified configuration
  option from the sys_config table, or a user variable if set.
---

# sys\_get\_config

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.sys_get_config(name,default)
```

## Description

`sys_get_config` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

The function returns a configuration option value from the [sys\_config table](../sys-schema-sys_config-table.md). It takes two arguments; _name_, a configuration option name, and _default_, which is returned if the given option does not exist in the table.

Both arguments are `VARCHAR(128)` and can be `NULL`. Returns `NULL` if _name_ is `NULL`, or if the given option is not found and _default_ is `NULL`.

## Examples

```sql
SELECT sys.sys_get_config('ps_thread_trx_info.max_length',NULL);
+----------------------------------------------------------+
| sys.sys_get_config('ps_thread_trx_info.max_length',NULL) |
+----------------------------------------------------------+
| 65535                                                    |
+----------------------------------------------------------+
```

## See Also

* [Sys Schema sys\_config Table](../sys-schema-sys_config-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
