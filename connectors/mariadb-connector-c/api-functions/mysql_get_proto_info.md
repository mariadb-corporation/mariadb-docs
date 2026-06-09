---
description: >-
  mysql_get_proto_info returns the protocol version number used for a MariaDB
  Connector/C connection; versions 9 and below are not supported.
---

# mysql\_get\_proto\_info

## Syntax

```c
unsigned int mysql_get_proto_info(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the protocol version number for the specified connection.

## Return Value

The protocol version number in use.

{% hint style="info" %}
The client library doesn't support protocol version 9 and prior.
{% endhint %}

## See Also

* [mysql\_get\_host\_info()](mysql_get_host_info.md)

{% @marketo/form formId="4316" %}
