---
description: The CONNECT storage engine.
---

# CONNECT BIN Table Type

## Overview

A table of type BIN is physically a binary file in which each row is a logical\
record of fixed length\[[1](connect-bin-table-type.md#_note-0)]. Within a record, column fields are\
of a fixed offset and length as with [FIX tables](connect-dos-and-fix-table-types.md). Specific to BIN tables\
is that numerical values are internally encoded using native platform\
representation, so no conversion is needed to handle numerical values in\
expressions.

It is not required that the lines of a BIN file be separated by characters such\
as CR and/or LF but this is possible. In such an event, the _lrecl_ option must\
be specified accordingly.

**Note:** Unlike for the [DOS and FIX types](connect-dos-and-fix-table-types.md), the width of the fields is the\
length of their internal representation in the file. For instance for a column\
declared as:

```
number int(5) not null,
```

The field width in the file is 4 characters, the size of a binary integer. This\
is the value used to calculate the offset of the next field if it is not\
specified. Therefore, if the next field is placed 5 characters after this one,\
this declaration is not enough, and the flag option will have to be used on the\
next field.

## Type Conversion in BIN Tables

Here are the correspondences between the column type and field format provided\
by default:

| Column type | File default format             |
| ----------- | ------------------------------- |
| Char(n)     | Text of n characters.           |
| Date        | Integer (4 bytes)               |
| Int(n)      | Integer (4 bytes)               |
| Smallint(n) | Short integer (2 bytes)         |
| TinyInt(n)  | Char (1 Byte)                   |
| Bigint(n)   | Large integer (8 bytes)         |
| Double(n,d) | Double floating point (8 bytes) |

However, the column type need not necessarily match the field format within the\
table file. In particular, this occurs for field formats that correspond to\
numeric types that are not handled by CONNECT\[[2](connect-bin-table-type.md#_note-1)]. Indeed, BIN table files may\
internally contain float numbers or binary numbers of any byte length in big-endian or little-endian representation\[[3](connect-bin-table-type.md#_note-2)]. Also, as in [DOS or FIX types](connect-dos-and-fix-table-types.md) tables, you may want to handle some character fields as numeric or\
vice versa.

This is why it is possible to specify the field format when it does not\
correspond to the column type default using the _field\_format_ column option\
in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement. Here are the available field formats for BIN tables:

| Field\_format         | Internal representation                                                           |
| --------------------- | --------------------------------------------------------------------------------- |
| \[n]{L or B or H}\[n] | n bytes binary number in little endian, big endian or host endian representation. |
| C                     | Characters string (n bytes)                                                       |
| I                     | integer (4 bytes)                                                                 |
| D                     | Double float (8 bytes)                                                            |
| S                     | Short integer (2 bytes)                                                           |
| T                     | Tiny integer (1 byte)                                                             |
| G                     | Big integer (8 bytes)                                                             |
| F or R                | Real or float (Floating point number on 4 bytes)                                  |
| X                     | Use the default format field for the column type                                  |

All field formats (except the first one) are a one-character specification\[[4](connect-bin-table-type.md#_note-3)].\
'X' is equivalent to not specifying the field format. For the 'C' character\
specification, _n_ is the column width as specified with the column type. For one-column formats, the\
number of bytes of the numeric fields corresponds to what it is on most\
platforms. However, it could vary for some. The G, I, S and T formats are deprecated because they correspond to supported data types and may not be supported in future versions.

## Example

Here is an example of a BIN table. The file record layout is supposed to be:

```
NNNNCCCCCCCCCCIIIISSFFFFSS
```

Here N represents numeric characters, C any characters, I integer bytes,\
S short integer bytes, and F float number bytes. The `IIII` field contains a\
date in numeric format.

The table could be created by:

```
CREATE TABLE testbal (
fig INT(4) NOT NULL field_format='C',
name CHAR(10) NOT NULL,
birth DATE NOT NULL field_format='L',
id CHAR(5) NOT NULL field_format='L2',
salary DOUBLE(9,2) NOT NULL DEFAULT 0.00 field_format='F',
dept INT(4) NOT NULL field_format='L2')
ENGINE=CONNECT table_type=BIN block_size=5 file_name='Testbal.dat';
```

Specifying the little-endian representation for binary values is not useful on most machines, but makes the create table statement portable on a machine using big endian, as well as the table file.

The field offsets and the file record length are calculated according the\
column internal format and eventually modified by the field format. It is not\
necessary to specify them for a packed binary file without line endings. If a line\
ending is desired, specify the ending option or specify the `lrecl` option adding the ending width. The table\
can be filled by:

```
INSERT INTO testbal VALUES
  (5500,'ARCHIBALD','1980-01-25','3789',4380.50,318),
  (123,'OLIVER','1953-08-10','23456',3400.68,2158),
  (3123,'FOO','2002-07-23','888',default,318);
```

Note that the types of the inserted values must match the column type, not the\
field format type.

The query:

```
SELECT * FROM testbal;
```

returns:

| fig  | name      | birth      | id    | salary  | dept |
| ---- | --------- | ---------- | ----- | ------- | ---- |
| 5500 | ARCHIBALD | 1980-01-25 | 3789  | 4380.50 | 318  |
| 123  | OLIVER    | 1953-08-10 | 23456 | 3400.68 | 2158 |
| 3123 | FOO       | 2002-07-23 | 888   | 0.00    | 318  |

## Numeric fields alignment

In binary files, numeric fields and record length can be aligned on 4-or-8-byte boundaries to optimize performance on certain processors. This can be\
modified in the OPTION\_LIST with an "align" option ("packed" meaning `align=1` is the default).

1. [↑](connect-bin-table-type.md#_ref-0) Sometimes it can be a physical record if LF or\
   CRLF have been written in the file.
2. [↑](connect-bin-table-type.md#_ref-1) Most of these are obsolete because CONNECT supports all column types except float
3. [↑](connect-bin-table-type.md#_ref-2) The default endian representation used in the table file can be specified by setting the ENDIAN option as ‘L’ or ‘B’ in the option list.
4. [↑](connect-bin-table-type.md#_ref-3) It can be specified\
   with more than one character, but only the first one is significant.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
