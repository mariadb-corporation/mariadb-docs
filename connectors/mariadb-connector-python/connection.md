# The connection class

### *class* Connection(\*args, \*\*kwargs)

MariaDB Connector/Python Connection Object

Handles the connection to a MariaDB or MySQL database server.
It encapsulates a database session.

Connections are created using the method mariadb.connect()

## Connection Parameters

The `mariadb.connect()` function accepts the following parameters:

### Basic Connection Parameters

- **`host`** (`str`) - Hostname or IP address of the database server. Can be a comma-separated list for failover support. Default: `'localhost'`
- **`port`** (`int`) - Port number of the database server. Default: `3306`
- **`user`**, **`username`** (`str`) - Username for authentication. Default: `None`
- **`password`**, **`passwd`** (`str`) - Password for authentication. Default: `None`
- **`database`**, **`db`** (`str`) - Database (schema) name to use. Default: `None`
- **`unix_socket`** (`str`) - Path to Unix socket file for local connections. Default: `None`

### Timeout Parameters

- **`connect_timeout`** (`float`) - Timeout in seconds for establishing connection. Default: `10.0`
- **`socket_timeout`** (`float`) - Timeout in seconds for socket operations. Default: `30.0`
- **`read_timeout`** (`float`) - Alias for `socket_timeout`. Default: `30.0`
- **`write_timeout`** (`float`) - Alias for `socket_timeout`. Default: `30.0`
- **`query_timeout`** (`int`) - Maximum query execution time in seconds (0 = no timeout). Default: `0`

### SSL/TLS Parameters

- **`ssl`**, **`use_ssl`** (`bool`) - Enable SSL/TLS encryption. Default: `False`
- **`ssl_ca`** (`str`) - Path to Certificate Authority (CA) certificate file in PEM format. Default: `None`
- **`ssl_cert`** (`str`) - Path to client certificate file in PEM format. Default: `None`
- **`ssl_key`** (`str`) - Path to client private key file in PEM format. Default: `None`
- **`ssl_capath`** (`str`) - Path to directory containing CA certificates in PEM format. Default: `None`
- **`ssl_cipher`** (`str`) - List of permitted cipher suites for SSL/TLS. Default: `None`
- **`ssl_crl`** (`str`) - Path to certificate revocation list file. Default: `None`
- **`ssl_crlpath`** (`str`) - Path to directory containing CRL files. Default: `None`
- **`ssl_verify_cert`** (`bool`) - Enable server certificate verification. Default: `False`
- **`tls_version`** (`str`) - TLS version(s) to use (e.g., 'TLSv1.2', 'TLSv1.3', 'TLSv1.2,TLSv1.3'). Automatically enables SSL. Default: `None`

### Connection Behavior Parameters

- **`autocommit`** (`bool`) - Enable autocommit mode. Default: `False`
- **`read_only`** (`bool`) - Set connection to read-only mode. Default: `False`
- **`compress`** (`bool`) - Enable protocol compression. Default: `False`
- **`local_infile`** (`bool`) - Enable LOAD DATA LOCAL INFILE statements. Default: `None`
- **`init_command`** (`str`) - SQL command to execute when connecting/reconnecting. Default: `None`

### Protocol and Performance Parameters

- **`binary`** (`bool`) - Use binary protocol (prepared statements) by default. Default: `False`
- **`max_allowed_packet`** (`int`) - Maximum packet size in bytes. Default: `16777216` (16MB)
- **`cache_prep_stmts`** (`bool`) - Enable prepared statement caching. Default: `True`
- **`prep_stmt_cache_size`** (`int`) - Maximum number of cached prepared statements. Default: `100`
- **`pipeline`** (`bool`) - Enable pipelining for prepared statements. Default: `True`
- **`client_flag`** (`int`) - Additional client capability flags. Default: `0`

### Character Encoding Parameters

- **`character_encoding`**, **`charset`** (`str`) - Character set to use for the connection. Default: `'utf8mb4'`

### Result Format Parameters

