---
description: >-
  Learn about AUTO_INCREMENT constraints in MariaDB Server. This section details
  how to automatically generate unique, sequential values for table columns,
  simplifying data management.
---

# AUTO\_INCREMENT Constraints

_To define an `AUTO_INCREMENT` column, select an integer data type to accommodate the range of anticipated values. Common choices include `INT`, `BIGINT`, `TINYINT`, `SMALLINT`, and `MEDIUMINT`, depending on size requirements. Ensure the chosen type provides sufficient capacity to avoid overflow while optimizing storage efficiency._

## Overview

MariaDB Enterprise Server supports `AUTO_INCREMENT` constraints:

* A column with an `AUTO_INCREMENT` constraint can act as a table's primary key when a natural primary key is not available
* Generated values for auto-increment columns are guaranteed to be unique and monotonically increasing
* Auto-increment columns provide compatibility with schemas designed for MariaDB Enterprise Server and MySQL

Alternatively, MariaDB Enterprise Server can use [sequences](../../reference/sql-structure/sequences/sequence-overview.md) as the primary key instead of columns with `AUTO_INCREMENT` constraints. Sequences are compliant with the SQL standard, while `AUTO_INCREMENT` constraints are not, so sequences are the better option for applications that require standard-compliant features.

## Choosing a Data Type for an `AUTO_INCREMENT` Column

When designing a schema, `AUTO_INCREMENT` columns should use integer data types. The following types can be used:

| Data Type                                                                                                                                                                                            | Signed Range                               | Unsigned Range           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------ |
| [TINYINT](../../reference/data-types/numeric-data-types/tinyint.md)                                                                                                                                  | -128 - 127                                 | 0 - 255                  |
| [SMALLINT](../../reference/data-types/numeric-data-types/smallint.md)                                                                                                                                | -32768 - 32767                             | 0 - 65535                |
| [MEDIUMINT](../../reference/data-types/numeric-data-types/mediumint.md)                                                                                                                              | -8388608 - 8388607                         | 0 - 16777215             |
| [INT](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/data-manipulation/server-constraints/data-types-int/README.md)       | -2147483648 - 2147483647                   | 0 - 4294967295           |
| [BIGINT](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/data-manipulation/server-constraints/data-types-bigint/README.md) | -9223372036854775808 - 9223372036854775807 | 0 - 18446744073709551615 |

To determine which type to use, consider the following points:

1. Do you want to be able to manually insert negative values? If not, then specify the UNSIGNED attribute for the column.

InnoDB can't generate negative `AUTO_INCREMENT` values, so it is only beneficial to use a signed integer column if you want the option to manually insert negative values, which would bypass the `AUTO_INCREMENT` handling.

2. How large will your table grow?

If your `AUTO_INCREMENT` column is being used as the table's primary key, then the maximum value for the chosen data type should be considered the maximum number of rows that can fit in the table:

| Data Type                                                                                                                                                                                            | Signed Range        | Unsigned Range       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- |
| [TINYINT](../../reference/data-types/numeric-data-types/tinyint.md)                                                                                                                                  | 127                 | 255                  |
| [SMALLINT](../../reference/data-types/numeric-data-types/smallint.md)                                                                                                                                | 32767               | 65535                |
| [MEDIUMINT](../../reference/data-types/numeric-data-types/mediumint.md)                                                                                                                              | 8388607             | 16777215             |
| [INT](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/data-manipulation/server-constraints/data-types-int/README.md)       | 2147483647          | 4294967295           |
| [BIGINT](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements-and-structure/sql-statements/data-manipulation/server-constraints/data-types-bigint/README.md) | 9223372036854775807 | 18446744073709551615 |

If you want to give your table the most room to grow, then it would be best to choose BIGINT UNSIGNED.

## Creating an InnoDB Table with an AUTO\_INCREMENT Column

Let's [create an InnoDB table with an AUTO\_INCREMENT column](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column) after confirming that the [default storage engine](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) is InnoDB:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';
```

```
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](https://mariadb.com/kb/en/\[\[create-database) statement:

```sql
CREATE DATABASE hq_sales;
```

4. Create the table using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
);
```

## Inserting a Row with an AUTO\_INCREMENT Column

If a column is specified as `AUTO_INCREMENT`, then its value will be automatically generated. There are multiple ways to insert rows with these automatically generated values.

### Omitting the Column

If the column is not specified, then InnoDB will automatically generate the value.

Let's insert a row into the table created in the [Creating an InnoDB Table with an AUTO\_INCREMENT Column](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column) section:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Insert a row with the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement, but do not specify the `AUTO_INCREMENT` column:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD');
```

