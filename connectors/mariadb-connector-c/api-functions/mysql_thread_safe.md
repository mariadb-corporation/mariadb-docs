---
description: >-
  mysql_thread_safe returns 1 if the MariaDB Connector/C client library was
  compiled with thread-safety support, or zero otherwise.
---

# mysql\_thread\_safe

## Syntax

```c
unsigned int mysql_thread_safe(void );
```

## Description

Indicates whether or not the client library is compiled as thread safe. Returns `1` if the client library was compiled as thread safe otherwise zero.

{% hint style="info" %}
By default the mariadb client library is compiled as thread safe.
{% endhint %}

## See also

* [mysql\_thread\_init()](mysql_thread_init.md)
* [mysql\_thread\_end()](mysql_thread_end.md)


{% @marketo/form formId="4316" %}
