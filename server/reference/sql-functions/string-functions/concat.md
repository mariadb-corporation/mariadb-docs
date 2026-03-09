---
description: >-
  Complete CONCAT reference for MariaDB. Complete function guide with syntax,
  parameters, return values, and usage examples with comprehensive examples and.
---

# CONCAT

## Syntax

```sql
CONCAT(str1,str2,...)
```

## Description

Returns the string that results from concatenating the arguments. May have one or more arguments. If all arguments are non-binary strings, the result is a non-binary string. If the arguments include any binary strings, the result is a binary string. A numeric argument is converted to its equivalent binary string form; if you want to avoid that, you can use an explicit type cast, as in this example:

```sql
SELECT CONCAT(CAST(int_col AS CHAR), char_col);
```

`CONCAT()` returns `NULL` if any argument is `NULL`.

A `NULL` parameter hides all information contained in other parameters from the result. Sometimes this is not desirable; to avoid this, you can:

* Use the [CONCAT\_WS()](concat_ws.md) function with an empty separator, because that function is `NULL`-safe.
* Use [IFNULL()](../control-flow-functions/ifnull.md) to turn NULLs into empty strings.

### Oracle Mode

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), `CONCAT` ignores [null](../../data-types/null-values.md).

## Examples

```sql
SELECT CONCAT('Ma', 'ria', 'DB');
+---------------------------+
| CONCAT('Ma', 'ria', 'DB') |
+---------------------------+
| MariaDB                   |
+---------------------------+

SELECT CONCAT('Ma', 'ria', NULL, 'DB');
+---------------------------------+
| CONCAT('Ma', 'ria', NULL, 'DB') |
+---------------------------------+
| NULL                            |
+---------------------------------+

SELECT CONCAT(42.0);
+--------------+
| CONCAT(42.0) |
+--------------+
| 42.0         |
+--------------+
```

Using `IFNULL()` to handle `NULL` values:

```sql
SELECT CONCAT('The value of @v is: ', IFNULL(@v, ''));
+------------------------------------------------+
| CONCAT('The value of @v is: ', IFNULL(@v, '')) |
+------------------------------------------------+
| The value of @v is:                            |
+------------------------------------------------+
```

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle):

```
SELECT CONCAT('Ma', 'ria', NULL, 'DB');
+---------------------------------+
| CONCAT('Ma', 'ria', NULL, 'DB') |
+---------------------------------+
| MariaDB                         |
+---------------------------------+
```

## See Also

* [GROUP\_CONCAT()](../aggregate-functions/group_concat.md)
* [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
