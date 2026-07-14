---
description: >-
  mysql_stmt_free_result frees client-side result memory for a Connector/C
  prepared statement, complementing mysql_stmt_store_result to manage buffer
  lifecycle.
---

# mysql\_stmt\_free\_result

## Syntax

```c
my_bool mysql_stmt_free_result(MYSQL_STMT * stmt);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Frees stored result memory of a prepared statement.

## Return Value

Returns zero on success, non-zero on failure.

## See Also

* [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md)

{% @marketo/form formId="4316" %}
