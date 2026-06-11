---
description: >-
  mysql_sqlstate returns the five-character SQLSTATE error code for the most
  recent MariaDB Connector/C function call, with 00000 indicating success.
---

# mysql\_sqlstate

## Syntax

```c
const char * mysql_sqlstate(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns a string containing the [SQLSTATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate) error code for the most recently invoked function that can succeed or fail. The error code consists of five characters. '00000' means no error. The values are specified by `ANSI SQL` and `ODBC`.

{% hint style="info" %}
Please note that not all client library error codes are mapped to `SQLSTATE` errors. Errors which can't be mapped will be returned as value HY000.
{% endhint %}

## See Also

* [mysql\_error()](mysql_error.md)
* [mysql\_errno()](mysql_errno.md)

{% @marketo/form formId="4316" %}
