---
description: >-
  Connect to and query MariaDB using a connector (from an application) or a
  client (interactively or from scripts).
---

# Connect and Query

Database connections are made using a **connector** (from an application) or a **client** (interactively or from scripts).

Clients and connectors listed here are supported under [MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies/).

Clients and connectors listed here are compatible with:

* MariaDB database products (including Enterprise Server and MaxScale)
* MariaDB Community Server

## MariaDB Connectors

MariaDB Connectors are available for many popular programming languages.

| Programming Language / Interface | Connector                                                                                            |
| -------------------------------- | ---------------------------------------------------------------------------------------------------- |
| C                                | [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c)            |
| C++                              | [MariaDB Connector/C++](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp)        |
| Java - JDBC                      | [MariaDB Connector/J](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j)            |
| Java - R2DBC                     | [MariaDB Connector/R2DBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-r2dbc)    |
| JavaScript                       | [MariaDB Connector/Node.js](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs) |
| ODBC                             | [MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc)      |
| Python                           | [MariaDB Connector/Python](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-python)  |

## MariaDB Client

MariaDB Client can be used interactively or within scripts.

MariaDB Client is included with distributions of MariaDB database products.

Compatible third-party clients exist but are not listed here.

| Executable Filename | Purpose                       |
| ------------------- | ----------------------------- |
| mariadb, mysql      | Connect from the command line |

For additional information about MariaDB Client, see MariaDB Client.

## Tools and Utilities

Tools and utilities listed here are included with distributions of MariaDB database products and make a client connection.

| Command-Line Executable     | Purpose                                                                       |
| --------------------------- | ----------------------------------------------------------------------------- |
| mariadb-admin, mysqladmin   | Check configuration and current status                                        |
| mariadb-backup, mariadb-backup | Create and restore physical backups (including Aria, InnoDB, MyISAM, MyRocks) |
| mariadb-binlog, mysqlbinlog | Read binary logs or relay logs                                                |
| mariadb-check, mysqlcheck   | Perform table maintenance operations                                          |
| mariadb-dump, mysqldump     | Create logical backups                                                        |
| mariadb-import, mysqlimport | Load table data from CSV, TSV, and other text file formats                    |
| mariadb-show, mysqlshow     | Display databases, tables, table columns, indexes                             |
| mariadb-slap, mysqlslap     | Generate client load for testing                                              |

## Business Intelligence (BI)

MariaDB database products are accessible from business intelligence (BI) platforms, including:

| BI Platform        | Detail                                                                                                                                                                                                                                                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Microsoft Power BI | [MariaDB Direct Query Adapter for Microsoft Power BI](../../graphical-and-enhanced-clients/mariadb-direct-query-adapter-for-microsoft-power-bi.md) enables Microsoft Power BI Desktop users to remotely connect to and query their MariaDB database, including on MariaDB MariaDB Cloud, without downloading the entire data set to their local machine. |

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
