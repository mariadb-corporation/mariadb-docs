---
title: Get Started
description: >-
  Documentation for MariaDB Server, MariaDB Enterprise Platform, and MariaDB
  Cloud. Install a database, connect your application, and find the reference
  you need.
icon: rocket
---

# Get Started

MariaDB Server is an open source relational database. It speaks standard SQL and the MySQL wire protocol, which means the clients, drivers, ORMs, and query tools you already use connect to it without modification. It ships transactions, replication, a choice of storage engines, and modern data types including JSON and native vectors in a single package, and it runs on Linux, Windows, and macOS.

These pages document the current release series. Version specific behavior is called out on the page where it applies, and per release detail lives in [Release Notes]({release-notes}).

There are three ways to run MariaDB, and they differ in who operates the database rather than in what the database does. **MariaDB Server** is the open source project: the database you download, run, and manage yourself, under no contract. **MariaDB Enterprise Platform** is the supported MariaDB product. It runs that same server under a support contract, on hardened builds, with routing, clustering, analytics, and management components bundled and tested together as one supported topology. **MariaDB Cloud** runs MariaDB as a fully managed service, which operates the hardware, updates, backups, and availability on your behalf. The SQL you write, the schemas you design, and most of this documentation apply to all three, so choosing one now does not lock you out of the others later.

The documentation is organized to be entered two ways. The Server, MariaDB Platform, and Cloud pages take you from nothing to a working database and then into the matching documentation. The task pages cut across all three and link directly to the pages that do the work, wherever they live, so you do not need to know that backups are documented under Server and cluster failover under Galera Cluster.

The Platform components each have a space of their own in the sidebar, grouped under MariaDB Platform. MaxScale routes and load balances queries. Galera Cluster and Raft Cluster handle replication and failover. ColumnStore and Exa run columnar analytics against operational data, and both require MariaDB Enterprise Server. GridGain provides the in-memory caching and acceleration layer. Language drivers, connection pooling, and prepared statement support are documented under [Connectors]({connectors}).

## Choose How to Run MariaDB

{% content-ref url="readme/community-server.md" %}
[community-server.md](readme/community-server.md)
{% endcontent-ref %}

{% content-ref url="readme/enterprise-platform.md" %}
[enterprise-platform.md](readme/enterprise-platform.md)
{% endcontent-ref %}

{% content-ref url="readme/cloud.md" %}
[cloud.md](readme/cloud.md)
{% endcontent-ref %}

{% content-ref url="choose-how-to-run-mariadb.md" %}
[choose-how-to-run-mariadb.md](choose-how-to-run-mariadb.md)
{% endcontent-ref %}

## Explore by Task

{% content-ref url="development.md" %}
[development.md](development.md)
{% endcontent-ref %}

{% content-ref url="deployment.md" %}
[deployment.md](deployment.md)
{% endcontent-ref %}

{% content-ref url="migration.md" %}
[migration.md](migration.md)
{% endcontent-ref %}

{% content-ref url="operations.md" %}
[operations.md](operations.md)
{% endcontent-ref %}

{% content-ref url="analytics.md" %}
[analytics.md](analytics.md)
{% endcontent-ref %}

{% content-ref url="ai.md" %}
[ai.md](ai.md)
{% endcontent-ref %}
