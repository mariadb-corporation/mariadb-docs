---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT CSV and FMT Table Types

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

## CSV Type

Many source data files are formatted with variable length fields and records.\
The simplest format, known as `CSV` (Comma Separated Variables), has column\
fields separated by a separator character. By default, the separator is a comma\
but can be specified by the `SEP_CHAR` option as any character, for instance\
a semi-colon.

If the CSV file first record is the list of column names, specifying the`HEADER=1` option will skip the first record on reading. On writing, if the\
file is empty, the column names record is automatically written.

For instance, given the following _people.csv_ file:

```
Name;birth;children
"Archibald";17/05/01;3
"Nabucho";12/08/03;2
```

You can create the corresponding table by:

```
CREATE TABLE people (
  name CHAR(12) NOT NULL,
  birth DATE NOT NULL date_format='DD/MM/YY',
  children SMALLINT(2) NOT NULL)
ENGINE=CONNECT table_type=CSV file_name='people.csv'
header=1 sep_char=';' quoted=1;
```

Alternatively the engine can attempt to automatically detect the column names, data types and widths using:

```
CREATE TABLE people
ENGINE=CONNECT table_type=CSV file_name='people.csv'
header=1 sep_char=';' quoted=1;
```

For CSV tables, the _flag_ column option is the rank of the column into the\
file starting from 1 for the leftmost column. This is to enable having column\
displayed in a different order than in the file and/or to define the table\
specifying only some columns of the CSV file. For instance:

```
CREATE TABLE people (
  name CHAR(12) NOT NULL,
  children SMALLINT(2) NOT NULL flag=3,
  birth DATE NOT NULL flag=2 date_format='DD/MM/YY')
ENGINE=CONNECT table_type=CSV file_name='people.csv'
header=1 sep_char=';' quoted=1;
```

In this case the command:

```
SELECT * FROM people;
```

will display the table as:

| name      | children | birth      |
| --------- | -------- | ---------- |
| Archibald | 3        | 2001-05-17 |
| Nabucho   | 2        | 2003-08-12 |

Many applications produce CSV files having some fields quoted, in particular\
because the field text contains the separator character. For such files,\
specify the 'QUOTED=_n_' option to indicate the level of quoting and/or the\
'`QCHAR=c`' to specify what is this eventual quoting character, which is`"` by default. Quoting with single quotes must be specified as`QCHAR=''''`. On writing, fields are quoted depending on the value of\
the quoting level, which is `–1` by default meaning no quoting:

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | The fields between quotes are read and the quotes discarded. On writing, fields are quoted only if they contain the separator character or begin with the quoting character. If they contain the quoting character, it are doubled. |
| 1 | Only text fields are written between quotes, except null fields. This includes also the column names of an eventual header.                                                                                                         |
| 2 | All fields are written between quotes, except null fields.                                                                                                                                                                          |
| 3 | All fields are written between quotes, including null fields.                                                                                                                                                                       |

Files written this way are successfully read by most applications including spreadsheets.

**Note 1:** If only the QCHAR option is specified, the QUOTED option will\
default to 1.

**Note 2:** For CSV tables whose separator is the tab character, specify`sep_char='\t'`.

**Note 3:** When creating a table on an existing CSV file, you can let\
CONNECT analyze the file and make the column description. However, this is a\
not an elaborate analysis of the file and, for instance, `DATE` fields will\
not be recognized as such but are regarded as string fields.

**Note 4:** The CSV parser only reads and buffers up to 4KB per row by default, rows longer than this is truncated when read from the file. If the rows are expected to be longer than this use `lrecl` to increase this. For example to set an 8KB maximum row read you would use `lrecl=8192`

### Restrictions on CSV Tables

* If [secure\_file\_priv](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv) is set to the path of some directory, then CSV tables can only be created with files in that directory.

## FMT Type

FMT tables handle files of various formats that are an extension of the concept\
of CSV files. CONNECT supports these files providing all lines have the same\
format and that all fields present in all records are recognizable (optional\
fields must have recognizable delimiters). These files are made by specific\
application and CONNECT handles them in read only mode.

