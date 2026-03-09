---
description: >-
  An architectural overview for SQL Server DBAs, covering MariaDB's storage
  engines (InnoDB), transaction logs (undo/redo), buffer pool, and system
  databases.
---

# Understanding MariaDB Architecture

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

MariaDB architecture is partly different from the architecture of traditional DBMSs, like SQL Server. Here we will examine the main components that a new MariaDB DBA needs to know. We will also discuss a bit of history, because this may help understand MariaDB philosophy and certain design choices.

This section is an overview of the most important components. More information is included in specific sections of this migration guide, or in other pages of the MariaDB documentation (see the links scattered over the text).

## Storage Engines

MariaDB was born from the source code of MySQL, in 2008. Therefore, its history begins with MySQL.

MySQL was born at the beginning of the 90s. Back in the days, if compared to its existing competitors, MySQL was lightweight, simple to install, easy to learn. While it had a very limited set of features, it was also fast in certain common operations. And it was open source. These characteristics made it suitable to back the simple websites that existed at that time.

The web evolved rapidly, and the same happened to MySQL. Being open source helped a lot in this respect, because the community needed functionalities that weren’t supported at that time.

MySQL was probably the first database system to support a [pluggable storage engine architecture](../../../../server-usage/storage-engines/). Basically, this means that MySQL knows very little about creating or populating a table, reading from it, building proper indexes and caches. It just delegated all these operations to a special plugin type called a storage engine.

