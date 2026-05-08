---
description: >-
  mysql_dump_debug_info instructs a MariaDB server to write connection
  status information to the error log, and requires the SUPER privilege for
  the current user.
---

# mysql\_dump\_debug\_info

## Syntax

```c
int mysql_dump_debug_info(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

This function is designed to be executed by an user with the SUPER privilege and is used to dump server status information into the log for the MariaDB Server relating to the connection.

Returns zero on success, nonzero if an error occurred.

{% hint style="info" %}
The server status information will be dumped into the [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) file, which can usually be found in the data directory of your server installation.
{% endhint %}

## See also

* [mysql\_debug()](mysql_debug.md)
* mysql\_debug\_end()


{% @marketo/form formId="4316" %}
