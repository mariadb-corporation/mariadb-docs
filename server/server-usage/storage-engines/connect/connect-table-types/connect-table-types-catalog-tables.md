---
description: The CONNECT storage engine.
---

# CONNECT Table Types - Catalog Tables

A catalog table is one that returns information about another table, or data source. It is similar to what MariaDB commands such as `DESCRIBE` or `SHOW` do. Applied to local tables, this just duplicates what these commands do, with the noticeable difference that they are tables and can be used inside queries as joined tables or inside sub-selects.

But their main interest is to enable querying the structure of external tables that cannot be directly queried with description commands. Let's see an example:

Suppose we want to access the tables from a Microsoft Access database as an ODBC type table. The first information we must obtain is the list of tables existing in this data source. To get it, we will create a catalog table that will return it extracted from the result set of the SQLTables ODBC function:

```sql
CREATE TABLE tabinfo (
  table_name VARCHAR(128) NOT NULL,
  table_type VARCHAR(16) NOT NULL)
ENGINE=CONNECT table_type=ODBC catfunc=TABLES
CONNECTION='DSN=MS Access Database;DBQ=C:/Program
Files/Microsoft Office/Office/1033/FPNWIND.MDB;';
```

The SQLTables function returns a result set having the following columns:

| Field       | Data Type | Null | Info Type  | Flag Value |
| ----------- | --------- | ---- | ---------- | ---------- |
| Table\_Cat  | char(128) | NO   | FLD\_CAT   | 17         |
| Table\_Name | char(128) | NO   | FLD\_SCHEM | 18         |
| Table\_Name | char(128) | NO   | FLD\_NAME  | 1          |
| Table\_Type | char(16)  | NO   | FLD\_TYPE  | 2          |
| Remark      | char(128) | NO   | FLD\_REM   | 5          |

**Note:** The Info Type and Flag Value are CONNECT interpretations of this result.

Here we could have omitted the column definitions of the catalog table or, as in the above example, chose the columns returning the name and type of the tables. If specified, the columns must have the exact name of the corresponding SQLTables result set, or be given a different name with the matching flag value specification.

(The Table\_Type can be TABLE, SYSTEM TABLE, VIEW, etc.)

For instance, to get the tables we want to use we can ask:

```
SELECT TABLE_NAME FROM tabinfo WHERE table_type = 'TABLE';
```

This will return:

| table\_name |
| ----------- |
| Categories  |
| Customers   |
| Employees   |
| Products    |
| Shippers    |
| Suppliers   |

Now we want to create the table to access the CUSTOMERS table. Because CONNECT can retrieve the column description of ODBC tables, it not necessary to specify them in the create table statement:

```sql
CREATE TABLE Customers ENGINE=CONNECT table_type=ODBC
CONNECTION='DSN=MS Access Database;DBQ=C:/Program
Files/Microsoft Office/Office/1033/FPNWIND.MDB;';
```

However, if we prefer to specify them (to eventually modify them) we must know what the column definitions of that table are. We can get this information with a catalog table. This is how to do it:

```sql
CREATE TABLE custinfo ENGINE=CONNECT table_type=ODBC
tabname=customers catfunc=columns
CONNECTION='DSN=MS Access Database;DBQ=C:/Program
Files/Microsoft Office/Office/1033/FPNWIND.MDB;';
```

Alternatively it is possible to specify what columns of the catalog table we want:

```sql
CREATE TABLE custinfo (
  column_name CHAR(128) NOT NULL,
  type_name CHAR(20) NOT NULL,
  LENGTH INT(10) NOT NULL flag=7,
  prec SMALLINT(6) NOT NULL flag=9)
  NULLABLE SMALLINT(6) NOT NULL)
ENGINE=CONNECT table_type=ODBC tabname=customers
catfunc=columns
CONNECTION='DSN=MS Access Database;DBQ=C:/Program
Files/Microsoft Office/Office/1033/FPNWIND.MDB;';
```

To get the column info:

```
SELECT * FROM custinfo;
```

which results in this table:

