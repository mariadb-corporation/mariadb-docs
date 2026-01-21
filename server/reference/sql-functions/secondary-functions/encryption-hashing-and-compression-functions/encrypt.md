---
description: >-
  Encrypt a string using Unix crypt(). This function encrypts a string using the
  Unix crypt() system call, typically used for password hashing.
---

# ENCRYPT

## Syntax

```sql
ENCRYPT(str[,salt])
```

## Description

Encrypts a string using the Unix crypt() system call, returning an encrypted binary string. The `salt` argument should be a string with at least two characters or the returned result will be NULL. If no salt argument is given, a random value of sufficient length is used.

It is not recommended to use ENCRYPT() with utf16, utf32 or ucs2 multi-byte character sets because the crypt() system call expects a string terminated with a zero byte.

Note that the underlying crypt() system call may have some limitations, such as ignoring all but the first eight characters.

If the [have\_crypt](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#have_crypt) system variable is set to `NO` (because the crypt() system call is not available), the ENCRYPT function will always return NULL.

## Examples

```sql
SELECT ENCRYPT('encrypt me');
+-----------------------+
| ENCRYPT('encrypt me') |
+-----------------------+
| 4I5BsEx0lqTDk         |
+-----------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
