---
description: The CONNECT storage engine.
---

# CONNECT Table Types - Special "Virtual" Tables

The special table types supported by CONNECT are the Virtual table type ([VIR](connect-table-types-vir.md) - introduced in [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15)), Directory Listing table type (DIR), the Windows Management Instrumentation Table Type (WMI), and the “Mac Address” type (MAC).

These tables are “virtual tables”, meaning they have no physical data but rather produce result data using specific algorithms. Note that this is close to what Views are, so they could be regarded as special views.

## DIR Type

A table of type DIR returns a list of file name and description as a result set. To create a DIR table, use a Create Table statement such as:

```sql
CREATE TABLE SOURCE (
  DRIVE CHAR(2) NOT NULL,
  PATH VARCHAR(256) NOT NULL,
  FNAME VARCHAR(256) NOT NULL,
  FTYPE CHAR(4) NOT NULL,
  SIZE DOUBLE(12,0) NOT NULL flag=5,
  MODIFIED DATETIME NOT NULL)
ENGINE=CONNECT table_type=DIR file_name='..\\*.cc';
```

When used in a query, the table returns the same file information listing than the system "DIR `*.cc`" statement would return if executed in the same current directory (here supposedly ..)

For instance, the query:

```sql
SELECT fname, SIZE, modified FROM SOURCE
  WHERE fname like '%handler%';
```

Displays:

| fname        | size   | modified            |
| ------------ | ------ | ------------------- |
| handler      | 152177 | 2011-06-13 18:08:29 |
| sql\_handler | 25321  | 2011-06-13 18:08:31 |

**Note:** the important item in this table is the flag option value (set sequentially from 0 by default) because it determines which particular information item is returned in the column:

| Flag value | Information                |
| ---------- | -------------------------- |
| 0          | The disk drive (Windows)   |
| 1          | The file path              |
| 2          | The file name              |
| 3          | The file type              |
| 4          | The file attribute         |
| 5          | The file size              |
| 6          | The last write access date |
| 7          | The last read access date  |
| 8          | The file creation date     |

### The Subdir option

When specified in the create table statement, the subdir option indicates to list, in addition to the files contained in the specified directory, all the files verifying the filename pattern that are contained in sub-directories of the specified directory. For instance, using:

```
CREATE TABLE DATA (
  PATH VARCHAR(256) NOT NULL flag=1,
  FNAME VARCHAR(256) NOT NULL,
  FTYPE CHAR(4) NOT NULL,
  SIZE DOUBLE(12,0) NOT NULL flag=5)
ENGINE=CONNECT table_type=DIR file_name='*.frm'
option_list='subdir=1';

SELECT PATH, COUNT(*), SUM(SIZE) FROM DATA GROUP BY PATH;
```

You will get the following result set showing how many tables are created in the MariaDB databases and what is the total length of the FRM files:

| path                                           | count(\*) | sum(size) |
| ---------------------------------------------- | --------- | --------- |
| \CommonSource\mariadb-5.2.7\sql\data\connect\\ | 30        | 264469    |
| \CommonSource\mariadb-5.2.7\sql\data\mysql\\   | 23        | 207168    |
| \CommonSource\mariadb-5.2.7\sql\data\test\\    | 22        | 196882    |

### The Nodir option (Windows)

The Boolean Nodir option can be set to false (0 or no) to add directories that match the file name pattern from the listed files (it is true by default). This is an addition to CONNECT version 1.6. Previously, directory names matching pattern were listed on Windows. Directories were and are never listed on Linux.

Note: The way file names are retrieved makes positional access to them impossible. Therefore, DIR tables cannot be indexed or sorted when it is done using positions.

Be aware, in particular when using the subdir option, that queries on DIR tables are slow and can last almost forever if made on a directory that contains a great number of files in it and its sub-directories.

dir tables can be used to populate a list of files used to create a multiple=2 table. However, this is not as useful as it was when the multiple 3 did not exist.

## Windows Management Instrumentation Table Type “WMI”

**Note:** This table type is available on Windows only.

WMI provides an operating system interface through which instrumented components provide information. Some Microsoft tools to retrieve information through WMI are the WMIC console command and the WMI CMI Studio application.