- **`named_tuple`** (`bool`) - Return rows as named tuples instead of regular tuples. Default: `False`
- **`dictionary`** (`bool`) - Return rows as dictionaries instead of tuples. Default: `False`
- **`native_object`** (`bool`) - Return native Python objects for certain types. Default: `False`

### Type Conversion Parameters

- **`converter`** (`dict`) - Custom type converter dictionary mapping field types to conversion functions. Default: `None`

### Connection Examples

**Basic connection with dictionary parameters:**

```python
import mariadb

conn = mariadb.connect(
    host='localhost',
    port=3306,
    user='myuser',
    password='mypassword',
    database='mydb'
)
```

**Connection with SSL/TLS:**

```python
conn = mariadb.connect(
    host='localhost',
    user='myuser',
    password='mypassword',
    database='mydb',
    ssl_ca='/path/to/ca-cert.pem',
    ssl_cert='/path/to/client-cert.pem',
    ssl_key='/path/to/client-key.pem',
    ssl_verify_cert=True
)
```

**Connection with URI (since version 2.0):**

```python
# Basic URI
conn = mariadb.connect("mariadb://myuser:mypassword@localhost:3306/mydb")

# URI with SSL parameters
conn = mariadb.connect(
    "mariadb://myuser:mypassword@localhost/mydb",
    ssl_ca='/path/to/ca-cert.pem',
    ssl_verify_cert=True
)
```

**Connection with timeouts and compression:**

```python
conn = mariadb.connect(
    host='localhost',
    user='myuser',
    password='mypassword',
    database='mydb',
    connect_timeout=5.0,
    socket_timeout=60.0,
    compress=True
)
```

**Connection with result format options:**

```python
# Return rows as dictionaries
conn = mariadb.connect(
    host='localhost',
    user='myuser',
    password='mypassword',
    database='mydb',
    dictionary=True
)

cursor = conn.cursor()
cursor.execute("SELECT id, name FROM users LIMIT 1")
row = cursor.fetchone()
print(row['name'])  # Access by column name
```

**Connection with failover hosts:**

```python
# Multiple hosts for automatic failover
conn = mariadb.connect(
    host='primary.example.com,secondary.example.com,tertiary.example.com',
    port=3306,
    user='myuser',
    password='mypassword',
    database='mydb'
)
```

## Connection constructors

#### Connection.xid(format_id: int, global_transaction_id: str, branch_qualifier: str) -> Xid

Creates a transaction ID object suitable for passing to the .tpc_\*()
methods of this connection.

Parameters:

- format_id: Format id. Default to value 0.
- global_transaction_id: Global transaction qualifier, which must be
  unique. The maximum length of the global transaction id is
  limited to 64 characters.
- branch_qualifier: Branch qualifier which represents a local
  transaction identifier. The maximum length of the branch qualifier
  is limited to 64 characters.

*Since version 1.0.1.*

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Create a transaction ID for distributed transaction
xid = conn.xid(1, "global_tx_12345", "branch_001")
print(f"XID: {xid}")  # Output: (1, 'global_tx_12345', 'branch_001')

conn.close()
```

## Connection methods

#### Connection.begin() -> None

Start a new transaction which can be committed by .commit() method,
or canceled by .rollback() method.

*Since version 1.1.0.*

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Start explicit transaction
conn.begin()

cursor = conn.cursor()
cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Alice", 1000))
cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE name = ?", ("Alice",))

# Commit the transaction
conn.commit()

cursor.close()
conn.close()
```

#### Connection.commit() -> None

Commit any pending transaction to the database.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                   ("John Doe", "john@example.com"))
    cursor.execute("INSERT INTO logs (action) VALUES (?)", 
                   ("User created",))
    
    # Commit both inserts as a single transaction
    conn.commit()
    print("Transaction committed successfully")
