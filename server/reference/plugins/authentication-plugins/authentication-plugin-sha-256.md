---
description: >-
  The SHA-256 authentication plugin uses the SHA-256 hashing algorithm for
  password storage, offering stronger security than the default SHA-1 method.
---

# Authentication Plugin - SHA-256

## Background

MySQL 5.6 added support for the [sha256\_password](pluggable-authentication-overview.md) authentication plugin, and MySQL 8.0 also added support for the [caching\_sha2\_password](authentication-with-pluggable-authentication-modules-pam/) authentication plugin.

The `caching_sha2_password` plugin is now the default authentication plugin in MySQL 8.0.4 and above, based on the value of the [default\_authentication\_plugin](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin) system variable.

## Support in MariaDB Server

{% hint style="warning" %}
MariaDB **Server** does not support the [sha256\_password](https://dev.mysql.com/doc/refman/5.6/en/sha256-pluggable-authentication.html) plugin. A `caching_sha2_password` authentication plugin was added in MariaDB [Community Server 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1) and [Enterprise Server 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.8/whats-new-in-mariadb-enterprise-server-11.8). See [MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804) for more information.
{% endhint %}

Reasons for not supporting the SHA-256 plugin:

* To use the protocol, you have to distribute the server's public key to all MariaDB users, which can be cumbersome and impractical.
* The server receives the password in clear text, which can cause problems if the user connects to a malicious server.

If you are migrating from a MySQL instance that is using SHA-256 authentication, you have to change the SHA-256 authentication to `mysql_native_authentication` :

```sql
ALTER USER user_name IDENTIFIED WITH mysql_native_password BY 'new_password'
```

## Support in Client Libraries

### Client Authentication Plugins

For clients that use the [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) library, MariaDB provides client authentication plugins that are compatible with MySQL's SHA-256 authentication plugins:

* `sha256_password`
* `caching_sha256_password`

When connecting with a [client or utility](../../../clients-and-utilities/) to a server, using a user account that authenticates with the `sha256_password` or `caching_sha256_password` authentication plugin, you may need to tell the client where to find the relevant client authentication plugin by specifying the `--plugin-dir` option:

```bash
mysql --plugin-dir=/usr/local/mysql/lib64/mysql/plugin --user=alice
```

{% hint style="warning" %}
For clients that use MariaDB's `libmysqlclient` library instead of [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), those authentication plugins are not supported.
{% endhint %}

#### `sha256_password`

The `sha256_password` client authentication plugin is compatible with MySQL's [sha256\_password](https://dev.mysql.com/doc/refman/5.6/en/sha256-pluggable-authentication.html) authentication plugin, which was added in MySQL 5.6.

#### `caching_sha256_password`

The `caching_sha256_password` client authentication plugin is compatible with MySQL's [caching\_sha2\_password](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html) authentication plugin, which was added in MySQL 8.0.

The `caching_sha2_password` plugin is now the default authentication plugin in MySQL 8.0.4 and above, based on the value of the [default\_authentication\_plugin](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin) system variable.

### Using the Plugin with MariaDB Connector/C

[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) supports `sha256_password` and `caching_sha2_password` authentication using the [client authentication plugins](authentication-plugin-sha-256.md#client-authentication-plugins) mentioned in the previous section.

It has supported the `sha256_password` client authentication plugin since MariaDB Connector/C 3.0.2. See [CONC-229](https://jira.mariadb.org/browse/CONC-229) for more information.

It has supported the `caching_sha256_password` client authentication plugin since MariaDB Connector/C 3.0.8 and MariaDB Connector/C 3.1.0. See [CONC-312](https://jira.mariadb.org/browse/CONC-312) for more information.

### Using Plugins with MariaDB Connector/ODBC

[MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc) supports `sha256_password` and `caching_sha2_password` authentication using the [client authentication plugins](authentication-plugin-sha-256.md#client-authentication-plugins) mentioned in the previous section.

It has supported `sha256_password` and `caching_sha2_password` authentication since MariaDB Connector/ODBC 3.1.4. See [ODBC-241](https://jira.mariadb.org/browse/ODBC-241) for more information.

### Using Plugins with MariaDB Connector/J

[MariaDB Connector/J](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j) supports `sha256_password` and `caching_sha2_password` authentication since MariaDB Connector/J 2.5.0. See [CONJ-327](https://jira.mariadb.org/browse/CONJ-327) and [CONJ-663](https://jira.mariadb.org/browse/CONJ-663) for more information.

note: The version 3.x being a rewrite of the connector, only caching\_sha2\_password is implemented, since sha256\_password is only implemented on EOL version.

### Using Plugins with MariaDB Connector/Node.js

[MariaDB Connector/Node.js](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs) supports `sha256_password` and `caching_sha2_password` authentication since MariaDB Connector/Node.js 2.5.0. See [CONJS-76](https://jira.mariadb.org/browse/CONJS-76) and [CONJS-77](https://jira.mariadb.org/browse/CONJS-77) for more information.

## See Also

* [MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804) contains the plans to use if we ever decide to support these protocols.
* [History of MySQL and MariaDB authentication protocols](https://mariadb.org/history-of-mysql-mariadb-authentication-protocols)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
