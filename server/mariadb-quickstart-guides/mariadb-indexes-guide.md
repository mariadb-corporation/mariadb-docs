---
description: Indexing Guide
---

# Getting Started with Indexes Guide

This guide explains the different types of indexes in MariaDB, their characteristics, and how they are used. Learn to create and manage Primary Keys, Unique Indexes, and Plain Indexes, along with key considerations for choosing and maintaining effective indexes for optimal query performance.

In MariaDB, the terms `KEY` and `INDEX` are generally used interchangeably in SQL statements.

### Index Types Overview

There are four main kinds of indexes:

* **Primary Keys:** Unique and not NULL.
* **Unique Indexes:** Must be unique but can contain NULL values.
* **Plain Indexes (or Regular Indexes):** Not necessarily unique.
* **Full-Text Indexes:** Used for full-text searching capabilities.

### Primary Key

A primary key uniquely identifies each record in a table. Its values must be unique, and it cannot contain `NULL` values. Each table can have only one primary key.

**InnoDB Considerations:**

* In InnoDB tables, the primary key is included as a suffix in all other indexes. Therefore, keeping the primary key compact (e.g., using an appropriate integer type) is important for performance and storage efficiency.
* If a table has no explicitly defined primary key and no `UNIQUE` indexes, InnoDB automatically creates an invisible 6-byte clustered index.

**Using `AUTO_INCREMENT`:** The `AUTO_INCREMENT` attribute is commonly used with numeric primary keys to automatically generate a unique ID for each new row.

```sql
CREATE TABLE `Employees` (
  `ID` TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `First_Name` VARCHAR(25) NOT NULL,
  `Last_Name` VARCHAR(25) NOT NULL,
  `Position` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`ID`)
);
```

Note: The column defined as a primary key (or part of it) must be explicitly declared as `NOT NULL`.

**Adding a Primary Key to an Existing Table:** Use `ALTER TABLE`. You cannot create a primary key with `CREATE INDEX`.

```sql
ALTER TABLE Employees ADD PRIMARY KEY(ID);
```

**Finding Tables Without Primary Keys:** This query uses the `information_schema` database to find tables lacking primary keys:

```sql
SELECT t.TABLE_SCHEMA, t.TABLE_NAME
FROM information_schema.TABLES AS t
LEFT JOIN information_schema.KEY_COLUMN_USAGE AS c
ON t.TABLE_SCHEMA = c.CONSTRAINT_SCHEMA
   AND t.TABLE_NAME = c.TABLE_NAME
   AND c.CONSTRAINT_NAME = 'PRIMARY'
WHERE t.TABLE_SCHEMA NOT IN ('information_schema', 'performance_schema', 'mysql', 'sys')
  AND c.CONSTRAINT_NAME IS NULL;
```

### Unique Index

A unique index ensures that all values in the indexed column (or combination of columns) are unique. However, unlike a primary key, columns in a unique index can store `NULL` values. 

Each key value uniquely identifies a row, but not every row needs to be represented if `NULL`s are allowed.

```python
### INSERT INTO `securedb`.`t_long_keys`
### SET
###   @1=1 /* INT meta=0 nullable=0 is_null=0 */
###   @2='a' /* VARSTRING(4073) meta=4073 nullable=1 is_null=0 */
###   @3=580 /* LONGINT meta=0 nullable=1 is_null=0 */
```

**Behavior (MariaDB 10.5+):**

* If the index type is not specified, `UNIQUE` typically creates a BTREE index, usable by the optimizer.
* If a key exceeds the maximum length for the storage engine and the engine supports long unique indexes, a HASH key might be created to enforce uniqueness.

**Creating Unique Indexes:** During table creation:

