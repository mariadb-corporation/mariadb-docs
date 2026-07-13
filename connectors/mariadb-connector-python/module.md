---
description: >-
  The MariaDB Connector/Python module provides connect, asyncConnect,
  create_pool, and create_async_pool constructors, DB API 2.0 type objects,
  and the exception hierarchy.
---

# The MariaDB Connector/Python module

<a id="module"></a>

<a id="module-mariadb"></a>

MariaDB Connector/Python module enables python programs to access MariaDB and
MySQL databases, using an API which is compliant with the Python DB API 2.0
(PEP-249).

## Constructors

### Connection

### connect(\*args, connectionclass=None, \*\*kwargs)

Creates a MariaDB Connection object.

The first positional argument, when given, is a connection URI string (see
*Since version 2.0* below). By default, the standard Connection class is used.

Parameter connectionclass specifies a subclass of the standard Connection
class. If not specified, the default is used.
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

Connection parameters can also be provided as keyword arguments. The most common ones are:

- **`host`** - Host name or IP address of the database server. Can be a comma-separated list of hosts for simple failover. Default: `'localhost'`
- **`port`** - Port number of the database server. Default: `3306`
- **`user`**, **`username`** - Username for authentication
- **`password`**, **`passwd`** - Password for authentication
- **`database`**, **`db`** - Default database (schema) to select when connecting
- **`unix_socket`** - Path to a Unix socket file for local connections (used in place of TCP)
- **`autocommit`** - Enable autocommit mode. Default: `False`
- **`converter`** - Conversion dictionary mapping `FIELD_TYPE` values to conversion functions

For the full list of accepted parameters — including SSL/TLS options, timeouts, prepared-statement caching, configuration file loading, the result format options (`dictionary`, `named_tuple`, `native_object`), and the parameters that only apply to the C extension — see [The connection class](connection.md).

#### Changed Parameters in Version 2.0

- **`reconnect`** (connection parameter) - Removed. Automatic reconnection is no longer supported; use connection pools or call `conn.reconnect()` manually.
- **`cursor_type`** (cursor option) - Removed in the pure-Python implementation; use `buffered=False` instead. The C extension still accepts it.
- **`prepared`** (cursor option) - Deprecated in favor of `binary=True`. It still works but emits a `DeprecationWarning`.

For migration guidance, see the [Migration Guide](migration-from-1.1-to-2.0.md).

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

### asyncConnect(\*args, connectionclass=None, \*\*kwargs)

*Since version 2.0*

Creates an asynchronous MariaDB Connection object for use with async/await.
As with `connect()`, the first positional argument, when given, is a
connection URI string.

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

**Note:** Connection pooling requires the `mariadb[pool]` package to be installed (the `--pre` flag is required while 2.0 is a Release Candidate):

```console
pip install --pre mariadb[pool]
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

- **\`min_size\`** (`int`) - Minimum number of connections in pool. Default: same as `max_size`
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

Integer constant stating the level of thread safety. In version 2.0 the value
is `3`, meaning threads may share the module, connections, and cursors. In
version 1.1 the value is `1`, meaning threads may share the module but not
connections.

### paramstyle

String constant stating the type of parameter marker. For mariadb the value is
qmark. For compatibility reasons mariadb also supports the format and
pyformat paramstyles with the limitation that they can’t be mixed inside a SQL statement.

### mariadbapi_version

String constant stating the version of the used MariaDB Connector/C library.

### client_version

*Since version 1.1.0*

Returns a version as an integer. In version 2.0 this is the version of MariaDB
Connector/Python itself, in the format:
MAJOR_VERSION \* 10000 + MINOR_VERSION \* 100 + PATCH_VERSION.
In version 1.1 it is the version of the MariaDB Connector/C library in use, in
the format:
MAJOR_VERSION \* 10000 + MINOR_VERSION \* 1000 + PATCH_VERSION.

### client_version_info

*Since version 1.1.0*
Returns a version as a tuple. In version 2.0 this is the version of MariaDB
Connector/Python itself and may include a release-stage suffix
(for example `(2, 0, 0, 'rc2')`). In version 1.1 it is the version of the
MariaDB Connector/C library, in the format:
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
