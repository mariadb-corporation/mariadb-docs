---
description: >-
  mysql_library_init initializes the MariaDB Connector/C library before any
  other functions are called, starting the embedded server if used in that
  configuration.
---

# mysql\_library\_init

## Syntax

```c
int mysql_library_init(int argc, char **argv, char **groups)
```

## Description

Call to initialize the library before calling other functions, both for embedded servers and regular clients. If used on an embedded server, the server is started and subsystems initialized. Returns zero for success, or nonzero if an error occurred.

Call [mysql\_library\_end()](mysql_library_end.md) to clean up after completion.

{% hint style="info" %}
`mysql_server_init()` is an alias.
{% endhint %}

## See also

* [mysql\_library\_end()](mysql_library_end.md)

{% @marketo/form formId="4316" %}
