---
description: Quickstart guide for MariaDB Connector/Python
---

# Connector/Python Guide

### Quickstart Guide: MariaDB Connector/Python

MariaDB Connector/Python is the official Python client library for connecting applications to MariaDB and MySQL databases. It implements the Python DB API 2.0 (PEP-249) standard, ensuring compatibility with common Python database programming patterns.

**Version 2.0** offers flexible distribution options:
- **Pure Python** - Works everywhere, no compiler or dependencies required
- **C extension** - Maximum performance (2-12× faster on data-heavy workloads)
- **Pre-compiled wheels** - No MariaDB Connector/C installation needed
- **Async/await support** - Native asynchronous operations for modern Python applications

## API Reference

- **[Connection API](../mariadb-connector-python/connection.md)** - Connection parameters, methods, and attributes
- **[Cursor API](../mariadb-connector-python/cursor.md)** - Cursor parameters, methods, and attributes  
- **[Connection Pooling API](../mariadb-connector-python/pooling.md)** - Pool configuration and usage

#### 1. Prerequisites

Before installing MariaDB Connector/Python, ensure you have:

* **Python:** Version 3.9 or later
* **MariaDB Connector/C:** Version 3.3.1 or later (optional - only required for C extension from source)

#### 2. Installation

Choose the installation option that best fits your needs:

**Pure Python (recommended for most users):**
```bash
pip install mariadb
```

**Pre-compiled binary wheels (best for production):**
```bash
pip install mariadb[binary,pool]
```

**C extension from source (maximum performance):**
```bash
# Requires MariaDB Connector/C installed
pip install mariadb[c,pool]
```

#### 3. Basic Usage

Here's a simple Python example demonstrating how to connect to MariaDB, execute queries, and manage transactions.

**Using Dictionary Configuration (All Versions):**

```python
import mariadb
import sys

# 1. Database Connection Configuration
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database_name'
}

def run_db_operations():
    conn = None
    cursor = None
    try:
        # 2. Establish a Connection
        print("Connecting to MariaDB...")
        conn = mariadb.connect(**db_config)
        print("Connection successful!")

        # 3. Create a Cursor Object
        cursor = conn.cursor()

        # ... (rest of the code continues below)
```

**Using URI Connection String (Since Version 2.0):**

```python
import mariadb
import sys

# 1. Database Connection URI (Available since MariaDB Connector/Python 2.0)
DATABASE_URL = "mariadb://your_username:your_password@localhost:3306/your_database_name"

def run_db_operations():
    conn = None
    cursor = None
    try:
        # 2. Establish a Connection
        print("Connecting to MariaDB...")
        conn = mariadb.connect(DATABASE_URL)
        print("Connection successful!")

        # 3. Create a Cursor Object
        cursor = conn.cursor()

        # --- Example: Create a Table (if it doesn't exist) ---
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE
                )
            """)
            conn.commit() # Commit the transaction for DDL
            print("Table 'users' created or already exists.")
        except mariadb.Error as e:
            print(f"Error creating table: {e}")
            conn.rollback() # Rollback in case of DDL error

        # --- Example: Insert Data (Parameterized Query) ---
        print("\nInserting data...")
        insert_query = "INSERT INTO users (name, email) VALUES (?, ?)"
        try:
            cursor.execute(insert_query, ("Alice Wonderland", "alice@example.com"))
            cursor.execute(insert_query, ("Bob Builder", "bob@example.com"))
            conn.commit() # Commit the transaction for DML
            print(f"Inserted {cursor.rowcount} rows.")
            print(f"Last inserted ID: {cursor.lastrowid}")
        except mariadb.IntegrityError as e:
            print(f"Error inserting data (might be duplicate email): {e}")
            conn.rollback()
        except mariadb.Error as e:
            print(f"Error inserting data: {e}")
            conn.rollback()

        # --- Example: Select Data ---
        print("\nSelecting data...")
        select_query = "SELECT id, name, email FROM users WHERE name LIKE ?"
        cursor.execute(select_query, ("%Alice%",)) # Note the comma for single parameter tuple
        
        print("Fetched data:")
        for row in cursor:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

        # --- Example: Update Data ---
        print("\nUpdating data...")
        update_query = "UPDATE users SET name = ? WHERE email = ?"
        cursor.execute(update_query, ("Alicia Wonderland", "alice@example.com"))
        conn.commit()
        print(f"Rows updated: {cursor.rowcount}")

        # --- Example: Delete Data ---
        print("\nDeleting data...")
        delete_query = "DELETE FROM users WHERE name = ?"
        cursor.execute(delete_query, ("Bob Builder",))
        conn.commit()
        print(f"Rows deleted: {cursor.rowcount}")

    except mariadb.Error as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        # 4. Close Cursor and Connection
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if conn:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    run_db_operations()
```

**Before Running:**

1. Replace `your_username`, `your_password`, and `your_database_name` with your actual MariaDB server credentials.
2. Ensure you have a MariaDB server running and the specified database exists.
3. The example assumes `your_table_name` is `users` with columns `id`, `name`, `email`. Adjust the table/column names as needed.

#### Important Notes:

* **Parameterized Queries:** Always use parameterized queries (e.g., `VALUES (?, ?)`) to prevent SQL injection vulnerabilities. Parameters are passed as a tuple or list to the `execute()` method.
* **Transactions (`conn.commit()` / `conn.rollback()`):** By default, autocommit is disabled. Call `conn.commit()` to save changes or `conn.rollback()` to undo them.
* **Error Handling:** Use `try...except mariadb.Error` blocks to gracefully handle database-related exceptions.
* **Resource Management:** Always close your `cursor` and `connection` objects in a `finally` block to ensure resources are released, even if errors occur.
* **URI Connections:** Version 2.0 supports standard URI connection strings for cleaner configuration.
* **Binary Protocol:** Use `binary=True` for prepared statements and better performance with repeated queries.

#### 4. Async/Await Support (New in 2.0)

For modern async applications (FastAPI, Starlette, etc.):

```python
import asyncio
import mariadb

async def async_operations():
    # Connect asynchronously
    conn = await mariadb.asyncConnect(
        "mariadb://your_username:your_password@localhost/your_database_name"
    )
    
    try:
        cursor = await conn.cursor()
        
        # Execute async query
        await cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (1,))
        user = await cursor.fetchone()
        print(f"User: {user}")
        
        await cursor.close()
    finally:
        await conn.close()

# Run async function
asyncio.run(async_operations())
```

**Async Connection Pool:**

```python
import asyncio
import mariadb

async def main():
    # Create async pool
    pool = await mariadb.create_async_pool(
        "mariadb://user:password@localhost/mydb",
        min_size=5,
        max_size=20
    )
    
    # Use pool
    async with await pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT COUNT(*) FROM users")
            count = (await cursor.fetchone())[0]
            print(f"Total users: {count}")
    
    await pool.close()

asyncio.run(main())
```

#### Further Resources:

* [PyPI MariaDB Connector/Python](https://pypi.org/project/mariadb/)
* [MariaDB Connector/Python Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/)
* [Migration Guide (1.1 to 2.0)](https://mariadb-corporation.github.io/mariadb-connector-python/migration-from-1.1-to-2.0.html)
* [Async/Await Support](https://mariadb-corporation.github.io/mariadb-connector-python/async-usage.html)
* [MariaDB Developers Python Quickstart (GitHub)](https://github.com/mariadb-developers/python-quickstart)
