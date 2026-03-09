---
description: >-
  Overview of user account authentication using plugins like pam or unix_socket
  and managing security with password validation plugins.
---

# Authentication for MariaDB Enterprise Server

## Overview

MariaDB Enterprise Server authentication is performed by database user accounts. Database user accounts are specified by user name, the hostname from which the account is connecting, and the authentication plugins configured for the account, such as mysql\_native\_password, pam, or unix\_socket.

## Change Password

The password for a [database user account](../user-account-management/) can be changed using the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/), [ALTER USER](../../reference/sql-statements/account-management-sql-statements/alter-user.md), and [SET PASSWORD](../../reference/sql-statements/account-management-sql-statements/set-password.md) statements.

```sql
WITH ALTER USER:

ALTER USER 'USER'@'192.0.2.%'
   IDENTIFIED BY 'PASSWD';
```

```sql
WITH SET PASSWORD:

SET PASSWORD FOR 'USER'@'192.0.2.%'
   = PASSWORD('PASSWD');
```

## Password Validation Plugins

If your MariaDB Enterprise Server node has a password validation plugin installed, then the password should also meet the configured requirements. When you try to set or change a user's password and the password validation plugin rejects the password, the following error message will be shown:

```sql
ERROR HY000: Your password does not satisfy the current policy requirements.
```

By default, the MariaDB Enterprise Server installs the [simple\_password\_check](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md) plugin, but the [cracklib\_password\_check](../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) plugin is also available.

For [simple\_password\_check](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md), the password requirements are configured by several system variables:

* [simple\_password\_check\_digits](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_digits)
* [imple\_password\_check\_letters\_same\_case](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_letters_same_cases)
* [simple\_password\_check\_minimal\_length](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_minimal_length)
* [simple\_password\_check\_other\_characters](../../reference/plugins/password-validation-plugins/simple-password-check-plugin.md#simple_password_check_other_characters)

## Authentication Plugins

MariaDB Enterprise Server uses authentication plugins to support different authentication methods. The default authentication plugin is mysql\_native\_password.

* [Authentication with ed25519](../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md)
* [Authentication with gssapi](authentication-with-gssapi.md)
* [Authentication with mysql\_native\_password](../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md)
* [Authentication with mysql\_old\_password](../../reference/plugins/authentication-plugins/authentication-plugin-mysql_old_password.md)
* [Authentication with pam](../../reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/)
* [Authentication with unix\_socket](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md)
* [Authentication with PARSEC](../../reference/plugins/authentication-plugins/authentication-plugin-parsec.md)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
