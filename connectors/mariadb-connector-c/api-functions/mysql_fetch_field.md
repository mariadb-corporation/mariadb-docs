---
description: >-
  mysql_fetch_field returns the definition of one result set column as a
  MYSQL_FIELD pointer; call it repeatedly to iterate over all columns in the
  result set.
---

# mysql\_fetch\_field

## Syntax

```c
MYSQL_FIELD * mysql_fetch_field(MYSQL_RES * result);
```

## Parameter

* `result` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

Returns the definition of one column of a result set as a pointer to a MYSQL\_FIELD structure. Call this function repeatedly to retrieve information about all columns in the result set.

## Return Value

A pointer of a `MYSQL_FIELD` structure, or NULL if there are no more fields.

{% hint style="info" %}
The field order will be reset if you execute a new SELECT query.

In case only information for a specific field is required the field can be selected by using the [mysql\_field\_seek()](mysql_field_seek.md) function or obtained by [mysql\_fetch\_field\_direct()](mysql_fetch_field_direct.md) function.
{% endhint %}

## See Also

* [mysql\_field\_seek()](mysql_field_seek.md)
* [mysql\_field\_tell()](mysql_field_tell.md)
* [mysql\_fetch\_field\_direct()](mysql_fetch_field_direct.md)
* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_use\_result()](mysql_use_result.md)

{% @marketo/form formId="4316" %}
