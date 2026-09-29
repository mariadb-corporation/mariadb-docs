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

* **Data types:** Most common types replicate as-is or with a straightforward mapping. A few (binary etc.) are replicated as `NULL`. See [Datatype Compatibility](#ii-datatype-compatibility-matrix).
* **Schema:** A primary key is recommended on every replicated table. Triggers, stored procedures, and some clauses are not carried over. See [Schema & Replication](#i-schema--replication-management).
* **SQL:** Analytical queries are translated automatically from MariaDB to Exasol syntax. Some functions and NULL and empty-string behaviors differ. See [SQL Syntax Differences](#iv-sql-syntax-differences).


## I. Schema & Replication Management

Exasol is kept in sync with MariaDB by MaxScale CDC (binlogrouter), which reads the MariaDB binary log and applies DDL and DML changes to Exasol in the background over the Exasol ODBC driver. This is a raw data stream that bypasses the SQL translation layer, so the behaviors below come from how CDC maps types and applies changes, not from SQL rewriting.

### Primary Key

A primary key is strongly recommended for every table captured by CDC. Tables without one are still replicated, but MaxScale CDC synthesizes a key from all columns for its `MERGE`-based upsert into Exasol — which is slower and can behave incorrectly when rows are not unique.

### Schema Feature Differences

| **MariaDB feature**                 | **Behavior in Exa**                                                                                                                       |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `AUTO_INCREMENT`                    | Becomes an `IDENTITY` column. Values are replicated from MariaDB, so uniqueness is preserved.                                             |
| `COLLATE`                           | Not supported in Exasol, but data replicates. Comparisons on Exasol are case-sensitive though                                               |
| `ON UPDATE CURRENT_TIMESTAMP`       | Not supported in Exasol, but updated values still replicate.                                                                          |
| `ON UPDATE CASCADE / ON DELETE CASCADE`  | Not supported in Exasol and cascaded child changes are NOT replicated.                                                               |
| Stored procedures, stored functions | Not replicated in Exasol, but their effects on table data are. Analytical queries can't call them; equivalent logic can be rebuilt as Exasol UDFs. |
| Triggers                            | Not replicated in Exasol, but their effects on table data are.                                                                                      |
| `LATIN1` character set              | Only UTF8 and ASCII                                                                                                                       |

## II. Datatype Compatibility Matrix

As of MaxScale 25.10.4, compatibility is tiered based on the level of automated support provided between the engines.

| **Compatibility Tier** | **Data Types**                                                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Native Compatible      | `INT`, `BIGINT`, `SMALLINT`, `DECIMAL`, `NUMERIC`, `DOUBLE`, `CHAR`, `VARCHAR`, `DATE`, `TIMESTAMP`                           |
| Rewrite Compatible     | `TEXT`, `BOOLEAN`, `TINYINT(1)`, `FLOAT`, `DATETIME`, `TIME`, `JSON`, `ENUM`, `SET`, `BIT`                                    |
| Replicated as NULL     | `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, `LONGBLOB`, `BINARY`, `VARBINARY`, `UUID`, `INET6`, `Spatial types` (Geometry, Point, etc.) |

<details>

<summary>Detailed schema mapping: MariaDB -> Exasol </summary>

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
| `BLOB`                                        | `VARCHAR(2000000)` | ⚠️ `NULL` for binary bytes; plain ASCII text replicates |
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

</details>

<details>

<summary>Data value replication results: precision and formatting differences on INSERT</summary>

Precision shifts and engine-specific behaviors during transfer.

| **Data Type**      | **MariaDB Value**          | **Exasol Value**           | **Comment**                   |
| ------------------ | -------------------------- | -------------------------- | ----------------------------- |
| `INT`              | `42`                       | `42`                       | ✅                             |
| `SMALLINT`         | `32767`                    | `32767`                    | ✅                             |
| `MEDIUMINT`        | `8388607`                  | `8388607`                  | ✅                             |
| `INT UNSIGNED`     | `3000000000`               | `3000000000`               | ✅                             |
| `BIGINT`           | `9223372036854775807`      | `9223372036854775807`      | ✅                             |
| `DECIMAL(10, 4)`   | `1234.5678`                | `1234,5678`                | ✅                             |
| `NUMERIC(15, 2)`   | `99999.99`                 | `99999,99`                 | ✅                             |
| `FLOAT`            | `3.14159`                  | `3.141590`                 | ⚠️ Precision distortion        |
| `DOUBLE`           | `2.718281828459`           | `2.718282`                 | ⚠️ Precision distortion        |
| `DOUBLE PRECISION` | `123456.7890123`           | `123456.789012`            | ⚠️ Precision distortion        |
| `REAL`             | `-9876.54321`              | `-9876.543210`             | ⚠️ Precision distortion        |
| `TINYINT(1)`       | `1`                        | `1`                        | ✅                             |
| `BOOLEAN`          | `1`                        | `1`                        | ✅                             |
| `CHAR(10)`         | `'test'` (len=4)           | `'test '` (len=40)         | ⚠️ Right-padded with spaces    |
| `VARCHAR(255)`     | `'Hello World...'`(len=14) | `'Hello World...'`(len=14) | ✅                             |
| `NCHAR(12)`        | `'Привет'` (len=6)         | `'Привет'` (len=36)        | ⚠️ Right-padded with spaces    |
| `NVARCHAR(200)`    | `'Extended Unicode...'`    | `'Extended Unicode...'`    | ✅                             |
| `DATE`             | `2023-10-25`               | `2023-10-25`               | ✅                             |
| `TIMESTAMP`        | `... 14:30:00`             | `... 14:30:00.000`         | ✅                             |
| `DATETIME`         | `... 14:30:00`             | `... 14:30:00.000`         | ✅                             |
| `DATETIME(6)`      | `... 14:30:00.123456`      | `... 14:30:00.123456`      | ✅                             |
| `TIME`             | `14:30:00`                 | `1970-01-01 14:30:00`      | ⚠️ Stored with Timestamp on 1970-01-01 |
| `TIME(6)`          | `14:30:00.987654`          | `1970-01-01 14:30:00.987654`| ⚠️ Stored with Timestamp on 1970-01-01  |
| `TIMESTAMP(6)`     | `... 14:30:00.555555`      | `... 14:30:00.555555`      | ✅                             |
| `YEAR(4)`          | `2024`                     | `2024`                     | ✅                             |
| `JSON`             | `{"key": "value"}`         | `{"key": "value"}`         | ✅                             |
| `TINYTEXT`         | `'tiny text data'`         | `'tiny text data'`         | ✅                             |
| `MEDIUMTEXT`       | `'medium text data'`       | `'medium text data'`       | ✅                             |
| `TEXT`             | `'standard text data'`     | `'standard text data'`     | ✅                             |
| `LONGTEXT`         | `'long text data'`         | `'long text data'`         | ✅                             |

</details>

## III. Semantic Logic & NULL Behavior

Read-only queries are routed by MaxScale SmartRouter to either MariaDB or Exasol, based on learned performance. Queries sent to Exasol pass through the ExasolRouter, where the SQLglot preprocessor translates MariaDB SQL into Exasol's dialect in real time. Translation covers most syntax, but the two engines still behave differently in the cases below.

Operational behaviors regarding Undefined values and empty strings differ significantly between the engines.

### 1. Comparison & Logic Tests

In Exasol, `NULL` represents an undefined value rather than a special value, which leads to discrepancies in comparison and sorting.
The following is based on using MariaDB Exa ExasolRouter with sqlglot processing as of MaxScale 25.10.4

| **Query**                 | **Result MariaDB** | **Result Exasol**  | **Comment**                               |
| ------------------------- | ------------------ | ------------------ | ----------------------------------------- |
| `SELECT NULL = NULL;`     | `NULL`             | `NULL`             | ✅                                         |
| `SELECT 99 = NULL;`       | `NULL`             | `NULL`             | ✅                                         |
| `SELECT IFNULL(1,0);`     | `1`                | `1`                | ✅ Column header becomes `COALESCE(1,0)`   |
| `SELECT IFNULL(NULL,10);` | `10`               | `10`               | ✅ Column header becomes `COALESCE(NULL,10)` |
| `SELECT NULLIF(1,1);`     | `NULL`             | `NULL`             | ✅                                         |
| `SELECT NULLIF(1,2);`     | `1`                | `1`                | ✅                                         |
| `SELECT COALESCE(N,N,1);` | `1`                | `1`                | ✅                                         |
| `SELECT 99 <=> NULL;`     | `0`                | ❌ Syntax Error    | ❌ Exasol does not support `<=>`           |
| `SELECT ISNULL(1);`       | `0`                | `0`                | ✅ Header becomes  `1 IS NULL`             |
| `SELECT SUM(x) FROM t;`   | `10`               | `10`               | ✅ Header becomes `SUM(T.X)`               |
| `SELECT AVG(x) FROM t;`   | `2.75`           | `2.75`               | ✅ Header becomes `AVG(T.X)`               |
| `SELECT COUNT(x) FROM t;` | `2`                | `2`                | ✅ Header becomes `COUNT(T.X)`             |
| `ORDER BY x` (ASC)        | `NULL`s come First | `NULL`s come First | ✅                                         |
| `ORDER BY x` (DESC)       | `NULL`s come Last  | `NULL`s come First | ❌ Opposite default sorting                |

### 2. Empty Strings vs. NULL

Exasol interprets an empty string (`''`) as a `NULL` value. MariaDB alignment requires Oracle compatibility mode.

| **Query**            | **MariaDB (Oracle Mode)** | **MariaDB (Standard)** | **Result Exasol Behavior**           |
| -------------------- | ------------------------- | ---------------------- | ------------------------------------ |
| `SELECT '';`         | `NULL`                    | `''`                   | `NULL`                               |
| `SELECT '' IS NULL;` | `1`                       | `0`                    | `1`                                  |
| `CHAR_LENGTH('');`   | `NULL`                    | `0`                    | `NULL` (evaluated as `LENGTH(NULL)`) |

* Workaround: Use `SET sql_mode = 'EMPTY_STRING_IS_NULL';` in MariaDB.

## IV. SQL Syntax Differences

### Reserved Words

Exasol reserves over 460 keywords. Common words like `schema`, `hour`, and `year` must be quoted with double quotes (`"column"`) — not backticks.

### Session Variables

User variables (`SET @x := 5`) and `SELECT ... INTO @var` are not supported on the analytical path. 
`SET` statements sent to Exasol are accepted but ignored, with no error, so a later query that references the variable fails with a syntax error.

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


## V. Functional Compatibility Matrix

The analytical path uses SQLglot to bridge MariaDB and Exasol dialects.

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

MariaDB writes NULL as \N in export files. Importing such a file directly into Exasol with IMPORT fails on TIMESTAMP columns, so replace \N with an empty value or NULL first. 
Loading through MariaDB and CDC needs no conversion, because NULLs replicate correctly.

### Empty Strings

Exasol treats an empty string ('') as NULL. The exasolrouter rewrites the literal '' to NULL, and empty strings in VARCHAR and TEXT columns arrive as NULL through CDC. As a result, CHAR_LENGTH('') returns NULL rather than 0.

### Load Data
* LOAD DATA [LOCAL] INFILE fails through the exasolrouter with a syntax error. Load into MariaDB directly and CDC will load the rows into Exasol.

### Formatting & Output Trade-offs

* Implicit Aliasing: MariaDB preserves the original query string (e.g., `SUM(x)`), while Exasol generates internal aliases (e.g., `SUM(T.X)`).
* Decimal Precision: Results through the exasolrouter often trims trailing zeros (e.g., `5` vs `5.0000`). Stored values are unchanged.

### Case Sensitivity
* Identifiers: table, column and schema names are matched case-insensitively (SQL_IDENTIFIER_COMPARISON = IGNORE CASE).
* String data: comparisons are case-sensitive. WHERE col = 'abc' will not match 'ABC', even for columns that used a case-insensitive collation in MariaDB. Use UPPER() or LOWER() on both sides to match MariaDB.

## VII. How It Works: Architecture & Query Flow

MariaDB Exa uses a Hybrid Transactional and Analytical Processing (HTAP) architecture to deliver transactional consistency alongside high-performance analytics.

### 1. The Analytical Path (Read)

* MaxScale SmartRouter: Acts as the intelligent entry point for client applications. It identifies read-only queries and routes them to either the MariaDB cluster or the analytical environment based on learned performance metrics.
* ExasolRouter (MariaDB Exa Router): When analytical routing is selected, the query is passed to this specialized router. It hosts the SQLglot Preprocessor.
* SQLglot Preprocessor: Automatically transpiles MariaDB-specific SQL dialect into Exasol-compatible dialect in real-time.

### 2. The Replication Path (Write)

* MaxScale CDC (binlogrouter): Manages background synchronization of DDL and DML changes from the MariaDB Binary Log directly to Exasol over the Exasol ODBC driver.
* Direct Sync: This pathway is a raw data stream and does not utilize the SQLglot preprocessor.
