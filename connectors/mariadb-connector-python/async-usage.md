# Async/Await Support

MariaDB Connector/Python 2.0 introduces native async/await support for asynchronous database operations. This enables efficient database access in async applications like FastAPI, Starlette, and other asyncio-based frameworks.

## API Reference

- **[Connection API](connection.md)** - Connection parameters, methods, and attributes
- **[Cursor API](cursor.md)** - Cursor parameters, methods, and attributes  
- **[Connection Pooling API](pooling.md)** - Pool configuration and usage

## Overview

The async API provides:
- **Native asyncio integration**: No thread pool wrapping required
- **Async connections**: `asyncConnect()` function and `AsyncConnection` class
- **Async cursors**: `AsyncCursor` class with async methods
- **Async connection pools**: `create_async_pool()` for connection pooling
- **Context manager support**: Async `with` statements for resource management
- **Same API surface**: Familiar interface matching the synchronous API

Both the pure Python and C extension implementations support async operations.

## Basic Async Connection

### Single Connection

```python
import asyncio
import mariadb

async def main():
    # Connect using URI
    conn = await mariadb.asyncConnect("mariadb://user:password@localhost/mydb")
    
    try:
        cursor = await conn.cursor()
        try:
            # Execute query
            await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
            
            # Fetch results
            row = await cursor.fetchone()
            print(row)
        finally:            
            await cursor.close()
    finally:
        await conn.close()

asyncio.run(main())
```

### Using Context Managers (Recommended)

```python
import asyncio
import mariadb

async def main():
    # Connection and cursor automatically closed
    async with await mariadb.asyncConnect(
        "mariadb://user:password@localhost/mydb"
    ) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
            row = await cursor.fetchone()
            print(row)

asyncio.run(main())
```

## Connection Parameters

Async connections support the same parameters as synchronous connections:

### URI Connection

```python
conn = await mariadb.asyncConnect(
    "mariadb://user:password@localhost:3306/mydb?autocommit=true&binary=true"
)
```

### Keyword Arguments

```python
conn = await mariadb.asyncConnect(
    host="localhost",
    port=3306,
    user="user",
    password="password",
    database="mydb",
    autocommit=True,
    binary=True
)
```

### Combining URI and Keywords

```python
# Keywords override URI values
conn = await mariadb.asyncConnect(
    "mariadb://user:password@localhost/mydb",
    database="otherdb"  # Overrides 'mydb'
)
```

## Async Cursor Operations

### Executing Queries

```python
async with await mariadb.asyncConnect("mariadb://localhost/mydb") as conn:
    async with conn.cursor() as cursor:
        # Simple query
        await cursor.execute("SELECT COUNT(*) FROM users")
        count = await cursor.fetchone()
        print(f"Total users: {count[0]}")
        
        # Parameterized query
        await cursor.execute(
            "SELECT name, email FROM users WHERE id = ?",
            (user_id,)
        )
        user = await cursor.fetchone()
```

### Fetching Results

```python
async with conn.cursor() as cursor:
    await cursor.execute("SELECT * FROM users")
    
    # Fetch one row
    row = await cursor.fetchone()
    
    # Fetch multiple rows
    rows = await cursor.fetchmany(10)
    
    # Fetch all remaining rows
    all_rows = await cursor.fetchall()
    
    # Iterate over results
    await cursor.execute("SELECT * FROM users")
    async for row in cursor:
        print(row)
```

### Inserting Data

```python
async with conn.cursor() as cursor:
    # Single insert
    await cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        ("Alice", "alice@example.com")
    )
    await conn.commit()
    
    # Get last inserted ID
    print(f"Inserted user ID: {cursor.lastrowid}")
```

### Batch Operations

```python
async with conn.cursor() as cursor:
    data = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com")
    ]
    
    await cursor.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        data
    )
    await conn.commit()
    print(f"Inserted {cursor.rowcount} rows")
```

## Async Transactions

