# Federated MariaDB Enterprise Spider Topology Migrate Tables

## Overview

The Federated MariaDB Enterprise Spider topology can be used to migrate tables from one MariaDB Enterprise Server node to another MariaDB Enterprise Server node:

* The MariaDB Enterprise Server node with the source table is configured as a Data Node.
* The MariaDB Enterprise Server node with the destination table is configured as a Spider Node.
* The Data Table is the source table on the Data Node.
* A Spider Table is created on the Spider Node that references the Data Table on the Data Node.
* On the Spider node, the Data Table's data is migrated to the destination table by querying the Spider Table like the following:

```sql
INSERT INTO innodb_tab
   SELECT * FROM spider_tab;
```

Follow the steps below to migrate tables using the Federated MariaDB Enterprise Spider topology.

## Deploy the Federated Topology

Before you can migrate tables, the Federated MariaDB Enterprise Spider topology must be deployed.

For additional information, see "[Deploy MariaDB Enterprise Spider](../../)".

## Create Local Tables

A local copy of the table must be created. This new table will contain the migrated data.

* On the Spider Node\*, create a local copy of each table that is being migrated:

```sql
CREATE DATABASE hq_sales;

CREATE SEQUENCE hq_sales.invoice_seq;

CREATE TABLE hq_sales.invoices (
   branch_id INT NOT NULL DEFAULT (1) CHECK (branch_id=1),
   invoice_id INT NOT NULL DEFAULT (NEXT VALUE FOR migrated_hq_sales.invoice_seq),
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(branch_id, invoice_id)
) ENGINE=InnoDB;
```

## Migrate the Tables

The table data can be migrated to the local table using the Spider Tables.

* On the Spider Node\*, migrate the table data to the local copy of the table using the [INSERT SELECT](../../../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
INSERT INTO hq_sales.invoices
   SELECT * FROM spider_hq_sales.invoices;
```

## Test Read Operations

On the Spider Node, read from the local copy of the table using a [SELECT](../../../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to confirm that the data has been migrated:

```sql
SELECT * FROM hq_sales.invoices;
```

```
+-----------+------------+-------------+----------------------------+---------------+----------------+
| branch_id | invoice_id | customer_id | invoice_date               | invoice_total | payment_method |
+-----------+------------+-------------+----------------------------+---------------+----------------+
|         1 |          1 |           1 | 2020-05-10 12:35:10.000000 |       1087.23 | CREDIT_CARD    |
|         1 |          2 |           2 | 2020-05-10 14:17:32.000000 |       1508.57 | WIRE_TRANSFER  |
|         1 |          3 |           3 | 2020-05-10 14:25:16.000000 |        227.15 | CASH           |
+-----------+------------+-------------+----------------------------+---------------+----------------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
