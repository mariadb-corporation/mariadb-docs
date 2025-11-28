---
description: >-
  Convert vector to text. This function takes a binary VECTOR data type and
  returns its JSON array string representation.
---

# VEC\_ToText

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/pBQsCgBA6SJpi0m3pZuk/" %}

{% include "../../../.gitbook/includes/vectors-are-available-from-....md" %}

## Syntax

```sql
VEC_ToText(v)
```

## Description

`VEC_ToText` converts a binary vector into a json array of numbers (floats). Returns `NULL` and throws a warning [Error 4201](../../error-codes/mariadb-error-codes-4200-to-4299/e4201.md) if given an invalid vector.

## Example

```sql
SELECT VEC_ToText(x'e360d63ebe554f3fcdbc523f4522193f5236083d');
+---------------------------------------------------------+
| VEC_ToText(x'e360d63ebe554f3fcdbc523f4522193f5236083d') |
+---------------------------------------------------------+
| [0.418708,0.809902,0.823193,0.598179,0.033255]          |
+---------------------------------------------------------+
```

Invalid vector:

```sql
SELECT VEC_ToText(x'aabbcc');
+-----------------------+
| VEC_ToText(x'aabbcc') |
+-----------------------+
| NULL                  |
+-----------------------+
1 row in set, 1 warning (0.000 sec)

Warning (Code 4201): Invalid binary vector format. Must use IEEE standard float 
  representation in little-endian format. Use VEC_FromText() to generate it.
```

## See Also

* [Error 4201: Invalid binary vector format](../../error-codes/mariadb-error-codes-4200-to-4299/e4201.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