except mariadb.Error as e:
    # Rollback on error
    conn.rollback()
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
```

#### Connection.change_user(user: Optional[str], password: Optional[str], database: Optional[str] = None) -> None

Changes the user and default database of the current connection

Parameters:
: - user: user name
  - password: password
  - database: name of default database

In order to successfully change users a valid username and password
parameters must be provided and that user must have sufficient
permissions to access the desired database. If for any reason
authorization fails an exception will be raised and the current user
authentication will remain.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

print(f"Current user: {conn.user}")
print(f"Current database: {conn.database}")

# Switch to a different user and database
try:
    conn.change_user("app_user", "app_pass", "app_db")
    print(f"Changed to user: {conn.user}")
    print(f"Changed to database: {conn.database}")
except mariadb.Error as e:
    print(f"Failed to change user: {e}")
finally:
    conn.close()
```

#### Connection.close() -> None

Close the connection now (rather than whenever ._\_del_\_() is called).

The connection will be unusable from this point forward; an Error
(or subclass) exception will be raised if any operation is attempted
with the connection. The same applies to all cursor objects trying to
use the connection.

Note that closing a connection without committing the changes first
will cause an implicit rollback to be performed.

**Example:**

```python
import mariadb

# Using context manager (recommended - auto-closes)
with mariadb.connect("mariadb://user:password@localhost/mydb") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
# Connection automatically closed here

# Manual close
conn = mariadb.connect("mariadb://user:password@localhost/mydb")
try:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"Total users: {count}")
finally:
    conn.close()  # Always close in finally block
```

#### Connection.cursor(cursor_class: Optional[type] = None, \*\*kwargs: Any) -> Cursor

Create a new cursor for executing queries.

**Parameters:**

- **cursor_class** (`Optional[type]`) - Optional custom cursor class (advanced usage)
- **\*\*kwargs** (`Any`) - Additional cursor parameters:
  - **named_tuple** (`bool`) - Return rows as named tuples
  - **dictionary** (`bool`) - Return rows as dictionaries
  - **buffered** (`bool`) - Buffer all results immediately
  - **binary** (`bool`) - Use binary protocol (prepared statements)

**Returns:**
- `Cursor` object

**Raises:**
- `ProgrammingError` - If connection is closed

By default, fetch methods return result set values as tuples. Use `dictionary=True` or `named_tuple=True` to change the return format.

**Removed in version 2.0:**
- **cursor_type** - Use `buffered=True` for buffered results
- **prepared** - Use `binary=True` instead
- **cursorclass** - No longer supported as a parameter

**Examples:**

```python
# Default cursor (unbuffered, text protocol, returns tuples)
cursor = conn.cursor()

# Buffered cursor (stores entire result set in memory)
cursor = conn.cursor(buffered=True)

# Binary protocol cursor (prepared statements)
cursor = conn.cursor(binary=True)

# Dictionary cursor (access columns by name)
cursor = conn.cursor(dictionary=True)
row = cursor.fetchone()
print(row['column_name'])

# Named tuple cursor (access columns as attributes)
cursor = conn.cursor(named_tuple=True)
row = cursor.fetchone()
print(row.column_name)
```

#### Connection.dump_debug_info() -> None

This function is designed to be executed by a user with the SUPER privilege
and is used to dump server status information into the log for the MariaDB
Server relating to the connection.

*Since version 1.1.2.*

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

try:
    # Dump debug information to server log
    # Requires SUPER privilege
    conn.dump_debug_info()
    print("Debug info dumped to server log")
except mariadb.Error as e:
    print(f"Error: {e}")
    # Output: Error: Access denied; you need (at least one of) the SUPER privilege(s)

conn.close()
```

#### Connection.get_server_version() -> tuple[int, int, int]

Returns a tuple representing the version of the connected server in
the following format: (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)

#### Connection.escape_string(escape_str: str) -> str

Parameters:
statement: string

This function is used to create a legal SQL string that you can use in
an SQL statement. The given string is encoded to an escaped SQL string.

*Since version 1.0.5.*

```python
# connection parameters
conn_params= {
    "user" : "example_user",
    "password" : "GHbe_Su3B8",
    "host" : "localhost"
}

with mariadb.connect(**conn_params) as connection:
    string = 'This string contains the following special characters: \\,"'
    print(connection.escape_string(string))
