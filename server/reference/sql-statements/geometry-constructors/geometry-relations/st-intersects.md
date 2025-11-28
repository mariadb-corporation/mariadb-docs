---
description: >-
  Checks if two geometries intersect. Returns 1 if the geometries share any
  portion of space (interior or boundary), 0 otherwise.
---

# ST\_INTERSECTS

## Syntax

```sql
ST_INTERSECTS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether geometry _`g1`_ spatially intersects geometry _`g2`_.

`ST_INTERSECTS()` uses object shapes, while [INTERSECTS()](intersects.md), based on the original MySQL implementation, uses object bounding rectangles.

`ST_INTERSECTS()` tests the opposite relationship to [ST\_DISJOINT()](st_disjoint.md).

## Examples

```sql
SET @g1 = ST_GEOMFROMTEXT('POINT(0 0)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(0 0, 0 2)');

SELECT ST_INTERSECTS(@g1,@g2);
+------------------------+
| ST_INTERSECTS(@g1,@g2) |
+------------------------+
|                      1 |
+------------------------+
```

```sql
SET @g2 = ST_GEOMFROMTEXT('LINESTRING(2 0, 0 2)');

SELECT ST_INTERSECTS(@g1,@g2);
+------------------------+
| ST_INTERSECTS(@g1,@g2) |
+------------------------+
|                      0 |
+------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
