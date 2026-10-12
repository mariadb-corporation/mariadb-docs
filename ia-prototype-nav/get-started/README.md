---
title: Get Started
description: >-
  Documentation for MariaDB Server, MariaDB Enterprise Platform, and MariaDB
  Cloud. Choose how to run MariaDB, start from a task, or go straight to a
  product.
icon: rocket
---

# Get Started

This documentation covers MariaDB Server, MariaDB Enterprise Platform, and MariaDB Cloud, with the connectors and tools that work with them. All three run the same database. The SQL you write and the schemas you design work the same way on each, so most of these pages apply wherever you run MariaDB.

If you are new to MariaDB, start by choosing how to run it. When you have a specific job to do, the task pages gather the relevant pages from across the products. Readers who already know which product they need can go straight to its section in the top navigation.

## Choose How to Run MariaDB

The three ways to run MariaDB differ in who operates the database and whether a support contract covers it.

* **MariaDB Server** is the open source database. You download it, run it, and manage it yourself, with no contract.
* **MariaDB Enterprise Platform** is MariaDB Enterprise Server plus the routing, clustering, analytics, and management components that a production deployment needs. The components are tested together and covered by a support contract, and you operate the deployment.
* **MariaDB Cloud** is a fully managed service. The service operates the hardware, the updates, the backups, and the availability for you.

The choice is not permanent. Your SQL and your schemas carry over if you move to another option later.

{% content-ref url="readme/community-server.md" %}
[Server](readme/community-server.md)
{% endcontent-ref %}

{% content-ref url="readme/enterprise-platform.md" %}
[MariaDB Platform](readme/enterprise-platform.md)
{% endcontent-ref %}

{% content-ref url="readme/cloud.md" %}
[Cloud](readme/cloud.md)
{% endcontent-ref %}

{% content-ref url="choose-how-to-run-mariadb.md" %}
[Choose How to Run MariaDB](choose-how-to-run-mariadb.md)
{% endcontent-ref %}

## Start From a Task

Each task page collects the pages for one job, wherever those pages live. For example, the Operations page links to backups in the Server documentation and to failover in the Galera Cluster documentation, so you do not have to know where each procedure is documented.

{% content-ref url="development.md" %}
[Development](development.md)
{% endcontent-ref %}

{% content-ref url="deployment.md" %}
[Deployment](deployment.md)
{% endcontent-ref %}

{% content-ref url="migration.md" %}
[Migration](migration.md)
{% endcontent-ref %}

{% content-ref url="operations.md" %}
[Operations](operations.md)
{% endcontent-ref %}

{% content-ref url="analytics.md" %}
[Analytics](analytics.md)
{% endcontent-ref %}

{% content-ref url="ai.md" %}
[AI](ai.md)
{% endcontent-ref %}

## Find a Product

The top navigation has one section for each product area.

| Section | What it documents |
| --- | --- |
| **Server** | MariaDB Server: installation, administration, security, high availability, and the SQL reference. |
| **MariaDB Platform** | MariaDB Enterprise Server and the Platform components: MaxScale, Galera Cluster, Raft Cluster, ColumnStore, Exa, GridGain, and the Enterprise Tools. |
| **Cloud** | MariaDB Cloud: launching and connecting to databases, high availability, data loading, and security. |
| **AI Tools** | MCP servers, plugins for coding agents, retrieval tools, and AI framework integrations. |
| **Connectors** | The MariaDB connectors for Java, Python, Node.js, C, C++, .NET, ODBC, and R2DBC, plus guides for other languages. |
| **Release Notes** | Release notes by product, starting with a page of the latest releases. |

Each MariaDB Platform component solves a specific production problem:

* **MaxScale** routes queries, balances reads, and hides failover from the application.
* **Galera Cluster** and **Raft Cluster** replicate data across nodes and handle failover.
* **ColumnStore** and **Exa** run columnar analytics on operational data. Both require MariaDB Enterprise Server.
* **GridGain** provides in-memory caching and acceleration.
* **Enterprise Tools** include MariaDB Enterprise Manager, which manages and monitors a set of servers, and the MariaDB Enterprise Kubernetes Operator, which runs MariaDB on Kubernetes.

## Versions

These pages document the current release series. When a feature behaves differently in an earlier version, the page that describes the feature tells you. For the changes in each release, see [Release Notes]({release-notes}).
