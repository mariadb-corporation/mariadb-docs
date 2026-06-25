# MariaDB Direct Query Adapter For Microsoft Power BI

MariaDB Direct Query Adapter for Power BI enables Microsoft Power BI Desktop users to remotely connect to and query their MariaDB database including on MariaDB Cloud without downloading the entire data set to their local machine.

MariaDB Direct Query Adapter is a Microsoft certified connector for Microsoft Power BI Desktop.

## About

Microsoft Power BI Desktop is a free business intelligence tool available as a downloadable desktop client. Built for analysts, Microsoft Power BI provides state-of-the-art interactive visualizations, with industry-leading data query and modeling built-in. It is one of the top business intelligence tools in use globally.

MariaDB database products support analytics and data warehousing in addition to transactional databases. Customers can meet the challenges from complex workloads using a single stack. MariaDB Enterprise Server includes pluggable smart storage engines to meet specific workload needs and connectors for high-performance data access by applications.

[MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore) is a columnar storage engine designed to handle the extremely large data sets and ad hoc queries of analytical workloads. Data is written to disk by column rather than row and is automatically partitioned. Columnar data storage is designed to deliver real time analysis on billions of rows. MariaDB Enterprise ColumnStore is a plugin storage engine and is included with MariaDB Enterprise Server.

MariaDB Direct Query Adapter enables Power BI users to work with remote data without the need to download it onto the local machine. Downloading analytical data sets can present challenges such as download speed and inadequate memory on a local machine, and even a powerful laptop or desktop is outperformed by the processing power of a high end server or MPP system. MariaDB's Direct Query Adapter enables users to avoid these limitations and provides robust querying and data visualization from any location.

## Requirements

MariaDB Direct Query Adapter for Microsoft Power BI requires:

* [Microsoft Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494)
* [MariaDB ODBC Connector v3.1.10 or later](https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector).

## Download and Install

To use MariaDB Direct Query Adapter with Microsoft Power BI Desktop:

1. Check the [system requirements for Microsoft Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494).
2. Download [Microsoft Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494) using the Microsoft instructions.
3. Download [MariaDB ODBC Connector](https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector).
4. Select MariaDB ODBC Connector v3.1.10 or later for Windows.
5. Click on the download or choose "Open" to start the MariaDB ODBC Connector Setup Wizard.
6. Click "Next".
7. Read and accept the terms and agreement.
8. Click "Next".
9. Choose "Typical" for installation type and click "Install".
10. When asked if you want to allow this app to makes changes to your device, click "Yes".
11. If you have older versions of MariaDB ODBC Connector 64-bit, select "Make User DSN's for older Connector version to use this version" and click "Finish". Otherwise, just click "Finish".

## Connect

Connect to your remote MariaDB database from Power BI Desktop using the MariaDB Direct Query Adapter.

1. Open Microsoft Power BI Desktop.
2. From the Power BI home screen, choose Get Data->More. Enter "MariaDB". Select MariaDB from the menu and click "Connect".
3. Enter the data source. This is an IP address and port number, or in the case of MariaDB Cloud, it is the qualified domain name and port number.
4. Select "DirectQuery" and click "OK".
5. Enter your user name and password and click "Connect".

You are now connected to your remote MariaDB database and can use Microsoft Power BI to run queries without the need to download the data locally.

## Queries

The MariaDB Direct Query Adapter for Power BI interacts with the SQL layer. It is upstream of the storage engine, so queries can be done regardless of the underlying storage engine.

For example, MariaDB Direct Query Adapter for Microsoft Power BI can be used to query data on a row-based transactional database using the InnoDB storage engines or a column-based data warehouse using the MariaDB Enterprise ColumnStore storage engine to deliver real time analysis of billions of rows of data.

## Relationships

Power BI depends on relationships for data analysis. These relationships are automatically established for row-based databases, for example those using the InnoDB storage engine.

Because column-based storage engines such as MariaDB Enterprise ColumnStore do not use indexes, relationships must be set up manually. For more about creating relationships in Power BI see [Create and Manage Relationships in Power BI](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
