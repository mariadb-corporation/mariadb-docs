---
description: >-
  Virtual and stored generated columns in TideSQL, and the pattern for indexing
  JSON paths through stored generated columns.
---

# TideSQL Generated Columns and JSON

## Generated Columns

The engine supports both `VIRTUAL` and `STORED` generated columns. A virtual column is computed on read and never returned from storage. A stored column is computed on write and persisted with the row, so it reads back without recomputation. A virtual column cannot be indexed on this engine, so a generated column you need to index must be `STORED` or `PERSISTENT`, which is the pattern the JSON section below uses.

```sql
CREATE TABLE orders (
  id       INT PRIMARY KEY,
  price    DECIMAL(10,2),
  qty      INT,
  total    DECIMAL(10,2) AS (price * qty) VIRTUAL,
  category VARCHAR(10) AS (CASE WHEN price >= 100 THEN 'premium' ELSE 'standard' END) VIRTUAL
) ENGINE=TIDESDB;

INSERT INTO orders (id, price, qty) VALUES (1, 49.99, 3);
SELECT * FROM orders;   -- total = 149.97, category = 'standard'
```

## JSON

MariaDB's `JSON` type is an alias for a text type, so JSON storage and the JSON functions such as `JSON_VALUE()`, `JSON_EXTRACT()`, `JSON_SET()`, and `JSON_CONTAINS()` work normally on TideSQL tables, evaluated by the server.

For efficient filtering on JSON paths, extract the paths you care about into stored generated columns and index those:

```sql
CREATE TABLE docs (
  id   INT NOT NULL PRIMARY KEY,
  data LONGTEXT,
  name VARCHAR(100) AS (JSON_VALUE(data, '$.name')) PERSISTENT,
  age  INT          AS (JSON_VALUE(data, '$.age'))  PERSISTENT,
  KEY idx_name (name),
  KEY idx_age (age)
) ENGINE=TIDESDB;

INSERT INTO docs (id, data) VALUES
  (1, '{"name":"Alice","age":30,"tags":["admin","dev"]}'),
  (2, '{"name":"Bob","age":25,"tags":["dev"]}');

SELECT * FROM docs WHERE name = 'Alice';   -- uses idx_name
SELECT * FROM docs WHERE age >= 30;        -- uses idx_age
```

This gives engine-native indexing through ordinary secondary indexes while keeping JSON manipulation in standard SQL.

<sub>_This page is licensed: GPLv2_</sub>
