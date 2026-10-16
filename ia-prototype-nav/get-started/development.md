---
title: Development
description: >-
  Take the first Python query on MariaDB Server to application code with a connection pool, explicit transactions, and MariaDB SQL features.
icon: code
---

# Development

The landing page ended with one Python script that opens a connection, reads the `shop.products` table, and closes. An application needs a little more than that: connections it can reuse, writes that land together or not at all, and SQL that does work your code would otherwise do. The steps below use MariaDB Connector/Python, and the pool step also shows Node.js and Java. For PHP, .NET, and C++, the connector quickstarts further down pick up the same thread.

## From a Script to an Application

{% stepper %}
{% step %}
### Open a Connection Pool

A connection pool keeps a set of open connections, so each request borrows one instead of paying for a new login. With MariaDB Connector/Python 1.1, the `ConnectionPool` class holds up to 64 connections, and calling `close()` on a pooled connection hands it back to the pool.

{% tabs %}
{% tab title="Python" %}
```python
import mariadb

pool = mariadb.ConnectionPool(
    pool_name="shop",
    pool_size=5,
    host="127.0.0.1",
    port=3306,
    user="root",
    password="changeme",
    database="shop",
)

conn = pool.get_connection()
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM products")
print(cur.fetchone()[0])
conn.close()  # back to the pool, not disconnected
```
{% endtab %}

{% tab title="Node.js" %}
```js
const mariadb = require('mariadb');

const pool = mariadb.createPool({
  host: '127.0.0.1',
  port: 3306,
  user: 'root',
  password: 'changeme',
  database: 'shop',
  connectionLimit: 5
});

async function main() {
  let conn;
  try {
    conn = await pool.getConnection();
    const rows = await conn.query('SELECT COUNT(*) AS n FROM products');
    console.log(rows[0].n);
  } finally {
    if (conn) conn.end();
    await pool.end();
  }
}

main();
```
{% endtab %}

{% tab title="Java" %}
```java
try (MariaDbPoolDataSource pool = new MariaDbPoolDataSource(
        "jdbc:mariadb://127.0.0.1:3306/shop?user=root&password=changeme&maxPoolSize=5")) {
    try (Connection conn = pool.getConnection();
         Statement stmt = conn.createStatement();
         ResultSet rs = stmt.executeQuery("SELECT COUNT(*) FROM products")) {
        rs.next();
        System.out.println(rs.getLong(1));
    }
}
```
{% endtab %}
{% endtabs %}

The [ConnectionPool reference]({connectors}/mariadb-connector-python/pool) lists the pool options, including `pool_reset_connection` and `pool_validation_interval`.
{% endstep %}

{% step %}
### Write Inside a Transaction

MariaDB Connector/Python follows the Python DB API (PEP 249), so autocommit is off, and nothing you write is saved until you call `conn.commit()`. The `?` placeholders are the connector's default parameter style, and the connector sends the values separately from the SQL text, so never build a query with string formatting.

```python
conn = pool.get_connection()
cur = conn.cursor()
try:
    cur.execute(
        "INSERT INTO products (name, price) VALUES (?, ?)",
        ("Monitor arm", 89.00),
    )
    cur.execute(
        "UPDATE products SET price = ? WHERE name = ?",
        (229.00, "Standing desk"),
    )
    conn.commit()
except mariadb.Error as e:
    conn.rollback()
    print(f"Rolled back: {e}")
finally:
    conn.close()
```

If either statement fails, the `rollback()` call undoes both. [Transactions with MariaDB Connector/Python]({connectors}/mariadb-connector-python/transactions-with-mariadb-connector-python) shows how to turn on autocommit when you want each statement saved on its own.
{% endstep %}

{% step %}
### Get the New Row Back With `RETURNING`

MariaDB Server accepts a `RETURNING` clause on `INSERT`, so the statement hands back the generated `id` and any default values in the same round trip. Your code skips the follow-up `SELECT` and reads the row from the cursor.

