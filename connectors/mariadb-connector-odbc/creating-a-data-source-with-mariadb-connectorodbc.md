---
description: >-
  Create a data source with MariaDB Connector/ODBC on Windows using ODBC
  Data Source Administrator or on Linux by configuring UnixODBC with a
  driver entry and DSN for MariaDB Server.
---

# Creating a Data Source with MariaDB Connector/ODBC

**MariaDB Connector/ODBC** is a database driver that uses the industry standard [Open Database Connectivity (ODBC) API](https://en.wikipedia.org/wiki/Open_Database_Connectivity). Some of the key features of the driver are:

* It is [LGPL-licensed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/faq/licensing-questions/licensing-faq).
* It is compliant with the ODBC 3.5 standard.
* It can be used as a drop-in replacement for MySQL Connector/ODBC.
* It supports both Unicode and ANSI modes.
* It primarily uses the MariaDB/MySQL binary protocol (i.e. server-side [prepared statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/prepared-statements)).

The current release series are:

* MariaDB Connector/ODBC 3.2 is the current stable release series.
* MariaDB Connector/ODBC 3.1 is the previous stable release series, which is currently still supported.

This page discusses how to create a data source with MariaDB Connector/ODBC.

## Creating a Data Source with MariaDB Connector/ODBC on Windows

To create a data source on Windows, you would use the [ODBC Data Source Administrator](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/open-the-odbc-data-source-administrator?view=sql-server-2017).

{% hint style="success" %}
If you are using the 64-bit version of MariaDB Connector/ODBC, then make sure you use the 64-bit version of ODBC Data Source Administrator. Similarly, if you are using the 32-bit version of MariaDB Connector/ODBC, then make sure you use the 32-bit version of ODBC Data Source Administrator.
{% endhint %}

To open the ODBC Data Source Administrator in **Windows 10**:

* On the Start page, type ODBC Data Sources. The ODBC Data Sources Desktop App should appear as a choice.

To open the ODBC Data Source Administrator in **Windows 7**:

* On the Start menu, click Control Panel.
* In Control Panel, click Administrative Tools.
* In Administrative Tools, click Data Sources (ODBC).

To open the ODBC Data Source Administrator in **Windows Server 2008**:

* On the Start menu, point to Administrative Tools, and then click Data Sources (ODBC).

## Creating a Data Source with MariaDB Connector/ODBC on Linux

Linux uses [UnixODBC](https://www.unixodbc.org) as a Driver Manager. To create a data source on Linux, there are two steps:

* First, configure UnixODBC to recognize MariaDB Connector/ODBC as a `Driver`.
* Second, configure UnixODBC with a Data Source Name (DSN) for your MariaDB Server.

You will need to ensure that [UnixODBC has been installed](creating-a-data-source-with-mariadb-connectorodbc.md#changing-unixodbcs-configuration-file-paths) before you can perform these steps.

### Configuring MariaDB Connector/ODBC as a UnixODBC Driver on Linux

The first step is to configure UnixODBC to recognize MariaDB Connector/ODBC as a `Driver`. To configure the `Driver`, you can use the [odbcinst](https://manpages.debian.org/stretch/odbcinst/odbcinst.1.en.html) tool, which can add a configuration entry for MariaDB Connector/ODBC to the system's global `/etc/odbcinst.ini` file.

For example, create a template file similar to the following, with a name like `MariaDB_odbc_driver_template.ini`:

```
[MariaDB ODBC 3.0 Driver]
Description = MariaDB Connector/ODBC v.3.0
Driver = /usr/lib64/libmaodbc.so
```

And then install it to the system's global `/etc/odbcinst.ini` file with the following command:

```bash
sudo odbcinst -i -d -f MariaDB_odbc_driver_template.ini
```

At this point, you should be able to connect to MariaDB by using the `Driver` with the `SQLDriverConnect` function. To connect with `SQLDriverConnect`, you would need to specify `Driver={MariaDB ODBC 3.0 Driver}` in your connection string along with your other connection parameters.

See [Parameters](mariadb-connector-odbc-guide.md#parameters) for connection string options.

### Configuring a DSN with UnixODBC on Linux

The second step is to configure UnixODBC with a Data Source Name (DSN) for your MariaDB Server. A `DSN` allows you to centrally configure all of your server's connection parameters, so that you can easily configure how to connect to your server in your environment. To configure the `DSN`, you can use the [odbcinst](https://manpages.debian.org/stretch/odbcinst/odbcinst.1.en.html) tool, which can add a configuration entry for the given data source to the system's global `/etc/odbc.ini` file or your user's local `~/.odbc.ini` file.

For example, create a template file similar to the following, with a name like `MariaDB_odbc_data_source_template.ini`:

```
[MariaDB-server]
Description=MariaDB server
Driver=MariaDB ODBC 3.0 Driver
SERVER=<your server>
USER=<your user>
PASSWORD=<your password>
DATABASE=<your database>
PORT=<your port>
```

And then you can install it to the system's global `/etc/odbc.ini` file with the following command:

```bash
sudo odbcinst -i -s -l -f MariaDB_odbc_data_source_template.ini
```

Or you can install it to your user's local `~/.odbc.ini` file with the following command:

```bash
odbcinst -i -s -h -f MariaDB_odbc_data_source_template.ini
```

At this point, you should be able to connect to MariaDB by using the `DSN` with either `SQLConnect` or the `SQLDriverConnect` functions. To connect with `SQLConnect`, you would have to provide `MariaDB-server` as the `ServerName` parameter. To connect with `SQLDriverConnect`, you would have to provide `DSN={MariaDB-server}` in the connection string along with your other connection parameters.

See [Parameters](mariadb-connector-odbc-guide.md#parameters) for connection string options.

{% hint style="danger" %}
UnixODBC also provides a GUI to add `DSNs`. However, MariaDB Connector/ODBC doesn't yet support this GUI interface for adding `DSNs`.
{% endhint %}

### Verifying a DSN Configuration with UnixODBC on Linux

You can verify that a `DSN` is properly configured with UnixODBC on Linux by using the [isql](https://manpages.debian.org/stretch/unixodbc/isql.1.en.html) utility.

For example, if the `DSN` is called `MariaDB-server`, then we can verify that it works properly by executing the following:

```bash
$ isql MariaDB-server
```

```sql
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+
SQL> SELECT @@global.hostname;
+-------------------------------------------+
| @@global.hostname                         |
+-------------------------------------------+
| ip-172-30-0-249.us-west-2.compute.internal|
+-------------------------------------------+
SQLRowCount returns 1
1 rows fetched
SQL> quit
```

### Changing UnixODBC's Configuration File Paths

You can also change the paths that unixODBC uses for its configuration files by changing some environment variables. For example:

* `ODBCSYSINI` - Overloads path to unixODBC configuration files. By default equals to `/etc`.
* `ODBCINSTINI` - Overloads the name of the drivers configuration file. It is relative to `ODBCSYSINI` and by default set to `odbcinst.ini`.
* `ODBCINI` - Overloads the path to user configuration file. By default it is set to `~/.odbc.ini`.

## Creating a Data Source with MariaDB Connector/ODBC on Mac OS X

Mac OS X uses [iODBC](https://www.iodbc.org) as a Driver Manager. To create a data source on Mac OS X, there are two primary ways to do it:

* You can create a data source with the [iODBC Administrator](https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/Downloads#Mac%20OS%20X) GUI tool.
* You can create a data source by manually editing the [iODBC configuration file](https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/ODBCMacOSX#Configuring).

### Creating a Data Source with iODBC Administrator on Mac OS X

iODBC Administrator is not installed by default. In order to use it, you need to download it from [iODBC's download page](https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/Downloads#Mac%20OS%20X) and then install it.

### Creating a Data Source with iODBC on Mac OS X

The steps to create a data source with iODBC on Mac OS X can be found [here](https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/ODBCMacOSX#Configuring). There are essentially two steps:

* First, configure iODBC to recognize MariaDB Connector/ODBC as a `Driver`.
* Second, configure iODBC with a Data Source Name (DSN) for your MariaDB Server.

#### Configuring MariaDB Connector/ODBC as a iODBC Driver on Mac OS X

The first step is to configure iODBC to recognize MariaDB Connector/ODBC as a `Driver`.

The iODBC `Driver` configuration file might be at one of these paths:

* The path specified by the `$ODBCINSTINI` environment variable.
* `~/.odbcinst.ini`
* `~/Library/ODBC/odbcinst.ini`
* `/etc/odbcinst.ini`
* `/Library/ODBC/odbcinst.ini`

{% hint style="success" %}
MariaDB Connector/ODBC's [PKG package](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-server-pkg-packages-on-macos) automatically configures itself as a `Driver` in `/Library/ODBC/odbcinst.ini`, so you can most likely skip this step.
{% endhint %}

To add MariaDB Connector/ODBC as a `Driver`, the configuration file would look something like the following:

```
[ODBC Drivers]
MariaDB ODBC 3.1 Driver = installed

[MariaDB ODBC 3.1 Driver]
Description=MariaDB Connector/ODBC v.3.1
Driver=/Library/MariaDB/MariaDB-Connector-ODBC/libmaodbc.dylib
Threading=0
```

#### Configuring a DSN with iODBC on Mac OS X

The second step is to configure iODBC with a Data Source Name (DSN) for your MariaDB Server. A `DSN` allows you to centrally configure all of your server's connection parameters, so that you can easily configure how to connect to your server in your environment.

The iODBC `DSN` configuration file might be at one of these paths:

* The path specified by the `$ODBCINI` environment variable.
* `~/.odbc.ini`
* `~/Library/ODBC/odbc.ini`
* `/etc/odbc.ini`
* `/Library/ODBC/odbc.ini`

To add a `DSN` that uses MariaDB Connector/ODBC, the configuration file would look something like the following:

```
[ODBC]
Debug = 1
DebugFile = /tmp/odbc-debugfile.log
Trace = 0
TraceFile = /tmp/odbc-tracefile.log
TraceAutoStop = 1

[ODBC Data Sources]
MariaDB-server = MariaDB ODBC 3.1 Driver

[MariaDB-server]
Description = MariaDB server
Driver = /Library/MariaDB/MariaDB-Connector-ODBC/libmaodbc.dylib
SERVER=<your server>
USER=<your user>
PASSWORD=<your password>
DATABASE=<your database>
PORT=<your port>
```

#### Verifying a DSN Configuration with iODBC on Mac OS X

You can verify that a `DSN` is properly configured with iODBC on Mac OS X by using the [iodbctest](https://manpages.debian.org/stretch/iodbc/iodbctest.1.en.html) utility.

For example, if the `DSN` is called `MariaDB-server`, then we can verify that it works properly by executing the following:

```bash
$ iodbctest "DSN=MariaDB-server"
```

{% @marketo/form formId="4316" %}
