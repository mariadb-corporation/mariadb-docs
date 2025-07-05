---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
---

# Data Loading with cpimport

## Overview

MariaDB Enterprise ColumnStore includes a bulk data loading tool called cpimport, which bypasses the SQL layer to decrease the overhead of bulk data loading.

Refer to, the [cpimport modes](../data-ingestion/columnstore-bulk-data-loading.md#cpimport-modes) for additional information and [ColumnStore Bulk Data Loading](../data-ingestion/columnstore-bulk-data-loading.md).

The cpimport tool:

* Bypasses the SQL layer to decrease overhead
* Does not block read queries
* Requires a write metadata lock on the table, which can be monitored with the [METADATA\_LOCK\_INFO plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin)
* Appends the new data to the table. While the bulk load is in progress, the newly appended data is temporarily hidden from queries. After the bulk load is complete, the newly appended data is visible to queries.
* Inserts each row in the order the rows are read from the source file. Users can optimize data loads for Enterprise ColumnStore's automatic partitioning by loading presorted data files.
* Supports parallel distributed bulk loads
* Imports data from text files
* Imports data from binary files
* Imports data from standard input (stdin)

## Intended Use Cases

You can load data using the cpimport tool in the following cases:

* You are loading data into a ColumnStore table from a text file stored on the primary node's file system.
* You are loading data into a ColumnStore table from a binary file stored on the primary node's file system.
* You are loading data into a ColumnStore table from the output of a command running on the primary node.

## Locking

MariaDB Enterprise ColumnStore requires a write metadata lock (MDL) on the table when a bulk data load is performed with cpimport.

When a bulk data load is running:

* Read queries will not be blocked.
* Write queries and concurrent bulk data loads on the same table will be blocked until the bulk data load operation is complete, and the write metadata lock on the table has been released.
* The write metadata lock (MDL) can be monitored with the [METADATA\_LOCK\_INFO plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin).

## Import the Schema

Before data can be imported into the tables, the schema must be created.

1. Connect to the primary server using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client):

```
$ mariadb --host 192.168.0.100 --port 5001 \
      --user db_user --password \
      --default-character-set=utf8
```

After the command is executed, it will prompt you for a password.

2. For each database that you are importing, create the database with the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement:

```
CREATE DATABASE inventory;
```

