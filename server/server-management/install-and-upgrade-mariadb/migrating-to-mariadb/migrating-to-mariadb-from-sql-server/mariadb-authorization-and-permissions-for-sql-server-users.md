# MariaDB Authorization and Permissions for SQL Server Users

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

## Understanding Accounts and Users

MariaDB authorizes access and check permissions on accounts, rather than users. Even if MariaDB supports standard SQL commands like [CREATE USER](../../../../reference/sql-statements/account-management-sql-statements/create-user.md) and [DROP USER](../../../../reference/sql-statements/account-management-sql-statements/drop-user.md), it is important to remember that it actually works with accounts.

An account is specified in the format `'user'@'host'`. The quotes are optional and allow one to include special characters, like dots. The host part can actually be a pattern, which follows the same syntax used in `LIKE` comparisons. Patterns are often convenient because they can match several hostnames.

Here are some examples.

Omitting the host part indicates an account that can access from any host. So the following statements are equivalent:

```sql
CREATE USER viviana;
CREATE USER viviana@'%';
```

However, such accounts may be unable to connect from localhost if an anonymous user `''@'%'` is present. See [localhost and %](../../../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md) for the details.

Accounts are not bound to a specific database. They are global. Once an account is created, it is possible to assign it permissions on any existing or non existing database.

