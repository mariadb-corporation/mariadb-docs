# Step 2: Configure Spider Node and Data Nodes

## Overview

This page details step 2 of the 3-step procedure "[Deploy Spider Sharded Topology](./)".

This step configures the Spider Node and Data Nodes and creates the Spider Table and Data Tables.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Create Spider User

The data node requires a user account that the Spider Node uses to connect.

**On each Data Node**, create the Spider user account for the Spider Node using the [CREATE USER](../../../reference/sql-statements/account-management-sql-statements/create-user.md) statement:

```sql
CREATE USER spider_user@192.0.2.1 IDENTIFIED BY "password";
```

Privileges will be granted to the user account in [Grant Privileges on the Data Table](step-2-configure-spider-node-and-data-nodes.md#grant-privileges).

## Test Spider User

**On the Spider Node**, confirm that the Spider user account can connect to the Data Node using MariaDB Client:

```bash
$ mariadb --user spider_user --host 192.0.2.2 --password
```

## Configure Connection Details

The Spider Node requires connection details for each Data Node.

**On the Spider Node**, create a server object to configure the connection details for each Data Node using the [CREATE SERVER](../../../reference/sql-statements/data-definition/create/create-server.md) statement:

1.  Create a Server object to configure the connection details for the Data Node at the headquarters branch:\\

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
2.  Create a server object to configure the connection details for the Data Node at the eastern branch:\\

    ```sql
    CREATE SERVER eastern_server
    FOREIGN DATA WRAPPER mariadb
    OPTIONS (
       HOST "192.0.2.3",
       PORT 5801,
       USER "spider_user",
       PASSWORD "password",
       DATABASE "eastern_sales"
    );
    ```
3.  Create a server object to configure the connection details for the Data Node at the western branch:

    ```sql
    CREATE SERVER western_server
    FOREIGN DATA WRAPPER mariadb
    OPTIONS (
       HOST "192.0.2.4",
       PORT 5801,
       USER "spider_user",
       PASSWORD "password",
       DATABASE "western_sales"
    );
    ```

The Data Node runs MariaDB Enterprise Server, so the `FOREIGN DATA WRAPPER` is set to `mariadb`.

Using a server object for connection details is optional. Alternatively, the connection details for the Data Node can be specified in the `COMMENT` table option of the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement when [creating the Spider Table](step-2-configure-spider-node-and-data-nodes.md#create-the-spider-table).

## Create the Data Tables

When queries read and write to a Spider Table, Spider reads and writes to the Data Tables for each partition on the on the Data Nodes. The Data Tables must be created on the Data Nodes with the same structure as the [Spider Table](step-2-configure-spider-node-and-data-nodes.md#create-the-spider-table).

If your Data Tables already exist, [grant privileges on the tables](step-2-configure-spider-node-and-data-nodes.md#grant-privileges) to the Spider user.

**On each Data Node**, create the Data Tables:

1.  On the Data Node for the headquarters server, create a database and table and add sample data:

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

    \
    The Spider Node reads and writes to the Data Table using the server and user account configured in "[Configure Connection Details](step-2-configure-spider-node-and-data-nodes.md#configure-connection-details)". The user account must have [privileges on the tables](step-2-configure-spider-node-and-data-nodes.md#grant-privileges).
2.  On the Data Node for the eastern branch of the business, create a database and table and add sample data:\\

    ```sql
    CREATE DATABASE eastern_sales;

    CREATE SEQUENCE eastern_sales.invoice_seq;

    CREATE TABLE eastern_sales.invoices (
       branch_id INT NOT NULL DEFAULT (2) CHECK (branch_id=2),
       invoice_id INT NOT NULL DEFAULT (NEXT VALUE FOR eastern_sales.invoice_seq),
       customer_id INT,
       invoice_date DATETIME(6),
       invoice_total DECIMAL(13, 2),
       payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
       PRIMARY KEY(branch_id, invoice_id)
    ) ENGINE=InnoDB;

    INSERT INTO eastern_sales.invoices
       (customer_id, invoice_date, invoice_total, payment_method)
    VALUES
       (2, '2020-05-10 12:31:00', 1351.04, 'CREDIT_CARD'),
       (2, '2020-05-10 12:45:27', 162.11, 'WIRE_TRANSFER'),
       (4, '2020-05-10 13:11:23', 350.00, 'CASH');
    ```

    \
    The Spider Node reads and writes to the Data Table using the server and user account configured in "[Configure Connection Details](step-2-configure-spider-node-and-data-nodes.md#configure-connection-details)". The user account must have [privileges on the tables](step-2-configure-spider-node-and-data-nodes.md#grant-privileges).\\
3.  On the Data Node for the western branch of the business, create a database and table and add sample data:\\

    ```sql
    CREATE DATABASE western_sales;

    CREATE SEQUENCE western_sales.invoice_seq;

    CREATE TABLE western_sales.invoices (
       branch_id INT NOT NULL DEFAULT (3) CHECK (branch_id=3),
       invoice_id INT NOT NULL DEFAULT (NEXT VALUE FOR western_sales.invoice_seq),
       customer_id INT,
       invoice_date DATETIME(6),
       invoice_total DECIMAL(13, 2),
       payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
       PRIMARY KEY(branch_id, invoice_id)
    ) ENGINE=InnoDB;

    INSERT INTO western_sales.invoices
       (customer_id, invoice_date, invoice_total, payment_method)
    VALUES
       (5, '2020-05-10 12:31:00', 111.50, 'CREDIT_CARD'),
       (8, '2020-05-10 12:45:27', 1509.23, 'WIRE_TRANSFER'),
       (3, '2020-05-10 13:11:23', 3301.66, 'CASH');
    ```

    \
    The Spider Node reads and writes to the Data Table using the server and user account configured in "[Configure Connection Details](step-2-configure-spider-node-and-data-nodes.md#configure-connection-details)". The user account must have [privileges on the tables](step-2-configure-spider-node-and-data-nodes.md#grant-privileges).\\

## Grant Privileges

The Spider Node connects to the Data Nodes with the user account configured in "[Create Spider User](step-2-configure-spider-node-and-data-nodes.md#create-spider-user)".

**On each Data Node**, grant the Spider user sufficient privileges to operate on the Data Table:

```sql
GRANT ALL PRIVILEGES ON hq_sales.invoices TO 'spider_user'@'192.0.2.1';
```

### Privileges for Spider BKA Mode

By default, the Spider user also requires the `CREATE TEMPORARY TABLES` privilege on the database containing the Data Table. The `CREATE TEMPORARY TABLES` privilege is required, because Spider uses temporary tables to optimize read queries when Spider BKA Mode is `1`.

Spider BKA Mode is configured using the following methods:

* The session value is configured by setting the [spider\_bka\_mode](../../../server-usage/storage-engines/spider/spider-system-variables.md#spider_bka_mode) system variable on the Spider Node. The default value is `-1`. When the session value is `-1`, the value for each [Spider Table](step-2-configure-spider-node-and-data-nodes.md#create-the-spider-table) is used.
* The value for each Spider Table is configured by setting the `bka_mode` option in the `COMMENT` table option. When the `bka_mode` option is not set, the implicit value is 1.

The default [spider\_bka\_mode](../../../server-usage/storage-engines/spider/spider-system-variables.md#spider_bka_mode) value is `-1`, and the implicit Spider Table value is `1`, so the default Spider BKA Mode is `1`.

**On the Data Node**, grant the Spider user the `CREATE TEMPORARY TABLES` privilege on the database:

```sql
GRANT CREATE TEMPORARY TABLES ON hq_sales.* TO 'spider_user'@'192.0.2.1';
```

## Create the Spider Table

The Spider Table must be created on the Spider Node with the same structure as the [Data Tables](step-2-configure-spider-node-and-data-nodes.md#create-the-data-tables). The Spider Table must have a partition for each Data Table.

**On the Spider Node**, create the Spider Table and reference the Data Node in the `COMMENT` table option:

```sql
CREATE DATABASE spider_sharded_sales;

CREATE TABLE spider_sharded_sales.invoices (
   branch_id INT NOT NULL,
   invoice_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(branch_id, invoice_id)
) ENGINE=Spider
PARTITION BY LIST(branch_id) (
   PARTITION hq_partition VALUES IN (1) COMMENT = 'server "hq_server", table "invoices"',
   PARTITION eastern_partition VALUES IN (2) COMMENT = 'server "eastern_server", table "invoices"',
   PARTITION western_partition VALUES IN (3) COMMENT = 'server "western_server", table "invoices"'
);
```

The `COMMENT` partition option is used to configure the Data Node and the Data Table for each partition. Set the server option to the server object for the partition configured in "[Configure Connection Details](step-2-configure-spider-node-and-data-nodes.md#configure-connection-details)". Set the `table` option to the [Data Table](step-2-configure-spider-node-and-data-nodes.md#create-the-data-tables) for the partition.

An alternative syntax is available. When you don't want to create a server object, the connection details for the Data Nodes can be specified in the `COMMENT` partition option:

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

Navigation in the procedure "Deploy Spider Sharded Topology":

This page was **step 2 of 3**.

Next: Step 3: Test Spider Sharded Topology.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