3. For each table that you are importing, create the table with the [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement:

```
CREATE TABLE inventory.products (
   product_name varchar(11) NOT NULL DEFAULT '',
   supplier varchar(128) NOT NULL DEFAULT '',
   quantity varchar(128) NOT NULL DEFAULT '',
   unit_cost varchar(128) NOT NULL DEFAULT ''
) ENGINE=Columnstore DEFAULT CHARSET=utf8;
```

{% hint style="info" %}
**Note:** To get the best performance from Enterprise ColumnStore, make sure to follow Enterprise ColumnStore's best practices for schema design.
{% endhint %}

## Appends Data

When MariaDB Enterprise ColumnStore performs a bulk data load, it appends data to the table in the order in which the data is read. Appending data reduces the I/O requirements of bulk data loads, so that larger data sets can be loaded very efficiently.

While the bulk load is in progress, the newly appended data is temporarily hidden from queries.

After the bulk load is complete, the newly appended data is visible to queries.

## Sort the Input File

When MariaDB Enterprise ColumnStore performs a bulk data load, it appends data to the table in the order in which the data is read.

The order of data can have a significant effect on performance with Enterprise ColumnStore, so it can be helpful to sort the data in the input file prior to importing it.

For additional information, see "[Load Ordered Data in Proper Order](../../high-availability/columnstore-query-tuning/query-tuning-recommendations-for-mariadb-enterprise-columnstore.md#load-ordered-data-in-proper-order)".

## Confirm the Field Delimiter

Before importing a file into MariaDB Enterprise ColumnStore, confirm that the field delimiter is not present in the data.

The default field delimiter for the cpimport tool is a pipe (|).

To use a different delimiter, you can set the field delimiter.

## Import from Text Files

The cpimport tool can import data from a text file if a file is provided as an argument after the database and table name.

For example, to import the file `inventory-products.txt` into the products table in the inventory database:

```
$ sudo cpimport \
   inventory products \
   inventory-products.txt
```

## Import from Binary Files

The cpimport tool can import data from a binary file if the `-I1 or -I2` option is provided and a file is provided as an argument after the database and table name.

For example, to import the file `inventory-products.bin` into the products table in the inventory database:

```
$ sudo cpimport -I1 \
   inventory products \
   inventory-products.bin
```

The `-I1 and -I2` options allow two different binary import modes to be selected:

| Option | Description                                                                                  |
| ------ | -------------------------------------------------------------------------------------------- |
| Option | Description                                                                                  |
| -I1    | Numeric fields containing NULL will be treated as NULL unless the column has a default value |
| -I2    | Numeric fields containing NULL will be saturated                                             |

The binary file should use the following format for data:

| Data Type(s) | Format                                                                                                                                                                                                                                   |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Type(s) | Format                                                                                                                                                                                                                                   |
| BIGINT       | Little-endian integer format Signed NULL: 0x8000000000000000ULL Unsigned NULL: 0xFFFFFFFFFFFFFFFEULL                                                                                                                                     |
| CHAR         | String padded with '0' to match the length of the field NULL: '0' for the full length of the field                                                                                                                                       |
| DATE         | Use the format represented by the struct Date NULL: 0xFFFFFFFE                                                                                                                                                                           |
| DATETIME     | Use the format represented by the struct DateTime NULL: 0xFFFFFFFFFFFFFFFEULL                                                                                                                                                            |
| DECIMAL      | Use an integer representation of the value without the decimal point Sizing depends on precision: \* 1-2: use 2 bytes \* 3-4: use 3 bytes \* 4-9: use 4 bytes \* 10+: use 8 bytes Signed and unsigned NULL: See equivalent-sized integer |
| DOUBLE       | Native IEEE floating point format NULL: 0xFFFAAAAAAAAAAAAAULL                                                                                                                                                                            |
| FLOAT        | Native IEEE floating point format NULL: 0xFFAAAAAA                                                                                                                                                                                       |
| INT          | Little-endian integer format Signed NULL: 0x80000000 Unsigned NULL: 0xFFFFFFFE                                                                                                                                                           |
| SMALLINT     | Little-endian integer format Signed NULL: 0x8000 Unsigned NULL: 0xFFFE                                                                                                                                                                   |
| TINYINT      | Little-endian integer format Signed NULL: 0x80 Unsigned NULL: 0xFE                                                                                                                                                                       |
| VARCHAR      | String padded with '0' to match the length of the field NULL: '0' for the full length of the field                                                                                                                                       |

### Binary DATE Format

In binary input files, the cpimport tool expects [DATE](https://github.com/mariadb-corporation/docs-server/blob/test/columnstore/data-import-with-mariadb-enterprise-columnstore/data-types-date/README.md) columns to be in the following format:

```
struct Date
{
  unsigned spare : 6;
  unsigned day : 6;
  unsigned month : 4;
  unsigned year : 16
};
```

### Binary DATETIME Format

In binary input files, the cpimport tool expects [DATETIME](https://github.com/mariadb-corporation/docs-server/blob/test/columnstore/data-import-with-mariadb-enterprise-columnstore/data-types-datetime/README.md) columns to be in the following format:

```
struct DateTime
{
  unsigned msecond : 20;
  unsigned second : 6;
  unsigned minute : 6;
  unsigned hour : 6;
  unsigned day : 6;
  unsigned month : 4;
  unsigned year : 16
};
```

### Import from Standard Input

The cpimport tool can import data from standard input (stdin) if no file is provided as an argument.

Importing from standard input is useful in many scenarios.

One scenario is when you want to import data from a remote database. You can use [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to query the table using the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement, and then pipe the results into the standard input of the cpimport tool:

```
$ mariadb --quick \
   --skip-column-names \
   --execute="SELECT * FROM inventory.products" \
   | cpimport -s '\t' inventory products
```

## Import from S3 using AWS CLI

The cpimport tool can import data from a file stored in a remote S3 bucket.

You can use the AWS CLI to copy the file from S3, and then pipe the contents into the standard input of the cpimport tool:

```
$ aws s3 cp --quiet s3://columnstore-test/inventory-products.csv - \
   | cpimport -s ',' inventory products
```

Alternatively, the columnstore\_info.load\_from\_s3 stored procedure can import data from S3-compatible cloud object storage.

## Set the Field Delimiter

The default field delimiter for the cpimport tool is a pipe (|).

If your data file uses a different field delimiter, you can specify the field delimiter with the -s option.

For a TSV (tab-separated values) file:

```
$ sudo cpimport -s '\t' \
   inventory products \
   inventory-products.tsv
```

For a CSV (comma-separated values) file:

```
$ sudo cpimport -s ',' \
   inventory products \
   inventory-products.csv
```

## Set the Quoting Style

By default, the cpimport tool does not expect fields to be quoted.

If your data file uses quotes around fields, you can specify the quote character with the -E option.

To load a TSV (tab-separated values) file that uses double quotes:

```
$ sudo cpimport -s '\t' -E '"' \
   inventory products \
   inventory-products.tsv
```

To load a CSV (comma-separated values) file that uses optional single quotes:

```
$ sudo cpimport -s ',' -E "'" \
   inventory products \
   inventory-products.csv
```

## Logging

The cpimport tool writes logs to different directories, depending on the Enterprise ColumnStore version:

* In Enterprise ColumnStore 5.5.2 and later, logs are written to /var/log/mariadb/columnstore/bulk/
* In Enterprise ColumnStore 5 releases before 5.5.2, logs are written to /var/lib/columnstore/data/bulk/
* In Enterprise ColumnStore 1.4, logs are written to /usr/local/mariadb/columnstore/bulk/

## Special Handling

### Column Order

The cpimport tool requires column values to be in the same order in the input file as the columns in the table definition.

### Date Format

The cpimport tool requires [DATE](https://github.com/mariadb-corporation/docs-server/blob/test/columnstore/data-import-with-mariadb-enterprise-columnstore/data-types-date/README.md) values to be specified in the format YYYY-MM-DD.

### Transaction Log

The cpimport tool does not write bulk data loads to the transaction log, so they are not transactional.

### Binary Log

The cpimport tool does not write bulk data loads to the binary log, so they cannot be replicated using [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication).

### EFS Storage

When Enterprise ColumnStore uses object storage and the Storage Manager directory uses EFS in the default Bursting Throughput mode, the cpimport tool can have performance problems if multiple data load operations are executed consecutively. The performance problems can occur because the Bursting Throughput mode scales the rate relative to the size of the file system, so the burst credits for a small Storage Manager volume can be fully consumed very quickly.

When this problem occurs, some solutions are:

* Avoid using burst credits by using Provisioned Throughput mode instead of Bursting Throughput mode
* Monitor burst credit balances in AWS and run data load operations when burst credits are available
* Increase the burst credit balance by increasing the file system size (for example, by creating a dummy file)

Additional information is available [here](../data-ingestion/columnstore-bulk-data-loading.md#cpimport-modes).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
