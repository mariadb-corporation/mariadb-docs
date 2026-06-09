---
description: >-
  mysql_stmt_param_metadata retrieves parameter metadata for a prepared
  statement handle, returning a MYSQL_RES pointer that describes the bound
  parameters.
---

# mysql\_stmt\_param\_metadata

## Syntax

```c
MYSQL_RES * mysql_stmt_param_metadata(MYSQL_STMT * stmt);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Return Value

Always returns `NULL`.

{% @marketo/form formId="4316" %}