```python
async with await mariadb.asyncConnect("mariadb://localhost/mydb") as conn:
    try:
        async with conn.cursor() as cursor:
            # Start transaction (autocommit is False by default)
            await cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (100, 1)
            )
            await cursor.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?",
                (100, 2)
            )
            
            # Commit transaction
            await conn.commit()
    except mariadb.Error as e:
        # Rollback on error
        await conn.rollback()
        print(f"Transaction failed: {e}")
        raise
```

## Async Connection Pools

Connection pools are essential for web applications handling multiple concurrent requests.

### Creating an Async Pool

```python
import asyncio
import mariadb

async def main():
    # Create pool
    pool = await mariadb.create_async_pool(
        host="localhost",
        user="user",
        password="password",
        database="mydb",
        min_size=5,    # Minimum connections
        max_size=20,   # Maximum connections
        ping_threshold=0.25  # Ping if idle > 250ms
    )
    
    # Use pool
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
            row = await cursor.fetchone()
            print(row)
    
    # Close pool when done
    await pool.close()

asyncio.run(main())
```

### Pool with URI

```python
pool = await mariadb.create_async_pool(
    "mariadb://user:password@localhost/mydb",
    min_size=10,
    max_size=50
)
```

### Pool Configuration

```python
pool = await mariadb.create_async_pool(
    host="localhost",
    user="user",
    password="password",
    database="mydb",
    min_size=5,           # Minimum pool size
    max_size=20,          # Maximum pool size
    ping_threshold=0.25,  # Ping connections idle > 250ms
    binary=True,          # Use binary protocol by default
    autocommit=False      # Transaction mode
)
```

## FastAPI Integration Example

```python
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import mariadb

# Global pool variable
pool = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create pool
    global pool
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
            user = await cursor.fetchone()
            
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            
            return user

@app.post("/users")
async def create_user(name: str, email: str):
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            try:
                await cursor.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    (name, email)
                )
                await conn.commit()
                
                return {
                    "id": cursor.lastrowid,
                    "name": name,
                    "email": email
                }
            except mariadb.IntegrityError:
                await conn.rollback()
                raise HTTPException(
                    status_code=400,
                    detail="User with this email already exists"
                )
```

## Error Handling

```python
import asyncio
import mariadb

async def main():
    try:
        conn = await mariadb.asyncConnect(
            "mariadb://user:password@localhost/mydb"
        )
    except mariadb.Error as e:
        print(f"Connection error: {e}")
        return
    
    try:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
            row = await cursor.fetchone()
    except mariadb.DatabaseError as e:
        print(f"Database error: {e}")
    except mariadb.ProgrammingError as e:
        print(f"Programming error: {e}")
    finally:
        await conn.close()

asyncio.run(main())
```

## Cursor Types

### Dictionary Cursor

Returns rows as dictionaries instead of tuples:

```python
async with conn.cursor(dictionary=True) as cursor:
    await cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (1,))
    user = await cursor.fetchone()
    print(user["name"])  # Access by column name
```

### Named Tuple Cursor

Returns rows as named tuples:

```python
async with conn.cursor(named_tuple=True) as cursor:
    await cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (1,))
    user = await cursor.fetchone()
    print(user.name)  # Access as attribute
```

### Unbuffered Cursor

Fetches rows on demand instead of buffering entire result set:

```python
async with conn.cursor(buffered=False) as cursor:
    await cursor.execute("SELECT * FROM large_table")
    
    # Fetch rows one at a time
    async for row in cursor:
        process_row(row)
        # Only one row in memory at a time
```

## Binary Protocol with Async

Use binary protocol for better performance with prepared statements:

```python
# Connection-level binary protocol
conn = await mariadb.asyncConnect(
    "mariadb://localhost/mydb?binary=true"
)

async with conn.cursor() as cursor:
    # All queries use binary protocol
    await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
    row = await cursor.fetchone()

# Or per-cursor
async with conn.cursor(binary=True) as cursor:
    await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
    row = await cursor.fetchone()
```

## Performance Considerations

### Connection Pooling

Always use connection pools in production:

