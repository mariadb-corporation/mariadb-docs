---
description: >-
  mysql_reset_connection resets session state on a MariaDB Connector/C
  connection — rolling back transactions and clearing variables — without
  disconnecting or reauthenticating.
---

# mysql\_reset\_connection

## Syntax

```c
int mysql_reset_connection(MYSQL * mysql);
```

* `mysql` - a MySQL handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Resets the current connection and clears session state. Similar to [mysql\_change\_user()](mysql_change_user.md) or [mariadb\_reconnect()](mariadb_reconnect.md), `mysql_reset_connection()` resets session status, but without disconnecting, opening, or reauthenticating.

On client side `mysql_reset_connection()`

* clears pending or unprocessed result sets
* clears status like `affected_rows`, info or `last_insert_id`
* invalidates active prepared statements

On server side `mysql_reset_connection()`

* drops temporary table(s)
* rollbacks active transaction
* resets auto commit mode
* releases table locks
* initializes session variables (and sets them to the value of corresponding global variables)
* closes active prepared statements
* clears user variables

Returns zero on success, non-zero if an error occurred.

This function was added in MariaDB Connector/C 3.0.0.

{% @marketo/form formId="4316" %}
