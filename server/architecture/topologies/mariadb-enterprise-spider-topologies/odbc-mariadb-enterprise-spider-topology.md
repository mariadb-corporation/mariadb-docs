# ODBC MariaDB Enterprise Spider Topology

## Overview

In the ODBC MariaDB Enterprise Spider topology, a Spider Node contains one or more "virtual" Spider Tables. A Spider Table does not store data. When the Spider Table is queried in this topology, the Enterprise Spider storage engine uses an ODBC foreign data wrapper to read from and write to an ODBC Data Source.

## Benefits

MariaDB Enterprise Spider:

* Supports a MariaDB foreign data wrapper. The MariaDB foreign data wrapper can be used to replace the older Federated and FederatedX storage engines.
* Supports an ODBC foreign data wrapper in MariaDB Enterprise Server 10.5 and later. The maturity can be confirmed by querying the [information\_schema.SPIDER\_WRAPPER\_PROTOCOLS](../../../server-usage/storage-engines/spider/information-schema-spider_wrapper_protocols-table.md) table.

The Spider ODBC topology:

* Can be used to query ODBC Data Sources from the Spider Node using the ODBC foreign data wrapper.
* Can be used to join ODBC Data Sources with tables on the Spider Node using the ODBC foreign data wrapper.
* Can be used to migrate table data from ODBC Data Sources to the Spider Node using the ODBC foreign data wrapper.

ODBC MariaDB Enterprise Spider Topology

<figure><img src="../../../.gitbook/assets/spider-federated-odbc.svg" alt=""><figcaption></figcaption></figure>

In the Spider ODBC topology, a Spider Node contains one or more "virtual" Spider Tables. A Spider Table does not store data. When the Spider Table is queried in this topology, the Enterprise Spider storage engine uses an ODBC foreign data wrapper to read from and write to an ODBC Data Source.

MariaDB Enterprise Spider implemented support for the ODBC foreign data wrapper in MariaDB Enterprise Server 10.5.

The maturity can be confirmed by querying the [information\_schema.SPIDER\_WRAPPER\_PROTOCOLS](../../../server-usage/storage-engines/spider/information-schema-spider_wrapper_protocols-table.md) table.

The Spider ODBC topology consists of:

* One MariaDB Enterprise Server node is a Spider Node
* One ODBC Data Source stores data for Spider Tables

The Spider Node:

* Contains one or more Spider Tables
* Uses the [Enterprise Spider storage engine](../../../server-usage/storage-engines/spider/) plugin for Spider Tables
* Uses an ODBC foreign data wrapper to query the ODBC Data Source

The ODBC Data Source:

* Contains the Data for each Spider Table
* Can be a non-MariaDB database server, such as Microsoft SQL Server, Oracle, or PostgreSQL

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

### Query Non-MariaDB Databases

The Spider ODBC topology can be used to query tables located on non-MariaDB databases:

* The non-MariaDB database is configured as an ODBC Data Source in the ODBC Driver Manager.
* The MariaDB Enterprise Server node that needs to query the ODBC Data Source is configured as a Spider Node.
* A Spider Table is created on the Spider Node that references the ODBC Data Source.
*   On the Spider Node, the ODBC Data Source is queried by querying the Spider Table like the following:

    ```sql
    SELECT * FROM spider_tab;
    ```
*   Local tables can also be referenced in queries:

    ```sql
    SELECT *
    FROM spider_tab s
    JOIN local_tab l
    ON s.id=l.id;
    ```

### Migrate Tables from Non-MariaDB Databases

* The Spider ODBC topology can be used to migrate tables from a non-MariaDB database to a MariaDB Enterprise Server node:
* The non-MariaDB database is configured as an ODBC Data Source in the ODBC Driver Manager.
* The MariaDB Enterprise Server node with the destination table is configured as a Spider Node.
* A Spider Table is created on the Spider Node that references the ODBC Data Source.
*   On the Spider Node, the ODBC Data Source's data is migrated to the destination table by querying the Spider Table like the following:

    ```sql
    INSERT INTO destination_tab
    SELECT * FROM spider_tab;
    ```

## Examples

### Load Spider with Configuration File (ES 10.4+)

```ini
[mariadb]
...
plugin_load_add = "ha_spider"
```

### Load Spider with INSTALL SONAME (ES 10.4+)

```sql
INSTALL SONAME "ha_spider";
```

### View Foreign Data Wrappers (ES 10.5+)

```sql
SELECT * FROM information_schema.SPIDER_WRAPPER_PROTOCOLS;
```

### Create ODBC Spider Table (with an Oracle remote server)

Follow the link under [Operations](odbc-mariadb-enterprise-spider-topology.md#operations) for further information on the setup.

```sql
INSTALL SONAME 'ha_spider';
CREATE DATABASE spider_test;
USE spider_test;
CREATE OR REPLACE TABLE contacts (
    contact_id  BIGINT NOT NULL PRIMARY KEY,
    first_name  VARCHAR(255) NOT NULL,
    last_name   VARCHAR(255) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    phone       VARCHAR(20),
    customer_id BIGINT
) ENGINE=SPIDER COMMENT='wrapper "odbc", dsn "ORARDS", table "CONTACTS"';
```

## Resources

### Schema Design

* [Schema Design](../../../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-schema-design.md)

### Operations

* [Use Spider ODBC to connect to Oracle](../../../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-operations/odbc-mariadb-enterprise-spider-topology-operations/use-spider-odbc-to-connect-to-oracle.md)

### Storage Engines

* [Enterprise Spider Storage Engine](../../../server-usage/storage-engines/spider/)

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