```

**Output:**

```none
This string contains the following special characters: \\,\"
```

#### Connection.kill(connection_id: int) -> None

This function is used to ask the server to kill a database connection
specified by the connection_id parameter.

The connection id can be retrieved by SHOW PROCESSLIST SQL command.

**Note:** This function requires the SUPER or CONNECTION ADMIN privilege.

**Example:**

```python
import mariadb
import time

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

cursor = conn.cursor()

# Get list of active connections
cursor.execute("SHOW PROCESSLIST")
processes = cursor.fetchall()

print("Active connections:")
for proc in processes:
    conn_id, user, host, db, command, time_val, state, info = proc
    print(f"ID: {conn_id}, User: {user}, DB: {db}, Command: {command}")

# Kill a specific connection (requires SUPER privilege)
target_connection_id = 123
try:
    conn.kill(target_connection_id)
    print(f"Connection {target_connection_id} killed successfully")
except mariadb.Error as e:
    print(f"Error killing connection: {e}")

cursor.close()
conn.close()
```

#### Connection.ping() -> None

Checks if the connection to the database server is still available.

If auto reconnect was set to true, an attempt will be made to reconnect
to the database server in case the connection
was lost

If the connection is not available an InterfaceError will be raised.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

try:
    # Check if connection is alive
    conn.ping()
    print("Connection is alive")
except mariadb.InterfaceError:
    print("Connection lost")
finally:
    conn.close()
```

#### Connection.reconnect() -> None

tries to reconnect to a server in case the connection died due to timeout
or other errors. It uses the same credentials which were specified in
connect() method.

**Example:**

```python
import mariadb
import time

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

try:
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    cursor.close()
    
    # Simulate connection timeout or network issue
    # In real scenario, connection might be lost
    
    # Reconnect with same credentials
    conn.reconnect()
    print("Reconnected successfully")
    
    cursor = conn.cursor()
    cursor.execute("SELECT 2")
    cursor.close()
    
except mariadb.Error as e:
    print(f"Error: {e}")
finally:
    conn.close()
```

#### Connection.reset() -> None

Resets the current connection and clears session state and pending
results. Open cursors will become invalid and cannot be used anymore.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Set some session variables
cursor.execute("SET @my_var = 100")
cursor.execute("SELECT @my_var")
print(cursor.fetchone())  # Output: (100,)

# Reset connection - clears session state
conn.reset()

# Previous cursor is now invalid, create new one
cursor = conn.cursor()
cursor.execute("SELECT @my_var")
print(cursor.fetchone())  # Output: (None,) - variable cleared

cursor.close()
conn.close()
```

#### Connection.rollback() -> None

Causes the database to roll back to the start of any pending
transaction

Closing a connection without committing the changes first will
cause an implicit rollback to be performed.
Note that rollback() will not work as expected if autocommit mode
was set to True or the storage engine does not support transactions.”

#### Connection.select_db(new_db: str) -> None

Gets the default database for the current connection.

The default database can also be obtained or changed by database
attribute.

*Since version 1.1.0.*

**Example:**

```python
import mariadb

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="secret"
)

print(f"Current database: {conn.database}")  # Output: None

# Select a database
conn.select_db("mydb")
print(f"Current database: {conn.database}")  # Output: mydb

cursor = conn.cursor()
cursor.execute("SELECT DATABASE()")
print(cursor.fetchone())  # Output: ('mydb',)

cursor.close()
conn.close()
```

#### Connection.show_warnings() -> Optional[List[tuple]]

Shows error, warning and note messages from last executed command.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Initially no warnings
print(conn.show_warnings())  # Output: None

# Generate a warning by inserting value out of range
cursor.execute("SET session sql_mode=''")
cursor.execute("CREATE TEMPORARY TABLE test_warn (a tinyint)")
cursor.execute("INSERT INTO test_warn VALUES (300)")  # Value too large for tinyint

# Get warnings
warnings = conn.show_warnings()
if warnings:
    for level, code, message in warnings:
        print(f"{level} ({code}): {message}")
    # Output: Warning (1264): Out of range value for column 'a' at row 1

cursor.close()
conn.close()
```

