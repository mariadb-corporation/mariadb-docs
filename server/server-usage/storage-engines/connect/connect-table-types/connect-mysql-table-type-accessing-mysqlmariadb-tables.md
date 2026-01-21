---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT MYSQL Table Type: Accessing MySQL/MariaDB Tables

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

This table type uses libmysql API to access a MySQL or MariaDB table or view. This\
table must be created on the current server or on another local or remote\
server. This is similar to what the [FederatedX](../../federatedx-storage-engine/) storage engine provides with some\
differences.

Currently the Federated-like syntax can be used to create such a table, for instance:

```sql
CREATE TABLE essai (
  num INTEGER(4) NOT NULL,
  line CHAR(15) NOT NULL)
ENGINE=CONNECT table_type=MYSQL
CONNECTION='mysql://root@localhost/test/people';
```

The connection string can have the same syntax as that used by FEDERATED

```
scheme://username:password@hostname:port/database/tablename
scheme://username@hostname/database/tablename
scheme://username:password@hostname/database/tablename
scheme://username:password@hostname/database/tablename
```

However, it can also be mixed with connect standard options. For instance:

```sql
CREATE TABLE essai (
  num INTEGER(4) NOT NULL,
  line CHAR(15) NOT NULL)
ENGINE=CONNECT table_type=MYSQL dbname=test tabname=people
CONNECTION='mysql://root@localhost';
```

It can also be specified as a reference to a federated server:

```
connection="connection_one"
connection="connection_one/table_foo"
```

The pure (deprecated) CONNECT syntax is also accepted:

```sql
CREATE TABLE essai (
  num INTEGER(4) NOT NULL,
  line CHAR(15) NOT NULL)
ENGINE=CONNECT table_type=MYSQL dbname=test tabname=people
option_list='user=root,host=localhost';
```

The specific connection items are:

| Option   | Default value           | Description                                      |
| -------- | ----------------------- | ------------------------------------------------ |
| Table    | The table name          | The name of the table to access.                 |
| Database | The current DB name     | The database where the table is located.         |
| Host     | localhost\*             | The host of the server, a name or an IP address. |
| User     | The current user        | The connection user name.                        |
| Password | No password             | An optional user password.                       |
| Port     | The currently used port | The port of the server.                          |
| Quoted   | 0                       | 1 if remote Tabname must be quoted.              |

*
  * When the host is specified as “localhost”, the connection is established on Linux using Linux sockets. On Windows, the connection is established by default using shared memory if it is enabled. If not, the TCP protocol is used. An alternative is to specify the host as “.” to use a named pipe connection (if it is enabled). This makes possible to use these table types with server skipping networking.

**Caution:** Take care not to refer to the MYSQL table itself to avoid an infinite loop!

MYSQL table can refer to the current server as well as to another server. Views\
can be referred by name or directly giving a source definition, for instance:

```sql
CREATE TABLE grp ENGINE=CONNECT table_type=mysql
CONNECTION='mysql://root@localhost/test/people'
SRCDEF='select title, count(*) as cnt from employees group by title';
```

