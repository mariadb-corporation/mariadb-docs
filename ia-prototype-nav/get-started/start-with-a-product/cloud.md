---
title: Cloud
description: >-
  Get started with MariaDB Cloud, the fully managed database service. Launch a
  database in minutes, connect your app, add high availability, and bring your
  data in.
icon: cloud
---

# Cloud

MariaDB Cloud runs MariaDB for you. Launch a database in minutes and the service takes care of the hardware, the updates, the backups, and the availability, so you spend your time building instead of operating. Choose a provisioned database for a steady workload, or go serverless and let it scale with demand. Because MariaDB Cloud handles the operations, getting started here is quick: launch, connect, and you are building.

It runs across major cloud providers and regions, so you can place the database near your application, and it carries the same MariaDB and MySQL compatibility as the self managed products, so your code and tools work unchanged. The pieces you would otherwise build and babysit, patching, backups, and failover, are on by default.

**Launch a database.** The fastest start is the portal, which walks you through creating a database, sizing it, and collecting the connection details. Prefer to script it from the beginning? Launch through the API with Python, the same pattern you will reuse to wire database creation into a deployment pipeline.

**Connect your application.** Point your code at the new database. The Java guide is a worked example of taking the connection details from the portal, opening a pool, and running a query, and the connection section has the equivalent for every supported language and driver, so the path is the same whatever you build in.

**Make it highly available.** One database is enough to build against, but production wants more. Set up a replicated topology and the service keeps serving reads and writes through the loss of a node. It costs little to turn on early, while your application is still easy to change.

**Bring your data in.** Already running a database elsewhere? Load it into MariaDB Cloud and you have moved from evaluating the service to running on it.

Start with the portal and you will have a database to talk to within a few minutes.

## Launch a database

{% content-ref url="{mariadb-cloud}/quickstart/using-the-portal" %}
[Launch Using the Portal]({mariadb-cloud}/quickstart/using-the-portal)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/quickstart/launch-db-using-python" %}
[Launch a Database Using Python]({mariadb-cloud}/quickstart/launch-db-using-python)
{% endcontent-ref %}

## Connect your application

{% content-ref url="{mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-from-java-app" %}
[Connect from a Java Application]({mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-from-java-app)
{% endcontent-ref %}

## Make it highly available

{% content-ref url="{mariadb-cloud}/high-availability-dr/ha-and-replicated-topology" %}
[High Availability and Replicated Topology]({mariadb-cloud}/high-availability-dr/ha-and-replicated-topology)
{% endcontent-ref %}

## Move your data in

{% content-ref url="{mariadb-cloud}/data-loading-migration/migrate-your-database-to-mariadb-cloud" %}
[Migrate Your Database to MariaDB Cloud]({mariadb-cloud}/data-loading-migration/migrate-your-database-to-mariadb-cloud)
{% endcontent-ref %}