#### Connection.tpc_begin(xid: Xid) -> None

Parameter:
: xid: xid object which was created by .xid() method of connection
  : class

Begins a TPC transaction with the given transaction ID xid.

This method should be called outside a transaction
(i.e., nothing may have been executed since the last .commit()
or .rollback()).
Furthermore, it is an error to call .commit() or .rollback() within
the TPC transaction. A ProgrammingError is raised if the application
calls .commit() or .rollback() during an active TPC transaction.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Create transaction ID
xid = conn.xid(0, "global_tx_001", "branch_001")

# Begin distributed transaction
conn.tpc_begin(xid)

cursor = conn.cursor()
cursor.execute("INSERT INTO orders (product, quantity) VALUES (?, ?)", ("Widget", 10))
cursor.close()

# Single-phase commit (no prepare)
conn.tpc_commit(xid)

conn.close()
```

#### Connection.tpc_commit(xid: Optional[Xid] = None) -> None

Optional parameter:

- xid
  : xid object which was created by .xid() method of connection class.

When called with no arguments, .tpc_commit() commits a TPC transaction
previously prepared with .tpc_prepare().

If .tpc_commit() is called prior to .tpc_prepare(), a single phase
commit is performed. A transaction manager may choose to do this if
only a single resource is participating in the global transaction.
When called with a transaction ID xid, the database commits the given
transaction. If an invalid transaction ID is provided,
a ProgrammingError will be raised.
This form should be called outside a transaction, and
is intended for use in recovery.

**Example (Two-Phase Commit):**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Create transaction ID
xid = conn.xid(0, "global_tx_002", "branch_002")

# Begin distributed transaction
conn.tpc_begin(xid)

cursor = conn.cursor()
cursor.execute("UPDATE inventory SET quantity = quantity - 5 WHERE product = ?", ("Widget",))
cursor.close()

# Prepare transaction (phase 1)
conn.tpc_prepare()

# Commit transaction (phase 2)
conn.tpc_commit()

conn.close()
```

#### Connection.tpc_prepare() -> None

Performs the first phase of a transaction started with .tpc_begin().
A ProgrammingError will be raised if this method was called outside
a TPC transaction.

After calling .tpc_prepare(), no statements can be executed until
.tpc_commit() or .tpc_rollback() have been called.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

xid = conn.xid(0, "global_tx_003", "branch_003")
conn.tpc_begin(xid)

cursor = conn.cursor()
cursor.execute("INSERT INTO transactions (amount) VALUES (?)", (100.00,))
cursor.close()

# Prepare the transaction (phase 1 of 2PC)
conn.tpc_prepare()

# At this point, transaction is prepared but not committed
# Can now commit or rollback
conn.tpc_commit()

conn.close()
```

#### Connection.tpc_recover() -> List[tuple]

Returns a list of pending transaction IDs suitable for use with
tpc_commit(xid) or .tpc_rollback(xid).

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Get list of pending prepared transactions
pending_xids = conn.tpc_recover()

if pending_xids:
    print(f"Found {len(pending_xids)} pending transactions")
    for xid_data in pending_xids:
        print(f"Pending XID: {xid_data}")
        # Can commit or rollback these transactions
        # xid = conn.xid(*xid_data)
        # conn.tpc_commit(xid)
else:
    print("No pending transactions")

conn.close()
```

#### Connection.tpc_rollback(xid: Optional[Xid] = None) -> None

Parameter:
: xid: xid object which was created by .xid() method of connection
  : class

Performs the first phase of a transaction started with .tpc_begin().
A ProgrammingError will be raised if this method outside a TPC
transaction.

After calling .tpc_prepare(), no statements can be executed until
.tpc_commit() or .tpc_rollback() have been called.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

xid = conn.xid(0, "global_tx_004", "branch_004")
conn.tpc_begin(xid)

