# InnoDB Strict Mode

[InnoDB](./) strict mode is similar to [SQL strict mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode). When it is enabled, certain InnoDB warnings become errors instead.

## Configuring InnoDB Strict Mode

InnoDB strict mode is enabled by default.

InnoDB strict mode can be enabled or disabled by configuring the [innodb\_strict\_mode](innodb-system-variables.md) server system variable.

Its global value can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_strict_mode=ON;
```

Its value for the current session can also be changed dynamically with [SET SESSION](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET SESSION innodb_strict_mode=ON;
```

It can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_strict_mode=ON
```

## InnoDB Strict Mode Errors

### Wrong Create Options

If InnoDB strict mode is enabled, and if a DDL statement is executed and invalid or conflicting [table options](../../../reference/sql-statements/data-definition/create/create-table.md#table-options) are specified, then an error is raised. The error will only be a generic error that says the following:

```sql
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")
```

However, more details about the error can be found by executing [SHOW WARNINGS](../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md).

For example, the error is raised in the following cases:

* The [KEY\_BLOCK\_SIZE](../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is set to a non-zero value, but the [ROW\_FORMAT](../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option is set to some row format other than the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format:

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
KEY_BLOCK_SIZE=4
ROW_FORMAT=DYNAMIC;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: cannot specify ROW_FORMAT = DYNAMIC with KEY_BLOCK_SIZE.   |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [KEY\_BLOCK\_SIZE](../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is set to a non-zero value, but the configured value is larger than either `16` or the value of the [innodb\_page\_size](innodb-system-variables.md#innodb_page_size) system variable, whichever is smaller.

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
KEY_BLOCK_SIZE=16;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: KEY_BLOCK_SIZE=16 cannot be larger than 8.                 |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [KEY\_BLOCK\_SIZE](../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is set to a non-zero value, but the [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) system variable is not set to `ON`.

```sql
SET GLOBAL innodb_file_per_table=OFF;
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
KEY_BLOCK_SIZE=4;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: KEY_BLOCK_SIZE requires innodb_file_per_table.             |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [KEY\_BLOCK\_SIZE](../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is set to a non-zero value, but it is not set to one of the supported values: \[1, 2, 4, 8, 16].

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
KEY_BLOCK_SIZE=5;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+-----------------------------------------------------------------------+
| Level   | Code | Message                                                               |
+---------+------+-----------------------------------------------------------------------+
| Warning | 1478 | InnoDB: invalid KEY_BLOCK_SIZE = 5. Valid values are [1, 2, 4, 8, 16] |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options")    |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB       |
+---------+------+-----------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [ROW\_FORMAT](../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option is set to the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format, but the [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) system variable is not set to `ON`.

```sql
SET GLOBAL innodb_file_per_table=OFF;
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
ROW_FORMAT=COMPRESSED;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: ROW_FORMAT=COMPRESSED requires innodb_file_per_table.      |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [ROW\_FORMAT](../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option is set to a value, but it is not set to one of the values supported by InnoDB: [REDUNDANT](innodb-row-formats/innodb-redundant-row-format.md), [COMPACT](innodb-row-formats/innodb-compact-row-format.md), [DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md), and [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md).

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
ROW_FORMAT=PAGE;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: invalid ROW_FORMAT specifier.                              |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* Either the [KEY\_BLOCK\_SIZE](../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is set to a non-zero value or the [ROW\_FORMAT](../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option is set to the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format, but the [innodb\_page\_size](innodb-system-variables.md#innodb_page_size) system variable is set to a value greater than `16k`.

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
ROW_FORMAT=COMPRESSED;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+-----------------------------------------------------------------------+
| Level   | Code | Message                                                               |
+---------+------+-----------------------------------------------------------------------+
| Warning | 1478 | InnoDB: Cannot create a COMPRESSED table when innodb_page_size > 16k. |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options")    |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB       |
+---------+------+-----------------------------------------------------------------------+
3 rows in set (0.00 sec)
```

* The [DATA DIRECTORY](../../../reference/sql-statements/data-definition/create/create-table.md#data-directoryindex-directory) table option is set, but the [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) system variable is not set to `ON`.

```sql
SET GLOBAL innodb_file_per_table=OFF;
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
DATA DIRECTORY='/mariadb';
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: DATA DIRECTORY requires innodb_file_per_table.             |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [DATA DIRECTORY](../../../reference/sql-statements/data-definition/create/create-table.md#data-directoryindex-directory) table option is set, but the table is a [temporary table](../../../reference/sql-statements/data-definition/create/create-table.md#create-temporary-table).

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TEMPORARY TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
DATA DIRECTORY='/mariadb';
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: DATA DIRECTORY cannot be used for TEMPORARY tables.        |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [INDEX DIRECTORY](../../../reference/sql-statements/data-definition/create/create-table.md#data-directoryindex-directory) table option is set.

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
INDEX DIRECTORY='/mariadb';
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning | 1478 | InnoDB: INDEX DIRECTORY is not supported                           |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [PAGE\_COMPRESSED](innodb-strict-mode.md#page_compressed) table option is set to `1`, so [InnoDB page compression](innodb-page-compression.md) is enabled, but the [ROW\_FORMAT](../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option is set to some row format other than the [COMPACT](innodb-row-formats/innodb-compact-row-format.md) or [DYNAMIC](innodb-row-formats/innodb-dynamic-row-format.md) row formats.

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
PAGE_COMPRESSED=1
ROW_FORMAT=COMPRESSED;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning |  140 | InnoDB: PAGE_COMPRESSED table can't have ROW_TYPE=COMPRESSED       |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [PAGE\_COMPRESSED](innodb-strict-mode.md#page_compressed) table option is set to `1`, so [InnoDB page compression](innodb-page-compression.md) is enabled, but the [innodb\_file\_per\_table](innodb-system-variables.md#innodb_file_per_table) system variable is not set to `ON`.

```sql
SET GLOBAL innodb_file_per_table=OFF;
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
PAGE_COMPRESSED=1;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning |  140 | InnoDB: PAGE_COMPRESSED requires innodb_file_per_table.            |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [PAGE\_COMPRESSED](innodb-strict-mode.md#page_compressed) table option is set to `1`, so [InnoDB page compression](innodb-page-compression.md) is enabled, but the [KEY\_BLOCK\_SIZE](../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is also specified.

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
PAGE_COMPRESSED=1
KEY_BLOCK_SIZE=4;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning |  140 | InnoDB: PAGE_COMPRESSED table can't have key_block_size            |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

* The [PAGE\_COMPRESSION\_LEVEL](../../../reference/sql-statements/data-definition/create/create-table.md#page_compression_level) table option is set, but\
  the [PAGE\_COMPRESSED](innodb-strict-mode.md#page_compressed) table option is set to `0`, so [InnoDB page compression](innodb-page-compression.md) is disabled.

```sql
SET SESSION innodb_strict_mode=ON;

CREATE OR REPLACE TABLE tab (
   id INT PRIMARY KEY,
   str VARCHAR(50)
)
PAGE_COMPRESSED=0
PAGE_COMPRESSION_LEVEL=9;
ERROR 1005 (HY000): Can't create table `db1`.`tab` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+--------------------------------------------------------------------+
| Level   | Code | Message                                                            |
+---------+------+--------------------------------------------------------------------+
| Warning |  140 | InnoDB: PAGE_COMPRESSION_LEVEL requires PAGE_COMPRESSED            |
| Error   | 1005 | Can't create table `db1`.`tab` (errno: 140 "Wrong create options") |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB    |
+---------+------+--------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

### COMPRESSED Row Format

If InnoDB strict mode is enabled, and if a table uses the [COMPRESSED](innodb-row-formats/innodb-compressed-row-format.md) row format, and if the table's [KEY\_BLOCK\_SIZE](../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) is too small to contain a row, then an error is returned by the statement.

### Row Size Too Large

If InnoDB strict mode is enabled, and if a table exceeds its row format's [maximum row size](innodb-row-formats/innodb-row-formats-overview.md#maximum-row-size), then InnoDB will return an error.

```sql
ERROR 1118 (42000): Row size too large (> 8126). Changing some columns to 
TEXT OR BLOB may help. IN current row format, BLOB prefix of 0 bytes IS stored inline.
```

See [Troubleshooting Row Size Too Large Errors with InnoDB](innodb-row-formats/troubleshooting-row-size-too-large-errors-with-innodb.md) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
