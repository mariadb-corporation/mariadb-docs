---
description: >-
  Create new database accounts. This guide covers the syntax for defining users,
  setting authentication methods, and establishing initial resource limits.
---

# CREATE USER

## Syntax

```bnf
CREATE [OR REPLACE] USER [IF NOT EXISTS] 
 user_specification [,user_specification ...] 
  [REQUIRE {NONE | tls_option [[AND] tls_option ...] }]
  [WITH resource_option [resource_option ...] ]
  [lock_option] [password_option] 

user_specification:
  username [authentication_option]

authentication_option:
  IDENTIFIED BY 'password' 
  | IDENTIFIED BY PASSWORD 'password_hash'
  | IDENTIFIED {VIA|WITH} authentication_rule [OR authentication_rule  ...]

authentication_rule:
    authentication_plugin
  | authentication_plugin {USING|AS} 'authentication_string'
  | authentication_plugin {USING|AS} PASSWORD('password')

tls_option:
  SSL 
  | X509
  | CIPHER 'cipher'
  | ISSUER 'issuer'
  | SUBJECT 'subject'

resource_option:
  MAX_QUERIES_PER_HOUR count
  | MAX_UPDATES_PER_HOUR count
  | MAX_CONNECTIONS_PER_HOUR count
  | MAX_USER_CONNECTIONS count
  | MAX_STATEMENT_TIME time

password_option:
  PASSWORD EXPIRE
  | PASSWORD EXPIRE DEFAULT
  | PASSWORD EXPIRE NEVER
  | PASSWORD EXPIRE INTERVAL N DAY

lock_option:
    ACCOUNT LOCK
  | ACCOUNT UNLOCK
}
```

## Description

The `CREATE USER` statement creates new MariaDB accounts. To use it, you must have the global [CREATE USER](grant.md#create-user) privilege or the [INSERT](grant.md#table-privileges) privilege for the [mysql](../../system-tables/the-mysql-database-tables/) database.

{% tabs %}
{% tab title="Current" %}
For each account, `CREATE USER` creates a new row in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) view (and the underlying [mysql.global\_priv](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md) table) that has no privileges.
{% endtab %}

