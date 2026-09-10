---
title: Analytics
description: >-
  Run analytical queries at scale on MariaDB. Use the ColumnStore columnar
  engine, scale up with Exa, and choose the right storage engine for reporting.
icon: chart-column
---

# Analytics

Run fast analytical queries on your MariaDB data. Reporting and analytics ask a different question than a transactional application: they scan large amounts of data instead of reading single rows, and a row oriented engine has to read whole rows even when a query wants only a few columns. MariaDB gives you engines built for the analytical job. The guides below get you to ColumnStore, to Exa, and to the reference that helps you put each table on the right engine. It is a choice worth making, because the wrong engine turns a query that should take seconds into one that takes minutes.

**Start with ColumnStore.** ColumnStore is a columnar engine for MariaDB. It stores each column separately, so an analytical query reads only the columns it touches and scans large tables quickly, and it compresses well because each column holds one kind of value. The quickstart gets it set up and running a query, which is enough to see the difference on your own data. The hardware guide covers sizing the machines, worth reading before you commit, because analytical speed depends heavily on memory, disk throughput, and cores.

**Scale up with Exa.** When one server is no longer enough and you need to spread queries across a cluster, Exa is the engine for the largest workloads. Its deployment guide is the first concrete step in deciding whether your data volume or concurrency has truly outgrown a single ColumnStore deployment.

**Put each table on the right engine.** Not every report needs a dedicated analytical engine. The storage engine chooser compares your options so you can match a table to how it is queried, and the DuckDB page shows where that newer columnar option stands today. Because MariaDB lets different tables use different engines in the same database, you can keep your transactional tables where they are and add a columnar engine only for the tables that need it.

Try ColumnStore on your data first, then reach further only when you need to.

## Run columnar analytics with ColumnStore

{% content-ref url="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide" %}
[ColumnStore Guide]({analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-hardware-guide" %}
[ColumnStore Hardware Guide]({analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-hardware-guide)
{% endcontent-ref %}

## Scale further with Exa

{% content-ref url="{analytics}/mariadb-exa/deployment" %}
[Deploy MariaDB Exa]({analytics}/mariadb-exa/deployment)
{% endcontent-ref %}

## Choose the right engine

{% content-ref url="{server}/server-usage/storage-engines/choosing-the-right-storage-engine" %}
[Choosing the Right Storage Engine]({server}/server-usage/storage-engines/choosing-the-right-storage-engine)
{% endcontent-ref %}

{% content-ref url="{server}/server-usage/storage-engines/duckdb-storage-engine" %}
[DuckDB Storage Engine]({server}/server-usage/storage-engines/duckdb-storage-engine)
{% endcontent-ref %}
