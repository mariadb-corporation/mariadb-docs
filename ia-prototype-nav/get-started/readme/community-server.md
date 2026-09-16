---
title: Server
description: >-
  Get started with MariaDB Server, the open source SQL database you run
  yourself. Install it, connect a client, run your first queries, and back up
  your data.
icon: database
---

# Server

MariaDB Server is the open source relational database you download and run yourself. It speaks standard SQL and the MySQL wire protocol, runs on Linux, Windows, and macOS, and carries no contract. The same server sits at the core of MariaDB Enterprise Platform and MariaDB Cloud, so what you learn here applies if your deployment grows into either.

Out of the box you get transactions, replication, a choice of storage engines, and modern data types including JSON and native vectors. Existing MySQL clients, drivers, and administration tools connect to it without changes.

Four steps take you from nothing to a working database.

**Install it.** Add the MariaDB package repository and install the server with your system's package manager. The installation guide has the exact commands for each platform and covers securing a fresh install, which sets the root authentication and removes the default test database.

**Connect to it.** Open a session with the `mariadb` command line client and confirm the server answers. The host, port, user, and password that work here are the same values your application's driver will use, which is why proving them at the command line first saves time later.

**Write some SQL.** Create a database, define a table, and run your first statements. Start with the basics, then move into the joins, functions, and query patterns that applications depend on as the schema grows.

**Protect your data.** Take a backup and restore it before the database holds anything you care about. Run both halves by hand once, so the procedure is known rather than assumed.

Install the server and connect a client. Those two steps confirm the environment, and everything after them is SQL and configuration.

## Install and Connect

{% content-ref url="../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/installing-mariadb-server-guide/" %}
[installing-mariadb-server-guide](../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/installing-mariadb-server-guide/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-connecting-guide/" %}
[mariadb-connecting-guide](../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-connecting-guide/)
{% endcontent-ref %}

## Learn the Basics

{% content-ref url="../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/basics-guide/" %}
[basics-guide](../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/basics-guide/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-usage-guide/" %}
[mariadb-usage-guide](../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-usage-guide/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-advanced-sql-guide/" %}
[mariadb-advanced-sql-guide](../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-advanced-sql-guide/)
{% endcontent-ref %}

## Protect Your Data

{% content-ref url="../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-backup-guide/" %}
[mariadb-backup-guide](../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-backup-guide/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-restore-guide/" %}
[mariadb-restore-guide](../start-with-a-product/%7Bserver%7D/mariadb-quickstart-guides/mariadb-restore-guide/)
{% endcontent-ref %}
