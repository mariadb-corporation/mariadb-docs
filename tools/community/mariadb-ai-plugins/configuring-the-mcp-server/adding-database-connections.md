---
description: >-
  Add the database connections that the mariadb-shell MCP server may use, with
  the format of a connection URI, its connection options, and solutions for
  common connection errors.
---

# Adding Database Connections

The MCP server only connects to the databases that you add as connections with `mcp setup`. Each connection consists of a connection URI and a password. The URI tells MariaDB Shell how to reach the server and which account to sign in with; the password is stored separately in the MariaDB Shell secret store.

This page describes how to add a connection, how to write the connection URI, and how to solve common errors when the setup can't connect.

## Add a Connection

Run the setup and choose to add a connection:

```bash
mariadb-shell -- mcp setup
```

The setup then asks for the connection URI and for the password of the account. If it stores the URI in a different spelling, it shows the form it uses, for example with the default port added. It verifies the connection by opening a session to the server and closing it again, and only stores the connection if this succeeds.

You can also pass the URI on the command line. The setup then asks only for the password:

```bash
mariadb-shell -- mcp setup --addConnection='mariadb://mcp@db.example.com:3306'
```

Put the URI in single quotes, because characters such as `?`, `&`, and `(` have a special meaning in the shell.

{% hint style="danger" %}
Always enter the password at the prompt of the setup. Don't write it into the connection URI, a script, or an environment variable. With `--addConnection`, the setup refuses a URI that contains a password. In the walkthrough, it removes the password from the URI and asks for it at the prompt.
{% endhint %}

Use a dedicated MariaDB account with limited privileges for each connection, as described in [Database Accounts for the MCP Server](database-accounts-for-the-mcp-server.md).

## Connection URI Format

A connection URI has the following format. The parts in square brackets are optional:

```text
[scheme://][user@]<host[:port]|socket>[/schema][?option=value&option=value...]
```