{% tab title="< 10.4" %}
For each account, `CREATE USER` creates a new row in [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table that has no privileges.
{% endtab %}
{% endtabs %}

If any of the specified accounts, or any permissions for the specified accounts, already exist, then the server returns `ERROR 1396 (HY000)`. If an error occurs, `CREATE USER` will still create the accounts that do not result in an error. Only one error is produced for all users which have not been created:

```
ERROR 1396 (HY000): 
  Operation CREATE USER failed for 'u1'@'%','u2'@'%'
```

CREATE USER, [DROP USER](drop-user.md), [CREATE ROLE](create-role.md), and [DROP ROLE](drop-role.md) all produce the same error code when they fail.

See [Account Names](create-user.md#account-names) below for details on how account names are specified.

One can also create users with [GRANT](grant.md) if [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) does not have [NO\_AUTO\_CREATE\_USER](../../../server-management/variables-and-modes/sql_mode.md#no_auto_create_user) set. `NO_AUTO_CREATE_USER` is set by default.

## OR REPLACE

If the optional `OR REPLACE` clause is used, it is basically a shortcut for:

```sql
DROP USER IF EXISTS name;
CREATE USER name ...;
```

For example:

```sql
CREATE USER foo2@test IDENTIFIED BY 'password';
ERROR 1396 (HY000): Operation CREATE USER failed for 'foo2'@'test'

CREATE OR REPLACE USER foo2@test IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.00 sec)
```

## IF NOT EXISTS

When the `IF NOT EXISTS` clause is used, MariaDB will return a warning instead of an error if the specified user already exists.

For example:

```sql
CREATE USER foo2@test IDENTIFIED BY 'password';
ERROR 1396 (HY000): Operation CREATE USER failed for 'foo2'@'test'

CREATE USER IF NOT EXISTS foo2@test IDENTIFIED BY 'password';
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+----------------------------------------------------+
| Level | Code | Message                                            |
+-------+------+----------------------------------------------------+
| Note  | 1973 | Can't create user 'foo2'@'test'; it already exists |
+-------+------+----------------------------------------------------+
```

## Authentication Options

If more than one authentication mechanism is declared using the `OR` keyword, the mechanisms are attempted in the order they are declared in the `CREATE USER` statement. As soon as one of the authentication mechanisms is successful, authentication is complete. If none of them is successful, the authentication has failed.

### IDENTIFIED BY 'password'

The optional `IDENTIFIED BY` clause can be used to provide an account with a password. The password should be specified in plain text. It will be hashed by the [PASSWORD](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function prior to being stored in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md)/[mysql.global\_priv\_table](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md) table.

For example, if our password is `mariadb`, then we can create the user with:

```sql
CREATE USER foo2@test IDENTIFIED BY 'mariadb';
```

If you do not specify a password with the `IDENTIFIED BY` clause, the user\
will be able to connect without a password. A blank password is not a wildcard\
to match any password. The user must connect without providing a password if no\
password is set.

The only [authentication plugins](../../plugins/authentication-plugins/) that this clause supports are [mysql\_native\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) and [mysql\_old\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md).

### IDENTIFIED BY PASSWORD 'password\_hash'

The optional `IDENTIFIED BY PASSWORD` clause can be used to provide an account with a password that has already been hashed. The password should be specified as a hash that was provided by the [PASSWORD](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function. It will be stored in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md)/[mysql.global\_priv\_table](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md) table as-is.

For example, if our password is `mariadb`, then we can find the hash with:

```sql
SELECT PASSWORD('mariadb');
+-------------------------------------------+
| PASSWORD('mariadb')                       |
+-------------------------------------------+
| *54958E764CE10E50764C2EECBB71D01F08549980 |
+-------------------------------------------+
1 row in set (0.00 sec)
```

And then we can create a user with the hash:

{% code overflow="wrap" %}
```sql
CREATE USER foo2@test IDENTIFIED BY PASSWORD '*54958E764CE10E50764C2EECBB71D01F08549980';
```
{% endcode %}

If you do not specify a password with the `IDENTIFIED BY` clause, the user will be able to connect without a password. A blank password is not a wildcard to match any password. The user must connect without providing a password if no password is set.

The only [authentication plugins](../../plugins/authentication-plugins/) that this clause supports are [mysql\_native\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) and [mysql\_old\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md).

### IDENTIFIED {VIA|WITH} authentication\_plugin

The optional `IDENTIFIED VIA authentication_plugin` allows you to specify that the account should be authenticated by a specific [authentication plugin](../../plugins/authentication-plugins/). The plugin name must be an active authentication plugin as per [SHOW PLUGINS](../administrative-sql-statements/show/show-plugins.md). If it doesn't show up in that output, then you will need to install it with [INSTALL PLUGIN](../administrative-sql-statements/plugin-sql-statements/install-plugin.md) or [INSTALL SONAME](../administrative-sql-statements/plugin-sql-statements/install-soname.md).

`VIA` and `WITH` are synonyms.

For example, this could be used with the [PAM authentication plugin](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md):

```sql
CREATE USER foo2@test IDENTIFIED VIA pam;
```

Some authentication plugins allow additional arguments to be specified after a `USING` or `AS` keyword. For example, the [PAM authentication plugin](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) accepts a [service name](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#configuring-the-pam-service):

```sql
CREATE USER foo2@test IDENTIFIED VIA pam USING 'mariadb';
```

The exact meaning of the additional argument would depend on the specific authentication plugin.

The `USING` or `AS` keyword can also be used to provide a plain-text password to a plugin if it's provided as an argument to the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function. This is only valid for [authentication plugins](../../plugins/authentication-plugins/) that have implemented a hook for the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function. For example, the [ed25519](../../plugins/authentication-plugins/authentication-plugin-ed25519.md) authentication plugin supports this:

```sql
CREATE USER safe@'%' IDENTIFIED VIA ed25519 USING PASSWORD('secret');
```

One can specify many authentication plugins, they all work as alternatives ways of authenticating a user:

```sql
CREATE USER safe@'%' IDENTIFIED VIA ed25519 USING PASSWORD('secret') OR unix_socket;
```

By default, when you create a user without specifying an authentication plugin, MariaDB uses the [mysql\_native\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) plugin.

## TLS Options

{% tabs %}
{% tab title="Current" %}
MariaDB allows you to encrypt data in transit between the server and clients using the Transport Layer Security (TLS) protocol. TLS was formerly known as Secure Socket Layer (SSL), but strictly speaking the SSL protocol is a predecessor to TLS and, that version of the protocol is now considered insecure. The documentation still uses the term SSL often and for compatibility reasons TLS-related server system and status variables still use the prefix ssl\_, but internally, MariaDB only supports its secure successors.
{% endtab %}

{% tab title="< 11.4" %}
By default, MariaDB transmits data between the server and clients **without encrypting it**. This is generally acceptable when the server and client run on the same host or in networks where security is guaranteed through other means. However, in cases where the server and client exist on separate networks or they are in a high-risk network, the lack of encryption does introduce security concerns as a malicious actor could potentially eavesdrop on the traffic as it is sent over the network between them.

To mitigate this concern, MariaDB allows you to encrypt data in transit between the server and clients using the Transport Layer Security (TLS) protocol. TLS was formerly known as Secure Socket Layer (SSL), but strictly speaking the SSL protocol is a predecessor to TLS and, that version of the protocol is now considered insecure. The documentation still uses the term SSL often and for compatibility reasons TLS-related server system and status variables still use the prefix ssl\_, but internally, MariaDB only supports its secure successors.
{% endtab %}
{% endtabs %}

See [Secure Connections Overview](../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md) for more information about how to determine whether your MariaDB server has TLS support.

You can set certain TLS-related restrictions for specific user accounts. For instance, you might use this with user accounts that require access to sensitive data while sending it across networks that you do not control. These restrictions can be enabled for a user account with the [CREATE USER](create-user.md), [ALTER USER](alter-user.md), or [GRANT](grant.md) statements. The following options are available:

| Option                    | Description                                                                                                                                                                                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REQUIRE NONE              | TLS is not required for this account, but can still be used.                                                                                                                                                                                                                                        |
| REQUIRE SSL               | The account must use TLS, but no valid X509 certificate is required. This option cannot be combined with other TLS options.                                                                                                                                                                         |
| REQUIRE X509              | The account must use TLS and must have a valid X509 certificate. This option implies REQUIRE SSL. This option cannot be combined with other TLS options.                                                                                                                                            |
| REQUIRE ISSUER 'issuer'   | The account must use TLS and must have a valid X509 certificate. Also, the Certificate Authority must be the one specified via the string issuer. This option implies REQUIRE X509. This option can be combined with the SUBJECT, and CIPHER options in any order.                                  |
| REQUIRE SUBJECT 'subject' | The account must use TLS and must have a valid X509 certificate. Also, the certificate's Subject must be the one specified via the string subject. This option implies REQUIRE X509. This option can be combined with the ISSUER, and CIPHER options in any order.                                  |
| REQUIRE CIPHER 'cipher'   | The account must use TLS, but no valid X509 certificate is required. Also, the encryption used for the connection must use a specific cipher method specified in the string cipher. This option implies REQUIRE SSL. This option can be combined with the ISSUER, and SUBJECT options in any order. |

The `REQUIRE` keyword must be used only once for all specified options, and the `AND` keyword can be used to separate individual options, but it is not required.

For example, you can create a user account that requires these TLS options with the following:

```sql
CREATE USER 'alice'@'%'
 REQUIRE SUBJECT '/CN=alice/O=My Dom, Inc./C=US/ST=Oregon/L=Portland'
 AND ISSUER '/C=FI/ST=Somewhere/L=City/ O=Some Company/CN=Peter Parker/emailAddress=p.parker@marvel.com'
 AND CIPHER 'SHA-DES-CBC3-EDH-RSA';
```

If any of these options are set for a specific user account, then any client who tries to connect with that user account will have to be configured to connect with TLS.

See [Securing Connections for Client and Server](../../../security/securing-mariadb/encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md) for information on how to enable TLS on the client and server.

## Resource Limit Options

It is possible to set per-account limits for certain server resources. The following table shows the values that can be set per account:

| Limit Type                  | Decription                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MAX\_QUERIES\_PER\_HOUR     | Number of statements that the account can issue per hour (including updates)                                                                                                                                                    |
| MAX\_UPDATES\_PER\_HOUR     | Number of updates (not queries) that the account can issue per hour                                                                                                                                                             |
| MAX\_CONNECTIONS\_PER\_HOUR | Number of connections that the account can start per hour                                                                                                                                                                       |
| MAX\_USER\_CONNECTIONS      | Number of simultaneous connections that can be accepted from the same account; if it is 0, max\_connections will be used instead; if max\_connections is 0, there is no limit for this account's simultaneous connections.      |
| MAX\_STATEMENT\_TIME        | Timeout, in seconds, for statements executed by the user. See also [Aborting Statements that Exceed a Certain Time to Execute](../../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md). |

If any of these limits are set to `0`, then there is no limit for that resource for that user.

Here is an example showing how to create a user with resource limits:

```sql
CREATE USER 'someone'@'localhost' WITH
    MAX_USER_CONNECTIONS 10
    MAX_QUERIES_PER_HOUR 200;
```

The resources are tracked per account, which means `'user'@'server'`; not per user name or per connection.

The count can be reset for all users using [FLUSH USER\_RESOURCES](../administrative-sql-statements/flush-commands/flush.md), [FLUSH PRIVILEGES](../administrative-sql-statements/flush-commands/flush.md) or [mariadb-admin reload](../../../clients-and-utilities/administrative-tools/mariadb-admin.md).

Per account resource limits are stored in the [user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table, in the [mysql](../../system-tables/the-mysql-database-tables/) database. Columns used for resources limits are named `max_questions`, `max_updates`, `max_connections` (for `MAX_CONNECTIONS_PER_HOUR`), and `max_user_connections` (for `MAX_USER_CONNECTIONS`).

## Account Names

Account names have both a user name component and a host name component, and are specified as `'user_name'@'host_name'`.

The user name and host name may be unquoted, quoted as strings using double quotes (`"`) or\
single quotes (`'`), or quoted as identifiers using backticks (\`\`\`). You must use quotes\
when using special characters (such as a hyphen) or wildcard characters. If you quote, you\
must quote the user name and host name separately (for example `'user_name'@'host_name'`).

### Host Name Component

If the host name is not provided, it is assumed to be `'%'`.

Host names may contain the wildcard characters `%` and `_`. They are matched as if by\
the [LIKE](../../sql-functions/string-functions/like.md) clause. If you need to use a wildcard character literally (for example, to\
match a domain name with an underscore), prefix the character with a backslash. See `LIKE`\
for more information on escaping wildcard characters.

Host name matches are case-insensitive. Host names can match either domain names or IP\
addresses. Use `'localhost'` as the host name to allow only local client connections. On Linux, the loopback interface (127.0.0.1) will not match 'localhost' as it is not considered a local connection: this means that only connections via UNIX-domain sockets will match 'localhost'.

You can use a netmask to match a range of IP addresses using `'base_ip/netmask'` as the\
host name. A user with an IP address _ip\_addr_ will be allowed to connect if the following\
condition is true:

```bash
ip_addr & netmask = base_ip
```

For example, given a user:

```sql
CREATE USER 'maria'@'247.150.130.0/255.255.255.0';
```

the IP addresses satisfying this condition range from 247.150.130.0 to 247.150.130.255.

Using `255.255.255.255` is equivalent to not using a netmask at all. Netmasks cannot be used for IPv6 addresses.

Note that the credentials added when creating a user with the `'%'` wildcard host will not grant access in all cases. For example, some systems come with an anonymous localhost user, and when connecting from localhost this will take precedence.

Before [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), the host name component could be up to 60 characters in length. Starting from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), it can be up to 255 characters.

### User Name Component

User names must match exactly, including case. A user name that is empty is known as an anonymous account and is allowed to match a login attempt with any user name component. These are described more in the next section.

For valid identifiers to use as user names, see [Identifier Names](../../sql-structure/sql-language-structure/identifier-names.md).

It is possible for more than one account to match when a user connects. MariaDB selects\
the first matching account after sorting according to the following criteria:

* Accounts with an exact host name are sorted before accounts using a wildcard in the\
  host name. Host names using a netmask are considered to be exact for sorting.
* Accounts with a wildcard in the host name are sorted according to the position of\
  the first wildcard character. Those with a wildcard character later in the host name\
  sort before those with a wildcard character earlier in the host name.
* Accounts with a non-empty user name sort before accounts with an empty user name.
* Accounts with an empty user name are sorted last. As mentioned previously, these are known as anonymous accounts. These are described more in the next section.

The following table shows a list of example account as sorted by these criteria:

```
+---------+-------------+
| User    | Host        |
+---------+-------------+
| joffrey | 192.168.0.3 |
|         | 192.168.0.% |
| joffrey | 192.168.%   |
|         | 192.168.%   |
+---------+-------------+
```

Once connected, you only have the privileges granted to the account that matched,\
not all accounts that could have matched. For example, consider the following\
commands:

```sql
CREATE USER 'joffrey'@'192.168.0.3';
CREATE USER 'joffrey'@'%';
GRANT SELECT ON test.t1 TO 'joffrey'@'192.168.0.3';
GRANT SELECT ON test.t2 TO 'joffrey'@'%';
```

If you connect as joffrey from `192.168.0.3`, you will have the `SELECT`\
privilege on the table `test.t1`, but not on the table `test.t2`. If you connect as joffrey from any other IP address, you will have the `SELECT` privilege on the table `test.t2`, but not\
on the table `test.t1`.

Usernames can be up to 80 characters long before 10.6 and starting from 10.6 it can be 128 characters long.

### Anonymous Accounts

Anonymous accounts are accounts where the user name portion of the account name is empty. These accounts act as special catch-all accounts. If a user attempts to log into the system from a host, and an anonymous account exists with a host name portion that matches the user's host, then the user will log in as the anonymous account if there is no more specific account match for the user name that the user entered.

For example, here are some anonymous accounts:

```sql
CREATE USER ''@'localhost';
CREATE USER ''@'192.168.0.3';
```

#### Fixing a Legacy Default Anonymous Account

On some systems, the [mysql.db](../../system-tables/the-mysql-database-tables/mysql-db-table.md) table has some entries for the `''@'%'` anonymous account by default. Unfortunately, there is no matching entry in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md)/[mysql.global\_priv\_table](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md) table, which means that this anonymous account doesn't exactly exist, but it does have privileges--usually on the default `test` database created by [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md). These account-less privileges are a legacy that is leftover from a time when MySQL's privilege system was less advanced.

This situation means that you will run into errors if you try to create a `''@'%'` account. For example:

```sql
CREATE USER ''@'%';
ERROR 1396 (HY000): Operation CREATE USER failed for ''@'%'
```

The fix is to [DELETE](../data-manipulation/changing-deleting-data/delete.md) the row in the [mysql.db](../../system-tables/the-mysql-database-tables/mysql-db-table.md) table and then execute [FLUSH PRIVILEGES](../administrative-sql-statements/flush-commands/flush.md):

```sql
DELETE FROM mysql.db WHERE User='' AND Host='%';
FLUSH PRIVILEGES;
```

Note that `FLUSH PRIVILEGES` is only needed if one modifies the `mysql` tables directly. It is not needed when using `CREATE USER`, `DROP USER`, `GRANT` etc.

And then the account can be created:

```sql
CREATE USER ''@'%';
Query OK, 0 rows affected (0.01 sec)
```

See [MDEV-13486](https://jira.mariadb.org/browse/MDEV-13486) for more information.

## Password Expiry

Besides automatic password expiry, as determined by [default\_password\_lifetime](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_password_lifetime), password expiry times can be set on an individual user basis, overriding the global setting, for example:

```sql
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;
```

See [User Password Expiry](../../../security/user-account-management/user-password-expiry.md) for more details.

## Account Locking

Account locking permits privileged administrators to lock/unlock user accounts. No new client connections will be permitted if an account is locked (existing connections are not affected). For example:

```sql
CREATE USER 'marijn'@'localhost' ACCOUNT LOCK;
```

See [Account Locking](../../../security/user-account-management/account-locking.md) for more details.

{% tabs %}
{% tab title="Current" %}
The _lock\_option_ and _password\_option_ clauses can occur in either order.
{% endtab %}

{% tab title="<10.4.7, <10.5.8" %}
Prior to [MariaDB 10.4.7](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes) and [MariaDB 10.5.8](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1058-release-notes), the _lock\_option_ must be placed before the _password\_option_.
{% endtab %}
{% endtabs %}

From [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes) and [MariaDB 10.5.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1058-release-notes), the _lock\_option_ and _password\_option_ clauses can occur in either order.

## See Also

* [GRANT](grant.md)
* [ALTER USER](alter-user.md)
* [RENAME USER](rename-user.md)
* [DROP USER](drop-user.md)
* [CREATE ROLE](create-role.md)
* [SET PASSWORD](set-password.md)
* [SHOW CREATE USER](../administrative-sql-statements/show/show-create-user.md)
* [Troubleshooting Connection Issues](../../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md)
* [Authentication from MariaDB 10.4](../../../security/user-account-management/authentication-from-mariadb-10-4.md)
* [Identifier Names](../../sql-structure/sql-language-structure/identifier-names.md)
* [mysql.user table](../../system-tables/the-mysql-database-tables/mysql-user-table.md)
* [mysql.global\_priv\_table](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md)
* [Password Validation Plugins](../../plugins/password-validation-plugins/) - permits the setting of basic criteria for passwords
* [Authentication Plugins](../../plugins/authentication-plugins/) - allow various authentication methods to be used, and new ones to be developed.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
