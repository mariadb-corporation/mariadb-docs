---
description: >-
  Connect to a local MariaDB server through a Unix socket file, or through a
  named pipe on Windows, instead of TCP.
---

# Sockets and Named Pipes

A server on the same machine can be reached without the network stack. On Linux and macOS, MariaDB Shell connects through the server's Unix socket file. On Windows, it can connect through a named pipe. Local transports avoid TCP overhead, and on Linux they make `unix_socket` authentication possible.

## Unix Socket Files

To connect through a socket file, give its path in place of the host and port. In a URI, you have two ways to write the path:

* Enclose it in parentheses. This is the more readable form.
* Write the first `/` as is, and encode every further `/` as `%2F`.

```text
mariadb://app@(/run/mysqld/mysqld.sock)/shop
mariadb://app@/run%2Fmysqld%2Fmysqld.sock/shop
```

Relative paths start with `./` or `../`, and are resolved against the current directory:

```text
app@(./data/mysqld.sock)
app@.%2Fdata%2Fmysqld.sock
```

On the command line, use `-S` or `--socket`, and in a connection dictionary, use the `socket` key:

{% tabs %}
{% tab title="Command line" %}
```sh
mariadb-shell -u app -S /run/mysqld/mysqld.sock -D shop --sql
```
{% endtab %}

{% tab title="Python" %}
```python
shell.connect({"user": "app", "socket": "/run/mysqld/mysqld.sock", "schema": "shop"})
```
{% endtab %}
{% endtabs %}

To confirm the transport, run `\status`. The `Connection` line reads `Localhost via UNIX socket`, and the `Unix socket` line shows the path.

### The Default Socket

MariaDB Shell uses the default socket file in the following cases:

* You pass `-S` or `--socket` without a value.
* The URI has the `mariadb://` or `mysql://` scheme, names `localhost` as the host, and has no port, as in `mariadb://app@localhost`.

The default path is compiled into MariaDB Connector/C, and is usually `/tmp/mysql.sock`. You can override it with the `MYSQL_UNIX_PORT` environment variable, or with a `socket` setting in the `[client]` or `[mariadb-shell]` group of an option file. See [Option Files and Login Paths](option-files-and-login-paths.md).

```ini
[client]
socket = /run/mysqld/mysqld.sock
```

{% hint style="warning" %}
Many Linux packages of MariaDB Server place the socket at `/run/mysqld/mysqld.sock` or `/var/lib/mysql/mysql.sock`, not at the Connector/C default. If a socket connection fails with error 2002, check the server's `socket` system variable and pass that path explicitly.
{% endhint %}

A URI or a set of options without a scheme connects over TCP, even for `localhost`. For example, `app@localhost` and `-h localhost -u app` both connect to `localhost:3306` over TCP. To use the default socket instead, add the scheme or `-S`.

### Socket Authentication

The `unix_socket` authentication plugin identifies the client by the operating system account that owns the connecting process, and works only over a socket. On many Linux installations, the MariaDB `root` account uses it. To connect as such an account, run MariaDB Shell as the matching operating system user, and connect through the socket without a password:

```sh
sudo mariadb-shell --no-password -u root -S /run/mysqld/mysqld.sock --sql
```

## Windows Named Pipes

MariaDB Server on Windows accepts named-pipe connections when it runs with the `named_pipe` system variable enabled. The pipe name is the value of the server's `socket` variable, which defaults to `MySQL`.

To connect through a named pipe, set the host to `.` and leave out the port. MariaDB Shell then uses the default pipe name, `MySQL`. To give a different pipe name, use one of the following forms:

{% tabs %}
{% tab title="URI" %}
```text
app@\\.\MariaDB
app@(\\.\MariaDB)
```

Enclose the name in parentheses when it contains characters that would otherwise need URL encoding.
{% endtab %}

{% tab title="Command line" %}
```powershell
mariadb-shell -u app -S MariaDB --sql
```
{% endtab %}

{% tab title="Python" %}
```python
shell.connect({"user": "app", "socket": "MariaDB"})
```
{% endtab %}
{% endtabs %}

On Windows, MariaDB Shell connects over TCP unless you ask for a named pipe. There are no Unix socket files on Windows, so `-S` and the `socket` key always name a pipe there.

{% hint style="info" %}
Sandbox instances on Windows don't enable named pipes, so you connect to them over TCP. See [Sandbox Instances](../sandbox-instances.md).
{% endhint %}

## Shared Memory

MariaDB Shell doesn't support shared-memory connections on Windows. It never requests the shared-memory transport from Connector/C, so a local connection without a pipe uses TCP, even if the server has `shared_memory` enabled.
