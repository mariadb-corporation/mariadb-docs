# SQL Server and MariaDB Types Comparison

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

This page helps to map each SQL Server type to the matching MariaDB type.

## Numbers

In MariaDB, numeric types can be declared as `SIGNED` or `UNSIGNED`. By default, numeric columns are `SIGNED`, so not specifying either will not break compatibility with SQL Server.

When using `UNSIGNED` values, there is a potential problem with subtractions. When subtracting an `UNSIGNED` valued from another, the result is usually of an `UNSIGNED` type. But if the result is negative, this will cause an error. To solve this problem, we can enable the [NO\_UNSIGNED\_SUBTRACTION](../../../variables-and-modes/sql_mode.md#no_unsigned_subtraction) flag in sql\_mode.

For more information see [Numeric Data Type Overview](../../../../reference/data-types/numeric-data-types/numeric-data-type-overview.md).

### Integer Numbers

| SQL Server Types | Size (bytes) | MariaDB Types                                                                                                                                 | Size (bytes) | Notes                                        |
| ---------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------- |
| tinyint          | 1            | [TINYINT](../../../../reference/data-types/numeric-data-types/tinyint.md)                                                                     | 1            |                                              |
| smallint         | 2            | [SMALLINT](../../../../reference/data-types/numeric-data-types/smallint.md)                                                                   | 2            |                                              |
|                  |              | [MEDIUMINT](../../../../reference/data-types/numeric-data-types/mediumint.md)                                                                 | 3            | Takes 3 bytes on disk, but 4 bytes in memory |
| int              | 1            | [INT](../../../../reference/data-types/numeric-data-types/int.md) / [INTEGER](../../../../reference/data-types/numeric-data-types/integer.md) | 4            |                                              |
| bigint           | 8            | [BIGINT](../../../../reference/data-types/numeric-data-types/bigint.md)                                                                       | 8            |                                              |

### Real Numbers (approximated)

| SQL Server Types | Precision | Size | MariaDB Types                                                                | Size |
| ---------------- | --------- | ---- | ---------------------------------------------------------------------------- | ---- |
| float(1-24)      | 7 digits  | 4    | [FLOAT(0-23)](../../../../reference/data-types/numeric-data-types/float.md)  | 4    |
| float(25-53)     | 15 digist | 8    | [FLOAT(24-53)](../../../../reference/data-types/numeric-data-types/float.md) | 8    |

MariaDB supports an alternative syntax: `FLOAT(M, D)`. M is the total number of digits, and D is the number of digits after the decimal point.

See also: [Floating-point Accuracy](../../../../reference/data-types/numeric-data-types/floating-point-accuracy.md).

#### Aliases

In SQL Server `real` is an alias for `float(24)`.

In MariaDB [DOUBLE](../../../../reference/data-types/numeric-data-types/double.md), and [DOUBLE PRECISION](../../../../reference/data-types/numeric-data-types/double-precision.md) are aliases for `FLOAT(24-53)`.

Normally, `REAL` is also a synonym for `FLOAT(24-53)`. However, the [sql\_mode](../../../variables-and-modes/sql_mode.md) variable can be set with the `REAL_AS_FLOAT` flag to make `REAL` a synonym for `FLOAT(0-23)`.

### Real Numbers (Exact)

| SQL Server Types | Precision | Size (bytes) | MariaDB Types                                                             | Precision | Size (bytes)                                                                            |
| ---------------- | --------- | ------------ | ------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------- |
| decimal          | 0 - 38    | Up to 17     | [DECIMAL](../../../../reference/data-types/numeric-data-types/decimal.md) | 0 - 38    | [See table](../../../../reference/data-types/data-type-storage-requirements.md#decimal) |

MariaDB supports this syntax: `DECIMAL(M, D)`. M and D are both optional. M is the total number of digits (10 by default), and D is the number of digits after the decimal point (0 by default). In SQL Server, defaults are 18 and 0, respectively. The reason for this difference is that SQL standard imposes a default of 0 for D, but it leaves the implementation free to choose any default for M.

SQL Server `DECIMAL` is equivalent to MariaDB `DECIMAL(18)`.

#### Aliases

The following [aliases](../../../../reference/data-types/numeric-data-types/dec-numeric-fixed.md) for `DECIMAL` are recognized in both SQL Server and MariaDB: `DEC`, `NUMERIC`. MariaDB also allows one to use `FIXED`.

### Money

SQL Server `money` and `smallmoney` types represent real numbers guaranteeing a very low level of approximation (five decimal digits are accurate), optionally associated with one of the supported currencies.

MariaDB doesn't have monetary types. To represent amounts of money:

* Store the currency in a separate column, if necessary. It's possible to use a foreign key to a currencies table, or the [ENUM](../../../../reference/data-types/string-data-types/enum.md) type.
* Use a non-approximated type:
  * [DECIMAL](../../../../reference/data-types/numeric-data-types/decimal.md) is very convenient, as it allows one to store the number as-is. But calculations are potentially slower.
  * An integer type is faster for calculations. It is possible to store, for example, the amount of money multiplied by 100.

There is a small incompatibility that users should be aware about. `money` and `smallmoney` are accurate to about 4 decimal digits. This means that, if you use enough decimal digits, operations on these types may produce different results than the results they would produce on MariaDB types.

### Bits

The [BIT](../../../../reference/data-types/numeric-data-types/bit.md) type is supported in MariaDB. Its maximum size is `BIT(64)`. The `BIT` type has a fixed length. If we insert a value which requires less bits than the ones that are allocated, zero-bits are padded on the left.

In MariaDB, binary values can be written in one of the following ways:

* `b'value'`
* `0value`\
  where `value` is a sequence of 0 and 1 digits. Hexadecimal syntax can also be used. For more details, see [Binary Literals](../../../../reference/sql-structure/sql-language-structure/binary-literals.md) and [Hexadecimal Literals](../../../../reference/sql-structure/sql-language-structure/hexadecimal-literals.md).

MariaDB and SQL Server have different sets of bitwise operators. See [Bit Functions and Operators](../../../../reference/sql-functions/secondary-functions/bit-functions-and-operators/).

## BOOLEAN Pseudo-Type

In SQL Server, it is common to use `bit` to represent boolean values. In MariaDB it is possible to do the same, but this is not a common practice.

A column can also be defined as [BOOLEAN](../../../../reference/data-types/numeric-data-types/boolean.md) or `BOOL`, which is just a synonym for [TINYINT](../../../../reference/data-types/numeric-data-types/tinyint.md). `TRUE` and `FALSE` keywords also exist, but they are synonyms for 1 and 0. To understand what this implies, see [Boolean Literals](../../../../reference/sql-structure/sql-language-structure/sql-language-structure-boolean-literals.md).

In MariaDB `'True'` and `'False'` are always strings.

## Date and Time

| SQL Server Types | Range                   | Precision | Size (bytes)    | MariaDB Types                                                                     | Range                   | Size (bytes) | Precision | Notes                                           |
| ---------------- | ----------------------- | --------- | --------------- | --------------------------------------------------------------------------------- | ----------------------- | ------------ | --------- | ----------------------------------------------- |
| date             | 0001-01-01 - 9999-12-31 | 3         | /               | [DATE](../../../../reference/data-types/date-and-time-data-types/date.md)         | 0001-01-01 - 9999-12-31 | 3            | /         | They cover the same range                       |
| datetime         | 1753-01-01 - 9999-12-31 | 8         | 0 to 3, rounded | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) | 001-01-01 - 9999-12-31  | 8            | 0 to 6    | MariaDB values are not approximated, see below. |
| datetime2        | 001-01-01 - 9999-12-31  | 8         | 6 to 8          | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) | 001-01-01 - 9999-12-31  | 8            | 0 to 6    | MariaDB values are not approximated, see below. |
| smalldatetime    |                         |           |                 | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) |                         |              |           |                                                 |
| datetimeoffset   |                         |           |                 | [DATETIME](../../../../reference/data-types/date-and-time-data-types/datetime.md) |                         |              |           |                                                 |
| time             |                         |           |                 | [TIME](../../../../reference/data-types/date-and-time-data-types/time.md)         |                         |              |           |                                                 |

