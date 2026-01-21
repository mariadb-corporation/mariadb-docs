---
description: >-
  Decrypt a string. This function decrypts an encrypted string using a password.
  It is the reverse of the ENCODE function.
---

# DECODE

## Syntax

```sql
DECODE(crypt_str,pass_str)
```

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle):

```sql
DECODE(expr, search_expr, result_expr [, search_expr2, result_expr2 ...] [default_expr])
```

In all modes:

```sql
DECODE_ORACLE(expr, search_expr, result_expr [, search_expr2, result_expr2 ...] [default_expr])
```

## Description

In the default mode, `DECODE` decrypts the encrypted string <kbd>_crypt\_str_</kbd> using <kbd>_pass\_str_</kbd> as the password. _crypt\_str_ should be a string returned from [ENCODE()](encode.md). The resulting string will be the original string only if <kbd>_pass\_str_</kbd> is the same.

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), `DECODE` compares <kbd>_expr_</kbd> to the search expressions, in order. If it finds a match, the corresponding result expression is returned. If no matches are found, the default expression is returned, or `NULL` if no default is provided.

`NULL` values are treated as equivalent.

`DECODE_ORACLE` is a synonym for the Oracle-mode version of the function, and is available in all modes.

## Examples

```sql
SELECT DECODE_ORACLE(2+1,3*1,'found1',3*2,'found2','default');
+--------------------------------------------------------+
| DECODE_ORACLE(2+1,3*1,'found1',3*2,'found2','default') |
+--------------------------------------------------------+
| found1                                                 |
+--------------------------------------------------------+

SELECT DECODE_ORACLE(2+4,3*1,'found1',3*2,'found2','default');
+--------------------------------------------------------+
| DECODE_ORACLE(2+4,3*1,'found1',3*2,'found2','default') |
+--------------------------------------------------------+
| found2                                                 |
+--------------------------------------------------------+

SELECT DECODE_ORACLE(2+2,3*1,'found1',3*2,'found2','default');
+--------------------------------------------------------+
| DECODE_ORACLE(2+2,3*1,'found1',3*2,'found2','default') |
+--------------------------------------------------------+
| default                                                |
+--------------------------------------------------------+
```

`NULL` values are treated as equivalent:

```sql
SELECT DECODE_ORACLE(NULL,NULL,'Nulls are equivalent','Nulls are not equivalent');
+----------------------------------------------------------------------------+
| DECODE_ORACLE(NULL,NULL,'Nulls are equivalent','Nulls are not equivalent') |
+----------------------------------------------------------------------------+
| Nulls are equivalent                                                       |
+----------------------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
