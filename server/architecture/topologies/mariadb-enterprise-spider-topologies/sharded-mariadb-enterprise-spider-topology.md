# Sharded MariaDB Enterprise Spider Topology

## Sharded MariaDB Enterprise Spider Topology

## Overview

In the Sharded MariaDB Enterprise Spider topology, a Spider Node contains one or more "virtual" Spider Tables. A Spider Table does not store data. When a Spider Table is queried in this topology, the Enterprise Spider storage engine uses a MariaDB foreign data wrapper to read from and write to Data Tables on Data Nodes. The data for the Spider Table is partitioned among the Data Nodes using the regular partitioning syntax.

## Benefits

MariaDB Enterprise Spider:

* Supports a MariaDB foreign data wrapper. The MariaDB foreign data wrapper can be used to replace the older Federated and FederatedX storage engines.
* Supports an ODBC foreign data wrapper in MariaDB Enterprise Server 10.5 and later. The ODBC foreign data wrapper was backported to MariaDB Enterprise Server in a previous version. The ODBC foreign data wrapper is beta maturity. The maturity can be confirmed by querying the [information\_schema.SPIDER\_WRAPPER\_PROTOCOLS](../../../server-usage/storage-engines/spider/information-schema-spider_wrapper_protocols-table.md) table.

The Spider Sharded topology:

* Can be used to consolidate multiple tables on multiple MariaDB Enterprise Server nodes into a single "virtual" table on the Spider Node using the MariaDB foreign data wrapper.
* Can be used to partition a large table across multiple MariaDB Enterprise Server nodes for horizontal scalability using the MariaDB foreign data wrapper.
* Defines Sharded Spider Tables with MariaDB Enterprise Server's regular partitioning syntax.

## Sharded MariaDB Enterprise Spider Topology

<figure><img src="../../../.gitbook/assets/spider-sharded (1).svg" alt=""><figcaption></figcaption></figure>

In the Spider Sharded topology, a Spider Node contains one or more "virtual" Spider Tables. A Spider Table does not store data. When a Spider Table is queried in this topology, the Enterprise Spider storage engine uses a MariaDB foreign data wrapper to read from and write to Data Tables on Data Nodes. The data for the Spider Table is partitioned among the Data Nodes using the regular partitioning syntax.

The Spider Sharded topology consists of:

* One MariaDB Enterprise Server node is a Spider Node
* One or more MariaDB Enterprise Server nodes are Data Nodes

The Spider Node:

* Contains one or more partitioned Spider Tables
* Uses the Enterprise Spider storage engine plugin for Spider Tables
* Uses a MariaDB foreign data wrapper to query the Data Tables on the Data Nodes

The Data Nodes:

* Contain Data Tables for one or more partitions of the Spider Table
* Use a non-Spider storage engine for each Data Table, such as InnoDB or ColumnStore

## Term Definitions

| Term                | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Node           | A Data Node is a MariaDB Enterprise Server node that contains one or more Data Tables.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Data Table          | A Data Table stores data for a Spider Table. When a Spider Table is queried, the Enterprise Spider storage engine uses the MariaDB foreign data wrapper to read from and write to the Data Table on a Data Node. The Data Table must be created on the Data Node with the same structure as the Spider Table. The Data Table must use a non-Spider storage engine, such as [InnoDB](../../../server-usage/storage-engines/innodb/) or [ColumnStore](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/). |
| ODBC Data Source    | An ODBC Data Source relies on an ODBC Driver and an ODBC Driver Manager to query an external data source.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ODBC Driver         | An ODBC Driver is a library that integrates with a ODBC Driver Manager to query an external data source.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ODBC Driver Manager | An ODBC Driver Manager allows applications to use ODBC Drivers.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Spider Node         | A Spider Node is a MariaDB Enterprise Server node that contains one or more Spider Tables.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Spider Table        | A Spider Table is a virtual table that does not store data. When a Spider Table is queried, the [Enterprise Spider storage engine](../../../server-usage/storage-engines/spider/) uses foreign data wrappers to read from and write to Data Tables on Data Nodes or ODBC Data Sources.                                                                                                                                                                                                                                       |

## Example Use Cases

### Shard Big Tables

The Spider Sharded topology can be used to split table data into multiple shards stored on remote MariaDB Enterprise Server nodes for horizontal scalability:

* One MariaDB Enterprise Server node is configured as a Spider Node and accepts application queries.
* One or more MariaDB Enterprise Server nodes are configured as Data Nodes and store shards.

### Consolidate Data for Multi-Location Businesses

The Spider Sharded topology can be used to implement a consolidated view of multiple remote databases:

* One MariaDB Enterprise Server is configured as a Spider Node and provides a consolidated view using Spider Tables.
* One or more MariaDB Enterprise Server nodes are configured as Data Nodes and contain the local data.

## Examples

### Load Spider with Configuration File

```ini
[mariadb]
...
plugin_load_add = "ha_spider"
```

### Load Spider with INSTALL SONAME

```sql
INSTALL SONAME "ha_spider";
```

### View Foreign Data Wrappers (ES 10.5+)

```sql
SELECT * FROM information_schema.SPIDER_WRAPPER_PROTOCOLS;
```

### Create Sharded Spider Table

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
   invoice_total DECIMAL(13, 2)
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(branch_id, invoice_id)
) ENGINE=Spider
PARTITION BY LIST(branch_id) (
   PARTITION hq_partition VALUES IN (1) COMMENT = 'server "hq_server", table "invoices"',
   PARTITION eastern_partition VALUES IN (2) COMMENT = 'server "eastern_server", table "invoices"',
   PARTITION western_partition VALUES IN (3) COMMENT = 'server "western_server", table "invoices"'
);
```

## Resources

### Deployment

* [Deploy MariaDB Enterprise Spider](/broken/spaces/aEnK0ZXmUbJzqQrTjFyb/pages/BbZ3TNWsYNwHXVyiSQ6z#spider-topologies)

### Schema Design

* [Schema Design](../../../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-schema-design.md)

### Operations

* [Operations](../../../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-operations/federated-mariadb-enterprise-spider-topology-operations/)
* [Add a Shard](../../../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-operations/sharded-mariadb-enterprise-spider-topology-operations/sharded-mariadb-enterprise-spider-topology-add-a-shard.md)
* [Backup and Restore](../../../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-operations/federated-mariadb-enterprise-spider-topology-operations/federated-mariadb-enterprise-spider-topology-backup-and-restore.md)

### Storage Engines

* [Enterprise Spider Storage Engine](../../../server-usage/storage-engines/spider/)

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
