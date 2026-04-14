# Geometry Types

## Description

MariaDB provides a standard way of creating spatial columns for geometry types, for example, with [CREATE TABLE](../../sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../sql-statements/data-definition/alter/alter-table/). Spatial columns are supported for [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/), [InnoDB](../../../server-usage/storage-engines/innodb/) and [ARCHIVE](../../../server-usage/storage-engines/archive.md)\
tables. See also [SPATIAL INDEX](spatial-index.md).

The basic geometry type is `GEOMETRY`, but the type can be more specific. The following types are supported:

* [POINT](../../sql-statements/geometry-constructors/geometry-constructors/point.md)
* [LINESTRING](../../sql-statements/geometry-constructors/geometry-constructors/linestring.md)
* [POLYGON](../../sql-statements/geometry-constructors/geometry-constructors/polygon.md)
* [MULTIPOINT](../../sql-statements/geometry-constructors/geometry-constructors/multipoint.md)
* [MULTILINESTRING](../../sql-statements/geometry-constructors/geometry-constructors/multilinestring.md)
* [MULTIPOLYGON](../../sql-statements/geometry-constructors/geometry-constructors/multipolygon.md)
* [GEOMETRYCOLLECTION](../../sql-statements/geometry-constructors/geometry-constructors/geometrycollection.md)
* GEOMETRY

## Examples

**Note:** For clarity, only one type is listed per table in the examples below, but a table row can contain multiple types.

```sql
CREATE TABLE object (shapeA POLYGON, shapeB LINESTRING);
```

```sql
INSERT INTO geometry_example VALUES
  (Point(0, 0)),
  (ST_PolygonFromText('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')),
  (ST_LineFromText('LINESTRING(0 0, 1 1, 2 2)')),
  (ST_MultiLineStringFromText(
    'MULTILINESTRING((0 1, 0 2, 0 3),
    (1 0, 2 0, 3 0))')),
  (ST_MultiPointFromText('MULTIPOINT(0 0, 1 1, 0 1, 1 0)')),
  (ST_MultiPolygonFromText(
    'MULTIPOLYGON(((0 40, 0 20, 6 30, 12 20, 12 40, 0 40),
    (15 40, 15 20, 25 20, 30 25, 30 35, 25 40, 15 40)))'));
```

```sql
SELECT ST_AsWKT(g) FROM geometry_example;

+-----------------------------------------------------------------------------------------------+
| ST_AsWKT(g)                                                                                   |
+-----------------------------------------------------------------------------------------------+
| POINT(0 0)                                                                                    |
| POLYGON((0 0,0 1,1 1,1 0,0 0))                                                                |
| LINESTRING(0 0,1 1,2 2)                                                                       |
| MULTILINESTRING((0 1,0 2,0 3),(1 0,2 0,3 0))                                                  |
| MULTIPOINT(0 0,1 1,0 1,1 0)                                                                   |
| MULTIPOLYGON(((0 40,0 20,6 30,12 20,12 40,0 40),(15 40,15 20,25 20,30 25,30 35,25 40,15 40))) |
+-----------------------------------------------------------------------------------------------+
```

### [POINT](../../sql-statements/geometry-constructors/geometry-constructors/point.md)

```sql
CREATE TABLE gis_point  (g POINT);
SHOW FIELDS FROM gis_point;
INSERT INTO gis_point VALUES
    (PointFromText('POINT(10 10)')),
    (PointFromText('POINT(20 10)')),
    (PointFromText('POINT(20 20)')),
    (PointFromWKB(AsWKB(PointFromText('POINT(10 20)'))));
```

### [LINESTRING](../../sql-statements/geometry-constructors/geometry-constructors/linestring.md)
```sql
CREATE TABLE gis_line  (g LINESTRING);
SHOW FIELDS FROM gis_line;
INSERT INTO gis_line VALUES
    (LineFromText('LINESTRING(0 0,0 10,10 0)')),
    (LineStringFromText('LINESTRING(10 10,20 10,20 20,10 20,10 10)')),
    (LineStringFromWKB(AsWKB(LineString(Point(10, 10), Point(40, 10)))));
```

