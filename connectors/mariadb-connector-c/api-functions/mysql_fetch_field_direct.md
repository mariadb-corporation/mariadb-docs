---
description: >-
  mysql_fetch_field_direct returns a MYSQL_FIELD pointer for a specific column
  in a result set, identified by its zero-based field number.
---

# mysql\_fetch\_field\_direct

## Syntax

```c
MYSQL_FIELD * mysql_fetch_field_direct(MYSQL_RES * res,
                                       unsigned int fieldnr);
```

## Parameters

* `res` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).
* `fieldnr` - the field number. This value must be within the range from 0 to number of fields - 1

## Description

Returns a pointer to a `MYSQL_FIELD` structure which contains field information from the specified result set.

## Return Value

Pointer to a `MYSQL_FIELD` structure or `NULL` if an invalid field number was specified

{% hint style="info" %}
The total number of fields can be obtained by `mysql_field_count()`.
{% endhint %}

## See Also

* [mysql\_fetch\_field()](mysql_fetch_field.md)
* [mysql\_field\_count()](mysql_field_count.md)

{% @marketo/form formId="4316" %}
