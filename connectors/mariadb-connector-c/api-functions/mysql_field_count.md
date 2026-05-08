---
description: >-
  mysql_field_count returns the number of columns in the most recent query
  result for a MariaDB connection, useful for checking whether a result set
  is available.
---

# mysql\_field\_count

## Syntax

```c
unsigned int mysql_field_count(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the number of columns for the most recent query on the connection represented by the link parameter as an unsigned integer. This function can be useful when using the [mysql\_store\_result()](mysql_store_result.md) function to determine if the query should have produced a non-empty result set or not without knowing the nature of the query.

{% hint style="info" %}
The mysql\_field\_count() function should be used to determine if there is a result set available.
{% endhint %}

## See also

* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_use\_result()](mysql_use_result.md)


{% @marketo/form formId="4316" %}
