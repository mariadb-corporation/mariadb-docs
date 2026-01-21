---
description: >-
  Strategies for moving data from PostgreSQL to MariaDB, using the CONNECT
  storage engine with ODBC/JDBC or foreign data wrappers.
---

# Migrating to MariaDB from PostgreSQL

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/DIKbJcrzYIyfEVdDst6b/" %}

There are many different ways to migrate from [PostgreSQL](https://www.postgresql.org/) to MariaDB. This article will discuss some of those options.

## MariaDB's CONNECT Storage Engine

MariaDB's [CONNECT](../../../server-usage/storage-engines/connect/) storage engine can be used to migrate from PostgreSQL to MariaDB. There are two primary ways that this can be done.

See [Loading the CONNECT Storage Engine](../../../server-usage/storage-engines/connect/installing-the-connect-storage-engine.md) for information on how to install the CONNECT storage engine.

### Tables with ODBC table\_type

The CONNECT storage engine allows you to create tables that refer to tables on an external server, and it can fetch the data using a compatible [ODBC](https://en.wikipedia.org/wiki/Open_Database_Connectivity) driver. PostgreSQL does have a freely available ODBC driver called [psqlODBC](https://odbc.postgresql.org/). Therefore, if you install `psqlODBC` on the MariaDB Server, and then configure the system's ODBC framework (such as [unixODBC](https://www.unixodbc.org/)), then the MariaDB server will be able to connect to the remote PostgreSQL server. At that point, you can create tables with the [ENGINE=CONNECT](../../../reference/sql-statements-and-structure/sql-statements/data-definition/create/create-table.md#storage-engine) and [table\_type=ODBC](../../../server-usage/storage-engines/connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md) table options set, so that you can access the PostgreSQL tables from MariaDB.

See [CONNECT ODBC Table Type: Accessing Tables From Another DBMS](../../../server-usage/storage-engines/connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md) for more information on how to do that.

Once the remote table is setup, you can migrate the data to local tables very simply. For example:

```sql
CREATE TABLE psql_tab (
   id INT,
   str VARCHAR(50)
) ENGINE = CONNECT
table_type=ODBC
tabname='tab'
CONNECTION='DSN=psql_server';

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE = InnoDB;

INSERT INTO tab SELECT * FROM psql_tab;
```

### Tables with JDBC table\_type

The CONNECT storage engine allows you to create tables that refer to tables on an external server, and it can fetch the data using a compatible [JDBC](https://en.wikipedia.org/wiki/Java_Database_Connectivity) driver. PostgreSQL does have a freely available [JDBC driver](https://jdbc.postgresql.org/). If you install this JDBC driver on the MariaDB server, then the MariaDB server will be able to connect to the remote PostgreSQL server via JDBC. At that point, you can create tables with the [ENGINE=CONNECT](../../../server-usage/storage-engines/connect/) and [table\_type=JDBC](../../../server-usage/storage-engines/connect/connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms.md) table options set, so that you can access the PostgreSQL tables from MariaDB.

See [CONNECT JDBC Table Type: Accessing Tables from Another DBMS](../../../server-usage/storage-engines/connect/connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms.md) for more information on how to do that.

Once the remote table is setup, you can migrate the data to local tables very simply. For example:

```sql
CREATE TABLE psql_tab (
   id INT,
   str VARCHAR(50)
) ENGINE = CONNECT
table_type=JDBC
tabname='tab'
CONNECTION='jdbc:postgresql://psql_server/db1';

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE = InnoDB;

INSERT INTO tab SELECT * FROM psql_tab;
```

## PostgreSQL's Foreign Data Wrappers

PostgreSQL's [foreign data wrappers](https://wiki.postgresql.org/wiki/Foreign_data_wrappers) can also be used to migrate from PostgreSQL to MariaDB.

### mysql\_fdw

[mysql\_fdw](https://github.com/EnterpriseDB/mysql_fdw) allows you to create a table in PostgreSQL that actual refers to a remote MySQL or MariaDB server. Since MySQL and MariaDB are compatible at the protocol level, this should also support MariaDB.

The foreign data wrapper also supports writes, so you should be able to write to the remote MariaDB table to migrate your PostgreSQL data. For example:

```sql
CREATE TABLE tab (
   id INT,
   str text
);

INSERT INTO tab VALUES (1, 'str1');

CREATE SERVER mariadb_server
   FOREIGN DATA WRAPPER mysql_fdw
   OPTIONS (host '10.1.1.101', port '3306');

CREATE USER MAPPING FOR postgres
   SERVER mariadb_server
   OPTIONS (username 'foo', password 'bar');

CREATE FOREIGN TABLE mariadb_tab (
   id INT,
   str text
)
SERVER mariadb_server
OPTIONS (dbname 'db1', table_name 'tab');

INSERT INTO mariadb_tab SELECT * FROM tab;
```

## PostgreSQL's COPY TO

PostgreSQL's [COPY TO](https://www.postgresql.org/docs/current/sql-copy.html) allows you to copy the data from a PostgreSQL table to a text file. This data can then be loaded into MariaDB with [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

## MySQL Workbench

MySQL Workbench has a [migration feature](https://www.mysql.com/products/workbench/migrate/) that requires an [ODBC](https://en.wikipedia.org/wiki/Open_Database_Connectivity) driver. PostgreSQL does have a freely available ODBC driver called [psqlODBC](https://odbc.postgresql.org/).

See [Set up and configure PostgreSQL ODBC drivers for the MySQL Workbench Migration Wizard](https://mysqlworkbench.org/2012/11/set-up-and-configure-postgresql-odbc-drivers-for-the-mysql-workbench-migration-wizard/) for more information.

## Known Issues

### Migrating Functions and Procedures

PostgreSQL's [functions](https://www.postgresql.org/docs/current/sql-createfunction.html) and [procedures](https://www.postgresql.org/docs/11/sql-createprocedure.html) use a language called [PL/pgSQL](https://www.postgresql.org/docs/current/plpgsql.html). This language is quite different than the default `SQL/PSM` language used for MariaDB's [stored procedures](../../../server-usage/stored-routines/stored-procedures/). `PL/pgSQL` is more similar to `PL/PSQL` from Oracle, so you may find it beneficial to try migrate with [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) set.

## See also

* [Set up and configure PostgreSQL ODBC drivers for the MySQL Workbench Migration Wizard](https://mysqlworkbench.org/2012/11/set-up-and-configure-postgresql-odbc-drivers-for-the-mysql-workbench-migration-wizard/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
