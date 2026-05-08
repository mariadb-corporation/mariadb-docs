---
description: >-
  mysql_get_client_version retrieves the client library version as an
  unsigned long; use mysql_get_client_info for the string representation.
---

# mysql\_get\_client\_version

## Syntax

```c
unsigned long mysql_get_client_version(void);
```

## Description

Returns a number representing the client library version.

{% hint style="info" %}
To obtain a string containing the client library version use the [mysql\_get\_client\_info()](mysql_get_client_info.md) function.
{% endhint %}

## See also

* [mysql\_get\_client\_info()](mysql_get_client_info.md)


{% @marketo/form formId="4316" %}
