---
title: Analytics
description: >-
  Put a columnar MariaDB ColumnStore table next to your InnoDB tables, load it, and run reports on live data without a separate warehouse.
icon: chart-column
---

# Analytics

The `shop.products` table from the landing page lives on InnoDB, a row store built for fast single-row reads and writes. Reports work the other way. They read a few columns across millions of rows, so MariaDB ColumnStore stores each column on its own and a query touches only the columns it needs. Because every table in MariaDB Server picks its own storage engine, a ColumnStore table can sit in the same database as your InnoDB tables, and one query can join them. MariaDB ColumnStore is open source and ships with both MariaDB Community Server and MariaDB Enterprise Server. For data that outgrows one server, MariaDB Exa runs analytics on a separate cluster as part of MariaDB Enterprise Platform.

{% hint style="info" %}
Need a server with ColumnStore on it? The [single-node install guide]({analytics}/mariadb-columnstore/management/deployment/install-guide/singlenode-localstorage) sets up ColumnStore on one machine with MariaDB Enterprise Server. On MariaDB Community Server, install the `mariadb-plugin-columnstore` package (`MariaDB-columnstore-engine` on RHEL) from the MariaDB repository instead. Either setup is enough for everything below.
{% endhint %}

## Report on Live Data in Three Steps

{% stepper %}
{% step %}
### Create a ColumnStore Table

Add a `sales` table to the `shop` database and set `ENGINE=ColumnStore`. ColumnStore tables don't use primary keys or indexes the way InnoDB tables do, so every column is a plain value.

```sql
CREATE TABLE shop.sales (
  sale_id    INT,
  product_id INT,
  sale_date  DATE,
  quantity   INT,
  price      DECIMAL(8,2)
) ENGINE=ColumnStore;
```

The [ColumnStore quickstart]({analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide) explains the architecture behind the engine.
{% endstep %}

{% step %}
### Bulk Load It With cpimport

The `cpimport` tool ships with ColumnStore and writes straight to the column files, skipping the SQL layer. It reads pipe-delimited text by default. On the server host, write a small file and load it.

```bash
printf '1|1|2026-09-01|2|39.00\n2|2|2026-09-01|1|249.00\n3|3|2026-09-02|10|4.50\n4|1|2026-09-03|3|39.00\n' > sales.txt

sudo cpimport shop sales sales.txt
```

Read queries keep running while the load is in progress. If your order history already sits in an InnoDB table, an `INSERT INTO shop.sales SELECT ...` statement run outside a transaction becomes the same bulk load. See [Data Loading with cpimport]({analytics}/mariadb-columnstore/clients-and-tools/data-import/mariadb-enterprise-columnstore-data-loading-with-cpimport) and [Data Loading with INSERT .. SELECT]({analytics}/mariadb-columnstore/clients-and-tools/data-import/mariadb-enterprise-columnstore-data-loading-with-insert-select).
{% endstep %}

{% step %}
### Join Across Engines

Revenue per product needs the sales figures from ColumnStore and the product names from InnoDB. One `SELECT` reads both:

```sql
SELECT p.name, SUM(s.quantity * s.price) AS revenue
FROM shop.sales AS s
JOIN shop.products AS p ON p.id = s.product_id
GROUP BY p.name
ORDER BY revenue DESC;
```

ColumnStore reaches the InnoDB table through a cross-engine connection, which you configure once with the `mcsSetConfig CrossEngineSupport` commands in [Start and Configure ColumnStore]({analytics}/mariadb-columnstore/management/deployment/install-guide/singlenode-localstorage/step-3-start-and-configure-enterprise-columnstore).
{% endstep %}
{% endstepper %}

## Columnar Engines

Start with ColumnStore on one server. When the data outgrows it, look at Exa.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>ColumnStore Quickstart</strong></td><td>How the columnar engine stores, compresses, and scans data, with more table and query examples.</td><td><a href="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide">mariadb-columnstore-guide</a></td></tr><tr><td><strong>ColumnStore Hardware</strong></td><td>Size memory, disk, and CPU cores before you pick machines, since scan throughput depends on all of them.</td><td><a href="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-hardware-guide">mariadb-columnstore-hardware-guide</a></td></tr><tr><td><strong>Deploy MariaDB Exa</strong></td><td>Spread analytical queries across a cluster for the largest data volumes.</td><td><a href="{analytics}/mariadb-exa/deployment">deployment</a></td></tr></tbody></table>

## Analytics Next to Transactions

Keep writes on InnoDB and run reports from a columnar engine, in the same database or the same MariaDB Cloud account.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>HTAP on MariaDB Cloud</strong></td><td>Pair a transactional MariaDB Cloud service with MariaDB Exa for analytics on the same data.</td><td><a href="{mariadb-cloud}/quickstart/htap-mariadb-exa">htap-mariadb-exa</a></td></tr><tr><td><strong>Choose a Storage Engine</strong></td><td>Match each table to how your application reads and writes it.</td><td><a href="{server}/server-usage/storage-engines/choosing-the-right-storage-engine">choosing-the-right-storage-engine</a></td></tr><tr><td><strong>HTAP Quickstart App</strong></td><td>A Docker walkthrough on GitHub that loads flight data into InnoDB and ColumnStore tables and joins across them.</td><td><a href="https://github.com/mariadb-developers/mariadb-htap-quickstart">mariadb-htap-quickstart</a></td></tr></tbody></table>
