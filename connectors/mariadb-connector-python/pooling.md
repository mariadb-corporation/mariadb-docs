---
description: >-
  MariaDB Connector/Python 2.0 connection pooling supports sync and async
  pools via create_pool and create_async_pool, with configurable size,
  health checks, and context managers.
---

# Connection pooling

*Since version 2.0:* Connection pooling is now a separate optional package. Install with:

```console
pip install --pre mariadb[pool]
```

{% hint style="info" %}
As of 2.0.0rc2, version 2.0 is a Release Candidate (RC), so the `--pre` flag is required. Version 1.1 (the latest stable/GA release) includes connection pooling by default.
{% endhint %}

A connection pool is a cache of connections to a database server where connections can be reused for future requests.
Since establishing a connection is resource-expensive and time-consuming, especially when used inside a middle tier
environment which maintains multiple connections and requires connections to be immediately available on the fly.

Especially for server-side web applications, a connection pool is the standard way to maintain a pool of database connections
which are reused across requests.

**Version 2.0 introduces:**
- Synchronous pools with `create_pool()`
- Asynchronous pools with `create_async_pool()`
- Improved API with `min_size` and `max_size` parameters
- Context manager support with `acquire()`

## Configuring and using a connection pool

The typical way for creating and using a connection pool is:

1. Create (and configure) a connection pool
2. Obtain a connection from connection pool using `acquire()`
3. Perform database operation(s)
4. Return the connection to the pool (automatically with context managers)

### Synchronous Connection Pool

*Since version 2.0*

Create a synchronous connection pool using `create_pool()`:

**Pool Configuration Parameters:**

- **`min_size`** (`int`) - Minimum number of connections in the pool. Default: same than max_size
- **`max_size`** (`int`) - Maximum number of connections in the pool. Default: 10
- **`max_idle_time`** (`float`) - Maximum time (seconds) a connection can be idle before being closed. Default: 600.0 (10 minutes)
- **`max_lifetime`** (`float`) - Maximum lifetime (seconds) of a connection before being replaced. Default: 3600.0 (1 hour)
- **`validation_interval`** (`float`) - Interval (seconds) between health checks. Default: 30.0
- **`acquire_timeout`** (`float`) - Timeout (seconds) when acquiring a connection from the pool. Default: 30.0
- **`enable_health_check`** (`bool`) - Enable periodic health checks on pooled connections. Default: True
- **`reset_connection`** (`bool`) - Reset connection state when returning to pool (clears session variables, temporary tables, and prepared statements). Default: False
- **`ping_threshold`** (`float`) - Ping connection if idle for more than this many seconds (0 = disabled). Default: 0.25

**Connection Release Behavior:**

When a connection is returned to the pool (either explicitly or via context manager), the pool automatically handles cleanup:

1. **If `reset_connection=True`**: Calls `conn.reset()` to clear all session state (session variables, temporary tables, prepared statements) without reconnecting. This ensures a clean state for the next user but adds overhead.

2. **If `reset_connection=False` (default)**: Checks if the connection has an active transaction. If a transaction is in progress, it automatically calls `conn.rollback()` to prevent transaction leakage between pool users.

**Best Practices:**
- Use `reset_connection=True` if you need guaranteed clean state (e.g., different users sharing a pool with session-specific settings)
- Use `reset_connection=False` (default) for better performance when session state doesn't matter
- Always commit or rollback transactions explicitly before releasing connections for clarity

**Connection Parameters:**

- All connection parameters from `mariadb.connect()` are supported (host, user, password, database, ssl_ca, etc.)

**Example - Synchronous Pool:**

```python
import mariadb

# Create pool with configuration
pool = mariadb.create_pool(
    host="localhost",
    user="example_user",
    password="GHbe_Su3B8",
    database="test",
    min_size=5,
    max_size=20,
    max_idle_time=600.0,
    max_lifetime=3600.0,
    ping_threshold=0.25,
    enable_health_check=True
)

# Acquire connection from pool
with pool.acquire() as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        print(f"Total users: {count}")

# Connection automatically returned to pool
```

**Example - Connection Parameters:**

