---
description: >-
  MariaDB Exa limitations: architecture and query-flow constraints, datatype
  mapping gaps in MaxScale CDC, SQL-dialect gaps in the SQLglot preprocessor,
  and the CDC primary-key requirement.
hidden: true
noIndex: true
icon: road-barrier
---

# Limitations

While MariaDB Exa (powered by Exasol) provides exceptional performance for analytical workloads, there are functional and operational limitations regarding architecture, datatype mapping, and SQL dialect compatibility. Data is kept in sync automatically, and most queries and schemas work without changes. This page covers the differences to plan for.

**At a glance**

* **Data types:** Most common types replicate as-is or with a straightforward mapping. A few, such as binary types, are replicated as `NULL`. See [Datatype Compatibility](#ii.-datatype-compatibility-matrix).
* **Schema:** A primary key is recommended on every replicated table. Triggers, stored procedures, and some clauses are not carried over. See [Schema and Replication](#i.-schema-and-replication-management).
* **SQL:** Analytical queries are translated automatically from MariaDB to Exasol syntax. Some functions, subquery shapes, and `NULL` and empty-string behaviors differ. See [SQL Syntax Differences](#iv.-sql-syntax-differences) and [Known Errors](#viii.-known-errors).

## I. Schema and Replication Management

Exasol is kept in sync with MariaDB by MaxScale CDC (binlogrouter), which reads the MariaDB binary log and applies DDL and DML changes to Exasol in the background over the Exasol ODBC driver. This is a raw data stream that bypasses the SQL translation layer, so the behaviors below come from how CDC maps types and applies changes, not from SQL rewriting.

### Primary Key

A primary key is strongly recommended for every table captured by CDC. Tables without one are still replicated, but MaxScale CDC synthesizes a key from all columns for its `MERGE`-based upsert into Exasol — which is slower and can behave incorrectly when rows are not unique.

### Schema Feature Differences

| **MariaDB feature**                     | **Behavior in Exa**                                                                                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AUTO_INCREMENT`, `SERIAL`              | Becomes a plain `DECIMAL` column, not an `IDENTITY` column. The generated values replicate from MariaDB.                                             |
| `COLLATE`                               | Not supported in Exasol, but data replicates. Comparisons on Exasol are case-sensitive.                                                              |
| `ON UPDATE CURRENT_TIMESTAMP`           | Not supported in Exasol, but updated values still replicate.                                                                                         |
| `ON UPDATE CASCADE`, `ON DELETE CASCADE` | Not supported in Exasol, and cascaded changes to child rows are not replicated.                                                                     |
| Stored procedures, stored functions     | Not replicated to Exasol, but their effects on table data are. Analytical queries can't call them; equivalent logic can be rebuilt as Exasol UDFs.   |
| Triggers                                | Not replicated to Exasol, but their effects on table data are.                                                                                       |
| `LATIN1` character set                  | Not supported. Exasol supports only UTF8 and ASCII.                                                                                                  |

## II. Datatype Compatibility Matrix

As of MaxScale 25.10, compatibility is tiered based on the level of automated support provided between the engines.

| **Compatibility Tier** | **Data Types**                                                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Native Compatible      | `INT`, `BIGINT`, `SMALLINT`, `DECIMAL`, `NUMERIC`, `DOUBLE`, `CHAR`, `VARCHAR`, `DATE`, `TIMESTAMP`                           |
| Rewrite Compatible     | `TEXT`, `BOOLEAN`, `TINYINT(1)`, `FLOAT`, `DATETIME`, `TIME`, `JSON`, `ENUM`, `SET`, `BIT`                                    |
| Replicated as NULL     | `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB`, `BINARY`, `VARBINARY`, `UUID`, `INET6`, `Spatial types` (Geometry, Point, etc.) |

<details>

<summary>Detailed schema mapping: MariaDB to Exasol</summary>

The following details how MariaDB types are created in Exasol during automated schema replication.

| **MariaDB Data type**                         | **Exasol Actual**  | **Comment**                                             |
| --------------------------------------------- | ------------------ | ------------------------------------------------------- |
| `INT`                                         | `DECIMAL(10,0)`    | ✅                                                       |
| `BIGINT`                                      | `DECIMAL(20,0)`    | ✅                                                       |
| `SMALLINT`                                    | `DECIMAL(5,0)`     | ✅                                                       |
| `MEDIUMINT`                                   | `DECIMAL(8,0)`     | ✅                                                       |
| `SERIAL`                                      | `DECIMAL(20,0)`    | ✅                                                       |
| `INT UNSIGNED`                                | `DECIMAL(10,0)`    | ✅                                                       |
| `DECIMAL(10,4)`                               | `DECIMAL(10,4)`    | ✅                                                       |
| `NUMERIC(15,2)`                               | `DECIMAL(15,2)`    | ✅                                                       |
| `FLOAT`                                       | `DOUBLE`           | ✅                                                       |
| `DOUBLE`, `DOUBLE PRECISION`, `REAL`          | `DOUBLE`           | ✅                                                       |
| `TINYINT(1)`                                  | `DECIMAL(3,0)`     | ✅                                                       |
| `BOOLEAN`                                     | `DECIMAL(3,0)`     | ✅                                                       |
| `BIT`                                         | `DECIMAL(20,0)`    | ✅                                                       |
| `CHAR(10)`                                    | `CHAR(40)`         | ✅ Length is 4×                                          |
| `VARCHAR(255)`                                | `VARCHAR(1020)`    | ✅ Length is 4×                                          |
| `NCHAR(12)`                                   | `CHAR(36)`         | ✅ Length is 3×                                          |
| `NVARCHAR(200)`                               | `VARCHAR(600)`     | ✅ Length is 3×                                          |
| `ENUM('A','B','C')`                           | `VARCHAR(1)`       | ✅ Sized to the longest value                            |
| `SET('X','Y','Z')`                            | `VARCHAR(5)`       | ✅ Sized to the longest combination                      |
| `JSON`                                        | `VARCHAR(2000000)` | ✅                                                       |
| `TINYTEXT`                                    | `VARCHAR(256)`     | ✅                                                       |
| `TEXT`                                        | `VARCHAR(2000000)` | ✅                                                       |
| `MEDIUMTEXT`                                  | `VARCHAR(16536)`   | ✅                                                       |
| `LONGTEXT`                                    | `VARCHAR(2000000)` | ✅                                                       |
| `TINYBLOB`                                    | `VARCHAR(256)`     | ⚠️ CDC inserts `NULL`                                   |
| `BLOB`                                        | `VARCHAR(2000000)` | ⚠️ CDC inserts `NULL`                                   |
| `MEDIUMBLOB`                                  | `VARCHAR(16536)`   | ⚠️ CDC inserts `NULL`                                   |
| `LONGBLOB`                                    | `VARCHAR(2000000)` | ⚠️ CDC inserts `NULL`                                   |
| `VARBINARY(255)`                              | `VARCHAR(255)`     | ⚠️ CDC inserts `NULL`                                   |
| `BINARY(16)`                                  | `CHAR(16)`         | ⚠️ CDC inserts `NULL`                                   |
| `DATE`                                        | `DATE`             | ✅                                                       |
| `DATETIME`, `TIMESTAMP`                       | `TIMESTAMP(0)`     | ✅                                                       |
| `DATETIME(6)`, `TIMESTAMP(6)`, `TIME(6)`      | `TIMESTAMP(6)`     | ✅                                                       |
| `TIME`                                        | `TIMESTAMP(0)`     | ⚠️ Stored as a timestamp on 1970-01-01                  |
| `YEAR(4)`                                     | `DECIMAL(4,0)`     | ✅                                                       |
| `INET6`                                       | `CHAR(16)`         | ⚠️ CDC inserts `NULL`                                   |
| `UUID`                                        | `CHAR(16)`         | ⚠️ CDC inserts `NULL`                                   |
| `GEOMETRY`, `POINT`                           | `GEOMETRY`         | ⚠️ CDC inserts `NULL`                                   |

In MaxScale 25.10, `CHAR` and `VARCHAR` lengths are carried over in bytes rather than characters, so a `utf8mb4` column is created four times wider in Exasol and a `utf8mb3` column three times wider.

</details>

<details>

<summary>Data value replication results: precision and formatting differences on INSERT</summary>

Precision shifts and engine-specific behaviors during transfer.

| **Data Type**      | **MariaDB Value**          | **Exasol Value**               | **Comment**                            |
| ------------------ | -------------------------- | ------------------------------ | -------------------------------------- |
| `INT`              | `42`                       | `42`                           | ✅                                      |
| `SMALLINT`         | `32767`                    | `32767`                        | ✅                                      |
| `MEDIUMINT`        | `8388607`                  | `8388607`                      | ✅                                      |
| `INT UNSIGNED`     | `3000000000`               | `3000000000`                   | ✅                                      |
| `BIGINT`           | `9223372036854775807`      | `9223372036854775807`          | ✅                                      |
| `DECIMAL(10, 4)`   | `1234.5678`                | `1234.5678`                    | ✅                                      |
| `NUMERIC(15, 2)`   | `99999.99`                 | `99999.99`                     | ✅                                      |
| `FLOAT`            | `3.14159`                  | `3.14159`                      | ✅ See the note below                   |
| `DOUBLE`           | `2.718281828459`           | `2.718281828459`               | ✅ See the note below                   |
| `DOUBLE PRECISION` | `123456.7890123`           | `123456.7890123`               | ✅ See the note below                   |
| `REAL`             | `-9876.54321`              | `-9876.54321`                  | ✅ See the note below                   |
| `TINYINT(1)`       | `1`                        | `1`                            | ✅                                      |
| `BOOLEAN`          | `1`                        | `1`                            | ✅                                      |
| `CHAR(10)`         | `'test'` (len=4)           | `'test '` (len=40)             | ⚠️ Right-padded with spaces             |
| `VARCHAR(255)`     | `'Hello World...'`(len=14) | `'Hello World...'`(len=14)     | ✅                                      |
| `NCHAR(12)`        | `'Привет'` (len=6)         | `'Привет'` (len=36)            | ⚠️ Right-padded with spaces             |
| `NVARCHAR(200)`    | `'Extended Unicode...'`    | `'Extended Unicode...'`        | ✅                                      |
| `DATE`             | `2023-10-25`               | `2023-10-25`                   | ✅                                      |
| `TIMESTAMP`        | `... 14:30:00`             | `... 14:30:00`                 | ✅                                      |
| `DATETIME`         | `... 14:30:00`             | `... 14:30:00`                 | ✅                                      |
| `DATETIME(6)`      | `... 14:30:00.123456`      | `... 14:30:00.123456`          | ✅                                      |
| `TIME`             | `14:30:00`                 | `1970-01-01 14:30:00`          | ⚠️ Stored as a timestamp on 1970-01-01 |
| `TIME(6)`          | `14:30:00.987654`          | `1970-01-01 14:30:00.987654`   | ⚠️ Stored as a timestamp on 1970-01-01 |
| `TIMESTAMP(6)`     | `... 14:30:00.555555`      | `... 14:30:00.555555`          | ✅                                      |
| `YEAR(4)`          | `2024`                     | `2024`                         | ✅                                      |
| `JSON`             | `{"key": "value"}`         | `{"key": "value"}`             | ✅                                      |
| `TINYTEXT`         | `'tiny text data'`         | `'tiny text data'`             | ✅                                      |
| `MEDIUMTEXT`       | `'medium text data'`       | `'medium text data'`           | ✅                                      |
| `TEXT`             | `'standard text data'`     | `'standard text data'`         | ✅                                      |
| `LONGTEXT`         | `'long text data'`         | `'long text data'`             | ✅                                      |

Floating-point values are stored exactly. Some Exasol clients display `DOUBLE` values with only six decimal places, so compare stored values rather than displayed ones.

</details>

## III. Semantic Logic and NULL Behavior

Read-only queries are routed by MaxScale SmartRouter to either MariaDB or Exasol, based on learned performance. Queries sent to Exasol pass through the ExasolRouter, where the SQLglot preprocessor translates MariaDB SQL into Exasol's dialect in real time. Translation covers most syntax, but the two engines still behave differently in the cases below.

### 1. Comparison & Logic Tests

In Exasol, `NULL` represents an undefined value rather than a special value, which leads to discrepancies in comparison and sorting. The following results are from queries sent through the ExasolRouter as of MaxScale 25.10.

| **Query**                 | **Result MariaDB** | **Result Exasol**  | **Comment**                                                     |
| ------------------------- | ------------------ | ------------------ | --------------------------------------------------------------- |
| `SELECT NULL = NULL;`     | `NULL`             | `NULL`             | ✅                                                               |
| `SELECT 99 = NULL;`       | `NULL`             | `NULL`             | ✅                                                               |
| `SELECT IFNULL(1,0);`     | `1`                | `1`                | ✅ Column header becomes `COALESCE(1,0)`                         |
| `SELECT IFNULL(NULL,10);` | `10`               | `10`               | ✅ Column header becomes `COALESCE(NULL,10)`                     |
| `SELECT NULLIF(1,1);`     | `NULL`             | `NULL`             | ✅                                                               |
| `SELECT NULLIF(1,2);`     | `1`                | `1`                | ✅                                                               |
| `SELECT COALESCE(N,N,1);` | `1`                | `1`                | ✅                                                               |
| `SELECT 99 <=> NULL;`     | `0`                | ❌ Error            | ❌ Exasol returns `Feature not supported: distinct predicate`    |
| `SELECT ISNULL(1);`       | `0`                | `0`                | ✅ Column header becomes `1 IS NULL`                             |
| `SELECT SUM(x) FROM t;`   | `10`               | `10`               | ✅ Column header becomes `SUM(T.X)`                              |
| `SELECT AVG(x) FROM t;`   | `2.75`             | `2.75`             | ✅ Column header becomes `AVG(T.X)`                              |
| `SELECT COUNT(x) FROM t;` | `2`                | `2`                | ✅ Column header becomes `COUNT(T.X)`                            |
| `ORDER BY x` (ASC)        | `NULL`s come first | `NULL`s come first | ✅                                                               |
| `ORDER BY x` (DESC)       | `NULL`s come last  | `NULL`s come first | ❌ Opposite default sorting                                      |

### 2. Empty Strings vs. NULL

Exasol interprets an empty string (`''`) as a `NULL` value. To get the same behavior in MariaDB, enable the `EMPTY_STRING_IS_NULL` SQL mode. Setting `sql_mode=ORACLE` alone does not change how empty strings are handled.

| **Query**            | **MariaDB (`EMPTY_STRING_IS_NULL`)** | **MariaDB (Standard)** | **Result Exasol Behavior**           |
| -------------------- | ------------------------------------ | ---------------------- | ------------------------------------ |
| `SELECT '';`         | `NULL`                               | `''`                   | `NULL`                               |
| `SELECT '' IS NULL;` | `1`                                  | `0`                    | `1`                                  |
| `CHAR_LENGTH('');`   | `NULL`                               | `0`                    | `NULL` (evaluated as `LENGTH(NULL)`) |

* Workaround: Use `SET sql_mode = 'EMPTY_STRING_IS_NULL';` in MariaDB.

## IV. SQL Syntax Differences

### Reserved Words

Exasol reserves over 460 keywords. Common words like `schema`, `hour`, and `year` must be quoted with double quotes (`"column"`) — not backticks.

### Default Database

The ExasolRouter does not apply the database named when the client connects. Unqualified table names then fail with an `object ... not found` error. Run `USE <database>;` after connecting, or qualify table names with the database name.

### Session Variables

User variables (`SET @x := 5`) and `SELECT ... INTO @var` are not supported on the analytical path. `SET` statements sent to Exasol are accepted but ignored, with no error, so a later query that references the variable fails with a syntax error.

Use literal values, a subquery, or a CTE instead:

```sql
-- Not supported
SET @a = 7;
SELECT @a;

SELECT 1, 2 INTO @a, @b FROM dual;

-- Instead
WITH v AS (SELECT 7 AS a) SELECT a FROM v;
```

`DEFINE` is a client-side EXAplus command, not SQL, and does not work through the ExasolRouter.

### Subqueries in the SELECT List

Correlated subqueries in the `SELECT` list, such as `(SELECT SUM(s.fare) FROM seats s WHERE s.order_id = o.order_id)`, generally work on the analytical path. The following cases fail.

#### Column Names That Match an Earlier Alias

If a subquery uses an unqualified column whose name matches an alias defined earlier in the same `SELECT` list, the SQL translation rewrites that column as a reference to the alias. Exasol then rejects the query with `invalid select-list in subselect`.

Qualify columns inside the subquery with a table alias, or rename the outer alias:

```sql
-- Fails: fare inside the subquery is treated as the outer alias "fare"
SELECT o.order_id AS fare,
       (SELECT SUM(fare) FROM seats WHERE o.order_id = order_id) AS total
FROM orders o;

-- Works: the inner column is qualified
SELECT o.order_id AS fare,
       (SELECT SUM(s.fare) FROM seats s WHERE s.order_id = o.order_id) AS total
FROM orders o;
```

#### SELECT DISTINCT With a Correlated Subquery

`SELECT DISTINCT` combined with a correlated subquery in the `SELECT` list fails with `Feature not supported: this kind of correlated subselect`. Apply `DISTINCT` to a derived table instead, or use `GROUP BY`:

```sql
-- Fails
SELECT DISTINCT o.order_id,
       (SELECT SUM(s.fare) FROM seats s WHERE s.order_id = o.order_id) AS total
FROM orders o;

-- Works
SELECT DISTINCT *
FROM (SELECT o.order_id,
             (SELECT SUM(s.fare) FROM seats s WHERE s.order_id = o.order_id) AS total
      FROM orders o) AS t;
```

#### LIMIT in a Correlated Subquery

Exasol does not allow `LIMIT` within correlated subqueries. On the analytical path, a subquery such as `ORDER BY ... LIMIT 1` works while it matches at most one row, and fails with `single-row subquery returns more than one row` as soon as it matches more. Because it depends on the data, the query can pass testing and fail later. Use an aggregate instead:

```sql
-- Fails when an order has more than one seat
SELECT o.order_id,
       (SELECT s.fare FROM seats s WHERE s.order_id = o.order_id
        ORDER BY s.fare LIMIT 1) AS lowest_fare
FROM orders o;

-- Works
SELECT o.order_id,
       (SELECT MIN(s.fare) FROM seats s WHERE s.order_id = o.order_id) AS lowest_fare
FROM orders o;
```

### GROUP_CONCAT Ordering

`GROUP_CONCAT` is translated to Exasol's `LISTAGG`. Without an explicit order, the order of the concatenated values can differ from MariaDB's. An `ORDER BY` placed on the subquery, outside the function, does not set the order of the list either.

## V. Functional Compatibility Matrix

The analytical path uses SQLglot to bridge MariaDB and Exasol dialects.

{% hint style="warning" %}
The function tables in this section were captured during earlier MariaDB Exa testing and are pending re-validation against MaxScale 25.10. Treat specific failure modes as indicative rather than authoritative.
{% endhint %}

<details>

<summary>Math functions and their Exasol equivalents</summary>

| **MariaDB Function** | **Exasol Function**  | **SQLglot preprocessor** | **Comment**                       |
| -------------------- | -------------------- | ------------------------ | --------------------------------- |
| `ABS`                | `ABS`                | —                        | ✅                                 |
| `CEIL` / `CEILING`   | `CEIL`               | —                        | ✅                                 |
| `FLOOR`              | `FLOOR`              | —                        | ✅                                 |
| `ROUND`              | `ROUND`              | —                        | ✅                                 |
| `SIGN`               | `SIGN`               | —                        | ✅                                 |
| `TRUNCATE`           | `TRUNC`              | —                        | Successfully renamed              |
| `MOD`                | `MOD`                | —                        | ✅                                 |
| `DIV`                | `TRUNC(a / b)`       | ❌                        | Passes `DIV` as-is; Exasol fails  |
| `CONV`               | —                    | 🛑                       | Native missing in Exasol          |
| `OCT`                | —                    | 🛑                       | Native missing in Exasol          |
| `CRC32 / CRC32C`     | —                    | 🛑                       | Native missing in Exasol          |
| `EXP`, `LN`, `LOG10` | `EXP`, `LN`, `LOG10` | —                        | Precision formatting differs      |
| `LOG`                | `LOG / LN`           | —                        | ✅                                 |
| `LOG2`               | `LOG(2, x)`          | —                        | ✅                                 |
| `POW`                | `POWER`              | ❌                        | Misses alias; passes `POW`        |
| `POWER`              | `POWER`              | ❌                        | Test mismatch: Int vs Float       |
| `SQRT`, `PI`         | `SQRT`, `PI`         | —                        | ✅                                 |
| `SIN`, `COS`, `TAN`  | `SIN`, `COS`, `TAN`  | —                        | ✅                                 |
| `ATAN2`              | `ATAN2`              | —                        | Exasol throws exception for (0,0) |
| `DEGREES`, `RADIANS` | `DEGREES`, `RADIANS` | —                        | ✅                                 |

</details>

<details>

<summary>String functions and their Exasol equivalents</summary>

| **MariaDB Function** | **Exasol Function** | **SQLglot preprocessor** | **Comment**                       |
| -------------------- | ------------------- | ------------------------ | --------------------------------- |
| `BIT_LENGTH`         | `BIT_LENGTH`        | —                        | ✅                                 |
| `CHAR_LENGTH`        | `CHARACTER_LENGTH`  | —                        | Successfully renamed              |
| `LENGTH`             | `LENGTH`            | —                        | ✅                                 |
| `INSTR`              | `INSTR`             | —                        | ✅                                 |
| `LOWER` / `LCASE`    | `LOWER`             | —                        | ✅                                 |
| `UPPER` / `UCASE`    | `UPPER`             | —                        | ✅                                 |
| `LEFT`, `RIGHT`      | `LEFT`, `RIGHT`     | —                        | ✅                                 |
| `MID`, `SUBSTR`      | `SUBSTR`            | —                        | ✅                                 |
| `INSERT`, `REPLACE`  | `INSERT`, `REPLACE` | —                        | ✅                                 |
| `SUBSTRING_INDEX`    | —                   | 🛑                       | Function not found                |
| `CONCAT`             | `CONCAT / \|\|`     | ❌                        | Data mismatch (NULL handling)     |
| `CONCAT_WS`          | —                   | 🛑                       | Function not found                |
| `SPACE`              | `SPACE`             | ❌                        | Data exception (strict typing)    |
| `ASCII`              | `ASCII`             | ❌                        | Data exception (right truncation) |
| `ORD`, `BIN`, `HEX`  | —                   | 🛑                       | Function not found                |
| `FORMAT`             | `TO_CHAR`           | ❌                        | Syntax error (unexpected keyword) |
| `STRCMP`             | `CASE WHEN...`      | ❌                        | Function not found                |
| `FIELD`, `ELT`       | `DECODE / CASE`     | ❌                        | Function not found                |
| `SOUNDEX`            | `SOUNDEX`           | ❌                        | Data mismatch (NULL behavior)     |
| `REGEXP`, `RLIKE`    | `REGEXP_LIKE`       | ❌                        | Syntax error (not translated)     |
| `UPDATEXML`          | —                   | 🛑                       | Function not found (XML missing)  |

</details>

<details>

<summary>Date and time functions and their Exasol equivalents</summary>

| **MariaDB Function**   | **Exasol Analog**      | **SQLglot preprocessor** | **Comment**                            |
| ---------------------- | ---------------------- | ------------------------ | -------------------------------------- |
| `CURDATE`              | `CURRENT_DATE`         | —                        | ✅                                      |
| `CURRENT_TIME`         | `CURRENT_TIMESTAMP`    | ❌                        | Not supported (Exasol lacks TIME type) |
| `CURTIME`              | `CURRENT_TIMESTAMP`    | —                        | ❌ Function not found                   |
| `NOW`, `SYSDATE`       | `CURRENT_TIMESTAMP`    | —                        | ❌ Syntax error (`DATE_` wrapper)       |
| `UTC_DATE`             | `CURRENT_DATE`         | —                        | 🛑 Function not found                  |
| `DATE`, `TIME`         | `CAST(...)`            | —                        | ❌ Syntax error (unexpected keyword)    |
| `DAY`, `MONTH`, `YEAR` | `DAY`, `MONTH`, `YEAR` | —                        | ✅                                      |
| `SECOND`               | `SECOND`               | —                        | ❌ Data mismatch (fractional vs int)    |
| `WEEK`                 | `WEEK`                 | —                        | ❌ Argument count mismatch (2 vs 1)     |
| `MAKEDATE`             | —                      | —                        | 🛑 Function not found                  |
| `CONVERT_TZ`           | `CONVERT_TZ`           | —                        | ❌ Data mismatch (.000000 added)        |

</details>

<details>

<summary>Aggregate, logic, and system functions and their Exasol equivalents</summary>

| **MariaDB Function** | **Exasol Function** | **Comment**                               |
| -------------------- | ------------------- | ----------------------------------------- |
| `COUNT, SUM, AVG`    | `COUNT, SUM, AVG`   | ✅                                         |
| `MIN, MAX`           | `MIN, MAX`          | Max has typing differences (Float vs Int) |
| `GROUP_CONCAT`       | `GROUP_CONCAT`      | ✅                                         |
| `BIT_AND / OR / XOR` | —                   | 🛑 Aggregate vs Scalar logic mismatch     |
| `CAST`, `COALESCE`   | `CAST`, `COALESCE`  | ✅                                         |
| `IFNULL`             | `NVL`               | Different names                           |
| `ISNULL`             | —                   | Use `IS NULL` syntax                      |
| `JSON_VALUE()`       | `JSON_VALUE`        | ✅                                         |
| `JSON_EXTRACT`       | `JSON_EXTRACT`      | Syntax differs                            |
| `DATABASE()`         | `CURRENT_SCHEMA`    | Different name                            |
| `CONNECTION_ID()`    | `CURRENT_SESSION`   | Different name                            |

</details>

## VI. Data Import and Null Handling

### NULL Conversions

MariaDB writes `NULL` as `\N` in export files. Importing such a file directly into Exasol with `IMPORT` fails on `TIMESTAMP` columns, so replace `\N` with an empty value or `NULL` first. Loading through MariaDB and CDC needs no conversion, because `NULL` values replicate correctly.

### Empty Strings

Exasol treats an empty string (`''`) as `NULL`. The ExasolRouter rewrites the literal `''` to `NULL`, and empty strings in `VARCHAR` and `TEXT` columns arrive as `NULL` through CDC. As a result, `CHAR_LENGTH('')` returns `NULL` rather than `0`.

### Load Data

`LOAD DATA [LOCAL] INFILE` fails through the ExasolRouter with a syntax error. Load into MariaDB directly, and CDC replicates the rows to Exasol.

### Formatting & Output Trade-offs

* Implicit Aliasing: MariaDB preserves the original query string (e.g., `SUM(x)`), while Exasol generates internal aliases (e.g., `SUM(T.X)`).
* Decimal Precision: Results through the ExasolRouter often have trailing zeros trimmed (e.g., `5` vs `5.0000`). Stored values are unchanged.

### Case Sensitivity

* Identifiers: table, column, and schema names are matched case-insensitively (`SQL_IDENTIFIER_COMPARISON = IGNORE CASE`).
* String data: comparisons are case-sensitive. `WHERE col = 'abc'` does not match `'ABC'`, even for columns that used a case-insensitive collation in MariaDB. Use `UPPER()` or `LOWER()` on both sides to match MariaDB.

## VII. How It Works: Architecture & Query Flow

MariaDB Exa uses a Hybrid Transactional and Analytical Processing (HTAP) architecture to deliver transactional consistency alongside high-performance analytics.

### 1. The Analytical Path (Read)

* MaxScale SmartRouter: Acts as the intelligent entry point for client applications. It identifies read-only queries and routes them to either the MariaDB cluster or the analytical environment based on learned performance metrics.
* ExasolRouter (MariaDB Exa Router): When analytical routing is selected, the query is passed to this specialized router. It hosts the SQLglot Preprocessor.
* SQLglot Preprocessor: Automatically transpiles MariaDB-specific SQL dialect into Exasol-compatible dialect in real-time.

### 2. The Replication Path (Write)

* MaxScale CDC (binlogrouter): Manages background synchronization of DDL and DML changes from the MariaDB Binary Log directly to Exasol over the Exasol ODBC driver.
* Direct Sync: This pathway is a raw data stream and does not utilize the SQLglot preprocessor.

## VIII. Known Errors

Errors you may see when running queries through MariaDB Exa, with their causes and workarounds. The same error number can appear for different Exasol errors, so match on the message text.

| **Error message**                                               | **Cause**                                                                                   | **Workaround**                                                                                          |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `invalid select-list in subselect`                              | A column inside a subquery has the same name as an earlier alias in the `SELECT` list.      | Qualify the column. See [Column Names That Match an Earlier Alias](#column-names-that-match-an-earlier-alias). |
| `Feature not supported: this kind of correlated subselect`     | `SELECT DISTINCT` with a correlated subquery in the `SELECT` list.                          | Apply `DISTINCT` to a derived table, or use `GROUP BY`. See [SELECT DISTINCT With a Correlated Subquery](#select-distinct-with-a-correlated-subquery). |
| `single-row subquery returns more than one row`                 | `LIMIT` in a correlated subquery that matches more than one row.                            | Use an aggregate such as `MIN()`. See [LIMIT in a Correlated Subquery](#limit-in-a-correlated-subquery). |
| `object ... not found`                                          | The table name is unqualified and no default database is set.                               | Run `USE <database>;` or qualify the table name. See [Default Database](#default-database).             |
| `Feature not supported: distinct predicate`                     | The `<=>` operator.                                                                         | Rewrite the comparison, for example as `(a = b OR (a IS NULL AND b IS NULL))`.                           |
