---
description: >-
  Open, switch, and close the global session, work with additional sessions in
  Python, and use the methods of a ClassicSession object.
---

# Sessions

A session is a connection from MariaDB Shell to a server. All sessions use the classic MariaDB client/server protocol and are represented in Python by `ClassicSession` objects.

## The Global Session

The shell has at most one global session at a time. SQL mode sends statements through it, the prompt shows its host, port, and TLS state, and in Python mode it is available as the `session` global object. The [utilities](../utilities/) also run against the global session unless they take their own connection data.

You establish the global session in one of these ways:

* Pass connection data on the command line when you start the shell. See [Starting MariaDB Shell](starting-mariadb-shell.md#connect-when-the-shell-starts).
* Use the `\connect` command, in either mode.
* Call `shell.connect()` in Python mode.
* Make an existing session object global with `shell.set_session()`.

When you open a new global session with `\connect` or `shell.connect()`, the shell closes the previous one and prints `Closing old connection...`.

### Connect with \connect

`\connect`, or its shortcut `\c`, opens a session and makes it the global session:

```text
MariaDB  SQL > \connect mariadb://app_user@db1.example.com:3306/shop
Creating a Classic session to 'app_user@db1.example.com:3306/shop'
Please provide the password for 'app_user@db1.example.com:3306':
Fetching schema names for auto-completion... Press ^C to stop.
Your MariaDB connection id is 412
Server version: 11.8.3-MariaDB-log MariaDB Server
Default schema set to `shop`.
MariaDB db1.example.com:3306 ssl  shop  SQL >
```

The command accepts the same URIs as the command line. To connect through an SSH tunnel, add `--ssh <ssh-uri>` before the URI. See [Connection URIs and Options](../connecting/connection-uris-and-options.md) and [SSH Tunnels](../connecting/ssh-tunnels.md).

### Connect from Python

`shell.connect(connectionData[, password])` opens the global session and returns it. The connection data is a URI string or a dictionary of connection options. The optional `password` argument overrides a password in the connection data:

```text
MariaDB  Py > shell.connect("mariadb://app_user@db1.example.com/shop")
MariaDB  Py > shell.connect({"user": "app_user", "host": "db1.example.com", "port": 3306, "schema": "shop"}, "s3cr3t")
```

`shell.get_session()` returns the global session object, the same object as the `session` global.

### Check the Session with \status

`\status`, or its shortcut `\s`, prints information about the global session, including the connection ID, the current user and schema, the TLS cipher, the server version, the client library version, the character sets, and the server uptime. `shell.status()` prints the same information from Python. Without a global session, the command reports `Not Connected.`

```text
MariaDB localhost:3306 ssl  SQL > \status
MariaDB Shell version 26.9.5

Connection Id:                31
Current schema:               shop
Current user:                 app_user@localhost
SSL:                          Cipher in use: TLS_AES_256_GCM_SHA384 TLSv1.3
Using delimiter:              ;
Server version:               11.8.3-MariaDB-log MariaDB Server
Protocol version:             Classic 10
Client library:               3.4.10
Connection:                   localhost via TCP/IP
...
```

### Change the Default Schema

`\use <schema>`, or `\u <schema>`, sets the default schema of the global session. In Python mode, `shell.set_current_schema("<schema>")` does the same.

### Reconnect and Disconnect

| Command | Python equivalent | Description |
| --- | --- | --- |
| `\reconnect` | `shell.reconnect()` | Reconnects the global session with the same connection data, for example after the server closed an idle connection. |
| `\disconnect` | `shell.disconnect()` | Closes the global session. The `session` global becomes `None`, and SQL statements fail with `Not connected.` until you connect again. |

## Additional Sessions in Python

In Python mode, you can open more sessions alongside the global one, for example to compare two servers or to run a long query on a separate connection.

* `shell.open_session([connectionData][, password])` opens a session and returns it without changing the global session. Without connection data, it opens a new session with the same connection data as the global session.
* `mysql.get_session(connectionData[, password])` and `mysql.get_classic_session(connectionData[, password])` do the same through the `mysql` module.
* `session.clone()` opens a new session to the same server as an existing one.

```python
replica = shell.open_session("mariadb://monitor@db2.example.com:3306")
primary_pos = session.run_sql("SELECT @@gtid_binlog_pos").fetch_one()[0]
replica_pos = replica.run_sql("SELECT @@gtid_slave_pos").fetch_one()[0]
print(primary_pos, replica_pos)
replica.close()
```

To make one of these sessions the global session, pass it to `shell.set_session()`:

```text
MariaDB db1.example.com:3306 ssl  Py > reporting = shell.open_session("mariadb://report@db3.example.com")
MariaDB db1.example.com:3306 ssl  Py > shell.set_session(reporting)
MariaDB db3.example.com:3306 ssl  Py >
```

Unlike `shell.connect()`, `shell.set_session()` does not close the previous global session. Sessions that you open yourself stay open until you call `close()` or the shell exits.

## ClassicSession Methods

A `ClassicSession` object, whether it is the global `session` or one you opened yourself, provides the following properties and methods. Each property also has a getter method, for example `uri` and `get_uri()`.

| Property | Description |
| --- | --- |
| `uri` | The connection URI of the session, without the password. |
| `ssh_uri` | The URI of the SSH tunnel the session uses, or an empty string. |
| `connection_id` | The connection ID that the server assigned to the session. |
| `server_vendor` | The vendor of the connected server: `MariaDB` or `MySQL`. |

| Method | Description |
| --- | --- |
| `run_sql(query[, args])` | Runs an SQL statement and returns a `ClassicResult`. Placeholders (`?`) in the statement are replaced by the values in the `args` list, which are escaped and quoted. |
| `start_transaction()` | Starts a transaction. |
| `commit()` | Commits the current transaction. |
| `rollback()` | Rolls back the current transaction. |
| `get_sql_mode()` | Returns the value of `sql_mode` for the session. |
| `is_open()` | Returns `True` if the session is open. |
| `close()` | Closes the session. |
| `clone()` | Opens and returns a new session to the same server with the same connection data. |
| `set_client_data(key, value)` | Stores a value in the session object under a key, for use by your own scripts and plugins. The value is not sent to the server. |
| `get_client_data(key)` | Returns a value stored with `set_client_data()`. |
| `help([member])` | Prints help for the class or one of its members. |

For example, the following code inserts rows in a transaction and rolls back if any statement fails:

```python
s = shell.open_session("mariadb://app_user@localhost/shop")
s.start_transaction()
try:
    for order_id, total in [(1001, 49.90), (1002, 15.00)]:
        s.run_sql("INSERT INTO orders (id, total) VALUES (?, ?)", [order_id, total])
    s.commit()
except Exception:
    s.rollback()
    raise
finally:
    s.close()
```

`run_sql()` returns a `ClassicResult` object. Use `fetch_one()` and `fetch_all()` to read rows, `get_column_names()` and `get_columns()` for metadata, `get_affected_items_count()` and `get_auto_increment_value()` after data changes, `get_warnings()` for warnings, and `next_result()` to move to the next result set of a multi-result statement. For the complete list, run `\? ClassicResult`. For more about processing results in Python, see [SQL and Python Modes](../using-mariadb-shell/sql-and-python-modes.md).
