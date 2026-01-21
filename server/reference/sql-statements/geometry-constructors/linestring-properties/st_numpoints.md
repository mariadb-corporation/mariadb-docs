---
description: >-
  Returns the count of Points in a LineString. This function calculates the
  total number of vertices defining the line.
---

# ST\_NUMPOINTS

## Syntax

```sql
ST_NumPoints(ls)
NumPoints(ls)
```

## Description

Returns the number of [Point](../geometry-constructors/point.md) objects in the [LineString](../geometry-constructors/linestring.md) value `ls`.

`ST_NumPoints()` and `NumPoints()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT NumPoints(GeomFromText(@ls));
+------------------------------+
| NumPoints(GeomFromText(@ls)) |
+------------------------------+
|                            3 |
+------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
