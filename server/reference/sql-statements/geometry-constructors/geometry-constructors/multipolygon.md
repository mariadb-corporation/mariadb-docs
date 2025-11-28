---
description: >-
  Constructs a MultiPolygon value from a list of WKB Polygon arguments. This
  function creates a geometry collection containing multiple polygons.
---

# MULTIPOLYGON

## Syntax

```sql
MultiPolygon(poly1,poly2,...)
```

## Description

Constructs a [WKB](../wkb/) MultiPolygon value from a set of WKB [Polygon](polygon.md) arguments. If any argument is not a WKB Polygon, the return value is `NULL`.

## Example

```sql
CREATE TABLE gis_multi_polygon  (g MULTIPOLYGON);
INSERT INTO gis_multi_polygon VALUES
    (MultiPolygonFromText('MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),
     ((59 18,67 18,67 13,59 13,59 18)))')),
    (MPolyFromText('MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),
        ((59 18,67 18,67 13,59 13,59 18)))')),
    (MPolyFromWKB(AsWKB(MultiPolygon(Polygon(LineString(
       Point(0, 3), Point(3, 3), Point(3, 0), Point(0, 3)))))));
```

MultiPolygon\_Example:

```sql
CREATE TABLE multipolygon_example (
  m MULTIPOLYGON
);
```

```sql
INSERT INTO multipolygon_example VALUES
  (ST_MultiPolygonFromText(
    'MULTIPOLYGON(((0 40, 0 20, 6 30, 12 20, 12 40, 0 40),
    (15 40, 15 20, 25 20, 30 25, 30 35, 25 40, 15 40)))')),
  (ST_MPolyFromText(
    'MULTIPOLYGON(((-5 45, 35 45, 35 15, -5 15, -5 45),
    (0 40, 0 20, 6 30, 12 20, 12 40, 0 40),
    (15 40, 15 20, 25 20, 30 25, 30 35, 25 40, 15 40)))')),
  (MultiPolygon(Polygon(LineString(Point(0, 0), Point(0, 1),
     Point(1, 1), Point(1, 0), Point(0, 0)))));
```

```sql
SELECT ST_AsWKT(m) FROM multipolygon_example;
```

```sql
+-------------------------------------------------------------------------------------------------------------------------------+
| ST_AsWKT(m)                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------+
| MULTIPOLYGON(((0 40,0 20,6 30,12 20,12 40,0 40),(15 40,15 20,25 20,30 25,30 35,25 40,15 40)))                                 |
| MULTIPOLYGON(((-5 45,35 45,35 15,-5 15,-5 45),(0 40,0 20,6 30,12 20,12 40,0 40),(15 40,15 20,25 20,30 25,30 35,25 40,15 40))) |
| MULTIPOLYGON(((0 0,0 1,1 1,1 0,0 0)))                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
