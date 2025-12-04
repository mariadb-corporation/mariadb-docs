# Sharded MariaDB Enterprise Spider Topology Add a Shard

## Overview

In a Sharded MariaDB Enterprise Spider topology, new shards can be added using the following procedure.

## Create Spider User

Each data node requires a user account that the Spider Node uses to connect.

On the Data Node hosting the new shard, create the Spider user account for the Spider Node using the [CREATE USER](../../../../../../reference/sql-statements/account-management-sql-statements/create-user.md) statement:

```sql
CREATE USER spider_user@192.0.2.1 IDENTIFIED BY "password";
```

Privileges are granted to the user account in a later step.

## Test Spider User

On the Spider Node, confirm that the Spider user account can connect to the Data Node using [MariaDB Client](../../../../../../clients-and-utilities/mariadb-client/):

```
$ mariadb --user spider_user --host 192.0.2.2 --password
```

## Configure Connection Details

The Spider Node requires connection details for each Data Node.

On the Spider Node, create a server object to configure the connection details for the Data Node hosting the new shard using the [CREATE SERVER](../../../../../../reference/sql-statements/data-definition/create/create-server.md) statement:

```sql
CREATE SERVER southern_server
   FOREIGN DATA WRAPPER mariadb
OPTIONS (
   HOST '192.0.2.6',
   PORT 5004,
   USER 'spider_user',
   PASSWORD 'password',
   DATABASE 'southern_sales'
);
```

The Data Node runs MariaDB Enterprise Server, so the `FOREIGN DATA WRAPPER` is set to mariadb.

Using a server object for connection details is optional. Alternatively, the connection details for the Data Node can be specified in the `COMMENT` table option of the [CREATE TABLE](../../../../../../reference/sql-statements/data-definition/create/create-table.md) statement when creating the Spider Table.

## Create the Data Table

When queries read and write to a Spider Table, Spider reads and writes to the Data Tables for each partition on the Data Nodes. The Data Tables must be created on the Data Nodes with the same structure as the Spider Table.

If your Data Tables already exist, grant privileges on the tables to the Spider user.

On the Data Node hosting the new shard, create the Data Tables:

```sql
CREATE DATABASE southern_sales;

CREATE SEQUENCE southern_sales.invoice_seq;

CREATE TABLE southern_sales.invoices (
   branch_id INT NOT NULL DEFAULT (4) CHECK (branch_id=4),
   invoice_id INT NOT NULL DEFAULT (NEXT VALUE FOR hq_sales.invoice_seq),
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(branch_id, invoice_id)
) ENGINE=InnoDB;

INSERT INTO southern_sales.invoices
   (customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, '2020-05-25 10:22:11', 2083.56, 'CREDIT_CARD'),
   (2, '2020-05-25 11:42:33', 515.22, 'WIRE_TRANSFER'),
   (3, '2020-05-25 13:15:16', 1213.80, 'CASH');
```

The Spider Node reads and writes to the Data Table using the server and user account configured previously. The user account must have privileges on the table.

## Grant Privileges

The Spider Node connects to the Data Nodes with the user account configured previously.

On the Data Node hosting the new shard, grant the Spider user sufficient privileges to operate on the Data Table:

```sql
GRANT ALL PRIVILEGES ON southern_sales.invoices TO 'spider_user'@'192.0.2.1';
```

### Privileges for Spider BKA Mode

By default, the Spider user also requires the [CREATE TEMPORARY TABLES](../../../../../../reference/sql-statements/data-definition/create/create-table.md) privilege on the database containing the Data Table. The [CREATE TEMPORARY TABLES](../../../../../../reference/sql-statements/data-definition/create/create-table.md) privilege is required, because Spider uses temporary tables to optimize read queries when Spider BKA Mode is 1.

Spider BKA Mode is configured using the following methods:

* The session value is configured by setting the [Spider BKA Mode](../../../spider-system-variables.md#spider_bka_mode) system variable on the Spider Node. The default value is -1. When the session value is -1, the value for each Spider Table is used.
* The value for each Spider Table is configured by setting the [bka\_mode](../../../spider-system-variables.md#spider_bka_mode) option in the COMMENT table option. When the bka\_mode option is not set, the implicit value is 1.

The default spider\_bka\_mode value is -1, and the implicit Spider Table value is 1, so the default [Spider BKA Mode](../../../spider-system-variables.md#spider_bka_mode) is 1.

On the Data Node hosting the new shard, grant the Spider user the [CREATE TEMPORARY TABLES](../../../../../../reference/sql-statements/data-definition/create/create-table.md) privilege on the database:

```sql
GRANT CREATE TEMPORARY TABLES ON southern_sales.* TO 'spider_user'@'192.0.2.1';
```

## Alter the Spider Table

A partition for the new shard must be added to the Spider Table on the Spider Node.

On the Spider Node, alter the Spider Table to add the partition and reference the name of the Data Node hosting the new shard in the COMMENT partition option:

```sql
ALTER TABLE spider_sharded_sales.invoices
   ADD PARTITION (
      PARTITION southern_partition VALUES IN (4) COMMENT = 'server "southern_server", table "invoices"'
   );
```

## Test Read Operations

On the Spider Node, read from the Spider Table using a [SELECT](../../../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement:

```sql
SELECT * FROM spider_sharded_sales.invoices;
```

```
+-----------+------------+-------------+----------------------------+---------------+----------------+
| branch_id | invoice_id | customer_id | invoice_date               | invoice_total | payment_method |
+-----------+------------+-------------+----------------------------+---------------+----------------+
|         1 |          1 |           1 | 2020-05-10 12:35:10.000000 |       1087.23 | CREDIT_CARD    |
|         1 |          2 |           2 | 2020-05-10 14:17:32.000000 |       1508.57 | WIRE_TRANSFER  |
|         1 |          3 |           3 | 2020-05-10 14:25:16.000000 |        227.15 | CASH           |
|         2 |          1 |           2 | 2020-05-10 12:31:00.000000 |       1351.04 | CREDIT_CARD    |
|         2 |          2 |           2 | 2020-05-10 12:45:27.000000 |        162.11 | WIRE_TRANSFER  |
|         2 |          3 |           4 | 2020-05-10 13:11:23.000000 |        350.00 | CASH           |
|         3 |          1 |           5 | 2020-05-10 12:31:00.000000 |        111.50 | CREDIT_CARD    |
|         3 |          2 |           8 | 2020-05-10 12:45:27.000000 |       1509.23 | WIRE_TRANSFER  |
|         3 |          3 |           3 | 2020-05-10 13:11:23.000000 |       3301.66 | CASH           |
|         4 |          1 |           1 | 2020-05-25 10:22:11.000000 |       2083.56 | CREDIT_CARD    |
|         4 |          2 |           2 | 2020-05-25 11:42:33.000000 |        515.22 | WIRE_TRANSFER  |
|         4 |          3 |           3 | 2020-05-25 13:15:16.000000 |       1213.80 | CASH           |
+-----------+------------+-------------+----------------------------+---------------+----------------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
