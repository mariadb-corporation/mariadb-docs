---
description: >-
  mysql_row_tell returns the current row cursor offset for a buffered
  MariaDB result set, which can then be passed to mysql_row_seek to restore
  that position.
---

# mysql\_row\_tell

## Syntax

```c
MYSQL_ROW_OFFSET mysql_row_tell(MYSQL_RES * res);
```

* `res` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md).

## Description

Returns the row offset of a result cursor. The returned offset value can be used to reposition the result cursor by calling [mysql\_row\_seek()](mysql_row_seek.md).

{% hint style="info" %}
This function will not work if the result set was obtained by [mysql\_use\_result()](mysql_use_result.md).
{% endhint %}

## See also

* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_row\_seek()](mysql_row_seek.md)


{% @marketo/form formId="4316" %}