| column\_name | type\_name | length | prec | nullable |
| ------------ | ---------- | ------ | ---- | -------- |
| CustomerID   | VARCHAR    | 5      | 0    | 1        |
| CompanyName  | VARCHAR    | 40     | 0    | 1        |
| ContactName  | VARCHAR    | 30     | 0    | 1        |
| ContactTitle | VARCHAR    | 30     | 0    | 1        |
| Address      | VARCHAR    | 60     | 0    | 1        |
| City         | VARCHAR    | 15     | 0    | 1        |
| Region       | VARCHAR    | 15     | 0    | 1        |
| PostalCode   | VARCHAR    | 10     | 0    | 1        |
| Country      | VARCHAR    | 15     | 0    | 1        |
| Phone        | VARCHAR    | 24     | 0    | 1        |
| Fax          | VARCHAR    | 24     | 0    | 1        |

Now you can create the CUSTOMERS table as:

```sql
CREATE TABLE Customers (
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
CONNECTION='DSN=MS Access Database;DBQ=C:/Program
Files/Microsoft Office/Office/1033/FPNWIND.MDB;';
```

Let us explain what we did here: First of all, the creation of the catalog\
table. This table returns the result set of an ODBC SQLColumns function sent to\
the ODBC data source. Columns functions always return a data set having some of\
the following columns, depending on the table type:

| Field             | Data Type    | Null | Info Type     | Flag Value | Returned by       |
| ----------------- | ------------ | ---- | ------------- | ---------- | ----------------- |
| Table\_Cat\*      | char(128)    | NO   | FLD\_CAT      | 17         | ODBC, JDBC        |
| Table\_Schema\*   | char(128)    | NO   | FLD\_SCEM     | 18         | ODBC, JDBC        |
| Table\_Name       | char(128)    | NO   | FLD\_TABNAME  | 19         | ODBC, JDBC        |
| Column\_Name      | char(128)    | NO   | FLD\_NAME     | 1          | ALL               |
| Data\_Type        | smallint(6)  | NO   | FLD\_TYPE     | 2          | ALL               |
| Type\_Name        | char(30)     | NO   | FLD\_TYPENAME | 3          | ALL               |
| Column\_Size\*    | int(10)      | NO   | FLD\_PREC     | 4          | ALL               |
| Buffer\_Length\*  | int(10)      | NO   | FLD\_LENGTH   | 5          | ALL               |
| Decimal\_Digits\* | smallint(6)  | NO   | FLD\_SCALE    | 6          | ALL               |
| Radix             | smallint(6)  | NO   | FLD\_RADIX    | 7          | ODBC, JDBC, MYSQL |
| Nullable          | smallint(6)  | NO   | FLD\_NULL     | 8          | ODBC, JDBC, MYSQL |
| Remarks           | char(255)    | NO   | FLD\_REM      | 9          | ODBC, JDBC, MYSQL |
| Collation         | char(32)     | NO   | FLD\_CHARSET  | 10         | MYSQL             |
| Key               | char(4)      | NO   | FLD\_KEY      | 11         | MYSQL             |
| Default\_value    | N.A.         |      | FLD\_DEFAULT  | 12         |                   |
| Privilege         | N.A.         |      | FLD\_PRIV     | 13         |                   |
| Date\_fmt         | char(32)     | NO   | FLD\_DATEFMT  | 15         | MYSQL             |
| Xpath/Jpath       | Varchar(256) | NO   | FLD\_FORMAT   | 16         | XML/JSON          |

'\*': These names have changed since earlier versions of CONNECT.

**Note:** ALL includes the ODBC, JDBC, MYSQL, DBF, CSV, PROXY, TBL, XML, JSON, XCOL, and WMI table types. More could be added later.

We chose among these columns the ones that were useful for our create\
statement, using the flag value when we gave them a different name (case\
insensitive).

The options used in this definition are the same as the one used later for\
the actual CUSTOMERS data tables except that:

1. The `TABNAME` option is mandatory here to specify what the queried table\
   name is.
2. The `CATFUNC` option was added both to indicate that this is a catalog\
   table, and to specify that we want column information.

**Note:** If the `TABNAME` option had not been specified, this table would\
have returned the columns of all the tables defined in the connected data\
source.

Currently the available `CATFUNC` are:

| Function    | Specified as:                | Applies to table types:                            |
| ----------- | ---------------------------- | -------------------------------------------------- |
| FNC\_TAB    | tables                       | ODBC, JDBC, MYSQL                                  |
| FNC\_COL    | columns                      | ODBC, JDBC, MYSQL, DBF, CSV, PROXY, XCOL, TBL, WMI |
| FNC\_DSN    | datasourcesdsnsqldatasources | ODBC                                               |
| FNC\_DRIVER | driverssqldrivers            | ODBC, JDBC                                         |

**Note:** Only the bold part of the function name specification is required.

