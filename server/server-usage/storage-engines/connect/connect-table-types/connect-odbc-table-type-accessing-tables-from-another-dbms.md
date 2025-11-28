# CONNECT ODBC Table Type: Accessing Tables From Another DBMS

{% hint style="info" %}
This storage engine has been deprecated.
{% endhint %}

ODBC (Open Database Connectivity) is a standard API for accessing database management systems (DBMS). CONNECT uses this API to access data contained in other DBMS without having to implement a specific application for each one. An exception is the access to MySQL that should be done using the [MYSQL table type](connect-mysql-table-type-accessing-mysqlmariadb-tables.md).

Note: On Linux, unixODBC must be installed.

These tables are given the type ODBC. For example, if a "Customers" table is\
contained in an Access™ database you can define it\
with a command such as:

```
CREATE TABLE Customer (
  CustomerID VARCHAR(5),
  CompanyName VARCHAR(40),
  ContactName VARCHAR(30),
  ContactTitle VARCHAR(30),
  Address VARCHAR(60),
  City VARCHAR(15),
  Region VARCHAR(15),
  PostalCode VARCHAR(10),
  Country VARCHAR(15),
  Phone VARCHAR(24),
  Fax VARCHAR(24))
ENGINE=CONNECT table_type=ODBC block_size=10
tabname='Customers'
CONNECTION='DSN=MS Access Database;DBQ=C:/Program
Files/Microsoft Office/Office/1033/FPNWIND.MDB;';
```

Tabname option defaults to the table name. It is required if the source table\
name is different from the name of the CONNECT table. Note also that for some data sources this name is case sensitive.

Often, because CONNECT can retrieve the table description using ODBC catalog\
functions, the column definitions can be unspecified. For instance this table\
can be simply created as:

```
CREATE TABLE Customer ENGINE=CONNECT table_type=ODBC
  block_size=10 tabname='Customers'
  CONNECTION='DSN=MS Access Database;DBQ=C:/Program Files/Microsoft Office/Office/1033/FPNWIND.MDB;';
```

The `BLOCK_SIZE` specification are used later to set the RowsetSize when\
retrieving rows from the ODBC table. A reasonably large RowsetSize can greatly\
accelerate the fetching process.

If you specify the column description, the column names of your table must\
exist in the data source table. However, you are not obliged to define all the\
data source columns and you can change the order of the columns. Some type\
conversion can also be done if appropriate. For instance, to access the\
FireBird sample table EMPLOYEE, you could define your table as:

```
CREATE TABLE empodbc (
  EMP_NO SMALLINT(5) NOT NULL,
  FULL_NAME VARCHAR(37) NOT NULL),
  PHONE_EXT VARCHAR(4) NOT NULL,
  HIRE_DATE DATE,
  DEPT_NO SMALLINT(3) NOT NULL,
  JOB_COUNTRY VARCHAR(15),
  SALARY DOUBLE(12,2) NOT NULL)
ENGINE=CONNECT table_type=ODBC tabname='EMPLOYEE'
CONNECTION='DSN=firebird';
```

This definition ignores the FIRST\_NAME, LAST\_NAME, JOB\_CODE, and JOB\_GRADE\
columns. It places the FULL\_NAME last column of the original table in second\
position. The type of the HIRE\_DATE column was changed from _timestamp_ t&#x6F;_date_ and the type of the DEPT\_NO column was changed from _char_ t&#x6F;_integer_.

Currently, some restrictions apply to ODBC tables:

1. Cursor type is forward only (sequential reading).
2. No indexing of ODBC tables (do not specify any columns as key). However,\
   because CONNECT can often add a where clause to the query sent to the data\
   source, indexing are used by the data source if it supports it. (Remote indexing is available with version 1.04, released with [MariaDB 10.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes))
3. CONNECT ODBC supports [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) and [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md). [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) are also supported\
   in a somewhat restricted way (see below). For other operations, use an ODBC\
   table with the EXECSRC option (see below) to directly send proper commands\
   to the data source.

## Random Access of ODBC Tables

In CONNECT version 1.03 (until [MariaDB 10.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes)) ODBC tables are not indexable. Version 1.04 (from [MariaDB 10.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes)) adds remote indexing facility to the ODBC table type.

However, some queries require random access to an ODBC table; for instance when it is joined to another table or used in an order by queries applied to a long column or large tables.

