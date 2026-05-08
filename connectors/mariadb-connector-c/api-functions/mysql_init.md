---
description: >-
  mysql_init allocates and initializes a MYSQL structure for use with
  mysql_real_connect, and also initializes the thread subsystem if not
  already done.
---

# mysql\_init

## Syntax

```c
MYSQL * mysql_init(MYSQL * mysql);
```

`mysql` - a pointer to MYSQL or NULL. In case of passing a NULL pointer mysql\_init() will allocate memory and return a pointer to a MYSQL structure.

## Description

Prepares and initializes a MYSQL structure to be used with [mysql\_real\_connect()](mysql_real_connect.md).

If mysql\_thread\_init() was not called before, mysql\_init() will also initialize the thread subsystem for the current thread.

{% hint style="info" %}
Members of the MYSQL structure are not intended for application use.

Any subsequent calls to any mysql function (except mysql\_options()) will fail until [mysql\_real\_connect()](mysql_real_connect.md) was called.

Memory allocated by mysql\_init() must be freed with [mysql\_close()](mysql_close.md).
{% endhint %}

## See also

* [mysql\_real\_connect()](mysql_real_connect.md)
* [mysql\_options()](mysql_options.md)
* [mysql\_thread\_init()](mysql_thread_init.md)
* [mysql\_close()](mysql_close.md)


{% @marketo/form formId="4316" %}
