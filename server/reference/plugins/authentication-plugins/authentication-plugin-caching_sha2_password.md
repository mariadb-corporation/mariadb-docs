# Authentication Plugin - caching\_sha2\_password

{% hint style="info" %}
This plugin is available from MariaDB Enterprise Server 11.8.
{% endhint %}

## Overview

MariaDB provides two authentication plugins that implement SHA-256 hashing for user account passwords:

* `caching_sha2_password`: Implements SHA-256 authentication, using caching on the server side for better performance, and with additional features for wider applicability.
* [sha256\_password](../../clientserver-protocol/1-connecting/caching_sha2_password-authentication-plugin.md): Implements basic SHA-256 authentication. This is deprecated and subject to removal in the future.

This page documents the **caching** SHA-256 authentication plugin. For the non-caching plugin, see [this page](authentication-plugin-sha-256.md).

`caching_sha2_password` is the default authentication plugin, rather than [mysql\_native\_password](authentication-plugin-mysql_native_password.md).

{% hint style="warning" %}
To connect to the server using an account that authenticates with the `caching_sha2_password` plugin, you must use a secure connection or an unencrypted connection that supports password exchange using an RSA key pair.
{% endhint %}

{% hint style="info" %}
**sha256** refers to the 256-bit digest length the plugin uses for encryption.
{% endhint %}

The `caching_sha2_password` plugin has the following advantages over the `sha256_password` plugin:

* On the server side, an in-memory cache enables faster reauthentication of users who have connected previously when they connect again.
* RSA-based password exchange is available regardless of the SSL library against which MariaDB is linked.
* Support is provided for client connections that use the Unix socket-file and shared-memory protocols.

## Installing the Plugin

The `caching_sha2_password` plugin exists in server and client forms:

* The server-side plugin is built into the server, doesn't have to be loaded explicitly, and cannot be disabled (unloaded).
* The client-side plugin is built into the `libmysqlclient` client library and is available to any program linked against `libmysqlclient`.

## Using the Plugin

To set up an account that uses the deprecated `sha256_password` plugin for SHA-256 password hashing, use the following statement, where _`password`_ is the account password:

```sql
CREATE USER 'sha2user'@'localhost'
IDENTIFIED WITH caching_sha2_password BY 'password';
```

The server assigns the `caching_sha256_password` plugin to the account and uses it to encrypt the password using SHA-256, storing the values in the `plugin` and `authentication_string` columns of the `mysql.user` system table.

To start the server with the default authentication plugin set to `sha256_password`, add this to the [configuration file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) (for instance, `my.cnf`):

```ini
[mysqld]
default_authentication_plugin=caching_sha2_password
```

This makes the `caching_sha256_password` plugin the default for new accounts. With that setting, you can simplify the creation of users that are meant to use this plugin for authentication:

```sql
CREATE USER 'some-user'@'localhost' IDENTIFIED BY 'password';
```

To use a plugin other than the (now) default, for example, the `mysql_native_password` plugin, issue this statement:

```sql
CREATE USER 'some-user'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'password';
```

## RSA Support

`caching_sha2_password` supports connections over secure transport. If configured, it also supports encrypted password exchange using RSA over unencrypted connections. RSA support has these features:

* Clients that are in possession of the RSA public key can perform RSA key pair-based password exchange with the server during the connection process.
*   For connections from accounts that authenticate with `caching_sha2_password` and RSA key pair-based password exchange, the server does not send the RSA public key to clients by default. Clients can use a client-side copy of the required public key, or request the public key from the server.

    Using a trusted local copy of the public key enables the client to avoid a round trip in the client/server protocol, and is more secure than requesting the public key from the server. On the other hand, requesting the public key from the server is more convenient (it requires no management of a client-side file) and may be acceptable in secure network environments.

    If the option is given to specify a valid public key file, it takes precedence over the option to request the public key from the server.

For clients using the `caching_sha2_password` plugin, passwords are never exposed as cleartext when connecting to the server. How password transmission occurs depends on whether a secure connection or RSA encryption is used:

* If the connection is secure, no RSA key pair is used. This applies to TCP connections encrypted using TLS, as well as Unix socket-file and shared-memory connections. The password is sent as cleartext but cannot be intercepted because the connection is secure.
* If the connection is not secure, an RSA key pair is used. This applies to TCP connections not encrypted using TLS and named-pipe connections. RSA is used only for password exchange between client and server, to prevent password snooping. When the server receives the encrypted password, it decrypts it. A scramble is used in the encryption to prevent repeat attacks.

**Cache Operation for SHA-2 Pluggable Authentication**

On the server side, the `caching_sha2_password` plugin uses an in-memory cache for faster authentication of clients who have connected previously. Entries consist of account-name/password-hash pairs. The cache works like this:

1. When a client connects, `caching_sha2_password` checks whether the client and password match some cache entry. If so, authentication succeeds.
2. If there is no matching cache entry, the plugin attempts to verify the client against the credentials in the `mysql.user` system table. If this succeeds, `caching_sha2_password` adds an entry for the client to the hash. Otherwise, authentication fails and the connection is rejected.

This way, when a client first connects, authentication against the `mysql.user` system table occurs. When the client connects subsequently, faster authentication against the cache occurs.

Password cache operations other than adding entries are handled by the `sha2_cache_cleaner` audit plugin, which performs these actions on behalf of `caching_sha2_password`:

* It clears the cache entry for any account that is renamed or dropped, or any account for which the credentials or authentication plugin are changed.
* It empties the cache when the [FLUSH PRIVILEGES](../../sql-statements/administrative-sql-statements/flush-commands/) statement is executed.
* It empties the cache at server shutdown. (This means the cache is not persistent across server restarts.)

Cache clearing operations affect the authentication requirements for subsequent client connections. For each user account, the first client connection for the user after any of the following operations must use a secure connection (made using TCP using TLS credentials, a Unix socket file, or shared memory) or RSA key pair-based password exchange:

* After account creation.
* After a password change for the account.
* After a [RENAME USER](../../sql-statements/account-management-sql-statements/rename-user.md) statement for the account.
* After issuing [FLUSH PRIVILEGES](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).

`FLUSH PRIVILEGES` clears the entire cache and affects all accounts that use the `caching_sha2_password` plugin. The other operations clear specific cache entries and affect only accounts that are part of the operation.

Once a user authenticates successfully, the account is entered into the cache, and subsequent connections do not require a secure connection or the RSA key pair, until another cache clearing event occurs that affects the account. (When the cache can be used, the server uses a challenge-response mechanism that does not use cleartext password transmission and does not require a secure connection.)
