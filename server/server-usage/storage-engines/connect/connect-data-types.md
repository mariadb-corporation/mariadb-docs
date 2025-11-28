# Data Types

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Many data types make no or little sense when applied to plain files. This why [CONNECT](./) supports only a restricted set of data types. However, ODBC, JDBC or MYSQL source tables may contain data types not supported by CONNECT. In this case, CONNECT makes an automatic conversion to a similar supported type when it is possible.

The data types currently supported by CONNECT are:

| Type name    | Description            | Used for                                                                                                                                                                                                                                                                                                                                                                               |
| ------------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TYPE\_STRING | Zero ended string      | [char](../../../reference/data-types/string-data-types/char.md), [varchar](../../../reference/data-types/string-data-types/varchar.md), [text](../../../reference/data-types/string-data-types/text.md)                                                                                                                                                                                |
| TYPE\_INT    | 4 bytes integer        | [int](../../../reference/data-types/numeric-data-types/int.md), [mediumint](../../../reference/data-types/numeric-data-types/mediumint.md), [integer](../../../reference/data-types/numeric-data-types/integer.md)                                                                                                                                                                     |
| TYPE\_SHORT  | 2 bytes integer        | [smallint](../../../reference/data-types/numeric-data-types/smallint.md)                                                                                                                                                                                                                                                                                                               |
| TYPE\_TINY   | 1 byte integer         | [tinyint](../../../reference/data-types/numeric-data-types/tinyint.md)                                                                                                                                                                                                                                                                                                                 |
| TYPE\_BIGINT | 8 bytes integer        | [bigint](../../../reference/data-types/numeric-data-types/bigint.md), longlong                                                                                                                                                                                                                                                                                                         |
| TYPE\_DOUBLE | 8 bytes floating point | [double](../../../reference/data-types/numeric-data-types/double.md), [float](../../../reference/data-types/numeric-data-types/float.md), real                                                                                                                                                                                                                                         |
| TYPE\_DECIM  | Numeric value          | [decimal](../../../reference/data-types/numeric-data-types/decimal.md), numeric, number                                                                                                                                                                                                                                                                                                |
| TYPE\_DATE   | 4 bytes integer        | [date](../../../reference/data-types/date-and-time-data-types/date.md), [datetime](../../../reference/data-types/date-and-time-data-types/datetime.md), [time](../../../reference/data-types/date-and-time-data-types/time.md), [timestamp](../../../reference/data-types/date-and-time-data-types/timestamp.md), [year](../../../reference/sql-functions/date-time-functions/year.md) |

## TYPE\_STRING

This type corresponds to what is generally known as [CHAR](../../../reference/data-types/string-data-types/char.md) or [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) by database users, or as strings by programmers. Columns containing characters have a maximum length but the character string is of fixed or variable length depending on the file format.

The DATA\_CHARSET option must be used to specify the character set used in the data source or file. Note that, unlike usually with MariaDB, when a multi-byte character set is used, the column size represents the number of bytes the column value can contain, not the number of characters.

## TYPE\_INT

The [INTEGER](../../../reference/data-types/numeric-data-types/integer.md) type contains signed integer numeric 4-byte values (the _int_ of the C language) ranging from `–2,147,483,648` to `2,147,483,647` for signed type and `0` to `4,294,967,295` for unsigned type.

## TYPE\_SHORT

The `SHORT` data type contains signed [integer numeric 2-byte](../../../reference/data-types/numeric-data-types/smallint.md) values (the _short integer_ of the C language) ranging from `–32,768` to `32,767` for signed type and `0` to `65,535` for unsigned type.

## TYPE\_TINY

The `TINY` data type contains [integer numeric 1-byte](../../../reference/data-types/numeric-data-types/tinyint.md) values (the _char_ of the C language) ranging from `–128` to `127` for signed type and `0` to`255` for unsigned type. For some table types, TYPE\_TINY is used to represent Boolean values (0 is false, anything else is true).

## TYPE\_BIGINT

The [BIGINT](../../../reference/data-types/numeric-data-types/bigint.md) data type contains signed integer 8-byte values (the _long long_ of the C language) ranging from `-9,223,372,036,854,775,808` to`9,223,372,036,854,775,807` for signed type and from `0` to`18,446,744,073,709,551,615` for unsigned type.

Inside tables, the coding of all integer values depends on the table type. In tables represented by text files, the number is written in characters, while in  tables represented by binary files (`BIN` or `VEC`) the number is directly stored in the binary representation corresponding to the platform.

