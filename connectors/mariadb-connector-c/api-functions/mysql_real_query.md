---
description: >-
  mysql_real_query sends a binary-safe SQL statement to a MariaDB server;
  use mysql_num_fields to determine whether the query returned a result set.
---

# mysql\_real\_query

## Syntax

```c
int mysql_real_query(MYSQL * mysql,
                     const char * q,
                     unsigned long);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `query` - a string containing the statement to be performed.
* `long` - length of the string.

## Description

`mysql_real_query()` is a binary-safe function for executing a statement on the database server. Returns zero on success, otherwise non-zero.

{% hint style="info" %}
Contrary to the [mysql\_query()](mysql_query.md) function, `mysql_real_query` is binary safe.

To determine if `mysql_real_query` returns a result set, use the [mysql\_num\_fields()](mysql_num_fields.md) function.
{% endhint %}

## See also

* [mysql\_query()](mysql_query.md)
* [mysql\_num\_fields()](mysql_num_fields.md)
* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_store\_result()](mysql_store_result.md)

{% @marketo/form formId="4316" %}
