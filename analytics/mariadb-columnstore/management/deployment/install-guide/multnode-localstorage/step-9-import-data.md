---
description: 'Step 9: Import Data'
---

# Step 9: Import Data

## Overview

This page details step 9 of the 9-step procedure "Deploy ColumnStore Shared Local Storage Topology".

This step bulk imports data to Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Import the Schema

Before data can be imported into the tables, create a matching schema.

**On the primary server**, create the schema:

1. For each database that you are importing, create the database with the CREATE DATABASE statement:

```sql
CREATE DATABASE inventory;
```

2. For each table that you are importing, create the table with the CREATE TABLE statement:

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

<table><thead><tr><th width="160">Interface</th><th width="236">Method</th><th>Benefits</th></tr></thead><tbody><tr><td>Shell</td><td><a href="step-9-import-data.md#cpimport">cpimport</a></td><td><ul><li>SQL access is not required</li></ul></td></tr><tr><td>SQL</td><td><a href="step-9-import-data.md#load-data-infile">LOAD DATA INFILE</a></td><td><ul><li>Shell access is not required</li></ul></td></tr><tr><td>Remote Database</td><td><a href="step-9-import-data.md#import-from-remote-database">Remote Database Import</a></td><td><ul><li>Use normal database client</li><li>Avoid dumping data to intermediate filed</li></ul></td></tr></tbody></table>

### cpimport

MariaDB Enterprise ColumnStore includes [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a TSV (tab-separated values) file, on the primary server run [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport):

```bash
$ sudo cpimport -s '\t' inventory products /tmp/inventory-products.tsv
```

### LOAD DATA INFILE

When data is loaded with the LOAD DATA INFILE statement, MariaDB Enterprise ColumnStore loads the data using [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a TSV (tab-separated values) file, on the primary server use LOAD DATA INFILE statement:

```sql
LOAD DATA INFILE '/tmp/inventory-products.tsv'
INTO TABLE inventory.products;
```

### Import from Remote Database

MariaDB Enterprise ColumnStore can also import data directly from a remote database. A simple method is to query the table using the SELECT statement, and then pipe the results into [cpimport](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/data-import-with-mariadb-enterprise-columnstore/mariadb-enterprise-columnstore-data-loading-with-cpimport), which is a command-line utility that is designed to efficiently load data in bulk. Alternative methods are available.

To import your data from a remote MariaDB database:

```bash
$ mariadb --quick \
   --skip-column-names \
   --execute="SELECT * FROM inventory.products" \
   | cpimport -s '\t' inventory products
```

## Next Step

Navigation in the procedure "Deploy ColumnStore Shared Local Storage Topology".

This page was step 9 of 9.

This procedure is complete.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
