---
description: >-
  Returns the length of a linear geometry. Calculates the total length of a
  LineString or MultiLineString in its associated spatial reference units.
---

# ST\_LENGTH

## Syntax

```sql
ST_LENGTH(ls)
```

## Description

Returns as a double-precision number the length of the [LineString](../geometry-constructors/linestring.md) value _`ls`_ in its associated spatial reference.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT ST_LENGTH(ST_GeomFromText(@ls));
+---------------------------------+
| ST_LENGTH(ST_GeomFromText(@ls)) |
+---------------------------------+
|                2.82842712474619 |
+---------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