You may also consider the following MariaDB types:

* [TIMESTAMP](../../../../reference/data-types/date-and-time-data-types/timestamp.md) has little to do with SQL Server's `timestamp`. In MariaDB it is the number of seconds elapsed since the beginning of 1970-01-01, with a decimal precision up to 6 digits (0 by default). The maximum allowed value is '2038-01-19 03:14:07'. Values are always stored in UTC. A TIMESTAMP column can optionally be automatically set to the current timestamp on insert, on update, or both. It is not meant to be a unique row identifier. Also, in MariaDB the range of TIMESTAMP values is
* [YEAR](../../../../reference/sql-functions/date-time-functions/year.md) is a 1-byte type representing years between 1901 and 2155, as well as 0000.

### Zero Values

MariaDB allows a special value where all the parts of a date are zeroes: `'0000-00-00'`. This can be disallowed by setting [sql\_mode=NO\_ZERO\_DATE](../../../variables-and-modes/sql_mode.md#no_zero_date).

It is also possible to use values where only some date parts are zeroes, for example `'1994-01-00'` or `'1994-00-00'`. These values can be disallowed by setting [sql\_mode=NO\_ZERO\_IN\_DATE](../../../variables-and-modes/sql_mode.md#no_zero_in_date). They are not affected by `NO_ZERO_DATE`.

### Syntax

Several different date formats are understood. Typically used formats are `'YYYY-MM-DD'` and `YYYYMMDD`. Several separators are accepted.

The syntax defined in standard SQL and ODBC are understood - for example, `DATE '1994-01-01'` and `{d '1994-01-01'}`. Using these eliminates possible ambiguities in contexts where a temporal value could be interpreted as a string or as an integer.

See [Date and Time Literals](../../../../reference/sql-structure/sql-language-structure/date-and-time-literals.md) for the details.

### Precision

For temporal types that include a day time, MariaDB allows a precision from 0 to 6 (microseconds), 0 being the default. The subsecond part is never approximated. It adds up to 3 bytes. See [Data Type Storage Requirements](../../../../reference/data-types/data-type-storage-requirements.md#microseconds) for the details.

## String and Binary

### Binary Strings

| SQL Server Types | Size (bytes) | MariaDB Types                                                                                                                                                          | Notes                    |
| ---------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| binary           | 1 to 8000    | [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) or [BLOB](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | See below for BLOB types |
| varbinary        | 1 to 8000    | [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) or [BLOB](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | See below for BLOB types |
| image            | 2^31-1       | [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) or [BLOB](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | See below for BLOB types |

The `VARBINARY` type is similar to `VARCHAR`, but stores binary byte strings, just like SQL Server `binary` does.

For large binary strings, MariaDB has four `BLOB` types, with different sizes. See [BLOB and TEXT Data Types](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) for more information.

### Character Strings

One important difference between SQL Server and MariaDB is that **in MariaDB character sets do not depend on types and collations**. Character sets can be set at database, table or column level. If this is not done, the default character sets applies, which is specified by the [character\_set\_server](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_server) system variable.

To create a MariaDB table that is identical to a SQL Server table, **it may be necessary to specify a character set for each string column**. However, in many cases using UTF-8 will work.

| SQL Server Types | Size (bytes) | MariaDB Types                                                                          | Size (bytes)        | Character set         |
| ---------------- | ------------ | -------------------------------------------------------------------------------------- | ------------------- | --------------------- |
| char             | 1 to 8000    | [CHAR](../../../../reference/data-types/string-data-types/char.md)                     | 0 to 255            | utf8mb4 (1, 4)        |
| varchar          | 1 to 8000    | [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md)               | 0 to 65,532 (2)     | utf8mb4 (1)           |
| text             | 2^31-1       | [TEXT](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | 2^31-1              | ucs2                  |
| nchar            | 2 to 8000    | [CHAR](../../../../reference/data-types/string-data-types/char.md)                     | 0 to 255            | utf16 or ucs2 (3, 4)  |
| nvarchar         | 2 to 8000    | [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md)               | 0 to 65,532 (2) (5) | utf16 or ucs2 (1) (3) |
| ntext            | 2^30 - 1     | [TEXT](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) | 2^31-1              | ucs2                  |

**Notes:**

1. If SQL Server uses a non-unicode collation, a subset of UTF-8 is used. So it is possible to use a smaller character set on MariaDB too.
2. [InnoDB](../../../../server-usage/storage-engines/innodb/) has a maximum row length of 65,535 bytes. [TEXT](../../../../reference/data-types/string-data-types/blob-and-text-data-types.md) columns do not contribute to the row size, because they are stored separately (except for the first 12 bytes).
3. In SQL Server, UTF-16 is used if data contains Supplementary Characters, otherwise UCS-2 is used. If not sure, use `utf16` in MariaDB.
4. In SQL Server, the value of `ANSI_PADDING` determines if `char` values should be padded with spaces to their maximum length. In MariaDB, this depends on the [PAD\_CHAR\_TO\_FULL\_LENGTH](../../../variables-and-modes/sql_mode.md#pad_char_to_full_length) sql\_mode flag.
5. See JSON, below.

## SQL Server Special Types

### rowversion

MariaDB does not have the `rowversion` type.

If the only purpose is to check if a row has been modified since its last read, a [TIMESTAMP](../../../../reference/data-types/date-and-time-data-types/timestamp.md) column can be used instead. Its default value should be `ON UPDATE CURRENT_TIMESTAMP`. In this way, the timestamp will be updated whenever the column is modified.

A way to preserve much more information is to use a [temporal table](../../../../reference/sql-structure/temporal-tables/system-versioned-tables.md). Past versions of the row will be preserved.

### sql\_variant

MariaDB does not support the `sql_variant` type.

MariaDB is quite flexible about implicit and explicit [type conversions](../../../../reference/sql-functions/string-functions/type-conversion.md). Therefore, for most cases storing the values as a string should be equivalent to using `sql_variant`.

Be aware that the maximum length of an `sql_variant` value is 8,000 bytes. In MariaDB, you may need to use `TINYBLOB`.

### uniqueidentifier

While MariaDB does not support the `uniqueidentifier` type, the [UUID](../../../../reference/data-types/string-data-types/uuid-data-type.md) type can typically be used for the same purpose.

`uniqueidentifier` columns contain 16-bit GUIDs. MariaDB UUID columns store UUIDv1 values (128 bits).

The UUID type was implemented in [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107). On older versions, you can generate unique values with the [UUID()](../../../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid.md) or [UUID\_SHORT()](../../../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_short.md) functions, and store them in `BIT(128)` or `BIT(64)` columns, respectively.

### xml

MariaDB does not support the `xml` type.

XML data can be stored in string columns. MariaDB supports several XML functions.

### JSON

With SQL Server, typically JSON documents are stored in `nvarchar` columns in a text form.

MariaDB has a [JSON](../../../../reference/data-types/string-data-types/json.md) pseudo-type that maps to [LONGTEXT](../../../../reference/data-types/string-data-types/longtext.md). However, from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) the `JSON` pseudo-type also checks that the value is valid a JSON document.

MariaDB supports different JSON functions than SQL Server. MariaDB currently has more functions, and SQL Server syntax will not work. See [JSON functions](../../../../reference/sql-functions/special-functions/json-functions/) for more information.

## MariaDB Specific Types

The following types are supported by MariaDB and don't have a direct equivalent in SQL Server. If you are migrating your database to MariaDB, you can consider using these types.

* [INET6](../../../../reference/data-types/string-data-types/inet6.md) - IPv6 addresses.
* [INET4](../../../../reference/data-types/string-data-types/inet4.md) - IPv4 addresses.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
