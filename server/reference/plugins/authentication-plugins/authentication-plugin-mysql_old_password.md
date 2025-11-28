---
description: >-
  This plugin provides backward compatibility for pre-4.1 clients using an
  older, insecure password hashing algorithm and should not be used for new
  installations.
---

# Authentication Plugin - mysql\_old\_password

The `mysql_old_password` authentication plugin is the default authentication plugin that is used for an account created when no authentication plugin is explicitly mentioned and [old\_passwords=1](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords) is set. It uses the pre-MySQL 4.1 password hashing algorithm, which is also used by the [OLD\_PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/old_password.md) function and by the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function when `old_passwords=1` is set.

{% hint style="danger" %}
It is not recommended to use the `mysql_old_password` authentication plugin for new installations. The password hashing algorithm is no longer secure, and the plugin is primarily provided for backward compatibility. The [ed25519](authentication-plugin-ed25519.md) authentication plugin is a more modern authentication plugin that provides simple password authentication.
{% endhint %}

## Installing the Plugin

The `mysql_old_password` authentication plugin is statically linked into the server, so no installation is necessary.

## Creating Users

The easiest way to create a user account with the `mysql_old_password` authentication plugin is to make sure that [old\_passwords=1](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords) is set, and create a user account via [CREATE USER](../../sql-statements/account-management-sql-statements/create-user.md#identified-by-password) that does not specify an authentication plugin, but instead specifies a password via the [IDENTIFIED BY](../../sql-statements-and-structure/sql-statements/account-management-sql-commands/create-user.md#identified-by-password) clause:

```sql
SET old_passwords=1;
CREATE USER username@hostname IDENTIFIED BY 'mariadb';
```

If [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) does not have `NO_AUTO_CREATE_USER` set, then you can also create the user via [GRANT](../../sql-statements/account-management-sql-statements/grant.md):

```sql
SET old_passwords=1;
GRANT SELECT ON db.* TO username@hostname IDENTIFIED BY 'mariadb';
```

You can also create the user account by providing a password hash via the [IDENTIFIED BY PASSWORD](../../sql-statements/account-management-sql-statements/create-user.md#identified-by-password) clause, and MariaDB validates whether the password hash is one that is compatible with `mysql_old_password`:

```sql
SET old_passwords=1;
Query OK, 0 rows affected (0.000 sec)

SELECT PASSWORD('mariadb');
+---------------------+
| PASSWORD('mariadb') |
+---------------------+
| 021bec665bf663f1    |
+---------------------+
1 row in set (0.000 sec)

CREATE USER username@hostname IDENTIFIED BY PASSWORD '021bec665bf663f1';
Query OK, 0 rows affected (0.000 sec)
```

Similar to all other [authentication plugins](./), you could also specify the name of the plugin in the `IDENTIFIED VIA` clause, while providing the password hash as the `USING` clause:

```sql
CREATE USER username@hostname IDENTIFIED VIA mysql_old_password USING '021bec665bf663f1';
Query OK, 0 rows affected (0.000 sec)
```

## Changing User Passwords

You can change a user account's password with the [SET PASSWORD](../../sql-statements/account-management-sql-statements/set-password.md) statement, while providing the plain-text password as an argument to the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function:

```sql
SET PASSWORD =  PASSWORD('new_secret')
```

You can also change the user account's password with the [ALTER USER](../../sql-statements/account-management-sql-statements/alter-user.md) statement. You have to make sure that [old\_passwords=1](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords) is set, and you have to specify a password via the [IDENTIFIED BY](../../sql-statements/account-management-sql-statements/create-user.md#identified-by-password) clause:

```sql
SET old_passwords=1;
ALTER USER username@hostname IDENTIFIED BY 'new_secret';
```

## Client Authentication Plugins

For clients that use the `libmysqlclient` or [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) libraries, MariaDB provides one client authentication plugin that is compatible with the `mysql_old_password` authentication plugin:

* `mysql_old_password`

When connecting with a [client or utility](../../../clients-and-utilities/) to a server as a user account that authenticates with the `mysql_old_password` authentication plugin. You may need to tell the client where to find the relevant client authentication plugin by specifying the `--plugin-dir` option:

```bash
mysql --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

However, the `mysql_old_password` client authentication plugin is generally statically linked into client libraries like `libmysqlclient` or [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), so this is not usually necessary.

### `mysql_old_password`

The `mysql_old_password` client authentication plugin hashes the password before sending it to the server.

## Support in Client Libraries

The `mysql_old_password` authentication plugin is one of the conventional authentication plugins, so all client libraries should support it.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
