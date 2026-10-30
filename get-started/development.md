---
title: Development
description: >-
  Build applications and agents on one SQL surface, with connection pools, transactions, and RETURNING, and connectors for Python, Node.js, Java, and more.
icon: code
---

# Development

The first real customer buys the standing desk. The script from the landing page could serve that one person, because it opens a connection, reads the `shop.products` table, and closes. A shop doesn't get one customer at a time, though. During a lunch-hour sale, every checkout that opens its own connection pays for a network handshake and a login before it runs a single query.

The order itself raises two more problems. The sale has to record the order and take the desk out of stock, and if the server stops between those two writes, the shop either sells a desk it doesn't have or loses track of one it sold. Then the confirmation page wants the new order number, which the database creates, not your code.

## Handle an Order

{% stepper %}
{% step %}
### Use a Connection Pool

A connection pool opens a set of connections once and lends them out, so each checkout borrows one instead of logging in again. The examples connect as the `shop_app` account from the [Server](choose-your-path/community-server.md) page. In MariaDB Connector/Python 1.1, the `ConnectionPool` class holds up to 64 connections, and calling `close()` on a pooled connection hands it back to the pool. The `connectionLimit` option in MariaDB Connector/Node.js and the `maxPoolSize` option in MariaDB Connector/J set the same cap.

{% tabs %}
{% tab title="Python" %}
```python
import mariadb

pool = mariadb.ConnectionPool(
    pool_name="shop",
    pool_size=5,
    host="127.0.0.1",
    port=3306,
    user="shop_app",
    password="app-password",
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
  user: 'shop_app',
  password: 'app-password',
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
    if (conn) await conn.release();
    await pool.end();
  }
}

main();
```
{% endtab %}

{% tab title="Java" %}
```java
try (MariaDbPoolDataSource pool = new MariaDbPoolDataSource(
        "jdbc:mariadb://127.0.0.1:3306/shop?user=shop_app&password=app-password&maxPoolSize=5")) {
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

The [ConnectionPool reference]({connectors}/mariadb-connector-python/api/pool) lists the pool options, including `pool_reset_connection` and `pool_validation_interval`.
{% endstep %}

{% step %}
### Write Inside a Transaction

The shop needs somewhere to record sales and a number to count down. The `shop_app` account can only change rows, so open the `mariadb` client as `root`, as on the landing page, to add a `stock` column to the `products` table, give the standing desk five units, and create an `orders` table:

```sql
ALTER TABLE shop.products ADD COLUMN stock INT NOT NULL DEFAULT 0;
UPDATE shop.products SET stock = 5 WHERE name = 'Standing desk';

CREATE TABLE shop.orders (
  id         INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT NOT NULL,
  quantity   INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (product_id) REFERENCES shop.products (id)
);
```

MariaDB Connector/Python follows the Python DB API (PEP 249), so autocommit is off, and nothing you write is saved until you call `conn.commit()`. That makes the two writes one unit. The `UPDATE` statement only decrements stock when enough is left, and the `cur.rowcount` attribute tells you whether it matched a row. The `?` placeholders are the connector's default parameter style, and the connector sends the values separately from the SQL text, so never build a query with string formatting.

```python
product_id, quantity = 2, 1  # the standing desk

conn = pool.get_connection()
cur = conn.cursor()
try:
    cur.execute(
        "UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?",
        (quantity, product_id, quantity),
    )
    if cur.rowcount == 0:
        raise ValueError("not enough stock")
    cur.execute(
        "INSERT INTO orders (product_id, quantity) VALUES (?, ?)",
        (product_id, quantity),
    )
    conn.commit()
except (mariadb.Error, ValueError) as e:
    conn.rollback()
    print(f"Rolled back: {e}")
finally:
    conn.close()
```

If either write fails, or the desk is sold out, the `rollback()` call undoes both. [Transactions with MariaDB Connector/Python]({connectors}/mariadb-connector-python/transactions-with-mariadb-connector-python) shows how to turn on autocommit when you want each statement saved on its own.
{% endstep %}

{% step %}
### Return the New Row

The `orders` table generates the order number with `AUTO_INCREMENT`, so your code doesn't know it until the row exists. A `RETURNING` clause on the `INSERT` statement hands back the new `id` and the server-filled `created_at` value in the same round trip, without a follow-up `SELECT`. Replace the `INSERT` and `commit()` lines in the previous step with these:

```python
    cur.execute(
        "INSERT INTO orders (product_id, quantity) VALUES (?, ?) "
        "RETURNING id, created_at",
        (product_id, quantity),
    )
    order_id, created_at = cur.fetchone()
    conn.commit()
    print(f"Order {order_id} placed at {created_at}")
