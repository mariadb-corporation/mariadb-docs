---
description: The CONNECT storage engine.
---

# CONNECT JDBC Table Type: Accessing Tables from Another DBMS

The JDBC table type should be distributed with all recent versions of MariaDB. However, if the automatic compilation of it is possible after the java JDK was installed, the complete distribution of it is not fully implemented in older versions. The distributed JdbcInterface.jar file contains the JdbcInterface wrapper only. New versions distribute a JavaWrappers.jar that contains all currently existing wrappers.

This will require that:

1. The Java SDK is installed on your system.
2. The java wrapper class files are available on your system.
3. And of course, some JDBC drivers exist to be used with the matching DBMS.

Point 2 was made automatic in the newest versions of MariaDB.

## Compiling From Source Distribution

Even when the Java JDK has been installed, CMake sometimes cannot find the location where it stands. For instance on Linux the Oracle Java JDK package might be installed in a path not known by the CMake lookup functions causing error message such as:

```
CMake Error at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:148 (message): 
  Could NOT find Java (missing: Java_JAR_EXECUTABLE Java_JAVAC_EXECUTABLE 
  Java_JAVAH_EXECUTABLE Java_JAVADOC_EXECUTABLE)
```

When this happen, provide a Java prefix as a hint on where the package was loaded. For instance on Ubuntu I was obliged to enter:

```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
```

After that, the compilation of the CONNECT JDBC type was completed successfully.

### Compiling the Java source files

They are the source of the java wrapper classes used to access JDBC drivers. In the source distribution, they are located in the CONNECT source directory.

The default wrapper, JdbcInterface, is the only one distributed with binary distribution. It uses the standard way to get a connection to the drivers via the DriverManager.getConnection method. Other wrappers, only available with source distribution, enable connection to a Data Source, eventually implementing pooling. However, they must be compiled and installed manually.

The available wrappers are:

| Wrapper             | Description                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| JdbcInterface       | Used to make the connection with available drivers the standard way.                                                           |
| ApacheInterface     | Based on the Apache common-dbcp2 package this interface enables making connections to DBCP data sources with any JDBC drivers. |
| MariadbInterface    | Makes connection to a MariaDB data source.                                                                                     |
| MysqlInterface      | Makes connection to a Mysql data source. Must be used with a MySQL driver that implements data sources.                        |
| OracleInterface     | Makes connection to an Oracle data source.                                                                                     |
| PostgresqlInterface | Makes connection to a Postgresql data source.                                                                                  |