The CONNECT WMI table type enables administrators and operators not capable of scripting or programming on top of WMI to enjoy the benefit of WMI without even learning about it. It permits to present this information as tables that can be queried, transformed, copied in documents or other tables.

To create a WMI table displaying information coming from a WMI provider, you must provide the namespace and the class name that characterize the information you want to retrieve. The best way to find them is to use the WMI CIM Studio that have tools to browse namespaces and classes and that can display the names of the properties of that class.

The column names of the tables must be the names (case insensitive) of the properties you want to retrieve. For instance:

```
CREATE TABLE ALIAS (
  friendlyname CHAR(32) NOT NULL,
  target CHAR(50) NOT NULL)
ENGINE=CONNECT table_type='WMI'
option_list='Namespace=root\\cli,Class=Msft_CliAlias';
```

WMI tables returns one row for each instance of the related information. The above example is handy to get the class equivalent of the alias of the WMIC command and also to have a list of many classes commonly used.

Because most of the useful classes belong to the 'root\cimv2' namespace, this is the default value for WMI tables when the namespace is not specified. Some classes have many properties whose name and type may not be known when creating the table. To find them, you can use the WMI CMI Studio application but his are rarely required because CONNECT is able to retrieve them.

Actually, the class specification also has default values for some namespaces. For the ‘root\cli’ namespace the class name defaults to ‘Msft\_CliAlias’ and for the ‘root\_cimv2’ namespace the class default value is ‘Win32\_ComputerSystemProduct’. Because many class names begin with ‘Win32\_’ it\
is not necessary to say it and specifying the class as ‘Product’ will effectively use class  'Win32\_Product’.

For example if you define a table as:

```
CREATE TABLE CSPROD ENGINE=CONNECT table_type='WMI';
```

It will return the information on the current machine, using the class\
ComputerSystemProduct of the CIMV2 namespace. For instance:

```
SELECT * FROM csprod;
```

Will return a result such as:

| Column            | Row 1                                |
| ----------------- | ------------------------------------ |
| Caption           | Computer system product              |
| Description       | Computer system product              |
| IdentifyingNumber | LXAP50X32982327A922300               |
| Name              | Aspire 8920                          |
| SKUNumber         |                                      |
| UUID              | 00FC523D-B8F7-DC12-A70E-00B0D1A46136 |
| Vendor            | Acer                                 |
| Version           | Aspire 8920                          |

**Note:** This is a transposed display that can be obtained with some GUI.

### Getting Column Information

An issue, when creating a WMI table, is to make its column definition. Indeed, even when you know the namespace and the class for the wanted information, it is not easy to find what are the names and types of its properties. However, because CONNECT can retrieve this information from the WMI provider, you can simply omit defining columns and CONNECT will do the job.

Alternatively, you can get this information using a catalog table (see below).

### Performance Consideration

Some WMI providers can be very slow to answer. This is not an issue for those that return few object instances, such as the ones returning computer, motherboard, or Bios information. They generally return only one row (instance). However, some can return many rows, in particular the "CIM\_DataFile" class. This is why care must be taken about them.

Firstly, it is possible to limit the allocated result size by using the ‘Estimate’ create table option. To avoid result truncation, CONNECT allocates a result of 100 rows that is enough for almost all tables.The 'Estimate' option permits to reduce this size for all classes that return only a few rows, and in some rare case to increase it to avoid truncation.

However, it is not possible to limit the time taken by some WMI providers to answer, in particular the CIM\_DATAFILE class. Indeed the Microsoft documentation says about it:

"Avoid enumerating or querying for all instances of CIM\_DataFile on a computer because the volume of data is likely to either affect performance or cause the computer to stop responding."

Sure enough, even a simple query such as:

```
SELECT COUNT(*) FROM cim WHERE drive = 'D:' AND PATH like '\\MariaDB\\%';
```

is prone to last almost forever (probably due to the LIKE clause). This is why, when not asking for some specific items, you should consider using the DIR table type instead.

### Syntax of WMI queries

Queries to WMI providers are done using the WQL language, not the SQL language. CONNECT does the job of making the WQL query. However, because of the restriction of the WQL syntax, the WHERE clause are generated only when respecting the following restrictions:

