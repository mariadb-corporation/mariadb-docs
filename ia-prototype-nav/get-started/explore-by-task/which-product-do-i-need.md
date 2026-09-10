---
title: Which Product Do I Need?
description: >-
  Choose between MariaDB Server, MariaDB Enterprise Platform, and MariaDB Cloud
  by matching each to how much of the database you want to run yourself.
icon: signs-post
---

# Which Product Do I Need?

MariaDB comes in three products, and they differ less in what the database can do than in how much of it you run yourself. The SQL, the storage engines, and most of the reference apply to all three. What changes is who operates the server, who holds the support contract, and which components ship alongside it. This page helps you match a product to your situation so you do not have to read three sets of documentation to decide.

## Start with the question of who operates it

The clearest split is operational. If you want to run the database on your own machines and manage it yourself, you want MariaDB Server. If you want someone else to run it and you want to consume it as a service, you want MariaDB Cloud. If you run it yourself but need a support contract and the components that back a production deployment, you want MariaDB Enterprise Platform.

**MariaDB Server** is the open source database, self managed, with no contract. It is the whole of the free product and the right choice for development, for evaluation, and for teams that operate their own infrastructure. It is also the database at the center of the other two products, so nothing you learn here is wasted if you move up later.

**MariaDB Enterprise Platform** is Enterprise Server plus components plus services. You still run it yourself, but you get a support contract, hardened builds, and the routing, clustering, analytics, and management pieces bundled and tested together. Choose it when you operate your own database but want commercial support and a production topology out of the box.

**MariaDB Cloud** is the managed service. You provision a database and the service handles hardware, updates, backups, and availability. Choose it when you would rather build on the database than run it, or when you want to scale capacity without managing servers.

## Then confirm the details

Read each product's own starting page to confirm the fit before you commit. Server's install guide shows exactly what self managing involves. The platform overview lists the components you get. The Cloud portal quickstart shows how little you have to operate.

{% content-ref url="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide" %}
[Install MariaDB Server]({server}/mariadb-quickstart-guides/installing-mariadb-server-guide)
{% endcontent-ref %}

{% content-ref url="{platform}/mariadb-platform-quickstart-guides/mariadb-overview-guide" %}
[Platform Overview]({platform}/mariadb-platform-quickstart-guides/mariadb-overview-guide)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/quickstart/using-the-portal" %}
[Launch MariaDB Cloud Using the Portal]({mariadb-cloud}/quickstart/using-the-portal)
{% endcontent-ref %}

## When the choice is about a component

Some decisions are not about the product but about a component you would add to it. If you are weighing where analytical queries should run, the storage engine chooser compares the options directly.

{% content-ref url="{server}/server-usage/storage-engines/choosing-the-right-storage-engine" %}
[Choosing the Right Storage Engine]({server}/server-usage/storage-engines/choosing-the-right-storage-engine)
{% endcontent-ref %}