```

`RETURNING` accepts the expressions a `SELECT` list can, except aggregate functions such as `COUNT()`, and `DELETE` supports it too, so a cancelled order can hand back the row it removed. See [INSERT...RETURNING]({server}/reference/sql-statements/data-manipulation/inserting-loading-data/insertreturning) and [DELETE]({server}/reference/sql-statements/data-manipulation/changing-deleting-data/delete).
{% endstep %}
{% endstepper %}

The customer sees the new order number on the confirmation page, the standing desk's stock drops by one with each order, and the connection goes back to the pool for the next checkout.

{% hint style="info" %}
MariaDB Connector/Python 2.0, now a release candidate, moves pooling into an optional package: `pip install --pre 'mariadb[pool]'`, then `mariadb.create_pool()`. The [1.1 to 2.0 migration guide]({connectors}/mariadb-connector-python/migration-from-1.1-to-2.0) maps each change.
{% endhint %}

## Connect From Your Language

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Python</strong></td><td>MariaDB Connector/Python, a DB API driver with built-in connection pooling.</td><td><a href="{connectors}/connectors-quickstart-guides/connector-python-guide">connector-python-guide</a></td></tr><tr><td><strong>Node.js</strong></td><td>MariaDB Connector/Node.js, with Promise and callback APIs.</td><td><a href="{connectors}/connectors-quickstart-guides/connector-node.js-guide">connector-node.js-guide</a></td></tr><tr><td><strong>Java</strong></td><td>MariaDB Connector/J for JDBC, plus MariaDB Connector/R2DBC for reactive code.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-j-guide">mariadb-connector-j-guide</a></td></tr><tr><td><strong>PHP</strong></td><td>PDO and mysqli, the drivers PHP already ships with.</td><td><a href="{connectors}/other/mariadb-php-connectors-guide">mariadb-php-connectors-guide</a></td></tr><tr><td><strong>C# and .NET</strong></td><td>MariaDB Connector/NET for ADO.NET applications.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-net-guide">mariadb-connector-net-guide</a></td></tr><tr><td><strong>C++</strong></td><td>MariaDB Connector/C++ for native applications.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-c++-guide">mariadb-connector-c++-guide</a></td></tr></tbody></table>

## Keep Going

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>JSON</strong></td><td>Keep product attributes like color and size in a JSON column and filter on them with <code>JSON_VALUE</code>.</td><td><a href="{server}/reference/sql-functions/special-functions/json-functions">json-functions</a></td></tr><tr><td><strong>Temporal Tables</strong></td><td>Let the server keep every past price and stock count, then read the table as it was with <code>FOR SYSTEM_TIME AS OF</code>.</td><td><a href="{server}/reference/sql-structure/temporal-tables/system-versioned-tables">system-versioned-tables</a></td></tr><tr><td><strong>Common Table Expressions</strong></td><td>Break a long query into named steps with <code>WITH</code>, including recursive queries over category trees.</td><td><a href="{server}/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions">common-table-expressions</a></td></tr><tr><td><strong>Python Quickstart</strong></td><td>A GitHub repository that runs create, read, update, and delete operations with MariaDB Connector/Python.</td><td><a href="https://github.com/mariadb-developers/python-quickstart">python-quickstart</a></td></tr><tr><td><strong>Node.js Quickstart</strong></td><td>A GitHub repository that queries, inserts, and batch-loads rows through the MariaDB Connector/Node.js pool.</td><td><a href="https://github.com/mariadb-developers/nodejs-quickstart">nodejs-quickstart</a></td></tr><tr><td><strong>Java Quickstart</strong></td><td>A GitHub repository with JDBC, JPA, Spring Boot, Jakarta EE, and Quarkus samples on MariaDB Connector/J.</td><td><a href="https://github.com/mariadb-developers/java-quickstart">java-quickstart</a></td></tr></tbody></table>
