---
description: >-
  mysql_server_init is an alias for mysql_library_init in MariaDB Connector/C,
  used to initialize the client library before making any other calls.
---

# mysql\_server\_init

## Syntax

```c
void mysql_server_init(void );
```

## Description

Call to initialize the library before calling other functions. `mysql_server_init()` is an alias for [mysql\_library\_init()](mysql_library_init.md).

## See Also

* [mysql\_library\_init()](mysql_library_init.md)
* [mysql\_library\_end()](mysql_library_end.md)

{% @marketo/form formId="4316" %}
