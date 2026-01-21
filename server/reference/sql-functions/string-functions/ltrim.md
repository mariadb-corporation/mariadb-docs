---
description: >-
  Remove leading spaces. This function returns the string with any leading
  whitespace characters removed.
---

# LTRIM

## Syntax

```sql
LTRIM(str)
```

## Description

Returns the string `str` with leading space characters removed.

Returns `NULL` if given a `NULL` argument. If the result is empty, returns either an empty string, or with [SQL\_MODE=Oracle](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), `NULL`.

The Oracle mode version of the function can be accessed outside of Oracle mode by using `LTRIM_ORACLE` as the function name.

## Examples

```sql
SELECT QUOTE(LTRIM('   MariaDB   '));
+-------------------------------+
| QUOTE(LTRIM('   MariaDB   ')) |
+-------------------------------+
| 'MariaDB   '                  |
+-------------------------------+
```

Oracle mode version:

```sql
SELECT LTRIM(''),LTRIM_ORACLE('');
+-----------+------------------+
| LTRIM('') | LTRIM_ORACLE('') |
+-----------+------------------+
|           | NULL             |
+-----------+------------------+
```

## See Also

* [RTRIM](rtrim.md) - trailing spaces removed
* [TRIM](trim.md) - removes all given prefixes or suffixes

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