```sql
CREATE TABLE `Employees` (
  `ID` TINYINT(3) UNSIGNED NOT NULL,
  `Employee_Code` VARCHAR(25) NOT NULL,
  `First_Name` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UK_EmpCode` (`Employee_Code`) -- Naming the unique key is good practice
);
```

After table creation using `ALTER TABLE`:

```sql
ALTER TABLE Employees ADD UNIQUE `UK_HomePhone` (`Home_Phone`);
```

After table creation using `CREATE UNIQUE INDEX`:

```sql
CREATE UNIQUE INDEX `IX_Position` ON Employees(Position);
```

**Multi-Column Unique Indexes:** An index can span multiple columns. MariaDB can use the leftmost part(s) of such an index if it cannot use the whole index (except for HASH indexes).

```sql
CREATE TABLE t1 (a INT NOT NULL, b INT, UNIQUE (a,b));
INSERT INTO t1 VALUES (1,1), (2,2);
INSERT INTO t1 VALUES (2,1); -- Valid: (2,1) is unique, though '2' in 'a' and '1' in 'b' are not individually unique here.
SELECT * FROM t1;
```

```
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    1 |
| 2 |    2 |
+---+------+
```

**`NULL` Values in Unique Indexes:** A `UNIQUE` constraint allows multiple `NULL` values because in SQL, `NULL` is never equal to another `NULL`.

```sql
INSERT INTO t1 VALUES (3,NULL), (3, NULL); -- Both rows are inserted
SELECT * FROM t1;
```

```
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    1 |
| 2 |    2 |
| 3 | NULL |
| 3 | NULL |
+---+------+
```

Verification:

```sql
SELECT (3, NULL) = (3, NULL);
```

```
+-----------------------+
| (3, NULL) = (3, NULL) |
+-----------------------+
|                     0 | -- 0 means false
+-----------------------+
```

**Conditional Uniqueness with Virtual Columns:** You can enforce uniqueness over a subset of rows using unique indexes on [virtual columns](../reference/sql-statements/data-definition/create/generated-columns.md). This example ensures `user_name` is unique for 'Active' or 'On-Hold' users, but allows duplicate names for 'Deleted' users:

```sql
CREATE TABLE Table_1 (
  user_name VARCHAR(10),
  status ENUM('Active', 'On-Hold', 'Deleted'),
  del CHAR(0) AS (IF(status IN ('Active', 'On-Hold'), '', NULL)) PERSISTENT,
  UNIQUE(user_name, del)
);
```

**Trailing Pad Characters:** If a unique index is on a column where trailing pad characters are stripped or ignored (e.g., `CHAR` vs `VARCHAR` behavior), inserts where values differ only by the number of trailing pad characters can result in duplicate-key errors.

**Long Keys and HASH Indexes (MariaDB 10.4+):** For engines like InnoDB, `UNIQUE` can be used with various column types and numbers. If a key's length exceeds the engine's maximum, a HASH key may be created.

```sql
-- Example table definition (simplified for brevity)
CREATE TABLE t_long_keys (
  a INT PRIMARY KEY,
  b BLOB,
  c1 VARCHAR(1000),
  UNIQUE KEY `uk_b` (b),
  UNIQUE KEY `uk_c1` (c1)
) ENGINE=InnoDB;

-- SHOW CREATE TABLE might reveal 'USING HASH' for uk_b or uk_c1 if they exceed length limits
SHOW CREATE TABLE t_long_keys\G
```

Example output snippet showing `USING HASH`:

```sql
...
  UNIQUE KEY `uk_b` (`b`) USING HASH,
...
```

### Plain Indexes (Regular Indexes)

Plain indexes do not enforce uniqueness; they are primarily used to speed up data retrieval.

```sql
CREATE TABLE t2 (a INT NOT NULL, b INT, INDEX `idx_a_b` (a,b));
INSERT INTO t2 VALUES (1,1), (2,2), (2,2); -- Duplicate (2,2) is allowed
SELECT * FROM t2;
```

```
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    2 |
| 2 |    2 |
+---+------+
```

### Full-Text Indexes

Full-text indexes are used for performing full-text searches on text data. For details, see the [Full-Text Indexes](../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) documentation.

### Choosing Indexes

* **Index for Queries:** Add indexes that match the `WHERE` clauses, `JOIN` conditions, and `ORDER BY` clauses of your application's queries.
* **Avoid Over-Indexing:** Extra indexes consume storage and can slow down `INSERT`, `UPDATE`, and `DELETE` operations.
* **Impact of Table Size:** Indexes provide more significant speed-ups on large tables (larger than buffer sizes) than on very small tables.
* **Use `EXPLAIN`:** Analyze your queries with the `EXPLAIN` statement to determine if indexes are being used effectively and identify columns that might benefit from indexing.
* **`LIKE '%word%'`:** Queries using a leading wildcard in a `LIKE` clause (e.g., `LIKE '%word%'`) typically cannot use standard BTREE indexes effectively and may result in full table scans unless a full-text index is used.
* **Delayed Writes:** For tables with many reads and writes, consider storage engine options or server configurations related to delayed writes to potentially improve performance by batching disk I/O. (This is an advanced topic.)
* **Creating Indexes on Existing Tables:** Use `CREATE INDEX index_name ON table_name (column_list);`
* **Large Tables:** For very large tables, it's often faster to load data into the table first and then create indexes, rather than creating indexes on an empty table and then loading data.

### Viewing Indexes

*   **`SHOW INDEX FROM table_name;`**: Displays information about all indexes on a table.SQL

    ```sql
    SHOW INDEX FROM Employees;
    ```
*   **`SHOW CREATE TABLE table_name;`**: Shows the `CREATE TABLE` statement, which includes definitions for all indexes.SQL

    ```sql
    SHOW CREATE TABLE Employees\G
    ```

### When to Remove an Index

Remove an index if:

* It is rarely or never used. Unused indexes still incur overhead during data modification operations.
* **Identifying Unused Indexes:**
  * If [user statistics](../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) are enabled, query the `information_schema.INDEX_STATISTICS` table.
  * If the [slow query log](../server-management/server-monitoring-logs/slow-query-log/) is enabled and the `log_queries_not_using_indexes` [server system variable](../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) is `ON`, queries performing full table scans will be logged, which can indicate missing or ineffective indexes.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
