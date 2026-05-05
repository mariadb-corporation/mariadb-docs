---
description: >-
  MariaDB Exa limitations: architecture and query-flow constraints, datatype
  mapping gaps in Debezium, SQL-dialect gaps in the SQLglot preprocessor, and
  the CDC primary-key requirement.
hidden: true
noIndex: true
icon: road-barrier
---

# Limitations

While MariaDB Exa (powered by Exasol) provides exceptional performance for analytical workloads, there are functional and operational limitations regarding architecture, datatype mapping, and SQL dialect compatibility.

## I. Architecture & Query Flow

The MariaDB Exa environment utilizes a Hybrid Transactional and Analytical Processing (HTAP) architecture to deliver transactional consistency alongside high-performance analytics.

### 1. The Analytical Path (Read)

* MaxScale SmartRouter: Acts as the intelligent entry point for client applications. It identifies read-only queries and routes them to either the MariaDB cluster or the analytical environment based on learned performance metrics.
* ExasolRouter (MariaDB Exa Router): When analytical routing is selected, the query is passed to this specialized router. It hosts the SQLglot Preprocessor.
* SQLglot Preprocessor: Automatically transpiles MariaDB-specific SQL dialect into Exasol-compatible dialect in real-time.

### 2. The Replication Path (Write)

* Debezium CDC Bridge: Manages background synchronization of DDL and DML changes from the MariaDB Binary Log directly to Exasol.
* Direct Sync: This pathway is a raw data stream and does not utilize the SQLglot preprocessor.

## II. Schema & Replication Management

### Primary Key Requirement

Every table being captured by CDC must define a primary key. Tables without primary keys are not supported by the JDBC Sink for upsert operations.

### Unsupported Schema Features

The following schema features are not supported:

* `COLLATE` clause.
* Character set `LATIN1`.
* `ON UPDATE` clauses.
* Triggers and stored procedures.

### Auto-increment

* `AUTO_INCREMENT`: Exasol uses `IDENTITY` columns instead.
* These can contain gaps and are not guaranteed to be unique.
* The counter can be changed with `ALTER TABLE ... MODIFY COLUMN ... IDENTITY`.

## III. Datatype Compatibility Matrix

Compatibility is tiered based on the level of automated support provided between the engines.

| **Compatibility Tier** | **Data Types**                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Native Compatible      | `INT`, `BIGINT`, `SMALLINT`, `DECIMAL`, `NUMERIC`, `FLOAT`, `DOUBLE`, `CHAR`, `VARCHAR`, `DATE`, `TIMESTAMP`, `BIT`, `ENUM`, `SET`, and `Binary types` |
| Rewrite Compatible     | `TEXT`, `BOOLEAN`, `TINYINT(1)`, `DATETIME`, `TIME`, `JSON`, `ENUM`, `SET`, `UUID`                                                                     |
| MariaDB Only           | `BLOB`, `BINARY`, `VARBINARY`, `TINYBLOB`, `Spatial types` (Geometry, Point, etc.)                                                                     |

### 1. Detailed Schema Mapping (CREATE TABLE)

The following details how MariaDB types are interpreted by Exasol during automated schema replication .

