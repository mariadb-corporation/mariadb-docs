---
title: Migration
description: >-
  Bring your data to MariaDB. Migrate from MySQL, PostgreSQL, and other
  databases, or move an existing database into MariaDB Cloud.
icon: arrow-right-arrow-left
---

# Migration

Moving to MariaDB from another database? Start here. How much work it takes depends on where you are coming from. Coming from MySQL is close to a drop in for many schemas. Coming from PostgreSQL or another system means translating some types and syntax. Moving into MariaDB Cloud gives you a managed target with a loading path of its own. Whatever your source, the guides below get you from your current database to a working MariaDB.

MariaDB's compatibility with MySQL is what makes many migrations straightforward: the SQL, the wire protocol, and the tooling line up, so a large share of applications move with little or no rewriting. Migrations from other systems take more care, and the guides here are honest about where that care is needed rather than promising a button.

**Know what changes first.** Before you move a single row, see how MariaDB differs from your current database. The differences guide shows you where a migration is mechanical and where it needs real translation, which turns the job from a surprise into a plan. The migration overview then lays out the supported source databases and the process that applies across them, so you know the shape of the work before you commit to it.

**Pick your source.** Each source database has its own guide, written for its particular differences, so following the one that matches you is faster than working from the overview alone. Coming from MySQL is the most common path and usually needs the fewest changes, since MariaDB shares much of its heritage. Coming from PostgreSQL, the PostgreSQL guide covers the type and syntax differences you will meet.

**Moving to the managed service?** MariaDB Cloud has its own path that loads your data into a provisioned database, and there is a dedicated guide for moving an existing Amazon RDS for MariaDB instance across.

Whatever your source, run the migration against a non production copy first, so you can time it and catch translation issues before they reach anyone.

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
