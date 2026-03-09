---
description: >-
  Learn how to export SQL DDL to MariaDB from database management systems like
  Oracle Database, Microsoft SQL Server, MySQL, and IBM DB2.
---

# DDL Export

This page covers DDL[^1] export instructions for several database management systems:

* [Oracle Database](ddl-export.md#oracle-database)
* [Microsoft SQL Server](ddl-export.md#microsoft-sql-server)
* [MySQL](ddl-export.md#mysql)
* [IBM DB2](ddl-export.md#ibm-db2)



## Oracle Database

There are two basic ways of getting a schema from Oracle, with different features and advantages. The instructions here are based on **Oracle 11.2**. In old versions of Oracle, there was no `SCHEMAS` parameter; instead, only a single schema to export was specified with an `OWNER` parameter.

### **Using Oracle Data Pump**

[Oracle Data Pump](https://docs.oracle.com/en/database/oracle/oracle-database/21/sutil/oracle-data-pump.html) is a tool used for backing up and restoring Oracle contents. The Data Pump commands (`expdp` and `impdp`) are just frontends that instruct the backend to do the actual dump and restore, which means that the output and input is not necessarily in the current directory. There is a default Data Pump destination directory, though.

{% hint style="info" %}
Be aware that, in order to get the schema, you cannot just export it. Rather than that, you export what you are looking for, and then use `impdp` to extract an SQL file with the contents that you have dumped.
{% endhint %}

What this means is that if you are working from a backup, or a dump as it is called in Oracle, created by `expdp`, this method of extracting a schema is useful. There is not a lot of flexibility though.

Here is an example for extracting a schema called _APP_. First we create a dump – this usually must be done by a system user, as access is needed to the export directory mentioned before.

{% hint style="info" %}
In Oracle, every user has a schema named the same as the user, and all objects have "owners".&#x20;

All schema names are case sensitive.
{% endhint %}

&#x20;The first parameter is the login. You log in as `sysdba`, which is a default DBA[^2] user authenticated by the operating system, hence no username/password is specified, just a slash (`/`).

{% code overflow="wrap" %}
```
$ expdp \"/ as sysdba\" SCHEMAS=APP CONTENT=METADATA_ONLY EXCLUDE=STATISTICS DUMPFILE=app.dmpimpdp \"/ as sysdba\" dumpfile=app.dmp sqlfile=app.sql
```
{% endcode %}

When run, the progress of the export is shown. When the process ends, it tells you where the export file is placed, which is the default Data Pump directory. In this case, it is `/u01/app/oracle/admin/XE/dpdump/`.

To extract the schema, run the import tool, like this:

```
$ impdp \"/ as sysdba\" dumpfile=app.dmp sqlfile=app.sql
```

The app.sql file in the default Data Pump directory is `/u01/app/oracle/admin/XE/dpdump/app.sql`.

The advantage of this method is that you can work from a backup. The disadvantage is that this method is not very flexible, and all facts on all objects are exported, even things that are not relevant for a migration.

To export all schema data, skip the `SCHEMAS` parameter, and instead add `FULL=Y`, like this:

{% code overflow="wrap" %}
```
$ expdp \"/ as sysdba\" FULL=Y CONTENT=METADATA_ONLY EXCLUDE=STATISTICS DUMPFILE=app.dmpimpdp \"/ as sysdba\" dumpfile=app.dmp sqlfile=app.sql
```
{% endcode %}

To get the DDL for the appropriate objects, use the `impdp` command like above, where you can use the `SCHEMAS` parameter to filter which schemas you are looking for. If you don't do this, you get the SQL for every object in the Oracle database, including system schemas.

### **Using dbms\_metadata.get\_ddl**

This method is much more flexible and creates more reasonable output, but it requires a running Oracle database. It uses a built-in PL/SQL package called `dbms_metadata`, where the `get_ddl` function is used to retrieve the DDL for a specific object. There is also a function called `set_transform_param` that is used to pass parameters to the `get_ddl` function.

This method only exports objects relevant for a migration – it does not export Oracle specific objects nor any system owned objects.

A similar operation as with Data Pump can be executed using a script like this – put it in an SQL file called `exp.sql`:

{% code expandable="true" %}
```plsql
# exp.sql
set long 99999999
set pagesize 0
set feedback off
set echo off
set heading off
SET TRIMSPOOL ON

BEGIN
   dbms_metadata.set_transform_param(dbms_metadata.session_transform, 'PRETTY', TRUE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform, 'TABLESPACE', FALSE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform, 'SQLTERMINATOR', TRUE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform, 'SEGMENT_ATTRIBUTES', FALSE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform, 'FORCE', FALSE);
END;
/

SELECT dbms_metadata.get_ddl(object_type, object_name, user)
  FROM user_objects
  WHERE object_type IN ('TABLE', 'VIEW', 'SEQUENCE', 'FUNCTION', 'PACKAGE',
   'PACKAGE_BODY', 'PROCEDURE', 'INDEX', 'SYNONYM', 'TRIGGER', 'TYPE')
  ORDER BY DECODE(object_type, 'TABLE', 1, 'VIEW', 2, 'INDEX', 3,
    'TRIGGER', 4, 'PACKAGE', 5, 'PACKAGE BODY', 6, 7), object_type;

EXIT
```
{% endcode %}

When done, run this script through the Oracle `SQL*Plus` utility. You can run that tool as an ordinary user with privileges appropriate to the schema to export. In other words, you do not need DBA privileges. Issue this command:

```
$ sqlplus -S app/app @exp.sql > schema.sql
```

To export all schemas using this method, excluding known system schemas, a slightly different SQL script is used, `expall.sql`:

{% code expandable="true" %}
```plsql
# expall.sql
set long 99999999
set pagesize 50000
set feedback off
set echo off
set heading off
SET TRIMSPOOL ON

BEGIN
   dbms_metadata.set_transform_param(dbms_metadata.session_transform,
     'PRETTY', TRUE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform,
     'TABLESPACE', FALSE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform,
     'SQLTERMINATOR', TRUE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform,
     'SEGMENT_ATTRIBUTES', FALSE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform,
     'FORCE', FALSE);
   dbms_metadata.set_transform_param(dbms_metadata.session_transform,
     'CONSTRAINTS_AS_ALTER', TRUE);
END;
/

column OWNER noprint new_value owner_name
break on OWNER skip page
ttitle LEFT '-- Dumping objects for user ' owner_name

SELECT owner, dbms_metadata.get_ddl(object_type, object_name, owner)
  FROM dba_objects
  WHERE object_type IN ('TABLE', 'VIEW', 'SEQUENCE', 'FUNCTION', 'PACKAGE',
     'PACKAGE_BODY', 'PROCEDURE', 'INDEX', 'SYNONYM', 'TRIGGER', 'TYPE')
    AND owner NOT IN('CTXSYS', 'DBSNMP', 'DMSYS', 'MDDATA', 'MDSYS',
      'OLAPSYS', 'ORDSYS', 'ORDPLUGINS', 'OUTLN', 'PUBLIC',
      'SI_INFORMTN_SCHEMA', 'SYS', 'SYSMAN', 'SYSTEM', 'XDB')
    AND temporary = 'N' AND generated = 'N' 
    AND (secondary = 'N' OR secondary IS NULL)
  ORDER BY owner, DECODE(object_type, 'TABLE', 1, 'VIEW', 2, 'INDEX', 3,
    'TRIGGER', 4, 'PACKAGE', 5, 'PACKAGE BODY', 6, 7), object_type;

EXIT
```
{% endcode %}

Run this script as a DBA user:

```
$ sqlplus -S / as sysdba @expall.sql > schema.sql
```

## Microsoft SQL Server

For most existing SQL server environments, admin work is done using the GUI tool SQL server Management Studio (SSMS). Use the generate scripts option in SSMS: See [this documentation](https://docs.microsoft.com/en-us/sql/ssms/scripting/generate-scripts-sql-server-management-studio?view=sql-server-ver15) for more details.

Command-line options exist – the SQL server team released a Python-based tool called `mssql-scripter`. Examples of usage are in [this document](https://cloudblogs.microsoft.com/sqlserver/2017/05/17/try-new-sql-server-command-line-tools-to-generate-t-sql-scripts-and-monitor-dynamic-management-views/). Full `mssql-scripter` [usage options are listed here](https://github.com/microsoft/mssql-scripter/blob/dev/doc/usage_guide.md).

## MySQL

Due to the similarities between MySQL and MariaDB, we are able to assess server configurations, too, for different types of `mysqldump` exports (`--all-databases` and `--databases`` `_`list-of-databases`_).

Use `mysqldump` with the connection information to back up all your databases on the existing MySQL Server:

```shellscript
mysqldump --user db_user --password \
--host localhost \
--no-data \
--events \
--routines \
--triggers \
-r mydump.sql \
--all-databases
```

You can also choose to export only select databases:

```bash
mysqldump --user user_db --password \
--host localhost \
--no-data \
--events \
--routines \
--triggers \
-r mydump.sql \
--databases mydb1 mydb2 …
```

Optionally, you can upload your configuration variables to find differences between your MySQL and MariaDB server configurations. Run this command:

{% code overflow="wrap" %}
```bash
mysql --user db_user --password --host localhost -e "SHOW GLOBAL VARIABLES;" > variables.log
```
{% endcode %}

The `variables.log` file can be used for offline comparison between MySQL and MariaDB, to identify any differences.

## IBM DB2

Log on to the DB2 server with a user that has `SELECT` privileges on the system catalog tables. In some specific cases, additional grants might be required, such as `SYSADM`, `SYSCTRL`, `SYSMAINT`, `SYSMON`, and `DBADM`. For our specific requirements, the `SELECT` privilege on system catalog tables suffices, though.

{% hint style="info" %}
In case of problems, request the DBA to export the schema DDL.
{% endhint %}

The following list gives examples of various extract options available when extracting DDL from a DB2 server.

* Generate the DDL script for all the objects created by user `foo` in `world` database:
  * `-d` defines the database/alias of the database that you want to extract.
  * `-u` defines the user name you want to export objects of.
  * `-e` is used to export all the possible objects including tables, stored procedures, aliases, triggers, etc.
  * `-o ddl_export.sql` represents the output file.
  * This is the complete command:\
    `$ db2look -d world -u foo -e -o ddl_export.sql`&#x20;
* Generate the DDL script for objects in a particular schema:
  * `-d` defines the database/alias of the database that you want to extract.
  * `-u` defines the user name we want to export objects of.
  * `-z` defines the schema name.
  * `-e` is used to export all the possible objects including tables, stored procedures, aliases, triggers, etc.
  * `-o ddl_export.sql` represents the output file name.
  * This is the complete command:\
    `$ db2look -d world -u foo -z globe -e -o ddl_export.sql`&#x20;
* Generate the DDL script of all the objects regardless of the user they are created with. This is the one most of the exports will be done with, for the sake of completion of the DDL script:
  * `-d` defines the database/alias of the database that you want to extract.
  * `-a` is used to extract objects for all users on the particular database.
  * `-o ddl_export.sql` represents the output file name.
  * `-e` is used to export all the possible objects including tables, stored procedures, aliases, triggers, etc.
  * This is the complete command:\
    `$ db2look -d world -a -e -o ddl_export.sql`

The `db2look` command arguments mentioned before work for all DB2 versions starting from DB2 9.7 to 11.5, but for specifics details, refer to the following DB2 pages:

* 9.7 - [db2look - DB2 statistics and DDL extraction tool command](https://www.ibm.com/support/knowledgecenter/SSEPGG_9.7.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0002051.html)
* 10.5 - [db2look - DB2 statistics and DDL extraction tool command](https://www.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0002051.html)
* 11.5 - [db2look - Db2 statistics and DDL extraction tool command](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0002051.html)



[^1]: **DDL (Data Definition Language)** is the part of SQL used to **define and change the structure of database objects**.

    It covers operations like:

    * Creating and removing objects: `CREATE`, `DROP`
    * Changing object definitions: `ALTER`
    * Clearing data while keeping the table structure: `TRUNCATE`

    DDL affects **schema metadata** (tables, columns, indexes, constraints, views), not day-to-day row updates like `INSERT`/`UPDATE`/`DELETE`.

[^2]: **DBA (Database Administrator)** is the person (or role) responsible for **operating and maintaining databases**.

    Typical DBA work includes **user access**, **backups and recovery**, **performance tuning**, **monitoring**, and **schema changes**.
