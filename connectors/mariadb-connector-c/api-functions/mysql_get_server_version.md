---
description: >-
  mysql_get_server_version retrieves the server version as an unsigned long;
  use mysql_get_server_info for the equivalent string representation.
---

# mysql\_get\_server\_version

## Syntax

```c
unsigned long mysql_get_server_version(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns an integer representing the version of connected server.

{% hint style="info" %}
The form of the version number is `VERSION_MAJOR * 10000 + VERSION_MINOR * 100 + VERSION_PATCH`
{% endhint %}

## See also

* [mysql\_get\_server\_info()](mysql_get_server_info.md)


{% @marketo/form formId="4316" %}
