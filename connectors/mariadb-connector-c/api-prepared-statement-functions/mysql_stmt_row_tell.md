---
description: >-
  mysql_stmt_row_tell returns the current row cursor offset of a buffered
  prepared statement result set, which can be passed to mysql_stmt_row_seek
  to restore the position.
---

# mysql\_stmt\_row\_tell

## Syntax

```c
MYSQL_ROW_OFFSET mysql_stmt_row_tell(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns the row offset of a result cursor. The returned offset value can be used to reposition the result cursor by calling [mysql\_stmt\_row\_seek()](mysql_stmt_row_seek.md).

{% hint style="info" %}
This function can be used for buffered result sets only, which can be obtained by executing the [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md) function.
{% endhint %}

## See Also

* [mysql\_stmt\_row\_seek()](mysql_stmt_row_seek.md)
* [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md)


{% @marketo/form formId="4316" %}
