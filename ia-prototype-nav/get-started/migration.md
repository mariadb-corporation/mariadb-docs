---
title: Migration
description: >-
  Bring your data to MariaDB Server. Migrate from MySQL, PostgreSQL, and other
  databases, or move an existing database into MariaDB Cloud.
icon: arrow-right-arrow-left
---

# Migration

How much work a migration takes depends almost entirely on the source database. Moving from MySQL is close to a drop-in replacement for many schemas, because MariaDB shares the wire protocol, most of the SQL dialect, and much of the tooling. Moving from PostgreSQL, Oracle, or another system means translating types, functions, and procedural code. Moving into MariaDB Cloud gives you a managed target with a data loading path of its own.

The guides below cover both the assessment and the move. The assessment matters more than it looks, because the cost of a migration is concentrated in the incompatibilities you find late.

**Know what changes first.** Before moving any data, read how MariaDB differs from your current database. The differences guide separates the mechanical parts of a migration from the parts that need real translation, which turns an open ended job into a scoped one. The migration overview then lists the supported source databases and the process shared across them.

**Pick your source.** Each source database has a guide written for its specific differences, and following the matching one is faster than working from the overview. MySQL is the most common path and usually needs the fewest changes. PostgreSQL requires attention to type and syntax differences. Oracle migrations can use `sql_mode=ORACLE`, which accepts a large share of PL/SQL without a rewrite.

**Moving to the managed service.** MariaDB Cloud has a loading path that imports your data into a provisioned database, and a dedicated guide covers moving an existing Amazon RDS for MariaDB instance across.

Run the migration against a non production copy first. That gives you a timing for the cutover and surfaces translation errors while they are still cheap to fix.

## Start With the Differences

{% content-ref url="explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/differences-between-mariadb-and-other-dbmss/" %}
[differences-between-mariadb-and-other-dbmss](explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/differences-between-mariadb-and-other-dbmss/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/" %}
[migrating-to-mariadb](explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/)
{% endcontent-ref %}

## Migrate From Another Database

{% content-ref url="explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-postgresql/" %}
[migrating-to-mariadb-from-postgresql](explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-postgresql/)
{% endcontent-ref %}

## Migrate Into MariaDB Cloud

{% content-ref url="explore-by-task/%7Bmariadb-cloud%7D/data-loading-migration/migrate-your-database-to-mariadb-cloud/" %}
[migrate-your-database-to-mariadb-cloud](explore-by-task/%7Bmariadb-cloud%7D/data-loading-migration/migrate-your-database-to-mariadb-cloud/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud/" %}
[migrating-from-mariadb-rds-to-mariadb-cloud](explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud/)
{% endcontent-ref %}