There are several ways to enable random (position) access to a CONNECT ODBC table. They are dependant on the following table options:

| Option       | Type    | Used For                          |
| ------------ | ------- | --------------------------------- |
| Block\_Size  | Integer | Specifying the rowset size.       |
| Memory\*     | Integer | Storing the result set in memory. |
| Scrollable\* | Boolean | Using a scrollable cursor.        |

`*` - To be specified in the option\_list.

When dealing with small tables, the simpler way to enable random access is to specify a rowset size equal or larger than the table size (or the result set size if a push down where clause is used). This means that the whole result is in memory on the first fetch and CONNECT will use it for further positional accesses.

Another way to have the result set in memory is to use the memory option. This option can be set to the following values:

**0.** No memory used (the default). Best when the table is read sequentially as in SELECT statements with only eventual WHERE clauses.**1.** Memory size required is calculated during the first sequential table read. The allocated memory is filled during the second sequential read. Then the table rows are retrieved from the memory. This should be used when the table are accessed several times randomly, such as in sub-selects or being the target table of a join.**2.** A first query is executed to get the result set size and the needed memory is allocated. It is filled on the first sequential reading. Then random access of the table is possible. This can be used in the case of ORDER BY clauses, when MariaDB uses position reading.

Note that the best way to handle ORDER BY is to set the max\_length\_for\_sort\_data variable to a larger value (its default value is 1024 that is pretty small). Indeed, it requires less memory to be used, particularly when a WHERE clause limits the retrieved data set. This is because in the case of an order by query, MariaDB firstly retrieves the sequentially the result set and the position of each records. Often the sort can be done from the result set if it is not too big. But if too big, or if it implies some “long” columns, only the positions are sorted and MariaDB retrieves the final result from the table read in random order. If setting the max\_length\_for\_sort\_data variable is not feasible or does not work, to be able to retrieve table data from memory after the first sequential read, the memory option must be set to 2.

For tables too large to be stored in memory another possibility is to make your table to use a scrollable cursor. In this case each randomly accessed row can be retrieved from the data source specifying its cursor position, which is reasonably fast. However, scrollable cursors are not supported by all data sources.

With CONNECT version 1.04 (from [MariaDB 10.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes)), another way to provide random access is to specify some columns to be indexed. This should be done only when the corresponding column of the source table is also indexed. This should be used for tables too large to be stored in memory and is similar to the remote indexing used by the [MYSQL table type](connect-mysql-table-type-accessing-mysqlmariadb-tables.md) and by the [FEDERATED engine](../../federatedx-storage-engine/).

There remains the possibility to extract data from the external table and to construct\
another table of any file format from the data source. For instance to construct\
a fixed formatted DOS table containing the CUSTOMER table data, create the\
table as

```
CREATE TABLE Custfix ENGINE=CONNECT File_name='customer.txt'
  table_type=fix block_size=20 AS SELECT * FROM customer;
```

Now you can use _custfix_ for fast database operations on the copied_customer_ table data.

## Retrieving data from a spreadsheet

ODBC can also be used to create tables based on tabular data belonging to an\
Excel spreadsheet:

```
CREATE TABLE XLCONT
ENGINE=CONNECT table_type=ODBC tabname='CONTACT'
CONNECTION='DSN=Excel Files;DBQ=D:/Ber/Doc/Contact_BP.xls;';
```

This supposes that a tabular zone of the sheet including column headers is\
defined as a table named CONTACT or using a “named reference”. Refer to the Excel documentation for how to\
specify tables inside sheets. Once done, you can ask:

```
SELECT * FROM xlcont;
```

This will extract the data from Excel and display:

| Nom                 | Fonction                            | Societe                 |
| ------------------- | ----------------------------------- | ----------------------- |
| Boisseau Frederic   |                                     | 9 Telecom               |
| Martelliere Nicolas |                                     | Vidal SA (Groupe UBM)   |
| Remy Agathe         |                                     | Price Minister          |
| Du Halgouet Tanguy  |                                     | Danone                  |
| Vandamme Anna       |                                     | GDF                     |
| Thomas Willy        |                                     | Europ Assistance France |
| Thomas Dominique    |                                     | Acoss (DG des URSSAF)   |
| Thomas Berengere    | Responsable SI Decisionnel          | DEXIA Credit Local      |
| Husy Frederic       | Responsable Decisionnel             | Neuf Cegetel            |
| Lemonnier Nathalie  | Directeur Marketing Client          | Louis Vuitton           |
| Louis Loic          | Reporting International Decisionnel | Accor                   |
| Menseau Eric        |                                     | Orange France           |

