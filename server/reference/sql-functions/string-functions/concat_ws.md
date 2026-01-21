---
description: >-
  Concatenate with separator. This function joins strings with a specified
  separator. It skips NULL values during concatenation.
---

# CONCAT\_WS

## Syntax

```sql
CONCAT_WS(separator,str1,str2,...)
```

## Description

`CONCAT_WS()` stands for Concatenate With Separator and is a special form of [CONCAT()](concat.md). The first argument is the separator for the rest of the arguments. The separator is added between the strings to be concatenated. The separator can be a string, as can the rest of the arguments.

If the separator is `NULL`, the result is `NULL`; all other `NULL` values are skipped. This makes `CONCAT_WS()` suitable when you want to concatenate some values and avoid losing all information if one of them is `NULL`.

## Examples

```sql
SELECT CONCAT_WS(',','First name','Second name','Last Name');
+-------------------------------------------------------+
| CONCAT_WS(',','First name','Second name','Last Name') |
+-------------------------------------------------------+
| First name,Second name,Last Name                      |
+-------------------------------------------------------+

SELECT CONCAT_WS('-','Floor',NULL,'Room');
+------------------------------------+
| CONCAT_WS('-','Floor',NULL,'Room') |
+------------------------------------+
| Floor-Room                         |
+------------------------------------+
```

In some cases, remember to include a space in the separator string:

```sql
SET @a = 'gnu', @b = 'penguin', @c = 'sea lion';
Query OK, 0 rows affected (0.00 sec)

SELECT CONCAT_WS(', ', @a, @b, @c);
+-----------------------------+
| CONCAT_WS(', ', @a, @b, @c) |
+-----------------------------+
| gnu, penguin, sea lion      |
+-----------------------------+
```

Using `CONCAT_WS()` to handle `NULL`s:

```sql
SET @a = 'a', @b = NULL, @c = 'c';

SELECT CONCAT_WS('', @a, @b, @c);
+---------------------------+
| CONCAT_WS('', @a, @b, @c) |
+---------------------------+
| ac                        |
+---------------------------+
```

## See Also

* [GROUP\_CONCAT()](../aggregate-functions/group_concat.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
