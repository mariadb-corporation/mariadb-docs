---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT VEC Table Type

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Warning: Avoid using this table type in production applications. This file format is specific to CONNECT and may not be supported in future versions.

Tables of type `VEC` are binary files that in some cases can provide good performance on read-intensive query workloads. CONNECT organizes their data on disk as columns of values from the same attribute, as opposed to storing it as rows of tabular records. This organization means that when a query needs to\
access only a few columns of a particular table, only those columns need to be read from disk. Conversely, in a row-oriented table, all values in a table are typically read from disk, wasting I/O bandwidth.

CONNECT provides two integral VEC formats, in which each column's data is adjacent.

## Integral vector formats

In these true vertical formats, the VEC files are made of all the data of the first column, followed by all the data of the second column etc. All this can be in one physical file or each column data can be in a separate file. In the first case, the option max\_rows=m, where m is the estimate of the maximum size (number of rows) of the table, must be specified to be able to insert some new records. This leaves an empty space after each column area in which new data can be inserted. In the second case, the “Split” option can be specified\[[2](connect-vec-table-type.md#_note-1)] at table creation and each column are stored in a file named sequentially from the table file name followed by the rank of the column. Inserting new lines can freely augment such a table.

## Differences between vector formats

These formats correspond to different needs. The integral vector format provides the best performance gain. It are chosen when the speed of decisional queries must be optimized.

In the case of a unique file, inserting new data are limited but there will be only one open and close to do. However, the size of the table cannot be calculated from the file size because of the eventual unused space in the file. It must be kept in a header containing the maximum number of rows and the current number of valid rows in the table. To achieve this, specify the option Header=_n_ when creating the table. If `n=1` the header are placed at the beginning of the file, if `n=2` it are a separate file with the type ‘.blk’, and if `n=3` the header are place at the end of the file. This last value is provided because batch inserting is sometimes slower when the header is at the beginning of the file. If not specified, the header option\
will default to 2 for this table type.

On the other hand, the "Split" format with separate files have none of these issues, and is a much safer solution when the table must frequently inserted or shared among several users.

For instance:

```sql
CREATE TABLE vtab (
a INT NOT NULL,
b CHAR(10) NOT NULL)
ENGINE=CONNECT table_type=VEC file_name='vt.vec';
```

This table, split by default, will have the column values in files vt1.vec and vt2.vec.

For vector tables, the option _block\_size=n_ is used for block reading and writing; however, to have a file made of blocks of equal size, the internal value of the _max\_rows=m_ option is eventually increased to become a multiple of n.

Like for BIN tables, numeric values are stored using platform internal layout, the correspondence between column types and internal format being the same than the default ones given above for BIN. However, field formats are not available for VEC tables.

## Header option

This applies to VEC tables that are not split. Because the file size depends on the MAX\_ROWS value, CONNECT cannot know how many valid records exist in the file. Depending on the value of the HEADER option, this information is stored in a header that can be placed at the beginning of the file, at the end of the file or in a separate file called fn.blk. The valid values for the HEADER option are:

|   |                                                               |
| - | ------------------------------------------------------------- |
| 0 | Defaults to 2 for standard tables and to 3 for inward tables. |
| 1 | The header is at the beginning of the file.                   |
| 2 | The header is in a separate file.                             |
| 3 | The header is at the end of the file.                         |

The value 2 can be used when dealing with files created by another application\
with no header. The value 3 makes sometimes inserting in the file faster than\
when the header is at the beginning of the file.

Note: VEC being a file format specific to CONNECT, no big endian / little endian conversion is provided. These files are not portable between machines using a different byte order setting.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