Here again, the columns description was left to CONNECT when creating the table.

## Multiple ODBC tables

The concept of multiple tables can be extended to ODBC tables when they are\
physically represented by files, for instance to Excel or Access tables. The\
condition is that the connect string for the table must contain a field\
DBQ=_filename_, in which wildcard characters can be included as for\
multiple=1 tables in their filename. For instance, a table contained in several\
Excel files CA200401.xls, CA200402.xls, ...CA200412.xls can be created by a\
command such as:

```
CREATE TABLE ca04mul (DATE CHAR(19), OPERATION VARCHAR(64),
  Debit DOUBLE(15,2), Credit DOUBLE(15,2))
ENGINE=CONNECT table_type=ODBC multiple=1
qchar= '"' tabname='bank account'
CONNECTION='DSN=Excel Files;DBQ=D:/Ber/CA/CA2004*.xls;';
```

Providing that in each file the applying information is internally set for\
Excel as a table named "bank account". This extension to ODBC does not support_&#x6D;ultiple_=2. The _qchar_ option was specified to make the identifiers\
quoted in the select statement sent to ODBC, in particular the when the table\
or column names contain blanks, to avoid SQL syntax errors.

**Caution:** Avoid accessing tables belonging to the currently running MariaDB server via the MySQL ODBC connector. This may not work and may cause the server to be restarted.

## Performance consideration

To avoid extracting entire tables from an ODBC source, which can be a lengthy\
process, CONNECT extracts the "compatible" part of query WHERE clauses and adds\
it to the ODBC query. Compatible means that it must be understood by the data\
source. In particular, clauses involving scalar functions are not kept because\
the data source may have different functions than MariaDB or use a different\
syntax. Of course, clauses involving sub-select are also skipped. This will\
transfer eventual indexing to the data source.

Take care with clauses involving string items because you may not know whether\
they are treated by the data source as case sensitive or case insensitive. If in\
doubt, make your queries as if the data source was processing strings as case\
sensitive to avoid incomplete results.

## Using ODBC Tables inside correlated sub-queries

Unlike not correlated subqueries that are executed only once, correlated subqueries are executed many\
times. It is what ODBC calls a "requery". Several methods can be used by CONNECT to deal with this\
depending on the setting of the MEMORY or SCROLLABLE Boolean options:

| Option         | Description                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| Default        | Implementing "requery" by discarding the current result set and re submitting the query (as MFC does) |
| Memory=1 or 2  | Storing the result set in memory as MYSQL tables do.                                                  |
| Scrollable=Yes | Using a scrollable cursor.                                                                            |

Note: the MEMORY and SCROLLABLE options must be specified in the OPTION \_ LIST.

Because the table is accessed several times, this can make queries last very long except for small tables\
and is almost unacceptable for big tables. However, if it cannot be avoided, using the memory method\
is the best choice and can be more than four times faster than the default method. If it is supported by the driver, using a scrollable cursor is slightly slower than using memory but can be an alternative to avoid memory problems when the sub-query returns a huge result set.

If the result set is of reasonable size, it is also possible to specify the block\_size option equal or slightly larger than the result set. The whole result set being read on the first fetch, can be accessed many times without having to do anything else.

Another good workaround is to replace within the correlated sub-query the ODBC table by a local copy of it because MariaDB is often able to optimize the query and to provide a very fast execution.

## Accessing specified views

Instead of specifying a source table name via the TABNAME option, it is\
possible to retrieve data from a “view” whose definition is given in a new\
option SRCDEF. For instance:

```
CREATE TABLE custnum (
  country VARCHAR(15) NOT NULL,
  customers INT(6) NOT NULL)
ENGINE=CONNECT TABLE_TYPE=ODBC BLOCK_SIZE=10
CONNECTION='DSN=MS Access Database;DBQ=C:/Program Files/Microsoft Office/Office/1033/FPNWIND.MDB;'
SRCDEF='select country, count(*) as customers from customers group by country';
```

Or simply, because CONNECT can retrieve the returned column definition:

