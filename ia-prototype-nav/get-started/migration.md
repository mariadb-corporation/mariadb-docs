---
title: Migration
description: >-
  Move to MariaDB Server from MySQL, PostgreSQL, Oracle, or SQL Server, or bring an existing database into MariaDB Cloud.
icon: arrow-right-arrow-left
---

# Migration

How much work a migration takes depends on where you're coming from. From MySQL, many schemas move over with few or no changes, because MariaDB shares the wire protocol, most of the SQL, and much of the tooling. From PostgreSQL, Oracle, or SQL Server, you translate data types, functions, and procedural code, and the guide for your source database tells you where those differences are.

Run the migration against a copy before you do it for real. You get a timing for the cutover, and translation problems show up while they're still cheap to fix.

## Start With the Differences

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Differences From Other Databases</strong></td><td>What changes when you move to MariaDB, so you can scope the work before you start.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/differences-between-mariadb-and-other-dbmss">differences-between-mariadb-and-other-dbmss</a></td></tr><tr><td><strong>Migration Overview</strong></td><td>The supported source databases and the steps every migration shares.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb">migrating-to-mariadb</a></td></tr><tr><td><strong>MySQL Compatibility</strong></td><td>Feature-by-feature compatibility between MySQL and MariaDB versions.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-compatibility-matrix">mysql-to-mariadb-compatibility-matrix</a></td></tr></tbody></table>

## Migrate From Your Database

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>From MySQL</strong></td><td>Replace MySQL in place or move over with replication.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql">moving-from-mysql</a></td></tr><tr><td><strong>From PostgreSQL</strong></td><td>Translate types, functions, and syntax from PostgreSQL.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-postgresql">migrating-to-mariadb-from-postgresql</a></td></tr><tr><td><strong>From Oracle</strong></td><td>Use <code>sql_mode=ORACLE</code> to run much of your PL/SQL without rewriting it.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-oracle">migrating-to-mariadb-from-oracle</a></td></tr><tr><td><strong>From SQL Server</strong></td><td>Map SQL Server types, syntax, and T-SQL habits to MariaDB.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server">migrating-to-mariadb-from-sql-server</a></td></tr><tr><td><strong>Into MariaDB Cloud</strong></td><td>Load an existing database into a MariaDB Cloud service.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading-migration">data-loading-migration</a></td></tr><tr><td><strong>From Amazon RDS to MariaDB Cloud</strong></td><td>Move an Amazon RDS for MariaDB instance to MariaDB Cloud.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud">migrating-from-mariadb-rds-to-mariadb-cloud</a></td></tr></tbody></table>