### [POLYGON](../../sql-statements/geometry-constructors/geometry-constructors/polygon.md)

```sql
CREATE TABLE gis_polygon   (g POLYGON);
SHOW FIELDS FROM gis_polygon;
INSERT INTO gis_polygon VALUES
    (PolygonFromText('POLYGON((10 10,20 10,20 20,10 20,10 10))')),
    (PolyFromText('POLYGON((0 0,50 0,50 50,0 50,0 0), (10 10,20 10,20 20,10 20,10 10))')),
    (PolyFromWKB(AsWKB(Polygon(LineString(Point(0, 0), Point(30, 0), Point(30, 30), Point(0, 0))))));
```

### [MULTIPOINT](../../sql-statements/geometry-constructors/geometry-constructors/multipoint.md)

```sql
CREATE TABLE gis_multi_point (g MULTIPOINT);
SHOW FIELDS FROM gis_multi_point;
INSERT INTO gis_multi_point VALUES
    (MultiPointFromText('MULTIPOINT(0 0,10 10,10 20,20 20)')),
    (MPointFromText('MULTIPOINT(1 1,11 11,11 21,21 21)')),
    (MPointFromWKB(AsWKB(MultiPoint(Point(3, 6), Point(4, 10)))));
```

### [MULTILINESTRING](../../sql-statements/geometry-constructors/geometry-constructors/multilinestring.md)

```sql
CREATE TABLE gis_multi_line (g MULTILINESTRING);
SHOW FIELDS FROM gis_multi_line;
INSERT INTO gis_multi_line VALUES
    (MultiLineStringFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))')),
    (MLineFromText('MULTILINESTRING((10 48,10 21,10 0))')),
    (MLineFromWKB(AsWKB(MultiLineString(LineString(Point(1, 2), Point(3, 5)), LineString(Point(2, 5), Point(5, 8), Point(21, 7))))));
```

### [MULTIPOLYGON](../../sql-statements/geometry-constructors/geometry-constructors/multipolygon.md)

```sql
CREATE TABLE gis_multi_polygon  (g MULTIPOLYGON);
SHOW FIELDS FROM gis_multi_polygon;
INSERT INTO gis_multi_polygon VALUES
    (MultiPolygonFromText('MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),((59 18,67 18,67 13,59 13,59 18)))')),
    (MPolyFromText('MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),((59 18,67 18,67 13,59 13,59 18)))')),
    (MPolyFromWKB(AsWKB(MultiPolygon(Polygon(LineString(Point(0, 3), Point(3, 3), Point(3, 0), Point(0, 3)))))));
```

### [GEOMETRYCOLLECTION](../../sql-statements/geometry-constructors/geometry-constructors/geometrycollection.md)

```sql
CREATE TABLE gis_geometrycollection  (g GEOMETRYCOLLECTION);
SHOW FIELDS FROM gis_geometrycollection;
INSERT INTO gis_geometrycollection VALUES
    (GeomCollFromText('GEOMETRYCOLLECTION(POINT(0 0), LINESTRING(0 0,10 10))')),
    (GeometryFromWKB(AsWKB(GeometryCollection(Point(44, 6), LineString(Point(3, 6), Point(7, 9)))))),
    (GeomFromText('GeometryCollection()')),
    (GeomFromText('GeometryCollection EMPTY'));
```

### [GEOMETRY](geometry-types.md)

```sql
CREATE TABLE gis_geometry (g GEOMETRY);
SHOW FIELDS FROM gis_geometry;
INSERT INTO gis_geometry SELECT * FROM gis_point;
INSERT INTO gis_geometry SELECT * FROM gis_line;
INSERT INTO gis_geometry SELECT * FROM gis_polygon;
INSERT INTO gis_geometry SELECT * FROM gis_multi_point;
INSERT INTO gis_geometry SELECT * FROM gis_multi_line;
INSERT INTO gis_geometry SELECT * FROM gis_multi_polygon;
INSERT INTO gis_geometry SELECT * FROM gis_geometrycollection;
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
