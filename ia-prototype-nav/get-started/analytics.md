---
title: Analytics
description: >-
  Run analytical queries at scale with MariaDB ColumnStore and MariaDB Exa, run analytics next to transactions, and pick the right storage engine for each table.
icon: chart-column
---

# Analytics

Analytical queries read a few columns across a lot of rows. A row store like InnoDB has to read whole rows to answer them, which is why reporting queries get slow on tables built for single-row lookups. MariaDB's columnar engines store each column on its own, so a query reads only the columns it needs.

MariaDB Server lets each table use its own storage engine, so you don't have to move everything. Keep the transactional tables on InnoDB and put the tables you report on where they run fastest. MariaDB ColumnStore and MariaDB Exa both need MariaDB Enterprise Server.

## Columnar Engines

Start with ColumnStore, and look at Exa when one server isn't enough.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>ColumnStore Quickstart</strong></td><td>Set up ColumnStore and run your first analytical query.</td><td><a href="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide">mariadb-columnstore-guide</a></td></tr><tr><td><strong>ColumnStore Hardware</strong></td><td>Size memory, disk, and cores before you commit machines, since analytics throughput depends on all three.</td><td><a href="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-hardware-guide">mariadb-columnstore-hardware-guide</a></td></tr><tr><td><strong>Deploy MariaDB Exa</strong></td><td>Spread analytical queries across a cluster for the largest data volumes.</td><td><a href="{analytics}/mariadb-exa/deployment">deployment</a></td></tr></tbody></table>

## Analytics Next to Transactions

Run reports on live data without a separate warehouse or an overnight batch job.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>HTAP on MariaDB Cloud</strong></td><td>Pair a transactional MariaDB service with Exa on MariaDB Cloud.</td><td><a href="{mariadb-cloud}/quickstart/htap-mariadb-exa">htap-mariadb-exa</a></td></tr><tr><td><strong>Choose a Storage Engine</strong></td><td>Match each table to how it's read and written.</td><td><a href="{server}/server-usage/storage-engines/choosing-the-right-storage-engine">choosing-the-right-storage-engine</a></td></tr><tr><td><strong>HTAP Quickstart App</strong></td><td>A sample app that writes transactions and reads analytics from the same MariaDB database.</td><td><a href="https://github.com/mariadb-developers/mariadb-htap-quickstart">mariadb-htap-quickstart</a></td></tr></tbody></table>
