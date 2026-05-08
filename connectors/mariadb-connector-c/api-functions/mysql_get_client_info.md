---
description: >-
  mysql_get_client_info retrieves the client library version as a string;
  use mysql_get_client_version for the equivalent numeric value.
---

# mysql\_get\_client\_info

## Syntax

```c
const char * mysql_get_client_info(void );
```

## Description

Returns a string representing the client library version

{% hint style="info" %}
To obtain the numeric value of the client library version use [mysql\_get\_client\_version()](mysql_get_client_version.md).
{% endhint %}

## See also

* [mysql\_get\_client\_version()](mysql_get_client_version.md)
* [mysql\_get\_host\_info()](mysql_get_host_info.md)
* [mysql\_get\_proto\_info()](mysql_get_proto_info.md)


{% @marketo/form formId="4316" %}