The _length_ (or _precision_) specification corresponds to the length of the table field in which the value is stored for text files only. It is used to set the output field length for all table types.

## TYPE\_DOUBLE

The `DOUBLE` data type corresponds to the C language [double](../../../reference/data-types/numeric-data-types/double.md) type, a floating-point double precision value coded with 8 bytes. Like for integers, the internal coding in tables depends on the table type, characters for text files, and platform binary representation for binary files.

The _length_ specification corresponds to the length of the table field in which the value is stored for text files only. The _scale_ (was_precision_) is the number of decimal digits written into text files. For binary table types (BIN and VEC) this does not apply. The _length_ and_scale_ specifications are used to set the output field length and number of decimals for all types of tables.

## TYPE\_DECIM

The `DECIMAL` data type corresponds to what MariaDB or ODBC data sources call `NUMBER`, `NUMERIC`, or [DECIMAL](../../../reference/data-types/numeric-data-types/decimal.md): a numeric value with a maximum number of digits (the precision) some of them eventually being decimal digits (the scale). The internal coding in `CONNECT` is a character representation of the number. For instance:

```sql
colname DECIMAL(14,6)
```

This defines a column _colname_ as a number having a _precision_ of 14 and a _scale_ of 6. Supposing it is populated by:

```sql
INSERT INTO xxx VALUES (-2658.74);
```

The internal representation of it are the character string`-2658.740000`. The way it is stored in a file table depends on the table type. The _length_ field specification corresponds to the length of the table field in which the value is stored and is calculated by CONNECT from the_precision_ and the _scale_ values. This length is _precision_ plus 1 if_scale_ is not 0 (for the decimal point) plus 1 if this column is not 
unsigned (for the eventual minus sign). In fix formatted tables the number is 
right justified in the field of width _length_, for variable formatted 
tables, such as CSV, the field is the representing character string.

Because this type is mainly used by CONNECT to handle numeric or decimal fields 
of ODBC, JDBC and MySQL table types, CONNECT does not provide decimal calculations or comparison by itself. This is why decimal columns of CONNECT tables cannot be indexed.

## DATE Data type

Internally, date/time values are stored by CONNECT as a signed 4-byte integer. 
The value 0 corresponds to 01 January 1970 12:00:00 am coordinated universal 
time ([UTC](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md)). All other date/time values are 
represented by the number of seconds elapsed since or before midnight 
(00:00:00), 1 January 1970, to that date/time value. Date/time values before 
midnight 1 January 1970 are represented by a negative number of seconds.

`CONNECT` handles dates from **13 December 1901, 20:45:52** to**18 January 2038, 19:14:07**.

Although date and time information can be represented in both CHAR and INTEGER 
data types, the DATE data type has special associated properties. For each DATE 
value, CONNECT can store all or only some of the following information: 
century, year, month, day, hour, minute, and second.

### Date Format in Text Tables

Internally, date/time values are handled as a signed 4-byte integer. But in text 
tables (type DOS, FIX, CSV, FMT, and DBF) dates are most of the time stored as 
a formatted character string (although they also can be stored as a numeric 
string representing their internal value). Because there are infinite ways to 
format a date, the format to use for decoding dates, as well as the field 
length in the file, must be associated to date columns (except when they are 
stored as the internal numeric value).

Note that this associated format is used only to describe the way the temporal 
value is stored internally. This format is used both for output to decode the 
date in a SELECT statement as well as for input to encode the date in INSERT or 
UPDATE statements. However, what is kept in this value depends on the data type 
used in the column definition (all the MariaDB temporal values can be specified). 
When creating a table, the format is associated to a date column using the 
DATE\_FORMAT option in the column definition, for instance:

```sql
CREATE TABLE birthday (
  Name VARCHAR(17),
  Bday DATE field_length=10 date_format='MM/DD/YYYY',
  Btime TIME field_length=8 date_format='hh:mm tt')
engine=CONNECT table_type=CSV;

INSERT INTO birthday VALUES ('Charlie','2012-11-12','15:30:00');

SELECT * FROM birthday;
```

The `SELECT` query returns:

| Name    | Bday       | Btime    |
| ------- | ---------- | -------- |
| Charlie | 2012-11-12 | 15:30:00 |

The values of the INSERT statement must be specified using the standard MariaDB syntax and these values are displayed as MariaDB temporal values. Sure enough, the column formats apply only to the way these values are represented inside the CSV files. Here, the inserted record are:

```
Charlie,11/12/2012,03:30 PM
```

