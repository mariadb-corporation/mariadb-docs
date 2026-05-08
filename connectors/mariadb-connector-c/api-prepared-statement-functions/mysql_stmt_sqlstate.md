---
description: >-
  mysql_stmt_sqlstate returns the five-character SQLSTATE error code for the
  most recently invoked prepared statement function, with '00000' indicating
  no error occurred.
---

# mysql\_stmt\_sqlstate

## Syntax

```c
const char * mysql_stmt_sqlstate(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns a string containing the [SQLSTATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate) error code for the most recently invoked prepared statement function that can succeed or fail. The error code consists of five characters. '00000' means no error. The values are specified by ANSI SQL and ODBC.

{% hint style="info" %}
Please note that not all client library error codes are mapped to SQLSTATE errors. Errors which can't be mapped will returned as value HY000.
{% endhint %}

## See Also

* [mysql\_errno()](../api-functions/mysql_errno.md)
* [mysql\_error()](../api-functions/mysql_error.md)


{% @marketo/form formId="4316" %}
