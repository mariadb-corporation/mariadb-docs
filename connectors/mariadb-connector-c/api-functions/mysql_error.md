---
description: >-
  mysql_error returns the error message string for the most recent failed
  MariaDB Connector/C function call, or an empty string if no error occurred.
---

# mysql\_error

## Syntax

```c
const char * mysql_error(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the last error message for the most recent function call that can succeed or fail. If no error occurred an empty string is returned.

{% hint style="info" %}
* Client error codes are listed in `errmsg.h` header file, server error codes are listed in `mysqld_error.h` header file of the server source distribution.
* Client error messages can be obtained by calling [mariadb\_get\_infov()](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/mariadb_get_infov) and passing the parameter `MARIADB_CLIENT_ERRORS`
{% endhint %}

## See Also

* [mysql\_errno()](mysql_errno.md)
* [mysql\_sqlstate()](mysql_sqlstate.md).

{% @marketo/form formId="4316" %}