1. No function.
2. No comparison between two columns.
3. No expression (currently a CONNECT restriction)
4. No BETWEEN and IN predicates.

Filtering with WHERE clauses not respecting these conditions will still be done by MariaDB only,\
except in the case of CIM\_Datafile class for the reason given above.

However, there is one point that is not covered yet, the syntax used to specify dates in queries. WQL does not recognize dates as number items but translates them to its internal format dates specified as text. Many formats are recognized as described in the Microsoft documentation but only one is useful because common to WQL and MariaDB SQL. Here is an example of a query on a table named "cim" created by:

```
CREATE TABLE cim (
  Name VARCHAR(255) NOT NULL,
  LastModified DATETIME NOT NULL)
ENGINE=CONNECT table_type='WMI'
option_list='class=CIM_DataFile,estimate=5000';
```

The date must be specified with the format in which CIM DATETIME values are stored (WMI uses the date and time formats defined by the Distributed Management Task Force).

```
SELECT * FROM cim WHERE drive = 'D:' AND PATH = '\\PlugDB\\Bin\\'
     and lastmodified > '20120415000000.000000+120';
```

This syntax must be strictly respected. The text has the format:

```
yyyymmddHHMMSS.mmmmmmsUUU
```

It is: year, month, day, hour, minute, second, millisecond, and signed minute deviation from [UTC](../../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md). This format is locale-independent so you can write a query that runs on any machine.

**Note 1:** The WMI table type is available only in Windows versions of CONNECT.

**Note 2:** WMI tables are read only.

**Note 3:** WMI tables are not indexable.

**Note 4:** WMI consider all strings as case insensitive.

## MAC Address Table Type “MAC”

**Note:** This table type is available on Windows only.

This type is used to display various general information about the computer and, in particular, about its network cards. To create such a table, the syntax to use is:

```
CREATE TABLE tabname (COLUMN definition)
ENGINE=CONNECT table_type=MAC;
```

Column names can be freely chosen because their signification, i.e. the values they will display, comes from the specified Flag option. The valid values for Flag are:

| Flag | Valeur         | Type         |
| ---- | -------------- | ------------ |
| 1    | Host name      | varchar(132) |
| 2    | Domain         | varchar(132) |
| 3    | DNS address    | varchar(24)  |
| 4    | Node type      | int(1)       |
| 5    | Scope ID       | varchar(256) |
| 6    | Routing        | int(1)       |
| 7    | Proxy          | int(1)       |
| 8    | DNS            | int(1)       |
| 10   | Name           | varchar(260) |
| 11   | Description    | varchar(132) |
| 12   | MAC address    | char(24)     |
| 13   | Type           | int(3)       |
| 14   | DHCP           | int(1)       |
| 15   | IP address     | char(16)     |
| 16   | SUBNET mask    | char(16)     |
| 17   | GATEWAY        | char(16)     |
| 18   | DHCP server    | char(16)     |
| 19   | Have WINS      | int(1)       |
| 20   | Primary WINS   | char(16)     |
| 21   | Secondary WINS | char(16)     |
| 22   | Lease obtained | datetime     |
| 23   | Lease expires  | datetime     |

**Note:** The information of columns having a Flag value less than 10 are unique for the computer, the other ones are specific to the network cards of the computer.

For instance, you can define the table _macaddr_ as:

```
CREATE TABLE MACADDR (
  Host VARCHAR(132) flag=1,
  Card VARCHAR(132) flag=11,
  Address CHAR(24) flag=12,
  IP CHAR(16) flag=15,
  Gateway CHAR(16) flag=17,
  Lease DATETIME flag=23)
ENGINE=CONNECT table_type=MAC;
```

If you execute the query:

```
SELECT host, address, ip, gateway, lease FROM MACADDR;
```

It will return, for example:

| Host    | Address           | IP           | Gateway       | Lease               |
| ------- | ----------------- | ------------ | ------------- | ------------------- |
| OLIVIER | 00-A0-D1-A4-61-36 | 0.0.0.0      | 0.0.0.0       | 1970-01-01 00:00:00 |
| OLIVIER | 00-1D-E0-9B-90-0B | 192.168.0.10 | 192.168.0.254 | 2011-09-18 10:28:5  |

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
