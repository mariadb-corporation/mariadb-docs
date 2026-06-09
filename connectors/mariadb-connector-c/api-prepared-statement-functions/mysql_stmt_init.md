---
description: >-
  mysql_stmt_init allocates and initializes a MYSQL_STMT prepared statement
  handle for a Connector/C connection, returning NULL if memory allocation
  fails.
---

# mysql\_stmt\_init

## Syntax

```c
MYSQL_STMT * mysql_stmt_init(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](../api-functions/mysql_init.md) or [mysql\_real\_connect()](../api-functions/mysql_real_connect.md).

## Description

Initializes and allocates memory for a prepared statement.&#x20;

## Return Value

Returns a pointer to a `MYSQL_STMT` structure or NULL if an error occurred.

{% hint style="info" %}
* Members of the `MYSQL_STMT` structure are not intended for application use`.\`
* A statement handles which was allocated by `mysql_stmt_init()` needs to be freed with [mysql\_stmt\_close()](mysql_stmt_close.md).\\
* Any subsequent calls to any `mysql_stmt` function will fail until [mysql\_stmt\_prepare()](mysql_stmt_prepare.md) was called.
{% endhint %}

## See Also

* [mysql\_stmt\_close()](mysql_stmt_close.md)
* [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)

{% @marketo/form formId="4316" %}
