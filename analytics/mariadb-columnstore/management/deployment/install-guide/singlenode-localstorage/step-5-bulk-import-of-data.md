---
description: 'Step 5: Bulk Import of Data'
---

# Step 5: Bulk Import of Data

## Overview

This page details step 5 of a 5-step procedure for deploying [Single-Node Enterprise ColumnStore with Local storage](./).

This step bulk imports data to Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Import the Schema

Before data can be imported into the tables, create a matching schema.

**On the primary server**, create the schema:

1. For each database that you are importing, create the database with the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement:

```sql
CREATE DATABASE inventory;
```

2. For each table that you are importing, create the table with the [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement:

```sql
CREATE TABLE inventory.products (
   product_name VARCHAR(11) NOT NULL DEFAULT '',
   supplier VARCHAR(128) NOT NULL DEFAULT '',
   quantity VARCHAR(128) NOT NULL DEFAULT '',
   unit_cost VARCHAR(128) NOT NULL DEFAULT ''
) ENGINE=Columnstore DEFAULT CHARSET=utf8;
```

## Import the Data

Enterprise ColumnStore supports multiple methods to import data into ColumnStore tables.

### cpimport

MariaDB Enterprise ColumnStore includes [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a TSV (tab-separated values) file, on the primary server run [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport):

```bash
$ sudo cpimport -s '\t' inventory products /tmp/inventory-products.tsv
```

### LOAD DATA INFILE

When data is loaded with the [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement, MariaDB Enterprise ColumnStore loads the data using [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a TSV (tab-separated values) file, on the primary server use [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) statement:

```sql
LOAD DATA INFILE '/tmp/inventory-products.tsv'
INTO TABLE inventory.products;
```

### Import from Remote Database

MariaDB Enterprise ColumnStore can also import data directly from a remote database. A simple method is to query the table using the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement, and then pipe the results into [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility that is designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a remote MariaDB database:

```bash
$ mariadb --quick \
   --skip-column-names \
   --execute="SELECT * FROM inventory.products" \
   | cpimport -s '\t' inventory products
```

## Next Step

Navigation in the Single-Node Enterprise ColumnStore topology with Local storage deployment procedure:

This page was step 5 of 5.

This procedure is complete.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
