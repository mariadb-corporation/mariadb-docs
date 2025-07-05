# InnoDB DYNAMIC Row Format

`DYNAMIC` is the default InnoDB row format.

The `DYNAMIC` row format is similar to the `COMPACT` row format, but tables using the `DYNAMIC` row format can store even more data on overflow pages than tables using the `COMPACT` row format. This results in more efficient data storage than tables using the `COMPACT` row format, especially for tables containing columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types. While InnoDB tables using the `COMPRESSED` row format can result in even greater space-efficiency, COMPRESSED requires substantially more memory and CPU to both read and write, so there is a significant performance and concurrency trade-off for that space-efficiency gain. COMPRESSED tables are not recommended for production use in most situations, while DYNAMIC row format scales well in high-performance environments.

## Supported Index Prefix Limits

The limit for indexing column values depends on the [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size) value:

| Page Size   | Index Prefix Limit |
| ----------- | ------------------ |
| Page Size   | Index Prefix Limit |
| 16k 32k 16k | 3072 bytes         |
| 8k          | 1536 bytes         |
| 4k          | 768 bytes          |

## Using the DYNAMIC Row Format

The default row format is `DYNAMIC`, as long as the [innodb\_default\_row\_format](../innodb-system-variables.md#innodb_default_row_format) system variable has not been modified. Therefore, in these versions, the easiest way to create an InnoDB table that uses the `DYNAMIC` row format is by **not** setting the [ROW\_FORMAT](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option at all in a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) statement.

It is recommended to set the [innodb\_strict\_mode](../innodb-system-variables.md#innodb_strict_mode) system variable to `ON` when using this row format.

For example:

```sql
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_default_row_format='dynamic';

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE=InnoDB;
```

### Create an InnoDB Table with the Dynamic Row Format by Default

InnoDB uses the Dynamic row format for new InnoDB tables by default, because the [innodb\_default\_row\_format](../innodb-system-variables.md#innodb_default_row_format) system variable is dynamic by default.

Let's create an InnoDB table after confirming that the default storage engine is InnoDB and that InnoDB's default row format is Dynamic:

1. Connect to the server using [MariaDB Client](../../../../clients-and-utilities/mariadb-client/):

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) system variable using the [SHOW SESSION VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

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

3. Confirm that InnoDB's default row format is Dynamic by checking the [innodb\_default\_row\_format](../innodb-system-variables.md#innodb_default_row_format) system variable using the [SHOW GLOBAL VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW GLOBAL VARIABLES
   LIKE 'innodb_default_row_format';
```

```
+---------------------------+---------+
| Variable_name             | Value   |
+---------------------------+---------+
| innodb_default_row_format | dynamic |
+---------------------------+---------+
```

4. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../../../reference/sql-statements/data-definition/create/create-database.md) statement:

```sql
CREATE DATABASE hq_sales;
```

5. Create the table using the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement:

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

6. Confirm that the table uses the Dynamic row format by querying the [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table:

```sql
SELECT NAME, ROW_FORMAT
FROM information_schema.INNODB_SYS_TABLES
WHERE NAME='hq_sales/invoices';
```

```
+-------------------+------------+
| NAME              | ROW_FORMAT |
+-------------------+------------+
| hq_sales/invoices | Dynamic    |
+-------------------+------------+
```

### Create an InnoDB Table with the Dynamic Row Format using `ROW_FORMAT`

An InnoDB table that uses the Dynamic row format can be created using the `ROW_FORMAT` table option.

Let's create an InnoDB table after confirming that the default storage engine is InnoDB and that InnoDB's default row format is not Dynamic:

1. Connect to the server using [MariaDB Client](../../../../clients-and-utilities/mariadb-client/):

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) system variable using the [SHOW SESSION VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

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

3. Confirm that InnoDB's default row format is not Dynamic by checking the [innodb\_default\_row\_format](../innodb-system-variables.md#innodb_default_row_format) system variable using the [SHOW GLOBAL VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW GLOBAL VARIABLES
   LIKE 'innodb_default_row_format';
```

```
+---------------------------+---------+
| Variable_name             | Value   |
+---------------------------+---------+
| innodb_default_row_format | compact |
+---------------------------+---------+
```

4. If the database does not exist, then create the database for the table using the [CREATE DATABASE](../../../../reference/sql-statements/data-definition/create/create-database.md) statement:

```sql
CREATE DATABASE hq_sales;
```

5. Create the table using the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement, and specify the Dynamic row format using the `ROW_FORMAT` table option:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
) ROW_FORMAT = Dynamic;
```

6. Confirm that the table uses the Dynamic row format by querying the [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table:

```sql
SELECT NAME, ROW_FORMAT
FROM information_schema.INNODB_SYS_TABLES
WHERE NAME='hq_sales/invoices';
```

```
+-------------------+------------+
| NAME              | ROW_FORMAT |
+-------------------+------------+
| hq_sales/invoices | Dynamic    |
+-------------------+------------+
```

### Convert InnoDB Tables to the Dynamic Row Format

If your database was physically upgraded from some older version of MariaDB Server or MySQL, then some of your tables may not be using the Dynamic row format. If you want to get the benefits of the Dynamic row format, then those tables will need to be converted to use it.

Let's convert some InnoDB tables to the Dynamic row format:

1. Connect to the server using MariaDB Client:

```
$ mariadb --user=root
```

2. Search for InnoDB tables that do not use the Dynamic row format by querying the [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table:

```sql
SELECT NAME, ROW_FORMAT
FROM information_schema.INNODB_SYS_TABLES
WHERE NAME NOT LIKE 'SYS_%'
AND ROW_FORMAT != 'Dynamic';
```

```
+-------------------+------------+
| NAME              | ROW_FORMAT |
+-------------------+------------+
| hq_sales/invoices | Compact    |
+-------------------+------------+
```

3. Alter the table using the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table.md) statement, and specify the Dynamic row format using the `ROW_FORMAT` table option:

```sql
ALTER TABLE hq_sales.invoices
   ROW_FORMAT = Dynamic;
```

4. Confirm that the table uses the Dynamic row format by querying the [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table again:

```
SELECT NAME, ROW_FORMAT
FROM information_schema.INNODB_SYS_TABLES
WHERE NAME='hq_sales/invoices';
```

```
+-------------------+------------+
| NAME              | ROW_FORMAT |
+-------------------+------------+
| hq_sales/invoices | Dynamic    |
+-------------------+------------+
```

## Index Prefixes with the DYNAMIC Row Format

The `DYNAMIC` row format supports index prefixes up to 3072 bytes. In earlier versions of MariaDB, the [innodb\_large\_prefix](../innodb-system-variables.md#innodb_large_prefix) system variable is used to configure the maximum index prefix length. In these versions, if [innodb\_large\_prefix](../innodb-system-variables.md#innodb_large_prefix) is set to `ON`, then the maximum prefix length is 3072 bytes, and if it is set to `OFF`, then the maximum prefix length is 767 bytes.

## Overflow Pages with the DYNAMIC Row Format

All InnoDB row formats can store certain kinds of data in overflow pages. This allows for the maximum row size of an InnoDB table to be larger than the maximum amount of data that can be stored in the row's main data page. See [Maximum Row Size](innodb-dynamic-row-format.md#maximum-row-size) for more information about the other factors that can contribute to the maximum row size for InnoDB tables.

In the `DYNAMIC` row format variable-length columns, such as columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types, can be completely stored in overflow pages.

InnoDB only considers using overflow pages if the table's row size is greater than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). If the row size is greater than this, then InnoDB chooses variable-length columns to be stored on overflow pages until the row size is less than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size).

For [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) columns, only values longer than 40 bytes are considered for storage on overflow pages. For [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) and [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) columns, only values longer than 255 bytes are considered for storage on overflow pages. Bytes that are stored to track a value's length do not count towards these limits. These limits are only based on the length of the actual column's data.

These limits differ from the limits for the `COMPACT` row format, where the limit is 767 bytes for all types.

Fixed-length columns greater than 767 bytes are encoded as variable-length columns, so they can also be stored in overflow pages if the table's row size is greater than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). Even though a column using the [CHAR](../../../../reference/data-types/string-data-types/char.md) data type can hold at most 255 characters, a [CHAR](../../../../reference/data-types/string-data-types/char.md) column can still exceed 767 bytes in some cases. For example, a `char(255)` column can exceed 767 bytes if the [character set](../../../../reference/data-types/string-data-types/character-sets/) is `utf8mb4`.

If a column is chosen to be stored on overflow pages, then the entire value of the column is stored on overflow pages, and only a 20-byte pointer to the column's first overflow page is stored on the main page. Each overflow page is the size of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). If a column is too large to be stored on a single overflow page, then it is stored on multiple overflow pages. Each overflow page contains part of the data and a 20-byte pointer to the next overflow page, if a next page exists.

This behavior differs from the behavior of the `COMPACT` row format, which always stores the column prefix on the main page. This allows tables using the `DYNAMIC` row format to contain a high number of columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
