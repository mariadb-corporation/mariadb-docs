# The MariaDB Connector/Python module

<a id="module"></a>

<a id="module-mariadb"></a>

MariaDB Connector/Python module enables python programs to access MariaDB and
MySQL databases, using an API which is compliant with the Python DB API 2.0
(PEP-249).

## Constructors

### Connection

### connect(dsn=None, connectionclass=mariadb.connections.Connection, \*\*kwargs)

Creates a MariaDB Connection object.

By default, the standard connectionclass mariadb.connections.Connection
will be created.

Parameter connectionclass specifies a subclass of
mariadb.Connection object. If not specified, default will be used.
This optional parameter was added in version 1.1.0.

*Since version 2.0:* Connection can be established using a URI string or keyword arguments. Keyword arguments override URI values when both are provided.

**URI Connection (recommended):**

```python
import mariadb

# Simple URI
conn = mariadb.connect("mariadb://user:password@localhost:3306/mydb")

# URI with query parameters
conn = mariadb.connect("mariadb://user:password@localhost/mydb?autocommit=true&binary=true")

# Keyword arguments override URI values
conn = mariadb.connect("mariadb://user:password@localhost/mydb", database="otherdb")
```

**Keyword Arguments:**

Connection parameters can also be provided as keyword arguments:

- **\`host\`** - The host name or IP address of the database server. If MariaDB Connector/Python was built with MariaDB Connector/C 3.3, it is also possible to provide a comma separated list of hosts for simple fail over in case of one or more hosts are not available.
- **\`user\`, \`username\`** - The username used to authenticate with the database server
- **\`password\`, \`passwd\`** - The password of the given user
- **\`database\`, \`db\`** - Database (schema) name to use when connecting with the database server
- **\`unix_socket\`** - The location of the unix socket file to use instead of using an IP port to connect. If socket authentication is enabled, this can also be used in place of a password.
- **\`port\`** - Port number of the database server. If not specified, the default value of 3306 will be used.
- **\`connect_timeout\`** - Connect timeout in seconds
- **\`read_timeout\`** - Read timeout in seconds
- **\`write_timeout\`** - Write timeout in seconds
- **\`local_infile\`** - Enables or disables the use of LOAD DATA LOCAL INFILE statements.
- **\`compress\`** (default: False) - Uses the compressed protocol for client server communication. If the server doesn’t support compressed protocol, the default protocol will be used.
- **\`init_command\`** - Command(s) which will be executed when connecting and reconnecting to the database server
- **\`default_file\`** - Read options from the specified option file. If the file is an empty string, default configuration file(s) will be used
- **\`default_group\`** - Read options from the specified group
- **\`plugin_dir\`** - Directory which contains MariaDB client plugins (C extension only, not available in pure Python)
- **\`binary\`** (default: False) - *Since version 2.0* - When enabled at connection level, all cursors default to binary protocol (prepared statements). Can be overridden per cursor.
- **\`cache_prep_stmts\`** (default: True) - *Since version 2.0* - Enables or disables prepared statement caching. When enabled, prepared statements are reused across executions.
- **\`prep_stmt_cache_size\`** (default: 100) - *Since version 2.0* - Maximum number of cached prepared statements per connection. When the cache is full, the least recently used statement is evicted.
- **\`pipeline\`** (default: False) - *Since version 2.0* - Enables pipelining for batch operations
- **\`ssl_key\`** - Defines a path to a private key file to use for TLS. This option requires that you use the absolute path, not a relative path. The specified key must be in PEM format
- **\`ssl_cert\`** - Defines a path to the X509 certificate file to use for TLS. This option requires that you use the absolute path, not a relative path. The X609 certificate must be in PEM format.
- **\`ssl_ca\`** - Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for TLS. This option requires that you use the absolute path, not a relative path.
- **\`ssl_capath\`** - Defines a path to a directory that contains one or more PEM files that contains one X509 certificate for a trusted Certificate Authority (CA)
- **\`ssl_cipher\`** - Defines a list of permitted cipher suites to use for TLS
- **\`ssl_crlpath\`** - Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for TLS. This option requires that you use the absolute path, not a relative path.
- **\`ssl_verify_cert\`** - Enables server certificate verification.
- **\`ssl\`** - The connection must use TLS security, or it will fail.
- **\`tls_version\`** - A comma-separated list (without whitespaces) of TLS versions. Valid versions are TLSv1.0, TLSv1.1,TLSv1.2 and TLSv1.3. Added in version 1.1.7.
- **\`autocommit\`** (default: False) - Specifies the autocommit settings. True will enable autocommit, False will disable it (default).
- **\`converter\`** - Specifies a conversion dictionary, where keys are FIELD_TYPE values and values are conversion functions

#### Removed Parameters in Version 2.0

The following parameters have been removed:

- **\`reconnect\`** / **\`auto_reconnect\`** - Automatic reconnection is no longer supported. Use connection pools or call `conn.reconnect()` manually.
- **\`cursor_type\`** - Replaced by `buffered=False` parameter in cursor creation.
- **\`prepared\`** - Replaced by `binary=True` parameter.

For migration guidance, see the [Migration Guide](migration-from-1.1-to-2.0.md).

#### NOTE
For a description of configuration file handling and settings please read the chapter [Configuration files](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/config_files#configuration-options) of the MariaDB Connector/C documentation.

**Examples:**

```python
import mariadb

