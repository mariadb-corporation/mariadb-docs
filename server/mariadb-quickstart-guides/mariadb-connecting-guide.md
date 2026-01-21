---
description: >-
  This guide details how to connect to a MariaDB server using the command-line
  client, covering options for host, user, password, and protocol.
---

# Connecting to MariaDB Guide

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/G9gr3KMrlccJhmFh3SNT/" %}

This guide details the parameters for connecting to a MariaDB server using client programs like `mariadb`. Learn about default connection behaviors and how to use various command-line options to customize your connection, including secure TLS configurations.

While the examples focus on the `mariadb` command-line client, the concepts apply to other clients like graphical interfaces or backup utilities (e.g., `mariadb-dump`). If you are completely new to MariaDB, refer to [A MariaDB Primer](mariadb-usage-guide.md) first.

### Default Connection Behavior

When a connection parameter is not explicitly provided, a default value is used. To connect using only default values with the `mariadb` client:

```
mariadb
```

In this scenario, the following defaults typically apply:

* **Host name:** `localhost`
* **User name:** Your Unix login name (on Unix-like systems) or `ODBC` (on Windows).
* **Password:** No password is sent.
* **Database:** The client connects to the server but not to a specific database by default.
* **Socket:** The default socket file is used for connection.

### Overriding Defaults

You can override these defaults by specifying parameters. For example:

```bash
mariadb -h 166.78.144.191 -u username -ppassword database_name
```

In this example:

* `-h 166.78.144.191`: Specifies the host IP address instead of `localhost`.
* `-u username`: Specifies `username` as the MariaDB user.
* `-ppassword`: Specifies `password` as the password.
  * **Note:** For passwords, there must be no space between `-p` and the password value.
  * **Security Warning:** Providing a password directly on the command line is insecure as it can be visible to other users on the system. It's more secure to use `-p` without the password value, which will prompt you to enter it.
* `database_name`: This is the name of the database to connect to, provided as the first argument after all options.
* The connection will use the default TCP/IP port (usually 3306).

### Connection Parameters

The following are common connection parameters:

#### host

* `--host=name`
* `-h name`

Connects to the MariaDB server on the given host.

Default: localhost.

MariaDB typically does not permit remote logins by default; see Configuring MariaDB for Remote Client Access.

#### password

* `--password[=passwd]`
* `-p[passwd]`

Specifies the password for the MariaDB account.

* **Security Best Practice:** For improved security, use the `-p` or `--password` option without providing the password value directly on the command line. You will be prompted to enter it, preventing it from being visible in command history or process lists.

#### pipe

* `--pipe`
* `-W`

(Windows only) Connects to the server using a named pipe, if the server was started with the `--enable-named-pipe` option.

#### port

* `--port=num`
* `-P num`

Specifies the TCP/IP port number for the connection.

Default: 3306.

#### protocol

* `--protocol=name`

Specifies the connection protocol. Possible values (case-insensitive): `TCP`, `SOCKET`, `PIPE`, `MEMORY`. The default protocol is typically the most efficient for the operating system (e.g., `SOCKET` on Unix).

* **TCP:** TCP/IP connection (local or remote). Available on all OS.
* **SOCKET:** Unix socket file connection (local server on Unix systems only). If `--socket` is not specified, the default is `/tmp/mysql.sock`.
* **PIPE:** Named-pipe connection (local or remote). Windows only.
* **MEMORY:** Shared-memory connection (local server on Windows systems only).

#### shared-memory-base-name

* `--shared-memory-base-name=name`

(Windows only) Specifies the shared-memory name for connecting to a local server started with the --shared-memory option. The value is case-sensitive.

Default: MARIADB.

#### socket

* `--socket=name`
* `-S name`

For connections to `localhost`:

* On Unix: Specifies the Unix socket file to use. _Default:_ `/tmp/mysql.sock`.
* On Windows: Specifies the name (case-insensitive) of the named pipe if the server was started with `--enable-named-pipe`. _Default:_ `MARIADB`.

#### user

* `--user=name`
* `-u name`

Specifies the MariaDB user name for the connection.

Default: Your Unix login name (on Unix-like systems) or ODBC (on Windows).

See the GRANT command for information on creating MariaDB user accounts.

### TLS Options

These options control the use of TLS (Transport Layer Security) for secure connections. For comprehensive details, see [Secure Connections Overview](../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md) and [TLS System Variables](../security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables.md).

* **`--ssl`**: Enable TLS for the connection. Automatically enabled if other `--ssl-*` flags are used. Disable with `--skip-ssl`.
* **`--ssl-ca=name`**: CA (Certificate Authority) file in PEM format. (Implies `--ssl`).
* **`--ssl-capath=name`**: Directory containing CA certificates in PEM format. (Implies `--ssl`).
* **`--ssl-cert=name`**: Client X.509 certificate in PEM format. (Implies `--ssl`).
* **`--ssl-cipher=name`**: Specific TLS cipher(s) to use for the connection. (Implies `--ssl`).
* **`--ssl-key=name`**: Client X.509 private key in PEM format. (Implies `--ssl`).
* **`--ssl-crl=name`**: Certificate Revocation List (CRL) file in PEM format. (Implies `--ssl`).
* **`--ssl-crlpath=name`**: Directory containing CRL files. (Implies `--ssl`).
* **`--ssl-verify-server-cert`**: Verifies the server's certificate "Common Name" against the hostname used for connecting. Disabled by default.

### Option Files

Connection parameters and other options can also be set in option files (configuration files), which most MariaDB clients read upon startup. To see which option files a client reads and the option groups it recognizes, typically run the client with the `--help` option.

{% @marketo/form formId="4316" %}
