---
description: >-
  Use the GridGain 9 Python Database API driver to connect to a cluster,
  configure SSL and authentication, run queries, and manage transactions.
---

# Python Database API Driver

GridGain 9 clients connect to the cluster via a standard socket connection. Clients do not become a part of the cluster topology, never hold any data, and are not used as a destination for compute calculations.

GridGain DB API driver uses the [Python Database API](https://peps.python.org/pep-0249/).

## Getting Started

### Prerequisites

To run the Python driver, the following is required:

- CMake 3.18 or newer to build the driver
- Python 3.10 or newer (3.10, 3.11, 3.12, 3.13 and 3.14 are tested)
- Access to a running Ignite 3 or GridGain 9 node

### Limitations

Script execution of SQL statements is not supported in current release.

### Installation

To install Python DB API driver, download it from pip.

```bash
pip install pygridgain_dbapi
```

After this, you can import `pygridgain_dbapi` into your project and use it.

## Connecting to Cluster

To connect to the cluster, use the `connect()` method:

```python
addr = ['127.0.0.1:10800']
return pygridgain_dbapi.connect(address=addr, timeout=10)
```

### Connection Parameters

The `connect()` function accepts the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| address | str or list[str] | **Required.** Cluster node address(es) for initial connection and fail-over. Examples: `'localhost:10800'` or `['host1:10800', 'host2:10800']` |
| identity | str | Username for authentication. Used with `secret` for basic authentication. |
| secret | str | Password for authentication. Used with `identity` for basic authentication. |
| schema | str | Default schema name. Default: `'PUBLIC'` |
| timezone | str | Client timezone for date/time operations. Default: server timezone |
| page_size | int | Maximum rows per request. Default: `1024` |
| timeout | int | Network operation timeout in seconds. Default: `30` |
| heartbeat_interval | float | Heartbeat interval in seconds. Set to 0 to disable. Default: `1.0` |
| autocommit | bool | Enable automatic transaction commit. Default: `True` |
| use_ssl | bool | Enable SSL/TLS encryption. Default: `False` |
| ssl_keyfile | str | Path to SSL key file. Required if `use_ssl=True` and using client authentication. |
| ssl_certfile | str | Path to SSL certificate file. Required if `use_ssl=True` and using client authentication. |
| ssl_ca_certfile | str | Path to CA certificate for server validation. Required if `use_ssl=True`. |

After you are done working with the cluster, remember to always close the connection to it.

```python
conn.close()
```

Alternatively, you can use the `with` statement to automatically close the connection when no longer necessary:

```python
with pygridgain_dbapi.connect(address=addr, timeout=10) as conn:
  conn.cursor()
```

### Configuring SSL for Connection

To ensure secure connection to the cluster, you can enable SSL for it by providing the key file and certificate, for example:

```python
def create_ssl_connection():
  """Create SSL-enabled connection to GridGain cluster."""
  addr = ['127.0.0.1:10800']
  return pygridgain_dbapi.connect(
      address=addr,
      timeout=10,
      use_ssl=True,
      ssl_keyfile='<path_to_ssl_keyfile.pem>',
      ssl_certfile='<path_to_ssl_certfile.pem>',
      # Optional: ssl_ca_certfile='<path_to_ssl_ca_certfile.pem>'
  )
```

{% hint style="info" %}
All paths to certificate file and keys should be provided in string format appropriate for the system.
{% endhint %}

### Configuring Authorization

If the cluster uses [basic authorization](../../administrators-guide/security/authentication.md#basic-authentication), you need to provide user `identity` and `secret` to authorize on it, for example:

```python
def create_authenticated_connection():
  """Create authenticated connection to GridGain cluster."""
  addr = ['127.0.0.1:10800']
  return pygridgain_dbapi.connect(
      address=addr,
      timeout=10,
      identity='user',
      secret='password'
  )
```

### Configuring Data Access

You can configure optional properties to fine-tune how data is accessed and how the connection behaves.

| Configuration name | Default | Description |
| --- | --- | --- |
| schema | 'PUBLIC' | A schema name to be used by default. |
| page_size | 1024 | Maximum number of rows that can be received or sent in a single request. |
| timeout | 30 | Timeout for network operations, in seconds. |
| heartbeat_interval | 1.0 | Interval between heartbeat probes, in seconds. Set to 0 or negative to disable heartbeats. See [Connection Heartbeats](#connection-heartbeats) for details. |
| timezone | (server) | Client's timezone. Required to correctly work with date/time values. By default, server's timezone is used. |

The example below shows how to set these properties:

```python
def create_configured_connection():
  """Create authenticated connection to GridGain cluster."""
  addr = ['127.0.0.1:10800']
  return conn = pygridgain_dbapi.connect(
    address=addr,
    timeout=10,
    schema='CUSTOM',
    page_size=2048
  )
```

{% hint style="info" %}
You can also configure `timeout` and `heartbeat_interval` parameters. See Connection Parameters Reference for the full list of available parameters.
{% endhint %}

### Connection Heartbeats

The Python DB API driver supports connection heartbeats to prevent the server from closing idle connections. When enabled, the driver automatically sends periodic heartbeat messages to the server during periods of inactivity.

The driver tracks when the last message was sent to the server. If the connection is idle for longer than the `heartbeat_interval`, a heartbeat message is sent. If other queries or operations are executed, no heartbeat is needed. Heartbeats keep the connection alive without requiring application changes.

By default, heartbeats are sent every 1 second. You can customize the heartbeat interval or disable it by setting the interval to 0:

```python
# Custom heartbeat interval (10 seconds)
conn = pyignite_dbapi.connect(
    address='localhost:10800',
    heartbeat_interval=10.0
)

# Disable heartbeats
conn = pyignite_dbapi.connect(
    address='localhost:10800',
    heartbeat_interval=0
)
```

{% hint style="warning" %}
Disabling heartbeats may cause the server to close idle connections after its configured idle timeout period. Only disable heartbeats if you ensure continuous activity or can handle reconnection
{% endhint %}

## Getting Cursor Object

To work with tables from Python client, you use the `cursor` object that can be retrieved from the connection object:

```python
conn.cursor()
```

Similar to the connection, you can use the `with` statement when getting the cursor:

```python
with conn.cursor() as cursor:
```

## Executing Single Query

The cursor object can be used to execute SQL statements with the `execute` command:

```python
# Create table
cursor.execute('''
          CREATE TABLE Person(
              id INT PRIMARY KEY,
              name VARCHAR,
              age INT
          )
      ''')
```

## Executing a Batched Query

You can use the `executemany` command to execute SQL queries with a batch of parameters. This kind of operation offers much higher performance than executing individual queries. The example below inserts two rows into the Person table:

```python
# Sample data
sample_data = [
  [1, "John", 30],
  [2, "Jane", 32],
  [3, "Bob", 28]
]

# Insert data (fixed table name)
cursor.executemany('INSERT INTO Person VALUES(?, ?, ?)', sample_data)
```

## Getting Query Results

The cursor retains a reference to the operation. If the operation returns results (for example, a `SELECT`), they will also be stored in the cursor. You can then use the `fetchone()` method to retrieve query results from the cursor:

```python
# Query data
cursor.execute('SELECT * FROM Person ORDER BY id')
results = cursor.fetchall()

print("All persons in database:")
for row in results:
  print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
```

## Working with Transactions

By default, transactions required for database operations are handled implicitly. However, you can disable automatic transaction handling and manually handle commits.

To do this, first, disable autocommit:

```python
conn.autocommit = False
```

Once autocommit is disabled, you need to commit your operations manually:

```python
# Insert valid records
cursor.execute('INSERT INTO Person VALUES(?, ?, ?)', [4, "Alice", 29])
cursor.execute('INSERT INTO Person VALUES(?, ?, ?)', [5, "Charlie", 31])

cursor.execute('INSERT INTO Person VALUES(?, ?, ?)', [6, "Invalid", new_age])

conn.commit()
print("Transaction committed successfully")
```

Operations that are not committed are sent to the cluster, but not yet written to the table. The table is only updated when the `commit` method is called. You can roll back all uncommitted operations with the `rollback` command:

```python
with conn.cursor() as cursor:
  try:
    # Insert valid records
    cursor.execute('INSERT INTO Person VALUES(?, ?, ?)', [4, "Alice", 29])
    cursor.execute('INSERT INTO Person VALUES(?, ?, ?)', [5, "Charlie", 31])

    cursor.execute('INSERT INTO Person VALUES(?, ?, ?)', [6, "Invalid", new_age])

    conn.commit()
    print("Transaction committed successfully")

  except Exception as e:
    # Rollback on any error
    conn.rollback()
    print(f"Transaction rolled back due to error: {e}")
```

{% hint style="info" %}
The `rollback` command rolls back all uncommitted data.
{% endhint %}
</content>