3. Select the same row with the [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to confirm that a value was automatically generated:

```sql
SELECT invoice_id
FROM hq_sales.invoices
WHERE branch_id = 1
AND customer_id = 1
AND invoice_date = '2020-05-10 12:35:10';
```

```
+------------+
| invoice_id |
+------------+
|          1 |
+------------+
```

### Specifying the Column's Value as 0

If the column's value is specified as 0, then InnoDB will automatically generate the value if the [sql\_mode](../../server-management/variables-and-modes/sql_mode.md) system variable does not contain `NO_AUTO_VALUE_ON_ZERO`.

Let's insert a row into the table created in the [Creating an InnoDB Table with an AUTO\_INCREMENT Column](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column) section:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Confirm that the session's value of the sql\_mode system variable does not contain\
   NO\_AUTO\_VALUE\_ON\_ZERO with the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'sql_mode';
```

```
+---------------+-------------------------------------------------------------------------------------------+
| Variable_name | Value                                                                                     |
+---------------+-------------------------------------------------------------------------------------------+
| sql_mode      | STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+---------------+-------------------------------------------------------------------------------------------+
```

3. Insert a row with the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement, and specify the `AUTO_INCREMENT` column's value as 0:

```sql
INSERT INTO hq_sales.invoices
   (invoice_id, branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (0, 1, 2, '2020-05-10 14:17:32', 1508.57, 'WIRE_TRANSFER');
```

4. Select the same row with the [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to confirm that a value was automatically generated:

```sql
SELECT invoice_id
FROM hq_sales.invoices
WHERE branch_id = 1
AND customer_id = 2
AND invoice_date = '2020-05-10 14:17:32';
```

```
+------------+
| invoice_id |
+------------+
|          2 |
+------------+
```

### Specifying the Column's Value as NULL

If the column's value is specified as NULL, then InnoDB will automatically generate the value if the column is defined as NOT NULL.

Let's insert a row into the table created in the [Creating an InnoDB Table with an AUTO\_INCREMENT Column](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column) section:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Insert a row with the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement, and specify the `AUTO_INCREMENT` column's value as NULL:

```sql
INSERT INTO hq_sales.invoices
   (invoice_id, branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (NULL, 1, 3, '2020-05-10 14:25:16', 227.15, 'CASH');
```

3. Select the same row with the [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to confirm that a value was automatically generated:

```sql
SELECT invoice_id
FROM hq_sales.invoices
WHERE branch_id = 1
AND customer_id = 3
AND invoice_date = '2020-05-10 14:25:16';
```

```
+------------+
| invoice_id |
+------------+
|          3 |
+------------+
```

## Getting the Last Inserted AUTO\_INCREMENT Value

After InnoDB inserts an automatically generated value into an `AUTO_INCREMENT` column, the application sometimes needs to know what value it inserted. For example, the application may need to use the value to insert a foreign key column in a dependent table. The [LAST\_INSERT\_ID()](../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md) function can be used to get the lasted inserted value for an `AUTO_INCREMENT` column without re-reading the row from the table.

Let's insert a row into the table created in the [Creating an InnoDB Table with an AUTO\_INCREMENT Column](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column) section and then use the [LAST\_INSERT\_ID()](../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md) function:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Insert a row with the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement, but do not specify the `AUTO_INCREMENT` column:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 4, '2020-05-10 12:37:22', 104.19, 'CREDIT_CARD');
```

3. Execute the [LAST\_INSERT\_ID()](../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md) function to get the `AUTO_INCREMENT` value for the new row:

```sql
SELECT LAST_INSERT_ID();

+------------------+
| LAST_INSERT_ID() |
+------------------+
|                4 |
+------------------+
```

4. Select the same row with the [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to confirm that the `AUTO_INCREMENT` column has the same value:

```sql
SELECT invoice_id
FROM hq_sales.invoices
WHERE branch_id = 1
AND customer_id = 4
AND invoice_date = '2020-05-10 12:37:22';
```

```
+------------+
| invoice_id |
+------------+
|          4 |
+------------+
```

## Choosing an AUTO\_INCREMENT Lock Mode for InnoDB

When multiple rows are inserted into a table concurrently, InnoDB needs to be able to generate multiple values concurrently in a safe manner. It has several different modes that can be used to do this, and each mode has its own advantages and disadvantages.

InnoDB's `AUTO_INCREMENT` lock mode is configured with the [innodb\_autoinc\_lock\_mode](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_autoinc_lock_mode) system variable. Users can choose between 3 different values:

| Value | Description                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | • This value configures Traditional Lock Mode. • Don't use traditional lock mode. • Traditional lock mode performs very poorly. • In traditional lock mode, InnoDB holds a table-level lock while generating AUTO\_INCREMENT values.                                                                                                                                                                             |
| 1     | • This value configures Consecutive Lock Mode. • Consecutive lock mode is the default lock mode. • In consecutive lock mode, InnoDB holds a table-level lock while generating AUTO\_INCREMENT values for statements that insert multiple new rows. However, InnoDB uses a lightweight internal lock to improve performance when generating an AUTO\_INCREMENT value for statements that insert a single new row. |
| 2     | • This value configures Interleaved Lock Mode. • Interleaved lock mode is the recommended lock mode for best performance. • If Galera Cluster is being used, then interleaved lock mode must be configured.                                                                                                                                                                                                      |

• In interleaved lock mode, InnoDB never holds a table-level lock while generating `AUTO_INCREMENT` values. • Interleaved lock mode is not safe to use if binlog\_format is set to `STATEMENT`.|

## Configuring the AUTO\_INCREMENT Lock Mode for InnoDB

The [innodb\_autoinc\_lock\_mode](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_autoinc_lock_mode) system variable configures the `AUTO_INCREMENT` Lock Mode for InnoDB.

1. Choose a configuration file for custom changes to system variables and options.

It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Use the z- prefix in the file name to ensure that your custom configuration file is read last.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

2. Set the [innodb\_autoinc\_lock\_mode](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_autoinc_lock_mode) system variable in the configuration file.\
   It needs to be set in a group that will be read by MariaDB Server, such as \[mariadb] or \[server].

For example:

```
[mariadb]
...
innodb_autoinc_lock_mode = 2
```

3. Restart the server:

```bash
$ sudo systemctl restart mariadb
```

## Setting a Table's Next AUTO\_INCREMENT Value

A table's next `AUTO_INCREMENT` value can be set with the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement. The value is set using the `AUTO_INCREMENT` table option.

Let's alter the `AUTO_INCREMENT` value for the table created in the [Creating an InnoDB Table with an AUTO\_INCREMENT Column](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column) section and then insert a row into the table, so we can confirm that it uses the new value:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Alter the table's next `AUTO_INCREMENT` value with the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement:

```
ALTER TABLE hq_sales.invoices
   AUTO_INCREMENT = 100;
```

3. Insert a row with the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement, but do not specify the `AUTO_INCREMENT` column:

```sql
INSERT INTO hq_sales.invoices
   (branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 5, '2020-05-10 12:43:19', 1105.98, 'CREDIT_CARD');
```

4. Execute the [LAST\_INSERT\_ID()](../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md) function to get the `AUTO_INCREMENT` value for the new row:

```sql
SELECT LAST_INSERT_ID();

+------------------+
| LAST_INSERT_ID() |
+------------------+
|              100 |
+------------------+
```

5. Select the same row with the [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to confirm that the `AUTO_INCREMENT` column has the same value:

```sql
SELECT invoice_id
FROM hq_sales.invoices
WHERE branch_id = 1
AND customer_id = 5
AND invoice_date = '2020-05-10 12:43:19';

+------------+
| invoice_id |
+------------+
|        100 |
+------------+
```

## Configure the Offset and Increment Values

The offset and increment values can be configured by setting the [auto\_increment\_offset and auto\_increment\_increment](auto_increment-constraints.md#configure-the-offset-and-increment-values) system variables.

When Galera Cluster is used, the offset and increment values are managed automatically by default. They can be managed manually by disabling the [wsrep\_auto\_increment\_control](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_auto_increment_control) system variable.

{% include "../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
