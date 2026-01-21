---
description: >-
  Convert text to vector. This function parses a JSON array string
  representation of a vector and converts it into the binary VECTOR data type.
---

# VEC\_FromText

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/pBQsCgBA6SJpi0m3pZuk/" %}

{% include "../../../.gitbook/includes/vectors-are-available-from-....md" %}

## Syntax

```sql
VEC_FromText(s)
```

## Description

`VEC_FromText` converts a text representation of the vector (json array of numbers) to a vector (little-endian IEEE float sequence of bytes, 4 bytes per float).

## Example

```sql
SELECT HEX(vec_fromtext('[1,2,3]')); 
+------------------------------+
| HEX(vec_fromtext('[1,2,3]')) |
+------------------------------+
| 0000803F0000004000004040     |
+------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
