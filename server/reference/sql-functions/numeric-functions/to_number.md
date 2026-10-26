---
description: >-
  Convert a string to a number. This Oracle-compatible function parses a string
  using a specified format and returns a numeric value.
---

# TO\_NUMBER

{% hint style="info" %}
`TO_NUMBER` is available from [MariaDB 12.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/12.2/mariadb-12.2-changes-and-improvements).
{% endhint %}

`TO_NUMBER` converts a string or a number to a number of the [DOUBLE](../../data-types/numeric-data-types/double.md) data type, optionally parsing the string with a format.

## Syntax

```bnf
TO_NUMBER(number_or_string_subject)
TO_NUMBER(string_subject,string_format)
```

## Description

The function returns the `DOUBLE` data type for all signatures and input data types.

With one argument, `TO_NUMBER` converts a number, or a string that holds a plain number such as `'-12.5'`, to `DOUBLE`.

With two arguments, `string_format` describes how `string_subject` is written. The format supports the following elements:

| Element | Meaning |
| --- | --- |
| `0`, `9` | A digit. |
| `X` | A hexadecimal digit. A format of `X` elements reads a hexadecimal string such as `'FF'`. |
| `,` (comma) | A group separator. The string must have a comma in the same position. |
| `.` (period) | The decimal point. |
| `$` | A dollar sign. The string must contain it. |
| `B` | Blank flag. Accepted in the format. |
| `EEEE` | Scientific notation, such as `1.5E+03`. Group separators can't be used with `EEEE`. |
| `S` | A sign, at the start or the end of the format. The string must have an explicit `+` or `-` in that position. |
| `MI` | A trailing sign, at the end of the format. The string ends with `-` for a negative value, or with a space for a positive one. |
| `PR` | A negative value in angle brackets, at the end of the format: `<1234.50>`. A positive value is enclosed in spaces instead. |
| `FM` | Format flag. Accepted at the start of the format. |

Without `S`, `MI`, or `PR`, a fixed-point format does not accept a sign, so `TO_NUMBER('-1234.50', '9999.99')` returns `NULL`.

If `string_subject` does not match `string_format`, `TO_NUMBER` returns `NULL` and raises warning 1411 (`Incorrect <number format> value`). Use [SHOW WARNINGS](../../sql-statements/administrative-sql-statements/show/show-warnings.md) to see it. A format that is not valid, such as `MI` at the start, raises error 1411 instead.

The function was introduced for Oracle compatibility, but does not include the following features:

* The `ON CONVERSION ERROR` clause
* The third parameter (nlsparam)
* The internationalized elements `G` (group separator), `D` (decimal delimiter), and the currency elements `C`, `L`, and `U`
* The elements `V`, `TM`, `TM9`, and `TME`

A format that contains one of these elements raises error 1235 (`This version of MariaDB doesn't yet support ...`). The internationalized elements are planned for [MDEV-36978](https://jira.mariadb.org/browse/MDEV-36978).

## Examples

Converting a plain number, and a currency amount with group separators:

```sql
SELECT TO_NUMBER('100.00');
+---------------------+
| TO_NUMBER('100.00') |
+---------------------+
|                 100 |
+---------------------+

SELECT TO_NUMBER('$1,234,567.89', '$9,999,999.99');
+---------------------------------------------+
| TO_NUMBER('$1,234,567.89', '$9,999,999.99') |
+---------------------------------------------+
|                                  1234567.89 |
+---------------------------------------------+
```

### Signs

`S` reads a leading or trailing `+` or `-`:

```sql
SELECT TO_NUMBER('-1,234.50', 'S9,999.99');
+-------------------------------------+
| TO_NUMBER('-1,234.50', 'S9,999.99') |
+-------------------------------------+
|                             -1234.5 |
+-------------------------------------+

SELECT TO_NUMBER('+1,234.50', 'S9,999.99');
+-------------------------------------+
| TO_NUMBER('+1,234.50', 'S9,999.99') |
+-------------------------------------+
|                              1234.5 |
+-------------------------------------+

SELECT TO_NUMBER('1,234.50-', '9,999.99S');
+-------------------------------------+
| TO_NUMBER('1,234.50-', '9,999.99S') |
+-------------------------------------+
|                             -1234.5 |
+-------------------------------------+
```

`MI` reads a trailing minus sign, and `PR` reads a negative value in angle brackets, as used in accounting:

```sql
SELECT TO_NUMBER('$1,234.50-', '$9,999.99MI');
+----------------------------------------+
| TO_NUMBER('$1,234.50-', '$9,999.99MI') |
+----------------------------------------+
|                                -1234.5 |
+----------------------------------------+

SELECT TO_NUMBER('<$1,234.50>', '$9,999.99PR');
+-----------------------------------------+
| TO_NUMBER('<$1,234.50>', '$9,999.99PR') |
+-----------------------------------------+
|                                 -1234.5 |
+-----------------------------------------+
```

With `MI` and `PR`, a positive value needs the space that takes the place of the sign or the brackets:

```sql
SELECT TO_NUMBER(' 1234.50 ', '9999.99PR');
+-------------------------------------+
| TO_NUMBER(' 1234.50 ', '9999.99PR') |
+-------------------------------------+
|                              1234.5 |
+-------------------------------------+

SELECT TO_NUMBER('1234.50', '9999.99PR');
+-----------------------------------+
| TO_NUMBER('1234.50', '9999.99PR') |
+-----------------------------------+
|                              NULL |
+-----------------------------------+
```

### Hexadecimal and Scientific Notation

```sql
SELECT TO_NUMBER('7FFFFFFF', 'XXXXXXXX');
+-----------------------------------+
| TO_NUMBER('7FFFFFFF', 'XXXXXXXX') |
+-----------------------------------+
|                        2147483647 |
+-----------------------------------+

SELECT TO_NUMBER('-1.5E+03', '9.9EEEE');
+----------------------------------+
| TO_NUMBER('-1.5E+03', '9.9EEEE') |
+----------------------------------+
|                            -1500 |
+----------------------------------+
```

### A String That Doesn't Match the Format

The format has room for only two digits, so the function returns `NULL` with a warning:

```sql
SELECT TO_NUMBER('1234', '99');
+-------------------------+
| TO_NUMBER('1234', '99') |
+-------------------------+
|                    NULL |
+-------------------------+

SHOW WARNINGS;
+---------+------+---------------------------------------------------------------------+
| Level   | Code | Message                                                             |
+---------+------+---------------------------------------------------------------------+
| Warning | 1411 | Incorrect <number format>='99' value: '1234' for function to_number |
+---------+------+---------------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
