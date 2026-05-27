---
description: >-
  mysql_ping checks whether a MariaDB server connection is still active and
  attempts an automatic reconnect if the connection has dropped and
  reconnect is enabled.
---

# mysql\_ping

## Syntax

```c
int mysql_ping(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Checks whether the connection to the server is working. If it has gone down, and global option reconnect is enabled an automatic reconnection is attempted.

Returns zero on success, nonzero if an error occurred.

This function can be used by clients that remain idle for a long while, to check whether the server has closed the connection and reconnect if necessary.

{% hint style="info" %}
If a reconnect occurred the `thread_id` will change. Also resources bundled to the connection (prepared statements, locks, temporary tables, ...) will be released.
{% endhint %}

## See also

* [mysql\_options()](mysql_options.md)
* [mysql\_kill()](mysql_kill.md)


{% @marketo/form formId="4316" %}
