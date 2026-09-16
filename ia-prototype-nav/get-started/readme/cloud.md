---
title: Cloud
description: >-
  Get started with MariaDB Cloud, the fully managed database service. Launch a
  database in minutes, connect your app, add high availability, and bring your
  data in.
icon: cloud
---

# Cloud

MariaDB Cloud is a fully managed database service for MariaDB and MySQL compatible workloads. You provision a database and the service operates the hardware, the updates, the backups, and the availability. Choose a provisioned instance for a steady workload, or serverless to scale with demand and avoid paying for idle capacity.

It runs across major cloud providers and regions, so the database can sit near your application, and it carries the same MariaDB and MySQL compatibility as the self managed products, so existing code and tools work unchanged. Patching, automated backups, and failover are on by default rather than being things you build.

**Launch a database.** The portal is the fastest start. It walks through creating a database, sizing it, and collecting the connection details. To script it instead, the API can provision a database from Python, which is the same pattern you would use to create databases from a deployment pipeline.

**Connect your application.** Point your code at the new database. The Java guide is a worked example: take the connection details from the portal, open a pool, run a query. The connection section has the equivalent for every supported language and driver.

**Make it highly available.** A single database is enough to build against. Production wants a replicated topology, which keeps serving reads and writes through the loss of a node. Enabling it early costs little while the application is still easy to change.

**Bring your data in.** Load an existing database into MariaDB Cloud to move from evaluating the service to running on it. There is a dedicated path for an existing Amazon RDS for MariaDB instance.

Create a database in the portal and connect to it. That confirms the credentials and the network path before you change any application code.

## Launch a Database

{% content-ref url="../start-with-a-product/%7Bmariadb-cloud%7D/quickstart/using-the-portal/" %}
[using-the-portal](../start-with-a-product/%7Bmariadb-cloud%7D/quickstart/using-the-portal/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bmariadb-cloud%7D/quickstart/launch-db-using-python/" %}
[launch-db-using-python](../start-with-a-product/%7Bmariadb-cloud%7D/quickstart/launch-db-using-python/)
{% endcontent-ref %}

## Connect Your Application

{% content-ref url="../start-with-a-product/%7Bmariadb-cloud%7D/connecting-to-mariadb-cloud-dbs/connect-from-java-app/" %}
[connect-from-java-app](../start-with-a-product/%7Bmariadb-cloud%7D/connecting-to-mariadb-cloud-dbs/connect-from-java-app/)
{% endcontent-ref %}

## Make It Highly Available

{% content-ref url="../start-with-a-product/%7Bmariadb-cloud%7D/high-availability-dr/ha-and-replicated-topology/" %}
[ha-and-replicated-topology](../start-with-a-product/%7Bmariadb-cloud%7D/high-availability-dr/ha-and-replicated-topology/)
{% endcontent-ref %}

## Move Your Data In

{% content-ref url="../start-with-a-product/%7Bmariadb-cloud%7D/data-loading-migration/migrate-your-database-to-mariadb-cloud/" %}
[migrate-your-database-to-mariadb-cloud](../start-with-a-product/%7Bmariadb-cloud%7D/data-loading-migration/migrate-your-database-to-mariadb-cloud/)
{% endcontent-ref %}
