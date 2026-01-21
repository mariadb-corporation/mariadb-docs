---
description: >-
  Returns the number of geometries in a GeometryCollection. Returns NULL if the
  argument is not a GeometryCollection.
---

# ST\_NUMGEOMETRIES

## Syntax

```sql
ST_NumGeometries(gc)
NumGeometries(gc)
```

## Description

Returns the number of geometries in the GeometryCollection `gc`.

`ST_NumGeometries()` and `NumGeometries()` are synonyms.

## Example

```sql
SET @gc = 'GeometryCollection(Point(1 1),LineString(2 2, 3 3))';

SELECT NUMGEOMETRIES(GeomFromText(@gc));
+----------------------------------+
| NUMGEOMETRIES(GeomFromText(@gc)) |
+----------------------------------+
|                                2 |
+----------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
