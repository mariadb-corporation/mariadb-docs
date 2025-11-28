---
description: >-
  Synonym for ST_CROSSES. Checks if two geometries cross, meaning they share
  some interior points but not all, and the intersection has a lower dimension.
---

# CROSSES

## Syntax

```sql
Crosses(g1,g2)
```

## Description

Returns `1` if `g1` spatially crosses `g2`. Returns `NULL` if `g1` is a [Polygon](../geometry-constructors/polygon.md) or a [MultiPolygon](../geometry-constructors/multipolygon.md), or if `g2` is a [Point](../geometry-constructors/point.md) or a [MultiPoint](../geometry-constructors/multipoint.md). Otherwise, returns `0`.

The term spatially crosses denotes a spatial relation between two given geometries that has the following properties:

* The two geometries intersect.
* Their intersection results in a geometry that has a dimension that is one less than the maximum dimension of the two given geometries.
* Their intersection is not equal to either of the two given geometries.

`CROSSES()` is based on the original MySQL implementation, and uses object bounding rectangles, while [ST\_CROSSES()](st-crosses.md) uses object shapes.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