One of the first plugins developed by third parties was [InnoDB](understanding-mariadb-architecture.md#innodb). It is very fast, and it adds two important features that are not otherwise supported: transactions and [foreign keys](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md).

Note that when MariaDB asks a storage engine to write or read a row, the storage engine could theoretically do anything. This led to the creation of very interesting alternative engines, like [BLACKHOLE](../../../../server-usage/storage-engines/blackhole.md) (which doesn’t write or read any data, acting like the /dev/null file in Linux), or [CONNECT](../../../../server-usage/storage-engines/connect/) (which can read and write to files written in many different formats, or remote DBMSs, or some other special data sources).

Nowadays InnoDB is the default MariaDB storage engine, and it is the best choice for most use cases. But for particular needs, sometimes using a different storage engine is desirable. In case of doubts about the best storage engine to use for a specific case, check the [Choosing the Right Storage Engine](../../../../server-usage/storage-engines/choosing-the-right-storage-engine.md) page.

When we create a table, we specify its storage engine or use the default one. It is possible to convert an existing table to another storage engine, though this is a blocking operation which requires a complete table copy. Third-party storage engines can also be installed while MariaDB is running.

Note that it is perfectly possible to use tables with different storage engines in the same transaction (even if some engines are not transactional). It is even possible to use different engines in the same query, for example with JOINs and subqueries.

The default storage engine can be changed by changing the [default\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) variable. A different default can be specified for temporary tables by setting [default\_tmp\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_tmp_storage_engine). MariaDB uses [Aria](../../../../server-usage/storage-engines/aria/aria-storage-engine.md) for system tables and temporary tables created internally to store the intermediate results of a query.

### InnoDB

It is worth spending some more words here about [InnoDB](../../../../server-usage/storage-engines/innodb/), the default storage engine.

#### Primary Key and Indexes

InnoDB primary keys are always the equivalent of SQL Server clustered indexes. In other words, an InnoDB table is always ordered by the primary key.

If an InnoDB table doesn't have a user-defined primary key, the first `UNIQUE` index whose columns are all `NOT NULL` is used as a primary key. If there is no such index, the table will have a _clustered index_. The terminology here can be a bit confusing for SQL Server and other DBMS users. A clustered index in InnoDB is a 6 bytes value that is added to the table. This index and its values are completely invisible to the users. It's important to note that clustered indexes are governed by a global mutex that greatly reduces their scalability.

Secondary indexes are ordered by the columns that are part of the index, and contain a reference to each entry's corresponding primary key value.

Some consequences of these design choices are the following:

* For performance reasons, a primary key value should be inserted in order. In other words, the last inserted value should be the highest. This order is normally followed when inserting values into an `AUTO_INCREMENT` primary key. The reason is that inserting values in the middle of an ordered data structure is slower, unless they fit into existing holes. If we insert primary key values randomly, InnoDB often has to rearrange pages to make some room for the new data.
* A big primary keys means that all secondary indexes are also big.
* A query by primary key will require a single search. A query on a secondary index that also reads columns not contained in the index will require one search on the index, plus one more search for each row that satisfies the index condition.
* We shouldn't explicitly include the primary key in a secondary index. If we do so, the primary key column will be duplicated in the index.

#### Tablespaces

For InnoDB, a _tablespace_ is a file containing data (not a file group as in SQL Server). The types of tablespaces are:

* [System tablespace](../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md).
* [File-per-table tablespaces](../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md).
* [Temporary tablespaces](../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces.md).

The system tablespace is stored in the file `ibdata`. It contains information used by InnoDB internally, like rollback segments, as well as some system tables. Historically, the system tablespace also contained all tables created by the user. In modern MariaDB versions, a table is created in the system tablespace only if the [innodb\_file\_per\_table](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) system variable is set to 0 at the moment of the table creation. By default, innodb\_file\_per\_table is 1.

Tables created while `innodb_file_per_table=1` are written into their own tablespace. These are `.ibd` files.

Starting from [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), temporary tables are written into temporary tablespaces, which means `ibtmp*` files. Previously, they were created in the system tablespace or in file-per-table tablespaces according to the value of `innodb_file_per_table`, just like regular tables. Temporary tablespaces, if present, are deleted when MariaDB starts.

**It is important to remember that tablespaces can never shrink**. If a file-per-table tablespace grows too much, deleting data won't recover space. Instead, a new table must be created and data needs to be copied. Finally, the old table will be deleted. If the system tablespace grows too much, the only solution is to move data into a new MariaDB installation.

#### Transaction Logs

In SQL Server, the transaction log contains both the undo log and the redo log. Usually we have only one transaction log.

In MariaDB the undo log and the redo log are stored separately. By default, the [redo log](../../../../server-usage/storage-engines/innodb/innodb-redo-log.md) is written to two files, called `ib_logfile0` and `ib_logfile1`. The [undo log](../../../../server-usage/storage-engines/innodb/innodb-undo-log.md) by default is written to the _system tablespace_, which is in the `ibdata1` file. However, it is possible to write it in separate files in a specified directory.

MariaDB provides no way to inspect the contents of the transaction logs. However, it is possible to inspect the [binary log](understanding-mariadb-architecture.md#the-binary-log).

InnoDB transaction logs are written in a circular fashion: their size is normally fixed, and when the end is reached, InnoDB continues to write from the beginning. However, if very long transactions are running, InnoDB cannot overwrite the oldest data, so it has to expand the log size instead.

#### InnoDB Buffer Pool

MariaDB doesn't have a central buffer pool. Each storage engine may or may not have a buffer pool. The [InnoDB buffer pool](../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) is typically assigned a big amount of memory. See [MariaDB Memory Allocation](../../../../ha-and-performance/mariadb-memory-allocation.md).

MariaDB has no extension like the SQL Server buffer pool extension.

A part of the buffer pool is called the [change buffer](../../../../server-usage/storage-engines/innodb/innodb-change-buffering.md). It contains dirty pages that have been modified in memory and not yet flushed.

#### InnoDB Background Threads

InnoDB has background threads that take care of flushing dirty pages from the change buffer to the tablespaces. They don't directly affect the latency of queries, but they are very important for performance.

[SHOW ENGINE InnoDB STATUS](../../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) shows information about them in the `BACKGROUND THREAD` section. They can also be seen using the [threads](../../../../reference/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md) table, in the [performance\_schema](../../../../reference/system-tables/performance-schema/).

InnoDB flushing is similar to _lazy writes_ and _checkpoints_ in SQL Server. It has no equivalent for _eager writing_.

For more information, see [InnoDB Page Flushing](../../../../server-usage/storage-engines/innodb/innodb-page-flushing.md) and [InnoDB Purge](../../../../server-usage/storage-engines/innodb/innodb-purge.md).

#### Checksums and Doublewrite Buffer

InnoDB pages have checksums. After writing pages to disk, InnoDB verifies that the checksums match. The checksum algorithm is determined by [innodb\_checksum\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm). Check the variable documentation for its consequences on performance, backward compatibility and encryption.

In case of a system crash, hardware failure or power outage, a page could be half-written on disk. For some pages, this causes a disaster. Therefore, InnoDB writes essential pages to disk twice. A backup copy of the new page version is written first. Then, the old page is overwritten. The backup copies are written into a file called the _doublewrite buffer_.

* If an event prevents the first page from being written, the old version of the page will still be available.
* If an event prevents the old page from being completely overwritten by its new version, the page can still be recovered using the doublewrite buffer.

The doublewrite buffer can disabled using the [innodb\_doublewrite](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite) variable, but this usually doesn't bring big performance benefits. The doublewrite buffer location can be changed with [innodb\_doublewrite\_file](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite_file).

### Aria

Even if we only create InnoDB tables, we use Aria indirectly, in two ways:

* For system tables.
* For internal temporary tables.

Aria is a non-transactional storage engine. By default it is crash-safe, meaning that all changes to data are written and fsynced to a write-ahead log and can always be recovered in case of a crash.

Aria caches indexes into the pagecache. Data are not directly cached by Aria, so it's important that the underlying filesystem caches reads and writes.

The pagecache size is determined by the [aria\_pagecache\_buffer\_size](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size) system variable. To know if it is big enough we can check the proportion of free pages (the ratio between [Aria\_pagecache\_blocks\_used](../../../../server-usage/storage-engines/aria/aria-status-variables.md#aria_pagecache_blocks_used) and [Aria\_pagecache\_blocks\_unused](../../../../server-usage/storage-engines/aria/aria-status-variables.md#aria_pagecache_blocks_unused)) and the proportion of cache misses (the ratio between [Aria\_pagecache\_read\_requests](../../../../server-usage/storage-engines/aria/aria-status-variables.md#aria_pagecache_read_requests) and [Aria\_pagecache\_reads](../../../../server-usage/storage-engines/aria/aria-status-variables.md#aria_pagecache_reads).

The proportion of dirty pages is the ratio between [Aria\_pagecache\_blocks\_used](../../../../server-usage/storage-engines/aria/aria-status-variables.md#aria_pagecache_blocks_used) and [Aria\_pagecache\_blocks\_not\_flushed](../../../../server-usage/storage-engines/aria/aria-status-variables.md#aria_pagecache_blocks_not_flushed) tells us if the log file is big enough.

The size of Aria log is determined by [aria\_log\_file\_size](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size).

## Databases

MariaDB does not support the concept of schema. In MariaDB SQL, _schema_ and _schemas_ are synonyms for _database_ and _databases_.

When a user connects to MariaDB, they don't connect to a specific database. Instead, they can access any table they have permissions for. There is however a concept of _default database_, see below.

A database is a container for database objects like tables and views. A database serves the following purposes:

* A database is a namespace.
* A database is a logical container to separate objects.
* A database has a default [character set](../../../../reference/data-types/string-data-types/character-sets/) and collation, which are inherited by their tables.
* Permissions can be assigned on a whole database, to make permission maintenance simpler.
* Physical data files are stored in a directory which has the same name as the database to which they belong.

### System Databases

MariaDB has the following system databases:

* [mysql](../../../../reference/system-tables/the-mysql-database-tables/) is for internal use only, and should not be read or written directly.
* [information\_schema](../../../../reference/system-tables/information-schema/) contains all information that can be found in SQL Server's information\_schema and more. However, while SQL Server's `information_schema` is a schema containing information about the local database, MariaDB's `information_schema` is a database that contains information about all databases.
* [performance\_schema](../../../../reference/system-tables/performance-schema/) contains information about MariaDB runtime. It is disabled by default. Enabling it requires setting the [performance\_schema](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema) system variable to 1 and restarting MariaDB.

### Default Database

When a user connects to MariaDB, they can optionally specify a default database. A default database can also be specified or changed later, with the [USE](../../../../reference/sql-statements/administrative-sql-statements/use-database.md) command.

Having a default database specified allows one to specify tables without specifying the name of the database where they are located. If no default database is specified, all table names must be fully qualified.

For example, the two following snippets are equivalent:

```
SELECT * FROM my_database.my_table;

-- is equivalent to:
USE my_database;
SELECT * FROM my_table;
```

Even if a default database is specified, tables from other databases can be accessed by specifying their fully qualified names:

```
-- this query joins my_database.my_table to your_database.your_table
USE my_database;
SELECT m.*
    FROM my_table m
    JOIN your_database.your_table y
        ON m.xyz = y.xyz;
```

MariaDB has the [DATABASE()](../../../../reference/sql-functions/secondary-functions/information-functions/database.md) function to determine the current database:

```
SELECT DATABASE();
```

Stored procedures and triggers don't inherit a default database from the session, nor by a caller procedure. In that context, the default database is the database which contains the procedure. `USE` can be used to change it. The default database will only be valid for the rest of the procedure.

## The Binary Log

Different tables can be built using different storage engines. It is important to note that not all engines are transactional, and that different engines implement the transaction logs in different ways. For this reason, MariaDB cannot replicate data from a primary to a replica using an equivalent of SQL Server transactional replication.

Instead, it needs a global mechanism to log the changes that are applied to data. This mechanism is the [binary log](../../../server-monitoring-logs/binary-log/), often abbreviated to binlog.

The binary log can be written in the following formats:

* STATEMENT logs SQL statements that modify data;
* ROW logs a reference to the rows that have been modified, if any (usually it’s the primary key), and the new values that have been added or modified, in a binary format.
* MIXED is a combination of the above formats. It means that ROW is used for statements that can safely be logged in this way (see below), and STATEMENT is used in other cases. This is the default format from [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102).

In most cases, STATEMENT is slower because the SQL statement needs to be re-executed by the replica, and because certain statements may produce a different result in the replica (think about queries that use LIMIT without ORDER BY, or the CURRENT\_TIMESTAMP() function). But there are exceptions, and besides, DDL statements are always logged as STATEMENT to avoid flooding the binary log. Therefore, the binary log may well contain both ROW and STATEMENT entries.

See [Binary Log Formats](../../../server-monitoring-logs/binary-log/binary-log-formats.md).

The binary log allows:

* replication, if enabled on the primary;
* promoting a replica to a primary, if enabled on that replica;
* incremental backups;
* seeing data as they were in a point of time in the past ([flashback](../../../server-monitoring-logs/binary-log/flashback.md));
* restoring a backup and re-appling the binary log, with the exception of a data change which caused problems (human mistake, application bug, SQL injection);
* Capture Data Changes (CDC), by streaming the binary log to technologies like Apache Kafka.

If you don't plan to use any of these features on a server, it is possible to [disable](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin) the binary log to slightly improve the performance.

The binary log can be inspected using the [mariadb-binlog](../../../../clients-and-utilities/logging-tools/mariadb-binlog/) utility, which comes with MariaDB. Enabling or disabling the binary log requires restarting MariaDB.

See also [MariaDB Replication Overview for SQL Server Users](mariadb-replication-overview-for-sql-server-users.md) and [MariaDB Backups Overview for SQL Server Users](mariadb-backups-overview-for-sql-server-users.md) for a better understanding of how the binary log is used.

## Plugins

Storage engines are a special type of [plugin](../../../../reference/plugins/). But others exist. For example, plugins can add authentication methods, new features, SQL syntax, functions, informative tables, and more.

A plugin may add some server variables and some status variables. Server variables can be used to configure the plugin, and status variables can be used to monitor its activities and status. These variables generally use the plugin's name as a prefix. For example InnoDB has a server variable called innodb\_buffer\_pool\_size to configure the size of its buffer pool, and a status variable called Innodb\_pages\_read which indicates the number of memory pages read from the buffer pool. The category [system variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/) of the MariaDB documentation has specific pages for system and status variables associated with various plugins.

Many plugins are installed by default, or available but not installed by default. They can be installed or uninstalled at runtime with SQL statements, like `INSTALL PLUGIN`, `UNINSTALL PLUGIN` and others; see [Plugin SQL Statements](../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/). 3rd party plugins can be made available for installation by simply copying them to the [plugin\_dir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir).

It is important to note that different plugins may have different maturity levels. It is possible to prevent the installation of plugins we don’t consider production-ready by setting the [plugin\_maturity](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity) system variable. For plugins that are distributed with MariaDB, the maturity level is determined by the MariaDB team based on the bugs reported and fixed.

Some plugins are developed by 3rd parties. Even some 3rd party plugins are included in MariaDB official distributions - the ones available on mariadb.org.

In MariaDB every authorization method (including the default one) is provided by an [authentication plugin](../../../../reference/plugins/authentication-plugins/). A user can be required to use a certain authentication plugin. This gives us much flexibility and control. Windows users may be interested in [gsapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) (which supports Windows authentication, Kerberos and NTLM) and [named\_pipe](../../../../reference/plugins/authentication-plugins/authentication-plugin-named-pipe.md) (which uses named pipe impersonation).

Other plugins that can be very useful include [userstat](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md), which includes statistics about resources and table usage, and [METADATA\_LOCK\_INFO](../../../../reference/plugins/other-plugins/metadata-lock-info-plugin.md), which provides information about metadata locks.

## Thread Pool

MariaDB supports [thread pool](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/). It works differently on UNIX and on Windows. On Windows, it is enabled by default and its implementation is quite similar to SQL Server. It uses the Windows native CreateThreadpool API.

If we don't use the thread pool, MariaDB will use its traditional method to handle connections. It consists of using a dedicated thread for each client connection. Creating a new thread has a cost in terms of CPU time. To mitigate this cost, after a client disconnects, the thread may be preserved for a certain time in the [thread cache](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size).

Whichever connection method we use, MariaDB has a maximum number of simultaneous connections, which can be changed at runtime. When the limit is reached, if more clients try to connect they will receive an error. This prevents MariaDB from consuming all the server resources and freezing or crashing. See [Handling Too Many Connections](../../../../ha-and-performance/optimization-and-tuning/system-variables/handling-too-many-connections.md).

## Configuration

MariaDB has many settings that\
control the server behavior. These can be set up when starting mysqld ([mysqld options](../../../starting-and-stopping-mariadb/mariadbd-options.md)), and the vast majority are also accessible as [server system variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md). These can be classified in these ways:

* Dynamic or static;
* Global, session, or both.

Note that server system variables are not to be confused with [user-defined variables](../../../../reference/sql-structure/sql-language-structure/user-defined-variables.md). The latter are not used for MariaDB configuration.

### Configuration Files

MariaDB can use several [configuration files](../../configuring-mariadb/configuring-mariadb-with-option-files.md). Configuration files are searched in several locations, including in the user directory, and if present they all are read and used. They are read in a consistent order. These locations depend on the operating system; see [Default Option File Locations](../../configuring-mariadb/configuring-mariadb-with-option-files.md#default-option-file-locations). It is possible to tell MariaDB which files it should read; see [Global Options Related to Option Files](../../configuring-mariadb/configuring-mariadb-with-option-files.md#global-options-related-to-option-files).

On Linux, by default the configuration files are called `my.cnf`. On Windows, by default the configuration files can be called `my.ini` or `my.cnf`. The former is more common.

If a variable is mentioned multiple times in different files, the occurrence that is read last will overwrite the others. Similarly, if a variable is mentioned several times in a single file, the occurrence that is read last overwrites the others.

The contents of each configuration file are organized by _option groups_. MariaDB Server and client programs read different groups. The read groups also depend on the MariaDB version. See [Option Groups](../../configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) for the details. Most commonly, the `[server]` or `[mysqld]` groups are used to contain all server configuration. The `[client-server]` group can be used for options that are shared by the server and the clients (like the port to use), to avoid repeating those variables multiple times.

### Dynamic and Static Variables

Dynamic variables have a value that can be changed at runtime, using the [SET](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) SQL statement. Static variables have a value that is decided at startup (see below) and cannot be changed without a restart.

The [Server System Variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) page states if variables are dynamic or static.

### Scope

A global system variable is one that affects the general behavior of MariaDB. For example [innodb\_buffer\_pool\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) determines the size of the InnoDB buffer pool, which is used by read and write operations, no matter which user issued them. A session system variable is one that affects MariaDB behavior for the current connection; changing it will not affect other connected users, or future connections from the current user.

A variable could exist in both the global and session scopes. In this case, the session value is what affects the current connection. When a user connects, the current global value is copied to the session scope. Changing the global value afterward will not change existing connections.

The [Server System Variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) page states the scope of each variable.

Global variables and some session variables can only be modified by a user with the [SUPER](../../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege (typically root).

### Syntax

To see the value of a system variable:

```
-- global variables:
SELECT @@global.variable_name;
-- session variables:
SELECT @@session.variable_name;
-- or just use the shortcut:
SELECT @@variable_name;
```

A longer syntax, which is mostly useful to get multiple variables, makes use of the same pattern syntax that is used by the [LIKE](../../../../reference/sql-functions/string-functions/like.md) operator:

```
-- global variables whose name starts with 'innodb':
SHOW GLOBAL VARIABLES LIKE 'innodb%';
-- session variables whose name starts with 'innodb':
SHOW SESSION VARIABLES LIKE 'innodb%';
SHOW VARIABLES LIKE 'innodb%';
```

To modify the global or session value of a dynamic variable:

```
SET @@global.variable_name = 'new 'value';
SET @@session.variable_name = 'new 'value';
```

Notice that if we modify a global variable in this way, the new value will be lost at server restart. For this reason we probably want to change the value in the configuration file too.

For further information see:

* The [SET](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.
* The [SHOW VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement.

### Setting System Variables with Startup Parameters

System variables can be set at server startup without writing their values into a configuration file. This is useful if we want a value to be set once, until we change it or restart MariaDB. Values passed in this way override values written in the configuration files.

The general rule is that every global variable can be passed as an argument of `mysqld` by prefixing its name with `--` and by replacing every occurrence of `_` with `-` in its name.

For example, to pass `bind_address` as a startup argument:

```
mysqld --bind-address=127.0.0.1
```

### Debugging Configuration

Mistyping a variable can prevent MariaDB from starting. We cannot set a variable that doesn't exist in the MariaDB version in use. In these cases, an error is written in the [error log](../../../server-monitoring-logs/error-log.md).

Having several configuration files and configuration groups, as well as being able to pass variables as command-line arguments, brings a lot of flexibility but can sometimes be confusing. When we are unsure about which values will be used, we can run:

```
mysqld --print-defaults
```

## Status Variables

MariaDB status variables and some system tables allow external tools to monitor a server, building graphs on how they change over time, and allow the user to inspect what is happening inside the server.

[Status variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) cannot be directly modified by the user. Their values indicate how MariaDB is operating. Their scope can be:

* Global, meaning that the value is about some MariaDB activity.
* Session, meaning that the value measures activities taking place in the current session.

Many status variables exist in both scopes. For example,[Cpu\_time](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#cpu_time) at global level indicates how much time the CPU was used by the MariaDB process (including all user sessions and all the background threads). At session level, it indicates how much time the CPU was used by the current session.

The status variables created by a plugin, usually, use the plugin name as a prefix.

The [SHOW STATUS](../../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) statement prints the values of the status variables that match a certain pattern.

```
-- Show all InnoDB global status variables
SHOW GLOBAL STATUS LIKE 'innodb%';
-- Show all InnoDB session status variables
SHOW SESSION STATUS LIKE 'innodb%';
SHOW STATUS LIKE 'innodb%';
-- Show global variables that contain the "size" substring:
SHOW GLOBAL STATUS LIKE '%size%';
```

Some status variables values are reset when [FLUSH STATUS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md#flush-status) is executed. A possible use:

```
DELIMITER ||
BEGIN NOT ATOMIC
SET @i = 0;
WHILE @i < 60 DO
    SHOW GLOBAL STATUS LIKE 'Com_select';
    FLUSH STATUS;
    DO SLEEP(1);
    SET @i = @i + 1;
END WHILE;
END ||
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
