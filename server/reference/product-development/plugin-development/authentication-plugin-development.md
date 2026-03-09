---
description: >-
  Details how to implement custom authentication methods, allowing users to
  connect using external credentials or protocols.
---

# Authentication Plugin Development

{% include "../../../.gitbook/includes/this-page-contains-backgrou....md" %}

## Authentication Plugin API

The authentication plugin API is extensively documented in the [source code](../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md) in the following files:

* `mysql/plugin_auth.h` (server part)
* `mysql/client_plugin.h` (client part)
* `mysql/plugin_auth_common.h` (common parts)

The MariaDB [source code](../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md) also contains some authentication plugins that are intended explicitly to be examples for developers. They are located in `plugin/auth_examples`.

The definitions of two example authentication plugins called `two_questions` and `three_attempts` can be seen in `plugin/auth_examples/dialog_examples.c`. These authentication plugins demonstrate how to communicate with the user using the [dialog](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#dialog) client authentication plugin.

The `two_questions` authentication plugin asks the user for a password and a confirmation ("Are you sure?").

The `three_attempts` authentication plugin gives the user three attempts to enter a correct password.

The password for both of these plugins should be specified in the plain text in the `USING` clause:

```sql
CREATE USER insecure IDENTIFIED VIA two_questions USING 'notverysecret';
```

### Dialog Client Authentication Plugin - Client Library Extension

The [dialog](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#dialog) client authentication plugin, strictly speaking, is not part of the client-server or authentication plugin API. But it can be loaded into any client application that uses the `libmysqlclient` or [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) libraries. This authentication plugin provides a way for the application to customize the UI of the dialog function.

In order to use the [dialog](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#dialog) client authentication plugin to communicate with the user in a customized way, the application will need to implement a function with the following signature:

```c
extern "C" char *mysql_authentication_dialog_ask(
  MYSQL *mysql, int type, const char *prompt, char *buf, int buf_len)
```

The function takes the following arguments:

* The connection handle.
* A question "type", which has one of the following values:
  * `1` - Normal question
  * `2` - Password (no echo)
* A prompt.
* A buffer.
* The length of the buffer.

The function returns a pointer to a string of characters, as entered by the user. It may be stored in `buf` or allocated with `malloc()`.

By using this function, a GUI application can open a dialog window, and a network application can send the question over the network, as required. If no `mysql_authentication_dialog_ask` function is provided by the application, the [dialog](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#dialog) client authentication plugin falls back to [fputs()](https://linux.die.net/man/3/fputs) and [fgets()](https://linux.die.net/man/3/fgets).

Providing this callback is particularly important on Windows, because Windows GUI applications have no associated console and the default dialog function will not be able to reach the user. An example of Windows GUI client that does it correctly is [HeidiSQL](../../../clients-and-utilities/graphical-and-enhanced-clients/heidisql.md).
