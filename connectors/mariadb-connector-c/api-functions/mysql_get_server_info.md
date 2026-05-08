---
description: >-
  mysql_get_server_info retrieves the connected server version string; use
  mysql_get_server_version for the equivalent numeric representation.
---

# mysql\_get\_server\_info

## Syntax

```c
const char * mysql_get_server_info(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the server version or NULL on failure.

{% hint style="info" %}
To obtain the numeric server version please use [mysql\_get\_server\_version()](mysql_get_server_version.md).
{% endhint %}

## See also

* [mysql\_get\_server\_version()](mysql_get_server_version.md)
* [mysql\_get\_client\_info()](mysql_get_client_info.md)


{% @marketo/form formId="4316" %}
