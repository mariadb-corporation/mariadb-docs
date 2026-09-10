---
title: Cloud
description: >-
  Get started with MariaDB Cloud, the managed database service. Launch a
  database, connect your application, and set up high availability without
  running servers yourself.
icon: cloud
---

# Cloud

MariaDB Cloud is the managed service that runs MariaDB for you. You provision a database through the portal or an API, and the service handles the hardware, the software updates, the backups, and the availability. It supports both provisioned and serverless deployments, so you can size a database for a steady workload or let it scale with demand. Because the service operates the database, most of the work that fills the other product pages, installing, patching, and clustering, is handled for you, and this page is shorter as a result.

This page is the first path into Cloud. It moves from launching a database, to connecting an application to it, to making it highly available, and finally to bringing existing data in.

The quickest start is the portal. It walks you through creating a database, choosing a size, and collecting the connection details, and it is the right first step even if you plan to automate later. If you would rather script the provisioning from the beginning, the Python quickstart launches a database through the API, which is the pattern you reuse for repeatable environments and for wiring database creation into a deployment pipeline.

With a database running, the next step is to connect to it from your application. The Java guide is a worked example of taking the connection details from the portal, opening a connection pool, and running a query. The connection section has an equivalent guide for each of the other supported languages and drivers, so the pattern is the same whatever your stack is written in.

A single database is enough to build against, but production wants more than one. The high availability guide sets up a replicated topology, so the service keeps serving reads and writes through the loss of a node. Standing this up early means your application meets a realistic topology while it is still cheap to change.

The last step, if you already run a database elsewhere, is to bring its data in. The migration guide loads an existing database into MariaDB Cloud, which is usually the step between evaluating the service and adopting it for real work.

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
