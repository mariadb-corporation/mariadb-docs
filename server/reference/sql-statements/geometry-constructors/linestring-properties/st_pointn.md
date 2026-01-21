---
description: >-
  Returns the N-th Point in a LineString. This function retrieves a specific
  point from the sequence based on its 1-based index.
---

# ST\_POINTN

## Syntax

```sql
ST_PointN(ls,N)
PointN(ls,N)
```

## Description

Returns the N-th [Point](../geometry-constructors/point.md) in the [LineString](../geometry-constructors/linestring.md) value `ls`. Points are numbered beginning with `1`.

`ST_PointN()` and `PointN()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(PointN(GeomFromText(@ls),2));
+-------------------------------------+
| AsText(PointN(GeomFromText(@ls),2)) |
+-------------------------------------+
| POINT(2 2)                          |
+-------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