The wrapper used by default is specified by the [connect\_java\_wrapper](../connect-system-variables.md#connect_java_wrapper) session variable and is initially set to `wrappers/JdbcInterface`. The wrapper to use for a table can also be specified in the option list as a wrapper option of the “create table” statements.

Note: Conforming java naming usage, class names are preceded by the java package name with a slash separator. However, this is not mandatory for CONNECT which adds the package name if it is missing.

The JdbcInterface wrapper is always usable when Java is present on your machine. Binary distributions have this wrapper already compiled as a JdbcInterface.jar file installed in the plugin directory whose path is automatically included in the class path of the JVM. Recent versions also add a JavaWrappers.jar that contains all these wrappers. Therefore there is no need to worry about its path.

Compiling the ApacheInterface wrapper requires that the Apache common-DBCP2 package be installed. Other wrappers are to be used only with the matching JDBC drivers that must be available when compiling them.

Installing the jar file in the plugin directory is the best place because it is part of the class path. Depending on what is installed on your system, the source files can be reduced accordingly. To compile only the JdbcInterface.java file the CMAKE\_JAVA\_INCLUDE\_PATH is not required. Here the paths are the ones existing on my Windows 7 machine and should be localized.

## Setting the Required Information

Before any operation with a JDBC driver can be made, CONNECT must initialize the environment that will make working with Java possible. This will consist of:

1. Loading dynamically the JVM library module.
2. Creating the Java Virtual Machine.
3. Establishing contact with the java wrapper class.
4. Connecting to the used JDBC driver.

Indeed, the JVM library module is not statically linked to the CONNECT plugin. This is to make it possible to use a CONNECT plugin that has been compiled with the JDBC table type on a machine where the Java SDK is not installed. Otherwise, users not interested in the JDBC table type would be obliged to install the Java SDK on their machine to be able to load the CONNECT storage engine.

### JVM Library Location

If the JVM library (jvm.dll on Windows, libjvm.so on Linux) was not placed in the standard library load path, CONNECT cannot find it and must be told where to search for it. This happens in particular on Linux when the Oracle Javapackage was installed in a private location.

If the JAVA\_HOME variable was exported as explained above, CONNECT can sometimes find it using this information. Otherwise, its search path can be added to the LD\_LIBRARY\_PATH environment variable. But all this is complicated because making environment variables permanent on Linux is painful (many different methods must be used depending on the Linux version and the used shell).

This is why CONNECT introduced a new global variable connect\_jvm\_path to store this information. It can be set when starting the server as a command line option or even afterwards before the first use of the JDBC table type:

```
set global connect_jvm_path="/usr/lib/jvm/java-8-oracle/jre/lib/i386/client"
```

or

```
set global connect_jvm_path="/usr/lib/jvm/java-8-oracle/jre/lib/i386/server"
```

The client library is smaller and faster for connection. The server library is more optimized and can be used in case of heavy load usage.

Note that this may not be required on Windows because the path to the JVM library can sometimes be found in the registry.

Once this library is loaded, CONNECT can create the required Java Virtual Machine.

### Java Class Path

This is the list of paths Java searches when loading classes. With CONNECT, the classes to load are the java wrapper classes used to communicate with the drivers , and the used JDBC driver classes that are grouped inside jar files. If the ApacheInterface wrapper must be used, the class path must also include all three jars used by the Apache package.

Caution: This class path is passed as a parameter to the Java Virtual Machine (JVM) when creating it and cannot be modified as it is a read only property. In addition, because MariaDB is a multi-threading application, this JVM cannot be destroyed and are used throughout the entire life of the MariaDB server. Therefore, be sure it is correctly set before you use the JDBC table type for the first time. Otherwise, there are practically no alternative than to shut down the server and restart it.

The path to the wrapper classes must point to the directory containing the wrappers sub-directory. If a JdbcInterface.jar file was made, its path is the directory where it is located followed by the jar file name. It is unclear where because this will depend on the installation process. If you start from a source distribution, it can be in the storage/connect directory where the CONNECT source files are or where you moved them or compiled the JdbcInterface.jar file.

For binary distributions, there is nothing to do because the jar file has been installed in the mysql share directory whose path is always automatically included in the class path available to the JVM.

Remaining are the paths of all the installed JDBC drivers that you intend to use. Remember that their path must include the jar file itself. Some applications use an environment variable CLASSPATH to contain them. Paths are separated by ‘:’ on Linux and by ‘;’ on Windows.

If the CLASSPATH variable actually exists and if it is available inside MariaDB, so far so good. You can check this using an UDF function provided by CONNECT that returns environment variable values:

```
CREATE FUNCTION envar RETURNS STRING soname 'ha_connect.so';
SELECT envar('CLASSPATH');
```

Most of the time, this will return null or some required files are missing. This is why CONNECT introduced a global variable to store this information. The paths specified in this variable are added and have precedence to the ones, if any, of the CLASSPATH environment variable. As for the jvm path, this variable connect\_class\_path should be specified when starting the server but can also be set before using the JDBC table type for the first time.

The current directory (sql/data) is also placed by CONNECT at the beginning of the class path.

As an example, here is how I start MariaDB when doing tests on Linux:

```
olivier@olivier-Aspire-8920:~$ sudo /usr/local/mysql/bin/mysqld -u root --console --default-storage-engine=myisam --skip-innodb --connect_jvm_path="/usr/lib/jvm/java-8-oracle/jre/lib/i386/server" --connect_class_path="/home/olivier/mariadb/10.1/storage/connect:/media/olivier/SOURCE/mysql-connector-java-6.0.2/mysql-connector-java-6.0.2-bin.jar"
```

## CONNECT JDBC Tables

These tables are given the type JDBC. For instance, supposing you want to access the boys table located on and external local or remote database management system providing a JDBC connector:

```
CREATE TABLE boys (
name CHAR(12),
city CHAR(12),
birth DATE,
hired DATE);
```

To access this table via JDBC you can create a table such as:

```
CREATE TABLE jboys ENGINE=CONNECT table_type=JDBC tabname=boys
CONNECTION='jdbc:mysql://localhost/dbname?user=root';
```

The CONNECTION option is the URL used to establish the connection with the remote server. Its syntax depends on the external DBMS and in this example is the one used to connect as root to a MySQL or MariaDB local database using the MySQL JDBC connector.

As for ODBC, the columns definition can be omitted and are retrieved by the discovery process. The restrictions concerning column definitions are the same as for ODBC.

Note: The dbname indicated in the URL corresponds for many DBMS to the catalog information. For MySQL and MariaDB it is the schema (often called database) of the connection.

### Using a Federated Server

Alternatively, a JDBC table can specify its connection options via a Federated server. For instance, supposing you have a table accessing an external Postgresql table defined as:

```
CREATE TABLE juuid ENGINE=CONNECT table_type=JDBC tabname=testuuid
CONNECTION='jdbc:postgresql:test?user=postgres&password=pwd';
```

You can create a Federated server:

```
CREATE server 'post1' FOREIGN DATA wrapper 'postgresql' OPTIONS (
HOST 'localhost',
DATABASE 'test',
USER 'postgres',
PASSWORD 'pwd',
PORT 0,
SOCKET '',
OWNER 'postgres');
```

Now the JDBC table can be created by:

```
CREATE TABLE juuid ENGINE=CONNECT table_type=JDBC CONNECTION='post1' tabname=testuuid;
```

or by:

```
CREATE TABLE juuid ENGINE=CONNECT table_type=JDBC CONNECTION='post1/testuuid';
```

In any case, the location of the remote table can be changed in the Federated server without having to alter all the tables using this server.

JDBC needs a URL to establish a connection. CONNECT was able to construct that URL from the information contained in such Federated server definition when the URL syntax is similar to the one of MySQL, MariaDB or Postgresql. However, other DBMSs such as Oracle use a different URL syntax. In this case, simply replace the HOST information by the required URL in the Federated server definition. For instance:

```
CREATE server 'oracle' FOREIGN DATA wrapper 'oracle' OPTIONS (
HOST 'jdbc:oracle:thin:@localhost:1521:xe',
DATABASE 'SYSTEM',
USER 'system',
PASSWORD 'manager',
PORT 0,
SOCKET '',
OWNER 'SYSTEM');
```

Now you can create an Oracle table with something like this:

```
CREATE TABLE empor ENGINE=CONNECT table_type=JDBC CONNECTION='oracle/HR.EMPLOYEES';
```

Note: Oracle, as Postgresql, does not seem to understand the DATABASE setting as the table schema that must be specified in the Create Table statement.

## Connecting to a JDBC driver

When the connection to the driver is established by the JdbcInterface wrapper class, it uses the options that are provided when creating the CONNECT JDBC tables. Inside the default Java wrapper, the driver’s main class is loaded by the DriverManager.getConnection function that takes three arguments:

| URL      | User                                                         | Password |
| -------- | ------------------------------------------------------------ | -------- |
| URL      | That is the URL that you specified in the CONNECTION option. |          |
| User     | As specified in the OPTION\_LIST or NULL if not specified.   |          |
| Password | As specified in the OPTION\_LIST or NULL if not specified.   |          |

The URL varies depending on the connected DBMS. Refer to the documentation of the specific JDBC driver for a description of the syntax to use. User and password can also be specified in the option list.

Beware that the database name in the URL can be interpreted differently depending on the DBMS. For MySQL this is the schema in which the tables are found. However, for Postgresql, this is the catalog and the schema must be specified using the CONNECT dbname option.

For instance a table accessing a Postgresql table via JDBC can be created with a create statement such as:

```
CREATE TABLE jt1 ENGINE=CONNECT table_type=JDBC
CONNECTION='jdbc:postgresql://localhost/mtr' dbname=PUBLIC tabname=t1
option_list='User=mtr,Password=mtr';
```

Note: In previous versions of JDBC, to obtain a connection, java first had to initialize the JDBC driver by calling the method Class.forName. In this case, see the documentation of your DBMS driver to obtain the name of the class that implements the interface java.sql.Driver. This name can be specified as an option DRIVER to be put in the option list. However, most modern JDBC drivers since version 4 are self-loading and do not require this option to be specified.

The wrapper class also creates some required items and, in particular, a statement class. Some characteristics of this statement will depend on the options specified when creating the table:

| Scrollable  | Block\_size                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------- |
| Scrollable  | To be specified in the option list. Determines the cursor type: no= forward\_only or yes=scroll\_insensitive. |
| Block\_size | Will be used to set the statement fetch size.                                                                 |

### Fetch Size

The fetch size determines the number of rows that are internally retrieved by the driver on each interaction with the DBMS. Its default value depends on the JDBC driver. It is equal to 10 for some drivers but not for the MySQL or MariaDB connectors.

The MySQL/MariaDB connectors retrieve all the rows returned by one query and keep them in a memory cache. This is generally fine in most cases, but not when retrieving a large result set that can make the query fail with a memory exhausted exception.

To avoid this, when accessing a big table and expecting large result sets, you should specify the BLOCK\_SIZE option to 1 (the only acceptable value). However a problem remains:

Suppose you execute a query such as:

```
SELECT id, name, phone FROM jbig LIMIT 10;
```

Not knowing the limit clause, CONNECT sends to the remote DBMS the query:

```
SELECT id, name, phone FROM big;
```

In this query big can be a huge table having million rows. Having correctly specified the block size as 1 when creating the table, the wrapper just reads the 10 first rows and stops. However, when closing the statement, these MySQL/MariaDB drivers must still retrieve all the rows returned by the query. This is why, the wrapper class when closing the statement also cancels the query to stop that extra reading.

The bad news is that if it works all right for some previous versions of the MySQL driver, it does not work for new versions as well as for the MariaDB driver that apparently ignores the cancel command. The good news is that you can use an old MySQL driver to access MariaDB databases. It is also possible that this bug are fixed in future versions of the drivers.

### Connection to a Data Source

This is the java preferred way to establish a connection because a data source can keep a pool of connections that can be re-used when necessary. This makes establishing connections much faster once it was done for the first time.

CONNECT provide additional wrappers whose files are located in the CONNECT source directory. The wrapper to use can be specified in the global variable connect\_java\_wrapper, which defaults to “JdbcInterface”.

It can also be specified for a table in the option list by setting the option wrapper to its name. For instance:

```
CREATE TABLE jboys 
ENGINE=CONNECT table_type=JDBC tabname='boys'
CONNECTION='jdbc:mariadb://localhost/connect?user=root&useSSL=false'
option_list='Wrapper=MariadbInterface,Scrollable=1';
```

They can be used instead of the standard JdbcInterface and are using created data sources.

The Apache one uses data sources implemented by the Apache-commons-dbcp2 package and can be used with all drivers including those not implementing data sources. However, the Apache package must be installed and its three required jar files accessible via the class path.

1. commons-dbcp2-2.1.1.jar
2. commons-pool2-2.4.2.jar
3. commons-logging-1.2.jar

Note: the versions numbers can be different on your installation.

The other ones use data sources provided by the matching JDBC driver. There are currently four wrappers to be used with mysql-6.0.2, mariadb, oracle and postgresql.

Unlike the class path, the used wrapper can be changed even after the JVM machine was created.

## Random Access to JDBC Tables

The same methods described for ODBC tables can be used with JDBC tables.

Note that in the case of the MySQL or MariaDB connectors, because they internally read the whole result set in memory, using the MEMORY option would be a waste of memory. It is much better to specify the use of a scrollable cursor when needed.

## Other Operations with JDBC Tables

Except for the way the connection string is specified and the table type set to JDBC, all operations with ODBC tables are done for JDBC tables the same way. Refer to the ODBC chapter to know about:

* Accessing specified views (SRCDEF)
* Data modifying operations.
* Sending commands to a data source.
* JDBC catalog information.

Note: Some JDBC drivers fail when the global time\_zone variable is ambiguous, which sometimes happens when it is set to SYSTEM. If so, reset it to a not ambiguous value, for instance:

```
set global time_zone = '+2:00';
```

## JDBC Specific Restrictions

Connecting via data sources created externally (for instance using Tomcat) is not supported yet.

Other restrictions are the same as for the ODBC table type.

## Handling the UUID Data Type

PostgreSQL has a native UUID data type, internally stored as BIN(16). This is neither an SQL nor a MariaDB data type. The best we can do is to handle it by its character representation.

UUID are translated to CHAR(36) when column definitions are set using discovery. Locally a PostgreSQL UUID column are handled like a CHAR or VARCHAR column. Example:

Using the PostgreSQL table testuuid in the text database:

```
Table « public.testuuid »
 Column | Type | Default
--------+------+--------------------
 id     | uuid | uuid_generate_v4()
 msg    | text |
```

Its column definitions can be queried by:

```
CREATE OR REPLACE TABLE juuidcol ENGINE=CONNECT table_type=JDBC tabname=testuuid catfunc=columns
CONNECTION='jdbc:postgresql:test?user=postgres&password=pwd';
```

```
SELECT TABLE_NAME "Table", COLUMN_NAME "Column", data_type "Type", 
  type_name "Name", column_size "Size" 
 FROM juuidcol;
```

This query returns:

| Table    | Column | Type | Name | Size       |
| -------- | ------ | ---- | ---- | ---------- |
| testuuid | id     | 1111 | uuid | 2147483647 |
| testuuid | msg    | 12   | text | 2147483647 |

Note: PostgreSQL, when a column size is undefined, returns 2147483647, which is not acceptable for MariaDB. CONNECT change it to the value of the connect\_conv\_size session variable. Also, for TEXT columns the data type returned is 12 (SQL\_VARCHAR) instead of -1 the SQL\_TEXT value.

Accessing this table via JDBC by:

```
CREATE TABLE juuid ENGINE=CONNECT TABLE_TYPE=JDBC TABNAME=testuuid
CONNECTION='jdbc:postgresql:test?user=postgres&password=pwd';
```

it are created by discovery as:

```
CREATE TABLE `juuid` (
  `id` CHAR(36) DEFAULT NULL,
  `msg` VARCHAR(8192) DEFAULT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 CONNECTION='jdbc:postgresql:test?user=postgres&password=pwd' `TABLE_TYPE`='JDBC' `TABNAME`='testuuid';
```

Note: 8192 being here the _connect\_conv\_size_ value.

Let's populate it:

```
INSERT INTO juuid(msg) VALUES('First');
INSERT INTO juuid(msg) VALUES('Second');
SELECT * FROM juuid;
```

Result:

| id                                   | msg    |
| ------------------------------------ | ------ |
| 4b173ee1-1488-4355-a7ed-62ba59c2b3e7 | First  |
| 6859f850-94a7-4903-8d3c-fc3c874fc274 | Second |

Here the id column values come from the DEFAULT of the PostgreSQL column that was specified as uuid\_generate\_v4().

It can be set from MariaDB. For instance:

```
INSERT INTO juuid
  VALUES('2f835fb8-73b0-42f3-a1d3-8a532b38feca','inserted');
INSERT INTO juuid VALUES(NULL,'null');
INSERT INTO juuid VALUES('','random');
SELECT * FROM juuid;
```

Result:

| id                                   | msg      |
| ------------------------------------ | -------- |
| 4b173ee1-1488-4355-a7ed-62ba59c2b3e7 | First    |
| 6859f850-94a7-4903-8d3c-fc3c874fc274 | Second   |
| 2f835fb8-73b0-42f3-a1d3-8a532b38feca | inserted |
|                                      | null     |
| 8fc0a30e-dc66-4b95-ba57-497a161f4180 | random   |

The first insert specifies a valid UUID character representation. The second one set it to NULL. The third one (a void string) generates a Java random UUID. UPDATE commands obey the same specification.

These commands both work:

```
SELECT * FROM juuid WHERE id = '2f835fb8-73b0-42f3-a1d3-8a532b38feca';
DELETE FROM juuid WHERE id = '2f835fb8-73b0-42f3-a1d3-8a532b38feca';
```

However, this one fails:

```
SELECT * FROM juuid WHERE id like '%42f3%';
```

Returning:

1296: Got error 174 'ExecuteQuery: org.postgresql.util.PSQLException:\
ERROR: operator does not exist: uuid \~ unknown\
hint: no operator corresponds to the data name and to the argument types.

because CONNECT cond\_push feature added the WHERE clause to the query sent to PostgreSQL:

```
SELECT id, msg FROM testuuid WHERE id LIKE '%42f3%'
```

and the LIKE operator does not apply to UUID in PostgreSQL.

To handle this, a new session variable was added to CONNECT: connect\_cond\_push. It permits to specify if cond\_push is enabled or not for CONNECT and defaults to 1 (enabled). In this case, you can execute:

```
set connect_cond_push=0;
```

Doing so, the where clause are executed by MariaDB only and the query will not fail anymore.

## Executing the JDBC tests

Four tests exist but they are disabled because requiring some work to localized them according to the operating system and available java package and JDBC drivers and DBMS.

Two of them, jdbc.test and jdbc\_new.test, are accessing MariaDB via JDBC drivers that are contained in a fat jar file that is part of the test. They should be executable without anything to do on Windows; simply adding the option –enable-disabled when running the tests.

However, on Linux these tests can fail to locate the JVM library. Before executing them, you should export the JAVA\_HOME environment variable set to the prefix of the java installation or export the LD\_LIBRARY\_PATH containing the path to the JVM lib.

## Fixing Problem With mariadb-dump

In some case or some platform, when CONNECT is set up for use with JDBC table types, this causes [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) with the option --all-databases to fail.

This was reported by Robert Dyas who found the cause - see the discussion at [MDEV-11238](https://jira.mariadb.org/browse/MDEV-11238).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
