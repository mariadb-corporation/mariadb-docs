---
description: >-
  Constructs a Polygon value from a list of WKB LineString arguments. It defines
  a filled shape using an outer ring and optional inner rings (holes).
---

# POLYGON

## Syntax

```sql
Polygon(ls1,ls2,...)
```

## Description

Constructs a WKB Polygon value from a number of [WKB](../wkb/) [LineString](linestring.md)\
arguments. If any argument does not represent the WKB of a LinearRing (that is,\
not a closed and simple LineString) the return value is `NULL`.

Note that according to the OpenGIS standard, a POLYGON should have exactly one ExteriorRing and all other rings should lie within that ExteriorRing and thus be the InteriorRings. Practically, however, some systems, including MariaDB's, permit polygons to have several 'ExteriorRings'. In the case of there being multiple, non-overlapping exterior rings [ST\_NUMINTERIORRINGS()](../polygon-properties/st_numinteriorrings.md) will return 1.

## Examples

```sql
SET @g = ST_GEOMFROMTEXT('POLYGON((1 1,1 5,4 9,6 9,9 3,7 2,1 1))');

CREATE TABLE gis_polygon   (g POLYGON);
INSERT INTO gis_polygon VALUES
    (PolygonFromText('POLYGON((10 10,20 10,20 20,10 20,10 10))')),
    (PolyFromText('POLYGON((0 0,50 0,50 50,0 50,0 0), (10 10,20 10,20 20,10 20,10 10))')),
    (PolyFromWKB(AsWKB(Polygon(LineString(Point(0, 0), Point(30, 0), Point(30, 30), Point(0, 0))))));
```

Non-overlapping 'polygon':

```sql
SELECT ST_NumInteriorRings(ST_PolyFromText('POLYGON((0 0,10 0,10 10,0 10,0 0),
  (-1 -1,-5 -1,-5 -5,-1 -5,-1 -1))')) AS NumInteriorRings;
+------------------+
| NumInteriorRings |
+------------------+
|                1 |
+------------------+
```

Polygon\_Example:

```sql
CREATE TABLE polygon_example (
  p POLYGON
);
```

```sql
INSERT INTO polygon_example VALUES
  (ST_PolygonFromText('POLYGON((0 40, 0 20, 6 30, 12 20, 12 40, 0 40))')),
  (ST_PolyFromText('POLYGON((15 40, 15 20, 25 20, 30 25, 30 35, 25 40, 15 40))')),
  (Polygon(LineString(Point(0, 0), Point(0, 1), Point(1, 1),
  Point(1, 0), Point(0, 0))));
```

```sql
SELECT ST_AsWKT(p) FROM polygon_example;
```

```sql
+------------------------------------------------------+
| ST_AsWKT(p)                                          |
+------------------------------------------------------+
| POLYGON((0 40,0 20,6 30,12 20,12 40,0 40))           |
| POLYGON((15 40,15 20,25 20,30 25,30 35,25 40,15 40)) |
| POLYGON((0 0,0 1,1 1,1 0,0 0))                       |
+------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
