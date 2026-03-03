<a id="faq"></a>

# MariaDB Connector/Python FAQ

This is a list of frequently asked questions about MariaDB Connector/Python. Feel free to suggest new
entries!

## API Reference

- **[Connection API](connection.md)** - Connection parameters, methods, and attributes
- **[Cursor API](cursor.md)** - Cursor parameters, methods, and attributes  
- **[Connection Pooling API](pooling.md)** - Pool configuration and usage

<a id="installation-faq"></a>

## Installation

### Error: “Python.h: No such file or directory”

The header files and libraries of the Python development package weren’t properly installed.
Use your package manager to install them system-wide:

**Alpine (using apk):**

```console
sudo apk add python3-dev
```

**Ubuntu/Debian (using apt):**

```console
sudo apt-get install python3-dev
```

**CentOS/RHEL (using yum):**

```console
sudo yum install python3-devel
```

**Fedora (using dnf):**

```console
sudo dnf install python3-devel
```

**MacOSX (using homebrew):**

```console
brew install mariadb-connector-c
```

**OpenSuse (using zypper):**

```console
sudo zypper in python3-devel
```

Note: The python3 development packages of your distribution might not cover all minor versions
of python3. If you are using python3.10 you may need to install python3.10-dev.

### Which installation option should I choose for version 2.0?

**Version 2.0** offers three installation options:

1. **Pure Python (default)** - `pip install mariadb`
   - Works everywhere, no compiler required
   - Good performance for most use cases
   - Recommended for development and testing

2. **Pre-compiled binary wheels** - `pip install mariadb[binary]`
   - Best for production
   - **MariaDB Connector/C is bundled** - no separate installation needed
   - Maximum performance without compilation
   - No compiler required

3. **C extension from source** - `pip install mariadb[c]`
   - **Requires MariaDB Connector/C 3.3.1+ to be pre-installed** on your system
   - Maximum performance
   - Requires C compiler for building
   - For custom builds or platforms without binary wheels

**For connection pooling**, add `[pool]` to any option:
```console
pip install mariadb[binary,pool]
```

### Do I need MariaDB Connector/C for version 2.0?

**No, not anymore!** This is a major change in version 2.0:

- **Pure Python** (default): No MariaDB Connector/C required
- **Binary wheels** (`mariadb[binary]`): No separate installation needed - MariaDB Connector/C is bundled inside the wheel
- **C extension from source** (`mariadb[c]`): Yes, requires MariaDB Connector/C 3.3.1+ to be pre-installed on your system

For most users, `pip install mariadb[binary,pool]` provides the best experience with no external dependencies.

### ModuleNotFoundError: No module named ‘packaging’