| **MariaDB Data type** | **Exasol Expected**                  | **Exasol Actual**                    | **Comment**                       |
| --------------------- | ------------------------------------ | ------------------------------------ | --------------------------------- |
| `INT`                 | —                                    | `DECIMAL(18,0)`                      | Expected wider type?              |
| `BIGINT`              | `DECIMAL(36,0)`                      | `DECIMAL(36,0)`                      | ✅                                 |
| `SMALLINT`            | `DECIMAL(5,0)`                       | `DECIMAL(9,0)`                       | ⚠️ mismatch                       |
| `MEDIUMINT`           | `DECIMAL(8,0)`                       | `DECIMAL(18,0)`                      | ⚠️ mismatch                       |
| `SERIAL`              | `DECIMAL(36,0) IDENTITY`             | —                                    | ❌ syntax error (IDENTIFIER\_PART) |
| `INT UNSIGNED`        | `DECIMAL(10,0)`                      | `DECIMAL(18,0)`                      | ⚠️ mismatch                       |
| `DECIMAL(10, 4)`      | `DECIMAL(10, 4)`                     | `DECIMAL(10,4)`                      | ✅                                 |
| `NUMERIC(15, 2)`      | `DECIMAL(15, 2)`                     | `DECIMAL(15,2)`                      | ✅                                 |
| `FLOAT`               | `FLOAT`                              | `DOUBLE`                             | ⚠️ mismatch                       |
| `DOUBLE`              | `DOUBLE`                             | `DOUBLE`                             | ✅                                 |
| `DOUBLE PRECISION`    | `DOUBLE PRECISION`                   | `DOUBLE`                             | ❓ mismatch?                       |
| `REAL`                | `DOUBLE PRECISION`                   | `DOUBLE`                             | ❓ mismatch?                       |
| `TINYINT(1)`          | `DECIMAL(3,0)`                       | `DECIMAL(3,0)`                       | ✅                                 |
| `BOOLEAN`             | `BOOLEAN`                            | `BOOLEAN`                            | ✅                                 |
| `BIT`                 | `DECIMAL(36,0)`                      | `DECIMAL(36,0)`                      | ✅                                 |
| `CHAR(10)`            | `CHAR(10)`                           | `CHAR(10)`                           | ✅                                 |
| `VARCHAR(255)`        | `VARCHAR(255)`                       | `VARCHAR(255)`                       | ✅                                 |
| `NCHAR(12)`           | `CHAR(12)`                           | `CHAR(12)`                           | ✅                                 |
| `NVARCHAR(200)`       | `VARCHAR(200)`                       | `VARCHAR(200)`                       | ✅                                 |
| `ENUM('A', 'B', 'C')` | `VARCHAR(500)`                       | `VARCHAR(65535)`                     | ✅                                 |
| `SET('X', 'Y', 'Z')`  | `VARCHAR(500)`                       | `VARCHAR(65535)`                     | ✅                                 |
| `JSON`                | `VARCHAR(2000000)`                   | `VARCHAR(2000000)`                   | ✅                                 |
| `TINYTEXT`            | `VARCHAR(255)`                       | `VARCHAR(255)`                       | ✅                                 |
| `TEXT`                | `VARCHAR(65535)`                     | `VARCHAR(65535)`                     | ✅                                 |
| `MEDIUMTEXT`          | `VARCHAR(2000000)`                   | `VARCHAR(2000000)`                   | ✅                                 |
| `LONGTEXT`            | `VARCHAR(2000000)`                   | `VARCHAR(2000000)`                   | ✅                                 |
| `TINYBLOB`            | <p><code>VARCHAR(255)</code><br></p> | <p><code>VARCHAR(255)</code><br></p> | ✅                                 |
| `BLOB`                | `VARCHAR(65535)`                     | `VARCHAR(65535)`                     | ✅                                 |
| `MEDIUMBLOB`          | `VARCHAR(2000000)`                   | `VARCHAR(2000000)`                   | ✅                                 |
| `LONGBLOB`            | `VARCHAR(2000000)`                   | `VARCHAR(2000000)`                   | ✅                                 |
| `VARBINARY(255)`      | `VARCHAR(255)`                       | `VARCHAR(255)`                       | ✅                                 |
| `BINARY(16)`          | `CHAR(16)`                           | `CHAR(16)`                           | ✅                                 |
| `DATE`                | `DATE`                               | `DATE`                               | ✅                                 |
| `DATETIME`            | `TIMESTAMP`                          | `TIMESTAMP(3)`                       | ⚠️ mismatch                       |
| `DATETIME(6)`         | `TIMESTAMP(6)`                       | `TIMESTAMP(6)`                       | ✅                                 |
| `TIME`                | `TIMESTAMP`                          | `TIMESTAMP(3)`                       | ⚠️ mismatch                       |
| `TIME(6)`             | `TIMESTAMP(6)`                       | `TIMESTAMP(6)`                       | ✅                                 |
| `TIMESTAMP`           | `TIMESTAMP`                          | `TIMESTAMP(3)`                       | ⚠️ mismatch                       |
| `TIMESTAMP(6)`        | `TIMESTAMP(6)`                       | `TIMESTAMP(6)`                       | ✅                                 |
| `YEAR(4)`             | `DECIMAL(4,0)`                       | `DECIMAL(18,0)`                      | ⚠️ mismatch                       |
| `INET6`               | —                                    | —                                    | 🛑 Debezium Fatal Crash           |
| `UUID`                | —                                    | —                                    | 🛑 Debezium Fatal Crash           |
| `XMLTYPE`             | —                                    | —                                    | 🛑 Debezium Fatal Crash           |

