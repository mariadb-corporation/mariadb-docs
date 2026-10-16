---
title: Cloud
description: >-
  Get started with MariaDB Cloud, the managed MariaDB service. Launch a database, connect your application, add high availability, and bring your data in.
icon: cloud
---

# Cloud

MariaDB Cloud runs MariaDB for you. You create a database, and the service takes care of the hardware, patching, backups, and failover. A Serverless database is ready in seconds and scales with demand. A Provisioned one gives you dedicated capacity for a steady workload. Both run on AWS, Google Cloud, and Azure, in regions near your application.

It's the same MariaDB as everywhere else in these docs, so your existing drivers, tools, and SQL work as they are.

## Launch a Database

The portal is the quickest way in. Use the API or Terraform when you want databases created from a pipeline.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Launch From the Portal</strong></td><td>Sign up, launch a Serverless or Provisioned service, and get the connection details.</td><td><a href="{mariadb-cloud}/quickstart/using-the-portal">using-the-portal</a></td></tr><tr><td><strong>Launch From Python</strong></td><td>Provision a database with a short script against the MariaDB Cloud API.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-python">launch-db-using-python</a></td></tr><tr><td><strong>Launch With Terraform</strong></td><td>Manage MariaDB Cloud databases as infrastructure as code.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-the-terraform-provider">launch-db-using-the-terraform-provider</a></td></tr></tbody></table>

## Connect and Stay Up

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Connect Your Application</strong></td><td>Connection settings for each supported language and driver.</td><td><a href="{mariadb-cloud}/connecting-to-mariadb-cloud-dbs">connecting-to-mariadb-cloud-dbs</a></td></tr><tr><td><strong>Connect From Java</strong></td><td>A worked example: take the details from the portal, open a pool, and run a query.</td><td><a href="{mariadb-cloud}/connecting-to-mariadb-cloud-dbs/connect-from-java-app">connect-from-java-app</a></td></tr><tr><td><strong>High Availability</strong></td><td>Switch to a replicated topology that keeps serving through the loss of a node.</td><td><a href="{mariadb-cloud}/high-availability-dr/ha-and-replicated-topology">ha-and-replicated-topology</a></td></tr></tbody></table>

## Bring Your Data In

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Migrate Your Database</strong></td><td>Load an existing database into a MariaDB Cloud service.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading-migration">data-loading-migration</a></td></tr><tr><td><strong>From Amazon RDS</strong></td><td>Move an Amazon RDS for MariaDB instance to MariaDB Cloud.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud">migrating-from-mariadb-rds-to-mariadb-cloud</a></td></tr><tr><td><strong>Import CSV Data</strong></td><td>Load CSV files into a MariaDB Cloud database with the <code>mariadb</code> client.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading/import-csv-data">import-csv-data</a></td></tr></tbody></table>