With deprecation of distutils (see [PEP-632](https://peps.python.org/pep-632)) version functions of distutils module were
replaced in MariaDB Connector/Python 1.1.5 by packaging version functions.

Before you can install MariaDB Connector/Python you have to install the packaging module:

```console
pip3 install packaging
```

### MariaDB Connector/Python requires MariaDB Connector/C >= 3.3.1, found version 3.1.2

The previously installed version of MariaDB Connector/C is too old and cannot be used for the MariaDB Connector/Python version
you are trying to install.

To determine the installed version of MariaDB Connector/C, execute the command:

```console
mariadb_config --cc_version
```

- Check if your distribution can be upgraded to a more recent version of MariaDB Connector/C, which fits the requirements.
- If your distribution doesn’t provide a recent version of MariaDB Connector/C, check the [MariaDB Connector Download page](https://mariadb.com/downloads/connectors/), which provides
  latest versions for the major distributions.
- If none of the above will work for you, build and install MariaDB Connector/C from source.

### OSError: mariadb_config not found

The mariadb_config program is used to retrieve configuration information (such as the location of
header files and libraries, installed version, etc.) from MariaDB Connector/C.

This error indicates that MariaDB Connector/C, an important dependency for client/server communication that needs
to be preinstalled, either was not installed or could not be found.

* If MariaDB Connector/C was previously installed, the installation script cannot detect the location of mariadb_config.
  Locate the directory where mariadb_config was installed and add this directory to your PATH.
  ```console
  # locate mariadb_config
  sudo find / -name "mariadb_config"
  ```
* If MariaDB Connector/C was not installed and the location of mariadb_config couldn’t be detected, please install
  MariaDB Connector/C.

### Error: struct st_mariadb_methods’ has no member named ‘db_execute_generate_request’

Even if the correct version of MariaDB Connector/C was installed, there are multiple mysql.h include files installed
on your system, either from libmysql or an older MariaDB Connector/C installation. This can be checked by executing:

```console
export CFLAGS="-V -E"
pip3 install mariadb > output.txt
```

Open output.txt in your favourite editor and search for “search starts here” where you can see the include
files and paths used for the build.

### Q: My distribution doesn’t provide a recent version of MariaDB Connector/C

If your distribution doesn’t provide a recent version of MariaDB Connector/C (required version is 3.3.1) you either
can download a version of MariaDB Connector/C from the [MariaDB Connector Download page](https://mariadb.com/downloads/connectors/) or build the package from source:

```console
mkdir bld
cd bld
cmake ..
make
make install
```

### Q: Does MariaDB Connector/Python provide pre-releases or snapshot builds which contain recent bug fixes?

No. If an issue was fixed, the fix will be available in the next release via Python’s package
manager repository (pypi.org).

### Q: How can I build an actual version from github sources?

To build MariaDB Connector/Python from github sources, checkout latest sources from github:

```console
git clone https://github.com/mariadb-corporation/mariadb-connector-python.git
```

and build and install it with:

```console
python3 setup.py build
python3 -m pip install .
```

## Connecting

### mariadb.OperationalError: Can’t connect to local server through socket ‘/tmp/mysql.sock’

1. Check if MariaDB server has been started.
2. Check if the MariaDB server was correctly configured and uses the right socket file:
   ```console
   mysqld --help --verbose | grep socket
   ```

   If the socket is different and cannot be changed, you can specify the socket in your
   connection parameters.
   ```python
   connection = mariadb.connect(unix_socket="/path_socket/mysql.sock", ....)
   ```

   Another option is setting the environment variable MYSQL_UNIX_PORT.
   ```console
   export MYSQL_UNIX_PORT=/path_to/mysql.sock
   ```

### How do I migrate from version 1.1 to 2.0?

See the comprehensive [Migration Guide](migration-from-1.1-to-2.0.md) for detailed instructions. Key changes:

1. **Installation**: `pip install mariadb[binary,pool]` for best experience
2. **Remove deprecated parameters**: `reconnect`, `auto_reconnect`, `cursor_type`, `prepared`
3. **Update cursor creation**: Use `binary=True` instead of `prepared=True`
4. **Update pooling**: Install `mariadb[pool]` and use `create_pool()` instead of `ConnectionPool()`
5. **Consider URI connections**: `mariadb.connect("mariadb://user:pass@host/db")`

### What happened to auto_reconnect?

Automatic reconnection was removed in version 2.0 because it:
- Silently hid connection failures
- Lost session state and uncommitted transactions
- Broke transaction isolation guarantees

**Migration**: Use connection pools (recommended) or call `conn.reconnect()` manually when needed.

### How do I use async/await with version 2.0?

Version 2.0 introduces native async support:

```python
import asyncio
import mariadb

async def main():
    conn = await mariadb.asyncConnect("mariadb://user:pass@host/db")
    cursor = await conn.cursor()
    await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
    row = await cursor.fetchone()
    await cursor.close()
    await conn.close()

asyncio.run(main())
```

For connection pools:
```python
pool = await mariadb.create_async_pool(
    "mariadb://user:pass@host/db",
    min_size=5,
    max_size=20
)
```

See [Async/Await Support](async-usage.md) for detailed documentation.

### What's the difference between prepared and binary?

In version 1.1, the parameter was called `prepared`. In version 2.0, it's renamed to `binary` for clarity:

**Version 1.1:**
```python
cursor = conn.cursor(prepared=True)
```

**Version 2.0:**
```python
cursor = conn.cursor(binary=True)
```

The functionality is the same - both use the MariaDB binary protocol (prepared statements).

### Should I use text or binary protocol?

**Text protocol (default):**
- Predictable behavior
- Good for ad-hoc queries
- No preparation overhead

**Binary protocol (`binary=True`):**
- Better performance for repeated queries
- Automatic prepared statement caching
- Recommended for hot paths

Enable at connection level for applications that mostly use parameterized queries:
```python
conn = mariadb.connect("mariadb://host/db?binary=true")
```

### Q: Which authentication methods are supported by MariaDB Connector/Python?

MariaDB Connector/Python uses MariaDB Connector/C for client-server communication (C extension only). The pure Python implementation supports standard authentication methods. All authentication plugins shipped together with MariaDB Connector/C can be used for user authentication in the C extension.

## General

### Q: How do I execute multiple statements with cursor.execute()?

Since MariaDB Connector/Python uses binary protocol for client-server communication, this feature is not supported yet.

### Q: Does MariaDB Connector/Python work with Python 2.x?

Python versions which reached their end of life are not officially supported. While MariaDB Connector/Python might still work
with older Python 3.x versions, it doesn’t work with Python version 2.x.

### Q: How can I see a transformed statement? Is there a mogrify() method available?

No, MariaDB Connector/Python Python uses binary protocol for client/server communication. Before a statement will be executed
it will be parsed and parameter markers which are different than question marks will be replaced by question
marks. Afterwards the statement will be sent together with data to the server. The transformed statement can
be obtained by cursor.statement attribute.

Example:

```python
data = ("Future", 2000)
statement = """SELECT DATE_FORMAT(creation_time, '%h:%m:%s') as time, topic, amount
               FROM mytable WHERE topic=%s and id > %s"""
cursor.execute(statement, data)
print(cursor.statement)
```

```console
SELECT DATE_FORMAT(creation_time, '%h:%m:%s') as time, topic, amount FROM mytable WHERE topic=? and id > ?
```

Please note, that there is no need to escape ‘%s’ by ‘%%s’ for the time conversion in DATE_FORMAT() function.

### Q: Does MariaDB Connector/Python support paramstyle “pyformat”?

The default paramstyle (see [PEP-249](https://peps.python.org/pep-249)) is **qmark** (question mark) for parameter markers. For compatibility
with other drivers MariaDB Connector/Python also supports (and automatically recognizes) the **format** and **pyformat** parameter
styles.

Mixing different paramstyles within the same query is not supported and will raise an exception.

## Transactions

### Q: Previously inserted records disappeared after my program finished

Default for autocommit in MariaDB Connector/Python is off, which means every transaction must be committed.
Uncommitted pending transactions are rolled back automatically when the connection is closed.

```python
.. code-block:: python

   with mariadb.connect(**conn_params) as conn:
       with conn.cursor() as cursor:
           cursor.execute("CREATE TABLE t1 (id int, name varchar(20))")

           # insert
           data = [(1, "Andy"), (2, "George"), (3, "Betty")]
           cursor.executemany("INSERT INTO t1 VALUES (?,?)", data)

           # commit pending transactions
           connection.commit()
```

{% @marketo/form formId="4316" %}
