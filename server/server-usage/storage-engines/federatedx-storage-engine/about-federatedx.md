# About FederatedX

The FederatedX storage engine is a fork of MySQL's [Federated storage engine](https://dev.mysql.com/doc/refman/5.5/en/federated-storage-engine.html), which is no longer being developed by Oracle. The original purpose of FederatedX was to keep this storage engine's development progressing-- to both add new features as well as fix old bugs.

Since [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), the [CONNECT](../connect/) storage engine also allows access to a remote database via MySQL or ODBC connection (table types: [MYSQL](../connect/connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables.md), [ODBC](../connect/connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md)). However, in the current implementation there are several limitations.

## What is the FederatedX storage engine?

The FederatedX Storage Engine is a storage engine that works with both MariaDB and MySQL. Where other storage engines are built as interfaces to lower-level file-based data stores, FederatedX uses libmysql to talk to the data source, the data source being a remote RDBMS. Currently, since FederatedX only uses libmysql, it can only talk to another MariaDB or MySQL RDBMS. The plan is of course to be able to use other RDBMS systems as a data source. There is an existing project Federated ODBC which was able to use PostgreSQL as a remote data source, and it is this type of functionality which will be brought to FederatedX in subsequent versions.

## History

The history of FederatedX is derived from the History of Federated. Cisco needed a MySQL storage engine that would allow them to consolidate remote tables on some sort of routing device, being able to interact with these remote tables as if they were local to the device, but not actually on the device, since the routing device had only so much storage space. The first prototype of the Federated Storage Engine was developed by JD (need to check on this- Brian Aker can verify) using the HANDLER interface. Brian handed the code to Patrick Galbraith and explained how it needed to work, and with Brian and Monty's tutelage and Patrick had a working Federated Storage Engine with MySQL 5.0. Eventually, Federated was released to the public in a MySQL 5.0 release.

When MySQL 5.1 became the production release of MySQL, Federated had more features and enhancements added to it, namely:

* New Federated SERVER added to the parser. This was something Cisco needed that made it possible to change the connection parameters for numerous Federated tables at once without having to alter or re-create the Federated tables.
* Basic Transactional support-- for supporting remote transactional tables
* Various bugs that needed to be fixed from MySQL 5.0
* Plugin capability

