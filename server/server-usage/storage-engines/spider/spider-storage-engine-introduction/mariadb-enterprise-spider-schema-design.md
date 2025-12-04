# MariaDB Enterprise Spider Schema Design

## Create Tables

Spider Tables can be created with MariaDB Enterprise Spider using the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement. The [Enterprise Spider storage engine](./) can be chosen for the table by specifying ENGINE=Spider.

For each Spider Table, MariaDB Enterprise Spider requires connection details for the Data Nodes. The connection details are provided by specifying [Connection Options](mariadb-enterprise-spider-schema-design.md#connection-options) in the COMMENT option for the table or partition, depending on the topology.

### Create Tables in a Federated Topology

In a Federated MariaDB Enterprise Spider topology, the [Connection Options](mariadb-enterprise-spider-schema-design.md#connection-options) are specified in the COMMENT table option for the Spider Table:

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

An alternative syntax is available. When you don't want to create a server object, the full connection details for the Data Node can be specified in the COMMENT table option:

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
COMMENT='table "invoices", host "192.0.2.2", port "5801", user "spider_user", password "password", database "hq_sales"';
```

### Create Tables in a Sharded Topology

In a Sharded MariaDB Enterprise Spider topology, the [Connection Options](mariadb-enterprise-spider-schema-design.md#connection-options) are specified in the COMMENT partition option for each partition of the Spider Table:

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

CREATE SERVER eastern_server
FOREIGN DATA WRAPPER mariadb
OPTIONS (
   HOST "192.0.2.3",
   PORT 5801,
   USER "spider_user",
   PASSWORD "password",
   DATABASE "eastern_sales"
);

CREATE SERVER western_server
FOREIGN DATA WRAPPER mariadb
OPTIONS (
   HOST "192.0.2.4",
   PORT 5801,
   USER "spider_user",
   PASSWORD "password",
   DATABASE "western_sales"
);

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

An alternative syntax is available. When you don't want to create a server object, the full connection details for the Data Nodes can be specified in the COMMENT partition option:

```sql
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
   PARTITION hq_partition VALUES IN (1) COMMENT = 'table "invoices", host "192.0.2.2", port 5801, user "spider_user", password "password", database "hq_sales"',
   PARTITION eastern_partition VALUES IN (2) COMMENT = 'table "invoices", host "192.0.2.3", port 5801, user "spider_user", password "password", database "eastern_sales"',
   PARTITION western_partition VALUES IN (3) COMMENT = 'table "invoices", host "192.0.2.4", port 5801, user "spider_user", password "password", database "western_sales"'
);
```

## Connection Options

The following connection options are supported in the COMMENT table option for Federated Spider Tables and in the COMMENT partition option for Sharded Spider Tables:

| Option      | Data Type | Definition                                                                                                             |
| ----------- | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| database    | String    | The database to select when connecting to the Data Node.                                                               |
| host        | String    | The hostname or IP address for the Data Node. This option is mutually exclusive with socket.                           |
| password    | String    | The password to use when connecting to the Data Node.                                                                  |
| port        | Integer   | The port to use when connecting to the Data Node. This option is mutually exclusive with socket.                       |
| socket      | String    | The path to the Unix socket file to use when connecting to the Data Node. This option is mutually exclusive with port. |
| ssl\_ca     | String    | The path to the file with the TLS certificate authority chain.                                                         |
| ssl\_capath | String    | The path to the directory with the TLS certificate authority chain files.                                              |
| ssl\_cert   | String    | The path to the TLS client certificate.                                                                                |
| ssl\_key    | String    | The path to the TLS private key.                                                                                       |
| ssl\_cipher | String    | The path to the TLS certificate authority chain.                                                                       |
| table       | String    | The table to query.                                                                                                    |
| user        | String    | The username to use when connecting to the Data Node.                                                                  |
| wrapper     | String    | The foreign data wrapper should be mariadb for the Federated and Sharded topologies or odbc for the ODBC topology.     |

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
