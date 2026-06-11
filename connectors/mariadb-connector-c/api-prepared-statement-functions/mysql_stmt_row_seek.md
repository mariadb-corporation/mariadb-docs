---
description: >-
  mysql_stmt_row_seek positions the row cursor to an arbitrary row in a buffered
  prepared statement result set, returning the previous cursor offset for later
  restoration.
---

# mysql\_stmt\_row\_seek

## Syntax

```c
MYSQL_ROW_OFFSET mysql_stmt_row_seek(MYSQL_STMT * stmt,
     MYSQL_ROW_OFFSET offset);
```

## Parameters

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `offset` - row offset. This value can be obtained either by [`mysql_stmt_row_seek()`](mysql_stmt_row_seek.md) or [mysql\_stmt\_row\_tell()](mysql_stmt_row_tell.md).

## Description

Positions the row cursor to an arbitrary row in a result set which was obtained by [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md).&#x20;

## Return Value

Returns the previous row offset.

{% hint style="info" %}
The result set must be obtained by [mysql\_use\_result()](../api-functions/mysql_use_result.md).
{% endhint %}

## See Also

* [mysql\_stmt\_row\_tell()](mysql_stmt_row_tell.md)
* [mysql\_stmt\_store\_result](mysql_stmt_store_result.md)

{% @marketo/form formId="4316" %}
