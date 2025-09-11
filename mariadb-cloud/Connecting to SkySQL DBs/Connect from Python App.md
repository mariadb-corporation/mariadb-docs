# Connect from Python App

## Overview

Python developers can use MariaDB Connector/Python to establish client connections with SkySQL.

## Connections

Connections are managed using the following Python class:

| Class | Description |
| --- | --- |
| Connection | Represents a connection to SkySQL. |

Connections are created, used, and managed using the following `Connection` class functions:

| Function | Description |
| --- | --- |
| connect() | Establishes a connection to a database server and returns a connection object. |
| cursor() | Returns a new cursor object for the current connection. |
| change_user() | Changes the user and default database of the current connection. |
| reconnect() | Tries to make a connection object active again by reconnecting to the server using the same credentials which were specified in connect() method. |
| close() | Closes the connection. |

Determine the connection information for your SkySQL database service:

| connect() parameter | Where to find it |
| --- | --- |
| user | Default username in the Service Credentials view, or the username you created |
| passwd | Default password in the Service Credentials view, the password you set on the default user, or the password for the user you created |
| host | Fully Qualified Domain Name in the Connection Parameters Portal |
| ssl_verify_cert | Set to True to support SSL |
| port | Read-Write Port or Read-Only Port in the Connection Parameters Portal |

## Code Example: Connect

The following code example connects to an example server.

Examples:

```python
# Module Import
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      host="192.0.2.1",
      port=3306,
      user="db_user",
      password="USER_PASSWORD")
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
   sys.exit(1)

# Use Connection
# ...

# Close Connection
conn.close()
```

```python
# Module Import
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      host="SKYSQL_SERVICE.mdb0000001.db.skysql.com",
      port=5009,
      ssl_verify_cert=True,
      user="DB00000001",
      password="USER_PASSWORD")
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
   sys.exit(1)

# Use Connection
# ...

# Close Connection
conn.close()
```

- The `connect()` function returns an instance of the `Connection` class, which is assigned to the `conn` variable.
- The connection attributes are passed as keyword arguments to the`connect()`function.
- When you are done with a connection, close it to free resources. Close the connection using the `close()`method.

## Multiple Connections

Instantiating the `Connection` class creates a single connection to MariaDB database products. Applications that require multiple connections may benefit from pooling connections.

## Close a Connection

MariaDB Connector/Python closes the connection as part of the class's destructor, which is executed when an instance of the class goes out of scope. This can happen in many cases, such as:

- When the program exits
- When the instance of the `Connection` class is defined in the local scope of a function, and the function returns
- When the instance of the `Connection` class is defined as an attribute of a custom class's instance, and the custom class's instance goes out of scope.

Connections can also be explicitly closed using the `close()` method, which is helpful when the connection is no longer needed, but the variable is still in scope.

## Connection Failover

Starting with MariaDB Connector/Python 1.1 when MariaDB Connector/Python is built with MariaDB Connector/C 3.3, the connector supports connection failover when `auto_reconnect` is
enabled and the connection string contains a comma-separated list of multiple server addresses.

To enable connection failover:

- Call the `mariadb.connect` function with the `host` argument specified as a comma-separated list containing multiple server addresses. The connector attempts to connect to the addresses in the order specified in the list.
- Set `auto_reconnect` to `True`. If the connection fails, the connector will attempt to reconnect to the addresses in the order specified in the list.

The following code example connects with connection failover enabled:

```python
# Module Import
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      host="192.0.2.1,192.0.2.0,198.51.100.0",
      port=3306,
      user="db_user",
      password="USER_PASSWORD")
   conn.auto_reconnect = True
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
   sys.exit(1)

# Use Connection
# ...

# Close Connection
conn.close()
```

```python
# Module Import
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      host="SKYSQL_SERVICE.mdb0000001.db.skysql.com,SKYSQL_SERVICE.mdb0000002.db.skysql.com",
      port=5009,
      ssl_verify_cert=True,
      user="DB00000001",
      password="USER_PASSWORD")
   conn.auto_reconnect = True
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
   sys.exit(1)

# Use Connection
# ...

# Close Connection
conn.close()
```