### 2. Data Value Replication Results (INSERT)

Precision shifts and engine-specific behaviors during transfer .

| **Data Type**      | **MariaDB Value**          | **Exasol Value**           | **Comment**                  |
| ------------------ | -------------------------- | -------------------------- | ---------------------------- |
| `INT`              | `42`                       | `42`                       | ✅                            |
| `SMALLINT`         | `32767`                    | `32767`                    | ✅                            |
| `MEDIUMINT`        | `8388607`                  | `8388607`                  | ✅                            |
| `INT UNSIGNED`     | `3000000000`               | `3000000000`               | ✅                            |
| `BIGINT`           | `9223372036854775807`      | `9223372036854775807`      | ✅                            |
| `DECIMAL(10, 4)`   | `1234.5678`                | `1234,5678`                | ✅                            |
| `NUMERIC(15, 2)`   | `99999.99`                 | `99999,99`                 | ✅                            |
| `FLOAT`            | `3.14159`                  | `3,14159012`               | ❌ Precision distortion       |
| `DOUBLE`           | `2.718281828459`           | `2,71828183`               | ❌ Precision distortion       |
| `DOUBLE PRECISION` | `123456.7890123`           | `123456,789`               | ❌ Precision distortion       |
| `REAL`             | `-9876.54321`              | `-9876,54297`              | ❌ Precision distortion       |
| `TINYINT(1)`       | `1`                        | `1`                        | ✅                            |
| `BOOLEAN`          | `1`                        | `1`                        | ✅                            |
| `CHAR(10)`         | `'test'` (len=4)           | `'test '` (len=10)         | ❌ Right-padded with spaces   |
| `VARCHAR(255)`     | `'Hello World...'`(len=19) | `'Hello World...'`(len=19) | ✅                            |
| `NCHAR(12)`        | `'Привет'` (len=6)         | `'Привет'` (len=12)        | ❌ Right-padded               |
| `NVARCHAR(200)`    | `'Extended Unicode...'`    | `'Extended Unicode...'`    | ✅                            |
| `DATE`             | `2023-10-25`               | `2023-10-25`               | ✅                            |
| `TIMESTAMP`        | `... 14:30:00`             | `... 13:30:00.000`         | ❌ Time/Precision discrepancy |
| `DATETIME`         | `... 14:30:00`             | `... 13:30:00.000`         | ❌ Time/Precision discrepancy |
| `DATETIME(6)`      | `... 14:30:00.123456`      | `... 14:30:00.123456`      | ✅                            |
| `TIME`             | `14:30:00`                 | `14:30:00`                 | ✅ Replicates as TIMESTAMP(3) |
| `TIME(6)`          | `14:30:00.987654`          | `...`                      | ✅ Replicates as TIMESTAMP(6) |
| `TIMESTAMP(6)`     | `... 14:30:00.555555`      | `... 13:30:00.555555`      | ❌ Time shift discrepancy     |
| `YEAR(4)`          | `2024`                     | `2024`                     | ✅                            |
| `JSON`             | `{"key": "value"}`         | `{"key": "value"}`         | ✅                            |
| `TINYTEXT`         | `'tiny text data'`         | `'tiny text data'`         | ✅                            |
| `MEDIUMTEXT`       | `'medium text data'`       | `'medium text data'`       | ✅                            |
| `TEXT`             | `'standard text data'`     | `'standard text data'`     | ✅                            |
| `LONGTEXT`         | `'long text data'`         | `'long text data'`         | ✅                            |

## IV. Semantic Logic & NULL Behavior

Operational behaviors regarding Undefined values and empty strings differ significantly between the engines.

### 1. Comparison & Logic Tests

In Exasol, `NULL` represents an undefined value rather than a special value, which leads to discrepancies in comparison and sorting .

