---
description: >-
  mysql_stmt_error retrieves the human-readable error message from the last
  Connector/C prepared statement call, complementing the numeric code from
  mysql_stmt_errno.
---

# mysql\_stmt\_error

## Syntax

```c
const char * mysql_stmt_error(MYSQL_STMT * stmt);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns a string containing the error message for the most recently invoked statement function that can succeed or fail. The string will be empty if no error occurred.

## Return Value

A string describing the last error or an empty string if no error occurred.

{% hint style="info" %}
Client error messages are listed in the errmsg.h header file, server error messages are listed in the mysqld\_error.h header file of the server source distribution.
{% endhint %}

## See Also

* [mysql\_stmt\_errno()](mysql_stmt_errno.md)
* [mysql\_stmt\_sqlstate()](mysql_stmt_sqlstate.md)

{% @marketo/form formId="4316" %}
