# Installation

## API Reference

- **[Connection API](connection.md)** - Connection parameters, methods, and attributes
- **[Cursor API](cursor.md)** - Cursor parameters, methods, and attributes  
- **[Connection Pooling API](pooling.md)** - Pool configuration and usage

<a id="id1"></a>

## Prerequisites

MariaDB Connector/Python 2.0 supports

* Python versions from 3.8 to 3.12
* MariaDB server versions from version 10.3 or MySQL server versions from version 5.7.
* MariaDB client library (MariaDB Connector/C) from version 3.3.1 (optional - only required for C extension).

## Installation Options

### Installing Version 1.1

If you need to install the version 1.1:

```console
pip install mariadb==1.1.10
```

Version 1.1:
- Always installs the C extension
- Requires MariaDB Connector/C to be pre-installed
- Does not support pure Python or binary wheels
- Connection pooling is included by default

For version 1.1 documentation, see the [1.1 branch documentation](https://mariadb-corporation.github.io/mariadb-connector-python/).

### Installing Version 2.0

MariaDB Connector/Python 2.0 offers three installation options:

### 1. Pure Python (Default)

Works everywhere, no compiler or C dependencies required:

```console
pip install mariadb
```

This is the default installation method. The pure Python implementation:
- Works on all Python interpreters (CPython, PyPy, etc.)
- Requires no compilation or system dependencies
- Provides good performance for most use cases
- Fully compatible with the C extension API

### 2. C Extension (Maximum Performance)

For maximum performance, install the C extension:

```console
pip install mariadb[c]
```

The C extension:
- Delivers 2-12× better performance on data-heavy workloads
- **Requires MariaDB Connector/C to be pre-installed** on your system
- Requires a C compiler for building from source
- Provides the same API as the pure Python implementation

### 3. Pre-compiled Binary Wheels

Pre-compiled wheels with no local C connector required:

```console
pip install mariadb[binary]
```

Binary wheels:
- Include the C extension pre-compiled
- **MariaDB Connector/C is bundled** - no separate installation needed
- No compiler required
- Available for common platforms (Windows, Linux, macOS)

### 4. With Connection Pooling

Connection pooling is now a separate optional package:

```console
pip install mariadb[pool]
```

Or combine with binary wheels:

```console
pip install mariadb[binary,pool]
```

### Microsoft Windows

**Option 1: Binary wheels (recommended)**

```console
pip install mariadb[binary,pool]
```

**Option 2: Pure Python**

```console
pip install mariadb[pool]
```

**Option 3: C extension from source**

First install MariaDB Connector/C. MSI installers for both 32-bit and 64-bit operating systems are available from [MariaDB Connector Download page](https://mariadb.com/downloads/connectors/).

Then install the C extension:

```console
pip install mariadb[c,pool]
```

On success, you should see a message at the end "Successfully installed mariadb-2.0.0rc2".

```console
Collecting mariadb
Downloading mariadb-2.0.0rc2-cp311-cp311-win_amd64.whl (210 kB)
---------------------------------------- 210.0/210.0 kB 3.2 MB/s eta 0:00:00
Installing collected packages: mariadb
Successfully installed mariadb-2.0.0rc2
```

## Installation from Source

### Pure Python Installation

The pure Python implementation has minimal requirements:

```console
cd source_package_dir
pip install .
```

No compiler or system dependencies required.

### C Extension Build Prerequisites

To build the C extension from source, you will need:

- C compiler (gcc, clang, or MSVC)
- Python development files (Usually installed with package **python3-dev**). Minimum supported version is Python 3.8.
- MariaDB Connector/C libraries and header files (version 3.3.1 or later)
  - Either from MariaDB server package or from MariaDB Connector/C package
  - If your distribution doesn't provide a recent version, download from [MariaDB Connector Download page](https://mariadb.com/downloads/connectors/) or build from source
- The mariadb_config program from MariaDB Connector/C (must be in your PATH)
- For POSIX systems: TLS libraries (GnuTLS or OpenSSL)
- Python's "packaging" module

**On POSIX systems**, ensure the PATH environment variable contains the directory with the mariadb_config utility.

**Installing the C extension from source:**

```console
cd source_package_dir
pip install mariadb-c/
```

**Installing with pooling support:**

```console
cd source_package_dir
pip install mariadb-pool/
```

For troubleshooting, check the [Installation FAQ](faq.md#installation-faq).

## Test suite

If you have installed the sources, after successful build you can run the test suite
from the source directory.

```console
pytest tests/ -v
```

You can configure the connection parameters by using the following environment variables

* TEST_DB_USER (default root)
* TEST_DB_PASSWORD
* TEST_DB_DATABASE (default ‘testp’)
* TEST_DB_HOST (default ‘localhost’)
* TEST_DB_PORT (default 3306)

{% @marketo/form formId="4316" %}