```
CREATE TABLE custnum ENGINE=CONNECT TABLE_TYPE=ODBC BLOCK_SIZE=10
CONNECTION='DSN=MS Access Database;DBQ=C:/Program Files/Microsoft Office/Office/1033/FPNWIND.MDB;'
SRCDEF='select country, count(*) as customers from customers group by country';
```

Then, when executing for instance:

```
SELECT * FROM custnum WHERE customers > 3;
```

The processing of the group by is done by the data source, which returns only\
the generated result set on which only the where clause is performed locally.\
The result:

| country   | customers |
| --------- | --------- |
| Brazil    | 9         |
| France    | 11        |
| Germany   | 11        |
| Mexico    | 5         |
| Spain     | 5         |
| UK        | 7         |
| USA       | 13        |
| Venezuela | 4         |

This makes possible to let the data source do complicated operations, such as\
joining several tables or executing procedures returning a result set. This\
minimizes the data transfer through ODBC.

## Data Modifying Operations

The only data modifying operations are the [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) , [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) commands.\
They can be executed successfully only if the data source database or tables\
are not read/only.

### INSERT Command

When inserting values to an ODBC table, local values are used and sent to the\
ODBC table. This does not make any difference when the values are constant but\
in a query such as:

```
INSERT INTO t1 SELECT * FROM t2;
```

Where t1 is an ODBC table, t2 is a locally defined table that must exist on the\
local server. Besides, it is a good way to create a distant ODBC table from\
local data.

CONNECT does not directly support INSERT commands such as:

```
INSERT INTO t1 VALUES(2,'Deux') ON duplicate KEY UPDATE msg = 'Two';
```

Sure enough, the “on duplicate key update” part of it is ignored, and will\
result in error if the key value is duplicated.

### UPDATE and DELETE Commands

Unlike the [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) command, [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) are supported in a simplified way. Only simple table commands are supported; CONNECT does not support multi-table commands, commands sent from a procedure, or issued via a trigger.\
These commands are just rephrased to correspond to the data source syntax and sent to the\
data source for execution. Let us suppose we created the table:

```
CREATE TABLE tolite (
  id INT(9) NOT NULL,
  nom VARCHAR(12) NOT NULL,
  nais DATE DEFAULT NULL,
  rem VARCHAR(32) DEFAULT NULL)
ENGINE=CONNECT TABLE_TYPE=ODBC tabname='lite'
CONNECTION='DSN=SQLite3 Datasource;Database=test.sqlite3'
CHARSET=utf8 DATA_CHARSET=utf8;
```

We can populate it by:

```
INSERT INTO tolite VALUES(1,'Toto',NOW(),'First'),
(2,'Foo','2012-07-14','Second'),(4,'Machin','1968-05-30','Third');
```

The function `now()` are executed by MariaDB and it returned value sent\
to the ODBC table.

Let us see what happens when updating the table. If we use the query:

```
UPDATE tolite SET nom = 'Gillespie' WHERE id = 10;
```

CONNECT will rephrase the command as:

```
UPDATE lite SET nom = 'Gillespie' WHERE id = 10;
```

What it did is just to replace the local table name with the remote table name\
and change all the back ticks to blanks or to the data source identifier quoting characters if QUOTED is specified.\
Then this command are sent to the data source to be executed by it.

This is simpler and can be faster than doing a positional update using a cursor\
and commands such as “select ... for update of ...” that are not supported by\
all data sources. However, there are some restrictions that must be understood\
due to the way it is handled by MariaDB.

1. MariaDB does not know about all the above. The command are parsed as if\
   it were to be executed locally. Therefore, it must respect the MariaDB syntax.
2. Being executed by the data source, the (rephrased) command must also respect\
   the data source syntax.
3. All data referenced in the SET and WHERE clause belongs to the data source.

This is possible because both MariaDB and the data source are using the SQL\
language. But you must use only the basic features that are part of the core\
SQL language. For instance, keywords like IGNORE or LOW\_PRIORITY will cause\
syntax error with many data source.

Scalar function names also can be different, which severely restrict the use of\
them. For instance:

```
UPDATE tolite SET nais = NOW() WHERE id = 2;
```

This will not work with SQLite3, the data source returning an “unknown scalar\
function” error message. Note that in this particular case, you can rephrase it\
to:

```
UPDATE tolite SET nais = DATE('now') WHERE id = 2;
```