In [MariaDB 10.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-1002-release-notes) FederatedX got support for assisted [table discovery](../storage-engines-storage-engine-development/table-discovery.md).

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```sql
INSTALL SONAME 'ha_federatedx';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) options. This can be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = ha_federatedx
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```sql
UNINSTALL SONAME 'ha_federatedx';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) or the [--plugin-load-add](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## How FederatedX works

Every storage engine has to implement derived standard handler class API methods for a storage engine to work. FederatedX is no different in that regard. The big difference is that FederatedX needs to implement these handler methods in such as to construct SQL statements to run on the remote server and if there is a result set, process that result set into the internal handler format so that the result is returned to the user.

### Internal workings of FederatedX

Normal database files are local and as such: You create a table called\
'users', a file such as 'users.MYD' is created. A handler reads, inserts,\
deletes, updates data in this file. The data is stored in particular format,\
so to read, that data has to be parsed into fields, to write, fields have to\
be stored in this format to write to this data file.

With the FederatedX storage engine, there will be no local files\
for each table's data (such as .MYD). A foreign database will store\
the data that would normally be in this file. This will necessitate\
the use of MySQL client API to read, delete, update, insert this\
data. The data will have to be retrieve via an SQL call\
"`SELECT * FROM users`". Then, to read this data, it will have to be retrieved via `mysql_fetch_row` one row at a time, then converted from the\
column in this select into the format that the handler expects.

The basic functionality of how FederatedX works is:

* The user issues an SQL statement against the local federatedX table. This statement is parsed into an item tree
* FederatedX uses the mysql handler API to implement the various methods required for a storage engine. It has access to the item tree for the SQL statement issued, as well as the Table object and each of its Field members. At
* With this information, FederatedX constructs an SQL statement
* The constructed SQL statement is sent to the Foreign data source through libmysql using the mysql client API
* The foreign database reads the SQL statement and sends the result back through the mysql client API to the origin
* If the original SQL statement has a result set from the foreign data source, the FederatedX storage engine iterates through the result set and converts each row and column to the internal handler format
* If the original SQL statement only returns the number of rows returned (affected\_rows), that number is added to the table stats which results in the user seeing how many rows were affected.

#### FederatedX table creation

The create table will simply create the .frm file, and within the`CREATE TABLE` SQL statement, there SHALL be any of the following :

```
connection=scheme://username:password@hostname:port/database/tablename
connection=scheme://username@hostname/database/tablename
connection=scheme://username:password@hostname/database/tablename
connection=scheme://username:password@hostname/database/tablename
```

Or using the syntax introduced in MySQL versions 5.1 for a Federated server (SQL/MED Spec xxxx)

```
connection="connection_one"
connection="connection_one/table_foo"
```

An example of a connect string specifying all the connection parameters would be:

```
connection=mysql://username:password@hostname:port/database/tablename
```

Or, using a Federated server, first a server is created:

```sql
CREATE server 'server_one' FOREIGN data wrapper 'mysql' options
  (HOST '127.0.0.1',
  DATABASE 'db1',
  USER 'root',
  PASSWORD '',
  PORT 3306,
  SOCKET '',
  OWNER 'root');
```

**MariaDB starting with** [**10.11.12**](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-101112-release-notes/README.md)

You can also use 'mariadb' as a wrapper.

Then the FederatedX table is created specifying the newly created Federated server.\
The following statements creates a federated table, `federated.t1` against the table `db1.t1` on the remote server.

```sql
CREATE TABLE federated.t1 (
  `id` INT(20) NOT NULL,
  `name` VARCHAR(64) NOT NULL DEFAULT ''
  )
ENGINE="FEDERATED" DEFAULT CHARSET=latin1
CONNECTION='server_one';
```

(Note that in MariaDB, the original Federated storage engine is replaced with\
the new FederatedX storage engine. And for backward compatibility, the old\
name "FEDERATED" is used in create table. So in MariaDB, the engine type\
should be given as "FEDERATED" without an extra "X", not "FEDERATEDX").

The equivalent of above, if done specifying all the connection parameters

```sql
CONNECTION="mysql://root@127.0.0.1:3306/db1/t1"
```

You can also change the server to point to a new schema:

```sql
ALTER SERVER 'server_one' options(DATABASE 'db2');
```

All subsequent calls to any FederatedX table using the 'server\_one' will now be against tables in `db2`! Guess what? You no longer have to perform an alter table in order to point one or more FederatedX tables to a new server!

This `connection="connection string"` is necessary\
for the handler to be able to connect to the foreign server, either\
by URL, or by server name.

### Method calls

One way to see how the FederatedX storage engine works is to compile a debug build of MariaDB and turn on a trace log. Using a two column table, with one record, the following SQL statements shown below, can be analyzed for what internal methods they result in being called.

#### SELECT

If the query is for instance "`SELECT * FROM foo`", then the primary methods you would see with debug turned on would be first:

```
ha_federatedx::info
ha_federatedx::scan_time:
ha_federatedx::rnd_init: share->select_query SELECT * FROM foo
ha_federatedx::extra
```

Then for every row of data retrieved from the foreign database in the result set:

```
ha_federatedx::rnd_next
ha_federatedx::convert_row_to_internal_format
ha_federatedx::rnd_next
```

After all the rows of data that were retrieved, you would see:

```
ha_federatedx::rnd_end
ha_federatedx::extra
ha_federatedx::reset
```

#### INSERT

If the query was "`INSERT INTO foo (id, ts) VALUES (2, now());`", the trace would be:

```
ha_federatedx::write_row
ha_federatedx::reset
```

#### UPDATE

If the query was "`UPDATE foo SET ts = now() WHERE id = 1;`", the resultant trace would be:

```
ha_federatedx::index_init
ha_federatedx::index_read
ha_federatedx::index_read_idx
ha_federatedx::rnd_next
ha_federatedx::convert_row_to_internal_format
ha_federatedx::update_row

ha_federatedx::extra
ha_federatedx::extra
ha_federatedx::extra
ha_federatedx::external_lock
ha_federatedx::reset
```

## FederatedX capabilities and limitations

* Tables MUST be created on the foreign server prior to any action on those tables via the handler, first version. IMPORTANT: IF you MUST use the FederatedX storage engine type on the REMOTE end, make sure that the table you connect to IS NOT a table pointing BACK to your ORIGINAL table! You know and have heard the screeching of audio feedback? You know putting two mirrors in front of each other how the reflection continues for eternity? Well, need I say more?!
* There is no way for the handler to know if the foreign database or table has changed. The reason for this is that this database has to work like a data file that would never be written to by anything other than the database. The integrity of the data in the local table could be breached if there was any change to the foreign database.
* Support for SELECT, INSERT, UPDATE, DELETE indexes.
* No ALTER TABLE, DROP TABLE or any other Data Definition Language calls.
* Prepared statements will not be used in the first implementation, it remains to be seen whether the limited subset of the client API for the server supports this.
* This uses SELECT, INSERT, UPDATE, DELETE and not HANDLER for its implementation.
* This will not work with the query cache.
* FederatedX does not support [GEOMETRY](../../../reference/sql-structure/geometry/geometry-types.md) types. Such tables cannot be created explicitly, nor discovered.

## How do you use FederatedX?

To use this handler, it's very simple. You must have two databases running, either both on the same host, or on different hosts.

First, on the foreign database you create a table, for example:

```sql
CREATE TABLE federated.test_table (
  id     INT(20) NOT NULL auto_increment,
  name   VARCHAR(32) NOT NULL DEFAULT '',
  other  INT(20) NOT NULL DEFAULT '0',
  PRIMARY KEY  (id),
  KEY name (name),
  KEY other_key (other))
DEFAULT CHARSET=latin1;
```

Then, on the server that will be connecting to the foreign host (client), you create a federated table without specifying the table structure:

```sql
CREATE TABLE federated_test_table ENGINE=FEDERATED 
  CONNECTION='mysql://root@127.0.0.1:9306/federated/test_table';
```

Notice the "ENGINE" and "CONNECTION" fields? This is where you\
respectively set the engine type, "FEDERATED" and foreign\
host information, this being the database your 'client' database\
will connect to and use as the "data file". Obviously, the foreign\
database is running on port 9306, so you want to start up your other\
database so that it is indeed on port 9306, and your FederatedX\
database on a port other than that. In my setup, I use port 5554\
for FederatedX, and port 5555 for the foreign database.

Alternatively (or if you're using MariaDB before version 10.0.2) you specify the federated table structure explicitly:

```sql
CREATE TABLE federated_test_table (
  id     INT(20) NOT NULL auto_increment,
  name   VARCHAR(32) NOT NULL DEFAULT '',
  other  INT(20) NOT NULL DEFAULT '0',
  PRIMARY KEY  (id),
  KEY name (name),
  KEY other_key (other))
ENGINE=FEDERATED
DEFAULT CHARSET=latin1
CONNECTION='mysql://root@127.0.0.1:9306/federated/test_table';
```

In this case the table structure must match exactly the table on the foreign server.

### How to see the storage engine in action

When developing this handler, I compiled the FederatedX database with debugging:

```
./configure --with-federatedx-storage-engine \
  --prefix=/home/mysql/mysql-build/federatedx/ --with-debug
```

Once compiled, I did a 'make install' (not for the purpose of installing the binary, but to install all the files the binary expects to see in the directory I specified in the build with

```
--prefix=/home/code-dev/maria
```

Then, I started the foreign server:

```bash
/usr/local/mysql/bin/mysqld_safe \
  --user=mysql --log=/tmp/mysqld.5555.log -P 5555
```

Then, I went back to the directory containing the newly compiled mysqld`<builddir>/sql/`, started up gdb:

```
gdb ./mysqld
```

Then, within the (gdb) prompt:

```
(gdb) run --gdb --port=5554 --socket=/tmp/mysqld.5554 --skip-innodb --debug
```

Next, I open several windows for each:

1. Tail the debug trace: tail -f /tmp/mysqld.trace|grep ha\_fed
2. Tail the SQL calls to the foreign database: tail -f /tmp/mysqld.5555.log
3. A window with a client open to the federatedx server on port 5554
4. A window with a client open to the federatedx server on port 5555

I would create a table on the client to the foreign server on port 5555, and then to the FederatedX server on port 5554. At this point, I would run whatever queries I wanted to on the FederatedX server, just always remembering that whatever changes I wanted to make on the table, or if I created new tables, that I would have to do that on the foreign server.

Another thing to look for is 'show variables' to show you that you have\
support for FederatedX handler support:

```sql
SHOW variables LIKE '%federat%'
```

and:

```sql
SHOW storage engines;
```

Both should display the federatedx storage handler.

## How do I create a federated server?

A federated server is a way to have a foreign data source defined-- with all connection parameters-- so that you don't have to specify explicitly the connection parameters in a string.

For instance, if you wanted to connect to a table, `first_db.test_table`, using this definition:

```sql
CREATE TABLE federated_test_table ENGINE=FEDERATED 
  CONNECTION='mysql://patg@192.168.1.123/first_db/test_table';
```

You could instead create this with a server:

```sql
CREATE SERVER 'server_one' FOREIGN data wrapper 'mysql' options
  (HOST '192.168.1.123',		
  DATABASE 'first_db',		
  USER 'patg',
  PASSWORD '',
  PORT 3306,
  SOCKET '',		
  OWNER 'root');
```

You could now specify the server instead of the full URL in the connection string:

```sql
CREATE TABLE federated_test_table ENGINE=FEDERATED 
  CONNECTION='server_one/test_table';
```

On the server where you create this `federated_test_table` you will now have access to the table `test_table` in the `first_db` database on the remote server found on 192.168.1.123.

## How does FederatedX differ from the old Federated Engine?

FederatedX from a user point of view is the same for the most part. What is different with FederatedX and Federated is the following:

* Rewrite of the main Federated source code from one single ha\_federated.cc file into three main abstracted components:
  * ha\_federatedx.cc - Core implementation of FederatedX
  * federated\_io.cc - Parent connection class to be over-ridden by derived classes for each RDBMS/client lib
  * federatated\_io\_.cc - derived federated\_io class for a given RDBMS
  * federated\_txn.cc - New support for using transactional engines on the foreign server using a connection poll
* Various bugs fixed (need to look at opened bugs for Federated)

## Where can I get FederatedX

FederatedX is part of [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1) and later. MariaDB merged with the latest FederatedX when there is a need to get a bug fixed. You can get the latest code/follow/participate in the project from the [FederatedX home page](https://launchpad.net/federatedx).

### What are the plans for FederatedX?

* Support for other RDBMS vendors using ODBC
* Support for pushdown conditions
* Ability to limit result set sizes

### See Also

* [CREATE SERVER](../../../reference/sql-statements/data-definition/create/create-server.md)
* [ALTER SERVER](../../../reference/sql-statements/data-definition/alter/alter-server.md)
* [DROP SERVER](../../../reference/sql-statements/data-definition/drop/drop-server.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
