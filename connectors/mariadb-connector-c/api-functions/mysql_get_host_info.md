---
description: >-
  mysql_get_host_info returns a string describing the connection type and server
  hostname for a MariaDB Connector/C connection, or NULL if invalid.
---

# mysql\_get\_host\_info

## Syntax

```c
char * mysql_get_host_info(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Describes the type of connection in use for the connection, including the server host name.&#x20;

## Return Value

Returns a string, describing host information or `NULL` if the connection is not valid.

## See Also

* [mysql\_get\_server\_version()](mysql_get_server_version.md)

{% @marketo/form formId="4316" %}
