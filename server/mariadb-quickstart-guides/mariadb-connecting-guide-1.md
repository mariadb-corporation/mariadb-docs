# Connecting to MariaDB Server

This article covers connecting to MariaDB and the basic connection parameters. If you are completely new to MariaDB, take a look at [A MariaDB Primer](../../kb/en/a-mariadb-primer/) first.

In order to connect to the MariaDB server, the client software must provide the correct connection parameters. The client software will most often be the [mariadb client](../clients-and-utilities/mariadb-client/), used for entering statements from the command line, but the same concepts apply to any client, such as a [graphical client](../clients-and-utilities/graphical-and-enhanced-clients/), a client to run backups such as [mariadb-dump](../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), etc. The rest of this article assumes that the mariadb command line client is used.

If a connection parameter is not provided, it will revert to a default value.

For example, to connect to MariaDB using only default values with the mariadb client, enter the following from the command line:

```bash
mariadb
```

In this case, the following defaults apply:

* The host name is `localhost`.
* The user name is either your Unix login name, or `ODBC` on Windows.
* No password is sent.
* The client will connect to the server with the default socket, but not any particular database on the server.

These defaults can be overridden by specifying a particular parameter to use. For example:

```bash
mariadb -h 166.78.144.191 -u username -ppassword database_name
```

In this case:

* `-h` specifies a host. Instead of using `localhost`, the IP `166.78.144.191` is used.
* `-u` specifies a user name, in this case `username`
* `-p` specifies a password, `password`. Note that for passwords, unlike the other parameters, there cannot be a space between the option (`-p`) and the value (`password`). It is also not secure to use a password in this way, as other users on the system can see it as part of the command that has been run. If you include the `-p` option, but leave out the password, you will be prompted for it, which is more secure.
* The database name is provided as the first argument after all the options, in this case `database_name`.
* It will connect with the default tcp\_ip port, 3306

## Connection Parameters

### host

```bash
--host=name
-h name
```

Connect to the MariaDB server on the given host. The default host is `localhost`. By default, MariaDB does not permit remote logins - see [Configuring MariaDB for Remote Client Access](mariadb-remote-connection-guide.md).

### password

```bash
--password[=passwd]
-p[passwd]
```

The password of the MariaDB account. It is generally not secure to enter the password on the command line, as other users on the system can see it as part of the command that has been run. If you include the `-p` or `--password` option, but leave out the password, you will be prompted for it, which is more secure.

### pipe

```bash
--pipe
-W
```

On Windows systems that have been started with the `--enable-named-pipe` option, use this option to connect to the server using a named pipe.

### port

```bash
--port=num
-P num
```

The TCP/IP port number to use for the connection. The default is `3306`.

### protocol

```bash
--protocol=name
```

Specifies the protocol to be used for the connection for the connection. It can be one of `TCP`, `SOCKET`, `PIPE` or `MEMORY` (case-insensitive). Usually you would not want to change this from the default. For example on Unix, a Unix socket file (`SOCKET`) is the default protocol, and usually results in the quickest connection.

* `TCP`: A TCP/IP connection to a server (either local or remote). Available on all operating systems.
* `SOCKET`: A Unix socket file connection, available to the local server on Unix systems only. If socket is not specified with --socket, in a config file or with the environment variable `MYSQL_UNIX_PORT` then the default `/tmp/mysql.sock` will be used.
* `PIPE`. A named-pipe connection (either local or remote). Available on Windows only.
* `MEMORY`. Shared-memory connection to the local server on Windows systems only.

### shared-memory-base-name

```bash
--shared-memory-base-name=name
```

Only available on Windows systems in which the server has been started with the `--shared-memory` option, this specifies the shared-memory name to use for connecting to a local server. The value is case-sensitive, and defaults to `MARIADB`.

### socket

```bash
--socket=name
-S name
```

For connections to localhost, this specifies either the Unix socket file to use (default `/tmp/mysql.sock`), or, on Windows where the server has been started with the `--enable-named-pipe` option, the name (case-insensitive) of the named pipe to use (default `MARIADB`).

### TLS Options

A brief listing is provided below. See [Secure Connections Overview](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md) and [TLS System Variables](../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md) for more detail.

#### ssl

```bash
--ssl
```

Enable TLS for connection (automatically enabled with other TLS flags). Disable with '`--skip-ssl`'

#### ssl-ca

```bash
--ssl-ca=name
```

CA file in PEM format (check OpenSSL docs, implies `--ssl`).

#### ssl-capath

```bash
--ssl-capath=name
```

|                                                   |
| ------------------------------------------------- |
| CA directory (check OpenSSL docs, implies --ssl). |

#### ssl-cert

```bash
--ssl-cert=name
```

X509 cert in PEM format (implies `--ssl`).

#### ssl-cipher

```bash
--ssl-cipher=name
```

TLS cipher to use (implies `--ssl`).

#### ssl-key

```bash
--ssl-key=name
```

X509 key in PEM format (implies `--ssl`).

#### ssl-crl

```bash
--ssl-crl=name
```

Certificate revocation list (implies `--ssl`).

#### ssl-crlpath

```bash
--ssl-crlpath=name
```

Certificate revocation list path (implies `--ssl`).

#### ssl-verify-server-cert

```bash
--ssl-verify-server-cert
```

Verify server's "Common Name" in its cert against hostname used when connecting. This option is disabled by default.

### user

```bash
--user=name
-u name
```

The MariaDB user name to use when connecting to the server. The default is either your Unix login name, or `ODBC` on Windows. See the [GRANT](../reference/sql-statements/account-management-sql-statements/grant.md) command for details on creating MariaDB user accounts.

## Option Files

It's also possible to use option files (or configuration files) to set these options. Most clients read option files. Usually, starting a client with the `--help` option will display which files it looks for as well as which option groups it recognizes.

## See Also

* [A MariaDB Primer](../../kb/en/a-mariadb-primer/)
* [mariadb client](../clients-and-utilities/mariadb-client/)
* [Clients and Utilities](../clients-and-utilities/)
* [Configuring MariaDB for Remote Client Access](../../kb/en/configuring-mariadb-for-remote-client-access/)
* [--skip-grant-tables](../server-management/starting-and-stopping-mariadb/mariadbd-options.md) allows you to start MariaDB without `GRANT`. This is useful if you lost your root password.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
