---
title: Migration
description: >-
  Move from MySQL to open MariaDB by rehearsing on a copy first, with guides for PostgreSQL, Oracle, SQL Server, and MariaDB Cloud.
icon: arrow-right-arrow-left
---

# Migration

You didn't start the shop on MariaDB. It already runs on MySQL, the `products` table has real prices in it, and customers place orders every hour. You want to move it to MariaDB Server without spending a weekend on surprises that a test run would have caught on a Tuesday.

From MySQL, the trip is short. MariaDB speaks the same wire protocol, accepts most of the same SQL, and loads a MySQL dump, so your application code and most of your schema come over unchanged. The trip from PostgreSQL, Oracle, or SQL Server is longer, because data types, built-in functions, and stored procedures need translation, and each source database has its own guide in the cards at the end.

## Rehearse on a Copy

The first move isn't the real one. You stand up a test MariaDB Server, copy the `shop` database into it, and check the result. Any schema problem shows up while it's cheap to fix, and you leave with a real number for how long the copy takes.

{% stepper %}
{% step %}
### Check for Incompatibilities

Before you dump anything, ask the MySQL source which tables use features that MariaDB stores differently. A MySQL `JSON` column arrives in MariaDB as `LONGTEXT` with a validity check, which is fine for most code but worth knowing about. MySQL's table-level `ENCRYPTION` and `COMPRESSION` options use syntax that MariaDB doesn't accept, so a dump that contains them stops partway through the import.

```sql
-- Columns that use the MySQL JSON type
SELECT table_schema, table_name FROM information_schema.COLUMNS
WHERE data_type = 'JSON';

-- Tables with MySQL encryption or compression options
SELECT table_schema, table_name, create_options FROM information_schema.TABLES
WHERE create_options LIKE '%ENCRYPTION=%' OR create_options LIKE '%COMPRESSION=%';
```

If the second query returns rows, remove those options with `ALTER TABLE` before you dump, and turn them back on with MariaDB syntax afterward. The [MySQL to MariaDB compatibility matrix]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-compatibility-matrix) lists the other differences, including authentication plugins and SQL syntax.
{% endstep %}

{% step %}
### Dump and Load

Use MySQL's own `mysqldump` tool on the source, because MariaDB's `mariadb-dump` tool hasn't been tested as widely against MySQL servers. Name the `shop` database with the `--databases` option instead of `--all-databases`, because MySQL's system databases differ from MariaDB's and fail on import. Then pipe the dump straight into the `mariadb` client on the test server.

```bash
mysqldump --user=root --password --databases shop \
  --single-transaction --routines --events \
  --triggers --hex-blob \
  | mariadb --host=new_server_ip --user=root --password
```

Both tools ask for a password at the same time, so the two prompts can overlap and swallow your input. To avoid that, put the MariaDB password in a `[client-mariadb]` section of the `~/.my.cnf` file on the source host, which the `mariadb` client reads and `mysqldump` ignores, and drop `--password` from the `mariadb` side. Most installs also allow `root` to log in only from `localhost`, so on the `mariadb` side use an account that can connect from the source host and create databases.

The `--single-transaction` option takes a consistent InnoDB snapshot, so checkout keeps writing on MySQL while the dump runs. The `--hex-blob` option keeps binary columns intact. A piped load can't resume if the connection drops, so when the database is large, write the dump to a file first. The [MySQL to MariaDB migration guide]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-migration-the-master-guide) covers the file method, server settings for big imports, and how to port users and privileges.
{% endstep %}

{% step %}
### Verify the Copy

Run the same two statements on MySQL and on MariaDB, then compare the output. Repeat them for every table in the `shop` database, not only the `products` table.

```sql
SELECT COUNT(*) FROM shop.products;
CHECKSUM TABLE shop.products;
```

Row counts must match exactly. A checksum can differ on a table with date and time columns even when the data is the same, because the two servers can store those rows in different formats, so compare those tables row by row. [`CHECKSUM TABLE`]({server}/reference/sql-statements/table-statements/checksum-table) explains what changes the value.

When the numbers agree, refresh the optimizer statistics on MariaDB with the `mariadb-check` tool. The MariaDB optimizer plans queries differently from the MySQL one, and it needs fresh statistics to pick good plans for the shop's queries.

```bash
mariadb-check -u root -p --analyze --all-databases
```
{% endstep %}
{% endstepper %}

## Cut Over

After the rehearsal, you know the dump time, and you know that the copy matches. If the shop can close for that long, repeat the same three steps against the production server and point the application at MariaDB. If it can't close at all, load the copy, then configure MariaDB as a replica of MySQL so that it keeps receiving every new order until you switch the connection string. [Migration from MySQL to MariaDB Galera Cluster using replication]({server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migration-from-mysql-to-mariadb-cluster-using-replication) walks through that setup.

## Keep Going

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MySQL Compatibility Matrix</strong></td><td>Check each MySQL feature your shop uses against the MariaDB version you target.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/mysql-to-mariadb-compatibility-matrix">mysql-to-mariadb-compatibility-matrix</a></td></tr><tr><td><strong>Differences From Other Databases</strong></td><td>See what changes when you move to MariaDB from another database system.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/differences-between-mariadb-and-other-dbmss">differences-between-mariadb-and-other-dbmss</a></td></tr><tr><td><strong>From PostgreSQL</strong></td><td>Translate PostgreSQL types, functions, and syntax to MariaDB.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-postgresql">migrating-to-mariadb-from-postgresql</a></td></tr><tr><td><strong>From Oracle</strong></td><td>Set <code>sql_mode=ORACLE</code> to run much of your PL/SQL without rewriting it.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-oracle">migrating-to-mariadb-from-oracle</a></td></tr><tr><td><strong>From SQL Server</strong></td><td>Map SQL Server types, syntax, and T-SQL habits to MariaDB.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/migrating-to-mariadb-from-sql-server">migrating-to-mariadb-from-sql-server</a></td></tr><tr><td><strong>Into MariaDB Cloud</strong></td><td>Load an existing database into a MariaDB Cloud service instead of a server you run.</td><td><a href="{mariadb-cloud}/cloud-data-handling/migration-data-loading/data-loading-migration">data-loading-migration</a></td></tr></tbody></table>
