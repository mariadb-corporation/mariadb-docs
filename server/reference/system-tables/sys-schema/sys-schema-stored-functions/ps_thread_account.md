---
description: >-
  This function returns the user account (username@hostname) associated with a
  specific Performance Schema thread ID.
---

# ps\_thread\_account

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.ps_thread_account(thread_id)
```

## Description

`ps_thread_account` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../) that returns the account (username@hostname) associated with the given _thread\_id_.

Returns `NULL` if the thread\_id is not found.

## Examples

```sql
SELECT sys.ps_thread_account(sys.ps_thread_id(CONNECTION_ID()));
+----------------------------------------------------------+
| sys.ps_thread_account(sys.ps_thread_id(CONNECTION_ID())) |
+----------------------------------------------------------+
| msandbox@localhost                                       |
+----------------------------------------------------------+

SELECT sys.ps_thread_account(sys.ps_thread_id(2042));
+-----------------------------------------------+
| sys.ps_thread_account(sys.ps_thread_id(2042)) |
+-----------------------------------------------+
| NULL                                          |
+-----------------------------------------------+

SELECT sys.ps_thread_account(sys.ps_thread_id(NULL));
+-----------------------------------------------+
| sys.ps_thread_account(sys.ps_thread_id(NULL)) |
+-----------------------------------------------+
| msandbox@localhost                            |
+-----------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
