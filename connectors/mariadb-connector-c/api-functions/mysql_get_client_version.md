---
description: >-
  mysql_get_client_version retrieves the client library version as an unsigned
  long; use mysql_get_client_info for the string representation.
---

# mysql\_get\_client\_version

## Syntax

```c
unsigned long mysql_get_client_version(void);
```

## Description

Returns a number representing the client library version. The value has the format XXYYZZ: major version \* 10000 + minor version \* 100 + patch version.

## Return Value

A long integer representing the client version

{% hint style="info" %}
* To obtain a string containing the client library version use the [mysql\_get\_client\_info()](mysql_get_client_info.md) function.
* Since MariaDB Server 10.2.6 and MariaDB Connector/C 3.0.1 the client library is bundled with server package and returns the server package version. To obtain the client version of the connector, please use the constant `MARIADB_PACKAGE_VERSION_ID`
{% endhint %}

## See Also

* [mysql\_get\_client\_info()](mysql_get_client_info.md)

{% @marketo/form formId="4316" %}
