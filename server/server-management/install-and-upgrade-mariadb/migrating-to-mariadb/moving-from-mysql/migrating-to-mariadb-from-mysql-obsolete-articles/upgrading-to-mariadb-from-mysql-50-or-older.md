---
description: >-
  Outdated page regarding migrating from MySQL to MariaDB Server. While
  potentially outdated, these resources may offer historical context or insights
  for specific scenarios.
---

# Upgrading to MariaDB From MySQL 5.0 or Older

If you upgrade to [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.1/changes-improvements-in-mariadb-5-1) from MySQL 5.1 you [don't have to do anything](../upgrading-from-mysql-to-mariadb.md) with your data or MySQL clients. Things should "just work".

When upgrading between different major versions of MariaDB or MySQL you need to\
run the [mysql\_upgrade](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md) program to convert data that are incompatible between versions. This will also update your privilege tables in the mysql database to the latest format.

In almost all cases [mysql\_upgrade](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md) should be able to convert your tables, without you having to dump and restore your data.

After installing MariaDB, just do:

```
mysql_upgrade --verbose
```

If you want to run with a specific TCP/IP port do:

```
mysql_upgrade --host=127.0.0.1 --port=3308 --protocol=tcp
```

If you want to connect with a socket do:

```
mysql_upgrade --socket=127.0.0.1 --protocol=socket
```

To see other options, use [--help](../../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md).

"mysql\_upgrade" reads the [my.cnf](../../../configuring-mariadb/configuring-mariadb-with-option-files.md) sections \[mysql\_upgrade] and \[client] for default values.

There are a variety of reasons tables need to be converted; they could be any of the following:

* The collation (sorting order) for an index column has changed
* A field type has changed storage format
  * [DECIMAL](../../../../../reference/data-types/numeric-data-types/decimal.md) and [VARCHAR](../../../../../reference/data-types/string-data-types/varchar.md) changed format between MySQL 4.1 and MySQL 5.0
* An engine has a new storage format
  * [ARCHIVE](../../../../../server-usage/storage-engines/archive.md) changed storage format between 5.0 and 5.1
* The format for storing [table names](../../../../../reference/sql-structure/sql-language-structure/identifier-names.md) has changed
  * In MySQL 5.1 table names are encoded so that the file names are identical on all computers. Old table names that contains forbidden file name characters will show up prefixed with #mysql50

## in `SHOW TABLES` until you convert them.

If you don't convert the tables, one of the following things may happen:

* You will get warnings in the error log every time you access a table with an invalid (old) file name.
* When searching on key values you may not find all rows
* You will get an error "ERROR 1459 (HY000): Table upgrade required" when accessing the table.
* You may get crashes

"mysql\_upgrade" works by calling mysqlcheck with different options and running the "mysql\_fix\_privileges" script. If you have trouble with "mysql\_upgrade", you can run these commands separately to get more information of what is going on.

Most of the things in the [MySQL 5.1 manual](https://dev.mysql.com/doc/refman/5.1/en/upgrading.html) section also applies to MariaDB.

The following differences exists between "mysql\_upgrade" in MariaDB and MySQL (as of [MariaDB 5.1.50](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.1/5.1.50)):

* MariaDB will convert long table names properly.
* MariaDB will convert [InnoDB](../../../../../server-usage/storage-engines/innodb/) tables (no need to do a dump/restore or [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/)).
* MariaDB will convert old archive tables to the new 5.1 format (note: new feature in testing).
* "mysql\_upgrade --verbose" will run "mysqlcheck --verbose" so that you get more information of what is happening.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
