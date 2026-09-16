---
title: ColumnStore
description: >-
  MariaDB ColumnStore is a columnar storage engine for analytical
  queries. It requires MariaDB Enterprise Server.
icon: table-columns
---

# ColumnStore

MariaDB ColumnStore is a columnar storage engine for MariaDB Enterprise Server. It stores each column separately rather than storing complete rows together, so a query reads only the columns it references. For an analytical query that touches four columns of a hundred column table, that is a large reduction in the data read. Columnar storage also compresses well, because every column holds values of one kind.

{% hint style="info" %}
MariaDB ColumnStore requires MariaDB Enterprise Server.
{% endhint %}

In either of the shapes below it can be distributed across a cluster of servers, so one query runs in parallel across all of them, which is what takes it to datasets a single server cannot answer against.

It runs two ways. As a standalone analytics deployment it holds the analytical data itself. Alongside MariaDB Enterprise Server it acts as a query accelerator, reading InnoDB data in near real time and answering analytical queries directly from operational tables, which removes the batch export that would otherwise sit between the two. Because MariaDB Server allows different storage engines for different tables in one database, adopting ColumnStore does not mean moving your transactional tables.

**Install and connect.** ColumnStore installs from the MariaDB Enterprise repository and can run on one server or across a cluster. Size the hardware before you commit, because analytical throughput depends far more on memory, disk bandwidth, and core count than transactional workloads do.

**Configure and secure it.** The guides cover the configuration that governs how data is distributed and how queries are parallelized, plus the access controls for a store that usually holds your whole reporting dataset.

**Understand the execution model.** The concepts pages cover columnar storage, extent elimination, and parallel query execution, which together explain why some queries are dramatically faster and others are not.

Load a copy of your own reporting data and compare query times against your current setup before planning a deployment.

{% content-ref url="{analytics}/mariadb-columnstore/columnstore-quickstart-guides" %}
[Quickstart Guides]({analytics}/mariadb-columnstore/columnstore-quickstart-guides)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/architecture" %}
[Architecture]({analytics}/mariadb-columnstore/architecture)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/management" %}
[Management]({analytics}/mariadb-columnstore/management)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/security" %}
[Security]({analytics}/mariadb-columnstore/security)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/use-cases" %}
[Use Cases]({analytics}/mariadb-columnstore/use-cases)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/high-availability" %}
[High Availability]({analytics}/mariadb-columnstore/high-availability)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/clients-and-tools" %}
[Clients & Tools]({analytics}/mariadb-columnstore/clients-and-tools)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/tutorials" %}
[Tutorials]({analytics}/mariadb-columnstore/tutorials)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-columnstore/reference" %}
[Reference]({analytics}/mariadb-columnstore/reference)
{% endcontent-ref %}