The [sql\_mode](../../../variables-and-modes/sql_mode.md) system variable has a [NO\_AUTO\_CREATE\_USER](../../../variables-and-modes/sql_mode.md#no_auto_create_user) flag. In recent MariaDB versions it is enabled by default. If it is not enabled, a [GRANT](../../../../reference/sql-statements/account-management-sql-statements/grant.md) statement specifying privileges for a non-existent account will automatically create that account.

For more information: [Account Management SQL Commands](../../../../reference/sql-statements/account-management-sql-statements/).

### Setting or Changing Passwords

Accounts with the same username can have different passwords.

By default, an account has no password. A password can be set, or changed, in the following way:

* By specifying it in [CREATE USER](../../../../reference/sql-statements/account-management-sql-statements/create-user.md).
* By the user, with [SET PASSWORD](../../../../reference/sql-statements/account-management-sql-statements/set-password.md).
* By root, with `SET PASSWORD` or [ALTER USER](../../../../reference/sql-statements/account-management-sql-statements/alter-user.md).

With all these statements (`CREATE USER`, `ALTER USER`, `SET PASSWORD`) it is possible to specify the password in plain or as a hash:

```sql
-- specifying plain passwords:
CREATE USER tom@'%.example.com' IDENTIFIED BY 'plain secret';
ALTER USER tom@'%.example.com' IDENTIFIED BY 'plain secret';
SET PASSWORD = 'plain secret';
-- specifying hashes:
CREATE USER tom@'%.example.com' IDENTIFIED BY PASSWORD 'secret hash';
ALTER USER tom@'%.example.com' IDENTIFIED BY PASSWORD 'secret hash';
SET PASSWORD = PASSWORD('secret hash');
```

The [PASSWORD()](../../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function uses the same algorithm used internally by MariaDB to generate hashes. Therefore it can be used to get a hash from a plain password. Note that this function should not be used by applications, as its output may depend on MariaDB version and configuration.

`SET PASSWORD` applies to the current account, by default. Superusers can change other accounts passwords in this way:

```sql
SET PASSWORD FOR tom@'%.example.com' = PASSWORD 'secret hash';
```

Passwords can have an expiry date, set by [default\_password\_lifetime](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_password_lifetime). To set a different date for a particular user:

```sql
CREATE USER 'tom'@'%.example.com' PASSWORD EXPIRE INTERVAL 365 DAY;
```

To set no expiry date for a particular user:

```sql
CREATE USER 'tom'@'%.example.com' PASSWORD EXPIRE NEVER;
```

For more details, see [User Password Expiry](../../../../security/user-account-management/user-password-expiry.md).

It is also possible to lock an account with immediate effect:

```sql
CREATE USER 'tom'@'%.example.com' ACCOUNT LOCK;
```

See [Account Locking](../../../../security/user-account-management/account-locking.md) for more details.

## Authentication Plugins

MariaDB supports [authentication plugins](../../../../reference/plugins/authentication-plugins/). These plugins implement user's login and authorization before they can use MariaDB.

Each user has one or more authentication plugins assigned. The default one is [mysql\_native\_password](../../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md). It is the traditional login using the username and password set in MariaDB, as described above.

On UNIX systems, root is also assigned the [unix\_socket](../../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) plugin, which allows a user logged in the operating system to be recognized by MariaDB.

Windows users may be interested in the [named pipe](../../../../reference/plugins/authentication-plugins/authentication-plugin-named-pipe.md) and [GSSAPI](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) plugins. GSSAPI also requires the use of a plugin on the [client side](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md#support-in-client-libraries).

A plugin can be assigned to a user with `CREATE USER`, `ALTER USER` or `GRANT`, using the `IDENTIFIED VIA` syntax. For example:

```sql
CREATE USER username@hostname IDENTIFIED VIA gssapi;
GRANT SELECT ON db.* TO username@hostname IDENTIFIED VIA named_pipe;
```

## TLS connections

A particular user can be required to use TLS connections. Additional requirements can be set:

* Having a valid X509 certificate.
* The certificate may be required to be issued by a particular authority.
* A particular certificate subject can be required.
* A particular certificate cipher suite can be required.

These requirements can be set with `CREATE USER`, `ALTER USER` or `GRANT`. For the syntax, see [CREATE USER](../../../../reference/sql-statements/account-management-sql-statements/create-user.md#tls-options).

MariaDB can be bundled with several cryptography libraries, depending on its version. For more information about the libraries, see [TLS and Cryptography Libraries Used by MariaDB](../../../../security/securing-mariadb/encryption/tls-and-cryptography-libraries-used-by-mariadb.md).

For more information about secure connections, see [Secure Connections Overview](../../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md).

## Permissions

Permissions can be granted to accounts. As mentioned before, the specified accounts can actually be patterns, and multiple accounts may match a pattern. For example, in this example we are creating three accounts, and we are assigning permissions to all of them:

```sql
CREATE USER 'tom'@'example.com';
CREATE USER 'tom'@'123.123.123.123;
CREATE USER 'tom'@'tomlaptop';
GRANT USAGE ON *.* TO tom@'%';
```

The following permission levels exist in MariaDB:

* [Global privileges](../../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges);
* [Database privileges](../../../../reference/sql-statements/account-management-sql-statements/grant.md#database-privileges);
* [Table privileges](../../../../reference/sql-statements/account-management-sql-statements/grant.md#table-privileges);
* [Column privileges](../../../../reference/sql-statements/account-management-sql-statements/grant.md#column-privileges);
* [Function](../../../../reference/sql-statements/account-management-sql-statements/grant.md#function-privileges) and [procedure privileges](../../../../reference/sql-statements/account-management-sql-statements/grant.md#procedure-privileges).

Note that database and schema are synonymous in MariaDB.

Permissions can be granted for non-existent objects that could exist in the future.

The list of supported privileges can be found in the [GRANT](../../../../reference/sql-statements/account-management-sql-statements/grant.md) page. Some highlights can be useful for SQL Server users:

* `USAGE` privilege has no effect. The `GRANT` command fails if we don't grant at least one privilege; but sometimes we want to run it for other purposes, for example to require a user to use TLS connections. In such cases, it is useful to grant `USAGE`.
* Normally we can obtain a list of all databases for which we have at least one permission. The `SHOW DATABASES` permission allows getting a list of all databases.
* There is no `SHOWPLAN` privilege in MariaDB. Instead, [EXPLAIN](../../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) requires the `SELECT` privilege for each accessed table and the `SHOW VIEW` privilege for each accessed view.
* The same permissions are needed to see a table structure (`SELECT`) or a view definition (`SHOW VIEW`).
* `REFERENCES` has no effect.

MariaDB does not support negative permissions (the `DENY` command).

Some differences concerning the SQL commands:

* In MariaDB `GRANT` and `REVOKE` statements can only assign/revoke permissions to one user at a time.
* While we can assign/revoke privileges at column level, we have to run a `GRANT` or `REVOKE` statement for each column. The `table (column_list)` syntax is not recognized by MariaDB.
* In MariaDB it is not needed (or possible) to specify a class type.

## Roles

MariaDB supports [roles](../../../../security/user-account-management/roles/). Permissions can be assigned to roles, and roles can be assigned to accounts.

An account may have zero or one default roles. A default role is a role that is automatically active for a user when they connect. To assign an account or remove a default role, these SQL statements can be used:

```sql
SET DEFAULT ROLE some_role FOR username@hostname;
SET DEFAULT ROLE NONE FOR username@hostname;
```

Normally a role is not a default role. If we assign a role in this way:

```sql
GRANT some_role TO username@hostname;
```

...the user will not have that role automatically enabled. They will have to enable it explicitly:

```sql
SET ROLE some_role;
```

MariaDB does not have predefined roles, like public.

For an introduction to roles, see [Roles Overview](../../../../security/user-account-management/roles/roles_overview.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