When specified, the columns of the mysql table must exist in the accessed table with the same name, but can be only a subset of them and specified in a different order. Their type must be a type supported by CONNECT and, if it is not identical to the type of the accessed table matching column, a conversion can be done according to the rules given in [Data type conversion](../connect-data-types.md#data-type-conversion).

Note: For columns prone to be targeted by a where clause, keep the column type compatible with the source table column type (numeric or character) to have a correct rephrasing of the where clause.

If you do not want to restrict or change the column definition, do not provide it and leave CONNECT get the column definition from the remote server. For instance:

```sql
CREATE TABLE essai ENGINE=CONNECT table_type=MYSQL
CONNECTION='mysql://root@localhost/test/people';
```

This will create the _essai_ table with the same columns than the people table. If the target table contains CONNECT incompatible type columns, see [Data type conversion](../connect-data-types.md#data-type-conversion) to know how these columns can be converted or skipped.

## Charset Specification

When accessing the remote table, CONNECT sets the connection charset set to the default local table charset as the FEDERATED engine does.

Do not specify a column character set if it is different from the table default character set even when it is the case on the remote table. This is because the remote column is translated to the local table character set when reading it. This is the default but it can be modified by the setting the [character\_set\_results](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_results) variable of the target server. If it must keep its setting, for instance to UTF8 when containing Unicode characters, specify the local default charset to its character set.

This means that it is not possible to correctly retrieve a remote table if it contains columns having different character sets. A solution is to retrieve it by several local tables, each accessing only columns with the same character set.

## Indexing of MYSQL tables

Indexes are rarely useful with MYSQL tables. This is because CONNECT tries to access only the\
requested rows. For instance if you ask:

```sql
SELECT * FROM essai WHERE num = 23;
```

CONNECT will construct and send to the server the query:

```sql
SELECT num, line FROM people WHERE num = 23
```

If the _people_ table is indexed on _num_, indexing are used on the remote server. This, in all cases,\
will limit the amount of data to retrieve on the network.

However, an index can be specified for columns that are prone to be used to join another table to the\
MYSQL table. For instance:

```
SELECT d.id, d.name, f.dept, f.salary
FROM loc_tab d STRAIGHT_JOIN cnc_tab f ON d.id = f.id
WHERE f.salary > 10000;
```

If the _id_ column of the remote table addressed by the _cnc\_tab_ MYSQL table is indexed (which is likely\
if it is a key) you should also index the _id_ column of the MYSQL _cnc\_tab_ table. If so, using “remote”\
indexing as does FEDERATED, only the useful rows of the remote table are retrieved during the\
join process. However, because these rows are retrieved by separate [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements, this is\
useful only when retrieving a few rows of a big table.

In particular, you should not specify an index for columns not used for joining and above all DO NOT\
index a joined column if it is not indexed in the remote table. This would cause multiple scans of the\
remote table to retrieve the joined rows one by one.

## Data Modifying Operations

The CONNECT MYSQL type supports [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) and [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) and a somewhat limited form\
of [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md). These are described below.

The MYSQL type uses similar methods than the ODBC type to implement the [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md),[UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) commands. Refer to the ODBC chapter for the restrictions\
concerning them.

For the [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) commands, there are fewer restrictions because the\
remote server being a MySQL server, the syntax of the command are always\
acceptable by the remote server.

For instance, you can freely use keywords like IGNORE or LOW\_PRIORITY as well\
as scalar functions in the SET and WHERE clauses.

However, there is still an issue on multi-table statements. Let us suppose you\
have a _t1_ table on the remote server and want to execute a query such as:

```sql
UPDATE essai AS x SET line = (SELECT msg FROM t1 WHERE id = x.num)
WHERE num = 2;
```

When parsed locally, you will have errors if no _t1_ table exists or if it\
does not have the referenced columns. When _t1_ does not exist, you can\
overcome this issue by creating a local dummy _t1_ table:

```
CREATE TABLE t1 (id INT, msg CHAR(1)) ENGINE=BLACKHOLE;
```

This will make the local parser happy and permit to execute the command on the\
remote server. Note however that having a local MySQL table defined on the\
remote _t1_ table does not solve the problem unless it is also names _t1_\
locally.

This is why, to permit to have all types of commands executed by the data\
source without any restriction, CONNECT provides a specific MySQL table subtype\
described now.

## Sending commands to a MariaDB Server

This can be done like for ODBC or JDBC tables by defining a specific table that are used to send commands and get the result of their execution..

```sql
  number int(5) not null flag=1,
CREATE TABLE send (
  command VARCHAR(128) NOT NULL,
  warnings INT(4) NOT NULL flag=3,
  message VARCHAR(255) flag=2)
ENGINE=CONNECT table_type=mysql
CONNECTION='mysql://user@host/database'
option_list='Execsrc=1,Maxerr=2';
```

The key points in this create statement are the EXECSRC option and the column definition.

The EXECSRC option tells that this table are used to send commands to the\
MariaDB server. Most of the sent commands do not return result set. Therefore,\
the table columns are used to specify the command to be executed and to get the\
result of the execution. The name of these columns can be chosen arbitrarily,\
their function coming from the FLAG value:

|         |                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------ |
| Flag=0: | The command to execute (the default)                                                                   |
| Flag=1: | The number of affected rows, or the result number of columns if the command would return a result set. |
| Flag=2: | The returned (eventually error) message.                                                               |
| Flag=3: | The number of warnings.                                                                                |

How to use this table and specify the command to send? By executing a command such as:

```sql
SELECT * FROM send WHERE command = 'a command';
```

This will send the command specified in the WHERE clause to the data source and\
return the result of its execution. The syntax of the WHERE clause must be\
exactly as shown above. For instance:

```sql
SELECT * FROM send WHERE command =
'CREATE TABLE people (
num integer(4) primary key autoincrement,
line char(15) not null';
```

This command returns:

| command                                                | warnings | number | message       |
| ------------------------------------------------------ | -------- | ------ | ------------- |
| CREATE TABLE people (num integer(4) primary key aut... | 0        | 0      | Affected rows |

### Sending several commands in one call

It can be faster to execute because there are only one connection for all\
of them. To send several commands in one call, use the following syntax:

```sql
SELECT * FROM send WHERE command IN (
"update people set line = 'Two' where id = 2",
"update people set line = 'Three' where id = 3");
```

When several commands are sent, the execution stops at the end of them or after\
a command that is in error. To continue after n errors, set the option\
maxerr=_n_ (0 by default) in the option list.

**Note 1:** It is possible to specify the SRCDEF option when creating an\
EXECSRC table. It are the command sent by default when a WHERE clause is\
not specified.

**Note 2:** Backslashes inside commands must be escaped. Simple quotes must be\
escaped if the command is specified between simple quotes, and double quotes if\
it is specified between double quotes.

**Note 3:** Sent commands apply in the specified database. However, they can\
address any table within this database.

**Note 4:** Currently, all commands are executed in mode AUTOCOMMIT.

### Retrieving Warnings and Notes

If a sent command causes warnings to be issued, it is useless to resend a “show\
warnings” command because the MariaDB server is opened and closed when sending\
commands. Therefore, getting warnings requires a specific (and tricky) way.

To indicate that warning text must be added to the returned result, you must\
send a multi-command query containing “pseudo” commands that are not sent to\
the server but directly interpreted by the EXECSRC table. These “pseudo”\
commands are:

|         |                                        |
| ------- | -------------------------------------- |
| Warning | To get warnings                        |
| Note    | To get notes                           |
| Error   | To get errors returned as warnings (?) |

Note that they must be spelled (case insensitive) exactly as above, no final “s”. For instance:

```sql
SELECT * FROM send WHERE command IN ('Warning','Note',
'drop table if exists try',
'create table try (id int key auto_increment, msg varchar(32) not
null) engine=aria',
"insert into try(msg) values('One'),(NULL),('Three') ",
"insert into try values(2,'Deux') on duplicate key update msg =
'Two'",
"insert into try(message) values('Four'),('Five'),('Six')",
'insert into try(id) values(NULL)',
"update try set msg = 'Four' where id = 4",
'select * from try');
```

This can return something like this:

| command                                               | warnings | number | message                                  |
| ----------------------------------------------------- | -------- | ------ | ---------------------------------------- |
| drop table if exists try                              | 1        | 0      | Affected rows                            |
| Note                                                  | 0        | 1051   | Unknown table 'try'                      |
| create table try (id int key auto\_increment, msg...  | 0        | 0      | Affected rows                            |
| insert into try(msg) values('One'),(NULL),('Three')   | 1        | 3      | Affected rows                            |
| Warning                                               | 0        | 1048   | Column 'msg' cannot be null              |
| insert into try values(2,'Deux') on duplicate key...  | 0        | 2      | Affected rows                            |
| insert into try(msge) values('Four'),('Five'),('Six') | 0        | 1054   | Unknown column 'msge' in 'field list'    |
| insert into try(id) values(NULL)                      | 1        | 1      | Affected rows                            |
| Warning                                               | 0        | 1364   | Field 'msg' doesn't have a default value |
| update try set msg = 'Four' where id = 4              | 0        | 1      | Affected rows                            |
| select \* from try                                    | 0        | 2      | Result set columns                       |

The execution continued after the command in error because of the MAXERR\
option. Normally this would have stopped the execution.

Of course, the last “select” command is useless here because it cannot return\
the table contain. Another MYSQL table without the EXECSRC option and with\
proper column definition should be used instead.

## Connection Engine Limitations

### Data types

There is a maximum key.index length of 255 bytes. You may be able to declare the table without an index and rely on the engine condition pushdown and remote schema.

The following types can't be used:

* [BIT](../../../../reference/data-types/numeric-data-types/bit.md)
* [BINARY](../../../../reference/data-types/string-data-types/binary.md)
* [TINYBLOB](../../../../reference/data-types/string-data-types/tinyblob.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md), [MEDIUMBLOB](../../../../reference/data-types/string-data-types/mediumblob.md), [LONGBLOB](../../../../reference/data-types/string-data-types/longblob.md)
* [TINYTEXT](../../../../reference/data-types/string-data-types/tinytext.md), [MEDIUMTEXT](../../../../reference/data-types/string-data-types/mediumtext.md), [LONGTEXT](../../../../reference/data-types/string-data-types/longtext.md)
* [ENUM](../../../../reference/data-types/string-data-types/enum.md)
* [SET](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md)
* [Geometry types](../../../../reference/sql-structure/geometry/geometry-types.md)

Note: [TEXT](../../../../reference/data-types/string-data-types/text.md) is allowed. However, the handling depends on the values given to the [connect\_type\_conv](../connect-system-variables.md#connect_type_conv) and [connect\_conv\_size](../connect-system-variables.md#connect_conv_size) system variables, and by default no conversion of TEXT columns is permitted.

### SQL Limitations

The following SQL queries are not supported

* [REPLACE INTO](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md)
* [INSERT ... ON DUPLICATE KEY UPDATE](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md)

## CONNECT MYSQL versus FEDERATED

The CONNECT MYSQL table type should not be regarded as a replacement for the [FEDERATED(X)](../../federatedx-storage-engine/) engine. The main use of the MYSQL type is to access other engine tables as if they were CONNECT tables. This was necessary when accessing tables\
from some CONNECT table types such as [TBL](connect-tbl-table-type-table-list.md), [XCOL](connect-xcol-table-type.md), [OCCUR](connect-occur-table-type.md), or [PIVOT](connect-pivot-table-type.md) that are\
designed to access CONNECT tables only. When their target table is not a\
CONNECT table, these types are silently using internally an intermediate MYSQL\
table.

However, there are cases where you can use MYSQL CONNECT tables yourself, for instance:

1. When the table are used by a [TBL](connect-tbl-table-type-table-list.md) table. This enables you to specify the connection parameters for each sub-table and is more efficient than using a\
   local FEDERATED sub-table.
2. When the desired returned data is directly specified by the SRCDEF option.\
   This is great to let the remote server do most of the job, such as grouping\
   and/or joining tables. This cannot be done with the FEDERATED engine.
3. To take advantage of the push\_cond facility that adds a where clause to the command sent to the remote table. This restricts the size of the result set and can be crucial for big tables.
4. For tables with the EXECSRC option on.
5. When doing tests. For instance to check a connection string.

If you need multi-table updating, deleting, or bulk inserting on a remote\
table, you can alternatively use the FEDERATED engine or a “send” table\
specifying the EXECSRC option on.

## See also

* [Using the TBL and MYSQL types together](connect-using-the-tbl-and-mysql-table-types-together.md)

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
