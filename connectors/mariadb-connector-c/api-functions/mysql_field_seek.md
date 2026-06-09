---
description: >-
  mysql_field_seek sets the field cursor to a given column offset in a MariaDB
  result set, controlling which field mysql_fetch_field returns next.
---

# mysql\_field\_seek

## Syntax

```c
MYSQL_FIELD_OFFSET mysql_field_seek(MYSQL_RES * result,
                                    MYSQL_FIELD_OFFSET offset);
```

## Parameters

* `result` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).
* `offset` - the field number. This number must be in the range from `0`..`number of fields - 1`.

## Description

Sets the field cursor to the given offset. The next call to [mysql\_fetch\_field()](mysql_fetch_field.md) will retrieve the field definition of the column associated with that offset.

## Return Value

Returns the previous value of the field cursor.

{% hint style="info" %}
* The number of fields can be obtained from [mysql\_field\_count()](mysql_field_count.md).
* To move the field cursor to the first field offset parameter should be null.
{% endhint %}

## See Also

* [mysql\_field\_tell()](mysql_field_tell.md)

{% @marketo/form formId="4316" %}
