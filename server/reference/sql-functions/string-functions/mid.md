---
description: >-
  Synonym for SUBSTRING(). Returns a substring starting at a specified position
  for a given length.
---

# MID

## Syntax

```sql
MID(str,pos,len)
```

## Description

MID(str,pos,len) is a synonym for [SUBSTRING(str,pos,len)](substring.md)!

## Examples

```sql
SELECT MID('abcd',4,1);
+-----------------+
| MID('abcd',4,1) |
+-----------------+
| d               |
+-----------------+

SELECT MID('abcd',2,2);
+-----------------+
| MID('abcd',2,2) |
+-----------------+
| bc              |
+-----------------+
```

A negative starting position:

```sql
SELECT MID('abcd',-2,4);
+------------------+
| MID('abcd',-2,4) |
+------------------+
| cd               |
+------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
