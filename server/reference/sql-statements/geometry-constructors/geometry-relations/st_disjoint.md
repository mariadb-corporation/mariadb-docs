---
description: >-
  Checks if two geometries are disjoint. Returns 1 if the geometries share no
  points, 0 otherwise.
---

# ST\_DISJOINT

## Syntax

```sql
ST_DISJOINT(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether geometry _`g1`_ is spatially disjoint from (does not intersect with) geometry _`g2`_.

`ST_DISJOINT()` uses object shapes, while [DISJOINT()](disjoint.md), based on the original MySQL implementation, uses object bounding rectangles.

`ST_DISJOINT()` tests the opposite relationship to [ST\_INTERSECTS()](st-intersects.md).

## Examples

```sql
SET @g1 = ST_GEOMFROMTEXT('POINT(0 0)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(2 0, 0 2)');

SELECT ST_DISJOINT(@g1,@g2);
+----------------------+
| ST_DISJOINT(@g1,@g2) |
+----------------------+
|                    1 |
+----------------------+

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(0 0, 0 2)');

SELECT ST_DISJOINT(@g1,@g2);
+----------------------+
| ST_DISJOINT(@g1,@g2) |
+----------------------+
|                    0 |
+----------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
