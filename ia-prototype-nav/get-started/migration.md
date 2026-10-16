---
title: Migration
description: >-
  Move a database to MariaDB Server or MariaDB Cloud from MySQL, PostgreSQL, Oracle, SQL Server, or Amazon RDS.
icon: arrow-right-arrow-left
---

# Migration

You've seen MariaDB Community Server answer a query from Python. Now bring your own data over. Most moves start from MySQL, where MariaDB shares the wire protocol, most of the SQL, and the dump tooling, so many schemas load with few changes. From PostgreSQL, Oracle, or SQL Server, you translate data types, functions, and procedural code, and the guide for your source database lists those differences.

## Move a MySQL Database to a Copy First

Run these three steps against a test copy of MariaDB Server before you touch production. You get a real timing for the cutover, and any schema problems show up while they're cheap to fix. The examples move a database called `shop`.

{% stepper %}
{% step %}
### Check What Changes

On the MySQL source, look for the features that don't carry over as-is. A binary MySQL `JSON` column arrives in MariaDB as `LONGTEXT` with a validity check. MySQL's table-level `ENCRYPTION` and `COMPRESSION` options use syntax that MariaDB doesn't accept, so a dump that contains them fails on import.

```sql
-- Columns that use the MySQL JSON type
SELECT table_schema, table_name FROM information_schema.COLUMNS
WHERE data_type = "JSON";

-- Tables with MySQL encryption or compression options
SELECT table_schema, table_name, create_options FROM information_schema.TABLES
WHERE create_options LIKE "%ENCRYPT%" OR create_options LIKE "%COMP%";
```

Remove the encryption and compression options with `ALTER TABLE` before you dump, and turn them back on with MariaDB syntax afterward. The [MySQL to MariaDB compatibility matrix]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-compatibility-matrix) covers authentication, SQL syntax, and the other high-impact differences.
{% endstep %}

{% step %}
### Dump From MySQL and Load Into MariaDB

Use MySQL's own `mysqldump` tool on the source, because MariaDB's `mariadb-dump` tool hasn't been tested as widely against MySQL servers. Name your databases with `--databases` instead of `--all-databases`, because the MySQL system databases differ from MariaDB's and fail on import. Pipe the dump straight into the `mariadb` client on the target server:

```bash
mysqldump --user=root --password --databases shop \
  --single-transaction --routines --events \
  --triggers --hex-blob \
  | mariadb --host=new_server_ip --user=root --password
```

The `--single-transaction` option takes a consistent InnoDB snapshot without locking tables. Binary columns come through intact because of the `--hex-blob` option. A streamed load can't resume if the connection drops, so for a large database, write the dump to a file first. The [MySQL to MariaDB migration guide]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-migration-the-master-guide) covers the file method, server settings for big imports, and porting users and privileges.
{% endstep %}

{% step %}
### Verify the Copy

Run the same statements on the MySQL source and on MariaDB, then compare the results table by table. Afterward, refresh the optimizer statistics on MariaDB with the `mariadb-check` tool, because the MariaDB optimizer plans queries differently from the MySQL one.

```sql
SELECT COUNT(*) FROM shop.products;
CHECKSUM TABLE shop.products;
```

```bash
mariadb-check -u root -p --analyze --all-databases
```

Row counts must match exactly. A checksum mismatch on a table with date and time columns can come from a different row storage format instead of different data, so check those tables row by row. [`CHECKSUM TABLE`]({server}/reference/sql-statements/table-statements/checksum-table) explains what changes the value.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**Need zero downtime?** Load the copy, then set up MariaDB as a replica of MySQL so it keeps up until you switch the application over. [Migration from MySQL to MariaDB Galera Cluster using replication]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migration-from-mysql-to-mariadb-cluster-using-replication) walks through it.
{% endhint %}

## Start With the Differences

Scope the work before you move any data.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Differences From Other Databases</strong></td><td>What changes when you move to MariaDB from another database system.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/differences-between-mariadb-and-other-dbmss">differences-between-mariadb-and-other-dbmss</a></td></tr><tr><td><strong>Migration Overview</strong></td><td>The supported source databases and the steps every migration shares.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb">migrating-to-mariadb</a></td></tr><tr><td><strong>MySQL Compatibility</strong></td><td>Feature-by-feature compatibility between MySQL and MariaDB versions.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-compatibility-matrix">mysql-to-mariadb-compatibility-matrix</a></td></tr></tbody></table>

## Migrate From Your Database

Pick your source database for the type mappings, syntax changes, and tools that apply to it.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>From MySQL</strong></td><td>Replace MySQL in place, move with a dump and restore, or switch over with replication.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql">moving-from-mysql</a></td></tr><tr><td><strong>From PostgreSQL</strong></td><td>Translate PostgreSQL types, functions, and syntax to MariaDB.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-postgresql">migrating-to-mariadb-from-postgresql</a></td></tr><tr><td><strong>From Oracle</strong></td><td>Set <code>sql_mode=ORACLE</code> to run much of your PL/SQL without rewriting it.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-oracle">migrating-to-mariadb-from-oracle</a></td></tr><tr><td><strong>From SQL Server</strong></td><td>Map SQL Server types, syntax, and T-SQL habits to MariaDB.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server">migrating-to-mariadb-from-sql-server</a></td></tr><tr><td><strong>Into MariaDB Cloud</strong></td><td>Load an existing database into a MariaDB Cloud service.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading-migration">data-loading-migration</a></td></tr><tr><td><strong>From Amazon RDS to MariaDB Cloud</strong></td><td>Move an Amazon RDS for MariaDB instance to MariaDB Cloud.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-from-mariadb-rds-to-mariadb-cloud">migrating-from-mariadb-rds-to-mariadb-cloud</a></td></tr></tbody></table>
