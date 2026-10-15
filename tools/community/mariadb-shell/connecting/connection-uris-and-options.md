---
description: >-
  Describe a connection with a mariadb:// URI, a Python dictionary, or
  command-line options, and learn which setting wins when they overlap.
---

# Connection URIs and Options

Every connection that MariaDB Shell opens is described by the same set of connection options: who connects, to which server, how the transport is secured, and so on. You can supply these options in three forms, and mix them:

* A connection URI, such as `mariadb://dba@db1.example.com:3306/shop`. You can pass it on the command line, to `\connect`, or to Python functions such as `shell.connect()`.
* A Python dictionary, such as `{"host": "db1.example.com", "user": "dba"}`.
* Command-line options, such as `-h db1.example.com -u dba`.

## URI Syntax

A connection URI has the following parts. Only the host, or a socket path, is required.

```text
[scheme://][user[:password]@]host[:port][/schema][?option=value[&option=value...]]
```

| Part | Description | Default |
| --- | --- | --- |
| `scheme` | The protocol: `mariadb` or its synonym `mysql`. Add `+ssh` to connect through an SSH tunnel. | Classic protocol |
| `user` | The database account. | Your operating system user name |
| `password` | The account password. See [Passwords](#passwords). | Prompted |
| `host` | A host name, an IPv4 address, or an IPv6 address in square brackets. In place of a host and port, you can give the path of a Unix socket file or a Windows named pipe. | `localhost` |
| `port` | The TCP port. | `3306` |
| `schema` | The default schema to select after connecting. | None |
| `option=value` | Additional connection options. See [Connection Options](#connection-options). | |

Some examples:

```text
mariadb://dba@db1.example.com:3306/shop
mariadb://dba@10.0.4.17/sakila?ssl-mode=VERIFY_IDENTITY
dba@db1.example.com
mariadb://dba@[2001:db8::17]:3307
mariadb://app@(/run/mysqld/mysqld.sock)/shop
mariadb+ssh://dba@db1.example.com
```

### Schemes

MariaDB Shell names itself by the `mariadb` scheme. The `mysql` scheme means exactly the same thing, so URIs that you wrote for MySQL Shell keep working. Both select the classic client/server protocol, which MariaDB Shell uses for every connection.

You can leave the scheme out. A URI without a scheme also opens a classic session. The only difference is the local transport: a `mariadb://` or `mysql://` URI for `localhost` without a port uses the default Unix socket, while a URI without a scheme uses TCP. See [Sockets and Named Pipes](sockets-and-named-pipes.md).

The scheme extension `+ssh`, as in `mariadb+ssh://` or `mysql+ssh://`, tunnels the connection through SSH. See [SSH Tunnels](ssh-tunnels.md).

Any other scheme is rejected:

```text
Invalid URI: Invalid scheme [postgres], supported schemes include: mariadb, mysql, mysqlx
```

The error message lists `mysqlx`, but MariaDB Shell has no X Protocol support, and a `mysqlx://` URI fails when you connect.

### Passwords

You can include the password in the URI, as in `dba:S3cret@db1`, but you should avoid it. A password on the command line is visible to other users in the process list and ends up in your shell history. Instead, let MariaDB Shell prompt for it, read it from standard input with `--passwords-from-stdin`, or store it in the [credential store](credential-store.md). MariaDB Shell removes the password whenever it displays a URI.

To connect to an account that has no password without being prompted, use `--no-password` on the command line, or write an empty password, as in `dba:@db1`.

### URL Encoding

Each part of a URI may contain only letters, digits, and the characters `-._~!$'()*+;`. Encode any other character as `%` followed by its two-digit hexadecimal code. Common cases:

| Character | Encoded |
| --- | --- |
| `@` | `%40` |
| `:` | `%3A` |
| `/` | `%2F` |
| `%` | `%25` |
| `#` | `%23` |
| `,` | `%2C` |
| Space | `%20` |

For example, the account `report` with the password `p@ss:word` is written `report:p%40ss%3Aword@db1`.

File paths are the most common values that need encoding. Instead of encoding each slash, you can enclose a socket path or an option value in parentheses:

```text
mariadb://app@(/run/mysqld/mysqld.sock)/shop
mariadb://dba@db1?ssl-mode=VERIFY_CA&ssl-ca=(/etc/mysql/certs/ca.pem)
mariadb://dba@db1?ssl-mode=VERIFY_CA&ssl-ca=%2Fetc%2Fmysql%2Fcerts%2Fca.pem
```

### IPv6 Addresses

Enclose a literal IPv6 address in square brackets. If the address has a zone ID, encode the `%` that separates it from the address as `%25`:

```text
mariadb://dba@[::1]:3306
mariadb://dba@[fe80::1%25en0]:3306/shop
```

## Connection Options

Add options to the query string of a URI, separated by `&`, or use them as keys of a connection dictionary. Option names are case-insensitive, and each option may appear only once. Values in a URI must be URL-encoded.

| Option | Description |
| --- | --- |
| `ssl-mode`, `ssl-ca`, `ssl-capath`, `ssl-cert`, `ssl-key`, `ssl-crl`, `ssl-crlpath`, `ssl-cipher`, `tls-version`, `tls-ciphersuites` | TLS settings. See [Encrypted Connections](encrypted-connections.md). |
| `connect-timeout` | How long to wait for the server, in milliseconds. `0` waits indefinitely. Default: the `connectTimeout` shell option, 10 seconds. |
| `compression`, `compression-algorithms`, `compression-level` | Protocol compression. See [Compressed Connections](compressed-connections.md). |
| `connection-attributes` | Key-value pairs that the server records for the session. See [Connection Attributes](#connection-attributes). |
| `local-infile` | Whether the client allows `LOAD DATA LOCAL INFILE`. See [Local Data Loading](#local-data-loading). |
| `ssh-host`, `ssh-user`, `ssh-port`, `ssh-identity-file`, `ssh-config-file` | SSH tunnel settings, valid only with a `+ssh` scheme. See [SSH Tunnels](ssh-tunnels.md). |

### Connection Attributes

MariaDB Shell sends attributes that identify the client when it connects, such as `program_name` with the value `mariadb-shell`. MariaDB Server stores them in the Performance Schema tables `session_connect_attrs` and `session_account_connect_attrs`, if the Performance Schema is enabled. You can add your own attributes to tag the sessions of a job or an application.

In a URI, write the attributes as a comma-separated list in square brackets:

```text
mariadb://etl@db1/shop?connection-attributes=[job=nightly-load,team=data]
```

In a dictionary, use a list of `key=value` strings or a nested dictionary. Values are stored as strings.

```python
session = shell.open_session({
    "uri": "etl@db1/shop",
    "connection-attributes": {"job": "nightly-load", "batch": 42},
})
```

To check the attributes of your own session:

```sql
SELECT ATTR_NAME, ATTR_VALUE
FROM performance_schema.session_connect_attrs
WHERE PROCESSLIST_ID = CONNECTION_ID();
```

Attributes are fixed for the lifetime of a session. To stop MariaDB Shell from sending its own attributes, set `connection-attributes=false`. Connector/C still sends its built-in attributes, such as `_client_name` and `_os`.

### Local Data Loading

The `local-infile` option controls whether the client lets the server read files from your machine for `LOAD DATA LOCAL INFILE`. MariaDB Connector/C allows this by default, so the statement works as long as the server's `local_infile` system variable is `ON`. To refuse such requests, set the option to `false` or `0`:

```sh
mariadb-shell 'mariadb://dba@db1/shop?local-infile=0'
mariadb-shell --local-infile=0 dba@db1/shop
```

With local loading turned off, the statement fails with error 4166, `The used command is not allowed because the MariaDB server or client has disabled the local infile capability`.

## Connection Dictionaries

In Python, any function that takes connection data also accepts a dictionary. Besides the [connection options](#connection-options), a dictionary accepts the following keys:

| Key | Description |
| --- | --- |
| `uri` | A URI to start from. The other keys add to it or override its parts. |
| `scheme` | `mariadb`, `mysql`, `mariadb+ssh`, or `mysql+ssh`. |
| `user` | The database account. |
| `password` | The account password. |
| `host` | The host name or IP address. |
| `port` | The TCP port, as an integer. |
| `socket` | The path of a Unix socket file, or the name of a Windows named pipe. |
| `schema` | The default schema. |

A dictionary also accepts the older SSH keys `ssh`, `ssh-password`, `ssh-identity-file`, `ssh-identity-file-password`, and `ssh-config-file`. See [SSH Tunnels](ssh-tunnels.md#the-older-ssh-options).

```python
shell.connect({
    "host": "db1.example.com",
    "port": 3306,
    "user": "dba",
    "schema": "shop",
    "ssl-mode": "VERIFY_IDENTITY",
    "ssl-ca": "/etc/mysql/certs/ca.pem",
})
```

When a dictionary contains both `uri` and a key for the same setting, the key wins. The following call connects to port 3307:

```python
shell.connect({"uri": "dba@db1.example.com:3306", "port": 3307})
```

## Parsing and Building URIs

`shell.parse_uri()` splits a URI into a dictionary, and `shell.unparse_uri()` assembles a URI from a dictionary. Both are useful in scripts that store or rewrite connection data.

```text
MariaDB localhost:3306 ssl  Py > shell.parse_uri("mariadb://dba:p%40ss@db1.example.com/shop?ssl-mode=VERIFY_IDENTITY&connect-timeout=3000")
{"connect-timeout": 3000, "host": "db1.example.com", "password": "p@ss", "schema": "shop", "scheme": "mariadb", "ssl-mode": "VERIFY_IDENTITY", "user": "dba"}

MariaDB localhost:3306 ssl  Py > shell.unparse_uri({"scheme": "mariadb", "user": "app user", "host": "::1", "port": 3306, "ssl-mode": "REQUIRED"})
mariadb://app%20user@[::1]:3306?ssl-mode=REQUIRED
```

`shell.unparse_uri()` encodes the values for you. A tunnel URI survives the round trip: `shell.unparse_uri(shell.parse_uri(uri))` returns the same `mariadb+ssh://` URI.

## Command-Line Options

You can pass a URI as the first argument of `mariadb-shell`, or with `--uri`, and you can describe or adjust the connection with individual options.

| Option | Description |
| --- | --- |
| `URI`, `--uri=<uri>` | The connection URI. |
| `-h`, `--host=<name>` | The host. |
| `-P`, `--port=<port>` | The TCP port. |
| `-S`, `--socket[=<path>]` | Connect through a Unix socket file, or a named pipe on Windows. Without a value, the default socket is used. |
| `-u`, `--user=<name>` | The database account. |
| `-p` | Prompt for the password. |
| `--password[=<password>]` | The password. With an empty value, MariaDB Shell connects without a password. |
| `--no-password` | Connect without a password and don't prompt for one. |
| `--passwords-from-stdin` | Read passwords from standard input instead of the terminal. |
| `-D`, `--schema=<name>`, `--database=<name>` | The default schema. |
| `--connect-timeout=<ms>` | The connection timeout, in milliseconds. |
| `-C`, `--compress[=<value>]` | Protocol compression. See [Compressed Connections](compressed-connections.md). |
| `--local-infile[=<bool>]` | Allow or refuse `LOAD DATA LOCAL INFILE`. |
| `--ssl-mode`, `--ssl-ca`, `--ssl-capath`, `--ssl-cert`, `--ssl-key`, `--ssl-crl`, `--ssl-crlpath`, `--ssl-cipher`, `--tls-version`, `--tls-ciphersuites` | TLS settings. See [Encrypted Connections](encrypted-connections.md). |
| `--ssh`, `--ssh-identity-file`, `--ssh-config-file` | An SSH tunnel. See [SSH Tunnels](ssh-tunnels.md). |
| `--credential-store-helper`, `--save-passwords` | The credential store. See [Credential Store](credential-store.md). |

Examples:

{% tabs %}
{% tab title="URI" %}
```sh
mariadb-shell mariadb://dba@db1.example.com:3306/shop --sql
```
{% endtab %}

{% tab title="Individual options" %}
```sh
mariadb-shell -h db1.example.com -P 3306 -u dba -D shop --sql
```
{% endtab %}

{% tab title="Script without a prompt" %}
```sh
printf '%s\n' "$DB_PASSWORD" | mariadb-shell --passwords-from-stdin \
  mariadb://report@db1.example.com/shop --sql -e "SELECT COUNT(*) FROM orders"
```
{% endtab %}
{% endtabs %}

## Precedence

When several sources describe the same setting, MariaDB Shell applies the following rules:

1. Option files are read first and have the lowest priority. See [Option Files and Login Paths](option-files-and-login-paths.md).
2. Command-line options are processed from left to right, and a later option overrides an earlier one. A URI is treated like one option that sets all of its parts. It also resets the port, socket, and schema, even if the URI leaves them out.

   As a result, an option after the URI overrides the URI, and an option before it does not. In the first command, MariaDB Shell connects to port 3307. In the second, it connects to port 3306, the default, because the URI resets the port:

   ```sh
   mariadb-shell dba@db1.example.com -P 3307
   mariadb-shell -P 3307 dba@db1.example.com
   ```
3. In a connection dictionary, an explicit key overrides the same part of the `uri` key.
4. The `password` argument of `shell.connect()` and `shell.open_session()` overrides a password in the connection data.

## Related Shell Options

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `connectTimeout` | float | `10` | The default connection timeout for shell sessions, in seconds. The `connect-timeout` connection option overrides it for one connection. |
| `ssh.configFile` | string | empty | The default OpenSSH configuration file for tunnels. |
| `credentialStore.helper` | string | `default` | The helper that stores passwords. |

For all shell options, see [Configuration Options](../customizing/configuration-options.md).
