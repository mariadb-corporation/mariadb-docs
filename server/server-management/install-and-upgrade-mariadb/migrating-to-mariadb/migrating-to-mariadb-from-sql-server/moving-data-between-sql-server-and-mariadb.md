# Moving Data Between SQL Server and MariaDB

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

There are several ways to move data between SQL Server and MariaDB. Here we will discuss them and we will highlight some caveats.

## Moving Data Definition from SQL Server to MariaDB

To copy SQL Server data structures to MariaDB, one has to:

1. Generate a CSV file from SQL Server data.
2. Modify the syntax so that it works in MariaDB.
3. Run the file in MariaDB.

### Variables That Affect DDL Statements

DDL statements are affected by some server system variables.

[sql\_mode](../../../variables-and-modes/sql_mode.md) determines the behavior of some SQL statements and expressions, including how strict error checking is, and some details regarding the syntax. Objects like [stored procedures](../../../../server-usage/stored-routines/stored-procedures/), [stored functions](../../../../server-usage/stored-routines/stored-functions/) [triggers](../../../../server-usage/triggers-events/triggers/) and [views](../../../../server-usage/views/), are always executed with the sql\_mode that was in effect during their creation. [sql\_mode='MSSQL'](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql) can be used to have MariaDB behaving as close to SQL Server as possible.

[innodb\_strict\_mode](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_strict_mode) enables the so-called InnoDB strict mode. Normally some errors in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) options are ignored. When InnoDB strict mode is enabled, the creation of InnoDB tables will fail with an error when certain mistakes are made.

