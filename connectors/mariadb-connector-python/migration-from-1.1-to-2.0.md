# Migration Guide: MariaDB Connector/Python 1.1 to 2.0

This guide helps you migrate your applications from MariaDB Connector/Python 1.1 to version 2.0.0.

## API Reference

- **[Connection API](connection.md)** - Connection parameters, methods, and attributes
- **[Cursor API](cursor.md)** - Cursor parameters, methods, and attributes  
- **[Connection Pooling API](pooling.md)** - Pool configuration and usage

## Overview

Version 2.0 is a major rewrite that introduces significant improvements and breaking changes:

- **Flexible distribution options**: Pure Python, C extension, and pre-compiled binary wheels
- **Native async/await support**: First-class asynchronous API
- **URI connection strings**: Standard `mariadb://` connection syntax
- **Full type hints**: Complete mypy and pyright compatibility
- **Improved performance**: Faster parameter binding and prepared statement caching
- **Unified protocol control**: Explicit binary vs text protocol selection

## Installation Changes

### Version 1.1 Installation

```bash
pip install mariadb
```

This always installed the C extension and required MariaDB Connector/C to be pre-installed.

### Version 2.0 Installation Options

**Pure Python (default, works everywhere):**
```bash
pip install mariadb
```

**C extension (maximum performance):**
```bash
pip install mariadb[c]
```
*Requires MariaDB Connector/C to be pre-installed on your system.*

**Pre-compiled binary wheels (no local C connector required):**
```bash
pip install mariadb[binary]
```
*MariaDB Connector/C is bundled - no separate installation needed.*

**With connection pooling:**
```bash
pip install mariadb[pool]
# or combined
pip install mariadb[binary,pool]
```

### Key Changes

- **Pure Python is now default**: No compiler or MariaDB Connector/C required
- **Connection pooling is optional**: Must explicitly install `mariadb[pool]`
- **Binary wheels available**: Pre-compiled for common platforms with MariaDB Connector/C bundled
- **C extension requires pre-installation**: MariaDB Connector/C must be installed separately when building from source with `mariadb[c]`

## Breaking Changes

### 1. Removed: Auto-Reconnect

**Version 1.1:**
```python
conn = mariadb.connect(
    host="localhost",
    user="root",
    password="secret",
    reconnect=True  # Automatic reconnection
)
```

**Version 2.0:**
```python
# reconnect and auto_reconnect parameters removed
conn = mariadb.connect(
    host="localhost",
    user="root",
    password="secret"
)

# Manual reconnection still available
try:
    conn.ping()
except mariadb.Error:
    conn.reconnect()  # Explicit reconnection only
```

**Why removed**: Auto-reconnect silently hid failures, caused unpredictable behavior with lost session state, uncommitted transactions, and broken transaction isolation.

**Migration**: Use connection pools instead. For manual reconnection, call `conn.reconnect()` explicitly.

### 2. Removed: cursor_type Parameter

**Version 1.1:**
```python
cursor = conn.cursor(cursor_type=mariadb.CURSOR.READ_ONLY)
```

**Version 2.0:**
```python
# Use buffered=False instead
cursor = conn.cursor(buffered=False)
```

**Migration**: Replace `cursor_type=CURSOR.READ_ONLY` with `buffered=False`.

### 3. Renamed: prepared → binary

**Version 1.1:**
```python
cursor = conn.cursor(prepared=True)
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
```

**Version 2.0:**
```python
cursor = conn.cursor(binary=True)
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
```

**Migration**: Replace `prepared=True` with `binary=True`.

### 4. Changed: Binary Protocol Behavior

**Version 1.1:**
Automatically promoted certain parameter types (bytes, datetime) to binary protocol, even when not requested.

**Version 2.0:**
- **Text protocol by default**: Predictable, debuggable
- **Explicit binary=True required**: No automatic promotion
- **Dict parameters always use text protocol**: Named parameter substitution

**Version 1.1 (automatic promotion):**
```python
cursor.execute("SELECT ?", (b'\xde\xad',))
# Silently used binary protocol
```

**Version 2.0 (explicit control):**
```python
# Text protocol (default)
cursor.execute("SELECT ?", (b'\xde\xad',))
# Sends: SELECT _binary'\xde\xad'

# Binary protocol (explicit)
cursor = conn.cursor(binary=True)
cursor.execute("SELECT ?", (b'\xde\xad',))
# Uses COM_STMT_PREPARE + COM_STMT_EXECUTE
```

**Migration**: If you relied on automatic binary protocol, explicitly set `binary=True`.

### 5. Connection Pooling Now Separate Package

**Version 1.1:**
```python
import mariadb

pool = mariadb.ConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="root",
    password="secret"
)
```

**Version 2.0:**
```bash
# First install pooling support
pip install mariadb[pool]
```

```python
import mariadb

# Synchronous pool
pool = mariadb.create_pool(
    host="localhost",
    user="root",
    password="secret",
    min_size=5,
    max_size=10
)

# Asynchronous pool (new in 2.0)
pool = await mariadb.create_async_pool(
    host="localhost",
    user="root",
    password="secret",
    min_size=5,
    max_size=10
)
```

**Migration**: 
1. Install `mariadb[pool]`
2. Use `create_pool()` instead of `ConnectionPool()`
3. Note: `pool_size` split into `min_size` and `max_size`

### 6. Removed: plugin_dir in Pure Python

