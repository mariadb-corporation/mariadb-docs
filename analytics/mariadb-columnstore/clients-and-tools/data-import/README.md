---
description: >-
  Data import methods for MariaDB Enterprise ColumnStore: cpimport, INSERT
  INTO .. SELECT and LOAD DATA INFILE auto-translation, batch insert mode, and
  load_from_s3 from S3 cloud storage.

---

# Data Import

## Overview

MariaDB Enterprise ColumnStore supports very efficient bulk data loads.

MariaDB Enterprise ColumnStore performs bulk data loads very efficiently using a variety of mechanisms, including the cpimport tool, specialized handling of certain SQL statements, and minimal locking during data import.

## cpimport

MariaDB Enterprise ColumnStore includes a bulk data loading tool called cpimport, which provides several benefits:

* Bypasses the SQL layer to decrease overhead
* Does not block read queries
* Requires a write metadata lock on the table, which can be monitored with the [METADATA\_LOCK\_INFO plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin)
* Appends the new data to the table. While the bulk load is in progress, the newly appended data is temporarily hidden from queries. After the bulk load is complete, the newly appended data is visible to queries.
* Inserts each row in the order the rows are read from the source file. Users can optimize data loads for Enterprise ColumnStore's automatic partitioning by loading presorted data files. For additional information, see "[Load Ordered Data in Proper Order](../../high-availability/columnstore-query-tuning/query-tuning-recommendations-for-mariadb-enterprise-columnstore.md#load-ordered-data-in-proper-order)".
* Supports parallel distributed bulk loads
* Imports data from text files
* Imports data from binary files
* Imports data from standard input (stdin)

## Batch Insert Mode

MariaDB Enterprise ColumnStore enables batch insert mode by default.

When batch insert mode is enabled, MariaDB Enterprise ColumnStore has special handling for the following statements:

* \[\[|load-data-infileLOAD DATA \[ LOCAL ] INFILE]]
* [INSERT INTO .. SELECT FROM ..](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert)

Enterprise ColumnStore uses the following rules:

* If the statement is executed outside of a transaction, Enterprise ColumnStore loads the data using cpimport, which is a command-line utility that is designed to efficiently load data in bulk. It executes cpimport using a wrapper called `cpimport.bin`.
* If the statement is executed inside of a transaction, Enterprise ColumnStore loads the data using the `DML` interface, which is slower.

Batch insert mode can be disabled by setting the `columnstore_use_import_for_batchinsert` system variable to OFF. When batch insert mode is disabled, Enterprise ColumnStore executes the statements using the `DML` interface, which is slower.

## Locking

MariaDB Enterprise ColumnStore requires a write metadata lock (MDL) on the table when a bulk data load is performed with `cpimport`.

When a bulk data load is running:

* Read queries will not be blocked.
* Write queries and concurrent bulk data loads on the same table will be blocked until the bulk data load operation is complete, and the write metadata lock on the table has been released.
* The write metadata lock (MDL) can be monitored with the [METADATA\_LOCK\_INFO plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/metadata-lock-info-plugin).

## Choose a Data Load Method

| Performance | Method                                                                                                                                                                                           | Interface | Format(s)                                           | Location(s)                               | Benefits                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | --------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------- |
| Fastest     | [cpimport](mariadb-enterprise-columnstore-data-loading-with-cpimport.md)                                                                                                                         | Shell     | • Text file. • Binary file • Standard input (stdin) | • Server file system                      | Lowest latency. • Bypasses SQL layer. • Non-blocking                                    |
| Fast        | columnstore\_info.load\_from\_s3                                                                                                                                                                 | SQL       | • Text file.                                        | • S3-compatible object storage            | • Loads data from the cloud. • Translates operation to cpimport command. • Non-blocking |
| Fast        | [LOAD DATA \[ LOCAL \] INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) | SQL       | • Text file.                                        | • Server file system • Client file system | • Translates operation to cpimport command. • Non-blocking                              |
| Slow        | [INSERT .. SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert)                                                      | SQL       | • Other table(s).                                   | • Same MariaDB server                     | • Translates operation to cpimport command. • Non-blocking                              |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
