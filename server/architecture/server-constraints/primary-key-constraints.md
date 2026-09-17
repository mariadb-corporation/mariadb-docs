# PRIMARY KEY Constraints

_Using an `AUTO_INCREMENT` column as the primary key in MariaDB is beneficial for ensuring unique row identification and efficient data retrieval. This approach automatically generates a unique integer for each new row, simplifying primary key management. It is especially useful in tables where data insertion occurs frequently, as it facilitates quick indexing and minimizes storage overhead due to its numeric nature. This practice helps maintain optimal performance in database operations, particularly when combined with clustered indexing in InnoDB._

## Overview

MariaDB Server supports `PRIMARY KEY` constraints to uniquely identify rows:

There can only be a single primary key for a given table.

* InnoDB uses the primary key as a clustered index, which means that InnoDB stores table data in the order determined by the primary key.
* Primary key indexes are B+ trees, which are very efficient for searching for exact values, performing range scans, and checking uniqueness.
* If no primary key is defined for a table, then InnoDB will use the table's first `NOT NULL` unique index as the table's primary key.
* If no primary key or `NOT NULL` unique index is defined for a table, then InnoDB will automatically create a primary key called `GEN_CLUST_INDEX`, using an internal `48-bit DB_ROW_ID` column as the key. Replication with such tables can be very slow, especially when [binlog\_format](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) is `MIXED or ROW`!
* For best performance, users should always create primary keys for their tables, and primary keys should be short, because the primary key columns are duplicated in every secondary index record.

## Using an AUTO\_INCREMENT Column as the Primary Key

If your table does not have a column or a set of columns that could act as a natural primary key, then you can define a single `AUTO_INCREMENT` column, which can serve as the table's primary key. See [InnoDB AUTO\_INCREMENT Columns](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column) for more details.

## Using a Sequence-backed Column as the Primary Key

If your table does not have a column or a set of columns that could act as a natural primary key, then you can use a sequence to generate an integer value to use as the table's primary key. Sequences were first added in MariaDB Server 10.3 and MariaDB Community Server 10.3. See [InnoDB Sequences](../../reference/sql-structure/sequences/) for more details.

## Creating an InnoDB Table with a Single Column Primary Key

Let's [create an InnoDB table with a single column primary](primary-key-constraints.md#creating-an-innodb-table-with-a-single-column-primary-key) key after confirming that the default storage engine is InnoDB:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';

+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) statement:

```
CREATE DATABASE hq_sales;
```

4. Create the table using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement and specify the primary key with the PRIMARY KEY() clause:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
);
```

For a single column primary key, the primary key can also be specified with the `PRIMARY KEY` column option:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD')
);
```

## Creating an InnoDB Table with a Composite Primary Key

Let's create an InnoDB table with a composite (multi-column) primary key after confirming that the default storage engine is InnoDB:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';

+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) statement:

```sql
CREATE DATABASE hq_sales;
```

4. Create the table using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement and specify the primary key with the PRIMARY KEY() clause:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id, branch_id)
);
```

## Adding a Primary Key to an InnoDB Table

Let's [create an InnoDB table without a primary key](primary-key-constraints.md#creating-an-innodb-table-with-a-single-column-primary-key), and then add a primary key to it:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';

+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) statement:

```sql
CREATE DATABASE hq_sales;
```

4. Create the table without a primary key using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD')
);
```

5. Alter the table using the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement and specify the new primary key with the ADD PRIMARY KEY() clause:

```sql
ALTER TABLE hq_sales.invoices ADD PRIMARY KEY (invoice_id);
```

## Dropping a Primary Key from an InnoDB Table

Let's drop the primary key from the table created in the [create an InnoDB table without a primary key](primary-key-constraints.md#creating-an-innodb-table-with-a-single-column-primary-key) section:

1. Alter the table using the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement and specify the `DROP PRIMARY KEY` clause:

```sql
ALTER TABLE hq_sales.invoices DROP PRIMARY KEY;
```

## Changing a Primary Key for an InnoDB Table

Let's change the primary key from the table created in the [create an InnoDB table without a primary key](primary-key-constraints.md#creating-an-innodb-table-with-a-single-column-primary-key) section:

1. Alter the table using the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement and specify the `DROP PRIMARY KEY` clause to drop the old primary key, and specify the new primary key with the `ADD PRIMARY KEY()` clause:

```sql
ALTER TABLE hq_sales.invoices
   DROP PRIMARY KEY,
   ADD PRIMARY KEY (invoice_id, branch_id);
```

## Finding Tables without Primary Keys

For best performance, every InnoDB table should have a primary key. It is possible to find tables without a primary key using a basic [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement.

Let's create an InnoDB table without a primary key, and then use a [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to confirm that it does not have one:

1. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine system variable](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) using the [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';

+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../reference/sql-statements/data-definition/create/create-database.md) statement:

```sql
CREATE DATABASE hq_sales;
```

4. Create the table without a primary key using the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD')
);
```

5. Query the [information\_schema](../../reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md).TABLES and [information\_schema.KEY\_COLUMN\_USAGE](../../reference/system-tables/information-schema/information-schema-tables/information-schema-key_column_usage-table.md) tables to find InnoDB tables that do not have a primary key:

```sql
SELECT t.TABLE_SCHEMA, t.TABLE_NAME
FROM information_schema.TABLES AS t
LEFT JOIN information_schema.KEY_COLUMN_USAGE AS c
ON t.TABLE_SCHEMA = c.CONSTRAINT_SCHEMA
   AND t.TABLE_NAME = c.TABLE_NAME
   AND c.CONSTRAINT_NAME = 'PRIMARY'
WHERE t.TABLE_SCHEMA != 'mysql'
   AND t.ENGINE = 'InnoDB'
   AND c.CONSTRAINT_NAME IS NULL;
```

```sql
+--------------+------------+
| TABLE_SCHEMA | TABLE_NAME |
+--------------+------------+
| hq_sales     | invoices   |
+--------------+------------+
```

6. To add a primary key, alter the table using the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement, and specify the primary key with the `ADD PRIMARY KEY()` clause:

```sql
ALTER TABLE hq_sales.invoices ADD PRIMARY KEY (invoice_id);
```

## Handling Duplicate Key Errors

A primary key uniquely identifies every row. Therefore, if a second row is inserted with an identical value, it will fail.

Let's try to insert two identical primary key values into the table created in the [Creating an InnoDB Table with a Single Column Primary Key](primary-key-constraints.md#creating-an-innodb-table-with-a-single-column-primary-key) section:

1. Insert a row with the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.invoices
   (invoice_id, branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 1, 1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD');
```

2. Insert a second row that has the same primary key value with the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.invoices
   (invoice_id, branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, 1, 2, '2020-05-10 14:17:32', 1508.57, 'WIRE_TRANSFER');
```

This will fail with the ER\_DUP\_ENTRY error code:

```sql
ERROR 1062 (23000): Duplicate entry '1' for key 'PRIMARY'
```

3. Fix the problem by inserting the row with a unique primary key value:

```sql
INSERT INTO hq_sales.invoices
   (invoice_id, branch_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (2, 1, 2, '2020-05-10 14:17:32', 1508.57, 'WIRE_TRANSFER');
```

To easily generate unique values for a primary key, consider using one of the following options:

* [InnoDB AUTO\_INCREMENT Columns](auto_increment-constraints.md#creating-an-innodb-table-with-an-auto_increment-column)
* [InnoDB Sequences](../../reference/sql-structure/sequences/)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