**Note:** The field\_length option exists because the MariaDB syntax does not allow specifying the field 
length between parentheses for temporal column types. If not specified, the field length is calculated 
from the date format (sometimes as a max value) or made equal to the default length value if there is no 
date format. In the above example it could have been removed as the calculated values are the ones 
specified. However, if the table type would have been DOS or FIX, these values could be adjusted to fit 
the actual field length within the file.

A `CONNECT` format string consists of a series of elements that represent a 
particular piece of information and define its format. The elements are 
recognized in the order they appear in the format string. Date and time format 
elements are replaced by the actual date and time as they appear in the 
source string. They are defined by the following groups of characters:

| Element | Description                                                                     |
| ------- | ------------------------------------------------------------------------------- |
| YY      | The last two digits of the year (that is, 1996 would be coded as "96").         |
| YYYY    | The full year (that is, 1996 could be entered as "96" but displayed as “1996”). |
| MM      | The one or two-digit month number.                                              |
| MMM     | The three-character month abbreviation.                                         |
| MMMM    | The full month name.                                                            |
| DD      | The one or two-digit month day.                                                 |
| DDD     | The three-character weekday abbreviation.                                       |
| DDDD    | The full weekday name.                                                          |
| hh      | The one or two-digit hour in 12-hour or 24-hour format.                         |
| mm      | The one or two-digit minute.                                                    |
| ss      | The one or two-digit second.                                                    |
| t       | The one-letter AM/PM abbreviation (that is, AM is entered as "A").              |
| tt      | The two-letter AM/PM abbreviation (that is, AM is entered as "AM").             |

### Usage Notes

* To match the source string, you can add body text to the format string, 
  enclosing it in single quotes or double quotes if it would be ambiguous. 
  Punctuation marks do not need to be quoted.
* The hour information is regarded as 12-hour format if a “t” or “tt” element 
  follows the “hh” element in the format or as 24-hour format otherwise.
