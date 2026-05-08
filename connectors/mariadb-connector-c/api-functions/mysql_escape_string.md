---
description: >-
  mysql_escape_string encodes a string using the default character set for
  safe use in SQL statements. Deprecated — use mysql_real_escape_string
  instead.
---

# mysql\_escape\_string

## Syntax

```c
unsigned long mysql_escape_string(char * to,
                                  const char * from,
                                  unsigned long);
```

## Description

Escapes a string using the default character set.

{% hint style="danger" %}
This function is deprecated and will be discontinued. Please use [mysql\_real\_escape\_string()](mysql_real_escape_string.md) instead.
{% endhint %}

## See also

* [mysql\_real\_escape\_string()](mysql_real_escape_string.md)


{% @marketo/form formId="4316" %}