FMT tables must be created as CSV tables, specifying their type as FMT. In\
addition, each column description must be added to its format specification.

## Column Format Specification of FMT tables

The input format for each column is specified as a FIELD\_FORMAT option. A\
simple example is:

```
IP Char(15) not null field_format=' %n%s%n',
```

In the above example, the format for this (1st) field is `' %n%s%n'`. Note\
that the blank character at the beginning of this format **is** significant. No\
trailing blank should be specified in the column formats.

The syntax and meaning of the column input format is the one of the C **scanf**\
function.

However, CONNECT uses the input format in a specific way. Instead of using it\
to directly store the input value in the column buffer; it uses it to delimit\
the sub string of the input record that contains the corresponding column\
value. Retrieving this value is done later by the column functions as for\
standard CSV files.

This is why all column formats are made of five components:

1. An eventual description of what is met and ignored before the column value.
2. A marker of the beginning of the column value written as `%n`.
3. The format specification of the column value itself.
4. A marker of the end of the column value written as `%n` (or `%m` for optional fields).
5. An eventual description of what is met after the column value (not valid is `%m` was used).

For example, taking the file _funny.txt_:

```
12345,'BERTRAND',#200;5009.13
 56, 'POIROT-DELMOTTE' ,#4256 ;18009
345 ,'TRUCMUCHE' , #67; 19000.25
```

You can make a table _fmtsample_ with 4 columns ID, NAME, DEPNO and SALARY, using the Create\
Table statement and column formats:

```
CREATE TABLE FMTSAMPLE (
  ID INTEGER(5) NOT NULL field_format=' %n%d%n',
  NAME CHAR(16) NOT NULL field_format=' , ''%n%[^'']%n''',
  DEPNO INTEGER(4) NOT NULL field_format=' , #%n%d%n',
  SALARY DOUBLE(12,2) NOT NULL field_format=' ; %n%f%n')
ENGINE=CONNECT table_type=FMT file_name='funny.txt';
```

**Field 1** is an integer (`%d`) with eventual leading blanks.

**Field 2** is separated from field 1 by optional blanks, a comma, and other\
optional blanks and is between single quotes. The leading quote is included in\
component 1 of the column format, followed by the `%n` marker. The column\
value is specified as `%[^']` meaning to keep any characters read until a\
quote is met. The ending marker (`%n`) is followed by the 5th component of\
the column format, the single quote that follows the column value.

**Field 3,** also separated by a comma, is a number preceded by a pound sign.

**Field 4,** separated by a semicolon eventually surrounded by blanks, is a\
number with an optional decimal point (`%f`).

This table are displayed as:

| ID    | NAME            | DEPNO | SALARY   |
| ----- | --------------- | ----- | -------- |
| 12345 | BERTRAND        | 200   | 5009.13  |
| 56    | POIROT-DELMOTTE | 4256  | 18009.00 |
| 345   | TRUCMUCHE       | 67    | 19000.25 |

## Optional Fields

To be recognized, a field normally must be at least one character long. For\
instance, a numeric field must have at least one digit, or a character field\
cannot be void. However many existing files do not follow this format.

Let us suppose for instance that the preceding example file could be:

```
12345,'BERTRAND',#200;5009.13
 56, 'POIROT-DELMOTTE' ,# ;18009
345 ,'' , #67; 19000.25
```

This will display an error message such as _“Bad format line x field y of_\
\&#xNAN;_FMTSAMPLE”._ To avoid this and accept these records, the corresponding fields\
must be specified as "optional". In the above example, fields 2 and 3 can have\
null values (in lines 3 and 2 respectively). To specify them as optional, their\
format must be terminated by `%m` (instead of the second `%n`). A statement\
such as this can do the table creation:

```
CREATE TABLE FMTAMPLE (
  ID INTEGER(5) NOT NULL field_format=' %n%d%n',
  NAME CHAR(16) NOT NULL field_format=' , ''%n%[^'']%m',
  DEPNO INTEGER(4) field_format=''' , #%n%d%m',
  SALARY DOUBLE(12,2) field_format=' ; %n%f%n')
ENGINE=CONNECT table_type=FMT file_name='funny.txt';
```