**Version 1.1:**
```python
conn = mariadb.connect(
    host="localhost",
    plugin_dir="/path/to/plugins"
)
```

**Version 2.0:**
```python
# plugin_dir removed in pure Python implementation
# Still available in C extension
conn = mariadb.connect(host="localhost")
```

**Migration**: The C extension still supports `plugin_dir`. Pure Python does not load native authentication plugins from disk.

## New Features

### 1. URI Connection Strings

**Version 2.0 introduces standard URI syntax:**

```python
# Simple connection
conn = mariadb.connect("mariadb://root:secret@localhost:3306/mydb")

# With query parameters
conn = mariadb.connect(
    "mariadb://root:secret@localhost:3306/mydb?binary=true&autocommit=true"
)

# Keyword arguments override URI values
conn = mariadb.connect(
    "mariadb://root:secret@localhost/mydb",
    database="otherdb"  # Overrides 'mydb'
)
```

**Migration**: Consider using URI strings for cleaner configuration, especially with environment variables:

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL")
conn = mariadb.connect(DATABASE_URL)
```

### 2. Async/Await Support

**New in 2.0 - Native asynchronous API:**

```python
import asyncio
import mariadb

async def main():
    # Single connection
    async with await mariadb.asyncConnect(
        "mariadb://user:pass@host/db"
    ) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
            row = await cursor.fetchone()
            print(row)

    # Connection pool
    pool = await mariadb.create_async_pool(
        "mariadb://user:pass@host/db",
        min_size=5,
        max_size=20
    )
    
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT 1")
            result = await cursor.fetchone()
    
    await pool.close()

asyncio.run(main())
```

**Migration**: For async applications (FastAPI, Starlette, etc.), use the async API instead of wrapping synchronous calls in thread pools.

### 3. Connection-Level Binary Protocol

**Version 2.0 allows setting binary protocol at connection level:**

```python
# All cursors default to binary protocol
conn = mariadb.connect(
    "mariadb://localhost/mydb?binary=true"
)

# Or with keyword argument
conn = mariadb.connect(
    host="localhost",
    database="mydb",
    binary=True
)

# All cursors now use binary protocol by default
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
```

**Migration**: For applications that mostly use prepared statements, set `binary=True` at connection level.

### 4. Prepared Statement Caching

**New in 2.0 - Automatic statement caching:**

```python
# Enabled by default
conn = mariadb.connect("mariadb://localhost/mydb")

# Configure cache size
conn = mariadb.connect(
    "mariadb://localhost/mydb?prep_stmt_cache_size=500"
)

# Disable caching (1.1-like behavior)
conn = mariadb.connect(
    "mariadb://localhost/mydb?cache_prep_stmts=false"
)
```

**Benefits**: 
- First execution pays PREPARE cost
- Subsequent executions reuse prepared statement
- 2-4× performance improvement for repeated queries

**Migration**: No changes needed - caching is automatic. Consider increasing `prep_stmt_cache_size` for applications with many distinct queries.


## Migration Checklist

### Step 1: Update Installation

```bash
# Choose your installation option
pip install mariadb[binary,pool]
```

### Step 2: Update Cursor Creation

**Before:**
```python
cursor = conn.cursor(prepared=True)
cursor = conn.cursor(cursor_type=mariadb.CURSOR.READ_ONLY)
```

**After:**
```python
cursor = conn.cursor(binary=True)
cursor = conn.cursor(buffered=False)
```

### Step 3: Remove Auto-Reconnect Logic

**Before:**
```python
conn = mariadb.connect(
    host="localhost",
    auto_reconnect=True
)
```

**After:**
```python
# Use connection pool (recommended)
pool = mariadb.create_pool(
    host="localhost",
    min_size=5,
    max_size=10
)

# Or handle reconnection manually
try:
    conn.ping()
except mariadb.Error:
    conn.reconnect()
```

## Performance Considerations

### Prepared Statement Caching

Version 2.0 introduces automatic prepared statement caching. For best performance:

1. **Use binary protocol for hot paths:**
   ```python
   conn = mariadb.connect("mariadb://localhost/mydb?binary=true")
   ```

2. **Increase cache size for many distinct queries:**
   ```python
   conn = mariadb.connect(
       "mariadb://localhost/mydb?prep_stmt_cache_size=500"
   )
   ```

3. **Reuse the same SQL statements** - the cache benefits repeated executions

### When to Use Binary Protocol

- **Connection-level**: When most queries are parameterized and repeated
- **Per-cursor**: For specific hot queries in mixed workloads
- **Text protocol**: For ad-hoc queries, SHOW commands, administrative queries

### Async for High Concurrency

For web applications with high concurrency (FastAPI, Starlette):

```python
# Instead of thread pool wrapping
pool = await mariadb.create_async_pool(
    "mariadb://localhost/mydb",
    min_size=10,
    max_size=50
)
```

## Compatibility Notes

### Python Version Support

- **Version 1.1**: Python 3.7 - 3.11
- **Version 2.0**: Python 3.8+ (check release notes for exact range)

### Server Compatibility

Both versions support:
- MariaDB Server 10.3+
- MySQL Server 5.7+

### API Compatibility

The `mariadb.connect()` API with keyword arguments remains largely backward compatible. Most 1.1 code will work with minimal changes after removing deprecated parameters.

{% @marketo/form formId="4316" %}
