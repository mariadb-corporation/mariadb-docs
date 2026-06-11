# mysql\_get\_timeout\_value\_ms

## Syntax

```bnf
#include <mysql.h>

unsigned int mysql_get_timeout_value_ms(const MYSQL *mysql);
```

## Parameter

| Parameter | Description                                                                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `mysql`   | A connection handle previously allocated by [mysql\_init()](mysql_init.md) and connected by [mysql\_real\_connect()](mysql_real_connect.md).  |

## Description

`mysql_get_timeout_value_ms` retrieves the current timeout value configured for asynchronous operations on the given connection, expressed in milliseconds.

## Return Value

The timeout value in milliseconds as an `unsigned int`.

{% hint style="info" %}
**This function is deprecated.** Use [`mariadb_get_infov()`](mariadb_get_infov.md) with the `MARIADB_CONNECTION_ASYNC_TIMEOUT` option instead.&#x20;
{% endhint %}

## See Also

* [`mysql_get_timeout_value()`](mysql_get_timeout_value.md)
* [`mariadb_get_infov()`](mariadb_get_infov.md)
