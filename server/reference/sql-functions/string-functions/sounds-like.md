---
description: >-
  Compare strings by sound. This operator tests if two strings have the same
  Soundex value, useful for fuzzy matching.
---

# SOUNDS LIKE

## Syntax

```sql
expr1 SOUNDS LIKE expr2
```

## Description

This is the same as [SOUNDEX](soundex.md)(expr1) = `SOUNDEX(expr2)`.

## Example

```sql
SELECT givenname, surname FROM users WHERE givenname SOUNDS LIKE "robert";
+-----------+---------+
| givenname | surname |
+-----------+---------+
| Roberto   | Castro  |
+-----------+---------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
