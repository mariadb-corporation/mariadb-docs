---
title: Analytics
description: >-
  Run analytical queries at scale with MariaDB ColumnStore and MariaDB Exa,
  and choose the right storage engine for each reporting table.
icon: chart-column
---

# Analytics

Analytical queries ask a different question than transactional ones. They scan large amounts of data across a few columns, where a row oriented engine has to read whole rows to get at them. MariaDB Enterprise Server offers columnar engines built for that access pattern, so reporting queries do not have to run against tables laid out for single row reads.

MariaDB ColumnStore and MariaDB Exa both require MariaDB Enterprise Server. Because MariaDB Server lets different tables in the same database use different storage engines, you can leave transactional tables where they are and move only the tables that are queried analytically.

**Start with ColumnStore.** ColumnStore is a columnar storage engine for MariaDB Enterprise Server. It stores each column separately, so a query reads only the columns it references, and it compresses well because every column holds one kind of value. It can run as a standalone analytics deployment or alongside MariaDB Enterprise Server as a query accelerator that reads InnoDB data in near real time, which removes the need for a separate batch pipeline. The quickstart sets it up and runs a query. The hardware guide covers sizing, and it is worth reading before you commit machines, because analytical throughput depends heavily on memory, disk bandwidth, and core count.

**Scale out with Exa.** When a single server no longer holds the data or the concurrency, Exa distributes queries across a cluster for the largest analytical workloads. Its deployment guide is the concrete first step in judging whether your volume has genuinely outgrown a single ColumnStore deployment.

**Put each table on the right engine.** The storage engine reference compares the options so you can match a table to how it is queried, and the DuckDB page covers where that newer columnar option stands today.

Run ColumnStore against a copy of your own data and compare the query times before planning anything larger.

## Run Columnar Analytics With ColumnStore

{% content-ref url="explore-by-task/%7Banalytics%7D/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide/" %}
[mariadb-columnstore-guide](explore-by-task/%7Banalytics%7D/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Banalytics%7D/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-hardware-guide/" %}
[mariadb-columnstore-hardware-guide](explore-by-task/%7Banalytics%7D/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-hardware-guide/)
{% endcontent-ref %}

## Scale Further With Exa

{% content-ref url="explore-by-task/%7Banalytics%7D/mariadb-exa/deployment/" %}
[deployment](explore-by-task/%7Banalytics%7D/mariadb-exa/deployment/)
{% endcontent-ref %}

## Choose the Right Engine

{% content-ref url="explore-by-task/%7Bserver%7D/server-usage/storage-engines/choosing-the-right-storage-engine/" %}
[choosing-the-right-storage-engine](explore-by-task/%7Bserver%7D/server-usage/storage-engines/choosing-the-right-storage-engine/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/server-usage/storage-engines/duckdb-storage-engine/" %}
[duckdb-storage-engine](explore-by-task/%7Bserver%7D/server-usage/storage-engines/duckdb-storage-engine/)
{% endcontent-ref %}
