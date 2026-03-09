---
description: >-
  Complete CONVERT() reference: CONVERT(expr,type) and CONVERT(expr USING
  charset) syntax, SIGNED/UNSIGNED/BINARY/CHAR types, and CAST() differences.
---

# CONVERT

## Syntax

```sql
CONVERT(expr,type), CONVERT(expr USING transcoding_name)
```

## Description

The `CONVERT()` and [CAST()](cast.md) functions take a value of one type and produce a value of another type.

The type can be one of the following values:

* [BINARY](../../data-types/string-data-types/binary.md)
* [CHAR](../../data-types/string-data-types/char.md)
* [DATE](../../data-types/date-and-time-data-types/date.md)
* [DATETIME](../../data-types/date-and-time-data-types/datetime.md)
* \[DECIMAL [(M\[,D\])](../../data-types/numeric-data-types/decimal.md)]
* [DOUBLE](../../data-types/numeric-data-types/double.md)
* [FLOAT](../../data-types/numeric-data-types/float.md)
* [INTEGER](../../data-types/numeric-data-types/int.md)
  * Short for `SIGNED INTEGER`
* SIGNED \[INTEGER]
* UNSIGNED \[INTEGER]
* [TIME](../../data-types/date-and-time-data-types/time.md)
* [VARCHAR](../../data-types/string-data-types/varchar.md) (in [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle))

Note that in MariaDB, `INT` and `INTEGER` are the same thing.

`BINARY` produces a string with the [BINARY](../../data-types/string-data-types/binary.md) data type. If the optional length is given, `BINARY(N)` causes the cast to use no more than `N` bytes of the argument. Values shorter than the given number in bytes are padded with 0x00 bytes to make them equal the length value.

`CHAR(N)` causes the cast to use no more than the number of characters given in the argument.

The main difference between the [CAST()](cast.md) and `CONVERT()` is that `CONVERT(expr,type)` is ODBC syntax while [CAST(expr as type)](cast.md) and `CONVERT(... USING ...)` are SQL92 syntax.

`CONVERT()` with `USING` is used to convert data between different [character sets](../../data-types/string-data-types/character-sets/). In MariaDB, transcoding names are the same as the corresponding character set names. For example, this statement converts the string 'abc' in the default character set to the corresponding string in the utf8 character set:

```sql
SELECT CONVERT('abc' USING utf8);
```

## Examples

```sql
SELECT enum_col FROM tbl_name 
ORDER BY CAST(enum_col AS CHAR);
```

Converting a [BINARY](../../data-types/string-data-types/binary.md) to string to permit the [LOWER](lower.md) function to work:

```sql
SET @x = 'AardVark';

SET @x = BINARY 'AardVark';

SELECT LOWER(@x), LOWER(CONVERT (@x USING latin1));
+-----------+----------------------------------+
| LOWER(@x) | LOWER(CONVERT (@x USING latin1)) |
+-----------+----------------------------------+
| AardVark  | aardvark                         |
+-----------+----------------------------------+
```

## See Also

* [Character Sets and Collations](../../data-types/string-data-types/character-sets/)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
