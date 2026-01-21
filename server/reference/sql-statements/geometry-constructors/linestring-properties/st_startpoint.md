---
description: >-
  Returns the start Point of a LineString. This function retrieves the initial
  coordinate in the linear geometry sequence.
---

# ST\_STARTPOINT

## Syntax

```sql
ST_StartPoint(ls)
StartPoint(ls)
```

## Description

Returns the [Point](../geometry-constructors/point.md) that is the start point of the [LineString](../geometry-constructors/linestring.md) value `ls`.

`ST_StartPoint()` and `StartPoint()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(StartPoint(GeomFromText(@ls)));
+---------------------------------------+
| AsText(StartPoint(GeomFromText(@ls))) |
+---------------------------------------+
| POINT(1 1)                            |
+---------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
