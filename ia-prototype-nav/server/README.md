---
title: Server
description: >-
  MariaDB Server is the open source relational database. Install it,
  connect a client, write SQL, and manage it in production.
icon: database
---

# Server

MariaDB Server is an open source relational database. It speaks standard SQL and the MySQL wire protocol, so existing clients, drivers, and administration tools connect to it unchanged. It runs on Linux, Windows, and macOS, and it is the database at the core of MariaDB Enterprise Platform and MariaDB Cloud, so what you learn here applies to all three.

The server ships transactions, replication, a pluggable storage engine layer, and modern data types including JSON and native vectors. The storage engine layer is worth knowing about early: InnoDB is the default and handles transactional work, and other engines serve other access patterns, and you can use different engines for different tables in the same database.

**Install and connect.** Add the MariaDB package repository and install the server with your platform's package manager, then secure the fresh install. Confirm it works with a `mariadb` client session before you involve an application, because that separates a database problem from a driver problem.

**Learn the SQL.** The tutorials cover the query patterns applications actually depend on, including joins and index design. Index design is the single highest leverage thing to get right, because it determines whether a query reads a handful of rows or scans the table.

**Run it.** The how-to guides cover managing the server, securing it, and the high availability and performance work that production demands: users and privileges, backups, replication, and query tuning.

**Look things up.** The reference covers every SQL statement and the client and utility programs that ship with the server, including the backup and import tools.

Install the server and connect a client. Everything after those two steps is SQL and configuration.

{% content-ref url="mariadb-quickstart-guides/README.md" %}
[Quickstart Guides](mariadb-quickstart-guides/README.md)
{% endcontent-ref %}

{% content-ref url="server-usage/README.md" %}
[Server Usage](server-usage/README.md)
{% endcontent-ref %}

{% content-ref url="server-management/README.md" %}
[Server Management](server-management/README.md)
{% endcontent-ref %}

{% content-ref url="security/README.md" %}
[Security](security/README.md)
{% endcontent-ref %}

{% content-ref url="architecture/README.md" %}
[Architecture](architecture/README.md)
{% endcontent-ref %}

{% content-ref url="clients-and-utilities/README.md" %}
[Clients & Utilities](clients-and-utilities/README.md)
{% endcontent-ref %}

{% content-ref url="ha-and-performance/README.md" %}
[HA & Performance](ha-and-performance/README.md)
{% endcontent-ref %}

{% content-ref url="reference/README.md" %}
[Reference](reference/README.md)
{% endcontent-ref %}
