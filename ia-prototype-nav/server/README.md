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

## Get Started

{% content-ref url="get-started/install-mariadb.md" %}
[install-mariadb.md](get-started/install-mariadb.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-mariadb.md" %}
[connect-to-mariadb.md](get-started/connect-to-mariadb.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/sql-joins.md" %}
[sql-joins.md](tutorials/sql-joins.md)
{% endcontent-ref %}

{% content-ref url="tutorials/working-with-indexes.md" %}
[working-with-indexes.md](tutorials/working-with-indexes.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/managing-the-server.md" %}
[managing-the-server.md](how-to-guides/managing-the-server.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/security.md" %}
[security.md](how-to-guides/security.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/high-availability-and-performance.md" %}
[high-availability-and-performance.md](how-to-guides/high-availability-and-performance.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-mariadb-server.md" %}
[what-is-mariadb-server.md](overview/what-is-mariadb-server.md)
{% endcontent-ref %}

{% content-ref url="concepts/architecture.md" %}
[architecture.md](concepts/architecture.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/sql-statements.md" %}
[sql-statements.md](reference/sql-statements.md)
{% endcontent-ref %}

{% content-ref url="reference/clients-and-utilities.md" %}
[clients-and-utilities.md](reference/clients-and-utilities.md)
{% endcontent-ref %}

{% content-ref url="release-notes/community-server-releases.md" %}
[community-server-releases.md](release-notes/community-server-releases.md)
{% endcontent-ref %}
