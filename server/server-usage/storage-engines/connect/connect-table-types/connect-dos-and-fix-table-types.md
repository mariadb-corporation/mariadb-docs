---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT DOS and FIX Table Types

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

## Overview

Tables of type DOS and FIX are based on text files (see [CONNECT Table Types - Data Files](connect-table-types-data-files.md)). Within a record, column fields are positioned at a fixed offset from\
the beginning of the record. Except sometimes for the last field, column fields\
are also of fixed length. If the last field has varying length, the type of the\
table is DOS. For instance, having the file _dept.dat_ formatted like:

```
0318 KINGSTON       70012 SALES       Bank/Insurance
0021 ARMONK         87777 CHQ         Corporate headquarter
0319 HARRISON       40567 SALES       Federal Administration
2452 POUGHKEEPSIE   31416 DEVELOPMENT Research & development
```

You can define a table based on it with:

```
CREATE TABLE department (
  NUMBER CHAR(4) NOT NULL,
  LOCATION CHAR(15) NOT NULL flag=5,
  director CHAR(5) NOT NULL flag=20,
  FUNCTION CHAR(12) NOT NULL flag=26,
  name CHAR(22) NOT NULL flag=38)
ENGINE=CONNECT table_type=DOS file_name='dept.dat';
```

Here the flag column option represents the offset of this column inside the\
records. If the offset of a column is not specified, it defaults to the end of\
the previous column and defaults to 0 for the first one. The _`lrecl`_\
parameter that represents the maximum size of a record is calculated by default\
as the end of the rightmost column and can be unspecified except when some\
trailing information exists after the rightmost column.

**Note:** A special case is files having an encoding such as UTF-8 (for\
instance specifying `charset=UTF8`) in which some characters may be\
represented with several bytes. Unlike the type size that MariaDB interprets as\
a number of characters, the `lrecl` value is the record size in bytes and the\
flag value represents the offset of the field in the record in bytes. If the\
flag and/or the `lrecl` value are not specified, they are calculated by\
the number of characters in the fields multiplied by a value that is the\
maximum size in bytes of a character for the corresponding charset. For UTF-8\
this value is 3 which is often far too much as there are very few characters\
requiring 3 bytes to be represented. When creating a new file, you are on the\
safe side by only doubling the maximum number of characters of a field to\
calculate the offset of the next field. Of course, for already existing files,\
the offset must be specified according to what it is in it.

Although the field representation is always text in the table file, you can\
freely choose the corresponding column type, characters, date, integer or\
floating point according to its contents.

Sometimes, as in the _number_ column of the above _department_ table, you\
have the choice of the type, numeric or characters. This will modify how the\
column is internally handled — in characters `0021`\
is different from `21` but not in numeric — as well\
as how it is displayed.

If the last field has fixed length, the table should be referred as having the\
type `FIX`. For instance, to create a table on the file _boys.txt_:

```
John      Boston      25/01/1986  02/06/2010
Henry     Boston      07/06/1987  01/04/2008
George    San Jose    10/08/1981  02/06/2010
Sam       Chicago     22/11/1979  10/10/2007
James     Dallas      13/05/1992  14/12/2009
Bill      Boston      11/09/1986  10/02/2008
```

You can for instance use the command:

```
CREATE TABLE boys (
  name CHAR(12) NOT NULL,
  city CHAR(12) NOT NULL,
  birth DATE NOT NULL date_format='DD/MM/YYYY',
  hired DATE NOT NULL date_format='DD/MM/YYYY' flag=36)
ENGINE=CONNECT table_type=FIX file_name='boys.txt' lrecl=48;
```

Here some _flag_ options were not specified because the fields have no\
intermediate space between them except for the last column. The offsets are\
calculated by default adding the field length to the _offset_ of the\
preceding field. However, for formatted date columns, the offset in the file\
depends on the format and cannot be calculated by default. For fixed files,\
the _lrecl_ option is the physical length of the record including the line\
ending character(s). It is calculated by adding to the end of the last field 2\
bytes under Windows (CRLF) or 1 byte under UNIX. If the file is imported from\
another operating system, the `ENDING` option will have to be specified with\
the proper value.

For this table, the last offset and the record length must be specified anyway\
because the date columns have field length coming from their format that is not\
known by CONNECT. Do not forget to add the line ending length to the total\
length of the fields.

This table is displayed as:

| name   | city     | birth      | hired      |
| ------ | -------- | ---------- | ---------- |
| John   | Boston   | 1986-01-25 | 2010-06-02 |
| Henry  | Boston   | 1987-06-07 | 2008-04-01 |
| George | San Jose | 1981-08-10 | 2010-06-02 |
| Sam    | Chicago  | 1979-11-22 | 2007-10-10 |
| James  | Dallas   | 1992-05-13 | 2009-12-14 |
| Bill   | Boston   | 1986-09-11 | 2008-02-10 |

Whenever possible, the fixed format should be preferred to the varying one\
because it is much faster to deal with fixed tables than with variable tables.\
Sure enough, instead of being read or written record by record, FIX tables are\
processed by blocks of `BLOCK_SIZE` records, resulting in far less\
input/output operations to execute. The block size defaults to 100 if not\
specified in the Create Table statement.

