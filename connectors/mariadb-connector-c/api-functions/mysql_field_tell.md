---
description: >-
  mysql_field_tell retrieves the current field cursor position in a result set,
  which can be passed to mysql_field_seek to restore that position.
---

# mysql\_field\_tell

## Syntax

```c
MYSQL_FIELD_OFFSET mysql_field_tell(MYSQL_RES * result);
```

## Parameter

* `result` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

Return the offset of the field cursor used for the last [mysql\_fetch\_field()](mysql_fetch_field.md) call. This value can be used as a parameter for the function [mysql\_field\_seek()](mysql_field_seek.md).

## Return Value

Returns the current offset of the field cursor

## See Also

* [mysql\_field\_seek()](mysql_field_seek.md)

{% @marketo/form formId="4316" %}
