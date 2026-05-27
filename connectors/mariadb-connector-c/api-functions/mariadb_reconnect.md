---
description: >-
  mariadb_reconnect attempts to re-establish a dropped MariaDB Connector/C
  connection using the original credentials, and requires the
  MYSQL_OPT_RECONNECT option to be set.
---

# mariadb\_reconnect

## Syntax

```c
my_bool  mariadb_reconnect(MYSQL * mysql)
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

mariadb\_reconnect() tries to reconnect to a server in case the connection died due to timeout or other errors. It uses the same credentials which were specified in [mysql\_real\_connect()](mysql_real_connect.md).

The function will return 0 on success.

The function will return an error, if the option MYSQL\_OPT\_RECONNECT wasn't specified before.

This function was added in Connector/C 3.0.

## See also

* [mysql\_real\_connect()](mysql_real_connect.md)
* [mysql\_options()](mysql_options.md)


{% @marketo/form formId="4316" %}