This understood by both parsers, and even if this function would return NULL\
executed by MariaDB, it does return the current date when executed by SQLite3.\
But this begins to become too trickery so to overcome all these restrictions,\
and permit to have all types of commands executed by the data source, CONNECT\
provides a specific ODBC table subtype described now.

## Sending commands to a Data Source

This can be done using a special subtype of ODBC table. Let us see this in an\
example:

```
CREATE TABLE crlite (
  command VARCHAR(128) NOT NULL,
  NUMBER INT(5) NOT NULL flag=1,
  message VARCHAR(255) flag=2)
ENGINE=CONNECT table_type=odbc
CONNECTION='Driver=SQLite3 ODBC Driver;Database=test.sqlite3;NoWCHAR=yes'
option_list='Execsrc=1';
```

The key points in this create statement are the EXECSRC option and the column\
definition.

The EXECSRC option tells that this table are used to send a command to the\
data source. Most of the sent commands do not return result set. Therefore, the\
table columns are used to specify the command to be executed and to get the\
result of the execution. The name of these columns can be chosen arbitrarily,\
their function coming from the FLAG value:

|         |                                                                                                                |
| ------- | -------------------------------------------------------------------------------------------------------------- |
| Flag=0: | The command to execute.                                                                                        |
| Flag=1: | The affected rows, or -1 in case of error, or the result number of column if the command returns a result set. |
| Flag=2: | The returned (eventually error) message.                                                                       |

How to use this table and specify the command to send? By executing a command\
such as:

```
SELECT * FROM crlite WHERE command = 'a command';
```

This will send the command specified in the WHERE clause to the data source and\
return the result of its execution. The syntax of the WHERE clause must be\
exactly as shown above. For instance:

```
SELECT * FROM crlite WHERE command =
'CREATE TABLE lite (
ID integer primary key autoincrement,
name char(12) not null,
birth date,
rem varchar(32))';
```

This command returns:

