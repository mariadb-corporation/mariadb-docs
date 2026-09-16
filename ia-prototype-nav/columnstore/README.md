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

It runs two ways. As a standalone analytics deployment it holds the analytical data itself. Alongside MariaDB Enterprise Server it acts as a query accelerator, reading InnoDB data in near real time and answering analytical queries directly from operational tables, which removes the batch export that would otherwise sit between the two. Because MariaDB Server allows different storage engines for different tables in one database, adopting ColumnStore does not mean moving your transactional tables.

**Install and connect.** ColumnStore installs from the MariaDB Enterprise repository and can run on one server or across a cluster. Size the hardware before you commit, because analytical throughput depends far more on memory, disk bandwidth, and core count than transactional workloads do.

**Configure and secure it.** The guides cover the configuration that governs how data is distributed and how queries are parallelized, plus the access controls for a store that usually holds your whole reporting dataset.

**Understand the execution model.** The concepts pages cover columnar storage, extent elimination, and parallel query execution, which together explain why some queries are dramatically faster and others are not.

Load a copy of your own reporting data and compare query times against your current setup before planning a deployment.

## Get Started

{% content-ref url="get-started/install-columnstore.md" %}
[install-columnstore.md](get-started/install-columnstore.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-columnstore.md" %}
[connect-to-columnstore.md](get-started/connect-to-columnstore.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/columnstore-tutorial.md" %}
[columnstore-tutorial.md](tutorials/columnstore-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-columnstore.md" %}
[configure-columnstore.md](how-to-guides/configure-columnstore.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-columnstore.md" %}
[secure-columnstore.md](how-to-guides/secure-columnstore.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-columnstore.md" %}
[what-is-columnstore.md](overview/what-is-columnstore.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-columnstore-works.md" %}
[how-columnstore-works.md](concepts/how-columnstore-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/columnstore-reference.md" %}
[columnstore-reference.md](reference/columnstore-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/columnstore-releases.md" %}
[columnstore-releases.md](release-notes/columnstore-releases.md)
{% endcontent-ref %}
