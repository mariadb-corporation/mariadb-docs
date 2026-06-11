---
description: >-
  mysql_close terminates an open database connection and releases the memory
  allocated for the MYSQL handle.
---

# mysql\_close

## Syntax

```c
void mysql_close(MYSQL * mysql);
```

## Parameter

* `mysql` - a `mysql` handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Closes a previously opened connection and deallocates all memory.

{% hint style="info" %}
To reuse a connection handle after `mysql_close()` the handle must be initialized again by [mysql\_init()](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/mysql_init).
{% endhint %}

## See Also

* [mysql\_init()](mysql_init.md)
* [mysql\_real\_connect()](mysql_real_connect.md)

{% @marketo/form formId="4316" %}
