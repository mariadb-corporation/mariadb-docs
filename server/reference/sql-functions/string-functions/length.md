---
description: >-
  Return the length of a string in bytes. This function counts the number of
  bytes in the string, which may differ from character count for multi-byte
  strings.
---

# LENGTH

## Syntax

```sql
LENGTH(str)
```

## Description

Returns the length of the string `str`.

In the default mode, when [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is not set, the length is measured in bytes. In this case, a multi-byte character counts as multiple bytes. This means that for a string containing five two-byte characters, `LENGTH()` returns 10, whereas [CHAR\_LENGTH()](char_length.md) returns 5.

When running Oracle mode, the length is measured in characters, and `LENGTH` is a synonym for [CHAR\_LENGTH()](char_length.md).

If `str` is not a string value, it is converted into a string. If `str` is `NULL`, the function returns `NULL`.

## Examples

```sql
SELECT LENGTH('MariaDB');
+-------------------+
| LENGTH('MariaDB') |
+-------------------+
|                 7 |
+-------------------+
```

When Oracle mode is not set:

```sql
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π')  | LENGTH('π')  | LENGTHB('π')  | OCTET_LENGTH('π')  |
+-------------------+--------------+---------------+--------------------+
|                 1 |            2 |             2 |                  2 |
+-------------------+--------------+---------------+--------------------+
```

In Oracle mode:

```sql
SELECT CHAR_LENGTH('π'), LENGTH('π'), LENGTHB('π'), OCTET_LENGTH('π');
+-------------------+--------------+---------------+--------------------+
| CHAR_LENGTH('π')  | LENGTH('π')  | LENGTHB('π')  | OCTET_LENGTH('π')  |
+-------------------+--------------+---------------+--------------------+
|                 1 |            1 |             2 |                  2 |
+-------------------+--------------+---------------+--------------------+
```

## See Also

* [CHAR\_LENGTH()](char_length.md)
* [LENGTHB()](lengthb.md)
* [OCTET\_LENGTH()](octet_length.md)
* [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