# URI connection (recommended)
with mariadb.connect("mariadb://example_user:GHbe_Su3B8@localhost/test") as connection:
    print(connection.character_set)

# Keyword arguments (still supported)
with mariadb.connect(user="example_user", host="localhost", database="test", password="GHbe_Su3B8") as connection:
    print(connection.character_set)

# Binary protocol enabled at connection level
with mariadb.connect("mariadb://localhost/test?binary=true") as connection:
    cursor = connection.cursor()  # Uses binary protocol by default
    cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
```

Output:

```none
utf8mb4
```

### Async Connection

### asyncConnect(dsn=None, \*\*kwargs)

*Since version 2.0*

Creates an asynchronous MariaDB Connection object for use with async/await.

**Usage:**

```python
import asyncio
import mariadb

async def main():
    # URI connection
    conn = await mariadb.asyncConnect("mariadb://user:password@localhost/mydb")
    
    # Or with keyword arguments
    conn = await mariadb.asyncConnect(
        host="localhost",
        user="user",
        password="password",
        database="mydb"
    )
    
    cursor = await conn.cursor()
    await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
    row = await cursor.fetchone()
    
    await cursor.close()
    await conn.close()

asyncio.run(main())
```

For detailed async usage, see [Async/Await Support](async-usage.md).

### Connection Pool

### create_pool(\*\*kwargs)

*Since version 2.0*

Creates a synchronous connection pool.

**Note:** Connection pooling requires the `mariadb[pool]` package to be installed:

```console
pip install mariadb[pool]
```

**Usage:**

```python
import mariadb

pool = mariadb.create_pool(
    host="localhost",
    user="user",
    password="password",
    database="mydb",
    min_size=5,
    max_size=20
)

with pool.acquire() as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1")
```

Keyword Arguments:

- **\`min_size\`** (`int`) - Minimum number of connections in pool. Default: 5
- **\`max_size\`** (`int`) - Maximum number of connections in pool. Default: 10
- **\`ping_threshold\`** (`float`) - Ping connections idle for more than this many seconds. Default: 0.25
- **\*\*kwargs** - Connection arguments as described in mariadb.connect() method

For detailed pooling documentation, see [Connection Pooling](pooling.md).

### create_async_pool(\*\*kwargs)

*Since version 2.0*

Creates an asynchronous connection pool for use with async/await.

**Note:** Requires `mariadb[pool]` package.

**Usage:**

```python
import asyncio
import mariadb

