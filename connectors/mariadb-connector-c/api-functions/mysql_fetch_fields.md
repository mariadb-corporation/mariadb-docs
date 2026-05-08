---
description: >-
  mysql_fetch_fields returns all column definitions for a MariaDB result set
  as an array of MYSQL_FIELD structures, one entry per column.
---

# mysql\_fetch\_fields

## Syntax

```c
MYSQL_FIELD * mysql_fetch_fields(MYSQL_RES * res);
```

* `res` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

This function serves an identical purpose to the [mysql\_fetch\_field()](mysql_fetch_field.md) function with the single difference that instead of returning one field at a time for each field, the fields are returned as an array. Each field contains the definition for a column of the result set.

{% hint style="info" %}
The total number of fields can be obtained by [mysql\_field\_count()](mysql_field_count.md).
{% endhint %}

## See also

* [mysql\_fetch\_field()](mysql_fetch_field.md)
* [mysql\_fetch\_field\_direct()](mysql_fetch_field_direct.md)
* [mysql\_field\_count()](mysql_field_count.md)


{% @marketo/form formId="4316" %}