| command                                                          | number | message       |
| ---------------------------------------------------------------- | ------ | ------------- |
| CREATE TABLE lite (ID integer primary key autoincrement, name... | 0      | Affected rows |

Now we can create a standard ODBC table on the newly created table:

```
CREATE TABLE tlite
ENGINE=CONNECT TABLE_TYPE=ODBC tabname='lite'
CONNECTION='Driver=SQLite3 ODBC Driver;Database=test.sqlite3;NoWCHAR=yes'
CHARSET=utf8 DATA_CHARSET=utf8;
```

We can populate it directly using the supported [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```
INSERT INTO tlite(name,birth) VALUES('Toto','2005-06-12');
INSERT INTO tlite(name,birth,rem) VALUES('Foo',NULL,'No ID');
INSERT INTO tlite(name,birth) VALUES('Truc','1998-10-27');
INSERT INTO tlite(name,birth,rem) VALUES('John','1968-05-30','Last');
```

And see the result:

```
SELECT * FROM tlite;
```

| ID | name | birth      | rem   |
| -- | ---- | ---------- | ----- |
| 1  | Toto | 2005-06-12 | NULL  |
| 2  | Foo  | NULL       | No ID |
| 3  | Truc | 1998-10-27 | NULL  |
| 4  | John | 1968-05-30 | Last  |

Any command, for instance [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md), can be executed from the _crlite_ table:

```
SELECT * FROM crlite WHERE command =
'update lite set birth = ''2012-07-14'' where ID = 2';
```

This command returns:

| command                                           | number | message       |
| ------------------------------------------------- | ------ | ------------- |
| update lite set birth = '2012-07-15' where ID = 2 | 1      | Affected rows |

Let us verify it:

```
SELECT * FROM tlite WHERE ID = 2;
```

| ID | name | birth      | rem   |
| -- | ---- | ---------- | ----- |
| 2  | Foo  | 2012-07-15 | No ID |

The syntax to send a command is rather strange and may seem unnatural. It is possible to use an easier\
syntax by defining a stored procedure such as:

```
CREATE PROCEDURE send_cmd(cmd VARCHAR(255))
MODIFIES SQL DATA
SELECT * FROM crlite WHERE command = cmd;
```

Now you can send commands like this:

```
call send_cmd('drop tlite');
```

This is possible only when sending one single command.

### Sending several commands together

Grouping commands uses an easier syntax and is faster because only one\
connection is made for the all of them. To send several commands in one call,\
use the following syntax:

```
SELECT * FROM crlite WHERE command IN (
  'update lite set birth = ''2012-07-14'' where ID = 2',
  'update lite set birth = ''2009-08-10'' where ID = 3');
```

When several commands are sent, the execution stops at the end of them or after\
a command that is in error. To continue after _n_ errors, set the option\
maxerr=_n_ (0 by default) in the option list.

**Note 1:** It is possible to specify the SRCDEF option when creating an\
EXECSRC table. It are the command sent by default when a WHERE clause is\
not specified.

**Note 2:** Most data sources do not allow sending several commands separated\
by semi-colons.

**Note 3:** Quotes inside commands must be escaped. This can be avoided by\
using a different quoting character than the one used in the command

**Note 4:** The sent command must obey the data source syntax.

**Note 5:** Sent commands apply in the specified database. However, they can\
address any table within this database, or belonging to another database using\
the name syntax _schema.tabname_.

## Connecting to a Data Source

There are two ways to establish a connection to a data source:

1. Using SQLDriverConnect and a Connection String
2. Using SQLConnect and a Data Source Name (DSN)

The first way uses a Connection String whose components describe what is needed to establish the connection. It is the most complete way to do it and by default CONNECT uses it.

The second way is a simplified way in which ODBC is just given the name of a DSN that must have been defined to ODBC or UnixOdbc and that contains the necessary information to establish the connection. Only the user name and password can be specified out of the DSN specification.

### Defining the Connection String

Using the first way, the connection string must be specified. This is sometimes the most difficult task when creating ODBC tables because, depending on the\
operating system and the data source, this string can widely differ.

The format of the ODBC Connection String is:

```
connection-string::= empty-string[;] | attribute[;] | attribute; connection-string
empty-string ::=
attribute ::= attribute-keyword=attribute-value | DRIVER=[{]attribute-value[}]
attribute-keyword ::= DSN | UID | PWD | driver-defined-attribute-keyword
attribute-value ::= character-string
driver-defined-attribute-keyword = identifier
```

Where character-string has zero or more characters; identifier has one or more\
characters; attribute- keyword is not case-sensitive; attribute-value may be\
case-sensitive; and the value of the DSN keyword does not consist solely of\
blanks. Due to the connection string grammar, keywords and attribute values\
that contain the characters `[]{}(),;?*=!@` should be avoided. The value of\
the DSN keyword cannot consist only of blanks, and should not contain leading\
blanks. Because of the grammar of the system information, keywords and data\
source names cannot contain the backslash () character. Applications do not\
have to add braces around the attribute value after the DRIVER keyword unless\
the attribute contains a semicolon (;), in which case the braces are required.\
If the attribute value that the driver receives includes the braces, the driver\
should not remove them, but they should be part of the returned connection\
string.

### ODBC Defined Connection Attributes

The ODBC defined attributes are:

* DSN - the name of the data source to connect to. You must create this before attempting to refer to it. You create new DSNs\
  through the ODBC Administrator (Windows), ODBCAdmin (unixODBC's GUI manager)\
  or in the odbc.ini file.
* DRIVER - the name of the driver to connect to. You can use this in DSN-less\
  connections.
* FILEDSN - the name of a file containing the connection attributes.
* UID/PWD - any username and password the database requires for authentication.
* SAVEFILE - request the DSN attributes are saved in this file.

Other attributes are DSN dependent attributes. The connection string can give\
the name of the driver in the DRIVER field or the data source in the DSN field\
(attention! meet the spelling and case) and has other fields that depend on the\
data source. When specifying a file, the DBQ field must give the **full** path\
and name of the file containing the table. Refer to the specific ODBC connector\
documentation for the exact syntax of the connection string.

### Using a Predefined DSN

This is done by specifying in the option list the Boolean option “UseDSN” as yes or 1. In addition, string options “user” and “password” can be optionally specified in the option list.

When doing so, the connection string just contains the name of the predefined Data Source. For instance:

```
CREATE TABLE tlite ENGINE=CONNECT TABLE_TYPE=ODBC tabname='lite'
CONNECTION='SQLite3 Datasource' 
OPTION_LIST='UseDSN=Yes,User=me,Password=mypass';
```

Note: the connection data source name (limited to 32 characters) should not be preceded by “DSN=”.

## ODBC Tables on Linux/Unix

In order to use ODBC tables, you will need to have unixODBC installed. Additionally, you will need the ODBC driver for your foreign server's protocol. For example, for MS SQL Server or Sybase, you will need to have FreeTDS installed.

Make sure the user running mysqld (usually the mysql user) has permission to the ODBC data source configuration and the ODBC drivers.\
If you get an error on Linux/Unix when using TABLE\_TYPE=ODBC:

```
Error Code: 1105 [unixODBC][Driver Manager]Can't open lib
'/usr/cachesys/bin/libcacheodbc.so' : file not found
```

You must make sure that the user running mysqld (usually "mysql") has enough\
permission to load the ODBC driver library. It can happen that the driver file\
does not have enough read privileges (use chmod to fix this), or loading is\
prevented by SELinux configuration (see below).

Try this command in a shell to check if the driver had enough permission:

```
sudo -u mysql ldd /usr/cachesys/bin/libcacheodbc.so
```

#### SELinux

SELinux can cause various problems. If you think SELinux is causing problems, check the system log (e.g. /var/log/messages) or the audit log (e.g. /var/log/audit/audit.log).

**mysqld can't load some executable code, so it can't use the ODBC driver.**

Example error:

```
Error Code: 1105 [unixODBC][Driver Manager]Can't open lib
'/usr/cachesys/bin/libcacheodbc.so' : file not found
```

Audit log:

```
type=AVC msg=audit(1384890085.406:76): avc: denied { execute }
for pid=1433 comm="mysqld"
path="/usr/cachesys/bin/libcacheodbc.so" dev=dm-0 ino=3279212
scontext=unconfined_u:system_r:mysqld_t:s0
tcontext=unconfined_u:object_r:usr_t:s0 tclass=file
```

**mysqld can't open TCP sockets on some ports, so it can't connect to the foreign server.**

Example error:

```
ERROR 1296 (HY000): Got error 174 '[unixODBC][FreeTDS][SQL Server]Unable to connect to data source' from CONNECT
```

Audit log:

```
type=AVC msg=audit(1423094175.109:433): avc:  denied  { name_connect } for  pid=3193 comm="mysqld" dest=1433 scontext=system_u:system_r:mysqld_t:s0 tcontext=system_u:object_r:mssql_port_t:s0 tclass=tcp_socket
```

## ODBC Catalog Information

Depending on the version of the used ODBC driver, some additional information\
on the tables are existing, such as table QUALIFIER or OWNER for old versions,\
now named CATALOG or SCHEMA since version 3.

CATALOG is apparently rarely used by most data sources, but SCHEMA (formerly\
OWNER) is and corresponds to the DATABASE information of MySQL.

The issue is that if no schema name is specified, some data sources return\
information for all schemas while some others only return the information of\
the “default” schema. In addition, the used “schema” or “database” is sometimes\
implied by the connection string and sometimes is not. Sometimes, it also can\
be included in a data source definition.

CONNECT offers two ways to specify this information:

1. When specified, the DBNAME create table option is regarded by ODBC tables as\
   the SCHEMA name.
2. Table names can be specified as “cat.sch.tab” allowing to set the catalog and\
   schema info.

When both are used, the qualified table name has precedence over DBNAME . For\
instance:

| Tabname | DBname | Description                                                    |
| ------- | ------ | -------------------------------------------------------------- |
| test.t1 |        | The t1 table of the test schema.                               |
| test.t1 | mydb   | The t1 table of the test schema (test has precedence)          |
| t1      | mydb   | The t1 table of the mydb schema                                |
| %.%.%   |        | All tables in all catalogs and all schemas                     |
| t1      |        | The t1 table in the default or all schema depending on the DSN |
| %.t1    |        | The t1 table in all schemas for all DSN                        |
| test.%  |        | All tables in the test schema                                  |

When creating a standard ODBC table, you should make sure only one source table\
is specified. Specifying more than one source table must be done only for\
CONNECT catalog tables (with CATFUNC=tables or columns).

In particular, when column definition is left to the Discovery feature, if tables with the same name are present in several schemas and the schema name is not specified, several columns with the same name are generated. This will make the creation fail with a not very explicit error message.

Note: With some ODBC drivers, the DBNAME option or qualified table name is useless because the\
schema implied by the connection string or the definition of the data source has priority over the\
specified DBNAME .

### Table name case

Another issue when dealing with ODBC tables is the way table and column names\
are handled regarding of the case.

For instance, Oracle follows to the SQL standard here. It converts non-quoted\
identifiers to upper case. This is correct and expected. PostgreSQL is not\
standard. It converts identifiers to lower case. MySQL/MariaDB is not\
standard. They preserve identifiers on Linux, and convert to lower case on\
Windows.

Think about that if you fail to see a table or a column on an ODBC data source.

## Non-ASCII Character Sets with Oracle

When connecting through ODBC, the MariaDB Server operates as a client to the foreign database management system. As such, it requires that you configure MariaDB as you would configure native clients for the given database server.

In the case of connecting to Oracle, when using non-ASCI character sets, you need to properly set the NLS\_LANG environment variable before starting the MariaDB Server.

For instance, to test this on Oracle, create a table that contains a series of special characters:

```
CREATE TABLE t1 (letter VARCHAR(4000));

INSERT INTO t1 VALUES
   (UTL_RAW.CAST_TO_VARCHAR2(HEXTORAW('C4'))),
   (UTL_RAW.CAST_TO_VARCHAR2(HEXTORAW('C5'))),
   (UTL_RAW.CAST_TO_VARCHAR2(HEXTORAW('C6')));

SELECT letter, RAWTOHEX(letter) FROM t1;

letter | RAWTOHEX(letter)
-------|-----------------
Ä     | C4
Å     | C5
Æ     | C6
```

Then create a connecting table on MariaDB and attempt the same query:

```
CREATE TABLE t1 (
   letter VARCHAR(4000))
ENGINE=CONNECT
DEFAULT CHARSET=utf8mb4
CONNECTION='DSN=YOUR_DSN'
TABLE_TYPE = 'ODBC'
DATA_CHARSET = latin1
TABNAME = 'YOUR_SCHEMA.T1';

SELECT letter, HEX(letter) FROM t1;

+--------+-------------+
| letter | HEX(letter) |
+--------+-------------+
| A      | 	    41 |
| ?      | 	    3F |
| ?      | 	    3F |
+--------+-------------+
```

While the character set is defined in a way that satisfies MariaDB, it has not been defined for Oracle, (that is, setting the NLS\_LANG environment variable). As a result, Oracle is not providing the characters you want to MariaDB and Connect.\
The specific method of setting the NLS\_LANG variable can vary depending on your operating system or distribution. If you're experiencing this issue, check your OS documentation for more details on how to properly set environment variables.

### Using systemd

With Linux distributions that use [systemd](../../../../server-management/starting-and-stopping-mariadb/systemd.md), you need to set the environment variable in the service file, (systemd doesn't read from the /etc/environment file).

This is done by setting the Environment variable in the \[Service] unit. For instance,

```
# systemctl edit mariadb.service

[Service]
Environment=NLS_LANG=GERMAN_GERMANY.WE8ISO8859P1
```

Then restart MariaDB,

```
# systemctl restart mariadb.service
```

You can now retrieve the appropriate characters from Oracle tables:

```
SELECT letter, HEX(letter) FROM t1;

+--------+-------------+
| letter | HEX(letter) |
+--------+-------------+
| Ä      | C384        |
| Å      | C385        |
| Æ      | C386        |
+--------+-------------+
```

### Using Windows

Microsoft Windows doesn't ignore environment variables the way systemd does on Linux, but it does require that you set the NLS\_LANG environment variable on your system. In order to do so, you need to open an elevated command-prompt, (that is, Cmd.exe with administrative privileges).

From here, you can use the Setx command to set the variable. For instance,

```
Setx NLS_LANG GERMAN_GERMANY.WE8ISO8859P1 /m
```

Note: For more detail about this, see [MDEV-17501](https://jira.mariadb.org/browse/MDEV-17501).

## `OPTION_LIST` Values Supported by the ODBC Tables

The following options can be given as comma-separated string to the `OPTION_LIST` value in the `CREATE TABLE` statement.

| Name           | Default | Description                                          |
| -------------- | ------- | ---------------------------------------------------- |
| MaxRes         | 0       | Maximum number of rows returned by catalog functions |
| ConnectTimeout | -1      | Connection timeout in seconds, unlimited by default  |
| QueryTimeout   | -1      | Query timeout in seconds, unlimited by default       |
| UseDSN         | false   | Use pre-configured DSN                               |

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