async def main():
    pool = await mariadb.create_async_pool(
        host="localhost",
        user="user",
        password="password",
        database="mydb",
        min_size=10,
        max_size=50
    )
    
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT 1")
    
    await pool.close()

asyncio.run(main())
```

For detailed async pooling, see [Async/Await Support](async-usage.md).

### Type constructors

### Binary()

Constructs an object capable of holding a binary value.

### Date(year, month, day)

Constructs an object holding a date value.

### DateFromTicks(ticks)

Constructs an object holding a date value from the given ticks value
(number of seconds since the epoch).
For more information see the documentation of the standard Python
time module.

### Time(hour, minute, second)

Constructs an object holding a time value.

### TimeFromTicks(ticks)

Constructs an object holding a time value from the given ticks value
(number of seconds since the epoch).
For more information see the documentation of the standard Python
time module.

### Timestamp(year, month, day, hour, minute, second)

Constructs an object holding a datetime value.

### TimestampFromTicks(ticks)

Constructs an object holding a datetime value from the given ticks value
(number of seconds since the epoch).
For more information see the documentation of the standard Python
time module.

## Attributes

### apilevel

String constant stating the supported DB API level. The value for mariadb is
`2.0`.

### threadsafety

Integer constant stating the level of thread safety. For mariadb the value is 1,
which means threads can share the module but not the connection.

### paramstyle

String constant stating the type of parameter marker. For mariadb the value is
qmark. For compatibility reasons mariadb also supports the format and
pyformat paramstyles with the limitation that they can’t be mixed inside a SQL statement.

### mariadbapi_version

String constant stating the version of the used MariaDB Connector/C library.

### client_version

*Since version 1.1.0*

Returns the version of MariaDB Connector/C library in use as an integer.
The number has the following format:
MAJOR_VERSION \* 10000 + MINOR_VERSION \* 1000 + PATCH_VERSION

### client_version_info

*Since version 1.1.0*
Returns the version of MariaDB Connector/C library as a tuple in the
following format:
(MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)

## Exceptions

Compliant to DB API 2.0 MariaDB Connector/C provides information about errors
through the following exceptions:

### *exception* DataError

Exception raised for errors that are due to problems with the processed data like division by zero, numeric value out of range, etc.

### *exception* DatabaseError

Exception raised for errors that are related to the database

### *exception* InterfaceError

Exception raised for errors that are related to the database interface rather than the database itself

### *exception* Warning

Exception raised for important warnings like data truncations while inserting, etc

### *exception* PoolError

Exception raised for errors related to ConnectionPool class.

### *exception* OperationalError

Exception raised for errors that are related to the database’s operation and not necessarily under the control of the programmer.

### *exception* IntegrityError

Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails

### *exception* InternalError

Exception raised when the database encounters an internal error, e.g. the cursor is not valid anymore

### *exception* ProgrammingError

Exception raised for programming errors, e.g. table not found or already exists, syntax error in the SQL statement

### *exception* NotSupportedError

Exception raised in case a method or database API was used which is not supported by the database

### Type objects

<!-- _Note: Type objects are handled as constants, therefore we can't
use autodata. -->

MariaDB Connector/Python type objects are immutable sets for type settings
and defined in DBAPI 2.0 (PEP-249).

Example:

```python
import mariadb
from mariadb.constants import FIELD_TYPE

print(FIELD_TYPE.GEOMETRY == mariadb.BINARY)
print(FIELD_TYPE.DATE == mariadb.DATE)
print(FIELD_TYPE.VARCHAR == mariadb.BINARY)
```

Output:

```none
True
True
False
```

### STRING

This type object is used to describe columns in a database that are
string-based (e.g. CHAR1).

### BINARY

This type object is used to describe (long) binary columns in a database
(e.g. LONG, RAW, BLOBs).

### NUMBER

This type object is used to describe numeric columns in a database.

### DATETIME

This type object is used to describe date/time columns in a database.

### ROWID

This type object is not supported in MariaDB Connector/Python and represents
an empty set.

{% @marketo/form formId="4316" %}
