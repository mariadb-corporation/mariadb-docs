---
description: >-
  mysql_query sends a null-terminated SQL string to the MariaDB server for
  execution, returning zero on success; use mysql_real_query for binary-safe
  operation.
---

# mysql\_query

## Syntax

```c
int mysql_query(MYSQL * mysql,
                const char * query);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `query` -a null terminated string containing the statement to be performed.

## Description

Performs a statement pointed to by the null terminate string query against the database. Contrary to [mysql\_real\_query()](mysql_real_query.md), mysql\_query() is not binary safe.

Returns zero on success, non zero on failure

{% hint style="info" %}
For executing multi statements the statements within the null terminated string statements must be separated by a semicolon.

If your statement contains binary data you should use [mysql\_real\_query()](mysql_real_query.md) or escape your data with [mysql\_hex\_string()](mysql_hex_string.md).

To determine if a statement returned a result set use the function [mysql\_num\_fields()](mysql_num_fields.md).
{% endhint %}

## See also

* [mysql\_real\_query()](mysql_real_query.md)
* [mysql\_num\_fields()](mysql_num_fields.md)
* [mysql\_hex\_string()](mysql_hex_string.md)
* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_store\_result()](mysql_store_result.md)


{% @marketo/form formId="4316" %}
