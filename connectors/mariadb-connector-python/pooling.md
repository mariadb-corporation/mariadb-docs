# Connection pooling

*Since version 2.0:* Connection pooling is now a separate optional package. Install with:

```console
pip install mariadb[pool]
```

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

**Example - URI Connection:**

```python
pool = mariadb.create_pool(
    "mariadb://example_user:GHbe_Su3B8@localhost/test",
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
        "mariadb://user:password@localhost/mydb",
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
# Install pooling package first
# pip install mariadb[pool]

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
