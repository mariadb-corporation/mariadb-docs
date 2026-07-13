---
description: >-
  mysql_stmt_next_result advances to the next result set when a prepared
  statement returns multiple results, enabling traversal of multi-statement
  query output.
---

# mysql\_stmt\_next\_result

## Syntax

```c
int mysql_stmt_next_result(MYSQL_STMT * stmt);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Prepares next result set from a previous call to [mysql\_stmt\_execute()](mysql_stmt_execute.md) which can be retrieved by [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md).

## Return Value

Returns zero on success, `-1` if there are no more result sets, and a positive value if an error occurred.

{% hint style="info" %}
* The function [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md) indicates if further result sets are available.
* If the execution of a stored procedure produced multiple result sets the return value of [mysql\_stmt\_errno()](mysql_stmt_errno.md)/[mysql\_stmt\_error()](mysql_stmt_error.md) might change and there will be no result set available.
{% endhint %}

## See Also

* [mysql\_stmt\_execute()](mysql_stmt_execute.md)
* [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md)

{% @marketo/form formId="4316" %}