The `DATASOURCE` and `DRIVERS` functions respectively return the list of available data sources and ODBC drivers available on the system.

The SQLDataSources function returns a result set having the following columns:

| Field       | Data Type    | Null | Info Type | Flag value |
| ----------- | ------------ | ---- | --------- | ---------- |
| Name        | varchar(256) | NO   | FLD\_NAME | 1          |
| Description | varchar(256) | NO   | FLD\_REM  | 9          |

To get the data source, you can do for instance:

```
CREATE TABLE datasources (
ENGINE=CONNECT table_type=ODBC catfunc=DSN;
```

The SQLDrivers function returns a result set having the following columns:

| Field       | Type         | Null | Info Type | Flag value |
| ----------- | ------------ | ---- | --------- | ---------- |
| Description | varchar(128) | YES  | FLD\_NAME | 1          |
| Attributes  | varchar(256) | YES  | FLD\_REM  | 9          |

You can get the driver list with:

```sql
CREATE TABLE drivers
ENGINE=CONNECT table_type=ODBC catfunc=drivers;
```

### Another Example, WMI table

To create a catalog table returning the attribute names of a WMI class, use the same table options as the ones used with the normal WMI table plus the additional option ‘catfunc=columns’. If specified, the columns of such a catalog table can be chosen among the following:

| Name           | Type | Flag | Description                    |
| -------------- | ---- | ---- | ------------------------------ |
| Column\_Name   | CHAR | 1    | The name of the property       |
| Data\_Type     | INT  | 2    | The SQL data type              |
| Type\_Name     | CHAR | 3    | The SQL type name              |
| Column\_Size   | INT  | 4    | The field length in characters |
| Buffer\_Length | INT  | 5    | Depends on the coding          |
| Scale          | INT  | 6    | Depends on the type            |

If you wish to use a different name for a column, set the Flag column option.

For example, before creating the "csprod" table, you could have created the info table:

```sql
CREATE TABLE CSPRODCOL (
  Column_name CHAR(64) NOT NULL,
  Data_Type INT(3) NOT NULL,
  Type_name CHAR(16) NOT NULL,
  LENGTH INT(6) NOT NULL,
  Prec INT(2) NOT NULL flag=6)
ENGINE=CONNECT table_type='WMI' catfunc=col;
```

Now the query:

```sql
SELECT * FROM csprodcol;
```

will display the result:

| Column\_name      | Data\_Type | Type\_name | Length | Prec |
| ----------------- | ---------- | ---------- | ------ | ---- |
| Caption           | 1          | CHAR       | 255    | 1    |
| Description       | 1          | CHAR       | 255    | 1    |
| IdentifyingNumber | 1          | CHAR       | 255    | 1    |
| Name              | 1          | CHAR       | 255    | 1    |
| SKUNumber         | 1          | CHAR       | 255    | 1    |
| UUID              | 1          | CHAR       | 255    | 1    |
| Vendor            | 1          | CHAR       | 255    | 1    |
| Version           | 1          | CHAR       | 255    | 1    |

This can help to define the columns of the matching normal table.

**Note 1:** The column length, for the Info table as well as for the normal table, can be chosen arbitrarily, it just must be enough to contain the returned information.

**Note 2:** The Scale column returns 1 for text columns (meaning case insensitive); 2 for float and double columns; and 0 for other numeric columns.

### Catalog Table result size limit

Because catalog tables are processed like the information retrieved by “Discovery” when table columns are not specified in a Create Table statement, their result set is entirely retrieved and memory allocated.

By default, this allocation is done for a maximum return line number of:

| Catfunc      | Max lines |
| ------------ | --------- |
| Drivers      | 256       |
| Data Sources | 512       |
| Columns      | 20,000    |
| Tables       | 10,000    |

When the number of lines retrieved for a table is more than this maximum, a warning is issued by CONNECT. This is mainly prone to occur with columns (and also tables) with some data sources having many tables when the table name is not specified.

If this happens, it is possible to increase the default limit using the MAXRES option, for instance:

```sql
CREATE TABLE allcols ENGINE=CONNECT table_type=odbc
CONNECTION='DSN=ORACLE_TEST;UID=system;PWD=manager'
option_list='Maxres=110000' catfunc=columns;
```

Indeed, because the entire table result is memorized before the query is executed; the returned value would be limited even on a query such as:

```sql
SELECT COUNT(*) FROM allcols;
```

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