[updatable\_views\_with\_limit](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#updatable_views_with_limit) determines whether view updates can be made with an [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) or [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statement with a `LIMIT` clause if the view does not contain all primary or not null unique key columns from the underlying table.

### Dumps and sys.sql\_modules

SQL Server Management Studio allows one to create a working SQL script to recreate a database - something that MariaDB users refer to as a _dump_. Several options allow fine-tuning the generated syntax. It could be necessary to adjust some of these options to make the output compatible with MariaDB. It is possible to export schemas, data or both. One can create a single global file, or one file for each exported object. Normally, producing a single file is more practical.

Alternatively, the [sp\_helptext()](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-helptext-transact-sql) procedure returns information about how to recreate a certain object. Similar information is also present in the [sql\_modules](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-sql-modules-transact-sql) table (`definition` column), in the `sys` schema. Such information, however, is not a ready-to-use set of SQL statements.

Remember however that [MariaDB does not support schemas](understanding-mariadb-architecture.md#databases). An SQL Server schema is approximately a MariaDB database.

To execute a dump, we can pass the file to [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md), the MariaDB command-line client.

Provided that a dump file contains syntax that is valid in MariaDB, it can be executed in this way:

```bash
mariadb --show-warnings < dump.sql
```

`--show-warnings` tells MariaDB to output any warnings produced by the statements contained in the dump. Without this option, warnings will not appear on screen. Warnings don't stop the dump execution.

Errors will appear on screen. Errors will stop the dump execution, unless the `--force` option (or just `-f`) is specified.

For other `mariadb` options, see [mariadb Command-line Client Options](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#options).

Another way to achieve the same purpose is to start the `mariadb` client in interactive mode first, and then run the `source` command. For example:

```bash
root@d5a54a082d1b:/# mariadb -uroot -psecret
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 22
Server version: 10.4.7-MariaDB-1:10.4.7+maria~bionic mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> \W
Show warnings enabled.
MariaDB [(none)]> source dump.sql
```

In this case, to show warnings we used the `\W` command, where "w" is uppercase. To hide warnings (which is the default), we can use `\w` (lowercase).

For other `mariadb` commands, see [mariadb Commands](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#mariadb-commands).

### CSV Data

If the table structures are already in MariaDB, we need only to import table data. While this can still be done as explained above, it may be more practical to export CSV files from SQL Server and import them into MariaDB.

SQL Server Management Studio and several other Microsoft tools allow one to export CSV files.

MariaDB allows importing CSV files with the [LOAD DATA INFILE](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement, which is essentially the MariaDB equivalent of `BULK INSERT`.

It can happen that we don't want to import the whole data, but some filtered or transformed version of it. In that case, we may prefer to use the [CONNECT](../../../../server-usage/storage-engines/connect/) storage engine to access CSV files and query them. The results of a query can be inserted into a table using [INSERT SELECT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-select.md).

## Moving Data from MariaDB to SQL Server

There are several ways to move data from MariaDB to SQL Server:

* If the tables don't exist at all in SQL Server, we need to generate a dump first. The dump can include data or not.
* If the tables are already in SQL Server, we can use CSV files instead of dumps to move the rows. CSV files are the most concise format to move data between different technologies.
* With the tables already in SQL Server, another way to move data is to insert the rows into [CONNECT](../../../../server-usage/storage-engines/connect/) tables that "point" to remote SQL Server tables.

### Using a Dump (Structure)

[mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) can be used to generate dumps of all databases, a specified database, or a set of tables. It is even possible to only dump a set of rows by specifying the `WHERE` clause.

By specifying the `--no-data` option we can dump the table structures without data.

`--compatible=mssql` will produce an output that should be usable in SQL Server.

### Using a Dump (Data)

mariadb-dump by default produces an output with both data and structure.

`--no-create-info` can be used to skip the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statements.

`--compatible=mssql` will produce an output that should be usable in SQL Server.

`--single-transaction` should be specified to select the source data in a single transaction, so that a consistent dump is produced.

`--quick` speeds up the dump process when dumping big tables.

### Using a CSV File

CSV files can also be used to export data to SQL Server. There are several ways to produce CSV files from MariaDB:

* The [SELECT INTO OUTFILE](../../../../reference/sql-statements/data-manipulation/selecting-data/select-into-outfile.md) statement.
* The [CONNECT](../../../../server-usage/storage-engines/connect/) storage engine, with the [CSV table type](../../../../server-usage/storage-engines/connect/connect-table-types/connect-csv-and-fmt-table-types.md).
* The [CSV](../../../../server-usage/storage-engines/csv/) storage engine (note that it doesn't support `NULL` and indexes).

### Using CONNECT Tables

The [CONNECT](../../../../server-usage/storage-engines/connect/) storage engine allows one to access external data, in many forms:

* [Data files](../../../../server-usage/storage-engines/connect/connect-table-types/connect-table-types-data-files.md) ([CSV](../../../../server-usage/storage-engines/connect/connect-table-types/connect-csv-and-fmt-table-types.md), [JSON](../../../../server-usage/storage-engines/connect/connect-table-types/connect-json-table-type.md), [XML](../../../../server-usage/storage-engines/connect/connect-table-types/connect-xml-table-type.md), HTML and more).
* Remote databases, using the [ODBC](../../../../server-usage/storage-engines/connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md) or [JDBC](../../../../server-usage/storage-engines/connect/connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms.md) standards, or [MariaDB/MySQL native protocol](../../../../server-usage/storage-engines/connect/connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables.md).
* Some [special data sources](../../../../server-usage/storage-engines/connect/connect-table-types/connect-table-types-special-virtual-tables.md).

`CONNECT` was mentioned previously because it could allow one to read a CSV file and query it in SQL, filtering and transforming the data that we want to move into regular MariaDB tables.

However, `CONNECT` can also access remote SQL Server tables. We can read data from it, or even write data.

To enable `CONNECT` to work with SQL Server, we need to fulfill these requirements:

* Install the ODBC driver, downloadable form [Microsoft](https://microsoft.com/) website. The driver is also available for Linux and MacOS.
* Install [unixODBC](https://www.unixodbc.org/).
* [Install CONNECT](../../../../server-usage/storage-engines/connect/installing-the-connect-storage-engine.md) (unless it is already installed).

Here is an example of a `CONNECT` table that points to a SQL Server table:

```sql
CREATE TABLE city (
    id INT PRIMARY KEY,
    city_name VARCHAR(100),
    province_id INT NOT NULL
)
    ENGINE=CONNECT,
    TABLE_TYPE=ODBC,
    TABNAME='city'
    CONNECTION='Driver=SQL Server Native Client 13.0;Server=sql-server-hostname;Database=world;UID=mariadb_connect;PWD=secret';
```

The key points here are:

* `ENGINE=CONNECT` tells MariaDB that we want to create a `CONNECT` table.
* `TABLE_TYPE` must be 'ODBC', so `CONNECT` knows what type of data source it has to use.
* `CONNECTION` is the connection string to use, including server address, username and password.
* `TABNAME` tells `CONNECT` what the remote table is called. The local name could be different.

`CONNECT` is able to query SQL Server to find out the remote table structure. We can use this feature to avoid specifying the column names and types:

```sql
CREATE TABLE city
    ENGINE=CONNECT,
    TABLE_TYPE=ODBC,
    TABNAME='city'
    CONNECTION='Driver=SQL Server Native Client 13.0;Server=sql-server-hostname;Database=world;UID=mariadb_connect;PWD=secret';
```

However, we may prefer to manually specify the MariaDB types, sizes and character sets to use.

### Linked Server

Instead of using MariaDB `CONNECT`, it is possible to use SQL Server Linked Server functionality. This will allow one to read data from a remote MariaDB database and copy it into local SQL Server tables. However, note that `CONNECT` allows more control on [types and character sets](sql-server-and-mariadb-types-comparison.md) mapping.

Refer to [Linked Servers](https://docs.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine?view=sql-server-ver15) section in Microsoft documentation.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
