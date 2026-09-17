# Step 2: Configure Spider Node and Data Node

## Overview

This page details step 2 of the 3-step procedure "[Deploy Spider Federated Topology](./)".

This step configures the Spider Node and Data Node and creates the Spider Table and Data Table.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Create Spider User

The data node requires a user account that the Spider Node uses to connect.

**On the Data Node**, create the Spider user account for the Spider Node using the [CREATE USER](../../../reference/sql-statements/account-management-sql-statements/create-user.md) statement:

```sql
CREATE USER spider_user@192.0.2.1 IDENTIFIED BY "password";
```

Privileges will be granted to the user account in [Grant Privileges on the Data Table](step-2-configure-spider-node-and-data-node.md#grant-privileges).

## Test Spider User

On the Spider Node, confirm that the Spider user account can connect to the Data Node using MariaDB Client:

```bash
$ mariadb --user spider_user --host 192.0.2.2 --password
```

## Configure Connection Details

The Spider Node requires connection details for the Data Node.

On the Spider Node, create a server object to configure the connection details for the Data Node using the [CREATE SERVER](../../../reference/sql-statements/data-definition/create/create-server.md) statement:

```sql
CREATE SERVER hq_server
FOREIGN DATA WRAPPER mariadb
OPTIONS (
   HOST "192.0.2.2",
   PORT 5801,
   USER "spider_user",
   PASSWORD "password",
   DATABASE "hq_sales"
);
```

The Data Node runs MariaDB Enterprise Server, so the `FOREIGN DATA WRAPPER` is set to `mariadb`.

Using a server object for connection details is optional. Alternatively, the connection details for the Data Node can be specified in the `COMMENT` table option of the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement when [creating the Spider Table](step-2-configure-spider-node-and-data-node.md#create-the-spider-table).

## Create the Data Table

When queries read and write to a Spider Table, Spider reads and writes to the Data Table on the Data Node. The Data Table must be created on the Data Node with the same structure as the Spider Table.

If your Data Table already exists, grant privileges on the table to the Spider user.

On the Data Node, create the Data Table:

```sql
CREATE DATABASE hq_sales;

CREATE SEQUENCE hq_sales.invoice_seq;

CREATE TABLE hq_sales.invoices (
   branch_id INT NOT NULL DEFAULT (1) CHECK (branch_id=1),
   invoice_id INT NOT NULL DEFAULT (NEXT VALUE FOR hq_sales.invoice_seq),
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(branch_id, invoice_id)
) ENGINE=InnoDB;

INSERT INTO hq_sales.invoices
   (customer_id, invoice_date, invoice_total, payment_method)
VALUES
   (1, '2020-05-10 12:35:10', 1087.23, 'CREDIT_CARD'),
   (2, '2020-05-10 14:17:32', 1508.57, 'WIRE_TRANSFER'),
   (3, '2020-05-10 14:25:16', 227.15, 'CASH');
```

The Spider Node reads and writes to the Data Table using the server and user account configured in "[Configure Connection Details](step-2-configure-spider-node-and-data-node.md#configure-connection-details)". The user account must have [privileges on the tables](step-2-configure-spider-node-and-data-node.md#grant-privileges).

## Grant Privileges

The Spider Node connects to the Data Node with the user account configured in "[Create Spider User](step-2-configure-spider-node-and-data-node.md#create-spider-user)".

**On the Data Node**, grant the Spider user sufficient privileges to operate on the Data Table:

```sql
GRANT ALL PRIVILEGES ON hq_sales.invoices TO 'spider_user'@'192.0.2.1';
```

### Privileges for Spider BKA Mode

By default, the Spider user also requires the [CREATE TEMPORARY TABLES](../../../reference/sql-statements/data-definition/create/create-table.md#create-temporary-table) privilege on the database containing the Data Table. The `CREATE TEMPORARY TABLES` privilege is required, because Spider uses temporary tables to optimize read queries when Spider BKA Mode is `1`.

Spider BKA Mode is configured using the following methods:

* The session value is configured by setting the [spider\_bka\_mode](../../../server-usage/storage-engines/spider/spider-system-variables.md#spider_bka_mode) system variable on the Spider Node. The default value is `-1`. When the session value is `-1`, the value for each [Spider Table](step-2-configure-spider-node-and-data-node.md#create-the-spider-table) is used.
* The value for each [Spider Table](step-2-configure-spider-node-and-data-node.md#create-the-spider-table) is configured by setting the `bka_mode` option in the `COMMENT` table option. When the `bka_mode` option is not set, the implicit value is `1`.

The default [spider\_bka\_mode](../../../server-usage/storage-engines/spider/spider-system-variables.md#spider_bka_mode) value is `-1`, and the implicit Spider Table value is `1`, so the default Spider BKA Mode is `1`.

On the Data Node, grant the Spider user the `CREATE TEMPORARY TABLES` privilege on the database:

```sql
GRANT CREATE TEMPORARY TABLES ON hq_sales.* TO 'spider_user'@'192.0.2.1';
```

## Create the Spider Table

The Spider Table must be created on the Spider Node with the same structure as the Data Table.

**On the Spider Node**, create the Spider Table and reference the Data Node in the `COMMENT` table option:

```sql
CREATE DATABASE spider_hq_sales;

CREATE TABLE spider_hq_sales.invoices (
   branch_id INT NOT NULL,
   invoice_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(branch_id, invoice_id)
) ENGINE=Spider
COMMENT='server "hq_server", table "invoices"';
```

The `COMMENT` table option is used to configure the Data Node and the Data Table. Set the server option to the server object configured in "[Configure Connection Details](step-2-configure-spider-node-and-data-node.md#configure-connection-details)". Set the `table` option to the [Data Table](step-2-configure-spider-node-and-data-node.md#create-the-data-table).

An alternative syntax is available. When you don't want to create a server object, the connection details for the Data Node can be specified in the `COMMENT` table option:

```sql
CREATE TABLE spider_hq_sales.invoices_alternate (
   branch_id INT NOT NULL,
   invoice_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(branch_id, invoice_id)
) ENGINE=Spider
COMMENT='table "invoices", host "192.0.2.2", port "5801", user "spider_user", password "user_password", database "hq_sales"';
```

## Next Step

Navigation in the procedure "Deploy Spider Federated Topology":

This page was step 2 of 3.

Next: Step 3: Test Spider Federated Topology.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