cursor = conn.cursor()
try:
    cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE id = ?", (1,))
    cursor.execute("UPDATE accounts SET balance = balance + 1000 WHERE id = ?", (2,))
    
    # Check for errors
    cursor.execute("SELECT balance FROM accounts WHERE id = 1")
    balance = cursor.fetchone()[0]
    
    if balance < 0:
        # Rollback the distributed transaction
        conn.tpc_rollback()
        print("Transaction rolled back - insufficient funds")
    else:
        conn.tpc_prepare()
        conn.tpc_commit()
        print("Transaction committed")
        
except mariadb.Error as e:
    conn.tpc_rollback()
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
```

## Connection attributes

#### Connection.auto_reconnect: bool

*removed in version 2.0*

(read/write)

Enable or disable automatic reconnection to the server if the connection
is found to have been lost.

When enabled, client tries to reconnect to a database server in case
the connection to a database server died due to timeout or other errors.

#### Connection.autocommit: bool

(read/write)

Toggles autocommit mode on or off for the current database connection.

Autocommit mode only affects operations on transactional table types.
Be aware that rollback() will not work if autocommit mode was switched
on.

By default, autocommit mode is set to False.

#### Connection.character_set: str

(read-only)

Client character set.

For MariaDB Connector/Python, it is always utf8mb4.

#### Connection.client_capabilities: int

(read-only)

Client capability flags.

*Since version 1.1.0.*

#### Connection.collation: str

(read-only)

Client character set collation

#### Connection.connection_id: int

(read-only)

Id of current connection

#### Connection.database: Optional[str]

(read-only)

Returns or sets the default database for the current connection.

The default database can also be obtained or changed by database
attribute.

*Since version 1.1.0.*

#### Connection.open: bool

(read-only)

Returns true if the connection is alive.

A ping command will be sent to the server for this purpose,
which means this function might fail if there are still
non-processed pending result sets.

*Since version 1.1.0.*

#### Connection.server_capabilities: int

(read-only)

Server capability flags.

*Since version 1.1.0.*

#### Connection.extended_server_capabilities: int

(read-only)

Extended server capability flags (only for MariaDB
database servers).

*Since version 1.1.0.*

#### Connection.server_info: str

(read-only)

Server version in alphanumerical format (str)

#### Connection.server_mariadb: bool

(read-only)

Returns `True` if the connected server is MariaDB, `False` if it's MySQL.

This property is useful for detecting server type and implementing server-specific logic.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

if conn.server_mariadb:
    print("Connected to MariaDB server")
    print(f"Version: {conn.server_info}")
    # Use MariaDB-specific features
    cursor = conn.cursor()
    cursor.execute("SELECT JSON_DETAILED('{\"a\": 1}')")
else:
    print("Connected to MySQL server")
    print(f"Version: {conn.server_info}")
    # Use MySQL-compatible features only

conn.close()
```

#### Connection.server_name: Optional[str]

(read-only)

Returns the server name.

#### Connection.server_port: int

(read-only)

Database server TCP/IP port. This value will be 0 in case of an unix
socket connection.

#### Connection.server_status: int

(read-only)

Return server status flags

*Since version 1.1.0.*

#### Connection.server_version: int

(read-only)

Returns an integer representing the server version.

The form of the version number is
VERSION_MAJOR \* 10000 + VERSION_MINOR \* 100 + VERSION_PATCH

#### Connection.server_version_info: tuple

(read-only)

Returns numeric version of connected database server in tuple format.

#### Connection.tls_cipher: Optional[str]

(read-only)

Returns the TLS cipher suite in use.

*Since version 1.0.5.*

#### Connection.tls_version: Optional[str]

(read-only)

Returns the TLS protocol version.

#### Connection.tls_peer_cert_info: Optional[dict]

(read-only)

Returns peer certificate information for TLS connections.

*Since version 1.1.11.*

#### Connection.unix_socket: Optional[str]

(read-only)

Returns the unix socket file name.

#### Connection.user: Optional[str]

(read-only)

Returns the username for the current connection or empty
string if it can’t be determined, e.g., when using socket
authentication.

#### Connection.warnings: int

(read-only)

Returns the number of warnings from the last executed statement., or zero
if there are no warnings.

{% @marketo/form formId="4316" %}
