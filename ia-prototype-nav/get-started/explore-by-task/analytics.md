---
title: Analytics
description: >-
  Run analytical queries on MariaDB. Use the ColumnStore columnar engine, the
  Exa engine, and choose the right storage engine for reporting workloads.
icon: chart-column
---

# Analytics

Analytics is querying large amounts of data to answer questions, rather than reading and writing single rows the way a transactional application does. A row oriented storage engine is built for the second job and struggles with the first, because it has to read whole rows even when a query touches only a few columns. MariaDB offers storage engines built for the analytical job instead. This page covers the two main options, ColumnStore and Exa, and the reference that helps you decide which engine a given table belongs in. The choice matters, because putting a reporting workload on the wrong engine is the difference between a query that returns in seconds and one that returns in minutes.

ColumnStore is a columnar storage engine for MariaDB. It stores each column separately, so an analytical query reads only the columns it needs and can scan large tables quickly, and it compresses well because a column holds values of one kind. The quickstart guide sets up ColumnStore and runs a query against it, which is enough to see the difference on your own data. The hardware guide covers sizing the machines it runs on, and it is worth reading before you commit to a deployment, because analytical performance depends heavily on memory, disk throughput, and core count.

Exa is the analytical engine for the largest workloads, where a single server is no longer enough and you need to spread queries across a cluster. The deployment guide covers standing it up, which is the first concrete step in evaluating whether your workload has genuinely outgrown a single ColumnStore deployment. For many workloads ColumnStore is sufficient, so reach for Exa when the data volume or the concurrency has moved past what one machine can serve.

Not every reporting query needs a separate analytical engine. The storage engine chooser compares the options directly, from the default transactional engine to the analytical ones, so you can match each table to the engine that suits how it is queried rather than moving everything at once. If you want to evaluate the newer columnar option, the DuckDB storage engine page documents where it stands today, including the fact that it is not yet ready for production use. Read the chooser first, then the specific engine pages, so a decision to add an analytical engine is deliberate rather than a default.

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
