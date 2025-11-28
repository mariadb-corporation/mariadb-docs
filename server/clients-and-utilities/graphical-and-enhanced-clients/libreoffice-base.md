# LibreOffice Base

[LibreOffice Base](https://www.libreoffice.org/discover/base/) is an open source RDBMS (relational database management system) frontend tool to create and manage various databases.

## Preparing the ODBC Connection

First, make sure to prepare MariaDB Connector/ODBC as explained in [MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc).

This includes

* downloading [the latest MariaDB Connector/ODBC](https://mariadb.com/downloads/#connectors),
* copying the shared library libmaodbc.so to /usr/lib/\[multi-arch],
* installing the unixodbc, unixodbc-dev, openssh-client, odbcinst packages, and
* creating a template file for the [ODBC driver](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc#configuring-mariadb-connectorodbc-as-a-unixodbc-driver-on-linux). 
* Install the ODBC driver from the template file by running:

```bash
$ sudo odbcinst -i -d -f MariaDB_odbc_driver_template.ini
odbcinst: Driver installed. Usage count increased to 1. 
    Target directory is /etc
```

Verify the installation was successful in `/etc/odbcinst.ini` file (this path is obtained by the config info _/-j_/ option, where drivers are installed in that predefined location).

```bash
$ odbcinst -j
unixODBC 2.3.6
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /home/anel/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8

$ cat /etc/odbcinst.ini 
[MariaDB ODBC 3.1 Driver]
Description=MariaDB Connector/ODBC v.3.1
Driver=/usr/lib/x86_64-linux-gnu/libmaodbc.so
UsageCount=1
```

* Create a template file for the [Data Source Name (DSN)](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc#configuring-a-dsn-with-unixodbc-on-linux). A sample “MariaDB\_odbc\_data\_source\_template.ini” could be:

|                                |
| ------------------------------ |
| \[MariaDB-server]              |
| Description=MariaDB server     |
| Driver=MariaDB ODBC 3.1 Driver |
| SERVER=localhost               |
| USER=anel                      |
| PASSWORD=                      |
| DATABASE=test                  |
| PORT=3306                      |

* Install data source:

```bash
odbcinst -i -s -h -f MariaDB_odbc_data_source_template.ini
```

* Verify successful installation in the /.odbc.ini file

```bash
$ cat ~/.odbc.ini 
[MariaDB-server]
Description=MariaDB server
Driver=MariaDB ODBC 3.1 Driver
SERVER=MariaDB
USER=anel
PASSWORD=
DATABASE=test
PORT=3306
```

* Verify successful installation also using the [isql](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc#verifying-a-dsn-configuration-with-unixodbc-on-linux) utility:

```bash
$ isql MariaDB-server
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+
SQL> show tables;
+--------------------------------------------------------------------------+
| Tables_in_test                                                           |
+--------------------------------------------------------------------------+
| Authors                                                                  |
| tbl_names                                                                |
| webposts                                                                 |
| webusers                                                                 |
+--------------------------------------------------------------------------+
SQLRowCount returns 4
4 rows fetched
```

## Start with LibreOffice Base

Start Libreoffice Base from the terminal by running _lobase_ (make sure to install the _libreoffice-base_ package if needed). The default option is to create a new database, which is _HSQLDB_. In order to connect to a running MariaDB server, choose _“Connect to an existing database”_ and choose _“ODBC”_ driver as shown below:

![](../../.gitbook/assets/librebase_1.png)

After that, choose DSN (the one that we created in the previous step) and click _“Next”_:

![](../../.gitbook/assets/librebase_2.png)

Provide a user name (and password if needed) and again check the connection (with the _“Test Connection”_ button) and click _“Next”_:

![](../../.gitbook/assets/librebase_3.png)

After that, we have options to register the database. Registration in this sense means that the database is viewable by other LibreOffice modules (like _LibreOffice Calc_ and _LibreOffice Writer_). So this step is optional. In this example, we will save as _“fosdem21\_mariadb.odb”_. See [Using a Registered Database](libreoffice-base.md#using-a-registered-database).

![](../../.gitbook/assets/librebase_4.png)

It opens the following window:

![](../../.gitbook/assets/librebase_5.png)

It consists of three panels:

1. “Database” window with the options,
2. "Tables",
3. "Queries",
4. "Forms",
5. "Reports".
6. "Tasks window (dependent on what is selected in the “Database” window). When “Tables” is selected, the options are:
7. "Create Table in Design View",
8. "Use Wizard to Create Table" and
9. "Create View".
10. "Tables" window - shows list of tables that are created.

As we can see, there are system tables in the _“mysql”_ database as well as _“test”_ database.

Let’s say we create a table using the REST API from JSON data from [posts](https://jsonplaceholder.typicode.com/posts), and another table using the same mechanism from [users](https://jsonplaceholder.typicode.com/users), and let’s call them _webposts_ and _webusers_. In order to do so, we have to enable the **CONNECT** storage engine plugin and start with REST\_API. See more in the [CONNECT - Files Retrieved Using Rest Queries](../../server-usage/storage-engines/connect/connect-table-types/connect-files-retrieved-using-rest-queries.md) article.

The queries we need to run in MariaDB are:

```sql
CREATE TABLE webusers ENGINE=CONNECT TABLE_TYPE=JSON
  HTTP='http://jsonplaceholder.typicode.com/users';

CREATE TABLE webposts ENGINE=CONNECT TABLE_TYPE=JSON
  HTTP='http://jsonplaceholder.typicode.com/posts';
```

The result in LibreOffice Base is as shown below:

![librebase\_6](../../.gitbook/assets/librebase_6.png)

Double clicking on the table opens a new window with the data displayed to inspect:

![](../../.gitbook/assets/librebase_7.png)

To create the table from the _“Tasks”_ window, use the option _“Create Table in Design View”_, where one can specify specific field names and types as shown:

![](../../.gitbook/assets/librebase_8.png)

From the “Tasks” window one can create a table using the option _“Use Wizard to Create Table”_ to create some sample tables.

One can fill the data in the existing table, or create and define the new table from the _LibreOffice Calc_ module with simple copy-paste (in the _"Tasks"_ window).

## Using a Registered Database

Other modules can use the registered database, for example, open _"LibreOffice Calc"_ and go to _"Tools"_, _"Options"_ and you will see the _"odb"_ file we registered when starting _"LibreOffice Base"_.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