| Part | Description |
| --- | --- |
| `scheme` | The protocol. `mariadb` is the default, and `mysql` is accepted as a synonym. For a connection through an SSH tunnel, use `mariadb+ssh`, as described in [Tunnel Database Connections via SSH](tunnel-database-connections-via-ssh.md). |
| `user` | The MariaDB account to sign in with. |
| `host` | The host name or IP address of the server. Enclose an IPv6 address in square brackets, for example `[2001:db8::10]`. |
| `port` | The TCP port of the server. Default: `3306`. |
| `socket` | The path of a Unix socket file, instead of host and port. See [Socket Connections](#socket-connections). |
| `schema` | A default schema for the session. See [Schemas and Options Are Part of the Connection](#schemas-and-options-are-part-of-the-connection). |
| `option=value` | Connection options, separated by `&`. See [Connection Options](#connection-options). |

### Examples

A server on the local network:

```text
mariadb://mcp@db.example.com:3306
```

A server addressed by its IPv6 address:

```text
mariadb://mcp@[2001:db8::10]:3306
```

A server that requires TLS and a verified server certificate:

```text
mariadb://mcp@db.example.com:3306?ssl-mode=VERIFY_IDENTITY&ssl-ca=/etc/ssl/certs/db-ca.pem
```

A server with a connection timeout of five seconds:

```text
mariadb://mcp@db.example.com?connect-timeout=5000
```

### Socket Connections

To connect to a server on the same machine through its Unix socket file, give the path of the socket instead of host and port. Either enclose the path in parentheses, or encode each `/` as `%2F`:

```text
mariadb://mcp@(/run/mysqld/mysqld.sock)
mariadb://mcp@%2Frun%2Fmysqld%2Fmysqld.sock
```

On Windows, you can connect to a server through a named pipe in the same way. `MySQL` is the default pipe name:

```text
mariadb://mcp@(\\.\MySQL)
```

### Special Characters

Apart from letters and digits, the user name, host, and option values can only contain the characters `-._~!$'()*+;` directly. Encode any other character as `%` followed by its hexadecimal ASCII code. For example, write the user name `app@eu` as `app%40eu`:

```text
mariadb://app%40eu@db.example.com
```

## Connection Options

The following options can be given in the query part of the URI. Option names aren't case-sensitive, and each option can only be given once.

| Option | Description |
| --- | --- |
| `ssl-mode` | Whether and how the connection uses TLS: `DISABLED`, `PREFERRED`, `REQUIRED`, `VERIFY_CA`, or `VERIFY_IDENTITY`. With `VERIFY_CA`, the server certificate must be signed by a trusted certificate authority; with `VERIFY_IDENTITY`, its host name must also match. |
| `ssl-ca` | The path of the certificate authority file, in PEM format. |
| `ssl-capath` | The path of a directory with certificate authority files, in PEM format. |
| `ssl-cert` | The path of the client certificate file, in PEM format. |
| `ssl-key` | The path of the client private key file, in PEM format. |
| `ssl-crl` | The path of a file with certificate revocation lists. |
| `ssl-crlpath` | The path of a directory with certificate revocation list files. |
| `ssl-cipher` | The permitted ciphers for TLS 1.2 and earlier. |
| `tls-version` | The permitted TLS protocol versions, for example `TLSv1.2,TLSv1.3`. |
| `tls-ciphersuites` | The permitted ciphers for TLS 1.3. |
| `auth-method` | The authentication plugin to use. |
| `connect-timeout` | The connection timeout in milliseconds. Default: 10 seconds. `0` disables the timeout. |
| `net-read-timeout` | The timeout for reading from the server, in milliseconds. |
| `net-write-timeout` | The timeout for writing to the server, in milliseconds. |
| `compression` | Whether the connection uses compression: `REQUIRED`, `PREFERRED`, or `DISABLED` (default). `true` and `false` are accepted as well. |
| `compression-algorithms` | A comma-separated list of compression algorithms. |
| `compression-level` | The compression level. |
| `connection-attributes` | Attributes that the server records for the session, in the form `[name1=value1,name2=value2]`. |

The timeouts are rounded up to whole seconds. The options for SSH tunnels are described in [Tunnel Database Connections via SSH](tunnel-database-connections-via-ssh.md). MariaDB Shell also accepts a few options for Kerberos and Oracle Cloud authentication, which aren't covered here.

## Schemas and Options Are Part of the Connection

The setup stores a connection under a normalized form of its URI. Spellings that mean the same connection are treated as one: a missing scheme is read as `mariadb://`, a missing port as `3306`, and the host name isn't case-sensitive.

A default schema and connection options, on the other hand, are part of the connection. If you add `mariadb://mcp@db.example.com/shop`, the agent must connect with exactly this URI, and the MCP server refuses `mariadb://mcp@db.example.com` unless it's configured as well. The same applies to options: if you add a connection with `ssl-mode=VERIFY_IDENTITY`, the agent can't connect to the same server without it. This way, the options you set are always applied to the agent's sessions.

In most cases, leave the schema out of the URI. The agent can then work with every schema that the account has privileges on, and qualifies object names with the schema. The agent finds the configured connections, with their exact URIs, with `db.list_connections`.

## Change or Remove a Connection

To remove a connection or to add it with a new password, run the setup again:

```bash
mariadb-shell -- mcp setup
```

Adding a connection that already exists updates its password.

Removing a connection revokes the agent's access to it. The MCP server checks the configured connections each time it opens a session, so it refuses the next session for the removed connection. A session that is in continuous use can stay open until it reaches its maximum lifetime of 12 hours. If the removal must take effect immediately, restart the MCP server.

## Troubleshooting

If the setup can't connect, it reports the error of the server or the client and doesn't store the connection:

```text
Could not connect to 'mariadb://mcp@db.example.com:3306': MySQL Error (1045): Access denied for user 'mcp'@'10.0.0.5' (using password: YES)
The connection was not stored.
```

The following table lists the most common errors. The numbers in parentheses at the end of some messages are operating system error codes.

| Error | Cause | Solution |
| --- | --- | --- |
| *MySQL Error (1045): Access denied for user '…'@'…' (using password: YES)* | The password is wrong, the account doesn't exist, or no account of that name may connect from your host. | Check the user name and enter the password again. Check which host the account is defined for, for example with `SELECT user, host FROM mysql.user`. |
| *MySQL Error (1130): Host '…' is not allowed to connect to this MariaDB server* | No account on the server may connect from your host. | Create the account for your host or network, as described in [Database Accounts for the MCP Server](database-accounts-for-the-mcp-server.md). |
| *MySQL Error (1044): Access denied for user '…'@'…' to database '…'* | The URI names a default schema that doesn't exist, or that the account has no privileges on. | Check the schema name, grant the account privileges on it, or leave the schema out of the URI. |
| *MySQL Error (4151): Access denied, this account is locked* | The account is locked. | Unlock it with `ALTER USER … ACCOUNT UNLOCK`. |
| *MySQL Error (1820): You must SET PASSWORD before executing this statement* | The password of the account has expired. | Set a new password for the account, then add the connection with the new password. |
| *MySQL Error (1226): User '…' has exceeded the 'max_user_connections' resource* | The account already has as many sessions open as its `MAX_USER_CONNECTIONS` limit allows. | Close other sessions of the account, or raise the limit. |
| *MySQL Error (2002): Can't connect to server on '…'* | No server is listening on the host and port, or a firewall blocks the connection. A timeout also produces this error. | Check the host name, the port, and that the server is running. If the server is only reachable through an SSH host, use a [tunnel](tunnel-database-connections-via-ssh.md). |
| *MySQL Error (2002): Can't connect to local server through socket '…'* | The socket file doesn't exist, or the server isn't running. | Check the path of the socket file, for example with `SELECT @@socket` on the server. |
| *MySQL Error (2005): Unknown server host '…'* | The host name can't be resolved. | Check the spelling of the host name, and that your machine can resolve it. |
| *'…' is not a valid connection URI.* | MariaDB Shell can't parse the URI, for example because of an unknown option, a character that must be encoded, or a port that isn't a number. | Check the option names against [Connection Options](#connection-options), and encode special characters as described in [Special Characters](#special-characters). |
| *The connection URI carries a password.* | The URI passed with `--addConnection` contains a password, for example `mcp:secret@host`. | Remove the password from the URI and enter it at the prompt. |
| *not a configured connection* | The agent used a URI that differs from the configured one, for example without its default schema or options. | Use the URI that `db.list_connections` reports. |