**Note 1:** It is not mandatory to declare in the table all the fields existing\
in the source file. However, if some fields are ignored, the _flag_ option of\
the following field and/or the _lrecl_ option will have to be specified.

**Note 2:** Some files have an EOF marker (CTRL+Z 1A) that can prevent the\
table to be recognized as fixed because the file length is not a multiple of\
the fixed record size. To indicate this, use in the option list the create\
option EOF. For instance, if after creating the FIX table _xtab_ on the\
file _foo.dat_ that you know have fixed record size, you get, when you try to\
use it, a message such as:

```
File foo.dat is not fixed length, len=302587 lrecl=141
```

After checking that the LRECL default or specified specification is correct,\
you can indicate to ignore that extra EOF character by:

```
ALTER TABLE xtab option_list='eof=1';
```

Of course, you can specify this option directly in the Create statement. All\
this applies to some other table types, in particular to BIN tables.

**Note 3:** The width of the fields is the length specified in the column\
declaration. For instance for a column declared as:

```
number int(3) not null,
```

The field width in the file is 3 characters. This is the value used to\
calculate the offset of the next field if it is not specified. If this length\
is not specified, it defaults to the MySQL default type length.

## Specifying the Field Format

Some files have specific format for their numeric fields. For instance, the\
decimal point is absent and/or the field should be filled with leading zeros.\
To deal with such files, as well in reading as in writing, the format can be\
specified in the `CREATE TABLE` column definition. The syntax of the field\
format specification is:

```
Field_format='[Z][N][d]'
```

The optional parts of the format are:

|   |                                                          |
| - | -------------------------------------------------------- |
| Z | The field has leading zeros                              |
| N | No decimal point exist in the file                       |
| d | The number of decimals, defaults to the column precision |

## Example

Let us see how it works in the following example. We define a table based on\
the file xfmt.txt having eight fields of 12 characters:

```
CREATE TABLE xfmt (
  col1 DOUBLE(12,3) NOT NULL,
  col2 DOUBLE(12,3) NOT NULL field_format='4',
  col3 DOUBLE(12,2) NOT NULL field_format='N3',
  col4 DOUBLE(12,3) NOT NULL field_format='Z',
  col5 DOUBLE(12,3) NOT NULL field_format='Z3',
  col6 DOUBLE(12,5) NOT NULL field_format='ZN5',
  col7 INT(12) NOT NULL field_format='N3',
  col8 SMALLINT(12) NOT NULL field_format='N3')
ENGINE=CONNECT table_type=FIX file_name='xfmt.txt';

INSERT INTO xfmt VALUES(4567.056,4567.056,4567.056,4567.056,-23456.8,
    3.14159,4567,4567);
SELECT * FROM xfmt;
```

The first row is displayed as:

| COL1     | COL2     | COL3    | COL4     | COL5       | COL6    | COL7 | COL8 |
| -------- | -------- | ------- | -------- | ---------- | ------- | ---- | ---- |
| 4567.056 | 4567.056 | 4567.06 | 4567.056 | -23456.800 | 3.14159 | 4567 | 4567 |

The number of decimals displayed for all float columns is the column precision, the second argument of the column type option. Of course, integer columns have no decimals, although their formats specify some.

More interesting is the file layout. To see it let us define another table\
based on the same file but whose columns are all characters:

```
CREATE TABLE cfmt (
  col1 CHAR(12) NOT NULL,
  col2 CHAR(12) NOT NULL,
  col3 CHAR(12) NOT NULL,
  col4 CHAR(12) NOT NULL,
  col5 CHAR(12) NOT NULL,
  col6 CHAR(12) NOT NULL,
  col7 CHAR(12) NOT NULL,
  col8 CHAR(12) NOT NULL)
ENGINE=CONNECT table_type=FIX file_name='xfmt.txt';
SELECT * FROM cfmt;
```

The (transposed) display of the select command shows the file text layout for\
each field. Below a third column was added in this document to comment this\
result.

| Column | Row 1        | Comment (all numeric fields are written right justified)                                                                        |
| ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| COL1   | 4567.056     | No format, the value was entered as is.                                                                                         |
| COL2   | 4567.0560    | The format ‘4’ forces to write 4 decimals.                                                                                      |
| COL3   | 4567060      | N3 → No decimal point. The last 3 digits are decimals. However, the second decimal was rounded because of the column precision. |
| COL4   | 00004567.056 | Z → Leading zeros, 3 decimals (the column precision)                                                                            |
| COL5   | -0023456.800 | Z3 → (Minus sign) leading zeros, 3 decimals.                                                                                    |
| COL6   | 000000314159 | ZN5 → Leading zeros, no decimal point, 5 decimals.                                                                              |
| COL7   | 4567000      | N3 → No decimal point. The last 3 digits are decimals.                                                                          |
| COL8   | 4567000      | Same. Any decimals would be ignored.                                                                                            |

**Note:** For columns internally using double precision floating-point numbers,\
MariaDB limits the decimal precision of any calculation to the column\
precision. The declared column precision should be at least the number of\
decimals of the format to avoid a loss of decimals as it happened for `col3`\
of the above example.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
