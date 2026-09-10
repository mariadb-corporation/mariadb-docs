---
title: Migration
description: >-
  Move your data to MariaDB. Migrate from MySQL, PostgreSQL, and other
  databases, or bring an existing database into MariaDB Cloud.
icon: arrow-right-arrow-left
---

# Migration

Migration is moving an existing database into MariaDB from somewhere else. The work depends on where you are coming from and where you are going. Moving from MySQL is close to a drop in for many schemas, while moving from PostgreSQL or another system involves translating types and syntax. Moving into MariaDB Cloud adds a managed target with its own loading path. This page gathers the entry point for each of those routes, because they live in different parts of the documentation and a reader planning a migration needs to see them together to plan the whole job.

Before you move anything, understand how MariaDB differs from your current database. The differences page compares MariaDB with other database systems, which tells you where a migration is mechanical and where it needs real translation work. Reading it first turns a migration from a surprise into a plan, because you learn which features map straight across and which have no direct equivalent. The migration overview then lays out the supported source databases and the general process that applies across all of them, so you know the shape of the work before you pick your specific source.

With the groundwork done, pick the guide for your source database. Moving from MySQL is the most common path and often needs the fewest changes, because MariaDB shares much of its heritage. Moving from PostgreSQL involves more translation, and the PostgreSQL guide covers the data type and syntax differences you will meet along the way. Each source guide is written for that database's particular differences, so following the one that matches your system is faster than working from the general overview alone.

If your target is the managed service rather than a server you run, MariaDB Cloud has its own migration path that loads your data into a provisioned database. There is also a guide for the specific case of moving from an existing Amazon RDS for MariaDB instance into MariaDB Cloud, which is common enough to have its own steps. Choose the target guide that matches where your database will live, then run the migration against a non production copy first so you can measure how long it takes and catch translation issues before they affect anyone.

## Start with the differences

{% content-ref url="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/differences-between-mariadb-and-other-dbmss" %}
[Differences Between MariaDB and Other Database Systems]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/differences-between-mariadb-and-other-dbmss)
{% endcontent-ref %}

{% content-ref url="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb" %}
[Migrating to MariaDB]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb)
{% endcontent-ref %}

## Migrate from another database

{% content-ref url="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-postgresql" %}
[Migrating to MariaDB from PostgreSQL]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-postgresql)
{% endcontent-ref %}

## Migrate into MariaDB Cloud

{% content-ref url="{mariadb-cloud}/data-loading-migration/migrate-your-database-to-mariadb-cloud" %}
[Migrate Your Database to MariaDB Cloud]({mariadb-cloud}/data-loading-migration/migrate-your-database-to-mariadb-cloud)
{% endcontent-ref %}

{% content-ref url="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud" %}
[Migrating from MariaDB RDS to MariaDB Cloud]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud)
{% endcontent-ref %}
