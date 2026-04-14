---
description: >-
  Schema qualifiers manage SQL mode dependent behavior for data types and
  functions.
---

# Schema Qualifiers

{% hint style="info" %}
* `mariadb_schema` and `oracle_schema` are not actual databases or schemas.
* They do not appear in `SHOW DATABASES`.
* These are prefix qualifiers that manage SQL-mode dependent behavior for function and data types.
{% endhint %}

## Description

MariaDB offers schema qualifiers that allow you to define how data types and functions are managed when SQL modes result in operational differences.

These qualifiers are used as prefixes and are part of the SQL language structure. These are not system databases or tables.&#x20;

The schema qualifiers listed below are supported:

* [mariadb\_schema](schema-qualifiers.md#mariadb_schema)
* [oracle\_schema](schema-qualifiers.md#oracle_schema)

Both prefixes describe the same mechanism, however the behavior differs based on the desired compatibility.

Certain SQL modes, such as [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), affect how MariaDB understands data type and functions. MariaDB translates several data type names and function behaviors according to Oracle Database standards when [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is active. This translation may lead to ambiguity: depending on the SQL mode in use, a data type or function name written without a qualifier could be interpreted differently.

For example, in Oracle mode, the data type [DATE](../../data-types/date-and-time-data-types/date.md) is interpreted as [DATETIME](../../data-types/date-and-time-data-types/datetime.md#oracle-mode). This behavior can be explicitly overridden at the statement level using schema qualifiers, without modifying the SQL mode session.

### Version Support

* `mariadb_schema` for data type qualification is supported since:
  * [MariaDB 10.3.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.24)
  * [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.14)
  * [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.5)
* `oracle_schema` is supported as part of the same schema qualifier mechanism.
* Functional qualification using schema qualifiers is supported since:
  * [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.17) (see [MDEV-27744](https://jira.mariadb.org/browse/MDEV-27744))

### Why Schema Qualifiers are Needed

Specific SQL modes, for example `SQL_MODE=ORACLE`, determine how MariaDB handles data types and functions.

This may result in ambiguity when:

* Switching between SQL modes
* Evaluating table definitions using `SHOW CREATE TABLE`
* Syncing data across servers

Regardless of the SQL mode that is currently in use, schema qualifiers provide explicit control over interpretation, ensuring reliable and consistent behavior.

### mariadb\_schema

The `mariadb_schema` qualifier forces MariaDB-native interpretation of the data type or function, regardless of the active SQL mode.

When the server sees the `mariadb_schema` qualifier, it disables sql\_mode-specific data type translation and interprets the data type literally. For example, `mariadb_schema.DATE` is interpreted as the traditional MariaDB `DATE` data type, regardless of the current SQL mode.

#### Data Type Qualification

In Oracle mode, the DATE type is translated to DATETIME:

```sql
SET sql_mode=ORACLE;

CREATE TABLE t1 (
d DATE
);
```

To specifically use the MariaDB-native DATE type while in Oracle mode:

```sql
CREATE TABLE t1 (
  d mariadb_schema.DATE
);
```

**Example**

```sql
SET sql_mode=ORACLE;

CREATE TABLE t1 (
  d DATE,
  d_m mariadb_schema.DATE
);

DESCRIBE t1;
```

**Output**

```sql
+-------+----------+
| Field | Type     | 
+-------+----------+
| d     | datetime |
| d_m   | date     |
+-------+----------+
```

### oracle\_schema

The `oracle_schema` qualifier enforces Oracle-compatible behavior of the data type or function, regardless of the active SQL mode. It supports Oracle semantics but acts similarly to `mariadb_schema`.

For example:

* In Oracle mode, the `DATE` data types behaves like `DATETIME`.
* Using `oracle_schema.DATE` ensures Oracle-compatible interpretation even when Oracle mode is not enabled.

#### Data Type Qualification

```sql
SET sql_mode=ORACLE;

CREATE TABLE t1 (
  d DATE,
  d_m mariadb_schema.DATE,
  d_o oracle_schema.DATE
);

DESCRIBE t1;
```

**Output**

```sql
+-------+----------+
| Field | Type     | 
+-------+----------+
| d     | datetime |
| d_m   | date     |
| d_o   | datetime |
+-------+----------+
```

### Using Both Qualifiers Together

The following example demonstrates how to use both qualifiers together in a single table definition to control data type behavior.&#x20;

To explicitly use Oracle-compatible behavior outside Oracle mode:

```sql
SET sql_mode=DEFAULT;

CREATE TABLE t1 (
d oracle_schema.DATE
);
```

When running in Oracle mode, both qualifiers can be used to explicitly control behavior.

```sql
SET sql_mode=ORACLE;

CREATE TABLE t1 (
d DATE,                  # Oracle-compatible (stored as DATETIME)
d_m mariadb_schema.DATE, # MariaDB-native DATE
d_o oracle_schema.DATE   # Oracle-compatible DATE
);

DESCRIBE t1;
```

**Output**

```sql
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| d     | datetime | YES  |     | NULL    |       |
| d_m   | date     | YES  |     | NULL    |       |
| d_o   | datetime | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+  
```

### Function Qualification

Starting with MariaDB 10.6.17, schema qualifiers can also be added to functions.&#x20;

Regardless of the current SQL mode, this enables the explicit selection of MariaDB-native or Oracle-compatible behavior.

Example syntax:

```sql
# MariaDB-native function behavior in any SQL mode
mariadb_schema.function_name(...) 

# Oracle-compatible function behavior in any SQL mode
oracle_schema.function_name(...)
```

**Behavior**

* `mariadb_schema.function_name(...)`: MariaDB-native behavior
* `oracle_schema.function_name(...)`: Oracle-compatible behavior

**Note**: Function behavior varies depending on the SQL mode and function.\
Detailed function-level differences are not fully listed here and may differ by version.

### SHOW CREATE TABLE

To prevent ambiguity in data type interpretation, MariaDB may display schema qualifiers when `SHOW CREATE TABLE` is executed.

```sql
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------------------+
| Table | Create Table                                                 |
+-------+--------------------------------------------------------------+
| t1    | CREATE TABLE "t1" (                                          |
|       |   "d" mariadb_schema.DATE DEFAULT NULL                       |
|       |  )                                                           |
+-------+--------------------------------------------------------------+
```

The prefix is displayed to indicate that the column uses MariaDB's native DATE type rather than the Oracle-compatible translated version.

The `mariadb_schema` prefix is only displayed when the data type is ambiguous. When the type is non-ambiguous or the SQL mode is set to default, it is not displayed.

This makes it easier to determine whether a column uses MariaDB-native or Oracle-compatible semantics.

### History

When running with [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), MariaDB server translates the `DATE` data type to `DATETIME`, for Oracle compatibility.&#x20;

```sql
SET SQL_mode=ORACLE;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------------------+
| Table | Create Table                                                 |
+-------+--------------------------------------------------------------+
| t1    | CREATE TABLE "t1" (                                          |
|       |   "d" datetime DEFAULT NULL                       |
|       |  )                                                           |
+-------+--------------------------------------------------------------+
```

**Note**: `DATE` was converted to `DATETIME`.

This translation can cause ambiguity. For example, if a table is created in default SQL mode and then evaluated in Oracle mode:

```sql
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
```

Before schema qualifiers were introduced, this would display:

```sql
CREATE TABLE "t1" (
  "d" DATE DEFAULT NULL
);
```

This created two problems:

* It was not clear whether DATE referred to the MariaDB DATE type or the Oracle-compatible DATETIME.
* It broke replication, causing a data type mismatch between the primary and the replica. (see [MDEV-19632](https://jira.mariadb.org/browse/MDEV-19632)).

To address this problem, MariaDB included schema qualifiers to explicitly qualify data types:

```sql
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------------------+
| Table | Create Table                                                 |
+-------+--------------------------------------------------------------+
| t1    | CREATE TABLE "t1" (                                          |
|       |   "d" mariadb_schema.DATE DEFAULT NULL                       |
|       |  )                                                           |
+-------+--------------------------------------------------------------+
```

This enables consistent and unambiguous behavior across all SQL modes.

### See Also

* [SQL Mode](../../../server-management/variables-and-modes/sql_mode.md)
* [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)
* [Data Types](../../data-types/)
* [SHOW CREATE TABLE](../../sql-statements/administrative-sql-statements/show/show-create-table.md)
