---
description: >-
  Checks if two geometries cross. Returns 1 if they intersect but one does not
  cover the other, and the intersection dimension is less than the maximum
  dimension.
---

# ST\_CROSSES

## Syntax

```sql
ST_CROSSES(g1,g2)
```

## Description

Returns `1` if geometry _`g1`_ spatially crosses geometry _`g2`_. Returns `NULL` if `g1` is a [Polygon](../geometry-constructors/polygon.md) or a [MultiPolygon](../geometry-constructors/multipolygon.md), or if `g2` is a [Point](../geometry-constructors/point.md) or a [MultiPoint](../geometry-constructors/multipoint.md). Otherwise, returns `0`.

The term spatially crosses denotes a spatial relation between two given geometries that has the following properties:

* The two geometries intersect.
* Their intersection results in a geometry that has a dimension that is one less than the maximum dimension of the two given geometries.
* Their intersection is not equal to either of the two given geometries.

`ST_CROSSES()` uses object shapes, while [CROSSES()](crosses.md), based on the original MySQL implementation, uses object bounding rectangles.

## Examples

```sql
SET @g1 = ST_GEOMFROMTEXT('LINESTRING(174 149, 176 151)');

SET @g2 = ST_GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SELECT ST_CROSSES(@g1,@g2);
+---------------------+
| ST_CROSSES(@g1,@g2) |
+---------------------+
|                   1 |
+---------------------+

SET @g1 = ST_GEOMFROMTEXT('LINESTRING(176 149, 176 151)');

SELECT ST_CROSSES(@g1,@g2);
+---------------------+
| ST_CROSSES(@g1,@g2) |
+---------------------+
|                   0 |
+---------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