* The "MM", "DD", "hh", "mm", "ss" elements can be specified with one or two 
  letters (e.g. "MM" or "M") making no difference on input, but placing a 
  leading zero to one-digit values on output [[1](connect-data-types.md#_note-0)] for two-letter elements.
* If the format contains elements DDD or DDDD, the day of week name is skipped 
  on input and ignored to calculate the internal date value. On output, the 
  correct day of week name is generated and displayed.
* Temporal values are always stored as numeric in [BIN](connect-table-types/connect-table-types-data-files.md#bin-table-type) and [VEC](connect-table-types/connect-table-types-data-files.md#vec-table-type-vecto) tables.

### Handling dates that are out of the range of supported CONNECT dates

If you want to make a table containing, for instance, historical dates not being convertible into CONNECT dates, make your column `CHAR` or `VARCHAR` and store the dates in the MariaDB format. All date functions applied to these strings will convert them to MariaDB dates and will work 
as if they were real dates. Of course they must be inserted and are displayed using the MariaDB format.

## NULL handling

`CONNECT` handles [null values](../../../reference/data-types/null-values.md) for data sources able to produce nulls. Currently 
this concerns mainly the [ODBC](connect-table-types/connect-odbc-table-type-accessing-tables-from-another-dbms.md), [JDBC](connect-table-types/connect-jdbc-table-type-accessing-tables-from-another-dbms.md), MONGO, [MYSQL](connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables.md), [XML](connect-table-types/connect-table-types-data-files.md#xml-table-type), [JSON](connect-table-types/connect-json-table-type.md) and [INI](connect-table-types/connect-table-types-data-files.md#ini-table-type) table types. For INI, [JSON](connect-table-types/connect-json-table-type.md), MONGO or XML types, null values are returned when the key is missing in the section (INI) or when the corresponding node does not exist in a row (XML, JSON, MONGO).

For other file tables, the issue is to define what a null value is. In a numeric column, 0 can sometimes be a valid value but, in some other cases, it 
can make no sense. The same for character columns; is a blank field a valid value or not?

A special case is DATE columns with a DATE _FORMAT specified. Any value not matching the format can be regarded as NULL.

`CONNECT` leaves the decision to you. When declaring a column in the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) 
statement, if it is declared NOT NULL, blank or zero values are considered 
as valid values. Otherwise they are considered as NULL values. In all 
cases, nulls are replaced on insert or update by pseudo null values, a zero-length character string for text types or a zero value for numeric types. Once 
converted to pseudo null values, they are recognized as NULL only for 
columns declared as nullable.

For instance:

```sql
CREATE TABLE t1 (a INT, b CHAR(10)) ENGINE=CONNECT;
INSERT INTO t1 VALUES (0,'zero'),(1,'one'),(2,'two'),(NULL,'???');
SELECT * FROM t1 WHERE a IS NULL;
```

The select query replies:

| a    | b    |
| ---- | ---- |
| NULL | zero |
| NULL | ???  |

Sure enough, the value 0 entered on the first row is regarded as NULL for a 
nullable column. However, if we execute the query:

```sql
SELECT * FROM t1 WHERE a = 0;
```

This will return no line because a NULL is not equal to 0 in an SQL where clause.

Now let us see what happens with not null columns:

```sql
CREATE TABLE t1 (a INT NOT NULL, b CHAR(10) NOT NULL) ENGINE=CONNECT;
INSERT INTO t1 VALUES (0,'zero'),(1,'one'),(2,'two'),(NULL,'???');
```

The insert statement will produce a warning saying:

| Level   | Code | Message                   |
| ------- | ---- | ------------------------- |
| Warning | 1048 | Column 'a' cannot be null |

It is replaced by a pseudo null `0` on the fourth row. Let us see the result:

```
SELECT * FROM t1 WHERE a IS NULL;
SELECT * FROM t1 WHERE a = 0;
```

The first query returns no rows, 0 are valid values and not NULL. The second query replies:

| a | b    |
| - | ---- |
| 0 | zero |
| 0 | ???  |

It shows that the NULL inserted value was replaced by a valid 0 value.

## Unsigned numeric types

They are supported by CONNECT since version 1.01.0010 for fixed numeric types 
(TINY, SHORT, INTEGER, and BITINT).

## Data type conversion

`CONNECT` is able to convert data from one type to another in most cases. These 
conversions are done without warning even when this leads to truncation or loss 
of precision. This is true, in particular, for tables of type ODBC, JDBC, MYSQL and PROXY (via MySQL) 
because the source table may contain some data types not supported by `CONNECT`. 
They are converted when possible to `CONNECT` types.

When converted, MariaDB types are converted as:

| MariaDB Types                                                                                                                                           | CONNECT Type             | Remark                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [integer](../../../reference/data-types/numeric-data-types/integer.md), [medium integer](../../../reference/data-types/numeric-data-types/mediumint.md) | TYPE\_INT                | 4 byte integer                                                                                                            |
| [small integer](../../../reference/data-types/numeric-data-types/smallint.md)                                                                           | TYPE\_SHORT              | 2 byte integer                                                                                                            |
| [tiny integer](../../../reference/data-types/numeric-data-types/tinyint.md)                                                                             | TYPE\_TINY               | 1 byte integer                                                                                                            |
| [char](../../../reference/data-types/string-data-types/char.md), [varchar](../../../reference/data-types/string-data-types/varchar.md)                  | TYPE\_STRING             | Same length                                                                                                               |
| [double](../../../reference/data-types/numeric-data-types/double.md), [float](../../../reference/data-types/numeric-data-types/float.md), real          | TYPE\_DOUBLE             | 8 byte floating point                                                                                                     |
| [decimal](../../../reference/data-types/numeric-data-types/decimal.md), numeric                                                                         | TYPE\_DECIM              | Length depends on precision and scale                                                                                     |
| all [date](../../../reference/data-types/date-and-time-data-types/date.md) related types                                                                | TYPE\_DATE               | Date format can be set accordingly                                                                                        |
| [bigint](../../../reference/data-types/numeric-data-types/bigint.md), longlong                                                                          | TYPE\_BIGINT             | 8 byte integer                                                                                                            |
| [enum](../../../reference/data-types/string-data-types/enum.md), [set](../../../reference/data-types/string-data-types/set-data-type.md)                | TYPE\_STRING             | Numeric value not accessible                                                                                              |
| All text types                                                                                                                                          | TYPE\_STRING TYPE\_ERROR | Depending on the value of the [connect\_type\_conv](connect-system-variables.md#connect_type_conv) system variable value. |
| Other types                                                                                                                                             | TYPE\_ERROR              | Not supported, no conversion provided.                                                                                    |

For [ENUM](../../../reference/data-types/string-data-types/enum.md), the length of the column is the length of the longest value of the enumeration. For [SET](../../../reference/data-types/string-data-types/set-data-type.md) the length is enough to contain all the set values concatenated with comma separator.

In the case of [TEXT](../../../reference/data-types/string-data-types/text.md) columns, the handling depends on the values given to the [connect\_type\_conv](connect-system-variables.md#connect_type_conv) and [connect\_conv\_size](connect-system-variables.md#connect_conv_size) system variables.

Note: [BLOB](../../../reference/data-types/string-data-types/blob.md) is currently not converted by default until a TYPE\_BIN type is added to CONNECT. However, the FORCE option (from Connect 1.06.006) can be specified for blob columns containing text and the SKIP option also applies to ODBC BLOB columns.

ODBC SQL types are converted as:

| SQL Types                                        | Connect Type | Remark                                                                                                                                                                                       |
| ------------------------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQL\_CHAR, SQL\_VARCHAR                          | TYPE\_STRING |                                                                                                                                                                                              |
| SQL\_LONGVARCHAR                                 | TYPE\_STRING | len = min(abs(len), connect\_conv\_size) If the column is generated by discovery (columns not specified) its length is [connect\_conv\_size](connect-system-variables.md#connect_conv_size). |
| SQL\_NUMERIC, SQL\_DECIMAL                       | TYPE\_DECIM  |                                                                                                                                                                                              |
| SQL\_INTEGER                                     | TYPE\_INT    |                                                                                                                                                                                              |
| SQL\_SMALLINT                                    | TYPE\_SHORT  |                                                                                                                                                                                              |
| SQL\_TINYINT, SQL\_BIT                           | TYPE\_TINY   |                                                                                                                                                                                              |
| SQL\_FLOAT, SQL\_REAL, SQL\_DOUBLE               | TYPE\_DOUBLE |                                                                                                                                                                                              |
| SQL\_DATETIME                                    | TYPE\_DATE   | len = 10                                                                                                                                                                                     |
| SQL\_INTERVAL                                    | TYPE\_STRING | len = 8 + ((scale) ? (scale+1) : 0)                                                                                                                                                          |
| SQL\_TIMESTAMP                                   | TYPE\_DATE   | len = 19 + ((scale) ? (scale +1) : 0)                                                                                                                                                        |
| SQL\_BIGINT                                      | TYPE\_BIGINT |                                                                                                                                                                                              |
| SQL\_GUID                                        | TYPE\_STRING | llen=36                                                                                                                                                                                      |
| SQL\_BINARY, SQL\_VARBINARY, SQL\_LONG-VARBINARY | TYPE\_STRING | len = min(abs(len), connect\_conv\_size) Only if the value of [connect\_type\_conv](connect-system-variables.md#connect_type_conv) is force. The column should use the binary charset.       |
| Other types                                      | TYPE\_ERROR  | Not supported.                                                                                                                                                                               |

JDBC SQL types are converted as:

| JDBC Types                    | Connect Type            | Remark                                                                                                                                                                                       |
| ----------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (N)CHAR, (N)VARCHAR           | TYPE\_STRING            |                                                                                                                                                                                              |
| LONG(N)VARCHAR                | TYPE\_STRING            | len = min(abs(len), connect\_conv\_size) If the column is generated by discovery (columns not specified), its length is [connect\_conv\_size](connect-system-variables.md#connect_conv_size) |
| NUMERIC, DECIMAL, VARBINARY   | TYPE\_DECIM             |                                                                                                                                                                                              |
| INTEGER                       | TYPE\_INT               |                                                                                                                                                                                              |
| SMALLINT                      | TYPE\_SHORT             |                                                                                                                                                                                              |
| TINYINT, BIT                  | TYPE\_TINY              |                                                                                                                                                                                              |
| FLOAT, REAL, DOUBLE           | TYPE\_DOUBLE            |                                                                                                                                                                                              |
| DATE                          | TYPE\_DATE              | len = 10                                                                                                                                                                                     |
| TIME                          | TYPE\_DATE              | len = 8 + ((scale) ? (scale+1) : 0)                                                                                                                                                          |
| TIMESTAMP                     | TYPE\_DATE              | len = 19 + ((scale) ? (scale +1) : 0)                                                                                                                                                        |
| BIGINT                        | TYPE\_BIGINT            |                                                                                                                                                                                              |
| UUID (specific to PostgreSQL) | TYPE\_STRINGTYPE\_ERROR | len=36If [connect\_type\_conv=NO](connect-system-variables.md#connect_type_conv)                                                                                                             |
| Other types                   | TYPE\_ERROR             | Not supported.                                                                                                                                                                               |

Note: The [connect\_type\_conv](connect-system-variables.md#connect_type_conv) SKIP option also applies to ODBC and JDBC tables.

1. [↑](connect-data-types.md#_ref-0) Here input and output are\
   used to specify respectively decoding the date to get its numeric value from\
   the data file and encoding a date to write it in the table file. Input is\
   performed within [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) queries; output is performed in [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) or [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md)\
   queries.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
