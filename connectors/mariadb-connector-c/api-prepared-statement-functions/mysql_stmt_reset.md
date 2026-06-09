---
description: >-
  mysql_stmt_reset resets a prepared statement on both client and server to its
  post-prepare state, clearing unbuffered results and errors while preserving
  bindings.
---

# mysql\_stmt\_reset

## Syntax

```c
my_bool mysql_stmt_reset(MYSQL_STMT * stmt);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md). Returns zero on success, nonzero if an error occurred.

## Description

Resets a prepared statement on the client and server to state after prepare.

## Return Value

Returns zero on success, 1 if an error occurred.

{% hint style="info" %}
* `mysql_stmt_reset()` resets the statement on the server, unbuffered result sets, and errors. Bindings and stored result sets will not be cleared. The latter one will be cleared when re-executing or closing the prepared statement.
* To reprepare a prepared statement with another SQL statement, use [mysql\_stmt\_prepare()](mysql_stmt_prepare.md).
{% endhint %}

## See Also

* [mysql\_stmt\_close()](mysql_stmt_close.md)
* [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)
* [mysql\_stmt\_execute()](mysql_stmt_execute.md)

{% @marketo/form formId="4316" %}