```python
conn = pool.get_connection()
cur = conn.cursor()
cur.execute(
    "INSERT INTO products (name, price) VALUES (?, ?) RETURNING id, name, price",
    ("Desk mat", 19.00),
)
print(cur.fetchone())
conn.commit()
conn.close()
```

`RETURNING` takes any expression a `SELECT` list can, and `REPLACE` and `DELETE` support it too. See [INSERT...RETURNING]({server}/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning).
{% endstep %}
{% endstepper %}

{% hint style="info" %}
MariaDB Connector/Python 2.0, now a release candidate, moves pooling into an optional package: `pip install --pre mariadb[pool]`, then `mariadb.create_pool()`. The [1.1 to 2.0 migration guide]({connectors}/mariadb-connector-python/migration-from-1.1-to-2.0) maps each change.
{% endhint %}

## Connect From Your Language

Each MariaDB connector has a quickstart that goes from an empty project to a query that returns rows.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Python</strong></td><td>MariaDB Connector/Python, a DB API driver with built-in connection pooling.</td><td><a href="{connectors}/connectors-quickstart-guides/connector-python-guide">connector-python-guide</a></td></tr><tr><td><strong>Node.js</strong></td><td>MariaDB Connector/Node.js, with Promise and callback APIs.</td><td><a href="{connectors}/connectors-quickstart-guides/connector-node.js-guide">connector-node.js-guide</a></td></tr><tr><td><strong>Java</strong></td><td>MariaDB Connector/J for JDBC, plus MariaDB Connector/R2DBC for reactive code.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-j-guide">mariadb-connector-j-guide</a></td></tr><tr><td><strong>PHP</strong></td><td>PDO and mysqli, the drivers PHP already ships with.</td><td><a href="{connectors}/other/mariadb-php-connectors-guide">mariadb-php-connectors-guide</a></td></tr><tr><td><strong>C# and .NET</strong></td><td>MariaDB Connector/NET for ADO.NET applications.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-net-guide">mariadb-connector-net-guide</a></td></tr><tr><td><strong>C++</strong></td><td>MariaDB Connector/C++ for native applications.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-c++-guide">mariadb-connector-c++-guide</a></td></tr></tbody></table>

## Use What MariaDB Adds

These features move work out of your application code and into a single SQL statement.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>JSON</strong></td><td>Store flexible attributes next to relational columns and filter on them with <code>JSON_VALUE</code> in the same query.</td><td><a href="{server}/reference/sql-functions/special-functions/json-functions">json-functions</a></td></tr><tr><td><strong>Temporal Tables</strong></td><td>Let the server keep every version of a row, then read the table as it was with <code>FOR SYSTEM_TIME AS OF</code>.</td><td><a href="{server}/reference/sql-structure/temporal-tables/system-versioned-tables">system-versioned-tables</a></td></tr><tr><td><strong>Common Table Expressions</strong></td><td>Break a long query into named steps with <code>WITH</code>, including recursive queries over trees and graphs.</td><td><a href="{server}/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions">common-table-expressions</a></td></tr></tbody></table>

## Start From a Sample App

MariaDB maintains quickstart repositories on GitHub that you can clone and run against the server from the landing page.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Python Quickstart</strong></td><td>Create a database and table, then run create, read, update, and delete operations with MariaDB Connector/Python.</td><td><a href="https://github.com/mariadb-developers/python-quickstart">python-quickstart</a></td></tr><tr><td><strong>Node.js Quickstart</strong></td><td>Query, insert, and batch-load rows with MariaDB Connector/Node.js, including its connection pool.</td><td><a href="https://github.com/mariadb-developers/nodejs-quickstart">nodejs-quickstart</a></td></tr><tr><td><strong>Java Quickstart</strong></td><td>Samples for JDBC, JPA, Spring Boot, Jakarta EE, and Quarkus on MariaDB Connector/J.</td><td><a href="https://github.com/mariadb-developers/java-quickstart">java-quickstart</a></td></tr></tbody></table>