```python
# Good: Connection pool
pool = await mariadb.create_async_pool(
    "mariadb://localhost/mydb",
    min_size=10,
    max_size=50
)

# Bad: Creating connections per request
async def handle_request():
    conn = await mariadb.asyncConnect("mariadb://localhost/mydb")
    # ... use connection
    await conn.close()
```

### Prepared Statement Caching

Enable for repeated queries (enabled by default):

```python
conn = await mariadb.asyncConnect(
    "mariadb://localhost/mydb?binary=true&prep_stmt_cache_size=150"
)
```

### Batch Operations

Use `executemany()` for bulk inserts:

```python
# Good: Batch insert
await cursor.executemany(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    data
)

# Bad: Loop with execute
for name, email in data:
    await cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )
```

## Async vs Sync Performance

The async implementation provides:

- **No GIL contention**: Pure Python async uses native asyncio I/O
- **Efficient concurrency**: Handle thousands of concurrent connections
- **Lower latency**: No thread pool overhead
- **Better resource usage**: Event loop scheduling vs thread context switching

Note: Async excels in high-concurrency scenarios, not single-threaded throughput.

## Complete Example

```python
import asyncio
import mariadb
from typing import Optional

async def setup_database():
    """Initialize database connection pool"""
    pool = await mariadb.create_async_pool(
        host="localhost",
        user="user",
        password="password",
        database="mydb",
        min_size=5,
        max_size=20,
        binary=True
    )
    return pool

async def get_user(pool, user_id: int) -> Optional[dict]:
    """Fetch user by ID"""
    async with await pool.acquire() as conn:
        async with conn.cursor(dictionary=True) as cursor:
            await cursor.execute(
                "SELECT id, name, email FROM users WHERE id = ?",
                (user_id,)
            )
            return await cursor.fetchone()

async def create_user(pool, name: str, email: str) -> int:
    """Create new user and return ID"""
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )
            await conn.commit()
            return cursor.lastrowid

async def update_user(pool, user_id: int, name: str, email: str) -> bool:
    """Update user information"""
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "UPDATE users SET name = ?, email = ? WHERE id = ?",
                (name, email, user_id)
            )
            await conn.commit()
            return cursor.rowcount > 0

async def delete_user(pool, user_id: int) -> bool:
    """Delete user by ID"""
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "DELETE FROM users WHERE id = ?",
                (user_id,)
            )
            await conn.commit()
            return cursor.rowcount > 0

async def main():
    # Setup
    pool = await setup_database()
    
    try:
        # Create user
        user_id = await create_user(pool, "Alice", "alice@example.com")
        print(f"Created user with ID: {user_id}")
        
        # Get user
        user = await get_user(pool, user_id)
        print(f"User: {user}")
        
        # Update user
        updated = await update_user(pool, user_id, "Alice Smith", "alice.smith@example.com")
        print(f"Updated: {updated}")
        
        # Delete user
        deleted = await delete_user(pool, user_id)
        print(f"Deleted: {deleted}")
        
    finally:
        # Cleanup
        await pool.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Best Practices

1. **Always use connection pools** in production applications
2. **Use context managers** for automatic resource cleanup
3. **Enable binary protocol** for repeated parameterized queries
4. **Handle errors properly** with try/except blocks
5. **Close pools** during application shutdown
6. **Configure pool sizes** based on your workload
7. **Use prepared statement caching** for better performance
8. **Avoid creating connections per request** - use pools instead

## Migration from Sync to Async

### Before (Synchronous)

```python
import mariadb

conn = mariadb.connect("mariadb://localhost/mydb")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
row = cursor.fetchone()
cursor.close()
conn.close()
```

### After (Asynchronous)

```python
import asyncio
import mariadb

async def main():
    conn = await mariadb.asyncConnect("mariadb://localhost/mydb")
    cursor = await conn.cursor()
    await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
    row = await cursor.fetchone()
    await cursor.close()
    await conn.close()

asyncio.run(main())
```

### With Context Managers

```python
async def main():
    async with await mariadb.asyncConnect("mariadb://localhost/mydb") as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
            row = await cursor.fetchone()

asyncio.run(main())
```

{% @marketo/form formId="4316" %}
