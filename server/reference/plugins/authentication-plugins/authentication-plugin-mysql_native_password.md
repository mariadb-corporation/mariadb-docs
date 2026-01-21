---
description: >-
  The mysql_native_password plugin is the default legacy authentication method,
  using SHA-1 hashing to verify passwords stored in the internal mysql.user
  table.
---

# Authentication Plugin - mysql\_native\_password

The `mysql_native_password` authentication plugin is the default authentication plugin that will be used for an account created when no authentication plugin is explicitly mentioned and [old\_passwords=0](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords) is set. It uses the password hashing algorithm introduced in MySQL 4.1, which is also used by the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function when [old\_passwords=0](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords) is set. This hashing algorithm is based on [SHA-1](https://en.wikipedia.org/wiki/SHA-1).

It is not recommended to use the `mysql_native_password` authentication plugin for new installations that require **high password security**. If someone is able to both listen to the connection protocol and get a copy of the mysql.user table, then the person would be able to use this information to connect to the MariaDB server. The [ed25519](authentication-plugin-ed25519.md) authentication plugin is a more modern authentication plugin that provides simple password authentication using a more secure algorithm.

## Installing the Plugin

The `mysql_native_password` authentication plugin is statically linked into the server, so no installation is necessary.

## Creating Users

The easiest way to create a user account with the `mysql_native_password` authentication plugin is to make sure that [old\_passwords=0](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords) is set, and then create a user account via [CREATE USER](../../sql-statements/account-management-sql-statements/create-user.md) that does not specify an authentication plugin, but does specify a password via the [IDENTIFIED BY](../../sql-statements/account-management-sql-statements/create-user.md#identified-by-password) clause:

```sql
SET old_passwords=0;
CREATE USER username@hostname IDENTIFIED BY 'mariadb';
```

If [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) does not have `NO_AUTO_CREATE_USER` set, then you can also create the user account via [GRANT](../../sql-statements/account-management-sql-statements/grant.md):

```sql
SET old_passwords=0;
GRANT SELECT ON db.* TO username@hostname IDENTIFIED BY 'mariadb';
```

You can also create the user account by providing a password hash via the [IDENTIFIED BY PASSWORD](../../sql-statements/account-management-sql-statements/create-user.md#identified-by-password-password_hash) clause, and MariaDB will validate whether the password hash is one that is compatible with `mysql_native_password`:

```sql
SET old_passwords=0;

SELECT PASSWORD('mariadb');
+-------------------------------------------+
| PASSWORD('mariadb')                       |
+-------------------------------------------+
| *54958E764CE10E50764C2EECBB71D01F08549980 |
+-------------------------------------------+

CREATE USER username@hostname
  IDENTIFIED BY PASSWORD '*54958E764CE10E50764C2EECBB71D01F08549980';
```

Similar to all other [authentication plugins](./), you could also specify the name of the plugin in the [IDENTIFIED VIA](../../sql-statements/account-management-sql-statements/create-user.md#identified-viawith-authentication_plugin) clause while providing the password hash as the `USING` clause:

```sql
CREATE USER username@hostname
  IDENTIFIED VIA mysql_native_password USING '*54958E764CE10E50764C2EECBB71D01F08549980';
```

## Changing User Passwords

You can change a user account's password with the [SET PASSWORD](../../sql-statements/account-management-sql-statements/set-password.md) statement while providing the plain-text password as an argument to the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function:

```sql
SET PASSWORD =  PASSWORD('new_secret')
```

You can also change the user account's password with the [ALTER USER](../../sql-statements/account-management-sql-statements/alter-user.md) statement. You would have to make sure that [old\_passwords=0](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_passwords) is set, and then you would have to specify a password via the [IDENTIFIED BY](../../sql-statements/account-management-sql-statements/alter-user.md#identified-by-password) clause:

```sql
SET old_passwords=0;
ALTER USER username@hostname IDENTIFIED BY 'new_secret';
```

## Client Authentication Plugins

For clients that use the `libmysqlclient` or [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) libraries, MariaDB provides one client authentication plugin that is compatible with the `mysql_native_password` authentication plugin:

* `mysql_native_password`

When connecting with a [client or utility](../../../clients-and-utilities/) to a server as a user account that authenticates with the `mysql_native_password` authentication plugin, you may need to tell the client where to find the relevant client authentication plugin by specifying the `--plugin-dir` option:

```bash
mysql --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

However, the `mysql_native_password` client authentication plugin is generally statically linked into client libraries like `libmysqlclient` or [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), so this is not usually necessary.

### `mysql_native_password`

The `mysql_native_password` client authentication plugin hashes the password before sending it to the server.

## Support in Client Libraries

The `mysql_native_password` authentication plugin is one of the conventional authentication plugins, so all client libraries should support it.

## Known Old Issues (Only Relevant for Old Installations)

### Mismatches Between Password and authentication\_string Columns

For compatibility reasons, the `mysql_native_password` authentication plugin tries to read the password hash from both the `Password` and `authentication_string` columns in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table. This has caused issues in the past if one of the columns had a different value than the other.

{% tabs %}
{% tab title="Current" %}
[CREATE USER](../../sql-statements/account-management-sql-statements/create-user.md), [ALTER USER](../../sql-statements/account-management-sql-statements/alter-user.md), [GRANT](../../sql-statements/account-management-sql-statements/grant.md), and [SET PASSWORD](../../sql-statements/account-management-sql-statements/set-password.md) set the `Password` and `authentication_string` columns in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table whenever an account's password is changed.
{% endtab %}

{% tab title="< 10.3.11 / 10.2.19" %}
[CREATE USER](../../sql-statements/account-management-sql-statements/create-user.md), [ALTER USER](../../sql-statements/account-management-sql-statements/alter-user.md), [GRANT](../../sql-statements/account-management-sql-statements/grant.md), and [SET PASSWORD](../../sql-statements/account-management-sql-statements/set-password.md) do **not** set the `Password` and `authentication_string` columns in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table whenever an account's password is changed.
{% endtab %}
{% endtabs %}

## See Also

* [ed25519](authentication-plugin-ed25519.md) secure connection plugin
* [History of MySQL and MariaDB authentication protocols](https://mariadb.org/history-of-mysql-mariadb-authentication-protocols)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