| **Query**                 | **Result MariaDB** | **Result Exasol**  | **Comment**                               |
| ------------------------- | ------------------ | ------------------ | ----------------------------------------- |
| `SELECT NULL = NULL;`     | `NULL`             | `(empty)`          | ✅                                         |
| `SELECT 99 = NULL;`       | `NULL`             | `(empty)`          | ✅                                         |
| `SELECT IFNULL(1,0);`     | `1`                | `1`                | Column header becomes `COALESCE(1,0)`     |
| `SELECT IFNULL(NULL,10);` | `10`               | `10`               | Column header becomes `COALESCE(NULL,10)` |
| `SELECT NULLIF(1,1);`     | `NULL`             | `(empty)`          | ✅                                         |
| `SELECT NULLIF(1,2);`     | `1`                | `1`                | ✅                                         |
| `SELECT COALESCE(N,N,1);` | `1`                | `1`                | ✅                                         |
| `SELECT 99 <=> NULL;`     | `0`                | ❌ Syntax Error     | Exasol does not support `<=>`             |
| `SELECT ISNULL(1);`       | `0`                | ❌ Not Found        | Use `IS NULL` instead                     |
| `SELECT SUM(x) FROM t;`   | `10`               | `10`               | Header becomes `SUM(T.X)`                 |
| `SELECT AVG(x) FROM t;`   | `2.7500`           | `2,75`             | ❌ Decimal point/separator differs         |
| `SELECT COUNT(x) FROM t;` | `2`                | `2`                | Header becomes `Count(T.X)`               |
| `ORDER BY x` (ASC)        | `NULL`s come First | `NULL`s come Last  | ❌ Opposite default sorting                |
| `ORDER BY x` (DESC)       | `NULL`s come Last  | `NULL`s come First | ❌ Opposite default sorting                |

### 2. Empty Strings vs. NULL

Exasol interprets an empty string (`''`) as a `NULL` value. MariaDB alignment requires Oracle compatibility mode.

| **Query**            | **MariaDB (Oracle Mode)** | **MariaDB (Standard)** | **Result Exasol Behavior**           |
| -------------------- | ------------------------- | ---------------------- | ------------------------------------ |
| `SELECT '';`         | `NULL`                    | `''`                   | `NULL`                               |
| `SELECT '' IS NULL;` | `1`                       | `0`                    | `1`                                  |
| `CHAR_LENGTH('');`   | `NULL`                    | `0`                    | `NULL` (evaluated as `LENGTH(NULL)`) |

* Workaround: Use `SET sql_mode = 'EMPTY_STRING_IS_NULL';` in MariaDB.

## V. SQL Syntax Differences

### Reserved Words

Exasol reserves over 460 keywords. Common words like `schema`, `hour`, and `year` must be quoted with double quotes (`"column"`) — not backticks (`` ` ``).

### SET Statements

The following constructs are not supported:

SQL

```
SET x := y;
SET x=1, y=2;
```

Use `DEFINE` instead:

SQL

```
DEFINE x=1;
DEFINE y=2;
```

### Variable Assignment From SELECT

Not supported:

SQL

```
SELECT 1, 2 INTO @a, @b FROM dual;
```

Instead, use:

SQL

```
DEFINE x = (SELECT 1 FROM dual);
```

## VI. Functional Compatibility Matrix

The analytical path uses SQLglot to bridge MariaDB and Exasol dialects.

1\. Math Functions

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

2\. String Functions

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

### 3. Date & Time Functions

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

4\. Aggregate, Logic & System Functions

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

## VII. Data Import and Null Handling

### NULL Conversions

MariaDB represents `NULL` values as `\N` in export files. Exasol `TIMESTAMP` columns do not accept `\N` — they must be converted explicitly (e.g., replace `\N` with `NULL` during import).

### Formatting & Output Trade-offs

* Implicit Aliasing: MariaDB preserves the original query string (e.g., `SUM(x)`), while Exasol generates internal aliases (e.g., `SUM(T.X)`).
* Decimal Precision: Exasol often trims trailing zeros (e.g., `5` vs `5.0000`) and may use a comma as a separator depending on locale.
* Case Sensitivity: The SQLglot preprocessor typically uppercases identifiers to match standard Exasol behavior.
* Load Data: `LOAD DATA LOCAL INFILE` is not supported in the analytical pathway.

\{% include "[https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/\~/reusable/pNHZQXPP5OEz2TgvhFva/](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/)" %\}

\{% @marketo/form formId="4316" %\}