Note that, because the statement must be terminated by `%m` with no\
additional characters, skipping the ending quote of field 2 was moved from the\
end of the second column format to the beginning of the third column format.

The table result is:

| ID    | NAME            | DEPNO | SALARY    |
| ----- | --------------- | ----- | --------- |
| 12345 | BERTRAND        | 200   | 5,009.13  |
| 56    | POIROT-DELMOTTE | NULL  | 18,009.00 |
| 345   | NULL            | 67    | 19,000.25 |

Missing fields are replaced by null values if the column is nullable, blanks\
for character strings and 0 for numeric fields if it is not.

**Note 1:** Because the formats are specified between quotes, quotes belonging\
to the formats must be doubled or escaped to avoid a `CREATE TABLE` statement syntax error.

**Note 2:** Characters separating columns can be included as well in component\
5 of the preceding column format or in component 1 of the succeeding column\
format but for blanks, which should be always included in component 1 of the\
succeeding column format because line trailing blanks can be sometimes lost.\
This is also mandatory for optional fields.

**Note 3:** Because the format is mainly used to find the sub-string\
corresponding to a column value, the field specification does not necessarily\
match the column type. For instance supposing a table contains two integer\
columns, NBONE and NBTWO, the two lines describing these columns could be:

```
NBONE integer(5) not null field_format=' %n%d%n',
NBTWO integer(5) field_format=' %n%s%n',
```

The first one specifies a required integer field (`%d`), the second line\
describes a field that can be an integer, but can be replaced by a "-" (or any\
other) character. Specifying the format specification for this column as a\
character field (`%s`) enables to recognize it with no error in all cases. Later\
on, this field are converted to integer by the column read function, and a\
null 0 value are generated for field specified in their format as\
non-numeric.

## Bad Record Error Processing

When no match if found for a column field the process aborts with a message\
such as:

```
Bad format line 3 field 4 of funny.txt
```

This can mean as well that one line of the input line is ill formed or that the\
column format for this field has been wrongly specified. When you know that\
your file contains records that are ill formatted and should be eliminated from\
normal processing, set the “maxerr” option of the CREATE TABLE statement, for\
instance:

```
Option_list='maxerr=100'
```

This will indicate that no error message be raised for the 100 first wrong\
lines. You can set Maxerr to a number greater than the number of wrong lines in\
your files to ignore them and get no errors.

Additionally, the “accept” option permit to keep those ill formatted lines with\
the bad field, and all succeeding fields of the record, nullified. If “accept”\
is specified without “maxerr”, all ill formatted lines are accepted.

**Note:** This error processing also applies to CSV tables.

## Fields Containing a Formatted Date

A special case is one of columns containing a formatted date. In this case, two\
formats must be specified:

1. The field recognition format used to delimit the date in the input record.
2. The date format used to interpret the date.
3. The field length option if the date representation is different than the\
   standard type size.

For example, let us suppose we have a web log source file containing records\
such as:

```
165.91.215.31 - - [17/Jul/2001:00:01:13 -0400] - "GET /usnews/home.htm HTTP/1.1" 302
```

The create table statement shall be like this:

```
CREATE TABLE WEBSAMP (
  IP CHAR(15) NOT NULL field_format='%n%s%n',
  DATE DATETIME NOT NULL field_format=' - - [%n%s%n -0400]'
  date_format='DD/MMM/YYYY:hh:mm:ss' field_length=20,
  FILE CHAR(128) NOT NULL field_format=' - "GET %n%s%n',
  HTTP DOUBLE(4,2) NOT NULL field_format=' HTTP/%n%f%n"',
  NBONE INT(5) NOT NULL field_format=' %n%d%n')
ENGINE=CONNECT table_type=FMT lrecl=400
file_name='e:\\data\\token\\Websamp.dat';
```

**Note 1:** Here, `field_length=20` was necessary because the default size\
for datetime columns is only 19. The `lrecl=400` was also specified because\
the actual file contains more information in each records making the record\
size calculated by default too small.

**Note 2:** The file name could have been specified as`'e:/data/token/Websamp.dat'`.

**Note 3:** FMT tables are currently read only.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
