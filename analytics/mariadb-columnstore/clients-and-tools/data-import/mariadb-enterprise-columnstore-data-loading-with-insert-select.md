---
description: >-
  MariaDB Enterprise ColumnStore translates INSERT INTO .. SELECT into a
  cpimport bulk load when batch insert mode is on and the statement runs
  outside a transaction.
---

# Data Loading with INSERT .. SELECT

## Overview

MariaDB Enterprise ColumnStore automatically translates `INSERT INTO .. SELECT FROM ..` statements into bulk data loads. By default, it translates the statement into a bulk data load that uses `cpimport.bin`, which is an internal wrapper around the `cpimport` tool.

## Intended Use Cases

You can load data using `INSERT INTO .. SELECT FROM ..` in the following cases:

You are loading data into a ColumnStore table by querying one or more local tables.

## Batch Insert Mode

MariaDB Enterprise ColumnStore enables batch insert mode by default.

When batch insert mode is enabled, MariaDB Enterprise ColumnStore has special handling for [INSERT INTO .. SELECT FROM ..](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statements.

Enterprise ColumnStore uses the following rules:

* If the statement is executed outside of a transaction, Enterprise ColumnStore loads the data using `cpimport`, which is a command-line utility that is designed to efficiently load data in bulk. Enterprise ColumnStore executes `cpimport` using a wrapper called cpimport.bin.
* If the statement is executed inside of a transaction, Enterprise ColumnStore loads the data using the DML interface, which is slower.

Batch insert mode can be disabled by setting the columnstore\_use\_import\_for\_batchinsert system variable to OFF. When batch insert mode is disabled, Enterprise ColumnStore executes the statements using the DML interface, which is slower.

## Locking

MariaDB Enterprise ColumnStore requires a write metadata lock (MDL) on the table when a bulk data load is performed with cpimport.

When a bulk data load is running:

* Read queries will not be blocked.
* Write queries and concurrent bulk data loads on the same table will be blocked until the bulk data load operation is complete, and the write metadata lock on the table has been released.
* The write metadata lock (MDL) can be monitored with the [METADATA\_LOCK\_INFO plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin).

## Importing the Schema

Before data can be imported into the tables, the schema must be created.

1. Connect to the primary server using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client):

```sql
$ mariadb --host 192.168.0.100 --port 5001 \
      --user db_user --password \
      --default-character-set=utf8
```

After the command is executed, it will prompt you for a password.

2. For each database that you are importing, create the database with the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement:

```sql
CREATE DATABASE inventory;
```

3. For each table that you are importing, create the table with the [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement:

```sql
CREATE TABLE inventory.products (
   product_name VARCHAR(11) NOT NULL DEFAULT '',
   supplier VARCHAR(128) NOT NULL DEFAULT '',
   quantity VARCHAR(128) NOT NULL DEFAULT '',
   unit_cost VARCHAR(128) NOT NULL DEFAULT ''
) ENGINE=Columnstore DEFAULT CHARSET=utf8;
```

{% hint style="info" %}
To get the best performance from Enterprise ColumnStore, make sure to follow Enterprise ColumnStore's best practices for schema design.
{% endhint %}

## Appending Data

When MariaDB Enterprise ColumnStore performs a bulk data load, it appends data to the table in the order in which the data is read. Appending data reduces the I/O requirements of bulk data loads, so that larger data sets can be loaded very efficiently.

While the bulk load is in progress, the newly appended data is temporarily hidden from queries.

After the bulk load is complete, the newly appended data is visible to queries.

## Sorting the Query Results

When MariaDB Enterprise ColumnStore performs a bulk data load, it appends data to the table in the order in which the data is read.

The order of data can have a significant effect on performance with Enterprise ColumnStore. If your data is not already sorted, it can be helpful to sort the query results using an ORDER BY clause.

For example:

```sql
# Perform import from other table
# and insert in sorted order
INSERT INTO inventory.orders
SELECT *
FROM innodb_inventory.orders
ORDER BY order_date;
```

For additional information, see "[Load Ordered Data in Proper Order](../../high-availability/columnstore-query-tuning/query-tuning-recommendations-for-mariadb-enterprise-columnstore.md#load-ordered-data-in-proper-order)".

## Confirming the Field Delimiter

Before importing a table's data into MariaDB Enterprise ColumnStore, confirm that the field delimiter is not present in the data.

The field delimiter is determined by the `columnstore_import_for_batchinsert_delimiter` system variable. By default, Enterprise ColumnStore sets the field delimiter to the `ASCII value 7`, which corresponds to the `BEL` character.

To use a different delimiter, you can set the field delimiter.

## Setting the Field Delimiter

When the data is passed to cpimport, each value is separated by a field delimiter. The field delimiter is determined by the `columnstore_import_for_batchinsert_delimiter` system variable.

By default, Enterprise ColumnStore sets the field delimiter to the `ASCII value 7`, which corresponds to the `BEL` character. In general, setting the field delimiter is only required if your data contains this value.

Set the field delimiter by setting the `columnstore_import_for_batchinsert_delimiter` system variable to the `ASCII` value for the desired delimiter character.

For example, if you want to use a comma (,) as the field delimiter, you would set `columnstore_import_for_batchinsert_delimiter` to 44:

```sql
# Set field delimiter
SET SESSION columnstore_import_for_batchinsert_delimiter=44;

# Perform import from other table
INSERT INTO inventory.products
SELECT *
FROM innodb_inventory.products;
```

## Setting the Quoting Style

When the data is passed to cpimport, each value is enclosed by a quote character. The quote character is determined by the `columnstore_import_for_batchinsert_enclosed_by` system variable.

By default, Enterprise ColumnStore sets the quote character to the `ASCII value 17`, which corresponds to the `DC1` character. In general, setting the quote character is only required if your data contains this value.

Set the quote character by setting the `columnstore_import_for_batchinsert_enclosed_by` system variable to the `ASCII` value for the desired quote character.

For example, if you want to use a double quote (") as the quote character, you would set `columnstore_import_for_batchinsert_enclosed_by` to 34:

```sql
# Set quote character
SET SESSION columnstore_import_for_batchinsert_enclosed_by=34;

# Perform import from other table
INSERT INTO inventory.products
SELECT *
FROM innodb_inventory.products;
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