The pool factories do not accept a connection URI string; pass connection settings as keyword arguments.

```python
pool = mariadb.create_pool(
    host="localhost",
    user="example_user",
    password="GHbe_Su3B8",
    database="test",
    min_size=10,
    max_size=50
)
```

### Asynchronous Connection Pool

*Since version 2.0*

Create an asynchronous connection pool for async/await applications:

```python
import asyncio
import mariadb

async def main():
    # Create async pool with configuration
    pool = await mariadb.create_async_pool(
        host="localhost",
        user="example_user",
        password="GHbe_Su3B8",
        database="test",
        min_size=5,
        max_size=20,
        max_idle_time=600.0,
        acquire_timeout=30.0,
        enable_health_check=True
    )
    
    # Acquire connection from pool
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT COUNT(*) FROM users")
            count = (await cursor.fetchone())[0]
            print(f"Total users: {count}")
    
    # Close pool when done
    await pool.close()

asyncio.run(main())
```

### FastAPI Example

```python
from fastapi import FastAPI
from contextlib import asynccontextmanager
import mariadb

pool = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pool
    # Startup: Create pool
    pool = await mariadb.create_async_pool(
        host="localhost",
        user="user",
        password="password",
        database="mydb",
        min_size=10,
        max_size=50
    )
    yield
    # Shutdown: Close pool
    await pool.close()

app = FastAPI(lifespan=lifespan)

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    async with await pool.acquire() as conn:
        async with conn.cursor(dictionary=True) as cursor:
            await cursor.execute(
                "SELECT id, name, email FROM users WHERE id = ?",
                (user_id,)
            )
            return await cursor.fetchone()
```

This inline example puts pool access directly in the route, which is fine for a quick reference but couples the database to the route and duplicates the acquire/cursor boilerplate across every endpoint. For a modular `db.py`/`main.py` split that exposes the pool through a FastAPI dependency instead, see [Dependency Injection Pattern (Advanced)](async-usage.md#dependency-injection-pattern-advanced).

### Pool Configuration in a Dependency

The pool configuration parameters described above matter most once the pool creation itself is centralized — a `get_db()` dependency is a natural place to set them, since it's the one function that owns the pool for the life of the application:

```python
import mariadb

pool: mariadb.AsyncConnectionPool | None = None


async def init_pool():
    global pool
    pool = await mariadb.create_async_pool(
        host="localhost",
        user="user",
        password="password",
        database="mydb",
        min_size=5,
        max_size=20,
        acquire_timeout=10.0,      # fail fast under load instead of the 30s default
        enable_health_check=True,  # ping idle connections before handing them out
        reset_connection=True      # clear session state between requests
    )


# This snippet omits close_pool() for brevity — see the linked section
# below for the matching shutdown call.
async def get_db():
    if pool is None:
        raise RuntimeError("Database pool has not been initialized")

    async with await pool.acquire() as conn:
        async with conn.cursor(dictionary=True) as cursor:
            yield cursor
```

`acquire_timeout` bounds how long a request waits for a connection before raising `mariadb.PoolError`, and `reset_connection=True` trades a small amount of overhead per request for a guarantee that no session state (temporary tables, session variables, prepared statements) leaks between requests sharing the pool. See the parameter table above for the rest of the pool-sizing and health-check options. For the full `db.py`/`main.py` wiring — startup/shutdown lifecycle and routes using `Depends(get_db)` — see [Dependency Injection Pattern (Advanced)](async-usage.md#dependency-injection-pattern-advanced).

## Migration from Version 1.1

**Version 1.1:**
```python
pool = mariadb.ConnectionPool(
    pool_name="mypool",
    pool_size=10,
    host="localhost",
    user="user",
    password="password"
)
conn = pool.get_connection()
```

**Version 2.0:**
```python
# Install pooling package first (--pre is required while 2.0 is an RC)
# pip install --pre mariadb[pool]

pool = mariadb.create_pool(
    host="localhost",
    user="user",
    password="password",
    min_size=5,
    max_size=10
)

with pool.acquire() as conn:
    # Use connection
    pass
```

{% @marketo/form formId="4316" %}
