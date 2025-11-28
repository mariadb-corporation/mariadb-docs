---
description: >-
  This function checks whether a specific user account is enabled for
  instrumentation in the Performance Schema setup_actors table.
---

# ps\_is\_account\_enabled

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_is_account_enabled(host,user)
```

## Description

`ps_is_account_enabled` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It takes _host_ and _user_ arguments, and returns an ENUM('YES','NO') depending on whether Performance Schema instrumentation for the given account is enabled.

## Examples

```sql
SELECT sys.ps_is_account_enabled('localhost', 'root');
+------------------------------------------------+
| sys.ps_is_account_enabled('localhost', 'root') |
+------------------------------------------------+
| YES                                            |
+------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
