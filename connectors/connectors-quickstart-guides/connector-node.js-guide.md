---
description: Quickstart guide for MariaDB Connector/Node.js
---

# Connector/Node.js Guide

### Quickstart Guide: MariaDB Connector/Node.js

MariaDB Connector/Node.js is a client library that enables Node.js applications to connect and interact with MariaDB and MySQL databases. It's built natively in JavaScript and supports both Promise and Callback APIs, with the Promise API being the default and recommended approach. It is licensed under the LGPL.

#### 1. Installation

The easiest way to install MariaDB Connector/Node.js is using npm (Node Package Manager):

```bash
npm install mariadb
```

#### 2. Basic Usage (Promise API - Recommended)

The Promise API simplifies asynchronous operations with `async/await`. For optimal performance and resource management, it's recommended to use a connection pool.

**a. Create a Connection Pool:**

```javascript
const mariadb = require('mariadb');
const pool = mariadb.createPool({
    host: 'localhost',
    port: 3306,
    user: 'your_username',
    password: 'your_password',
    database: 'your_database_name',
    connectionLimit: 5 // Adjust as needed
});

console.log("Connection pool created.");
```

Replace `localhost`, `3306`, `your_username`, `your_password`, and `your_database_name` with your actual database details.

**b. Perform Database Operations:**

Here's an `async` function example to get a connection, execute queries, and release the connection back to the pool.

```javascript
async function executeDatabaseOperations() {
    let conn;
    try {
        conn = await pool.getConnection(); // Get a connection from the pool

        // --- SELECT Query ---
        const rows = await conn.query("SELECT id, name FROM your_table_name WHERE status = ?", ["active"]);
        console.log("Selected Rows:", rows);

        // --- INSERT Query (with parameters for security) ---
        const res = await conn.query("INSERT INTO your_table_name (name, status) VALUES (?, ?)", ["New Entry", "pending"]);
        console.log("Insert Result:", res); // res will contain { affectedRows: 1, insertId: ..., warningStatus: 0 }

    } catch (err) {
        console.error("Database operation error:", err);
        throw err; // Re-throw to handle higher up
    } finally {
        if (conn) {
            conn.release(); // Release connection back to the pool
            console.log("Connection released to pool.");
        }
    }
}

// Call the async function
executeDatabaseOperations()
    .then(() => console.log("All database operations attempted."))
    .catch((err) => console.error("Overall operation failed:", err))
    .finally(() => {
        // Optional: End the pool when your application is shutting down
        // pool.end();
        // console.log("Connection pool ended.");
    });
```

#### 3. Basic Usage (Callback API - for Compatibility)

If you need compatibility with older Node.js database drivers (`mysql`, `mysql2`), you can use the Callback API.

```javascript
const mariadb = require('mariadb/callback');

// Create a single connection
mariadb.createConnection({
    host: 'localhost',
    port: 3306,
    user: 'your_username',
    password: 'your_password',
    database: 'your_database_name'
}, (err, conn) => {
    if (err) {
        console.error("Connection error:", err);
        return;
    }

    console.log("Connected using Callback API.");

    // Execute a query
    conn.query("SELECT 1 AS val", (queryErr, rows) => {
        if (queryErr) {
            console.error("Query error:", queryErr);
            conn.end(); // Close connection on error
            return;
        }
        console.log("Query Result (Callback):", rows);

        // Close the connection when done
        conn.end((endErr) => {
            if (endErr) {
                console.error("Error closing connection:", endErr);
            } else {
                console.log("Connection closed (Callback).");
            }
        });
    });
});
```

#### Important Notes:

* **Error Handling:** Always include robust error handling (`try...catch` for Promises, `if (err)` for Callbacks) in your database interactions.
* **Parameterized Queries:** Always use parameterized queries (e.g., `WHERE status = ?`, `VALUES (?, ?)`) to prevent SQL injection attacks.
* **Connection Pooling:** For production applications, always use a connection pool (`mariadb.createPool()`) instead of single connections to manage resources efficiently.
* **`conn.release()` vs. `conn.end()`:** When using a pool, use `conn.release()` to return the connection to the pool. Use `conn.end()` or `pool.end()` only when gracefully shutting down your application.

#### Further Resources:

* [MariaDB Connector/Node.js GitHub Repository](https://github.com/mariadb-corporation/mariadb-connector-nodejs)
* [MariaDB Connector/Node.js Documentation](../mariadb-connector-nodejs/mariadb-connector-node-js-guide.md)
* [npm mariadb package page](https://www.npmjs.com/package/mariadb)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
