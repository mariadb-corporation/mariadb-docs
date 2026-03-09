---
description: The CONNECT storage engine.
---

# CONNECT Table Types - Data Files

Most of the tables processed by CONNECT are just plain DOS or UNIX data files, logically regarded as tables thanks to the description given when creating the table. This description comes from the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement. Depending on the application, these tables can already exist as data files, used as is by CONNECT, or can have been physically made by CONNECT as the result of a `CREATE TABLE ... SELECT ...` and/or INSERT statement(s).

The file _path/name_ is given by the `FILE_NAME` option. If it is a relative path/name, it are relative to the database directory, the one containing the table `.FRM` file.

Unless specified, the maturity of file table types is stable.

## Multiple File Tables

A **multiple** file table is one that is physically contained in several files of the same type instead of just one. These files are processed sequentially during the process of a query and the result is the same as if all the table files were merged into one. This is great to process files coming from different sources (such as cash register log files) or made at different time periods (such as bank monthly reports) regarded as one table. Note that the operations on such files are restricted to sequential Select and Update; and that VEC multiple tables are not supported by CONNECT. The file list depends on the setting of the **multiple** option of the `CREATE TABLE` statement for that table.

Multiple tables are specified by the option MULTIPLE=_n_, which can take This storage engine has been deprecated.four values:

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Not a multiple table (the default). This can be used in an [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.   |
| 1 | The table is made from files located in the same directory. The FILE\_NAME option is a pattern such as 'cash\*.log' that all the table file path/names verify. |
| 2 | The FILE\_NAME gives the name of a file that contains the path/names of all the table files. This file can be made using a DIR table.                          |
| 3 | Like multiple=1 but also including eligible files from the directory sub-folders.                                                                              |

The `FILEID` special column, described [here](../using-connect/using-connect-virtual-and-special-columns.md), allows query pruning by filtering the file list or doing some grouping on the files that make a multiple table.

**Note:** Multiple was not initially implemented for XML tables. This restriction was removed in version 1.02.

## Record Format

This characteristic applies to table files handled by the operating system input/output functions. It is **fixed** for table types [FIX](connect-dos-and-fix-table-types.md), [BIN](connect-bin-table-type.md), [DBF](connect-dbf-table-type.md) and [VEC](connect-vec-table-type.md), and it is variable for [DOS](connect-dos-and-fix-table-types.md), VCT, [FMT](connect-csv-and-fmt-table-types.md) and some [JSON](connect-json-table-type.md) tables.

For fixed tables, most I/O operations are done by block of BLOCK\_SIZE rows. This diminishes the number of I/O’s and enables block indexing.

Starting with CONNECT version 1.6.6, the BLOCK\_SIZE option can also be specified for variable tables. Then, a file similar to the block indexing file is created by CONNECT that gives the size in bytes of each block of BLOCK\_SIZE rows. This enables the use of block I/Os and block indexing to variable tables. It also enables CONNECT to return the exact row number for info commands

## File Mapping

For file-based tables of reasonable size, processing time can be greatly enhanced under Windows(TM) and some flavors of UNIX or Linux by using the technique of “file mapping”, in which a file is processed as if it were entirely in memory. Mapping is specified when creating the table by the use of the `MAPPED=YES` option. This does not apply to tables not handled by system I/O functions ([XML](connect-xml-table-type.md) and [INI](connect-ini-table-type.md)).

## Big File Tables

Because all files are handled by the standard input/output functions of the operating system, their size is limited to 2GB, the maximum size handled by standard functions. For some table types, CONNECT can deal with files that are larger than 2GB, or prone to become larger than this limit. These are the [FIX](connect-dos-and-fix-table-types.md),[BIN](connect-bin-table-type.md) and [VEC](connect-vec-table-type.md) types. To tell connect to use input/output functions dealing with big files, specify the option `huge=1` or `huge=YES` for that table. Note however that CONNECT cannot randomly access tables having more than 2G records.

## Compressed File Tables

CONNECT can make and process some tables whose data file is compressed. The only supported compression format is the gzlib format. Zip and zlib formats are supported differently. The table types that can be compressed are [DOS](connect-dos-and-fix-table-types.md),[FIX](connect-dos-and-fix-table-types.md),[BIN](connect-bin-table-type.md),[CSV](connect-csv-and-fmt-table-types.md) and [FMT](connect-csv-and-fmt-table-types.md). This can save some disk space\
at the cost of a somewhat longer processing time.

Some restrictions apply to compressed tables:

* Compressed tables are not indexable.
* Update and partial delete are not supported.

Use the numeric compress option to specify a compressed table:

1. Not compressed
2. Compressed in gzlib format.
3. Made of compressed blocks of block\_size records (enabling block indexing)

## Relational Formatted Tables

These are based on files whose records represent one table row. Only the column representation within each record can differ. The following relational formatted tables are supported:

* [DOS and FIX Table Types](connect-dos-and-fix-table-types.md)
* [DBF Table Type](connect-dbf-table-type.md)
* [BIN Table Type](connect-bin-table-type.md)
* [VEC Table Type](connect-vec-table-type.md)
* [CSV and FMT Table Types](connect-csv-and-fmt-table-types.md)

## NoSQL Table Types

These are based on files that do not match the relational format but often represent hierarchical data. CONNECT can handle JSON, INI-CFG, XML and some HTML files..

The way it is done is different from what PostgreSQL does. In addition to including in a table some column values of a specific data format (JSON, XML) to be handled by specific functions, CONNECT can directly use JSON, XML or INI files that can be produced by other applications and this is the table definition that describes where and how the contained information must be retrieved.

This is also different from what MariaDB does with [dynamic columns](../../../../reference/sql-structure/nosql/dynamic-columns.md), which is close to what MySQL and PostgreSQL do with the JSON column type.

The following NoSQL types are supported:

* [XML Table Type](connect-xml-table-type.md)
* [JSON Table Type](connect-json-table-type.md)
* [INI Table Type](connect-ini-table-type.md)

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
